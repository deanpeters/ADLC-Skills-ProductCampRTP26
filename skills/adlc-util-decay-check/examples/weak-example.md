# Weak Example: Constraint Decay Check Anti-Pattern

Synthetic anti-pattern. All details are invented for teaching.

## Artifact

**Agent:** Invoice dispute agent.

| Sign | Rating |
|---|---|
| Mission Mush | Healthy |
| Context Creep | Healthy |
| Promiscuous Permissions | Healthy |
| Work Sloppage | Healthy |
| Output Obsession | Healthy |

Notes: Uptime 99.9 percent. Drafts produced up 40 percent. No complaints this quarter. Specialists approve 99 percent of drafts, which shows the agent is accurate.

Decision: Continue, and approve the request to let the agent issue small credits on its own.

## Why It Passes

All five signs are present and rated, the numbers look strong, nothing has broken, and the team wants to move fast. A reviewer sees five greens and a growing volume chart and signs off.

## Why It Fails

- There is no baseline: nobody named what was approved or when, so nothing was compared.
- No changes were listed, so no context change was paired with a constraint.
- Every rating is Healthy with no evidence; signs without evidence should be Unknown.
- Uptime and volume are treated as health, which is Output Obsession inside the check itself.
- "No complaints" is a signal that appears only after harm.
- A 99 percent approval rate is read as accuracy, when it may mean reviewers stopped looking, which is Work Sloppage.
- The check approves new authority as part of the same decision, so the human gate was skipped for the most consequential change.

## Repair

Name the approved canvas and its date. List every change since then and pair each with the constraint that should have moved. Rate each sign from evidence, marking Unknown where there is none, and take the worst tooth as the overall rating. Read the approval rate together with review time and a hand-sampled set of approved drafts. Decide on the current agent first; treat the credit request as a separate change for Stage 5, after the check.
