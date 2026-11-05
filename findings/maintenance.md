---
title: Maintenance and change field guide
adlc_phase: maintenance
sources_used: 37
status: draft for Productside review
---

This page is one of the digital takeaways and examples that support Productside's teaching and advisory services on the Agentic Development Lifecycle (ADLC). It is written so you can use it without opening the sources.

## What this phase is for

Maintenance is the long middle of an agent's life: after launch and before retirement. Its work is keeping the agent correct, safe and affordable while the things around it keep moving. Prompts get edited, the model underneath is updated or withdrawn, source documents change, connectors break, and users start asking different questions.

The decision it supports: should we make this change, ship it, hold it, or roll it back, and who is accountable for the answer? Teams that treat launch as the finish line discover the agent has quietly gotten worse. Teams that change things casually cannot say whether a change helped.

## What the sources agree on

1. **Agents drift rather than crash.** Quality erodes through stale knowledge, documents edited out of view, shifting user behavior and broken integrations, while answers stay confident. See [Microsoft, Manage the agent lifecycle](https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle), [Salesforce, Well-Architected](https://architect.salesforce.com/docs/architect/well-architected/guide/agentic-enterprise.html), [BCG, Scaling agents](https://www.bcg.com/publications/2026/the-four-pillars-cios-can-use-to-scale-agentic-ai). (Inference: consistent across vendors, but no source measures how often or how fast drift occurs.)

2. **Treat the whole agent as the versioned unit, not only the model.** Prompts, tool descriptions, retrieval content, memory settings, permissions and guardrails all change behavior and all need versions, owners and rollback. See [IBM, Agent lifecycle management](https://www.ibm.com/think/topics/agent-lifecycle-management), [AWS, AgentOps](https://aws.amazon.com/blogs/machine-learning/agentops-operationalize-agentic-ai-at-scale-with-amazon-bedrock-agentcore/), [ZenML](https://www.zenml.io/blog/mlops-vs-llmops), [Microsoft, Foundry lifecycle](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/development-lifecycle). (Fact as stated practice; effect on outcomes is not measured.)

3. **Every meaningful change re-runs the evaluations.** A fixed set of cases, run before release and after any prompt or model change, is the regression check. See [IBM, ADLC](https://www.ibm.com/think/topics/agent-development-lifecycle-adlc), [Microsoft, Foundry lifecycle](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/development-lifecycle), [Xia et al.](https://arxiv.org/abs/2411.13768), [Torres, AI evals](https://www.producttalk.org/ai-evals/). (Fact as recommended practice.)

4. **Test suites alone do not catch drift; sample production too.** Scheduled evaluations and sampled scoring of live traffic detect decay that offline sets miss. See [Microsoft, Monitoring dashboard](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard), [AWS, Monitoring production agents](https://aws.amazon.com/blogs/machine-learning/monitoring-production-agent-lifecycle-with-aws-devops-agent-and-agentcore-evaluations/), [Databricks](https://docs.databricks.com/aws/en/mlflow3/genai/agent-observability-and-quality). (Fact that vendors advise it; their product claims are theirs.)

5. **Record which version produced which behavior.** Snowflake logs the version per turn because one conversation can span versions; Microsoft saves immutable versions for comparison and rollback. See [Snowflake](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-monitor), [Microsoft, Foundry lifecycle](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/development-lifecycle), [Google SRE, Release engineering](https://sre.google/sre-book/release-engineering/). (Fact for those products; mapping "build" to "prompt plus model" is Inference.)

6. **Roll out gradually and keep a way back.** Canary, blue-green or rolling releases, rollback plans and kill switches are named by several sources. See [IBM, ADLC](https://www.ibm.com/think/topics/agent-development-lifecycle-adlc), [IBM, Agent lifecycle management](https://www.ibm.com/think/topics/agent-lifecycle-management), [Salesforce](https://architect.salesforce.com/docs/architect/well-architected/guide/agentic-enterprise.html), [Google SRE, Release engineering](https://sre.google/sre-book/release-engineering/).

7. **Someone must own the agent after launch.** Microsoft's minimum before shipping is a named owner, a monitoring plan and a route to improvement or retirement; EY and BCG ask for inventories with owners and graduation criteria. See [Microsoft, Manage the agent lifecycle](https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle), [EY](https://www.ey.com/en_ca/insights/assurance/technology-risk/six-steps-to-enhance-agentic-ai-governance), [BCG](https://www.bcg.com/publications/2026/the-four-pillars-cios-can-use-to-scale-agentic-ai), [Microsoft, Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents). (Inference that this generalizes beyond large organizations.)

8. **Standards expect continuing monitoring and a record.** The UK code of practice lists maintenance duties such as current patches and watching for unexpected behavior; EU AI Act Articles 9 and 72 require continuous, documented risk and post-market monitoring for high-risk systems; NIST frames its functions as repeating across the lifecycle. See [UK DSIT](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai), [EU Art. 9](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9), [EU Art. 72](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72), [NIST AI RMF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf). (Fact; the EU provisions apply only to high-risk systems, and none is written for agents specifically.)

9. **Long-lived context and connectors are a maintenance surface.** Growing history, too many tool definitions and conflicting instructions degrade results, and upgrades change connector schemas. See [Breunig, How long contexts fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html), [Breunig, How to fix your context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html), [Perrone](https://theaiengineer.substack.com/p/why-ai-agents-keep-failing-in-production), [Osmani, Long-running agents](https://www.oreilly.com/radar/long-running-agents/). (Inference: anecdotal and often small-model evidence.)

10. **Learn from incidents without blame.** Written postmortems with typed, owned actions turn a failure into a change. See [Google SRE, Postmortem culture](https://sre.google/sre-book/postmortem-culture/), [SRE Workbook](https://sre.google/workbook/postmortem-culture/), [Example postmortem](https://sre.google/sre-book/example-postmortem/). (Fact as practice from infrastructure operations; agent adaptation is Inference.)

## Where they disagree or differ

- **Retraining versus prompt-level change.** The ML operations sources (CRISP-ML(Q), Google Cloud, INNOQ, Microsoft's maturity model) center on data drift and retraining triggers. Agents built on hosted models rarely retrain, so ZenML and the Mississippi State survey point to prompts, retrieval and tools as the change surface. See [Google Cloud MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning), [Studer et al.](https://arxiv.org/abs/2003.05155), [Stone et al.](https://arxiv.org/abs/2503.15577).
- **Model versus harness.** Osmani's digest says most gains come from the harness, not the model; Anthropic notes that scaffolding built for one model generation can become dead weight on the next. A model upgrade is therefore a reason to re-test and possibly remove scaffolding, not only to celebrate. See [Osmani, New software lifecycle](https://www.oreilly.com/radar/the-new-software-lifecycle/), [Anthropic, Harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
- **Automation of improvement.** Microsoft's optimizer proposes changes and a person applies one; Wang et al. expect a move toward proactive, online intervention but call it a research direction. Zhang et al. found automated failure attribution identified the failing step only about 14 percent of the time on their dataset, so human review remains necessary. See [Microsoft, Optimizer](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-optimizer-overview), [Wang et al.](https://arxiv.org/abs/2606.01581), [Zhang et al.](https://arxiv.org/abs/2505.00212).
- **Thresholds.** Microsoft suggests investigating below 95 percent success; AWS offers 5 percent error and 3-second P95 latency as starting alarms; Microsoft's optimizer calls a score change under 0.03 noise. Each source calls these illustrative. See [AWS, Optimizing observability](https://aws.amazon.com/blogs/machine-learning/optimizing-production-agents-with-amazon-bedrock-agentcore-observability/).
- **Vocabulary.** "Agent lifecycle management" (IBM), "AgentOps" (IBM, AWS), "operational steady state" (Microsoft), "monitoring and maintenance" (CRISP-ML(Q)) and "ITSM for the ADLC" (BCG) overlap heavily. See [IBM, AgentOps](https://www.ibm.com/think/topics/agentops), [Microsoft, ADLC](https://learn.microsoft.com/en-us/agents/architecture/deployment-lifecycle).
- **Vendor slant.** Platform sources describe controls that their own products provide; consultancies (EY, BCG) argue for governance structures they sell.

## What to do in this phase

1. **Assign ownership.** Name one accountable owner per agent plus a technical steward. Decide who may approve a change and who may stop the agent. Evidence: an inventory entry with owner, version, identity and data sources.
2. **Establish the baseline.** Freeze a representative evaluation set (built from reviewed production failures) and record current scores, cost per task and latency. Decide acceptable tolerances as ranges, since outputs vary.
3. **Version everything that shapes behavior.** Prompts, tool descriptions, retrieval sources, model identifier, settings and permissions. Decide how versions are labeled and logged per request.
4. **Classify changes.** Separate routine edits, model or provider changes, new tools or permissions, and data-source changes. Higher classes need more evidence and wider sign-off, including legal or security review where permissions grow.
5. **Run the change gate.** Re-run the evaluations, compare against baseline on quality, safety, cost and latency, and read a sample of traces by hand. Watch for a lower error count that simply reflects the agent avoiding the task, which Torres reports after a model update.
6. **Release gradually.** Canary or sample a share of traffic, with a rollback path agreed in advance. Check settings that packaged releases may not carry, such as monitoring, authentication and sharing, a pitfall Microsoft documents for its platform.
7. **Monitor and sample.** Combine operational alerts with scheduled evaluations and periodic human trace review. Torres reports reviewing about 60 traces every week or two for one product.
8. **Watch the dependencies.** Track model deprecation notices, connector and schema changes, credential expiry and source-document edits. Plan a migration path before a provider's notice arrives, since forced retirement from model deprecation is a likely first encounter (Hypothesis).
9. **Run incident reviews.** Use a blameless written review with owned, typed actions. For high-risk systems in the EU, check reporting deadlines in Article 73 with counsel.
10. **Review periodically.** Quarterly, decide: continue, change, migrate or retire.

## Artifacts this phase should produce

| Artifact | Purpose | Minimum contents |
|---|---|---|
| Agent inventory entry | Show who owns what is running | Owner, steward, version, model, tools, identity, data sources, risk tier |
| Change log | Tie behavior shifts to changes | Date, what changed, class, evidence reviewed, approver, rollback step |
| Regression evaluation set and baseline | Detect regressions and drift | Cases from real failures, scoring method, tolerances, last results |
| Model upgrade test report | Decide whether to adopt a new model | Side-by-side scores, cost, latency, trace review notes, decision |
| Monitoring and alert plan | Make decay visible | Signals, sampling rate, thresholds as starting points, who is paged |
| Incident review | Convert failures into changes | Impact, timeline, contributing factors, owned actions, what went well |
| Dependency register | Anticipate forced change | Provider versions, deprecation dates, connectors, credential expiry |

## Questions a product leader should ask

1. Who owns this agent today, and what is that person's authority to stop it?
2. What exactly changed since the last release, and where is that recorded?
3. Which model version is serving traffic, and what happens when the provider retires it?
4. When did we last run the full regression set, and does it include recent real failures?
5. Did the error rate fall because behavior improved or because the agent now declines the task?
6. How would we know quality has slipped if no one complained?
7. Can we roll back in minutes, and have we rehearsed it?
8. Which settings, permissions or sources sit outside version control?
9. What did our last incident teach us, and which action items are still open?
10. What does an evaluation run cost, and are we spending it where risk is highest?
11. Which scaffolding exists only to compensate for an older model?
12. Is continuing, changing or retiring this agent a decision we made, or one that happened to us?

## Failure modes

- **Silent prompt edits.** Someone adjusts instructions in a live console. Warning sign: behavior changed and nobody can say when.
- **Upgrade by assumption.** A newer model is swapped in because it scored well elsewhere. Warning sign: no side-by-side run on your own cases.
- **Stale baseline.** The evaluation set never includes new failures. Warning sign: scores stay high while complaints rise.
- **Green dashboards, failing users.** Infrastructure metrics pass while answers are wrong, as AWS illustrates. Warning sign: no quality sampling.
- **Orphaned agent.** The build team disbanded. Warning sign: an inventory entry with no reachable owner.
- **Context creep.** History, tools and rules accumulate. Warning sign: rising token use with flat or falling quality.
- **Unreviewed autonomy in change.** Automated optimizers apply changes without human approval. Warning sign: improvement claims without a held-out set.
- **Post-incident drift.** Reviews are written but actions never close. Warning sign: the same incident type recurs.

## Gaps in the evidence

Fewer than a dozen of the sources are independent of vendors or consultancies, and none is a controlled study of agent maintenance. Treat these as unverified:

- **Unknown:** how often agents drift, how quickly, and which cause dominates. Every drift claim is assertion or anecdote.
- **Unknown:** how much a model upgrade typically changes agent behavior. The best evidence is one practitioner's account.
- **Unknown:** whether any named threshold (95 percent success, 3-second latency, score gains) transfers beyond its source.
- **Unverified:** the results of Torres, Perrone, Breunig and Bockeler are single-author experience, often on small models or one product.
- The MLOps and SRE sources predate agents; applying them is Inference.
- Legal sources cover high-risk systems only, and implementing details may have changed. This page is not legal advice.
- Staffing, budget and cost of ownership for maintenance are barely covered; Osmani's cost crossover figure is illustrative.
- Backward compatibility for agent-to-agent interfaces and shared tools is not addressed by any source in this phase.

## Sources

- [Microsoft, Manage the agent lifecycle](https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle): drift causes, ownership, stages (Microsoft Learn, 2026-07-13; license not verified)
- [Microsoft, Foundry lifecycle](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/development-lifecycle): immutable versions, evaluation after change (2026-08-21; not verified)
- [Microsoft, Agent development lifecycle](https://learn.microsoft.com/en-us/agents/architecture/deployment-lifecycle): operational steady state (2026-07-06; not verified)
- [Microsoft, Monitoring dashboard](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard): scheduled evaluations and alerts (2026-09-25; not verified)
- [Microsoft, Agent optimizer](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-optimizer-overview): human-approved optimization (2026-08-07; not verified)
- [Microsoft, Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents): fleet inventory columns (2026-07-15; not verified)
- [Microsoft, ALM strategy](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/alm): environments, settings not carried (2026-01-16; not verified)
- [Microsoft, Determine operability](https://learn.microsoft.com/en-us/agents/architecture/determine-operability): operability definition (2026-02-19; not verified)
- [IBM, What is the ADLC](https://www.ibm.com/think/topics/agent-development-lifecycle-adlc): CI re-runs, progressive release (undated; not verified)
- [IBM, Agent lifecycle management](https://www.ibm.com/think/topics/agent-lifecycle-management): whole-agent scope, controls (2026-06-23; not verified)
- [IBM, What is AgentOps](https://www.ibm.com/think/topics/agentops): operating discipline definition (undated; not verified)
- [IBM, Deploy agents across the enterprise](https://www.ibm.com/think/topics/ai-agent-deployment): post-launch monitoring list (2026-06-25; not verified)
- [Salesforce, Well-Architected](https://architect.salesforce.com/docs/architect/well-architected/guide/agentic-enterprise.html): drift detection, versioned prompts (undated; not verified)
- [AWS, AgentOps](https://aws.amazon.com/blogs/machine-learning/agentops-operationalize-agentic-ai-at-scale-with-amazon-bedrock-agentcore/): versioned releasable items (2026-06-01; not verified)
- [AWS, Monitoring production agents](https://aws.amazon.com/blogs/machine-learning/monitoring-production-agent-lifecycle-with-aws-devops-agent-and-agentcore-evaluations/): green dashboards, sampled scoring (2026-09-11; not verified)
- [AWS, Optimizing observability](https://aws.amazon.com/blogs/machine-learning/optimizing-production-agents-with-amazon-bedrock-agentcore-observability/): starter alarm thresholds (2026-07-31; not verified)
- [Snowflake, Monitor Cortex Agent requests](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-monitor): version per turn (undated; not verified)
- [Databricks, Observability and quality](https://docs.databricks.com/aws/en/mlflow3/genai/agent-observability-and-quality): trace-to-dataset loop (undated; not verified)
- [Anthropic, Effective harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents): scaffolding tied to a model generation (2025-11-26; not verified)
- [BCG, Scaling agents](https://www.bcg.com/publications/2026/the-four-pillars-cios-can-use-to-scale-agentic-ai): baselines and tolerances (2026-07-14; not verified)
- [EY, Six steps](https://www.ey.com/en_ca/insights/assurance/technology-risk/six-steps-to-enhance-agentic-ai-governance): accountability and inventory (2026-01-23; not verified)
- [Xia et al., Evaluation-driven development](https://arxiv.org/abs/2411.13768): closed loop (arXiv, 2024-11-21; not verified)
- [Zhang et al., Failure attribution](https://arxiv.org/abs/2505.00212): attribution limits (arXiv, 2025-04-30; not verified)
- [Wang et al., Agent system operations](https://arxiv.org/abs/2606.01581): anomaly and resolution taxonomy (arXiv, 2026-06-01; not verified)
- [Torres, AI evals](https://www.producttalk.org/ai-evals/): eval method (Product Talk, 2026-09-02; not verified)
- [Torres, 4 new evals](https://www.producttalk.org/4-new-evals-and-16-experiment-variants/): avoidance after a model update (2026-09-16; not verified)
- [Torres, Building my first AI product](https://www.producttalk.org/ai-playbook/): weekly trace review (2025-08-20; not verified)
- [Perrone, Why agents keep failing](https://theaiengineer.substack.com/p/why-ai-agents-keep-failing-in-production): connector breakage (2026-03-13; not verified)
- [Breunig, How long contexts fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html): context failure modes (2025-06-22; CC BY-NC 4.0 per site footer)
- [Breunig, How to fix your context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html): remedies (2025-06-26; CC BY-NC 4.0 per site footer)
- [Osmani, The new software lifecycle](https://www.oreilly.com/radar/the-new-software-lifecycle/): model versus harness (O'Reilly Radar, 2026-07-15; not verified)
- [Osmani, Long-running agents](https://www.oreilly.com/radar/long-running-agents/): state outside the model (2026-06-08; not verified)
- [Google SRE, Release engineering](https://sre.google/sre-book/release-engineering/): release discipline (undated; not verified)
- [Google SRE, Postmortem culture](https://sre.google/sre-book/postmortem-culture/): blameless reviews (undated; not verified)
- [Google SRE Workbook, Postmortem culture](https://sre.google/workbook/postmortem-culture/): case study, incentives (undated; not verified)
- [Google SRE, Example postmortem](https://sre.google/sre-book/example-postmortem/): template shape (undated; not verified)
- [Google Cloud, MLOps pipelines](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning): retraining triggers (2024-08-28; not verified)
- [Studer et al., CRISP-ML(Q)](https://arxiv.org/abs/2003.05155): monitoring and maintenance phase (arXiv, 2020-03-11; not verified)
- [Stone et al., Navigating MLOps](https://arxiv.org/abs/2503.15577): LLM operations shift (arXiv, 2025-03-19; not verified)
- [ZenML, MLOps vs LLMOps](https://www.zenml.io/blog/mlops-vs-llmops): versioned prompts and golden tests (undated; vendor marketing; not verified)
- [UK DSIT, Code of practice](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai): maintenance provisions (2025-01-31; Open Government Licence v3.0)
- [EU AI Act Article 9](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9): continuous risk management (2024-06-13; not verified)
- [EU AI Act Article 72](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72): post-market monitoring (2024-06-13; not verified)
- [EU AI Act Article 73](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-73): incident reporting deadlines (2024-06-13; not verified)
- [NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf): repeating functions (NIST, 2023-01-26; not verified)
