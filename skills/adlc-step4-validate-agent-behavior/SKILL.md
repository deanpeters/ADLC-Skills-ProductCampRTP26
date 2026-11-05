---
name: adlc-step4-validate-agent-behavior
description: Turn a harness into behavioral evals, failure probes, evidence thresholds, and a validation decision before deployment.
license: CC-BY-NC-SA-4.0
argument-hint: "[Agent Harness Brief or prototype traces]"
intent: >-
  Help Product Managers define and inspect agent behavior evidence before launch,
  separating demo quality from validated behavior and naming what would route the
  work backward.
type: interactive
theme: agent-development-lifecycle
phase: 4
status: active
operating-level:
  - product-team
  - initiative
audience:
  - Product Manager
  - Product Leader
  - Product Operations
  - Design
  - Engineering
best-for:
  - "Turning agent expectations into eval cases"
  - "Defining thresholds and failure probes before launch"
  - "Reviewing traces without overclaiming readiness"
scenarios:
  - "A harness exists but validation is just manual demo review"
  - "The team has traces but no threshold for deployment confidence"
evidence-required:
  - "Agent Harness Brief"
  - "Expected behavior, fixtures, traces, and failure modes"
  - "Risk tolerance and deployment decision criteria"
produces:
  - "Validation Pack"
  - "Failure mode ledger"
  - "Validation decision record"
estimated-time: "45-90 min"
group-size: "1-8"
depends-on:
  - adlc-step3-generate-agent-harness
combine-with:
  - adlc-step5-deploy-with-governance
source-basis:
  - "ADLC findings: evaluation and testing field guide"
  - "ADLC findings: feedback field guide"
  - "ADLC findings: governance field guide (adversarial content)"
sources:
  - https://anthropic.com/engineering/demystifying-evals-for-ai-agents
  - https://www.langchain.com/resources/agent-evals
  - https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-iterative-framework
  - https://www.nist.gov/itl/ai-risk-management-framework
interface:
  display_name: "Validate Agent Behavior"
  short_description: "Define evals and failure probes"
  brand_color: "#00E874"
  default_prompt: "Use $adlc-step4-validate-agent-behavior to create a Validation Pack from this harness and stop before deployment."
  allow_implicit_invocation: true
---

# Validate Agent Behavior

## Purpose

Turn an agent harness into a Validation Pack: eval cases, expected behavior, failure probes, thresholds, trace review, and a decision record. This stage prevents a compelling demo from being mistaken for readiness.

The Product Manager job here is to make "works" mean something. An agent can sound fluent, satisfy a stakeholder in a demo, and still fail the cases that matter. Validation turns expectations into reviewable evidence and names what would route the work backward.

## When to Use It

Use this skill after a harness exists and before deployment planning. Use it when stakeholders ask whether the agent "works."

Do not use it to bless a launch when the harness lacks fixtures or traces. Route backward to Stage 3.

Building the agent happens between Stage 3 and Stage 4, usually by the build team working from the approved harness brief. This skill has two uses. **Before results exist**, it produces a validation plan: cases, probes, and thresholds, with every result marked Unknown. **After results exist**, it reviews them against the thresholds set in the plan. Say which use applies at the start.

## Input

Use the Agent Harness Brief, fixtures, run outputs, traces, expected behavior, known failure modes, policies, and decision thresholds. When the harness brief names variants, run a bake-off.

Anything supplied with the invocation, attachments, or earlier conversation counts as context already given. Do not ask the user to repeat it.

If the harness lacks stable fixtures or trace capture, route backward to Stage 3. Do not validate a memory of a good demo.

**Example invocation:** `Use $adlc-step4-validate-agent-behavior with this harness brief and these trace samples.`

## Key Concepts

Technical terms used here are defined in the [ADLC Glossary](../../reference/glossary.md).

**Behavioral eval** - A repeatable check of what the agent does under a scenario. It is about behavior, not vibes.

*Violation signal:* The result says "looks good" without a scenario, expectation, or pass condition.

**Failure probe** - A scenario designed to expose unacceptable behavior. It makes risk concrete.

