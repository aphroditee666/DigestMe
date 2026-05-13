# Hacker News LLM

> 分类: AI专题
> URL: https://hnrss.org/newest?q=LLM
> 抓取: 20 篇

---

## 1. Adola: Reducing LLM input tokens by 70%

- 日期: 2026-05-09 15:42
- 链接: https://adola.app/

```
0% decrease
same accuracyKeep what matters.
Rose 1 trims noisy context before your model call and keeps the answer intact.
See the APIfrom adola import Adola client = Adola(api_key="adola_live_...") result = client.compress( input=open("retrieved_context.txt").read(), query="Which incident caused latency?", compression={"target_ratio": 0.3}, include_spans=False, ) compressed = result["output"] receipt = result["receipt"]
Quickstart.
Compress context before the model call. Use the returned text in your next request.
Open docsQuality first, savings second.
Rose 1 cuts context hard while keeping answers stable across reasoning, science, and math checks.
Hard questions, shorter prompts.
No measured drop with 70% compression.
0% decrease
same accuracy0% decrease
same accuracy2% decrease
near match0% decrease
same accuracy0% decrease
same accuracyThe production shell is already wired.
Use Adola where context piles up: agent traces, retrieval, prompt gateways, and support copilots. The same workspace gives those flows keys, receipts, billing, and deployable services.
Agent traces
Trim long tool transcripts before the next planning step.
RAG retrieval
Shrink over-retrieved chunks while keeping the answer-bearing spans.
Prompt gateways
Add a compression hop without changing model providers.
Support copilots
Compress ticket history, policy docs, and account context.
For teams that need smaller prompts without turning the model blind.
Start compressing.
Create a workspace, issue a project key, run the playground, and measure what comes out.
```

---

## 2. SubQ: A New LLM with a 12M Token Context That Rivals Claude and ChatGPT

- 日期: 2026-05-09 15:31
- 链接: https://felloai.com/subq-llm-review/

```
On May 5, 2026, a Miami-based startup called Subquadratic came out of stealth with $29 million in seed funding and a single, very loud claim: it has built the first frontier LLM that does not rely on quadratic attention. Its model, SubQ, ships with a 12 million token context window, runs roughly 52x faster than FlashAttention at 1 million tokens, and costs about a fifth of what Claude Opus or GPT-5.5 charge for comparable workloads.
If those numbers hold up, this is the most significant architectural shift in language models since the original 2017 transformer paper. If they do not, it joins a long list of subquadratic experiments that promised the world and quietly underperformed at scale.
This review walks through what SubQ actually is, how its Subquadratic Sparse Attention (SSA) mechanism works, what the benchmarks show, what credible researchers are skeptical about, and how to think about it if you build with AI today.
Key Takeaways
- Launched May 5, 2026 by Subquadratic, founded by CEO Justin Dangel and CTO Alex Whedon (former Head of Generative AI at Meta).
- $29M seed round with backers including Justin Mateen (Tinder co-founder), Javier Villamizar (ex-SoftBank Vision Fund), and early investors in Anthropic, OpenAI, Stripe, and Brex.
- 12 million token context window in the research model, 1 million tokens in the production API.
- SSA architecture scales linearly with context length instead of quadratically, cutting attention compute by roughly 1,000x at 12M tokens.
- Benchmarks: 95.0% on RULER 128K, 65.9% on MRCR v2 at 1M tokens, 81.8% on SWE-Bench Verified.
- Three products in private beta: SubQ API, SubQ Code (CLI agent), and SubQ Search (free long-context research tool).
- Skepticism is high. The full technical report has not been released, weights are not open, and prior subquadratic architectures (Mamba, RWKV, DeepSeek Sparse Attention) have repeatedly underperformed transformers at frontier scale.
What SubQ Actually Is
SubQ is a closed-weights large language model trained on a brand new attention mechanism the company calls Subquadratic Sparse Attention, or SSA. Standard transformer attention compares every token in a sequence with every other token. That is what makes it powerful, and it is also what makes context windows expensive. Doubling the input quadruples the compute.
SSA replaces this with content-dependent token selection. For each query token, the model picks a small subset of positions in the sequence that actually matter, then computes exact attention only over those. Compute scales linearly with context length rather than with its square.
This is not the same as the fixed-pattern sparse attention used in Longformer or BigBird, where the sparsity is hardcoded by position. It is also not the state-space approach taken by Mamba or RWKV, which replace attention entirely with recurrent dynamics. SSA keeps attention, but makes it choose where to look.
Subquadratic claims this gives the model three properties at once: linear cost, content-aware routing, and the ability to retrieve from arbitrary positions in the sequence. Until now, sparse attention designs have generally hit two of those three.
How SSA Works
The company published a technical post breaking down the mechanism and the training pipeline. The short version:
- Pre-training establishes base language modeling and long-context representations across very long sequences.
- Supervised fine-tuning layers in instruction-following and code generation behavior.
- Reinforcement learning specifically targets long-context retrieval failure modes, the kind where the model produces a plausible-looking answer that quietly drops the wrong fact from a 200-page input.
The infrastructure piece matters as much as the math. Linear memory scaling and distributed sequence parallelism let Subquadratic train stably on sequences of one million tokens or more, something most labs avoid because the GPU memory cost is brutal under standard attention.
Hardware-wise, the wall-clock speedups they report are measured on Nvidia B200s using FlashAttention-2 as the baseline:
The further out you go, the bigger the gap. At 12 million tokens, Subquadratic claims attention compute drops by almost 1,000x versus standard transformers, which is the headline number being repeated everywhere.
The Benchmark Numbers
Subquadratic released three benchmark results alongside the launch. None are state-of-the-art across the board, but each one tells a slightly different story.
Two things stand out. First, RULER at 128K is essentially saturated, so SubQ matching Opus is more about not regressing than winning. Second, the MRCR and SWE-Bench numbers Subquadratic uses for Opus differ between its press release and its own technical post, which is strange and worth flagging. Either way, SubQ trails Opus on MRCR if you believe the technical post numbers, and beats it if you believe the press numbers.
What is not in dispute is the cost-per-result. On RULER 128K, Subquadratic says SubQ hits 95.0% accuracy at $8 of compute, against roughly $2,600 for Opus to hit 94.8%. That is a 300x cost reduction at the same accuracy, which is the part of the story that matters most for anyone shipping production AI workloads. Our AI pricing comparison covers what that kind of unit-economics shift looks like in practice across the major providers.
What 12 Million Tokens Actually Buys You
A 12M token window is roughly 9 million words, or about 120 books worth of text in one prompt. That is enough to fit:
- An entire mid-sized company codebase, including tests and documentation.
- Every legal filing in a complex case.
- A full year of customer support transcripts for a mid-market SaaS product.
- The entirety of the King James Bible roughly nine times over.
The practical implication, if SubQ delivers, is that retrieval-augmented generation (RAG) becomes optional for a much wider set of problems. Today, almost every serious AI deployment runs a retrieval pipeline because you cannot fit the relevant data into the context. Embed, chunk, rerank, stuff, generate. SubQ’s pitch is that for many of those workloads you can skip that whole stack and just put the documents in.
That does not eliminate RAG, but it does compress the use case. Static knowledge bases, internal codebases, and document review look like the obvious early targets. Real-time data, fast-changing information, and user-specific personalization still need retrieval.
The Three Products
Subquadratic launched three products simultaneously, all in private beta as of May 5.
SubQ API is the developer entry point. It exposes the 1M-token production model through OpenAI-compatible endpoints with tool use support. The 12M context window is gated to research and select enterprise partners for now.
SubQ Code is a CLI coding agent that loads entire codebases into context and reasons across them. Subquadratic also positions it as a long-context layer for existing tools, claiming compatibility with Claude Code, Codex, and Cursor. Their published numbers claim a 25% lower bill and 10x faster exploration when SubQ Code sits underneath those agents. That is the most directly testable claim in the launch and the one most likely to either prove SubQ out or expose it.
SubQ Search is a long-context research tool offered free to consumers. Subquadratic is using it as a land-and-expand wedge against Perplexity and ChatGPT search. The economics presumably work because attention cost at 1M+ tokens is cheap on their stack and brutally expensive on everyone else’s.
Pricing for the API has not been disclosed yet beyond the general claim of being roughly one-fifth the cost of leading frontier models.
Why Researchers Are Skeptical
Within hours of the launch, the AI research community split. The case against SubQ is not personal. It is historical.
Subquadratic attention is one of the most heavily explored areas in machine learning. Mamba, RWKV, Hyena, RetNet, BASED, DeepSeek Sparse Attention, and Kimi Linear all took different swings at the same problem. Each one demonstrated linear scaling on benchmarks. Each one ran into the same wall: pure subquadratic architectures match dense attention at small and medium scale, then visibly underperform on downstream benchmarks at frontier scale, or end up in hybrid configurations that lose the pure scaling benefit.
A widely shared LessWrong post on this lineage argued that nearly all subquadratic claims to date are “incremental improvement number 93595 to the transformer architecture” because practical implementations remain quadratic in the regimes that matter and only improve attention by a constant factor.
Two specific concerns surfaced fast.
AI engineer Will Depue posted that SubQ is “almost surely a sparse attention finetune of Kimi or DeepSeek,” meaning the impressive base model behavior comes from existing open-source weights and the SSA contribution is the sparse attention layer added on top. Subquadratic has not denied or confirmed this, and has not released weights or a full technical report.
AI commentator Dan McAteer captured the binary mood: “SubQ is either the biggest breakthrough since the Transformer or it’s AI Theranos.” That is not a serious technical critique, but it is the right frame for how the field is reading this. Either the model is what Subquadratic says it is, or the gap between marketing benchmarks and production behavior will become visible quickly once outsiders get hands-on.
The clearest path to credibility is the technical report, the weights or detailed architecture description, and independent benchmarks from labs the company does not pay. Subquadratic says all three are coming. They are not here yet.
How SubQ Compares to Other Long-Context Models
Long-context is not a new battlefield. Gemini has shipped 2M token windows for over a year. Claude pushed past 1M last fall. The interesting comparison is on cost-at-context, not raw context length.
The point of comparison is not whether SubQ wins on accuracy. On most benchmarks Opus or Gemini still leads. The point is whether the cost-per-correct-answer at long context is genuinely 50x to 300x lower, because if it is, the choice for any document-heavy or code-heavy workload changes.
What This Means for Builders
For most people shipping product on top of LLMs, here is the practical read.
If SubQ’s claims hold up under independent testing, three things change. RAG becomes optional for many use cases. Codebase-scale coding agents become economically viable. And the model selection layer that products like Fello AI bundle gets one more strong option, since the value of having a single Mac and iPhone interface to every frontier model only grows when the models start specializing on different axes (cost, speed, context, raw reasoning).
If SubQ’s claims do not hold up, the most likely outcome is that the SSA mechanism still ends up being a useful component in hybrid architectures, similar to how mixture-of-experts went from skepticism to standard practice over a few years. The 1,000x number gets walked back, the 50x number probably survives in narrower domains.
The most concrete thing to do today is wait for the technical report, run your own evaluations through SubQ Code on a real codebase you understand well, and treat the marketing benchmarks as a starting point rather than a verdict.
Pricing and How to Access SubQ
All three products are in private beta. Subquadratic is taking access requests through forms on its website. The company has not published a public pricing page yet. Based on launch interviews, expect:
- SubQ API: roughly 1/5 the per-token cost of Claude Opus or GPT-5.5 at comparable context lengths.
- SubQ Code: licensed per developer seat, with the long-context layer pitched as a drop-in cost reducer for teams already using Claude Code, Codex, or Cursor.
- SubQ Search: free to consumers during beta.
If you want to use SubQ alongside other frontier models without juggling separate accounts, an aggregator like Fello AI can sit in front of multiple providers on Mac, iPhone, and iPad. SubQ is not currently available in Fello AI because it is in private beta, but it will be added as soon as it releases publicly, or sooner if early access opens up.
Final Verdict
SubQ is the most architecturally interesting LLM launch since DeepSeek V3, and that is true whether or not the 1,000x number survives contact with independent reviewers. A linear-scaling attention mechanism that holds up on RULER, MRCR, and SWE-Bench is genuinely new, and the team behind it (ex-Meta, Google, Oxford, ByteDance, Cambridge research) is credible enough to take seriously.
The honest read is that the marketing is ahead of the evidence. The gap will close in one of two directions over the next quarter. Either the technical report, the weights, and the independent benchmarks confirm the headline numbers, in which case SubQ permanently changes how long-context AI is built, or the gap becomes the story and SubQ joins the long list of architectures that worked beautifully in a paper and disappointingly in production.
For now, SubQ earns a careful watch, an early-access request if you run long-context workloads, and a healthy dose of “wait for the technical report” before you bet anything serious on it.
FAQ
What is SubQ?
SubQ is a large language model launched May 5, 2026 by Subquadratic, a Miami-based AI startup. It uses a new attention mechanism called Subquadratic Sparse Attention (SSA) and supports a 12 million token context window in its research configuration.
What is Subquadratic Sparse Attention?
SSA is an attention mechanism that scales linearly with context length instead of quadratically. For each query token, the model selects a small subset of positions to attend to based on content rather than fixed patterns, then computes exact attention only over those.
How big is SubQ’s context window?
The research model supports 12 million tokens, roughly 9 million words. The production API exposes a 1 million token context window.
Is SubQ open source?
No. SubQ is closed-weights and not open source. Subquadratic has said a technical report is forthcoming but has not committed to releasing weights.
How does SubQ compare to Claude or GPT?
On long-context benchmarks like RULER 128K, SubQ is competitive with Claude Opus 4.6. On MRCR v2 at 1M tokens, it scores 65.9%, behind GPT-5.5’s 74.0%. The differentiator is cost: Subquadratic claims roughly 300x lower cost at the same accuracy on RULER 128K and 50x lower cost than frontier models at 1M tokens.
Can I use SubQ today?
Access is private beta only. The SubQ API, SubQ Code (CLI agent), and SubQ Search (free research tool) all require an access request through subq.ai. SubQ Search is the easiest entry point.
Is SubQ legit, or hype?
It is too early to say with confidence. The company has published benchmark results and a technical post explaining SSA, but has not released weights, a full technical report, or independent benchmarks. Several researchers, including Will Depue, have publicly questioned whether SubQ is a sparse-attention finetune of an existing open-source model rather than a fully new architecture. Independent verification over the next few weeks will decide it.
```

