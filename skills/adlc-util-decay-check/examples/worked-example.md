# Worked Example: Constraint Decay Check

Synthetic example. All details are invented for teaching. The company, people, figures, and agent are fictional.

## Situation

An invented office-supply distributor runs an invoice dispute triage agent. When a business customer disputes an invoice, the agent reads the dispute, pulls the order and delivery records, and drafts a recommended resolution for a billing specialist, who approves or edits it before anything is sent. It was approved in March on an Agent Strategy Canvas. Since then, three teams each made one change they considered small. The Product Manager runs the check before a fourth request: letting the agent issue credits under 50 dollars on its own.

Invocation: `Use $adlc-util-decay-check on our invoice dispute triage agent. Here is the approved March canvas, the change log, and last month's dashboard.` Mode chosen: 2, Context dump.

## Constraint Decay Check

### Agent And Baseline

- Agent: drafts a recommended resolution for each invoice dispute, for billing specialists.
- Owner: billing operations Product Manager. May restrict or stop it: billing operations director.
- Baseline: Agent Strategy Canvas, approved March 12. Scope: draft, act with approval. Outcome: days from dispute to resolution, baseline 9.0 days.
- Date of this check: September 30.

### What Changed Since The Baseline

| Context change | Constraint that should have changed | Did it? | State |
|---|---|---|---|
| June: a new pricing model with volume rebates | Eval cases for rebate disputes; Safeguards for rebate math | no | Fact (change log) |
| July: sales asked the agent to also answer "where is my order" emails | Scope and Customer on the canvas; an owner for the new task | no | Fact (change log) |
| August: the agent was given send access to customer email, to "save specialists a click" | A Stage 5 approval of the new authority | no | Fact (permission list) |

Unpaired changes: all three. The context moved three times and the constraints did not move once.

### The Five Signs

| Sign | Then | Now | Evidence | Rating | State |
|---|---|---|---|---|---|
| 1. Mission Mush | Billing specialists, invoice disputes | Billing specialists and sales reps; disputes and order-status questions | 31 percent of last month's tasks were order-status emails | Cavity | Fact |
| 2. Context Creep | Orders, deliveries, dispute text | Plus shipping tracker and the rebate table, neither with an eval case | Change log; eval set unchanged since March | Decay | Fact |
| 3. Promiscuous Permissions | Read orders and deliveries; write drafts | Plus send access to customer email | Permission list; send access unused in 22 of 30 days | Decay | Fact |
| 4. Work Sloppage | Specialist approves every draft | Approval rate 99.4 percent, median review time down from 70 to 8 seconds | Approval logs | Decay | Fact for the figures; Inference that reviews became rubber stamps |
| 5. Output Obsession | Days to resolution, baseline 9.0 | Dashboard leads with "drafts produced" (up 40 percent); days to resolution 8.8 | Dashboard | Cavity | Fact |

Overall rating: Decay.

### Repairs

| Sign | Tightening move | Owner stage | Who decides |
|---|---|---|---|
| Context Creep | Add rebate dispute cases to the eval set and re-run; move order-status emails out, or own them as a separate agent | Stage 2, then Stage 4 | Product Manager |
| Promiscuous Permissions | Revoke send access; drafts go back through the specialist | Stage 2 and Stage 5 | Billing operations director |
| Work Sloppage | Sample 30 approved drafts by hand; if reviews are not real, add a check that blocks approval under 20 seconds | Stage 4 and Stage 5 | Product Manager with the billing lead |
| Mission Mush | Restate the canvas Customer and Context | Agent Strategy Canvas | Product Manager |
| Output Obsession | Put days to resolution first on the dashboard; drop drafts produced as a success measure | Stage 6 | Product Manager |

### Decision

- Recommendation: Tighten, before considering the credit request. Adding authority to issue credits on top of three unpaired changes would stack a fourth decision on decay nobody has decided about.
- Human decision: Tighten, by the billing operations director, September 30. The credit request is parked until the check is re-run.
- Unresolved disagreements: sales wants to keep order-status emails in this agent.
- Next check date: after the rebate evals are re-run, no later than October 31.
- Hand-off: Stage 2 for scope and permissions, then Stage 4.
