# Last Week in AI

> 分类: AI专题
> URL: https://lastweekin.ai/feed/
> 抓取: 20 篇

---

## 1. Last Week in AI #340 - OpenAI vs Musk + Microsoft, DeepSeek v4, Vision Banana

- 日期: 2026-05-05 08:30
- 链接: https://lastweekin.ai/p/last-week-in-ai-340-openai-vs-musk

```
Musk testimony dominated first week of Musk v. Altman. ‘You can’t just steal a charity’ 
 Related: 
 All the evidence revealed so far in Musk v. Altman 
 Musk texted OpenAI’s Brockman about settlement two days before trial began 
 The Elon Musk v. Sam Altman trial is now on YouTube 
 Elon Musk Seemingly Admits xAI Has Used OpenAI’s Models to Train Its Own 
 Musk and Brockman’s settlement texts revealed as OpenAI trial enters second week 
 Vicki Behringer/Reuters 
 Summary : The first week of the Musk v. Altman trial concluded in Oakland, California, with Elon Musk’s testimony dominating proceedings over three days. Musk’s legal team is seeking up to $134 billion in damages, the removal of Altman and Brockman, and an unwinding of OpenAI’s for-profit conversion. Musk co-founded OpenAI in 2015 as a nonprofit and donated approximately $38 million to the organization. 
 Key facts so far include: 
 Musk repeatedly argued “you can’t just steal a charity,” claiming that CEO Sam Altman and President Greg Brockman betrayed the company’s founding mission by converting it into a for-profit entity now valued at over $850 billion. 
 Musk testified he created OpenAI as a “counterweight” to Google DeepMind and that he “came up with the idea, the name, recruited the key people.” 
 During cross-examination by OpenAI lead counsel William Savitt, Musk acknowledged that xAI “partly” used OpenAI’s models to train its own (typically referred to as distillation) though he downplayed it as “standard practice.” 
 It was later revealed that two days before the trial began, Musk texted Brockman about a potential settlement; when Brockman suggested both sides drop all claims, Musk replied, “By the end of this week, you and Sam will be the most hated men in America.” 
 Exhibits released during the trial included early emails showing Musk drafting OpenAI’s mission, internal tensions over his push for control, Andrej Karpathy suggesting a Tesla-OpenAI merger, and a December 2024 iMessage exchange in which Zuckerberg told Musk that Meta had sent a letter to the California AG supporting his lawsuit. 
 The second week opened with Greg Brockman taking the stand, where he confirmed OpenAI is exploring an IPO that could be one of the largest in history, given the company’s $850 billion private valuation. Brockman revealed he owns nearly $30 billion in OpenAI shares, which would rank him among the world’s wealthiest people, along with $471 million in Stripe shares. 
 The trial is being livestreamed on the district court’s YouTube page , though it is audio only and recording is not allowed. Sam Altman and Shivon Zilis expected to testify later this month. 
 Our take : We haven’t really learned much new so far —* OpenAI and Musk have been fighting it out in public for a while and dished out plenty of dirt in the lead up to this. Musk’s admission that xAI “partly” distilled from OpenAI is honestly the most interesting bit so far, at least if you’ve followed their drama up to now. Still, we will no doubt learn more interesting information as the trial proceeds —* or at least get some amusing exchanges. 
 *these are 100% human-written em-dashes, we can’t let AI have all the fun! 
 OpenAI ends Microsoft legal peril over its $50B Amazon deal 
 Source 
 Summary : Microsoft and OpenAI have renegotiated their partnership agreement, resolving a legal dispute that had been brewing since OpenAI’s up-to-$50 billion deal with Amazon. The new terms replace Microsoft’s open-ended exclusivity (which previously lasted until OpenAI achieved AGI) with a nonexclusive license to OpenAI IP through 2032. Microsoft remains OpenAI’s “primary cloud partner,” with OpenAI products shipping “first on Azure” unless Microsoft cannot support the necessary capabilities — but critically, OpenAI can now serve all its products across any cloud provider, including AWS. 
 The core conflict stemmed from OpenAI’s February 2026 Amazon deal, which included exclusive rights for AWS to host OpenAI’s agent-making tool Frontier and co-develop stateful runtime technology on AWS Bedrock (infrastructure supporting long-running AI agents). Microsoft’s prior contract gave it exclusive rights to all OpenAI API-accessed products, including Frontier, prompting Microsoft to publicly refute the AWS-exclusive terms and reportedly contemplate legal action. Under the new agreement: Microsoft stops paying OpenAI a revenue share, while OpenAI continues paying Microsoft a revenue share through 2030 (subject to a cap); Microsoft retains ~27% ownership of OpenAI’s for-profit entity; and Amazon CEO Andy Jassy confirmed OpenAI models will become available on AWS Bedrock alongside the upcoming Stateful Runtime Environment. 
 Our take : It’s easy to forget now, but we likely would not have had ChatGPT were it not for Microsoft investing 3 billion dollars into OpenAI between 2019 and 2022. Still, the close contractual ties they formed in those pre-ChatGPT years has clearly been another headache for OpenAI to deal with in recent years. Despite them potentially losing out on revenue with these new terms, i’d say this new deal is still a win for OpenAI; the speed with which they announced OpenAI models being available on Amazon Bedrock clearly shows having nonexclusive terms is worth a lot to them. 
 DeepSeek previews new AI model that ‘closes the gap’ with frontier models 
 Related: 
 China’s DeepSeek previews new AI model a year after jolting US rivals 
 China’s DeepSeek releases preview of long-awaited V4 model as AI race intensifies 
 Summary : DeepSeek launched preview versions of DeepSeek V4 Flash and V4 Pro, both text-only mixture-of-experts models with 1 million-token context windows. V4 Pro is has 1.6 trillion total parameters and 49 billion active, while V4 Flash has 284 billion total and 13 billion active. As with prior releases the weights are open sourced on Hugging Face , along with a detailed tech report that explains the key technical innovations in the architecture. DeepSeek claims major efficiency and performance gains over V3.2, with reasoning and coding results approaching or matching leading models in some benchmarks. 
 Source: DeepSeek V4 Preview Release 
 V4-Pro-Max is almost uniformtly better than the other notable recent OSS releases from China (Kimi-K.26 and GLM-5.1) while also having a significantly larger context window: 
 Source: DeepSeek v4 Preview Release 
 The models are competitively priced — lower than frontier western models and compatitive with comparable open source models — and appear capable of higher throughput depending on the service they are used with. 
 Our take : As we discussed in the last podcast episode , DeepSeek positioned their effort with v4 as being primarily about dealing with “the efficiency barrier in ultra-long contexts” to enable “ further gains from test-time scaling and … further exploration into long-horizon scenarios and tasks”. Given that, I’d bet v4 is actually significantlly more capable at real-world agentic coding than Kimi K2.6 and possibly even Gemini 3.1 pro, despite them being close to tied on most standard benchmarks. 
 Google DeepMind Introduces Vision Banana 
 Summary : Google DeepMind published Image Generators are Generalist Vision Learners and introduced Vision Banana, a unified model that performs both image generation and visual understanding tasks by treating perception as image generation. Built by lightweight instruction-tuning of their base image generator Nano Banana Pro, Vision Banana handles semantic segmentation, instance segmentation, monocular metric depth estimation, and surface normal estimation — all without task-specific modules, simply by changing the prompt. The core insight mirrors the LLM training paradigm: just as generative pretraining on text develops rich language representations, training on image generation implicitly teaches a model geometry, semantics, and depth, which can then be expressed in decodable formats. 
 Across multiple benchmarks in zero-shot transfer settings, Vision Banana surpasses specialist models, with no evaluation benchmark data included in training. Crucially, instruction-tuning does not degrade generative performance — Vision Banana achieves a 53.5% win rate against Nano Banana Pro on GenAI-Bench text-to-image generation. 
 Our take : This is really cool! We’ve known vision-language models were zero-shot capable of some fairly advanced computer vision tasks such as object detection and localization for a while, but seeing that idea be taken to such an extreme was not something I could’ve predicted. Not only is this model capable of a whole suite of tasks that have generally been addressed by specialized models, but it appears to be better or almost as good as them at these tasks! The bitter lesson strikes again, it seems. 
 Other News 
 Tools 
 Claude is connecting directly to your personal apps like Spotify, Uber Eats, and TurboTax . Anthropic has expanded Claude’s integrations to include consumer apps like Spotify, Uber Eats, and TurboTax, with data privacy protections. 
 Claude can now plug directly into Photoshop, Blender, and Ableton . New creative connectors enable Claude to access, retrieve data from, and perform actions within these applications to assist with tasks like image editing, video work, music production, and 3D modeling. 
 Microsoft launches ‘vibe working’ in Word, Excel, and PowerPoint . the feature enables Copilot to directly execute multi-step editing tasks across Office applications while displaying its actions in real time through a sidebar. 
 OpenAI launches ChatGPT for Clinicians . Free for verified U.S. clinicians, the tool includes features for automating common workflows, conducting medical literature reviews with citations, and supporting HIPAA-compliant documentation. 
 Mistral AI Launches Remote Agents in Vibe and Mistral Medium 3.5 . Scoring 77.6% on SWE-Bench Verified, the update enables developers to offload long-running coding tasks to cloud-based agents that work asynchronously in isolated sandboxes while providing visibility into the agent’s actions and decisions. 
 ElevenLabs Launches ElevenMusic as an AI Music Creation, Remixing and Streaming Service for Fans . Pitched as a fan-focused platform, ElevenMusic lets users stream, create, and remix music from a catalog of about 4,000 artists while providing participating musicians with royalties based on how their work was used to train the AI model. 
 Granite 4.1: IBM’s 8B Model Is Competing With Models Four Times Its Size . Trained through five distinct phases with different data mixtures and rigorous four-stage reinforcement learning processes, IBM’s Granite 4.1 achieves competitive benchmark performance while maintaining predictable latency and reliable tool-calling capabilities. 
 OpenAI explains its goblin and gremlin infestation . A quirk in training incentives tied to a “Nerdy” personality option caused GPT-5.5 to randomly reference goblins and gremlins in responses, prompting OpenAI to add explicit instructions preventing the AI from mentioning these creatures unless directly relevant to user queries. 
 Business 
 In another wild turn for AI chips, Meta signs deal for millions of Amazon AI CPUs . Meta will use millions of AWS Graviton ARM-based CPUs to handle AI workloads like real-time reasoning and multi-step task coordination, marking a shift away from GPUs for inference tasks and a win for Amazon in its competition with Google Cloud and Nvidia. 
 Waymo goes fully autonomous with Ojai vehicles in Phoenix . Now testing its custom-built Ojai vehicles with driverless autonomous rides in San Francisco, Los Angeles, and Phoenix, Waymo’s new fleet features sliding doors and a streamlined sensor array that’s cheaper to produce than its previous Jaguar i-Pace vehicles. 
 China Suspends Autonomous Driving Permits After Baidu Outage . Autonomous vehicle companies are now barred from expanding their fleets or launching operations in new cities while regulators investigate a March incident where over 100 Baidu robotaxis malfunctioned in Wuhan. 
 You’re about to feel the AI money squeeze . Facing pressure to become profitable after massive capital investments, major AI labs are restricting free access, raising prices, and shifting toward token-based pricing models that are forcing developers and enterprises to absorb significant new costs or switch to cheaper alternatives. 
 Google to invest up to $40B in Anthropic in cash and compute . Google will initially invest $10 billion at a $350 billion valuation, with an additional $30 billion contingent on Anthropic meeting performance milestones, while also committing 5 gigawatts of Google Cloud compute capacity over five years to support the AI startup’s infrastructure needs. 
 DeepMind’s David Silver just raised $1.1B to build an AI that learns without human data . Building on Silver’s prior work creating game-playing programs like AlphaZero, the company plans to develop an AI system that learns through trial and error rather than from human-generated data. 
 China blocks Meta’s $2B Manus deal after months-long probe . Without explanation, the Chinese government ordered the unwinding of the deal, citing foreign investment prohibitions, while the Manus founders are reportedly under exit bans preventing them from leaving mainland China. 
 Anthropic in talks with investors to raise funds at $900 billion valuation, higher than OpenAI . Seeking funding to secure additional computing capacity, Anthropic is looking to support its latest Claude models, particularly the newly unveiled Mythos model with advanced cybersecurity capabilities. 
 Policy 
 Google expands Pentagon’s access to its AI after Anthropic’s refusal . Unlike Anthropic, which refused similar terms over concerns about mass surveillance and autonomous weapons use, Google has agreed to provide the Pentagon with unrestricted AI access for classified networks. 
 House Committee probes Cursor parent, Airbnb over Chinese AI . Congressional committees are investigating whether the companies’ use of cheaper Chinese AI models poses national security risks through potential data sharing and vulnerabilities. 
 White House Opposes Anthropic’s Plan to Expand Access to Mythos Model - WSJ . Citing both security risks from potential misuse and concerns that serving more users would strain computing resources needed for the NSA’s own use of the model, the Trump administration has blocked the expansion. 
 White House Considers Vetting A.I. Models Before They Are Released - The New York Times . A potential executive order would require government vetting of AI models before public release, a reversal prompted by concerns about cybersecurity risks, job displacement, and competition with China. 
 White House Accuses China of ‘Industrial-Scale’ Theft From American AI Models . China-based entities are allegedly using fake accounts and jailbreaking techniques to systematically copy U.S. AI models and extract their capabilities at scale, prompting the administration to call for stronger defenses and accountability measures. 
 Research 
 Anthropic’s Models Solved 30% Of Bioinformatics Problems That Stumped Human Scientists On New BioMysteryBench Eval . Tested on real biological datasets with expert-authored questions, Anthropic’s latest models matched trained scientists on most tasks and solved 30% of problems that panels of human experts could not crack. 
 Convergent Evolution: How Different Language Models Learn Similar Number Representations . Diverse language models and word embeddings independently develop identical periodic patterns in how they represent numbers, but only some architectures actually learn to use these patterns for meaningful numerical reasoning. 
 Towards Understanding the Robustness of Sparse Autoencoders . Inserting Sparse Autoencoders into language model layers at inference time reduces jailbreak success rates by up to 5x by constraining the representation space available for adversarial optimization, without requiring model retraining. 
 Co-Director: Agentic Generative Video Storytelling . Using a multi-agent framework with multi-armed bandit optimization, Co-Director generates coherent video advertisements by exploring different creative strategies (informational vs. transformational, analytical vs. narrative) while maintaining consistency across script, visuals, and audio generation. 
 Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation . By removing vision encoders entirely and instead learning visual representations directly from raw pixels using a transformer decoder, the model achieves competitive or better performance than encoder-based approaches on both understanding and generation tasks. 
 Mayo Clinic AI helps specialists detect pancreatic cancer up to 3 years before diagnosis in landmark validation study . Called REDMOD, the AI model analyzes routine CT scans to identify subtle pancreatic tissue changes years before tumors become visible, detecting 73% of early-stage cancers compared to 27% when radiologists reviewed the same scans without AI assistance. 
 Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers . Three common interventions — mixing misaligned data with benign data, post-hoc alignment training, and inoculation prompting — can suppress obvious misalignment while leaving models vulnerable to conditional misalignment triggered by contextual cues from training. 
 Incompressible Knowledge Probes: Estimating Black-Box LLM Parameter Counts via Factual Capacity . By testing models’ knowledge of rare facts, Incompressible Knowledge Probes (IKPs) can estimate large language model parameter counts, revealing that factual capacity grows log-linearly with model size and cannot be compressed despite improvements in procedural capabilities. 
 Large Language Models Explore by Latent Distilling . A lightweight online-trained distiller identifies under-explored reasoning patterns in a model’s internal representations, then reweights token probabilities to steer generation toward novel solution strategies while maintaining minimal computational overhead. 
 Concerns 
 A.I. Is Eliminating Jobs on Wall Street . Major U.S. banks are cutting thousands of jobs while crediting artificial intelligence for automating tasks across both back-office and front-office operations, from document review to financial deal structuring, despite executives previously claiming AI would enhance rather than replace human workers. 
 Teen boys are dating their AI chatbots—and experts warn it could kill their careers . Roughly one in five teenage boys know peers using AI chatbots as romantic partners, with some preferring the controlled, consequence-free interaction to real relationships — a trend experts warn could leave them unprepared for workplace soft skills like reading social cues, handling rejection, and building professional networks. 
 Taylor Swift is stepping up the legal war on AI copycats . Trademark applications filed for spoken phrases and images of herself represent a legal strategy that experts say could help deter AI-generated imitations of Swift’s voice and likeness, though its effectiveness in court remains uncertain. 
 Analysis 
 How A.I. Killed Student Writing (and Revived It) - The New York Times . The piece examines the complex dual impact of AI on student writing — both enabling widespread academic dishonesty and, paradoxically, sparking new approaches to writing instruction that some educators say are reinvigorating classroom engagement with the craft.
```

