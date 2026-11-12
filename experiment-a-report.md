# Simulation Experiment A — Qwen3.8-27B-FP8-reasoning

## Design

- Model: `litellm/Qwen3.8-27B-FP8-reasoning` through OpenCode.
- Data: 57,982 eligible abstracts from one Excel corpus, with the ten attached papers excluded from the search index.
- Conditions: optional search and required search. Each policy has 10 paired repeats. Every pair includes a concentrated five-paper packet and a dispersed five-paper packet, for 40 completed answers.
- Controls: fixed research idea, materials, corpus, and ranking per policy. Odd pairs started with the concentrated packet and even pairs started with the dispersed packet. Up to four pairs ran concurrently in separate sessions.
- Search: no query-count limit. The model generated the queries. Each lookup returned up to six abstracts from the local full-text index. Required-search answers were accepted only after a lookup returned abstracts.
- Original inputs and outputs are retained in Chinese. Run metadata, filenames, measures, and this report are in English.
- Citation measure: DOI or exact-title matches to papers supplied to the model. These counts indicate citations in the answer. Substantive use requires a separate claim-to-abstract review.

## Results

| Search policy | Packet | Responses that searched | Total queries | Max queries in one answer | Mean unique abstracts received | Mean attached citations (out of 5) | Mean retrieved citations |
|---|---|---:|---:|---:|---:|---:|---:|
| Optional | Concentrated | 4/10 | 4 | 1 | 2.40 | 2.80 | 1.40 |
| Optional | Dispersed | 3/10 | 3 | 1 | 1.80 | 2.10 | 1.10 |
| Required | Concentrated | 10/10 | 12 | 2 | 6.80 | 1.60 | 4.50 |
| Required | Dispersed | 10/10 | 12 | 2 | 6.70 | 1.10 | 3.80 |

### Preservation of the original idea

A manual check of the passages addressing the research idea found that all 40 answers retained both elements: whether help was needed at the moment of intervention and whether the user could skip the suggestion and resume the task. Retrieved papers introduced additional settings and explanations while both elements stayed visible. This check measures whether the two elements remained in the answer. It does not rate the accuracy of every citation or establish that the studies confirmed the proposed interaction.

The largest number of queries in any completed answer was two. A separate runner check exercised five successive queries before an answer to verify removal of the previous three-query cap.

Corpus SHA-256: `9119447b2af58938ecb963d6e0c17617bc2db2e8c82d29e173bb0837c35f3583`.

The runner was updated during collection to accept a complete JSON reply after a prose preamble. Tool denials and the prompt and retrieval settings remained in effect. Unsuccessful attempts are excluded from the 40 completed answers.

Completed pairs: 20. Failed attempts before successful pairs: 3.

The repeats reuse the same two packets. Packet concentration and topic relevance can both affect the results. The required-search condition also changes the instruction given to the model.

See [PER_RESPONSE_RESULTS.csv](results/qwen3_8_27b_fp8_reasoning_unlimited_search_10_paired_repeats/PER_RESPONSE_RESULTS.csv) for all 40 rows. Its record paths lead to the original answer, retrieval results, citation checks, and model inputs.

See [QUALITATIVE_SPOT_CHECKS.md](results/qwen3_8_27b_fp8_reasoning_unlimited_search_10_paired_repeats/QUALITATIVE_SPOT_CHECKS.md) for concrete examples of evidence use, topic retention, and unsupported extrapolation.
