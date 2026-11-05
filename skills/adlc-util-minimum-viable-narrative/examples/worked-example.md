# Worked Example: Minimum Viable Narrative

Synthetic example. All details are invented for teaching.

This continues the renewal-plan idea from a synthetic Guided-mode exercise (case 08) past Stage 1. Case 08 stops at Stage 1, so the harness details below are invented for this example only: an agent that drafts renewal plans for a customer success manager (CSM) to edit, at draft autonomy, never sending anything to a customer, never changing the CRM, and never proposing pricing or discounts.

**Opening:** "We will tell one story per prototype variant, in labelled action and response turns, and save a portable prompt and build instruction for each, then decide pivot, punt, or pursue before the bake-off. I will use the harness brief and anything earlier, ask no more than eight context questions, and stop at that decision. Choose 1. Guided, 2. Context dump, or 3. Best guess." Mode chosen: **Guided**.

**What the skill already had, in one line:** "From the harness brief I have two variants, plan first and risks first; the bet; the draft-only ceiling; and the handback for any contract term the agent cannot confirm. I'll skip Q1 and Q2."

## Questions Asked

| Label | Answer | Used for |
|---|---|---|
| Narrative Q3/8 | Sam, a CSM with 40 accounts, the Monday a renewal comes up 90 days out. | Audience |
| Narrative Q4/8 | Sam has a renewal call in two weeks for an account worth a fifth of Sam's book, a crowded inbox, and no time to pull usage, tickets, and contract terms together. Sam knows support has been rough this quarter but not how rough, and isn't sure the renewal date in the CRM matches the signed contract. | Setup |
| Narrative Q5/8 | Sam opens the account and sees a draft plan with each claim linked to where it came from. | Encounter |
| Narrative Q6/8 | The skill offered four draft turns from the harness fixtures. The Product Manager kept turns 2 to 4 and rewrote turn 1, which had Sam only "open the plan": "Sam flags the usage claim that looks wrong." | Plan-first turns |
| Narrative Q7/8 | Risks first replaces turn 1 with two turns: Sam picks the top risk to look into, then dismisses one already known. The contract and editing turns stay the same. | Risks-first turns |
| Narrative Q8/8 | Sam edits the draft and is ready for the call in under two hours, confident nothing was missed. | Resolution |

Six numbered questions against a budget of eight, no follow-ups. Q6 started from draft turns, so the person corrected one passive Action instead of inventing four turns, and kept two of the three optional actions the skill offered for the turns where Sam would hesitate.

## Prototype Hypothesis

> If we draft renewal plans from usage, tickets, and contract terms for the CSM to edit, for CSMs preparing renewals, then we will help them finish a plan in under two hours with a risk section that catches what they would have missed.

## Target Audience

Sam, a CSM with 40 accounts, on the Monday a renewal comes up 90 days out.

## Setup

Sam has a renewal call in two weeks for an account worth a fifth of Sam's book, a crowded inbox, and no time to pull usage, support history, and contract terms together. Sam knows support has been rough this quarter but not how rough, and isn't sure the renewal date in the CRM matches the signed contract.

## Encounter

Sam follows Monday's renewal reminder into the account and finds a draft plan waiting, every claim in it tied to where it came from.

## Action-Response Loop, Variant: Plan First

| Turn | Human Action | System Response |
|---|---|---|
| 1 of 4 | Sam flags a usage claim that looks wrong. | It shows the usage figures behind the claim and the dates they cover, and offers to drop the claim if Sam still disagrees. |
| 2 of 4 | Sam keeps the claim and moves on to the contract terms. | The renewal date it couldn't confirm is left blank, with where it looked, and it asks Sam for the date instead of guessing. (Handback; shared) |
| 2 of 4 (optional) | Sam asks why the CRM date wasn't used. | It shows the CRM date beside the contract clause that doesn't match it, and still leaves the date to Sam. |
| 3 of 4 | Sam types in the renewal date from the signed contract. | It marks the date as Sam's and re-checks the plan's timeline against it. (Shared) |
| 4 of 4 | Sam rewrites the risk section in their own words. | It keeps Sam's edits marked as Sam's and gives back a plan ready to take into the call. (Shared) |

