# Architectural Research: Technical Formalization of AI Personas

## 1. Objective
The goal of this research phase is to deconstruct the abstract concept of a "personality" into deterministic, machine-readable data structures. By isolating behavioral traits into modular JSON schemas, we eliminate static system prompting and enable real-time, context-aware persona mutations within local LLMs (Qwen 32B).

---

## 2. Theoretical Framework (Cognitive Dimensions)
To translate human behavior into code, the Zelos orchestrator categorizes a digital persona into three operational layers:

### A. Static Blueprint (Core Traits)
These are immutable parameters that define the absolute boundaries of the AI's behavior. They do not change based on context.
*   **Linguistic Constraints:** Vocabulary limits, sentence structures, and professional jargon levels.
*   **Ethical & Operational Boundaries:** Core values, compliance rules, and fallback protocols for unanswerable queries.

### B. Dynamic Context (Environmental Rules)
Rules that dictate how the AI adapts its communication channel based on telemetry data.
*   **Channel Adaptation:** Shifting style based on platform (e.g., highly concise for Apple Notes, professional/structured for Apple Mail).
*   **Temporal & Situational Awareness:** Modifying urgency and response density based on timestamp or detected user stress indicators.

### C. Volatile State (Interaction Mood)
A short-term memory layer that tracks the immediate conversation dynamics.
*   **Sentiment Reflection:** Adapting the model's tone based on the user's recent inputs (e.g., matching enthusiasm or mirroring analytical behavior).
*   **Attention Steering:** Dynamically scaling the context window priority based on whether the user is brainstorming or asking for a code review.

---

## 3. JSON Mapping Strategy

The theoretical layers above are mapped into three distinct JSON modules to maintain strict Separation of Concerns (SoC):

### `traits.json` (The Persona Definition)
Defines *who* the AI is. It contains explicit constraints regarding vocabulary, tone, and logical boundaries.
*   *Key metrics to measure:* Token overhead of the prompt vs. behavioral compliance of Qwen 32B.

### `context_rules.json` (The Environment Matrix)
Defines *how* the AI acts under specific circumstances. This file contains conditional logic blocks parsed by the Python orchestrator before runtime injection.

### `interaction_state.json` (The Runtime Telemetry)
A dynamic file updated continuously by the application loop, functioning as a sliding-window tracker for session mood and topic focus.

---

## 4. Current Engineering Challenges & Benchmarks

During Phase 1, the research focuses heavily on the following technical constraints:
1.  **Token Efficiency:** How dense can a JSON-based persona definition be without overloading the context window of a local 32B model?
2.  **Attention Drift:** Does the model maintain strict adherence to JSON-defined boundaries during long, multi-turn conversations?
3.  **Parsing Latency:** Ensuring that local Python JSON-Schema validation happens in sub-millisecond timeframes before generating the LLM inference prompt.