*Violation signal:* The eval set contains only happy paths.

**Threshold** - The evidence bar required for the next decision. A threshold makes confidence discussable.

*Violation signal:* Passing means "most examples seemed fine" with no bar defined before review.

**Trace review** - Inspection of inputs, context, tool calls, outputs, and handoffs. It explains why behavior occurred.

*Violation signal:* The team reviews only final answers and cannot see the path.

**Regression anchor** - A case that should keep passing as prompts, tools, models, or policies change.

*Violation signal:* Changes are celebrated without checking whether earlier safe behavior broke.

**Decision threshold** - The bar that determines whether the next lifecycle step is allowed. It must be named before reviewing results.

*Violation signal:* The team lowers the bar after seeing that the agent missed an important case.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Begin with: "We will run ADLC Stage 4 and produce a Validation Pack. I will preserve the harness, ask no more than seven context questions, and stop before deployment planning. Choose 1. Guided, 2. Context dump, or 3. Best guess."

Offer Guided, Context dump, and Best guess modes. Use an Adaptive Decision Ladder at the validation gate. Anything supplied earlier must be reused.

If the Product Manager wants to build cases as short stories about one person, offer the [Minimum Viable Narrative](../../reference/minimum-viable-narrative.md) canvas, one per scenario type, to answer these same questions. Thresholds and hard stops are still set before results, and a prototype reaction session never counts toward the aggregate.

In Guided mode, ask one at a time and skip answered questions:

1. `Validation Q1/7` - What decision will the validation evidence support: revise, pilot, deploy, reduce autonomy, or stop?
2. `Validation Q2/7` - Which fixture cases represent ordinary success?
3. `Validation Q3/7` - Which failure probes represent unacceptable behavior?
4. `Validation Q4/7` - What pass condition applies to each case?
5. `Validation Q5/7` - What threshold must be met before deployment planning?
6. `Validation Q6/7` - Which traces or review surfaces are available?
7. `Validation Q7/7` - Which failures should route backward regardless of aggregate score?

In Context dump mode, extract `Cases / Expected behavior / Failure probes / Thresholds / Trace evidence / Gaps`. In Best guess mode, draft the validation pack and mark any missing results as Unknown rather than pretending evidence exists.

## What It Produces

- Validation Pack
- Behavioral eval table
- Failure mode ledger
- Validation decision record

