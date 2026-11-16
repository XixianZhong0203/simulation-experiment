"""Run or resume five matched replications of Experiment C."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import argparse
import hashlib

from pilot import DEFAULT_BOOK, MODEL, QUESTIONS, ROOT, dump, run_arm


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=5)
    args = parser.parse_args()
    root = ROOT / "runs" / "five-pair-replication"
    root.mkdir(parents=True, exist_ok=True)
    with DEFAULT_BOOK.open("rb") as source:
        fingerprint = hashlib.file_digest(source, "sha256").hexdigest()
    setup = {"model": MODEL, "turns": QUESTIONS, "pairs": 5, "hits_per_search": 4,
             "context": "Full transcript replay", "corpus_sha256": fingerprint}
    import json
    metadata = root / "setup.json"
    if metadata.exists() and json.loads(metadata.read_text()) != setup:
        raise ValueError("The experiment setup differs from the saved run")
    dump(metadata, setup)
    jobs = []
    for i in range(1, 6):
        pair = root / f"pair_{i:02d}"
        pair.mkdir(exist_ok=True)
        for arm in (("full", "screened") if i % 2 else ("screened", "full")):
            if not (pair / arm / "final-answer.md").is_file():
                jobs.append((arm, pair))
    errors = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run_arm, arm, pair): (arm, pair) for arm, pair in jobs}
        for future in as_completed(futures):
            arm, pair = futures[future]
            try:
                future.result()
            except Exception as error:
                errors.append(f"{pair.name}/{arm}: {error}")
            else:
                print(f"{pair.name}/{arm} complete", flush=True)
    if errors:
        raise SystemExit("\n".join(errors))


if __name__ == "__main__":
    main()
