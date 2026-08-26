# Quickstart

Fresh machine, five minutes.

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
```

Then:

```bash
python batch.py prompts.jsonl -o answers.jsonl --workers 4
```

If nothing happens, check docs/usage.md first.
