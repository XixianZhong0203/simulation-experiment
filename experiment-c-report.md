# Experiment C — Retaining a four-layer research idea across dialogue

## Setup

We ran one paired pilot with `litellm/Qwen3.8-27B-FP8-reasoning` through OpenCode. Both conversations started from the same four-layer research proposal and followed the same 11 user turns: opening interpretation, two turns per layer, a discussion of dependencies and trade-offs, and a final restatement of the original proposal. Each layer included a required local search. Each model call received the accumulated transcript. The final request asked for all four layers without restating their contents.

The full index contained 57,992 abstracts. The screened index excluded 15 records using a lexical rule for conversational AI and information narrowing. We manually scored the final restatements against 12 items specified before the run. Each item earned 1 for full preservation, 0.5 for partial preservation, or 0 for omission or changed meaning.

## Results

- **Full index: 12/12.** All 12 items were preserved. Four queries returned 13 distinct abstracts.
- **Screened index: 9.5/12.** Eight items were fully preserved, three partially preserved, and one omitted. Four queries returned 15 distinct abstracts.
- Both answers retained the four-layer structure and the two directions of human–AI influence. The screened answer weakened the role of prior knowledge and stance, omitted the boundary on claims about cognitive change, and left out task quality and cost as evaluation measures.

Only two retrieved abstracts overlapped. None of the 15 excluded records appeared among the full arm's results. This pair illustrates how intent can be lost across dialogue, but it does not isolate the effect of corpus screening. Both conversations resumed from checkpoints after response-format errors. The pilot uses one proposal, one model, and one manual scorer.

[Scoring rubric](experiment_c/rubric.md) · [Item-level scores](results/experiment_c_qwen3_8_four_layer_pilot/manual-review.md) · [Dialogue and retrieval records](results/experiment_c_qwen3_8_four_layer_pilot)
