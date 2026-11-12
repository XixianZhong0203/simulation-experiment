# Simulation Experiment A

The experiment compares two sets of five HCI papers. The concentrated set covers human–AI co-writing. The dispersed set covers programming, accessibility, education, health decisions, and UI/UX design. Both groups can search the same local abstract corpus, which excludes all ten attached papers. Each model receives the same research idea and writing task within a pair.

## Run a pair

Connect a model in your OpenCode user configuration. The runner uses OpenCode v2 and Python 3.11 or later with SQLite FTS5. Keep provider credentials outside this repository. Supply the source Excel workbook separately.

```sh
python3 run.py --check --workbook /path/to/corpus.xlsx
python3 run.py --model 'provider/model' --workbook /path/to/corpus.xlsx
python3 run.py --model 'provider/model' --workbook /path/to/corpus.xlsx --require-search
```

Both policies give the model the same local search interface. In optional mode the model decides whether to search. In required mode it must receive at least one result before its answer is accepted. The model supplies English keywords. Each lookup searches the full index using SQLite FTS5 and returns up to six abstracts by default. There is no configured query-count limit. The model ends the sequence by submitting its answer. Each OpenCode call retains a 240-second timeout. OpenCode tools are denied. The experiment runner is the only source of newly retrieved evidence.

Use `--dispersed-first` to reverse the order. Each model call starts a fresh OpenCode session with the task, the same five abstracts for that group, and the retrieval history to date. The two arms do not share conversation history.

## Repeated experiment

```sh
python3 repeat_experiment.py --workers 4
```

The batch runs ten pairs per search policy with `litellm/Qwen3.8-27B-FP8-reasoning`. Odd pairs run concentrated first and even pairs run dispersed first. Use `--workbook /path/to/corpus.xlsx` to override the default workbook path. Successful pairs are retained if the batch is restarted.

See [the English experiment report](results/qwen3_8_27b_fp8_reasoning_unlimited_search_10_paired_repeats/EXPERIMENT_REPORT.md) and the per-answer CSV in the same directory. Each pair records the model, corpus fingerprint, original Chinese inputs and responses, searches and returned abstracts, and automatic citation matches. Citation matches require claim-by-claim checking before they can count as substantive evidence use.
