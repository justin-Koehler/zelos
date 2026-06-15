import json
import os
import sys
from typing import Dict, Any
from jsonschema import validate, ValidationError

def load_json_file(file_path: str) -> Dict[str, Any]:
    """
    Loads and parses a JSON file from the local file system.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Target file not found at path: {file_path}")
        
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def validate_structure(data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
    """
    Validates a data dictionary against a formal JSON-Schema (Draft 2020-12).
    """
    validate(instance=data, schema=schema)
    return True

def run_single_validation(json_relative_path: str, schema_relative_path: str) -> bool:
    """
    Executes a single structural check for a given file and schema pair.
    """
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(current_script_dir, "..", ".."))
    
    json_path = os.path.join(base_dir, json_relative_path)
    schema_path = os.path.join(base_dir, schema_relative_path)

    try:
        data_instance = load_json_file(json_path)
        schema_ruleset = load_json_file(schema_path)
        validate_structure(data_instance, schema_ruleset)
        print(f"Validation successful: '{json_relative_path}' matches contract.")
        return True

    except FileNotFoundError as fnf_error:
        print(f"Pipeline Error [File Management]: {fnf_error}")
        return False
    except json.JSONDecodeError as json_error:
        print(f"Pipeline Error [Syntax Layer]: Invalid JSON syntax in {json_relative_path}.")
        print(f"Details: {json_error.msg} inside line {json_error.lineno}.")
        return False
    except ValidationError as schema_error:
        error_path = ".".join(str(segment) for segment in schema_error.path) or "root"
        print(f"Pipeline Error [Structural Contract Failed] in {json_relative_path}")
        print(f"Location: {error_path} -> {schema_error.message}")
        return False

if __name__ == "__main__":
    print("Zelos Orchestration Framework: Data-Layer Validation")
    print("=" * 60)
    
    # Validation Execution Matrix
    success_traits = run_single_validation(
        "data/profiles/default/traits.json", 
        "data/schemas/traits.schema.json"
    )
    print("-" * 60)
    success_context = run_single_validation(
        "data/profiles/default/context_rules.json", 
        "data/schemas/context_rules.schema.json"
    )
    print("=" * 60)
    
    if not success_traits or not success_context:
        sys.exit(1)
    sys.exit(0)
