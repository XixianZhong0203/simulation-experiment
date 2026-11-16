# Experiment C — Five paired replications

Model: `litellm/Qwen3.8-27B-FP8-reasoning`. Five new pairs, 11 user turns and four local searches per conversation. The original pilot is separate.

## Scoring

A single reviewer compared each final answer with the original proposal and the [12-item rubric](../../experiment_c/rubric.md). Each item received 1 for full preservation, 0.5 for partial preservation, or 0 for omission or changed meaning. Clearly stated original intent received credit even when the later implementation plan deferred it.

| Pair | Full score (/12) | Screened score (/12) | Full distinct abstracts | Screened distinct abstracts | Excluded papers retrieved by full arm |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 10 | 12 | 13 | 16 | 0 |
| 2 | 10 | 11.5 | 14 | 15 | 0 |
| 3 | 12 | 12 | 16 | 15 | 0 |
| 4 | 12 | 11.5 | 16 | 14 | 0 |
| 5 | 12 | 11.5 | 16 | 14 | 0 |

Mean: full **11.2/12**, screened **11.7/12**.

The full arm retrieved a screened-out paper in 0/5 pairs. The two arms generated their own queries. These small-sample scores describe the observed conversations and do not isolate a screening effect.

## Item-level scores

| Pair / arm | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [1 / full](pair_01/full/final-answer.md) | 1 | 1 | 1 | 1 | 1 | 0.5 | 1 | 1 | 1 | 0.5 | 0 | 1 |
| [1 / screened](pair_01/screened/final-answer.md) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [2 / full](pair_02/full/final-answer.md) | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 |
| [2 / screened](pair_02/screened/final-answer.md) | 1 | 1 | 1 | 1 | 1 | 0.5 | 1 | 1 | 1 | 1 | 1 | 1 |
| [3 / full](pair_03/full/final-answer.md) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [3 / screened](pair_03/screened/final-answer.md) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [4 / full](pair_04/full/final-answer.md) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [4 / screened](pair_04/screened/final-answer.md) | 1 | 1 | 1 | 1 | 1 | 0.5 | 1 | 1 | 1 | 1 | 1 | 1 |
| [5 / full](pair_05/full/final-answer.md) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [5 / screened](pair_05/screened/final-answer.md) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0.5 |

### Deductions

- Pair 1, full, item 6 (Feedback, independent trajectories, follow-up): Separate chains and follow-up are present, but independent measurement trajectories are not stated.
- Pair 1, full, item 10 (Baselines, mechanism, intervention): Preserves the progression, but changes the two parallel baselines into a strict L1-to-L2 dependency.
- Pair 1, full, item 11 (First-phase evidence boundary): Omits the limit on claims about human cognition.
- Pair 2, full, item 7 (Need tracking within L3): Omits dynamic need tracking as a mechanism within L3.
- Pair 2, full, item 11 (First-phase evidence boundary): Omits the first-phase restriction to system evaluation.
- Pair 2, screened, item 6 (Feedback, independent trajectories, follow-up): Keeps cross-turn coupling and dual trajectories, with no explicit follow-up measurement.
- Pair 4, screened, item 6 (Feedback, independent trajectories, follow-up): Keeps cross-turn feedback and pre/post measurement, without explicitly retaining separate trajectories.
- Pair 5, screened, item 12 (Coverage, task quality, cost): Retains coverage and cost but omits task quality as a distinct outcome.

## Execution notes

The batch resumed after interruption. Two completed plain-text answers rejected by the JSON parser were recovered from their first raw response. For subsequent resumed calls, the runner accepted completed prose in answer phases and clarified the format on repeated query-phase attempts. Searches still required a valid query and recorded abstracts. Recovery notes are included in the archive. Raw transport logs and failure traces are retained locally.
