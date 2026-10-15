# Agent vs dense: rescued, lost and never-found questions

Frozen question set (298 questions), agent run 3 times. Ranks are the position of the correct paper in the top 10 (`-` = not in top 10). Queries are exactly what the agent wrote.

Counts: Rescued 8, Lost 8, Never found 5

## Rescued (dense missed the top 5, agent found it in at least one run)

### q091 (problem)
**Question:** How can incoming LLM inference requests be dispatched in real time across parallel decode workers with limited batch slots and KV-cache memory, so that explicit latency and throughput targets are traded off in a principled way rather than via ad hoc heuristics?
**Correct paper:** Online Linear Programming for Multi-Objective Routing in LLM Serving (2607.03948)
**Dense rank:** -   **Agent ranks, runs 1-3:** 1, 1, 1   **Searches:** 3, 3, 3

- Run 1:
  - query: How can incoming LLM inference requests be dispatched in real time across parallel decode workers with limited batch slots and KV-cache memory, so that explicit latency and throughput targets are traded off in a principled way rather than via ad hoc heuristics?
    - correct paper in top 10: no; top 3: From Inference Engine to Inference Control Plane: Connecting; A rigor-matched audit of periodic-step layer skipping for ef; AdaptiveSD A Stability-Aware, Runtime-Adaptive Speculative D
  - query: SLO-aware request routing across decode replicas with KV cache capacity constraints optimization
    - correct paper in top 10: yes; top 3: Online Linear Programming for Multi-Objective Routing in LLM; The risk of KV cache compression; Minima-KV: Retention-Preserving KV Cache Compression with Mi
  - query: online dispatch LLM requests decode workers batch slots KV memory latency throughput tradeoff optimization
    - correct paper in top 10: yes; top 3: Online Linear Programming for Multi-Objective Routing in LLM; Deadline-Aware Adaptive Prefill Chunking for Efficient Large; BlockServe: Block-Grained Continuous Batching for High-Throu
- Run 2:
  - query: How can incoming LLM inference requests be dispatched in real time across parallel decode workers with limited batch slots and KV-cache memory, so that explicit latency and throughput targets are traded off in a principled way rather than via ad hoc heuristics?
    - correct paper in top 10: no; top 3: From Inference Engine to Inference Control Plane: Connecting; A rigor-matched audit of periodic-step layer skipping for ef; AdaptiveSD A Stability-Aware, Runtime-Adaptive Speculative D
  - query: SLO-aware request routing across decode replicas with KV cache capacity constraints optimization
    - correct paper in top 10: yes; top 3: Online Linear Programming for Multi-Objective Routing in LLM; The risk of KV cache compression; Minima-KV: Retention-Preserving KV Cache Compression with Mi
  - query: online dispatching LLM requests decode workers batch slots KV memory latency throughput tradeoff optimization
    - correct paper in top 10: yes; top 3: Online Linear Programming for Multi-Objective Routing in LLM; Deadline-Aware Adaptive Prefill Chunking for Efficient Large; BlockServe: Block-Grained Continuous Batching for High-Throu
- Run 3:
  - query: How can incoming LLM inference requests be dispatched in real time across parallel decode workers with limited batch slots and KV-cache memory, so that explicit latency and throughput targets are traded off in a principled way rather than via ad hoc heuristics?
    - correct paper in top 10: no; top 3: From Inference Engine to Inference Control Plane: Connecting; A rigor-matched audit of periodic-step layer skipping for ef; AdaptiveSD A Stability-Aware, Runtime-Adaptive Speculative D
  - query: SLO-aware request routing across decode replicas KV cache memory constraint optimization latency throughput tradeoff
    - correct paper in top 10: yes; top 3: Online Linear Programming for Multi-Objective Routing in LLM; Minima-KV: Retention-Preserving KV Cache Compression with Mi; The risk of KV cache compression
  - query: dispatching LLM requests across decode workers with batch slot and KV-cache capacity constraints, principled latency-throughput tradeoff via optimization or control
    - correct paper in top 10: yes; top 3: Online Linear Programming for Multi-Objective Routing in LLM; BlockServe: Block-Grained Continuous Batching for High-Throu; Minima-KV: Retention-Preserving KV Cache Compression with Mi

### q100 (problem)
**Question:** How can we get language models to realistically imitate students of varying skill levels, given that they tend to answer nearly everything correctly even when told to act like a weak student?
**Correct paper:** From Mastery Profile to Simulated Response: Stochastic Student Knowledge Graphs (SSKG) for Faithful LLM Student Simulation (2608.21668)
**Dense rank:** 6   **Agent ranks, runs 1-3:** 2, 2, 2   **Searches:** 2, 3, 2

- Run 1:
  - query: How can we get language models to realistically imitate students of varying skill levels, given that they tend to answer nearly everything correctly even when told to act like a weak student?
    - correct paper in top 10: yes; top 3: Evaluating and Improving Pedagogical Fit in LLM-Based AI Tut; Task Competence Is Not Instruction Following: Evaluating Ins; StudentBench: AI and human tutoring yield equivalent GRE lea
  - query: simulating student responses with LLMs at controllable proficiency levels, avoiding overly correct answers, knowledge tracing
    - correct paper in top 10: yes; top 3: From Mastery Profile to Simulated Response: Stochastic Stude; Evaluating and Improving Pedagogical Fit in LLM-Based AI Tut; SWIM: Student Writing Simulation via Proficiency-Conditioned
- Run 2:
  - query: How can we get language models to realistically imitate students of varying skill levels, given that they tend to answer nearly everything correctly even when told to act like a weak student?
    - correct paper in top 10: yes; top 3: Evaluating and Improving Pedagogical Fit in LLM-Based AI Tut; Task Competence Is Not Instruction Following: Evaluating Ins; StudentBench: AI and human tutoring yield equivalent GRE lea
  - query: simulating students with LLMs knowledge tracing persona capability-constrained answering realistic errors
    - correct paper in top 10: yes; top 3: Pretrained Persona Mixture Models and Tandem Models for Huma; From Mastery Profile to Simulated Response: Stochastic Stude; Evaluating and Improving Pedagogical Fit in LLM-Based AI Tut
  - query: LLM simulated students answering with realistic mistakes and weak-student knowledge gaps, not overly accurate
    - correct paper in top 10: yes; top 3: From Mastery Profile to Simulated Response: Stochastic Stude; Evaluating and Improving Pedagogical Fit in LLM-Based AI Tut; StudentBench: AI and human tutoring yield equivalent GRE lea
- Run 3:
  - query: How can we get language models to realistically imitate students of varying skill levels, given that they tend to answer nearly everything correctly even when told to act like a weak student?
    - correct paper in top 10: yes; top 3: Evaluating and Improving Pedagogical Fit in LLM-Based AI Tut; Task Competence Is Not Instruction Following: Evaluating Ins; StudentBench: AI and human tutoring yield equivalent GRE lea
  - query: simulating student response accuracy with LLMs knowledge tracing persona of varying ability
    - correct paper in top 10: yes; top 3: From Mastery Profile to Simulated Response: Stochastic Stude; Evaluating and Improving Pedagogical Fit in LLM-Based AI Tut; Findings of the First Teaching Monster Challenge: A Benchmar

### q143 (vague)
**Question:** Does training a model to pick evidence before answering actually beat plain BM25 or hybrid retrieval on LongBench-v2 multiple choice?
**Correct paper:** When Learned Context Planning Fails to Beat Strong Retrieval: A Controlled Study of Planning, Routing, and Reranking for Long-Context QA (2609.26976)
**Dense rank:** 6   **Agent ranks, runs 1-3:** 2, 2, 2   **Searches:** 3, 3, 3

- Run 1:
  - query: Does training a model to pick evidence before answering actually beat plain BM25 or hybrid retrieval on LongBench-v2 multiple choice?
    - correct paper in top 10: yes; top 3: A decodability criterion predicts when hidden-state selectio; Assessing the Downstream Utility of Evidence-Aware Retrieval; Knowing Before Answering: Decoding Language Models for Relia
  - query: trained evidence selection before answer vs BM25 hybrid retrieval LongBench-v2 long-context multiple choice
    - correct paper in top 10: yes; top 3: Assessing the Downstream Utility of Evidence-Aware Retrieval; When Learned Context Planning Fails to Beat Strong Retrieval; RIMS: Preference Optimization via Smoothed Multi-pair Aggreg
  - query: learned evidence selection then answer generation outperforms BM25 and hybrid retrieval baselines on LongBench-v2 multiple-choice questions
    - correct paper in top 10: yes; top 3: Assessing the Downstream Utility of Evidence-Aware Retrieval; When Learned Context Planning Fails to Beat Strong Retrieval; RIMS: Preference Optimization via Smoothed Multi-pair Aggreg
