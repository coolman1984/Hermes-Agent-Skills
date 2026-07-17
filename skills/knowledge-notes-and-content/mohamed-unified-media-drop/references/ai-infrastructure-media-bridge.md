# AI Infrastructure Media Bridge

Use this reference when Mohamed sends media about model serving, local LLM hardware, inference engines, quantization, GPU memory, GPU clusters, self-hosting, or AI infrastructure choices.

## Durable handling pattern

1. Treat the source as a decision lens first, not as a buying/building trigger.
2. Extract the author's engine/hardware recommendations faithfully, but separate them from Mohamed-facing application.
3. Enrich with 3-7 primary or high-trust sources from official docs, repositories, or vendor pages for the named tools.
4. Convert the source into a compact evaluation template when it affects Mohamed's agent OS, knowledge engine, market workflow, or company-reporting system.
5. Create an Intelligence Vault bridge if the source helps decide build-vs-buy, local-vs-cloud, serving architecture, privacy, cost, latency, or product/service positioning.
6. Do not promote it into a new standalone infrastructure project unless Mohamed already has a concrete workload, customer, benchmark target, or purchase decision.

## Mohamed-specific application

For local/self-hosted LLM infrastructure, the useful output is usually a small decision card:

- actual hardware available
- target model and size
- context length
- concurrency/users/agents
- workload shape: long input, long output, structured output, repeated prefixes
- privacy constraint
- production vs personal use
- candidate engines to benchmark
- benchmark metrics: first-token latency, per-token latency, memory headroom, throughput, p95/p99 latency, cost per useful run

## Pitfalls

- Do not turn every AI-infra post into a shopping list.
- Do not choose an inference engine from popularity alone; tie it to hardware, workload, and serving model.
- Do not treat a local demo server as production without discussing security, observability, backpressure, routing, and failure behavior.
- Do not overfit one author's opinionated ranking; label it as source opinion and verify tool capabilities against official docs when possible.

## Recommended executive classification

Most such sources should be classified as: save and attach to an existing project.

Only classify as act now when there is a current workload ready to benchmark or an imminent purchase/deployment decision.