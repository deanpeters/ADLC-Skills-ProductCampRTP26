---
title: "The ADLC working model: Productside synthesis"
author_or_publisher: Productside
published: 2026-10-01
license: "(c) 2026 280 Group LLC dba Productside; all rights reserved unless the repo LICENSE says otherwise"
adlc_phases: [goal, architecture, tools-context, governance, observability, deployment, evaluation, feedback, maintenance, retirement, fleet-ops]
reliability: productside-synthesis
status: draft for Productside review
---

# The ADLC working model

This page is one of the digital takeaways and examples that support Productside's teaching and advisory services on the Agentic Development Lifecycle (ADLC). It consolidates lifecycle ideas that recur across practitioner books and courses, together with Productside's own teaching experience, into one working model. It restates the ideas in Productside's words and organization. It is **Productside synthesis, not a summary of any single source**, and it does not reproduce anyone's text. Evidence labels: **Practice** (widely repeated practitioner guidance), **Inference** (Productside's reading), **Hypothesis** (plausible, untested).

For what published sources say phase by phase, see the phase guides in this folder.

## 1. A loop, not a line

Practitioner descriptions of the ADLC come in different sizes. Some name seven steps (goal, design, selection, build, optional training, evaluation, monitoring). Others name eight concerns (architecture, development and tools, knowledge and context, security and governance, observability, deployment, evaluation, feedback). A third group adapts the classic systems lifecycle: concept, requirements, design, construction, acceptance, deployment, maintenance, decommissioning.

They agree on the shape more than on the labels:

- The work **repeats**. Production signal feeds the next round of design and prompt changes. **Practice.**
- The concerns **overlap**. Governance, evaluation and observability are built alongside the agent, not added at the end. **Practice.**
- Two areas are genuinely **new** compared with conventional delivery: evaluation (you cannot assert one correct output) and operations (you must watch behavior, not just uptime). **Practice.**

Productside reads the differing phase counts as differences of grain, not of substance. **Inference.**

## 2. Frame the goal as part of the system

In an agent, the goal is not only a business metric. It becomes working material for the agent itself, often in its instructions. So the framing step defines three things together: the objective, the persona or tone, and the **non-negotiable limits**, including what the agent must not do. A simple example: an agent that helps someone book travel may never complete a booking without a final human confirmation. **Practice.**

Before any of that, ask whether an agent is the right answer. Tasks that need exactly repeatable output, or that are simple enough that judgment adds nothing, are better served by conventional automation. Filter them out early. **Practice.**

## 3. Design decisions that set the course

- **Pattern.** Choose among a single reasoning-and-acting agent, a router with specialists, sequential or group workflows, and reflection for quality control. Choose the orchestration style (handoffs, a supervisor, layered planning) deliberately. **Practice.**
- **Context strategy.** Decide how context is assembled, remembered and trimmed before building. **Practice.**
- **Build, buy or platform.** Weigh model quality, cost and speed, framework fit, and which existing interfaces must become tools. Open protocols for tool access and agent-to-agent delegation are worth settling early. **Practice.**
- **Fine-tuning is optional.** For most organizational uses it is unnecessary; good context design usually gets the same result. Treat training as a late, narrow step for a specific style or deeply proprietary knowledge. **Practice; Inference on "most".**
- **Draw the line between judgment and enforcement.** Decide what the model reasons about and what fixed rules enforce. Put anything that must always hold on the enforcement side. **Practice.**

## 4. Knowledge, memory and context

Agents need more than a prompt. Productside finds it useful to separate three kinds of memory: structured domain knowledge (entities and their relationships), semantic retrieval over documents such as policies and guidelines, and a record of what the agent actually did (which steps ran, which tools were called, what came back). The third kind doubles as operational memory and as the raw material for debugging and learning. **Inference**, built on common practitioner patterns.

## 5. Governance built in from the start

Conventional security controls are necessary but not enough. Agent-specific controls include screening inputs before the model sees them, detecting personal data in outputs, role-based permissions on each tool, human approval for high-impact actions, and tamper-evident audit trails. The point of agreement is timing: weave them into the agent's operating path during design, not after launch. **Practice.**

## 6. Observability

Trace every model call: model, tokens, latency, cost, prompt and response, and where it sits in the chain of agents and tools. With traces linked as a tree, diagnosis becomes following a path from the session to the step that returned bad data, instead of guessing. **Practice.**

Track a short set of operating signals: cost per request, wait time, tool-call failure rate, user feedback, and hallucination rate. Watching processor and memory alone misses whether the agent is behaving well. **Practice.**

## 7. Evaluation: the hardest new discipline

- Build a test set of realistic scenarios, on the order of fifty to a hundred to start, drawn from real work and including awkward cases. **Practice; the number is a rule of thumb.**
- Score quality and goal adherence, not exact wording. Use a capable judge model for scale, with human experts for calibration and for what judges miss. **Practice.**
- Evaluate **at each level** of a multi-agent design: faithfulness where workers use sources, hallucination where results are combined, and reasoning quality where decisions are made. **Practice.**
- Keep conventional tests for security controls and connectivity, and test agent-specific failures such as prompt injection. **Practice.**
- Put **regression gates** in the release path against baselines you have calibrated, so changes that lower quality do not ship. **Practice.**
- Automate what can be encoded as acceptance criteria first, then add human quality review for what cannot. **Practice.**

## 8. Deployment

Give each team of agents its own isolated environment with resource limits. Control access through a gateway, authenticate internal traffic in both directions, and manage secrets through the platform rather than storing them in files. Releasing an agent into shared use is the moment it becomes available to users and to other agents, so define who may call it before that point. **Practice.**

## 9. Feedback and improvement

Feedback from operators and users should reach an evaluation pipeline that classifies failures, collects the patterns that worked, and returns them to the agent as worked examples in its instructions. Baselines tighten as the system stabilizes, and the lifecycle returns to design and build for the next iteration. A mature agent is never "done"; it keeps earning trust. **Practice.**

## 10. Scaling beyond single agents

When an organization runs many agents, the unit of management changes.

- **Templates over handcrafting.** Many agents differ only in a few settings (for example, which data source they query). Keep a library of reusable agent templates, and treat the agent's configuration as the unit of work. **Practice.**
- **Certify templates, not every instance.** If the changes a template allows are narrow and cannot alter the kinds of actions the agent takes, approving the template can stand in for approving each variant. This holds only when the permitted variation really cannot affect behavior. **Hypothesis**, with the stated limit.
- **Fleets.** Group related agents so they start and stop together, expose defined input and output channels, share a purpose broad enough to avoid near-duplicate fleets, and report aggregated health and metrics. **Practice.**
- **Fleet shapes.** A hierarchy (one manager, many workers) gives control and predictability and costs speed, which suits regulated or critical work. A swarm (peers with direct links) gives flexibility and speed and costs repeatability. A federation (peer managers, each with its own workers) sits between. Choose by where the work falls on the control-versus-agility spectrum. **Practice.**
- **Assembling a fleet.** Choose the shape, define inputs and outputs, then select agents the way a manager staffs a team: reuse an existing template first, build new only when nothing fits, and start with the agents doing the core work. **Practice.**
- **Fleet-level watching.** At scale nobody can read every agent's logs. Aggregate metrics and health per fleet, and consider observer agents that summarize logs and metrics for the people on call. **Practice; observer agents are Hypothesis in terms of proven value.**
- **Regional or regulatory variants.** A well-built fleet can be copied as a template for a variant that must keep data in a particular region. **Hypothesis.**

## 11. Maintenance and retirement

- **Updates run the same gauntlet** as a new release: the same tests, the same standards. **Practice.**
- **Versions coexist.** Publish a changed fleet or agent as a new version and keep the old one available until dependents have moved. Taking the old version down should be an explicit act. **Practice.**
- **Retire gracefully.** Stop accepting new requests, let in-flight work finish, then shut down, so paid or important work is not cut off midstream. Reserve immediate shutdown for emergencies, such as a compromised agent or work that is clearly stuck. Warn users early and point them to a replacement where one exists. **Practice.**

## 12. Looking ahead (speculative)

Some practitioners expect agents to build and test other agents, groups of fleets to form larger ecosystems, and eventually agent-run business functions with their own legal standing. Treat all of this as **Hypothesis**. It is useful for planning conversations, not for current commitments.

## Further reading

Books and courses that informed this synthesis are listed in [Further reading](bibliography.md).

## How Productside uses this page

- As a bridge between sources that count phases differently, when advising a team that has adopted one vocabulary.
- As the base for the crosswalk of sources onto a single Productside ADLC phase model.
- As a checklist for review conversations: which of these concerns has no owner on your team?
