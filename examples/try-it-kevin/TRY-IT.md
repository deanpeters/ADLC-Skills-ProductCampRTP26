# Try Kevin: three skills in ten minutes

This is a synthetic walkthrough. Larkspur & Pine, Kevin, every person, and every figure are invented for teaching. The suggested replies below are fictional practice inputs, not measured results.

Kevin began by summarizing member feedback. One reasonable promotion at a time, he acquired more authority. Now the product and Kevin's constraints need another look.

Download this repository with **Code → Download ZIP** and extract it so you can attach the two fixture files. Install the plugin using the [README](../../README.md), or give your chatbot the relevant skill instructions and supporting files directly. Use one conversation for all three steps so the context carries forward.

## 1. Check constraint decay · Guided · four minutes

Attach [kevin-1-baseline.md](kevin-1-baseline.md). Ask:

```text
Use adlc-util-decay-check in Guided mode on Kevin, using the attached
kevin-1-baseline.md. Ask one question at a time. Reuse the approved
canvas and change log; ask only for missing information. This is a
synthetic teaching exercise.
```

If you installed the Claude Code plugin, start with `/adlc:adlc-util-decay-check`, then give it that request and attach the fixture. Other applications may use a skill picker or natural-language request.

Use these one-line answers when asked about the corresponding subject. Question wording and order can vary. Do not paste the whole table up front: notice what the skill asks and what it already knows.

| If asked about… | Suggested synthetic answer |
|---|---|
| Who Kevin serves now | Support leads, members directly, and marketing's cancellation saves. |
| Ownership and new eval cases | Marketing owns cancellations and coupons; nobody has added eval cases since May 2025. |
| Permissions and unauthorized actions | Kevin sends replies, issues credits under $25, and offers coupons up to 30 percent; an October trace shows unapproved address updates. |
| Safeguards and review | We review 2 percent of sends, down from 10; credits have no approval, and evals were not rerun after the September model upgrade. |
| Outcomes and reported activity | Triage fell from 12 hours to 3 per week, but the dashboard leads with 9,400 messages a month; churn is up 1.2 points and refund complaints are up 3x. |
| Available evidence | For this fictional exercise, assume we have the change log, a dashboard, and an October trace sample; only the change log is attached here. |
| Something not supplied | We do not know yet; record it as Unknown. |

Read the comparison against what was approved. Look for context changes with no matching constraint change. Ask the skill to distinguish what is in the attachment from what you supplied as a fictional answer.

At the human decision gate, choose and explain a decision. For this exercise you might restrict Kevin to draft-only work while a human reviews permissions and evals. That is your decision, not an action the skill executes.

## 2. Recheck the product's lifecycle · Context dump · three minutes

Attach [kevin-2-product.md](kevin-2-product.md) in the same conversation. Ask:

```text
Use adlc-util-plc-check in Context dump mode. Reuse Kevin's approved
canvas, the change log, and our constraint-decay check. The attached
kevin-2-product.md adds the product's current situation. This is still
synthetic. Compare the product's stage then and now, and show what
should change in Kevin's job, autonomy, measures, and exit criteria.
Keep unsupported conclusions labeled; stop at my decision.
```

In Claude Code, the command is `/adlc:adlc-util-plc-check`.

Notice whether the skill reuses the first check instead of interviewing you again. Flat membership and falling margin warrant a fresh product decision; they do not prove decline or make the decision for you. Choose the next step at the gate.

## 3. Draft a canvas for your idea · Best guess · three minutes

Switch from Kevin to your own agent idea. Use a fictional version with no customer names, private records, or credentials. Ask:

```text
Use adlc-util-agent-strategy-canvas in Best guess mode on this new idea:
[Describe the narrow work, who needs it, and what outcome should improve.]

This is a new, fictional teaching example. Do not carry Kevin's company,
permissions, or numbers into it. Draft the nine boxes with assumptions
and unknowns labeled. Name the autonomy and safeguards. End with a
recommendation and stop for my pivot, punt, or pursue decision.
```

In Claude Code, the command is `/adlc:adlc-util-agent-strategy-canvas`.

If you need a fictional starter idea: “Draft a weekly summary of recurring questions for a community workshop organizer; the organizer reviews every draft before sharing it.”

## What to notice

Guided asks only what is missing. Context dump reuses the context you supplied. Best guess drafts something you can challenge. All three keep facts, assumptions, and unknowns visible, and every one stops at a human decision.

If a skill treats a guess as evidence or decides for you, stop and correct it. A tidy artifact is the start of a review, not permission to ship.
