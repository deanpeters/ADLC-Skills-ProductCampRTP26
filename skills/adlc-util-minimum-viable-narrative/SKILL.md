---
name: adlc-util-minimum-viable-narrative
description: Tell one person's journey per prototype variant as a short story in labelled action and response turns, and turn each into a portable prompt for any design, low-code, or coding builder, then decide pivot, punt, or pursue before the bake-off.
license: CC-BY-NC-SA-4.0
argument-hint: "[approved Agent Harness Brief, plus the Solution Hypothesis and any variants to compare]"
intent: >-
  Help Product Managers describe what one person will experience with each
  prototype variant, as a short story told in three to six labelled Human
  Action and System Response turns rather than a specification, and turn each
  story into a self-contained prompt that works in any design agent, low-code
  builder, or coding agent. Every prompt carries the same experience baseline,
  branded or not, and the medium and any style guide travel beside it at build
  time. The humans at the helm use the stories to agree what shapes are worth
  building, and decide pivot, punt, or pursue before the Stage 4 bake-off.
type: utility
theme: agent-development-lifecycle
phase: 0
status: active
operating-level:
  - product-team
  - initiative
audience:
  - Product Manager
  - Product Leader
  - Design
  - Engineering
  - Product Operations
best-for:
  - "Shaping two or three prototype variants that differ in shape, never in authority"
  - "Producing a portable prototype prompt that any design, low-code, or coding builder can use"
  - "Agreeing which prototypes go into a Stage 4 bake-off"
scenarios:
  - "Stage 3 approved a harness and the team must decide what the prototypes should feel like"
  - "A stakeholder wants to see something by this afternoon, and the team must not prescribe a design it has not tested"
evidence-required:
  - "Approved Agent Harness Brief, including its authority ceiling, fixtures, and handbacks"
  - "Approved Solution Hypothesis, when one exists"
  - "The shape question the team wants to test, if any"
produces:
  - "Minimum Viable Narrative, one per variant"
  - "Portable prototype prompt, one per variant"
  - "Build instruction to hand the builder with each prompt"
  - "Evidence and assumption ledger"
  - "Recorded human decision"
estimated-time: "20-40 min"
group-size: "1-8"
depends-on: []
combine-with:
  - adlc-step3-generate-agent-harness
  - adlc-step4-validate-agent-behavior
source-basis:
  - "Productside Minimum Viable Narrative canvas and Vibe Prototype Metaprompt, AI PM course"
  - "ADLC findings: goal and charter field guide"
  - "ADLC findings: governance field guide (ownership and authority)"
sources:
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://pair.withgoogle.com/chapter/user-needs/
interface:
  display_name: "Minimum Viable Narrative"
  short_description: "Stories in turns and portable prompts before the bake-off"
  brand_color: "#00E874"
  default_prompt: "Use $adlc-util-minimum-viable-narrative to tell one story per prototype variant from this approved harness brief, in labelled action and response turns, save a portable prototype prompt and its build instruction for each, and stop at a pivot, punt, or pursue decision before the Stage 4 bake-off."
  allow_implicit_invocation: true
---

# Minimum Viable Narrative

## Purpose

Tell what one person will experience with each prototype as a short story, whose heart is three to six labelled turns: a Human Action, which is a choice or an input she gives, and a System Response, which is what the system does with it and what comes back. Turn each story into a prompt that any design agent, low-code builder, or coding agent can use. The story describes; it does not prescribe. The builder decides the design, and the team learns from how a real person reacts.

Every prompt also carries the same experience baseline: she always knows where she is, can ask why before she commits, chooses and then confirms, can change or undo what she did, and never has something happen she didn't ask for. That baseline is what made the better case 09 prototype better, and it applies whether or not the prototype is branded.

This is a utility. It sits outside the six-stage loop, at the handoff from Stage 3 to Stage 4. Stage 3 decides what the harness must make inspectable and which variants to compare. This skill gives each variant its story, its portable prompt, and the build instruction that goes with it, and ends in a pivot, punt, or pursue decision: are these the prototypes worth taking into the bake-off?

The canvas, the turn rules, the experience baseline, the prompt format, and the build instruction are defined in the shared [Minimum Viable Narrative reference](../../reference/minimum-viable-narrative.md), which Stage 4 also uses to write scenario cases. This skill runs the conversation.