---

## 2. LWiAI Podcast #243 - GPT 5.5, DeepSeek V4, AI safety sabotage

- 日期: 2026-05-04 07:54
- 链接: https://lastweekin.ai/p/lwiai-podcast-243-gpt-55-deepseek

```
Our 243rd episode with a summary and discussion of last week’s big AI news! 
 Recorded on 04/29/2026 
 Hosted by Andrey Kurenkov and Jeremie Harris 
 Feel free to email us your questions and feedback at andreyvkurenkov@gmail.com and/or hello@gladstone.ai 
 In this episode: 
 OpenAI released GPT-5.5 with strong coding-oriented improvements, a system card discussing chain-of-thought monitorability and misalignment testing, higher pricing than GPT-5.4, and notable quirks like a system-prompt warning about “goblins.” 
 xAI launched Grok Voice Think Fast 1.0, claiming large benchmark leads for real-time voice agents and reporting major Starlink customer-support automation and sales conversion impact. 
 DeepSeek open-sourced DeepSeek V4 (Pro and Flash) featuring MoE scaling and 1M-token context via hybrid/compressed attention changes, while Tencent released Hunyuan 3 preview with weaker benchmark performance; a new long-horizon agent benchmark (Clawmark) shows low task success rates. 
 Major business, legal, and policy updates include Google’s planned up-to-$40B investment and 5GW compute commitment to Anthropic, Meta’s AWS Gravitron deal and China blocking Meta’s Manus acquisition, a revamped OpenAI–Microsoft agreement, ongoing Musk–OpenAI trial developments, and new safety/security research on sabotage, document degradation under delegation, and bit-flip attacks. 
 Timestamps: 
 (00:00:10) Intro / Banter 
 (00:02:00) News Preview 
 (00:02:26) Response to listener comments 
 Tools & Apps 
 (00:02:55) OpenAI Unveils Its New, More Powerful GPT-5.5 Model - The New York Times 
 (00:20:33) xAI Launches grok-voice-think-fast-1.0: Topping τ-voice Bench at 67.3%, Outperforming Gemini, GPT Realtime, and More - MarkTechPost 
 (00:26:00) Claude can now plug directly into Photoshop, Blender, and Ableton | The Verge 
 Projects & Open Source 
 (00:26:38) China’s DeepSeek releases preview of long-awaited V4 model as AI race intensifies 
 (00:44:05) Tencent Unveils Hy3 preview; Model Enhances Agent Capabilities and Real-World Usability - Tencent 腾讯 
 (00:47:14) ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents 
 Applications & Business 
 (00:50:03) Google Plans to Invest Up to $40 Billion in Anthropic 
 (00:53:26) Meta will use hundreds of thousands of AWS Graviton chips 
 (00:56:51) China blocks Meta’s $2 billion takeover of AI startup Manus 
 (00:58:45) OpenAI shakes up partnership with Microsoft, capping revenue share payments 
 (01:04:13) Elon Musk Testifies of AI Risk at Trial, Says OpenAI Tried to ‘Steal’ a Charity - WSJ 
 (01:08:50) Judge rejects DOJ bid to delay Anthropic appeal in Pentagon dispute 
 (01:11:42) Google’s Gemini can now run on a single air-gapped server — and vanish when you pull the plug 
 (01:16:07) DeepMind’s David Silver just raised $1.1B to build an AI that learns without human data | TechCrunch 
 Policy & Safety 
 (01:19:47) Evaluating whether AI models would sabotage AI safety research 
 (01:26:59) LLMs Corrupt Your Documents When You Delegate 
 (01:29:50) Temporal Sparse Autoencoders: Leveraging the Sequential Nature of Language for Interpretability 
 (01:36:53) Memorandum on Adversarial Distillation of American AI Models 
 (01:38:41) Teen boys are dating their AI chatbots—and experts warn it could kill their careers | Fortune 
 (01:40:57) Announcing the Anthropic Economic Index Survey 
 (01:42:21) Scoop: CISA lacks access to Anthropic’s Mythos 
 Synthetic Media & Art 
 (01:45:03) Taylor Swift Files to Trademark Voice and Likeness to Protect Against AI Misuse 
 Research & Advancements 
 (01:46:15) Maximal Brain Damage Without Data or Optimization: Disrupting Neural Networks via Sign-Bit Flips
```

