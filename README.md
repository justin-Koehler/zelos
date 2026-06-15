# Zelos: Local AI Orchestrator with Context-Aware Personalization Layer

Zelos is a privacy-first, fully local AI orchestration system powered by Ollama executing the Qwen 32B model. The primary focus of this repository is to research, design, and implement a decoupled personalization layer using structured JSON and SQL databases. 

Instead of relying on static system prompts, this project explores how a digital persona can be scientifically structured and dynamically injected into a local LLM runtime environment.

---

## Active Milestone: Phase 1 — Persona Research & Data Structuring

The project is currently in an intensive research and design phase. Before writing the execution engine, the core challenge is to analyze what defines a digital personality and how human behavioral traits can be translated into deterministic, machine-readable data formats.

### Current Research Objectives & Roadmap

* [ ] **Analyze Personality Constructs:** Researching cognitive and linguistic frameworks to split a "persona" into modular, technical sub-components (e.g., long-term core values, volatile mood states, response constraints, and domain knowledge).
* [ ] **Design the JSON Architecture:** Defining strict JSON schemas to ensure personality files are reproducible, structured, and easily expandable.
* [ ] **Establish Modular JSON Layouts:** Planning the isolation of behavioral data into dedicated modules:
    *   `traits.json` — Long-term behavioral blueprints, specific tone-of-voice rules, and logical constraints.
    *   `context_rules.json` — Operational instructions defining how the AI adapts based on external factors like time, location, or communication channels.
    *   `interaction_state.json` — Tracking short-term conversation dynamics to simulate a shifting AI "mood" or focus area.
* [ ] **Context Window Optimization:** Evaluating how different JSON structures impact the token usage and attention mechanisms of the local Qwen 32B model.

---

## Targeted Tech Stack

*   **Research & Modeling:** JSON-Schema, Python 3.10+
*   **Local Inference Engine:** Ollama (Model: Qwen 32B), Open WebUI / OpenClaw
*   **Data Layout:** SQLite (for long-term relational context), JSON (for behavioral configuration)

---

## Project Status

This repository is currently in the **architectural planning, research, and design phase**. The repository structure is being initialized to support the foundational JSON personality schemas. Progress and research notes will be updated directly within this Phase 1 roadmap.

## License
Distributed under the MIT License. See `LICENSE` for more information.
