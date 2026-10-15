# Agentic RAG evidence test

Code, questions, and saved results for the article *Does Agentic RAG Actually Retrieve Better
Evidence? I Tested It on 298 Questions*.

The test asks one thing. For each of 298 questions over 2,000 recent arXiv papers, does a search agent that can
rewrite its own queries put the right paper in the top 5 more often than plain search, and at what
cost? Four retrieval designs are compared on the same questions.

| Design | What it does |
|---|---|
| `dense` | One search with the question, using `BAAI/bge-small-en-v1.5` embeddings. |
| `rerank` | Dense top 50, reordered by `cross-encoder/ms-marco-MiniLM-L-6-v2`. |
| `multiquery` | Claude Haiku 5.5 writes 3 rewrites; the 4 searches are merged with reciprocal rank fusion (RRF, k = 60). |
| `agent` | Claude Haiku 5.5 sees the top 5 titles after each search and stops or writes a new query, up to 3 searches, merged with RRF. |

## Results (298 reviewed questions)

| Design | recall@5 (percent) | MRR@10 |
|---|---|---|
| dense | 95.6 | 0.895 |
| rerank | 97.0 | 0.959 |
| multiquery | 93.6 (3 runs) | 0.868 (3 runs) |
| agent | 96.9 (3 runs) | 0.906 (3 runs) |

Only the reranker's gain in rank quality clears zero. The agent's gain in recall (+1.2 points,
range -0.8 to +3.5) does not. The article explains the setup, the limits, and what changed after the
pilot. `PLAN.md` has the full plan and a results section.

## Layout

| Path | Contents |
|---|---|
| `data/` | The 20 question pilot (300 papers). |
| `data_full/` | The full run. `papers.jsonl` (2,000 papers), `questions.jsonl`, `questions_review.csv` (review values and notes), `sources.json`, `FROZEN.txt` (hashes and analysis plan). |
| `results/` | Saved per question rows. `full.jsonl` (dense, rerank), `full_run1..3.jsonl` (multiquery, agent), `pilot.jsonl`, and `rescued_and_lost_examples.md`. |
| `config.py`, `retrievers.py`, `metrics.py` | Settings, the four designs, and the scoring functions. |
| `collect_papers.py`, `make_questions.py`, `retry_skipped.py`, `fix_questions.py`, `build_review_sheet.py` | Building the collection and the questions. |
| `run_eval.py`, `run_llm_runs.sh`, `summarize_runs.py`, `export_examples.py` | Running and summarising. |

## Run it

Python 3.9 was used.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here          # only needed for multiquery and agent
MODE=full python run_eval.py --designs dense,rerank
MODE=full python run_eval.py --designs multiquery,agent --out results/full_run1.jsonl
MODE=full python summarize_runs.py
```

The first time, `run_eval.py` embeds the papers and caches the vectors in `data_full/`. Only
questions marked `1` in the `ok (1/0)` column of `data_full/questions_review.csv` are scored.
`config.py` holds the model prices (list prices copied on 2026-10-15). Check them before you run.

## Notes you should know

- **Review.** An AI assistant did a first pass over all 300 questions (abstract plus the three
  nearest other papers). The author spot checked 30 of the passes. The notes column says
  `PROVISIONAL`. Questions q064 and q088 are marked 0 and excluded.
- **Randomness.** Claude Haiku 5.5 rejects a non default temperature, so multiquery and agent
  vary between runs. That is why they were run three times.
- **Key loading.** `llm.py` in this repository reads the key only from `ANTHROPIC_API_KEY`. The
  version that produced the results could also read it from a private file. Nothing else differs.
- **Data.** Titles and abstracts come from the arXiv API. arXiv states that its metadata is
  available under a CC0 dedication (https://info.arxiv.org/help/license/index.html). Full texts were not
  used.
- **No license file yet.** The code has no license until the author adds one.
