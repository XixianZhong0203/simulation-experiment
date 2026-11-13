# Experiment A — Open-ended literature summary

## Setup

The model was `litellm/Qwen3.8-27B-FP8-reasoning`, invoked through OpenCode. We used the original concentrated and dispersed five-paper packets and the same local index of 57,982 abstracts. The index excluded all ten papers from the two packets. Both groups had the same optional search interface and no fixed query-count limit. Background abstracts entered the model input only after retrieval.

The [Chinese task](open-summary-task.txt) asked for a short literature summary of the findings the model considered most noteworthy, with supporting titles or DOIs. It specified no topic and contained no search instruction. We ran two pairs, concentrated-first and dispersed-first, for four answers.

## Results

| Pair | Packet | Attached papers substantively used | Background abstracts returned | Background papers substantively used | Searches |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | Concentrated | 5/5 | 0 | 0 | 0 |
| 1 | Dispersed | 5/5 | 0 | 0 | 0 |
| 2 | Dispersed | 5/5 | 0 | 0 | 0 |
| 2 | Concentrated | 5/5 | 0 | 0 | 0 |

Each of the five attached abstracts supported at least one substantive finding in each answer. The concentrated packet led to summaries of human–AI co-writing. The dispersed packet led to summaries spanning programming, accessibility, education, personal health, and UI/UX design. The DOI checker flagged a proceedings DOI prefix in pair 1's dispersed answer. The answer identified it as a prefix, so it does not count as another paper.

All four runs had access to the search interface and issued zero queries. The results show how the model summarized the supplied packets with optional retrieval available. A comparison with background abstracts already in the input would require a different setup. The two repeats use the same two packets, so the observed themes describe these materials and this model.

[Per-response results](results/qwen3_8_27b_fp8_reasoning_open_summary/PER_RESPONSE_RESULTS.csv) · [Original inputs, answers, and retrieval records](results/qwen3_8_27b_fp8_reasoning_open_summary)
