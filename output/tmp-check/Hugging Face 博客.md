# Hugging Face 博客

> 分类: AI专题
> URL: https://huggingface.co/blog/feed.xml
> 抓取: 30 篇

---

## 1. "OncoAgent: A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support"

- 日期: 2026-05-09 18:09
- 链接: https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/oncoagent-official-paper

```
"OncoAgent: A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support"
- user: oncoagent-research tags:
- oncology
- multi-agent
- LangGraph
- RAG
- QLoRA
- AMD
- open-source
- clinical-ai
- healthcare
OncoAgent: A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support
Technical preprint · May 2026 · OncoAgent Research Group
Abstract
We present OncoAgent, an open-source, privacy-preserving clinical decision support system for oncology. OncoAgent combines a dual-tier fine-tuned LLM architecture with a state-of-the-art multi-agent LangGraph topology, a four-stage Corrective RAG pipeline over 70+ physician-grade NCCN and ESMO guidelines, and a three-layer reflexion safety validator enforcing a strict Zero-PHI policy.
The system routes clinical queries through an additive complexity scorer to either a 9B parameter speed-optimised model (Tier 1) or a 27B deep-reasoning model (Tier 2), both fine-tuned via QLoRA on a corpus of 266,854 real and synthetically generated oncological cases using the Unsloth framework on AMD Instinct MI300X hardware (192 GB HBM3).
Sequence packing on MI300X enabled full-dataset fine-tuning in approximately 50 minutes — a 56× throughput acceleration over API-based generation. Post-fix, CRAG document grading achieved a 100% success rate with a mean RAG confidence score of 2.3+. The complete system is 100% open source and deployable on-premises, eliminating proprietary cloud API dependency and preserving patient data sovereignty.
Keywords: clinical decision support, oncology AI, multi-agent systems, retrieval-augmented generation, QLoRA, AMD ROCm, open-source healthcare AI, HITL safety, LangGraph, Corrective RAG
1. Introduction
Oncology is one of the most information-dense and cognitively demanding domains in clinical medicine. The volume, heterogeneity, and rapid evolution of evidence-based guidelines — from the National Comprehensive Cancer Network (NCCN) to the European Society for Medical Oncology (ESMO) — create a persistent knowledge gap between published evidence and bedside practice.
AI-assisted clinical decision support systems hold transformative potential for closing this gap, yet most commercially available systems fail in three critical ways:
- Hallucinated recommendations not grounded in validated guidelines
- Cloud API dependency that precludes on-premises deployment in privacy-sensitive hospital environments
- Monolithic LLM architectures prone to context saturation under complex multi-comorbidity presentations
OncoAgent is designed around three core principles:
- Architectural decomposition: Clinical reasoning is decomposed across eight specialised LangGraph nodes, each with a bounded, auditable function.
- Grounded generation: All model outputs are anchored to a curated vector knowledge base through a four-stage retrieval pipeline with explicit relevance gating.
- Hardware sovereignty: The full inference and training stack runs natively on AMD Instinct MI300X using ROCm and open-source frameworks — enabling hospital deployment without data exfiltration.
2. Related Work
2.1 Clinical LLMs and Decision Support
Large language models have demonstrated significant promise in clinical NLP tasks including diagnostic coding, literature summarisation, and patient communication. Domain-specific fine-tuning approaches — exemplified by BioMedLM, Med-PaLM 2, and ClinicalBERT — consistently improve performance on medical benchmarks over general-purpose models. OncoAgent extends this line of work by targeting the specific subdomain of oncological triage and treatment pathway recommendation, where hallucination consequences are most severe.
2.2 Multi-Agent Architectures
Decomposed multi-agent systems have emerged as a principled approach to complex reasoning tasks. OncoAgent synthesises four canonical SOTA patterns:
- Claude Code pattern — deterministic safety harnesses separated from LLM reasoning
- Hermes Agent pattern — structured tool-calling with per-session memory isolation
- Corrective RAG (Shi et al., 2024) — document relevance grading and query reformulation
- Reflexion (Shinn et al., 2023) — self-correcting generation via feedback-augmented retry loops
2.3 Retrieval-Augmented Generation in Medicine
Standard bi-encoder retrieval is ill-suited for clinical domains where terminological precision is critical (e.g., "tyrosine kinase inhibitor" vs. "TKI"). OncoAgent implements a multi-stage pipeline with cross-encoder re-ranking, and integrates Hypothetical Document Embeddings (HyDE; Gao et al., 2022) to resolve medical synonym mismatches by projecting natural language queries into the guideline embedding space.
3. System Architecture
3.1 Overview
OncoAgent is implemented as a stateful directed graph using LangGraph. The system state is represented as an immutable AgentState
TypedDict containing 11 logical sections and approximately 30 typed keys. Each node appends to specific keys without mutating upstream data, preserving a complete audit trail.
The 8-node topology is:
Router → Ingestion → Corrective RAG → Specialist ↔ Critic → HITL Gate → Formatter → END
↓
Fallback → END
Key properties:
- 5 conditional edges
- 1 reflexion retry loop (max 2 iterations)
- 1 mandatory HITL interrupt for high-complexity or low-confidence outputs
3.2 Complexity Router and Model Tiering
Case complexity is quantified using a weighted additive model prior to specialist invocation:
S = w_cancer + w_stage + w_mutations + w_treatment
Where:
Decision boundary: S ≥ 0.5
→ Tier 2 (Qwen 3.6-27B deep reasoning) · S < 0.5
→ Tier 1 (Qwen 3.5-9B speed triage)
Validation: A Stage IV pancreatic carcinoma case with KRAS + BRCA2 mutations correctly produced S = 0.80
, routing to Tier 2. ✅
Clinicians may also manually override the tier selection through the UI.
3.3 Corrective RAG with Document Grading
The CRAG node grades each retrieved document for clinical relevance before forwarding to the Specialist. Documents that fail binary relevance classification trigger automatic query reformulation (max 1 retry). This eliminates the primary hallucination source in RAG pipelines — retrieval of plausibly titled but semantically irrelevant content.
After migrating from Qwen 3.5 to Qwen 2.5 Instruct for the grading step, success rate improved from 0% → 100%, with RAG confidence score reaching 2.3+ on uterine cancer triage tests.
3.4 Reflexion Safety Loop (Critic Node)
The Critic node runs a three-layer validation cascade before any output reaches the HITL gate:
- Formatting check — validates structural compliance with the OncoCoT output schema
- Safety check — deterministic rule-based scan for prohibited output patterns (absolute dosing without guideline citation, drug interaction omissions, etc.)
- LLM entailment check — verifies that the Specialist's recommendation is fully supported by the retrieved RAG context
On FAIL, the Critic's specific feedback is injected back into the Specialist context for a retry (max 2 iterations). Crucially, the Critic runs as deterministic code, not LLM-controlled logic — ensuring safety enforcement cannot be bypassed by adversarial prompting.
3.5 Human-in-the-Loop Gate and Fallback
The HITL gate provides a mandatory clinician interrupt for all Tier 2 cases and any output where rag_confidence < 0.3
. A dedicated Fallback node catches unrecoverable failures and returns a clinically safe refusal — "Información no concluyente en las guías provistas"
— avoiding hallucinated alternatives under any failure mode.
3.6 Per-Patient Memory Isolation
The PatientMemoryStore
module assigns each patient session a unique thread_id
(format PT-XXXX
), passed as a configurable
parameter to LangGraph's native checkpointing system. This enforces strict per-patient memory isolation while enabling iterative multi-turn consultations within a session.
4. Knowledge Base Construction and RAG Pipeline
4.1 Guideline Ingestion and Sanitisation
The knowledge base was constructed from 77 direct physician guideline PDFs identified by a concurrent web scraper that processed 138 NCCN detail pages in under 60 seconds. Text extraction used PyMuPDF
(fitz) for block-level structural parsing, preserving the semantic reading order of multi-column clinical layouts.
A regex-based sanitisation step strips institutional branding prior to ingestion. Patient-facing materials are excluded via heuristic filtering. The resulting corpus covers 70+ professional oncological guidelines across all major cancer types including HCC, NSCLC, breast, colorectal, and neuroendocrine tumours.
4.2 Medical Embeddings and Vector Store
Standard general-purpose embedding models (e.g., all-MiniLM-L6-v2
) were rejected due to poor clinical terminology semantics. OncoAgent uses:
- Embeddings:
pritamdeka/S-PubMedBert-MS-MARCO
— fine-tuned on PubMed and MS-MARCO for asymmetric medical semantic search - Vector store: Local ChromaDB persistent index — zero-cloud, Zero-PHI compliant
4.3 Four-Stage Retrieval Pipeline
Anti-Hallucination Policy: Any query failing Stage 2 returns "Información no concluyente en las guías provistas"
without invoking the Specialist. This guarantees zero hallucinated recommendations for out-of-domain clinical inputs.
Distance threshold calibration against the NCCN corpus established:
- Medical-query distances: ~0.06–0.09
- Out-of-domain distances: ~0.11–0.15
- Hard threshold: 0.10
An optional HyDE module generates a hypothetical guideline paragraph and uses it as the embedding anchor for Stage 1 retrieval, resolving synonym mismatches (e.g., "neoplasia pulmonar"
vs. "lung carcinoma"
).
5. Dual-Tier QLoRA Fine-Tuning
5.1 Training Corpus: OncoCoT (266,854 Samples)
All cases use ChatML template for Qwen compatibility. Thinking tokens were disabled (chat_template_kwargs: {enable_thinking: False}
) to prevent JSON parse corruption.
5.2 QLoRA Configuration
Both tiers use 4-bit NormalFloat4 (NF4) quantisation via BitsAndBytes, with LoRA adapters targeting all major projection modules: q_proj
, k_proj
, v_proj
, o_proj
, gate_proj
, up_proj
, down_proj
.
5.3 AMD MI300X Optimisation with Unsloth
The original HuggingFace transformers
+ PEFT pipeline failed on the MI300X due to two independent issues:
- Tokenisation conflicts between
trl
v0.24.0 strict EOS validation and theQwen3VLProcessor
wrapper - Insufficient VRAM headroom for target effective batch sizes under standard precision
Migration to Unsloth's FastLanguageModel resolved both simultaneously:
- VRAM reduction: ~60% drop in peak usage (from OOM to stable ~64 GB on 192 GB device)
- Training speed: ~2× improvement to ~16 s/step at effective batch 16
AMD ROCm-specific adaptations required:
# 1. Pass inner tokenizer, not the Qwen3VLProcessor wrapper
trainer = SFTTrainer(tokenizer=model.get_tokenizer(), ...)
# 2. Prevent incompatible EOS injection
training_args = SFTConfig(eos_token=None, ...)
# 3. AMD-specific bitsandbytes for ROCm 6.2/gfx942
# pip install bitsandbytes --find-links <amd-continuous-release-wheel>
# 4. BF16 workaround (is_bf16_supported() returns False on ROCm despite hardware support)
training_args = TrainingArguments(fp16=True, ...)
# Final deployment uses native BF16:
model = AutoModelForCausalLM.from_pretrained(..., torch_dtype=torch.bfloat16)
5.4 Sequence Packing and Throughput Breakthrough
Sequence packing via packing=True
in SFTConfig
concatenates multiple short clinical records into single 2048-token sequences, eliminating padding overhead and drastically reducing forward pass count.
The combined effect of Unsloth kernels and sequence packing on the MI300X enabled full-dataset fine-tuning of the 266,854-sample corpus in approximately 50 minutes — against an initial 5-hour estimate — representing roughly a 6× training time compression. GPU utilisation peaked at ~70%, with consistent throughput at ~11.3 s/iteration.
Checkpoint-1000 results: Tier 1 adapter trained for 1,339 steps · training loss ≈ 0.05 · adapter size 187 MB · verified against 11-file manifest including
adapter_model.safetensors
,adapter_config.json
, andtokenizer.json
.
The system supports adaptive inference routing: local BF16 inference via the LocalModelManager
singleton when ROCm is available, with graceful fallback to the Featherless.ai API for high availability.
6. Safety and Privacy Framework
6.1 Zero-PHI Policy
A dedicated Zero-PHI redaction node runs as the first processing step in the Ingestion node, before any text reaches an LLM. It identifies and replaces Protected Health Information (patient names, dates of birth, MRN numbers, addresses, facility identifiers) with clinically neutral placeholders. The redacted representation is stored in AgentState
; the original text is discarded.
This ensures that no PHI reaches any downstream LLM call — local or remote — and satisfies HIPAA de-identification requirements by design rather than policy.
6.2 Layered Safety Architecture
The system's safety guarantees are enforced at four independent layers. A failure at any single layer does not compromise the overall posture.
Layers 1 and 2 operate at the retrieval layer. Layer 3 at the generation layer. Layer 4 at the deployment layer. All Layer 3 checks run as deterministic code — not LLM-controlled logic — preventing safety bypass via adversarial prompting.
7. Clinical Interface
The OncoAgent UI is implemented as a real-time streaming Gradio application in a ChatGPT-style conversational layout. It features:
- Left sidebar: Session controls, KPI tiles, evidence source tabs
- Main chat area: Live agentic reasoning updates as each node completes
Real-time transparency is achieved via LangGraph's .stream(stream_mode="updates")
API, which emits {node_name: node_output}
dictionaries as each node completes. The UI maps each node to a human-readable clinical label (e.g., corrective_rag
→ "Retrieving NCCN/ESMO guidelines"), providing clinicians with full pipeline visibility.
The rag_confidence
score and retrieved source count are prominently surfaced, giving clinicians immediate visibility into the quality of guideline grounding behind each recommendation.
The interface was designed to WCAG 2.1 AA standards — Lucide-style inline SVG icons, slate-900/sky-500 dark theme, Figtree/Inter typography, prefers-reduced-motion
media query, all transitions capped at 200 ms.
8. Results
9. Discussion
9.1 Hardware Sovereignty as a Clinical Requirement
The ability to run the complete OncoAgent stack — training, inference, RAG, and UI — on a single AMD MI300X instance without cloud API dependencies is not merely an engineering convenience. In hospital environments governed by HIPAA (US), GDPR (EU), and equivalent national frameworks, the legal and ethical obligation to maintain data within controlled infrastructure is absolute. OncoAgent demonstrates that SOTA multi-agent clinical AI is achievable within this constraint.
9.2 The Throughput Breakthrough
The 56× synthetic data generation acceleration (from ~120 to ~6,800 cases/hr) and the ~6× training time compression together represent a significant practical contribution to the feasibility of domain-specific fine-tuning in time-constrained settings. These results suggest that AMD's CDNA3 architecture, when paired with Unsloth's Triton kernel optimisations and SFT sequence packing, may be substantially underutilised by standard HuggingFace training pipelines — and that the performance gap can be closed without changes to the underlying model architecture.
9.3 Limitations
Several limitations warrant acknowledgement:
- The training corpus relies on approximately 36% synthetically generated cases. Clinical accuracy validation against board-certified oncologist judgments has not yet been performed at scale.
- The current knowledge base covers NCCN guidelines primarily in English; ESMO and non-English clinical corpora remain for future work.
- The Tier 1 adapter represents checkpoint-1000 of a potentially longer trajectory; full convergence and downstream clinical benchmark evaluation (MedQA, USMLE-style oncology subsets) are planned for subsequent releases.
10. Conclusion
OncoAgent establishes a complete, open-source, privacy-preserving clinical decision support architecture for oncology that integrates SOTA multi-agent design patterns, domain-specific fine-tuning, and a four-stage grounded retrieval pipeline.
The system demonstrates that production-grade clinical AI does not require proprietary infrastructure: the full stack — including 266k-sample QLoRA fine-tuning, 70+ guideline RAG, eight-node LangGraph orchestration, three-layer reflexion safety validation, and real-time clinical streaming UI — runs on a single AMD Instinct MI300X instance under ROCm.
The architectural contributions — particularly the synthesis of Corrective RAG, Reflexion, and HITL gating into a single coherent safety stack — represent a replicable blueprint for domain-specific clinical AI deployments where hallucination consequences are life-critical.
All code, adapter weights, and the OncoCoT synthetic corpus will be released publicly on Hugging Face Spaces and GitHub.
References
- Singhal, K. et al. (2023). Large language models encode clinical knowledge. Nature, 620, 172–180.
- Nori, H. et al. (2023). Can generalist foundation models outcompete special-purpose tuning? Case study in medicine. arXiv:2311.16452.
- Wang, L. et al. (2024). A survey on large language model based autonomous agents. Frontiers of Computer Science, 18(6), 186345.
- Shi, W. et al. (2024). Corrective Retrieval Augmented Generation. arXiv:2401.15884.
- Shinn, N. et al. (2023). Reflexion: Language agents with verbal reinforcement learning. NeurIPS 2023.
- Nogueira, R. and Cho, K. (2019). Passage Re-ranking with BERT. arXiv:1901.04085.
- Gao, L. et al. (2022). Precise Zero-Shot Dense Retrieval without Relevance Labels. arXiv:2212.10496.
- Hu, E.J. et al. (2021). LoRA: Low-Rank Adaptation of Large Language Models. arXiv:2106.09685.
- Dettmers, T. et al. (2023). QLoRA: Efficient Finetuning of Quantized LLMs. NeurIPS 2023.
- Han, S. et al. (2024). LangGraph: Building stateful multi-actor applications with LLMs. LangChain Technical Report.
OncoAgent is intended as a clinical decision support tool. All outputs require review by licensed medical professionals prior to any clinical application.
```

---

## 2. EMO: Pretraining mixture of experts for emergent modularity

- 日期: 2026-05-08 16:03
- 链接: https://huggingface.co/blog/allenai/emo

```
EMO: Pretraining mixture of experts for emergent modularity
Today we're releasing EMO, a new mixture-of-experts (MoE) model pretrained end-to-end so that modular structure emerges directly from the data without relying on human-defined priors. EMO lets you use a small subset of its experts - just 12.5% of the total - for a given task while keeping near full-model performance, and still works as a strong general-purpose model when all experts are used together.
Large language models are typically trained and deployed as monolithic systems: a single model is initialized, pretrained, fine-tuned, and served as one unified entity. But applications often need only a subset of capabilities, such as code generation, mathematical reasoning, or domain-specific knowledge. As frontier language models routinely reach trillions of parameters, using and adapting the full model becomes impractical for most users and incurs unnecessary computational cost and memory to host parameters that may not even be needed.
Mixture-of-experts (MoE) models seem like a natural way to relax this constraint. Instead of using one large feedforward network at each layer, MoEs contain many smaller ones, called experts, and activate only a small subset for each input token. In principle, a task that only needs one capability could load only the relevant experts.
In practice, however, existing MoEs still need the full model to work well. Even within a single input, different tokens often activate different experts, so a task can end up using all the experts during its generation. As we show in our paper, this happens partly because experts in standard MoEs often specialize in low-level lexical patterns like prepositions or punctuation rather than higher-level domains or capabilities. As a result, small subsets of experts are not reliably usable on their own.
We instead want MoE models whose experts organize into coherent groups that can be selectively used and composed.
One way to encourage this during pretraining is to route tokens to experts based on predefined semantic domains, such as math, biology, or code. Prior work like BTX and our FlexOlmo project has tried this. However, predefined domains come with important limitations. They require domain labels across the pretraining corpus, which can be ambiguous and expensive to obtain, and they may inject too much human bias into how the model is allowed to organize itself. More importantly, fixing the domains upfront also fixes the model's modular structure: if a new domain or capability emerges at inference time, it isn't obvious which experts should be used.
That's where EMO comes in.
We show that EMO - a 1B-active, 14B-total-parameter (8-expert active, 128-expert total) MoE trained on 1 trillion tokens - supports selective expert use: for a given task or domain, we can use only a small subset of experts (just 12.5% of total experts) while retaining near full-model performance. At the same time, when all experts are used together, EMO remains a strong general-purpose model. In contrast, a standard MoE of equal architecture trained on the same data shows severe degradation when selectively using its expert subsets.
EMO is an MoE trained with modularity as a first-class objective. For a given domain (e.g., math, code, biomedical), users can select a small subset of experts of any size and retain near full-model performance. This turns a single model into a composable architecture, enabling flexible deployment with improved memory-accuracy tradeoffs for large, sparse MoEs.
How do we get modularity to emerge?
In an MoE, a small network called the router decides which experts each token activates. We want the router to learn that tokens from similar domains should activate similar subsets of experts. Our key observation is that tokens from the same document usually come from the same domain. We therefore use document boundaries as a weak supervisory signal: during training, all tokens in a document are restricted to choose their active experts from a shared expert pool.
Comparison of training of a standard MoE and EMO (k = 2, n = 10, shared experts omitted for simplicity). (Left) In a standard MoE, each token independently selects its top-k experts. Across tokens, all experts are used. (Right) In EMO, the router first selects a subset of experts for each document, and all tokens are constrained to route within this subset. This enforces consistent expert usage across the document, encouraging groups of experts to form domain specialization.
For example, in an MoE with 10 total experts and 2 active experts per token, all tokens in a document are restricted to route within the same pool of 4 experts, as shown in the figure above. This pool is chosen by the router itself: we average the router's expert preferences across all tokens in the document, then select the most-used experts as the document's shared pool. Different documents can use different pools, allowing recurring expert groups to emerge directly from the training data.
There are a few considerations when implementing the system:
Load balancing. One technical challenge is load balancing. In standard MoE training, the load-balancing objective is used to prevent the model from collapsing onto only a small number of experts. At first glance, this seems to conflict with EMO's training objective: we are explicitly restricting each document to use only a subset of experts.
The conflict comes from the scale at which load balancing is usually applied. In many MoE implementations, load balancing is computed locally, often within a micro-batch containing only a small number of documents. This local objective can push tokens within the same document to spread across many experts, directly opposing EMO's objective of keeping expert usage consistent within a document.
To resolve this, we apply load balancing globally across many documents. At this larger scale, the two objectives become complementary: EMO encourages tokens within the same document to use a coherent expert pool, while global load balancing encourages different documents to collectively cover all experts. In practice, we found that global load-balancing is important for stable training.
Document pool size. The document pool size controls how restrictive the modularity constraint is. A smaller pool forces tokens in the same document to share a tighter set of experts, encouraging stronger modularity; a larger pool gives the model more flexibility but weakens the constraint.
Rather than fixing one pool size, we randomly sample it during training. This prevents EMO from overfitting to a single subset size and lets it support different expert subset sizes at inference time.
Benchmark results
On general-purpose benchmarks, EMO matches the performance of a standard MoE model, showing that the modularity objective does not come at the cost of full-model performance. The more important question, however, is whether the model can still work when we only keep a subset of experts. In this setting, we construct task-specific expert subsets by ranking experts according to their routing usage on a small amount of task validation data, keeping the most-used experts and discarding the rest.
The figure below shows that EMO remains robust under selective expert use. When we keep only 25% of the experts (32 expert subset), EMO loses only about 1% absolute performance across all benchmarks; even when we keep only 12.5% of the experts (16 expert subset), the overall drop is only about 3%. This holds both before and after fine-tuning. In contrast, the matching standard MoE degrades sharply as the expert subset gets smaller, often falling close to or below random performance in the smallest expert subset settings.
Furthermore, we show that selecting the right experts for a task is surprisingly cheap: a single example with few-shot demonstrations is enough to identify a module that performs on par with one selected using a full validation set. And EMO isn't tied to any particular selection method: it works well with existing expert-pruning approaches like Easy-EP, and the two complement each other.
Smaller 130B-token setting. Averaged performance over 16 MMLU categories across different memory budgets. EMO expert subsets push the Pareto frontier in memory-accuracy trade-off, outperforming standard MoEs and even fixed-budget models trained from scratch.
What are expert subsets specializing to?
To see what EMO actually learned after training, we clustered router activations of the first 100 tokens across 12K pretraining documents. The difference from a standard MoE is stark.
EMO's token clusters correspond to things like Health, Medical & Wellness, News Reporting, US Politics & Elections, and Film & Music. A standard MoE produces clusters like Prepositions, Proper Names, Copula Verbs, or Definite Articles. In EMO, tokens from a given document mostly land in the same cluster; in a standard MoE, they end up scattered across many.
The contrast is easiest to see on a single example. Take a health article: in EMO, almost every token would route into the Health, Medical & Wellness cluster. In a standard MoE, the top cluster is Possessives & Definite Articles; the model would group the article with every other text that happens to use the word the or your, regardless of what that text is about.
Token clusters of pretraining data on MoEs trained on 1T tokens. EMO clusters correspond to semantically meaningful domains, with tokens from the same document largely grouped together. Standard MoE training produces clusters of surface-level or syntactic features, with document tokens dispersed across multiple clusters.
Because EMO forms modules that map to semantic domains rather than surface features, you can pick a small expert subset and still have a functioning model: the group corresponds to a real capability.
You can play around with the clustering results yourself in our interactive visualization.
What we're releasing
We're releasing the full EMO-trained model, a matched standard-MoE baseline trained on the same data, and the training code. We hope these artifacts are useful for other groups studying emergent modularity in MoEs.
There's more work to do. EMO is an early step toward making large sparse models more modular, but many questions remain: how to better select and compose expert subsets, how to update modules without disrupting the full model, and how to use modular structure for better interpretability and control. Releasing these models should help the community to study these questions and build toward modular language models that are easier to deploy, adapt, inspect, and compose.
```

---

## 3. vLLM V0 to V1: Correctness Before Corrections in RL

- 日期: 2026-05-06 19:06
- 链接: https://huggingface.co/blog/ServiceNow-AI/correctness-before-corrections

```
vLLM V0 to V1: Correctness Before Corrections in RL
TL;DR. vLLM V1 matched our vLLM V0 reference after we fixed four things:
processed rollout logprobs, V1-specific runtime defaults, the inflight
weight-update path, and the fp32 lm_head
used for the final projection. We
fixed the backend behavior before changing the RL objective.
The reference run used vLLM 0.8.5
; the V1 runs used vLLM 0.18.1
. Figure 1
shows the final result. The red run is the initial V1 attempt, and the green
run is the final V1 run after the fixes described below.
Migration Objective
vLLM V1 is a substantial rewrite of the V0 engine. Our migration target was therefore deliberately narrow:
- verify that V1 returned rollout logprobs in the form the trainer expected
- rerun the same workload against the V0 reference
- evaluate objective-level changes only after backend parity was restored
The first visible symptoms appeared in:
clamp_log_ratio_new_old_indicator
kl_new_old
entropy
reward
Those metrics came from a GSPO training run, the objective used for this experiment. The same class of mismatch can surface in PPO, GRPO, or any online RL system that treats rollout-side logprobs as part of the optimization target.
The initial V1 run showed the problem clearly. The trainer-side logprobs and reward moved away from the V0 reference early in training.
The same pattern appears in the trainer metrics. Clip rate is the easiest signal to read in the initial comparison.
Failure Modes
We separated the possible causes into three layers:
- Semantic mismatch: the backend returns logprobs with different meaning relative to what the trainer expects.
- Inference-path mismatch: the backend uses different runtime defaults for caching, scheduling, or request handling, so the same prompts follow a different execution path.
- Objective mismatch: the RL objective needs correction for the amount of staleness or backend mismatch that remains.
We initially suspected the third category too early. The useful diagnosis came from treating the first two as backend behavior problems and ruling them out first.
V1 Backend Fixes
Logprob Semantics
The first issue was semantic. vLLM V1 returns logprobs from the raw model outputs by default, before logits post-processing such as temperature scaling, penalties, and top-k/top-p filtering. PipelineRL expected logprobs from the processed distribution used by the sampler.
The required setting was:
logprobs-mode=processed_logprobs
This removed the obvious mean offset in rollout logprobs. The training curves still showed a gap relative to the known-good reference, so the next issue had to be in the inference path.
The policy-ratio plot shows this directly. Once processed_logprobs
is on for
V1, the mean policy ratio stays centered extremely close to 1.0
across all
three runs. That establishes the mean-bias fix. The remaining mismatch shows up
in clip rate, KL, entropy, and downstream training behavior.
Runtime Defaults
The early V1 run mixed the engine version with V1 runtime defaults:
- prefix caching, left unset in the early run so the vLLM
0.18.1
default applied - async scheduling, left unset in the early run so the vLLM
0.18.1
default applied - an ad-hoc
disable-cascade-attn
override that was set through launch-time kwarg passthrough and sits outside the parity recipe in committed config
For the parity run, we made these choices explicit:
vllm_config:
use_v1: true
vllm_kwargs:
logprobs-mode: processed_logprobs
enable-prefix-caching: false
async-scheduling: false
Prefix caching deserves a separate note. It is normally a correctness-preserving inference optimization for a fixed model state. In this online RL setup, it was a V1-only difference in cache lifetime and reuse relative to the V0 reference path. The actor was also handling repeated prefixes, concurrent requests, async scheduling, and inflight weight updates.
A prefix-cache hit can reuse state computed before a weight update when the cache policy ignores the weight-update boundary. Disabling prefix caching removed one V1-only degree of freedom from the parity comparison.
Inflight Weight Updates
Weight synchronization also had to match the online-RL update model. One option was to make V1 stricter than V0 by draining requests and clearing caches at every update. That would answer a separate question. We first needed to verify that V1 could match the existing V0 behavior.
What V0 effectively did was closer to:
- block execution at an engine boundary
- load the new weights
- resume without an explicit cached-state invalidation
The nearest V1 analogue was:
await engine.pause_generation(mode="keep", clear_cache=False)
await engine_client.collective_rpc_async(
"receive_weight_update",
args=(request.model_dump_json(),),
)
await engine.resume_generation()
Two details matter:
mode="keep"
matches the old inflight update model more closely thanwait
orabort
clear_cache=False
matches the V0 wrapper behavior, which left cached state intact on update
Lag was a useful runtime diagnostic. The initial V1 path carries more persistent lag later in training than the corrected V1 run.
The Remaining Gap: fp32 lm_head
The V1 backend fixes above removed the obvious migration issues, but final
parity still required matching the numerical path used to compute logits. The
trainer used an fp32 lm_head
for the final projection. The rollout backend
had to match that behavior.
A closely related issue appears in the MiniMax-M1 technical report: their RL run showed a training/inference token-probability mismatch that they traced to the LM output head and fixed by computing the head in fp32.
This matters because the RL update consumes token logprobs directly. Small changes in logits can become visible in policy ratios, KL, and clipping. The final projection precision is therefore part of the correctness surface for online RL. The ScaleRL paper later includes fp32 logits/head computation as part of its RL recipe and ablates it as a useful design choice for large-scale RL.
With the fp32 lm_head
path included, reward gives a compact view of the final
parity result. In Figure 6, the final V1 run tracks the V0 reference; the
initial V1 attempt produces a clearly different reward curve.
Ablations
The negative results are important because they rule out common explanations.
processed_logprobs
alone: fixed the semantic logprob bug; the training mismatch remained.- Batch invariance: the mismatch remained in a separate test, with higher lag, higher clip rate, and NCCL complications.
- Treating the first V1 run as a fair baseline: the first V1 run had multiple V1-only defaults enabled, so it was a confounded migration comparison.
Why We Fixed Backend Correctness First
Objective-side corrections such as truncated importance sampling, importance-ratio reweighting, and related methods are useful tools. If rollouts are intentionally stale, generated asynchronously, or produced by a backend where equivalence to the trainer-side policy is unavailable, then some form of correction is often the right thing to add.
The first problem here was inference correctness. After moving to V1, the rollout backend returned logprobs and runtime behavior that broke the trainer assumption. Adding an objective-side correction at that point would have mixed two questions:
- is the inference backend producing the right logprobs?
- given correct logprobs, does the objective still need an off-policy or async correction?
Those questions need to be separated. Otherwise an objective-side correction can compensate for broken inference-backend behavior, which makes the training curve harder to interpret.
The current objective can still improve. After inference parity is restored, the next improvement is the usual async/off-policy cleanup:
- keep explicit behavior-policy logprobs from rollout time
- recompute trainer-side old-policy logprobs at optimization time
- separate backend mismatch correction from the policy-update ratio
- track diagnostics like ESS for the correction term alongside aggregate trainer metrics
The main lesson from this migration is narrower: fix backend correctness first, then add corrections for the mismatch that remains.
```

---

## 4. Adding Benchmaxxer Repellant to the Open ASR Leaderboard

- 日期: 2026-05-06 00:00
- 链接: https://huggingface.co/blog/open-asr-leaderboard-private-data

```
Adding Benchmaxxer Repellant to the Open ASR Leaderboard
TLDR: Appen Inc. and DataoceanAI have provided high-quality English ASR datasets covering scripted and conversational speech over multiple accents. To prevent potential risks of benchmaxxing or test-set contamination, we will keep these datasets private for a high-quality measure of performance on multiple tasks.
We’re not updating the average WER at this time: by default, the leaderboard’s Average WER remains computed on public datasets only. You can optionally include the private datasets using the toggle to see their impact 👀
Since its launch in September 2023, the Open ASR Leaderboard has been visited over 710K times. We’re blown away by the community’s interest and motivation to keep pushing speech recognition 🗣️
Two words sum up the objectives (but also challenges) in maintaining a benchmark like the Open ASR Leaderboard:
Standardization: models can have different conventions for their usage and outputs, e.g. with/without punctuation and casing. Datasets have the same challenges and can be structured differently. To this end, all test sets have been gathered into a single dataset on the Hub for easy access and previewing. Moreover, to standardize model outputs and dataset transcripts, we use a normalizer that (among other things) removes punctuation and casing, and maps to American spelling. It is based on the normalizer of Whisper.
Openness: the UI code and evaluation scripts are open-sourced. This has helped not only to incorporate new models, but also to improve the quality of the evaluation procedure through community feedback and contributions.
Standardization and openness are essential for meaningful benchmarking, but they also make benchmarks more susceptible to benchmark-specific optimization ("benchmaxxing"), where models improve leaderboard performance without corresponding gains in real-world robustness. As models and use cases evolve, the Open ASR Leaderboard will continue incorporating high-quality datasets and new evaluation settings to better reflect real-world performance and improve robustness against benchmark-specific optimization.
As discussed in our report, there is no single "catch-all" ASR model: some perform better on American English, others on diverse accents and multilingual settings, while others are optimized for speed or conversational audio. Different applications also prioritize different capabilities, so a model that performs less well on one dimension is not necessarily a worse model overall. The goal of the Open ASR Leaderboard is to capture these nuances and provide a more holistic view of ASR performance.
New high-quality, private datasets
To this end, we have worked with Appen Inc. and DataoceanAI to curate high-quality datasets for ASR benchmarking. Below is some information on the various splits.
Below are sample audio showing the variety of content (scripted, conversational, acronyms, disfluencies, proper nouns).
While private datasets may sound contrary to the spirit of openness, we believe that incorporating such datasets will increase the trustworthiness of the Open ASR Leaderboard, as they are less likely to be exploited for benchmaxxing, whether by model developers who explicitly use the public test sets or who try to find training data that closely resembles a particular dataset to boost their score in the macroaverage.
With these datasets, we can also provide targeted metrics to highlight gaps and biases between controlled and often saturated settings (scripted, American accent) and more nuanced conditions (conversational and non-American accents). Below is a screenshot of the new "Private data" tab.
Below is how each column is computed.
- "Average WER" computes a macroaverage of the data provider averages, so that they are weighted equally.
- "Avg Scripted" performs a macroaverage of all scripted datasets.
- "Avg Conversational" performs a macroaverage of all conversational datasets.
- "Avg US" performs a macroaverage of all datasets with American accents.
- "Avg non-US" performs a macroaverage of all datasets with non-American accents.
We intentionally do not provide a score on each split, to avoid model developers from boosting their score with a specific data provider or accent.
How can I evaluate my model on this data?
Get your model on the Open ASR Leaderboard, and we'll run the evaluation! As before, the process for adding a model to the leaderboard takes place on the Open ASR Leaderboard GitHub:
- Open a pull request, and a model checklist will appear. As before, you should report your results on the public datasets.
- We will verify the results on the public sets and compute the metrics on the private ones.
- Confirm the results we’ve obtained.
While you wait for your model to be added to the Open ASR Leaderboard, you can self-report your metrics on the public sets by adding a YAML file like this to your model card. Your model will then appear on an (unverified) leaderboard that appears on the dataset page (see screenshot below). More on this approach to decentralized evaluation can be read here.
Do models trained on the data providers have an advantage?
They could. We’ve asked Appen and DataoceanAI to not provide this data to their clients. But even if they do not provide this exact data, data from a similar distribution could still help the model on the corresponding evaluation set (similar to benchmaxxing by optimizing for a challenging task from the public sets). To this end, having multiple data providers balances out the advantage a model may get from having used data from one of the providers. And we are open to more data providers and eval sets for the "Private data" tab!
Moreover, to ensure that the private sets do not affect the model ranking, we’ve defaulted the Average WER to not include the Private sets in its macroaverage.
In the screenshot below, you can see that "Private data" is toggled off. This means that the macroaverage across datasets does not include it.
Simply toggle on "Private data" splits to include them in the macroaverage.
The "Rank Δ" column shows how the ordering changes relative to the default macroaverage configuration. Including or excluding public datasets also changes the macroaverage, allowing users to tailor the evaluation to the use cases and data distributions most relevant to their application.
What's next?
We’re excited to hear the community’s feedback on how the new track and dataset toggling features help users identify the model(s) that best fit their application(s). We’re also looking into evaluations that better reflect real-world noisy conditions, and you can expect some news on that 😉
While preparing the private evaluation sets, we took extra care to ensure consistent audio and transcript quality across datasets, including developing tooling to identify challenging cases such as low signal-to-noise conditions or transcript mismatches, since these factors can meaningfully affect WER. More on that in a future post!
```

---

## 5. Granite 4.1 LLMs: How They’re Built

- 日期: 2026-04-29 15:01
- 链接: https://huggingface.co/blog/ibm-granite/granite-4-1

```
Granite 4.1 LLMs: How They’re Built
Authors: Granite Team, IBM
TL;DR — Granite 4.1 is a family of dense, decoder‑only LLMs (3B, 8B, and 30B) trained on ~15T tokens using a multi‑stage pre‑training pipeline, including long‑context extension of up to 512K tokens. The models are further refined with supervised fine‑tuning on ~4.1M high‑quality curated samples and reinforcement learning via on‑policy GRPO with DAPO loss (Yu et al., 2025). Notably, the 8B instruct model matches or surpasses the previous Granite 4.0‑H‑Small (32B‑A9B MoE) despite using a simpler dense architecture with fewer parameters. All Granite 4.1 models are released under the Apache 2.0 license.
Links:
Overview
Building high‑quality small language models goes beyond simply scaling compute—it requires rigorous data curation throughout training. For Granite 4.1, we prioritized data quality over quantity, progressively refining the data mixture across five pre‑training stages. We further curated supervised fine‑tuning data using an LLM‑as‑Judge framework and applied a multi‑stage reinforcement learning pipeline to systematically strengthen performance in math, coding, instruction following, and general chat.
Model Architecture
Granite 4.1 models use a decoder-only dense transformer architecture. The core design choices include Grouped Query Attention (GQA), Rotary Position Embeddings (RoPE), SwiGLU activations, RMSNorm, and shared input/output embeddings.
All three model sizes share the same training pipeline and data strategy, differing only in architecture dimensions.
Pre-Training
Granite 4.1 is trained from scratch on approximately 15 trillion tokens using a five‑phase training strategy. Phases 1–2 focus on foundational pre‑training, phases 3–4 perform mid‑training with progressively higher‑quality data annealing, and phase 5 introduces long‑context training, extending the context window to 512K tokens. Each phase employs a distinct data mixture and learning‑rate schedule, gradually shifting from broad web‑scale data to more curated, domain‑specific content.
Figure 2: The five-phase pre-training pipeline. Phases 1–2 are pre-training, Phases 3–4 are mid-training (high-quality data annealing), and Phase 5 is long context training (LCE).
Phase 1: General Pre-Training (10T tokens)
The first phase establishes broad language understanding using a general mixture of training data with a power learning rate schedule and warmup.
Data composition:
- CommonCrawl ~59% — general web data
- Code ~20% — programming languages and repositories
- Math ~7% — mathematical reasoning data
- Technical ~10.5% — scientific papers, technical documentation and manuals
- Multilingual ~2% — non-English language data
- Domain Specific ~1.5% — domain-specific content
Phase 2: Math/Code Pre-Training (2T tokens)
Phase 2 sharply increases the proportion of code and mathematical data, pivoting toward stronger reasoning capabilities while still maintaining general language coverage.
Data composition:
- Math ~35% — a 5x increase over Phase 1
- Code ~30% — a 1.5x increase
- CommonCrawl-HQ ~12% — high-quality common crawl subset
- Synthetic ~9% — synthetic high-quality data
- Technical ~10%
- Multilingual ~3%
- Domain ~1%
Phase 3: High-Quality Data Annealing (2T tokens)
Phase 3 transitions into mid-training with a more balanced, high-quality mixture and an exponential decay learning rate schedule. This is where we start blending in chain-of-thought and synthetic instruction data.
Data composition:
- CommonCrawl-HQ ~16.67%
- Math ~16.67%
- Code ~16.67%
- Synthetic ~8.5%
- Technical ~12.5%
- Multilingual ~4.5%
- Long Chain-of-Thought ~12.5% — reasoning trajectories
- Language Instructions ~7.5% — instruction tuning data
- Code Instructions ~4.5% — instruction tuning data
Phase 4: High-Quality Data Annealing — Refinement (0.5T tokens)
The fourth phase continues mid-training with a linear learning rate decay to zero, focusing the model on the highest-quality data available.
Data composition:
- CommonCrawl-HQ ~40%
- Code ~20%
- Math ~20%
- Long Chain-of-Thought ~6%
- Code Instructions ~5%
- Language Instructions ~9%
Figure 3: How the data mix evolves across the pre-training phases. Notice the progressive shift from web-heavy (Phase 1) to quality-heavy with instruction and reasoning data (Phases 3–4).
Phase 5: Long Context Training (LCE)
The fifth and final phase also part of of mid-training extends the context window from 4K to 512K through a staged long-context extension process:
- 32K extension — using the same data mix as Phase 4
- 128K extension — same data mix as Phase 4
- 512K extension — 80% books + 20% code repository data (8b and 30b only)
The LCE phase uses an exponential learning rate schedule starting at 1e-4
and decaying to 0
. To ensure the model natively handles long sequences without degrading short-context performance, we do a model merge after each LCE stage. RULER benchmark of base models:
SFT: Data Preparation & Quality Control
Supervised fine‑tuning (SFT) is what turns the base model into a reliable instruction‑following assistant, making data quality critically important—since even a small number of incorrect or hallucinated samples can instill undesirable behaviors. To address this, we apply a rigorous LLM‑as‑Judge framework alongside rule‑based filtering to curate high-quality samples. Together, the pipeline automatically assess each sample against structural, semantic, and behavioral criteria, fixing issues when possible and filtering out samples that fail to meet our quality standards.
Figure 4: The SFT data quality pipeline. Raw conversation data passes through an LLM-as-Judge with a multi-dimensional rubric, producing accept/borderline/reject verdicts. Hard-reject defects (hallucination, false premise, incorrect computation) trigger automatic rejection regardless of score.
Our rigorous LLM‑as‑Judge framework evaluates only assistant responses, treating system prompts, user inputs, retrieved documents, and tool outputs strictly as contextual information. This ensures that the judge assesses what the model says, rather than what it was asked to do. In RAG settings, responses that are not grounded in the retrieved context are flagged as hallucinations, while tool‑use outputs are validated against the set of allowed tools and their parameter schemas.
We employ specialized judge prompts tailored to different SFT data types, including multi‑turn dialogue, RAG‑augmented responses, tool‑calling interactions, and multilingual conversations. Each response is scored across six weighted dimensions—instruction following, correctness, completeness, conciseness, naturalness, and calibration (with optional critical‑thinking checks). Samples are accepted, flagged as borderline, or rejected based on deterministic score thresholds, with hard‑reject rules overriding scores for severe defects such as hallucinations, false premises, or incorrect computations.
To complement semantic evaluation, we apply a deterministic rule‑based pipeline that enforces structural integrity through text normalization, truncation and length filtering, schema validation, and leakage detection. A final global deduplication step ensures dataset‑wide uniqueness. All filtering and correction actions are fully auditable.
SFT Training Details
After passing through the LLM-as-Judge, rule-based filtering, and global deduplication pipeline, we fine-tune base models on these approximately 4.1 million high-quality samples. The following details apply to all three model variants:
Training Configuration:
Reinforcement Learning: Multi-Stage RL Pipeline
After SFT, we apply a multi-stage reinforcement learning pipeline to further improve the model's capabilities across specific domains. Rather than a single RL pass, we run multiple targeted RL stages, each optimizing for different capabilities.
Training Methodology
We use On-policy GRPO (Group Relative Policy Optimization) (Shao et al., 2024) with DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization) loss (Yu et al., 2025) which provides more stable training signals compared to standard GRPO. However, due to computationally intensive nature of dynamic sampling, we switch it off during our training runs.
RL training configuration
RL Pipeline
Figure 10 depicts our Reinforcement Learning pipeline for training Granite 4.1 models. Through extensive experimentation with a variety of reinforcement learning recipes, we found that this sequence of steps minimizes catastrophic forgetting while simultaneously maximizing performance across multiple domains.
Figure 10: The Granite 4.1 reinforcement learning pipeline consisting of four sequential stages: Multi-domain RL, RLHF, Identity and Knowledge-calibration RL, and Math RL.
Multi-domain RL
In this stage, the model is trained jointly on a unified mixture of data drawn from multiple domains. Every gradient update therefore reflects the full diversity of tasks, which prevents catastrophic forgetting, boosts overall benchmark performance, and minimizes regressions on any individual task.
The different domains covered in this stage include:
During this stage, we trained the models on 45,504 unique prompts (averaged across all Granite 4.1 models) and found that a learning rate of 5e‑7
with a KL‑loss coefficient ($\beta$) of 0.05
performed best for multi‑domain reinforcement learning.
RLHF
To further improve the model's helpfulness and chat ability, we train our model on generic-chat prompts using a multilingual scalar reward model. With this stage, we observed an average improvement of ~18.9 points (averaged across the three Granite 4.1 models) in Alpaca-Eval compared to the SFT checkpoints.
To mitigate policy drift from its previously learned knowledge, we use a conservative learning rate of 3e-7
and higher KL-loss coeff $\beta$ of 0.09
in this stage. We use an average of 17,920 unique prompts in this RLHF stage.
Identity & Knowledge-Calibration RL
In this stage, we train the model for a few steps (~40 training steps) on identity and knowledge calibration prompts. We observed that this small training stage significantly improves the model's self-identification capabilities.
Similar to the RLHF stage, we used a learning rate of 3e-7
and KL-loss coeff $\beta$ of 0.09
, and we use 1728 unique prompts in this stage.
Math RL
During our RL training, we found that the RLHF stage causes a drop in math benchmark scores (e.g., in GSM8K, DeepMind-Math). The Math RL stage enables the model to recover from this drop and surpasses the original SFT performance on math benchmarks: ~3.8 points on average for GSM8K, and ~23.48 points on average for DeepMind-Math. We use an average of 13,504 unique prompts in this stage and similar to the multi-domain RL stage, we used a learning rate of 5e-7
and KL-loss coeff $\beta$ of 0.05
.
Results
Base Model Benchmarks
Instruct Model Benchmarks
Supported languages: English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, and Chinese.
Granite 4.1 Comparison with Leading Open‑Source Models
Granite 4.1 delivers competitive instruction‑following and tool‑calling capabilities without relying on long chains of thought. By avoiding extended reasoning traces, it provides predictable latency, stable token usage, and lower operational cost. This makes Granite 4.1 a production‑ready, open‑source choice for enterprise workloads where efficiency, reliability, and cost control are critical.
Granite 4.1-8B vs. Granite 4.0-H-Small (32B-A9B)
A striking result: the Granite 4.1-8B dense model consistently matches or outperforms the previous-generation Granite 4.0-H-Small, a 32B-parameter Mixture-of-Experts model with 9B active parameters.
Figure 13: Granite 4.1-8B (dark blue) vs. Granite 4.0-H-Small 32B-A9B (light blue) across benchmarks. The 8B dense model matches or exceeds the larger MoE model on IFEval, AlpacaEval, MMLU-Pro, BBH, GSM8K, DeepMind-Math, Evalplus, ArenaHard, BFCL V3 and MBPP(+).
Granite 4.1 Model Family Comparison
Figure 14: Comparison across the Granite 4.1 family — 30B, 8B, and 3B models. Scores scale predictably with model size, with the 30B model leading across all benchmarks.
FP8 Quantization
We also released fp8 quantized variants of the Granite 4.1 models, optimized for inference with vLLM. The precision is reduced from 16‑bit to 8‑bit, resulting in approximately a 50% reduction in both disk footprint and GPU memory usage. Quantization is applied only to the weights and activations of linear operators within the transformer blocks using LLM Compressor, while all other layers are preserved at their original precision.
Infrastructure
We trained the Granite 4.1 Language Models on an NVIDIA GB200 NVL72 cluster hosted on CoreWeave:
- Intra-rack communication: 72-GPU NVLink domain
- Inter-rack communication: Non-blocking, full Fat-Tree NDR 400 Gb/s InfiniBand network
- Scale: Thousands of GPUs across the cluster
This infrastructure provides the scalable, high-bandwidth interconnect needed for efficient distributed training at the token volumes required (15T+ tokens across pre-training alone).
Getting Started
Granite 4.1 models are available under the Apache 2.0 license. Here's how to get started with the 30B instruct model wiht tool calling example:
pip install torch torchvision torchaudio
pip install accelerate
pip install transformers
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda"
model_path = "ibm-granite/granite-4.1-30b"
tokenizer = AutoTokenizer.from_pretrained(model_path)
# drop device_map if running on CPU
model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device)
model.eval()
tools = [
{
"type": "function",
"function": {
"name": "get_current_weather",
"description": "Get the current weather for a specified city.",
"parameters": {
"type": "object",
"properties": {
"city": {
"type": "string",
"description": "Name of the city"
}
},
"required": ["city"]
}
}
}
]
# change input text as desired
chat = [
{ "role": "user", "content": "What's the weather like in London right now?" },
]
chat = tokenizer.apply_chat_template(chat, \
tokenize=False, \
tools=tools, \
add_generation_prompt=True)
# tokenize the text
input_tokens = tokenizer(chat, return_tensors="pt").to(device)
# generate output tokens
output = model.generate(**input_tokens,
max_new_tokens=100)
# decode output tokens into text
output = tokenizer.batch_decode(output)
# print output
print(output[0])
Expected Output:
<|start_of_role|>system<|end_of_role|>You are a helpful assistant with access to the following tools. You may call one or more tools to assist with the user query.
You are provided with function signatures within <tools></tools> XML tags:
<tools>
{"type": "function", "function": {"name": "get_current_weather", "description": "Get the current weather for a specified city.", "parameters": {"type": "object", "properties": {"city": {"type": "string", "description": "Name of the city"}}, "required": ["city"]}}}
</tools>
For each tool call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:
<tool_call>
{"name": <function-name>, "arguments": <args-json-object>}
</tool_call>. If a tool does not exist in the provided list of tools, notify the user that you do not have the ability to fulfill the request.<|end_of_text|>
<|start_of_role|>user<|end_of_role|>What's the weather like in London right now?<|end_of_text|>
<|start_of_role|>assistant<|end_of_role|><tool_call>
{"name": "get_current_weather", "arguments": {"city": "London"}}
</tool_call><|end_of_text|>
Resources:
- Granite 4.1 HF Collection
- PRISM: Demystifying Retention and Interaction in Mid-Training
- GitHub: ibm-granite/granite-4.1-language-models
- Granite Documentation
- Granite Community Resources
Granite 4.1 marks a significant step forward for high‑quality, open‑source language models. By prioritizing data quality and rigor at every stage—from pre‑training curation to supervised fine‑tuning and multi‑stage reinforcement learning—we deliver a substantially improved post‑training pipeline. The result is stronger instruction following, tool use, and conversational performance, showing that carefully trained dense 8B models can rival much larger MoE architectures. We’re excited to see how the community adopts and builds on these models.
```

---

## 6. DeepInfra on Hugging Face Inference Providers 🔥

- 日期: 2026-04-29 00:00
- 链接: https://huggingface.co/blog/inference-providers-deepinfra

```
DeepInfra on Hugging Face Inference Providers 🔥
We're thrilled to share that DeepInfra is now a supported Inference Provider on the Hugging Face Hub!
DeepInfra joins our growing ecosystem, enhancing the breadth and capabilities of serverless inference directly on the Hub's model pages. Inference Providers are also seamlessly integrated into our client SDKs (for both JS and Python), making it super easy to use a wide variety of models with your preferred providers.
DeepInfra is a serverless AI inference platform offering one of the most cost-effective pricing per token in the industry. With a catalog of over 100 models, DeepInfra makes it easy for developers to integrate a wide range of AI capabilities into their applications with minimal setup.
DeepInfra supports a broad spectrum of model types - from LLMs to text-to-image, text-to-video, embeddings, and more. As part of this initial integration, DeepInfra is launching support for conversational and text-generation tasks on Hugging Face, enabling access to popular open-weight LLMs such as DeepSeek V4, Kimi-K2.6, GLM-5.1, and many more. Support for additional tasks (text-to-image, text-to-video, embeddings, and more) will roll out soon!
Read more about how to use DeepInfra as an Inference Provider in its dedicated documentation page.
See the full list of models supported by DeepInfra here.
Follow DeepInfra on Hugging Face: https://huggingface.co/DeepInfra.
How it works
In the website UI
- In your user account settings, you are able to:
- Set your own API keys for the providers you've signed up with. If no custom key is set, your requests will be routed through HF.
- Order providers by preference. This applies to the widget and code snippets in the model pages.
- As mentioned, there are two modes when calling Inference Providers:
- Custom key (calls go directly to the inference provider, using your own API key of the corresponding inference provider)
- Routed by HF (in that case, you don't need a token from the provider, and the charges are applied directly to your HF account rather than the provider's account)
- Model pages showcase third-party inference providers (the ones that are compatible with the current model, sorted by user preference)
From the client SDKs
DeepInfra is available through the Hugging Face SDKs - huggingface_hub
(>= 1.11.2) for Python and @huggingface/inference
for JavaScript.
The following examples show how to use DeepSeek V4 Pro through DeepInfra. Use a Hugging Face token to authenticate - the request will be routed to DeepInfra automatically.
From your favorite Agent Harness
Hugging Face Inference Providers are integrated in most Agent Harnesses - including Pi, OpenCode, Hermes Agents, OpenClaw, and more. This means you can plug DeepInfra-hosted models straight into your favorite tools without any extra glue code. Browse the full list of integrations here.
from Python
import os
from openai import OpenAI
client = OpenAI(
base_url="https://router.huggingface.co/v1",
api_key=os.environ["HF_TOKEN"],
)
completion = client.chat.completions.create(
model="deepseek-ai/DeepSeek-V4-Pro:deepinfra",
messages=[
{
"role": "user",
"content": "Write a Python function that returns the nth Fibonacci number using memoization."
}
],
)
print(completion.choices[0].message)
from JS
import { OpenAI } from "openai";
const client = new OpenAI({
baseURL: "https://router.huggingface.co/v1",
apiKey: process.env.HF_TOKEN,
});
const chatCompletion = await client.chat.completions.create({
model: "deepseek-ai/DeepSeek-V4-Pro:deepinfra",
messages: [
{
role: "user",
content: "Write a Python function that returns the nth Fibonacci number using memoization.",
},
],
});
console.log(chatCompletion.choices[0].message);
Billing
For direct requests, i.e. when you use the key from an inference provider, you are billed by the corresponding provider. For instance, if you use a DeepInfra API key you're billed on your DeepInfra account.
For routed requests, i.e. when you authenticate via the Hugging Face Hub, you'll only pay the standard provider API rates. There's no additional markup from us; we just pass through the provider costs directly. (In the future, we may establish revenue-sharing agreements with our provider partners.)
Important Note ‼️ PRO users get $2 worth of Inference credits every month. You can use them across providers. 🔥
Subscribe to the Hugging Face PRO plan to get access to Inference credits, ZeroGPU, Spaces Dev Mode, 20x higher limits, and more.
We also provide free inference with a small quota for our signed-in free users, but please upgrade to PRO if you can!
Feedback and next steps
We would love to get your feedback! Share your thoughts and/or comments here: https://huggingface.co/spaces/huggingface/HuggingDiscussions/discussions/49
```

---

## 7. Introducing NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal Intelligence for Documents, Audio and Video Agents

- 日期: 2026-04-28 15:58
- 链接: https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence

```
Introducing NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal Intelligence for Documents, Audio and Video Agents
- NVIDIA Nemotron 3 Nano Omni is a new omni-modal understanding model built for real-world document analysis, multiple image reasoning, automatic speech recognition, long audio-video understanding, agentic computer use, and general reasoning.
- It extends the Nemotron multimodal line from a strong vision-language system to a broader text + image + video + audio model.
- Nemotron 3 Nano Omni delivers best-in-class accuracy on complex document intelligence leaderboards such as MMlongbench-Doc, OCRBenchV2, while also leading in video and audio leaderboards like WorldSense and DailyOmni. It achieves top accuracy on VoiceBench for audio understanding and ranks as the most cost‑efficient open video understanding model on MediaPerf.
- Under the hood, it combines the Nemotron 3 hybrid Mamba-Transformer Mixture-of-Experts backbone with a C-RADIOv4-H vision encoder and Parakeet-TDT-0.6B-v2 audio encoder.
- The architecture is designed to preserve fine visual detail, add native audio understanding, and scale to very long multimodal contexts for dense images, documents, videos, and mixed-modality reasoning.
- The training recipe uses staged multimodal alignment and context extension, followed by preference optimization and multimodal reinforcement learning.
- Nemotron 3 Nano Omni delivers up to 9x higher throughput and 2.9x the single-stream reasoning speed on multimodal use-cases, compared to alternatives.
- Download the BF16, FP8 and NVFP4 checkpoints at HuggingFace.
- For more information about the model architecture, training recipe, data pipelines and benchmarks, read the full Nemotron 3 Nano Omni report.
Building on Nemotron Nano V2 VL, Nemotron 3 Nano Omni delivers substantial visual gains and adds entirely new audio and video+audio capabilities - while also leading another open-weights omni model, Qwen3-Omni, in many domains.
Efficiency highlights
Compared to other open omni models with the same interactivity, Nemotron 3 Nano Omni delivers 7.4x higher system efficiency for multi-document use cases and 9.2x higher system efficiency for video use cases
Figure 1. Total system throughput for multi-document and video use cases sustained by each model at a fixed per‑user interactivity threshold (tokens/sec/user)
What Nemotron 3 Nano Omni is designed for
At a high level, Nemotron 3 Nano Omni is aimed at five classes of workloads:
1. Real-world document analysis
This is not only about OCR. The model is positioned for long, messy, high-value documents where understanding depends on layout, tables, figures, formulas, section structure, and cross-page references. Think contracts, technical papers, reports, manuals, multi-page forms, or compliance packets. The model can handle 100+ page documents.
2. Automatic Speech Recognition
Nemotron 3 Nano Omni includes strong speech understanding capabilities that enable high-quality transcription across diverse audio conditions. It handles long-form audio with varying speakers, accents, and background noise. These capabilities can be integrated into broader workflows, allowing spoken content to be transcribed, analyzed, and combined with other modalities for tasks like summarization, question answering, and cross-modal reasoning.
3. Long audio-video understanding
Many enterprise and developer workflows depend on mixed audio and visual evidence: screen recordings with narration, training videos, meetings with slides, tutorials, product demos, customer support captures, and long-form video archives. Nemotron 3 Nano Omni is built to reason over those inputs jointly.
4. Agentic computer use
The Nemotron 3 Nano Omni model is specifically trained for agentic computer use, enabling it to assist with tasks in graphical user interface (GUI) environments. Its capabilities include interpreting screenshots, monitoring the state of the user interface, grounding its reasoning in on-screen visuals, and helping with action selection or workflow automation.
5. General multimodal reasoning
The model is designed for more than perception. It excels at reasoning-intensive tasks that require synthesizing information across long context windows, multiple modalities, and structured or semi-structured evidence. It can carry out multi-step reasoning, perform calculations, and connect signals from text, images, tables, and other inputs to arrive at coherent, well-supported answers.
Model architecture and key innovations
Nemotron 3 Nano Omni uses a unified encoder-projector-decoder design. The language backbone is Nemotron 3 Nano 30B-A3B, paired with the C-RADIOv4-H vision encoder and the Parakeet-TDT-0.6B-v2 audio encoder. The modality-specific encoders connect into the LLM backbone through lightweight projectors.
Figure 2. Model architecture of NVIDIA Nemotron 3 Nano Omni 30B-A3B
A hybrid Mamba-Transformer-MoE backbone for long multimodal context
The model backbone interleaves three key components: 23 Mamba selective state-space layers for efficient long-context processing; 23 MoE layers with 128 experts, top-6 routing, and a shared expert for conditional capacity; and 6 grouped-query attention layers to preserve strong global interaction and expressivity.
Nemotron 3 Nano Omni combines state-space models, attention, and MoE in a unified design that maintains strong reasoning performance while remaining practical for long, multimodal contexts.
Dynamic resolution for dense documents, charts, and screens
On the vision side, the Nemotron 3 Nano Omni replaces the tiling strategy used in the v2 model with dynamic resolution processing at native aspect ratio. Each image can be represented using a variable number of 16 x 16 patches, with a minimum of 1,024 to a maximum of 13,312 visual patches per image. For square images, this is equivalent to 512 x 512 and 1840 x 1840, respectively.
That flexibility is critical for handling high-resolution, complex visual inputs such as OCR-heavy documents, financial tables, slides, research figures, screenshots, and GUI layouts—especially when both fine details and overall structure need to be understood together.
Conv3D temporal compression for video
For video, Nemotron 3 Nano Omni uses a dedicated Conv3D tubelet embedding path. Instead of embedding each frame independently, every pair of consecutive frames is fused into a single "tubelet" before the ViT, halving the number of vision tokens the language model has to attend to. This allows us to either double the number of frames with the same token budget, or halve the number of tokens with the same number of frames
EVS — Efficient Video Sampling
EVS is an important feature, enabled during inference time, that drops redundant video tokens after the vision encoder. This reduces latency and improves throughput while maintaining accuracy. The first frame of the video is kept entirely, then for each subsequent frame, EVS keeps the “dynamic” tokens where the video is changing and drops the “static” ones where nothing has changed from the previous frame. We combine this with Conv3D to enable superior compression: Conv3D fuses tokens from pairs of frames into one, and then EVS prunes redundant static information.
Native audio input, not just text transcripts
The audio side is powered by Parakeet-TDT-0.6B-v2, connected to the backbone through its own 2-layer MLP projector. Audio is sampled at 16 kHz, and the model is trained with inputs up to 1,200 seconds (20 minutes), while the LLM max context length supports 5+ hours.
This represents a shift from traditional VLM pipelines by enabling native audio processing within a shared multimodal sequence, allowing audio, visual, and text tokens to be jointly modeled. This is crucial for scenarios like narrated screen recordings, video Q&A where speech alters visual meaning, long-form instructional or meeting content, and tasks requiring temporally grounded multimodal reasoning.
Lightweight modality projectors and unified token interleaving
Each encoder is connected to the LLM with a lightweight 2-layer MLP projector that maps encoder features into the shared embedding space. Once projected, vision, audio, and text tokens are interleaved and processed jointly.
This design keeps the overall system modular while still enabling genuine cross-modal reasoning inside the backbone itself.
Training data, infrastructure and systems story
The SFT stages are trained on NVIDIA H100, scaling from 32 to 128 nodes depending on the stage. The stack uses Megatron-LM, Transformer Engine, and Megatron Energon, with tensor parallelism, expert parallelism, sequence parallelism, context parallelism for the long context stages, online sequence packing, and selective activation recomputation.
Post-SFT reinforcement learning uses NeMo-RL and NeMo Gym with a Megatron backend. The RL infrastructure used a Ray-based distributed setup across B200 and H100 clusters, plus multimodal deduplication, so repeated rollouts do not multiply image, video, and audio memory.
We open-source substantial parts of our training code.
Using RL to shape reliable multimodal behavior
We introduce multi-environment text and omni training in Nemotron 3 Nano Omni. Our text RL training stage happens across diverse environments in Nemo-Gym, which evaluates the model’s ability to perform sequences of actions such as tool calling, writing code, and multi-part planning that satisfy the verifiable criteria.
Omni RL trains the model to reason across images, video, audio, and text within a unified framework, covering tasks from single-modality to fully multimodal scenarios. A diverse verifier suite evaluates outputs across formats like multiple-choice, math, GUI grounding, and ASR, while intentionally including unanswerable cases to teach the model to abstain when evidence is insufficient rather than hallucinate.
Data and data pipelines
Nemotron 3 Nano Omni is trained on an enhanced dataset that emphasizes high-quality reasoning across multiple modalities. We significantly expand task coverage and introduce synthetic data for complex reasoning scenarios where public datasets are limited. To support this, we build task-specific, multi-stage pipelines for scalable synthetic data generation.
As one example, we generated approximately 11.4M synthetic QA pairs (~45B tokens) from a large corpus of real-world PDFs using NeMo Data Designer. This dataset is used to strengthen long-context document reasoning during post-training and delivers a 2.19× improvement in overall accuracy on MMLongBench-Doc.
We detail the full pipeline evolution, including failure analysis and key lessons learned, in our Data Designer developer note. The note also includes nine runnable pipeline recipes that can serve as starting points for building your own document-understanding datasets.
Example workflows
Example 1: Long multi-page document analysis
Nemotron 3 Nano Omni can analyze and reason over long documents such as financial reports, academic papers, product manuals, etc. The following example retrieves financial metrics across a 100+ page document to calculate another metric:
Figure 3: Stylized example from the MMLongBench-Doc benchmark
The model was prompted to answer the question as follows:
Extract information from all the given images, then answer the question using a single word or phrase. Return 'Not answerable' if the answer cannot be derived from the the images.
The model is capable of long-context retrieval, structured extraction, table/chart reading and multi-page reasoning all in one go.
Example 2: Video + audio understanding
Nemotron-3 Nano Omni performs joint audio-visual analysis, both locally for specific scenes and globally across the entire video. This enables it to answer complex questions that require cross-modal reasoning—such as identifying specific visuals shown exactly when a certain topic is mentioned in the audio.
Video
Question
Watch the video and listen to the narration.
1.What structure is on fire as shown in the video and how much money was being spent in its renovation project ?
2. Describe in short what visuals are shown when the eye-witness narrates her experience?
Answer
1. The structure on fire is the Notre Dame Cathedral, which was undergoing an almost $7 million renovation project.
2. When the eye-witness narrates her experience, the visuals show the cathedral engulfed in flames and thick smoke, scaffolding surrounding the burning roof, firefighters using ladders to spray water, a crowd of people watching from the riverbank, and views of the burning structure against the Paris skyline.
Example 3: Agentic computer use / screenshot reasoning
Nemotron 3 Omni can be integrated into agentic computer-use systems to reason over user intents, analyze GUI elements, and execute actions to accomplish tasks.
The model was given access to a web environment with the following system prompt:
You are a GUI agent. You are given an instruction, a screenshot of the screen and your previous interactions with the computer. You need to perform a series of actions to complete the task. The passoword of the computer is {password}.
For each step, provide your response in this format:
{thought}
## Action:
{action}
## Code:
{code}
In the code section, the code should be either pyautogui code or one of the following functions wrapped in the code block:
- {"name": "computer.wait", "description": "Make the computer wait for 20 seconds for installation, running code, etc.", "parameters": {"type": "object", "properties": {}, "required": []}}
- {"name": "computer.terminate", "description": "Terminate the current task and report its completion status", "parameters": {"type": "object", "properties": {"status": {"type": "string", "enum": ["success", "failure"], "description": "The status of the task"}, "answer": {"type": "string", "description": "The answer of the task"}}, "required": ["status"]}}
User Instruction
Find the Driver License Eligibility Requirements
Model Response:
The GIF above shows the actions that the agent takes to fulfill the user’s request
- It clicks on the “License & IDs” tab
- Then it clicks on “Driver’s License” from the dropdown menu
- Then it clicks on “Driver’s License Eligibility” on the left
- It scrolls down on this page and back up
- Finally it produces the following response for the user:
Successfully found the Driver License Eligibility Requirements page on the Virginia DMV website. The page contains comprehensive information about driver license eligibility including:
**General Requirements:**
- Must be a resident of the Commonwealth of Virginia
- Must be at least 16 years and 3 months of age
**First Time Drivers:**
- Must complete a state-approved driver education program
- Must obtain a learner's permit at least 60 days before taking the road skills test
- Must be at least 15 years and 6 months of age for a learner's permit
- No exceptions to age requirements
**New Residents:**
- Temporary residents: must obtain license within 6 months
- Permanent residents: must obtain license within 1 year
**Military Personnel:**
- Active-duty members of the Armed Forces stationed in Virginia
- Spouses and dependents 16 years and 3 months or older may drive with valid out-of-state license
- If vehicle is co-owned and out-of-state plates are used, all co-owners must be active duty members
**Out-of-State Students:**
- Full-time students enrolled in accredited Virginia schools (not employed) may drive with valid out-of-state license
- Full-time students who are employed are considered Virginia residents for vehicle laws
**Non-Residents:**
- Non-residents temporarily living in Virginia may drive with home state license for no more than 6 months
- Note: This does not apply to commercial vehicle drivers
- If becoming gainfully employed, must hold Virginia driver's license
**Identification and Residency Requirements:**
- Proof of identity (acceptable documents listed in DMV 141)
- Proof of legal presence in the U.S.
- Proof of Virginia residency
- Proof of Social Security number
- Proof of name change (if applicable)
Additional resources available: interactive document guide, "Acceptable Documents for Obtaining a Driver's License or Photo ID Card" (DMV 141), and Spanish language version.
Example 4: Mixed document + chart + narration reasoning
Nemotron-3 Nano Omni can analyze charts, figures shown in images, along with audio files to generate any commonalities, discrepancies across the media.
Audio
Question
Use both the slide content and the spoken commentary.
List out any extra points mentioned by the speaker that is not shown in the slide
Answer
Based on the speaker's commentary and the visual content of the slide, here are the extra points mentioned that are not explicitly shown or detailed in the slide:
* **The Topic:** The speaker explicitly states she will be covering **multitask learning** with neural networks, while the slide title is simply "Some notation" (though it contains the mathematical definitions for tasks).
* **Nature of the Output:** She describes the output ($y$) as a **probability distribution** over possible labels (e.g., tiger, tiger cat, lynx, cat), whereas the slide only shows a bar chart with class labels without explicitly labeling the vector as a distribution.
* **Specific Task Example (Paper Titles):** She introduces a concrete example where the input is the **title of a paper** and the neural network is tasked with estimating the **length of the paper**. The slide shows "length of paper" near the bar chart, but does not visually distinguish how a paper title maps to these bars versus representing animal classes.
* **Optimization Techniques:** She mentions that the loss function is typically optimized using **stochastic gradient descent** or a **"favorite optimizer,"** which are procedural steps not written on the slide (which only defines the loss function $\mathcal{L}$ to minimize).
* **Input Diversity:** She specifies that inputs can be a **"wide range of unstructured inputs,"** specifically mentioning **images** and **text**. The slide visually displays a single image (a structured input) and uses a generic variable $x$ for the input class.
Example 5: Soundscape
Nemotron-3 Nano Omni can analyze charts, figures shown in images, along with audio files to generate any commonalities, discrepancies across the media.
Audio
Question
What is producing the main sound in this audio, and what does the acoustic environment suggest about where it was recorded?
Answer
The main sound is a bird chirping, and the presence of multiple bird calls and a natural, open acoustic environment suggests the recording was made outdoors in a natural setting like a forest or park.
Example 6: Music
Nemotron-3-Nano-Omni can interpret and reason about general audio, including soundscapes and environmental sounds.
Audio
Question
What's the overall vibe of this song, and what kind of scenario would it complement well?
Answer
The song has a calm, reflective, and slightly melancholic vibe, with a gentle piano melody and soft string accompaniment. It would complement a quiet, introspective scene such as a rainy evening, a peaceful walk, or a moment of personal reflection.
Getting started with Nemotron 3 Nano Omni
References
- NVIDIA Nemotron Nano V2 VL. Technical report: https://arxiv.org/abs/2511.03929
- NVIDIA Nemotron 3: Efficient and Open Intelligence. Technical report: https://arxiv.org/abs/2512.20856
- C-RADIOv4-H. Hugging Face model page: https://huggingface.co/nvidia/C-RADIOv4-H
- Parakeet-TDT-0.6B-v3. Hugging Face model page: https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3
- Megatron-LM. GitHub: https://github.com/NVIDIA/Megatron-LM
- Transformer Engine. GitHub: https://github.com/NVIDIA/TransformerEngine
- Megatron Energon. GitHub: https://github.com/NVIDIA/Megatron-Energon
```

---

## 8. How to build scalable web apps with OpenAI's Privacy Filter

- 日期: 2026-04-27 00:00
- 链接: https://huggingface.co/blog/openai-privacy-filter-web-apps

```
How to build scalable web apps with OpenAI's Privacy Filter
- Document Privacy Explorer: drop in a PDF or DOCX, read the document back with every PII span highlighted in place.
- Image Anonymizer: upload an image, get it back with redacted black bars over names, emails, and account numbers. The image is also editable on a canvas so you can make your own annotations before downloading.
- SmartRedact Paste: paste sensitive text, share a public URL that serves the redacted version, keep a private reveal link for yourself.
All three are built on gradio.Server, which lets you pair custom HTML/JS frontends with Gradio's queueing, ZeroGPU allocation, and gradio_client
SDK. In all these apps, gradio.Server
plays the same backend role, and that consistency is exactly what makes it really powerful.
The model
Privacy Filter is a 1.5B-parameter model with 50M active parameters, permissively licensed under Apache 2.0. PII categories are private_person
, private_address
, private_email
, private_phone
, private_url
, private_date
, account_number
, secret
. Context is 128,000 tokens. Achieves state-of-the-art performance on the PII-Masking-300k benchmark. Full numbers and methodology are in the official release blog.
1. Document Privacy Explorer
Try it at ysharma/OPF-Document-PII-Explorer.
User problem. You want to read a PII-heavy document (a contract, a resume, an exported chat log) with every detected span highlighted by category, a filter in the sidebar, and a summary dashboard up top. The reading experience should feel like a normal document, not a form.
What Privacy Filter does here. The whole file goes through in a single 128k-context forward pass, so there's no chunking, no stitching, and span offsets line up directly with the rendered text. BIOES decoding keeps span boundaries clean through long ambiguous runs.
What gr.Server
does here. You could wire this up in Blocks with gr.HighlightedText
and a sidebar, and it would work. The reading experience we wanted (serif body, category filters that toggle CSS classes client-side instead of re-running the model, a summary dashboard that doesn't force a page re-render) was easier to hand-author than to compose. gr.Server
lets us serve the reader view as a single HTML file and expose the model behind one queued endpoint:
import gradio as gr
from fastapi.responses import HTMLResponse
from gradio.data_classes import FileData
server = gr.Server()
@server.get("/", response_class=HTMLResponse)
async def homepage():
return FRONTEND_HTML # reader view; see app.py
@server.api(name="analyze_document")
def analyze_document(file: FileData) -> dict:
text = extract_text(file["path"]) # PyMuPDF / python-docx
source_text, spans = run_privacy_filter(text) # single 128k pass
return {
"text": source_text,
"spans": spans, # [{start, end, label}, ...]
"stats": compute_stats(source_text, spans),
}
Note the decorator: @server.api(name="analyze_document")
, not a plain @server.post
. That's the piece that plugs the handler into Gradio's queue, so concurrent uploads are serialized, @spaces.GPU
composes correctly on ZeroGPU, and the same endpoint is reachable from both the browser and gradio_client
with no duplicated code. The browser calls it with the Gradio JS client:
<script type="module">
import { Client, handle_file } from "https://cdn.jsdelivr.net/npm/@gradio/client/dist/index.min.js";
const client = await Client.connect(window.location.origin);
async function uploadFile(file) {
const result = await client.predict("/analyze_document", { file: handle_file(file) });
renderResults(result.data[0]); // { text, spans, stats }
}
</script>
2. Image Anonymizer
Try it at ysharma/OPF-Image-Anonymizer.
User problem. You want to share an image or any screenshot (a Slack thread, a receipt, a Stripe dashboard) with black bars over the PII. You want to toggle bars on and off, drag them to reposition, or draw one by hand for anything the model missed, then export the result.
What Privacy Filter does here. Tesseract runs OCR and returns per-word bounding boxes. The backend reconstructs the full text with a char-offset to box map, then runs Privacy Filter once over the whole text. Detected character spans are looked up against the word map and joined into pixel rectangles per line.
What gr.Server
does here. gr.ImageEditor
supports layered annotation and is a reasonable starting point for image redaction. The workflow we wanted (per-bar category metadata, toggle all bars in a category at once, client-side PNG export at natural resolution with no server round-trip) was cleaner to build on a custom <canvas>
frontend. gr.Server
hands back pixel rectangles from one queued endpoint and lets the canvas own everything else:
@server.api(name="anonymize_screenshot")
def anonymize_screenshot(image: FileData) -> dict:
img = Image.open(image["path"]).convert("RGB")
full_text, char_to_box = ocr_image(img) # per-word boxes + char map
spans = run_privacy_filter(full_text)
boxes = spans_to_pixel_boxes(spans, char_to_box)
return {
"image_data_url": pil_to_base64(img),
"width": img.width,
"height": img.height,
"boxes": boxes, # [{x, y, w, h, label, text}, ...]
}
The frontend invokes it with client.predict("/anonymize_screenshot", { image: handle_file(file) })
, the same pattern as above. Toggles, drags, new-bar drawing, and PNG export all happen in the browser; edits never round-trip to the server.
3. SmartRedact Paste
Try it at ysharma/OPF-SmartRedact-Paste.
User problem. You want a pastebin that redacts before sharing. You paste a log line, an email, a support ticket. You get two URLs back. The public one serves the redacted version with <PRIVATE_PERSON>
, <PRIVATE_EMAIL>
, <ACCOUNT_NUMBER>
placeholders, following the redaction convention from the official blog examples. The private one is gated by a token you keep and shows the original with spans highlighted.
What Privacy Filter does here. Swap each detected span with a <CATEGORY>
placeholder on the stored paste. That's the entire redaction step. Multilingual text (Spanish, French, Chinese, Hindi, and others in the model-card examples) routes through the same call with no change.
What gr.Server
does here. This app needs two distinct GET routes for the same paste ID, one public and one token-gated, and the URL shape matters because the reveal URL is the thing you keep. gr.Server
works here because it's a FastAPI app underneath — which is also why @server.api
and plain @server.get
can sit side by side in the same process. Note: this can also be built with gr.Blocks()
by mounting custom routes with FastAPI :
# Model call → queued endpoint. Hit from the browser via
# client.predict("/create_paste", { text, ttl }).
@server.api(name="create_paste")
def create_paste(text: str, ttl: str = "never") -> dict:
source_text, spans = run_privacy_filter(text)
redacted = redact(source_text, spans) # <CATEGORY> placeholders
pid, reveal_token = secrets.token_urlsafe(6), secrets.token_urlsafe(22)
PASTES[pid] = Paste(pid, reveal_token, source_text, redacted, spans,
expires_at=_ttl(ttl)) # see app.py
return {
"view_path": f"/view/{pid}",
"reveal_path": f"/view/{pid}?token={reveal_token}",
}
# View page → plain FastAPI GET. No model, no queue needed, and we
# actually want the bespoke URL shape `/view/{pid}?token=...` that a
# queued endpoint couldn't give us.
@server.get("/view/{pid}", response_class=HTMLResponse)
async def view_paste(pid: str, token: str | None = None):
p = _store_get(pid) # see app.py for store
if p is None:
return HTMLResponse(_not_found(), status_code=404)
revealed = bool(token) and secrets.compare_digest(token, p.reveal_token)
return HTMLResponse(_render_view(p, revealed))
A daemon thread evicts expired pastes every 30 seconds. The whole service, including storage, is about 200 lines of application code because everything lives in one process.
What gradio.Server
provides
The split across all three apps is the same — anything that touches the model goes through @server.api
, everything else stays on plain FastAPI routes:
@server.api
gives you Gradio's queue (serialized requests, correct @spaces.GPU
composition on ZeroGPU, progress events) and it's what the browser hits through @gradio/client
. The same endpoint is also what gradio_client
users hit from Python — one function, two SDKs, no duplicated code. Plain @server.get
/@server.post
are reserved for the static surfaces: HTML pages, file lookups, cheap dict reads. That's the rule of thumb from the gradio.Server intro post, and it's what makes these three apps feel consistent even though their UIs are very different.
Try them
Drop in a resume, a screenshot of a Slack thread, a log line with a token in it. The fun part is seeing what Privacy Filter catches (and occasionally misses) on text you actually care about.
Recommended reading
- OpenAI's release post: Introducing OpenAI Privacy Filter
- Model card: openai/privacy-filter on Hugging Face
- Redaction examples and taxonomy on Model card
```

---

## 9. DeepSeek-V4: a million-token context that agents can actually use

- 日期: 2026-04-24 00:00
- 链接: https://huggingface.co/blog/deepseekv4

```
DeepSeek-V4: a million-token context that agents can actually use
Focusing on long running agentic workloads. Running a frontier open model as an agent today breaks in predictable ways. The model stops. You reprompt. The trace blows past the context budget, or the KV cache fills the GPU, or tool-call round trips degrade halfway through a long task. V4 is built to fix these known failures, and point the way for the community to follow.
This post covers three things: what the architecture does differently to make long-context inference cheap, the agent-specific post-training decisions that compound on top of it, and some takeaways from the paper that help reason about these changes.
The KV cache problem for agents
A 1M context window is just capacity, not performance. Whether you can use it depends on the cost of every forward pass at that depth. For an agent running a long tool-use trajectory (a SWE-bench task, a multi-step browse session, a terminal session with hundreds of commands), every tool result is appended to the context, and every subsequent token pays the full attention cost against everything that came before.
Two numbers matter: single-token inference FLOPs and KV cache size. Both grow with sequence length. At 1M tokens, DeepSeek-V4-Pro requires 27% of single-token inference FLOPs compared with DeepSeek-V3.2, so it runs faster on the same hardware. It also uses 10% of the KV cache memory. V4-Flash drops these numbers even further: 10% of the FLOPs and 7% of the KV cache.
If we compare the KV cache memory against a established architecture like grouped query attention with 8 heads, stored in the usual bfloat16 format, DeepSeek v4 requires roughly 2% the cache size. This makes it much easier to deploy for very large context handling.
Figure 1: benchmark comparison (left), per-token FLOPs and accumulated KV cache against sequence length (right).
Hybrid attention: CSA and HCA
The efficiency gain comes from splitting attention into two mechanisms and interleaving them across layers.
Compressed Sparse Attention (CSA) compresses KV entries by 4x along the sequence dimension using softmax-gated pooling with a learned positional bias. A lightning indexer (FP4, ReLU-scored multi-head dot product) picks the top-k compressed blocks per query. It inherits the sparse-selection idea from DeepSeek Sparse Attention in V3.2, but runs it over blocks that are already 4x shorter than the original sequence. The indexer's search space shrinks with it.
Figure 3: CSA. The compressor collapses every 4 tokens into one compressed KV entry. The lightning indexer picks the top-k compressed blocks per query. A sliding-window branch handles the most recent uncompressed tokens.
Heavily Compressed Attention (HCA) compresses KV entries by 128x and drops the sparse selection. Every query attends densely to every compressed block. The compressed sequence is short enough that dense attention is cheap.
Figure 4: HCA. A heavier compressor (128x vs. 4x) followed by dense attention over the compressed stream, with the same sliding-window branch for recency.
The layers alternate between CSA and HCA. Different layers carry different attention patterns, and forcing one mechanism across all of them wastes capacity. In V4-Pro's 61-layer stack, layers 0–1 are HCA, layers 2–60 alternate CSA and HCA, and the MTP block at the end runs sliding-window only.
Both paths use FP8 storage for most KV entries and BF16 only for the RoPE dimensions. The lightning indexer inside CSA runs in FP4. These storage choices compound with the compression ratios to produce the 2% KV cache figure.
Figure 2: overall architecture. Attention layers alternate between CSA and HCA. Feed-forward layers use DeepSeekMoE. Residual connections are replaced with manifold-constrained hyper-connections (mHC).
What changes for agents
Efficient long-context attention is necessary for agent workflows but not sufficient. The paper describes three post-training and infrastructure choices that target agent use cases directly.
Interleaved thinking across tool calls
V3.2 kept reasoning traces across tool-result rounds but discarded them whenever a new user message arrived. For an agent handling a single user turn, this was fine. For multi-turn agentic workflows, where the user sends a follow-up after the agent has already chained several tool calls, the model lost its accumulated reasoning and had to reconstruct state.
V4 preserves reasoning content across user message boundaries when the conversation contains tool calls. The model retains the complete reasoning history across all rounds, including across user turns. This allows a coherent, cumulative chain of thought over long-horizon agent tasks. For conversational use without tools, the old behavior is preserved: reasoning is flushed on each turn to keep context concise.
Figure 7: thinking with tools (top) preserves reasoning across all turns. Thinking without tools (bottom) discards reasoning at each new user message.
Tool-call schema with dedicated tokens
V4 introduces a |DSML|
special token and an XML-based tool-call format. The XML format reduces escaping failures compared to JSON-in-string tool calls, a common failure mode when models emit nested quoted content.
The schema separates string parameters (passed as-is with string="true"
) from structured parameters (passed as JSON with string="false"
). This removes a class of parsing errors around numbers and booleans that JSON tool-call formats routinely hit.
DSec: a sandbox built for RL rollouts
The agent behavior was trained with RL against real tool environments. The paper describes the sandbox infrastructure built for that purpose. DeepSeek Elastic Compute (DSec) is a Rust platform that exposes four execution substrates behind one Python SDK: function calls, containers, microVMs (Firecracker), and full VMs (QEMU). A single cluster runs hundreds of thousands of concurrent sandboxes.
Three DSec features matter for agent training: fast image loading via layered 3FS storage (so RL rollouts do not wait on container startup), preemption-safe trajectory replay (so interrupted training steps resume without re-running tool calls), and a uniform API across substrates (so training harnesses target function calls or full VMs without rewriting). These infrastructure decisions underpin the agent benchmark scores.
Agent benchmark results
The knowledge and reasoning numbers are competitive but not leading. The agent numbers are where V4-Pro-Max separates from the field.
Specific numbers from the agent section of Table 6:
- Terminal Bench 2.0: V4-Pro-Max scores 67.9, ahead of GLM-5.1 (63.5) and K2.6 (66.7), behind GPT-5.4-xHigh (75.1) and Gemini-3.1-Pro (68.5).
- SWE Verified: 80.6 resolved, within a point of Opus-4.6-Max (80.8) and Gemini-3.1-Pro (80.6).
- MCPAtlas Public: 73.6, second only to Opus-4.6-Max (73.8).
- Toolathlon: 51.8, ahead of K2.6 (50.0), GLM-5.1 (40.7), and Gemini-3.1-Pro (48.8).
In the paper's internal R&D coding benchmark, 30 curated tasks across PyTorch, CUDA, Rust, and C++, V4-Pro-Max hits 67% pass rate, versus 47% for Sonnet 4.5 and 70% for Opus 4.5. In a survey of 85 DeepSeek developers using V4-Pro as their daily driver, 52% said it was ready to replace their current primary coding model and 39% leaned toward yes.
The long-context retrieval numbers are in Figure 9. MRCR 8-needle accuracy stays above 0.82 through 256K tokens and holds at 0.59 at 1M.
Figure 9: MRCR 8-needle retrieval. V4-Pro-Max stays above 0.82 through 256K and holds at 0.59 at 1M.
Using the models
Four checkpoints are on the Hub. The instruct models use FP4 for MoE expert weights and FP8 for everything else. The base models are FP8 throughout.
- deepseek-ai/DeepSeek-V4-Pro (1.6T / 49B activated, instruct)
- deepseek-ai/DeepSeek-V4-Flash (284B / 13B activated, instruct)
- deepseek-ai/DeepSeek-V4-Pro-Base (1.6T / 49B activated, base)
- deepseek-ai/DeepSeek-V4-Flash-Base (284B / 13B activated, base)
Both instruct models support three reasoning modes: Non-think (fast, no chain of thought), Think High (explicit reasoning in <think>
blocks), and Think Max (maximum reasoning effort with a dedicated system prompt). Think Max requires a context window of at least 384K tokens. The recommended sampling parameters across all modes are temperature=1.0, top_p=1.0
.
The V4-Pro numbers on SWE Verified, MCPAtlas, and the internal R&D benchmark put it at parity with frontier closed models on agent tasks. The open question is how the community's tool harnesses adapt to the |DSML|
schema and whether the interleaved thinking gains transfer to out-of-domain agent frameworks.
Figures in this blog post are from the technical report at DeepSeek_V4.pdf.
```

---

## 10. How to Use Transformers.js in a Chrome Extension

- 日期: 2026-04-23 00:00
- 链接: https://huggingface.co/blog/transformersjs-chrome-extension

```
How to Use Transformers.js in a Chrome Extension
While building it, we ran into several practical observations about Manifest V3 runtimes, model loading, and messaging that are worth sharing.
Who this is for
This guide is for developers who want to run local AI features in a Chrome extension with Transformers.js under Manifest V3 constraints.
By the end, you will have the same architecture used in this project: a background service worker that hosts models, a side panel chat UI, and a content script for page-level actions.
What we will build
In this guide, we will recreate the core architecture of Transformers.js Gemma 4 Browser Assistant, using the published extension as a reference and the open-source codebase as the implementation map.
- Live extension: Chrome Web Store
- Source code: github.com/nico-martin/gemma4-browser-extension
- End result: a background-hosted Transformers.js engine, a side panel chat UI, and a content script for page extraction and highlighting.
1) Chrome extension architecture (MV3)
Before diving in, a quick scope note: I will not go deep on the React UI layer or Vite build configuration. The focus here is the high-level architecture decisions: what runs in each Chrome runtime and how those pieces are orchestrated.
If Manifest V3 is new to you, read this short overview first: What is Manifest V3?.
1.1 Runtime contexts and entry points
In MV3, your architecture starts in public/manifest.json
. This project defines three entry points:
background.service_worker = background.js
, built fromsrc/background/background.ts
.side_panel.default_path = sidebar.html
, built fromsrc/sidebar/index.html
.content_scripts[].js = content.js
withmatches: http(s)://*/*
andrun_at: document_idle
, built fromsrc/content/content.ts
.
The background service worker also handles chrome.action.onClicked
to open the side panel for the active tab.
Related entry point to know: a popup can be defined with action.default_popup
and works well for quick actions. This project uses a side panel for persistent chat, but the orchestration pattern is the same.
1.2 What runs where
The key design decision is to keep heavy orchestration in the background and keep UI/page logic thin.
- Background (
src/background/background.ts
) is the control plane: agent lifecycle, model initialization, tool execution, and shared services like feature extraction. - Side panel (
src/sidebar/*
) is the interaction layer: chat input/output, streaming updates, and setup controls. - Content script (
src/content/content.ts
) is the page bridge: DOM extraction and highlight actions.
One practical consequence of this division is that the conversation history also lives in background (Agent.chatMessages
): the UI sends events like AGENT_GENERATE_TEXT
, background appends the message, runs inference, then emits MESSAGES_UPDATE
back to the side panel.
This split avoids duplicate model loads, keeps the UI responsive, and respects Chrome's security boundaries around DOM access.
1.3 Messaging contract
Once runtimes are separated, messaging becomes the backbone. In this project, all messages are typed through enums in src/shared/types.ts
.
- Side panel -> background (
BackgroundTasks
):CHECK_MODELS
,INITIALIZE_MODELS
AGENT_INITIALIZE
,AGENT_GENERATE_TEXT
,AGENT_GET_MESSAGES
,AGENT_CLEAR
EXTRACT_FEATURES
- Background -> side panel (
BackgroundMessages
):DOWNLOAD_PROGRESS
,MESSAGES_UPDATE
- Background -> content (
ContentTasks
):EXTRACT_PAGE_DATA
,HIGHLIGHT_ELEMENTS
,CLEAR_HIGHLIGHTS
The orchestration rule is simple: the background is the single coordinator; side panel and content script are specialized workers that request actions and render results.
Typical request flow:
- Side panel sends
AGENT_GENERATE_TEXT
. - Background appends to
Agent.chatMessages
and runs model/tool steps. - Background emits
MESSAGES_UPDATE
. - Side panel re-renders from the updated message list.
2) Transformers.js integration details
2.1 Models and responsibilities
In src/shared/constants.ts
, this extension uses two model roles:
- TextGeneration / LLM:
onnx-community/gemma-4-E2B-it-ONNX
(text-generation
,q4f16
) - VectorEmbeddings:
onnx-community/all-MiniLM-L6-v2-ONNX
(feature-extraction
,fp32
)
The split is intentional: Gemma 4 handles reasoning/tool decisions, while MiniLM generates vector embeddings for the semantic similarity search in ask_website
and find_history
.
2.2 Where inference runs
All inference runs in background (src/background/background.ts
):
- text generation via
pipeline("text-generation", ...)
with consistent KV Caching enabled by our newDynamicCache
class - embeddings via
pipeline("feature-extraction", ...)
plus vector normalization
This gives a single model host for all tabs/sessions, avoids duplicate memory usage, and keeps the side panel UI responsive. Because models are loaded from the background service worker, artifacts are cached under the extension origin (chrome-extension://<extension-id>
) rather than per-website origins, which gives one shared cache for the whole extension install.
MV3 lifecycle note: service workers can be suspended and restarted, so model runtime state should be treated as recoverable and re-initialized when needed.
2.3 Download and cache lifecycle
The model lifecycle is explicit:
CHECK_MODELS
inspects what is already cached and estimates remaining download size.INITIALIZE_MODELS
downloads/initializes models and emitsDOWNLOAD_PROGRESS
to the UI.- Long-lived instances are reused after setup:
- generation pipeline in
src/background/agent/Agent.ts
- embedding pipeline in
src/background/utils/FeatureExtractor.ts
- generation pipeline in
Permissions and privacy are part of the architecture, not a checkbox at the end. In this project, public/manifest.json
asks for sidePanel
, storage
, scripting
, and tabs
, plus host_permissions
for http(s)://*/*
:
sidePanel
: required to open and control the side panel UX.storage
: required to persist tool/settings state across sessions.tabs
+scripting
: required for tab-aware tools and page-level actions.host_permissions
onhttp(s)://*/*
: required because content extraction/highlighting is designed to work on arbitrary websites.
Why keep this narrow: permissions define user trust and Chrome Web Store review risk. Request only what your features actually need, and state clearly that inference runs locally in the extension runtime so users understand where their data is processed.
3) Agent and tool execution loop
3.1 Tool-calling basics (why this layer exists)
Before the execution loop, it helps to understand how model tool calling works (the basis for any agentic workflow). You pass messages plus a tool schema (name
, description
, and parameters
), and Transformers.js formats the actual prompt from those inputs using the model's chat template. Because chat templates are model-specific, the exact tool-call format depends on the model you use. With Gemma-4-style templates, the model emits a special tool-call token block when it decides to call one.
import { pipeline } from "@huggingface/transformers";
const generator = await pipeline(
"text-generation",
"onnx-community/gemma-4-E2B-it-ONNX",
{
dtype: "q4f16",
device: "webgpu",
},
);
const messages = [{ role: "user", content: "What's the weather in Bern?" }];
const output = await generator(messages, {
max_new_tokens: 128,
do_sample: false,
tools: [
{
type: "function",
function: {
name: "getWeather",
description: "Get the weather in a location",
parameters: {
type: "object",
properties: {
location: {
type: "string",
description: "The location to get the weather for",
},
},
required: ["location"],
},
},
},
],
});
At generation time, the model can emit output like:
<|tool_call>call:getWeather{location:<|"|>Bern<|"|>}<tool_call|>
That is exactly why this project has a normalization layer (webMcp
) and a parser (extractToolCalls
): model output must be converted into deterministic tool executions.
3.2 Tool interface in this project
src/background/agent/webMcp.tsx
normalizes extension tools into a model-friendly shape:
name
,description
,inputSchema
,execute
Example tools include get_open_tabs
, go_to_tab
, open_url
, close_tab
, find_history
, ask_website
, and highlight_website_element
.
3.3 Loop design (Agent.runAgent
)
The core design choice here is to separate internal model messages from UI-facing chat messages:
- Internal model transcript (
messages
): system/user/tool/assistant turns used for messages ingenerator(...)
. - UI transcript (
chatMessages
): what the user sees, including streamed assistant text plus tool execution metadata (tools
) and performance metrics.
Execution flow:
- Add user input to
chatMessages
, create a placeholder assistant message, and stream tokens. - Parse streamed/final model output with
extractToolCalls.ts
into{ message, toolCalls }
. - Keep the user-visible assistant message as plain text, while tool calls execute in background.
- Append tool results to the assistant tool metadata and feed results back as the next prompt turn.
- Repeat until no tool calls remain, then finalize assistant content + metrics.
This keeps user communication clean while preserving a deterministic tool loop in the background.
4) Data boundaries and persistence
State placement is another architectural decision that matters a lot in MV3. In this implementation, state is split by lifecycle and access pattern:
- Conversation state: background memory (
Agent.chatMessages
) for fast turn-by-turn orchestration. - Tool preferences:
chrome.storage.local
so settings persist across sessions. - Semantic history vectors: IndexedDB (
VectorHistoryDB
) for larger local retrieval data. - Extracted page content: background cache (
WebsiteContentManager
) keyed by active URL.
As described in section 1.2, keeping conversation history in background gives one canonical state across UI updates. This keeps short-lived state in memory, durable settings in extension storage, and heavy retrieval data in a local database.
5) Build and packaging notes
You do not need a complex build setup, but MV3 does require predictable outputs for each runtime.
- Multi-entry build in
vite.config.ts
: - Ensure manifest-aligned output names/paths (
sidebar.html
,background.js
,content.js
). - Keep the content script as a self-contained output to avoid runtime chunk-loading issues.
The goal is simple: one artifact per Chrome entry point, in the exact place public/manifest.json
expects.
Final takeaway
The architecture choice that unlocks this whole project is clear separation of concerns: background owns orchestration and model execution, UI surfaces stay thin, and content scripts handle page access.
This project uses a side panel, but the same approach works for other setups:
- Popup-first assistant: use
action.default_popup
for quick interactions, with background owning conversation state and model execution. - Side-panel copilot: keep long-running conversations in a persistent panel while background handles tool loops and caching.
- Per-tab agents: keep one agent state per
tabId
in background when each tab should have its own context. - Hybrid UI (popup + side panel + options page): all UI entry points talk to the same background coordinator and reuse the same message contracts.
The practical rule is simple: decide where state lives (global
, tabId
, or site-scoped), keep that state and the model inference in background (basically as background services), and let UI/content runtimes act as focused clients.
```

---

## 11. QIMMA قِمّة ⛰: A Quality-First Arabic LLM Leaderboard

- 日期: 2026-04-21 10:09
- 链接: https://huggingface.co/blog/tiiuae/qimma-arabic-leaderboard

```
QIMMA قِمّة ⛰: A Quality-First Arabic LLM Leaderboard
QIMMA validates benchmarks before evaluating models, ensuring reported scores reflect genuine Arabic language capability in LLMs.
🏆 Leaderboard · 🔧 GitHub · 📄 Paper
If you've been tracking Arabic LLM evaluation, you've probably noticed a growing tension: the number of benchmarks and leaderboards is expanding rapidly, but are we actually measuring what we think we're measuring?
We built QIMMA قمّة (Arabic for "summit"), to answer that question systematically. Instead of aggregating existing Arabic benchmarks as-is and running models on them, we applied a rigorous quality validation pipeline before any evaluation took place. What we found was sobering: even widely-used, well-regarded Arabic benchmarks contain systematic quality issues that can quietly corrupt evaluation results.
This post walks through what QIMMA is, how we built it, what problems we found, and what the model rankings look like once you clean things up.
🔍 The Problem: Arabic NLP Evaluation Is Fragmented and Unvalidated
Arabic is spoken by over 400 million people across diverse dialects and cultural contexts, yet the Arabic NLP evaluation landscape remains fragmented. A few key pain points have motivated this work:
Translation issues. Many Arabic benchmarks are translations from English. This introduces distributional shifts. Questions that feel natural in English become awkward or culturally misaligned in Arabic, making benchmark data less representative of how Arabic is naturally used.
Absent quality validation. Even native Arabic benchmarks are often released without rigorous quality checks. Annotation inconsistencies, incorrect gold answers, encoding errors, and cultural bias in ground-truth labels have all been documented in established resources.
Reproducibility gaps. Evaluation scripts and per-sample outputs are rarely released publicly, making it hard to audit results or build on prior work.
Coverage fragmentation. Existing leaderboards cover isolated tasks and narrow domains, making holistic model assessment difficult.
To illustrate where QIMMA sits relative to existing platforms:
QIMMA is the only platform combining all five properties: open source, predominantly native Arabic content, systematic quality validation, code evaluation, and public per-sample inference outputs.
⛰ What's in QIMMA?
QIMMA consolidates 109 subsets from 14 source benchmarks into a unified evaluation suite of over 52,000 samples, spanning 7 domains:
A few things stand out about this design:
- 99% native Arabic content. The only exception is code evaluation, which is inherently language-agnostic.
- First Arabic leaderboard with code evaluation. QIMMA integrates Arabic-adapted versions of HumanEval+ and MBPP+, making it possible to assess coding capability with Arabic-language problem statements.
- Diversity in Domains and Tasks. QIMMA evaluates real-world competency areas including education, governance, healthcare, creative expression, and software development.
🔬 The Quality Validation Pipeline
This is the methodological heart of QIMMA. Before running a single model, we applied a multi-stage validation pipeline to every sample in every benchmark.
Stage 1: Multi-Model Automated Assessment
Each sample was independently evaluated by two state-of-the-art LLMs:
- Qwen3-235B-A22B-Instruct
- DeepSeek-V3-671B
We chose two models with strong Arabic capability but different training data compositions, so that their combined judgment is more robust than either alone.
Each model scores a sample against a 10-point rubric, with binary scores (0 or 1) per criterion:
A sample is eliminated if either model scores it below 7/10. Samples where both models agree on elimination are dropped immediately. However, where only one model flags a sample, it proceeds to human review in Stage 2.
Stage 2: Human Annotation and Review
Flagged samples are reviewed by native Arabic speakers with cultural and dialectal familiarity. Human annotators make final calls on:
- Cultural context and regional variation
- Dialectal nuance
- Subjective interpretation
- Subtle quality issues automated assessment may miss
For culturally sensitive content, multiple perspectives are considered, since "correctness" can genuinely vary across Arab regions.
⚠️ What We Found: Systematic Quality Problems
The pipeline revealed recurring quality issues across benchmarks; not isolated errors, but systematic patterns reflecting gaps in how benchmarks were originally constructed.
By the Numbers
Taxonomy of Issues Found
⚖️ Answer Quality
False or mismatched gold indices, factually wrong answers, missing or raw text answers.
📄 Text & Formatting Quality
Corrupt or illegible text, spelling and grammar errors, and duplicate samples.
💬 Cultural Sensitivity
Stereotype reinforcement and monolithic generalizations about diverse communities.
🤝 Gold Answer Compliance
Misalignment of gold answers with evaluation protocols.
💻 Code Benchmark: A Different Kind of Quality Work
Code benchmarks required a different intervention. Rather than discarding samples, we refined the Arabic problem statements in 3LM's Arabic adaptations of HumanEval+ and MBPP+, leaving task identifiers, reference solutions, and test suites completely unchanged.
The modification rates were striking:
Modifications fell into five categories:
- Linguistic refinement : normalizing toward natural Modern Standard Arabic and consistent imperative style
- Clarity improvements : fixing ambiguous instructions and unclear constraints
- Consistency normalization : standardizing mathematical terminology, punctuation, and example formatting
- Structural corrections : fixing broken triple-quoted strings, indentation errors, corrupted text fragments
- Semantic refinements : clarifying whether ranges are inclusive/exclusive, preserving task intent
⚙️ Evaluation Setup
Evaluation Framework
QIMMA uses LightEval, EvalPlus and FannOrFlop as its evaluation framework, chosen for consistency, multilingual community adoption, and reproducibility.
Metrics by Task Type
Prompt Templates
QIMMA standardizes prompting by question format, with six template types:
All prompts are in Arabic. For MizanQA and ArabCulture, benchmark-specific system prompts from the original papers are preserved.
🏆 Leaderboard Results
Results as of April 2026; covering top 10 evaluated models. Visit the live leaderboard for current rankings.
- Scale does not guarantee best performance. The top 10 spans models from 32B to 397B parameters, with several mid-size models outperforming larger ones on specific domains.
- Arabic-specialized models lead on cultural and linguistic tasks. Jais-2-70B-Chat ranks highest on ArabicMMLU and ArabCulture, while Karnak leads on 3LM STEM and ArabLegalQA.
- Coding remains the hardest domain for Arabic-specialized models. The top HumanEval+ and MBPP+ scores belong to multilingual models, with Qwen3.5-397B leading both.
The Size-Performance Relationship
Across the full leaderboard (46 models), a clear but imperfect size-performance correlation emerges. However, there are interesting exceptions:
- Arabic-specialized models often outperform size-matched multilingual models
- Instruction-tuned models consistently outperform their base counterparts except for Qwen3
- Some smaller Arabic-specialized models (Fanar-1-9B, ALLaM-7B) outperform much larger multilingual models on specific domains
🌟 What Makes QIMMA Different
To summarize the distinctive properties of QIMMA:
🔗 Resources
- 🏆 Leaderboard: QIMMA Leaderboard
- 💻 Code: GitHub
- 📄 Paper: Are Arabic Benchmarks Reliable? QIMMA's Quality-First Approach to LLM Evaluation
🔖 Citation
@misc{alqadi2026arabicbenchmarksreliableqimmas,
title={Are Arabic Benchmarks Reliable? QIMMA's Quality-First Approach to LLM Evaluation},
author={Leen AlQadi and Ahmed Alzubaidi and Mohammed Alyafeai and Hamza Alobeidli and Maitha Alhammadi and Shaikha Alsuwaidi and Omar Alkaabi and Basma El Amel Boussaha and Hakim Hacid},
year={2026},
eprint={2604.03395},
archivePrefix={arXiv},
primaryClass={cs.CL},
url={https://arxiv.org/abs/2604.03395},
}
```

---

## 12. AI and the Future of Cybersecurity: Why Openness Matters

- 日期: 2026-04-21 00:00
- 链接: https://huggingface.co/blog/cybersecurity-openness

```
AI and the Future of Cybersecurity: Why Openness Matters
What is Mythos?
Mythos is a “frontier AI model”, a large language model (LLM) that can be used to process software code (among many other things). This follows a general trend in LLM development, where LLM performance on code-related tasks has recently skyrocketed. What’s particularly significant about Mythos is the system it’s embedded within: It's the system, not the model alone, that has enabled Mythos to rapidly find and patch software vulnerabilities. Understanding this distinction is key to understanding the current landscape of AI cybersecurity.
What Mythos demonstrates is that the following system recipe is powerful:
- substantial compute power
- models trained on troves of software-relevant data
- scaffolding built to handle software vulnerability probing and patching
- speed (enabled by compute power and the capital behind it)
- some degree of system autonomy
Together, these ingredients can uncover software vulnerabilities, find exploits, and build patches. It’s in this recipe — not in any one model — that both the benefits and the risks come in.
This matters because others can build comparable systems. Smaller models embedded in systems built with deep security expertise could potentially produce similar outcomes more cheaply, which is particularly promising for defense. AI cybersecurity capability is jagged: It doesn’t scale smoothly with model size or general benchmark performance. The system the model is embedded within matters a lot.
So what Mythos has demonstrated is that it’s possible to build an AI system that finds and addresses software vulnerabilities. We already knew this was possible and there has been increasing work on this, but we’re just beginning to explore what it means in the context of agentic AI: Systems that can rapidly and autonomously take action.
How Openness Can Be a Structural Advantage
As autonomous systems that identify software vulnerabilities proliferate (and they will), open code and tooling can help level the playing field. Software security has become a speed race across four stages: detection, verification, coordination, and patch propagation. Open ecosystems distribute these across a community, where more closed-source projects centralize knowledge and action across all four stages inside a single vendor, representing a single point of failure where only one organization can see and fix the code. The distributed nature of open development is robust to such constraints, and can be especially powerful in communities with dedicated security professionals, like the Linux kernel security team, the Open Source Security Foundation, and the team at Hugging Face working on model and supply-chain security.
A common argument for more closed systems is proprietary obscurity, where the code underlying a system is inaccessible. Unfortunately, this provides less protection than it used to. AI systems are increasingly able to assist with reverse engineering of stripped binaries, which matters because most legacy firmware and embedded code is closed, binary-only, and no longer maintained. That code represents a huge attack surface, and it’s becoming more legible and accessible as AI tools improve.
There’s also a risk created by how AI is being used inside closed codebases. When companies adopt AI coding tools under the wrong incentives (for instance, evaluating engineers by the volume of features shipped rather than code quality) AI-accelerated development can introduce more vulnerabilities into proprietary code than traditional development would. Those vulnerabilities then sit inside a closed codebase where only one organization can find and fix them, while AI-enabled attackers are increasingly capable of discovering them from the outside. The combination of more vulnerabilities produced more quickly, behind a single-organization firewall, is exactly the kind of imbalance that open ecosystems are positioned to avoid.
Underlying all of this is capability asymmetry between attackers and defenders. Open models and open tooling narrow that gap by giving defenders access to the same class of capabilities attackers can reach for — capabilities that would otherwise be concentrated within a small number of well-resourced entities.
Building Defenses with Open Tools and Semi-Autonomous Agents
Cybersecurity defense is where open source and AI agents can play a key role together. Based on the System Card, it appears that Mythos is capable of operating with close to full autonomy, something we’ve advised against due to the potential loss of control. AI agents that are instead semi-autonomous, where the types of actions they can take are prespecified and certain steps require human approval, hit a sweet spot of benefit and risk. In semi-autonomous systems, people remain in control, and the AI agent is responsible for specific subtasks. This is possible to do with open code that organizations can run privately within their own institutions, specifying allowable tools, skills, and system access privileges. With this setup, AI agents can be deployed defensively, finding vulnerabilities and assisting with patching under an organization’s own controls.
The semi-autonomous approach depends on humans being able to actually understand what an AI agent did and why. That’s much more possible when the system is built on open components, such as open agent scaffolding, open rule engines, and auditable decision logs and traces, than when it’s a black box. The “human in the loop” is only meaningful if the human can see into the loop.
Companies don’t have to build these capabilities entirely from scratch. There’s a rich open-source ecosystem of security tooling, including vulnerability scanners, intrusion detection systems, log analyzers, and fuzzing frameworks, that AI agents can be integrated with.
Why This Matters Especially for High-Stakes Organizations
For high-stakes organizations, starting from open, auditable foundations means security teams can actually inspect how their monitoring works, rather than trusting a single vendor’s claims. This is particularly important where sensitive data and processes are involved, and where sensitive material should generally not be flowing through external AI providers. Open systems can be rigorously analyzed by in-house security professionals, fine-tuned on an organizations’s own secure data, modified to produce organization-specific oversight mechanisms, and run entirely within an organization’s own infrastructure, keeping everything behind appropriate firewalls.
The Path Forward
Attackers will develop models that take advantage of vulnerabilities. A significant part of the answer is leaning into transparent practices: open security reviews, published threat models, shared vulnerability databases, and open tooling that any team can adopt. The alternative of each organization trying to secure itself in isolation with proprietary tools doesn’t scale against attackers who are coordinating and sharing techniques in their own communities.
The future of AI cybersecurity will be shaped less by any single model and more by the ecosystems that surround them. Openness provides defenders with the visibility, the control, the community, and the shared infrastructure to stay ahead.
```

---

## 13. Ecom-RLVE: Adaptive Verifiable Environments for E-Commerce Conversational Agents

- 日期: 2026-04-16 00:00
- 链接: https://huggingface.co/blog/ecom-rlve

```
Ecom-RLVE: Adaptive Verifiable Environments for E-Commerce Conversational Agents
TL;DR — We extend the RLVE framework from single-turn reasoning puzzles to multi-turn, tool-augmented e-commerce conversations. EcomRLVE-GYM provides 8 verifiable environments — product discovery, substitution, cart building, returns, order tracking, policy QA, bundle planning, and multi-intent journeys — each with procedural problem generation, a 12-axis difficulty curriculum, and algorithmically verifiable rewards. We train a Qwen 3 8B model with DAPO over 300 steps and present early results demonstrating that environment scaling and adaptive difficulty transfer to agentic, real-world task completion.
This project originated in the Pytorch OpenEnv Hackathon and is still evolving, follow us for updates 🔥
Why RL for shopping agents?
Large language models can hold fluent conversations, yet deploying them as shopping assistants reveals a persistent gap: fluency ≠ task completion. A customer who asks "find me a USB-C charger under $25 that ships in two days" needs an agent that invokes the right catalog search, filters on three hard constraints, avoids hallucinating product IDs it never retrieved, and handles follow-ups when the top result goes out of stock.
Supervised fine-tuning can teach surface-level tool use from demonstrations, but it cannot scale to the combinatorial space of constraint configurations, partial-information dialogues, and multi-step transactional workflows that real e-commerce demands.
Reinforcement learning with verifiable rewards (RLVR) offers an alternative: the agent optimises for outcomes — did the products satisfy the constraints? Was the cart correct? Was the return initiated for the right order line? The challenge is constructing reward functions that are both verifiable (no LLM-as-a-judge subjectivity) and adaptive (difficulty that grows with the policy's capability).
From RLVE-Gym to EcomRLVE-GYM
RLVE-Gym provides 400 environments for sorting, multiplication, Sudoku, and other algorithmic-reasoning tasks; however, those are all single-turn, text-in / text-out puzzles — extending to agentic domains was left as future work.
EcomRLVE-GYM fills that gap: we stay in the verifiable regime (e-commerce outcomes can be checked algorithmically) while extending to multi-turn, tool-augmented, agentic conversations — environments where the agent must act (call tools, modify world state) rather than merely reason (produce a text answer) and compensates for the deficiency of the search system.
EcomRLVE-GYM transforms customer-service outcomes structurally verifiable:
Every signal above can be evaluated by a program with access to the hidden ground-truth goal. No human annotation or LLM-as-a-judge is needed.
What a training episode looks like
Before we explain the framework, here is what a single EcomRLVE episode looks like at difficulty d = 4
. The environment generates a hidden goal, a simulated user opens the chat, and the agent must use tools to satisfy the request. Every action is verified algorithmically — no LLM judge required.
The reward is fully computed by code: F1 over (product, variant, qty)
tuples, an efficiency bonus for finishing in fewer turns, and a hallucination check that every recommended product ID was actually retrieved. If the agent had picked the Lightning variant instead of USB-C, the simulated user would have corrected it mid-dialogue — and the F1 would have dropped.
The eight environments
Each environment covers a distinct real-world shopping scenario. The agent must complete the task using tools (catalog search, cart operations, order lookups, policy queries) and is scored by a program — not a human or another LLM.
Every environment uses the same three-part reward signal:
- Task reward — did the agent actually complete the goal? (e.g., were the right products recommended, was the cart correct, was the right order tracked?)
- Efficiency reward — did the agent complete it without wasting turns? Turns the user caused (asking a follow-up, confirming an action) don't count against the agent — only turns caused by agent mistakes do.
- Hallucination penalty — did the agent only recommend products it actually retrieved during the session? Recommending product IDs that were never looked up is penalised, so the agent cannot invent results from memory.
Invalid outputs (malformed JSON, illegal tool calls) trigger an immediate failure score, creating a strong incentive for well-formed responses from step one.
Adaptive difficulty curriculum
A single difficulty number d
controls 12 independent aspects of a task simultaneously. This is important because e-commerce conversations are hard in many different ways at once — not just along one dimension.
Here are four representative difficulty axes:
The other eight axes cover turn budget, input noise (typos, slang), context switches, retrieval depth, order-history size, policy complexity, and tool budget. The full breakdown is in the technical report.
Adaptive scheduling. Each environment tracks the agent's success rate independently and only advances to harder problems once the agent is passing the current level reliably. This keeps every environment training at the agent's capability frontier — avoiding both "too easy to learn from" and "too hard to make progress on".
Deep dive: Cart Building (E_CART)
Cart building is a good showcase because it requires the full search → inspect → clarify → act loop, has a binary ground truth, and introduces a challenge absent from most recommendation benchmarks: variant selection.
To succeed, the agent must develop five distinct skills:
The agent uses six tools to accomplish this:
The problem
The generator samples 1–5 target products (scaling in difficulty with d
), each potentially requiring a specific variant (USB-C vs Lightning, Matte vs Glossy) and a quantity > 1. The agent must:
- Search the catalog to find each product
- Call
catalog.get_variants
to see available options - Add the correct
(product_id, variant_id, qty)
tuples to the cart
Why variants matter
Real product catalogs have sparse variant data — many products have none, and those that do typically vary only by colour or size. To create a richer discrimination task, we synthesize variants at episode initialization:
- A per-category priority list picks the most natural attribute to vary (electronics →
connector_type
; clothing →size
; kitchen →material
). - For each target product, we generate 3 variants: 1 target + 2 plausible distractors. An "Anker 65W USB-C Charger" produces
{USB-C, Lightning, HDMI}
. - The verifier checks composite keys
(product_id, variant_id)
— correct product but wrong variant means the unit is unmatched.
Difficulty scaling
At d = 0
the agent adds a single product with no variant complexity — learning the basic catalog.search → cart.add
workflow. At d = 6
it juggles 3 items, nearly all requiring a specific variant, with half needing qty > 1.
Scoring
The cart must be exactly right — correct product, correct variant, correct quantity. Partial credit is given for partially correct carts, but a perfect score requires every item to match. If the agent adds the wrong variant, the simulated user corrects it mid-dialogue ("that's the Lightning version, but I need USB-C"), giving the agent a chance to self-correct before the episode ends.
Trajectories: easy vs. hard
Two real E_CART episodes from a Qwen 3 8B agent. Same environment, same agent — difficulty alone changes the game.
At d=1 the agent solves the task in 3 clean turns. At d=8 it spirals — picking Bamboo instead of Charcoal, XL instead of XS, never fixing the air fryer despite two user corrections, then hallucinating that the variant doesn't exist. This is exactly the kind of multi-step error cascade that the difficulty curriculum surfaces, and that adaptive training should teach the agent to recover from.
User simulation
A verifiable environment needs a user simulator that behaves realistically. We use Qwen3.5 (9.7B) to generate natural, varied user messages rather than canned templates — covering everything from typo-filled requests to mid-conversation topic switches.
Two design choices matter for training quality:
Preferences match stated constraints. Each simulated user has a hidden set of preferences (price sensitivity, brand loyalty, shipping speed, etc.). These are deliberately biased toward whatever constraints the user communicated — so if the user said "under $25", the reward function actually cares about price. Without this, an agent could be penalised for correctly following the user's instructions.
Strategic omission. The LLM deliberately withholds some constraints from the opening message to force the agent to ask clarifying questions. The system tracks exactly what was and wasn't mentioned, so the agent is never penalised for information it was never given.
Environment scaling
Following RLVE's methodology, we define nested environment collections:
C1 ⊂ C2 ⊂ C4 ⊂ C8
We hypothesise — consistent with RLVE's findings — that C8 agents outperform single-environment specialists, even on the specialist's own task.
Early results
We trained Qwen 3 8B with DAPO on C1 (Cart Building) for 300 steps as an initial viability study.
We saw progressive growth in difficulty reached, confirming that adaptive scheduling produces a steady learning signal rather than the saturation (static-low) or starvation (static-high) patterns predicted by the RLVE paper.
Try it yourself
Run a live episode directly in your browser using the embedded demo below. Here is how to get started:
- Pick an environment from the dropdown (e.g.,
E_CART
for cart building orE_PD
for product discovery). - Set a difficulty —
0
is a simple single-constraint task;6+
introduces missing information, noisy retrieval, and variant selection. - Click "Reset Episode" — the simulated user will open with a shopping request.
- You are the agentnow: Make tool calls, analyse outputs and submit the final list of product ids.
- Click "Reset Episode" between runs to start a fresh scenario.
Resources
The environments, verifiers, and training configs are all open-source:
git clone https://github.com/owlgebra-ai/EcomRLVE-Gym
cd EcomRLVE-Gym
pip install -e .
The 2M-product catalog is on the Hub:
from datasets import load_dataset
catalog = load_dataset("owlgebra-ai/Amazebay-catalog-2M", split="train")
print(f"{len(catalog)} products loaded")
References
Zeng, Z., Ivison, H., Wang, Y., et al. (2025). RLVE: Scaling Up Reinforcement Learning for Language Models with Adaptive Verifiable Environments. ICML 2025. arXiv:2511.07317
Yu, Q., Zhang, Z., Zhu, R., et al. (2025). DAPO: An Open-Source LLM Reinforcement Learning System at Scale. arXiv:2503.14476
Shao, Z., Wang, P., Zhu, Q., et al. (2024). DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. arXiv:2402.03300
DeepSeek-AI. (2025). DeepSeek-R1: Incentivizing Reasoning in LLMs through Reinforcement Learning. Nature.
Meta AI. (2024). Llama 3.1: A Foundation Model for General Intelligence. llama.meta.com
Qwen Team. (2025). Qwen3 Technical Report. arXiv:2505.09388
```

---

## 14. The PR you would have opened yourself

- 日期: 2026-04-16 00:00
- 链接: https://huggingface.co/blog/transformers-to-mlx

```
The PR you would have opened yourself
TL;DR
We provide a Skill and a test harness to help port language models from transformers to mlx-lm, so they become (almost) instantly available the moment they are added to transformers. The Skill is designed to support contributors and reviewers as an aide, not an automation. We explain why we did it, how, and comment about how to meaningfully contribute to open source in the age of agents.
The advent of code agents
In 2026, code agents started to actually work. What used to be auto-completion at the side of your editor turned into a system that one-shots reasonable solutions from brief specifications. The generated code usually works out of the box, covers what you asked for, and makes reasonable assumptions about details you didn't specify. This is great. As Jensen Huang puts it, we've instantly gone from 30 million to one billion coders in the world. Creative minds are unleashed.
But it forces us to rethink open source.
Take the transformers library as an example. It has hundreds of contributors, is used in thousands of projects, has been downloaded over a billion times. Suddenly, anyone with an agent can instruct it to find some open issue, fix it, and submit a PR. And that's exactly what's happening. Those people feel happy because they are contributing to a great library, but the sad reality is that, most of the time, they don't realize they are not.
Why not? There are two assumptions that agent-generated PRs usually miss.
Codebases like transformers care deeply about the code. It's cool to build projects where it doesn't matter what the code looks like, but transformers is not one of them. Being used by thousands of people, transformers is primarily built as a human-to-human communication method, through code. Model files read top to bottom, because we want practitioners to understand them without jumping through complex abstractions. This permeates throughout the library design and is the reason why, for example, we favor flat hierarchies.
Agents don't have that context. Because design decisions are not explicit, agents suggest refactors to "improve" the codebase by following "best practices", without realizing they are breaking implicit contracts between the library and its users. They are verbose, generalize too early, don't notice when a change affects other areas, introduce subtle bugs, break performance. They are also sycophantic, and accept any idea as good and follow it through diligently, including ones a maintainer would have pushed back early on with a terse comment.
A small number of maintainers still has to read every PR, understand it, decide if the design direction is right, identify side effects, and write feedback. PR volume has gone up tenfold, but the amount of maintainers has not (and cannot, because team coordination does not scale).
What does this have to do with MLX?
Transformers is one of the first projects to feel this pressure because of sheer volume, but the same dynamic is happening everywhere. As an example from a different domain, App Store reviewers are swamped because anyone can now build and submit an app, so many do.
The same logic applies to MLX: their maintainers care deeply about the code and read every PR carefully. We wanted to see whether agents could help contributors land high-quality model ports fast, and at the same time support reviewers in their work. Not only do we aspire to produce PRs that could have come from a careful human submission, but we also provide additional artifacts to increase the signal: generation examples, numerical comparisons, and a separate non-agentic test harness for reproducibility.
Another connection between transformers and MLX is that, most times, mlx-lm models are ported from transformers implementations. Because transformers focuses on clarity and readability, it has become the source of truth for model definitions. Downstream contributors wait until the transformers implementations are ready before they port to other frameworks. As a side effect, this is an excellent environment for an agent because it naturally limits the scope: rather than creating an implementation from scratch, the agent relies on transformers code as the source of truth.
This approach supports our goal: when a model lands in transformers, it should be available on MLX shortly after.
What we did
We built a Skill that mlx-lm contributors can use to port a model from transformers to MLX. Given a prompt like "convert the olmo_hybrid architecture to MLX", the Skill sets up a virtual environment to work on, discovers and downloads the relevant models from the Hub, reads the transformers modeling code, writes the MLX implementation, and runs a battery of tests. If results don't look right, it debugs and iterates, and does not declare success until it's satisfied.
We designed it to be useful to reviewers as much as contributors.
For the contributor, the Skill of course handles all the scaffolding: finding model variants on the Hub, diffing their configs to spot parameters that vary across model variants, downloading checkpoints, setting up editable installs of both mlx-lm and transformers. But it also handles the more difficult modeling tasks. It pays attention to salient architecture details and verifies sensitive areas, like RoPE configurations, that may result in hard-to-find bugs. It detects when the config doesn't declare a dtype and infers it from the safetensors metadata header. It runs per-layer comparisons between transformers and MLX to pinpoint exactly where divergence occurs. These are the kinds of checks that only someone with porting experience would think to run.
For the reviewer, the Skill produces a PR that is upfront about being agent-assisted, but does look like a careful human submission. Reviewers will see that the code follows mlx-lm conventions: idiomatic solutions, no unnecessary comments, no speculative abstractions, no modifications to shared utilities without explicit approval. Given that the code is agent-assisted, we try to include more data than the median PR, to provide as much signal as possible. The PR body includes a report with a summary of the variants and their architectural differences, generation examples, numerical comparisons, dtype verification, per-layer comparisons against the transformers baseline. The PR always discloses that it was agent-assisted, and the Skill will not open it until the contributor has accepted the results.
For verification, the Skill generates a test manifest for a separate, non-agentic test harness that is, by design, easily reproducible and not subject to LLM hallucinations or complacency (more on this below).
How we did it
Skills are recipes for agents: simple text files with guidelines that steer the model through a complex task. They are not magic; you can achieve the same results via prompting and iteration. But they provide consistency (every run follows the same process, whereas different people would prompt differently), minimize ambiguity and serve as documentation: anyone can read the Skill to understand what it does, identify missing cases and suggest improvements.
We bootstrapped the Skill by porting a model ourselves, in conversation with Claude. I asked it to port GLM 4.7 from transformers to mlx-lm, giving instructions as I would during a normal session. One trick: I pointed Claude at a checkout of mlx-lm from which I had deleted the already-existing implementation, so I could compare the output against the ground truth. After a few iterations I had a working implementation, a conversation that revealed how Claude approached the problem, and the first draft of the Skill, which Claude created as a summary of the process. I edited it heavily, and incorporated the learnings from @gabegoodhart, who kindly shared their own porting conversation for a different model 🙌.
We repeated this loop several times and the Skill grew. On the technical side, we covered stuff such as RoPE bugs that may produce plausible output that degrades with long sequences, float32 precision contamination that silently kills inference speed (you'd be surprised how frequently these things happen!), config fields that vary across model variants in ways the implementation must handle, distributed inference for super large models that don't fit on a single machine. We taught it how to invoke the hf
CLI to discover and download models. Most importantly, we instructed it to run the tests that experienced porters would, and to not declare success until they pass.
Source: @Prince_Canuma
On the cultural side, we covered softer characteristics and explained the conventions that make a PR easy to review: don't use comments to explain code (the reviewer has to parse the comment and the code 🤦♂️), never propose refactors, don't touch shared utilities without asking. These rules cost the agent nothing but save the reviewer lots of time.
The end result: the contributor types a prompt, and the Skill produces a PR like this one, plus a test manifest for the external test harness.
Test harness
The Skill shares a comprehensive results report as part of the PR. All these come from tests the agent runs during conversion, but we didn't want the reviewer to take a leap of faith to accept them. To go a step forward, we created a separate, non-agentic test harness that runs systematic tests on the converted code. This brings a couple of benefits:
- Removes uncertainty about the LLM hallucinating results, or being too complacent about them.
- Guarantees reproducibility: anyone can download the test harness repo and run the tests.
- Documentation and transparency. All results are saved at various levels: summary reports, per-model details, raw inputs/outputs saved as JSON files. The tests are also copied to results folders so we know what we ran even if we make changes to the harness in the future.
The test harness is not a CI gate. Some checks are straightforward (is the output dtype correct?), but most are qualitative. Is it normal that a pre-trained model repeats itself in long sequences? Is a 4% relative logits difference against the transformers baseline acceptable? These are judgement calls based on experience with similar architectures. The harness provides useful signal, but it's the reviewer and contributor who still have to make the call.
How to use the Skill
The Skill is designed for the people who are already opening mlx-lm model PRs, or who would do it manually on their own. It's not meant for mass consumption, because PRs to mlx-lm are rarely accepted on sight. The typical cycle is: contributor opens a PR, reviewers point out improvements, both sides iterate until the quality bar is met. If this is true for expert submissions, it will remain true for agent-assisted ones.
If you're not prepared to engage in that cycle, you probably shouldn't be opening a PR. The reviewers will make an effort to understand your code (even knowing it was agent-assisted), so you should do the same. Own the code, and be ready to incorporate their feedback. In particular, don't hand reviewer comments back to an agent and post whatever it produces. LLMs double down on their decisions, go on tangents, and don't push back effectively. Once you engage with the reviewer, this becomes a person-to-person conversation, so it's your turn to discuss and be respectful of the time they put in.
You can also use the Skill to learn; you don't need to submit anything until your confidence and experience build. Read the Skill to identify problem areas you weren't aware of: it contains nearly 15 thousand words among the skill file, reference docs and utility scripts. Point it to your own fork of mlx-lm, try a conversion, and compare your output against the accepted implementation once it lands in the official repo. If you do this a few times, you'll learn a lot about transformers, MLX, and language model architectures.
If you're ready:
uv run https://raw.githubusercontent.com/huggingface/transformers-to-mlx/main/install_skill.py
uvx hf skills add --claude
We developed and tested the Skill using Claude Code. The same approach would work with Codex or other coding agents, but we haven't tested them. If you try the Skill in a different environment, please let us know how it goes!
Next steps and known shortcomings
The Skill works well for LLMs in mlx-lm, but there's plenty of room to grow.
What's next
- mlx-vlm. Vision-language models live in a separate repo with different conventions. Beyond the modeling code, mlx-vlm requires processors to handle image pre-processing before the LLM sees the input. We're looking forward to collaborating with Prince Canuma to help him do what he does.
- llama.cpp. Some of the same challenges apply. Processors require image processing algorithms to be replicated in C++, and numerical differences are unavoidable. This is an area where a tightly scoped agent might help.
- The test harness. We want to expand the test battery and potentially explore safe automation to run tests automatically on our infra.
What doesn't work yet
- Shared utilities in mlx-lm. mlx-lm is less strict than transformers about extracting common patterns into shared functions. The Skill is purposefully biased towards self-contained model files (same as transformers), but reviewers regularly ask for refactors to move repeated code into shared modules.
- VLMs and other architectures, as noted above.
- Quantized model uploads. The Skill tests quantization but doesn't upload quantized models to the Hub. We think it doesn't make sense to upload while the PR is being reviewed, but we could create a flow to do it later.
- Thinking tests. No thinking-specific tests have been designed yet. The Skill will convert and verify generations from these models, but won't validate the thinking structure.
Conclusion
The bottleneck in open source is not typing speed: it's understaning the codebase to change it without breaking the implicit and explicit contracts with users. Agents can help in this process, if we teach them what matters. We explored what this looks like in the context of mlx-lm, and hope it's useful for contributors and reviewers to land high-quality model conversions faster!
Resources
Contributions:
The libraries:
Background:
- Claude Code Skills docs
- Transformers design philosophy
- The Transformers Library: standardizing model definitions
Thank you!
Thanks a lot to Ben, Shaun, Aritra for reading previous versions of this post and making it so much better 🙌
We are incredibly indebted to Apple for making MLX an open-source project, and to the community for instantly recognizing its value and contributing enthusiastically 🙏
```

---

## 15. Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers

- 日期: 2026-04-16 00:00
- 链接: https://huggingface.co/blog/train-multimodal-sentence-transformers

```
Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers
As a practical example, I'll walk through finetuning Qwen/Qwen3-VL-Embedding-2B
for Visual Document Retrieval (VDR), the task of retrieving relevant document pages (as images, with charts, tables, and layout intact) for a given text query. The resulting tomaarsen/Qwen3-VL-Embedding-2B-vdr
demonstrates how much performance you can gain by finetuning on your own domain. On my evaluation data, the finetuned model achieves an NDCG@10 of 0.947 compared to the base model's 0.888, and outperforms all existing VDR models I tested against, including models up to 4x its size.
If you're new to multimodal models in Sentence Transformers, I recommend reading Multimodal Embedding & Reranker Models with Sentence Transformers first. For training text-only embedding, reranker, or sparse embedding models, see the Prior Blogposts section at the end.
Table of Contents
- Why Finetune?
- Training Components
- Model
- Dataset
- Loss Function
- Training Arguments
- Evaluator
- Trainer
- Results
- Training Multimodal Reranker Models
- Additional Resources
Why Finetune?
General-purpose multimodal embedding models like Qwen/Qwen3-VL-Embedding-2B
are trained on diverse data to perform well across a wide range of languages and tasks: image-text matching, visual question answering, document understanding, and more. But this generality means the model is rarely the best choice for any specific task.
Consider Visual Document Retrieval: given a text query like "What was the company's Q3 revenue?", the model must find the most relevant document screenshot from a corpus of thousands. This requires understanding document layouts, charts, tables, and text, which is a very different skill from e.g. matching pictures of shoes with product descriptions.
By finetuning on domain-specific data, the model can learn these specialized patterns. In my experiment, finetuning improved NDCG@10 from 0.888 to 0.947, ahead of every recent multimodal model I tested, including ones up to 4x larger.
Training Components
Training multimodal Sentence Transformer models involves the same components as training text-only models:
- Model: The multimodal model to train or finetune.
- Dataset: The data used for training and evaluation.
- Loss Function: A function that quantifies the model's performance and guides the optimization process.
- Training Arguments (optional): Parameters that influence training performance and tracking/debugging.
- Evaluator (optional): A tool for evaluating the model before, during, or after training.
- Trainer: Brings together the model, dataset, loss function, and other components for training.
The multimodal training pipeline uses the same SentenceTransformerTrainer
as text-only training. The key difference is that your datasets contain images (or other modalities) alongside text, and the model's processor handles the image preprocessing automatically.
Let's walk through each component, using Visual Document Retrieval (matching text queries to document screenshots) as a running example.
Model
The most common approach is to finetune an existing multimodal embedding model, or to start from a Vision-Language Model (VLM) checkpoint. The Transformer
module automatically detects supported modalities from the model's processor.
To finetune an existing multimodal embedding model (e.g. one that already has a modules.json
file), you can pass processor_kwargs
and model_kwargs
to control preprocessing and model loading respectively. processor_kwargs
are passed directly to AutoProcessor.from_pretrained(...)
(e.g., image resolution bounds: higher max_pixels
means higher quality but more memory), while model_kwargs
are passed to the appropriate AutoModel.from_pretrained(...)
call (e.g., precision, attention implementation):
from sentence_transformers import SentenceTransformer
model = SentenceTransformer(
"Qwen/Qwen3-VL-Embedding-2B",
model_kwargs={"attn_implementation": "flash_attention_2", "torch_dtype": "bfloat16"},
processor_kwargs={"min_pixels": 28 * 28, "max_pixels": 600 * 600},
)
You can also start from a fresh VLM checkpoint that hasn't been trained for embeddings yet. Sentence Transformers will attempt to recognize the architecture, infer the supported modalities from the processor, and set up the appropriate forward method and pooling. If the automatic detection doesn't work perfectly for a particular model, the configuration in the saved sentence_bert_config.json
can be edited to adjust modality settings, forward methods, and output handling:
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-VL-2B")
In both cases, the Transformer
module inspects the processor to determine which modalities are available, and Pooling
is added automatically if needed. You can verify the supported modalities:
print(model.modalities)
# ['text', 'image', 'video', 'message']
print(model.supports("image"))
# True
Alternative: Building multimodal models with Router
Instead of using a single VLM backbone, you can compose separate encoders for different modalities using the Router
module. This lets you combine any existing encoders and route inputs to the appropriate one based on detected modality:
from sentence_transformers import SentenceTransformer
from sentence_transformers.sentence_transformer.modules import Dense, Pooling, Router, Transformer
# Create separate encoders for different modalities
text_encoder = Transformer("sentence-transformers/all-MiniLM-L6-v2")
text_pooling = Pooling(text_encoder.get_embedding_dimension(), pooling_mode="mean")
text_projection = Dense(text_encoder.get_embedding_dimension(), 768)
# SigLIP outputs pooled embeddings directly, so no separate Pooling module is needed
image_encoder = Transformer("google/siglip2-base-patch16-224")
# Route inputs based on modality
router = Router(
sub_modules={
"text": [text_encoder, text_pooling, text_projection],
"image": [image_encoder],
},
)
model = SentenceTransformer(modules=[router])
Since Router-based multimodal models use separate encoders per modality, their embedding spaces are initially unaligned. Training is required to align the spaces for meaningful cross-modal similarity. The
Dense
projection layer shown above helps map embeddings from different encoders into a shared space.
This approach is useful when you want to use lightweight, specialized encoders rather than a large VLM. You can also combine Router-based multimodality with task-based routing (e.g. different encoders for queries vs. documents) using route_mappings
. See the Router
documentation for advanced routing scenarios.
Dataset
Visual Document Retrieval Dataset
For this example, I use the tomaarsen/llamaindex-vdr-en-train-preprocessed
dataset, a preprocessed English subset of llamaindex/vdr-multilingual-train
. The source dataset was released alongside the Visual Document Retrieval Goes Multilingual blogpost by LlamaIndex, and consists of ~500k multilingual query-image samples collected from public internet PDFs, with queries synthetically generated using VLMs (gemini-1.5-pro and Qwen2-VL-72B).
My preprocessed version filters to the 53,512 English samples and resolves 4 of the 16 ID-based hard negatives per sample into actual document screenshot images, so it can be used directly for training without further preprocessing:
from datasets import load_dataset
train_dataset = load_dataset("tomaarsen/llamaindex-vdr-en-train-preprocessed", "train", split="train")
train_dataset = train_dataset.select_columns(["query", "image", "negative_0"])
eval_dataset = load_dataset("tomaarsen/llamaindex-vdr-en-train-preprocessed", "eval", split="train")
The train
config contains the first 10,000 samples, and the eval
config contains the next 300 samples (a full
config with all 53,512 samples is also available). For training, I select query
, image
, and negative_0
to form (anchor, positive, hard negative) triplets. Including additional hard negatives would likely improve the training signal, but each extra negative also increases memory usage and training time, so I stick with one. For evaluation, I keep all four hard negatives per query to build a more challenging retrieval corpus (more on that in the Evaluator section).
Dataset Format
Just like text-only training, the dataset format must match your chosen loss function. The rules are the same:
- If your loss function requires a Label, your dataset must have a column named "label" or "score".
- All columns other than "label" or "score" are considered Inputs. The number of these columns must match the number of valid inputs for your chosen loss function. Beyond the label column, the column names don't matter, only the order does.
For multimodal datasets, the inputs can contain:
- Text: strings.
- Image: PIL images, file paths, URLs, or numpy/torch arrays.
- Audio: file paths, numpy/torch arrays, dicts with
"array"
and"sampling_rate"
keys, or (iftorchcodec
is installed)torchcodec.AudioDecoder
instances. - Video: file paths, numpy/torch arrays, dicts with
"array"
and"video_metadata"
keys, or (iftorchcodec
is installed)torchcodec.VideoDecoder
instances. - Multimodal dicts: a dict mapping modality names to values, e.g.
{"text": ..., "image": ...}
. The keys must be"text"
,"image"
,"audio"
, or"video"
.
The data collator automatically calls model.preprocess()
, which detects the modality of each input and applies the appropriate preprocessing. No manual tokenization or image processing is needed.
Many Hugging Face datasets that work out of the box with Sentence Transformers have been tagged with
sentence-transformers
, allowing you to easily find them at https://huggingface.co/datasets?other=sentence-transformers.
Loss Function
CachedMultipleNegativesRankingLoss
For this training, I use CachedMultipleNegativesRankingLoss
, a common choice for retrieval tasks. It accepts (query, positive) pairs with any number of additional hard negative columns, from 0 up to n, as long as each sample has the same number of negatives.
During training, the loss pushes each query's similarity to its positive up and its similarity to every negative down. The negatives come from two sources:
- Hard negatives: the negative column(s) explicitly supplied in the dataset (just
negative_0
in our triplet setup). - In-batch negatives: the positives and hard negatives from every other sample in the same batch, reused as additional negatives for this query at no extra cost.
More negatives per query means a stronger training signal, so a larger batch size directly improves training quality. Beyond that, the "cached" variant of the loss uses gradient caching to make large effective batch sizes feasible even when GPU memory is limited.
The mini_batch_size
parameter controls how many samples are processed at once during the cached forward passes. For large multimodal models, setting this to a small value (e.g., 1) is important to avoid out-of-memory errors without sacrificing the benefits of large effective batch sizes:
from sentence_transformers.sentence_transformer.losses import CachedMultipleNegativesRankingLoss
loss = CachedMultipleNegativesRankingLoss(model, mini_batch_size=1)
MatryoshkaLoss
To produce embeddings that work well at multiple dimensionalities, I wrap the base loss with MatryoshkaLoss
. This trains the model so that truncating the embedding to a smaller number of dimensions still yields good performance:
from sentence_transformers.sentence_transformer.losses import CachedMultipleNegativesRankingLoss, MatryoshkaLoss
loss = CachedMultipleNegativesRankingLoss(model, mini_batch_size=1)
loss = MatryoshkaLoss(model, loss, matryoshka_dims=[2048, 1536, 1024, 512, 256, 128, 64])
This is especially useful for multimodal models, where embeddings can be large (2048 dimensions for Qwen3-VL). With Matryoshka training, you can use truncated embeddings (e.g., 256 or 128 dimensions) at deployment time for faster search with minimal quality loss. As I'll show in the Results section, the finetuned model achieves near-peak performance even at 512 dimensions.
Training Arguments
The SentenceTransformerTrainingArguments
class lets you control training hyperparameters. Here's the configuration used for the VDR finetuning:
from sentence_transformers.sentence_transformer.training_args import SentenceTransformerTrainingArguments, BatchSamplers
run_name = "Qwen3-VL-Embedding-2B-vdr"
args = SentenceTransformerTrainingArguments(
# Required parameter:
output_dir=f"models/{run_name}",
# Optional training parameters:
num_train_epochs=1,
per_device_train_batch_size=64,
per_device_eval_batch_size=64,
learning_rate=2e-5,
warmup_ratio=0.1,
fp16=False,
bf16=True,
batch_sampler=BatchSamplers.NO_DUPLICATES,
# Optional tracking/debugging parameters:
eval_strategy="steps",
eval_steps=0.1,
save_strategy="steps",
save_steps=0.1,
save_total_limit=2,
logging_steps=0.05,
run_name=run_name,
)
A few things to note for (multimodal) training:
bf16=True
: bfloat16 is generally preferred over float16 due to better numerical stability.batch_sampler=BatchSamplers.NO_DUPLICATES
: When usingMultipleNegativesRankingLoss
or its cached variant, having no duplicate samples in a batch ensures that every in-batch negative is a truly different sample.per_device_train_batch_size=64
: This may seem large for a 2B parameter VLM, butCachedMultipleNegativesRankingLoss
withmini_batch_size=1
handles the memory constraints through gradient caching.eval_steps
,save_steps
, andlogging_steps
: Setting these to a fraction (e.g., 0.1) means evaluation, saving, and logging will happen every 10% of an epoch, which is useful for monitoring training progress.
Evaluator
To track retrieval performance before, during, and after training, I use the InformationRetrievalEvaluator
. It computes standard retrieval metrics like NDCG@10, MAP, and Recall@k:
from sentence_transformers.sentence_transformer.evaluation import InformationRetrievalEvaluator
# Build the evaluation data from the eval dataset.
# Queries and corpus use integer IDs: query 0's relevant document is corpus 0.
eval_queries = {qid: sample["query"] for qid, sample in enumerate(eval_dataset)}
eval_corpus = {did: sample["image"] for did, sample in enumerate(eval_dataset)}
num_eval = len(eval_dataset)
# Add hard negatives to the corpus with offset IDs (num_eval, 2*num_eval, ...)
# so they don't collide with the positive document IDs (0..num_eval-1).
negative_columns = ["negative_0", "negative_1", "negative_2", "negative_3"]
for neg_idx, neg_col in enumerate(negative_columns):
for did, sample in enumerate(eval_dataset):
eval_corpus[num_eval * (neg_idx + 1) + did] = sample[neg_col]
# Each query's relevant document is the positive at the same index
eval_relevant_docs = {idx: [idx] for idx in range(len(eval_dataset))}
eval_evaluator = InformationRetrievalEvaluator(
queries=eval_queries,
corpus=eval_corpus,
relevant_docs=eval_relevant_docs,
batch_size=1,
show_progress_bar=True,
name="vdr-eval-hard",
)
The evaluator takes text queries, a corpus of images (including hard negatives), and a mapping of which documents are relevant to which queries. Note that the corpus contains a mix of positive and hard negative document screenshots, making this a challenging evaluation. Using batch_size=1
prevents out-of-memory issues during evaluation of the large VLM.
Trainer
The SentenceTransformerTrainer
brings everything together. Here's the complete training script:
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from sentence_transformers.sentence_transformer.evaluation import InformationRetrievalEvaluator
from sentence_transformers.sentence_transformer.losses import CachedMultipleNegativesRankingLoss, MatryoshkaLoss
from sentence_transformers.sentence_transformer.model_card import SentenceTransformerModelCardData
from sentence_transformers.sentence_transformer.trainer import SentenceTransformerTrainer
from sentence_transformers.sentence_transformer.training_args import (
BatchSamplers,
SentenceTransformerTrainingArguments,
)
# 1. Load a model to finetune with (optional) model card data
model = SentenceTransformer(
"Qwen/Qwen3-VL-Embedding-2B",
model_card_data=SentenceTransformerModelCardData(
language="en",
license="apache-2.0",
model_name="Qwen3-VL-Embedding-2B model trained on Visual Document Retrieval query-document screenshot pairs",
),
model_kwargs={"attn_implementation": "flash_attention_2", "torch_dtype": "bfloat16"},
# Control image resolution: lower values save memory, higher values preserve detail
processor_kwargs={"min_pixels": 28 * 28, "max_pixels": 600 * 600},
)
# 2. Load a dataset to finetune on: (query, positive, negative_0) triplets for training,
# all 4 hard negatives retained for evaluation
train_dataset = load_dataset("tomaarsen/llamaindex-vdr-en-train-preprocessed", "train", split="train")
train_dataset = train_dataset.select_columns(["query", "image", "negative_0"])
eval_dataset = load_dataset("tomaarsen/llamaindex-vdr-en-train-preprocessed", "eval", split="train")
# 3. Define a loss function
loss = CachedMultipleNegativesRankingLoss(model, mini_batch_size=1)
loss = MatryoshkaLoss(model, loss, matryoshka_dims=[2048, 1536, 1024, 512, 256, 128, 64])
# 4. (Optional) Specify training arguments
run_name = "Qwen3-VL-Embedding-2B-vdr"
args = SentenceTransformerTrainingArguments(
# Required parameter:
output_dir=f"models/{run_name}",
# Optional training parameters:
num_train_epochs=1,
per_device_train_batch_size=64,
per_device_eval_batch_size=64,
learning_rate=2e-5,
warmup_ratio=0.1,
fp16=False, # BF16 is preferred over FP16 for VLMs due to better numerical stability
bf16=True, # Set to True if your GPU supports BF16 (most modern GPUs do)
batch_sampler=BatchSamplers.NO_DUPLICATES, # MultipleNegativesRankingLoss benefits from no duplicates
# Optional tracking/debugging parameters:
eval_strategy="steps",
eval_steps=0.1,
save_strategy="steps",
save_steps=0.1,
save_total_limit=2,
logging_steps=0.05,
run_name=run_name, # Used in e.g. Trackio if installed
# report_to=["codecarbon", "trackio"], # Uncomment to enable logging (pip install codecarbon trackio)
)
# 5. (Optional) Create an evaluator & evaluate the base model
eval_queries = {qid: sample["query"] for qid, sample in enumerate(eval_dataset)}
eval_corpus = {did: sample["image"] for did, sample in enumerate(eval_dataset)}
num_eval = len(eval_dataset)
negative_columns = ["negative_0", "negative_1", "negative_2", "negative_3"]
for neg_idx, neg_col in enumerate(negative_columns):
for did, sample in enumerate(eval_dataset):
eval_corpus[num_eval * (neg_idx + 1) + did] = sample[neg_col]
eval_relevant_docs = {idx: [idx] for idx in range(len(eval_dataset))}
eval_evaluator = InformationRetrievalEvaluator(
queries=eval_queries,
corpus=eval_corpus,
relevant_docs=eval_relevant_docs,
batch_size=1,
show_progress_bar=True,
name="vdr-eval-hard",
)
eval_evaluator(model)
# 6. Create a trainer & train
trainer = SentenceTransformerTrainer(
model=model,
args=args,
train_dataset=train_dataset,
eval_dataset=eval_dataset,
loss=loss,
evaluator=eval_evaluator,
)
trainer.train()
# 7. (Optional) Evaluate at each Matryoshka dimension
eval_evaluator(model)
for dim in [2048, 1536, 1024, 512, 256, 128, 64]:
dim_evaluator = InformationRetrievalEvaluator(
queries=eval_queries,
corpus=eval_corpus,
relevant_docs=eval_relevant_docs,
truncate_dim=dim,
batch_size=1,
show_progress_bar=True,
name=f"vdr-eval-hard-{dim}d",
)
dim_evaluator(model)
# 8. Save the trained model
model.save_pretrained(f"models/{run_name}/final")
# 9. (Optional) Push it to the Hugging Face Hub
# This pushes to your personal namespace, e.g. {your_username}/Qwen3-VL-Embedding-2B-vdr
model.push_to_hub("Qwen3-VL-Embedding-2B-vdr")
The training script is nearly identical to a text-only training script. The only differences are:
- Model loading: We pass
model_kwargs
for precision and attention implementation, andprocessor_kwargs
for image resolution bounds. - Loss function: We use
CachedMultipleNegativesRankingLoss
withmini_batch_size=1
to handle the large VLM without running out of memory. - Evaluator: The evaluator uses images in the corpus and text as queries, enabling cross-modal retrieval evaluation.
Everything else (the trainer, training arguments, dataset loading) works exactly the same as text-only training.
Results
Model Size vs NDCG@10
After training for just 1 epoch, the finetuned tomaarsen/Qwen3-VL-Embedding-2B-vdr model achieves an NDCG@10 of 0.947 on the evaluation set (300 queries, 1500 corpus documents, cosine similarity). This is a significant improvement over the base Qwen/Qwen3-VL-Embedding-2B model's 0.888, and outperforms all existing VDR models:
Full NDCG@10 numbers by model (20 models)
The finetuned 2B model outperforms even the 8B Qwen3-VL-Embedding model, demonstrating the power of task-specific finetuning. Finetuning on your own domain is often worth considering, even when a larger general-purpose model is available!
Matryoshka Dimensions vs NDCG@10
The comparison above uses full-size 2048-dim embeddings. Thanks to the Matryoshka training, the finetuned model also holds up well when truncated to fewer dimensions, letting you trade off embedding size and retrieval quality at deployment time:
The finetuned model's peak is at the full 2048 dimensions (0.948), but it stays within 0.3% of peak all the way down to 512 (4x smaller), and retains over 92% of peak even at 64 (32x smaller). Matryoshka training concentrates the most important information in the earlier dimensions, so moderate truncation costs very little performance.
Full NDCG@10 numbers by dimension
The gap between 1024 and 2048 dimensions is small (0.946 vs. 0.948), so I've saved the model with truncate_dim=1024
set in its configuration. This means that SentenceTransformer("tomaarsen/Qwen3-VL-Embedding-2B-vdr")
produces 1024-dimensional embeddings by default, halving the storage footprint compared to the full 2048. If you want a different dimensionality, pass truncate_dim=N
when loading to override it.
Training Multimodal Reranker Models
You can also finetune multimodal Cross Encoder (reranker) models using the same training infrastructure. The key difference is using CrossEncoderTrainer
and Cross Encoder-specific loss functions. This section provides a brief overview; see the full training examples for complete, runnable scripts with dataset preparation and evaluation.
Here's a simplified example based on the doodles training script, which trains a reranker to match images with text captions:
from sentence_transformers.cross_encoder import CrossEncoder
from sentence_transformers.cross_encoder.losses import BinaryCrossEntropyLoss
from sentence_transformers.cross_encoder.modules import LogitScore, Transformer
from sentence_transformers.cross_encoder.trainer import CrossEncoderTrainer
from sentence_transformers.cross_encoder.training_args import CrossEncoderTrainingArguments
# 1. Build the model from modules
transformer = Transformer(
"Qwen/Qwen3.5-0.8B",
transformer_task="any-to-any",
model_kwargs={"torch_dtype": "bfloat16", "device_map": "auto", "attn_implementation": "flash_attention_2"},
processing_kwargs={"chat_template": {"add_generation_prompt": True}},
)
# Extend chat template to support "query" and "document" roles
transformer.processor.chat_template = transformer.processor.chat_template.replace(
'message.role == "user"', 'message.role in ["user", "query", "document"]'
)
# LogitScore: score = log(P("1")) - log(P("0"))
score_head = LogitScore(
true_token_id=transformer.tokenizer.convert_tokens_to_ids("1"),
false_token_id=transformer.tokenizer.convert_tokens_to_ids("0"),
)
model = CrossEncoder(
modules=[transformer, score_head],
num_labels=1,
prompts={
"image_to_text": "Given the image, judge whether the text matches it. Respond with 1 if they match, 0 if they don't.",
"text_to_image": "Given the text, judge whether the image matches it. Respond with 1 if they match, 0 if they don't.",
},
)
# 2. Define the loss
loss = BinaryCrossEntropyLoss(model)
# 3. Multi-dataset training with separate directions
trainer = CrossEncoderTrainer(
model=model,
args=args,
train_dataset={"image_to_text": train_image_to_text, "text_to_image": train_text_to_image},
eval_dataset={"image_to_text": eval_image_to_text, "text_to_image": eval_text_to_image},
loss=loss,
evaluator=[image_to_text_evaluator, text_to_image_evaluator],
)
trainer.train()
There are multiple valid architectural choices for multimodal rerankers, including:
- Any-to-Any + LogitScore: Uses the multimodal language model to generate a token, then computes the log-odds of "1" vs "0".
- Feature Extraction + Pooling + Dense: Uses only the multimodal base model, and extracts the last token's hidden state and projects it to a score via a Dense layer, avoiding the language modeling head computation.
Both approaches are demonstrated in the multimodal cross encoder training examples.
The two scripts linked above split the training data into two datasets, one per direction (image-to-text and text-to-image), with a task-specific prompt for each that tells the model how to score in that direction. Each positive pair is then expanded with randomly sampled negatives so the loss sees a balanced mix of matches and non-matches.
Additional Resources
Training Examples
The Sentence Transformers repository includes several multimodal training examples:
- Visual Document Retrieval: The training script used in this blogpost to finetune a VLM-based embedding model for document screenshot retrieval
- Multimodal Reranker (Any-to-Any): Train a multimodal reranker using LogitScore
- Multimodal Reranker (Feature Extraction): Train a multimodal reranker using Pooling + Dense
Documentation
Additionally, the following pages may be useful to learn more about training with Sentence Transformers:
- Sentence Transformer > Training Overview
- Sentence Transformer > Loss Overview
- Cross Encoder > Training Overview
- Cross Encoder > Loss Overview
- Dataset Overview
- API Reference
Companion Blogposts
The direct prerequisite and the prior training guides are listed first, followed by related technique posts that stack with multimodal training:
- Multimodal Embedding & Reranker Models with Sentence Transformers: multimodal inference, the companion to this training post.
- Training and Finetuning Embedding Models with Sentence Transformers: the general training guide for text-only embedding models.
- Training and Finetuning Reranker Models with Sentence Transformers: Cross Encoder (reranker) training, including the ModernBERT-base reranker example.
- Training and Finetuning Sparse Embedding Models with Sentence Transformers: SPLADE and other sparse encoder training.
- 🪆 Introduction to Matryoshka Embedding Models: background on the
MatryoshkaLoss
used in this post to produce embeddings that truncate gracefully. - Train 400x faster Static Embedding Models with Sentence Transformers: CPU-friendly text embeddings, a natural counterpart to heavy VLM-based models.
- Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval: post-training compression that also applies to multimodal embeddings.
- Visual Document Retrieval Goes Multilingual: the LlamaIndex post that introduced the dataset used in this blogpost's Visual Document Retrieval example.
```

---

## 16. Inside VAKRA: Reasoning, Tool Use, and Failure Modes of Agents

- 日期: 2026-04-15 12:07
- 链接: https://huggingface.co/blog/ibm-research/vakra-benchmark-analysis

```
Inside VAKRA: Reasoning, Tool Use, and Failure Modes of Agents
VAKRA Dataset | LeaderBoard | Release Blog | GitHub | Submit to Leaderboard
We recently introduced VAKRA, a tool-grounded, executable benchmark for evaluating how well AI agents reason and act in enterprise-like environments.
Unlike traditional benchmarks that test isolated skills, VAKRA measures compositional reasoning across APIs and documents, using full execution traces to assess whether agents can reliably complete multi-step workflows.
VAKRA provides an executable environment where agents interact with over 8,000+ locally hosted APIs backed by real databases spanning 62 domains, along with domain-aligned document collections. Tasks can require 3-7 step reasoning chains that combine structured API interaction with unstructured retrieval under natural-language tool-use constraints.
As can be seen below, models perform poorly on VAKRA - in this blog, we include additional dataset details about the tasks in VAKRA and present an analysis of failure modes we observed on different tasks.
Task Description
As shown below, the VAKRA benchmark comprises of four tasks, each testing a different set of capabilities.
Fig 1: Representative examples of each capability in the VAKRA benchmark
Capability 1: API Chaining using Business Intelligence APIs
This capability includes 2,077 test instances across 54 domains, requiring the use of tools from the SLOT-BIRD and SEL-BIRD collections (Elder et al., 2026). Compared to the setup in Elder et al., the tool universe in SLOT-BIRD and SEL-BIRD is expanded through the inclusion of a larger number of domains. Each domain is restricted to one tool collection, and tasks involve chaining 1–12 tool calls to arrive at the final answer.
{
"query": "Which football team has a build-up play speed of 31, build-up plan dribbling of 53, and build-up play passing of 32?",
"tool_calls":[
{
"name": "get_data",
"arguments":{"tool_universe_id="486ea46224d1-aeb8037c5e78"},
"label": "retrieved_data_1"
},
{
"name": "select_data_equal_to",
"arguments":{"data_label":"retrieved_data_1","key_name":"play_speed","value":31},
"label": "FILTERED_DF_0"
},
{
"name": "select_data_equal_to",
"arguments":{"data_label":"FILTERED_DF_0","key_name":"play_dribble","value":53},
"label": "FILTERED_DF_1"
},
{
"name": "select_data_equal_to",
"arguments":{"data_label":"FILTERED_DF_1","key_name":"play_passing","value":32},
"label": "FILTERED_DF_2"
},
{"name":{get_team_name},"arguments":{"data_label":"FILTERED_DF_2","n":1}}}],
"answer": "FC Barcelona"
}
Fig 2: Data sample from SEL-BIRD collection
As shown above, each instance has an associated JSON data source from which the answer must be derived. The MCP servers supporting this task include a special tool, called get_data(tool_universe_id=id)
, which must be called at the beginning of each instance.
This tool initializes the data source, returns a lightweight preview of the data (see below Figure 3), and stores the full dataset server-side to avoid large data transfers. This prevents the inefficient transfer of large data over the MCP protocol. The call also configures the MCP server to expose the appropriate tool set based on the tool_universe_id
and aligns the data source with the domain-specific database for the instance.
The SLOT-BIRD collection provides a global set of 7 tools for generic data manipulation (e.g., filtering, sorting), inspired by systems like Tableau and
Google Analytics. The SEL-BIRD collection extends this by introducing more specialized tools: some are shared with SLOT-BIRD, while others are derived by flattening categorical arguments into separate functions (e.g., sort_data
with argument ascending: bool = False
becomes sort_data_ascending
and sort_data_descending
). Additionally, the generic (retrieve_data
) function from SLOT-BIRD is replaced with query-specific getters. Every key in the data for a given instance has an associated get function (get_KEY_NAME
) for an average of 4 get functions per instance.
{
"handle": "retrieved_data_1",
"num_records": 2,
"key_details": [
{"name": "team_name", "dtype": "str", "first_3_values": ["FC Barcelona", "Manchester City"]},
{"name": "play_speed", "dtype": "int32", "first_3_values": [31, 40]},
{"name": "play_dribble", "dtype": "int32", "first_3_values": [53, 30]},
{"name": "play_passing", "dtype": "int32", "first_3_values": [32, 16]}
]}
Fig 3: Data preview obtained from `get_data` function
Capability 2: Tool Selection using Dashboard APIs
This capability includes 1,597 instances across 17 domains, requiring tools from an expanded REST-BIRD collection (Elder et al.).
These use endpoint-style interfaces that provide highly specific, query-aligned endpoints that encapsulate most computation. They are served as REST APIs running in a FastAPI server, which is wrapped by the MCP server. This task requires selecting the correct APIs from the domain-specific tool set (as shown in the example in Figure 1). Each domain contains a minimum of 6 to a maximum of 328 tools (with an average of 116 tools). Similar to the previous task, the get_data
tool configures the MCP server to expose only the relevant domain-specific APIs.
The OpenAI API Specification restricts the tool list input to a maximum length of 128 tools. This restriction requires an agent builder using this API to manage the length of the tool list directly via a shortlisting mechanism. In the baseline agents in our repository, a simple shortlisting capability handles this challenge.
Capability 3: Multi-Hop Reasoning using Dashboard APIs
The Capability 3 segment of the benchmark has 869 test instances drawn from 38 subject domains. These instances rely again on the REST-BIRD API collection, but add multi-hop reasoning to the challenge (refer to example in Figure 1). Multi-hop questions require multiple pieces of supporting evidence to be extracted and combined to reach an answer. The instances in this section require between one and five logical hops to answer a query. The question types distribution for queries within the test dataset is shown below in Figure 4.
Fig 4: API Hop-Type distribution for Capability 3 (MultiHop) and Hybrid Hop-Type distribution for Capability 4 (MultiHop MultiSource Reasoning)
Capability 4: Multi-Hop, Multi-Source Reasoning and Policy Adherence
Capability 4 includes 644 instances across 41 domains and is also built on the REST-BIRD API collection. Figure 4 above shows a distribution of hybrid hops for test queries without policies. It contains the most complex queries with the following characteristics:
Multi-Source: This segment adds document indices per domain. Queries in this capability could require information from these document indexes as well as API calls. Similar to Capability 3, this task also has Multi-Hop queries. The required information source applies at the per-hop level, so, for example, a question may entail three logical hops with sources: API - RAG (Document Retrieval) - API. To enforce correct reasoning, sources are decontaminated during data generation, i.e. information required for a given hop is available in only one source. For example, if a hop is to be answered using APIs, the document index is built by removing documents that likely contain the information needed to answer the question.
Multi-Turn: This segment of the dataset also adds multi-turn conversations to the setting. Each instance is a dialog with multiple turns. The data is released as context-response pairs, where the context encodes the current dialog history and the agent is only responsible for answering the current turn.
Tool-usage Policies: A subset of these instances includes tool-use policies that the agent is required to follow. These policies take the form of plain-text instructions about the knowledge sources that the agent is allowed to access and under which circumstances. For example:
If a user's query pertains to Technology & Software, which is/are about Topics focusing on codebases,
software platforms, applications, and user interactions in tech, make sure you try answering them by
only using document retrievers. Do not use other types of tools.
The baseline agent in the project repo imposes adherence to these policies through a simple addition to the prompt: "You are a helpful assistant with access to tools.\n Tool Usage Constraint: {additional_instructions}."
. Of course, agent builders are free to choose any constraint enforcement mechanism.
Evaluation Framework
VAKRA evaluates agents in tool environments where success depends on both the ability to execute coherent, multi-step workflows and answer correctness. We introduce an execution-centric evaluation framework that assesses not only final outputs but also the full tool-execution trajectory that includes tool calls, inputs, and intermediate results.
Evaluation Metric
The VAKRA Evaluator operates over two key inputs for each sample: a predicted final response and the corresponding tool-call trajectory. The tool calls from the predicted trajectory are executed in the same environment as the ground truth to verify intermediate tool outputs.
The evaluation follows a waterfall-style pipeline (Figure 6), where later stages are conditioned on earlier success:
- For Capability 4 tasks, policy adherence is first verified programmatically (this step is not applied to other capabilities).
- The predicted tool call sequence is then compared against the ground truth sequence.
- Only samples with valid trajectories proceed to final response evaluation.
Fig 6: Waterfall-style Evaluation Pipeline
Tool-Sequence Comparison Due to the presence of an executable environment, agents can explore the environment and sometimes return the answer by invoking a different set of APIs than the ones identified by us. In order to support alternative but valid tool invocations and reasoning paths, correctness is assessed by executing each predicted tool and comparing the set of tool responses against those from the ground truth (rather than enforcing strict step-level matching).
Specifically, we first perform a programmatic check, verifying whether all information present in the ground-truth tool responses is recovered by the predicted tool responses. This check may be inconclusive in cases involving partial matches, semantic equivalence, or differences in representation (e.g., ordering, aggregation, or formatting). In such cases, we apply a secondary LLM-based evaluation, adapted from the CRAG framework Yang et al., 2024, to determine whether the predicted trajectory retrieves all required information despite structural differences. This step uses an adapted prompt to determine whether the predicted trajectory captures all required information, even if obtained through a different sequence of tool calls.
Final Response Evaluation For trajectories that pass the previous check, the final response is evaluated using an LLM-based judge. This step ensures that the response is (i) grounded in the predicted tool outputs, and (ii) factually consistent with the ground truth answer, accounting for potential variations in phrasing or structure.
This design ensures that agents are rewarded not only for producing correct answers, but for obtaining them through valid and complete reasoning processes.
Scoring
Every capability is equally weighted to obtain a final leaderboard score
To obtain a capability score, every sample within a capability is equally weighted for capabilities 1 through 3.
For capability 4, we weight heterogeneous queries higher:
Error Analysis
We now present detailed error analysis across the four VAKRA capabilities. To facilitate our analysis, we adopt stage-wise error categorization to assign each failure to the first point of breakdown. Specifically, we evaluate, in order: (i) whether the correct tool(s) were selected, (ii) whether the required arguments were provided without omissions or hallucinations, (iii) whether argument values were correct, and (iv) whether the final response is both accurate and grounded in the tool outputs.
Failure Stage Isolation
Since a single sample may exhibit multiple errors across different steps, we sequentially classify each instance to the earliest failing stage (e.g., tool selection errors take precedence over argument errors). This avoids double-counting and allows error categories to be interpreted as disjoint fractions of the dataset. While more granular metrics (e.g., precision/recall over tool usage) are possible (Elder et al., 2026), we find this formulation provides a simple and interpretable breakdown of agent failures.
The instances in this part of the benchmark required selecting and sequencing multiple tools to solve a single task. We have 2077 samples in this capability. This was challenging for all models, but GPT-OSS-120B performed best on this segment of the benchmark.
- GPT-OSS-120B outperformed the other models by a large margin, mostly from a better understanding of the tool schemas.
- The tools in this part of the benchmark involve a large number of parameters, many of which are optional, and GPT-OSS-120B was especially robust, as compared to the others, at choosing the right parameters to fill.
- Overall, synthesizing a correct answer after making all tool calls correctly was less challenging in this section of the benchmark, most likely because the tool call sequencing made the tool choice problem less amenable to guessing compared with the Dashboard API capability
Fig 7: SEL-BIRD vs SLOT-BIRD Error Types Analysis
The Business Intelligence (BI) API capability contains two sets of APIs, from the SLOT-BIRD and SEL-BIRD tool collections. The SEL part of this benchmark had 600 samples, while the SLOT part of the benchmark had 1477 samples. These two collections are grouped under the BI API capability, but have slightly different characteristics. The SLOT-BIRD collection has a smaller number of generic tools with a large number of parameter values to fill, while the SEL-BIRD collection has a larger set of tools and fewer parameters per tool. This focus is reflected in the relative errors made by models using these two tool collections.
- Using SLOT-BIRD, all models except for GPT-OSS-120b made a substantial number of errors producing correct names for the tool arguments. This is largely the reason that GPT-OSS-120b performed so well overall in this segment of the benchmark.
- With fewer parameters to fill, the same models made very few such errors when using the SEL-BIRD tool collection, but they made many more errors selecting the correct tools, reflecting the increased difficulty of choosing from a larger (and dynamic) tool set.
- As shown above, for the 1597 samples in the tool selection capability, Gemini-3-flash-preview outperforms the other models tested on all error categories.
- As expected, since the dashboard API instances require the models to choose from a large number of tool options, but each tool requires only a small number of parameters, there are a large number of errors in tool selection and parameter value selection.
- There seems to be little problem with hallucinating or skipping required parameters. However, even when all tool calls are made correctly, models (especially Gemini-3-flash-preview and Claude-Sonnet-4-5 still struggle to synthesize a correct answer from the tool responses, as evidenced by the large drop-offs at the far right side of the plot.
Multi-Hop Reasoning: Effect of Hop Depth on Model Performance
Fig 8: Comparison of Accuracy Across Models by Hop Depth
Multi-hop reasoning increases the difficulty of the original task by requiring models to successfully answer multiple implicitly coupled questions, each of which requires selecting and calling the correct API. As expected, all models performed best on the questions with only a single logical hop, and saw performance degradations on 2-hop and again on 3+ hop questions.
Multi-Hop Multi-Source Reasoning: Effect of Hybrid Hops on Model Performance
Fig 9: Model Accuracy Rates by Interaction Type (API, Document-Retriever, Hybrid)
The final segment of the dataset includes document sources in addition to the tool/API sources in the other segments. This leads to instances that require single or multiple API calls, single or multiple document searches, or some combination of API calls and document searches.
- As before, there is a marked difference in performance on instances that require single API calls (1-hop API) as compared to those that require multiple API invocations (2-hop API), and including document retrievers makes the task more challenging (RAG Hops and Hybrid).
- Interestingly, we find that on questions that require a single document retriever call (1-hop RAG), GPT-OSS-120B tries to directly return the answer from parameter knowledge, though when the question appears to require multiple hops, it answers the question. We hypothesize that since the questions for 1-hop RAG are very Wikipedia-entity focussed the model skips the tool call (we don't see this problem on 1-hop API, where back-end database-specific entities/facts might be present more frequently in the question).
- It is also interesting that the performance of Gemini-3-flash-preview shoots up on 2-hop API-RAG as compared to other hybrid hop-patterns. This is likely explained by the relatively strong performance of Gemini-3-flash-preview on the dashboard APIs (Tool Selection Capability), and thus, once the correct intermediate answer is identified using the tool-call, the retrieval query is likely to be more successful.
Effect of Policies on Model Performance
Fig 10: Model Accuracy Rates by Policy Type
Policies introduce an additional layer of difficulty on top of multi-hop, multi-source reasoning. When policies align with the required source for answering i.e. they do not affect the tool list required for models to answer the question, we refer to it as "No Updates to Answer" -- as shown in Figure 10, all models except for Granite-4.0-h-Small-32B experience a clear drop in performance under policy constraints that restrict access to the most relevant information source (i.e. "Policy updates the answer").
In general, we find that models either violate constraints or fail to retrieve sufficient information, where they sometimes understood the policy but could not answer the question correctly, or they exhibit one of the previously analyzed failure modes.
Overall, tool-use policy-constrained settings suggest that while models can reason over tools and sources, they struggle to incorporate external constraints into that reasoning - often a key requirement for reliable real-world deployment.
Conclusion
VAKRA exposes a critical gap between surface-level tool competence and robust, end‑to‑end agent reliability. Although modern models can increasingly select APIs and execute isolated tool calls, VAKRA shows that these abilities alone are insufficient for real‑world deployment. In practice, models often break down when required to perform compositional reasoning under execution constraints—spanning APIs, documents, dialog context, and policy requirements.
Try VAKRA — Where Does Your Agent Break?
Think your agent is solid? Put it to the test.
Run it on VAKRA and see where it falls apart—tool selection, multi-hop reasoning, or policy constraints.
- ⭐ Submit to the leaderboard: https://github.com/IBM/vakra?tab=readme-ov-file#submitting-to-the-live-leaderboard
- 📦 Explore the dataset: https://huggingface.co/datasets/ibm-research/VAKRA
- 🛠️ Check out the code: https://github.com/IBM/vakra
👉 Try it and tell us what your agent learned
```

---

## 17. Meet HoloTab by HCompany. Your AI browser companion.

- 日期: 2026-04-15 09:25
- 链接: https://huggingface.co/blog/Hcompany/holotab

```
Meet HoloTab by HCompany. Your AI browser companion.
We built one of the most powerful computer-use AIs in the world. And made it directly accessible from your browser. On March 31st, we released Holo3, our most advanced computer-use model to date.
Building something powerful is one thing; making it accessible and easy to use is another. We’re doing both.
HoloTab is a Chrome extension that navigates the web just like a person would. It automates tasks across any website with zero setup or technical skills required. You describe what you want, and the agent handles it directly inside your browser, navigating interfaces, filling fields, and making decisions the same way you would. The vision models, the action planning, the interface understanding, all of it is running underneath, working for you, and all you ever see is the result.
Routines: Show it once. Run it anytime.
Some tasks are quick and forgettable, but others are long and repetitive, the kind that reliably eat up your afternoon. You might find yourself cross-referencing competitor pricing across twenty different e-commerce tabs to update a master spreadsheet, or filtering through a dozen job boards and company career pages to find new listings, painstakingly porting the details into a tracking doc to manage your applications.
That's where routines come in. You start a recording, and HoloTab captures what you do in your tab in real time while you click or narrate along the way, demonstrating what you're doing and why. Your screen and your actions give HoloTab everything it needs, enriching the routine with enough context to actually understand the goal.
Once the recording stops, a routine is generated. From then on, you can re-run your routine or schedule it whenever you need to, and HoloTab will handle the rest on its own.
Built for everyone
Computer-use AI is going to change how people work, research, and get things done, both in their professional and personal lives, and that shift is already closer than most people realize. But it shouldn't require a technical background to access, and the benefits shouldn't accrue only to teams with engineers who know how to wire these systems together.
HoloTab is free and ready for everyone to use today: https://chromewebstore.google.com/detail/holotab/hlaoiikljjgcjdhkakedfngifaopbcop
```

---

## 18. Waypoint-1.5: Higher-Fidelity Interactive Worlds for Everyday GPUs

- 日期: 2026-04-09 00:00
- 链接: https://huggingface.co/blog/waypoint-1-5

```
Waypoint-1.5: Higher-Fidelity Interactive Worlds for Everyday GPUs
Try it
What is Waypoint-1.5?
Waypoint-1.5 is Overworld’s next real-time video world model, built to bring interactive generative worlds to the hardware people actually own.
The first release of Waypoint showed that real-time generative worlds were possible. It proved that interactive world models could be more than passive video demos, and that locally runnable systems could begin to close the gap between generating a world and actually stepping into one.
Waypoint-1.5 builds directly on that foundation. This release improves visual fidelity, expands the range of hardware that can run the model locally, and takes another step toward interactive world simulation without datacenter-scale compute.
On desktop hardware including RTX 3090 through 5090, Waypoint-1.5 can generate real-time environments at up to 720p and 60 FPS. This release also introduces a 360p tier designed to run smoothly across a much broader range of consumer hardware, including gaming laptops, and (soon) Apple Silicon Macs.
What’s new in Waypoint-1.5?
The biggest change in Waypoint-1.5 is accessibility.
With Waypoint-1, we proved the core experience. With Waypoint-1.5, we wanted to make that experience available on more machines without giving up real-time interactivity. That meant building two model tiers: a 720p model for higher-performance hardware, and a 360p model optimized for broader deployment.
We also scaled training dramatically. Waypoint-1.5 was trained on nearly 100x more data than Waypoint-1, which significantly improves the model’s ability to generate more coherent environments and more consistent motion over time.
Under the hood, Waypoint-1.5 also incorporates more efficient video modeling techniques to reduce redundant computation across frames. That matters because real-time world models are not judged only by how a single frame looks. They are judged by whether the world responds instantly, stays coherent as you move through it, and remains usable on local hardware.
Why this matters for world models
A lot of recent progress in generative video and world models has focused on visual fidelity. Those results matter, but fidelity alone is not what makes an interactive world feel real.
What people remember is responsiveness. They remember whether the environment reacts to them, whether motion stays coherent, whether the world holds together as they explore it, and whether the whole experience feels immediate instead of delayed.
That is the gap we care about most: the difference between watching a generated scene and actually being inside one.
If world models only run on large GPU clusters, they remain impressive demos. If they run locally on consumer hardware, they become something much more useful: a foundation for interactive entertainment, creative tooling, simulation, and AI-native environments people can actually explore.
Waypoint-1.5 is designed around that idea: not just better videos, but more responsive and explorable worlds that remain accessible on consumer hardware.
How to experience Waypoint-1.5
There are two ways to play Waypoint-1.5.
The first is local execution through Overworld Biome. This release is designed to run across a wide range of hardware configurations, and the updated Biome runtime makes local setup much simpler. With the new installer flow, users can go from download to running the model locally in minutes.
The second is Overworld Stream, which lets you try Waypoint-1.5 instantly in the browser with no local setup required.
Whether you want immediate access or full local control, Waypoint-1.5 is built to support both.
Additionally, we provide World Engine, our flexible, easy to use, core inference library powering our official clients, along with nearly a dozen third party clients and libraries.
The path forward
Waypoint started with a simple question: what would it take for generative worlds to become truly interactive?
Early generative systems showed that models could produce convincing images and videos. But building environments that people can explore, control, and interact with in real time is a different challenge entirely.
Waypoint-1.5 is another step in that direction, improving fidelity and expanding hardware accessibility while continuing to push real-time interactive generation onto local machines.
We think the future of world models will not be defined only by what they can render, but by whether people can actually inhabit and interact with them in real time.
Download Waypoint-1.5, run it locally with Biome, or jump in instantly on Overworld.stream.
And if you build something fun, strange, or unexpectedly immersive with it, we’d love to see it.
```

---

## 19. Multimodal Embedding & Reranker Models with Sentence Transformers

- 日期: 2026-04-09 00:00
- 链接: https://huggingface.co/blog/multimodal-sentence-transformers

```
Multimodal Embedding & Reranker Models with Sentence Transformers
Multimodal embedding models map inputs from different modalities into a shared embedding space, while multimodal reranker models score the relevance of mixed-modality pairs. This opens up use cases like visual document retrieval, cross-modal search, and multimodal RAG pipelines.
If you want to train your own multimodal models, check out the companion blogpost: Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers.
Table of Contents
- What are Multimodal Models?
- Installation
- Multimodal Embedding Models
- Multimodal Reranker Models
- Retrieve and Rerank
- Input Formats and Configuration
- Supported Models
- Additional Resources
What are Multimodal Models?
Traditional embedding models convert text into fixed-size vectors. Multimodal embedding models extend this by mapping inputs from different modalities (text, images, audio, or video) into a shared embedding space. This means you can compare a text query against image documents (or vice versa) using the same similarity functions you're already familiar with.
Similarly, traditional reranker (Cross Encoder) models compute relevance scores between pairs of texts. Multimodal rerankers can score pairs where one or both elements are images, combined text-image documents, or other modalities.
For example, you can compare a text query against image documents, find video clips matching a description, or build RAG pipelines that work across modalities.
Installation
Multimodal models require some extra dependencies. Install the extras for the modalities you need (see Installation for more details):
# For image support
pip install -U "sentence-transformers[image]"
# For audio support
pip install -U "sentence-transformers[audio]"
# For video support
pip install -U "sentence-transformers[video]"
# Mix and match as needed
pip install -U "sentence-transformers[image,video,train]"
VLM-based models like Qwen3-VL-2B require a GPU with at least ~8 GB of VRAM. For the 8B variants, expect ~20 GB. If you don't have a local GPU, consider using a cloud GPU service or Google Colab. On CPU, these models will be extremely slow; text-only or CLIP models are better suited for CPU inference.
Multimodal Embedding Models
Loading a Model
Loading a multimodal embedding model works exactly like loading a text-only model:
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")
Some models might require a
revision
argument for now if the integration pull requests for the model is still pending. Once they're merged, you'll be able to load them without specifying a revision, like above.
The model automatically detects which modalities it supports, so there's nothing extra to configure. See Processor and Model kwargs if you want to control things like image resolution or model precision.
Encoding Images
With a multimodal model loaded, model.encode()
accepts images alongside text. Images can be provided as URLs, local file paths, or PIL Image objects (see Supported Input Types for all accepted formats):
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")
# Encode images from URLs
img_embeddings = model.encode([
"https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
"https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
])
print(img_embeddings.shape)
# (2, 2048)
Cross-Modal Similarity
You can compute similarities between text embeddings and image embeddings, since the model maps both into the same space:
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")
# Encode images
img_embeddings = model.encode([
"https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
"https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
])
# Encode text queries (one matching + one hard negative per image)
text_embeddings = model.encode([
"A green car parked in front of a yellow building",
"A red car driving on a highway",
"A bee on a pink flower",
"A wasp on a wooden table",
])
# Compute cross-modal similarities
similarities = model.similarity(text_embeddings, img_embeddings)
print(similarities)
# tensor([[0.5115, 0.1078],
# [0.1999, 0.1108],
# [0.1255, 0.6749],
# [0.1283, 0.2704]])
As expected, "A green car parked in front of a yellow building" is most similar to the car image (0.51), and "A bee on a pink flower" is most similar to the bee image (0.67). The hard negatives ("A red car driving on a highway", "A wasp on a wooden table") correctly receive lower scores.
You might notice that even the best matching scores (0.51, 0.67) aren't very close to 1.0. This is due to the modality gap: embeddings from different modalities tend to cluster in separate regions of the space. Cross-modal similarities are typically lower than within-modal ones (e.g., text-to-text), but the relative ordering is preserved, so retrieval still works well.
Encoding Queries and Documents
For retrieval tasks, encode_query()
and encode_document()
are the recommended methods. Many retrieval models prepend different instruction prompts depending on whether the input is a query or a document, similar to how chat models might apply different system prompts depending on the goal. Model authors can specify their prompts in the model config, and encode_query()
/ encode_document()
automatically load and apply the correct one:
encode_query()
uses the model's"query"
prompt (if available) and setstask="query"
.encode_document()
uses the first available prompt from"document"
,"passage"
, or"corpus"
, and setstask="document"
.
Under the hood, both are thin wrappers around encode()
, they just handle prompt selection for you. Here's what cross-modal retrieval looks like:
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")
# Encode text queries with the query prompt
query_embeddings = model.encode_query([
"Find me a photo of a vehicle parked near a building",
"Show me an image of a pollinating insect",
])
# Encode document screenshots with the document prompt
doc_embeddings = model.encode_document([
"https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
"https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
])
# Compute similarities
similarities = model.similarity(query_embeddings, doc_embeddings)
print(similarities)
# tensor([[0.3907, 0.1490],
# [0.1235, 0.4872]])
These methods accept the same input types as encode()
(images, URLs, multimodal dicts, etc.) and pass through the same parameters. For models without specialized query/document prompts, they behave identically to encode()
.
Multimodal Reranker Models
Multimodal reranker (CrossEncoder) models score the relevance between pairs of inputs, where each element can be text, an image, audio, video, or a combination. They tend to outperform embedding models in terms of quality, but are slower since they process each pair individually. The currently available pretrained multimodal rerankers focus on text and image inputs, but the architecture supports any modality that the underlying model can handle.
Ranking Mixed-Modality Documents
The rank()
method scores and ranks a list of documents against a query, supporting mixed modalities:
from sentence_transformers import CrossEncoder
model = CrossEncoder("Qwen/Qwen3-VL-Reranker-2B")
query = "A green car parked in front of a yellow building"
documents = [
# Image documents (URL or local file path)
"https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
"https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
# Text document
"A vintage Volkswagen Beetle painted in bright green sits in a driveway.",
# Combined text + image document
{
"text": "A car in a European city",
"image": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
},
]
rankings = model.rank(query, documents)
for rank in rankings:
print(f"{rank['score']:.4f}\t(document {rank['corpus_id']})")
"""
0.9375 (document 0)
0.5000 (document 3)
-1.2500 (document 2)
-2.4375 (document 1)
"""
The reranker correctly identifies the car image (document 0) as the most relevant result, followed by the combined text+image document about a car in a European city (document 3). The bee image (document 1) scores lowest. Keep in mind that the modality gap can influence absolute scores: text-image pair scores may occupy a different range than text-text or image-image pair scores.
You can also check which modalities a reranker supports using modalities
and supports()
, just like with embedding models:
print(model.modalities)
# ['text', 'image', 'video', 'message']
print(model.supports("image"))
# True
# Check if the model supports a specific pair of modalities
print(model.supports(("image", "text")))
# True
Predicting Pair Scores
You can also use predict()
to get raw relevance scores for specific pairs of inputs:
from sentence_transformers import CrossEncoder
model = CrossEncoder("jinaai/jina-reranker-m0", trust_remote_code=True)
scores = model.predict([
("A green car", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"),
("A bee on a flower", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg"),
("A green car", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg"),
])
print(scores)
# [0.9389156 0.96922314 0.46063158]
Retrieve and Rerank
A common pattern is to use an embedding model for fast initial retrieval, then refine the top results with a reranker:
from sentence_transformers import SentenceTransformer, CrossEncoder
# Step 1: Retrieve with an embedding model
embedder = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")
query = "revenue growth chart"
query_embedding = embedder.encode_query(query)
# Pre-compute corpus embeddings (do this once, then store them)
document_screenshots = [
"path/to/doc1.png",
"path/to/doc2.png",
# ... potentially millions of document screenshots
]
corpus_embeddings = embedder.encode_document(document_screenshots, show_progress_bar=True)
# Simple cosine similarity retrieval, viable as long as embeddings fit in memory
similarities = embedder.similarity(query_embedding, corpus_embeddings)
top_k_indices = similarities.argsort(descending=True)[0][:10]
# Step 2: Rerank the top-k results with a reranker model
reranker = CrossEncoder("nvidia/llama-nemotron-rerank-vl-1b-v2", trust_remote_code=True)
top_k_documents = [document_screenshots[i] for i in top_k_indices]
rankings = reranker.rank(query, top_k_documents)
for rank in rankings:
print(f"{rank['score']:.4f}\t{top_k_documents[rank['corpus_id']]}")
Since the corpus embeddings are pre-computed, the initial retrieval is fast even over millions of documents. The reranker then provides more accurate scoring over the smaller candidate set.
Input Formats and Configuration
Supported Input Types
Multimodal models accept a variety of input formats. Here's a summary of what you can pass to model.encode()
:
Checking Modality Support
You can check which modalities a model supports using the modalities
property and supports()
method:
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")
# List all supported modalities
print(model.modalities)
# ['text', 'image', 'video', 'message']
# Check for a specific modality
print(model.supports("image"))
# True
print(model.supports("audio"))
# False
The "message"
modality indicates that the model accepts chat-style message inputs with interleaved content. In practice, you rarely need to use this directly. When you pass strings, URLs, or multimodal dicts, the model converts them to the appropriate message format internally. Sentence Transformers supports two message formats:
- Structured (most VLMs, e.g. Qwen3-VL): Content is a list of typed dicts, e.g.
[{"type": "text", "text": "..."}, {"type": "image", "image": ...}]
- Flat (e.g. Deepseek-V3): Content is a direct value, e.g.
"some text"
The format is auto-detected from the model's chat template.
Since all inputs get converted into the same message format internally, you can mix input types in a single encode()
call:
embeddings = model.encode([
# A text input
"A green car parked in front of a yellow building",
# An image input (URL)
"https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
# A combined text + image input
{
"text": "A car in a European city",
"image": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
},
])
Click here if you need to pass raw message inputs
If a model doesn't follow either format and you need full control, you can pass raw message dicts with role
and content
keys directly:
embeddings = model.encode([
[
{
"role": "user",
"content": [
{"type": "image", "image": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"},
{"type": "text", "text": "Describe this vehicle."},
],
}
],
])
This bypasses the automatic format conversion and passes the messages directly to the processor's apply_chat_template()
.
Processor and Model kwargs
You may want to control image resolution bounds or model precision. Use processor_kwargs
and model_kwargs
when loading the model:
model = SentenceTransformer(
"Qwen/Qwen3-VL-Embedding-2B",
model_kwargs={"attn_implementation": "flash_attention_2", "torch_dtype": "bfloat16"},
processor_kwargs={"min_pixels": 28 * 28, "max_pixels": 600 * 600},
)
processor_kwargs
controls how inputs are preprocessed (e.g., image resolution bounds). Highermax_pixels
means higher quality but more memory and compute. These are passed directly toAutoProcessor.from_pretrained(...)
.model_kwargs
controls how the underlying model is loaded (e.g., precision, attention implementation). These are passed directly to the appropriateAutoModel.from_pretrained(...)
call (e.g.,AutoModel
,AutoModelForCausalLM
,AutoModelForSequenceClassification
, etc., depending on the configuration of the model modules).
See the SentenceTransformer API Reference documentation for more details on these kwargs.
In Sentence Transformers v5.4,
tokenizer_kwargs
has been renamed toprocessor_kwargs
to reflect that multimodal models use processors rather than just tokenizers. The old name is still accepted but deprecated.
Supported Models
Here are the multimodal models supported in v5.4, also available in the v5.4 integrations collection:
Supported Multimodal Embedding Models
Supported Multimodal Reranker Models
Text-Only Reranker Models (also new in v5.4)
Click here for a text-only reranker usage example
from sentence_transformers import CrossEncoder
model = CrossEncoder("mixedbread-ai/mxbai-rerank-base-v2")
query = "How do I bake sourdough bread?"
documents = [
"Sourdough bread requires a starter made from flour and water, fermented over several days.",
"The history of bread dates back to ancient Egypt around 8000 BCE.",
"To bake sourdough, mix your starter with flour, water, and salt, then let it rise overnight.",
"Rye bread is a popular alternative to wheat-based breads in Northern Europe.",
]
pairs = [(query, doc) for doc in documents]
scores = model.predict(pairs)
print(scores)
# [ 7.3077507 -2.6217823 8.724761 -2.2488995]
rankings = model.rank(query, documents)
for rank in rankings:
print(f"{rank['score']:.4f}\t{documents[rank['corpus_id']]}")
# 8.7248 To bake sourdough, mix your starter with flour, water, and salt, then let it rise overnight.
# 7.3078 Sourdough bread requires a starter made from flour and water, fermented over several days.
# -2.2489 Rye bread is a popular alternative to wheat-based breads in Northern Europe.
# -2.6218 The history of bread dates back to ancient Egypt around 8000 BCE.
CLIP Models
The older CLIP models continue to be supported:
These simple CLIP models still work well on lower-resource hardware.
Click here for a CLIP usage example
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/clip-ViT-L-14")
images = [
"https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
"https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
"https://huggingface.co/datasets/huggingface/cats-image/resolve/main/cats_image.jpeg"
]
texts = ["A green car", "A bee on a flower", "Some cats on a couch", "One cat sitting in the window"]
image_embeddings = model.encode(images)
text_embeddings = model.encode(texts)
print(image_embeddings.shape, text_embeddings.shape)
# (3, 768) (4, 768)
similarities = model.similarity(image_embeddings, text_embeddings)
print(similarities)
# tensor([[0.2208, 0.1042, 0.0617, 0.0907], First image (car) is most similar to "A green car"
# [0.1205, 0.2303, 0.0632, 0.0917], Second image (bee) is most similar to "A bee on a flower"
# [0.1107, 0.0196, 0.2425, 0.1162]]) Third image (multiple cats) is most similar to "Some cats on a couch"
Additional Resources
Documentation
- Sentence Transformer > Usage
- Sentence Transformer > Pretrained Models
- Cross Encoder > Usage
- Cross Encoder > Pretrained Models
- Installation
Training
To learn how to finetune these multimodal models on your own data, see the companion blogpost: Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers.
- Sentence Transformer > Training Overview
- Sentence Transformer > Training Examples
- Cross Encoder > Training Overview
- Cross Encoder > Training Examples
- Sparse Encoder > Training Overview
- Sparse Encoder > Training Examples
Hugging Face Hub
- Sentence Transformers models on the Hub
- Sentence Transformers datasets on the Hub
- v5.4 Integrations Collection
Companion Blogposts
The training companion to this post and adjacent Sentence Transformers guides:
- Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers: the direct training companion to this post, with a Visual Document Retrieval walkthrough.
- Training and Finetuning Embedding Models with Sentence Transformers: the general training guide for text-only bi-encoder embedding models.
- Training and Finetuning Reranker Models with Sentence Transformers: Cross Encoder (reranker) training, applicable to text-only and multimodal rerankers.
- Training and Finetuning Sparse Embedding Models with Sentence Transformers: SPLADE training for sparse retrieval.
- 🪆 Introduction to Matryoshka Embedding Models: variable-size embeddings; also applied to multimodal models in the training companion post.
- Train 400x faster Static Embedding Models with Sentence Transformers: CPU-friendly text embedding models.
- Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval: post-training compression of embedding vectors.
```

---

## 20. Safetensors is Joining the PyTorch Foundation

- 日期: 2026-04-08 00:00
- 链接: https://huggingface.co/blog/safetensors-joins-pytorch-foundation

```
Safetensors is Joining the PyTorch Foundation
How we got here
Safetensors started as a Hugging Face project born out of a concrete need: a way to store and share model weights that couldn't execute arbitrary code. The pickle-based formats that dominated the ecosystem at the time meant that there was a very real risk you’d be running malicious code. While this was an acceptable risk when ML was still budding, it would become unacceptable as open model sharing became central to how the ML community works.
The format we built is intentionally simple: a JSON header with a hard limit of 100MB, describing tensor metadata, followed by raw tensor data. Zero-copy loading that maps tensors directly from disk. Lazy loading so you can read individual weights without deserializing an entire checkpoint.
What we didn't fully anticipate was how broadly it would be adopted. Today, Safetensors is the default format for model distribution across the Hugging Face Hub and others, used by tens of thousands of models across all modalities in ML. It has become the preferred way for the open source ML community to share models.
Why the PyTorch Foundation
We want Safetensors to truly belong to the community. The project has always been open source, but code contributions are just one part of its evolution. By bringing more companies and contributors into the governance of the project, we make sure that progress reflects the breadth of the community building on top of it. Joining the PyTorch Foundation means Safetensors now has a vendor-neutral home. The trademark, the repository, and the governance of the project sit with the Linux Foundation rather than any single company. Hugging Face's two core maintainers, Luc and Daniel, remain on the Technical Steering Committee and continue to lead the project day-to-day, but Safetensors now formally belongs to the community that depends on it.
We believe safety is best guaranteed when every contributor can build on what already exists; a principle now embedded in the project's governance itself.
What this means for users and contributors
For the vast majority of users, nothing changes. The format is the same, the APIs are the same, the Hub integration is the same: no breaking changes. Models stored in Safetensors format today will continue to work exactly as they do now.
For contributors, the path to becoming a maintainer is now formally documented and open to anyone in the community. The project's governance lives in GOVERNANCE.md and MAINTAINERS.md in the repository. For organizations building on top of Safetensors, neutral governance under the Linux Foundation provides a stable, long-term foundation, entirely community-driven.
What comes next
Safetensors is a well-established project, adopted by the ecosystem at large, but we're still convinced we're at the very beginning of the project.
We're working with the PyTorch team so that Safetensors may be used within PyTorch core as a serialization system for torch models.
The coming months will see significant growth, and we couldn't think of a better home for that next chapter than the PyTorch Foundation. The roadmap ahead includes device-aware loading and saving, so tensors can load directly onto CUDA, ROCm, and other accelerators without unnecessary CPU staging.
We're also building first-class APIs for Tensor Parallel and Pipeline Parallel loading, so each rank or pipeline stage loads only the weights it needs. And as the ecosystem's quantization landscape continues to evolve, we'll be formalizing support for FP8, block-quantized formats like GPTQ and AWQ, and sub-byte integer types.
These are problems the whole ecosystem has a stake in solving, and being inside the PyTorch Foundation means we can work on them in collaboration with the other hosted projects rather than in parallel.
Get involved
Safetensors is open source and contributions are welcome at every level, from bug reports and documentation to new features and participation in governance.
- GitHub: github.com/huggingface/safetensors
- Documentation: huggingface.co/docs/safetensors
- PyTorch Foundation: pytorch.org/foundation
If you're a developer, researcher, or organization that builds on Safetensors and want to be more involved in shaping its direction, open an issue, start a discussion, or reach out to the maintainers directly. The project has always belonged to the community that uses it. The governance now reflects that too.
```

---

## 21. Welcome Gemma 4: Frontier multimodal intelligence on device

- 日期: 2026-04-02 00:00
- 链接: https://huggingface.co/blog/gemma4

```
Welcome Gemma 4: Frontier multimodal intelligence on device
These models are the real deal: truly open with Apache 2 licenses, high quality with pareto frontier arena scores, multimodal including audio, and sizes you can use everywhere including on-device. Gemma 4 builds on advances from previous families and makes them click together. In our tests with pre-release checkpoints we have been impressed by their capabilities, to the extent that we struggled to find good fine-tuning examples because they are so good out of the box.
We collaborated with Google and the community to make them available everywhere: transformers, llama.cpp, MLX, WebGPU, Rust; you name it. This blog post will show you how to build with your favorite tools so let us know what you think!
Table of Contents
- What is New with Gemma 4?
- Overview of Capabilities and Architecture
- Multimodal Capabilities
- Deploy Anywhere
- Multi-Token Prediction Drafters
- Fine-tuning & Demos
- Try Gemma 4
- Benchmark Results
- Acknowledgements
What is new with Gemma 4?
Similar to Gemma-3n, Gemma 4 supports image, text, and audio inputs, and generates text responses. The text decoder is based on the Gemma model with support for long context windows. The image encoder is similar to the one from Gemma 3 but with two crucial improvements: variable aspect ratios, and configurable number of image token inputs to find your sweet spot between speed, memory, and quality. All models support images (or video) and text inputs, while the small variants (E2B and E4B) support audio as well.
Gemma 4 comes in four sizes, all base and instruction fine-tuned:
Overview of Capabilities and Architecture
Gemma 4 leverages several architecture components used in previous Gemma versions and other open models, and leaves out complex or inconclusive features such as Altup. The combination is a mix designed to be highly compatible across libraries and devices, that can efficiently support long context and agentic use cases, whilst being ideal for quantization.
As shown in the benchmarks above, this feature mix (combined with the training data and recipe) enables the 31B dense model to achieve an estimated LMArena score (text only) of 1452, while the 26B MoE reaches 1441 with just 4B active parameters 🤯. As we'll see, multimodal operation is comparatively as good as text generation, at least in informal and subjective tests.
These are the main architecture characteristics in Gemma 4:
- Alternating local sliding-window and global full-context attention layers. Smaller dense models use sliding windows of 512 tokens while larger models use 1024 tokens.
- Dual RoPE configurations: standard RoPE for sliding layers, pruned RoPE for global layers, to enable longer context.
- Per-Layer Embeddings (PLE): a second embedding table that feeds a small residual signal into every decoder layer.
- Shared KV Cache: the last N layers of the model reuse key-value states from earlier layers, eliminating redundant KV projections.
- Vision encoder: uses learned 2D positions and multidimensional RoPE. Preserves the original aspect ratios and can encode images to a few different token budgets (70, 140, 280, 560, 1120).
- Audio encoder: USM-style conformer with the same base architecture as the one in Gemma-3n.
Per-Layer Embeddings (PLE)
One of the most distinctive features in smaller Gemma 4 models is Per-Layer Embeddings (PLE), which was introduced previously in Gemma-3n. In a standard transformer, each token gets a single embedding vector at input, and the same initial representation is what the residual stream builds on across all layers, forcing the embedding to frontload everything the model might need. PLE adds a parallel, lower-dimensional conditioning pathway alongside the main residual stream. For each token, it produces a small dedicated vector for every layer by combining two signals: a token-identity component (from an embedding lookup) and a context-aware component (from a learned projection of the main embeddings). Each decoder layer then uses its corresponding vector to modulate the hidden states via a lightweight residual block after attention and feed-forward. This gives each layer its own channel to receive token-specific information only when it becomes relevant, rather than requiring everything to be packed into a single upfront embedding. Because the PLE dimension is much smaller than the main hidden size, this adds meaningful per-layer specialization at modest parameter cost. For multimodal inputs (images, audio, video), PLE is computed before soft tokens are merged into the embedding sequence — since PLE relies on token IDs that are lost once multimodal features replace the placeholders. Multimodal positions use the pad token ID, effectively receiving neutral per-layer signals.
Shared KV Cache
The shared KV cache is an efficiency optimization that reduces both compute and memory during inference. The last num_kv_shared_layers
layers of the model don't compute their own key and value projections. Instead, they reuse the K and V tensors from the last non-shared layer of the same attention type (sliding or full).
In practice, this has a minimal impact on quality while being much more efficient (in terms of both memory and compute) for long context generation and on-device use.
Multimodal Capabilities
We saw in our tests that Gemma 4 supports comprehensive multimodal capabilities out of the box. We don't know what was the training mix, but we had success using it for tasks such as OCR, speech-to-text, object detection, or pointing. It also supports text-only and multimodal function calling, reasoning, code completion and correction.
Here, we show a few inference examples across different model sizes. You can run them conveniently with this notebook. We encourage you to try the demos and share them below this blog!
Object Detection and Pointing
GUI detection
We test Gemma 4 on GUI element detection and pointing across different sizes, with the following image and text prompt: "What's the bounding box for the "view recipe" element in the image?"
With this prompt, the model natively responds in JSON format with the detected bounding boxes - no need for specific instructions or grammar-constrained generation. We found the coordinates refer to an image size of 1000x1000, relative to the input dimensions.
We visualize the outputs below for your convenience. We parse the bounding boxes from the returned JSON: json\n[\n {"box_2d": [171, 75, 245, 308], "label": "view recipe element"}\n]\n
Object Detection
We test models to detect everyday objects, here we ask them to detect the bike and compare different model outputs. As in the previous case, we parse the bounding box from the json and translate to image space coordinates.
Multimodal Thinking and Function Calling
We asked Gemma 4 to write HTML code to reconstruct a page we made with Gemini 3. Below you can find the code to do this, we enable thinking and ask each model to generate up to 4000 new tokens, to make it foolproof.
Inference code
messages = [
{
"role": "user",
"content": [
{
"type": "image",
"image": "https://huggingface.co/datasets/merve/vlm_test_images/resolve/main/landing_page.png",
},
{"type": "text", "text": "Write HTML code for this page."},
],
}
]
inputs = processor.apply_chat_template(
messages,
tokenize=True,
return_dict=True,
return_tensors="pt",
add_generation_prompt=True,
enable_thinking=True,
).to(model.device)
output = model.generate(**inputs, max_new_tokens=4000)
input_len = inputs.input_ids.shape[-1]
generated_text_ids = output[0][input_len:]
generated_text = processor.decode(generated_text_ids, skip_special_tokens=True)
result = processor.parse_response(generated_text)
print(result["content"])
Video Understanding
Smaller Gemma 4 models can take in videos with audio while larger ones can take in videos without audio. While the models are not explicitly post-trained on videos, they can understand videos both with and without audio. The model is particularly strong in audios
Inference code
messages = [
{
"role": "user",
"content": [
{"type": "video", "url": "https://huggingface.co/datasets/merve/vlm_test_images/resolve/main/concert.mp4"},
{"type": "text", "text": "What is happening in the video? What is the song about?"},
],
},
]
inputs = processor.apply_chat_template(
messages,
tokenize=True,
return_dict=True,
return_tensors="pt",
add_generation_prompt=True,
load_audio_from_video=True, # disable this for larger models
).to(model.device)
output = model.generate(**inputs, max_new_tokens=200)
input_len = inputs.input_ids.shape[-1]
generated_text_ids = output[0][input_len:]
generated_text = processor.decode(generated_text_ids, skip_special_tokens=True)
print(result["content"])
Captioning
We have tested all models on captioning. All checkpoints perform very well and accurately capture nuance in complex scenerios. Here's the image we use, with the prompt "Write single detailed caption for this image.".
Inference code
messages = [
{
"role": "user",
"content": [
{"type": "image", "url": "https://huggingface.co/datasets/merve/vlm_test_images/resolve/main/bird.png"},
{"type": "text", "text": "Write single detailed caption for this image."},
],
},
]
inputs = processor.apply_chat_template(
messages,
tokenize=True,
return_dict=True,
return_tensors="pt",
add_generation_prompt=True,
).to(model.device)
output = model.generate(**inputs, max_new_tokens=512)
input_len = inputs.input_ids.shape[-1]
generated_text_ids = output[0][input_len:]
generated_text = processor.decode(generated_text_ids, skip_special_tokens=True)
result = processor.parse_response(generated_text)
print(result["content"])
Audio Question Answering
These models are trained to answer questions about speech in audio. Music and non-speech sounds were not part of the training data.
Inference code
messages = [
{
"role": "user",
"content": [
{"type": "audio", "url": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/obama_first_45_secs.mp3"},
{"type": "text", "text": "Can you describe this audio in detail?"},
],
},
]
inputs = processor.apply_chat_template(
messages,
tokenize=True,
return_dict=True,
return_tensors="pt",
add_generation_prompt=True,
).to(model.device)
output = model.generate(
**inputs,
max_new_tokens=1000,
do_sample=False,
)
print(processor.decode(output[0], skip_special_tokens=True))
Here is an example if you want to do transcription:
Inference code
messages = [
{
"role": "user",
"content": [
{"type": "audio", "url": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/obama_first_45_secs.mp3"},
{"type": "text", "text": "Transcribe the audio?"},
],
},
]
inputs = processor.apply_chat_template(
messages,
tokenize=True,
return_dict=True,
return_tensors="pt",
add_generation_prompt=True,
).to(model.device)
output = model.generate(
**inputs,
max_new_tokens=1000,
do_sample=False,
)
print(processor.decode(output[0], skip_special_tokens=True))
Multimodal Function Calling
We test the model by asking to get the weather in the place shown in the image.
Inference code
import re
WEATHER_TOOL = {
"type": "function",
"function": {
"name": "get_weather",
"description": "Gets the current weather for a specific location.",
"parameters": {
"type": "object",
"properties": {
"city": {"type": "string", "description": "The city name"},
},
"required": ["city"],
},
},
}
tools = [WEATHER_TOOL]
messages = [
{"role": "user", "content": [
{"type": "text", "text": "What is the city in this image? Check the weather there right now."},
{"type": "image", "image": "https://huggingface.co/datasets/merve/vlm_test_images/resolve/main/thailand.jpg"},
]},
]
inputs = processor.apply_chat_template(
messages,
tools=[WEATHER_TOOL],
tokenize=True,
return_dict=True,
return_tensors="pt",
add_generation_prompt=True,
enable_thinking=True,
).to(model.device)
output = model.generate(**inputs, max_new_tokens=1000)
input_len = inputs.input_ids.shape[-1]
generated_text_ids = output[0][input_len:]
generated_text = processor.decode(generated_text_ids, skip_special_tokens=True)
result = processor.parse_response(generated_text)
print(result["content"])
Deploy Anywhere
Gemma 4 comes with day-0 support for many open-source inference engines, and is ideal for tool calling and agents! We also release ONNX checkpoints that can run on many hardware backends, allowing use cases on edge devices or in browser!
transformers
Gemma 4 comes with first-class transformers support from the get-go 🤗. This integration allows using the model with other libraries like bitsandbytes, PEFT and TRL. Make sure to install the latest version of transformers.
pip install -U transformers
The easiest way to infer with the small Gemma 4 models is through the any-to-any
pipeline. You can initialize it as follows.
from transformers import pipeline
pipe = pipeline("any-to-any", model="google/gemma-4-e2b-it")
You can then pass in images and text as follows.
messages = [
{
"role": "user",
"content": [
{
"type": "image",
"image": "https://huggingface.co/datasets/merve/vlm_test_images/resolve/main/thailand.jpg",
},
{"type": "text", "text": "Do you have travel advice going to here?"},
],
}
]
output = pipe(messages, max_new_tokens=100, return_full_text=False)
output[0]["generated_text"]
# Based on the image, which appears to show a magnificent, ornate **Buddhist temple or pagoda**, likely in Southeast Asia (such as Thailand, Myanmar, or Cambodia), here is some general travel advice..
When inferring with videos, you can include the audio track using the load_audio_from_video
argument.
messages = [
{
"role": "user",
"content": [
{
"type": "video",
"image": "https://huggingface.co/datasets/merve/vlm_test_images/resolve/main/rockets.mp4",
},
{"type": "text", "text": "What is happening in this video?"},
],
}
]
pipe(messages, load_audio_from_video=True)
Going a level lower, you can load Gemma 4 using the AutoModelForMultimodalLM
class, especially useful for fine-tuning. The built-in chat template takes care of formatting the inputs correctly, please make sure you use it to prevent subtle mistakes when building the prompt manually.
Inference code
from transformers import AutoModelForMultimodalLM, AutoProcessor
model = AutoModelForMultimodalLM.from_pretrained("google/gemma-4-E2B-it", device_map="auto")
processor = AutoProcessor.from_pretrained("google/gemma-4-E2B-it")
messages = [
{
"role": "user",
"content": [
{
"type": "video",
"image": "https://huggingface.co/datasets/merve/vlm_test_images/resolve/main/rockets.mp4",
},
{"type": "text", "text": "What is happening in this video?"},
],
}
]
inputs = processor.apply_chat_template(
messages,
tokenize=True,
add_generation_prompt=True,
return_dict=True,
return_tensors="pt"
).to(model.device)
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
Llama.cpp
Gemma 4 models come with image+text support in llama.cpp from the get-go! This unlocks using Gemma 4 with all of your favorite local apps: llama-cpp server, lmstudio, Jan as well as coding agents like Pi across many backends such as Metal and CUDA.
You can install llama-cpp as follows.
brew install llama.cpp # MacOS
winget install llama.cpp # Windows
You can then start a server compatible with the OpenAI API Replace the quantization scheme at the end of the command with the precision of your choice.
llama-server -hf ggml-org/gemma-4-E2B-it-GGUF
Check out this link for more options on combining llama.cpp with different coding agents and local apps. Find all the GGUF checkpoints in this collection.
Plug in your local agent
We worked on making sure the new models work locally with agents like openclaw, hermes, pi, and open code. All thanks to llama.cpp! Run the following to try Gemma 4 right away.
First, start your local server:
llama-server -hf ggml-org/gemma-4-26b-a4b-it-GGUF:Q4_K_M
For hermes:
hermes model
For openclaw:
openclaw onboard
For pi define a ~/.pi/agent/models.json
:
{
"providers": {
"llama-cpp": {
"baseUrl": "http://localhost:8080/v1",
"api": "openai-completions",
"apiKey": "none",
"models": [
{
"id": "ggml-org-gemma-4-26b-4b-gguf"
}
]
}
}
}
For open code define a ~/.config/opencode/opencode.json
:
{
"$schema": "https://opencode.ai/config.json",
"provider": {
"llama.cpp": {
"npm": "@ai-sdk/openai-compatible",
"name": "llama-server (local)",
"options": {
"baseURL": "http://127.0.0.1:8080/v1"
},
"models": {
"gemma-4-26b-4b-it": {
"name": "Gemma 4 (local)",
"limit": {
"context": 128000,
"output": 8192
}
}
}
}
}
}
transformers.js
transformers.js enables running Gemma 4 right inside browser. You can check out the model card to see text-only, image & text, audio & text inference in detail here. We also shipped a demo for you to test the model here.
MLX
Full multimodal support of Gemma 4 is available using the open-source mlx-vlm
library. Here's how to ask the model to describe an image:
pip install -U mlx-vlm
mlx_vlm.generate \
--model google/gemma-4-E4B-it \
--image https://huggingface.co/datasets/huggingface/documentation-images/resolve/0052a70beed5bf71b92610a43a52df6d286cd5f3/diffusers/rabbit.jpg \
--prompt "Describe this image in detail"
mlx-vlm supports TurboQuant, which delivers the same accuracy as the uncompressed baseline while using ~4x less active memory and running a lot faster end-to-end. This makes long-context inference practical on Apple Silicon without sacrificing quality. Use it like this:
mlx_vlm.generate \
--model "mlx-community/gemma-4-26b-a4b-it-4bit" \
--prompt "Your prompt here" \
--kv-bits 3.5 \
--kv-quant-scheme turboquant
For audio examples and more details, please check the MLX collection.
Mistral.rs
mistral.rs is a Rust-native inference engine with day-0 Gemma 4 support across all modalities (text, image, video, audio) and builtin tool-calling and agentic functionality. Install mistral.rs:
curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/EricLBuehler/mistral.rs/master/install.sh | sh # Linux/macOS
irm https://raw.githubusercontent.com/EricLBuehler/mistral.rs/master/install.ps1 | iex # Windows
You can then start an OpenAI-compatible HTTP server:
mistralrs serve mistralrs-community/gemma-4-E4B-it-UQFF --from-uqff 8
Or, use interactive mode:
mistralrs run -m google/gemma-4-E4B-it --isq 8 --image image.png -i "Describe this image in detail."
mistralrs run -m google/gemma-4-E4B-it --isq 8 --audio audio.mp3 -i "Transcribe this fully."
Find all models here. Please, follow the instructions in the model cards for installation and inference guidelines.
Multi-Token Prediction Drafters
Google has released Multi-Token Prediction (MTP) drafters for the Gemma 4 family: small assistant models that accelerate inference via speculative decoding. The drafter proposes several future tokens at once, and the target model verifies them in a single forward pass. You get the same outputs as the target model, just faster — no quality loss, no changes to reasoning behaviour. Reported end-to-end speedups go up to ~3x depending on hardware, batch size, and workload.
Assistants are available for all four Gemma 4 sizes (E2B, E4B, 26B A4B, 31B). They share the KV cache with the target model to avoid recomputing context, and the smaller edge variants additionally use an embedder clustering trick to keep memory and compute low on-device.
Find the checkpoints in the Gemma 4 collection and the mlx-community collection.
Fine-tuning for all
Gemma 4 models are ideal for fine-tuning in your favorite tools and platforms and at any budget.
Fine-tuning with TRL
Gemma 4 is fully supported for fine-tuning with TRL. To celebrate, TRL has been upgraded with support for multimodal tool responses when interacting with environments, meaning models can now receive images back from tools during training, not just text.
To showcase this, we've built an example training script where Gemma 4 learns to drive in the CARLA simulator. The model sees the road through a camera, decides what to do and learns from the outcome. After training, it consistently changes lanes to avoid pedestrians. The same approach works for any task where a model needs to see and act: robotics, web browsing, or other interactive environments.
Get started:
# pip install git+https://github.com/huggingface/trl.git
python examples/scripts/openenv/carla_vlm_gemma.py \
--env-urls https://sergiopaniego-carla-env.hf.space \
https://sergiopaniego-carla-env-2.hf.space \
--model google/gemma-4-E2B-it
Find the example here.
Fine-tuning with TRL on Vertex AI
Additionally, we have prepared an example on how to fine-tune Gemma 4 with TRL on Vertex AI using SFT, to showcase how to extend the function calling capabilities, whilst freezing both the vision and audio towers. The examples include how to build a custom Docker container with latest Transformers, TRL, etc. with CUDA support on Google Cloud, and how to run it via Vertex AI Serverless Training Jobs.
# pip install google-cloud-aiplatform --upgrade --quiet
from google.cloud import aiplatform
aiplatform.init(
project="<PROJECT_ID>",
location="<LOCATION>",
staging_bucket="<BUCKET_URI>",
)
job = aiplatform.CustomContainerTrainingJob(
display_name="gemma-4-fine-tuning",
container_uri="<CONTAINER_URI>",
command=["python", "/gcs/gemma-4-fine-tuning/train.py"],
)
job = job.submit(
replica_count=1,
machine_type="a3-highgpu-1g",
accelerator_type="NVIDIA_H100_80GB",
accelerator_count=1,
base_output_dir="<BUCKET_URI>/output-dir",
environment_variables={
"MODEL_ID": "google/gemma-4-E2B-it",
"HF_TOKEN": <HF_TOKEN>,
},
boot_disk_size_gb=500,
)
You can find the complete example in the "Hugging Face on Google Cloud" docs at https://hf.co/docs/google-cloud/examples/vertex-ai-notebooks-fine-tune-gemma-4.
Fine-tuning with Unsloth Studio
If you want to fine tune and run a Gemma 4 model in a UI, try out Unsloth Studio. It runs locally or on Google Colab. First, install and start the app:
# install unsloth studio on MacOS, Linux, WSL
curl -fsSL https://unsloth.ai/install.sh | sh
# install unsloth studio on Windows
irm https://unsloth.ai/install.ps1 | iex
# launch unsloth studio
unsloth studio -H 0.0.0.0 -p 8888
# Search for for a Gemma 4 model like google/gemma-4-E2B-it
Then select any of the Gemma 4 models from the hub.
Try Gemma 4
We have shipped demos for you to try different Gemma 4 models. We include demos based on transformers implementation for E4B, 26B/A4B, and dense 31B models, as well as a WebGPU demo with transformers.js 🚀
Benchmark Results
Gemma 4 models demonstrate exceptional performance across diverse benchmarks, from reasoning and coding to vision and long-context tasks. The graph below shows model performance vs size, with Gemma 4 models forming an impressive Pareto frontier:
Source: Google (blog.google)
Here are detailed benchmark results for the instruction-tuned models:
Acknowledgements
Landing Gemma-4 in the open-source ecosystem took a lot of effort from many people and not only the authors of this blog post. In no particular order, we thank many people from the open-source team: Gemma 4 transformers integration is owed to Cyril, Raushan, Eustache, Arthur, Lysandre. We thank Joshua for transformers.js integration and demo, Eric for mistral.rs integration, Son for Llama.cpp, Prince for MLX integration, Quentin, Albert and Kashif for TRL, Adarsh for SGLang transformers backend and Toshihiro for building the demos. This work wouldn't have been possible without Google's extensive contribution with the model artefact, but also the significant effort contributing the model to transformers in an effort to standardize it. The open-source ecosystem is now more complete, with a very capable, freely-licensed, open-source model. The Gemma 4 transformers integration was handled by Cyril, Raushan, Eustache, Arthur, Lysandre. We thank Joshua for the transformers.js integration and demo, Eric for mistral.rs integration, Son for Llama.cpp, Prince for MLX, Quentin for TRL, Adarsh for SGLang transformers backend, and Toshihiro for building several demos.
This work wouldn't have been possible without Google's extensive contribution with the model artefact, but also their significant effort contributing the model to transformers in an effort to standardize it. The open-source ecosystem is now more complete, with a very capable, freely-licensed, open-source model.
```

---

## 22. Falcon Perception

- 日期: 2026-04-01 07:13
- 链接: https://huggingface.co/blog/tiiuae/falcon-perception

```
Falcon Perception
TL;DR — Falcon Perception is a 0.6B-parameter early-fusion Transformer for open-vocabulary grounding and segmentation from natural language prompts. The model processes image patches + text in one sequence using a hybrid attention mask, and produces variable numbers of instances with a small, structured token interface and lightweight output heads. On SA-Co, Falcon Perception reaches 68.0 Macro-F1 (vs. 62.3 for SAM 3) with the main remaining gap being presence calibration (MCC 0.64 vs. 0.82). We also introduce PBench, a diagnostic benchmark that breaks down performance by capability (attributes, OCR-guided disambiguation, spatial constraints, relations) and by dense long-context crowded scenes.
We also relase Falcon OCR, a 0.3B-parameter model which reaches a score of 80.3 and 88.6 on the olmOCR benchmark and OmniDocBench respectively, while having the highest throughput of any open source OCR model.
This post is a brief, practical write-up of what we built, why we built it this way, and what we learned along the way.
The problem: why do perception systems end up as pipelines?
Many open-vocabulary perception systems are built as modular pipelines: a (often frozen) vision backbone extracts features, a separate fusion/decoder stage combines them with language, and additional components handle matching and post-processing. This family of designs works well in many settings, but it comes with trade-offs: it can be hard to scale cleanly, hard to attribute improvements to the right component, and easy to accumulate complexity as we add a new fix for each failure mode.
We asked a simpler question: can a single early-fusion Transformer backbone handle both perception and language modeling, if we choose the right attention pattern, output interface, and training signal?
In our experiments, the answer is largely yes. The rest of this post describes the main design choices and the evidence behind them.
The architecture: early fusion, hybrid attention, and an efficient dense interface
A single autoregressive Transformer processes a unified sequence of image patches, text, and task tokens.
The model predicts object properties in a fixed order: <coord>
→ <size>
→ <seg>
.
Bounding box coordinates and sizes are decoded via specialized heads and re-injected as Fourier features.
High-resolution segmentation masks are generated by a dot product between the <seg>
token and upsampled image features.
One Backbone, Two Behaviors
At its core, Falcon Perception is a dense Transformer that processes image patches and text tokens in a shared parameter space from the first layer. Instead of a separate vision backbone followed by a late-fusion decoder, we keep a single backbone and rely on masking and a lightweight output interface to make the dense prediction problem tractable.
Images and text have different structure: pixels are 2D and benefit from bidirectional context, while the prediction interface is naturally sequential. We address this with a hybrid attention mask:
- Image tokens attend to all other image tokens bidirectionally, building a global visual context (like a vision encoder would).
- Text and task tokens attend causally to everything before them — the full visual prefix plus preceding text.
This allows the same backbone to behave like a bidirectional visual encoder on image tokens, while still supporting autoregressive prediction over task tokens.
Chain-of-Perception: coarse-to-fine supervision for dense outputs
Dense perception is not a fixed-size prediction problem: an image may contain zero instances or hundreds. Autoregressive generation gives a clean variable-length interface, but fully autoregressive dense generation (e.g., polygons or high-resolution masks token-by-token) quickly becomes expensive.
We use a small structured interface, Chain-of-Perception, which decomposes each instance into three steps:
<coord> → <size> → <seg>
- Coordinate token: The model first predicts the center of the instance — resolving which object it's talking about.
- Size token: Then the spatial extent — resolving how big it is.
- Segmentation token: Finally, a single embedding that, when dot-producted with upsampled image features, produces a full-resolution binary mask.
This ordering is deliberate. Committing to geometry first reduces ambiguity (“which instance?”), and makes the mask prediction step closer to pixel refinement conditioned on the resolved object.
Specialized Heads, Minimal Overhead
The backbone is shared, while decoding uses lightweight heads tailored to the output type:
Coordinate & Size Heads use Fourier feature encoding : mapping continuous coordinates through a random Gaussian projection into a high-dimensional sinusoidal space. This overcomes the spectral bias of neural networks, yielding more precise localization than discrete binning alone. Decoded coordinates are re-injected into the sequence as conditioning for subsequent tokens.
Segmentation Head computes a dot product between the
<seg>
token’s hidden state and content-aware upsampled image features. Because the<seg>
token is produced after geometry and has access to early-fused visual context, we can avoid the separate mask-query machinery and Hungarian matching that often appears in decoder-based instance segmentation training.
PBench: a benchmark designed to isolate what is missing
Existing referring-expression benchmarks like RefCOCO are saturated — models routinely hit 90%+ — and they conflate what went wrong. Did the model fail because it can't read text? Can't understand spatial relationships? Can't handle a crowd?
We introduce PBench, a diagnostic benchmark that separates samples by the dominant capability required:
Each sample targets one dominant capability: OCR prompts avoid spatial qualifiers, and spatial prompts avoid in-image text disambiguators. This yields a capability profile rather than a single opaque score, and makes it easier to decide where to invest next (data, training curriculum, or post-training).
Training: distillation, large-scale data, and a three-stage recipe
Multi-Teacher Distillation
Rather than training from random weights (which in our ablations was unstable for segmentation), Falcon Perception initializes via multi-teacher distillation. Two strong vision teachers contribute complementary signals:
- DINOv3 (ViT-H): strong local features critical for segmentation
- SigLIP2: language-aligned features for open-vocabulary understanding
The distilled initialization achieves 74.25% zero-shot accuracy on ImageNet-1k and 85.11% linear-probe mIoU on Pascal VOC, providing a strong visual foundation before perception-specific training.
Data: 54M Images, 195M Positive Expressions, 488M Hard Negatives
We build the training set through a multi-stage pipeline:
- Hierarchical clustering of web-scraped images via DINOv3 embeddings to ensure uniform concept coverage.
- VLM-driven listing generates dense object descriptions per image, categorized by PBench complexity level (60% basic, 40% advanced).
- Negative mining produces semantic, visual, and fine-grained hard negatives to combat hallucination.
- Ensemble consensus — SAM 3, Qwen3-VL-30B, and Moondream3 must agree (IoU > 0.8) for automatic acceptance.
- Human verification — disagreements go to annotators, recovering hard samples that confuse automated systems.
We maintain a strict 1:1 ratio of positive to negative samples. This makes presence calibration a first-class target: the model should reliably say “absent,” not only draw masks when confident.
The Three Stages (700 GT Total)
Stage 1 — In-Context Listing (450 GT): The model learns to autoregressively list scene inventories — predicting text expressions and their locations. Full causal attention between queries enables learning of object co-occurrence ("fork, then knife, then plate"). This builds broad scene understanding.
Stage 2 — Task Alignment (225 GT): The attention mask is modified so queries can no longer see each other, simulating independent queries at inference time. Loss on text tokens is masked, focusing gradient signal entirely on presence classification and localization. This stage transitions from "scene understanding" to "answer this specific question."
Stage 3 — Long-Context Finetuning (10 GT): A short phase with the mask limit raised to 600 per expression and a minimal constant learning rate. This adapts the model for extreme crowd density without forgetting earlier capabilities.
Key design choices validated through ablations:
- Muon optimizer for the specialized heads (vs. AdamW) — yields +4.8 points on SA-Co detection
- Raster ordering of instances (vs. random/size) — +10 points over random ordering on SA-Co
- Gram feature regularization — prevents drift from the distillation features, improving segmentation by +1.5 points
- Global loss normalization across ranks — corrects bias from variable-length packed sequences in FSDP
Results
SA-Co: Best-in-Class Mask Quality
On the SA-Co open-vocabulary segmentation benchmark, Falcon Perception (0.6B parameters) achieves 68.0 Macro-F1, compared to 62.3 for SAM 3, with large gains on attribute-heavy (+8.2), food & drink (+12.2), and sports equipment (+4.0) splits. At the same time, Falcon Perception lags SAM 3 on presence calibration (MCC: 0.64 vs 0.82), which is the clearest remaining improvement axis.
Here's an example output — the prompt "Falcon" produces precise instance masks:
Falcon Perception also performs well for reffering expressions, able to correctly segment the burger with a black bun in each frame of the video:
PBench: Scaling with Prompt Complexity
This is where the early-fusion design shows the largest differences:
On simple objects, the gap is modest. As prompts become more compositional—requiring OCR-guided disambiguation, spatial constraints, or relational binding—the gap widens.
In our PBench Dense split, Falcon Perception (0.6B) substantially outperforms generalist VLM baselines (e.g., 72.6 vs 8.9 for Qwen3-VL-30B in our evaluation setup), and matches or exceeds the 8B model on spatial and relational tiers.
Qualitative Results: OCR, Spatial, Relational, and Dense
As prompts grow more compositional — requiring OCR-guided disambiguation, spatial constraints, relational binding, or scaling to hundreds of instances — the early-fusion advantage becomes visually clear:
- OCR-Guided Grounding (Level 2): When the distinguishing signal is text written on an object, Falcon Perception reads it correctly while SAM 3 cannot differentiate.
- Spatial Understanding (Level 3): When prompts specify spatial relationships, Falcon Perception forms a coherent 2D scene map.
- Relational Reasoning (Level 4): When the target is defined through interactions rather than appearance, Falcon Perception understands the scene graph.
- Dense Scenes: Scaling to Hundreds of Instances: The autoregressive interface is particularly useful when scenes are extremely crowded, where fixed-query decoders can run into practical limits.
Level 2 — OCR-Guided Grounding: Falcon Perception reads text on objects to disambiguate; SAM 3 cannot.
"168 wine bottles": Falcon Perception identifies the bottles labeled "168", while SAM 3 highlights every bottle. "Honolulu direction sign": Falcon reads the text to find the right sign.
Level 3 — Spatial Understanding: Falcon Perception resolves spatial constraints; SAM 3 returns false positives.
"Lower meat skewer on left grill," "black car to the right of red car at bottom," "Belgian flag on the left" — Falcon Perception resolves the correct instance from spatial constraints. SAM 3 predicts false positives for multiple candidates.
Level 4 — Relational Reasoning: Falcon Perception understands interactions; SAM 3 ignores relational constraints.
"Pastry next to brown round bread," "person using phone," "person holding helmet in hand" — Falcon Perception identifies the interacting instance. SAM 3 highlights all instances of the object class, ignoring the relational constraint.
Dense Scenes: Falcon Perception scales to hundreds of instances; SAM 3's decoder runs out of query tokens.
"Snow goose," "pigeon," "colorful canned drinks" — Falcon Perception autoregressively segments hundreds of instances. SAM 3's fixed-size decoder runs out of query tokens beyond ~200 instances.
Falcon OCR: extending early fusion to document understanding
Modern OCR has moved well beyond extracting text from clean scans. Today's systems must handle multi-column layouts, mathematical formulas, tables, charts, and multilingual content — all in one pass. Most competitive OCR VLMs tackle this with a familiar recipe: a vision encoder feeding a separate text decoder, plus task-specific glue. These systems work, but they tend to be large (1B–3B+ parameters).
We took a different path: reuse the same early-fusion dense Transformer from Falcon Perception, but train a smaller 0.3B-parameter variant from scratch specifically for OCR. The result is Falcon OCR — a single backbone that processes image patches and text tokens in a shared parameter space with the same hybrid attention mask (bidirectional for image tokens, causal for text tokens), and switches tasks through prompts rather than additional modules.
We trained from scratch (no multi-teacher distillation) because the visual features OCR needs — fine-grained glyph recognition, stroke-level discrimination — differ substantially from the object-level features useful for segmentation. Starting fresh lets the backbone develop text-optimized representations from the ground up.
Training
We train on a curated English-language mixture spanning three core tasks: general document text parsing (digital PDFs, old scans, typewritten documents), mathematical and scientific formula recognition, and table structure recognition. The mixture also includes handwriting, real-world scene text, and synthetic samples generated from rendered LaTeX and HTML sources. The training objective is pure next-token prediction on structured text outputs.
Training proceeds in two phases: a long pre-training phase at constant learning rate where the model learns core OCR capabilities across all element types, followed by a short cosine-decay finetuning phase where the learning rate is annealed to near zero.
Benchmark results
We evaluate on olmOCR (binary correctness checks across diverse inputs) and OmniDocBench (continuous metrics over full-page parses). All comparison models are significantly larger and/or use proprietary infrastructure. At 80.3% on olmOCR with only 0.3B parameters, Falcon OCR is within 1.7 points of the top system and leads all models on Multi-Column (87.1%) and Tables (90.3%). On OmniDocBench it scores 88.64 overall, ahead of DeepSeek OCR v2, GPT 5.2, and Mistral OCR 3.
Serving throughput
At 0.3B parameters, Falcon OCR is roughly 3x smaller than 0.9B-class OCR VLMs, which translates directly into higher serving throughput. Measured on a single A100-80GB with vLLM at high concurrency:
The compact footprint and vLLM integration (continuous batching, PagedAttention, optimized CUDA kernels) make it practical for large-scale document digitization where millions of pages need processing.
What we see in the results
More broadly, these results suggest that the early-fusion single-stack Transformer is a viable alternative to the "vision encoder plus text decoder" recipe for OCR. One backbone, shared parameter space, one decoding interface, and better data and training signals rather than increasingly complex pipelines. We hope this encourages more work in this direction.
Qualitative examples
Falcon OCR processes images captured under challenging real-world conditions with varying lighting, diverse text semantics (mathematical formulae, structured tables, handwritten notes), and complex document layouts, to produce structured text output.
Click each category below to expand.
Handwriting and Real-world Images: Accurate transcription of handwritten text and in-the-wild captures under adverse conditions.
Falcon OCR extracts text from handwritten documents and real-world photographs with variable lighting, orientation, and content complexity.
Table Extraction: Faithful reproduction of tabular structure and cell content across diverse formats.
Falcon OCR accurately reproduces cell entries and structural layout from tables of varying formats and complexity.
Mathematical Formulae: Accurate recognition of equations across varying levels of symbolic complexity.
Falcon OCR correctly transcribes mathematical expressions ranging from simple equations to multi-line derivations with nested operators.
Complex Document Layouts: Faithful text extraction from multi-column, mixed-content documents.
Falcon OCR preserves reading order and structural fidelity when extracting text from documents with multi-column layouts, figures, and footnotes.
Inference: Fast, Practical, and Open
The release includes an inference stack built on PyTorch’s FlexAttention, which makes it practical to express the custom attention patterns and efficiently serve packed variable-length sequences.
Paged Inference Engine
- Paged KV cache with virtual page tables (no wasted memory from padding)
- Continuous batching: new sequences enter mid-generation, finished ones release pages immediately
- CUDA graph capture for the decode loop
- Background tokenization overlapped with GPU compute
- HR feature cache: LRU cache with pinned-memory buffers for async GPU-CPU transfer of upsampled image features — subsequent queries on the same image skip the expensive upsampling step
In our setup on an H100, typical latencies are on the order of ~100ms prefill, ~200ms upsampling (0ms if cached), and ~50ms decode for a handful of instances. (These numbers depend on resolution, sequence length, and the number of predicted instances.)
Docker and MLX Integration for Falcon-OCR
For the Falcon-OCR model, we also provide a vLLM docker server for fast deployment and MLX integration for Apple-Silicon
Please check out the github repo for details.
The Bigger Picture: A "Bitter Lesson" for Perception
Falcon Perception is intentionally minimal: one backbone, one objective family, and small heads only where outputs are continuous and dense. The working assumption is that most gains should come from data, compute, and training signals, rather than continually expanding the pipeline with specialized modules.
The architecture doesn't block any obvious scaling path: add more images and harder prompts for better grounding, mix in text-only data for better language, increase context length for denser scenes. It's still just one sequence model.
Falcon Perception is developed by the Falcon Vision Team at the Technology Innovation Institute (TII), Abu Dhabi, UAE.
Citation
If you use Falcon-Perception, please cite
@article{bevli2026falcon,
title = {Falcon Perception},
author = {Bevli, Aviraj and Chaybouti, Sofian and Dahou, Yasser and Hacid, Hakim and Huynh, Ngoc Dung and Le Khac, Phuc H. and Narayan, Sanath and Para, Wamiq Reyaz and Singh, Ankit},
journal = {arXiv preprint arXiv:2603.27365},
year = {2026},
url = {https://arxiv.org/abs/2603.27365}
}
```

---

## 23. Any Custom Frontend with Gradio's Backend

- 日期: 2026-04-01 00:00
- 链接: https://huggingface.co/blog/introducing-gradio-server

```
gradio.Server: Any Custom Frontend with Gradio's Backend
gr.HTML
: building rich, interactive frontends entirely inside Gradio using custom HTML, CSS, and JavaScript. That unlocked a lot. But what if that's not enough?
What if you want to build with your own frontend framework entirely like React, Svelte, or even plain HTML/JS, while still benefiting from Gradio's queuing system, API infrastructure, MCP support, and ZeroGPU on Spaces?
That's exactly the problem gradio.Server
solves. And it changes what's possible with Gradio and Hugging Face Spaces.
What We Wanted to Build
Text Behind Image : an editor where you upload a photo, the background gets removed using an ML model, and then you place stylized text between the foreground subject and the background. The text appears to sit behind the person or object in the image.
This needs:
- A drag-and-drop canvas with layered rendering (background → text → foreground)
- A rich control panel with sliders for font size, weight, letter spacing, color, opacity, stroke, shadow, 3D extrusion, perspective transforms, and more
- A backend ML endpoint that runs a background-removal model and returns a transparent PNG
- Export to PNG on the client side
There's no way to express this UI in Gradio components. It's a full web application. But We still wanted the backend power of Gradio: queuing, concurrency management, ZeroGPU support, and hosting on HF Spaces without infrastructure headaches.
Enter gradio.Server
gradio.Server
extends FastAPI. It gives you the full power of FastAPI (custom routes, middleware, file uploads, any response type) while adding Gradio's API engine on top: queuing, SSE streaming, concurrency control, and gradio_client
compatibility.
Here's the entire backend for Text Behind Image:
import os
import torch
from PIL import Image
from torchvision import transforms
from transformers import AutoModelForImageSegmentation
from gradio import Server
from gradio.data_classes import FileData
from fastapi.responses import HTMLResponse
import spaces
torch.set_float32_matmul_precision("high")
birefnet = AutoModelForImageSegmentation.from_pretrained(
"ZhengPeng7/BiRefNet", trust_remote_code=True
)
birefnet.to("cuda")
birefnet.float()
transform_image = transforms.Compose([
transforms.Resize((1024, 1024)),
transforms.ToTensor(),
transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])
app = Server()
@spaces.GPU
def segment(image: Image.Image) -> Image.Image:
"""Run BiRefNet segmentation to produce a transparency mask."""
image_size = image.size
input_images = transform_image(image).unsqueeze(0).to("cuda")
with torch.no_grad():
preds = birefnet(input_images)[-1].sigmoid().cpu()
pred = preds[0].squeeze()
mask = transforms.ToPILImage()(pred).resize(image_size)
image.putalpha(mask)
return image
@app.api(name="remove_background")
def remove_background(image_path: FileData) -> FileData:
"""Remove background from an image. Returns transparent PNG."""
im = Image.open(image_path["path"]).convert("RGB")
result = segment(im)
out_path = image_path["path"].rsplit(".", 1)[0] + ".png"
result.save(out_path)
return FileData(path=out_path)
@app.get("/", response_class=HTMLResponse)
async def homepage():
html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
with open(html_path, "r", encoding="utf-8") as f:
return f.read()
app.launch(show_error=True)
That's it. ~50 lines of Python. The model loads at startup, @spaces.GPU
handles ZeroGPU allocation, and gradio.Server
manages queuing and concurrency. Let's break down what's happening.
Why @app.api()
Instead of a Plain FastAPI Route?
If this were a regular FastAPI app, you'd define a @app.post()
route for background removal. That works, until two users hit it at once. Without concurrency management, both requests fight for the GPU, and the app crashes or returns garbage.
@app.api()
solves this. It wraps your function with Gradio's queuing engine: requests are serialized, concurrency is controlled, and on ZeroGPU Spaces, GPU allocation is handled automatically via @spaces.GPU
. As a bonus, any @app.api()
endpoint is also callable via gradio_client
, so other apps or scripts can use your Space programmatically:
from gradio_client import Client, handle_file
client = Client("ysharma/text-behind-image")
result = client.predict(
image_path=handle_file("photo.jpg"),
api_name="/remove_background"
)
Meanwhile, @app.get("/")
is a standard FastAPI route that serves the HTML page. Both coexist naturally because Server
is a FastAPI app.
The Frontend: Pure HTML/CSS/JS
The index.html
in this example is a self-contained ~1300-line web application. No React, no build step, no bundler. Just vanilla HTML with:
- A three-layer canvas: background image → text layer → foreground (transparent PNG) stacked with CSS
z-index
- Drag-and-drop text positioning using pointer events
- A control panel with 20+ parameters: font family (25+ fonts), size, weight, spacing, color, opacity, background fill, stroke, shadow, 3D extrusion depth and angle, rotation, skew, and full CSS perspective transforms
- Client-side PNG export using
<canvas>
compositing
The frontend talks to the backend using the Gradio JS Client:
import { Client, handle_file } from "https://cdn.jsdelivr.net/npm/@gradio/client/dist/index.min.js";
const client = await Client.connect(window.location.origin);
const result = await client.predict("/remove_background", {
image_path: handle_file(file),
});
foregroundLayer.src = result.data[0].url; // transparent PNG
This is the key part: by using the Gradio JS client rather than a raw fetch()
call, the frontend goes through Gradio's queue. That means concurrency is managed, GPU requests don't collide, and you could even show queue position or progress to the user. Everything else, text rendering, layer compositing, export, happens in the browser.
What This Unlocks
Here's what was not possible before gradio.Server
:
With gradio.Server
, Gradio doubles as a backend framework, use its UI system when you want it, bring your own frontend when you don't.
If you want Gradio's UI, you can use gr.Blocks
, gr.Interface
, gr.ChatInterface
. If you want your own UI, use gradio.Server
and bring whatever frontend you like. Either way, you get Spaces hosting, API queuing, gradio_client
access, the full HF ecosystem, and more.
Try It
The app is live on Spaces: ysharma/text-behind-image
Upload any photo with a clear subject, and start layering text behind it. Try the 3D extrusion, perspective tilt, and stroke effects, they combine nicely.
What's Next
This post covered the core idea: gradio.Server
lets you pair any frontend with Gradio's backend. There's more to explore, including MCP tool registration with @app.mcp.tool()
, SSE streaming for real-time updates, batch processing, and patterns for building multi-page apps with shared state.
We'll dig into those in a follow-up post. Stay tuned.
Recommended reading
- Docs: gradio.Server
- Guide: Server mode
```

---

## 24. Granite 4.0 3B Vision: Compact Multimodal Intelligence for Enterprise Documents

- 日期: 2026-03-31 15:10
- 链接: https://huggingface.co/blog/ibm-granite/granite-4-vision

```
Granite 4.0 3B Vision: Compact Multimodal Intelligence for Enterprise Documents
- Table Extraction: Accurately parsing complex table structures (e.g., multi-row, multi-column, etc.) from document images
- Chart Understanding: Converting charts and figures into structured machine-readable formats, summaries, or executable code
- Semantic Key-Value Pair (KVP) Extraction: Identifying and grounding semantically meaningful key-value field pairs across diverse document layouts
The model ships as a LoRA adapter on top of Granite 4.0 Micro, our dense language model, keeping vision and language modular for text-only fallbacks and seamless integration into mixed pipelines. It continues to support vision-language tasks such as producing detailed natural-language descriptions from images (e.g., “Describe this image in detail”). The model can be used standalone or in tandem with Docling to enhance document processing pipelines with deep visual understanding capabilities.
How Granite 4.0 3B Vision Was Built
Granite 4.0 3B Vision’s performance is the result of three key investments: A purpose-built chart understanding dataset constructed via a novel code-guided data augmentation approach, a novel variant of the DeepStack architecture that enables high-detail visual feature injection, and a modular design that keeps the model practical for enterprise deployment.
ChartNet: Teaching Models to Truly Understand Charts
Charts present a challenge for vision-language models (VLMs) because understanding them requires jointly reasoning over visual patterns, numerical data, and natural language, a combination most VLMs cannot handle well, especially when spatial precision matters—such as reading exact values off a line chart. To close this gap, we’ve developed ChartNet: a million-scale multimodal dataset purpose-built for chart interpretation and reasoning, described in detail in our upcoming CVPR 2026 paper.
ChartNet uses a code-guided synthesis pipeline to generate 1.7 million diverse chart samples spanning 24 chart types and 6 plotting libraries [see Figure 1]. What makes it so distinctive is that each sample consists of five aligned components—plotting code, rendered image, data table, natural language summary, and QA pairs—providing models a deeply cross-modal view of what a chart means, not just what it looks like. The dataset also includes human-annotated and real-world subsets, filtered for visual fidelity, semantic accuracy, and diversity.
The result is a training resource that moves VLMs from merely describing charts to genuinely understanding the structured information they encode—with consistent gains across model sizes, architectures, and tasks.
Figure 1: ChartNet’s synthetic data generation pipeline.
DeepStack: Smarter Visual Feature Injection
Most VLMs inject visual information into their language model at a single point, which forces the model to handle both high-level semantics and fine-grained spatial detail simultaneously. Granite 4.0 3B Vision takes a different approach with DeepStack Injection: abstract visual features are routed into earlier layers for semantic understanding, while high-resolution spatial features are fed into later layers to preserve detail. The result is a model that understands both what is in a document and where—which is critical for tasks like table extraction, chart understanding, and KVP parsing where layout matters as much as content. For a full technical breakdown, see the Model Architecture section of the model card.
Modularity: One Model, Two Modes
Granite 4.0 3B Vision is packaged as a LoRA adapter on top of Granite 4.0 Micro, rather than as a standalone model. In practice, this means the same deployment can serve both multimodal and text-only workloads, automatically falling back to the base model when vision isn’t required. This keeps enterprise integration straightforward without sacrificing performance.
How It Performs
Charts: Evaluated on the human-verified ChartNet benchmark using LLM-as-a-judge, Granite 4.0 3B Vision achieves the highest Chart2Summary (86.4%) score among all evaluated models, including significantly larger ones [see Figure 2]. It also ranks second on Chart2CSV (62.1%), behind only Qwen3.5-9B (63.4%), a model more than double its size.
Figure 2: Granite 4.0 3B Vision performance on chart2csv and chart2summary, compared against peer vision-language models using LLM-as-a-judge.
Tables: We evaluate table extraction in two settings: cropped tables (isolated regions) and full-page documents (tables embedded in complex layouts) [see Figure 3]. The benchmark suite includes TableVQA-extract (cropped table images), OmniDocBench-tables (full-page documents), and PubTables-v2 (both cropped and full-page settings). Models are tasked with extracting tables in HTML format and scored using TEDS, a metric that captures both structural and content accuracy. Granite 4.0 3B Vision achieves the strongest performance across benchmarks, leading on PubTablesV2 on both cropped (92.1) and full-page (79.3), OmniDocBench (64.0), and TableVQA (88.1) scores among all evaluated models.
Figure 3: Granite 4.0 3B Vision’s table extraction performance across cropped and full-page benchmarks (TableVQA-extract, PubTables-v2, OmniDocBench-tables), measured by TEDS.
Semantic KVP: VAREX is a benchmark specifically designed to discriminate between small extraction models, comprising 1,777 U.S. government forms spanning simple flat layouts to complex nested and tabular structures. Models are evaluated using exact match (EM), a strict metric that requires the model’s extracted key-value pairs to match the ground truth. Granite 4.0 3B Vision achieves 85.5% EM accuracy zero-shot.
How to Use It
Granite 4.0 3B Vision can operate either as a stand‑alone visual information extraction engine or as part of a fully automated document‑processing pipeline with Docling. The model is designed to support scalable, accurate extraction across diverse document types and visual formats.
1. Stand‑Alone Image Understanding Granite 4.0 3B Vision can run directly on individual images, making this option useful for applications with existing workflows that need targeted visual extraction without modifying upstream systems. This offers easy integration into existing automation workflows and is suitable for lightweight, task‑specific tools (e.g., form parsers, chart analyzers, etc.).
2. Integrated Document Understanding Pipeline With Docling Granite 4.0 3B Vision can also be integrated seamlessly with Docling to support complete end‑to‑end document understanding. This mode can offer:
- Large‑scale processing of multi‑page PDFs
- Automated detection, segmentation, and cropping of figures, tables, and other visual elements with Docling and redirection of clean crops to Granite Vision model for fine-grained extraction
- Efficient workflow with lower overall computational costs and faster throughput
- Higher accuracy, more reliable extraction, and significantly improved efficiency across large document collections
Example Use Cases
- Form Processing: Extract structured fields from invoices, forms, and receipts using KVP capabilities or generate natural‑language descriptions of figures using image2text feature (e.g., “Describe this image in detail”).
- Financial Report Analysis: Use Docling to parse reports, detect figures, and crop visual elements. Process charts using Granite Vision’s chart2csv, chart2code, and tables using tables_json capabilities to convert them into structured, machine‑readable data enabling actionable insights.
- Research Document Intelligence: Utilize Docling to handle OCR and layout parsing across dense academic PDFs, and pass extracted figures to chart2summary and table crops to tables_html to make visual content discoverable alongside free-form text in a single pipeline.
Try It Today
Granite 4.0 3B Vision is available now on HuggingFace, released under the Apache 2.0 license. Full technical details, training methodology, and benchmark results are available in the model card. We’d love to hear what you build with it—share your feedback in the community tab.
```

---

## 25. Training mRNA Language Models Across 25 Species for $165

- 日期: 2026-03-31 08:23
- 链接: https://huggingface.co/blog/OpenMed/training-mrna-models-25-species

```
Training mRNA Language Models Across 25 Species for $165
Part II: Building the Pipeline, From Structure Prediction to Codon Optimization
By OpenMed, Open-Source Agentic AI for Healthcare & Life Sciences
TL;DR: We built an end-to-end protein AI pipeline covering structure prediction, sequence design, and codon optimization. After comparing multiple transformer architectures for codon-level language modeling, CodonRoBERTa-large-v2 emerged as the clear winner with a perplexity of 4.10 and a Spearman CAI correlation of 0.40, significantly outperforming ModernBERT. We then scaled to 25 species, trained 4 production models in 55 GPU-hours, and built a species-conditioned system that no other open-source project offers. Complete results, architectural decisions, and runnable code below.
Contents
- What We Built
- The Architecture Exploration
- The Pipeline
- Scaling to Multi-Species
- The End-to-End Workflow
- Where This Stands and What's Next
- References
Imagine going from a therapeutic protein concept to a synthesis-ready, codon-optimized DNA sequence in an afternoon. That is the pipeline OpenMed set out to build, and this post documents the process from start to finish.
In Part I, we mapped the landscape of protein AI: the architectures powering structure prediction, the open-source tools available for protein design, and the ecosystem of models from AlphaFold to ESMFold. That was a survey. This is the build.
At OpenMed, we set out to build a complete pipeline that takes a protein idea from concept to expression-ready DNA. That means three stages: predict the 3D structure of a protein, design amino acid sequences that fold into that structure, and optimize the underlying DNA codons so the protein actually expresses in the target organism. Along the way, we ran extensive experiments comparing transformer architectures for codon optimization, scaled our best model to 25 species, and built tooling that ties it all together.
This is not a polished success story. It is a transparent account of what worked, what surprised us, and what we would do differently, with runnable code and full results at every step.
1. What We Built
The pipeline has three components, each addressing a different stage of the protein engineering workflow described in Part I. Structure prediction determines what shape a protein takes. Sequence design determines which amino acids will produce that shape. Codon optimization determines which DNA will produce those amino acids efficiently in a living cell.
The mRNA optimization work is where we invested the most effort, and where we have the most to share. The folding and design components use established tools (ESMFold from Meta, ProteinMPNN from the Baker Lab, both covered in depth in Part I). The codon optimization component is entirely ours: new models, new training infrastructure, new evaluation metrics.
2. The Architecture Exploration
In Part I, we surveyed the protein AI landscape and noted that most biological language models are adaptations of NLP architectures. The open question was which architecture. BERT variants dominate protein modeling (ESM-2, ProtTrans), but codon sequences have different statistical properties than both natural language and amino acid sequences. Codons are triplets drawn from a small 64-token alphabet, with strong positional dependencies and species-specific usage biases. We needed to find out what works from first principles.
The core question: which transformer architecture works best for codon-level language modeling?
This matters because codon optimization is crucial for therapeutic mRNA, vaccines, and recombinant protein production. The genetic code is degenerate: the same protein can be encoded by astronomically many different DNA sequences, but some codon arrangements express 100x better than others. The Pfizer-BioNTech COVID vaccine, for example, was codon-optimized for human expression. We wanted to build a model that could learn these preferences directly from natural coding sequences, rather than relying on hand-crafted frequency tables.
The Contenders
We started with a small CodonBERT baseline (6M params, following Sanofi's published architecture) and scaled up through two families: ModernBERT, which represented the latest efficiency innovations from the NLP community, and RoBERTa, the proven workhorse behind Meta's ESM protein language models.
The choice of RoBERTa was deliberate. As we discussed in Part I, Meta's ESM-2 (which powers ESMFold) is itself a RoBERTa variant trained on protein sequences. We hypothesized that the same architecture family that learned amino acid patterns might also learn codon patterns. ModernBERT was the counterpoint: a 2024 architecture with RoPE embeddings, Flash Attention, and alternating local/global attention layers, representing everything the NLP community had learned since RoBERTa's 2019 release.
The Training Setup
To ensure a fair comparison, every model was trained on identical data with the same evaluation protocol. We used 250,000 coding sequences (CDS) from E. coli RefSeq, covering chromosome and complete assembly accessions. This is a clean, well-annotated dataset where codon usage patterns are well-characterized in the literature, giving us ground truth to validate against.
Our tokenizer maps each codon to a single token: 64 codons plus 5 special tokens (PAD, UNK, CLS, SEP, MASK) for a 69-token vocabulary. This is intentionally minimal. Unlike BPE tokenizers used in NLP, where subword boundaries are statistically learned, codon boundaries are biologically defined. Every three nucleotides encode one amino acid. Our tokenizer respects this.
Training ran on 4 A100 GPUs (80GB) with FSDP sharding, using 15,000 to 25,000 steps depending on model size. All models used masked language modeling (MLM) with 15% masking rate, the same objective used by ESM-2 for protein sequences.
The Results
The result was unambiguous: RoBERTa outperformed ModernBERT by 6x on perplexity (4.01 vs 26.24). This was not a marginal difference. ModernBERT, despite its modern attention patterns and efficient architecture, fundamentally underperformed the classic RoBERTa design on codon sequences.
What We Learned
1. Pre-trained NLP weights do not transfer to biology
We initialized ModernBERT from its published English-language checkpoint, expecting the learned attention patterns to provide a useful starting point. They did not. Our best explanation: ModernBERT's pre-training on English text instilled inductive biases (subword frequency distributions, positional attention patterns) that actively interfere with learning codon statistics. RoBERTa, initialized randomly and trained purely on biological data, had no such baggage. This aligns with what the field has seen more broadly: ESM-2 and ProtTrans both train from scratch on biological data rather than fine-tuning from NLP checkpoints.
2. Hyperparameter tuning unlocked biological alignment
This was the most surprising and practically important finding of the exploration. Compare CodonRoBERTa-large v1 and v2:
Same architecture. Same data. Same number of parameters. The only differences: half the learning rate and a longer warmup (2,000 steps vs 1,000). Yet v2's predicted codon likelihoods are 16x better correlated with real biological codon preferences, as measured by Codon Adaptation Index.
The perplexity actually got slightly worse (4.10 vs 4.01), which means v2 is marginally less accurate at predicting the exact masked codon. But it is dramatically better at predicting codons that biology actually uses. The slower training schedule let the model settle into representations that capture genuine biological signal rather than overfitting to surface statistics.
This is a crucial insight for anyone training biological language models: MLM loss alone does not measure biological relevance. Domain-specific metrics are essential. In our case, CAI correlation turned out to be the metric that separates a useful model from a technically impressive but biologically meaningless one.
3. The base model is remarkably efficient
CodonRoBERTa-base (92M params) achieved nearly identical perplexity to the large model (4.01 vs 4.10) with 3.4x fewer parameters and proportionally less training time. Its CAI correlation (0.219) is lower than v2's (0.404), but still well above the baseline and ModernBERT. For teams without access to multi-GPU clusters, the base model is a practical choice that captures most of the codon modeling performance at a fraction of the cost.
3. The Pipeline
In Part I, we described the three-stage workflow that most computational protein engineering projects follow: predict structure, design sequences, optimize codons. Here we run each stage with real data and report what we actually got.
- Fold: Predict the 3D structure (ESMFold)
- Design: Generate sequences that fold into that structure (ProteinMPNN)
- Optimize: Choose the best codons for expression (CodonRoBERTa)
3.1 Protein Folding with ESMFold
ESMFold architecture. The model parses a single amino acid sequence through the ESM-2 encoder, then predicts 3D coordinates via a folding trunk and structure module. Figure from Bertoline et al., Biomolecules 2024, CC-BY 4.0.
As covered in Part I, ESMFold is Meta's single-sequence structure predictor. It uses ESM-2, a 15-billion-parameter protein language model trained on 65 million UniRef sequences, as its backbone. The key advantage over AlphaFold 2 is speed: ESMFold skips the computationally expensive multiple sequence alignment (MSA) step and predicts structures directly from a single amino acid sequence. That makes it seconds per protein instead of hours.
The tradeoff is accuracy. ESMFold achieves ~0.87 TM-score on CASP14 targets vs. AlphaFold's ~0.92. For rapid prototyping and candidate screening, that gap is acceptable. When a pipeline generates 100 designed sequences and needs to refold all of them to check viability, speed matters more than the last few percentage points of accuracy.
Our Results: 30 Protein Chains
We ran ESMFold on 30 protein chains sourced from the Protein Data Bank. These are real experimental structures with known ground truth, spanning sequence lengths from 211 to 519 residues. The set deliberately includes both easy targets (single-domain proteins) and challenging ones (chains from a multi-chain ribosomal complex, PDB 7K00) to stress-test the model.
import json
# Load our actual results
metrics = json.load(open('outputs/esmfold_metrics.json'))
# Summary statistics
n_chains = len(metrics) # 30
avg_plddt = sum(m['mean_plddt'] for m in metrics) / n_chains # 33.8
avg_ptm = sum(m['ptm'] for m in metrics) / n_chains # 0.79
print(f"Chains: {n_chains}")
print(f"Average pLDDT: {avg_plddt:.1f}")
print(f"Average PTM: {avg_ptm:.2f}")
Results breakdown:
The PTM scores are solid: anything above 0.5 suggests the model has the overall topology correct, and our average of 0.79 indicates high confidence in the predicted folds. The pLDDT scores are lower than published ESMFold benchmarks, which initially concerned us. The explanation turned out to be our test set composition: the ribosomal chains from 7K00 are part of a large multi-chain complex, and ESMFold (which predicts single chains in isolation) cannot model the inter-chain contacts that stabilize these structures. For single-domain proteins in our set, pLDDT scores were consistently above 70.
Running ESMFold
# Activate environment
source .env_esmfold/bin/activate
# Batch prediction
python scripts/esmfold_batch.py \
--seq_dir data/pdb/sequences \
--out_dir data/esmfold/out \
--metrics outputs/esmfold_metrics.json \
--device cuda:0
Each prediction takes ~10-30 seconds on an A100. The output includes:
- PDB structure files
- pLDDT scores (per-residue confidence, 0-100)
- PTM scores (topology confidence, 0-1)
- Predicted Aligned Error (PAE) matrices
3.2 Sequence Design with ProteinMPNN
ProteinMPNN architecture. (A) The encoder processes backbone atom distances; the decoder autoregressively generates amino acid sequences. (B) Random decoding order improves diversity. (C) Tied positions enable symmetric and multi-state design. Figure from Dauparas et al., Science 2022, CC-BY 4.0.
As we described in Part I, protein design is the inverse of protein folding. Folding goes sequence to structure: given amino acids, predict the 3D shape. Inverse folding goes the other way: given a target 3D shape, find amino acid sequences that will fold into it.
ProteinMPNN, from David Baker's lab at the University of Washington, is the current gold standard for this task. It was published in Science in 2022 and has since been validated experimentally: designed sequences fold into their target structures at rates far exceeding random or earlier computational methods. The architecture treats the protein backbone as a graph, where nodes are amino acid positions and edges connect spatially proximate residues (K-nearest neighbors in 3D). A message-passing neural network propagates information through this graph, then autoregressively generates a sequence one residue at a time.
Our Results: Scaffold 7K00
We ran ProteinMPNN on PDB structure 7K00 (a large multi-chain ribosomal complex):
python proteinmpnn/protein_mpnn_run.py \
--pdb_path data/pdb/raw/7K00.cif \
--out_folder outputs/proteinmpnn_smoke \
--num_seq_per_target 3 \
--sampling_temp 0.1
Results:
Here's what the output looks like:
>7K00, score=1.7100, global_score=1.7100
GIREKIKLVSSAGTGHFYTTTKNKRTKPEKLELKKFDPVVRQHVIYKEAKI/MKRTFQPSVLK...
>T=0.1, sample=1, score=0.8857, seq_recovery=0.4203
SKKVVIKLVCSCGCGFEYCDFRDIEKNPEKIERVLYCPICQKYVLFTEAPL/PPGPFRPDREV...
The first line is the native (natural) sequence extracted from the crystal structure. Subsequent lines are ProteinMPNN's designed variants. At temperature 0.1 (low randomness), the model recovers ~42% of the original amino acids, purely from 3D geometry. This is a strong result: it means the model independently rediscovered nearly half the residues that evolution selected, using only the backbone coordinates as input.
Several practical notes from running ProteinMPNN. Scores are negative log-likelihoods, so lower is better. The 42% recovery rate is typical for well-resolved structures and consistent with the original paper's benchmarks. Higher sampling temperatures produce more diverse but riskier sequences. For real design work, the most powerful feature is partial design: catalytic residues, binding site amino acids, or any positions with known functional importance can be fixed in place, while ProteinMPNN redesigns only the scaffold around them. This is the standard approach for engineering a more stable version of an enzyme without disrupting its active site.
3.3 mRNA Optimization
This is where the pipeline transitions from existing tools to our own models. ESMFold and ProteinMPNN are established, well-validated software that we integrated. Codon optimization is where we built something new.
Why Codon Choice Matters
Codon usage frequencies vary dramatically between organisms. These heatmaps compare codon preferences across E. coli, yeast, and CHO cells, the three expression hosts covered by our multi-species models. Figure from Kim et al., J. Microbiol. Biotechnol. 2025, CC-BY 4.0.
The genetic code is degenerate: most amino acids are encoded by multiple codons. Leucine, for example, has six: TTA, TTG, CTT, CTC, CTA, and CTG. All six produce the same amino acid in the final protein. Methionine and tryptophan are the exceptions, with only one codon each.
This redundancy means that for any given protein, there are astronomically many DNA sequences that encode it. A typical 300-amino-acid protein has roughly 10^150 possible codon combinations. They all produce the same amino acid chain, but they do not all produce the same amount of protein. Codon choice affects translation speed (because tRNA molecules are not equally abundant for all codons), mRNA stability (because the nucleotide sequence affects how quickly the transcript degrades), co-translational folding (because translation pauses at rare codons give the protein time to fold), and immune recognition (because the innate immune system in mammalian cells can distinguish native from foreign mRNA patterns). In practice, bad codon choices can reduce protein expression by 100x. This is why every mRNA vaccine, every recombinant protein therapeutic, and every gene therapy vector goes through codon optimization.
The Traditional Approach and Why It Is Limited
The scale of the codon optimization problem. For a typical mRNA, there are over 10^600 possible codon sequences encoding the same protein. The challenge is finding the arrangement that maximizes expression. Figure from Zhang et al. (LinearDesign), Nature 2023, CC-BY 4.0.
The classical method is simple: measure which codons appear most frequently in highly-expressed genes of the target organism, then replace every codon with the most frequent synonym. This is codified as the Codon Adaptation Index (CAI), a per-sequence score that measures how closely the codon usage matches the organism's preferred distribution.
CAI-based optimization works, but it is crude. It treats each codon position independently, ignoring the sequence context. It produces repetitive sequences (the same "optimal" codon used everywhere for a given amino acid), which can cause ribosome stalling and mRNA secondary structure problems. And it misses complex dependencies: the optimal codon at position 50 might depend on what codons are at positions 48 and 52, which a frequency table cannot capture.
Our Approach: Masked Language Modeling
We reframe codon optimization as a language modeling problem. Instead of looking up frequencies in a table, we train a transformer on hundreds of thousands of natural coding sequences using masked language modeling (MLM), the same pre-training objective used by BERT, RoBERTa, and Meta's ESM protein models. The model sees a codon sequence with 15% of positions masked and learns to predict the missing codons from context.
What the model learns, implicitly, is the grammar of codon usage: which codon patterns appear in nature, which codons tend to co-occur, and how preferences shift depending on the surrounding sequence context. This is fundamentally richer than a frequency table because the model captures long-range dependencies across the entire coding sequence.
CodonRoBERTa: Our Best Model
After our architecture exploration (see above), CodonRoBERTa-large-v2 emerged as the winner:
# configs/mrna/production/roberta_large_v2.yaml
model_type: roberta
hidden_size: 1024
num_hidden_layers: 24
num_attention_heads: 16
intermediate_size: 4096
vocab_size: 69
max_position_embeddings: 8192
learning_rate: 5e-5 # Critical: lower than v1
warmup_steps: 2000 # Critical: longer warmup
max_steps: 25000
Training:
python scripts/training/run_mlm_train.py \
--config configs/mrna/roberta_large_v2.yaml \
--train_file data/mrna/processed/train_250k.fasta \
--output_dir outputs/models/CodonRoBERTa-large-v2
Evaluation: Three Metrics That Matter
Evaluating a codon language model is not straightforward. As we learned from the v1/v2 comparison above, a model can have excellent perplexity (accurately predicting masked codons) while having poor biological alignment (predicting codons that nature does not actually prefer). We evaluate on three complementary axes:
1. Perplexity measures how well the model predicts masked codons, computed as the exponentiated cross-entropy loss. A perplexity of 4.10 means the model is, on average, choosing between ~4 equally likely codons at each masked position. Given that most amino acids have 2-6 synonymous codons, this indicates the model has learned meaningful preferences rather than guessing uniformly. Lower is better. CodonRoBERTa-large-v2: 4.10.
2. CAI Correlation (Spearman) measures whether a model's predicted codon likelihoods align with known biological codon usage preferences. We compute the Codon Adaptation Index for each test sequence, then correlate it with the model's pseudo-log-likelihood score. A positive correlation means the model assigns higher probability to sequences that biology actually uses. This is the metric that matters most for practical codon optimization, because it directly measures whether the model has learned biologically relevant patterns vs. just statistical ones. CodonRoBERTa-large-v2: 0.404 (p < 10^-20).
3. Synonymous Recovery asks: when the model predicts a codon for a masked position, does it at least get the amino acid right? Even if it picks the wrong synonym (e.g., CTT instead of CTC for leucine), predicting the correct amino acid shows the model understands the protein-level constraint. CodonRoBERTa-large-v2: 12.1% top-1 synonymous.
Running the Evaluations
# Perplexity
python scripts/evals/advanced/eval_perplexity.py \
--model outputs/models/CodonRoBERTa-large-v2/final \
--test_file data/mrna/processed/test_6k.fasta \
--output outputs/eval_results/CodonRoBERTa-large-v2/perplexity.json
# CAI Correlation
python scripts/evals/advanced/eval_cai_correlation.py \
--model outputs/models/CodonRoBERTa-large-v2/final \
--test_file data/mrna/processed/test_6k.fasta \
--output outputs/eval_results/CodonRoBERTa-large-v2/cai_correlation.json
# Synonymous Recovery
python scripts/evals/advanced/eval_synonymous_recovery.py \
--model outputs/models/CodonRoBERTa-large-v2/final \
--test_file data/mrna/processed/test_6k.fasta \
--output outputs/eval_results/CodonRoBERTa-large-v2/synonymous_recovery.json
The Final Leaderboard
Putting it all together across our model variants:
The RoBERTa family dominates across the board. For production use, CodonRoBERTa-large-v2 is the clear choice: it has the strongest biological alignment (CAI 0.404) while maintaining competitive perplexity. For teams with limited compute, CodonRoBERTa-base delivers nearly the same perplexity at 3.4x fewer parameters. ModernBERT underperformed substantially, which we attribute to its NLP-pretrained weights interfering with codon pattern learning.
Using the Model
from transformers import RobertaForMaskedLM
import torch
# Load model (available soon on Hugging Face)
model = RobertaForMaskedLM.from_pretrained("OpenMed/CodonRoBERTa-large-v2")
tokenizer = CodonTokenizer() # Our custom 69-token vocabulary
# Score a sequence
sequence = "ATG GCT AAA GGT..." # Space-separated codons
inputs = tokenizer(sequence, return_tensors='pt')
with torch.no_grad():
outputs = model(**inputs)
# Pseudo-log-likelihood gives a "naturalness" score
# Predict alternatives for a masked position
masked_seq = "ATG [MASK] AAA GGT..."
inputs = tokenizer(masked_seq, return_tensors='pt')
predictions = model(**inputs).logits
top_codons = predictions[0, mask_pos].topk(5)
4. Scaling to Multi-Species
Single-species codon optimization is useful, but limited. Every organism has its own codon usage biases shaped by millions of years of evolution. E. coli favors different codons than human cells, which favor different codons than yeast. A model trained only on E. coli data will not produce optimal codons for human expression.
The industry standard is to use separate CAI tables for each organism. We wanted something better: a single model that understands codon usage across organisms, can be conditioned on a target species, and can transfer knowledge from data-rich organisms (human, with 145k annotated coding sequences) to data-poor ones (E. coli, with 9k). After establishing CodonRoBERTa-large-v2 as our best architecture on single-species data, we built this system.
The Data Engineering Challenge
Assembling a multi-species codon dataset is not as simple as downloading a few genomes. Each organism lives in a different NCBI RefSeq assembly, with different annotation quality, different CDS boundaries, and different sequence conventions. We wrote an automated pipeline that downloads CDS sequences from 25 organisms, validates them (checking for proper start/stop codons, length divisible by 3, no internal stops), labels each sequence with a species token, and splits into train/test sets with stratification by species.
# scripts/training/download_multispecies_cds.py
# Automated download from NCBI RefSeq for 25 organisms
SPECIES = {
# Bacteria (19 species)
'bacteria': [
('GCF_000005845.2', 'Escherichia coli K-12', 'ECOLI'),
('GCF_000009045.1', 'Bacillus subtilis 168', 'BSUBT'),
('GCF_000006945.2', 'Salmonella enterica', 'SENTE'),
('GCF_000195955.2', 'Mycobacterium tuberculosis', 'MTUBE'),
# ... 15 more bacteria
],
# Yeast (3 species)
'yeast': [
('GCF_000146045.2', 'Saccharomyces cerevisiae S288C', 'YEAST'),
('GCF_000002515.2', 'Schizosaccharomyces pombe', 'SPOMBE'),
('GCF_000027005.1', 'Pichia pastoris', 'PICHIA'),
],
# Mammals (3 species)
'mammals': [
('GCF_000001405.40', 'Homo sapiens GRCh38', 'HUMAN'),
('GCF_000001635.27', 'Mus musculus GRCm39', 'MOUSE'),
('GCF_003668045.3', 'Cricetulus griseus CHO-K1', 'CHO'),
]
}
The final dataset spans three domains of biotechnology relevance:
The coverage is deliberate: bacteria are the workhorse of recombinant protein production, yeast dominates industrial biomanufacturing, and mammalian cells (especially CHO and human) are required for therapeutic proteins and mRNA vaccines. These 25 organisms collectively cover the vast majority of real-world codon optimization use cases.
The Tokenization Innovation
A model that sees sequences from 25 different organisms needs to know which organism it is looking at. We solved this by extending our 69-token codon vocabulary with 25 species tokens, creating a 94-token system. Each sequence is prepended with its species token (e.g., [HUMAN]
, [ECOLI]
, [YEAST]
), so the model learns species-specific codon preferences within a single shared architecture.
# scripts/training/codon_tokenizer.py
class MultiSpeciesCodonTokenizer(CodonTokenizer):
"""Extended tokenizer with species-awareness"""
def __init__(self):
super().__init__()
# 0-4: [PAD], [UNK], [CLS], [SEP], [MASK]
# 5-68: 64 codons (AAA, AAC, ..., TTT)
# 69-93: 25 species tokens
self.species_tokens = [
'[ABAUM]', '[BSUBT]', '[CHO]', '[ECOLI]',
'[HUMAN]', '[MOUSE]', '[YEAST]', # ... +18 more
]
def encode(self, dna_seq: str, species: str = None):
"""Encode with species token prepended"""
ids = super().encode(dna_seq)
if species and species in self.species_to_id:
ids = [self.species_to_id[species]] + ids
return ids
This design has three advantages. First, it enables species-conditioned generation: the same model produces human-optimal or E. coli-optimal codons depending on which species token is prepended. Second, it enables cross-species transfer learning: universal codon patterns (like avoiding certain dinucleotides, or preferring GC-rich codons in GC-rich genomes) are shared across all species, while species-specific preferences are captured by conditioning on the species token. Third, the 94-token vocabulary is backward-compatible with our 69-token single-species models, since the first 69 tokens are identical.
Training the Universal Base Model
The universal base model is a 311.9M-parameter RoBERTa-large, identical in architecture to our single-species v2 but with the expanded 94-token vocabulary. It was trained for 48 hours on 4 A100 GPUs using the full 362k-sequence multispecies dataset.
# configs/mrna/production/roberta_large_multispecies.yaml
model:
name: "CodonRoBERTa-large-multispecies"
vocab_size: 94 # 69 base + 25 species
hidden_size: 1024
num_hidden_layers: 24
num_attention_heads: 16
training:
max_steps: 50000 # ~4.5 epochs over 362k sequences
learning_rate: 5e-5
per_device_train_batch_size: 4 # 4 GPUs = 16 effective
gradient_accumulation_steps: 2 # 32 total batch size
bf16: true
fsdp: "full_shard auto_wrap" # Critical for 311M params
Training command:
torchrun --nproc_per_node=4 --master_port=29501 \
scripts/training/run_multispecies_train.py \
--config configs/mrna/production/roberta_large_multispecies.yaml
Results:
The test perplexity of 24.9 is higher than our single-species model's 4.01, which might look like a regression. It is not. The multispecies model must learn distinct codon preferences for 25 different organisms, each with its own evolutionary history and tRNA pools. A bacterium like M. tuberculosis (65% GC content) uses completely different codons than human cells (41% GC). The model is solving a fundamentally harder problem, and the perplexity reflects that. What matters is whether species-specific fine-tuning can recover performance, and it does.
Species-Specific Fine-Tuning
The universal base model is a generalist. For production use, specialists perform better. OpenMed's fine-tuning strategy starts from the multispecies checkpoint and trains further on a single species at a lower learning rate (2e-5 vs 5e-5), preserving cross-species knowledge while specializing the model's predictions for one organism.
Dataset splits:
# scripts/training/split_species_datasets.py
# Automated splitting for 6 priority species
RESULTS = {
'HUMAN': {'train': 131_245, 'test': 6_908},
'MOUSE': {'train': 88_022, 'test': 4_633},
'CHO': {'train': 42_541, 'test': 2_239},
'ECOLI': {'train': 8_547, 'test': 450},
'YEAST': {'train': 5_439, 'test': 287},
'PICHIA':{'train': 4_548, 'test': 240},
}
Training all three priority species:
# HUMAN: Therapeutic mRNA, vaccines
torchrun --nproc_per_node=4 scripts/training/run_multispecies_train.py \
--config configs/mrna/production/roberta_large_human_finetune.yaml
# ECOLI: Protein expression, metabolic engineering
torchrun --nproc_per_node=4 scripts/training/run_multispecies_train.py \
--config configs/mrna/production/roberta_large_ecoli_finetune.yaml
# CHO: Biopharmaceutical production
torchrun --nproc_per_node=4 scripts/training/run_multispecies_train.py \
--config configs/mrna/production/roberta_large_cho_finetune.yaml
Comprehensive Results:
The most important result here is the HUMAN model: at 24.3 perplexity, it is the only specialist that beats the universal base, making it our production model for therapeutic mRNA applications. But the ECOLI result is arguably more interesting from a research perspective. With only 8,547 training sequences (compared to 131k for human), the E. coli specialist still improved over the multispecies base. This validates the transfer learning hypothesis: training on 25 species first, then fine-tuning on a small species-specific dataset, works better than training on the small dataset alone. For the many organisms where annotated CDS data is scarce, this approach opens the door to reasonable codon optimization without needing tens of thousands of species-specific sequences.
The CHO model showed slight degradation (25.5 vs 24.9), which we attribute to insufficient training steps. ECOLI got 5,000 steps for 8.5k sequences (0.59 steps per sequence), while CHO got 10,000 steps for 42.5k sequences (0.24 steps per sequence). A rerun with 15,000 steps should close this gap. All three specialists fine-tuned in just 7 hours total, leveraging the 48-hour investment in the multispecies base.
The Complete Model Suite
After 55 hours of training, we have:
All models will be released on Hugging Face under the OpenMed organization. The naming convention follows OpenMed/{model-name}
for direct use with from_pretrained()
.
Universal Models:
OpenMed/CodonRoBERTa-large-multispecies
(311.9M params)- Trained on 25 species
- Perplexity: 24.9
- Use case: Cross-species optimization, rare organisms
Species-Specific Specialists:
OpenMed/CodonRoBERTa-large-human
(311.9M params)- Perplexity: 24.3 (best overall)
- Use case: mRNA vaccines, gene therapy, therapeutic proteins
OpenMed/CodonRoBERTa-large-ecoli
(311.9M params)- Perplexity: 25.3
- Use case: Bacterial protein expression, metabolic engineering
OpenMed/CodonRoBERTa-large-cho
(311.9M params)- Perplexity: 25.5
- Use case: Mammalian cell culture, biopharmaceuticals
Single-Species Models:
OpenMed/CodonRoBERTa-large-v2
(312M params)- Perplexity: 4.10, CAI: 0.404
- Trained on 250k E. coli only
- Still the best for pure E. coli optimization
OpenMed/CodonRoBERTa-base
(92M params)- Perplexity: 4.01, CAI: 0.219
- Best efficiency option (3.4x smaller than large)
Production Deployment Strategy
For therapeutic mRNA (Moderna, BioNTech-style vaccines):
from transformers import RobertaForMaskedLM
# Load human-optimized model
model = RobertaForMaskedLM.from_pretrained("OpenMed/CodonRoBERTa-large-human")
# Optimize amino acid sequence to DNA
optimized_dna = optimize_for_human(protein_seq, model)
For industrial protein production:
# E. coli expression
model_ecoli = RobertaForMaskedLM.from_pretrained("OpenMed/CodonRoBERTa-large-ecoli")
# CHO cell expression
model_cho = RobertaForMaskedLM.from_pretrained("OpenMed/CodonRoBERTa-large-cho")
For rare/unmodeled organisms:
# Use multispecies base with species conditioning
model_multi = RobertaForMaskedLM.from_pretrained("OpenMed/CodonRoBERTa-large-multispecies")
# Prepend species token: [YEAST], [PICHIA], [MOUSE], etc.
Infrastructure & Reproducibility
Hardware requirements:
- 4×A100 80GB GPUs (training)
- Single A100 40GB (inference)
- FSDP (Fully Sharded Data Parallel) for 311M params
- bf16 mixed precision (critical for stability)
Storage footprint:
- ~150 GB total (data, trained models, and checkpoints across all runs)
Complete training pipeline:
# 1. Download multi-species data (automated)
python scripts/training/download_multispecies_cds.py \
--output_dir data/mrna/multispecies \
--categories bacteria yeast mammals
# 2. Train universal base (48 hours)
torchrun --nproc_per_node=4 \
scripts/training/run_multispecies_train.py \
--config configs/mrna/production/roberta_large_multispecies.yaml
# 3. Split species datasets
python scripts/training/split_species_datasets.py \
--input data/mrna/multispecies/train_multispecies.fasta \
--output_dir data/mrna/species_specific
# 4. Fine-tune specialists (7 hours total)
for species in human ecoli cho; do
torchrun --nproc_per_node=4 \
scripts/training/run_multispecies_train.py \
--config configs/mrna/production/roberta_large_${species}_finetune.yaml
done
# 5. Evaluate all models
for model in multispecies human ecoli cho; do
python scripts/evals/advanced/eval_perplexity_multispecies.py \
--model_path outputs/models/CodonRoBERTa-large-${model}/final \
--test_file data/mrna/species_specific/${model}_test.fasta \
--output_file outputs/evals/${model}_perplexity.json
done
Total compute cost:
- 55 GPU-hours on A100 80GB (~$165 on AWS p4d.24xlarge)
- All models trained to convergence in under 3 days wall-clock time
What This Enables
The multi-species suite covers the three pillars of applied codon optimization. For therapeutic mRNA, the HUMAN specialist model optimizes codons for expression in human cells, directly applicable to vaccine design (Moderna and BioNTech both codon-optimize their mRNA constructs) and gene therapy vectors. For recombinant protein production, the ECOLI specialist handles the most common bacterial expression host, while the CHO specialist covers the mammalian cell line used to produce most monoclonal antibodies and biopharmaceuticals. For organisms not covered by a specialist, the multispecies base model accepts any of the 25 species tokens and generates organism-appropriate codons.
The transfer learning result is particularly relevant for the broader community. Many industrially important organisms (non-model bacteria, insect cells, plant cells) have limited annotated CDS data. Our results with E. coli (8.5k sequences, improved over base) suggest that multispecies pre-training followed by small-scale fine-tuning is a viable path for these organisms, without requiring the tens or hundreds of thousands of sequences that training from scratch demands.
By the Numbers
The full project consumed 55 GPU-hours on 4 A100 80GB GPUs (~$165 at AWS spot pricing), produced ~150 GB of models and checkpoints across 4 training runs, and covers 381,283 CDS sequences from 25 species downloaded from NCBI RefSeq. All models use the same 311.9M-parameter architecture, are saved in safetensors format for fast loading, and run inference on a single GPU with 16GB+ VRAM. Everything is released under Apache 2.0.
5. The End-to-End Workflow
The modern computational protein design workflow. Structure generation (top) produces backbone coordinates; sequence optimization (bottom) finds amino acid sequences that fold into the target shape. Our pipeline adds a third step: codon optimization for expression. Figure from Kortemme, Cell 2024, CC-BY 4.0.
In Part I, we described the protein engineering loop as a cycle of prediction, design, and optimization. Here is what that looks like in practice with OpenMed's pipeline. Each step feeds into the next, and the entire computational phase runs in an afternoon on a single GPU.
Consider a concrete scenario: engineering a more stable version of a therapeutic enzyme that degrades too quickly in the bloodstream.
Step 1: Fold (ESMFold). Predict the structure of the starting sequence to understand its active site and identify regions that might be destabilized. ESMFold returns a 3D structure in PDB format, per-residue confidence scores (pLDDT) highlighting uncertain regions, and an overall topology confidence metric (PTM).
Step 2: Design (ProteinMPNN). Keep the active site fixed but redesign the scaffold for improved stability. ProteinMPNN takes the backbone coordinates, a list of immutable positions (catalytic residues), and generates 100 diverse candidate sequences, each predicted to fold into the target shape.
Step 3: Verify (ESMFold). Refold all 100 candidates with ESMFold to confirm they still adopt the correct shape. Filter for high mean pLDDT (>80), correct topology (RMSD to original), and low clash scores.
Step 4: Optimize (CodonRoBERTa). Take the best amino acid sequences and use CodonRoBERTa-large-v2 to generate optimal DNA sequences for expression in the target organism (E. coli, yeast, or mammalian cells). The model scores synonymous codon choices based on learned biological preferences, identifies contextually optimal codons rather than just globally frequent ones, and produces sequences with high CAI correlation.
Step 5: Synthesize and Test. Order the DNA from a synthesis company, clone it into an expression vector, and test expression and activity in the lab.
This loop, from hypothesis to synthesis-ready DNA, replaces what once took months of iterative wet-lab trial and error. A researcher arrives at the bench with 5-10 computationally vetted candidates instead of one or two educated guesses. The success rate improves, the cost drops, and the design cycle compresses from months to days.
For a full ecosystem overview, tool selection guide, and license reference, see Part I.
6. Where This Stands and What's Next
The Landscape
OpenMed is not working in isolation. Two recent models push the codon/mRNA modeling frontier further:
mRNABERT (Xiong et al., Nature Communications 2025): 86M-param BERT with a dual tokenization scheme (single nucleotides for UTRs, codons for CDS) and cross-modality contrastive learning against frozen ProtT5-XL protein embeddings. Trained on 18M sequences. Achieves R^2 = 0.66 on full-length mRNA translation efficiency, a 1.6-10x improvement over prior RNA models. Code and weights available (Apache 2.0).
NUWA (Zhong et al., bioRxiv 2026): Three domain-specific RoBERTa encoders (Bacteria, Eukaryota, Archaea) with curriculum MLM and supervised contrastive learning. Trained on 115M sequences across ~25,000 species. Beats CodonBERT on 11/13 BEACON benchmark tasks. No code or weights released.
Both models train on 50-300x more data than OpenMed used. That is the primary gap, and we are transparent about it.
Here is what OpenMed does that neither of them offers:
Species-conditioned single model. mRNABERT has no species conditioning at all. NUWA trains three separate models (one per domain of life). We put 25 species tokens into one 94-token vocabulary and train a single model that can be prompted for any organism. More parameter-efficient, more flexible.
Transfer learning to low-resource organisms, validated. We showed that fine-tuning the multispecies base on just 8.5k E. coli sequences improves over the base model. Neither mRNABERT nor NUWA demonstrates this.
Full open-source pipeline. ESMFold + ProteinMPNN + CodonRoBERTa, end to end, with training code, configs, eval scripts, and model weights. All Apache 2.0. mRNABERT releases code but not the pipeline. NUWA releases nothing.
In Progress: CodonJEPA
OpenMed is running a proof-of-concept for a fundamentally different approach: Joint Embedding Predictive Architecture (JEPA) for codon sequences.
Standard MLM predicts masked tokens. JEPA predicts masked embeddings. The hypothesis: if the model is forced to predict in embedding space rather than token space, it should learn that synonymous codons (different DNA, same amino acid) are functionally equivalent. MLM cannot achieve this because it is trained to distinguish every token.
The architecture:
- Context encoder: RoBERTa-base (768-dim, 12 layers), trained normally
- Target encoder: EMA copy of the context encoder (momentum 0.990 to 0.999, no gradients)
- Predictor: Lightweight 4-layer transformer (384-dim), predicts target embeddings from context
- Masking: Multi-block strategy (4 contiguous blocks per sequence, 15-20% mask scale)
- Collapse prevention: VICReg regularization (variance + covariance loss)
Early results from our evaluation suite (JEPA vs. MLM baseline, same data, same hyperparameters, 15k steps each):
The synonymous robustness result is the one that matters most for our hypothesis. JEPA embeddings are nearly identical (99.97% cosine similarity) for sequences that differ only in synonymous codon choices. MLM embeddings shift significantly (94.14%). This means JEPA does learn that synonymous codons are interchangeable, exactly as predicted.
The open challenge: JEPA currently suffers from dimensional collapse (91.78% of variance concentrated in one component). This is a known failure mode for self-supervised methods and suggests the VICReg regularization weights need tuning. The architecture works; the training dynamics need more iteration.
This is early-stage research, not production-ready. But if the collapse problem can be solved, JEPA could produce codon embeddings that are inherently amino-acid-aware, something that MLM, by its token-level prediction objective, fundamentally cannot achieve.
Roadmap
CodonRoBERTa (scaling up):
- Retrain on mRNABERT's public 36M-sequence dataset (Zenodo). Same architecture, same species tokens, 100x more data
- Add cross-modality contrastive alignment with ProtT5-XL (proven by mRNABERT to boost protein property prediction)
- Extend species-specific fine-tuning to YEAST, PICHIA, MOUSE
- Add mRNA stability and immunogenicity prediction heads
CodonJEPA (fixing and scaling):
- Solve dimensional collapse (stronger VICReg weights, alternative regularizers)
- Benchmark against mRNABERT's contrastive approach on the same downstream tasks
- If JEPA embeddings hold up, integrate as a drop-in replacement for MLM embeddings in the pipeline
Pipeline:
- Integrate RFdiffusion for de novo backbone generation
- Add solubility and expression prediction heads
- Fine-tune ESMFold on specialized domains (antibodies, enzymes)
Setup and Requirements
Hardware:
- Tested on 4×A100 GPUs (80GB)
- Folding inference: ~16-20GB VRAM for typical proteins
- Training: Scales with FSDP (Fully Sharded Data Parallel)
- Minimum for inference: Single GPU with 16GB+ VRAM
Environment:
- Use
.env_esmfold
virtual environment for folding - For training: PyTorch 2.5.1+cu121 with flash-attn2
- Python 3.10+ recommended
Licenses (all commercial-friendly):
- ESMFold: MIT
- ProteinMPNN: MIT
- OpenFold: Apache-2.0
- Our CodonRoBERTa: Apache-2.0
7. References
OpenMed's work builds on foundational research from Meta AI, the Baker Lab at the University of Washington, DeepMind, and the broader open-source computational biology community.
Key Papers
Protein Structure Prediction
- Jumper, J. et al. "Highly accurate protein structure prediction with AlphaFold." Nature (2021). DOI
- Lin, Z. et al. "Evolutionary-scale prediction of atomic-level protein structure with a language model." Science (2023). DOI
- Ahdritz, G. et al. "OpenFold: Retraining AlphaFold2 yields new insights." Nature Methods (2024). DOI
Protein Design
- Dauparas, J. et al. "Robust deep learning-based protein sequence design using ProteinMPNN." Science (2022). DOI
- Watson, J.L. et al. "De novo design of protein structure and function with RFdiffusion." Nature (2023). DOI
mRNA & Codon Optimization
- Cheng, J. et al. "CodonBERT: a language model for codon optimization." Nucleic Acids Research (2024). DOI
- Xiong, Y. et al. "mRNABERT: advancing mRNA sequence design with a universal language model and comprehensive dataset." Nature Communications (2025). DOI
- Zhong, Y. et al. "Large mRNA language foundation modeling with NUWA for unified sequence perception and generation." bioRxiv (2026). DOI
- Warner, B. et al. "ModernBERT: Smarter, Better, Faster, Longer." arXiv (2024). arXiv
Models and Data: Coming Soon
All models, training code, and the multi-species dataset described in this post will be publicly released under the OpenMed organization on Hugging Face under Apache 2.0 / MIT licenses.
Models (7 checkpoints):
Dataset:
Training code and evaluation scripts will be released alongside the models.
Follow OpenMed on Hugging Face to be notified when models go live.
The ML Engineer's Guide to Protein AI: From Protein to Optimized DNA | March 2026
Read Part I: The AlphaFold Revolution, covering the landscape of protein AI.
Questions or collaboration ideas? Reach out on Hugging Face or open a discussion on the model pages.
```

---

## 26. TRL v1.0: Post-Training Library Built to Move with the Field

- 日期: 2026-03-31 00:00
- 链接: https://huggingface.co/blog/trl-v1

```
TRL v1.0: Post-Training Library Built to Move with the Field
TRL now implements more than 75 post-training methods. But coverage isn’t the goal by itself. What matters is making these methods easy to try, compare, and actually use in practice. The design of the library wasn’t decided upfront. It is the result of years of iteration — the first commit goes back more than six years — and it has been shaped by everything the field threw at it: new algorithms, new models, shifting paradigms. Over time, this pressure forced the codebase toward a very specific design. Parts of it might look unusual at first, but like in many evolutionary codebases, they exist for a reason.
TRL is built for a field that doesn’t sit still. So the question is not how to design the perfect abstraction. It is how to make stable software in a domain that keeps invalidating its own assumptions. This is what we tried to solve in TRL v1.0, and this post explains how.
1. A moving target: post-training as a shifting field
Post-training has not evolved as a smooth refinement of one recipe. It has moved through successive centers of gravity, each changing not just the objective, but the shape of the stack.
PPO [Schulman et al., (2017); Ziegler et al., (2019)] made one architecture look canonical: a policy, a reference model, a learned reward model, sampled rollouts, and an RL loop.
Then DPO-style methods such as the original DPO [Rafailov et al., (2023)], ORPO [Hong et al., (2024)], and KTO [Ethayarajh et al., (2024)] cut through that stack: preference optimization could work without a separate reward model, value model, or any online RL. Components that had looked fundamental suddenly looked optional.
RLVR-style methods such as GRPO [Shao et al., (2024)] shifted the center again. On tasks like math, code, and tool use, rewards often come from verifiers or deterministic checks rather than learned reward models. Sampling and rollouts matter again, but the objects in the loop are no longer quite the ones PPO libraries were designed around.
The lesson is not just that methods change. The definition of the core keeps changing with them. Strong assumptions here have a short half-life. This is probably why no post-training library is really stable yet.
2. From project to library: TRL has a chaos-adaptive design
So what does it mean to build a library for a field that won't sit still? The answer is counterintuitive: don't try to capture the essence of what's stable today. Instead, design around what could change. Reward models illustrate why: they looked essential in PPO, became optional in DPO, and came back as verifiers in RLVR methods — structures that could be deterministic functions rather than learned models. Any abstraction built around their original form would have been obsolete twice over by now. The library survives by recognizing that strong assumptions have a short life, and by making that changeability central to how the codebase is organized.
This is the environment in which TRL is downloaded 3 million times a month, and in which major downstream projects treat it as stable infrastructure. The field keeps shifting the ground, and at the same time, those users need things not to break.
A shift in nature: from code to contract
TRL didn’t make a deliberate decision to become a library. It found out it already was one. Projects like Unsloth and Axolotl — with thousands of users between them — had built directly on top of TRL’s trainers and APIs. A breaking change in TRL propagated instantly into their stacks. A renamed argument, a shifted default, a restructured output — any of these became someone else’s incident. The shift had already happened. v1.0 is the moment TRL acknowledged it explicitly.
Stable and experimental, under the same roof
The unusual thing about TRL’s stability model is not what it guarantees, it is what it tolerates alongside those guarantees. Stable and experimental coexist within the same package, with explicitly different contracts. The stable core follows semantic versioning. The experimental layer makes no such promises — it is where new methods land while they are still being evaluated, and where the API can move fast to keep up with the field.
This isn’t a compromise. It’s a response to a specific constraint: the field produces new methods faster than any of them can earn stability. Refusing to add immature methods would make TRL irrelevant within months. Adding them all to stable would break every downstream project every time an algorithm turned out not to work as expected.
from trl import SFTTrainer # ⚖️ stable
from trl.experimental.orpo import ORPOTrainer # 🧪 experimental
Promotion from experimental to stable isn’t automatic. What matters is the ratio between maintenance cost and actual usage. Some methods earn their place because the community uses them heavily. Others become viable because we can make them cheap enough to maintain — and the design of the codebase is what makes that possible.
In practice, the stable surface includes trainers for SFT, DPO, Reward modeling, RLOO, and GRPO, along with their close variants. The experimental surface is broader and moves faster; for an up-to-date view, the best reference is the TRL documentation.
The breaking changes needed to reach v1.0 were distributed deliberately across the 0.x releases. Migration from the last 0.x version is minimal — see the migration guide.
Deliberately limiting abstractions
In a domain where patterns keep changing, the temptation is to build flexible abstractions that can accommodate anything. Our answer was the opposite: limit abstractions to the strict minimum — while recognizing that this “minimum” is almost always overestimated.
In practice, this translates into a very local approach to code:
- avoid generic class hierarchies
- favor explicit implementations
- accept, and even encourage, duplication
The goal is not to eliminate structure altogether — shared utilities still exist — but to avoid imposing abstractions where the domain itself is not yet stable. For instance, rather than defining a common base class for offline trainers, we prefer independent implementations when their future evolution is uncertain.
# ❌ No
class OfflineTrainer(Trainer):
def some_common_method(self): ...
class DPOTrainer(OfflineTrainer): ...
class KTOTrainer(OfflineTrainer): ...
# ✅ Better
class DPOTrainer(Trainer):
def some_common_method(self): ...
class KTOTrainer(Trainer):
def some_common_method(self): ...
Another example:
# ❌ No
# collator.py
class TRLCollator: ...
# dpo_trainer.py
class DPOTrainer:
def __init__(self, ...):
self.collator = TRLCollator(...)
# kto_trainer.py
class KTOTrainer:
def __init__(self, ...):
self.collator = TRLCollator(...)
# ✅ Better
# dpo_trainer.py
class DataCollatorForPreference: ...
class DPOTrainer:
def __init__(self, ...):
self.collator = DataCollatorForPreference(...)
# kto_trainer.py
class DataCollatorForUnpairedPreference: ...
class KTOTrainer:
def __init__(self, ...):
self.collator = DataCollatorForUnpairedPreference(...)
Judges are a good example of what happens when we don’t follow this principle. Early on, we introduced a Judge
abstraction to unify the various ways of evaluating model outputs. It looked reasonable at the time. In practice, it was never really used — the abstraction didn’t match how people actually approached evaluation, and it added indirection without adding value. It still lives in the repo, mostly as legacy. In hindsight, shipping the concrete implementations without the unifying abstraction would have served users better.
More explicit, but more adaptable
This approach favors explicit and modifiable usage over rigid frameworks: less magic, but more control. It comes with an obvious cost: code duplication. While often seen as an anti-pattern, in this context it has proven not only acceptable, but effective. Contrary to intuition, it remains manageable in practice with a small but consistent discipline: keeping deltas between implementations minimal and avoiding unnecessary divergence. Like in the Transformers design philosophy, we accept duplication and local explicitness by design. The motivations largely coincide, with some nuance in focus.
This is easier to see than to describe. Compare RLOO and GRPO: large parts of their implementation are duplicated almost line for line. That is not accidental, and it is not dead weight. These methods are close enough that keeping their code paths aligned makes them easier to read, easier to evolve, and cheaper to maintain.
3. Where TRL fits
The goal of this comparison is not to argue that TRL should be judged as best on every axis. It should not. Some systems are built for maximum throughput (like PipelineRL), some are optimized for a narrower slice of the problem (like LLaMA-Factory), and some offer a more opinionated development experience in a specific environment (like Tinker). TRL occupies a different place in the ecosystem: it is a general-purpose post-training library that tries to keep the API and the code as simple as the domain allows, while combining broad method coverage, deep Hugging Face integration, a relatively low infrastructure burden, and an explicit stability contract.
Libraries like Unsloth and Axolotl are not included here because they build on top of TRL rather than sitting beside it in the comparison; in that sense, many of their users are also TRL users indirectly.
Ecosystem
Training methods
Project health
Some rows are factual (GitHub stars
, Last release
, Last commit
), others are qualitative judgments (Semver stability
).
Taken together, these comparisons point to a clear role for TRL: a general-purpose library designed to keep breadth, simplicity, integration, and stability in the same place. Its full downstream footprint is hard to measure, since most deployments are private and reverse dependencies are largely invisible, but the available signals already show that TRL operates at a distinctly different scale.
4. What’s next
By now, the logic of v1.0 should be clear: it is not a claim that post-training has stabilized. On the contrary, it is an acknowledgment that the field will keep shifting, and that we're confident that the library has the right shape to absorb whatever comes next. The question is not what comes after v1.0, but what’s next for v1.0.
Asynchronous GRPO
Today, GRPO in TRL is primarily used through a synchronous loop: generate rollouts, score them, then step the optimizer. That shape is simple and dependable, but it ties throughput to the slowest stage and leaves performance on the table at scale.
The fix is conceptually simple: generation and training don't need to be lock-stepped. We already have an early asynchronous GRPO design, and the next step is to harden it. The core idea is to decouple generation and training, letting generation run continuously on dedicated inference resources while training consumes a steady stream of scored trajectories, with buffering, backpressure, and clear policy-version accounting. This improves utilization and scales across GPUs and nodes. Other libraries already offer forms of asynchronous RL, but bringing it to TRL would make this style of training available through broader integrations, simpler APIs, and a much lower barrier to adoption.
Graduating methods to stable
The next candidates include KTO and newer distillation trainers such as SDFT, SDPO, and possibly GOLD or GKD. As discussed in Section 2, before moving them to stable, the goal is to minimize code differences across implementations and monitor sustained community interest relative to maintenance cost.
Scaling
TRL supports large-scale training, including multi-node runs and larger models; the next step is to make this path significantly more robust and easier to operate in production. That includes stronger guarantees around distributed stability, clearer scaling defaults, and deeper support for Mixture-of-Experts (MoE), especially expert parallelism, where routing, load balancing, and memory behavior become critical.
Making training legible to agents
Training is still too often driven by vibes. Loss curves go down, reward curves go up, a few samples look better than before, and people convince themselves the run is working. When it fails, they scroll through logs, compare runs by eye, and guess. That is already a weak interface for humans. For agents, it is worse: it is barely an interface at all.
One of the most important directions for TRL is to make training legible to software, not just to people. That means going beyond dashboards and raw metrics to produce explicit signals: is the policy improving, collapsing, over-optimizing the verifier, drifting off-distribution, or plateauing? The goal is for TRL to surface these patterns automatically, explain them clearly, and turn them into actions.
The plan is to embed heuristics directly into the training loop and emit structured, actionable warnings — the kind a beginner can act on immediately and an agent can parse:
[TRL] WARNING: VRAM utilization at 34%. Consider increasing per_device_train_batch_size from 4 to 16.
...
[TRL] WARNING: Group reward std is 0.01 (near zero). Advantage signal has collapsed. Consider revisiting your reward function to ensure it provides sufficient variance for learning.
...
[TRL] WARNING: Clip ratio outside [0.8, 1.2] for 43% of updates. Consider reducing the learning rate.
Not just logging what happened — reasoning about what it means and what to do next. Useful for beginners who need guardrails, and for agents that need a training stack they can actually automate.
5. Conclusion
Post-training doesn't converge. It shifts, and the next shift is already coming.
v1.0 is not a claim that things have settled. It's an acknowledgment that they haven't yet, and a commitment that the library can be relied on anyway. Six years of evolving alongside the field — and alongside the hundreds of contributors who made it possible — shaped a design we're confident is ready for what comes next, whatever that turns out to be. The community and the downstream projects had already assumed that stability — v1.0 makes it real.
pip install --upgrade trl
Migration from the last 0.x release is minimal, and the migration guide covers everything. If you're new, now is a good time to start.
```

---

## 27. Liberate your OpenClaw

- 日期: 2026-03-27 00:00
- 链接: https://huggingface.co/blog/liberate-your-openclaw

```
Liberate your OpenClaw 🦀
If you've been cut off and your OpenClaw, Pi, or Open Code agents need resuscitation, you can move them to open models in two ways:
- Use an open model served through Hugging Face Inference Providers.
- Run a fully local open model on your own hardware.
The hosted route is the fastest way back to a capable agent. The local route is the right fit if you want privacy, zero API costs, and full control.
To do so, just tell your claude code, your cursor or your favorite agent: help me move my OpenClaw agents to Hugging Face models, and link this page.
Hugging Face Inference Providers
Hugging Face inference providers is an open platform that routes to providers of open source models. It’s the right choice if you want the best models or you don’t have the necessary hardware.
First, you’ll need to create a token here. Then you can add that token to openclaw
like so:
openclaw onboard --auth-choice huggingface-api-key
Paste your Hugging Face token when prompted, and you’ll be asked to select a model.
We’d recommend GLM-5 because of its excellent Terminal Bench scores, but there are thousands to chose from here.
You can update your Hugging Face model at any time entering its repo_id
in the OpenClaw config:
{
agents: {
defaults: {
model: {
primary: "huggingface/zai-org/GLM-5:fastest"
}
}
}
}
Note: HF PRO subscribers get $2 free credits each month which applies to Inference Providers usage, learn more here.
Local Setup
Running models locally gives you full privacy, zero API costs, and the ability to experiment without rate limits.
Install Llama.cpp, a fully open source library for low resource inference.
# on mac or linux
brew install llama.cpp
# on windows
winget install llama.cpp
Start a local server with a built-in web UI:
llama-server -hf unsloth/Qwen3.5-35B-A3B-GGUF:UD-Q4_K_XL
Here, we’re using Qwen3.5-35B-A3B, which works great with 32GB of RAM. If you have different requirements, please check out the hardware compatibility for the model you're interested in. There are thousands to choose from.
If you load the GGUF in llama.cpp, use an OpenClaw config like this:
openclaw onboard --non-interactive \
--auth-choice custom-api-key \
--custom-base-url "http://127.0.0.1:8080/v1" \
--custom-model-id "unsloth-qwen3.5-35b-a3b-gguf" \
--custom-api-key "llama.cpp" \
--secret-input-mode plaintext \
--custom-compatibility openai
Verify the server is running and the model is loaded:
curl http://127.0.0.1:8080/v1/models
Which path should you choose?
Use Hugging Face Inference Providers if you want the quickest path back to a capable OpenClaw agent. Use llama.cpp
if you want privacy, full local control, and no API bill.
Either way, you do not need a closed hosted model to get OpenClaw back on its feet!
```

---

## 28. A New Framework for Evaluating Voice Agents (EVA)

- 日期: 2026-03-24 02:01
- 链接: https://huggingface.co/blog/ServiceNow-AI/eva

```
A New Framework for Evaluating Voice Agents (EVA)
Introduction
Conversational voice agents present a distinct evaluation challenge: they must simultaneously satisfy two objectives — accuracy (completing the user's task correctly and faithfully) and conversational experience (doing so naturally, concisely, and in a way appropriate for spoken interaction). These objectives are deeply intertwined: mishearing a confirmation code renders perfect LLM reasoning meaningless, a wall of options overwhelms a caller who can't skim spoken output, and delayed responses can pass every accuracy check while remaining unusable in practice. Existing frameworks treat these as separate concerns — evaluating task success or conversational dynamics, but not both.
We introduce EVA, an end-to-end evaluation framework for conversational voice agents that evaluates complete, multi-turn spoken conversations using a realistic bot-to-bot architecture. EVA produces two high-level scores, EVA-A (Accuracy) and EVA-X (Experience), and is designed to surface failures along each dimension. EVA is the first to jointly score task success and conversational experience. We release EVA with an initial airline dataset of 50 scenarios covering flight rebooking, cancellation handling, vouchers, and more — the first in a planned series of domains.
We also provide benchmark results for 20 cascade and audio-native systems, such as speech-to-speech (S2S) models and Large Audio Language Models (LALMs). Our biggest finding is that there is a consistent Accuracy-Experience tradeoff; agents that perform well on task completion tend to deliver worse user experiences, and vice versa.
- 🌐 Website — Explore the full framework, early results, and a demo.
- 💻 GitHub — Dive into the code, framework, and judge prompts.
- 📂 HF Dataset - Explore the dataset
Background and Motivation
The field currently lacks a framework that evaluates the full quality of voice agent interactions, as most existing efforts assess individual components in isolation. For example, AudioBench, SD-Eval, VoxEval, Kimi-Audio-Evalkit, VoiceBench and VoxDialogue evaluate core speech understanding capabilities for Speech-to-Text (STT) — transcription, paralinguistics, acoustic cues — but remain confined to single-turn, non-interactive settings. On the other hand, EmergentTTS-Eval and SHEET assess perceived speech quality using subjective listening tests (e.g., Mean Opinion Score). Beyond speech perception, FD-Bench, Talking Turns, Full-Duplex-Bench provide deeper analyses of conversational dynamics — interruptions, backchanneling, turn-taking — yet evaluate these in isolation from task-oriented tool use, leaving the relationship between dialogue quality and agentic capability unexamined. More recent efforts, notably VoiceAgentBench and CAVA, take steps towards evaluating the agentic capabilities of commercial voice agent systems, including tool-calling and complex instruction-following. However, these voice-agentic capabilities are not evaluated within complete conversational workflows that voice agents must navigate in practice: from initial user request through multi-step tool orchestration to final task resolution.
The lack of frameworks that jointly capture accuracy and experience underscores the need for a framework that treats voice agent quality as an integrated whole. This means evaluating not only whether the task succeeded, but whether the agent communicated accurately, concisely, and naturally throughout, and surfacing how these dimensions trade off against one another in realistic deployment conditions.
EVA
The Framework
End-to-end evaluation reveals interaction dynamics that are not apparent at the component level: whether the agent interrupts users during natural pauses in speech, whether it recovers smoothly when a user corrects a transcription error, or whether high latency disrupts the conversational flow enough to prompt users to repeat themselves or abandon the task entirely.
EVA simulates multi-turn spoken conversations over live audio in which the agent must invoke appropriate tools, adhere to task-specific policies, and reach a deterministically verifiable end state. EVA evaluates voice agents using a bot-to-bot audio architecture composed of five core components:
User Simulator — A conversational AI configured with a specific goal and persona that plays the role of a caller. It operates in audio using high-quality Text-to-Speech (TTS) models, ensuring the evaluation captures representative speech-understanding challenges in natural-sounding conversational speech and realistic turn-taking dynamics.
Voice Agent — The voice agent being evaluated, built with Pipecat, an open-source Python framework for real-time voice applications. EVA supports both cascade architectures (STT → LLM → TTS) and audio-native models (S2S or LALM → TTS).
Tool Executor — The engine that provides deterministic, reproducible tool responses via custom Python functions. It dynamically queries and modifies a predefined per-scenario database.
Validators — A set of validation metrics that check that conversations are complete and that the user faithfully reproduced the intended behavior and speech, with no human annotation required. Any conversation that fails in this validation step is regenerated, ensuring that only valid, correctly executed conversations enter evaluation. This stands in contrast to approaches that rely on post-hoc human labeling to identify simulator errors.
Metrics Suite — A suite of metrics evaluates the voice agent using the conversation recording, transcript, and tool call logs.
Data
Each test case (scenario) in our framework is an evaluation record, structured to make tests reproducible:
- User Goal — What the caller is trying to accomplish. Includes a highly specific user objective with an exact decision tree that guides the user simulator through the conversation, leaving no ambiguity about the intended outcome.
- User Persona — How the caller should behave — their speaking style, patience level, and personality traits.
- Scenario Database — The backend data the agent's tools will query.
- Ground Truth — The expected final state of the scenario database after a successful conversation.
We release EVA with a synthetic airline dataset of 50 scenarios and 15 tools, spanning IRROPS rebooking, voluntary itinerary changes, cancellations, same-day standby, and compensation vouchers. Scenarios are designed to test temporal reasoning, policy-following, constraint satisfaction, and named-entity handling.
See the full demo here.
Evaluation Methodology
EVA evaluates voice agents across two fundamental dimensions, EVA-A for accuracy, and EVA-X for experience. EVA also includes a set of diagnostic metrics. Unlike the primary metrics, these are not used directly to compare or rank models — rather, they offer granular insight into why a model scores the way it does, helping identify and understand specific failure modes (e.g., ASR, speech synthesis, etc.). We report pass@k (the probability that at least one of k runs succeeds) and pass^k (the probability that all k runs succeed) across three trials per scenario (k = 3), capturing both peak performance and behavioral consistency.
EVA uses two evaluation methods: deterministic code-based metrics, which compute scores directly from structured data and are fast; and LLM-as-Judge metrics, which use Large Language Models (LLMs) to assess qualitative aspects of the conversation, or Large Audio Language Models (LALM) to evaluate speech directly. Each judge-based metric uses the model that performs best on a curated evaluation dataset for that specific metric.
EVA-A: Accuracy
Task completion alone is a necessary but insufficient measure of accuracy. An agent can reach the correct end state while fabricating a policy detail, misreading a confirmation code aloud, or hallucinating a flight number mid-conversation. These failures are invisible to a binary pass/fail check but directly harm users. EVA-A therefore measures three dimensions of accuracy:
- Task Completion [Deterministic] — Measures whether the agent correctly completed the task by comparing the expected end state of the scenario database against the actual end state after the conversation.
- Faithfulness [LLM-as-Judge] — Measures whether the agent's responses were grounded in its instructions, policies, user inputs, and tool call results — flagging fabrications, misrepresentations, policy violations, and hallucinations.
- Speech Fidelity [LALM-as-Judge] — Measures whether the speech system faithfully reproduced the intended text in spoken audio, with particular focus on entities critical to get right in a voice context, such as confirmation codes, flight numbers, and dollar amounts. This is the only metric in any end-to-end voice agent benchmark that evaluates the quality of the agent's own spoken output at the audio level.
EVA-X: Experience
Turn-taking timing matters, but it tells only part of the story. An agent can have perfect timing while overwhelming a caller with a wall of spoken options they cannot skim, or repeatedly asking for information already given. These failures degrade the experience without ever involving a mistimed response. EVA-X therefore measures three dimensions of experience:
- Conciseness [LLM-as-Judge] — Measures whether the agent's responses were appropriately brief and focused for spoken delivery, since phone users cannot skim, re-read, or scroll back through long responses.
- Conversation Progression [LLM-as-Judge] — Measures whether the agent moved the conversation forward effectively — avoiding repetition, retaining context across turns, and driving toward task completion without stalling.
- Turn-Taking [LLM-as-Judge] — Measures whether the agent spoke at the right time — neither interrupting the user nor introducing excessive silence after they finish speaking.
Findings
We evaluated 20 systems — proprietary and open-source, cascade and audio-native — and find a consistent accuracy-experience tradeoff: agents that perform well on task completion tend to deliver worse user experiences, and vice versa — a tradeoff invisible to benchmarks that score only task completion. No single configuration dominates both axes, confirming that accuracy and experience must be measured jointly.
Additionally, we identified named entity transcription as a dominant failure mode. A single misheard character can cascade into an authentication failure and a full conversation breakdown. Also, multi-step workflows break agents in predictable ways. Rebooking a flight while preserving ancillary services — seats, baggage — is the dominant complexity breaker across all configurations. Finally, we observed that additional calibration is needed for real-world use cases. The gap between pass@3 and pass^3 is substantial across all configurations. Even agents that can complete a task often cannot do so consistently, which is critical for real-world success.
View the early results here.
Limitations
EVA is designed to provide rigorous, end-to-end evaluation of conversational voice agents, but several limitations are important to acknowledge, across the framework, data, and metrics dimensions:
Metrics — LLM-as-judge models carry inherent biases and may favor certain response styles independent of quality, with additional risk of systematic bias when the evaluated and judge models share a provider. While we validate our judges against labeled datasets and report accuracy measurements on our website, these alignment scores do not eliminate systematic bias entirely. Additionally, task completion is measured as binary, which does not capture partial credits and may understate the relative quality of systems that fail gracefully versus catastrophically.
Simulation — The current release covers 50 English-language scenarios in a single domain (airline); results may not generalize to other domains, languages, or accents. Also, the user simulator may not perfectly replicate real caller behavior (e.g., disfluencies, hesitations, emotions) or guarantee full policy adherence.
Framework — The user simulator relies on a single commercial provider whose voice characteristics may systematically favor certain ASR systems, and the bot-to-bot pipeline — including audio format conversions and real-time audio interfaces — may not fully represent production deployments. Also, full reproduction requires commercial API access, and latency measurements will vary across providers and infrastructure.
What's Next
On the evaluation side, we plan to add prosodic quality assessment (pronunciation, rhythm, expressiveness) — currently an open problem after finding very low alignment between LALM-as-Judge and human judgments. We also plan robustness testing under noisy conditions, diverse accents, multilingual users, and varied speaker behaviors, alongside affect-aware evaluation of how agents respond to user distress. In terms of data, we are developing additional domain datasets — each with distinct policy structures, named entity profiles, and conversational dynamics — and more complex scenarios involving compound requests, multi-step follow-ups, and longer conversational memory. On the tooling front, we will release a results and error analysis application that automatically identifies errors per metric and model, surfaces representative examples for exploration, and generates structured summaries of each model’s strengths and weaknesses. Finally, we intend to expand the leaderboard continuously to provide an up-to-date assessment of voice agent capabilities across the field.
View more details about limitations and our upcoming roadmap here.
Acknowledgements
Core contributors include Tara Bogavelli, Gabrielle Gauthier Melançon, Katrina Stankiewicz, Oluwanifemi Bamgbose, Hoang Nguyen, Raghav Mehndiratta, and Hari Subramani.
We also thank Lindsay Brin, Akshay Kalkunte, Joseph Marinier, Jishnu Nair, and Aman Tiwari for their careful data review and thoughtful contributions to the framework, and Fanny Riols, Anil Madamala, Sridhar Nemala, and Srinivas Sunkara for their management, leadership, and support throughout. We also extend our thanks to the PAVA and CLAE ServiceNow teams, whose prior work on evaluations and voice agents provided valuable inspiration for this project.
Citation
@misc{eva-2026,
title={A New End-to-end Framework for Evaluating Voice Agents (EVA)},
author={Bogavelli, Tara and Gauthier Melançon, Gabrielle and Stankiewicz, Katrina and Bamgbose, Oluwanifemi and Nguyen, Hoang and Mehndiratta, Raghav and Subramani, Hari},
year={2026},
url={https://github.com/ServiceNow/eva}
}
```

---

## 29. Build a Domain-Specific Embedding Model in Under a Day

- 日期: 2026-03-20 19:38
- 链接: https://huggingface.co/blog/nvidia/domain-specific-embedding-finetune

```
Build a Domain-Specific Embedding Model in Under a Day
With a single GPU and less than a day of training time, you can transform a general-purpose embedding model into one that truly understands your domain, no manual labeling required. To help you hit the ground running, we are also releasing a ready-to-use synthetic training dataset generated from NVIDIA's public documentation using this exact pipeline. Using this data and the recipe, we saw over 10% improvement in both Recall@10 and NDCG@10. Atlassian applied this recipe to fine-tune on their JIRA dataset, increasing Recall@60 from 0.751 to 0.951, a 26% improvement - on a single GPU.
🔗Quick Links to Dataset and Code:
🧑💻Open Source Projects Recipe Integrates:
- NeMo Data Designer for synthetic data generation
- NeMo Automodel for embedding model training
- BEIR for Information retrieval evaluation
- NeMo Export-Deploy for ONNX/TensorRT conversion
- NVIDIA NIM for production inference serving
📋Prerequisites:
- A directory of domain documents (text files - .txt, .md, or similar)
- A valid NVIDIA API key (free at build.nvidia.com)
- NVIDIA Ampere GPU or newer with at least 80GB memory (with Compute Capability >= 8.0)
- This tutorial has been tested on 1xA100 (80GB), and 1xH100 (80GB)
By the end of this post, you’ll know how to:
📄 Generate training data from domain documents without labeled data
🎯 Use hard negative mining for effective contrastive training
🔗 Improve embedding quality with multi-hop queries
⚙️ Fine-tune a bi-encoder embedding model
📊 Evaluate whether fine-tuning improves retrieval
🚀 Deploy the fine-tuned model in your pipeline
⚙️Setup
In this tutorial, we will finetune the base model Llama-Nemotron-Embed-1B-v2 - a 1-billion-parameter embedding model that balances quality and inference cost. To get started, follow this setup guide.
📚 Step 1: Generate Training Data from Documents
Fine-tuning an embedding model requires thousands of (query, relevant document) pairs. Most use cases don’t have this data readily available. Creating it manually is expensive, slow, and often biased by the annotator’s personal interpretation of what’s “relevant.”
Instead of labeling data by hand, you can use an LLM (nvidia/nemotron-3-nano-30b-a3b) to read your documents and automatically generate high-quality synthetic question–answer pairs.
nemotron embed sdg -c default corpus_dir=./data/my_domain_docs
How does it work?
Behind the scenes, this runs a four-stage synthetic data generation (SDG) pipeline powered by NeMo Data Designer:
What does the output look like?
Source document chunk:
The thermal design power (TDP) of the H100 GPU is 700W in SXM form factor. The cooling solution must maintain junction temperature below 83°C under sustained workloads. Liquid cooling is recommended for dense deployments exceeding 4 GPUs per node, as air cooling cannot dissipate sufficient heat in standard 2U chassis configurations.
Generated QA pairs:
{
"question": "What cooling approach is recommended when deploying more than 4 H100 GPUs per server node?",
"answer": "Liquid cooling is recommended for dense deployments exceeding 4 GPUs per node, as air cooling cannot dissipate sufficient heat in standard 2U chassis configurations.",
"query_type": "contextual",
"reasoning_type": "factual",
"question_complexity": 3,
"segment_ids": [1],
"quality_score": 8.5
}
{
"question": "How does the 700W TDP of the H100 SXM constrain the choice between air and liquid cooling in multi-GPU configurations?",
"answer": "The 700W TDP generates substantial heat that must be dissipated to keep junction temperatures below 83°C. In dense configurations exceeding 4 GPUs per node, air cooling in standard 2U chassis cannot handle this thermal load, making liquid cooling necessary.",
"query_type": "multi_hop",
"reasoning_type": "causal",
"question_complexity": 4,
"segment_ids": [1, 2],
"hop_count": 2,
"quality_score": 9.0
}
Notice the difference: the first question is a simple factual lookup. The second requires multi-hop, causal reasoning. The pipeline generates both types, with configurable complexity levels (2–5) and hop counts (1–3). Each QA pair then undergoes quality evaluation, receiving sub-scores for relevance, accuracy, context support, and clarity, along with an overall score. Only pairs that meet the threshold are included in training.
⛏️ Step 2: Mine Hard Negatives (and Why They Matter)
If you train an embedding model with only positive pairs (query + correct document), it learns to distinguish obviously different documents but fails on the hard cases — passages that look relevant but are not the right answer. In a real retrieval system, these near-misses are exactly the documents that cause bad answers. Hard negative mining finds these confusing passages so the model can learn to tell them apart.
nemotron embed prep -c default
The above command runs three sub-steps automatically:
2a. Train / Validation / Test Split
The generated QA pairs are split into training (80%) and test (20%) sets. The test set is formatted as a BEIR-compatible benchmark for standardized evaluation in Step 5.
2b. Hard Negative Mining
Using the base embedding model, the pipeline:
- Embeds every query and every passage in the corpus.
- Computes similarity between each query and all passages.
- Masks out each query's labeled positive documents.
- Applies a margin filter: any non-positive document scoring above 95% of the minimum positive score is eliminated. This exclusion zone guards against false negatives — unlabeled passages that are so close to the positive they may actually be relevant.
- From the surviving candidates, selects the top-k highest-scoring documents as hard negatives (5 per query by default).
The result: hard negatives are the most similar non-positive passages that still fall safely below the positive-score ceiling. They are passages the current model considers highly relevant but that are not the labeled answer.
Why this works: Training on easy negatives (completely unrelated passages) teaches the model nothing new. Training on hard negatives forces it to learn the subtle distinctions that matter in your domain. For example, in a medical corpus, a question about "metformin dosage for Type 2 diabetes" might have hard negatives about "metformin side effects" or "insulin dosage for Type 1 diabetes" — close but critically different. The 95% margin ceiling prevents the miner from selecting passages that are too close to the positive, which could actually be correct answers that simply weren't labeled during SDG.
2c. Multi-Hop Unrolling
Multi-hop questions reference multiple positive documents. For example, a question like "How does the thermal management system in Section 3.2 relate to the power constraints described in Section 5.1?" has two positive passages.
Unrolling creates one training example per (query, positive document) pair, so the contrastive loss sees each positive independently. A question with 2 positive documents becomes 2 training examples, each with the same hard negatives but a different positive.
The final output is a training-ready JSON file:
{
"question_id": "q42_0",
"question": "How does the thermal management system in Section 3.2 relate to the power constraints described in Section 5.1?",
"pos_doc": [{"id": "Section 3.2"}],
"neg_doc": [{"id": "d_x7y8z9"}, {"id": "d_m4n5o6"}, {"id": "d_p1q2r3"}, {"id": "d_s4t5u6"}, {"id": "d_v7w8x9"}]
},
{
"question_id": "q42_1",
"question": "How does the thermal management system in Section 3.2 relate to the power constraints described in Section 5.1?",
"pos_doc": [{"id": "Section 5.1"}],
"neg_doc": [{"id": "d_x7y8z9"}, {"id": "d_m4n5o6"}, {"id": "d_p1q2r3"}, {"id": "d_s4t5u6"}, {"id": "d_v7w8x9"}]
}
🔍 Step 3: Understand Multi-Hop Questions and Why They Improve Retrieval
Standard embedding fine-tuning generates one question per passage and trains the model to match them. This works for simple factual lookups, but real users ask complex questions that span multiple documents or sections. If the model has only seen single-hop training data, it will struggle to retrieve all the relevant passages for these complex queries.
The SDG pipeline generates questions at 1 to 3 hops by default:
- 1-hop: "What is the TDP of the H100 SXM?" — answered by a single passage.
- 2-hop: "How does the H100's TDP relate to cooling requirements in dense deployments?" — requires connecting information from two passages.
- 3-hop: "Given the TDP, cooling constraints, and rack density limits, what is the maximum number of H100 GPUs deployable in a standard data center row?" — synthesizes three passages.
Each hop is tracked with its own context summary and segment IDs, so the training data preserves the full reasoning chain. After unrolling (Step 2c), each (question, relevant passage) pair becomes an independent training signal, teaching the model that all of these passages are relevant to the multi-hop query.
The fine-tuned model learns to retrieve contextually related documents, not just lexically similar ones.
🧠 Step 4: Fine-Tune the Embedding Model
nemotron embed finetune -c default
How contrastive learning works
The training uses a biencoder architecture with contrastive loss.
The temperature of 0.02 is deliberately aggressive, it produces a very sharp probability distribution. This works well because the hard negatives from Step 2 are high-quality: they are genuinely confusing passages that the model needs strong gradients to learn to distinguish.
Key hyperparameters
Checkpoint frequency
If ckpt_every_steps
is omitted from the config, checkpoint frequency is set automatically:
- Map-style datasets (known length): defaults to once per epoch.
- Iterable datasets (unknown length): defaults to twice during training.
This means you can start with a small corpus (50–100 documents) for a quick proof-of-concept and scale up later without manually tuning checkpoint settings.
📈 Step 5: Measure the Improvement
Did fine-tuning actually help? Let’s find out by running a standardized evaluation comparing the base model against the fine-tuned checkpoint on the held-out test set:
nemotron embed eval -c default
The evaluation uses the BEIR framework and computes four standard information retrieval metrics at k = 1, 5, 10, and 100:
- nDCG@k: Ranking quality — are the best documents ranked highest?
- Recall@k: Coverage — what fraction of relevant documents appear in the top k?
- Precision@k: Accuracy — what fraction of the top k results are actually relevant?
- MAP@k: Average precision across all queries
A successful fine-tune typically results in a 10% improvement in nDCG@10 and Recall@10 within <1 day.
Results using Retrieval Synthetic NVDocs:
📊 Comparison (Base -> Fine-tuned)
============================================================
NDCG:
NDCG@1: 0.55178 → 0.60796 (+0.05618, +10.2%)
NDCG@5: 0.51894 → 0.57689 (+0.05795, +11.2%)
NDCG@10: 0.55506 → 0.61559 (+0.06053, +10.9%)
NDCG@100: 0.60617 → 0.66567 (+0.05950, +9.8%)
Recall:
Recall@1: 0.28478 → 0.31547 (+0.03069, +10.8%)
Recall@5: 0.54486 → 0.60288 (+0.05802, +10.6%)
Recall@10: 0.62979 → 0.69296 (+0.06317, +10.0%)
Recall@100: 0.81421 → 0.87020 (+0.05599, +6.9%)
What if the numbers don't improve?
The pipeline makes it easy to iterate:
- Low quality scores in SDG? Check your document quality — clean, well-formatted text produces better synthetic data. Try a larger and more powerful LLM.
- Not enough training data? Add more documents to your corpus and re-run Stage 0.
- Overfitting? The default 3 epochs is calibrated for the small example dataset; for most real-world data, 1–2 epochs is enough. Also consider increasing the quality threshold to keep only the best training examples.
- Wrong learning rate? Try double or half of the default learning rate.
🏆 Real-World Results: Atlassian
This recipe has been validated on real enterprise data by Atlassian. They applied this pipeline to fine-tune Llama-Nemotron-Embed-1B-v2 on a public Jira dataset using a single NVIDIA A100 80GB GPU, following the same stages described above
Recall@60 jumped from 0.751 to 0.951 — a 26.7% gain.
The fine-tuned model retrieves the correct document within the top 60 results for 95.1% of queries, up from 75.1% with the base model. For a retrieval system underpinning Jira search, this directly translates into more relevant results for millions of users. Find more details in their blog post Advancing semantic search for millions of Rovo users.
🚀 Step 6: Export and Deploy
A PyTorch checkpoint is great for evaluation but too slow for production. The final two stages convert the model and serve it behind an API.
Export to ONNX / TensorRT
nemotron embed export -c default
This exports the fine-tuned checkpoint to ONNX (opset 17). Optionally, it compiles a TensorRT engine for maximum inference throughput, with configurable optimization profiles for batch size (1–64) and sequence length (3–256):
# ONNX only (runs anywhere)
nemotron embed export -c default export_to_trt=false
# FP8 quantization for further speedup
nemotron embed export -c default quant_cfg=fp8
Deploy with NVIDIA NIM
The exported model is deployed inside an NVIDIA NIM container — a production-ready inference microservice exposing an OpenAI-compatible /v1/embeddings endpoint:
nemotron embed deploy -c default
Once running, any client can call it:
curl -X POST http://localhost:8000/v1/embeddings \
-H "Content-Type: application/json" \
-d '{"input": ["What cooling is needed for 8 H100 GPUs in a 2U chassis?"],
"model": "custom",
"input_type": "query"}'
Because NIM serves an OpenAI-compatible API, you can drop it into any existing RAG pipeline that uses the embeddings API format — no code changes needed.
Verify deployment accuracy
The pipeline includes a NIM accuracy verification step that runs the same BEIR evaluation against the deployed endpoint:
nemotron embed eval -c default eval_nim=true eval_base=false
This catches any accuracy loss from the ONNX/TensorRT conversion. Metrics that match within tolerance (0.03 for @1, 0.01 for @5+) are marked with a check; deviations beyond conversion noise are flagged.
Putting It All Together
The full embedding fine-tuning pipeline can be run in six commands, from raw documents to a deployed model.
# 1. Generate synthetic training data from your documents
nemotron embed sdg -c default corpus_dir=./data/my_docs
# 2. Prepare the training data (split data, mine hard negatives, unroll)
nemotron embed prep -c default
# 3. Fine-tune the embedding model
nemotron embed finetune -c default
# 4. Evaluate the base vs. fine-tuned model
nemotron embed eval -c default
# 5. Export the optimized model
nemotron embed export -c default
# 6. Deploy the model
nemotron embed deploy -c default
Expected time and resources
Total: under a day, with most time being hands-off training. For a small corpus (~500 documents), the entire pipeline completes in about 2–3 hours.
The pipeline can run end-to-end, but each stage can also be executed independently depending on your starting point. For example, if you have raw documents, you can begin with synthetic data generation (SDG), while datasets that already include hard negatives can skip earlier steps and go directly to fine-tuning. Since every stage uses standard formats such as JSON, BEIR, and ONNX, it’s easy to integrate custom components or reuse intermediate outputs in other workflows. The recipe is also flexible in how it runs, supporting execution on a local machine, inside Docker containers, or on Slurm-based clusters.
Try It Yourself
If you have domain documents and some time in your hand, you can generate your first batch of synthetic training data today! The full pipeline - from documents to a deployed, domain-adapted embedding model - runs in under a day on a single GPU. You can start with our ready-made nvidia/Retrieval-Synthetic-NVDocs-v1 dataset to try the pipeline right away. Let us know what you build.
Star the repos for Nemotron, NeMo Data Designer and NeMo Automodel if you find them useful.
```

---

## 30. State of Open Source on Hugging Face: Spring 2026

- 日期: 2026-03-17 16:37
- 链接: https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026

```
State of Open Source on Hugging Face: Spring 2026
This post builds on an earlier analysis conducted mid-2025, available here, which examined what the Hugging Face Community is building. We recommend reading additional perspectives on the open source ecosystem in and outside of Hugging Face from the Data Provenance Initiative, Interconnects, OpenRouter and a16z, and MIT and the Linux Foundation. As the Hugging Face ecosystem is distributed, analyses are a combination of Hugging Face and community members' work, each of which is appropriately credited.
Activity in the open source AI ecosystem has rapidly grown, with the number of users, model, and dataset repositories all close to doubling. In 2025, Hugging Face grew to 13 million users, more than 2 million public models, and over 500,000 public datasets. This growth signals more than increased interest in open source; it reflects a shift toward active participation, with users increasingly creating derivative artifacts such as fine-tuned models, adapters, benchmarks, and applications rather than only consuming pre-trained systems.
Data from Hugging Face | Hugging Face's two million models and counting: Graph and story by AI World
The ecosystem remains highly concentrated. Approximately half of the models on Hugging Face have less than 200 total downloads, and the top 200 most downloaded models, or 0.01% of models, comprise 49.6% of all downloads.
Specialized communities form around particular domains, languages, or problem areas, and often show sustained engagement and reuse even when their overall download counts are modest. Open source AI is best understood as a collection of overlapping sub-ecosystems rather than a single uniform market.
Open Source in Competition
More companies, both large and small, are building on open source. Over 30% of the Fortune 500 now maintain verified accounts on Hugging Face. Startups frequently use open models as default components: Thinking Machines built its Tinker model options entirely on open weights, while popular IDEs such as VSCode and Cursor support both open and closed models. Established American companies such as Airbnb have increased their engagement with the open ecosystem, and Hugging Face has seen more legacy companies upgrading their organizational subscriptions over the course of 2025.
Big Tech companies are frequently creating new repositories on Hugging Face Hub; visualized side-by-side, the strong increase in repository growth shows investment over time. NVIDIA has emerged as the strongest contributor.
Data from Hugging Face | Big Tech Is All-In On Open-Source AI, Graph and story by AI World
Studies of open software more broadly suggest that the downstream value created by open artifacts far exceeds the cost of producing them. Similar dynamics are emerging in AI, where open models are reused, adapted, and specialized across thousands of downstream applications. Organizations that rely exclusively on closed systems often incur higher costs and face reduced flexibility in deployment and customization.
The Geography of Open Source
All-time downloads over the past four years show clear frontrunner regions in model popularity. The U.S. and China have historically been top contributors, with the UK, Germany, and France as secondary in popularity. Models developed by individual users or distributed organizations without a clear geographic base account for about half of all platform downloads.
Data from Hugging Face | Graph and Research from Longpre et al. “Economies of Open Intelligence: Tracing Power & Participation in the Model Ecosystem”
The geographic composition of the open source ecosystem has fundamentally changed. Hugging Face data shows China surpassing the U.S. in monthly downloads and overall downloads. In the past year, Chinese models quickly accounted for the plurality or 41% of downloads.
Data and Graph from Hugging Face
Industry's share of overall development fell from around 70% before 2022 to roughly 37% in 2025. Meanwhile, independent or unaffiliated developers rose from 17% to 39% of all downloads over the same period, at times accounting for more than half of total usage. Individuals and small collectives focused on quantizing, adapting, and redistributing base models. These intermediaries now steer a meaningful portion of what typical users can run and how innovations spread through the ecosystem.
Data from Hugging Face | Graph and Research from Longpre et al. “Economies of Open Intelligence: Tracing Power & Participation in the Model Ecosystem”
Different regions contribute in different ways. The United States and Western Europe have historically dominated through large industry labs (Google, Meta, OpenAI, Stability AI), while China has increasingly led on both releases and adoption. France, Germany, and the UK continue to contribute through research organizations, national AI initiatives, and specialized model families. Ecosystems supporting a variety of contributors and organizational forms tend to produce more widely adopted artifacts.
Countries, Organizations, and Individual Users
Popular models from startups were more widespread. Competitive countries were France and South Korea. Notably, the fourth most popular entity for developing new trending models were individual users, not organizations. Creating competitive models at a user level is more accessible than ever before.
Data and Graph from Hugging Face
Between the U.S. and China
Of the newly created models in 2025, the majority of trending models were either developed in China or derivative of a model developed in China. The most popular models were developed by large organizations, predominantly from the U.S. and China. For more on the Chinese AI ecosystem, read our three part series reflecting on the changes in one year since the "DeepSeek Moment", with one on strategic changes, two on architectural changes, and three on organizations and the future.
In 2025, China’s AI ecosystem steered heavily into open source, following the viral release of DeepSeek’s R1 model in January. The number of competitive Chinese organizations releasing models and the number of repositories on Hugging Face skyrocketed. Baidu went from zero releases on the Hub in 2024 to over 100 in 2025. ByteDance and Tencent each increased releases by eight to nine times. Organizations that had previously favored closed approaches, including Baidu and MiniMax, shifted decisively toward open releases.
Data and Graph from Hugging Face
A similar number of popular U.S. organizations have consistently contributed a higher volume of repositories over time. Meta and its former Facebook research organization account for a significant proportion of open releases, as does Google to a lesser extent.
Data and Graph from Hugging Face
Next to each other, the steep upward trajectory of repository growth among popular Chinese organizations emerges as a key strategic difference.
Data and Graph from Hugging Face
Global Open Source and Sovereignty
Open source AI is increasingly tied to questions of sovereignty. Open weight models allow governments and public institutions to fine-tune systems on local data under national legal frameworks. Models that can be deployed on domestic hardware reduce reliance on foreign-controlled cloud infrastructure. Transparency around model architecture, training processes, and evaluation supports regulatory review and public accountability. Read more about the open source approach to sovereignty here.
At the national level, governments are taking action. South Korea's National Sovereign AI Initiative launched mid-2025 named national champions LG AI Research, SK Telecom, Naver Cloud, NC AI, and Upstage to produce competitive domestic models. Three models from South Korea trended simultaneously on Hugging Face Hub in February 2026. In March 2026, In 2026, South Korea and U.S. startup Reflection AI announced a data center partnership, also bringing frontier open weight models to South Korea.
Switzerland's Swiss AI initiative and various EU-funded projects reflect similar priorities. The UK's principle of "public money, public code" has influenced several government-backed AI initiatives.
Hugging Face Trending Page February 2026
These investments in open-source and open weight AI are already paying dividends for countries with thriving AI training ecosystems of their own, as we see that models and datasets are typically most used in the regions where they're developed; with developers often turning to the models that best represent their languages and reflect similar technical and application requirements.
Data and Graph from Hugging Face
Model Popularity
Most liked models on the Hub show community attention, in terms of ability to go back to or reference the model or general popularity. While this metric does not always reflect usage, the attention collected over time can show signals of interest. In one year, the most liked models went from predominantly U.S.-developed from Meta’s Llama family, to an international mix with China’s DeepSeek-R1 at the top.
Data and Graphic from Hugging Face
Papers and Scientific Contributions
While determining the value of scientific contributions can be determined by many metrics, our upvote feature on the Hub shows papers from large AI organizations be widely appreciated by community members. Notably, the most upvoted papers are from large organizations, mostly from the U.S. and China. The majority of the top organizations are Chinese Big Tech companies, with ByteDance sharing a high volume of high impact papers.
Space by Hugging Face | PaperVerse Explorer
Of Hugging Face's Daily Papers, a set of papers curated by Hugging Face's AK, papers that reference model and dataset creation, showing the most open source adoption, are generally diverse. Prominent takeaways show medical papers being influential, while Big Tech's influence is sparse.
Data from Hugging Face | Graphic and story by AI World
Derivative Models
How our community members choose to build on models, whether via fine-tuning, merging, or other methods, reflects model popularity and usability. Alibaba as an organization has more derivative models than both Google and Meta combined, with the Qwen family constituting more than 113,000 derivative models. When including all models that tag Qwen, that number balloons to over 200,000 models.
Data and Graph from Hugging Face
Adoption and Accessibility
Model development has increasingly emphasized accessibility alongside scale. Smaller models are downloaded and deployed at far higher rates than very large systems, reflecting practical constraints around cost, latency, and hardware availability.
This small-model dominance occurs in part because far more models are released at that size. But even when normalizing for this, the data from the ATOM Project's Relative Adoption Metric shows that the median top-10 models from 1-9B parameters are only downloaded about 4x more than models above 100B. Automated systems and CI pipelines further inflate small model download counts, but the trend toward smaller, deployable models is real.
Data from Hugging Face | Graph and Article by ATOM
Engagement with open models tends to peak almost immediately after release, then slow. Mean engagement duration is approximately 6 weeks. Continuous improvement and frequent updates have become critical for maintaining relevance. DeepSeek's successive releases (V3, R1, V3.2) kept it competitive even as challengers emerged. Organizations that stagnate in development tend to lose share quickly to those with frequent updates or domain-specific fine-tunes.
Data from Hugging Face | Graph and Research from Choksi et al. "The Brief and Wondrous Life of Open Models"
The mean size of downloaded open models rose from 827M parameters in 2023 to 20.8B in 2025, driven largely by quantization and mixture-of-experts architectures. The median, however, increased only marginally, from 326M to 406M parameters. This divergence indicates that high-end LLM users are pulling up the mean while underlying small-model usage remains stable.
Data from Hugging Face | Graph and Research from Longpre et al. "Economies of Open Intelligence: Tracing Power & Participation in the Model Ecosystem"
Performance differences between frontier models and smaller systems often narrow rapidly through fine-tuning and task-specific adaptation. On the Hub, models with hundreds of millions of parameters support search, tagging, and document processing workflows, while models in the single-digit billions are widely used for coding, reasoning, and multimodal tasks. As a result, most major model developers now release families of models spanning a range of sizes. The rise of capable small models shifts autonomy closer to the edge, reducing dependency on centralized cloud providers.
Compute, Hardware, and Open Source
Open source AI development is closely linked to hardware trends. Most models are optimized for NVIDIA GPUs, but support for AMD hardware continues to expand. Stability AI model collections now optimize for both NVIDIA and AMD platforms. Libraries increasingly target both, and tooling has improved to make cross-hardware deployment more straightforward. In 2025 Hugging Face launched the Kernel Hub to load and run kernels optimized for NVIDIA and AMD GPUs.
In parallel, Chinese open models are being released with explicit support for domestically developed chips. Alibaba has invested in inference-focused chip architectures designed to fill Chinese data centers with hardware capable of running open source models locally.
While access to compute remains a core necessity across the board for development and deployment of AI models, open-source and open-weight models are helping break away from an ecosystem where it becomes the be-all and end-all, with increasingly more models at all levels of performance pushing efficiency from 10x to 1000x lower costs than flagship AI models the largest developers.
Data and Graphic from Hugging Face
Still, the question of infrastructure investment for open source remains urgent. Public funding for data centers capable of training and serving open models has become a growing policy discussion, particularly in Europe and the UK. The gap between the compute resources available to large closed-model companies and those accessible to the open source community continues to shape what is feasible in open development.
Sub-Communities: Robotics
Robotics has emerged as one of the fastest-growing sub-communities on Hugging Face. The numbers are striking: robotics datasets grew from 1,145 in 2024 to 26,991 in 2025, climbing from rank 44 to the single largest dataset category on the Hub in just three years. For comparison, text generation, the second-largest category, had only around 5,000 datasets in 2025.
Data from Hugging Face | Graph and Story by AI World
Community-contributed datasets span everything from household manipulation tasks to autonomous driving. The largest multimodal dataset for spatial intelligence, Learning to Drive (L2D), was released through a LeRobot collaboration with Yaak. Datasets like RoboMIND, with over 107,000 real-world trajectories across 479 distinct tasks and multiple robot embodiments, provide the kind of scale and diversity needed for training generalizable robotic policies.
Hugging Face's acquisition of Pollen Robotics opened open source robotic sales to both industry and academic labs, as well as everyday hobbyists. LeRobot, Hugging Face's open source robotics library that provides models, datasets, and tools for real-world robotics in PyTorch, covering imitation learning, reinforcement learning, and vision-language-action models, experienced rapid growth. Over the past year, its GitHub repository stars nearly tripled.
Data from GitHub | Graphic from star-history.com
Sub-Communities: AI for Science
Scientific research has become another particularly active area. Open models and datasets are increasingly used for protein folding, molecular dynamics, drug discovery, and scientific data analysis. All frontier AI companies now have dedicated science teams, though much current focus remains on literature discovery rather than direct experimentation.
Space by Hugging Face | Science Release Heatmap
Community-led projects have formed around shared research goals, often involving hundreds of contributors working across institutions and disciplines. These efforts highlight the role of open source as a mechanism for coordinating large-scale, interdisciplinary work that would be difficult to organize through traditional academic or corporate structures alone.
Looking Forward
The open source AI ecosystem continues to evolve through a combination of global participation, technical specialization, and institutional adoption. Several trends are likely to define the next phase.
The geographic rebalancing of power is accelerating. Western organizations increasingly seek commercially deployable alternatives to Chinese models, creating urgency around efforts like OpenAI's GPT-OSS, AI2's OLMo, and Google's Gemma to offer competitive open options from US and European developers. Whether these efforts can match the adoption momentum of Qwen and DeepSeek will be a defining question of 2026.
The growth of sub-communities in robotics and science suggests that open source AI is expanding beyond language and image generation into the physical and experimental domains. The infrastructure, norms, and coordination mechanisms developed around text and image models are being adapted for new modalities and use cases.
For researchers, developers, companies, and governments, open source remains a foundational layer for building, evaluating, and governing AI systems. With increasing agent deployments, open-source and its interoperability will be key for agents to thrive. Its trajectory over the past year makes one thing clear: the open source ecosystem is where much of the practical work of AI development, adaptation, and deployment takes place, and its influence on the broader AI landscape continues to grow.
Thank you to the Hugging Face community for continuing to build the foundation of the AI ecosystem 🤗
If you want to cite this blog post, you may use the following BibTeX:
@misc{hf_state_of_os_spring26,
author = {Avijit Ghosh and Lucie-Aimée Kaffee and Yacine Jernite and Irene Solaiman},
title = {State of Open Source on Hugging Face: Spring 2026},
booktitle = {Hugging Face Blog},
year = {2026},
url = {https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026},
}
```

---
