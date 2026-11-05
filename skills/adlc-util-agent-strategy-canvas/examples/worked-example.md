# Worked Example: Agent Strategy Canvas

Synthetic example. All details are invented for teaching.

This is the handoff from Stage 1 to Stage 2 in a synthetic payroll-notice use case: an invented payroll services provider scoping one narrow capability that its clients' own people and agents can call. The Product Manager has an approved Agent Intent Brief and must decide whether it deserves system design. The example below supplies the context for this attendee edition.

**Opening:** "We will run the Agent Strategy Canvas and produce a nine-box canvas with a gut-check. I will use what you already supplied, ask no more than ten context questions (one to choose a candidate, then three for each space), and stop at a pivot, punt, or pursue decision before system design. Choose 1. Guided, 2. Context dump, or 3. Best guess." Mode chosen: **Guided**.

**What the skill already had, in one line:** "From your approved brief I have the candidate, the specialist and the calling system, the trigger, draft autonomy, every blocked action, the success measures, and the stop conditions. I'll skip Q1, Q3, Q5, Q6, and Q8, and ask only what the brief left open."

## Questions Asked

| Label | Question | Answer | Used for |
|---|---|---|---|
| Problem Q2/10 | The brief names who has the problem. How often does it happen? | I don't know yet. | Customer: frequency Unknown |
| Problem Q4/10 | Under what conditions does it occur or get worse? | When there's both an original and a corrected filing for the same quarter, when the agency changes its notice layout, and when the response is due within days. That's from conversations with three clients. | Cause |
| Solution Q7/10 | What is the high-level sequence of actions? | Take in the notice, read it, find the client's matching filings and deposits, show the candidates, draft the response and the missing-items list, and hand it back for review. | Steps |
| Value Q9/10 | The brief's stop conditions cover the harms. What would show it going wrong before that? | Specialists overriding the match more often, or matching dropping after an agency changes its layout. | Monitor |
| Value Q10/10 | What does good look like at each step? | The notice comes in with its source recorded; it's recognized as in or out of scope; the right filing and period are found; when more than one filing fits, every candidate is shown with the reason; there's a draft marked draft; and a specialist has reviewed it within an hour. | Milestones |

Five numbered questions against a budget of ten, no follow-ups, no repeats. Q2 and Q9 were partly answered by the brief, so the skill said what it had and asked only for the missing part.

## The Canvas

**Agent name and description:** Notice packet assist. For a payroll tax specialist at a client employer, it prepares a draft response packet for one tax agency notice about a quarterly payroll filing.

**"Is an agent needed" screen:** a fixed workflow could look up records, but matching a free-text notice to the right filing is variable work, so an agent stays on the table (Inference).

### Problem Space

| Box | Answer | State |
|---|---|---|
| 1. Customer | A payroll tax specialist in a client's HR or finance team; at larger clients, the client's own orchestration agent submits the notice. How often notices arrive: Unknown. | Fact (who, from the brief); Unknown (how often) |
| 2. Context | A tax agency sends a notice about a quarterly payroll filing. The specialist must find the filing, the deposits, and the employee records behind it. | Fact (from the brief) |
| 3. Cause | Made worse by an original and a corrected filing for the same quarter, a changed notice layout, and a response due within days. | Assumption, from conversations with three clients |

*Space note:* "The problem space has a person, a trigger, and three conditions. Frequency is Unknown."

### Solution Space

| Box | Answer | State |
|---|---|---|
| 4. Scope | Draft. It reads the notice, finds matching filing and deposit records for that one client, and returns a summary, a draft response, and a missing-items list for a specialist to review. | Fact (from the brief) |
| 5. Safeguards | Never files or amends a return, pays, contacts the agency, writes to the client's payroll records, or looks at another client's records. Statements about what is owed and penalty relief belong to the client's signer. A notice outside coverage comes back "out of scope." | Fact (from the brief) |
| 6. Steps | Take in the notice. Read it. Find the client's matching filings and deposits. Show the candidates. Draft the response and missing-items list. Hand it back for review. | Fact (Product Manager's statement) |

**Step marking** (shown, no new question):

| Step | Done by |
|---|---|
| Take in the notice | person, or the client's own agent |
| Read it | agent |
| Find matching filings and deposits | agent |
| Show the candidates | agent |
| Draft response and missing-items list | agent |
| Review, and any release to an agency | person (specialist reviews; signer approves) |
| Out-of-scope, unmatched, or ambiguous cases | handback, with a reason |

### Value Validation

| Box | Answer | State |
|---|---|---|
| 7. Metrics | Time from notice to reviewed packet, target under an hour. Whether specialists say the missing-items list was right. Baseline "a few days," unmeasured. | Fact (measures, from the brief); Assumption (baseline) |
| 8. Monitor | Specialists overriding the match more often. Matching dropping after a layout change. | Fact (Product Manager's statement) |
| 9. Milestones | Source recorded. In or out of scope recognized. Right filing and period found. Every candidate shown with the reason when more than one fits. Draft marked draft. Reviewed within an hour. | Fact (Product Manager's statement) |

### Step To Milestone Check

| Step | Milestone | Observable by someone other than the builder? |
|---|---|---|
| Take in the notice | Source recorded | yes |
| Read it | Recognized as in or out of scope | yes |
| Find filings and deposits | Right filing and period found | yes |
| Show the candidates | Every candidate shown with the reason when more than one fits | yes |
| Draft and list | Draft marked draft | yes |
| Hand back for review | Reviewed within an hour | yes |

## Gut-Check

| Question | Result | Why |
|---|---|---|
| Is the scope governable? | yes | Every safeguard can be enforced by read-only access scoped to one client and by the absence of any filing, payment, or agency tool. None relies only on an instruction. (Inference) |
| Can success be measured without ambiguity? | yes, with one Assumption | Time and list accuracy are observable by the specialist. The baseline is an Assumption, and the way to measure it is named below, so the cross-check passes. |

Cross-checks: all pass. The Cause box is the one most likely to change, and it feeds Stage 4 edge cases.

## Evidence Ledger

| Claim | State | Basis |
|---|---|---|
| A specialist spends a few days finding the records | Assumption | Conversations with three clients; not measured |
| How often notices arrive | Unknown | Not supplied |
| Corrected filings and layout changes make it worse | Assumption | Conversations with three clients |
| The capability can be held to read-only access scoped to one client | Inference | The provider already keeps each client's records separately (supplied) |

## Decision

- Recommendation: Pursue into Stage 2.
- Human decision: the Product Manager chose to pursue. This is the person's choice, recorded for the example, not the skill's approval.
- Unresolved disagreements: none recorded.
- Cheapest test that would turn the biggest Unknown into a Fact: time five of a specialist's own past notices, with identifying details removed. Natural home: the first tiny act in the [Solution Hypothesis](../../adlc-util-solution-hypothesis/SKILL.md), after Stage 2.
- Next step: Stage 2.