- Run 2:
  - query: Does training a model to pick evidence before answering actually beat plain BM25 or hybrid retrieval on LongBench-v2 multiple choice?
    - correct paper in top 10: yes; top 3: A decodability criterion predicts when hidden-state selectio; Assessing the Downstream Utility of Evidence-Aware Retrieval; Knowing Before Answering: Decoding Language Models for Relia
  - query: trained evidence selection before answering vs BM25 hybrid retrieval LongBench-v2 long-context multiple choice
    - correct paper in top 10: yes; top 3: When Learned Context Planning Fails to Beat Strong Retrieval; Assessing the Downstream Utility of Evidence-Aware Retrieval; SeDeM: Selective Decompression of Hidden-State Memories for 
  - query: learned evidence selection trained retriever before answer LongBench-v2 outperforms BM25 hybrid retrieval baseline
    - correct paper in top 10: yes; top 3: Assessing the Downstream Utility of Evidence-Aware Retrieval; STEC: Evidence Compression for Deep Search in Open-domain Mu; Candidate-Constrained Retrieval-Augmented Generation for Lon
- Run 3:
  - query: Does training a model to pick evidence before answering actually beat plain BM25 or hybrid retrieval on LongBench-v2 multiple choice?
    - correct paper in top 10: yes; top 3: A decodability criterion predicts when hidden-state selectio; Assessing the Downstream Utility of Evidence-Aware Retrieval; Knowing Before Answering: Decoding Language Models for Relia
  - query: trained evidence selection before answer LongBench-v2 compared with BM25 and hybrid retrieval baselines
    - correct paper in top 10: yes; top 3: Assessing the Downstream Utility of Evidence-Aware Retrieval; STEC: Evidence Compression for Deep Search in Open-domain Mu; EvidentialRAG: Quantifying and Mitigating Information Confli
  - query: LongBench-v2 evidence extraction then answer reinforcement learning versus BM25 hybrid retrieval long-context multiple choice
    - correct paper in top 10: yes; top 3: When Learned Context Planning Fails to Beat Strong Retrieval; GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning f; STEC: Evidence Compression for Deep Search in Open-domain Mu

### q147 (specific)
**Question:** How can sentence-embedding similarity be used to track whether the diversity of language model outputs on open-ended prompts and divergent-thinking tests has changed across successive model releases?
**Correct paper:** Are LLMs becoming similarly creative? Evidence from three years of models (2608.19437)
**Dense rank:** 9   **Agent ranks, runs 1-3:** 1, 1, 1   **Searches:** 2, 2, 2

- Run 1:
  - query: How can sentence-embedding similarity be used to track whether the diversity of language model outputs on open-ended prompts and divergent-thinking tests has changed across successive model releases?
    - correct paper in top 10: yes; top 3: Apples to Apples? Towards Comparable Crosslingual Language M; Similarity All The Way Up: Multilingual Generalization in LL; Evaluating Multilingual Sentence Embeddings for Translation 
  - query: embedding-based semantic diversity of LLM generations across model versions creativity divergent thinking
    - correct paper in top 10: yes; top 3: Are LLMs becoming similarly creative? Evidence from three ye; CreativityNeuro: Steering Language Model Weights to Improve ; CreativeInstruct: Scalably Teaching LLMs to Balance Quality,
- Run 2:
  - query: How can sentence-embedding similarity be used to track whether the diversity of language model outputs on open-ended prompts and divergent-thinking tests has changed across successive model releases?
    - correct paper in top 10: yes; top 3: Apples to Apples? Towards Comparable Crosslingual Language M; Similarity All The Way Up: Multilingual Generalization in LL; Evaluating Multilingual Sentence Embeddings for Translation 
  - query: embedding-based semantic diversity of LLM generations across model versions creativity divergent thinking
    - correct paper in top 10: yes; top 3: Are LLMs becoming similarly creative? Evidence from three ye; CreativityNeuro: Steering Language Model Weights to Improve ; CreativeInstruct: Scalably Teaching LLMs to Balance Quality,
- Run 3:
  - query: How can sentence-embedding similarity be used to track whether the diversity of language model outputs on open-ended prompts and divergent-thinking tests has changed across successive model releases?
    - correct paper in top 10: yes; top 3: Apples to Apples? Towards Comparable Crosslingual Language M; Similarity All The Way Up: Multilingual Generalization in LL; Evaluating Multilingual Sentence Embeddings for Translation 
  - query: embedding-based semantic diversity of LLM generations across model versions creativity divergent thinking
    - correct paper in top 10: yes; top 3: Are LLMs becoming similarly creative? Evidence from three ye; CreativityNeuro: Steering Language Model Weights to Improve ; CreativeInstruct: Scalably Teaching LLMs to Balance Quality,

### q166 (problem)
**Question:** How can I decide which machine-generated training examples to keep when scoring each example independently fails to capture how samples interact, and what cheaper way is there to choose where interaction-aware scoring is most needed under a limited compute budget?
**Correct paper:** Effective Synthetic Data Curation Requires Group-Level Signals (2610.00779)
**Dense rank:** -   **Agent ranks, runs 1-3:** 4, 2, 3   **Searches:** 2, 3, 3

- Run 1:
  - query: How can I decide which machine-generated training examples to keep when scoring each example independently fails to capture how samples interact, and what cheaper way is there to choose where interaction-aware scoring is most needed under a limited compute budget?
    - correct paper in top 10: no; top 3: Critical-State RL: Diagnosing Trainable States for Multi-Tur; Task Competence Is Not Instruction Following: Evaluating Ins; Training-Aware Target Coverage for Synthetic Data Selection
  - query: synthetic data selection set-level interaction redundancy diversity subset selection beyond per-sample scores cheap proxy for when to use joint selection
    - correct paper in top 10: yes; top 3: Training-Aware Target Coverage for Synthetic Data Selection; Are Diversity Metrics Measuring Diversity? A Capability-Cont; Coresets Before Score Sets: Evaluation-Unsupervised Prompt S
- Run 2:
  - query: How can I decide which machine-generated training examples to keep when scoring each example independently fails to capture how samples interact, and what cheaper way is there to choose where interaction-aware scoring is most needed under a limited compute budget?
    - correct paper in top 10: no; top 3: Critical-State RL: Diagnosing Trainable States for Multi-Tur; Task Competence Is Not Instruction Following: Evaluating Ins; Training-Aware Target Coverage for Synthetic Data Selection
  - query: submodular data selection synthetic training examples diversity interaction-aware subset selection cheap proxy for where to score
    - correct paper in top 10: yes; top 3: Training-Aware Target Coverage for Synthetic Data Selection; Coresets Before Score Sets: Evaluation-Unsupervised Prompt S; CODS: Iterative Bellman-Residual Data Selection for Reusable
  - query: joint subset selection synthetic data interaction effects marginal utility scoring fails redundancy cheap estimator for when to use set-level selection
    - correct paper in top 10: no; top 3: Learning-Enabled Estimation: Tight Characterizations under S; Selection Bias Correction in Retail Intelligence; Offline Policy Evaluation as a decision support tool for des
- Run 3:
  - query: How can I decide which machine-generated training examples to keep when scoring each example independently fails to capture how samples interact, and what cheaper way is there to choose where interaction-aware scoring is most needed under a limited compute budget?
    - correct paper in top 10: no; top 3: Critical-State RL: Diagnosing Trainable States for Multi-Tur; Task Competence Is Not Instruction Following: Evaluating Ins; Training-Aware Target Coverage for Synthetic Data Selection
  - query: submodular data selection synthetic training examples diversity interaction-aware selection cheap proxy
    - correct paper in top 10: yes; top 3: Training-Aware Target Coverage for Synthetic Data Selection; Data Mixing as Mixture Experiment: Response Surface Methodol; Beyond Non-IID: Learner--Client Distribution Mismatch in Fed
  - query: joint subset selection synthetic data pairwise interaction redundancy influence functions cheap proxy for when to use set-level scoring
    - correct paper in top 10: yes; top 3: Training-Aware Target Coverage for Synthetic Data Selection; Coresets Before Score Sets: Evaluation-Unsupervised Prompt S; CODS: Iterative Bellman-Residual Data Selection for Reusable

### q233 (vague)
**Question:** paper about neural networks that go beyond pairwise connections, like hypergraph version of MLP?
**Correct paper:** Higher Structures in Deep Learning (2609.00472)
**Dense rank:** -   **Agent ranks, runs 1-3:** 5, 6, 4   **Searches:** 3, 3, 3

