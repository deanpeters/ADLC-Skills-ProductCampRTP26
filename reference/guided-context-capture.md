# Guided Context Capture

Shared interaction contract for ADLC skills.

## Opening Contract

Every skill begins by naming:

- the ADLC stage
- the artifact it will produce
- the expected question budget or time
- the human decision where it will stop

Then offer:

1. **Guided** - Ask one question at a time with progress shown.
2. **Context dump** - Accept notes, artifacts, links, or pasted material; extract what is already answered and ask only about material gaps.
3. **Best guess** - Draft from available context; label every inferred detail and end with assumptions requiring validation.

## Context Already Supplied

Treat all of the following as answers already given:

- text included with the invocation
- attached or linked files the agent can inspect
- pasted notes or research
- approved upstream artifacts from earlier skills
- decisions recorded earlier in the conversation

Do not ask the user to repeat it.

## One-Question Turns

In Guided mode:

1. Ask one decision-relevant question per turn.
2. Explain why the answer changes the artifact when useful.
3. Offer concise numbered responses when likely answers can be anticipated.
4. Include `Other (specify)` when needed.
5. Show progress as `ADLC Context Qx/y` or a stage-specific label.

**One subject per question.** A question may name two parts of one subject, such as who does the work and who is affected. It must not combine two separate decisions, such as success evidence and a stop condition.

**Answered questions.** Before the first question, say in one line what you already have from the invocation and earlier context, and skip those questions.

**Partly answered questions.** Say what you already have and ask only for the missing part. Do not re-ask the whole question.

**Unclear answers.** When an answer would change the artifact but is too vague to use, ask one follow-up, labeled `Qx/y follow-up`. Follow-ups are not counted in the numbered budget, but a stage may use at most two. If an answer is still unclear after its follow-up, record your best reading as an Assumption and move on.

**Reuse.** When an answer also covers a later question, use it there and ask only for what is left.

**Budget.** The opening states the most numbered questions the stage will ask. Do not exceed it. Progress labels keep their fixed numbers when questions are skipped, so a label sequence with gaps is expected.

## Re-entry After A Route Back

When a later stage routes work back to this one:

1. Start from the approved artifact this stage produced before.
2. Name the route-back reason and the later artifact that raised it.
3. Change only what the reason requires, and record the changes in a short "Changes from the previous version" section.
4. Re-run the gate. A revised artifact still needs human approval.

Do not restart the stage from scratch unless the human asks.

## Saving Artifacts

Every artifact is meant to be shared. The humans at the helm use it to collaborate, decide, and document, so it should be easy to save, pass around, and pick up again.

**When to save.** If the person names a folder, at the invocation or at any point before the gate, save the artifact there as a Markdown file. If no folder is named, offer once, at the gate, to save it. Do not ask earlier, and do not ask twice.

**Save after the decision.** Write the file after the person chooses at the gate, so the decision is recorded in it. If the person stops before the gate, save a draft marked `Status: draft, no decision yet` only when asked.

**Start every saved file with a header.**

```
# <Artifact name>
- ADLC step: <stage or utility>
- Date: <date>
- Built from: <the upstream files or context it used>
- Decision: <the option chosen at the gate>
- Decided by: <the name given, or "not recorded">
- Synthetic: <yes, when the content is invented for teaching>
```

**Use fixed file names** so every run of the loop looks the same:

| Step | File |
|---|---|
| Stage 1 | `stage-1-agent-intent-brief.md` |
| Agent Strategy Canvas | `agent-strategy-canvas.md` |
| Stage 2 | `stage-2-agent-system-map.md` |
| Solution Hypothesis | `solution-hypothesis.md` |
| Stage 3 | `stage-3-agent-harness-brief.md` |
| Minimum Viable Narrative | `minimum-viable-narrative.md`, plus one `prototype-prompt-<variant>.md` per variant |
| Stage 4 | `stage-4-validation-plan.md` before results; `stage-4-validation-pack.md` with results |
| Stage 5 | `stage-5-governed-deployment-plan.md` |
| Stage 6 | `stage-6-observation-review.md`, plus `stage-6-retirement-plan.md` when retiring |

**Never overwrite silently.** If the file exists, as after a route back or a revision, save the new one with `-v2`, `-v3`, and so on, and say so.

**Reuse what is saved.** When a folder is set, read the earlier artifacts from it instead of asking the person to attach them. They count as context already supplied.

**Folder access.** Save only where the session can write. If it cannot, say so and give the artifact in the conversation for the person to save.

## Adaptive Decision Ladder

At the decision gate, present:

1. Recommended option first, labeled `(Recommended)`. The recommendation is whichever option the evidence supports, not always the approval option. When the artifact is weak, put the route-back, revise, or stop option first and mark it recommended. Each skill lists its options in a default order; reorder them when the evidence calls for it.
2. Two or three genuinely distinct alternatives.
3. One sentence explaining the tradeoff of each option.
4. `Other (specify)` when the choices are not exhaustive.

The skill stops after the gate. It does not silently invoke the next stage.