---

## 3. LLM generated parsers and compliance checkers for Sparrow DSL

- 日期: 2026-05-09 15:13
- 链接: https://news.ycombinator.com/item?id=48075633

```
Hi I believe LLM are really cool in generating DSL code. If one provides well structured and clear prompt. I am the author of Sparrow ( https://github.com/melezhik/Sparrow6/blob/master/documentation/taskchecks.md ) DSL for text parsing and automation with SDK for many programming languages , and I am really impressed how well deep seek generates parsers and compliance checkers for different configuration files - sudoers, sshd, redis, forgejo to name a few. Here are just some examples: - forgejo - https://chat.deepseek.com/share/y3f2om2b6hvzcm752h - redis - https://chat.deepseek.com/share/9eakpdlaa6b88e38u3 - sshd - https://chat.deepseek.com/share/1roo31ihmuz10xjxem - sudoers - https://chat.deepseek.com/share/is2ey6vgbhvdbyqtoa Here are two prompts I use : - With Python SDK - https://gist.github.com/melezhik/d57132c9d3ba0ae9cee30a7c04c98399
- With Raku SDK - https://gist.github.com/melezhik/6f25775aab9f5ec2e22f1193e7ca824b You may choose any of them replace words sshd/forgejo by any word of your interest and try it out with free deep seek chat bot, expert level with browser, have fun PS you’d better try Raku SDK prompt as it handles configuration files with logical groups ( ini style ) as well , but you can easily modify the Python one by stealing the phrasing from Raku prompt 
 Comments URL: https://news.ycombinator.com/item?id=48075633 
 Points: 3 
 # Comments: 0
```

---

## 4. Anthropic NLAs translate LLM activations to human-readable text for safety

- 日期: 2026-05-09 14:54
- 链接: https://presciente.com/edition/78

```
Anthropic's NLAs Decode LLM 'Thoughts,' Improving Claude Safety Anthropic's NLAs Decode LLM 'Thoughts,'
Anthropic's Natural Language Autoencoders (NLAs) translate internal LLM activations into human-readable text, enhancing model interpretability. This method offers direct insights for debugging and safety improvements, particularly for models like Claude. Research also shows LLMs process emotional valence asymmetrically, with negative emotions localized in early layers. Separately, new watermarking techniques like SLAM maintain high detection accuracy with minimal quality loss.
Slow day: 0 thin deep dives and Pulse came up short. We ship what we have, no filler. Back tomorrow.
Yesterday's leadkey Linux LPE and Educational Platform Breach Highlight Systemic Software Vulnerabilities· Ed. 77
- 1
Anthropic Claude operators should pilot Natural Language Autoencoders this week to directly audit internal model activations for safety and reliability improvements.
- 2
RAG system architects should integrate AdaGATE into multi-hop retrieval pipelines by May 15 to enhance evidence selection and reduce token consumption by 15-20%.
- 3
Product managers should evaluate SLAM watermarking for new content generation features launching in Q3 2026, ensuring high detection accuracy with minimal quality degradation.
SLAM's superior watermarking technique presents a clear competitive threat to LLM providers using older methods, especially given its minimal quality loss. Enterprises increasingly require content provenance for AI-generated text. This will drive public acknowledgement or feature parity from major players.
When2Speak offers a clear, material improvement for a recognized weakness in LLMs. Given the rising trend of 'ai agent frameworks' and 'ai agent development,' open-source projects like Haystack and MLflow will quickly adopt this capability to support multi-agent systems.
AdaGATE addresses a limitation of RAG systems on multi-hop questions while materially reducing token costs. This is highly valuable for enterprises, creating strong competitive pressure on major RAG framework vendors. Given rising 'ai orchestration frameworks' and 'llm inference efficiency' trends, this will be a priority.
```

