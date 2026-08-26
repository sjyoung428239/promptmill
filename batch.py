import argparse
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from openai import OpenAI

_write_lock = threading.Lock()


def load_done(out_path):
    done = set()
    if Path(out_path).exists():
        with open(out_path, encoding="utf-8") as f:
            for line in f:
                try:
                    done.add(json.loads(line)["id"])
                except Exception:
                    pass
    return done


def ask(client, model, prompt, tries=3):
    for attempt in range(tries):
        try:
            r = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}])
            return r.choices[0].message.content
        except Exception:
            time.sleep(2 ** attempt)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("-o", "--out", default="answers.jsonl")
    ap.add_argument("--model", default="gpt-4o-mini")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    client = OpenAI()
    done = load_done(args.out)
    items = []
    with open(args.src, encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            if row["id"] not in done:
                items.append(row)
    print("%d pending, %d already done" % (len(items), len(done)))

    out = open(args.out, "a", encoding="utf-8")
    errs = open("errors.jsonl", "a", encoding="utf-8")

    def work(row):
        text = ask(client, args.model, row["prompt"])
        with _write_lock:
            if text is None:
                errs.write(json.dumps(row) + "\n")
                errs.flush()
            else:
                out.write(json.dumps(
                    {"id": row["id"], "answer": text},
                    ensure_ascii=False) + "\n")
                out.flush()

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(work, items))
    print("done")


if __name__ == "__main__":
    main()
