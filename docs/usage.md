# Usage

The README covers the basics. This page collects the
longer examples and the notes that did not fit up front.

## Basic

```bash
python batch.py prompts.jsonl -o answers.jsonl --workers 4
```

## Notes

- Idempotent: skips ids already present in the output
- JSONL in, JSONL out: stream-safe for huge inputs