---

## 5. Canvas Data Breach; DeepSeek V4 Flash Boosts LLM Inference 4.3x

- 日期: 2026-05-09 14:08
- 链接: https://presciente.com/edition/77

```
Canvas Data Breach Impacts Education; DeepSeek V4 Flash raises LLM Inference 4.3x DeepSeek V4 Flash Boosts LLM Inference 4.3x
The Canvas educational platform experienced a data breach, with ShinyHunters threatening data release by May 12, 2026, posing compliance risks for Instructure and its clients. Separately, DeepSeek's V4 Flash engine on Metal and the PARSE framework are improving LLM inference, with PARSE achieving 1.25x to 4.3x throughput gains. Telegraph English also offers a semantic prompt compression method, reducing token costs by approximately 50% while maintaining 99.1% accuracy.
0 short dives, Pulse at 1. Out as-is, no polish.
Yesterday's leadOpen-Source Agent Orchestration Shifts to Deterministic Control Flow· Ed. 76
- 1
Instructure Canvas customers must audit their data exposure and prepare for potential data disclosure by May 12, 2026, due to the ShinyHunters breach.
- 2
Platform teams should evaluate DeepSeek V4 Flash and the PARSE framework for LLM inference, aiming for 1.25x to 4.3x throughput gains by Q3 2026.
- 3
AI application developers should pilot Telegraph English's prompt compression to reduce token costs by approximately 50% for prompt-heavy workloads this month.
The 50% token reduction from Telegraph English is a direct attack on the cost structure of any prompt-heavy LLM application. As seen with the rapid adoption of speculative decoding for inference speed, the quickly integrates step-change efficiency gains. Libraries like LangChain or LlamaIndex, which intermediate API calls, are perfectly positioned to offer this as a value-add service to reduce their users' token bills.
ShinyHunters has a documented history of following through on data leak threats to maintain their reputation. The May 12 deadline is extremely aggressive for a large organization like Instructure to navigate internal approvals for a payment. The most probable outcome is the deadline passes, and ShinyHunters leaks the data to make their next threat against a different victim more credible.
```

---

## 6. What if new proofs are included in LLM training so LLM rediscover it?

- 日期: 2026-05-09 08:58
- 链接: https://news.ycombinator.com/item?id=48073325

```
If I were to sell the power of LLMs as powerful research agents, and if I had enough money, I could think about introducing little "gems" into the training set of LLM so that my model would be able to discover new theorems and proofs. There is a lot of money at the table, and I am sure there are a lot of genius people with little pay. Perhaps this kind of thinking is wrong?, only bad people would think like this?, how could one detect such a trick without knowing the training set? 
 Comments URL: https://news.ycombinator.com/item?id=48073325 
 Points: 3 
 # Comments: 1
```

---

## 7. Why LLM-as-judge fails for code evaluation. Here's what works.

- 日期: 2026-05-09 06:45
- 链接: https://navigara.medium.com/the-story-of-navigara-how-we-built-the-performance-layer-for-modern-engineering-d621ffcce6bb

```
Article URL: https://navigara.medium.com/the-story-of-navigara-how-we-built-the-performance-layer-for-modern-engineering-d621ffcce6bb 
 Comments URL: https://news.ycombinator.com/item?id=48072486 
 Points: 2 
 # Comments: 0
```

---

## 8. Meltdown: LLM Client Made in Python and Tk

- 日期: 2026-05-09 02:48
- 链接: https://github.com/Merkoba/Meltdown