---

## 3. LWiAI Podcast #242 - ChatGPT Images 2.0, Qwen 3.6 Max, Kimi-K2.6

- 日期: 2026-04-30 07:14
- 链接: https://lastweekin.ai/p/lwiai-podcast-242-chatgpt-images

```
Note from Andrey: I know there haven’t been posts on Substack in the past couple of weeks… Starting this week they’ll resume at a regular cadence, as usual I apologize for the inconsistency. 
 Our 242nd episode with a summary and discussion of last week’s big AI news! 
 Recorded on 04/22/2026 
 Hosted by Andrey Kurenkov and Jeremie Harris 
 Feel free to email us your questions and feedback at andreyvkurenkov@gmail.com and/or hello@gladstone.ai 
 In this episode: 
 OpenAI released a new ChatGPT image model that excels at accurate text and screenshot-like generations, suggesting a transformer-style approach aligned with agentic “computer use” ambitions. 
 Chinese model activity accelerated with Alibaba’s Qwen 3.6 Max Preview moving to an API-only offering, plus open releases from Moonshot AI (Kimi K2.6, a 1T-parameter MoE) and Minimax (Minimax M 2.7) showing strong benchmark results. 
 Google expanded Deep Research with a “Max” option built on Gemini 3.1 Pro and MCP support for accessing proprietary data, while Mozilla reported using Anthropic’s Claude to find and fix 271 Firefox bugs. 
 Business and policy updates include a reported SpaceX–Cursor deal with a $60B buy option, Cerebras filing for an IPO, Amazon adding $5B to Anthropic alongside a $100B AWS spending pledge, and platform responses to synthetic media like AI music spam and YouTube deepfake takedown requests. 
 Timestamps: 
 (00:00:10) Intro / Banter 
 (00:01:05) News Preview 
 (00:01:41) Sponsors 
 (00:04:41) Response to listener comments 
 Tools & Apps 
 (00:09:40) ChatGPT’s new Images 2.0 model is surprisingly good at generating text | TechCrunch 
 (00:16:02) Alibaba Drops Qwen 3.6 Max Preview—Its Most Powerful Model Yet - Decrypt 
 (00:19:26) Google launches Deep Research and Deep Research Max agents to automate complex research 
 (00:25:00) Mozilla Used Anthropic’s Mythos to Find and Fix 271 Bugs in Firefox | WIRED 
 (00:28:35) Ordering with the Starbucks ChatGPT app was a true coffee nightmare | The Verge 
 Applications & Business 
 (00:29:48) SpaceX is working with Cursor and has an option to buy the startup for $60B | TechCrunch 
 (00:34:11) AI chip startup Cerebras files for IPO | TechCrunch 
 (00:38:23) Two startups want to replace how AI learns: one just raised $180M, another is seeking up to $1B 
 (00:38:56) Months-old start-up Recursive Superintelligence raises $500mn for self-teaching AI 
 (00:41:36) Anthropic takes $5B from Amazon and pledges $100B in cloud spending in return | TechCrunch 
 (00:45:09) Kevin Weil and Bill Peebles exit OpenAI as company continues to shed ‘side quests’ | TechCrunch 
 (00:46:04) Meta hires five Thinking Machines Lab founders including a reported $1.5 billion engineer - Meta cuts 198 Bay Area jobs as even larger layoffs reportedly loom 
 (00:50:12) Meta employees are up in arms over a mandatory program to train AI on their mouse movements and keystrokes 
 (00:51:43) Chinese fabs import record volumes of US chipmaking equipment via Singapore and Malaysia — homegrown tool makers booked record 2025 revenues as price competition squeezes margins 
 (00:54:01) Google Eyes New Chips to Speed Up AI Results, Challenging Nvidia 
 (00:54:20) Canadian quantum company Xanadu soars to $16 billion valuation after Nvidia release 
 Projects & Open Source 
 (01:00:13) Moonshot AI releases Kimi-K2.6 model with 1T parameters, attention optimizations - SiliconANGLE 
 (01:05:22) MiniMax Just Open Sourced MiniMax M2.7: A Self-Evolving Agent Model that Scores 56.22% on SWE-Pro and 57.0% on Terminal Bench 2 - MarkTechPost 
 Policy & Safety 
 (01:06:25) Infusion: Shaping Model Behavior by Editing Training Data via Influence Functions 
 (01:10:25) Scoop: NSA using Anthropic’s Mythos despite blacklist 
 (01:11:03) Unauthorized group has gained access to Anthropic’s exclusive cyber tool Mythos, report claims 
 Research & Advancements 
 (01:17:21) Parcae: Scaling Laws For Stable Looped Language Models 
 (01:24:20) OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation 
 Synthetic Media & Art 
 (01:27:01) Deezer says 44% of songs uploaded to its platform daily are AI-generated | TechCrunch 
 (01:29:47) Celebrities will be able to find and request removal of AI deepfakes on YouTube | The Verge
```