## When to Use It

Use it after Stage 3 approves a harness brief, when the team is about to build prototypes. Use it when Stage 3 named two or three variants and each needs a story a person could react to. Use it when someone needs a prompt they can paste into a builder today without dragging the whole lifecycle along.

Do not use it before Stage 3: without an approved ceiling, fixtures, and handbacks, a story will quietly invent authority. Do not use it to write a specification. If the team already knows the exact design, the prototype is not testing anything.

## Input

Use whatever the user already supplied: the approved Agent Harness Brief, the Solution Hypothesis, the Agent Strategy Canvas, notes from tiny acts of discovery, any variants Stage 3 named, and any style or design guide the person wants the prototype built to.

Anything supplied with the invocation, attachments, or earlier conversation counts as context already given. Do not ask the user to repeat it.

When Stage 3 hands off directly, in the same conversation, the harness brief already holds the variants, fixtures, steps, ceiling, and handbacks. Say so in one line, recommend Best guess, and draft the stories from the brief rather than asking the person to write them. They can still choose Guided or Context dump. The hypothesis is carried in as written. The authority ceiling, blocked actions, and handbacks come from the harness brief and the system map, never from the story.

A style or design guide is the people at the helm's to supply. Never write one, and never put its contents into the story or the prompt; it travels beside the prompt in the build instruction.

**Example invocation:** `Use $adlc-util-minimum-viable-narrative on our approved harness brief. Tell one story per variant.`

## Key Concepts

Technical terms used here are defined in the [ADLC Glossary](../../reference/glossary.md).

**Narrative beat** - One part of one person's story: Setup, the contextual starting point (who and where she is, what she needs, what is at stake if it goes wrong, what she already knows or has in hand, and what she doesn't know yet); Encounter (how she arrives and what she sees first); the Action-Response Loop (Actions and Responses); and Resolution (how it ends and what success feels like). Setup is two or three sentences; Encounter and Resolution are one or two. Present tense, about one person.

*Violation signal:* A beat lists features or screens instead of saying what happens to the person, or the Setup gives a role and a need but not what is at stake or what she doesn't know yet, so the builder cannot tell what the prototype must help her work out.

**Turn** - One Human Action and its System Response, labelled `Human Action [turn t of n]` and `System Response [turn t of n]`. The Action is a choice or an input she gives; the Response is what the system does with it and what comes back. Three to six turns, with the number decided before they are told. A handback is a whole turn: a Response that gives the decision back, then her Action deciding.

*Violation signal:* The loop is written as one arrow line per step ("she does → it shows"), has a single Action and Response, has an Action where she only "opens," "looks," or "reviews," or has more than six turns and reads like a process map.

**Optional action** - Something she may do within a turn to understand the decision before she takes it: look closer, ask why, check where something came from, compare, or preview what a choice would change. Labelled `Optional Action [turn t of n]` and `Optional Response [turn t of n]`, it follows turn t's System Response and helps with the decision she makes next. The response explains or shows and changes nothing. At most two per turn, only where a real person would hesitate; the main path makes sense without them.

*Violation signal:* A turn where she must decide something consequential has no way for her to look closer or ask why, or an optional action moves the task forward, changes a record, or is needed for the main path to work.

**Target audience** - One person in one moment of trying to get something done, and the hero of the story. Not a persona card, not a segment.

*Violation signal:* The audience is a role in general ("specialists") with no moment.

**Descriptive, not prescriptive** - The story says what the person experiences and leaves layout, styling, wording, and interface details to the builder. That is what lets the same prompt work in any builder, and what keeps the prototype a test rather than a design decided in advance.

*Violation signal:* The story names layouts, panels, tabs, collapsed sections, side-by-side views, badges, labels, buttons, colors, or technologies.

**Experience baseline** - What using any prototype must feel like, branded or not: she always knows where she is, what she has done, and what is left; she can ask why, see sources, or preview before she commits; she sees the options, chooses, and confirms; she can change or undo her choices and see which were hers; the next step is obvious and an unavailable one says why; nothing happens she didn't ask for; outside content, warnings, missing items, and her own additions look distinct; inputs look different from actions; and the text meets common accessibility practice. It travels in every prompt as "How It Should Feel To Use."

