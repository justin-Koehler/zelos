# Architectural Research: Technical Formalization of AI Personas

## 1. Objective
The goal of this research phase is to deconstruct the abstract concept of a "personality" into deterministic, machine-readable data structures. By isolating behavioral traits into modular data layers, we eliminate static system prompting and enable real-time, context-aware persona mutations within local inference setups.

---

## 2. Theoretical Framework (Cognitive Dimensions)
To translate human behavior into code, the Zelos orchestrator categorizes a digital persona into three distinct operational layers, mirroring the McAdams Three-Level Personality Framework:

### A. Static Blueprint (Dispositional Traits)
These are immutable parameters that define the absolute boundaries of the AI's behavior, acting as the psychological foundation. They do not change based on context.
*   **Linguistic Constraints:** Vocabulary limits, specific sentence structures, and professional jargon thresholds (e.g., stripping out standard AI politeness tokens).
*   **Ethical & Operational Boundaries:** Core values, compliance rules, and rigid fallback protocols for unanswerable queries.

### B. Dynamic Context (Characteristic Adaptations)
Rules that dictate how the AI adapts its communication channel and behavioral presentation based on telemetry data.
*   **Channel Adaptation:** Shifting execution style based on the active application frontend (e.g., highly concise, fragment-focused for Apple Notes vs. professional and executive-structured for Apple Mail).
*   **Temporal Awareness:** Modifying response density and operational urgency based on timestamp indicators or environment context.

### C. Persistent Narrative (Life Narrative & Memory)
The relational memory layer that tracks long-term historical dynamics, preventing the model from resetting its context window state between execution loops.
*   **Relational Continuity:** Remembering historical user interactions, ongoing individual projects, and previously established user preferences.
*   **Contextual Linking:** Enabling cross-application data bridging (e.g., cross-referencing information written in Apple Notes while formulating a response inside Apple Mail).

---

## 3. Data Mapping Strategy

The theoretical layers above are mapped into three distinct, decoupled storage modules to maintain a strict Separation of Concerns (SoC):

### `traits.json` (The Persona Definition)
Defines *who* the AI is at its core. It contains explicit constraints regarding vocabulary, continuous psychometric variables (OCEAN matrix), and logical boundaries.
*   *Key Metrics:* Token overhead of the schema structure vs. behavioral compliance of the local model.

### `context_rules.json` (The Environment Matrix)
Defines *how* the AI acts under specific circumstances. This file contains conditional rule blocks parsed by the Python orchestrator to adjust output constraints (like paragraph ceilings or formatting permissions) based on the active application.

### `ZELOS_MEMORIES` (The Local SQLite Database)
The relational memory core of the architecture. Instead of wasting context tokens on complete raw logs, Python query scripts retrieve targeted historical facts and interaction telemetry, dynamically injecting them into the inference stream on a per-need basis.
