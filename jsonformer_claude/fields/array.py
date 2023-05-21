from jsonformer_claude.fields.base import BaseField


class ArrayField(BaseField):
    end_tokens = ["]"]

    def insert_generation_marker(self):
        self.obj[self.key] = [self.generation_marker]
