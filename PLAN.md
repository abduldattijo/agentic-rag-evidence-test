# Does agentic RAG actually retrieve better evidence? Plan, pilot and full-run results

Article question: on a small, reproducible set of recent AI papers, does an agent that decides
whether to search again find the right paper more often than simpler designs, and at what cost?

The title asks a question. The conclusion is written after the full run and must follow its numbers.

## What the pilot is, and is not

- **Is:** a dry run of the whole pipeline on 20 questions and 300 papers, to find mistakes in the
  harness and the questions, and to measure real cost and time before the full run.
- **Is not:** a result. Nothing from the pilot goes in the article as a finding. The pilot corpus is
  tiny, so retrieval is easier than it will be in the full run, and 20 questions cannot separate
  designs.
- **Rule:** do not tune designs on pilot questions to make a design look better. The full run uses a
  different seed, so no pilot question appears in it.

## The four designs (all use the same corpus, embedder, question set)

| Design | What it does | LLM calls |
|---|---|---|
| `dense` | One search with the original question. The baseline. | 0 |
| `multiquery` | LLM writes 3 rewrites; search the original and each; fuse with reciprocal-rank fusion. | 1 |
| `rerank` | Dense top 50, then a cross-encoder reorders them. | 0 |
| `agent` | First search is the original question; then an LLM sees the top 5 titles and either stops or writes a new query; at most 3 searches. Final order: the searches are fused by rank (RRF, same setting as `multiquery`). | up to 2 |

Pilot-discovered harness correction: the agent first merged searches by best raw score. On pilot
question q005 a rewritten query pushed the right paper from rank 1 to rank 4, because scores from
different queries are not comparable. It now fuses by rank (RRF, k=60, depth 50), exactly as
`multiquery`. The RRF setting was fixed from the existing design, not tuned on pilot outcomes.
The pilot result before the change is kept in `results/archive/`.

Fairness note: `agent` and `multiquery` get more searches than `dense`. The report prints searches
per question next to every result. The comparison to read is cost-quality, not "more searches win".

## What is recorded for every question and design

recall@5 (is the right paper in the top 5), reciprocal rank (MRR@10), searches, LLM tokens in/out,
dollars, latency. The report adds 95% bootstrap ranges, paired differences against `dense`, the
questions where a design lost a paper `dense` had, and how often the agent used all searches and
still missed.

## Steps

Set up once:

```bash
cd agentic-rag-eval
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 tests/test_metrics.py        # should print 5 "ok" lines
```

1. **Fill in prices.** Open `config.py` and copy the current USD-per-million-token prices for the two
   models into `PRICES`. The harness refuses to call an LLM until this is done. Check
   `MAX_USD` (default $5 hard stop) and confirm the models' training cutoff is before
   `PUBLISHED_AFTER`.
2. **Collect papers.** `python collect_papers.py` (about 2 to 4 minutes; arXiv asks for a 3 s wait
   between requests). Open `data/papers.jsonl` and read five lines.
3. **Write and review questions.** `python make_questions.py`, then open
   `data/questions_review.csv` and fill the `ok (1/0)` column for **every** row:
   - 0 if the question names the paper's title or is answerable by many papers,
   - 1 otherwise,
   - in `other_papers_that_also_answer`, note any paper in `papers.jsonl` that is an equally good
     answer (a survey, a follow-up).
   Rows with a `title_overlap` above 0.3 deserve a close look.
4. **Free designs first.** `python run_eval.py --designs dense,rerank --limit 5`, then the same for
   all 20. No LLM spend.
5. **LLM designs on 5 questions.** `python run_eval.py --designs multiquery,agent --limit 5`. Read
   `results/pilot.jsonl`: look at each agent `trace` (the queries it wrote).
6. **All designs, all 20.** `python run_eval.py`, then `python report.py`.
7. **Write down the cost.** Spend per question for each LLM design, times 300 questions, is the
   projected cost of the full run.

