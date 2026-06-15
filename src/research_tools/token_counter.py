import json
import os
import sys
from typing import Dict, Any, Final
import tiktoken

# Architectural Constants
TOKENIZER_MODEL: Final[str] = "cl100k_base"
TARGET_PROFILE: Final[str] = "default"

def calculate_json_density(payload: Dict[str, Any], encoding_name: str = TOKENIZER_MODEL) -> int:
    """
    Minifies a JSON dictionary structure into a compressed string representation 
    and evaluates its exact mathematical BPE token length.
    """
    # Programmatic minification: Strips human-readable whitespace and cosmetics
    minified_json: str = json.dumps(payload, separators=(',', ':'))
    
    # Ingest directly into the Byte-Pair Encoding (BPE) engine
    tokenizer = tiktoken.get_encoding(encoding_name)
    return len(tokenizer.encode(minified_json))

def execute_profile_profiling(profile: str = TARGET_PROFILE) -> int:
    """
    Ingests all verified datasets from the storage layer, maps their byte payload,
    and outputs density diagnostics directly into the CLI console.
    """
    # Robust absolute path building from script context
    base_dir: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    profile_dir: str = os.path.join(base_dir, "data", "profiles", profile)

    print("Zelos Orchestration Framework: Token Profiling & Context Density")
    print("=" * 64)

    # Dictionary mapping target files to descriptive technical labels
    target_matrix: dict[str, str] = {
        "traits.json": "Core Traits Layer (DNA)",
        "context_rules.json": "Situational Context (Adaptation)"
    }

    total_infrastructure_overhead: int = 0

    for file_name, technical_label in target_matrix.items():
        file_path = os.path.join(profile_dir, file_name)
        
        if not os.path.exists(file_path):
            print(f"Profiling Error: Execution aborted. Missing payload: {file_name}")
            print("=" * 64)
            return 1

        try:
            with open(file_path, "r", encoding="utf-8") as target_file:
                json_data = json.load(target_file)
                
            layer_tokens = calculate_json_density(json_data)
            total_infrastructure_overhead += layer_tokens
            
            # Print padded format alignment for maximum CLI aesthetic readability
            print(f"-> {technical_label:<32} : {layer_tokens:>4} Tokens")
            
        except json.JSONDecodeError:
            print(f"Syntax Error: Could not parse {file_name}. Invalid JSON.")
            print("=" * 64)
            return 1

    print("-" * 64)
    print(f"Total Combined Architectural Infrastructure Overhead : {total_infrastructure_overhead:>4} Tokens")
    print("=" * 64)
    return 0

if __name__ == "__main__":
    sys.exit(execute_profile_profiling())