```
This is a desktop application to interact with large language models
.
It has hundreds of arguments and commands and many power user features.
It's written 100% in python
and uses tkinter
for the GUI.
- Screenshots
- Installation
- Models
- ChatGPT
- Gemini
- Claude
- Kimi
- Paths
- Profiles
- Input
- Commands
- Tabs
- Markdown
- Snippets
- Find
- Images
- Console
- Listener
- Logs
- Upload
- Signals
- System
- Aliases
- Triggers
- Tasks
- Config
- Args
- Argfile
- Loading
- Prompts
- Palette
- Taps
- Gestures
- Variables
- Files
- Images
- Themes
- Compact
- Autoscroll
- JoinLines
- Pins
- Lockets
- Repeat
- Keywords
- Tips
- Search
- Memory
- Next
- Browser
Note: By default llama.cpp
(local model) support is not installed.
Read below to learn how to enable it.
Also, this has only been tested on linux
.
You can install it with pipx:
pipx install git+https://github.com/Merkoba/Meltdown
That will only enable remote features like ChatGPT
and Gemini
.
But that means the installation is easier and faster.
If you want to enable llama.cpp
support for local models do this:
pipx install git+https://github.com/Merkoba/Meltdown#egg=meltdown[llama]
The difference is #egg=meltdown[llama]
added at the end.
For amd
you might need to install some vulkan
system packages.
To install it with Vulkan
support (GPU), you can do this:
CMAKE_ARGS="-DGGML_VULKAN=on" pipx install git+https://github.com/Merkoba/Meltdown#egg=meltdown[llama]
This is important because the GPU accelerates tokens per second
a lot on local models.
nvidia
GPUs haven't been tested yet.
Intalling with pipx
provides the meltdown
command.
And if on linux
, you should now have a .desktop
entry to launch it.
You can uninstall it with pipx uninstall meltdown
.
To install manually, use a virtual env and requirements.txt
.
You can use scripts/venv.sh
to automate this.
To add local model support run scripts/add_llama.sh
.
There's a scripts/add_llama_amd.sh
to install with Vulkan
support for AMD
.
Or maybe you want scripts/add_llama_amd_rocm.sh
for rocm
.
Pick one of those for local model support.
The llama.cpp
library is defined in llama_reqs.txt
.
These should be called after running venv.sh
as they only add extra libraries.
To run the program, use run.sh
in the root dir.
Try it:
nix run
or nix run .#amd
Install it:
nix profile install
or nix profile install .#amd
Or install properly in your system through your config files.
Read more about llama-cpp-python
.
This is the library used to interface with llama.cpp
.
It is responsible for compiling llama.cpp
.
Local gguf
models can be used.
Here's a good one you can use:
You can find more on that site.
The bigger the model, the longer it will take to load.
llama.cpp
is the inference engine
used, through llama-cpp-python
.
Responses can be instant (when ready) or streamed as new bits arrive.
Streaming can be stopped. Models can be unloaded.
There is an argument to auto unload a model after x mintues.
For example: --auto-unload 60
(1 hour).
ChatGPT from OpenAI is supported.
You must first set the API key for it to work.
This can be done using the model menu.
Or using the openaikey
command.
Then pick a model using the model menu or writing the name directly.
Gemini from Google is supported.
You must first set the API key for it to work.
This can be done using the model menu.
Or using the googlekey
command.
Then pick a model using the model menu or writing the name directly.
Claude from Anthropic is supported.
You must first set the API key for it to work.
This can be done using the model menu.
Or using the anthropickey
command.
Then pick a model using the model menu or writing the name directly.
Kimi from Moonshot is supported.
You must first set the API key for it to work.
This can be done using the model menu.
Or using the moonshotkey
command.
Then pick a model using the model menu or writing the name directly.
Most files are saved in the system's data directory.
In linux this is ~/.local/share
.
The config files are saved in the system's config directory.
In linux this is ~/.config
.
The full paths take into account the name of the program and profile.
For example for a profile called dev
:
Data: ~/.local/share/meltdown/dev
Config: ~/.config/meltdown/dev
In general things inside config
should be "safe" to backup, with minimal personal information.
Data holds all conversations and widget history like input. It also holds API keys. So data should be treated as private.
It's possible to override these paths through arguments.
Using --data-dir
and --config-dir
.
Different profiles can be created and used.
By default it uses the main
profile.
Profiles have independent configs and data.
To launch with a different profile use the --profile
argument.
For example: --profile dev
.
To access the directories where profiles save files, use the /profile
command.
To enter messages for the AI, there is an input at the bottom.
Simply write something and press Enter.
Up/Down arrows can be used to go back to previous inputs used.
Right clicking the input shows recent inputs.
There is a Write
button that opens a popup larger input to write more elaborate prompts.
The Write
popup requires ctrl + Enter
to submit, or use the button.
The input can also be used to run commands.
There is a System Prompt
which you can modify using the main menu
, or with /system
.
The system prompt defines rules that will influence the responses you get.
There are many commands to perform actions.
To use a command you can type them in the input.
For example: /logtext
.
Some commands accept arguments.
For example: /find fun
Commands can be autocompleted with tab
.
Multiple tab
uses cycles between more matches.
Commands do a similarity check, so slightly malformed commands will match if similar enough.
Each conversation is represented by a tab in a horizontal tab bar.
To open a new tab click the New
button, or with /new
,
or double clicking the empty tab bar, or with ctrl + t
, or ctrl + n
.
There are various ways to close tabs:
There is a maximum amount of tabs that can be opened at the same time (configurable).
After that limit is hit (100 by default), you will need to close old tabs to open new ones.
Its advised to not configure this limit to a very big number since problems can arise with many tabs.
The suggested workflow is to close all tabs after a while or closing Old
tabs.
The mousewheel can be used to cycle between tabs and there are some shortcuts and commands for this.
There is also shift + wheel
which you can use in the text output area to cycle tabs.
If ctrl + wheel
is used in the tab bar, it will move/re-order the tabs left/right.
And shift + wheel
can be used to scroll the tab bar without changing the tab.
There is a tab list which shows all the open tabs, which you can type to filter.
This is accessed by right clicking the conversation or with /list
.
When tabs are created they get a short random word for its name.
After the first response from the AI, the name will be updated to a more relevant one.
The name can be renamed by right clicking the tab/conversation, or with /rename
.
Tabs can be moved left/right by dragging them. Multiple tabs can be selected by shift/ctrl clicking them. This allows you to move or close more tabs at the same time.
Tabs can be closed by middle clicking them. Empty tabs won't require a confirmation. The need for confirmations can also be configured through arguments.
When there is a single tab, the tab bar is not shown, as soon as second tab is created, the tab bar is shown. This can be configured, to always show the tab bar, or to never show it.
There is a check that avoid creating new tabs when the last tabs is empty.
Instead it focuses the last empty tab. At the end or at the start.
To disable this you can use --no-keep-empty-tab
.
There is a markdown parser implemented from scratch, no library is used.
It can format the most common cases like bold, italic, quotes, backticks, headers, separators, snippets.
The text output is only parsed when needed, at the end of streams. It is also able to only format the last line added to the textarea. It aims to be as efficient as it can.
Each kind of markdown can be enabled or disabled for user
or ai
. For example bold can be enabled
for only the user, or the ai, or both, or none. This is done through arguments.
Triple backticks produce snippets:
These get colored depending on the language used.
To achieve syntax highlighting, the Pygments
library is used.
There are buttons on the top right to do several actions:
Use
saves a sample of the snippet to the $snippet
variable which can be used on the input.
Explain
directly asks the AI to explain a sample.
Find
finds text inside the snippet.
Select
selects all the text in the snipper.
Copy
copies all the text in the snippet.
There is a find widget that allows searching for text inside conversations.
It can be activated with ctrl + f
or /find
, or f3
.
It can also be accesed through the More
menu.
It supports finding partial words, or whole words (bound).
It supports finding in text sensitive mode, or text insensitive mode.
It supports finding in reverse with shift + enter
, or shift + f3
, or middle clicking the buttons.
There is a command to find in all conversations: /findall
.
It's possible to generate images using Dall-E
.
An OpenAI
key is required for this.
To use it there is the /image
command.
For example: /image powerhouse of the cell
.
It will use the normal streaming mechanisms.
The response, if any, is the full URL
.
Some parts of image generation can be customized through arguments.
To enable the console use --console
.
This allows you to send actions from the terminal that launched the program.
You can enter a simple text prompt, or send a command if the command prefix is used.
It uses prompt_toolkit
and shows autocomplete suggestions with recently used words, or commands.
You could have the main program displayed on a monitor and control it with the terminal in another monitor for instance.
The console is not enabled by default because it can be problematic on certain environments depending on how the program was launched (i.e High CPU usage). But it should work well on normal terminal launches.
There's a listener mode that can be enabled with --listen
.
When the listener is active, it will listen for file changes using watchdog
.
If it finds text, it will use it as the prompt, or as a command if it starts with the command prefix.
It will then empty the file after using it.
You can do for instance echo "hello" > /tmp/mlt_meltdown.input
.
Or: echo "/new" > /tmp/mlt_meltdown.input
.
By default it checks /tmp/mlt_meltdown.input
if on linux.
Temp Dir + mlt_meltdown.input
.
But the file path can also be set with --listen-file
.
This is another way to control the program remotely.
There is a logging system to save conversations to the file system.
It supports output in text
, json
, or markdown
.
To log a conversation you can right click it and select Save Log
.
Or use the commands: /log
, /logtext
, /logjson
, /logmarkdown
.
It's possible to also log all the open conversations (tabs).
By default the logs are saved in the data
directory but it can be configured.
After saving a log, feedback is shown to easily open the file.
Conversations can be uploaded to a text hosting service.
For now it works with rentry.org
.
The password (edit code) can be configured through --upload-password
.
If no password is set, a random short word is used.
After the text is uploaded, a message appears that allows you to copy the URL.
The URL and password are also printed in the conversation window.
All the conversation can be uploaded, or just the last item.
There is a signals system that allows to make requests to remote servers.
To use this, a json file must be created and pointed to with the --signals
argument.
For example: --signals ~/signals.json
.
Multiple signals can be defined. This is a demo with all the available keys:
{
"test": {
"url": "https://test.com/submit",
"method": "POST",
"format": "text",
"items": "all",
"content": "status",
"length": 500,
"single": true,
"data": {
"username": "melt",
"key": "someAuthKey"
}
}
}
url
and content
are always required, the rest are optional.
url
is the url to use for the request. (required)
method
can be post
, get
, or put
. (default post
)
format
can be text
, json
, or markdown
. (default json
)
items
can be all
, to include the full conversation. Or last
, to include only the last item. (default all
)
content
is the key used for the conversation text. (required)
length
limits the content to that amount of characters. (default: 0)
single
sends the content as a single line. (default: false)
data
all the data keys needed to be sent. (default: empty)
For data, keywords are supported.
For example you can have "date": "((now))"
(Unix timestamp)
Or: "date": "((date))"
(Full date)
To run a signal you use the command with the name: /signal test
.
Feedback is shown in the window if the signal failed or if it ran successfully.
At the top there are system monitors, like CPU
, RAM
, Temperature
, and GPU
related ones.
GPU
might not work for all users. It has only been tested for AMD
in certain systems.
The monitors turn off a short time after the last response (1 minute).
For example --system-suspend 5
turns off the monitors after 5 minutes since last use.
And --system-suspend 0
will keep the system monitors running all the time.
They turn red when they reached a threshold, which can be configured.
By default, the system frame will only be shown if a local model is loaded.
To disable this behavior you can use --no-system-auto-hide
.
Command aliases can be set. And they can be chained.
For example: --alias test="/top & /sleep 0.5 & /about"
.
Then when using the /test
command, it will perform those 3 commands.
In that example there's a delay of 500ms between /top
and /about
.
This can be useful to quickly change between model configurations.
For example: --alias mini="/config model gpt-4o-mini & /config temperature 0.1"
.
It's possible to change the input text from a word or phrase to a full longer value.
The text is converted upon submit.
You can register triggers like this:
--trigger "the thing = Come up with a new theory about The Thing"
And if you submit exactly "the thing", it will be converted to the full text.
The =
is needed here because triggers can contain spaces.
A possible trigger you might want could be:
--trigger "... = Please continue talking"
This can be a powerful way to interact with the AI.
Tasks that run periodically can be registered.
Format is [seconds] [commands] [/now (optional)]
For example --task "60 /signal update"
This will run the update
signal every 60 seconds.
If you add /now
it will run the first one when the program starts.
For example --task "60 /signal update /now"
Units can be used, this includes s
, m
, h
, and d
.
Which mean seconds, minutes, hours, and days.
For example --task "2h /prompt tell me something about ((noun))"
.
This will run that task every 2 hours.
The config
command allows to change the configuration of the program.
This means any widget can be set.
For example /config model gemini-1.5
.
Or /config name_user Bob
.
To know the name of the widget, hover over it.
Arguments are usually set when launching the program, but they can also be changed while it's running.
This can be done with the arg
command.
For example: /arg taps false
. (boolean)
Or /arg delay 0.2
. (ints or floats)
Or /arg f1 /close
. (strings)
Or /arg custom_prompts [one = prompt one, two = prompt two]
(lists of strings)
The =
format is required because the name of custom prompts can have multiple words.
While this is possible, some argument changes won't work, and some might cause problems.
It's possible to point to a json file that overrides arguments.
For example: --argfile ~/args.json
.
This is a way to launch with different configurations easily.
For example:
{
"auto_unload": 60,
"aliases": [
"gpt /loadconfig gpt",
"gem /loadconfig gem",
"pro /loadconfig pro",
"llama /loadconfig llama",
"think /promptforce Tell something interesting you thought about ((noun))...",
"listen /notify Listen to this",
"talk /listen & /think"
],
"custom_prompts": [
"In Spanish = Explain ((words)) spanish",
"In Japanse = Explain ((words)) japanese"
],
"tasks": [
"2h /talk"
],
"variables": [
"meta /media/struct1/models/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf"
]
}
It's possible to save the current config and session.
This can be done through the main menu
or through commands.
For example: /saveconfig
, or /saveconfig books
.
Or: /savesession
, or /savesession books
.
Loading: /loadconfig books
, /loadsession books
.
If arguments are not used, a file picker appears.
Config meaning the current configuration of all the widgets.
Session meaning the set of conversations (tabs and their content).
When highlighted words are clicked, a menu with several options appear.
Custom Prompts can be registered to explain these words in a special way.
For this the keywords are needed, like ((words))
For example: --custom-prompt Spanish="shortly explain ((words)) in spanish"
Apart from typing the commands in the input (which supports autocompletion with tab), there is another way to run commands through a palette.
To spawn it, tap ctrl
twice in a row, or in the main menu
, or with /palette
.
You can filter it by typing some letters.
When ctrl
is pressed twice in a row quickly, a command gets executed.
By default it opens the Command Palette
but it can be configured.
There are 4 mouse gestures that can be mapped to commands.
These are up
, down
, left
, and right
.
To trigger these, hold the right mouse button, move to a direction, and release the button.
By default these scroll up/down and move to tabs left/right.
Variables can be set, unset, and read.
These are used in the inputs.
For example you can do: /set name George
.
Then you can write: who is $name?
.
The input is converted to its full form before being used.
So that would be converted to who is George?
.
You can unset with /unset name
.
Read with /var name
.
Variables can be filled at startup using arguments.
For example: --var "name George" --var "num 1200"
.
The prefix like $
can be changed.
For example: --variable-prefix @
So you can do: who is @name?
.
Variables also work in the model
field.
There is a files panel where you can enter file paths.
For now it can do simple text file analysis.
And it can also be used for image files when using special models.
When the file is used it is removed from the input, and not used for the next prompts.
The used file paths are remembered in the session file, but not their content.
Multi-modal models like llava 1.5 can be used.
Download the model gguf and the mmproj gguf (clip model):
https://huggingface.co/mys/ggml_llava-v1.5-7b/tree/main
Put those 2 files in the same directory.
Rename the clip model file to mmproj.gguf
.
Set Mode
to images
.
Now you can use the File
field to include a URL or path to an image.
And you can use the input to include text as normal.
While this has been tested to work, it's still considered experimental.
There are 3 available color themes. dark
, light
, and high contrast
.
You can access Theme
in the main menu
.
Or by using the /theme
command.
The application needs to restart for the theme to take effect.
It's also possible to change the border color and size.
Using: --border-size
and --border-color
.
There is a border effect that can be enabled with --border-effect
.
The color can be changed with --border-effect-color
.
This changes the color of the border when a response starts to stream.
Then restores the normal color when the stream is done.
There is a compact mode which hides some widgets from the window.
This can be useful if you want a less distracting interface.
To toggle compact mode you can use the main menu
, or f8
, or /compact
, or --compact
.
There are arguments you can use to define which panels get removed in compact mode.
The output window can be auto scrolled.
That means it will scroll slowly downwards or upwards.
So you can read text without manual intervention.
To activate this you can click Autoscroll
in the Go To Bottom
panel.
Or use the /autoscroll
command. This command accepts optional up
, and down
arguments.
To scroll upwards you can also middle click the Top
button.
There is also f9
and shift + f9
shortcuts.
The scroll delay can be configured through arguments.
When the autoscroll mode is active, the button has a different color.
When the scroll ends the autoscroll mode gets disabled.
The mode also gets disabled when manually scrolled.
You can use --no-autoscroll-interrupt
to avoid stopping it when scrolling up/down.
There are buttons on each side to make scrolling slower or faster.
Multiple lines can be joined with a character, in case you want a more concise presentation.
For example:
Sentence One
Sentence Two
Sentence Three
That would be converted to Sentence One 👾 Sentence Two 👾 Sentence Three
.
To enable this you can use --join-lines-user
and --join-lines-ai
.
To change the char, you can use --join-lines-char 😀
It ignores triple backtick snippets, it tries to keep those lines intact.
There's also --clean-lines-ai
, to collapse multiple empty lines into a single line.
Conversations/tabs can be pinned.
This can be done using the tab's context menu.
Or using /pin
, /unpin
, /togglepin
.
This allows finding them easily through the special pin list.
And allows closing either just normal tabs or just pins.
Sometimes you might need to access some data but don't feel comfortable having it printed anywhere or even visible for a couple of seconds. This can be for several reasons revolving around privacy and personal security.
You might want to have a way to have the computer/AI have a peek at this data and respond with the necessary safe information you request.
Lockets are registered at startup through arguments.
For example --locket name some command
.
Multiple lockets can be registered.
Then the /locket
command can be used like:
/locket date what is the week day?
/locket joe what ice cream does he like?
These can be using commands that fetch date or profile information.
On the item right click menu there are some Repeat
options.
This is a way to re-run the prompt, with or without history.
This is a smart command that cuts off history up to that point when making the prompt.
This can be a way to check how different models might have answered to the same input.
There are some keywords that you can use in commands, the input, or system prompt.
Name of the user.
Name of the AI.
Current date.
Current unix time in seconds.
Name of the current tab.
Random noun.
This is a special syntax to create uselinks
.
These are used to prompt directly on click.
Right clicking inputs like model
and input
show recently used items.
Middle clicking items in these lists delete them from the list.
There are 3 scrollable panels at the top, which can be scrolled by clicking the arrows on the sides or by using the mousewheel.
Middle clicking the panel arrows scrolls instantly to that side.
There are /like
and /dislike
commands.
Not all available configs are displayed in the interface. Check config.py to see what you can manually configure with the /config
command.
This is a tool that when enabled allows the AI to use their search engine to find information.
This might not work on all models.
This is a tool that allows the AI to read and write files to store information.
Right now only Claude supports this.
The AI might need to be instructed directly to use this tool.
Save prompts for later with /next some prompt
.
For when you have an idea but you can't use it right now because it would interrupt an operation.
/next what is the speed of a falcon?
Then when you are ready to use it just do /next
.
The input is then filled with the prompt.
Any amount of items can be saved at once.
They get removed when used.
There's a custom-made file picker to browse and pick files and dirs.
It allows keyboard shortcuts like Backspace, Arrows, typeahead, Enter.
```

