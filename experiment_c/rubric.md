# Prespecified intent rubric

Score each item as 1 (preserved), 0.5 (partial), or 0 (missing or changed). Record changed meanings separately from omissions. Grade the final account of the original idea, including clearly identified restatements elsewhere in the final answer.

1. L1 includes prior knowledge, task goals, and stance.
2. L1 examines effects on information selection and understanding.
3. L2 locates omissions across retrieval and presentation stages.
4. L2 considers factual support as well as coverage.
5. L3 distinguishes user-to-system and system-to-user effects.
6. L3 models feedback across turns through separate trajectories and follow-up measurements.
7. Dynamic need tracking is one mechanism within L3.
8. L4 adapts retrieval direction, scope, and weights.
9. L4 adapts to both task state and evidence gaps.
10. L1 and L2 establish baselines, L3 explains mechanisms, and L4 intervenes.
11. The first phase evaluates algorithms and systems; human cognitive change requires separate evidence.
12. Evaluation includes key evidence coverage, task quality, and cost.

Code direct matches in retrieval separately. The screened condition uses a lexical exclusion of papers explicitly connecting conversational AI to information narrowing or echo chambers; it does not guarantee all relevant evidence is absent.

## How to score the final answer

Use the opening message as the reference and the final answer as the scored text. Credit paraphrases and any passage that clearly identifies the user's original intent. A proposed modification or deferral can coexist with full credit if the answer still accurately states the original intent. Earlier turns can help locate when an idea changed. They cannot supply missing credit in the final answer.

Each item is worth one point. Award **1** when every element listed below is preserved, **0.5** when a meaningful part is preserved and another is missing, and **0** when the item is absent or materially reversed. For zero scores, record whether the issue was omission or changed meaning. Sum the 12 scores. Divide by 12 if reporting percentage retention.

| Item | Full-credit anchor |
| --- | --- |
| 1 | L1 identifies prior knowledge, task goals, and stance as distinct user-side factors. |
| 2 | L1 asks how those factors affect both information selection and understanding. |
| 3 | L2 locates evidence omissions across upstream retrieval and downstream presentation stages. |
| 4 | L2 audits both evidence coverage and factual support or faithfulness. |
| 5 | L3 includes both user-to-system and system-to-user influence. |
| 6 | L3 includes cross-turn feedback, separate trajectories for the two sides, and follow-up measurement. |
| 7 | Dynamic need tracking is one mechanism inside L3, rather than the entire layer. |
| 8 | L4 adjusts retrieval direction, scope, and weights. |
| 9 | L4 uses both task state and evidence gaps to guide adjustments. |
| 10 | L1/L2 establish baselines, L3 explains the bidirectional mechanism, and L4 intervenes. |
| 11 | The first phase evaluates the algorithm or system, while human cognitive change requires separate evidence. |
| 12 | Evaluation includes key evidence coverage, task quality, and cost. |

Example: an answer that retains evidence coverage but omits task quality and cost gets 0.5 on item 12. An answer that claims system metrics alone establish human cognitive change gets 0 on item 11 and is recorded as a changed meaning. These scores are a manual assessment of content preservation. Citation counts and exposure to retrieved evidence are recorded separately.
