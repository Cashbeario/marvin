# SDD.md — Software Design Document
MARVIN: Multi-Agent Reasoning and Virtualized Intelligence Network
Aether Neural — AGI Cognition Engine v3.0

"We are born with many mental resources. We learn from interacting with others.
Emotions are different Ways to Think."
— Marvin Minsky, Society of Mind

---

### Table of Contents
1. [System Overview](#1-system-overview)
2. [Architectural Philosophy](#2-architectural-philosophy)
3. [Core Architectural Layers](#3-core-architectural-layers)
4. [Cognitive Workspace Architecture (CWA)](#4-cognitive-workspace-architecture-cwa)
5. [Sovereign Domain Mesh](#5-sovereign-domain-mesh)
6. [Tribe v2 Model Integration](#6-tribe-v2-model-integration)
7. [MoMoA — Mixture of Multi-Agent Architecture](#7-momoa-mixture-of-multi-agent-architecture)
8. [Agent Taxonomy](#8-agent-taxonomy)
9. [Cognitive Function Mapping](#9-cognitive-function-mapping)
10. [NATS JetStream Orchestration Harness](#10-nats-jetstream-orchestration-harness)
11. [MCP Host / Server Architecture](#11-mcp-host--server-architecture)
12. [Memory Architecture](#12-memory-architecture)
13. [Ignition Engine — Attention & Selection](#13-ignition-engine--attention--selection)
14. [LLM Council](#14-llm-council)
15. [Self-Improvement & Observation Agent](#15-self-improvement--observation-agent)
16. [AutoResearch Agent (ARA)](#16-autoresearch-agent-ara)
17. [System of Record](#17-system-of-record)
18. [Backup & Resilience Architecture](#18-backup--resilience-architecture)
19. [Data Flows & Sequence Diagrams](#19-data-flows--sequence-diagrams)
20. [API & Interface Contracts](#20-api--interface-contracts)
21. [Security & Sovereignty Model](#21-security--sovereignty-model)
22. [Deployment Architecture](#22-deployment-architecture)
23. [Configuration Reference](#23-configuration-reference)
24. [Open Problems & Solutions](#24-open-problems--solutions)
25. [Implementation Roadmap](#25-implementation-roadmap)
26. [Operational Runbooks](#26-operational-runbooks)
27. [Metrics & Observability](#27-metrics--observability)
28. [Glossary](#28-glossary)
29. [References](#29-references)
30. [Appendices](#30-appendices)

---

### 1. System Overview
MARVIN is a brain-inspired, fully autonomous, self-improving multi-agent AGI framework. It combines five foundational architectures into a unified sovereign intelligence harness:

| Framework Role | Component |
| :--- | :--- |
| **CWA (Cognitive Workspace Architecture)** | Global attention-gated workspace for agent coordination |
| **MoMoA (Mixture of Multi-Agent Architecture)** | Task-level orchestration via heterogeneous agent ensembles |
| **Society of Mind / MoA** | Emergent cognition from competitive specialist collaboration |
| **Sovereign Domain Mesh** | Federated ownership, data sovereignty, and inter-node routing |
| **Tribe v2 Model Integration** | Team identity, role inheritance, and cross-tribe communication protocol |

MARVIN operates autonomously, using the user’s vision as its north star. It achieves goals through:
* **Parallel Teams** — multiple specialized agent teams running concurrently
* **LLM Council** — a deliberative body of language models that resolves conflicts and sets strategy
* **Self-Improving Observation Agent** — monitors, evaluates, and proposes system mutations
* **AutoResearch Agent (ARA)** — overnight cognitive self-experimentation for continuous improvement
* **Exhaustive Backup System** — layered redundancy with state replay
* **System of Record** — immutable, append-only ledger of all agent actions and decisions
* **NATS JetStream** — the nervous system for triggering, orchestration, communication, and replay

---

### 2. Architectural Philosophy

#### 2.1 Convergent Design Principles
MARVIN treats the brain not as a blueprint but as a source of convergent design principles. Both biological intelligence and MARVIN face the same fundamental computational challenges:
* **Coordination of specialists** — how to manage heterogeneous processors with different latencies and modalities
* **Asynchronous data fusion** — how to bind multi-modal, temporally staggered inputs into coherent state
* **Coherent behavior under uncertainty** — how to act decisively when information is incomplete
* **Conflict resolution** — how to arbitrate when specialists disagree
* **Continuous learning without forgetting** — how to grow without destroying established competence

#### 2.2 Minsky’s Society of Mind as Engineering Primitive
MARVIN operationalizes Minsky’s nine cognitive principles as system-level engineering constraints:

| Minsky Principle | MARVIN Implementation |
| :--- | :--- |
| **Born with mental resources** | Pre-loaded agent ensemble with base skills |
| **Learn from interacting with others** | Inter-agent message passing + episodic replay |
| **Emotions as different Ways to Think** | Agent priority signals / urgency weights in ignition |
| **Think about recent thoughts** | Metacognition Agent with rolling workspace introspection |
| **Think on multiple levels** | Hierarchical agency: Orchestrator → Team → Specialist |
| **Accumulate commonsense knowledge** | Semantic Memory Agent + Knowledge Graph |
| **Switch among Ways to Think** | Dynamic tool/agent selection via salience scoring |
| **Multiple ways to represent things** | Neuro-symbolic dual representation |
| **Multiple models of self** | Self-model registry updated by Observation Agent |

#### 2.3 Inner Conflict as a Feature
MARVIN deliberately introduces controlled tension between agents. Specialist disagreement is not an error condition — it is a signal that the problem is non-trivial and triggers the LLM Council for deliberation. This mirrors the brain’s competitive workspace dynamics and prevents premature convergence on suboptimal solutions.

---

### 3. Core Architectural Layers
┌─────────────────────────────────────────────────────────────────────┐
│ USER VISION / GOALS │
│ (North Star — Immutable Intent) │
└─────────────────────────────┬───────────────────────────────────────┘
│
┌─────────────────────────────▼───────────────────────────────────────┐
│ LLM COUNCIL │
│ Strategic deliberation · Conflict resolution │
│ Goal decomposition · Ethics arbitration │
└───────┬─────────────────────┬─────────────────────┬────────────────┘
│ │ │
┌───────▼──────┐ ┌───────────▼──────────┐ ┌──────▼──────────────────┐
│ ORCHESTRATOR│ │ METACOGNITION AGENT │ │ OBSERVATION AGENT │
│ (CWA Core) │ │ (Self-monitoring) │ │ (Self-improvement) │
└───────┬──────┘ └──────────────────────┘ └───────────┬─────────────┘
│ │
│ ┌────────────────▼────────────────┐
│ │ AUTORESEARCH AGENT (ARA) │
│ │ (Cognitive self-experiments) │
│ └────────────────┬────────────────┘
│ │
┌───────▼───────────────────────────────────────────────▼────────────────┐
│ COGNITIVE WORKSPACE (Blackboard) │
│ Shared state · Ignition dynamics · Global broadcast │
└───────┬──────────────────────────────────────────────────────────────┘
│
┌───────▼────────────────────────────────────────────────────────────┐
│ HETEROGENEOUS AGENT ENSEMBLE │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│ │Cognitive │ │Perceptual│ │ Memory │ │Procedural│ │ Critic │ │
│ │ Agents │ │ Agents │ │ Agents │ │ Agents │ │ Agents │ │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │
└───────┬────────────────────────────────────────────────────────────┘
│┌───────▼────────────────────────────────────────────────────────────┐
│ NATS JETSTREAM HARNESS │
│ Triggering · Orchestration · Replay · Communication Bus │
└───────┬────────────────────────────────────────────────────────────┘
│
┌───────▼────────────────────────────────────────────────────────────┐
│ SOVEREIGN DOMAIN MESH + TRIBE v2 LAYER │
│ Federated nodes · Retained ownership · Cross-tribe routing │
└───────┬────────────────────────────────────────────────────────────┘
│
┌───────▼────────────────────────────────────────────────────────────┐
│ MCP SKILL HOOKS · PLUGINS · TOOLS │
│ Skills MCP Server · Tools MCP Server · SSH Server · Extensions │
└────────────────────────────────────────────────────────────────────┘

---

### 4. Cognitive Workspace Architecture (CWA)

#### 4.1 The Workspace
The Cognitive Workspace is the single source of truth for all in-flight system state. All agents communicate exclusively through the workspace — no direct peer-to-peer channels exist at the task level.

**Workspace Schema (JSON):**
```json
{
  "workspace_id": "uuid",
  "created_at": "ISO8601",
  "plan_id": "uuid",
  "phase": "planning | executing | validating | broadcasting | done",
  "items": [
    {
      "item_id": "uuid",
      "sender_agent_id": "string",
      "sender_agent_type": "cognitive | perceptual | memory | procedural | critic",
      "timestamp": "ISO8601",
      "content_type": "plan | hypothesis | observation | result | error | critique",
      "content": {},
      "urgency": 0.0,
      "confidence": 0.0,
      "salience_score": 0.0,
      "status": "pending | ignited | inhibited | broadcast | archived"
    }
  ],
  "broadcast_slot": null,
  "inhibited_items": [],
  "global_context": {}
}
```

#### 4.2 Workspace Orchestrator
The Orchestrator is a stateful controller implementing a deterministic state machine.

**States:** IDLE → PLANNING → EXECUTING → VALIDATING → BROADCASTING → DONE

| From | To | Trigger |
| :--- | :--- | :--- |
| IDLE | PLANNING | User goal received |
| PLANNING | EXECUTING | Plan posted to workspace by Planner Agent |
| EXECUTING | VALIDATING | All plan steps resolved |
| VALIDATING | BROADCASTING | Critic Agent posts status: approved |
| VALIDATING | EXECUTING | Critic Agent posts status: rejected |
| BROADCASTING | DONE | Global broadcast acknowledged by all subscribers |
| ANY | IDLE | Reset signal or timeout |

#### 4.3 Ignition Mechanism
The Ignition Engine governs which workspace item receives the global broadcast slot at each cognitive cycle.

**Salience Computation:** `s_i = Temp(∑f w_f · x̃(i,f))` where `Temp(z) = z^(1/T), T = 0.7` (default)

**Default weights:**
- `w_urgency = 0.40`
- `w_goal_sim = 0.25`
- `w_recency = 0.15`
- `w_confidence = 0.20`

**Adaptive Threshold:**
```
τ = τ0 + k_load · L + k_conf · C − k_prio · P

Defaults:
τ0 = 0.50
k_load = 0.20 (load pressure factor)
k_conf = 0.15 (conflict index factor)
k_prio = 0.30 (plan priority factor)
```

**Buffer Normalization:** `ŝ_i = β · z-score(s_i) + (1−β) · rank_quantile(s_i)` where `β = 0.5`

**Winner-Take-All Broadcast:** When `ŝ_i ≥ τ`, the highest-scoring item fires. Competing items are inhibited for the broadcast window (300–500 ms logical time units). Hysteresis band `h = 0.10` prevents thrashing.

#### 4.4 Data Fusion for Binding
For multi-modal inputs arriving asynchronously:

| Decision Algorithm | Application |
| :--- | :--- |
| **Kalman Filter (EKF/UKF)** | Continuous state estimation from noisy sensors |
| **Dempster-Shafer Theory** | Combining discrete evidence from multiple classifiers |
| **LSTM-based anomaly scorer** | Time-series anomaly detection |

**Temporal Buffer Policy:** Buffer duration = 2× the p95 latency of the slowest critical agent for the current event type. Critical agents are designated per event by the active plan.

---

### 5. Sovereign Domain Mesh

#### 5.1 Concept
The Sovereign Domain Mesh is a federated network of MARVIN nodes where each node retains full ownership of its data, models, and compute. Nodes collaborate without surrendering sovereignty.

#### 5.2 Node Anatomy
┌─────────────────────────────┐
│ DOMAIN NODE │
│ ┌───────────────────────┐ │
│ │ Local Agent Pool │ │
│ │ Local Workspace │ │
│ │ Local SOR │ │
│ └──────────┬────────────┘ │
│ │ │
│ ┌──────────▼────────────┐ │
│ │ Domain Gateway │ │
│ │ (ACL + Sovereignty │ │
│ │ enforcement) │ │
│ └──────────┬────────────┘ │
└─────────────┼───────────────┘
│ Mesh Protocol (mTLS + JWT)
▼
Other Domain Nodes

#### 5.3 Sovereignty Rules
* **Data stays in domain** — no raw data leaves the originating node without explicit owner consent
* **Model weights are local** — fine-tuned models do not cross node boundaries unless exported with signed provenance
* **Results are shareable** — processed outputs (embeddings, summaries, decisions) may be shared via the mesh
* **Audit trail is immutable** — every cross-domain call is logged in both the originating and receiving SOR

#### 5.4 Mesh Protocol
| Layer | Technology |
| :--- | :--- |
| **Transport** | NATS Leaf Nodes over mTLS |
| **Auth** | JWT with domain-scoped claims |
| **Discovery** | NATS service discovery + domain registry |
| **Routing** | Consistent hashing on domain_id + conversation_id |
| **Conflict** | Last-write-wins with vector clocks for non-critical state |

#### 5.5 Cross-Domain ACL Schema
```json
{
  "acl_id": "uuid",
  "source_domain": "string",
  "target_domain": "string",
  "allowed_operations": ["read_result", "request_skill", "publish_event"],
  "denied_operations": ["read_raw_data", "export_model"],
  "expiry": "ISO8601",
  "signed_by": "owner_keypair_fingerprint"
}
```

---

### 6. Tribe v2 Model Integration

#### 6.1 What Is a Tribe?
A Tribe is a named, persistent team of agents with a shared identity, shared memory namespace, and a designated Tribe Leader. Tribes map to functional domains (e.g., tribe:research, tribe:engineering, tribe:creativity).

#### 6.2 Tribe Schema
```json
{
  "tribe_id": "uuid",
  "name": "string",
  "domain": "string",
  "leader_agent_id": "string",
  "members": [
    {
      "agent_id": "string",
      "role": "specialist | generalist | critic | scribe",
      "skills": ["skill_name"],
      "status": "active | standby | hibernating"
    }
  ],
  "shared_memory_ns": "tribe:{tribe_id}:memory",
  "workspace_partition": "tribe:{tribe_id}:workspace",
  "inter_tribe_channels": ["tribe_id"],
  "created_at": "ISO8601",
  "version": "2.0"
}
```

#### 6.3 Tribe Lifecycle
FORMATION → BRIEFING → ACTIVE → DELIBERATING → REPORTING → DISSOLVING

#### 6.4 Inter-Tribe Communication
Tribes communicate via NATS subjects namespaced by tribe: `tribe.{source_tribe_id}.to.{target_tribe_id}.{message_type}`

Cross-tribe messages require acknowledgment from the target Tribe Leader before processing. The LLM Council mediates disputes that span tribe boundaries.

#### 6.5 Role Inheritance
Tribe v2 supports role inheritance. A generalist agent inherits the skill set of any absent specialist agent at reduced confidence (confidence × 0.7). This prevents deadlock when a specialist agent fails.

---

### 7. MoMoA — Mixture of Multi-Agent Architecture

#### 7.1 Concept
MoMoA abstracts the MoE (Mixture of Experts) paradigm from the token level to the task level. Instead of routing tokens to sub-networks, MoMoA routes entire sub-tasks to independent, specialized agents.

#### 7.2 Routing Logic
Task received → Task Classifier (LLM-based) → Tribe/Agent Selection

| Task Type | Target |
| :--- | :--- |
| code_generation | Tribe:Engineering |
| research | Tribe:Research |
| creative | Tribe:Creativity |
| analysis | Tribe:Analytics |
| system_ops | Tribe:Operations |
| unknown | LLM Council |

#### 7.3 Compositional Chains
Agents may recursively delegate sub-tasks to other agents (up to depth 4). Circular delegation is detected via a call-stack hash and rejected.

#### 7.4 Confidence Aggregation
`final_confidence = weighted_harmonic_mean([agent_confidence × agent_reliability_score for each agent])`

`agent_reliability_score` is maintained by the Observation Agent and updated after each task.

---

### 8. Agent Taxonomy

#### 8.1 Cognitive & Linguistic Agents (The Neocortex)
| Agent | Model Backend | Primary Function |
| :--- | :--- | :--- |
| **Planner Agent** | Claude Opus / GPT-4-class | Goal decomposition, plan emission |
| **Reasoner Agent** | Claude Sonnet / Qwen3-35B | Multi-step logical inference |
| **Synthesizer Agent** | LLM (configurable) | Output generation from multiple inputs |
| **Neuro-Symbolic Agent** | LLM + symbolic solver | Formal verification, constraint satisfaction |
| **Creative Agent** | LLM (high temperature) | Novel ideation, metaphor generation |
| **Debate Agent** | LLM (adversarial) | Devil’s advocate, hypothesis stress-testing |

#### 8.2 Perceptual Agents (The Sensory Cortices)
| Agent | Architecture | Modality |
| :--- | :--- | :--- |
| **Vision Agent** | ViT / CNN | Image, video, screen capture |
| **Audio Agent** | Whisper-class | Speech-to-text, sound classification |
| **Code Perception Agent** | Tree-sitter AST | Source code structure extraction |
| **Document Agent** | PDF/DOCX parser | Structured document ingestion |
| **SNN Agent** | Spiking Neural Net | Time-series, real-time sensor streams |

#### 8.3 Memory Agents (The Hippocampus & Temporal Lobe)
| Agent | Storage Backend | Function |
| :--- | :--- | :--- |
| **Episodic Memory Agent** | Vector DB (pgvector / Qdrant) | Multi-modal episode storage and retrieval |
| **Semantic Memory Agent** | Knowledge Graph (Neo4j) | Factual world knowledge, entity relations |
| **Working Memory Agent** | Redis | Short-term in-flight state |
| **Associative Memory Agent** | Graph + Vector hybrid | Entity relationship tracking |
| **Compaction Agent** | LLM summarizer | Context window compression with loss budgets |

#### 8.4 Procedural & Reflexive Agents (The Cerebellum & Brainstem)
| Agent Type | Function |
| :--- | :--- |
| **Tool Executor Agent** | Deterministic MCP tool call dispatcher |
| **Shell Agent** | Deterministic Bash / system command execution |
| **SSH Agent** | Deterministic Remote VPS execution via SSH |
| **Browser Agent** | Playwright Web automation |
| **Validator Agent** | Rule-based Schema, format, constraint checking |
| **Monitor Agent** | Metrics collector System health, latency, error rates |

#### 8.5 Executive Agents
| Agent | Function |
| :--- | :--- |
| **Orchestrator Agent** | CWA workspace management, ignition cycle execution |
| **Metacognition Agent** | Monitors own cognitive processes, introspects workspace |
| **Observation Agent** | System-wide performance analysis, improvement proposals |
| **Genesis Agent** | Creates new agents when novel task types are detected |
| **Mediator Agent** | Conflict resolution between disagreeing agents |
| **Scribe Agent** | Maintains SOR, generates audit trails |
| **AutoResearch Agent (ARA)** | Cognitive self-experimentation, overnight optimization |

#### 8.6 Agent Capability Declaration Schema
Every agent must register at startup:
```json
{
  "agent_id": "uuid",
  "agent_role": "string",
  "agent_type": "cognitive | perceptual | memory | procedural | executive | critic",
  "tribe_id": "uuid | null",
  "description": "string",
  "skills": [
    {
      "skill_name": "string",
      "input_schema": {},
      "output_schema": {},
      "avg_latency_ms": 0,
      "reliability_score": 1.0
    }
  ],
  "model_backend": "string | null",
  "compute_cost_tier": "low | medium | high",
  "supports_streaming": false,
  "circuit_breaker_threshold": 3,
  "version": "string"
}
```

---

### 9. Cognitive Function Mapping
Each of the ten target cognitive functions maps to specific MARVIN subsystems:

| Cognitive Function | Subsystem(s) |
| :--- | :--- |
| Perception | Perceptual Agents (Vision, Audio, Document, Code, SNN) → Workspace ingestion |
| Generation | Synthesizer Agent, Creative Agent, Code Generator Agent |
| Attention | Ignition Engine — salience scoring and winner-take-all broadcast |
| Learning | Observation Agent + Genesis Agent + Agent Memory Graphs |
| Memory | Episodic, Semantic, Working, Associative Memory Agents |
| Reasoning | Reasoner Agent, Neuro-Symbolic Agent, Debate Agent |
| Metacognition | Metacognition Agent — workspace introspection and self-modeling |
| Executive Functions | Orchestrator, Planner, LLM Council — planning, inhibition, flexibility |
| Problem Solving | MoMoA routing → Tribe selection → Compositional chains |
| Social Cognition | Tribe v2 inter-agent protocol, Mediator Agent, LLM Council |

---

### 10. NATS JetStream Orchestration Harness

#### 10.1 Role
NATS JetStream serves as the nervous system of MARVIN. All triggering, orchestration, inter-agent communication, and replay flows through JetStream.

#### 10.2 Stream Topology
| Stream | Purpose |
| :--- | :--- |
| MARVIN_EVENTS | system-wide event bus (all agents subscribe) |
| MARVIN_WORKSPACE | workspace item publications |
| MARVIN_PLANS | plan emissions and updates |
| MARVIN_TOOLCALLS | MCP tool call requests and results |
| MARVIN_SOR | system of record append stream |
| MARVIN_SELFIMPROVE | observation and improvement proposals |
| MARVIN_TRIBE_{ID} | per-tribe communication channels |
| MARVIN_COUNCIL | LLM council deliberation messages |
| MARVIN_BACKUP | backup triggers and state snapshots |
| MARVIN_REPLAY | replay command channel |
| MARVIN_ARA | AutoResearch experiment ledger |

#### 10.3 Subject Naming Convention
`marvin.{domain}.{tribe_id}.{agent_id}.{message_type}.{version}`

#### 10.4 Message Envelope
```json
{
  "message_id": "uuid",
  "conversation_id": "uuid",
  "plan_id": "uuid",
  "sender": {
    "agent_id": "string",
    "tribe_id": "string | null",
    "domain": "string"
  },
  "receiver": "string | 'workspace' | 'broadcast'",
  "timestamp": "ISO8601",
  "sequence": 0,
  "performative": "request | inform | confirm | reject | vote | propose",
  "content": {},
  "schema_version": "1.0",
  "sor_required": true
}
```

#### 10.5 Triggering Architecture
External Input → `marvin.events.input.received.v1` → Orchestrator → Workspace/Plan Request → Planner Agent → Plan Emission

#### 10.6 Replay Architecture
All JetStream streams are configured with retention limits and replicas. To replay a plan execution: `marvin.replay.from.{sequence_number}.{plan_id}`.

---

### 11. MCP Host / Server Architecture

#### 11.1 MCP Server Inventory
| Server Label | Primary Tools |
| :--- | :--- |
| tools_mcp_server.py | write_file, read_file, execute_bash, execute_python, git_ops |
| skills_mcp_server.py | list_skills, get_skill, register_skill, update_skill |
| ssh_mcp_server.py | ssh_connect, ssh_execute, ssh_transfer, ssh_list_sessions |
| code_mcp_server.py | index_repository, search_index, lint, type_check, run_tests |
| plugin:{name} | User-defined plugins via MCP spec |

#### 11.2 MCPHost Router
The MCPHost class maintains a `_tool_map: Dict[str, MCPConnection]` that routes tool names to their server.

#### 11.3 Skills Hook System
Skills are `SKILL.md` documents. Agents must list and get relevant skills before execution and report usage in the SOR.

#### 11.4 Plugin Architecture
Plugins extend MARVIN without modifying core. A plugin is a valid MCP server registered at runtime.

---

### 12. Memory Architecture

#### 12.1 Memory Hierarchy
| Level | Name | Backend | TTL | Size Limit |
| :--- | :--- | :--- | :--- | :--- |
| L0 | Working Memory | Redis | session duration | 10 MB |
| L1 | Episodic Memory | Vector DB | 90 days (default) | unlimited |
| L2 | Semantic Memory | Knowledge Graph | persistent | unlimited |
| L3 | Associative Memory | Graph + Vector hybrid | persistent | unlimited |
| L4 | Procedural Memory | Skills MCP + agent code | versioned | unlimited |

#### 12.2 Memory Manager Hooks
Hooks for startup, user input, tool calls, response, compaction, reset, and shutdown.

#### 12.3 Context Compaction Algorithm
When context pressure ≥ 75%, identify old messages, inject entity graph summary, call summarizer LLM, and replace with compacted message. Loss budget: ≥ 95% of entity relationships, ≥ 80% of factual content.

#### 12.4 Anti-Forgetting Architecture
Agent-specific Memory Graphs store nodes (actions/decisions) and weighted edges (outcomes).

---

### 13. Ignition Engine — Attention & Selection

#### 13.1 Cycle Execution
1. Per-feature robust normalization.
2. Salience scoring with temperature sharpening.
3. Buffer-level normalization (hybrid z-score + rank quantile).
4. Load, conflict, priority computation to determine threshold `tau`.
5. Winner-take-all with diversity penalty.

#### 13.2 Health Monitoring
Metrics for acceptance rate, single-agent dominance, p95 time-to-ignition, item staleness, and conflict resolution.

#### 13.3 Anti-Gaming Controls
Per-agent influence cap, spike detector, and weight bounds.

---

### 14. LLM Council

#### 14.1 Purpose
Convenes when Mediator cannot resolve disagreement, strategic direction is needed, or major system mutations/new agents are proposed.

#### 14.2 Council Composition
Chair (Planner Agent) + Members (Reasoner, Debate, Critic, Metacognition). Quorum: 3, Vote Threshold: 0.67.

#### 14.3 Deliberation Protocol
Proposal → Positions → Challenges → Vote → Decision/Escalation.

#### 14.4 Governance
Sessions are time-bounded; decisions are immutable once in SOR.

---

### 15. Self-Improvement & Observation Agent

#### 15.1 Observation Agent Responsibilities
Monitors metrics, identifies bottlenecks, proposes mutations, triggers A/B tests, and maintains self-model registry.

#### 15.2 Self-Improvement Loop
Monitor → Detect → Fork/Signal/Propose/Trigger.

#### 15.3 Genesis Agent
Scaffolds new agents when novel task clusters are detected, following LLM Council advice and running A/B tests.

#### 15.4 Performance Metrics
Accuracy, Latency, Cost, and Criticality aggregated into a reliability_score.

---

### 16. AutoResearch Agent (ARA)

#### 16.1 Concept
Runs overnight cognitive experiments on `cognition_config.json` to optimize ignition weights, routing policies, memory strategies, etc.

#### 16.2 Scope of ARA Experiments
Can modify ignition parameters, routing weights, memory thresholds, council rules, etc. Cannot modify core source code, streams, or SOR.

#### 16.3 The Evaluation Metric — composite_fitness
Weighted combination of Accuracy, Latency, Cost, Hallucination rate, and Task completion.

#### 16.4 ARA Architecture
Orchestrator, Hypothesis Generator, Experiment Runner, Critic, Scribe, and Regression Guard agents.

#### 16.5 Experiment Loop
Setup baseline → Propose change → Wait for eval → Evaluate → Keep/Discard → Write to SOR.

#### 16.6 Hypothesis Generation Strategies
Local search, Hypothesis-driven, Simplification, Cross-pollination, Radical change.

#### 16.7 Keep/Discard Logic
Based on improvement vs complexity cost.

#### 16.8 Safety Architecture
Regression Guard halt conditions and blast radius limits (max change, max params).

---

### 17. System of Record

#### 17.1 Architecture
Append-only, cryptographically signed ledger via NATS JetStream (MARVIN_SOR).

#### 17.2 SOR Entry Schema
Includes sor_id, sequence, timestamp, event_type, agent_id, payload, hash chain, and signature.

#### 17.3 SOR Guarantees
Immutability, Ordering, Integrity, Auditability, and Retention.

#### 17.4 Scribe Agent
Sole writer to the SOR; validates and signs all entries.

---

### 18. Backup & Resilience Architecture

#### 18.1 Backup Layers
L1 (Hot: NATS replication), L2 (Warm: Hourly snapshot), L3 (Cold: Daily full), L4 (SOR: Continuous replay).

#### 18.2 Orchestrator Failover
Active-passive failover with heartbeat monitoring.

#### 18.3 Circuit Breaker
Per-agent protection: CLOSED → OPEN → HALF_OPEN.

#### 18.4 Byzantine Fault Tolerance
Min 3 validators and 2-of-3 consensus for high-stakes tasks.

---

### 19. Data Flows & Sequence Diagrams

#### 19.1 Standard Task Flow
User → Orchestrator → Planner → Workspace → Agent → Critic → Synthesizer → User.

#### 19.2 LLM Council Escalation Flow
Mediator → Council Deliberation → Decision/Human Override → SOR → Orchestrator.

#### 19.3 ARA Experiment Flow
ARA Orchestrator → Hypothesis → MARVIN Core → Critic → Scribe → Advance/Rollback.

---

### 20. API & Interface Contracts

#### 20.1 Agent Communication Protocol (ACL)
Conforms to Section 10.4 schema; follows FIPA-ACL semantics.

#### 20.2 REST API (External Interface)
Endpoints for tasks, workspace, SOR, agents, tribes, council, ARA, health, and metrics.

#### 20.3 WebSocket API (Streaming)
Real-time streaming of workspace events and agent activity.

---

### 21. Security & Sovereignty Model

#### 21.1 Authentication
JWT for agents/mesh, OAuth2/OIDC for humans, Bearer tokens for MCP.

#### 21.2 Authorization
NATS subject ACLs, workspace ownership tags, and SOR read-only rules.

#### 21.3 Data Sovereignty Enforcement
Gateway rejects raw data egress; logs all transfers.

#### 21.4 Secrets Management
Vault / AWS Secrets Manager; reference by env var/path.

---

### 22. Deployment Architecture

#### 22.1 Minimum Viable Deployment
Single node with NATS, Orchestrator, a few agents, MCP servers, Redis, and SQLite/Postgres.

#### 22.2 Production Deployment
Kubernetes cluster with NATS cluster, tribe pods (auto-scaled), clustered memory services, LLM gateway, and SOR service.

#### 22.3 Scalability Patterns
Horizontal pod autoscaling, sharded workspaces, and load-balanced LLM calls.

---

### 23. Configuration Reference
Reference for `llm`, `context`, `ignition`, `nats`, `memory`, `circuit_breaker`, `backup`, `tribe`, `council`, `bft`, and `ara` settings.

---

### 24. Open Problems & Solutions

#### 24.1 Credit Assignment → Counterfactual Contribution Tracing (CCT)
Measure agent impact via shadow replays with candidate substitution and Shapley values.

#### 24.2 Neuro-Symbolic Robustness → Iterative Semantic Grounding with Divergence Detection (ISG-DD)
Generate multiple translations, measure divergence, and use graduated response tiers.

#### 24.3 Temporal Dynamics → Adaptive Multi-Timescale Workspace (AMTW)
Partition workspace into Fast/Medium/Slow lanes with per-tier ignition frequencies.

#### 24.4 Emergent Specialization → Evolutionary Role Discovery (ERD)
Evolve agent configurations as genomes driven by CCT fitness scores.

#### 24.5 Benchmarking → MARVIN Evaluation Suite (MES)
Concrete benchmarks and ablations with statistical rigor requirements.

---

### 25. Implementation Roadmap

* **Phase 0: Foundation (Weeks 1-4)**: NATS JetStream, SOR, Basic Agent Runtime, MCP Host.
* **Phase 1: Core Cognition (Weeks 5-10)**: Cognitive Workspace, Ignition Engine v1, Orchestrator, Memory Hierarchy.
* **Phase 2: Agent Ecosystem (Weeks 11-16)**: Agent Taxonomy, Tribe v2, LLM Council, MCP Servers.
* **Phase 3: Self-Improvement (Weeks 17-22)**: Observation Agent, Genesis Agent, AutoResearch Agent (ARA), ERD.
* **Phase 4: Production Hardening (Weeks 23-26)**: Sovereign Mesh, Backup/Recovery, Circuit Breakers, MES Benchmarking.
* **Phase 5: Advanced Cognition (Weeks 27-34)**: ISG-DD, AMTW, CCT, Dempster-Shafer Fusion.
* **Phase 6: Autonomous Operation (Weeks 35-40)**: Full Self-Improvement Loop, Cross-Domain Learning, Human-in-the-Loop Escalation, Continuous Deployment.

---

### 26. Operational Runbooks
Includes daily health check, incident response (Ignition stall, Agent cascade failure, SOR corruption), and maintenance procedures (Add new agent, Deploy config, Restore backup).

---

### 27. Metrics & Observability
KPIs for Quality, Latency, Throughput, Reliability, Efficiency, and Self-Improvement. Prometheus export and logging schema definitions.

---

### 28. Glossary
Definitions for Agent, ARA, Broadcast, Circuit Breaker, Cognitive Workspace, Composite Fitness, CWA, Domain, ERD, Genesis Agent, Ignition, Inhibition, JetStream, LLM Council, MCP, MoMoA, NATS, Observation Agent, Orchestrator, Salience, Scribe Agent, SOR, Tribe, and Workspace.

---

### 29. References
Foundational papers (Baars, Minsky, etc.), architectural precedents (AutoGPT, Autogen, etc.), and technology stack versions.

---

### 30. Appendices
Templates for `cognition_program.md`, Agent Capability Declaration, and SOR Entry Examples. Detailed Error Code list and Capacity Planning Guide.

---
*(End of SDD.md)*
