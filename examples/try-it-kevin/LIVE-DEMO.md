# Live CLI demo: context first, then three skills

Synthetic teaching exercise. Larkspur & Pine, Kevin, and every figure are fictional. This uses the existing story files; no sandbox or model API setup is required beyond your Claude Code access and the installed ADLC plugin.

Open Claude Code at the **repository root**, not inside `kevin-sandbox/`. Use one conversation. The first two skills make a short demo; add the canvas if time permits.

## Set the session context once

```text
We're running a short, synthetic demo for ProductCamp RTP.

Read:
@examples/try-it-kevin/kevin-1-baseline.md
@examples/try-it-kevin/kevin-2-product.md

Kevin, Larkspur & Pine, and every figure are fictional.
The May 2025 canvas is the approved baseline. Later changes
describe what happened; they do not automatically authorize it.

Reuse this context throughout our conversation. Keep facts,
assumptions, and unknowns distinct. Don't invent missing evidence
or make decisions for me.

Briefly confirm what you understand. Don't run a skill yet.
```

## 1. Guided: ask only for what is missing

```text
/adlc:adlc-util-decay-check
Use Guided mode on Kevin. Reuse the context above and ask only
what's missing, one question at a time. Stop for my decision.
```

Use the [suggested fictional replies](TRY-IT.md#1-check-constraint-decay--guided--four-minutes) when asked. One useful live answer:

> Kevin sends replies, issues credits under $25, and offers coupons up to 30 percent. An October trace shows address changes nobody approved.

If asked for evidence, explain that the fixture change log is supplied but the dashboard and trace sample are assumed fictional exercise inputs. Do not pretend to have attached actual evidence. Choose a decision at the gate before moving on.

## 2. Context dump: reuse the story

```text
/adlc:adlc-util-plc-check
Use Context dump mode. Reuse everything we just learned about Kevin
and the product's numbers you already read.
Has the product changed enough that Kevin's job should change too?
Keep unknowns visible and stop for my decision.
```

## 3. Best guess: draft a new idea

```text
/adlc:adlc-util-agent-strategy-canvas
Use Best guess mode for a new fictional idea:
an agent that drafts weekly customer-feedback summaries for a
Product Manager, who reviews every draft before sharing it.
Do not carry Kevin's company or numbers into this new example.
Draft the nine boxes, label assumptions and unknowns, and stop
for my pivot, punt, or pursue decision.
```

Connecting line: **“Guided asks. Context dump reuses. Best guess drafts. In every case, I still decide.”**
