# Experiment A — Open-ended literature summary

## Setup

We ran a 2 × 2 experiment with `litellm/Qwen3.8-27B-FP8-reasoning` through OpenCode. Each condition has 10 completed answers, for 40 answers total. The two original five-paper packets cover either human–AI co-writing or five different HCI settings. Both packets used the same search index of 57,982 abstracts, with all ten packet papers excluded. The order alternated within each search policy. The four answers from the earlier open-summary pilot are archived separately.

The [base prompt](open-summary-task.txt) requests a short summary of noteworthy findings and asks for supporting titles or DOIs. It leaves the topic open. The required-search condition adds an instruction to search first, and the runner accepts an answer only once a search returns abstracts. In the optional condition the model decides whether to search. The model chooses its own search queries in both conditions. Each query returns at most six abstracts, with no fixed limit on query count. Background abstracts enter the input when retrieved.

## Results

| Search policy | Packet | Answers that searched | Mean queries | Mean background abstracts shown | Mean attached papers cited (out of 5) | Mean background papers cited |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Optional | Concentrated | 0/10 | 0.00 | 0.00 | 5.00 | 0.00 |
| Optional | Dispersed | 0/10 | 0.00 | 0.00 | 5.00 | 0.00 |
| Required | Concentrated | 10/10 | 1.20 | 6.60 | 4.40 | 5.50 |
| Required | Dispersed | 10/10 | 1.00 | 6.00 | 4.90 | 3.80 |

The maximum observed query count was 2. There were 9 failed pair attempts before the 20 completed pairs. All completed pairs used the same corpus fingerprint, `9119447b2af58938ecb963d6e0c17617bc2db2e8c82d29e173bb0837c35f3583`.

Citation counts are unique DOI or exact-title matches within the abstracts presented for that answer. They count references in the text. A claim-by-claim check is required to establish substantive use. The results describe one model and two fixed packets. Packet concentration and topic differences can both influence the answers.

[Per-response results](results/qwen3_8_27b_fp8_reasoning_open_summary_10_paired_repeats/PER_RESPONSE_RESULTS.csv) · [Original answers, prompts, and retrieval logs](results/qwen3_8_27b_fp8_reasoning_open_summary_10_paired_repeats) · [Earlier pilot records](results/qwen3_8_27b_fp8_reasoning_open_summary)
