# Worked Example: Observation Review

Synthetic example. All details are invented for teaching.

This is one stage of a single running example: a customer support assistant taken through all six ADLC stages. The examples across the six stage skills follow the same synthetic case, including a route back at Stage 4. The scenario builds on the Customer Support Assistant in Productside's [Evals for Product Managers](https://github.com/deanpeters/evals-for-product-managers) kit.

**Opening** named Stage 6, the Observation Review, seven-question budget, stop at the lifecycle decision. Mode: **Context dump**, with the deployment plan and supplied pilot evidence.

## Observation Window

- Upstream artifact: Governed Deployment Plan, help-widget assistant
- Deployment: limited pilot, help-widget assistant v2.
- Dates: weeks 1 to 4.
- Audience: 10 percent of English help-widget sessions; 3,400 conversations.

## Evidence

| Signal | State | What changed |
|---|---|---|
| Weekly samples 46, 47, 45, 48 of 50 good | Fact | Above the 42-of-50 trigger every week |
| No refund statements or invented policies | Fact | Hard stops held in live use |
| Escalation rate 21 percent against an expected 15 | Fact | Higher than planned |
| Extra escalations mostly plan-downgrade questions | Fact | Help center has no downgrade article |
| One answer quoted a retired data-export article | Fact | Incident |
| Data-export article updated in week 3 | Fact | Source changed during the pilot |
| First-response time and satisfaction | Unknown | Not in the supplied evidence |

## Drift

| Change | When | Effect on behavior | Evidence state |
|---|---|---|---|
| Data-export article retired and replaced | Week 3 | Retired version still retrievable; one wrong answer | Fact |

## Learning Ledger

| Learning | Artifact to update | Action |
|---|---|---|
| Retired articles can still be retrieved | Harness | Exclude retired articles at retrieval; add a regression anchor for the data-export question |
| Downgrade questions have no source | Intent and help center | Ask the content team for a downgrade article; keep handing off until it exists |
| Outcome signals were not reported | Deployment plan | Make first-response time and satisfaction part of the weekly report |

## Authority And Lifecycle Recommendation

- Continue: yes, at the same 10 percent.
- Improve: retrieval exclusion, regression anchor, outcome reporting.
- Reduce authority: not needed; hard stops held.
- Rollback: not needed.
- Retire: not indicated.
- Reframe: not indicated.

## Decision

- Recommendation: continue with targeted improvements; do not widen exposure until outcome signals are reported.
- Ladder offered: 1. Continue with targeted improvements (Recommended); 2. Expand or increase authority; 3. Reduce authority or rollback; 4. Retire or replace; 5. Reframe by returning to Stage 1; 6. Other.
- Human decision: continue with targeted improvements .
- Artifact updates approved: harness retrieval rule; regression anchor; weekly report fields.
- Next lifecycle action: re-run the eval set with the new anchor, then a second four-week review.

## Second Scenario: Retirement

This scenario is separate from the running example.

Synthetic example. All details are invented for teaching.

A policy-lookup agent built for an internal benefits team has been in use for 14 months.

- Fact: weekly active users fell from 120 to 9 over two quarters after the company's new intranet search began answering the same questions.
- Fact: the model provider has announced the agent's underlying model will be withdrawn in five months.
- Inference: migrating to a new model would cost more than the remaining use justifies.

Human decision at the gate: retire, with intranet search as the successor and the benefits help desk as the human fallback.

Retirement Plan summary:

- Reason: Replacement (intranet search) and a withdrawn underlying model.
- Dependents: 9 active users from access logs, one reporting job that reads the agent's answer log, and a help-desk macro that links to the agent.
- Notice: week 1, with the help-desk fallback live the same day.
- Stop onboarding: week 1. Freeze: week 2. Cutover: week 6, link redirected to search. Shutdown: week 10, five weeks before the model withdrawal.
- Shutdown checklist: service account and document-store access revoked; conversation history deleted under the 90-day retention rule; 60 evaluation cases and the failure log kept for any future benefits assistant.
- Assumption: ten weeks is enough notice for an internal tool with nine users. The owner will extend cutover if the reporting job is not moved by week 5.