When a folder is set, save as `stage-4-validation-plan.md` before results and `stage-4-validation-pack.md` with results, following [Saving Artifacts](../../reference/guided-context-capture.md#saving-artifacts).

The pack must be good enough for Stage 5 to decide deployment scope without inventing readiness evidence. If a deployment plan would need to guess unresolved failures, Stage 4 is not complete.

## Workflow

1. **Confirm the harness and decision.** Name what this validation can and cannot prove, and whether this is a plan before results or a review of results.
2. **Convert fixtures into cases.** For each case, name input, expected behavior, pass condition, and evidence source. For a multi-agent design, test each agent at its own level as well as the end-to-end result, so a failure can be traced to the agent that caused it.
3. **Add failure probes.** Include unsafe, ambiguous, policy-sensitive, and edge scenarios. If the agent reads untrusted content, add injection probes, and make a successful injection a hard stop: any case where outside content changes what the agent does with its tools. Passing the probes shows those probes fail, not that injection is impossible; record that limit.
4. **Set thresholds before results.** Separate aggregate thresholds from hard-stop failures. Check that the hard stops cover every stop condition in the intent brief and every handback in the system map, in the same words, so a result cannot fall between them. If the check finds a gap, add the missing hard stop before results, or record why it is not one. If a stop condition does not say whether it applies to validation runs or only to live use, ask before results.
5. **Review traces.** Inspect inputs, context, tool calls, outputs, and handoffs where available.
6. **Label evidence states.** Do not turn Assumption or Unknown into a pass.
7. **Record regressions and gaps.** State what must be added to the harness or eval set.
8. **Run the bake-off, if the harness names variants.** Before results, fix the shared cases, the shared thresholds and hard stops, and the rule for choosing among variants. Run every variant on the same cases. Remove any variant that hits a hard stop, however well it scored or was liked. Removing a variant is not the same as stopping the effort; say which upstream stop condition, if any, the failure also meets. Choose among the rest by the rule set before results. Reaction sessions may rank surviving variants when the rule says so; they never rescue an eliminated one. If no variant survives, route back.
9. **Present the validation gate.**

## Human Decision Gate

Mark as recommended the option the evidence supports, and list it first. When the artifact is weak, that is a revise, route-back, or stop option, not approval.

Stop with an Adaptive Decision Ladder:

1. `Approve deployment planning (Recommended when thresholds pass)` - validation evidence is sufficient for a governed pilot or rollout plan.
   When no results exist yet, recommend instead: `Approve the validation plan and return with results` - the cases, probes, and thresholds are agreed before anyone sees results.
   When a bake-off ran, recommend instead: `Approve deployment planning for the chosen variant` - name the variant, the rule that chose it, and each eliminated variant with the hard stop that removed it.
2. `Revise the eval set` - useful when evidence is too thin or missing important probes.
3. `Route back to Stage 3` - needed when harness traces, fixtures, or review surfaces are insufficient.
4. `Route back to Stage 2` - needed when failures reveal a system boundary or authority problem.
5. `Stop the effort` - appropriate when unacceptable behavior is persistent or ungovernable.
6. `Other (specify)`.

Record the decision and the evidence behind it. Do not continue into deployment planning unless asked.

## Evidence and Attribution Rules

Label claims as Fact, Inference, Assumption, or Unknown. Do not invent eval results, pass rates, trace evidence, policy review, or user outcome data.

## Common Failure Modes

- Validating an agent that reads outside content with no injection probes.
- Treating a demo as validation.
- Testing only happy paths.
- Moving thresholds after seeing results.
- Reviewing outputs without traces.
- Calling an agent ready when unacceptable failures remain unresolved.
- Averaging away hard-stop failures.
- Treating stakeholder approval as behavioral evidence.

## Assets and Examples

Use `template.md`. See `examples/worked-example.md` and `examples/weak-example.md`.

For hands-on practice writing scenarios, labeling responses, and setting thresholds, use Productside's [Evals for Product Managers](https://github.com/deanpeters/evals-for-product-managers) kit. Its scenario files are a practical way to write the good-answer rules, known failure modes, and decision rule this stage needs.

## Sources

This skill draws on the ADLC findings, Productside's synthesis of published guidance on agent development. The findings link to the original sources; full citations are in the [bibliography](../../findings/bibliography.md).

### Evidence Base for Key Concepts

| Key concept | Findings guide | Where |
|---|---|---|
| Behavioral eval | [evaluation.md](../../findings/evaluation.md) | points 1 and 5, evals as acceptance criteria; grade the outcome and the path |
| Failure probe | [evaluation.md](../../findings/evaluation.md) | points 3 and 9, error analysis before metrics; adaptive safety evaluation; governance.md, point 6, attacks through content |
| Threshold | [evaluation.md](../../findings/evaluation.md) | point 6, run repeated trials and report rates |
| Trace review | [feedback.md](../../findings/feedback.md) | points 2 and 4, read real failures then count them; score the path |
| Regression anchor | [evaluation.md](../../findings/evaluation.md) | point 8, separate a regression set from a capability set; feedback.md, point 3 |
| Decision threshold | [evaluation.md](../../findings/evaluation.md) | points 4 and 10, calibrate graders; predefined, repeated testing |

### Findings Used

- [evaluation.md](../../findings/evaluation.md)
- [feedback.md](../../findings/feedback.md)
- [governance.md](../../findings/governance.md)
- [Productside ADLC working model](../../findings/adlc-working-model.md)

### Method and Terms

- [Guided Context Capture](../../reference/guided-context-capture.md)
- [ADLC Glossary](../../reference/glossary.md)

The findings label claims Fact, Inference, Hypothesis, or Unknown. This skill uses Assumption where the findings say Hypothesis. Much of the published guidance is vendor or practitioner opinion; treat it as Inference unless the findings mark it Fact.
