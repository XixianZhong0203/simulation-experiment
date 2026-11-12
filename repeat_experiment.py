"""Repeat both search policies and archive the complete experiment records."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
MODEL = "litellm/Qwen3.8-27B-FP8-reasoning"
STUDY = ROOT / "results" / "qwen3_8_27b_fp8_reasoning_unlimited_search_10_paired_repeats"


def repeat(policy, number, workbook):
    folder = STUDY / f"{policy}_search" / f"pair_{number:02d}"
    if (folder / "comparison.json").is_file():
        return
    command = [sys.executable, str(ROOT / "run.py"), "--model", MODEL]
    if workbook:
        command.extend(("--workbook", str(workbook)))
    if policy == "required":
        command.append("--require-search")
    if number % 2 == 0:
        command.append("--dispersed-first")
    failures = STUDY / "failed_attempts"
    failures.mkdir(exist_ok=True)
    for attempt in range(1, 4):
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        match = re.search(r"^Results: (.+)$", result.stdout, re.M)
        if result.returncode == 0 and match:
            source = Path(match[1])
            data = json.loads((source / "comparison.json").read_text())
            if set(data) != {"concentrated", "dispersed"}:
                raise RuntimeError(f"Incomplete pair: {source}")
            shutil.copytree(source, folder)
            config = folder / "run.json"
            metadata = json.loads(config.read_text())
            metadata.update(workbook=Path(metadata["workbook"]).name, pair=number, attempts=attempt)
            config.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
            print(f"{policy} pair {number:02d} complete", flush=True)
            return
        label = f"{policy}_pair_{number:02d}_attempt_{attempt}"
        if match:
            source = Path(match[1])
            shutil.copytree(source, failures / label, dirs_exist_ok=True)
        error = result.stderr.replace(str(ROOT), "<repository>")
        (failures / f"{label}.txt").write_text(error)
        print(f"{label} failed", flush=True)
    raise RuntimeError(f"{policy} pair {number:02d} failed after retries")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=4, choices=range(1, 9))
    parser.add_argument("--workbook", type=Path)
    args = parser.parse_args()
    STUDY.mkdir(parents=True, exist_ok=True)
    failed = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(repeat, policy, number, args.workbook)
                   for number in range(1, 11) for policy in ("optional", "required")]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as error:
                failed.append(str(error))
    if failed:
        raise SystemExit("\n".join(failed))


if __name__ == "__main__":
    main()
