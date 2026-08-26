.PHONY: test lint run

test:
	python -m pytest -q

lint:
	python -m compileall -q .

run:
	python batch.py prompts.jsonl -o answers.jsonl --workers 4