- Run 1:
  - query: paper about neural networks that go beyond pairwise connections, like hypergraph version of MLP?
    - correct paper in top 10: no; top 3: Every Layer Counts: An Exponential $L_2$ Depth Hierarchy for; MPP-GNN: Subject-Adaptive Community Detection for fMRI-Based; A concentration result for multilayer feedforward neural net
  - query: hypergraph neural network higher-order interactions beyond pairwise message passing
    - correct paper in top 10: yes; top 3: Schreier-Coset Graph Rewiring; $α$-Graph: Attention-Infused Normalizing Flow Approach to Tr; Efficient Dynamic Algorithms for Graph Neural Networks with 
  - query: hypergraph neural network multilayer perceptron higher-order relations hyperedges
    - correct paper in top 10: yes; top 3: From Abductive Explanations to Global Logical Rules for Node; Optimizing Hypergraph-Based RAG: Toward Better Fact Extracti; Higher Structures in Deep Learning
- Run 2:
  - query: paper about neural networks that go beyond pairwise connections, like hypergraph version of MLP?
    - correct paper in top 10: no; top 3: Every Layer Counts: An Exponential $L_2$ Depth Hierarchy for; MPP-GNN: Subject-Adaptive Community Detection for fMRI-Based; A concentration result for multilayer feedforward neural net
  - query: hypergraph neural network higher-order interactions beyond pairwise message passing
    - correct paper in top 10: yes; top 3: Schreier-Coset Graph Rewiring; $α$-Graph: Attention-Infused Normalizing Flow Approach to Tr; Efficient Dynamic Algorithms for Graph Neural Networks with 
  - query: hypergraph neural networks message passing on hyperedges set-based multilayer perceptron higher-order relations
    - correct paper in top 10: yes; top 3: Schreier-Coset Graph Rewiring; Higher Structures in Deep Learning; Subgraph Filtering for Fair Graph Neural Networks
- Run 3:
  - query: paper about neural networks that go beyond pairwise connections, like hypergraph version of MLP?
    - correct paper in top 10: no; top 3: Every Layer Counts: An Exponential $L_2$ Depth Hierarchy for; MPP-GNN: Subject-Adaptive Community Detection for fMRI-Based; A concentration result for multilayer feedforward neural net
  - query: hypergraph neural network higher-order interactions beyond pairwise message passing
    - correct paper in top 10: yes; top 3: Schreier-Coset Graph Rewiring; $α$-Graph: Attention-Infused Normalizing Flow Approach to Tr; Efficient Dynamic Algorithms for Graph Neural Networks with 
  - query: hypergraph neural network multilayer perceptron higher-order set interactions tensor
    - correct paper in top 10: yes; top 3: Higher Structures in Deep Learning; Iterative tensor network transformations for element-wise ev; Schreier-Coset Graph Rewiring

### q277 (problem)
**Question:** How can I tell whether a language model's answer is fabricated by analyzing the structure of its attention patterns in a single forward pass, rather than sampling multiple responses?
**Correct paper:** Detecting Hallucination in LLMs: Tracing the Topological Signatures of Impaired Context Sharing (2609.21096)
**Dense rank:** -   **Agent ranks, runs 1-3:** 2, 2, 2   **Searches:** 3, 3, 3

- Run 1:
  - query: How can I tell whether a language model's answer is fabricated by analyzing the structure of its attention patterns in a single forward pass, rather than sampling multiple responses?
    - correct paper in top 10: no; top 3: What Attention Recalls and Recurrence Controls in Hybrid Lan; How Strong Is the Evidence for the Artificial Hivemind? Reev; Diagnosing Correctness Probes under Self-Judgement Confoundi
  - query: hallucination detection from attention maps single forward pass without sampling
    - correct paper in top 10: yes; top 3: The Hallucination Signal Is a Mean Shift: Why Simple Probes ; Detecting Hallucination in LLMs: Tracing the Topological Sig; CrossHallu: Do Hallucination Signals Generalize Across Langu
  - query: attention entropy and attention graph features for detecting LLM hallucinations in one pass
    - correct paper in top 10: yes; top 3: Detecting Hallucination in LLMs: Tracing the Topological Sig; The Hallucination Signal Is a Mean Shift: Why Simple Probes ; CrossHallu: Do Hallucination Signals Generalize Across Langu
- Run 2:
  - query: How can I tell whether a language model's answer is fabricated by analyzing the structure of its attention patterns in a single forward pass, rather than sampling multiple responses?
    - correct paper in top 10: no; top 3: What Attention Recalls and Recurrence Controls in Hybrid Lan; How Strong Is the Evidence for the Artificial Hivemind? Reev; Diagnosing Correctness Probes under Self-Judgement Confoundi
  - query: hallucination detection from attention maps single forward pass without sampling
    - correct paper in top 10: yes; top 3: The Hallucination Signal Is a Mean Shift: Why Simple Probes ; Detecting Hallucination in LLMs: Tracing the Topological Sig; CrossHallu: Do Hallucination Signals Generalize Across Langu
  - query: attention entropy features hallucination detection single pass zero-shot self-check
    - correct paper in top 10: yes; top 3: The Hallucination Signal Is a Mean Shift: Why Simple Probes ; Detecting Hallucination in LLMs: Tracing the Topological Sig; CrossHallu: Do Hallucination Signals Generalize Across Langu
- Run 3:
  - query: How can I tell whether a language model's answer is fabricated by analyzing the structure of its attention patterns in a single forward pass, rather than sampling multiple responses?
    - correct paper in top 10: no; top 3: What Attention Recalls and Recurrence Controls in Hybrid Lan; How Strong Is the Evidence for the Artificial Hivemind? Reev; Diagnosing Correctness Probes under Self-Judgement Confoundi
  - query: hallucination detection from attention maps single forward pass without sampling
    - correct paper in top 10: yes; top 3: The Hallucination Signal Is a Mean Shift: Why Simple Probes ; Detecting Hallucination in LLMs: Tracing the Topological Sig; CrossHallu: Do Hallucination Signals Generalize Across Langu
  - query: attention entropy features hallucination detection single pass transformer
    - correct paper in top 10: yes; top 3: The Hallucination Signal Is a Mean Shift: Why Simple Probes ; Detecting Hallucination in LLMs: Tracing the Topological Sig; CrossHallu: Do Hallucination Signals Generalize Across Langu

### q290 (vague)
**Question:** Is there a way to make BPE vocab more efficient by hiding rarely-used intermediate merge tokens and giving their slots to better ones?
**Correct paper:** Pruned BPE: Post-training Visibility Pruning and Token Reallocation for Byte Pair Encoding (2608.00837)
**Dense rank:** 6   **Agent ranks, runs 1-3:** 2, 2, 1   **Searches:** 2, 2, 2

- Run 1:
  - query: Is there a way to make BPE vocab more efficient by hiding rarely-used intermediate merge tokens and giving their slots to better ones?
    - correct paper in top 10: yes; top 3: TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM; ESF-Bench: Benchmarking Challenging Slot-Filling Scenarios f; Vowel Signs Are Not Letters: A Pre-tokenization Ceiling on M
  - query: BPE vocabulary pruning removing unused merge tokens reallocating vocabulary slots
    - correct paper in top 10: yes; top 3: Pruned BPE: Post-training Visibility Pruning and Token Reall; The Functionalizer: Lossless Functional Decomposition for Su; Vowel Signs Are Not Letters: A Pre-tokenization Ceiling on M
- Run 2:
  - query: Is there a way to make BPE vocab more efficient by hiding rarely-used intermediate merge tokens and giving their slots to better ones?
    - correct paper in top 10: yes; top 3: TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM; ESF-Bench: Benchmarking Challenging Slot-Filling Scenarios f; Vowel Signs Are Not Letters: A Pre-tokenization Ceiling on M
  - query: BPE vocabulary pruning removing unused merge tokens reallocating vocabulary slots
    - correct paper in top 10: yes; top 3: Pruned BPE: Post-training Visibility Pruning and Token Reall; The Functionalizer: Lossless Functional Decomposition for Su; Vowel Signs Are Not Letters: A Pre-tokenization Ceiling on M
- Run 3:
  - query: Is there a way to make BPE vocab more efficient by hiding rarely-used intermediate merge tokens and giving their slots to better ones?
    - correct paper in top 10: yes; top 3: TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM; ESF-Bench: Benchmarking Challenging Slot-Filling Scenarios f; Vowel Signs Are Not Letters: A Pre-tokenization Ceiling on M
  - query: BPE vocabulary pruning removing unused intermediate merges reallocating vocabulary slots
    - correct paper in top 10: yes; top 3: Pruned BPE: Post-training Visibility Pruning and Token Reall; The Functionalizer: Lossless Functional Decomposition for Su; Where to cut, how deep: BPE and Unigram-LM on chemistry SMIL

