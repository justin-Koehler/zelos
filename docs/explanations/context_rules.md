# Engineering Research: Contextual Adaptation Framework (Tier 2)

## 1. WHAT: The Data Structure Specification

The second layer of Zelos allows the AI to adapt automatically to your workspace environment. It is stored as a compact `context_rules.json` file. The data architecture for the active workspace looks like this:

```json
{
  "active_application": "apple_mail",
  "layout_mode": "concise_paragraphs",
  "focus_modifier": "You are writing an email. Be business-focused, executive, and direct. No corporate fluff. Tell the truth immediately in sharp paragraphs."
}
```

This structural payload controls three critical dimensions in the background:
*   `active_application`: A unique name tag identifying which macOS application you are currently using.
*   `layout_mode`: A direct typographical formatting directive for the model (e.g., paragraphs or short text fragments).
*   `focus_modifier`: A precise behavioral instruction that overrides the default style of the generic AI.

---

## 2. WHY: Architectural and Psychological Rationale

Monolithic system prompts that combine personality traits and layout rules inside a single long text file make the AI inaccurate. Zelos resolves this by separating these layers completely (The McAdams Framework).

### Automatic Adaptation with Zero User Effort
Standard AI assistants do not know where you are typing. With Zelos, you never have to waste time telling the AI: *"Achtung, I am in Apple Mail, make it formal."* The system detects the application on its own and switches gears in the background. This eliminates user friction and prevents you from typing manual instructions before every question.

### Saving Precious Tokens on Local Hardware
Loading layout rules for all applications simultaneously into the context window of a local model like Qwen 32B wastes massive amounts of memory. Because we decouple these rules, Python loads only the exact JSON snippet for the application you are currently using. Your local system remains fast, responsive, and highly efficient.

### Securing AI Focus (Mitigating Attention Drift)
Large Language Models suffer from a positioning bias—they frequently forget instructions located in the middle of long text prompts. Because we isolate the context rules, our prompt builder can place the most critical boundary directive (`focus_modifier`) at the absolute end of the prompt, right before your question. The AI never loses track of the structural formatting rules.

---

## 3. HOW: Concrete Pipeline Implementation

The system processes this environment layout using a fast, five-stage background pipeline:

```text
+-----------------------+      +-----------------------+      +-----------------------+

| 1. OS APP DETECTION   | ───> | 2. DYNAMIC ROUTING    | ───> | 3. DATA LAYER CHECK   |
| Python queries macOS  |      | The system fetches the|      | validator.py verifies |
| for the active state  |      | matching target JSON  |      | the JSON file against |
| (e.g., Apple Mail).   |      | from local storage.   |      | the schema contract.  |
+-----------------------+      +-----------------------+      +-----------------------+
                                                                          │
                                                                          ▼
+-----------------------+      +-----------------------+      +-----------------------+

| OFFLINE INFRASTRUCT.  | <─── | 5. PROMPT COMPILATION | <─── | 4. DENSITY METRICS    |
| Secure localhost API  |      | Appends instructions  |      | token_counter.py      |
| executes the private  |      | at the absolute end   |      | monitors the precise  |
| model inference loop. |      | to guarantee focus.   |      | token footprint size. |
+-----------------------+      +-----------------------+      +-----------------------+
```

*   **Step 1:** The program uses a native AppleScript bridge to immediately detect when you switch to an application like Apple Mail.
*   **Step 2:** The data layers route the state token and automatically pull the correct `context_rules.json` file.
*   **Step 3:** The `validator.py` utility validates the JSON against `context_rules.schema.json`. If a syntax error is found, it stops execution instantly to prevent crashes.
*   **Step 4:** The orchestrator strips away cosmetic spaces to save memory footprint. The `token_counter.py` calculates the exact mathematical BPE token length.
*   **Step 5:** The dynamic prompt synthesizer merges your static DNA (Traits) and appends the app instructions right before your question. The final optimized bundle goes via localhost to Ollama—zero cloud, maximum speed, complete privacy.
