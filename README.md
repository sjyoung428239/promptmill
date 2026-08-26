# promptmill

Feed a thousand prompts, get a thousand answers

Built for my own use; public in case it helps someone.

## How to use

```bash
python batch.py prompts.jsonl -o answers.jsonl --workers 4
```

## What it does

- Concurrent workers with a rate ceiling
- JSONL in, JSONL out: stream-safe for huge inputs
- Idempotent: skips ids already present in the output
- Retries failed items with backoff, logs them aside

## Installation

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
```

## Project structure

```text
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── bug_report.md
│   ├── dependabot.yml
│   └── pull_request_template.md
├── docs/
│   ├── configuration.md
│   ├── development.md
│   ├── faq.md
│   └── usage.md
├── examples/
│   └── quickstart.md
├── tests/
│   └── test_smoke.py
├── .editorconfig
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── Makefile
├── SECURITY.md
├── batch.py
├── prompts.sample.jsonl
└── requirements.txt
```

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

## Why

Needed this for myself; figured others might too.

## License

MIT - see [LICENSE](LICENSE).