## Lost (dense had it in the top 5, agent missed it in at least one run)

### q035 (vague)
**Question:** Is there a runtime that checks LLM-written data-processing code and swaps it for a memory-bounded implementation so agent tool calls don't blow up on big files?
**Correct paper:** SkillEffect: Checked Lowering for Memory-Bounded Agent Tools (2608.17007)
**Dense rank:** 2   **Agent ranks, runs 1-3:** 1, 1, 7   **Searches:** 3, 2, 3

- Run 1:
  - query: Is there a runtime that checks LLM-written data-processing code and swaps it for a memory-bounded implementation so agent tool calls don't blow up on big files?
    - correct paper in top 10: yes; top 3: Look Before You Leap: Pre-Action Verification for LLM Agents; SkillEffect: Checked Lowering for Memory-Bounded Agent Tools; Auto: The AGI Compiler
  - query: rewrite LLM-generated pandas code to streaming chunked execution memory limit agent data analysis
    - correct paper in top 10: yes; top 3: PLSQLBench: Benchmarking LLM Systems for Executable Procedur; LeanStream: A Speculate-and-Refine Streaming Framework for E; Agentic Coding in the Wild: Characterizing GitHub Copilot Tr
  - query: compile LLM agent tool code to bounded-memory streaming operators runtime rewrite out-of-core data processing
    - correct paper in top 10: yes; top 3: SkillEffect: Checked Lowering for Memory-Bounded Agent Tools; Agentic Coding in the Wild: Characterizing GitHub Copilot Tr; Learning Agent Execution for KV-Cache Management in Agentic 
- Run 2:
  - query: Is there a runtime that checks LLM-written data-processing code and swaps it for a memory-bounded implementation so agent tool calls don't blow up on big files?
    - correct paper in top 10: yes; top 3: Look Before You Leap: Pre-Action Verification for LLM Agents; SkillEffect: Checked Lowering for Memory-Bounded Agent Tools; Auto: The AGI Compiler
  - query: rewriting LLM-generated pandas code to streaming chunked execution for out-of-memory avoidance in agent tools
    - correct paper in top 10: yes; top 3: Agentic Coding in the Wild: Characterizing GitHub Copilot Tr; SkillEffect: Checked Lowering for Memory-Bounded Agent Tools; Context as an Environment: Programmatic Context Management f
- Run 3:
  - query: Is there a runtime that checks LLM-written data-processing code and swaps it for a memory-bounded implementation so agent tool calls don't blow up on big files?
    - correct paper in top 10: yes; top 3: Look Before You Leap: Pre-Action Verification for LLM Agents; SkillEffect: Checked Lowering for Memory-Bounded Agent Tools; Auto: The AGI Compiler
  - query: rewriting LLM-generated pandas code to streaming or chunked execution to bound memory on large files
    - correct paper in top 10: no; top 3: LeanStream: A Speculate-and-Refine Streaming Framework for E; HyperZip: Efficient Data Compression through Personalized Di; BlockServe: Block-Grained Continuous Batching for High-Throu
  - query: compiler pass that lowers LLM-generated dataframe code to out-of-core memory-bounded execution for agent tool calls
    - correct paper in top 10: yes; top 3: The Bitter Lesson of Tool Calling; SkillEffect: Checked Lowering for Memory-Bounded Agent Tools; PLSQLBench: Benchmarking LLM Systems for Executable Procedur

### q135 (specific)
**Question:** How can retrieval-augmented language models, thermal infrared imaging, vision foundation models, and wireless sensing be combined into one pipeline for assessing structural damage, and does graph-based retrieval outperform vector-based retrieval for questions that span multiple documents?
**Correct paper:** Integrated Multimodal AI System for Retrieval-Augmented Reasoning, Object Sensing, and Damage Analysis (2608.08935)
**Dense rank:** 1   **Agent ranks, runs 1-3:** 6, 1, 1   **Searches:** 3, 3, 2

- Run 1:
  - query: How can retrieval-augmented language models, thermal infrared imaging, vision foundation models, and wireless sensing be combined into one pipeline for assessing structural damage, and does graph-based retrieval outperform vector-based retrieval for questions that span multiple documents?
    - correct paper in top 10: yes; top 3: Integrated Multimodal AI System for Retrieval-Augmented Reas; TRIAGE: Trustworthy Retrieval Instrumentation And Graph Eval; Less Is More: Graph-free Multimodal RAG via Multi-signal Lat
  - query: multimodal structural damage assessment pipeline thermal infrared vision foundation model wireless sensing retrieval-augmented LLM knowledge graph
    - correct paper in top 10: yes; top 3: Integrated Multimodal AI System for Retrieval-Augmented Reas; Constructing Dynamic Master Logic Models as Knowledge Graphs; AISA: AI Safety Assistant Framework for Continuous Improveme
  - query: graph RAG versus vector RAG multi-document multi-hop question answering comparison
    - correct paper in top 10: no; top 3: SelfGraphRAG: Bridging the Supervision Gap in Graph-Based RA; Less Is More: Graph-free Multimodal RAG via Multi-signal Lat; Automating Multi-Hop RAG Evaluation via TRIAD: From Context 
- Run 2:
  - query: How can retrieval-augmented language models, thermal infrared imaging, vision foundation models, and wireless sensing be combined into one pipeline for assessing structural damage, and does graph-based retrieval outperform vector-based retrieval for questions that span multiple documents?
    - correct paper in top 10: yes; top 3: Integrated Multimodal AI System for Retrieval-Augmented Reas; TRIAGE: Trustworthy Retrieval Instrumentation And Graph Eval; Less Is More: Graph-free Multimodal RAG via Multi-signal Lat
  - query: multimodal structural health monitoring pipeline thermal infrared wireless sensing vision foundation model retrieval-augmented LLM graph RAG comparison
    - correct paper in top 10: yes; top 3: Integrated Multimodal AI System for Retrieval-Augmented Reas; TRACE: Learning to Self-Calibrate Wireless Digital Twins fro; Robust Fault Detection in Mechanical Multimodal Time Series 
  - query: graph-based versus vector retrieval multi-hop multi-document question answering comparison GraphRAG structural engineering damage assessment
    - correct paper in top 10: yes; top 3: SelfGraphRAG: Bridging the Supervision Gap in Graph-Based RA; Less Is More: Graph-free Multimodal RAG via Multi-signal Lat; STEC: Evidence Compression for Deep Search in Open-domain Mu
- Run 3:
  - query: How can retrieval-augmented language models, thermal infrared imaging, vision foundation models, and wireless sensing be combined into one pipeline for assessing structural damage, and does graph-based retrieval outperform vector-based retrieval for questions that span multiple documents?
    - correct paper in top 10: yes; top 3: Integrated Multimodal AI System for Retrieval-Augmented Reas; TRIAGE: Trustworthy Retrieval Instrumentation And Graph Eval; Less Is More: Graph-free Multimodal RAG via Multi-signal Lat
  - query: multimodal structural health monitoring pipeline thermal infrared wireless sensing vision foundation model LLM retrieval graph RAG damage assessment
    - correct paper in top 10: yes; top 3: Integrated Multimodal AI System for Retrieval-Augmented Reas; Robust Fault Detection in Mechanical Multimodal Time Series ; TRACE: Learning to Self-Calibrate Wireless Digital Twins fro

### q140 (vague)
**Question:** Is there a transformer that feeds the last layer's hidden state back in as the next input instead of just the sampled token?
**Correct paper:** Full-bandwidth transformer (2608.08888)
**Dense rank:** 1   **Agent ranks, runs 1-3:** -, 5, 4   **Searches:** 3, 3, 3

- Run 1:
  - query: Is there a transformer that feeds the last layer's hidden state back in as the next input instead of just the sampled token?
    - correct paper in top 10: yes; top 3: Full-bandwidth transformer; Rotate the Loop: Blockwise Conformality for Looped Transform; Maglev: Sliding Recurrent Memory
  - query: continuous thought hidden state recurrence fed back as next input embedding instead of discrete token sampling
    - correct paper in top 10: no; top 3: Register Tokens for Bounded-State Reasoning in Diffusion Lan; Training Continuous Chain of Thought Models: A Tale of Two R; What Attention Recalls and Recurrence Controls in Hybrid Lan
  - query: Coconut continuous latent reasoning last hidden state fed back as input embedding
    - correct paper in top 10: no; top 3: Training Continuous Chain of Thought Models: A Tale of Two R; Reason Through the Latent! Making Latent Visual Reasoning Ne; A*-Thought-V2: Efficient Latent Reasoning via Geometric Dyna
