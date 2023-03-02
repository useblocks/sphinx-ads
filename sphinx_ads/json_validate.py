import json
from pathlib import Path
from typing import Any, Dict, List

from jsonschema import Draft7Validator


class Errors:
    def __init__(self, schema_errors: List[Any]):
        self.schema = schema_errors


def check_json_data(json_data: Dict[str, Dict[str, Any]]) -> Errors:
    """
    Checks a given json data, if it passes our JSON schema validation.

    Current checks:
    * Schema validation

    :param json_data: File path to a needs.json file
    :return: Dict, with error reports
    """
    schema_path = Path(__file__).parent / "json_schema.json"
    with open(schema_path) as schema_file:
        needs_schema = json.load(schema_file)

    validator = Draft7Validator(needs_schema)
    schema_errors = list(validator.iter_errors(json_data))

    # In future there may be additional types of validations.
    # So lets already use a class for all errors
    return Errors(schema_errors)
