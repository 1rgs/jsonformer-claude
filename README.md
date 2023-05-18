# Jsonformer Claude: Generate Structured JSON from Anthropic's Claude Model

Generating structured JSON from language models can be a challenging task. The generated JSON must be syntactically correct and follow a schema that specifies the structure of the JSON. Jsonformer Claude is a library based on Jsonformer that works with Anthropic's language models to generate bulletproof JSON data following a given schema.

### Features

- Robust JSON generation: Jsonformer Claude ensures that the generated JSON is always syntactically correct and adheres to the specified schema.
- Efficiency: Jsonformer Claude generates only the content tokens and fills in the fixed tokens, making it more efficient than generating a full JSON string and parsing it.
- Compatible with Anthropic models: Jsonformer Claude is designed to work with Anthropic's Claude model for JSON generation.

### Supported schema types

Jsonformer Claude currently supports a subset of JSON Schema. Below is a list of the supported schema types:

- number
- boolean
- string
- array
- object

## Example Usage

```python
import asyncio
import anthropic

from jsonformer_claude.main import JsonformerClaude

# Replace with your Anthropic API key
api_key = "your-anthropic-api-key"

# Create an Anthropic client
client = anthropic.Client(api_key)

# Define the JSON schema
json_schema = { ... }

# Define the prompt
prompt = "Generate a person's information based on the following schema:"

# Create a JsonformerClaude instance
gen_json = JsonformerClaude(
    anthropic_client=client,
    json_schema=json_schema,
    prompt=prompt
)

# Generate structured JSON data
generated_data = await gen_json()

print(generated_data)
```

## Installation

```bash
pip install jsonformer-claude
```

## Development

To develop and contribute to Jsonformer Claude, ensure you have [Poetry](https://python-poetry.org/docs/#installation) installed for dependency management.

```bash
poetry install
```

```bash
poetry run python -m jsonformer_claude.example
```

## License

Jsonformer Claude is released under the MIT License. You are free to use, modify, and distribute this software for any purpose, commercial or non-commercial, as long as the original copyright and license notice are included.