- Run 2:
  - query: Is there a transformer that feeds the last layer's hidden state back in as the next input instead of just the sampled token?
    - correct paper in top 10: yes; top 3: Full-bandwidth transformer; Rotate the Loop: Blockwise Conformality for Looped Transform; Maglev: Sliding Recurrent Memory
  - query: continuous thought feedback last hidden state as next input embedding transformer without token sampling
    - correct paper in top 10: yes; top 3: Full-bandwidth transformer; Looped Latent Attention: Cross-Loop KV Compression for Loope; Maglev: Sliding Recurrent Memory
  - query: Coconut continuous latent reasoning hidden state fed back as input embedding
    - correct paper in top 10: no; top 3: Training Continuous Chain of Thought Models: A Tale of Two R; Reason Through the Latent! Making Latent Visual Reasoning Ne; A*-Thought-V2: Efficient Latent Reasoning via Geometric Dyna
- Run 3:
  - query: Is there a transformer that feeds the last layer's hidden state back in as the next input instead of just the sampled token?
    - correct paper in top 10: yes; top 3: Full-bandwidth transformer; Rotate the Loop: Blockwise Conformality for Looped Transform; Maglev: Sliding Recurrent Memory
  - query: continuous latent thought feeding last hidden state back as next input embedding, Coconut chain of continuous thought
    - correct paper in top 10: no; top 3: Training Continuous Chain of Thought Models: A Tale of Two R; A*-Thought-V2: Efficient Latent Reasoning via Geometric Dyna; Reason Through the Latent! Making Latent Visual Reasoning Ne
  - query: recurrent transformer feeding final-layer hidden state back as input embedding for next position, bypassing token sampling, hidden state recurrence
    - correct paper in top 10: yes; top 3: Maglev: Sliding Recurrent Memory; Rotate the Loop: Blockwise Conformality for Looped Transform; Full-bandwidth transformer

### q151 (problem)
**Question:** How can computational stylometric analysis determine whether the third Gospel and the book describing the early church's history were composed by the same writer?
**Correct paper:** Is Luke the Author of a Gospel and the Acts of the Apostles? (2609.17762)
**Dense rank:** 1   **Agent ranks, runs 1-3:** 1, 1, -   **Searches:** 1, 2, 2

- Run 1:
  - query: How can computational stylometric analysis determine whether the third Gospel and the book describing the early church's history were composed by the same writer?
    - correct paper in top 10: yes; top 3: Is Luke the Author of a Gospel and the Acts of the Apostles?; Writing Style Similarity Reflects Academic Genealogy; Abstractiveness Metrics for Evaluating Text Summarization: A
- Run 2:
  - query: How can computational stylometric analysis determine whether the third Gospel and the book describing the early church's history were composed by the same writer?
    - correct paper in top 10: yes; top 3: Is Luke the Author of a Gospel and the Acts of the Apostles?; Writing Style Similarity Reflects Academic Genealogy; Abstractiveness Metrics for Evaluating Text Summarization: A
  - query: stylometry Lukan authorship Gospel of Luke Acts function word analysis
    - correct paper in top 10: yes; top 3: Is Luke the Author of a Gospel and the Acts of the Apostles?; AuthBench: A Large-Scale Multilingual Benchmark for Authorsh; Sparse Readout Prism: Explaining Logit-Lens Scores in Featur
- Run 3:
  - query: How can computational stylometric analysis determine whether the third Gospel and the book describing the early church's history were composed by the same writer?
    - correct paper in top 10: yes; top 3: Is Luke the Author of a Gospel and the Acts of the Apostles?; Writing Style Similarity Reflects Academic Genealogy; Abstractiveness Metrics for Evaluating Text Summarization: A
  - query: stylometry Luke-Acts authorship attribution function words computational analysis
    - correct paper in top 10: no; top 3: AuthBench: A Large-Scale Multilingual Benchmark for Authorsh; CHiPS: Character Histograms and Positional Signals for Light; Writing Style Similarity Reflects Academic Genealogy

### q186 (specific)
**Question:** How can a JEPA-style latent world model be trained so that the most predictive information is packed into the leading coordinates of a wide embedding, allowing planning with only a short prefix of the latent?
**Correct paper:** Adaptive Latent Capacity for World Models (2609.32921)
**Dense rank:** 2   **Agent ranks, runs 1-3:** 9, 6, 8   **Searches:** 3, 3, 3

- Run 1:
  - query: How can a JEPA-style latent world model be trained so that the most predictive information is packed into the leading coordinates of a wide embedding, allowing planning with only a short prefix of the latent?
    - correct paper in top 10: yes; top 3: JEPA-TTT: Persistent Test-Time Training of Latent World Mode; Adaptive Latent Capacity for World Models; Spectral-Target Physical Latent Structuring for JEPA-Style W
  - query: nested dropout ordered representations JEPA world model prefix planning latent truncation
    - correct paper in top 10: no; top 3: Reusing Rollouts under Policy Lag: Prefix-Normalized Policy ; Latent-Kernel Discrete Flow Maps for Few-Step Generation; NCP-ArchPreview Technical Report: Moving towards Latent Spac
  - query: matryoshka representation learning world model JEPA coarse-to-fine latent planning
    - correct paper in top 10: yes; top 3: JEPA-TTT: Persistent Test-Time Training of Latent World Mode; Spectral-Target Physical Latent Structuring for JEPA-Style W; Behavioral Monitoring of JEPA World Models with Jacobian Cen
- Run 2:
  - query: How can a JEPA-style latent world model be trained so that the most predictive information is packed into the leading coordinates of a wide embedding, allowing planning with only a short prefix of the latent?
    - correct paper in top 10: yes; top 3: JEPA-TTT: Persistent Test-Time Training of Latent World Mode; Adaptive Latent Capacity for World Models; Spectral-Target Physical Latent Structuring for JEPA-Style W
  - query: nested dropout or matryoshka representation JEPA world model prefix latent planning coarse-to-fine ordering
    - correct paper in top 10: no; top 3: JEPA-TTT: Persistent Test-Time Training of Latent World Mode; Reusing Rollouts under Policy Lag: Prefix-Normalized Policy ; Latent Memory Palace: Reasoning for Control as Autoregressiv
  - query: Matryoshka JEPA latent world model nested representations truncated embedding prefix planning
    - correct paper in top 10: yes; top 3: JEPA-TTT: Persistent Test-Time Training of Latent World Mode; Spectral-Target Physical Latent Structuring for JEPA-Style W; NCP-ArchPreview Technical Report: Moving towards Latent Spac
- Run 3:
  - query: How can a JEPA-style latent world model be trained so that the most predictive information is packed into the leading coordinates of a wide embedding, allowing planning with only a short prefix of the latent?
    - correct paper in top 10: yes; top 3: JEPA-TTT: Persistent Test-Time Training of Latent World Mode; Adaptive Latent Capacity for World Models; Spectral-Target Physical Latent Structuring for JEPA-Style W
  - query: nested dropout ordered representations JEPA world model prefix planning
    - correct paper in top 10: no; top 3: Behavioral Monitoring of JEPA World Models with Jacobian Cen; MDN-VJEPA: Multimodal Probabilistic Joint-Embedding World Mo; Reusing Rollouts under Policy Lag: Prefix-Normalized Policy 
  - query: matryoshka representation learning world model latent prefix coarse-to-fine planning joint embedding predictive
    - correct paper in top 10: yes; top 3: Spectral-Target Physical Latent Structuring for JEPA-Style W; Adaptive Latent Capacity for World Models; MDN-VJEPA: Multimodal Probabilistic Joint-Embedding World Mo

### q207 (specific)
**Question:** How can one causally test whether the recurrent hidden state of a meta-learned reinforcement learning update rule helps or hurts by pinning, freezing, or transplanting it while keeping the learned meta-parameters fixed?
**Correct paper:** Self-discovering RL in the Era of Experience: Is Learning History an Asset or a Burden? (2609.35897)
**Dense rank:** 5   **Agent ranks, runs 1-3:** -, -, 7   **Searches:** 3, 3, 3

- Run 1:
  - query: How can one causally test whether the recurrent hidden state of a meta-learned reinforcement learning update rule helps or hurts by pinning, freezing, or transplanting it while keeping the learned meta-parameters fixed?
    - correct paper in top 10: yes; top 3: When Validation Stops Learning: Auditing Update Admission fo; Understanding LLM Parameter Update Sparsity through the Lens; When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k 
  - query: causal ablation of hidden state in learned reinforcement learning update rule meta-learning
    - correct paper in top 10: yes; top 3: From Static Policies to Adaptive Priors in Offline Reinforce; Understanding LLM Parameter Update Sparsity through the Lens; Improving Offline Goal-Conditioned Reinforcement Learning vi
  - query: learned optimizer LSTM hidden state intervention reset freeze transplant meta-trained update rule reinforcement learning ablation
    - correct paper in top 10: no; top 3: SafeExplorer: An Unbiased Policy Gradient for Reinforcement ; CODS: Iterative Bellman-Residual Data Selection for Reusable; Constrained Flow Policy Updates: A Generalized Schrödinger B
