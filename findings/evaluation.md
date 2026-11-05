---
title: Evaluation and testing field guide
adlc_phase: evaluation
sources_used: 36
status: draft for Productside review
---

This guide is a digital takeaway that supports Productside's teaching and advisory services on the Agentic Development Lifecycle (ADLC). It synthesizes 36 sources. Evidence labels used below: Fact, Inference, Hypothesis, Unknown.

## What this phase is for

Evaluation answers one question before and after every release: how often does this agent do the right thing, on the work our users actually bring, at a cost and risk we accept? It turns "good enough" from an opinion into a measured pass rate against a bar the business chose in advance.

The decision it supports is go, hold or roll back for each change, whether that change is a new agent, a prompt edit, a model swap or a new tool. It also supports a prior decision: whether the requirement is concrete enough to build at all.

## What the sources agree on

1. **Evals are the acceptance criteria for probabilistic features.** Because output varies run to run, the unit of acceptance becomes a pass rate over representative cases, set against a threshold. A written scenario with acceptance criteria that two reviewers would grade identically is the starting point. Label: Inference, but consistent across vendors and practitioners. [Pollick, Evals are the new acceptance criteria](https://rickpollick.com/blog/evals-are-the-new-acceptance-criteria); [Microsoft, iterative evaluation framework](https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-iterative-framework); [Microsoft, evaluation checklist](https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-checklist); [Google ADK](https://google.github.io/adk-docs/evaluate/).

2. **Start small, from real failures.** Twenty to fifty cases drawn from observed problems beat a large synthetic suite built first. These numbers are rules of thumb, not tested thresholds. Label: Inference. [Anthropic, Demystifying evals](https://anthropic.com/engineering/demystifying-evals-for-ai-agents); [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system); [LangChain, run/trace/thread](https://www.langchain.com/resources/agent-evals); [Braintrust, how to test agents](https://www.braintrust.dev/articles/how-to-test-ai-agents).

3. **Error analysis comes before metrics.** Read real outputs and traces, name the failure types, then decide which deserve an automated check. Generic off-the-shelf scores are discouraged. Label: Inference, from practitioners with consulting or training interests. [Husain, AI evals FAQ](https://hamel.dev/blog/posts/evals-faq/); [Torres, AI evals guide](https://www.producttalk.org/ai-evals/); [Yan, fixing your process](https://eugeneyan.com/writing/eval-process/).

4. **Use three grader types and calibrate the middle one.** Code checks are cheap and rigid, model judges are flexible but biased and variable, and humans are the slow reference. Judges should be measured against human labels (agreement, precision, recall) before anyone trusts them, and binary pass/fail beats numeric scales to start. Known judge biases include position and length effects. Label: Fact that the bias studies exist (Yan's survey of them); Inference for the practice. [Anthropic, Demystifying evals](https://anthropic.com/engineering/demystifying-evals-for-ai-agents); [Husain, LLM-as-judge guide](https://hamel.dev/blog/posts/llm-judge/); [Yan, evaluating LLM evaluators](https://eugeneyan.com/writing/llm-evaluators/); [Wolfe, agent evaluation guide](https://cameronrwolfe.substack.com/p/agent-evals); [Microsoft, common approaches](https://learn.microsoft.com/en-us/agents/architecture/common-evaluation-approaches).

5. **Grade the outcome, and also the path.** An agent can claim success without changing the world, or reach a right answer through a risky or wasteful route. Check final state of the environment, then add trajectory checks (tool choice, arguments, order, step count). Do not demand one exact tool sequence, since several can be valid. Label: Inference. [Google Cloud, methodical approach](https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation); [IBM, agent evaluation](https://www.ibm.com/think/topics/ai-agent-evaluation); [Arize, trajectory evals](https://arize.com/docs/ax/evaluate/evaluators/trace-and-session-evals/trace-level-evaluations/agent-trajectory-evaluations); [OpenAI, trace grading](https://developers.openai.com/api/docs/guides/trace-grading); [Chip Huyen, Agents](https://huyenchip.com/2025/01/07/agents.html); [Beyond black-box benchmarking](https://arxiv.org/abs/2503.06745).

6. **Run repeated trials and report rates.** Single runs mislead. Pass-at-least-once and pass-every-time answer different questions, and customer-facing work usually needs the stricter one. Set gates with margin below the target because judge scores themselves wobble. Label: Fact per the authors for judge variability. [Anthropic, Demystifying evals](https://anthropic.com/engineering/demystifying-evals-for-ai-agents); [AWS, GitHub Actions evaluation](https://aws.amazon.com/blogs/machine-learning/automated-agent-evaluation-with-amazon-bedrock-agentcore-and-github-actions/); [Microsoft, common approaches](https://learn.microsoft.com/en-us/agents/architecture/common-evaluation-approaches).

7. **Offline and online evaluation are complements.** Offline sets with known answers gate releases; online scoring of sampled live traffic catches drift and unforeseen queries. Reviewed production failures should become permanent test cases. Label: Inference, widely repeated. [LangChain](https://www.langchain.com/resources/agent-evals); [Microsoft, agents in production](https://microsoft.github.io/ai-agents-for-beginners/10-ai-agents-production/); [Databricks, evaluate and monitor](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor); [Microsoft, traces into datasets](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/traces-to-dataset).

8. **Separate a regression set from a capability set.** The regression set should stay near full marks and block releases on change; the capability set should be hard, and mastered tasks can graduate into regression. Rerun the full suite on triggers such as a model change, new tool or incident. Label: Inference. [Anthropic, Demystifying evals](https://anthropic.com/engineering/demystifying-evals-for-ai-agents); [Microsoft, iterative framework](https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-iterative-framework); [Microsoft, checklist](https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-checklist).

9. **Safety evaluation must be adaptive and reported per risk.** In NIST's hijacking work, attacks tuned to a newer model raised measured success from 11 percent to 81 percent, so a fixed attack list understates risk. Report by attack type, allow retries, and do not average away a rare severe failure. Label: Fact for that experiment; generalizing is Inference. [NIST CAISI, hijacking evaluations](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations); [CSA on NIST red-teaming](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-red-teaming-standards-202603/).

10. **Governance frameworks expect predefined, repeated testing.** The EU AI Act's risk-management article (high-risk systems only) requires metrics and probabilistic thresholds set in advance and testing before release. NIST's framework treats measurement as a recurring function, and its generative AI profile names risks such as confabulation. Label: Fact. [EU AI Act Article 9](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9); [NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf); [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).

## Where they disagree or differ

- **Vocabulary.** Microsoft's "core, variations, architecture, edge cases" sorts tests by purpose; Anthropic's capability versus regression sorts by expected pass rate; LangChain's run, trace and thread sorts by scope. They overlap, so pick one scheme and name it. [Microsoft](https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-iterative-framework); [LangChain](https://www.langchain.com/resources/agent-evals).
- **How much to trust model judges.** Vendor pages (IBM, Google ADK, Arize) present judges as a scalable default and say little about validation. Husain and Yan argue the value lies in the human annotation process and that generic judges mislead. Arize's single correct/incorrect trajectory label is coarse and unvalidated in its own page. [IBM](https://www.ibm.com/think/topics/ai-agent-evaluation); [Arize](https://arize.com/docs/ax/evaluate/evaluators/trace-and-session-evals/trace-level-evaluations/agent-trajectory-evaluations).
- **Who owns it.** Pollick and Anthropic put product and domain staff in charge of cases and rubrics; Husain wants one domain expert, not a committee, and in-house annotation. Product tooling pages assume engineers. [Pollick](https://rickpollick.com/blog/evals-are-the-new-acceptance-criteria); [Husain](https://hamel.dev/blog/posts/llm-judge/).
- **Public benchmarks.** The research papers show what good benchmark design looks like (real tasks, state-based checking, reproducible environments) but their scores are from 2023 and obsolete. They do not predict your workflow's results. [SWE-bench](https://arxiv.org/abs/2310.06770); [WebArena](https://arxiv.org/abs/2307.13854); [AgentBench](https://arxiv.org/abs/2308.03688).
- **Vendor slant.** Every platform source steers toward its own tooling. Salesforce's press release claims a first-of-its-kind testing capability and offers no evidence; treat that as marketing. Anthropic's reported 90 percent gain from multi-agent research rests on an internal evaluation readers cannot inspect. [Salesforce](https://www.salesforce.com/news/press-releases/2024/11/20/agentforce-testing-center-announcement/); [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system).
- **Delivery metrics.** DORA's five measures describe delivery speed and stability, not output quality. Applying "change fail rate" to a prompt change is an adaptation (Inference). [DORA](https://dora.dev/guides/dora-metrics/).

## What to do in this phase

1. **Define success before building.** Product, domain experts and risk write specific success statements and name what the agent must decline. Decide the bar and the cost of false positives versus false negatives. Evidence: signed-off criteria and a stated baseline, even a manual one.
2. **Review real behavior.** Product and a domain expert read a random sample of traces, note errors, and group them. Decide which failure types justify automation. Evidence: categorized failure log.
3. **Build the first set.** Twenty to fifty cases from real work and incidents, plus edge, adversarial and off-topic cases; synthetic cases fill gaps. Fix ambiguous or unsolvable cases. Evidence: dataset with source, expected result and owner.
4. **Choose graders.** Code checks first, judges for semantic qualities, humans for calibration. Measure judge agreement on held-out human labels. Evidence: agreement figures and known disagreement patterns.
5. **Run baseline and iterate.** Several trials per case, fresh isolated environment, stubbed external services. Record agent version, date and pass rate. Evidence: a baseline report with variance.
6. **Add trajectory and safety layers.** Check tool choice, arguments and step count; run adversarial tests with retries and per-attack reporting. Security and risk join here. Evidence: per-risk results.
7. **Set the gate.** Block on release-critical scores (task completion, safety); treat cost and latency as warnings unless limits are agreed. Leadership accepts residual risk explicitly. Evidence: gate policy and a decision record.
8. **Connect to operations.** Sample live traffic, convert reviewed failures into regression cases, and rerun the full suite on triggers. Hand the suites to the observability and feedback phases. Evidence: failure-to-case conversion log.

## Artifacts this phase should produce

| Artifact | Purpose | Minimum contents |
|---|---|---|
| Success criteria sheet | Defines "good enough" | Success statements, declines, thresholds, baseline, owner |
| Failure taxonomy | Directs where to automate | Categories, examples, frequency, severity |
| Golden and regression sets | Repeatable acceptance | Cases, expected results, source, version, graduation rule |
| Grader specification | Makes scoring explainable | Grader type, rubric, human-agreement figures, known biases |
| Baseline and run reports | Compares versions | Agent version, date, trials, pass rate, variance, cost |
| Release gate record | Records the go/no-go | Gate rules, results, accepted residual risk, approver |
| Safety test log | Evidence for risk reviewers | Attack types, attempts, per-type results |

## Questions a product leader should ask

1. What is the written bar, and who agreed to it before the build?
2. Where did the test cases come from, and how many are real failures?
3. What is the pass rate across repeated trials, and how much does it vary?
4. How was each model judge checked against human labels, and by whom?
5. Do we score the final state, the path, or only the reply?
6. Which failures would be unacceptable even if rare, and are they reported separately?
7. What happens to a release when the gate fails, and who can override it?
8. Which events force a full rerun, such as a model, tool or knowledge change?
9. How do production failures become test cases, and how fast?
10. Is the suite saturating, and when did we last add hard cases?
11. Does the agent beat the existing process, or only match it at lower cost?
12. Who reads sampled transcripts each week?

## Failure modes

- **Judge trusted without validation.** Sign: nobody can state judge-to-human agreement.
- **Vague criteria.** Sign: reviewers disagree on pass or fail for the same output.
- **Benchmark substitution.** Sign: a public leaderboard score appears in the launch case instead of your own results.
- **Single-run results.** Sign: scores shift between reruns and nobody is surprised.
- **Outcome-only scoring.** Sign: answers pass while cost, steps or tool use drift upward.
- **Static suite.** Sign: scores near 100 percent while complaints rise.
- **Engineering-only ownership.** Sign: product cannot explain what the cases cover.
- **Averaged safety.** Sign: one headline safety number and no per-risk view.
- **Contaminated runs.** Sign: results depend on test order or leftover state.

## Gaps in the evidence

- No controlled study in the corpus compares evaluation methods or shows that any threshold or sample size works. The 20 to 50 case advice, 10 percent sampling and 0.8 gate are rules of thumb from vendors and practitioners. Unknown.
- Judge reliability is argued from experience and older studies; model-specific numbers have aged. Hypothesis for any given domain.
- Most guidance comes from vendor documentation and individual practitioners, many with training or tooling to sell. Few independent or peer-reviewed sources address agents in product settings.
- Multi-agent, long-horizon and memory-heavy systems have thin coverage; Chip Huyen defers memory evaluation.
- Cost, staffing and time to run a credible suite are barely quantified.
- Survey figures on adoption (for example the LangChain-cited rates) are secondhand and of unknown representativeness.
- The retirement point below is Productside's inference, not a tested practice.

Link to retirement: save evaluation sets and failure logs before an agent is shut down, since they are reusable for the successor, subject to data-handling rules (Inference).

## Sources

All third-party sources: license not verified. Dates are as stated by the sources ("unknown" where not captured).

- [Pollick, Evals Are the New Acceptance Criteria](https://rickpollick.com/blog/evals-are-the-new-acceptance-criteria), Rick Pollick, 2026-06-08, https://rickpollick.com/blog/evals-are-the-new-acceptance-criteria. Evals as definition of done.
- [Husain, Using LLM-as-a-Judge](https://hamel.dev/blog/posts/llm-judge/), Hamel Husain, 2024-10-29, https://hamel.dev/blog/posts/llm-judge/. Expert-aligned judge method.
- [Husain, AI Evals: Everything You Need to Know](https://hamel.dev/blog/posts/evals-faq/), Hamel Husain, 2026, https://hamel.dev/blog/posts/evals-faq/. Error analysis and FAQ.
- [Yan, An LLM-as-Judge Won't Save The Product](https://eugeneyan.com/writing/eval-process/), Eugene Yan, 2025-04, https://eugeneyan.com/writing/eval-process/. Process over judges.
- [Yan, Evaluating LLM-Evaluators](https://eugeneyan.com/writing/llm-evaluators/), Eugene Yan, 2024-08-18, https://eugeneyan.com/writing/llm-evaluators/. Judge styles and biases.
- [Wolfe, Agent Evaluation: A Detailed Guide](https://cameronrwolfe.substack.com/p/agent-evals), Cameron R. Wolfe, 2026-05-18, https://cameronrwolfe.substack.com/p/agent-evals. Vocabulary and layering.
- [Huyen, Agents](https://huyenchip.com/2025/01/07/agents.html), Chip Huyen, 2025-01-07, https://huyenchip.com/2025/01/07/agents.html. Planning and tool failure metrics.
- [Torres, AI Evals: A Hands-On Guide](https://www.producttalk.org/ai-evals/), Teresa Torres, Product Talk, 2026-09-02, https://www.producttalk.org/ai-evals/. PM-oriented steps.
- [Anthropic, Demystifying evals for AI agents](https://anthropic.com/engineering/demystifying-evals-for-ai-agents), Anthropic, 2026-01-09, https://anthropic.com/engineering/demystifying-evals-for-ai-agents. Graders, trials, regression versus capability.
- [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), Anthropic, 2025-06-13, https://www.anthropic.com/engineering/multi-agent-research-system. Small start, rubric judge, human testers.
- [Microsoft, four-stage iterative framework](https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-iterative-framework), Microsoft Learn, 2026-02-10, https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-iterative-framework. Staged test growth.
- [Microsoft, evaluation checklist](https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-checklist), Microsoft Learn, 2026-02-10, https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-checklist. Triggers and categories.
- [Microsoft, common evaluation approaches](https://learn.microsoft.com/en-us/agents/architecture/common-evaluation-approaches), Microsoft Learn, 2026-02-20, https://learn.microsoft.com/en-us/agents/architecture/common-evaluation-approaches. Test generation and graders.
- [Microsoft, traces into datasets](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/traces-to-dataset), Microsoft Learn, 2026-09-28, https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/traces-to-dataset. Production traces as test data (preview).
- [Microsoft, agents in production](https://microsoft.github.io/ai-agents-for-beginners/10-ai-agents-production/), Microsoft, date unknown, https://microsoft.github.io/ai-agents-for-beginners/10-ai-agents-production/. Offline and online loop.
- [IBM, What is AI Agent Evaluation](https://www.ibm.com/think/topics/ai-agent-evaluation), IBM Think, date unknown, https://www.ibm.com/think/topics/ai-agent-evaluation. Metric families.
- [Google Cloud, methodical approach](https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation), Google Cloud (Hugo Selbie), 2025-11-17, https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation. Three pillars and quality gate.
- [Google ADK, Why Evaluate Agents](https://google.github.io/adk-docs/evaluate/), Google, date unknown, https://google.github.io/adk-docs/evaluate/. Response plus trajectory.
- [OpenAI, Trace grading](https://developers.openai.com/api/docs/guides/trace-grading), OpenAI, date unknown, https://developers.openai.com/api/docs/guides/trace-grading. Grading traces.
- [Databricks, Evaluate and monitor agents](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor), Databricks, date unknown, https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor. One scorer definition across dev and production.
- [AWS, automated agent evaluation with GitHub Actions](https://aws.amazon.com/blogs/machine-learning/automated-agent-evaluation-with-amazon-bedrock-agentcore-and-github-actions/), AWS, 2026-09-08, https://aws.amazon.com/blogs/machine-learning/automated-agent-evaluation-with-amazon-bedrock-agentcore-and-github-actions/. Merge gate example.
- [Salesforce, Agentforce Testing Center announcement](https://www.salesforce.com/news/press-releases/2024/11/20/agentforce-testing-center-announcement/), Salesforce, 2024-11-20, https://www.salesforce.com/news/press-releases/2024/11/20/agentforce-testing-center-announcement/. Vendor marketing, claims unverified.
- [LangChain, run/trace/thread evaluation](https://www.langchain.com/resources/agent-evals), LangChain, 2026-06-23, https://www.langchain.com/resources/agent-evals. Evaluation levels and rollout.
- [Braintrust, How to test AI agents](https://www.braintrust.dev/articles/how-to-test-ai-agents), Braintrust, 2026-08-16, https://www.braintrust.dev/articles/how-to-test-ai-agents. Layers and gating.
- [Arize, Agent Trajectory Evaluations](https://arize.com/docs/ax/evaluate/evaluators/trace-and-session-evals/trace-level-evaluations/agent-trajectory-evaluations), Arize, date unknown, https://arize.com/docs/ax/evaluate/evaluators/trace-and-session-evals/trace-level-evaluations/agent-trajectory-evaluations. Trajectory judging.
- [DORA, software delivery performance metrics](https://dora.dev/guides/dora-metrics/), DORA (Google Cloud), 2026-01-05, https://dora.dev/guides/dora-metrics/. Delivery metrics and pitfalls.
- [Beyond Black-Box Benchmarking](https://arxiv.org/abs/2503.06745), IBM Research authors, arXiv, 2025-03-09, https://arxiv.org/abs/2503.06745. Why single scores hide behavior.
- [SWE-bench](https://arxiv.org/abs/2310.06770), Jimenez et al., arXiv, 2023-10-10, https://arxiv.org/abs/2310.06770. Execution-based benchmark design.
- [WebArena](https://arxiv.org/abs/2307.13854), Zhou et al., arXiv, 2023-07-25, https://arxiv.org/abs/2307.13854. Reproducible environment and end-state scoring.
- [AgentBench](https://arxiv.org/abs/2308.03688), Liu et al., arXiv, 2023-08-07, https://arxiv.org/abs/2308.03688. Multi-environment benchmark and failure categories.
- [NIST CAISI, hijacking evaluations](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations), NIST, 2025-01-17, https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations. Adaptive red-team evaluation.
- [CSA on NIST agent red-teaming](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-red-teaming-standards-202603/), Cloud Security Alliance, 2026-03-31, https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-red-teaming-standards-202603/. Secondhand summary, some items draft.
- [NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), NIST, 2023-01-26, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf. Measure function.
- [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), NIST, 2024-07-26, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf. Generative AI risk areas.
- [EU AI Act Article 9](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9), European Commission AI Act Service Desk, 2024-06-13, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9. Predefined testing metrics.
