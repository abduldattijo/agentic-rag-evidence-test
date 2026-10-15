#!/bin/bash
# Three independent runs of the two LLM designs on the frozen question set.
cd "$(dirname "$0")"
for i in 1 2 3; do
  MODE=full ./.venv/bin/python run_eval.py --designs multiquery,agent --out results/full_run$i.jsonl > results/full_run$i.log 2>&1
done
echo finished > results/full_runs.done
