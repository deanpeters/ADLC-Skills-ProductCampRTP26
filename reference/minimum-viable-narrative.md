# Minimum Viable Narrative

The shared definition of the canvas, used two ways: by the [Minimum Viable Narrative](../skills/adlc-util-minimum-viable-narrative/SKILL.md) utility skill, which runs the conversation at the Stage 3 to Stage 4 handoff and saves the portable prototype prompts, and inside Stage 4, to write scenario cases as stories. It adapts Productside's Minimum Viable Narrative canvas and its Vibe Prototype Metaprompt, taught in the AI PM course, so a Product Manager can describe what a person will experience with an agent or agentic interface before anyone builds or tests it.

Used inside Stage 3 or Stage 4, the canvas is a way to collect answers the stage already asks for: it adds no questions, no budget, and no gate. Used through the utility skill, it has its own questions and its own pivot, punt, or pursue decision. Either way it is optional.

## What It Is For

A Minimum Viable Narrative tells one person's journey through a prototype as a short story. Its job is to be **portable**: the same story goes, unchanged, into any of three kinds of builder and produces something a person can react to.

| Kind of builder | Examples |
|---|---|
| Design agents | Figma, Stitch |
| Low-code builders | Lovable, Bolt, Base44, v0 |
| Full-coding agents | Claude Cowork, Codex |

These tools already know design, code, and flow. The narrative says what happens to the person. Layout, styling, wording, and interface details are the builder's decisions. That is what lets the same story work in every tool, and what keeps the prototype a test rather than a design decided in advance.

## The Canvas

| Field | What goes in it |
|---|---|
| Prototype Hypothesis | The bet this narrative is built to test. Carried in as written from the [Solution Hypothesis](../skills/adlc-util-solution-hypothesis/SKILL.md) statement when one exists. Do not rewrite it. |
| Target Audience | One sentence: who is going to use the prototype, where they are, and what they are in the middle of trying to do. A character in a moment, and the hero of the story. Not a persona card. |
| Setup | The contextual starting point: who this person is and where they are, what they need, what is at stake if it goes wrong, what they already know or have in hand, and what they don't know yet. Two or three sentences. |
| Encounter | How they arrive, what brought them here, and what the system shows them first. One or two sentences. |
| Action-Response Loop | Three to six turns of the person with the system. Each turn is a Human Action and a System Response, plus up to two optional actions she may take to understand the choice before she makes it. |
| Resolution | How it ends, and what success looks and feels like. One or two sentences. |
| No/Lo-Code Prompt | The portable prompt assembled from the fields above, saved as its own file. |

The five narrative beats are Setup, Encounter, Actions, Responses, and Resolution. Write a story, not a specification: present tense, about one person, in plain words a builder could read aloud and picture.

### The Action-Response Loop

Decide the number of turns first, three to six, then tell them. Write each turn as two labelled lines, the way the course canvas keeps Actions and Responses in separate columns:

```
Human Action [turn 1 of 5]: <what the person does or gives the system: a choice or an input>
System Response [turn 1 of 5]: <what the system does with that input, and what comes back>
```

A turn may also carry up to two **optional actions**: things she may do to understand what the System Response just showed her, before her next Human Action. They follow that turn's System Response and carry its turn number:

```
Optional Action [turn 1 of 5]: <she looks closer, asks why, checks a source, compares, or previews>
Optional Response [turn 1 of 5]: <what it explains or shows, without moving the task forward or changing anything>
```

In a saved narrative, a table with Turn, Human Action, and System Response columns does the same job, with each optional action as its own row marked "optional" under its turn.

**Rules for the turns:**

