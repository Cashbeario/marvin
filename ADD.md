# ADD.md — Architecture Design Document
## MARVIN: Multi-Agent Reasoning and Virtualized Intelligence Network
### Aether Neural — AGI Cognition Engine v3.0

---

### 1. Introduction
This document provides a detailed technical implementation guide for the MARVIN AGI framework. It builds upon the high-level design in `SDD.md`, focusing on the internal patterns, message structures, and component interactions that enable autonomous, self-improving intelligence.

### 2. Core Communication Patterns

#### 2.1 The NATS JetStream Backbone
MARVIN uses NATS JetStream as its "nervous system." All communication is asynchronous and event-driven.

*   **Pub/Sub Pattern:** Agents subscribe to specific subjects (e.g., `marvin.events.input.>`) to trigger their cognitive processes.
*   **Request/Reply Pattern:** Used for deterministic tool calls (MCP) and LLM Council voting.
*   **Persistent Streams:**
    *   `MARVIN_WORKSPACE`: Stores the current state of the cognitive blackboard.
    *   `MARVIN_SOR`: Immutable append-only ledger for all system actions.
    *   `MARVIN_REPLAY`: Replay command channel for state reconstruction.

#### 2.2 Cognitive Workspace Interaction
Agents do not communicate directly. Instead, they "post" to the workspace.

1.  **Submission:** Agent A publishes a message to `marvin.workspace.item.new.v1`.
2.  **Validation:** The Orchestrator validates the schema.
3.  **Ignition:** The Ignition Engine calculates salience using the formula `s_i = Temp(∑f w_f · x̃(i,f))`.
4.  **Broadcast:** If salience meets the adaptive threshold `tau`, the item is published to `marvin.workspace.broadcast.v1`, triggering downstream agents.

---

### 3. Component Deep Dive

#### 3.1 Ignition Engine (Salience Scoring)
The Ignition Engine implements a competitive attention mechanism. It selects the most "relevant" thought for global broadcast.

**Logic:**
*   **Salience Score (`s`):** A weighted sum of Urgency (0.40), Goal Similarity (0.25), Recency (0.15), and Confidence (0.20).
*   **Adaptive Threshold (`tau`):** `τ = τ0 + k_load · L + k_conf · C − k_prio · P`. It dynamically adjusts based on system load and conflict levels.
*   **Inhibition:** When a "thought" is ignited, competing thoughts are temporarily suppressed (Inhibited Registry) to prevent cognitive noise.

#### 3.2 Tribe v2: Team Coordination
Tribes provide a mechanism for multi-agent collaboration on complex sub-tasks.

*   **Tribe Leader:** A designated agent (usually a high-capability LLM like Claude Opus) that coordinates the tribe's internal workspace partition.
*   **Shared Memory:** Tribes have access to namespaced Redis keys (`tribe:{id}:memory`) for fast, shared state during a task.
*   **Role Inheritance:** If a specialist fails, a generalist in the same tribe inherits the skill set at reduced confidence (0.7).

#### 3.3 AutoResearch Agent (ARA) Experiment Loop
ARA continuously optimizes the system's "hyperparameters" (ignition weights, compaction thresholds).

1.  **Hypothesis Generation:** ARA proposes a mutation to `cognition_config.json`.
2.  **Sandboxed Evaluation:** The system runs with the new config for an evaluation window (50 tasks).
3.  **Fitness Function:** `composite_fitness = 0.35 * accuracy + 0.20 * latency + 0.15 * cost + 0.20 * hallucination + 0.10 * completion`.
4.  **Keep/Discard Logic:** Based on improvement vs complexity cost.

#### 3.4 LLM Council Deliberation
The highest deliberative body, convened for strategic decisions or when the Mediator fails to resolve conflicts.
*   **Quorum:** 3 members required.
*   **Vote Threshold:** 0.67 (2/3 majority).
*   **Protocol:** Chair (Planner) presents issue → Members (Reasoner, Debate, Critic) post positions → Debate Agent challenges → Vote.

---

### 4. Data Persistence & Sovereignty

#### 4.1 System of Record (SOR)
The SOR is the "ground truth." Every message with `sor_required: true` is hashed into a chain.
*   **Integrity:** Cryptographically signed (Ed25519) hash chains.
*   **Auditability:** Every cross-domain call and tool invocation is logged.
*   **Resilience:** JetStream replication (3x) + file-backed persistence.

#### 4.2 Sovereign Domain Mesh
Nodes interact via the Mesh Gateway over mTLS.
*   **Sovereignty Rules:** Raw data and model weights never leave the domain.
*   **ACLs:** Define cross-domain permissions (`read_result`, `publish_event`, etc.).
*   **Auditability:** Cross-domain calls are logged in both source and target SORs.

---

### 5. Implementation Stack
*   **Orchestration:** Kubernetes 1.28+
*   **Messaging:** NATS JetStream 2.10+
*   **In-Memory Store:** Redis 7.x
*   **Vector Database:** Qdrant (Episodic Memory)
*   **Knowledge Graph:** Neo4j (Semantic Memory)
*   **Model Interface:** MCP (Model Context Protocol)
*   **Metrics:** Prometheus + Grafana

---

### 6. Advanced Cognitive Mechanisms
*   **CCT (Counterfactual Contribution Tracing):** Shapley-based credit assignment for multi-agent tasks.
*   **ISG-DD (Iterative Semantic Grounding):** Triple-translation validation for symbolic logic.
*   **AMTW (Adaptive Multi-Timescale Workspace):** Fast, Medium, and Slow lanes for asynchronous agent synchronization.