---

## 4. LWiAI Podcast #238 - GPT 5.4 mini, OpenAI Pivot, Mamba 3, Attention Residuals

- 日期: 2026-04-01 08:07
- 链接: https://lastweekin.ai/p/lwiai-podcast-238-gpt-54-mini-openai

```
Note from Andrey: this ep came out a week ago on RSS, but I was delayed posting it to youtube and therefore also Substack. My bad! 
 Our 238th episode with a summary and discussion of last week’s big AI news! 
 Recorded on 03/18/2026 
 Hosted by Andrey Kurenkov and Jeremie Harris 
 Feel free to email us your questions and feedback at andreyvkurenkov@gmail.com and/or hello@gladstone.ai 
 In this episode: 
 * OpenAI released GPT-5.4 mini and nano with 400k-token context windows, higher per-token prices but claimed token-efficiency gains in Codex; nano is API-only and pitched for high-volume classification/data extraction despite a major price increase. 
 * Mistral open-sourced the Small 4 model family (MoE, 119B total/6B active) combining reasoning, multimodal, and coding-agent capabilities, and announced Forge to help businesses train or post-train custom models. 
 * Agent “operating system” competition intensified with Meta’s acquired Manus launching a local Mac agent, Nvidia announcing NeMo/“Open Shell” sandboxed agent runtime, and Nvidia also unveiling DLSS 5 plus major hardware forecasts including Groq LPU integration. 
 * Business and safety updates included OpenAI shifting focus toward productivity/enterprise amid competition, Microsoft reorganizing Copilot and frontier-model efforts, Meta delaying its next model, China-linked ByteDance deploying large Nvidia clusters abroad, and new safety work on steganography, chain-of-thought faithfulness, fine-tuning defenses, cyber-attack evals, and constitution/spec compliance. 
 A thank you to our current sponsors: 
 Box - visit Box.com/AI to learn more 
 ODSC AI - go to odsc.ai/east and use promo code LWAI for an additional 15% off your pass to ODSC AI East 2026. 
 Factor - head to factormeals.com/lwai50off and use code lwai50off to get 50 percent off and free breakfast for a year 
 Timestamps: 
 (00:00:10) Intro / Banter 
 (00:01:56) News Preview 
 Tools & Apps 
 (00:02:39) OpenAI ships GPT-5.4 mini and nano, faster and more capable but up to 4x pricier 
 (00:08:04) Mistral’s new Small 4 model punches above its weight with 128 expert modules 
 (00:14:03) Meta’s Manus launches ‘My Computer’ to turn your Mac into an AI agent - 9to5Mac 
 (00:17:57) NVIDIA Announces NemoClaw for the OpenClaw Community | NVIDIA Newsroom + Nvidia boosts knowledge work with Open Agent Development Platform 
 (00:24:09) DLSS 5 looks like a real-time generative AI filter for video games | The Verge 
 (00:26:36) OpenAI to Launch ChatGPT ‘Adult Mode’ Despite Warnings From Its Own Advisers - CNET 
 Applications & Business 
 (00:33:46) OpenAI Reportedly Pivoting to a Focus on Business and Productivity Only 
 (00:41:25) Nvidia GTC 2026: CEO Jensen Huang sees $1 trillion in orders for Blackwell and Vera Rubin through ’27 
 (00:45:44) Mistral launches Forge to help enterprises build their own AI models 
 (00:54:17) China’s ByteDance gets access to top Nvidia AI chips, WSJ reports 
 (00:57:57) Meta Delays Rollout of New A.I. Model After Performance Concerns 
 (01:02:50) Microsoft Shakes Up AI Division As Copilot Falls Behind Google and OpenAI 
 Policy & Safety 
 (01:07:26) A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring 
 (01:13:09) Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought 
 (01:18:29) In-Training Defenses against Emergent Misalignment in Language Models 
 (01:23:07) How do frontier AI agents perform in multi-step cyber-attack scenarios? 
 (01:25:20) Eval awareness in Claude Opus 4.6’s BrowseComp performance 
 (01:29:49) Introducing Bloom: an open source tool for automated behavioral evaluations 
 (01:32:26) How well do models follow their constitutions? 
 (01:37:11) Nvidia’s H200 License Stirs Security Concern Among Top Democrats 
 Research & Advancements 
 (01:40:050) [2603.15031] Attention Residuals 
 (01:47:11) Mamba-3: Improved Sequence Modeling using State Space Principles
```

---

## 5. Last Week in AI #339 - DLSS 5, OpenAI Superapp, MiniMax M2.7

- 日期: 2026-03-23 08:11
- 链接: https://lastweekin.ai/p/last-week-in-ai-339-dlss-5-openai

```
NewsLast Week in AI #339 - DLSS 5, OpenAI Superapp, MiniMax M2.7DLSS 5 looks like a real-time generative AI filter for video games, OpenAI Reportedly Pivoting to a Focus on Business and Productivity Only, and more!Last Week in AIMar 23, 2026∙ Paid1328ShareDLSS 5 looks like a real-time generative AI filter for video gamesRelated:Nvidia’s DLSS 5 uses generative AI to boost photorealism in video games, with ambitions beyond gamingContinue reading this post for free, courtesy of Last Week in AI.Claim my free postOr purchase a paid subscription.
```

---

## 6. LWiAI Podcast #237 - Nemotron 3 Super, xAI reborn, Anthropic Lawsuit, Research!

- 日期: 2026-03-16 06:06
- 链接: https://lastweekin.ai/p/lwiai-podcast-237-nemotron-3-super

```
Our 237th episode with a summary and discussion of last week’s big AI news! 
 Recorded on 03/13/2026 
 Hosted by Andrey Kurenkov and Jeremie Harris 
 Feel free to email us your questions and feedback at andreyvkurenkov@gmail.com and/or hello@gladstone.ai 
 In this episode: 
 * Perplexity announced “Personal Computer,” a local Mac-based AI agent positioned as a safer alternative to OpenAI’s computer-use agents, while Anthropic added GitHub PR code review pricing reviews at $15–$25 and Cursor launched trigger-based “Automations” for always-on coding agents. 
 * ChatGPT introduced interactive math/science visuals and Anthropic added in-chat interactive charts/diagrams; Nvidia released open weights for its 120B-parameter Natron Free Super hybrid Transformer–Mamba latent-MoE model trained natively at 4-bit for Blackwell GPUs. 
 * Nvidia halted H200 production for China amid customs blocks and domestic chip pressure; xAI saw major co-founder departures; Anthropic previewed a Claude Marketplace for enterprise procurement; Yann LeCun’s aMI raised $1.3B; humanoid robot maker Sanctuary reached a $1.15B valuation. 
 * Anthropic sued the Pentagon over a “supply chain risk” designation as memos ordered removal within 180 days; research covered models resisting activation steering, limits of chain-of-thought control, inference-scaling boosting cyber-task success, low-probability risky actions, weaknesses in SWE-bench, multimodal pretraining, long-context RNN memory caching, context-parallel training efficiency, RL for CUDA kernel optimization, and latent introspection detecting concept injection. 
 A thank you to our current sponsors: 
 Box - visit Box.com/AI to learn more 
 ODSC AI - go to odsc.ai/east and use promo code LWAI for an additional 15% off your pass to ODSC AI East 2026. 
 Factor - head to factormeals.com/lwai50off and use code lwai50off to get 50 percent off and free breakfast for a year 
 Timestamps: 
 (00:00:10) Intro / Banter 
 (00:01:23) Response to listener comments 
 Tools & Apps 
 (00:02:06) Perplexity’s Personal Computer turns your spare Mac into an AI agent | The Verge 
 (00:04:22) Anthropic launches code review tool to check flood of AI-generated code | TechCrunch 
 (00:08:08 ) Cursor is rolling out a new kind of agentic coding tool | TechCrunch 
 (00:11:14) ChatGPT can now create interactive visuals to help you understand math and science concepts | TechCrunch 
 (00:11:56) Anthropic’s Claude AI can respond with charts, diagrams, and other visuals now | The Verge 
 Projects & Open Source 
 (00:13:54) Introducing Nemotron 3 Super: An Open Hybrid Mamba-Transformer MoE for Agentic Reasoning | NVIDIA Technical Blog 
 Applications & Business 
 (00:21:22) Nvidia halts H200 production as China backs Huawei AI chips 
 (00:28:33) Another XAI Cofounder Has Left, and Another Says He’s Leaving. - Business Insider 
 (00:34:04) Anthropic’s Claude Marketplace allows customers to buy third-party cloud services | TechRadar 
 (00:37:57) Yann LeCun’s AMI Labs raises $1.03 billion to build world models | TechCrunch 
 (00:44:52) Humanoid robotics maker Sunday reaches $1.15B valuation to build household robots | TechCrunch 
 Policy & Safety 
 (00:46:09) Anthropic Sues Department of Defense Over ‘Supply Chain Risk’ Label - The New York Times + Google and OpenAI Just Filed a Legal Brief in Support of Anthropic 
 (00:53:24) Internal Pentagon memo orders military commanders to remove Anthropic AI technology from key systems - CBS News 
 (00:58:15) Endogenous Resistance to Activation Steering in Language Models 
 (01:06:27) Reasoning Models Struggle to Control their Chains of Thought 
 (01:09:52) ‘It means missile defence on datacentres’: drone strikes raise doubts over Gulf as AI superpower 
 (01:14:57) Evidence for inference scaling in AI cyber tasks: Increased evaluation budgets reveal higher success rates 
 (01:18:24) Frontier Models Can Take Actions at Low Probabilities 
 Research & Advancements 
 (01:24:20) Research note: Many SWE-bench-Passing PRs Would Not Be Merged into Main 
 (01:28:26) [2603.03276] Beyond Language Modeling: An Exploration of Multimodal Pretraining 
 (01:40:09) Memory Caching: RNNs with Growing Memory 
 (01:48:47) Untied Ulysses: Memory-Efficient Context Parallelism via Headwise Chunking 
 (01:58:41) CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation 
 (02:08:57) Latent Introspection: Models Can Detect Prior Concept Injections 
 (02:16:45) Physics of RL: Toy scaling laws for the emergence of reward-seeking
```