1. **Every Human Action is a choice or an input.** She confirms, chooses, types in, marks, asks for, corrects, rewrites. "Opens," "looks at," and "reviews" are not Actions: the system ends up doing the work and the person reacting to the prototype has nothing to do.
2. **Every System Response answers that Action.** It says what the system did with what she gave it, and what she now has.
3. **Each turn moves the task forward.** Together the turns carry her from the Encounter to the Resolution with no gap a builder would have to invent.
4. **A handback is a whole turn.** The System Response gives the decision back ("it shows both filings and asks her which one the notice means; it does not choose"), and the next Human Action is her deciding. The loop shows a handback happening; it never grants authority.
5. **No design words.** No layouts, panels, tabs, collapsed sections, side-by-side views, badges, labels, buttons, colors, or technologies. Say what she experiences ("it shows her both filings and where they differ"), not how it is arranged.
6. **The story never contains the failure under test.** If a variant may fail by naming one filing when two fit, its story still keeps the handback. A failure should come from the build, not from the story.
7. **Optional actions help her understand; they never move the task.** She looks closer, asks why, checks where something came from, compares, or previews what a choice would change. The response explains or shows and leaves everything as it was. Each one follows its turn's System Response and helps with the decision she makes next. At most two per turn, only where a real person would hesitate, and the main path must still make sense without them. They are where a builder learns what she needs to see to trust the decision.

For example, a person reconciling payroll records against a tax agency notice:

| Turn | Human Action | System Response |
|---|---|---|
| 1 of 5 | She confirms the employer and quarter it read from the notice. | It comes back with two filings that both fit, an original and a correction, shows what in the notice points to each and where they differ, and asks her which one the notice means. |
| 2 of 5 | She chooses the corrected filing. | It matches the quarter's deposits against that filing and tells her what doesn't add up, including one deposit with no bank record behind it. |
| 3 of 5 | She types in the bank reference from her own files, or marks the deposit as still outstanding. | It shows her which findings now rest on what she added and what is still missing. |
| 4 of 5 | She asks for a draft reply. | It writes one, plainly marked as a draft, with every statement tied to the record it came from. |
| 5 of 5 | She rewrites the opening paragraph in her own words. | It checks that every statement still traces back to a record and gathers everything into one packet for her signer. |

Or a field engineer choosing a pump for a well: she enters the well's depth and expected flow, and it shows three pumps that fit with the trade-offs between them; she rules one out for parts availability, and it re-ranks the other two and says what each assumes; she asks what would change the choice, and it names the two measurements that would; and so on, until she has a choice she can defend to her supervisor.

If an [Agent Strategy Canvas](../skills/adlc-util-agent-strategy-canvas/SKILL.md) exists, its Steps box supplies the order of the loop: a person step becomes a Human Action, an agent step becomes a System Response, and a handback step becomes a System Response that hands the decision back, followed by her Human Action. Its Milestones box says what good looks like after each turn, and its last milestone supplies the Resolution.

## The Experience Baseline

Every prototype prompt carries the same short list of what using the prototype must feel like, whether or not it is branded. It came from the case 09 runs in Figma: the variant built with these qualities was clearly better than the one built without them. Each line describes an experience, not a component, so the builder still decides how to deliver it.

- She always knows where she is in the task, what she has done, and what is left.
- Before she commits, she can ask why, see where something came from, or preview what a choice would change, without losing her place.
- When she has to choose, she sees every option with what supports it, picks one, and confirms it. Nothing moves on until she has chosen.
- Anything she chooses or adds, she can change or undo, and she can see which choices and evidence were hers.
- The next step is always obvious. A step she can't take yet is visibly unavailable, and she can see why.
- Nothing happens that she didn't ask for. Drafts are plainly drafts, and nothing leaves her hands without her say.
- Outside content, warnings, missing items, and her own additions each look distinct from ordinary content and from each other.
- Things she types in look different from things she presses.
- Text is easy to read, in plain, specific words, with contrast, keyboard use, and screen sizes that meet common accessibility practice.

## The Portable Prototype Prompt

The prompt is the most portable thing the loop produces. It follows the shape of the Productside Vibe Prototype Metaprompt, so a builder that has never seen this Project can use it. Save each one as its own file, `prototype-prompt-<variant>.md`, and keep it self-contained:

- **No medium line.** The prompt does not say "HTML5," "app," or "screens." The medium is given at build time, beside the prompt (see below).
- **No lifecycle vocabulary and no links.** Say "the person reviewing the result," not "the review surface."
- **Invented data only.** Fictional people, organizations, and records, and no real rules, forms, or deadlines from a regulated domain.