---

## 9. Show HN: Nexa-gauge – Cache/cost-aware graph-based eval for LLM and RAG

- 日期: 2026-05-09 00:45
- 链接: https://github.com/harnexa/nexa-gauge

```
A cache-aware evaluation engine for measuring LLM and RAG output quality with repeatable metrics, cost estimates, and structured reports.
Read the Documentation · Quickstart · CLI Usage · Report Bug · Request Feature
nexa-gauge
is a Python package and command-line toolkit for evaluating generated outputs from LLM, RAG, and agentic systems. It replaces ad-hoc manual checks with a typed evaluation graph that can estimate cost, execute only the required nodes, reuse cached artifacts, and emit structured per-case reports.
It is designed for prompt iteration, benchmark runs, regression testing, release gates, and production evaluation workflows where teams need measurable quality and safety signals.
Core evaluation coverage includes:
- Relevance - measures whether generated claims answer the user question.
- Grounding - checks whether generated claims are supported by supplied context.
- Red team scoring - evaluates safety and risk behavior with configurable rubrics.
- GEval / LLM-as-a-judge - scores outputs against explicit criteria or evaluation steps.
- Reference metrics - computes overlap-based metrics against known reference answers.
Install the package from PyPI:
pip install nexa-gauge
Install optional Hugging Face dataset support:
pip install "nexa-gauge[huggingface]"
Set your provider key:
export OPENAI_API_KEY="<your-key>"
Estimate cost before running billable evaluation work:
nexagauge estimate eval --input sample.json --limit 10
Run the full evaluation graph and write per-case reports:
nexagauge run eval --input sample.json --limit 10 --output-dir ./report
- Graph-based evaluation pipeline - predictable node topology for scanning, chunking, claim extraction, metric execution, aggregation, and reporting.
- Estimate-first execution - preview uncached eligible cost before making LLM-backed calls.
- Cache-aware runs - avoid duplicate LLM spend and recomputation when inputs, prompts, and model routes are unchanged.
- Structured JSON reports - write per-case report files for CI, dashboards, notebooks, and downstream analytics.
- Per-node model routing - configure global models, node-specific models, fallback models, and temperatures.
- Scalable CLI execution - tune case-level workers, in-flight cases, and global LLM concurrency.
- Local and hosted datasets - evaluate JSON, JSONL, CSV, text files, and Hugging Face datasets.
nexa-gauge
runs evaluations through a deterministic node graph. Each target executes only its required upstream dependencies.
Typical execution paths:
grounding: scan -> chunk -> refiner -> claims -> grounding
relevance: scan -> chunk -> refiner -> claims -> relevance
geval: scan -> geval_steps -> geval
eval: full graph execution and aggregate metric summary
For a full architecture diagram, see docs/architecture.md.
The CLI entry point is nexagauge
.
nexagauge --help
nexagauge run --help
nexagauge estimate --help
nexagauge cache --help
Primary commands:
Common examples:
# Estimate full evaluation cost for a dataset slice
nexagauge estimate eval --input sample.json --limit 100
# Run full evaluation and write JSON reports
nexagauge run eval --input sample.json --limit 100 --output-dir ./report
# Run full evaluation with explicit chunk/refiner strategies
nexagauge run eval --input sample.json --limit 100 --chunker semchunk --refiner mmr --refiner-top-k 3
# Run only the grounding metric branch
nexagauge run grounding --input sample.json --limit 25
# Preview cache cleanup
nexagauge cache delete --dry-run
Common flags:
See docs/cli-code-flow.md and the hosted CLI documentation for deeper usage details.
Use --input
with local files or hosted datasets.
Canonical record fields include:
Common aliases such as response
, answer
, output
, completion
, query
, prompt
, ground_truth
, and label
are normalized during scanning.
nexa-gauge
combines deterministic metrics with LLM-as-a-judge evaluation.
GEval is split into two phases:
geval_steps
resolves reusable evaluation steps from criteria or accepts provided steps.geval
scores each case against those resolved steps and selected input fields.
This design makes rubric-based evaluation repeatable and cache-friendly across datasets.
Cost control is a first-class part of the runtime.
# Preview uncached work before execution
nexagauge estimate eval --input sample.json --limit 50
# Reuse cache during normal runs
nexagauge run eval --input sample.json --limit 50 --output-dir ./report
# Ignore cache reads but still write fresh outputs
nexagauge run eval --input sample.json --limit 50 --force
# Disable cache reads and writes for debugging
nexagauge run eval --input sample.json --limit 50 --no-cache
The cache is deterministic and route-aware. Inputs, evaluation criteria, model routing, prompt versions, parser versions, and relevant upstream artifacts are included in cache keys so stale outputs are not reused across incompatible runs.
For run
, cache location can be controlled with:
export NEXAGAUGE_CACHE_DIR="./.nexagauge-cache"
Inspect the active cache root:
nexagauge cache dir
Clear cached node outputs:
nexagauge cache delete --dry-run
nexagauge cache delete --yes
For local development or repeatable runs, copy the environment template:
cp .env.example .env
Minimum configuration for OpenAI-backed runs:
OPENAI_API_KEY=<your-key>
LLM_MODEL=gpt-4o-mini
Supported per-node overrides follow this pattern:
LLM_CLAIMS_MODEL=openai/gpt-4o-mini
LLM_CLAIMS_FALLBACK_MODEL=openai/gpt-4o
LLM_GROUNDING_TEMPERATURE=0.0
Runtime overrides can also be passed through the CLI:
nexagauge run eval \
--input sample.json \
--llm-model openai/gpt-4o-mini \
--llm-model grounding=openai/gpt-4o \
--llm-fallback openai/gpt-4o
Clone the repository and install it from source:
git clone https://github.com/harnexa/nexa-gauge.git
cd nexa-gauge
pip install -e .
Contributor workflow with uv
:
uv sync
make lint
make test
make ci
Build distributions:
uv build
Expected artifacts:
dist/nexa_gauge-<version>-py3-none-any.whl
dist/nexa_gauge-<version>.tar.gz
Releases use release-please
. Conventional Commit titles such as feat:
, fix:
, docs:
, deps:
, and chore:
are recommended for cleaner generated release notes, but they are not required by CI.
- Hosted documentation: harnexa.dev/nexa-gauge/docs/introduction
- Local getting started guide: docs/get-started.md
- Architecture: docs/architecture.md
- CLI code flow: docs/cli-code-flow.md
- Product summary: docs/PRODUCT_SUMMARY.md
- License: MIT
- Security policy: SECURITY.md
- Contributing guide: CONTRIBUTING.md
- Code of conduct: CODE_OF_CONDUCT.md
Distributed under the MIT License. See LICENSE for details.
```