## Go / no-go before the full run

Proceed only if all of these hold:

- [x] At least 16 of the 20 questions pass review (pilot: 17 of 20; q000, q010, q018 failed) (otherwise the question prompt needs work).
- [x] The run finishes all four designs with no crashes and no malformed model replies that were
      silently ignored (pilot: no crashes; the agent's JSON replies parsed).
- [x] The agent never exceeds 3 searches and stops on its own at least sometimes (pilot and full run).
- [x] Measured spend projects to a full-run cost you are willing to pay (pilot: about $0.0001 per
      question per LLM design; the full run cost $0.14 for three runs).
- [x] Each hand-checked miss was a real retrieval miss, not a question with another valid answer
      (full run: all 13 dense misses were re-read against the gold and nearby papers; see below).

The pilot does **not** gate on which design wins.

## Known risks, and what the harness does about them

| Risk | Handling |
|---|---|
| Questions share words with the abstract, inflating dense retrieval | Title-overlap score and hand review; mixed question types (`specific`, `problem`, `vague`) |
| Another paper also answers the question | `other_papers_that_also_answer` column; sample misses by hand |
| The model already knows the papers | Only papers after `PUBLISHED_AFTER`, a date you verify against the model's cutoff |
| The question writer and the agent share a style | Different models for writing questions (`QUESTION_MODEL`) and for retrieval (`AGENT_MODEL`) |
| Small question set | Pilot 20, full 298 reviewed questions; every number printed with a 95% range. Dense already hits 95.6%, so only 13 questions can show a gain |
| Overspending | `PRICES` must be filled in; `MAX_USD` aborts the run |
| Cherry-picked opening example | The report counts how often the agent searches fully and still misses; pick the example from that list, and say how common it is |

## Full run: what was done

```bash
MODE=full python collect_papers.py       # 2,000 papers, 300 source papers + 5 close neighbours each
MODE=full python make_questions.py       # 295 questions; retry_skipped.py added the other 5
MODE=full python build_review_sheet.py   # worksheet: abstract + 3 nearest other papers per question
MODE=full python fix_questions.py        # post-review fixes (q014, q075, q215)
MODE=full python run_eval.py --designs dense,rerank
./run_llm_runs.sh                        # multiquery + agent, 3 runs
MODE=full python summarize_runs.py
MODE=full python export_examples.py      # results/rescued_and_lost_examples.md
```

Settings: `claude-sonnet-5-5` wrote the questions ($0.58); `claude-haiku-5-5` is the rewriter and agent,
with thinking disabled and no temperature (these models reject a non-default temperature, so outputs are
not exactly repeatable). Prices were copied from the provider's pricing page on 2026-10-15 and are in
`config.py`.

Decisions made along the way, all before the LLM designs were run:

- **Harder corpus.** The pilot was too easy (dense scored 17 of 17 at rank 1). Each source paper got its
  5 nearest same-topic papers in the corpus, chosen by TF-IDF (not the retrieval embedder) before any
  retrieval was run. The nearest neighbours are only moderately close (median top-1 cosine 0.15), so the
  test is "harder than random", not adversarial.
- **Agent merge by rank.** The agent first merged searches by best raw score; pilot question q005 showed
  scores from different queries are not comparable. It now fuses by rank (RRF, k=60, depth 50), the same
  setting as `multiquery`. The setting was not tuned on outcomes; the old pilot result is in
  `results/archive/`.
- **Review.** All 300 questions got a first-pass review by Claude (abstract plus 3 nearest other papers),
  marked provisional in the notes. The user spot-checked 30 `ok = 1` rows and found no unsupported
  answers. q064 and q088 are `ok = 0` (they ask for a result the abstract does not report). 298 questions
  remain.
- **Fixes after review.** q075 and q215 repeated 4+ words of their title and were regenerated (q215 twice,
  because the first rewrite matched another paper). q014 was replaced because its source was a pilot
  source. q061 and q122 list a related paper in notes only.
- **Freeze.** The question set, corpus and analysis plan are in `data_full/FROZEN.txt` with hashes. No
  question was dropped or re-marked after seeing dense results.
- **Not filtered on results.** Questions dense ranks first were kept. Removing them would select the test
  set using a result already seen.

## Full run: results (298 questions, 2,000 papers)

Dense and rerank are deterministic (one run). Multiquery and agent were run 3 times; the table shows the
mean and the range across runs.

| Design | recall@5 | MRR@10 | Searches / question | Median latency | $ / query |
|---|---|---|---|---|---|
| dense | 0.956 | 0.895 | 1.0 | 0.01 s | 0 |
| rerank | 0.970 | 0.959 | 1.0 | 1.46 s | 0 |
| multiquery | 0.936 (0.930 to 0.943) | 0.868 (0.866 to 0.871) | 4.0 | 1.37 s | $0.00006 |
| agent | 0.969 (0.966 to 0.970) | 0.906 (0.902 to 0.909) | 1.7 | 1.40 s | $0.00009 |

Paired differences against dense (same questions, 95% bootstrap range):

| Design | recall@5 | MRR@10 |
|---|---|---|
| rerank | +0.013 [-0.007, +0.037], no clear difference | +0.064 [+0.037, +0.093], better |
| multiquery | -0.020 [-0.046, +0.004], no clear difference | -0.026 [-0.057, +0.002], no clear difference |
| agent | +0.012 [-0.008, +0.035], no clear difference | +0.011 [-0.006, +0.029], no clear difference |

What it shows, and what it does not:

- On this corpus the agent is not clearly better than dense search. The reranker is the only clear
  improvement, and only in rank quality, at no model cost.
- Dense misses 13 of 298 questions in the top 5. The agent rescued 7 to 8 of them per run but lost 3 to 5
  hits dense had, so the net gain is small. Multiquery rescued 5 to 7 and lost 11 to 13.
- The agent stopped after one search on about 58% of questions and used all three on about 27%; on 7 to 8
  questions per run it used all three and still missed.
- Rescues come from rewrites that supply the paper's own vocabulary (for example "SLO-aware request
  routing"). Losses come from rewrites that invent terminology absent from the question and let
  distractors displace a paper dense already had; only q186 and q207 were lost in every run.
- Run-to-run spread is about 0.5 points, much smaller than the uncertainty from 298 questions.
- Total LLM spend for the three runs: about $0.14. Question writing: $0.60.

Limits to state in the article:

- Only 13 questions can show a gain, so differences below about 3 points cannot be separated from noise.
- One corpus (recent arXiv AI papers), one question-writing model, one agent model; questions were
  written from abstracts, which favours lexical and dense retrieval.
- The question review was a first pass by Claude with a 30-row spot-check by the user, not a full human
  check.
- The one added source (q014) has no planted neighbours and may be easier.
- Twelve pilot papers also appear in the full corpus, and one pilot source was replaced, so the pilot and
  full run are not fully independent.

Where to find the evidence:

- `results/full.jsonl`, `results/full_run1.jsonl` to `results/full_run3.jsonl`: per-question rows
  with rankings, traces, tokens, dollars and latency.
- `results/rescued_and_lost_examples.md`: every rescued, lost and never-found question with the agent's
  queries.
- `data_full/FROZEN.txt`, `data_full/questions_review.csv`: the frozen set and the review notes.

## Article outline (the order the evidence is shown)

1. Open with one real question where the agent searched repeatedly and still missed, with its
   queries, and the share of questions where that happens.
2. The four designs in plain words, one diagram.
3. The test: how questions were made, how they were checked, what counts as a hit.
4. Results table with ranges; the cost-quality chart (recall@5 against dollars per correct).
5. Where extra reasoning hurt: the questions a design lost that `dense` had.
6. What this does and does not show: a small test on recent AI papers, not a general rule.
7. Code: link to this folder.