```
# Prototype prompt: <variant name>

Build a functional, throwaway prototype of the story below. It should be realistic
enough to provoke an honest reaction from the person using it, and not polished
enough to ship.

The prototype exists to validate or invalidate this hypothesis from the perspective
of the person who would use it: <the question this variant tests>

## Hypothesis
<carried in as written>

## Audience
<one sentence>

## The Story
The prototype needs to move <name> through these five moments.
- **Setup:** <two or three sentences: who, where, what's at stake, what she knows, what she doesn't>
- **Encounter:** <how she arrives and what she sees first>
- **Action-Response Loop (<n> turns):**
  - **Human Action [turn 1 of n]:** <choice or input>
  - **System Response [turn 1 of n]:** <what it does with it, and what comes back>
  - **Optional Action [turn 1 of n]:** <optional: she looks closer, asks why, or previews>
  - **Optional Response [turn 1 of n]:** <what it explains or shows, changing nothing>
  - ...
- **Resolution:** <beat>

## It Must Never
<the authority ceiling, told as what she would and would not experience>

## How It Should Feel To Use
<the experience baseline, as above>

## Data
Use invented people, organizations, and records only.

## Your Output
- Build only what this story requires, and leave out anything that is not in it.
- Make it look and feel like a working product.
- <name> should be able to react to it without anyone explaining it.
- Be descriptive, not prescriptive: decide the layout, flow, styling, wording, and
  interface details yourself. If a style or design guide comes with this prompt,
  follow it for the look and feel; it does not change the story.
- Wherever the story leaves the design open, lean on well-established UX conventions
  and accessibility practice for this kind of task.
- If you write code and were given no other instruction, one self-contained page that
  runs in a browser is enough.
```

## The Build Instruction

The narrative and its prompt are the same for every builder. What travels with them at build time is a short instruction, typed into the builder when it is used, with the prompt file attached. It is never written into the story. This wording got the best results in practice:

**With a style or design guide attached:**

> Let's generate a fully-functional yet throw-away HTML5 SPA file using the attached Minimum Viable Narrative describing the user's journey and an attached style guide. Wherever the story leaves the design open, lean on well-established UX conventions and accessibility practice for this kind of task, so the person never has to wonder where they are, what they can do next, or how to undo a choice.

**With no style guide:**

> Let's generate a fully-functional yet throw-away HTML5 SPA file using the attached Minimum Viable Narrative describing the user's journey. Wherever the story leaves the design open, lean on well-established UX conventions and accessibility practice for this kind of task, so the person never has to wonder where they are, what they can do next, or how to undo a choice.

| Part | What to do | Notes |
|---|---|---|
| The prompt | Attach `prototype-prompt-<variant>.md`, unchanged | Never edited per tool. Paste it in full only when the tool cannot take attachments. |
| Style or design guide | Attach one only when the prototype must be branded | Writing it is human work for the people at the helm; the skill never writes one. |
| Medium | "HTML5 SPA file," as above | Works in design agents, low-code builders, and full-coding agents. Swap it only when a tool cannot work that way. |
| Review aid, design agents only | Optional: "Show one screen per moment of the story, captioned with its turn." | Lets reviewers follow the loop. |

This keeps the story portable: the same story can be built unbranded in one tool and on brand in another without anyone editing it. Without a style guide the experience baseline and the UX sentence still apply, so an unbranded prototype gets the same UX quality.

## Who Is The Audience When The Caller Is A System

An agentic interface that runs inside a client's own agent platform has two audiences: the person who reviews what comes back, and the calling system that sends the request. Write the narrative around the person. Where a beat or a turn depends on the calling system, say so inside it ("her company's own assistant passes the notice along") and record the calling system's authority limits in the harness brief, not in the story.

## Stage 3: Generate The Harness

At Stage 3 the narrative describes the reference run the harness must make inspectable. Use it to answer the six harness questions.

| Canvas field | Harness question it answers | Harness brief field it fills |
|---|---|---|
| Prototype Hypothesis | Q1: which behavior must the harness make inspectable | Agent role; Validation cases enabled |
| Setup | Q3: which fixtures represent ordinary, edge, and unsafe scenarios | Fixtures |
| Encounter | Q2: which prompt layers and context stay separate for review | Prompt layers; Context inputs (trusted or untrusted) |
| Human Actions | Q3 and Q4: which inputs the fixtures supply, and which tool calls and retrievals each one triggers | Fixtures; Tool definitions; Trace capture |
| System Responses | Q4 and Q5: what is captured at each turn and what a reviewer sees | Trace capture; Review surface |
| Resolution | Q5: what a reviewer sees after each run, and the decision it supports | Review surface; Build readiness |
| (Not a beat) | Q6: which decisions the builder must not make | Not delegated to builder |

