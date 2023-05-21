import re
from typing import Any

from dataclasses import dataclass



@dataclass
class FieldResponse:
    value_found: bool
    value_valid: bool
    value: Any | None


class BaseField():
    schema = None
    end_tokens = [",", "}"]
    obj = None
    key = None
    generation_marker = None
    json_former = None

    def __init__(self, schema: dict, obj: Any, key: str, generation_marker: str):
        self.schema = schema
        self.obj = obj
        self.key = key
        self.generation_marker = generation_marker

    def insert_generation_marker(self):
        if type(self.obj) is dict:
            self.obj[self.key] = self.generation_marker

        if type(self.obj) is list:
            self.obj.append(self.generation_marker)

    def get_value(self, stream: str) -> str | None:
        """
        Will return None if a terminating characters has not yet been found.

        If a terminating character has been found, it'll return that value for processing.
        """
        value = []

        for char in stream:
            if char not in self.end_tokens:
                value.append(char)
            else:
                return "".join(value)
        return None

    def validate_value(self, val: str) -> bool:
        return True

    def postprocess_value(self, val: str) -> Any:
        return val

    def generate_value(self, stream: str) -> Any:
        value = self.get_value(stream=stream)

        if value is not None and self.validate_value(val=value):
            value = self.postprocess_value(val=value)
            return FieldResponse(
                value_found=True,
                value_valid=True,
                value=value
            )
        elif value is not None and not self.validate_value(val=value):
            return FieldResponse(
                value_found=True,
                value_valid=False,
                value=value
            )

        return FieldResponse(
            value_found=False,
            value_valid=False,
            value=None
        )
