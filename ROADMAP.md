# Zelos Project Roadmap

This document outlines the strategic milestones, engineering requirements, and research phases for Zelos, a privacy-first, fully local AI orchestrator. The core objective is to transition from static prompt engineering to a dynamic, decoupled context and personality injection framework powered by Ollama (Qwen 32B).

---

## Epoch 1: Persona Research & Data Structuring
STATUS: ACTIVE CURRENT FOCUS

The objective of this phase is to deconstruct abstract human behavioral traits into machine-readable, schema-validated JSON formats and establish the foundational research for context-window optimization.

### Architectural Deliverables & Task Breakdown

*   TASK 1.1: Cognitive Taxonomy Research
    *   Analyze linguistic and psychological frameworks to isolate "personality" into distinct code variables.
    *   Document findings inside `docs/persona_research.md`.

*   TASK 1.2: JSON Schema Definition (`data/schemas/`)
    *   Architect `traits.schema.json` to enforce strict formatting for tone, vocabulary boundaries, and core values.
    *   Architect `context_rules.schema.json` to validate conditional triggers based on external parameters (time, location, interface).

*   TASK 1.3: Reference Profile Implementation (`data/profiles/default/`)
    *   Construct the initial baseline profile using the compiled schemas to benchmark early model compliance.

*   TASK 1.4: Automation Tools & Infrastructure Testing
    *   Develop `src/research_tools/validator.py` leveraging Python's `jsonschema` library to achieve sub-millisecond data-layer verification.
    *   Build `src/research_tools/token_counter.py` to continuously profile the token footprint of injected JSON structures against the Qwen 32B context window.

---

## Epoch 2: Local Core & Context Synthesis Engine
STATUS: PLANNED

The objective of this phase is to build the central execution engine that ingests the JSON structures from Epoch 1 and synthesizes them into a highly optimized runtime prompt for the local LLM.

### Architectural Deliverables & Task Breakdown

*   TASK 2.1: Ollama Interface Wrapper (`src/llm_core/`)
    *   Develop a thread-safe, resilient Python client wrapped around the Ollama REST API layer.
    *   Configure optimal temperature, top_p, and repeat_penalty profiles customized for Qwen 32B adherence.

*   TASK 2.2: The Prompt Synthesis Engine
    *   Design the core module responsible for merging isolated JSON data streams (`traits.json` + `context_rules.json`) into a single, cohesive system prompt dynamically at runtime.

*   TASK 2.3: State & Telemetry Persistence (SQL Layer)
    *   Initialize a local SQLite instance (`data/sql/`) to store conversational history and user state tracking.
    *   Build query abstraction layers to inject historical context segments based on keyword matching.

---

## Epoch 3: macOS System Integration Bridges
STATUS: PLANNED

The objective of this phase is to bridge the localized intelligence layer with native desktop productivity data, transforming Zelos from a simple chatbot into an active system orchestrator.

### Architectural Deliverables & Task Breakdown

*   TASK 3.1: Apple Notes Ingestion Engine
    *   Implement an Inter-Process Communication (IPC) bridge using Python's `osascript` engine or native PyObjC wrappers to poll and parse the local Apple Notes SQLite backend securely.

*   TASK 3.2: Apple Mail Parsing Layer
    *   Construct a secure, read-only interface to index recent local email threads, extracting contextual entities to enrich the prompt generation matrix.

*   TASK 3.3: TCC Security & Permission Sandbox Compliance
    *   Engineer dedicated exception handling and graceful fallback protocols to manage macOS Transparency, Consent, and Control (TCC) security prompts without freezing the main application event loop.

---

## Epoch 4: Production Optimization & Semantic Evolution
STATUS: PLANNED

The final phase scales the architecture from an operational prototype to a high-performance, responsive, and intelligently semantic local system.

### Architectural Deliverables & Task Breakdown

*   TASK 4.1: Asynchronous Execution Engine
    *   Refactor the central orchestration architecture using Python’s `asyncio` framework to handle file I/O, SQL querying, and macOS app synchronization concurrently without blocking human interaction.

*   TASK 4.2: Transition to Semantic RAG
    *   Evaluate and implement a lightweight, local vector database (e.g., ChromaDB) to replace keyword-based SQL queries with mathematical vector embeddings for advanced long-term memory retrieval.

*   TASK 4.3: Telemetry & Evaluation Framework
    *   Build automated test suites to measure semantic drift, context window efficiency, and local hardware utilization under maximum load conditions.

---

## Critical Engineering Risks & Mitigation Strategies

| Risk Factor | Impact | Mitigation Strategy |
| :--- | :--- | :--- |
| **Context Window Overload** | High | Strict monitoring via the `token_counter.py` utility; implementing sliding-window pruning techniques on dynamic logs. |
| **Model Attention Drift** | Medium | Rigorous structuring of the synthesized prompt, placing strict operational rules at the very end of the context window to enforce Qwen 32B compliance. |
| **macOS API Deprecation** | Low | Isolating OS-level connectors behind strict interface abstract classes, making it easy to swap AppleScript for PyObjC if system APIs change. |