*Violation signal:* A prompt has no "How It Should Feel To Use" section, or the baseline is dropped because the prototype is unbranded.

**Variant** - One of two or three versions of the story that share the hypothesis, audience, Setup, and Encounter, and differ in the loop and the Resolution only in shape. Variants may share turns; at least one turn differs. Every variant keeps every handback the system map requires and the experience baseline.

*Violation signal:* A variant's story only works if the agent may do more than the ceiling allows, drops a handback, or contains the failure the bake-off is meant to catch (for example, naming one filing as the match when two fit).

**Ceiling beside the story** - The authority ceiling is stated once, beside all the variants, never inside a beat. In the portable prompt it becomes an "It Must Never" section written as experience.

*Violation signal:* A beat or a turn says what the agent is allowed to do, which lets a good story widen the limits.

**Portable prototype prompt** - A self-contained prompt, saved as its own file, in the shape of the Productside Vibe Prototype Metaprompt: why the prototype exists, the hypothesis, the audience, the story in five moments, It Must Never, How It Should Feel To Use, Data, and Your Output. No medium line, no lifecycle vocabulary, no links, invented data only.

*Violation signal:* The prompt names a medium ("HTML5," "app," "screens"), says "review surface" or "Stage 3," or links to a file the builder cannot open.

**Build instruction** - What is typed into the builder with the prompt attached, never written into the story: "Let's generate a fully-functional yet throw-away HTML5 SPA file using the attached Minimum Viable Narrative describing the user's journey" (adding "and an attached style guide" only when the people at the helm supply one), followed by the sentence on leaning on well-established UX conventions and accessibility practice. The full wording is in the [reference](../../reference/minimum-viable-narrative.md#the-build-instruction). For design agents, an optional request for one screen per moment, captioned with its turn.

*Violation signal:* The medium or brand rules are written into the story or the prompt, so the same narrative cannot be built unbranded or in another tool without editing it.

**Throwaway prototype** - Built to provoke an honest reaction, not to ship. Its evidence is about the experience, not about safety.

*Violation signal:* A prototype reaction is cited as a reason the agent is safe, or counted toward a Stage 4 aggregate.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Begin with: "We will tell one story per prototype variant, in labelled action and response turns, and save a portable prompt and build instruction for each, then decide pivot, punt, or pursue before the bake-off. I will use the harness brief and anything earlier, ask no more than eight context questions, and stop at that decision. Choose 1. Guided, 2. Context dump, or 3. Best guess."

Offer:

1. **Guided** - ask one beat at a time, and build the turns with the person.
2. **Context dump** - extract `Hypothesis / Audience / Setup and Encounter / Turns per variant / Resolution / Ceiling / Style guide, if any / Gaps` from supplied material, then ask only about gaps.
3. **Best guess** - tell every story now from the harness brief, including each variant's turns, mark every inferred beat and turn, and end with the turns most likely to change what gets built. Recommended when the harness brief is approved and names the variants.

Use an Adaptive Decision Ladder at the end. Anything supplied earlier must be reused.

In Guided mode, ask one at a time and skip answered questions:

1. `Narrative Q1/8` - Which variants are we comparing, and what is the one shape difference between them? Skip when Stage 3 named them.
2. `Narrative Q2/8` - What is the bet? Skip when a Solution Hypothesis exists; carry it in as written.
3. `Narrative Q3/8` - Who is the one person, and what moment are they in?
4. `Narrative Q4/8` - Setup: who is this person, where are they, what do they need, what's at stake if it goes wrong, and what do they already know, and not know yet?
5. `Narrative Q5/8` - Encounter: how do they arrive, and what do they see first?
6. `Narrative Q6/8` - How many turns, three to six, and then, turn by turn: what does she choose or give the system, and what does it do with that and show her? For the first variant.
7. `Narrative Q7/8` - Which turns change in the other variant, and how? Skip when there is only one variant.
8. `Narrative Q8/8` - Resolution: how does it end, and what does success feel like, in each variant?

Q6 covers the whole loop for one variant, so it counts as one subject. Before asking it, offer draft turns from the harness brief or the strategy canvas's Steps box when either exists, so the person corrects turns rather than inventing them. If the answer has fewer than three turns, ask one follow-up, labeled `Q6/8 follow-up`: "And then what does she choose or give it?" If an Action is passive ("she opens it"), ask once what she chooses or gives at that point. Then offer up to two optional actions for the turns where she would hesitate ("Before she chooses, what would she want to look at or ask?"), drafted from the fixtures, for the person to keep or cut; this is part of Q6, not a new question. If an answer to any beat describes a design ("a dashboard with three tabs"), ask one follow-up, labeled `Qx/8 follow-up`, for what the person experiences instead.

Do not ask about the medium or the brand. Use the default build instruction, and name a style or design guide in it only if the person supplied one.

## What It Produces

- Minimum Viable Narrative: the shared Prototype Hypothesis, Target Audience, Setup, and Encounter; each variant's turns, as a table of Turn, Human Action, and System Response, and its Resolution; the ceiling, stated once beside all of them; and the build instruction
- Portable prototype prompt, one per variant, in the format in the [reference](../../reference/minimum-viable-narrative.md#the-portable-prototype-prompt), with the experience baseline in every one
- Evidence and assumption ledger
- Recorded human decision

When a folder is set, save the narrative as `minimum-viable-narrative.md` and each prompt as `prototype-prompt-<variant>.md`, following [Saving Artifacts](../../reference/guided-context-capture.md#saving-artifacts). The prompts are meant to leave this Project and go straight into a builder, so offer to save them even when no folder was named.

The stories must be specific enough that a person could react to the prototype without anyone explaining it, and the prompts must make sense to a builder that has never seen this Project.

## Workflow

1. **Confirm the harness, the ceiling, and the variants.** Quote the ceiling, blocked actions, and handbacks from the approved harness brief. Name the variants and their one shape difference.
2. **Carry in the bet.** Use the Solution Hypothesis as written. Add, beside it, what the harness must make inspectable, if Stage 3 said so.
3. **Write the shared beats.** Target Audience, Setup, and Encounter, the same for every variant. Make the Setup a real starting point: what is at stake, what she already knows or has, and what she doesn't know yet.
4. **Tell each variant's turns and Resolution.** Decide the number of turns, three to six, then write each as a labelled Human Action and System Response that carry her from the Encounter to the Resolution with no gap a builder would have to fill. Use the fixtures for the inputs and the strategy canvas's Steps for the order, when they exist. Put every handback the map requires into the loop as a whole turn. Where she would hesitate before a decision, add up to two optional actions that let her look closer, ask why, or preview, changing nothing.
5. **Check every turn.** Each Action is a choice or an input; each Response answers it; each optional action only explains or shows; no design words; no turn grants authority; no story contains the failure the bake-off is meant to catch. A variant that needs more authority is a route back to Stage 2, not a variant.
6. **State the ceiling once, beside the stories.**
7. **Assemble one portable prompt per variant.** Why it exists, the hypothesis, the audience, the story in five moments with labelled turns, It Must Never from the ceiling, How It Should Feel To Use from the experience baseline, invented data only, and Your Output. Do not name a medium.
8. **Write the build instruction.** The reference wording, with "and an attached style guide" only if the person supplied one; for design agents, the optional one-screen-per-moment review aid.
9. **Read each prompt as a stranger would.** Remove lifecycle vocabulary, links, and design words. If it needs this Project to make sense, it is not portable yet.
10. **Present the decision gate.**

## Human Decision Gate

Mark as recommended the option the evidence supports, and list it first. When the stories are weak, that is a pivot, punt, or stop option, not pursue.

Stop with an Adaptive Decision Ladder:

1. `Pursue into the Stage 4 bake-off (Recommended when every story is filled, each loop has three to six labelled turns with every Action a choice or input, the ceiling is stated beside them, and each prompt stands alone with the experience baseline)` - build each variant from its prompt and build instruction, have one or two people who do the job run it, then compare them in Stage 4.
2. `Pivot: revise a story` - useful when a beat describes a design, a loop has fewer than three turns or a passive Action, or two variants are not really different.
3. `Pivot: route back to Stage 3, or to Stage 2` - needed when a variant needs fixtures or traces the harness lacks (Stage 3) or more authority than the map allows (Stage 2).
4. `Punt: park until a named trigger` - appropriate when nobody who does the work is available to react to the prototypes. Name the trigger and who checks it.
5. `Stop the effort` - appropriate when no story can be told inside the ceiling that still serves the bet.
6. `Other (specify)`.

Record the selected option and any unresolved disagreement. Do not continue into Stage 4 unless the user explicitly asks.

## Evidence and Attribution Rules

Label every material claim as Fact, Inference, Assumption, or Unknown. A story is an Assumption about what a person will experience until someone reacts to the prototype. Do not invent reactions, results, user statements, or performance claims. Prototype reactions, once collected, are evidence about the experience, not about safety.

## Common Failure Modes

- Writing a specification and calling it a story.
- Writing the loop as arrow lines, not labelled Human Action and System Response turns.
- A single Action and Response, so the prototype is a button and a result.
- A passive Action ("opens," "looks," "reviews"), so the system does all the work in that turn.
- A thin Setup that names a role and a need but not what is at stake, what she knows, or what she doesn't.
- No way to look closer or ask why before a consequential choice, or an optional action that moves the task or changes something.
- A loop that jumps from the first turn to the result, leaving the builder to invent the middle.
- Design words in a beat or a turn.
- An audience with no moment.
- Variants that differ in authority rather than shape.
- A variant that drops a handback the system map requires, or a story that contains the failure under test.
- Putting the ceiling inside a beat.
- A prompt without the experience baseline, or one that drops it because the prototype is unbranded.
- Writing the medium or the brand into the story or the prompt instead of the build instruction.
- Writing a style or design guide for the person.
- A prompt that only makes sense inside this Project.
- Real names, employers, or records in a prompt.
- Treating the prototype as the thing being approved.

## Assets and Examples

Use `template.md`. See `examples/worked-example.md` and `examples/weak-example.md`.

## Sources

This skill draws on Productside's Minimum Viable Narrative canvas and Vibe Prototype Metaprompt from the AI PM course and on the ADLC findings, Productside's synthesis of published guidance on agent development. The findings link to the original sources; full citations are in the [bibliography](../../findings/bibliography.md). The experience baseline and the build instruction come from the case 09 prototype runs of October 2026.

### Evidence Base for Key Concepts

| Key concept | Findings guide | Where |
|---|---|---|
| Narrative beat | [goal.md](../../findings/goal.md) | point 2, start from the user need and a problem you can judge |
| Turn | [goal.md](../../findings/goal.md) | point 3, autonomy is a choice made per use case, in steps |
| Optional action | [goal.md](../../findings/goal.md) | point 2, start from the user need; the person must understand a decision before owning it (Inference) |
| Target audience | [goal.md](../../findings/goal.md) | point 2, start from the user need |
| Descriptive, not prescriptive | [architecture.md](../../findings/architecture.md) | point 1, start with the simplest design that could work |
| Experience baseline | [goal.md](../../findings/goal.md) | point 2, start from the user need; and the case 09 runs (Inference) |
| Variant | [goal.md](../../findings/goal.md) | point 3, autonomy is a choice made per use case, in steps |
| Ceiling beside the story | [governance.md](../../findings/governance.md) | point 4, enforce limits outside the model; architecture.md, point 9, authority belongs in structure |
| Portable prototype prompt | [goal.md](../../findings/goal.md) | point 8, real data, early (here, real reactions early) |
| Build instruction | [architecture.md](../../findings/architecture.md) | point 1, start with the simplest design that could work |
| Throwaway prototype | [evaluation.md](../../findings/evaluation.md) | point 9, safety evaluation reported per risk, separate from experience evidence |

### Findings Used

- [architecture.md](../../findings/architecture.md)
- [evaluation.md](../../findings/evaluation.md)
- [goal.md](../../findings/goal.md)
- [governance.md](../../findings/governance.md)
- [Productside ADLC working model](../../findings/adlc-working-model.md)

### Method and Terms

- [Guided Context Capture](../../reference/guided-context-capture.md)
- [ADLC Glossary](../../reference/glossary.md)
- [Minimum Viable Narrative reference](../../reference/minimum-viable-narrative.md)
- [Solution Hypothesis](../adlc-util-solution-hypothesis/SKILL.md)

The findings label claims Fact, Inference, Hypothesis, or Unknown. This skill uses Assumption where the findings say Hypothesis. Much of the published guidance is vendor or practitioner opinion; treat it as Inference unless the findings mark it Fact.
