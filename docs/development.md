# Development

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
```

## Tests

```bash
python -m pytest -q
```

## Conventions

- functions stay small; extract early
- comments explain *why*, not *what*
- no new dependencies without a good reason