- Run 2:
  - query: How can one causally test whether the recurrent hidden state of a meta-learned reinforcement learning update rule helps or hurts by pinning, freezing, or transplanting it while keeping the learned meta-parameters fixed?
    - correct paper in top 10: yes; top 3: When Validation Stops Learning: Auditing Update Admission fo; Understanding LLM Parameter Update Sparsity through the Lens; When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k 
  - query: causal ablation of hidden state in learned reinforcement learning update rule meta-learned LSTM optimizer
    - correct paper in top 10: no; top 3: Reusing Rollouts under Policy Lag: Prefix-Normalized Policy ; Understanding LLM Parameter Update Sparsity through the Lens; Constrained Flow Policy Updates: A Generalized Schrödinger B
  - query: learned optimizer recurrent state intervention meta-learned RL update rule hidden state reset transplant ablation
    - correct paper in top 10: no; top 3: A Reproducibility Study of Partial Residual Ablations in Pre; Represent, Then Generate: Multimodal-Conditioned Time-Series; Large Language Models as Unified Multimodal Learners for Cli
- Run 3:
  - query: How can one causally test whether the recurrent hidden state of a meta-learned reinforcement learning update rule helps or hurts by pinning, freezing, or transplanting it while keeping the learned meta-parameters fixed?
    - correct paper in top 10: yes; top 3: When Validation Stops Learning: Auditing Update Admission fo; Understanding LLM Parameter Update Sparsity through the Lens; When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k 
  - query: ablating recurrent state of learned RL update rule meta-learned LSTM optimizer hidden state intervention
    - correct paper in top 10: no; top 3: Efficient Long-Horizon Learning for Learned Optimization; Train Smarter, Not Harder: Switching Signal-Guided Training ; Lyapunov Guidance: A Unified Framework for Stabilizing Gener
  - query: learned policy gradient update rule recurrent memory causal intervention reset hidden state meta-learned drift discovery
    - correct paper in top 10: no; top 3: PolicyAttention: Softmax Attention Implements Policy Mirror ; Understanding LLM Parameter Update Sparsity through the Lens; SafeExplorer: An Unbiased Policy Gradient for Reinforcement 

### q259 (problem)
**Question:** How can a language model trained on only 10 million words of text be made to learn more effectively, generalize to unseen inputs, and keep earlier capabilities, and what general guidance explains how to arrange limited training data to achieve this?
**Correct paper:** Data-Efficient Language Modeling: From Frontier Advancement to Principle-Guided Model Improvement (2609.10702)
**Dense rank:** 1   **Agent ranks, runs 1-3:** 2, 3, 6   **Searches:** 3, 3, 3

- Run 1:
  - query: How can a language model trained on only 10 million words of text be made to learn more effectively, generalize to unseen inputs, and keep earlier capabilities, and what general guidance explains how to arrange limited training data to achieve this?
    - correct paper in top 10: yes; top 3: Data-Efficient Language Modeling: From Frontier Advancement ; Optimal Model Activation Policies for Inference Networks of ; What Should Data Teach? Moving Bottlenecks Across Circuit, S
  - query: BabyLM 10 million words data-efficient pretraining curriculum catastrophic forgetting
    - correct paper in top 10: no; top 3: What Should Data Teach? Moving Bottlenecks Across Circuit, S; When Synthetic Data Hurts: On Catastrophic Forgetting in Ski; AgentBrew: Lifelong Knowledge Brewing from Strong Teachers t
  - query: BabyLM challenge strict-small track 10M words pretraining language model sample efficiency
    - correct paper in top 10: yes; top 3: Data-Efficient Language Modeling: From Frontier Advancement ; Feeding BabyLMs Macaroni: Code-Switching Curricula Cause Cro; Selecting Open-Weight Language Models for Zero-Shot Intent C
- Run 2:
  - query: How can a language model trained on only 10 million words of text be made to learn more effectively, generalize to unseen inputs, and keep earlier capabilities, and what general guidance explains how to arrange limited training data to achieve this?
    - correct paper in top 10: yes; top 3: Data-Efficient Language Modeling: From Frontier Advancement ; Optimal Model Activation Policies for Inference Networks of ; What Should Data Teach? Moving Bottlenecks Across Circuit, S
  - query: BabyLM challenge 10 million words data-efficient pretraining curriculum catastrophic forgetting
    - correct paper in top 10: no; top 3: What Should Data Teach? Moving Bottlenecks Across Circuit, S; When Synthetic Data Hurts: On Catastrophic Forgetting in Ski; Feeding BabyLMs Macaroni: Code-Switching Curricula Cause Cro
  - query: BabyLM strict-small track 10M words pretraining techniques generalization retention
    - correct paper in top 10: yes; top 3: Relative Generalization Invariance of LLM Pretraining; Learned, Then Lost: A Measured Single-Example Counterfactual; Don't Repeat Yourself: Self-Supervised Fine-Tuning for Cover
- Run 3:
  - query: How can a language model trained on only 10 million words of text be made to learn more effectively, generalize to unseen inputs, and keep earlier capabilities, and what general guidance explains how to arrange limited training data to achieve this?
    - correct paper in top 10: yes; top 3: Data-Efficient Language Modeling: From Frontier Advancement ; Optimal Model Activation Policies for Inference Networks of ; What Should Data Teach? Moving Bottlenecks Across Circuit, S
  - query: BabyLM 10 million words curriculum learning continual learning catastrophic forgetting data arrangement
    - correct paper in top 10: no; top 3: When Synthetic Data Hurts: On Catastrophic Forgetting in Ski; Federated Continual Learning as a Distributed Drift-Plus-Pen; When Does Continual Learning Require Learning
  - query: BabyLM challenge strict-small track sample-efficient pretraining 10M words
    - correct paper in top 10: no; top 3: Edge Phoneme Recognition for Children's Speech through Age-A; Feeding BabyLMs Macaroni: Code-Switching Curricula Cause Cro; NL-PAC: Specification Ambiguity and Certified Minimax Risk F

### q297 (specific)
**Question:** Do features derived from phase structure in attention add predictive power beyond a combined baseline when forecasting contradiction outcomes or answer changes under repeated pressure prompts?
**Correct paper:** Two tests of phase-structure features for transition prediction (2609.00335)
**Dense rank:** 1   **Agent ranks, runs 1-3:** 5, 9, 1   **Searches:** 3, 3, 3

- Run 1:
  - query: Do features derived from phase structure in attention add predictive power beyond a combined baseline when forecasting contradiction outcomes or answer changes under repeated pressure prompts?
    - correct paper in top 10: yes; top 3: Two tests of phase-structure features for transition predict; Ordered Network Analysis of Epistemic Emotions during Collab; Prompt Robustness Is Task-Dependent: Comparing Objective and
  - query: attention phase features predict answer flips under repeated pushback LLM incremental predictive value over baseline
    - correct paper in top 10: no; top 3: What Attention Recalls and Recurrence Controls in Hybrid Lan; Uncertainty-gated selection for block-sparse attention; Route, Don't Fix: Regime-Dependent Decoding Correction and a
  - query: phase-locking value attention heads sycophancy flip prediction incremental AUC over logit baseline
    - correct paper in top 10: no; top 3: Maglev: Sliding Recurrent Memory; Train Smarter, Not Harder: Switching Signal-Guided Training ; Linear Attention Architectures: Mechanisms, Trade-offs, and 
- Run 2:
  - query: Do features derived from phase structure in attention add predictive power beyond a combined baseline when forecasting contradiction outcomes or answer changes under repeated pressure prompts?
    - correct paper in top 10: yes; top 3: Two tests of phase-structure features for transition predict; Ordered Network Analysis of Epistemic Emotions during Collab; Prompt Robustness Is Task-Dependent: Comparing Objective and
  - query: attention phase features predict answer flips under repeated pressure prompts sycophancy contradiction forecasting
    - correct paper in top 10: yes; top 3: What Attention Recalls and Recurrence Controls in Hybrid Lan; Tracing mechanisms of sycophantic agreement in language mode; Clarification Is Not Correction: LLMs Fail to Let Go
  - query: phase-locking attention heads oscillatory dynamics predict LLM sycophancy belief flip under repeated pushback baseline logit features
    - correct paper in top 10: no; top 3: Detecting Hallucination in LLMs: Tracing the Topological Sig; Behavioral Latency as Weak Event-Time Supervision for EEG Re; The Hallucination Signal Is a Mean Shift: Why Simple Probes 