**Resolution:** Sam is ready for the call in under two hours.

## Action-Response Loop, Variant: Risks First

| Turn | Human Action | System Response |
|---|---|---|
| 1 of 5 | Sam picks the biggest of the three risks it found, a jump in support tickets, to look into. | It shows the tickets behind that risk and when they started. |
| 1 of 5 (optional) | Sam asks how the three risks were ranked. | It explains what each ranking rests on, changing nothing. |
| 2 of 5 | Sam dismisses another risk Sam already knows about. | It asks for one line on why, moves the risk to "reviewed," and shows the plan built around the rest. |
| 3 of 5 | Sam moves on to the contract terms. | The renewal date it couldn't confirm is left blank, with where it looked, and it asks Sam for the date instead of guessing. (Handback; shared) |
| 3 of 5 (optional) | Sam asks why the CRM date wasn't used. | It shows the CRM date beside the contract clause that doesn't match it, and still leaves the date to Sam. |
| 4 of 5 | Sam types in the renewal date from the signed contract. | It marks the date as Sam's and re-checks the plan's timeline against it. (Shared) |
| 5 of 5 | Sam rewrites the risk section in their own words. | It keeps Sam's edits marked as Sam's and gives back a plan ready to take into the call. (Shared) |

**Resolution:** Sam is ready for the call in under two hours, sure nothing was missed.

### How The Variants Differ

Plan first opens on the whole plan and lets Sam challenge one claim; risks first opens on the risks and lets Sam triage them. The contract and editing turns are shared, so the bake-off compares the opening.

## No/Lo-Code Prompt

| Variant | File | Labelled turns? | Experience baseline? | Reads cleanly to a stranger? |
|---|---|---|---|---|
| Plan first | `prototype-prompt-plan-first.md` | yes | yes | yes |
| Risks first | `prototype-prompt-risks-first.md` | yes | yes | yes |

The risks-first prompt, in full:

```
# Prototype prompt: renewal plan, risks first

Build a functional, throwaway prototype of the story below. It should be realistic
enough to provoke an honest reaction from the person using it, and not polished
enough to ship.

The prototype exists to validate or invalidate this hypothesis from the perspective
of the person who would use it: does a customer success manager prepare a renewal
plan faster, and miss less, when the risks come first?

## Hypothesis
If we draft renewal plans from usage, tickets, and contract terms for the CSM to edit,
for CSMs preparing renewals, then we will help them finish a plan in under two hours
with a risk section that catches what they would have missed.

## Audience
Sam, a customer success manager with 40 accounts, on the Monday a renewal comes up
90 days out.

## The Story
The prototype needs to move Sam through these five moments.
- **Setup:** Sam has a renewal call in two weeks for an account worth a fifth of Sam's
  book, a crowded inbox, and no time to pull usage, support history, and contract terms
  together. Sam knows support has been rough this quarter but not how rough, and isn't
  sure the renewal date in the CRM matches the signed contract.
- **Encounter:** Sam follows Monday's renewal reminder into the account and finds a
  draft plan waiting, every claim in it tied to where it came from.
- **Action-Response Loop (5 turns):**
  - **Human Action [turn 1 of 5]:** Sam picks the biggest of the three risks it found,
    a jump in support tickets, to look into.
  - **System Response [turn 1 of 5]:** It shows the tickets behind that risk and when
    they started.
  - **Optional Action [turn 1 of 5]:** Sam asks how the three risks were ranked.
  - **Optional Response [turn 1 of 5]:** It explains what each ranking rests on,
    changing nothing.
  - **Human Action [turn 2 of 5]:** Sam dismisses another risk Sam already knows about.
  - **System Response [turn 2 of 5]:** It asks for one line on why, moves the risk to
    "reviewed," and shows the plan built around the rest.
  - **Human Action [turn 3 of 5]:** Sam moves on to the contract terms.
  - **System Response [turn 3 of 5]:** The renewal date it couldn't confirm is left
    blank, with where it looked, and it asks Sam for the date instead of guessing.
  - **Optional Action [turn 3 of 5]:** Sam asks why the CRM date wasn't used.
  - **Optional Response [turn 3 of 5]:** It shows the CRM date beside the contract
    clause that doesn't match it, and still leaves the date to Sam.
  - **Human Action [turn 4 of 5]:** Sam types in the renewal date from the signed
    contract.
  - **System Response [turn 4 of 5]:** It marks the date as Sam's and re-checks the
    plan's timeline against it.
  - **Human Action [turn 5 of 5]:** Sam rewrites the risk section in their own words.
  - **System Response [turn 5 of 5]:** It keeps Sam's edits marked as Sam's and gives
    back a plan ready to take into the call.
- **Resolution:** Sam is ready for the call in under two hours, sure nothing was missed.

## It Must Never
- Send anything to the customer. Nothing in the prototype lets Sam do that.
- Change the account record.
- Suggest a price or a discount.
- Fill in a contract term it couldn't confirm.

## How It Should Feel To Use
- Sam always knows where they are in the task, what they have done, and what is left.
- Before Sam commits, Sam can ask why, see where something came from, or preview what
  a choice would change, without losing their place.
- When Sam has to choose, Sam sees every option with what supports it, picks one, and
  confirms it. Nothing moves on until Sam has chosen.
- Anything Sam chooses or adds, Sam can change or undo, and can see which choices and
  evidence were Sam's.
- The next step is always obvious. A step Sam can't take yet is visibly unavailable,
  and Sam can see why.
- Nothing happens that Sam didn't ask for. Drafts are plainly drafts, and nothing
  leaves Sam's hands without Sam's say.
- Outside content, warnings, missing items, and Sam's own additions each look distinct
  from ordinary content and from each other.
- Things Sam types in look different from things Sam presses.
- Text is easy to read, in plain, specific words, with contrast, keyboard use, and
  screen sizes that meet common accessibility practice.

## Data
Use invented people, companies, and records only.

## Your Output
- Build only what this story requires, and leave out anything that is not in it.
- Make it look and feel like a working product.
- Sam should be able to react to it without anyone explaining it.
- Be descriptive, not prescriptive: decide the layout, flow, styling, wording, and
  interface details yourself. If a style or design guide comes with this prompt,
  follow it for the look and feel; it does not change the story.
- Wherever the story leaves the design open, lean on well-established UX conventions
  and accessibility practice for this kind of task.
- If you write code and were given no other instruction, one self-contained page that
  runs in a browser is enough.
```

The plan-first prompt is the same except for its question, its loop, and its Resolution.

## Build Instruction

Typed into the builder with `prototype-prompt-risks-first.md` attached:

> Let's generate a fully-functional yet throw-away HTML5 SPA file using the attached Minimum Viable Narrative describing the user's journey. Wherever the story leaves the design open, lean on well-established UX conventions and accessibility practice for this kind of task, so the person never has to wonder where they are, what they can do next, or how to undo a choice.

- Style or design guide: none supplied, so the instruction leaves out "and an attached style guide." The experience baseline in each prompt still applies.
- Review aid, design agents only: show one screen per moment of the story, captioned with its turn.

## Authority Ceiling (stated once, beside the stories)

- Autonomy level: draft.
- Blocked actions: sending anything to a customer; changing the CRM; proposing pricing or discounts.
- Handbacks every variant keeps: any contract term or renewal date the agent cannot confirm is left for the CSM, never filled in.

## Evidence Ledger

| Claim | State | Basis |
|---|---|---|
| Risks first will help Sam miss less | Assumption | The story; no reactions yet |
| A plan in under two hours | Assumption | Target from Stage 1 |
| Every variant keeps the unconfirmed-term handback | Fact | Approved harness brief (invented for this example) |

## Decision

- Recommendation: Pursue into the Stage 4 bake-off with both variants.
- Human decision: the Product Manager chose to pursue. This is the person's choice, recorded for the example, not the skill's approval.
- Revisit trigger: not applicable.
- Unresolved disagreements: none recorded.
- Next step: build each variant from its prompt and the build instruction, have one or two CSMs run it, then Stage 4, a bake-off between plan first and risks first.
