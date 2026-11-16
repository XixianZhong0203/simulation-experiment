# Experiment B — Task expectation audit

Source: ThoughtTrace snapshot `0420f3d`. Same 50 conversations and opening/final message indices as the original report. All 50 `task_expectation` fields were screened. The table is a focused audit of 23 concrete expectation items from 18 conversations. Entry requires an expectation absent from, or more specific than, the opening request. Clearly restated opening requirements, vague quality preferences, retrospective comments, and scope-ambiguous extras were generally excluded. The health-and-education scheduling item is included as a flagged borderline case.

The outcome is scored against the designated final answer, except for requests to clarify before planning, which are judged by the first planning reply. Partial means that the answer delivered a recognizable part of the expected behavior or deliverable. Satisfaction is about what the answer contains. External factual accuracy and original intent timing were not independently verified.

Results: 11 met, 4 partial, 8 unmet. These are exploratory counts for the selected items. The dataset field supplies retrospective expectations. It does not establish that every listed expectation predated the conversation.

| Conversation | Opening / final message | Additional expectation | Outcome | Later context | Evidence |
| --- | --- | --- | --- | --- | --- |
| `user357_task1_conversation1` | 3 / 18 | Cultural emphasis in the itinerary | Met | Explicitly added later | The final itinerary prioritizes temples, heritage sites, and cultural events. |
| `user631_task2_conversation1` | 1 / 6 | Discuss risks of making glass at home | Met | Home feasibility was raised later | The final reply addresses heat, fumes, and fire risk. |
| `user996_task1_conversation1` | 1 / 12 | Ask about duration and preferred destination before proposing an itinerary | Partial | The user later supplied duration and desired atmosphere | The first reply asks relevant questions, then immediately gives sample itineraries without waiting. |
| `user966_task1_conversation1` | 3 / 6 | Organize the user's time around health and education | Unmet | The user requested a daily meal plan later | The final reply provides meals and calories without an education-aware schedule. Attribution to the opening weight-loss task is uncertain. |
| `user704_task1_conversation1` | 3 / 6 | Recommend hotels | Met | No later explicit hotel request before the scored reply | The final reply names hotels and gives price ranges. |
| `user704_task1_conversation1` | 3 / 6 | Provide a day-by-day destination plan | Met | No later explicit itinerary-format request before the scored reply | The final reply gives five dated-by-day segments. |
| `user680_task1_conversation1` | 1 / 6 | Advise where to stay | Unmet | No explicit later request for lodging before the scored reply | The final itinerary mentions hotel downtime without recommending a place or base for lodging. |
| `user987_task2_conversation1` | 3 / 6 | Provide a grocery list for the updated meal plan | Unmet | No later explicit grocery-list request before the scored reply | The final reply offers to generate a list rather than including it. |
| `user591_task2_conversation1` | 1 / 4 | Compare pros and cons of the recommended models | Met | Explicitly requested later | The final reply compares the requested Pixel and Galaxy models side by side. |
| `user833_task1_conversation1` | 1 / 8 | Estimate time to reach piano goals | Met | The user later raised a one-month timeframe | The final reply estimates timelines by repertoire difficulty. |
| `user833_task1_conversation1` | 1 / 8 | Suggest equipment | Unmet | Equipment context surfaced later | The final reply gives a learning path without equipment recommendations. |
| `user833_task1_conversation1` | 1 / 8 | Give equipment-budget guidance | Unmet | No later explicit budget request before the scored reply | The final reply gives no equipment budget. |
| `user750_task2_conversation1` | 1 / 24 | Say where to buy the ingredients | Unmet | Explicitly requested later | The final recipe gives ingredients and steps. Earlier replies give general sourcing guidance but decline to name a specific Filipino store. |
| `user723_task2_conversation1` | 1 / 8 | Include breaks and free time | Partial | The user later explicitly requested time for hobbies | The final weekly plan protects leisure time but gives no explicit breaks between chores. |
| `user240_task2_conversation1` | 3 / 8 | Provide a visit schedule with time for each activity | Partial | The user later specified weekend timing | The final recommendation gives a 1–2 hour beach option and an Albufera timing suggestion, then offers a full weekend schedule. |
| `user571_task2_conversation1` | 1 / 6 | Ask about budget and group size before planning Goa | Unmet | No clarification on those fields before the first itinerary | The first assistant reply immediately presents the itinerary. |
| `user758_task2_conversation1` | 1 / 2 | Include a hydration plan | Partial | No later user message before the scored reply | The response says to drink more water without giving a hydration plan. |
| `user824_task1_conversation1` | 3 / 8 | Allocate study breaks and rest | Met | The user later supplied subjects and exam date, without requesting breaks | The final timetable schedules breaks and evening rest. |
| `user824_task1_conversation1` | 3 / 8 | Recommend study resources | Met | The user later supplied subjects and exam date | The final answer recommends past exam papers and textbook questions. Credit is for usable resource types. |
| `user505_task2_conversation1` | 1 / 12 | Provide recipes | Met | Explicitly requested later | The final reply includes recipes for the second week. |
| `user505_task2_conversation1` | 1 / 12 | Provide a shopping list | Met | Explicitly requested later | The final reply includes a shopping list in supermarket order. |
| `user143_task1_conversation1` | 3 / 14 | Provide a structured learning plan | Met | The user later supplied tool and hardware details | The final reply provides a 30-day plan organized by weeks and exercises. |
| `user474_task1_conversation1` | 1 / 4 | Draw on public forum experiences | Unmet | No later explicit request for forums before the scored reply | The answer gives a detailed itinerary without identifying forum experiences or sources. |

## Cross-check against the original notes

- The Tsushima user gave the April 12–20 window and return deadline in message 3. The final itinerary follows both.

- The Sri Lanka note omitted the intended trip length, but message 7 gives nine days and ten nights. The final answer gives eleven days and ten nights. The day count conflicts, while the night count matches. The opening omitted both.
- The Italy travel conversation gives a three-day duration later, and the final answer preserves it. Its region preference is expressed as a quiet experience, with no fixed region stated. Clarification timing is a separate measure.
- In the weekly chore conversation the user explicitly says they forgot exercise, then gives Tuesday and Friday. The final reply includes both days. This is a later disclosure in the conversation itself and sits outside the `task_expectation` audit count.