- Run 3:
  - query: Do features derived from phase structure in attention add predictive power beyond a combined baseline when forecasting contradiction outcomes or answer changes under repeated pressure prompts?
    - correct paper in top 10: yes; top 3: Two tests of phase-structure features for transition predict; Ordered Network Analysis of Epistemic Emotions during Collab; Prompt Robustness Is Task-Dependent: Comparing Objective and
  - query: attention phase features predict answer flips sycophancy repeated pushback LLM incremental predictive validity
    - correct paper in top 10: yes; top 3: Tracing mechanisms of sycophantic agreement in language mode; Two tests of phase-structure features for transition predict; Jagged Judges: Epistemic Stability Under Perturbation, Press
  - query: phase structure attention heads incremental validity contradiction forecasting pressure prompts combined baseline
    - correct paper in top 10: yes; top 3: Two tests of phase-structure features for transition predict; Lévy Attention: Single-Pass Predictive Uncertainty for Conti; Capability Emergence Can Be Forecast: Per-Seed, In Advance, 

## Never found (dense and all 3 agent runs missed the top 5)

### q001 (problem)
**Question:** How can we make studies measuring whether AI assistance meaningfully helps non-experts plan chemical, biological, radiological, or nuclear attacks comparable across research efforts, given inconsistent definitions of who counts as a non-expert, differing threat scopes, baselines, scoring rubrics, and decision rules?
**Correct paper:** A Threshold Exceedance Framework for CBRN Uplift Evaluation in Frontier Language Models (2607.12200)
**Dense rank:** 8   **Agent ranks, runs 1-3:** 8, 8, 8   **Searches:** 1, 1, 1

- Run 1:
  - query: How can we make studies measuring whether AI assistance meaningfully helps non-experts plan chemical, biological, radiological, or nuclear attacks comparable across research efforts, given inconsistent definitions of who counts as a non-expert, differing threat scopes, baselines, scoring rubrics, and decision rules?
    - correct paper in top 10: yes; top 3: Real-World Evaluation of an AI Agent Drafting Translational ; Defining and Categorising Human-AI Interactions in Clinical ; The Agentic Garden of Forking Paths
- Run 2:
  - query: How can we make studies measuring whether AI assistance meaningfully helps non-experts plan chemical, biological, radiological, or nuclear attacks comparable across research efforts, given inconsistent definitions of who counts as a non-expert, differing threat scopes, baselines, scoring rubrics, and decision rules?
    - correct paper in top 10: yes; top 3: Real-World Evaluation of an AI Agent Drafting Translational ; Defining and Categorising Human-AI Interactions in Clinical ; The Agentic Garden of Forking Paths
- Run 3:
  - query: How can we make studies measuring whether AI assistance meaningfully helps non-experts plan chemical, biological, radiological, or nuclear attacks comparable across research efforts, given inconsistent definitions of who counts as a non-expert, differing threat scopes, baselines, scoring rubrics, and decision rules?
    - correct paper in top 10: yes; top 3: Real-World Evaluation of an AI Agent Drafting Translational ; Defining and Categorising Human-AI Interactions in Clinical ; The Agentic Garden of Forking Paths

### q011 (vague)
**Question:** Is there a small ~2B open language model where they compared training with vs. without instruction-style data in the pretraining corpus?
**Correct paper:** Index SLM Technical Report (2607.09885)
**Dense rank:** 6   **Agent ranks, runs 1-3:** -, -, -   **Searches:** 3, 3, 3

- Run 1:
  - query: Is there a small ~2B open language model where they compared training with vs. without instruction-style data in the pretraining corpus?
    - correct paper in top 10: yes; top 3: Task Competence Is Not Instruction Following: Evaluating Ins; Relative Generalization Invariance of LLM Pretraining; IKS-Instruct: A 24,000-Example Multilingual Dataset for Teac
  - query: pretraining from scratch with and without instruction data mixed into pretraining corpus 2B parameter model ablation
    - correct paper in top 10: no; top 3: Learned, Then Lost: A Measured Single-Example Counterfactual; NAVER LABS System Re-implementation for the IWSLT 2026 Instr; What Should Data Teach? Moving Bottlenecks Across Circuit, S
  - query: OLMo or MiniCPM pretraining data ablation instruction-formatted data included in pretraining mix versus excluded small model
    - correct paper in top 10: no; top 3: A Reproducibility Study of Partial Residual Ablations in Pre; What Should Data Teach? Moving Bottlenecks Across Circuit, S; Small Models Scout Bottleneck Order for Large-Model Data Con
- Run 2:
  - query: Is there a small ~2B open language model where they compared training with vs. without instruction-style data in the pretraining corpus?
    - correct paper in top 10: yes; top 3: Task Competence Is Not Instruction Following: Evaluating Ins; Relative Generalization Invariance of LLM Pretraining; IKS-Instruct: A 24,000-Example Multilingual Dataset for Teac
  - query: pretraining corpus ablation with and without instruction data small 2B model open weights
    - correct paper in top 10: no; top 3: Learned, Then Lost: A Measured Single-Example Counterfactual; ResonatorLM: Causal Resonant Field Mixing for Efficient Long; MechaTerp-TRACE: A Novel Approach for Component Ablation Ana
  - query: OLMo or Gemma-style 2B pretraining mixture ablation: instruction-formatted data included vs excluded in pretraining, from-scratch small LM
    - correct paper in top 10: no; top 3: A Reproducibility Study of Partial Residual Ablations in Pre; Represent, Then Generate: Multimodal-Conditioned Time-Series; Matched-Input Estimates Differ in Sign Across Architectures:
- Run 3:
  - query: Is there a small ~2B open language model where they compared training with vs. without instruction-style data in the pretraining corpus?
    - correct paper in top 10: yes; top 3: Task Competence Is Not Instruction Following: Evaluating Ins; Relative Generalization Invariance of LLM Pretraining; IKS-Instruct: A 24,000-Example Multilingual Dataset for Teac
  - query: pretraining with and without instruction data ablation 2B parameter model OLMo SmolLM
    - correct paper in top 10: no; top 3: NAVER LABS System Re-implementation for the IWSLT 2026 Instr; Beyond Retraining-Free MoE Compression: A Cost-Normalized St; OmniEdu: Open Foundation Models for Learning and Teaching
  - query: instruction data mixed into pretraining corpus ablation small language model 2B from scratch versus no instruction data
    - correct paper in top 10: no; top 3: Task Competence Is Not Instruction Following: Evaluating Ins; What Should Data Teach? Moving Bottlenecks Across Circuit, S; MechaTerp-TRACE: A Novel Approach for Component Ablation Ana

### q063 (specific)
**Question:** How can pre-computed key-value attention states be saved and restored into a new context so a frozen small language model reproduces identical outputs without recomputation, while gaining accuracy on competition math and cutting decode cost?
**Correct paper:** Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel (2607.14431)
**Dense rank:** -   **Agent ranks, runs 1-3:** -, -, -   **Searches:** 2, 3, 2

- Run 1:
  - query: How can pre-computed key-value attention states be saved and restored into a new context so a frozen small language model reproduces identical outputs without recomputation, while gaining accuracy on competition math and cutting decode cost?
    - correct paper in top 10: no; top 3: What Attention Recalls and Recurrence Controls in Hybrid Lan; QEvict: Recoverable Quantized KV Eviction for Attention-Drif; Lexical Perturbations Disrupt LLM Reasoning: An Empirical St
  - query: precomputed KV cache reuse frozen small model math reasoning identical outputs without recomputation
    - correct paper in top 10: yes; top 3: MetaKV: Adaptive KV Cache Compression for Constrained LLM In; The risk of KV cache compression; Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Tu
- Run 2:
  - query: How can pre-computed key-value attention states be saved and restored into a new context so a frozen small language model reproduces identical outputs without recomputation, while gaining accuracy on competition math and cutting decode cost?
    - correct paper in top 10: no; top 3: What Attention Recalls and Recurrence Controls in Hybrid Lan; QEvict: Recoverable Quantized KV Eviction for Attention-Drif; Lexical Perturbations Disrupt LLM Reasoning: An Empirical St
  - query: precomputed KV cache reuse frozen small model competition math accuracy decode speedup
    - correct paper in top 10: yes; top 3: The risk of KV cache compression; Where Activation Sparsity and KV-Cache Sparsity Cross in LLM; Codec-Gauge: Learning Compression-Friendly Gauges for Transf
  - query: cartridges trained KV cache corpus compressed prefix self-study frozen model reuse
    - correct paper in top 10: no; top 3: The risk of KV cache compression; PuzzleKV: Page-Wise Low-Rank Decomposition for KV Cache Comp; MetaKV: Adaptive KV Cache Compression for Constrained LLM In
