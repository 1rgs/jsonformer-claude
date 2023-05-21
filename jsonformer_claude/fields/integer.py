from jsonformer_claude.fields.base import BaseField


class IntField(BaseField):
    def validate_value(self, val: str) -> bool:
        try:
            if val.isdigit():
                val = int(val)
            else:
                val = float(val)

            if "max" in self.schema and val > self.schema["max"]:
                return False

            if "min" in self.schema and val < self.schema["min"]:
                return False

            return True
        except Exception as e:
            return False

    def postprocess_value(self, val: str) -> int | float:
        return int(val) if val.isdigit() else float(val)
