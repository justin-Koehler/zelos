# Cognitive Taxonomy Research: The McAdams Three-Level Personality Framework

## 1. Definition and Core Concepts

In personality psychology, static trait frameworks (such as the Big Five) often fail to capture how an individual adapts to changing environments in real time. To solve this limitation, psychologist Dan McAdams developed a three-tiered evolutionary framework. It conceptualizes personality not as a single checklist, but as a dynamic, layered architecture consisting of structural disposition, situational adaptation, and historical narrative.

For the Zelos project, this framework provides the definitive blueprint for building a scalable, modular AI persona. Instead of forcing an entire character definition into a single, unmanageable system prompt, the AI's identity is decoupled software-side into three isolated architectural layers.

---

## 2. Implementing the McAdams Framework in AI Architecture

The Zelos engine translates the three psychological tiers directly into dedicated software data structures to maintain a strict Separation of Concerns (SoC):

### Tier 1: Dispositional Traits (The Foundation)
This layer defines the static, cross-situational, and enduring characteristics of the persona—the psychological baseline.
*   **AI Implementation:** Stored as continuous numerical float values within `data/profiles/default/traits.json`.
*   **Operational Function:** This contains the baseline Big Five parameters (OCEAN matrix) and static linguistic prohibitions (e.g., forbidding standard corporate AI phrasing). For the Steve Jobs persona, Tier 1 enforces a permanent baseline of high intensity, minimalism, and low agreeableness, independent of the current context.

### Tier 2: Characteristic Adaptations (The Contextual Matrix)
This layer governs how the core personality mutates its behavioral output based on changing roles, channels, environments, or user states. A human communicates differently in a formal business email than in a quick, raw personal note.
*   **AI Implementation:** Stored as conditional conditional logic blocks within `data/profiles/default/context_rules.json`.
*   **Operational Function:** The local Python orchestrator reads system telemetry data from the active application interface. If the user interacts via Apple Mail, Tier 2 structures the prompt to enforce a highly focused, professional business executive persona. If the interface switches to Apple Notes, the system dynamically routes into a raw, unfiltered brainstorming mode.

### Tier 3: Life Narrative (The Identity and Memory Layer)
The deepest tier of personality. It synthesizes past interactions with present events to create a coherent sense of identity, self-evolution, and relationship history with the interlocutor.
*   **AI Implementation:** Persisted and continuously updated within a local SQLite database (`data/sql/`).
*   **Operational Function:** This layer serves as the long-term relational memory of the system. It tracks historical conversation logs, active user projects, and learned preferences. Before any model inference occurs, the system queries the SQL layer to inject relevant historical facts into the active context window, simulating a continuous, developing human relationship.

---

## 3. Research Insights and Software Engineering Value

Applying the McAdams framework to local model orchestration yielded two critical architectural insights:

### Context Window and Token Efficiency
Injecting all personality metrics, situational routing rules, and full conversational histories simultaneously into the context window of a local 32B model causes high token overhead, slowing down local inference times. The modularity of this framework allows the system to load Tier 1 as a lightweight static component, while selectively filtering and dynamically injecting Tier 2 and Tier 3 data on a per-inference basis.

### Absolute Persona Interchangeability
Decoupling the tiers guarantees complete architectural modularity. If the Steve Jobs persona needs to be swapped out for a different archetype, the developer only needs to replace the `traits.json` file (Tier 1). The underlying logical routing matrix for macOS applications (Tier 2) and the persistent database history (Tier 3) remain fully operational and entirely untouched.