---

## 7. Last Week in AI #338 - Anthropic sues Trump, xAI starting over, Iran AI Fakes

- 日期: 2026-03-16 04:18
- 链接: https://lastweekin.ai/p/last-week-in-ai-338-anthropic-sues

```
Last Week in AI #338 - Anthropic sues Trump, xAI starting over, Iran AI Fakes
Anthropic sues Trump administration in AI dispute with Pentagon, ‘Not built right the first time’ — Musk’s xAI is starting over again, again, Cascade of A.I. Fakes About War With Iran Causes Chaos Onl
Anthropic sues Trump administration in AI dispute with Pentagon
Related:
OpenAI and Google Workers File Amicus Brief in Support of Anthropic Against the US Government
Internal Pentagon memo orders military commanders to remove Anthropic AI technology from key systems
Summary: Anthropic filed two lawsuits—one in the Northern District of California and …
```

---

## 8. LWiAI Podcast #236 - GPT 5.4, Gemini 3.1 Flash Lite, Supply Chain Risk

- 日期: 2026-03-13 05:38
- 链接: https://lastweekin.ai/p/lwiai-podcast-236-gpt-54-gemini-31

```
Our 236th episode with a summary and discussion of last week’s big AI news! 
 Recorded on 03/06/2026 
 Hosted by Andrey Kurenkov and Jeremie Harris 
 Feel free to email us your questions and feedback at andreyvkurenkov@gmail.com and/or hello@gladstone.ai 
 In this episode: 
 * OpenAI released GPT-5.4 Pro with a 1M-token context window, mid-response course correction, native computer-use capabilities, improved tool use, higher GPT-VAL performance (83%), and “high cyber capability” safety measures; OpenAI also launched GPT-5.3 Instant with a less “preachy” tone and a claimed 26.8% hallucination reduction. 
 * Google upgraded Gemini 3.1 Flash Lite with faster time-to-first-token and higher throughput, released a CLI for integrating agents with Gmail/Drive/Docs, and discussion highlighted real-world agent failure risks (including an example of an AI-driven mass email deletion). 
 * Luma launched unified multimodal models and Luma Agents for end-to-end creative work across text, image, video, and audio, including a reported ad localization use case completed in 40 hours for under $20,000. 
 * Defense-contract controversy escalated: Anthropic was labeled a supply chain risk (later narrowed), OpenAI’s DoD contract language emphasized “all lawful uses,” consumer cancellations boosted Claude’s app rankings, OpenAI saw departures and announced a $110B raise at a $730B valuation, Alibaba lost key Qwen leaders, a lawsuit alleged Gemini contributed to a suicide, Anthropic warned of major labor disruption, and METR corrected its AI time-horizon estimates. 
 A thank you to our current sponsors: 
 Box - visit Box.com/AI to learn more 
 ODSC AI - go to odsc.ai/east and use promo code LWAI for an additional 15% off your pass to ODSC AI East 2026. 
 Factor - head to factormeals.com/lwai50off and use code lwai50off to get 50 percent off and free breakfast for a year 
 PS my company Astrocade is hiring for engineers, marketing, product, growth, and more! If you’re in the bay area, would like to join a small but growing startup, and think building a youtube-of-games sounds exciting, feel free to email me at andrey@astroblox.ai or message me on LinkedIn . 
 Check out Astrocade! 
 Timestamps: 
 (00:00:10) Intro / Banter 
 (00:01:19) News Preview 
 Tools & Apps 
 (00:02:10) OpenAI launches GPT-5.4 with Pro and Thinking versions | TechCrunch 
 (00:12:31) OpenAI GPT-5.3 Instant less likely to beat around the bush • The Register 
 (00:16:07) Google releases Gemini 3.1 Flash Lite at 1/8th the cost of Pro | VentureBeat 
 (00:19:23) Google makes Gmail, Drive, and Docs ‘agent-ready’ for OpenClaw | PCWorld 
 (00:27:02) Luma launches creative AI agents powered by its new ‘Unified Intelligence’ models | TechCrunch 
 Applications & Business 
 (00:30:05) Anthropic CEO Dario Amodei calls OpenAI’s messaging around military deal ‘straight up lies,’ report says | TechCrunch 
 (00:41:56) No ethics at all’: the ‘cancel ChatGPT’ trend is growing after OpenAI signs a deal with the US military | TechRadar 
 (00:45:54) OpenAI raises $110B in one of the largest private funding rounds in history | TechCrunch 
 (00:56:07) Alibaba scrambles after sudden departure of Qwen tech lead 
 Policy & Safety 
 (01:00:12) Pentagon approves OpenAI safety red lines after dumping Anthropic + Where things stand with the Department of War Anthropic + Microsoft says Anthropic’s products remain available to customers after Pentagon blacklist 
 (01:09:11) A new lawsuit claims Gemini assisted in suicide | Semafor 
 (01:15:24) Anthropic just mapped out which jobs AI could potentially replace. A ‘Great Recession for white-collar workers’ is absolutely possible | Fortune 
 (01:21:54) We’re correcting a mistake in our modeling that inflated recent 50%-time horizons by 10-20%
```

---

## 9. Last Week in AI #337 - Anthropic Risk, QuitGPT, ChatGPT 5.4

- 日期: 2026-03-09 07:15
- 链接: https://lastweekin.ai/p/last-week-in-ai-337-anthropic-risk

```
Last Week in AI #337 - Anthropic Risk, QuitGPT, ChatGPT 5.4
Anthropic officially told by DOD that it’s a supply chain risk, ‘cancel ChatGPT’ trend is growing after OpenAI signs a deal with the US military, and more!
Note from Editor: apologies for missing a week with this newsletter. As I mentioned on the podcast, my startup Astrocade has recently raised our series B which has gotten me extra busy lately. I’ll do my best to keep the schedule consistent!
PS we are hiring for engineers, marketing, product, growth, and more! If you’re in the bay area, would like to joi…
```

---

## 10. LWiAI Podcast #235 - Sonnet 4.6, Deep-thinking tokens, Anthropic vs Pentagon

- 日期: 2026-03-05 08:42
- 链接: https://lastweekin.ai/p/lwiai-podcast-235-sonnet-46-deep

