# Zelos: Local AI Orchestrator with Context-Aware Personalization

Zelos is a privacy-first, fully local AI orchestration system driven by an isolated data architecture instead of static prompt engineering. The system translates advanced psychological models into machine-readable data streams to continuously inject runtime context into a local inference engine.

The core objective of this repository is to demonstrate strict Separation of Concerns (SoC), automated context validation, and native OS-level integration under zero-cloud constraints.

---

## Architectural Philosophy (The McAdams Framework)

Based on our cognitive taxonomy research, Zelos rejects monolithic system prompts. Instead, the architecture splits the digital persona into three decoupled layers to maximize token efficiency and maintain clean data boundaries:

```text
+--------------------------------------------------------+

| 1. PERSISTENT MEMORY (Life Narrative)                  |
|    Technology: Local SQLite Database                   |
|    Function: Tracks conversation history & identity    |
+--------------------------------------------------------+
                           |
                           v  [Injects Historical Context]
+--------------------------------------------------------+

| 2. SITUATIONAL CONTEXT (Characteristic Adaptations)    |
|    Technology: JSON / Schema Validation                |
|    Function: Mutates behavior based on Active App      |
+--------------------------------------------------------+
                           |
                           v  [Adapts Tone & Layout Rules]
+--------------------------------------------------------+

| 3. CORE DNA (Dispositional Traits)                     |
|    Technology: JSON / OCEAN Psychometrics              |
|    Function: Static baseline (e.g., Agreeableness 0.15)|
+--------------------------------------------------------+
                           |
                           v  [Synthesized System Prompt]
+--------------------------------------------------------+

|             LOCAL LLM INFERENCE LOOP                   |
+--------------------------------------------------------+
```

---

## Data Validation and Inference Pipeline

Every input goes through a deterministic validation and synthesis engine before reaching the local model. This guarantees sub-millisecond data-layer verification and protects the context window from token bloating.

```text
User Input
   │
   ▼
[System Detector] ──> Identifies Active Application (e.g., Apple Mail / Notes)
   │
   ▼
[Data Layer]      ──> Fetches:
   │                  ├── Core Traits (traits.json)
   │                  ├── Situational Rules (context_rules.json)
   │                  └── Persistent Memory (ZELOS_MEMORIES via SQLite)
   │
   ▼
[Validator.py]    ──> Schema Check (Draft 2020-12)
   │                  │
   │                  ├── [Pass] ──> Token Optimization (token_counter.py)
   │                  └── [Fail] ──> Hard Fallback/Crash Prevention
   │
   ▼
[Synthesis]       ──> Builds Final Dynamic Prompt
   │
   ▼
Ollama API        ──> Local Execution
```

---

## Detailed Pipeline Specifications

### 1. User Input
The raw prompt or trigger initiated by the user inside the presentation layer. Unlike standard setups where the input is immediately sent straight to the model, Zelos holds the input in a staging area to intercept, clean, and enrich it with structural context first.

### 2. System Detector
A low-level macOS system query utilizing native Python subprocess handles and osascript execution bridges. By identifying if the user is actively working in Apple Mail or Apple Notes, the pipeline shifts the system persona autonomously. This removes user friction entirely since the user never has to waste prompt tokens manually typing application context.

### 3. Data Layer
The file system and database management layer responsible for reading the decoupled data sources. It enforces our core research philosophy by strictly isolating personality DNA from environment-based layout instructions and long-term history. This keeps our source files highly modular, readable, and easy to maintain.

### 4. Validator.py
An automated quality-gate utility executing sub-millisecond structural checks using the formal Draft 2020-12 JSON-Schema standard. If a profile is misconfigured, the pipeline catches the error instantly. A successful pass hands clean data down the line, while a failure triggers a hard fallback to protect the system and prevent the local model from consuming corrupt context.

### 5. Synthesis
The programmatic compiler that fuses user inputs, psychometric variables, and layout structures into one single, optimized system context window. This module specifically mitigates the critical engineering risk of Attention Drift (Lost in the Middle) by placing strict behavioral boundaries at the very end of the prompt right before the User Input, forcing the local model to maintain perfect character alignment throughout long conversations.

### 6. Ollama API
The local inference gateway communicating directly with your hardware over a secure, localhost REST API to run the model natively. This guarantees the ultimate value proposition of the system: absolute privacy. Zero data packets are transmitted to third-party cloud servers. Your private emails, confidential notes, and personalized behavioral profiles remain fully isolated on your local machine.

---

## Repository Architecture

```text
├── docs/                        # Research and Cognitive Frameworks
│   ├── persona_research.md      # Strategic objectives and engineering risks
│   ├── big_fives_research.md    # OCEAN model parameterization (Agreeableness 0.15)
│   └── mcadams_model_research.md# Dynamic 3-level data-decoupling strategy
│
├── data/                        # Isolated Structured Data
│   ├── schemas/                 # Strict structural rules for validation
│   │   ├── traits.schema.json   # Validates identity and linguistic taboos
│   │   └── context_rules.schema.json # Validates application routing parameters
│   └── profiles/                # Concrete archetypes
│       └── default/             # Reference profile: Steve Jobs Persona
│           ├── traits.json      # Hardcoded psychometrics and behavioral rules
│           └── context_rules.json # App-specific mutations (Mail vs. Notes)
│
├── src/                         # Python Core Execution
│   ├── __init__.py
│   └── research_tools/          # Milestone automation utilities
│       ├── validator.py         # Sub-millisecond JSON structural validator
│       └── token_counter.py     # Context window and attention drift tool
│
├── README.md                    # System Overview and Design
├── ROADMAP.md                   # Milestone tracking and risk mitigation matrix
└── requirements.txt             # Environment dependencies
```

---

## Research Insights Implemented

*   **Linguistic De-Bloating:** By setting the psychometric variable `agreeableness` to `0.15` in the data layer, the orchestration layer programmatically strips out corporate AI apologies and conversational fluff, optimizing processing speed.
*   **Mitigating Attention Drift:** The prompt synthesis engine is architected to inject strict behavioral constraints at the very end of the system context window, keeping the local model strictly aligned with the chosen archetype during deep, long-turn conversations.

---

## Project Status

This repository is currently executing **Epoch 1 (Persona Research & Data Structuring)**. The theoretical frameworks are finalized, the repository topography is deployed, and the core validation schemas are active. Progress is tracked transparently within the `ROADMAP.md` file.

## License
Distributed under the MIT License. See `LICENSE` for more information.
