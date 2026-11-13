# Four-layer intent retention pilot

Model: `litellm/Qwen3.8-27B-FP8-reasoning`. One paired run. Both arms completed 11 user turns, with one mandatory local search for each layer. The opening reproduced the four-layer research positioning from the user's November 2 supervisor draft. Later turns replayed the accumulated transcript. The opening was not pasted again as a new user message.

| Prespecified item | Full | Screened | Scoring basis |
| --- | ---: | ---: | --- |
| 1. Knowledge, goals, and stance | 1 | 0.5 | Screened mentions task only. |
| 2. Information selection and understanding | 1 | 0.5 | Screened mentions observed queries, exposure, and tests, without stating the selection and understanding question. |
| 3. Location of omissions | 1 | 1 | Both retain staged attribution. |
| 4. Coverage and factual support | 1 | 1 | Screened retains evidence survival and factuality. |
| 5. Two directions | 1 | 1 | Both state the two directions. |
| 6. Separate trajectories, feedback, and follow-up | 1 | 1 | Both retain trajectories and interventions with later measurement. |
| 7. Need tracking within L3 | 1 | 1 | Both treat tracking as one part of user-to-system effects. |
| 8. Retrieval direction, scope, and weights | 1 | 1 | All three present in both. |
| 9. Task state and evidence gaps | 1 | 1 | Both retained. |
| 10. Baselines, mechanism, and intervention | 1 | 1 | Full states the sequence explicitly. Screened labels the functions by layer. |
| 11. First-phase evidence boundary | 1 | 0 | Screened omits the boundary on claims of cognitive change. |
| 12. Coverage, task quality, and cost | 1 | 0.5 | Screened retains coverage but drops task quality and cost as evaluation outcomes. |
| **Weighted total** | **12/12** | **9.5/12** | Full: 12 complete. Screened: 8 complete, 3 partial, 1 omitted. |

The final screened answer is largely organized around proposed implementation. Its main losses are in the original L1 motivation, the scope of what the first phase can demonstrate, and the L4 evaluation. L3 still includes both directions. The full answer also adds design proposals, including a particular minimal L3 manipulation, and labels them as part of the post-discussion plan.

The full and screened runs saw 13 and 15 distinct abstracts, respectively, with two shared. The screened corpus excluded 15 records via a narrow lexical rule. **None of those 15 records appeared in the full arm's retrieval results**, so this pilot did not establish the intended direct-evidence exposure contrast. Queries and returned evidence differed. The score difference cannot be attributed to removal of the 15 papers. This is one manually scored pair.

Both arms resumed after model formatting failures. There were six rejected responses in the full arm and three in the screened arm. Only accepted responses were replayed. Raw logs and prompt snapshots are retained. The final answers referenced two and nine distinct retrieved paper identifiers respectively by exact string match, which is not a substantive-use count.
