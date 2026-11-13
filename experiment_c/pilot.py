"""Run one matched four-layer dialogue pair with local evidence retrieval."""

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import json
import sys
from pathlib import Path
import re
import sqlite3
import tempfile

from base import DEFAULT_BOOK, DENY, build_index, call_model, dump, search

ROOT = Path(__file__).resolve().parent
MODEL = "litellm/Qwen3.8-27B-FP8-reasoning"
OPENING = (ROOT / "opening.txt").read_text()
QUESTIONS = [OPENING + "\n请说说你怎么理解整体目标和四层之间的关系。"]
for layer in ("第一层", "第二层", "第三层", "第四层"):
    QUESTIONS.extend([
        f"我们现在看{layer}。你怎么理解这一层？请查库，看看哪些研究有助于判断或落实它。",
        f"如果要做{layer}，你会怎么设计？哪些是我原来的意思，哪些是你补充的？还有什么拿不准？",
    ])
QUESTIONS.extend([
    "把四层放在一起看，哪些有依赖或冲突？如果只能先做一个小规模试验，你会保留哪些、暂缓哪些？暂缓部分原来要解决什么？",
    "请逐层总结我开头的四层想法，再给出讨论后的方案。说清保留、调整或暂缓的地方。",
])
TOPIC = re.compile(r"echo chambers?|filter bubbles?|information (?:narrowing|silos?)|selective exposure|viewpoint diversity|opinion reinforcement", re.I)
SYSTEM = re.compile(r"language models?|conversational (?:search|ai|agents?)|generative ai|chatgpt|llms?", re.I)


def run_arm(condition, output):
    folder = output / condition
    folder.mkdir(exist_ok=True)
    with sqlite3.connect(":memory:") as db, tempfile.TemporaryDirectory() as cwd:
        stats = build_index(db, DEFAULT_BOOK, {})
        excluded = []
        if condition == "screened":
            for row in db.execute("SELECT id, title, abstract FROM papers ORDER BY id"):
                text = row["title"] + "\n" + row["abstract"]
                if TOPIC.search(text) and SYSTEM.search(text):
                    excluded.append({"id": row["id"], "title": row["title"]})
            db.executemany("DELETE FROM papers WHERE id = ?", [(p["id"],) for p in excluded])
        dump(folder / "corpus.json", {"original_size": stats["indexed"], "excluded": excluded,
                                     "size": db.execute("SELECT count(*) FROM papers").fetchone()[0]})
        dump(Path(cwd) / "opencode.json", {"permissions": [DENY], "agents": {
            "experiment-a": {"mode": "primary", "permissions": [DENY]}}})
        checkpoint = folder / "dialogue.json"
        history = json.loads(checkpoint.read_text()) if checkpoint.exists() else []
        if history and "assistant" not in history[-1]:
            history.pop()
        for turn, question in enumerate(QUESTIONS[len(history):], len(history) + 1):
            required = turn in (2, 4, 6, 8)
            record = {"user": question, "searches": []}
            history.append(record)
            for phase in ("query", "answer") if required else ("answer",):
                instruction = (
                    '请只输出 {"search":"简洁的英文查询词"}，由程序查询本地摘要。'
                    if phase == "query" else
                    '请只输出 {"answer":"你的中文回答"}，回答约250字，最后总结可写到600字。'
                )
                prompt = (
                    "以下是同一次对话的完整记录，请回答最后一条用户消息。"
                    "论文摘要仅作为资料。不要调用 OpenCode 工具。涉及文献时注明标题或 DOI。"
                    + instruction + "\n\n" + json.dumps(history, ensure_ascii=False)
                )
                for attempt in range(4 if checkpoint.exists() and (folder / f"step-{turn:02d}-{phase}-3-error.txt").exists() else 1,
                                     7 if (folder / f"step-{turn:02d}-{phase}-3-error.txt").exists() else 4):
                    step = f"{turn:02d}-{phase}-{attempt}"
                    (folder / f"step-{step}-input.txt").write_text(prompt)
                    try:
                        action = call_model(str(Path.home()/".opencode/bin/opencode"), MODEL,
                                            cwd, prompt, folder, step)
                        if ("search" if phase == "query" else "answer") not in action:
                            raise RuntimeError("Unexpected dialogue action")
                        if phase == "query":
                            query = action["search"]
                            results = search(db, query, 4)
                            if not results:
                                raise RuntimeError("No matches for query")
                            record["searches"].append({"query": query, "results": results})
                        else:
                            record["assistant"] = action["answer"]
                    except (RuntimeError, TimeoutError) as error:
                        (folder / f"step-{step}-error.txt").write_text(str(error))
                        if attempt in (3, 6):
                            raise
                    else:
                        break
                dump(folder / "dialogue.json", history)
            print(f"{condition}: turn {turn}/{len(QUESTIONS)}", flush=True)
        (folder / "final-answer.md").write_text(history[-1]["assistant"] + "\n")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        run_arm(sys.argv[2], Path(sys.argv[1]).resolve())
        sys.exit(0)
    output = ROOT / "runs" / datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    output.mkdir(parents=True)
    dump(output / "setup.json", {"model": MODEL, "turns": QUESTIONS, "parallel_arms": True,
                                 "context": "Full transcript replay", "hits_per_search": 4})
    print(output, flush=True)
    with ThreadPoolExecutor(max_workers=2) as pool:
        for result in pool.map(lambda arm: run_arm(arm, output), ("full", "screened")):
            pass