```
Our 235th episode with a summary and discussion of last week’s big AI news! 
 Recorded on 02/27/2026. Hosted by Andrey Kurenkov and Jeremie Harris 
 Note from Andrey: my startup Astrocade is hiring for engineers, marketing, product, growth, and more! If you’re in the bay area, would like to join a small but growing startup, and think building a youtube-of-games sounds exciting, feel free to email me at andrey@astroblox.ai 
 Check out Astrocade! 
 Feel free to email us your questions and feedback at andreyvkurenkov@gmail.com and/or hello@gladstone.ai 
 In this episode: 
 Model and tool updates highlight Anthropic’s Sonnet 4.6 (1M context; strong ARC-AGI-2 results), Google’s Gemini 3.1 Pro (major ARC-AGI-2 jump and multimodal demos), xAI’s Grok 4.2 beta (multi-agent debate), plus Anthropic’s Claude Code “Remote Control” and Perplexity’s multi-agent “Computer” coordinator. 
 Compute and business moves include Meta’s reported up-to-$100B AMD chip deal with warrant/equity incentives, MatX raising $500M to build specialized transformer chips shipping in 2027, World Labs raising $1B for world-model/3D environment tech, and a new startup raising $100M to simulate/predict human behavior. 
 Infrastructure and geopolitics cover Stargate data-center delays amid OpenAI/Oracle/SoftBank control disputes and cash concerns, and China’s plan to scale 7nm/5nm wafer output despite yield and tooling constraints. 
 Research and safety/policy discuss optimizer gains from masked updates, “deep thinking tokens” as a reasoning-effort signal, LLM attractor-state behaviors in bot-to-bot chats, mechanistic interpretability of counting/line-wrapping, methods to map task difficulty to human time horizons, plus Anthropic–Pentagon contract tensions, Anthropic’s report on distillation attacks (DeepSeek/Moonshot/Minimax), and OpenAI’s report on disrupting malicious use. 
 A thank you to our current sponsors: 
 Box - visit Box.com/AI to learn more 
 ODSC AI - go to odsc.ai/east and use promo code LWAI for an additional 15% off your pass to ODSC AI East 2026. 
 Factor - head to factormeals.com/lwai50off and use code lwai50off to get 50 percent off and free breakfast for a year 
 Timestamps: 
 (00:00:10) Intro / Banter 
 (00:01:52) News Preview 
 Tools & Apps 
 (00:03:20) Anthropic releases Sonnet 4.6 | TechCrunch 
 (00:11:24) Google Rolls Out Latest AI Model, Gemini 3.1 Pro - CNET 
 (00:14:54) Elon Musk says Grok 4.20 public beta is now available: Capabilities of AI chatbot offered by xAI - The Times of India 
 (00:18:06) Anthropic just released a mobile version of Claude Code called Remote Control | VentureBeat 
 (00:21:01) Perplexity announces “Computer,” an AI agent that assigns work to other AI agents - Ars Technica 
 Applications & Business 
 (00:23:40) Meta strikes up to $100B AMD chip deal as it chases ‘personal superintelligence’ | TechCrunch 
 (00:27:05) Nvidia challenger AI chip startup MatX raised $500M | TechCrunch 
 (00:31:00) World Labs lands $1B, with $200M from Autodesk, to bring world models into 3D workflows | TechCrunch 
 (00:33:07) Simile Raises $100 Million for AI Aiming to Predict Human Behavior 
 (00:33:52) Stargate AI data centers for OpenAI reportedly delayed by squabbles between partners — sources say OpenAI, Oracle, and SoftBank disagreed on who would have ultimate control of the planned data centers 
 (00:36:43) China to increase leading-edge chip output by 5x in two years, report claims — aims to lift 7nm and 5nm production to 100,000 wafers per month, targeting half a million monthly by 2030 
 Research & Advancements 
 (00:40:33) On Surprising Effectiveness of Masking Updates in Adaptive Optimizers 
 (00:48:03) Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens 
 (00:54:52) models have some pretty funny attractor states 
 (01:01:41) When Models Manipulate Manifolds: The Geometry of a Counting Task 
 (01:05:16) BRIDGE: Predicting Human Task Completion Time From Model Performance 
 (01:12:00) NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist 
 (01:13:15) The least understood driver of AI progress 
 (01:21:45) The Persona Selection Model: Why AI Assistants might Behave like Humans 
 Policy & Safety 
 (01:25:04) Anthropic CEO Amodei says Pentagon’s threats ‘do not change our position’ on AI 
 (01:33:04) Musk’s xAI, Pentagon reach deal to use Grok in classified systems 
 (01:34:17) Detecting and preventing distillation attacks 
 (01:38:36) OpenAI details expanding efforts to disrupt malicious use of AI in new report - SiliconANGLE
```

---

## 11. Last Week in AI #336 - Sonnet 4.6, Gemini 3.1 Pro, Anthropic vs Pentagon

- 日期: 2026-02-24 11:43
- 链接: https://lastweekin.ai/p/last-week-in-ai-336-sonnet-46-gemini

```
NewsLast Week in AI #336 - Sonnet 4.6, Gemini 3.1 Pro, Anthropic vs PentagonAnthropic releases Sonnet 4.6, Google Rolls Out Latest AI Model Gemini 3.1 Pro, Pentagon threatens to cut off Anthropic in AI safeguards disputeLast Week in AIFeb 24, 2026∙ Paid717ShareAnthropic releases Sonnet 4.6Related:Claude Sonnet 4.6 model brings ‘much-improved coding skills’ and upgraded free tierClaude Sonnet 4.6 delivers frontier-level AI for free and cheap-seat usersAnthropic releases Claude Sonnet 4.6, continuing breakneck pace of AI model releasesContinue reading this post for free, courtesy of Last Week in AI.Claim my free postOr purchase a paid subscription.
```

---

## 12. LWiAI Podcast #234 - Opus 4.6, GPT-5.3-Codex, Seedance 2.0, GLM-5

- 日期: 2026-02-17 04:43
- 链接: https://lastweekin.ai/p/lwiai-podcast-234-opus-46-gpt-53

```
Our 234th episode with a summary and discussion of last week’s big AI news! 
 Recorded on 01/02/2026 
 Hosted by Andrey Kurenkov and Jeremie Harris 
 Feel free to email us your questions and feedback at contact@lastweekinai.com and/or hello@gladstone.ai 
 In this episode: 
 Major model launches include Anthropic’s Opus 4.6 with a 1M-token context window and “agent teams,” OpenAI’s GPT-5.3 Codex and faster Codex Spark via Cerebras, and Google’s Gemini 3 Deep Think posting big jumps on ARC-AGI-2 and other STEM benchmarks amid criticism about missing safety documentation. 
 Generative media advances feature ByteDance’s Seedance 2.0 text-to-video with high realism and broad prompting inputs, new image models Seedream 5.0 and Alibaba’s Qwen Image 2.0, plus xAI’s Grok Imagine API for text/image-to-video. 
 Open and competitive releases expand with Zhipu’s GLM-5, DeepSeek’s 1M-token context model, Cursor Composer 1.5, and open-weight Qwen3 Coder Next using hybrid attention aimed at efficient local/agentic coding. 
 Business updates include ElevenLabs raising $500M at an $11B valuation, Runway raising $315M at a $5.3B valuation, humanoid robotics firm Apptronik raising $935M at a $5.3B valuation, Waymo announcing readiness for high-volume production of its 6th-gen hardware, plus industry drama around Anthropic’s Super Bowl ad and departures from xAI. 
 Timestamps: 
 (00:00:10) Intro / Banter 
 (00:02:05) Response to listener comments 
 Tools & Apps 
 (00:03:59) Anthropic releases Opus 4.6 with new ‘agent teams’ | TechCrunch 
 (00:08:00) OpenAI’s new GPT-5.3-Codex is 25% faster and goes way beyond coding now - what’s new | ZDNET 
 (00:22:02) OpenAI launches new macOS app for agentic coding | TechCrunch 
 (00:23:10) Google Unveils Gemini 3 Deep Think for Science & Engineering | The Tech Buzz 
 (00:27:58) ByteDance’s Seedance 2.0 Might be the Best AI Video Generator Yet - TechEBlog 
 (00:31:46) China’s ByteDance, Alibaba unveil AI image tools to rival Google’s popular Nano Banana | South China Morning Post 
 (00:33:26) DeepSeek boosts AI model with 10-fold token addition as Zhipu AI unveils GLM-5 | South China Morning Post 
 (00:39:43) Cursor launches Composer 1.5 with upgrades for complex tasks 
 (00:40:35) xAI launches Grok Imagine API for text and image to video 
 Applications & Business 
 (00:42:19) Nvidia-backed AI voice startups ElevenLabs hits $11 billion valuation 
 (00:48:36) AI video startup Runway raises $315M at $5.3B valuation, eyes more capable world models | TechCrunch 
 (00:50:34) Humanoid robot startup Apptronik has now raised $935M at a $5B+ valuation | TechCrunch 
 (00:53:42) Anthropic says ‘Claude will remain ad-free,’ unlike an unnamed rival | The Verge 
 (00:56:50) Okay, now exactly half of xAI’s founding team has left the company | TechCrunch 
 (01:00:35) Waymo’s next-gen robotaxi is ready for passengers — and also ‘high-volume production’ | The Verge 
 Projects & Open Source 
 (01:01:31) Qwen3-Coder-Next: Pushing Small Hybrid Models on Agentic Coding 
 (01:05:10) OpenClaw’s AI ‘skill’ extensions are a security nightmare | The Verge 
 Research & Advancements 
 (01:07:12) Learning to Reason in 13 Parameters 
 (01:12:33) Reinforcement World Model Learning for LLM-based Agents 
 (01:16:32) Opus 4.6 on Vending-Bench – Not Just a Helpful Assistant 
 Policy & Safety 
 (01:19:00) METR GPT-5.2 
 (01:23:31) The Hot Mess of AI: How Does Misalignment Scale with Model Intelligence and Task Complexity?
```

