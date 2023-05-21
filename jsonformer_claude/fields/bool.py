from jsonformer_claude.fields.base import BaseField


class BoolField(BaseField):
    end_tokens = [",", "}"]

    def validate_value(self, val: str) -> bool:
        return val in ["true", "false"]

    def postprocess_value(self, val: str):
        return val == "true"
