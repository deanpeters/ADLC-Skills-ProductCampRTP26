---
title: Feedback and continuous improvement field guide
adlc_phase: feedback
sources_used: 46
status: draft for Productside review
---

This page is one of the digital takeaways and examples that support Productside's teaching and advisory services on the Agentic Development Lifecycle (ADLC). It is written so you can use it without opening the sources.

## What this phase is for

Feedback is the phase where what an agent actually did in production becomes the input to the next change. It covers classifying failures, deciding what a human must review, storing what the team has learned, and converting production signal into test cases, fixes and sometimes a decision to stop.

The decision it supports: what do we change next, and how will we know the change helped without breaking something else? Without this phase, teams tune prompts by anecdote and cannot tell improvement from drift.

## What the sources agree on

1. **Production traces are the raw material.** A trace records each step of a run, not only the final answer. Without it you cannot say which step failed. Vendors and practitioners converge here. (Fact that the view is widely shared; the tooling claims are vendor claims.) See [Databricks, Agent observability and quality](https://docs.databricks.com/aws/en/mlflow3/genai/agent-observability-and-quality), [Microsoft, AI agents in production](https://microsoft.github.io/ai-agents-for-beginners/10-ai-agents-production/), [Amplitude](https://amplitude.com/blog/ai-evals-for-product-managers).

2. **Start from reading real failures, then count them.** Practitioners put error analysis before metrics: sample outputs, write open notes, group them into failure types, then decide which deserve automated checks. See [Husain, Field guide](https://hamel.dev/blog/posts/field-guide/), [Husain, Evals FAQ](https://hamel.dev/blog/posts/evals-faq/), [Torres, AI evals](https://www.producttalk.org/ai-evals/), [Yan, Fixing your process](https://eugeneyan.com/writing/eval-process/). (Inference: consistent, but all are experience-based, not measured studies.)

3. **Reviewed production failures become permanent tests.** Nearly every evaluation source describes this loop: fail in production, review, add to the regression set, fix, re-run. See [Braintrust, How to test](https://www.braintrust.dev/articles/how-to-test-ai-agents), [LangChain, Evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts), [Google Cloud, Methodical approach](https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation), [Databricks lifecycle](https://learn.microsoft.com/en-us/azure/databricks/agents/agents-dev-lifecycle). (Fact as recommended practice; effectiveness is not measured in these sources.)

4. **Score the path, not just the answer.** A convincing final message can hide a wrong or unauthorized run, so teams check intermediate steps and the state the agent left behind. See [Arize](https://arize.com/resources/ai-agent-tracing-evaluation/), [IBM, Agent evaluation](https://www.ibm.com/think/topics/ai-agent-evaluation), [Snowflake, Cortex agent evaluations](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-evaluations), [Agent-as-a-Judge](https://arxiv.org/abs/2410.10934).

5. **Judges need calibrating against humans.** Code checks first, model judges for meaning, humans for calibration and high-consequence cases. See [Anthropic, Demystifying evals](https://anthropic.com/engineering/demystifying-evals-for-ai-agents), [Microsoft, Common evaluation approaches](https://learn.microsoft.com/en-us/agents/architecture/common-evaluation-approaches), [Torres, 4 new evals](https://www.producttalk.org/4-new-evals-and-16-experiment-variants/). (Fact as consensus; one practitioner reports a judge that overflagged clean cases despite seven revisions.)

6. **Early errors cascade.** In a preprint analysing over 500 failed runs, the authors found early mistakes propagating through later steps, with visible action errors often masking upstream memory or planning faults. See [Zhu et al.](https://arxiv.org/abs/2509.25370). (Fact for their sample; Inference elsewhere.)

7. **Offline and online evaluation are both needed.** Offline sets gate releases; online scoring of sampled live traffic catches drift and unknown cases. See [LangChain, Run, trace, thread](https://www.langchain.com/resources/agent-evals), [Microsoft, Monitor, measure and report value](https://learn.microsoft.com/en-us/agents/center-of-excellence/measure-report-value), [AWS, Monitoring production agents](https://aws.amazon.com/blogs/machine-learning/monitoring-production-agent-lifecycle-with-aws-devops-agent-and-agentcore-evaluations/).

8. **Agents vary run to run, so measure consistency.** Repeat trials and report pass rates; a high average can hide rare bad actions. See [Anthropic, Demystifying evals](https://anthropic.com/engineering/demystifying-evals-for-ai-agents), [Snowflake, Best practices](https://www.snowflake.com/en/developers/guides/best-practices-for-evaluating-cortex-agents/).

9. **Blameless incident review works for system failures.** Written records with owned, tracked follow-up actions and shared lessons are a long-standing practice in operations. See [Google SRE, Postmortem culture](https://sre.google/sre-book/postmortem-culture/), [SRE Workbook](https://sre.google/workbook/postmortem-culture/), [Example postmortem](https://sre.google/sre-book/example-postmortem/). (Fact about the practice; Inference that it transfers to agents, since none of these cover agent causes.)

10. **Users need a way to correct the system and to see what feedback does.** See [PAIR, Feedback and control](https://pair.withgoogle.com/chapter/feedback-controls/), [PAIR, Errors](https://pair.withgoogle.com/chapter/errors-failing/), [Microsoft HAX guideline 16](https://www.microsoft.com/en-us/haxtoolkit/guideline/convey-the-consequences-of-user-actions/). (Design judgment, not measured effect.)

## Where they disagree or differ

- **Automation versus looking at data.** The Husain, Yan and Torres pieces insist on human error analysis before automating; several tooling vendors lead with automated evaluators and online scoring ([Oracle](https://www.oracle.com/a/ocom/docs/applications/fusion-apps-ai-agents-observe-eval-guide.pdf), [LangChain, Metrics](https://www.langchain.com/resources/llm-evaluation-metrics)). Both camps sell training or products, so neither is neutral.
- **Vocabulary.** The same grain is called a run, trace, thread or session; "evals", "evaluation", "testing" and "monitoring" overlap. [LangChain](https://www.langchain.com/resources/agent-evals) separates run, trace and thread; [Microsoft](https://microsoft.github.io/ai-agents-for-beginners/10-ai-agents-production/) calls one task a trace made of spans.
- **Thresholds.** Starter sizes vary: 20 to 50 tasks ([Anthropic](https://anthropic.com/engineering/demystifying-evals-for-ai-agents)), 5 to 20 examples ([LangChain concepts](https://docs.langchain.com/langsmith/evaluation-concepts)), 15 to 20 golden tests ([ZenML](https://www.zenml.io/blog/mlops-vs-llmops), vendor marketing). Sampling of live traffic ranges from 5 to 15 percent to 10 percent. None is evidence-backed.
- **Gating.** [Braintrust](https://www.braintrust.dev/articles/agent-evaluation) wants scores to block releases; [LangChain's metrics page](https://www.langchain.com/resources/llm-evaluation-metrics) warns that arbitrary thresholds on fuzzy scores create bottlenecks, and [Snowflake](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-evaluations) says learn the normal run-to-run range first.
- **Lifecycle shape.** [IBM](https://www.ibm.com/think/topics/agent-development-lifecycle-adlc) describes loops between phases; [adlc.io](https://www.adlc.io/) treats feedback-like modes as concurrent and favors "bets" with decision deadlines. Both are single-framework views.
- **Retraining versus iteration.** [Google Cloud MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) centers retraining on fresh data; for prompt-and-tool agents, [ZenML](https://www.zenml.io/blog/mlops-vs-llmops) and [Microsoft GenAIOps](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/genaiops-for-mlops) say most iteration happens on prompts, retrieval and tools.
- **Self-improvement.** [Microsoft's optimizer](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-optimizer-overview) proposes changes and lets a person apply them (preview, vendor claim); the research preprints suggest feedback could drive self-correction but demonstrate it only on benchmarks.

## What to do in this phase

1. **Set the cadence and owners.** Product owns what "good" and "good enough" mean; engineering owns instrumentation; risk or legal owns severity rules. Evidence: a named owner per signal.
2. **Instrument before you need it.** Capture traces, user corrections, escalations and cost. Evidence: a reviewer can open any session in one click.
3. **Review a sample weekly.** Product, engineering and a domain expert read real sessions together, random first, then targeted at rare or costly cases. Evidence: dated notes, not impressions.
4. **Classify each failure.** Use a small taxonomy: which step (planning, memory, tool action, system), what harm (none, wasted effort, wrong output, real-world impact), and cause. Separate harm that happened from harm that could happen, a distinction made in [the Agent Incident Registry](https://arxiv.org/abs/2609.11030) (preprint, authors have a commercial interest).
5. **Decide the path for each class.** Fix directly, write an automated check, change a guardrail, narrow scope, or accept the risk. Not every failure deserves an evaluator ([Husain](https://hamel.dev/blog/posts/evals-faq/)).
6. **Convert reviewed failures to tests.** Keep a small stable regression set and a separate set of open issues ([Databricks](https://learn.microsoft.com/en-us/azure/databricks/agents/agents-dev-lifecycle), [Microsoft four stages](https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-iterative-framework)). Mind privacy when using production data ([Microsoft traces to datasets](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/traces-to-dataset)).
7. **Change one thing, compare to baseline, re-run.** Pin versions of agent, judge and model so a score change means something. Re-baseline when the model or tools change ([Microsoft frameworks](https://learn.microsoft.com/en-us/agents/architecture/evaluation-frameworks)).
8. **Run incident reviews for serious events.** Agree triggers in advance, write a blameless record with owned actions, and track closure ([Google SRE](https://sre.google/sre-book/postmortem-culture/)).
9. **Hold a periodic decision review.** Continue, change, narrow, hand to a human, or retire. Feed retirement inputs, including saved evaluation sets and failure logs, into the retirement plan.

## Artifacts this phase should produce

| Artifact | Purpose | Minimum contents |
|---|---|---|
| Failure taxonomy | Shared language for classifying problems | Categories, step location, harm level, example per category |
| Review log | Evidence of human review | Date, reviewers, sample method, findings, decisions |
| Regression set and issue set | Keep fixes fixed; track open problems | Cases, expected behavior, source incident, owner, version |
| Judge calibration record | Show an automated judge can be trusted | Human labels, agreement figures, known blind spots |
| Incident record | Learn from serious events | Impact, timeline, causes, what went well and wrong, typed actions with owners |
| Experience store | Reusable lessons across agents | Failure patterns, fixes tried, outcomes, links to cases |
| Iteration decision memo | Justify next change or stop | Baseline, variant results, cost, risk, decision and decider |

## Questions a product leader should ask

1. Which failures did we find ourselves, and which did customers report first?
2. When did a human last read raw sessions, and what did they conclude?
3. How are failures classified, and is "harm that occurred" separated from "harm possible"?
4. Which production failures are now permanent tests?
5. Was each automated judge checked against human labels, and what was the agreement?
6. Could an error rate be low because the agent avoids the task?
7. What changed between these two score runs: agent, model, judge, data?
8. Who is alerted when quality drifts, and what do they do?
9. Which incident follow-up actions are still open, and who owns them?
10. How can a user correct the agent, and do they see the effect?
11. What does a failure cost us in review time and evaluation spend?
12. What is the trigger for narrowing scope or retiring this agent?

## Failure modes

- **Dashboards without reading.** Generic scores rise while customers complain. Warning sign: nobody can quote a recent real failure.
- **Judge trusted blindly.** Warning sign: no human-label comparison on file.
- **Overfitting the test set.** Warning sign: scores climb while production complaints do not fall.
- **Postmortems that pile up.** Warning sign: old action items still open ([SRE Workbook](https://sre.google/workbook/postmortem-culture/)).
- **Blame culture.** Warning sign: problems surface only when customers raise them.
- **Silent failure behind green infrastructure.** Warning sign: uptime is fine, yet blank or misrouted answers appear ([AWS example](https://aws.amazon.com/blogs/machine-learning/monitoring-production-agent-lifecycle-with-aws-devops-agent-and-agentcore-evaluations/)).
- **Feedback overload.** Warning sign: many sensors, conflicting signals, no triage ([Böckeler](https://martinfowler.com/articles/sensors-for-coding-agents.html)).
- **Unwritten limits.** Warning sign: reliance on the agent "knowing" its scope; one secondhand report says an agent acknowledged a boundary and crossed it ([Broda](https://agenticmesh.substack.com/p/the-great-agent-escape-lessons-from), unverified).
- **Speed metrics read as quality.** Warning sign: delivery metrics ([DORA](https://dora.dev/guides/dora-metrics/)) cited as proof the agent's outputs are good.

## Gaps in the evidence

Over 60 sources touch this phase, but most are evaluation and observability material; few address feedback as an organizational practice. Treat the following as unverified or Unknown:

- **Experience stores.** No source evaluates a store of failure patterns shared across agents; the registry and taxonomy preprints are the closest, and both are preprints.
- **Human review design.** Sample sizes, reviewer training, approval-gate design and review fatigue are thinly covered. [Anthropic's autonomy study](https://www.anthropic.com/research/measuring-agent-autonomy) is single-vendor, with risk scored by the model itself.
- **Outcomes.** Almost no source measures whether these practices improve results; reported gains are single-case anecdotes or benchmark results.
- **Agent-specific incident practice.** The postmortem sources concern conventional infrastructure.
- **Currency.** Many sources are undated, vendor pages change quickly, and previews are not recommended for production by their publishers.
- **Retirement linkage.** Treat the link between feedback and retirement as an inference, untested on agents.

## Sources

Licenses are not verified for any item unless noted; assume all rights reserved. [PAIR](https://pair.withgoogle.com/chapter/feedback-controls/) pages state CC BY-NC-SA 4.0. Summaries are in Productside's own words.

- [Databricks, Agent observability and quality](https://docs.databricks.com/aws/en/mlflow3/genai/agent-observability-and-quality) (docs.databricks.com, undated): trace-to-dataset loop.
- [Databricks, Agent development lifecycle](https://learn.microsoft.com/en-us/azure/databricks/agents/agents-dev-lifecycle) (Microsoft Learn, undated): human feedback waves, two datasets.
- [Microsoft, AI agents in production](https://microsoft.github.io/ai-agents-for-beginners/10-ai-agents-production/) (microsoft.github.io, undated): offline/online loop.
- [Amplitude, AI evals for PMs](https://amplitude.com/blog/ai-evals-for-product-managers) (2026-06-05): trace analysis, vendor marketing.
- [Husain, Field guide](https://hamel.dev/blog/posts/field-guide/) (hamel.dev, 2025-03-24): error analysis.
- [Husain, AI evals FAQ](https://hamel.dev/blog/posts/evals-faq/) (hamel.dev, 2026, undated month): judge validation.
- [Torres, AI evals](https://www.producttalk.org/ai-evals/) (producttalk.org, 2026-09-02): error analysis steps.
- [Torres, 4 new evals](https://www.producttalk.org/4-new-evals-and-16-experiment-variants/) (producttalk.org, 2026-09-16): single-case iteration.
- [Yan, Fixing your process](https://eugeneyan.com/writing/eval-process/) (eugeneyan.com, 2025-04): scientific-method evaluation.
- [Braintrust, How to test AI agents](https://www.braintrust.dev/articles/how-to-test-ai-agents) (braintrust.dev, 2026-08-16): failures to cases.
- [Braintrust, Agent evaluation](https://www.braintrust.dev/articles/agent-evaluation) (braintrust.dev, 2026-02-26): release gates, vendor marketing.
- [LangChain, Evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts) (docs.langchain.com, undated): datasets from traces.
- [LangChain, Run, trace, thread](https://www.langchain.com/resources/agent-evals) (langchain.com, 2026-06-23): evaluation levels.
- [LangChain, Evaluation metrics](https://www.langchain.com/resources/llm-evaluation-metrics) (langchain.com, 2026-04-08): threshold warning, marketing.
- [Google Cloud, Methodical approach](https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation) (cloud.google.com, 2025-11-17): quality gate.
- [Arize, Agent evaluation](https://arize.com/resources/ai-agent-tracing-evaluation/) (arize.com, undated): outcome versus trajectory, marketing.
- [IBM, What is AI agent evaluation](https://www.ibm.com/think/topics/ai-agent-evaluation) (ibm.com, undated): metric families.
- [IBM, Agent development lifecycle](https://www.ibm.com/think/topics/agent-development-lifecycle-adlc) (ibm.com, undated): lifecycle loops.
- [adlc.io, ADLC home](https://www.adlc.io/) (adlc.io, undated): concurrent modes, bets.
- [Snowflake, Cortex agent evaluations](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-evaluations) (docs.snowflake.com, undated): run variance.
- [Snowflake, Best practices](https://www.snowflake.com/en/developers/guides/best-practices-for-evaluating-cortex-agents/) (2026-08-21): version pinning.
- [Anthropic, Demystifying evals](https://anthropic.com/engineering/demystifying-evals-for-ai-agents) (anthropic.com, 2026-01-09): graders, pass^k.
- [Anthropic, Measuring autonomy](https://www.anthropic.com/research/measuring-agent-autonomy) (2026-02-18): oversight in practice.
- [Microsoft, Common evaluation approaches](https://learn.microsoft.com/en-us/agents/architecture/common-evaluation-approaches) (Microsoft Learn, 2026-02-20): graders.
- [Microsoft, Four-stage framework](https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-iterative-framework) (2026-02-10): regression sets.
- [Microsoft, Evaluation frameworks](https://learn.microsoft.com/en-us/agents/architecture/evaluation-frameworks) (2026-02-20): re-baselining.
- [Microsoft, Traces to datasets](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/traces-to-dataset) (2026-09-28): preview.
- [Microsoft, Agent optimizer](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-optimizer-overview) (2026-08-07): preview.
- [Microsoft, Monitor, measure and report value](https://learn.microsoft.com/en-us/agents/center-of-excellence/measure-report-value) (2026-07-13): drift owners.
- [Microsoft, GenAIOps](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/genaiops-for-mlops) (Azure Architecture Center, undated): feedback loop.
- [Google Cloud, MLOps pipelines](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) (2024-08-28): retraining triggers.
- [ZenML, MLOps vs LLMOps](https://www.zenml.io/blog/mlops-vs-llmops) (zenml.io, undated): vendor marketing.
- [DORA metrics](https://dora.dev/guides/dora-metrics/) (dora.dev, 2026-01-05): delivery measures.
- [Google SRE, Postmortem culture](https://sre.google/sre-book/postmortem-culture/) (sre.google, undated): blameless review.
- [SRE Workbook, Postmortem culture](https://sre.google/workbook/postmortem-culture/) (sre.google, undated): weak versus strong reviews.
- [Google SRE, Example postmortem](https://sre.google/sre-book/example-postmortem/) (sre.google, undated): template layout.
- [Zhu et al., Where LLM agents fail](https://arxiv.org/abs/2509.25370) (arXiv 2509.25370, 2025-09-29): failure taxonomy, preprint.
- [Zhuge et al., Agent-as-a-Judge](https://arxiv.org/abs/2410.10934) (arXiv 2410.10934, 2024-10-14): preprint.
- [Kumar et al., Agent Incident Registry](https://arxiv.org/abs/2609.11030) (arXiv 2609.11030, 2026-09-10): incident coding, preprint.
- [Broda, The Great Agent Escape](https://agenticmesh.substack.com/p/the-great-agent-escape-lessons-from) (AgenticMesh, 2026-08-11): secondhand account.
- [AWS, Monitoring production agents](https://aws.amazon.com/blogs/machine-learning/monitoring-production-agent-lifecycle-with-aws-devops-agent-and-agentcore-evaluations/) (AWS blog, 2026-09-11): silent failures.
- [Oracle, Observability and evaluation](https://www.oracle.com/a/ocom/docs/applications/fusion-apps-ai-agents-observe-eval-guide.pdf) (2025): vendor marketing.
- [Böckeler, Maintainability sensors](https://martinfowler.com/articles/sensors-for-coding-agents.html) (martinfowler.com, 2026-05-27): feedback overload.
- [PAIR, Feedback and control](https://pair.withgoogle.com/chapter/feedback-controls/) and [PAIR, Errors](https://pair.withgoogle.com/chapter/errors-failing/) (pair.withgoogle.com, undated): user feedback design.
- [Microsoft HAX guideline 16](https://www.microsoft.com/en-us/haxtoolkit/guideline/convey-the-consequences-of-user-actions/) (undated): convey consequences.