---

## 10. Show HN: [Video] Tribute to LLM releases in April 2026

- 日期: 2026-05-08 23:53
- 链接: https://www.youtube.com/watch?v=uu5ffMH_X9w

```
Article URL: https://www.youtube.com/watch?v=uu5ffMH_X9w 
 Comments URL: https://news.ycombinator.com/item?id=48070211 
 Points: 2 
 # Comments: 0
```

---

## 11. How Do You Know If a Skill Is Any Good? LLM-as-Judge Scoring

- 日期: 2026-05-08 22:11
- 链接: http://instructionmanuel.com/scoring-skills-with-llm-as-judge

```
How Do You Know If a Skill Is Any Good? LLM-as-Judge Scoring
Last time, I walked through writing skills that agents can actually execute and introduced skill-validator as a way to catch structural and content issues before an agent ever sees the skill. At the end, I mentioned that skill-validator also supports LLM-as-judge scoring across dimensions like clarity, actionability, token efficiency, and novelty—and promised to dig into that.
This is that post.
Deterministic validation (like structure checks, link validation, content analysis) tells you whether a skill is well-formed. It catches missing files, broken references, bloated token counts, and vague language. Those checks are valuable, and they're where most teams should start.
But they don't answer the harder question: is the skill actually good? A skill can pass every structural check and still produce unpredictable agent behavior because its instructions are ambiguous, its steps aren't actionable, or it doesn't teach the agent anything it doesn't already know.
Measuring those qualities requires a different kind of evaluation where the criteria are inherently subjective. That's where LLM-as-judge scoring comes in. I'll continue using Doc Detective's agent tools as the running example, the same skills I've been building and validating for a few posts now.
The vibe check problem
Most teams evaluate skill quality by reading the skill, running the agent, looking at the output, deciding if it seems right. This is what some practitioners call "vibe-based evaluation," and it works well enough when you have one or two skills and a subject matter expert doing the checking.
It breaks down in three predictable ways:
Inconsistency across reviewers. Two people reading the same skill will notice different things and weight different qualities. One reviewer focuses on completeness. Another on conciseness. Neither is wrong, but the skill gets different verdicts depending on who reviews it, and no one can articulate exactly what standard they're applying.
No baseline for comparison. When you revise a skill, how do you know the revision is better? Without a structured assessment, you're comparing gut feelings across time. "It felt clearer before" isn't something you can act on reliably.
Invisible drift. Skills degrade as projects evolve. A step references a tool that's been replaced. An entry criterion assumes a file structure that's changed. Structural validation catches some of this, but qualitative drift (instructions that were once clear becoming ambiguous as context shifts) goes unnoticed until the agent starts producing unexpected output.
These problems aren't unique to skills. They're the same challenges technical writers face with any documentation review process. The difference is that skills have a faster feedback loop because when a skill is unclear, the agent shows you immediately by doing something wrong. That tight feedback loop makes skills a useful place to experiment with structured quality measurement.
What LLM-as-judge scoring actually is
Instead of a human reading the skill and deciding whether it's clear enough, you give the skill text to an LLM along with explicit criteria for what "good" looks like (a rubric), and the LLM scores the skill against each criterion.
If you've used style guides, it's the same idea. Define what "good" looks like, then check compliance. The LLM just applies the rubric without fatigue or mood variation.
Here's a simplified version of what a scoring rubric looks like in practice:
You are evaluating an agent skill for quality. Score each
dimension from 1-5 based on the criteria below.
CLARITY: Can an agent determine exactly what to do from this
text alone, without needing external context or interpretation?
5 = Every step is unambiguous
3 = Most steps are clear; a few require interpretation
1 = Steps are vague or contradictory
ACTIONABILITY: Does the skill provide concrete, executable
steps rather than general guidance?
5 = All instructions are directly executable
3 = Mix of executable steps and general advice
1 = Mostly principles or suggestions, few concrete steps
For each dimension, return the score and a brief justification.
The LLM reads the skill, applies the rubric, and returns structured scores with reasoning. That reasoning is often as valuable as the scores themselves, as it surfaces specific passages that are ambiguous or vague, giving you something concrete to revise.
A few caveats. LLM judges carry biases. They tend to favor longer responses, score their own model's outputs higher, and sound confident even when they're wrong (no surprise there). These biases don't disqualify the approach, but they mean scoring is a signal to investigate, not a verdict to accept. A low score says "look at this more carefully." A high score doesn't guarantee the skill works perfectly in practice.
Six dimensions of skill quality
skill-validator scores skills across six dimensions. Here's what each one measures and why it matters:
Scope discipline maps directly to the single responsibility principle I covered in a previous post, and directive precision measures the specificity of your instruction language, how consistently you use directive phrasing ("must," "always") over advisory phrasing ("consider," "may"). If your skills already follow the design principles from that post, you're likely in good shape on both.
Clarity and actionability
These two are related but distinct. Clarity asks, "can the reader understand what to do?" Actionability asks, "does the skill tell the reader how?" The twist is that the reader is an LLM, and LLMs resolve ambiguity differently than humans. A human encounters "handle any failures" and draws on experience to fill the gap or asks a colleague when uncertain. An LLM draws on training data, picks one interpretation, and executes it confidently without flagging that the instruction was ambiguous.
Consider this step from a hypothetical skill:
Review the test results and handle any failures.
A human tester knows what "handle" means in context. An LLM picks one interpretation and runs with it. Doc Detective's doc-detective-test
skill avoids this by being explicit:
**If `--fix` is specified:**
1. For each failing test, analyze the failure
2. Determine if the failure is in the documentation or the test spec
3. If documentation: propose a fix to the source file
4. If test spec: propose a fix to the test specification
5. Re-run the fixed test to verify the fix resolves the failure
Similarly, "review the output for quality issues" is clear in intent but not actionable because it doesn't specify what constitutes a quality issue.
Now consider "Compare the output against the acceptance criteria in the spec. For each criterion, verify it's satisfied. Flag any criterion that isn't met, with the specific gap identified."
The difference matters more for agents than for humans. A human reviewer has professional judgment to fill in "review for quality." An agent needs the review criteria spelled out.
The same principle applies to entry criteria. Rather than "make sure everything is ready before starting," Doc Detective specifies what "ready" means:
**Entry criteria:**
- Documentation input (file path or inline text) is provided
- Input is readable and contains step-by-step procedures
Both scoring dimensions look for the same underlying quality: can an agent execute each step as written, without filling gaps the skill should have filled?
Novelty
Does this skill teach the agent something it doesn't already know? If an LLM would produce essentially the same output without the skill loaded, the skill is consuming context budget without providing meaningful uplift.
This connects to a distinction between two types of skills:
Uplift skills encode techniques that improve agent performance beyond baseline. A skill that teaches a specific test specification format, or a particular approach to error message formatting, falls here. These skills genuinely improve output quality because they provide information the model doesn't have. Doc Detective's skills score well on novelty because they encode project-specific workflows (the test spec format, injection syntax, and fix-loop logic) that no model would know without explicit instruction.
Preference skills sequence existing capabilities according to your workflows. Your changelog format. Your review gate order. The specific terminology your style guide requires. These skills tell the model which of its existing capabilities to apply, and in what order, rather than teaching something new.
Both types are valuable, but they score differently on novelty. A preference skill might score low on novelty while still being essential to your workflow because the value isn't in teaching something new but in encoding a decision that would otherwise be inconsistent.
If a skill scores high on every dimension except novelty, that's not necessarily a problem. It might mean the skill encodes important preferences that the model can already follow. But if you're investing significant effort in a skill that scores low on novelty, it's worth asking whether the skill is providing real value or just repeating what the model would do anyway.
Novelty also has a shelf life. As models improve, skills that once provided uplift may duplicate built-in capabilities. Periodic scoring catches this drift.
Token efficiency
Every token in a skill competes with every other token in the agent's context window. A skill that takes 3,000 tokens to convey what could be said in 1,000 costs context budget that could hold the document being tested, the conversation history, or other tools the agent needs to do its job.
This principle led Vercel to cut their AGENTS.md from 40KB to 8KB after finding that shorter, focused context actually improved agent performance. More isn't always better when every token counts.
Token efficiency scoring assesses whether a skill conveys its instructions concisely. It looks for redundancy, unnecessary preamble, overly verbose examples, and sections that could be moved to reference files (loaded on demand) rather than sitting in the main skill body. The Agent Skills spec supports this through progressive disclosure: the SKILL.md file loads into context when the skill is invoked, while reference files load only when the agent encounters a link to them.
What a scoring run looks like
Running LLM-as-judge scoring with skill-validator follows the same pattern as the deterministic checks covered in the previous post, with an additional flag and an API key:
skill-validator score evaluate skills/doc-detective-inject/
The output provides per-dimension scores with reasoning:
Scoring skill: /home/hawkeyexl/Workspaces/agent-tools/skills/doc-detective-inject
SKILL.md Scores
Clarity: 5/5
Actionability: 4/5
Token Efficiency: 4/5
Scope Discipline: 5/5
Directive Precision: 5/5
Novelty: 5/5
──────────────────────────────
Overall: 4.67/5
"Exceptionally clear instructions for a proprietary tool with explicit entry/exit criteria, precise directives, and novel domain-specific matching logic. Minor verbosity in examples and tables could be trimmed without losing instructional value."
Novel details: This document contains **high novelty** in its specification of proprietary comment injection patterns and action-matching heuristics.
**Novel details to fact-check:** The semantic matching rules table (exact/contains/pattern priority order), the specific content patterns per action type (e.g., `goTo` matching "navigation verb" lines, `type` matching quoted text after type verbs), the file-type-to-comment-syntax mapping including the `<?doc-detective step {...} ?>` XML processing instruction format, and the `<!-- test {"testId":"..."} -->` wrapper convention with `<!-- test end -->` terminator. These appear to be Doc Detective-specific implementation patterns not documented in standard testing frameworks.
A few things to notice about these results.
The reasoning matters more than the numbers. A 4.0 on actionability becomes useful when paired with a concrete revision target. (There's some irony in the actionability score itself not being actionable without the reasoning.)
High scores don't mean the skill works. Scoring measures the quality of the instructions, not the quality of the approach. You still need to run the agent and observe results. That's when we get to agent execution test, which is a related but distinct topic.
Low scores are investigation prompts. A token efficiency score of 3.5 doesn't mean the skill is bad. Whether it's worth pursuing depends on how constrained your context budget is.
Dimensions fight each other. The six dimensions aren't independent. Novelty and token efficiency are the most consistent friction: a skill that teaches something genuinely new needs enough detail to teach the concept, and that detail costs tokens. Clarity and token efficiency pull the same way—explicit instructions score well on clarity but spend context budget. Actionability and scope discipline conflict when specifying edge cases pushes a skill past single-responsibility boundaries. These tensions are structural tradeoffs, not scoring bugs. Don't chase 5.0 across every dimension. Decide which dimensions matter most for each skill's purpose and accept what comes with that priority. A high-novelty skill at 3.5 on token efficiency might be exactly right.
Scoring works best as one signal among several. Pair it with the deterministic checks from the previous post and actual agent execution testing, and you get a more complete picture than any single approach provides.
Scoring in the quality pipeline
Consider how scoring fits into the broader validation pipeline:
Each layer catches problems the others can't. Deterministic checks won't tell you if a skill is clear. Scoring won't tell you if the agent actually follows it correctly. Execution testing is slow and expensive to run on every change. Together, the three layers form a practical quality pipeline where you can run cheaper checks frequently and more expensive checks selectively.
For Doc Detective's agent tools, the pipeline runs like this: deterministic validation runs on every PR (via the validation script I described last time), while scoring runs happen when skills are created or significantly revised, and agent execution testing happens before major releases.
Documentation quality is measurable
LLM-as-judge scoring enables a shift from "I think this skill is good enough" to "clarity scored high, but actionability dropped after the last revision." That gives teams a shared vocabulary for discussing quality and a baseline for tracking improvement over time.
If you're working with agent skills and want to try this, skill-validator handles the mechanics. Start with the deterministic checks to get your skills structurally sound, then add scoring to see where quality gaps hide.
Also, I walked through how Doc Detective's skills actually work to enable AI-assisted test generation for your documentation—a practical application of everything this series has covered so far. If you're curious, check it out on docsastests.com.
```