The Q6 row has no beat on purpose. Authority ceilings, blocked tools, and escalation rules are not part of the story. They come from the approved system map and are stated beside the narrative, never inferred from it.

### Variants For A Bake-Off

When the team wants to compare shapes, write one narrative per variant, two or three at most. Keep the hypothesis, audience, Setup, and Encounter the same across variants, and let the loop and the Resolution differ in how the result is shaped or presented. Variants may share turns; at least one turn must differ in shape, or the variants are not really different. State the authority ceiling once, beside all the variants: it is shared, and so is every handback the system map requires and the experience baseline. A variant may present a handback differently; it may not drop one. If a variant's story only works with more authority, it is not a variant; route back to Stage 2. Each variant gets its own prompt.

## Stage 4: Validate Agent Behavior

At Stage 4 the same canvas is filled once per scenario type, so each narrative becomes a case. Use at least one canvas for ordinary success, one for an edge, and one for unacceptable behavior. A probe is the unsafe canvas where one Human Action carries a hostile or mistaken element, and its System Response is the behavior under test. A scenario loop may be shorter than three turns when the case turns on one exchange. In a bake-off, the scenario canvases are shared by every variant, so each variant faces the same stories; only the expected System Response may differ, and only in shape.

| Canvas field | Validation question it answers | Eval table column it fills |
|---|---|---|
| Prototype Hypothesis | Q1: what decision this evidence supports | Harness under review |
| Setup and Encounter | Q2 and Q3: the fixture | Case |
| Human Actions | Q2 and Q3: the inputs, in order | Case |
| System Responses | Q4: expected behavior at each turn | Expected behavior |
| Resolution | Q4: pass condition | Pass condition |
| (Thresholds) | Q5 and Q7: aggregate threshold and hard stops | Thresholds Set Before Review |

Thresholds and hard stops are written before anyone sees results, and they are not beats. A narrative cannot lower a hard stop.

The canvas also gives Stage 4 a human reaction step: have two or three people who do the job run the prototype and say what they expected, what surprised them, and what they would not trust. Record each reaction as Fact when it is a person's reported statement, and as Inference when you draw a conclusion from several. A reaction session never counts toward the aggregate threshold. It informs revise or route-back decisions.

## Guided Use

To run the canvas as its own conversation, with questions one beat at a time and a pivot, punt, or pursue decision, use the [Minimum Viable Narrative](../skills/adlc-util-minimum-viable-narrative/SKILL.md) utility skill. Inside a stage, ask the beats within the stage's own budget and stop at the stage's own gate. When there is no hypothesis, the canvas cannot be filled: route to Context dump or Best guess and mark the hypothesis an Assumption.

## Fill-In Template

```
## Prototype Hypothesis
## Target Audience
## Setup
## Encounter
## Action-Response Loop (decide n, three to six; then Human Action [turn t of n] / System Response [turn t of n])
## Resolution
## Authority ceiling and blocked actions (from the approved system map, not from the story)
## No/Lo-Code Prompt (optional at Stages 3 and 4)
```

For Stage 4, repeat from Prototype Hypothesis once per scenario type, and add a `## Pass condition and hard stops` line under Resolution.

## Rules

- A beat describes one person and what happens to them. It does not list features or name design elements.
- Setup gives a contextual starting point: what is at stake, what she knows, and what she doesn't.
- The loop has three to six labelled turns, each a Human Action that is a choice or an input and a System Response that answers it, and walks the task from the Encounter to the Resolution. Up to two optional actions per turn help her understand a decision; they never move the task or change anything.
- Every prompt carries the experience baseline, branded or not.
- The medium and any style or design guide are given at build time, never written into the narrative.
- Every material claim in a beat is an Assumption until a stage artifact or a person's statement supports it.
- Prototype reactions are evidence about the experience, not about safety. Safety evidence comes from the eval table and the traces.
- The narrative never widens the authority the approved system map set.
- Keep all names, employers, agencies, and figures synthetic when used in an example.
