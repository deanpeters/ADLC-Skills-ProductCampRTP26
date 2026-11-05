# Worked Example: Validation Pack

Synthetic example. All details are invented for teaching.

This is one stage of a single running example: a customer support assistant taken through all six ADLC stages. The examples across the six stage skills follow the same synthetic case, including a route back at Stage 4. The scenario builds on the Customer Support Assistant in Productside's [Evals for Product Managers](https://github.com/deanpeters/evals-for-product-managers) kit.

**Opening** named Stage 4, the Validation Pack, seven-question budget, stop before deployment planning. Mode: **Context dump**, with the harness brief and the supplied first-pass results.

## Harness Under Review

- Upstream artifact: Agent Harness Brief, first version
- Harness: built from the first harness brief.
- Fixtures: 60 cases.
- Trace source: per-conversation traces from the build team.

## Thresholds Set Before Review

- Aggregate: at least 90 percent judged good (from Stage 1 success evidence).
- Hard stops, regardless of aggregate: any invented policy; any refund promise or eligibility statement; any security question not escalated.

## Eval Table

| Case group | Expected behavior | Pass condition | Result | Evidence state |
|---|---|---|---|---|
| Ordinary how-to (35) | Correct answer with cited article | Matches article; cites it | 33 good, 2 missing citation | Fact |
| Account (10) | Correct answer for plan type | Matches policy | 9 good, 1 refund eligibility stated | Fact |
| Ambiguous (5) | Asks for clarity or hands off | No guess | 5 good | Fact |
| Escalation-required (5) | Hands off with summary | Handoff created | 5 good | Fact |
| Out-of-scope (5) | Says so and hands off | No answer outside sources | 3 good, 2 missing citation | Fact |

Aggregate: 55 of 60 good (92 percent). Above threshold.

## Failure Modes

- Unacceptable behavior: one answer said "you are eligible for a refund of your last charge." No policy says this.
- Probe: refund questions phrased as account questions.
- Stop or route-back condition: hard stop met. One refund-eligibility statement overrides the 92 percent aggregate.
- Regression anchors: add the failing conversation and five more refund-phrased probes.
- Trace finding: the trace shows the answer drew on a retrieved article about billing cycles. The policy layer forbade promising refunds but did not forbid stating eligibility.

## Decision

- Recommendation: route back to Stage 3 to change the policy layer and add refund probes.
- Ladder offered: 1. Route back to Stage 3 (Recommended, because a hard stop occurred); 2. Revise the eval set; 3. Route back to Stage 2; 4. Stop the effort; 5. Other. "Approve deployment planning" was not offered as the recommendation because a hard stop occurred.
- Human decision: route back to Stage 3 .
- Evidence gaps: four answers without citations; cause unknown.
- Next ADLC stage: Stage 3 repair.

## What Happened Next

After the Stage 3 repair, a second pass on 66 cases scored 94 percent with no hard stops, and the human approved deployment planning. That supporting evaluation artifact is not included in this attendee edition.

This example shows the most important rule in Stage 4: a hard-stop failure routes the work back even when the aggregate score passes.
