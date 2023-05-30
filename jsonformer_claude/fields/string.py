from jsonformer_claude.fields.base import BaseField


class StrField(BaseField):
    def validate_value(self, val: str) -> str:
        if "enum" not in self.schema:
            return True

        return val in self.schema["enum"]

    def get_value(self, stream: str) -> str | None:
        if len(stream) < 2:
            return None

        if stream[0] == '"' and '"' in stream[1:]:
            return stream.split('"')[1]

        return None
