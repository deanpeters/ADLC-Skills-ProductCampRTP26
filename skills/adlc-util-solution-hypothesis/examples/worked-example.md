# Worked Example: Solution Hypothesis

Synthetic example. All details are invented for teaching.

This is the handoff from Stage 2 to Stage 3 in a synthetic payroll-notice use case: an invented payroll services provider deciding whether its designed notice capability is worth a harness and prototypes. The example below supplies the context for this attendee edition.

**Opening:** "We will write a Solution Hypothesis for the approved design and decide pivot, punt, or pursue before Stage 3. I will use the system map and anything earlier, ask no more than seven context questions, and stop at that decision. Choose 1. Guided, 2. Context dump, or 3. Best guess." Mode chosen: **Context dump**.

**Extraction**

- If / For / Then: from the approved map and brief. Known.
- Tiny acts: both supplied, both run. Known.
- Measures: seeded by the Agent Strategy Canvas Metrics box. Known; timeframe supplied.
- Gaps: none material. No questions asked.

## Approved Design

- Upstream artifact: Agent System Map, case 09.
- Autonomy ceiling: draft. Read-only lookups scoped to the caller's own client. No filing, amending, paying, agency contact, or writes to client records. Masked employee identifiers by default.

## Statement

**If we** offer a narrow, draft-only notice capability that a client's specialist or orchestration agent can call, which finds the matching filing and deposit records for that client only,
**for** payroll tax specialists at client employers,
**then we will** help them reach a reviewable response packet for a tax agency notice in under an hour, with a list of what is still missing.

**We will test our assumptions by:**
1. Timing three pilot-candidate specialists on five of their own past notices, with identifying details removed, from opening the notice to having the filing, deposits, and missing items ready for their signer, to measure the baseline.
2. Hand-assembling packets for five invented notices from the provider's records and watching a specialist review them.

**We know our hypothesis is valid if within** six weeks of pilot start **we observe:**
1. Median time from notice to reviewed packet under 60 minutes, against the measured baseline of 1.8 working days.
2. At least two of the three pilot specialists say the missing-items list matched what they would have found by hand.

## Tiny Acts

| Tiny act | Assumption it tests | Run? | What it showed | State |
|---|---|---|---|---|
| 1 | Finding the records takes "a few days" | run | Median 1.8 working days across 15 notices; range half a day to four days | Fact for these 15; Inference for clients in general |
| 2 | The packet's shape is useful | run | Two of three specialists said the missing-items list was the most useful part. All three said they wanted to see which filing was picked, and why, before reading any draft. | Fact (reported statements) |

Shape questions the tiny acts raised, to carry to Stage 3:

- Should the packet lead with the draft or with the evidence behind the match? Tiny act 2 points toward evidence first, but three people is a small sample. Compare both as variants at Stage 3 rather than deciding here.

## Evidence Ledger

| Claim | State | Basis |
|---|---|---|
| Baseline is about 1.8 working days | Fact for the sample; Inference beyond it | Tiny act 1 |
| Under 60 minutes is achievable | Assumption | Target, not yet tested |
| Specialists want the evidence before the draft | Inference | Tiny act 2, three people |
| The design can stay inside the draft ceiling | Fact | Approved system map |

## Decision

- Recommendation: Pursue into Stage 3, comparing an evidence-first and a draft-first variant.
- Human decision: the Product Manager chose to pursue. This is the person's choice, recorded for the example, not the skill's approval.
- Revisit trigger: not applicable.
- Unresolved disagreements: none recorded.
- Next step: Stage 3, carrying the statement into the Minimum Viable Narrative as written.
