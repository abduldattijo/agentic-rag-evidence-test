# First-pass review exceptions. Any qid not listed here is provisionally ok=1 with no note.
# value: (ok, [alternative paper ids], note)   note starting with CHECK: = needs a closer look
D = {}
D["q000"] = (1, ["2609.13997"], "CHECK: 2609.13997 also gives guided signal on unsolvable RLVR problems; question's 'objective for the original unhinted prompt' is specific to the gold paper")
D["q053"] = (1, [], "CHECK: title overlap 0.5; shares 'spoken dialogue state tracking' with the title, so likely easy. Not a copy of the title.")
D["q061"] = (1, ["2609.04409"], "CHECK: 2609.04409 evaluates cross-lingual consistency methods; question asks for an inference-time latent edit that keeps accuracy, which fits the gold paper better")
D["q064"] = (0, [], "CHECK: asks how much labeled wrist data is needed to close the gap; abstract only says it fine-tuned with varying amounts and does not report a quantity")
D["q066"] = (1, [], "CHECK: title overlap >0.3; shares 'label-free checks' with the title, otherwise a paraphrase")
D["q075"] = (1, [], "CHECK: title overlap >0.3; shares 'optimal transport' and 'zero-shot classification' with the title")
D["q078"] = (1, [], "CHECK: title overlap >0.3; shares 'multimodal financial event' with the title")
D["q083"] = (1, [], "CHECK: a keyword string rather than a question (same style as pilot q017)")
D["q088"] = (0, [], "CHECK: asks for output 'as readable as clinician-written responses'; the abstract reports the opposite (outputs stay 3.2 grade levels harder to read)")
D["q122"] = (1, ["2608.29461"], "CHECK: sibling paper 2608.29461 (causal model of sandbagging with activation interventions) may also answer 'activation editing that recovers hidden capability'; gold states it matches fine-tuning without weight updates")
D["q134"] = (1, [], "CHECK: title overlap >0.3; shares 'embedding network' and 'distance correlation' with the title")
D["q215"] = (1, [], "CHECK: title overlap >0.3; shares 'Fisher', 'on-policy self-distillation', 'feedback' with the title")
D["q275"] = (1, [], "CHECK: title overlap >0.3; shares 'AI agent drafting' and 'impact summaries' with the title")
D["q155"] = (1, [], "CHECK: title overlap >0.3; shares 'Wasserstein barycenters' and 'flow matching' with the title")
D["q299"] = (1, [], "CHECK: title overlap >0.3; shares 'neuro-symbolic AGI', 'Belnap', 'intensional' with the title")
# --- after user spot-check (see fix_questions.py): q014 replaced, q075/q215 rewritten,
# q061/q122 alt ids removed (related only). The CSV is the source of truth from here on.