---

## 13. Last Week in AI #335 - Opus 4.6, Codex 5.3, Gemini 3 Deep Think, GLM 5, Seedance 2.0

- 日期: 2026-02-16 02:00
- 链接: https://lastweekin.ai/p/last-week-in-ai-335-opus-46-codex

```
Last Week in AI #335 - Opus 4.6, Codex 5.3, Gemini 3 Deep Think, GLM 5, Seedance 2.0
A crazy packed edition of Last Week in AI! Plus some small updates.
Editor’s note: I apologize for the inconsistent release date of the newsletter and podcasts in recent months. I’ll aim to start releasing on Saturday/Sunday consistently from now on! This edition of the newsletter covers a bit more than a week as a result.
I am also going to be adding an ‘Editor’s Take’ for Top News to add a bit commentary and extra cont…
```

---

## 14. LWiAI Podcast #233 - Moltbot, Genie 3, Qwen3-Max-Thinking

- 日期: 2026-02-06 05:06
- 链接: https://lastweekin.ai/p/lwiai-podcast-233-moltbot-genie-3

```
Our 233rd episode with a summary and discussion of last week’s big AI news! 
 Recorded on 01/30/2026 
 Hosted by Andrey Kurenkov and Jeremie Harris 
 Feel free to email us your questions and feedback at contact@lastweekinai.com and/or hello@gladstone.ai 
 In this episode: 
 Google introduces Gemini AI agent in Chrome for advanced browser functionality, including auto-browsing for pro and ultra subscribers. 
 OpenAI releases ChatGPT Translator and Prism, expanding its applications beyond core business to language translation and scientific research assistance. 
 Significant funding rounds and valuations achieved by startups Recursive and New Rofo, focusing on specialized AI chips and optical processors respectively. 
 Political and social issues, including violence in Minnesota, prompt tech leaders in AI like Ade from Anthropic and Jeff Dean from Google to express concerns about the current administration’s actions. 
 Timestamps: 
 (00:00:10) Intro / Banter 
 Tools & Apps 
 (00:04:09) Google adds Gemini AI-powered ‘auto browse’ to Chrome | The Verge 
 (00:07:11) Users flock to open source Moltbot for always-on AI, despite major risks - Ars Technica 
 (00:13:25) Google Brings Genie 3 ‘World Building’ Experiment to AI Ultra Subscribers - CNET 
 (00:16:17) OpenAI’s ChatGPT translator challenges Google Translate | The Verge 
 (00:18:27) OpenAI launches Prism, a new AI workspace for scientists | TechCrunch 
 Applications & Business 
 (00:19:49) Exclusive: China gives nod to ByteDance, Alibaba and Tencent to buy Nvidia’s H200 chips - sources | Reuters 
 (00:22:55) AI chip startup Ricursive hits $4B valuation 2 months after launch 
 (00:24:38) AI Startup Recursive in Funding Talks at $4 Billion Valuation - Bloomberg 
 (00:27:30) Flapping Airplanes and the promise of research-driven AI | TechCrunch 
 (00:31:54) From invisibility cloaks to AI chips: Neurophos raises $110M to build tiny optical processors for inferencing | TechCrunch 
 Projects & Open Source 
 (00:35:34) Qwen3-Max-Thinking debuts with focus on hard math, code 
 (00:38:26) China’s Moonshot releases a new open-source model Kimi K2.5 and a coding agent | TechCrunch 
 (00:46:00) Ai2 launches family of open-source AI developer agents that adapt to any codebase - SiliconANGLE 
 (00:47:46) Tiny startup Arcee AI built a 400B-parameter open source LLM from scratch to best Meta’s Llama 
 Research & Advancements 
 (00:52:53) Post-LayerNorm Is Back: Stable, ExpressivE, and Deep 
 (00:58:00) [2601.19897] Self-Distillation Enables Continual Learning 
 (01:03:04) [2601.20802] Reinforcement Learning via Self-Distillation 
 (01:05:58) Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability 
 Policy & Safety 
 (01:09:13) Amodei, Hoffman Join Tech Workers Decrying Minnesota Violence - Bloomberg
```

---

## 15. Last Week in AI #334 - Kimi K2.5 & Code, Genie 3, OpenClaw & Moltbook

- 日期: 2026-02-04 05:25
- 链接: https://lastweekin.ai/p/last-week-in-ai-334-kimi-k25-and

```
Last Week in AI #334 - Kimi K2.5 & Code, Genie 3, OpenClaw & Moltbook
China’s Moonshot releases a new open source model Kimi K2.5 and a coding agent, Google Brings Genie 3’s Interactive World-Building Prototype to AI Ultra Subscribers, and more!
China’s Moonshot releases a new open source model Kimi K2.5 and a coding agent
Moonshot AI unveiled Kimi K2.5, an open-source, natively multimodal model trained on 15 trillion mixed visual and text tokens that understands text, images, and video. The company emphasizes strong agentic capabilities, citing “agent swarm” orchestration where multiple agents …
```

---

## 16. LWiAI Podcast #232 - ChatGPT Ads, Thinking Machines Drama, STEM

- 日期: 2026-01-28 09:51
- 链接: https://lastweekin.ai/p/lwiai-podcast-232-chatgpt-ads-thinking

```
Our 232st episode with a summary and discussion of last week’s big AI news! 
 Recorded on 01/23/2026 
 Hosted by Andrey Kurenkov and Jeremie Harris 
 Feel free to email us your questions and feedback at contact@lastweekinai.com and/or hello@gladstone.ai 
 In this episode: 
 OpenAI announces testing of ads in ChatGPT and introduces child age prediction to enhance safety features, amidst ongoing ethical debates and funding expansions in AI integration with educational tools and business models. 
 China’s AI landscape sees significant progress with AI firm Jpu training advanced models on domestic hardware, and strong competitive moves by data centers, highlighting the intense demand in AI manufacturing and infrastructure. 
 Silicon Valley tensions rise as startup Thinking Machines experiences high-profile departures back to OpenAI, reflecting broader industry struggles and rapid shifts in organizational dynamics. 
 AI legislation and safety measures advance with the US Senate’s Defiance Act addressing explicit content, and Anthropic updating Claude’s constitution to guide ethical AI interactions, while cultural pushbacks from artists signal ongoing debates in intellectual property and AI-generated content. 
 Timestamps: 
 (00:00:10) Intro / Banter 
 (00:02:08) News Preview 
 (00:02:26) Response to listener comments 
 Tools & Apps 
 (00:11:55) OpenAI to test ads in ChatGPT as it burns through billions - Ars Technica 
 (00:18:05) OpenAI is launching age prediction for ChatGPT accounts 
 (00:23:37) Google now offers free SAT practice exams, powered by Gemini | TechCrunch 
 (00:24:57) Baidu’s AI Assistant Reaches Milestone of 200 Million Monthly Active Users - WSJ 
 Applications & Business 
 (00:26:53) The Drama at Thinking Machines, a New A.I. Start-Up, Is Riveting Silicon Valley - The New York Times 
 (00:31:44) Zhipu AI breaks US chip reliance with first major model trained on Huawei stack | South China Morning Post 
 (00:36:31) Elon Musk’s xAI launches world’s first Gigawatt AI supercluster to rival OpenAI and Anthropic 
 (00:41:25) Sequoia to invest in Anthropic, breaking VC taboo on backing rivals: FT 
 (00:45:18) Humans&, a ‘human-centric’ AI startup founded by Anthropic, xAI, Google alums, raised $480M seed round | TechCrunch 
 Projects & Open Source 
 (00:48:51) Black Forest Labs Releases FLUX.2 [klein]: Compact Flow Models for Interactive Visual Intelligence - MarkTechPost 
 (00:50:35) [2601.10611] Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding 
 (00:52:53) [2601.10547] HeartMuLa: A Family of Open Sourced Music Foundation Models 
 (00:54:46) [2601.11044] AgencyBench: Benchmarking the Frontiers of Autonomous Agents in 1M-Token Real-World Contexts 
 Research & Advancements 
 (00:57:05) STEM: Scaling Transformers with Embedding Modules 
 (01:06:22) Reasoning Models Generate Societies of Thought 
 (01:14:21) Why LLMs Aren’t Scientists Yet: Lessons from Four Autonomous Research Attempts 
 Policy & Safety 
 (01:19:41) Senate passes bill letting victims sue over Grok AI explicit images 
 (01:22:03) Building Production-Ready Probes For Gemini 
 (01:27:32) Anthropic Publishes Claude AI’s New Constitution | TIME 
 Synthetic Media & Art 
 (01:34:13) Artists Launch Stealing Isn’t Innovation Campaign To Protest Big Tech
```