---

## 12. Ask HN: What kind of computer language will LLM use?

- 日期: 2026-05-08 22:03
- 链接: https://news.ycombinator.com/item?id=48069336

```
I think in little time LLM will have the capability to translate easily code from one computer language to another, for example the LLM could "think" in prolog + lisp instead python. LLM will be able to write thousands of lines of APL or J in just a minute, we will have to accept that python is not the language for future LLMs. Perhaps the power of macros will not be defeated by its complexity because for an LLM a thousand line macro is just another simple code, prolog unification could mean building slots to construct new powerful artifacts that we are not able to have in our minds at the moment. LLM will no longer learn natural language or our most used computer languages, the next step is designing languages for a system that can keep in his head millions lines of code. 
 Comments URL: https://news.ycombinator.com/item?id=48069336 
 Points: 3 
 # Comments: 4
```

---

## 13. Show HN: Openloom – Turn Loom links into transcripts and frames an LLM can watch

- 日期: 2026-05-08 18:25
- 链接: https://www.useopenloom.com/

```
Let AI Watch Your Videos
Turn Loom recordings into timestamped screenshots, transcripts, and structured docs your AI tools can use.
No accounts, no tracking. Your video is processed entirely in your browser.
Turn Loom recordings into timestamped screenshots, transcripts, and structured docs your AI tools can use.
No accounts, no tracking. Your video is processed entirely in your browser.
```