- Run 3:
  - query: How can pre-computed key-value attention states be saved and restored into a new context so a frozen small language model reproduces identical outputs without recomputation, while gaining accuracy on competition math and cutting decode cost?
    - correct paper in top 10: no; top 3: What Attention Recalls and Recurrence Controls in Hybrid Lan; QEvict: Recoverable Quantized KV Eviction for Attention-Drif; Lexical Perturbations Disrupt LLM Reasoning: An Empirical St
  - query: precomputed KV cache reuse frozen small language model math reasoning accuracy decode speedup
    - correct paper in top 10: yes; top 3: MetaKV: Adaptive KV Cache Compression for Constrained LLM In; PuzzleKV: Page-Wise Low-Rank Decomposition for KV Cache Comp; VarRate: Training-Free Variable-Rate KV Cache Compression fo

### q222 (specific)
**Question:** Can a language model be fine-tuned on its own plans that an automated checker accepted, so that it solves replanning tasks in a single non-reasoning pass without a stronger teacher or gold solutions?
**Correct paper:** Governance Records as Supervision: Verifier-Selected Self-Training for Structured Workflow Repair (2608.18324)
**Dense rank:** -   **Agent ranks, runs 1-3:** -, -, -   **Searches:** 3, 3, 3

- Run 1:
  - query: Can a language model be fine-tuned on its own plans that an automated checker accepted, so that it solves replanning tasks in a single non-reasoning pass without a stronger teacher or gold solutions?
    - correct paper in top 10: no; top 3: Correct Diagnosis, Better Feedback: A Symbolic-Verifier for ; Not All LLM Reasoning is Visible in the Chain-of-Thought; Don't Repeat Yourself: Self-Supervised Fine-Tuning for Cover
  - query: self-training language model on verified self-generated plans for PDDL replanning without reasoning tokens
    - correct paper in top 10: no; top 3: SCP-NL2TL: Selective Conformal Prediction with Semantic Veri; Recursive Synthesis for Long-Horizon Terminal Tasks; Register Tokens for Bounded-State Reasoning in Diffusion Lan
  - query: STaR-style rejection sampling fine-tuning on validator-accepted plans, LLM planning replanning single forward pass, no chain-of-thought, self-improvement with plan validator VAL
    - correct paper in top 10: no; top 3: Provably Complete Generalized Planning with LLMs; Reward-Free Evolving Agents via Pairwise Validator; Mitigating Exploration Bias in RL for Multi-Instruction Foll
- Run 2:
  - query: Can a language model be fine-tuned on its own plans that an automated checker accepted, so that it solves replanning tasks in a single non-reasoning pass without a stronger teacher or gold solutions?
    - correct paper in top 10: no; top 3: Correct Diagnosis, Better Feedback: A Symbolic-Verifier for ; Not All LLM Reasoning is Visible in the Chain-of-Thought; Don't Repeat Yourself: Self-Supervised Fine-Tuning for Cover
  - query: self-training on verified self-generated plans PDDL replanning without reasoning tokens fine-tuning
    - correct paper in top 10: no; top 3: Matching Supervision to the Student's Learning Capacity: A U; From RLVR to RLSVR: Task Transformation Induces Self-Verifia; SPADE: Self-Play in Adaptive Synthetic Executable Environmen
  - query: rejection sampling fine-tuning LLM own valid plans VAL validator replanning distillation no chain-of-thought
    - correct paper in top 10: no; top 3: Risk-Controlled Selective LLM Answering by Pricing Label-Fre; When Self-Consistency Backfires: Majority Vote Hurts the Maj; Benchmarks Are Not Validation: A System-Level View of Financ
- Run 3:
  - query: Can a language model be fine-tuned on its own plans that an automated checker accepted, so that it solves replanning tasks in a single non-reasoning pass without a stronger teacher or gold solutions?
    - correct paper in top 10: no; top 3: Correct Diagnosis, Better Feedback: A Symbolic-Verifier for ; Not All LLM Reasoning is Visible in the Chain-of-Thought; Don't Repeat Yourself: Self-Supervised Fine-Tuning for Cover
  - query: self-training LLM on verifier-accepted plans PDDL replanning single-pass without reasoning tokens
    - correct paper in top 10: no; top 3: From RLVR to RLSVR: Task Transformation Induces Self-Verifia; Skill Self-Play: Pushing the Frontier of LLM Capability with; Matching Supervision to the Student's Learning Capacity: A U
  - query: self-improvement LLM fine-tuned on validator-accepted self-generated plans, PDDL replanning, no teacher model, no reasoning tokens
    - correct paper in top 10: no; top 3: Chain-of-Experience for Continual LLM Improvement; GAUGE: When Not to Trust LLM-as-a-Judge in User-Simulated Ev; AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design f

### q239 (vague)
**Question:** Is there a bound on how many rollouts you need to detect that one action is better than another at a decision point, based on how much the policy's value varies there?
**Correct paper:** The Variance of Thought: Policy Variance, Critical Forks, and Local Credit Assignment (2608.22467)
**Dense rank:** -   **Agent ranks, runs 1-3:** -, -, -   **Searches:** 3, 3, 3

- Run 1:
  - query: Is there a bound on how many rollouts you need to detect that one action is better than another at a decision point, based on how much the policy's value varies there?
    - correct paper in top 10: no; top 3: Reusing Rollouts under Policy Lag: Prefix-Normalized Policy ; Rollout Efficiency in Reinforcement Learning for Reasoning L; Offline Policy Evaluation as a decision support tool for des
  - query: sample complexity of Monte Carlo rollouts to distinguish action values, variance-dependent bound, policy evaluation at decision point
    - correct paper in top 10: yes; top 3: The Sample Complexity of Policy Learning with Mu-Resets; Robust Average-Reward Markov Decision Processes: Minimax-Opt; Reusing Rollouts under Policy Lag: Prefix-Normalized Policy 
  - query: variance-aware Monte Carlo rollout count bound to identify better action at state, Bernstein concentration, advantage estimation sample complexity
    - correct paper in top 10: no; top 3: Robust Average-Reward Markov Decision Processes: Minimax-Opt; In-Distribution Imagination for Model-Based Offline Reinforc; PAIR: Pairwise-Aware Inclusion Reweighting for Adaptive Roll
- Run 2:
  - query: Is there a bound on how many rollouts you need to detect that one action is better than another at a decision point, based on how much the policy's value varies there?
    - correct paper in top 10: no; top 3: Reusing Rollouts under Policy Lag: Prefix-Normalized Policy ; Rollout Efficiency in Reinforcement Learning for Reasoning L; Offline Policy Evaluation as a decision support tool for des
  - query: sample complexity of action comparison with Monte Carlo rollouts depending on variance of value at a state, bound on number of simulations to identify better action
    - correct paper in top 10: yes; top 3: Robust Average-Reward Markov Decision Processes: Minimax-Opt; The Sample Complexity of Policy Learning with Mu-Resets; Critical-State RL: Diagnosing Trainable States for Multi-Tur
  - query: variance-dependent bound on number of rollouts to identify best action at a state, Monte Carlo policy evaluation, action gap and value variance
    - correct paper in top 10: yes; top 3: Robust Average-Reward Markov Decision Processes: Minimax-Opt; Reusing Rollouts under Policy Lag: Prefix-Normalized Policy ; The Variance of Thought: Policy Variance, Critical Forks, an
- Run 3:
  - query: Is there a bound on how many rollouts you need to detect that one action is better than another at a decision point, based on how much the policy's value varies there?
    - correct paper in top 10: no; top 3: Reusing Rollouts under Policy Lag: Prefix-Normalized Policy ; Rollout Efficiency in Reinforcement Learning for Reasoning L; Offline Policy Evaluation as a decision support tool for des
  - query: sample complexity of comparing two actions via Monte Carlo rollouts depends on variance of value at a state, bound on number of samples to identify better action
    - correct paper in top 10: yes; top 3: Sample Complexity of Multicalibration for Multilevel Propert; The Sample Complexity of Policy Learning with Mu-Resets; Robust Average-Reward Markov Decision Processes: Minimax-Opt
  - query: variance-dependent sample complexity bound for identifying the better action at a state using rollouts, Bernstein-type concentration, action gap and value variance
    - correct paper in top 10: no; top 3: Robust Average-Reward Markov Decision Processes: Minimax-Opt; Critical-State RL: Diagnosing Trainable States for Multi-Tur; The Free Inference Dimension: Complexity Measure for Zero-Co