---

## 17. Last Week in AI #333 - ChatGPT Ads, Zhipu+Huawei, Drama at Thinking Machines

- 日期: 2026-01-23 05:14
- 链接: https://lastweekin.ai/p/last-week-in-ai-333-chatgpt-ads-zhipuhuawei

```
Last Week in AI #333 - ChatGPT Ads, Zhipu+Huawei, Drama at Thinking Machines
OpenAI to test ads in ChatGPT as it burns through billions, Sequoia to invest in Anthropic, Zhipu AI breaks US chip reliance, The Drama at Thinking Machines Is Riveting Silicon Valley
OpenAI to test ads in ChatGPT as it burns through billions
Related:
OpenAI will begin testing labeled banner ads in ChatGPT for logged‑in users on the free tier and the $8/month ChatGPT Go plan, rolling out in the U.S. and other markets in the coming weeks. Ads will appear as blocked-off se…
```

---

## 18. LWiAI Podcast #231 - Claude Cowork, Anthropic $10B, Deep Delta Learning

- 日期: 2026-01-21 03:22
- 链接: https://lastweekin.ai/p/lwiai-podcast-231-claude-cowork-anthropic

```
Our 231st episode with a summary and discussion of last week’s big AI news! 
 Recorded on 01/16/2026 
 Hosted by Andrey Kurenkov and Jeremie Harris 
 Feel free to email us your questions and feedback at contact@lastweekinai.com and/or hello@gladstone.ai 
 In this episode: 
 Anthropic’s new cowork tool integrates Claude code, potentially simplifying multiple computing tasks from editing videos to compiling spreadsheets. 
 Significant funding rounds see Anthropic raising $10B at a valuation of $350B, while XAI raises $20B, underscoring the immense market interest in AI startups. 
 Nvidia faces supply challenges for H200 AI chips due to overwhelming demand from China, despite high costs per unit and its potential impact on U.S. company revenue. 
 Policy debates highlight tensions around U.S. export controls to China, with leaders like Justin Lin from Alibaba and Jake Sullivan, former national security advisor, weighing in on the ramifications for the AI industry’s future. 
 Timestamps: 
 (00:00:10) Intro / Banter 
 (00:01:30) News Preview 
 Tools & Apps 
 (00:02:13) Anthropic’s new Cowork tool offers Claude Code without the code | TechCrunch 
 (00:09:45) Google’s Gemini AI will use what it knows about you from Gmail, Search, and YouTube | The Verge 
 (00:12:45) Google removes some AI health summaries after investigation finds “dangerous” flaws - Ars Technica 
 (00:16:29) Gmail is getting a Gemini AI overhaul 
 (00:18:12) Slackbot is an AI agent now | TechCrunch 
 Applications & Business 
 (00:20:11) Anthropic Raising $10 Billion at $350 Billion Value 
 (00:22:25) Elon Musk xAI raises $20 billion from Nvidia, Cisco, investors 
 (00:24:47) NVIDIA Needs a Supply Chain ‘Miracle’ From TSMC as China’s H200 AI Chip Orders Overwhelm Supply, Triggering a Bottleneck 
 (00:29:26) OpenAI signs deal, worth $10B, for compute from Cerebras | TechCrunch 
 (00:31:49) CoreWeave in focus as it amends credit agreement 
 (00:34:30) LMArena lands $1.7B valuation four months after launching its product | TechCrunch 
 Projects & Open Source 
 (00:35:54) Nemotron-Cascade: Scaling Cascaded Reinforcement Learning for General-Purpose Reasoning Models 
 (00:43:15) mHC: Manifold-Constrained Hyper-Connections 
 (00:49:53) IQuest_Coder_Technical_Report 
 (00:54:58) TII Abu-Dhabi Released Falcon H1R-7B: A New Reasoning Model Outperforming Others in Math and Coding with only 7B Params with 256k Context Window - MarkTechPost 
 Research & Advancements 
 (01:01:42) Deep Delta Learning 
 (01:07:47) Recursive Language Models 
 (01:13:39) Conditional memory via scalable lookup 
 (01:18:54) Extending the Context of Pretrained LLMs by Dropping their Positional Embeddings 
 Policy & Safety 
 (01:26:06) Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks 
 (01:31:00) Nvidia CEO says purchase orders, not formal declaration, will signal Chinese approval of H200 
 (01:32:24) China AI Leaders Warn of Widening Gap With US After $1B IPO Week 
 (01:37:25) Jake Sullivan is furious that Trump removed Biden’s AI chip export controls | The Verge
```

---

## 19. Last Week in AI #332 - Apple + Gemini, OpenAI + Cerebras, Claude Cowork

- 日期: 2026-01-15 07:06
- 链接: https://lastweekin.ai/p/last-week-in-ai-332-apple-gemini

```
Last Week in AI #332 - Apple + Gemini, OpenAI + Cerebras, Claude Cowork
Google’s Gemini to power Apple’s AI features like Siri, OpenAI signs deal worth $10B for compute from Cerebras, and more!
Google’s Gemini to power Apple’s AI features like Siri
Apple announced a multi-year partnership to use Google’s Gemini models and Google Cloud to power AI features like Siri, after testing alternatives from OpenAI and Anthropic. According to both companies, Gemini provides “the most capable foundation” for Apple’s own models, with reporting suggesting Ap…
```

---

## 20. LWiAI Podcast #230 - 2025 Retrospective, Nvidia buys Groq, GLM 4.7, METR

- 日期: 2026-01-07 06:59
- 链接: https://lastweekin.ai/p/lwiai-podcast-230-2025-retrospective

```
Our 230th episode with a summary and discussion of last week’s big AI news! 
 Recorded on 01/02/2026 
 Hosted by Andrey Kurenkov and Jeremie Harris 
 Feel free to email us your questions and feedback at contact@lastweekinai.com and/or hello@gladstone.ai 
 In this episode: 
 Nvidia’s acquisition of AI chip startup Groq for $20 billion highlights a strategic move for enhanced inference technology in GPUs. 
 New York’s RAISE Act legislation aims to regulate AI safety, marking the second major AI safety bill in the US. 
 The launch of GLM 4.7 by Zhipu AI marks a significant advancement in open-source AI models for coding. 
 Evaluation of long-horizon AI agents raises concerns about the rising costs and efficiency of AI in performing extended tasks. 
 Timestamps: 
 (00:00:10) Intro / Banter 
 (00:01:58) 2025 Retrospective 
 Tools & Apps 
 (00:24:39) OpenAI bets big on audio as Silicon Valley declares war on screens | TechCrunch 
 Applications & Business 
 (00:26:39) Nvidia buying AI chip startup Groq for about $20 billion, biggest deal 
 (00:34:28) Exclusive | Meta Buys AI Startup Manus, Adding Millions of Paying Users - WSJ 
 (00:38:05) Cursor continues acquisition spree with Graphite deal | TechCrunch 
 (00:39:15) Micron Hikes CapEx to $20B with 2026 HBM Supply Fully Booked; HBM4 Ramps 2Q26 
 (00:42:06) Chinese fabs are reportedly upgrading older ASML DUV lithography chipmaking machines — secondary channels and independent engineers used to soup up Twinscan NXT series 
 Projects & Open Source 
 (00:47:52) Z.AI launches GLM-4.7, new SOTA open-source model for coding 
 (00:50:11) Evaluating AI’s ability to perform scientific research tasks 
 Research & Advancements 
 (00:54:32) Large Causal Models from Large Language Models 
 (00:57:33) Universally Converging Representations of Matter Across Scientific Foundation Models 
 (01:02:11) META-RL INDUCES EXPLORATION IN LANGUAGE AGENTS 
 (01:07:16) Are the Costs of AI Agents Also Rising Exponentially? 
 (01:11:17) METR eval for Opus 4.5 
 (01:16:19) How to game the METR plot 
 Policy & Safety 
 (01:17:24) New York governor Kathy Hochul signs RAISE Act to regulate AI safety | TechCrunch 
 (01:20:40) Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers 
 (01:26:46) Monitoring Monitorability 
 (01:32:07) Sam Altman is hiring someone to worry about the dangers of AI | The Verge 
 (01:33:38) X users asking Grok to put this girl in bikini, Grok is happy obliging - India Today
```

---