---

## 14. Show HN: UltraCompress – first mathematically lossless 5-bit LLM compression

- 日期: 2026-05-08 16:49
- 链接: https://github.com/sipsalabs/ultracompress

```
Lossless 5-bit transformer compression ? 22 architectures validated end-to-end at sub-1% PPL drift, including the first public state-space model (Mamba-2.8B) and 405B-class flagship (Hermes-3).
- PyPI v0.5.4 LIVE ?
pip install ultracompress==0.5.4
. New:uc bench <packed_dir>
measures TTFT, tokens/sec, decode-TPS, and peak VRAM on any UC pack. - 22 architectures validated end-to-end at 5 bpw, all sub-1% PPL drift vs bf16 baseline.
- Hermes-3-Llama-3.1-405B compressed (250 GB v3 pack, 126 layers). HF upload in flight via the resilient uploader. Largest dense model compressed by Sipsa to date ? single 32 GB GPU streaming inference path.
- 39 public HF repos in the SipsaLabs org with bit-identical-reconstruction artifacts.
pip install ultracompress==0.5.4
hf download SipsaLabs/qwen3-1.7b-base-uc-v3-bpw5 --local-dir ./qwen3-1.7b-base-uc
uc verify ./qwen3-1.7b-base-uc # bit-identical W_base reconstruction
uc bench ./qwen3-1.7b-base-uc # NEW: TTFT, tokens/sec, peak VRAM
The v3 pack format ships:
- 5-bit GSQ codes per weight + per-block(64) absmax scale + per-Linear V18-C low-rank correction (rank=32, alpha scalar)
- Reconstruction:
W_full = grid[codes] * absmax + alpha * U @ V
- SHA-256-verified bit-identical reconstruction on every pack ?
uc verify
is cryptographic ground truth
13 documented entries in docs/HONEST_NEGATIVE_RESULTS_2026_05_08.md
:
- Per-Linear adaptive bpw v1 REFUTED apples-to-apples (1.005097x vs uniform 1.004876x)
- V18-C train_steps depth-adaptive within noise on Qwen3-1.7B-Base
- V18-C SVD-warm-start NEGATIVE (worse than random init)
- rank/train_steps push: 1.0040x is the empirical floor for Qwen3-1.7B-Base
- PyPI: https://pypi.org/project/ultracompress/0.5.4/
- HuggingFace org: https://huggingface.co/SipsaLabs
- Site: https://sipsalabs.com
- Benchmarks: https://sipsalabs.com/benchmarks
- Phase 0 POC ($5K, 1 week, 3 customer-picked models): https://sipsalabs.com/poc
Apache 2.0. See LICENSE.
USPTO provisional patents 64/049,511 + 64/049,517 filed 2026-04-25.
```

---

## 15. Ask HN: How do we handle the rise of low quality "This is LLM" comments?

- 日期: 2026-05-08 14:28
- 链接: https://news.ycombinator.com/item?id=48063759

```
Every post that reaches the top of HN will have at least a few comments saying "This is LLM!" It has become a proxy for "I don't like this article, so it must be a LLM" To me, it feels like lazy karma farming, as these comments often do get a few upvotes. And of course, accuse a 100 posts if being LLM, you are guaranteed to be right at least once, then like astrologers you can claim success. Is there anything we can do to discourage this type of lazy and low effort posting? 
 Comments URL: https://news.ycombinator.com/item?id=48063759 
 Points: 9 
 # Comments: 20
```

---

## 16. Mesh LLM to build private personal AI, using open models

- 日期: 2026-05-08 14:15
- 链接: https://www.anarchai.org

```
Article URL: https://www.anarchai.org 
 Comments URL: https://news.ycombinator.com/item?id=48063539 
 Points: 3 
 # Comments: 0
```

---

## 17. Yes, I set up Karpathy's LLM wiki. Now what?

- 日期: 2026-05-08 13:46
- 链接: https://twitter.com/keane42443/status/2052426761477255448

```
We’ve detected that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.
Help Center
Terms of Service Privacy Policy Cookie Policy Imprint Ads info © 2026 X Corp.
```

---

## 18. How LLM Inference Works

- 日期: 2026-05-08 13:04
- 链接: https://twitter.com/akshay_pachaar/status/2050941458614751327

```
We’ve detected that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.
Help Center
Terms of Service Privacy Policy Cookie Policy Imprint Ads info © 2026 X Corp.
```

---

## 19. Phishing Arena – multi-agent LLM tournament to study adversarial email security

- 日期: 2026-05-08 12:54
- 链接: https://github.com/Krabby24/phishing-arena

```
A Multi-Agent LLM Tournament for Adversarial Email Security Research
Phishing Arena is a controlled, reproducible benchmark where four commercial LLMs compete in rotating roles — Phisher, Filter, and Target — to study adversarial email security dynamics in Italian.
The system runs a full tournament of 48 matches across 24 role permutations × 2 repetitions, with 20 rounds per match. The Phisher agent is equipped with a CampaignMemory feedback loop that accumulates round outcomes, enabling adaptive behavior without prescriptive instructions.
Critical finding: 79% of successful bypasses show no identifiable evasion technique — they succeed through contextual plausibility, not technical obfuscation.
Round flow:
[Phisher] → email → [Filter] → bypass? → [Target]
↑ |
└──────── CampaignMemory ←───────────────┘
Three roles per match:
- Phisher — generates contextualised phishing emails targeting a synthetic professional profile
- Filter — classifies each email as phishing or legitimate (blind: no knowledge of phisher techniques)
- Target — simulates a realistic user reaction if the email bypasses the filter
git clone https://github.com/Krabby24/phishing-arena
cd phishing-arena
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt
Set your API keys in a .env
file at the project root:
ANTHROPIC_API_KEY=...
OPENAI_API_KEY=...
DEEPSEEK_API_KEY=...
XAI_API_KEY=...
python run_test.py
The script will prompt you to delete any existing checkpoint before starting fresh. The tournament resumes automatically from the last completed match if interrupted.
Set MODE = "dev"
in config.py
to run with three Gemini 2.5 Flash instances for architecture testing.
python paper/figures/generate_figures.py
Output: figures/*.pdf
— vector format, ready for Overleaf.
TOURNAMENT = {
"rounds_per_match": 20,
"phishing_ratio": 0.40,
"matches_per_pair": 2,
}
12 Italian professional archetypes with varying cybersecurity familiarity levels (very low → high), each paired with 50 contextualised legitimate emails. Archetypes span: CEO, CFO, HR Manager, IT Manager, Responsabile Acquisti, Direttore Marketing, Commerciale, Avvocato, Contabile, Office Manager, Responsabile IT Bancario, Titolare Hospitality.
Full tournament results are available in data/results/
. The analysis report is in paper/
.
To reproduce the analysis, run the tournament with the provided configuration and apply analysis/metrics.py
to the output JSON.
If you use Phishing Arena in your research, please cite:
@misc{stocco2025phishingarena,
author = {Marco Stocco},
title = {Phishing Arena: A Multi-Agent {LLM} Tournament
for Adversarial Email Security Research},
year = {2025},
publisher = {arXiv},
url = {https://arxiv.org/abs/XXXX.XXXXX}
}
MIT License — see LICENSE for details.
```

---

## 20. SubQ: Sub-quadratic LLM built for 12M-token reasoning

- 日期: 2026-05-08 06:26
- 链接: https://subq.ai/

```
12M
SubQ is a sub-quadratic LLM built for 12M-token reasoning, allowing agents to work across full repositories, long histories, and persistent state without quality loss.
12M
150
1/5
Use Cases
Reason across 12M tokens in one prompt: entire repos, months of PRs, and long-running agent state, with room to spare at one-fifth the cost.
~ Approximate token counts.
Architecture
SubQ is the first model built on a fully sub-quadratic sparse-attention architecture. LLMs today waste compute by processing every possible relationship between words, but only a small fraction of these relationships matter.
SubQ finds and focuses only on those, ensuring compute is used where it matters most. At 12M tokens, this reduces attention compute almost 1,000×, changing the way LLMs scale.
Benchmarks
n/r = result was not reported by the model provider
* = internally evaluated
SubQ results are third-party validated
Products
The full-context API for developers and enterprise teams. Process full repositories and pipeline states in a single API call at linear cost.
The long-context layer for coding agents. Plug into Claude Code, Codex, and Cursor to map codebases, gather context, and answer token-heavy questions faster.
About
Subquadratic is a frontier AI research and infrastructure company building a new class of LLMs. While other major labs focus on incremental improvements to Transformer models, we're pushing foundational change at the model architecture level — enabling large-context, multi-modal inference that scales efficiently where transformers can't.
Built by researchers from
Early Access
Join the private preview.
```

---
