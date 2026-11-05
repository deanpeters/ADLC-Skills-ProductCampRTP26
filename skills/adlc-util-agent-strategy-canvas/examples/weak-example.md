# Weak Example: Agent Strategy Canvas Anti-Pattern

Synthetic anti-pattern. All details are invented for teaching.

## Artifact

**Agent name and description:** Payroll Tax Agent. An AI agent that manages our clients' payroll tax work.

| Box | Answer |
|---|---|
| 1. Customer | Our clients. |
| 2. Context | Payroll tax is complicated and time-consuming. |
| 3. Cause | Regulations change often. |
| 4. Scope | The agent handles payroll tax notices and keeps clients compliant. |
| 5. Safeguards | The agent will be careful and follow all applicable rules. |
| 6. Steps | Read the notice, figure out the answer, respond, and learn from the result. |
| 7. Metrics | Adoption, time savings, and client satisfaction. |
| 8. Monitor | Client complaints and support tickets. |
| 9. Milestones | Launch, scale, and optimize. |

Gut-check: Governable, yes. Measurable, yes.

## Why It Passes

Every box has text, the three spaces are present, and the language is plain. A reviewer short on time sees nine filled boxes and a gut-check that says yes, and the topic is clearly real.

## Why It Fails

- The candidate is an area, not a narrow piece of work: "manages our clients' payroll tax work."
- Customer is "our clients," not a person doing the work, and nobody said how often the problem occurs.
- Cause is a general fact about the world, not a condition anyone could see in a real case.
- Scope says "handles" and "keeps clients compliant" with no autonomy level, which quietly gives the agent authority over filings and responses.
- Safeguards is an instruction ("will be careful"), not a structural limit, so the agent could ignore it without anything stopping it.
- Steps ends in "respond" and "learn," with no marking of which steps a person approves and no handback.
- Metrics measure adoption and satisfaction, with no baseline and no way to tell whether the work improved.
- Monitor lists complaints and tickets, which appear only after a client has been affected.
- Milestones are phases of a project, not what good looks like at each step.
- The gut-check says yes twice with no reasons, and no cross-check was run.

## Repair

Choose one narrow candidate, such as preparing a draft response packet for one kind of notice. Name the specialist as the customer and mark frequency Unknown until measured. Write Scope at a named autonomy level, and turn Safeguards into blocked actions and read-only access. Mark each step as agent, person, or handback. Replace the metrics with time to a reviewed packet and a baseline, replace Monitor with signals that move before harm, and give every step a milestone someone else could observe. Then run the gut-check with a reason for each answer.
