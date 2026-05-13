# Hugging Face

> 分类: AI专题
> URL: https://wechat2rss.bestblogs.dev/feed/8b68fdb4f24ab2287100988a8cec36363fec4214.xml
> 抓取: 10 篇

---

## 1. 社区发布丨全面开源！商汤日日新SenseNova U1发布，迈向模型理解生成统一时代

- 日期: 2026-04-29 11:02
- 链接: https://mp.weixin.qq.com/s?__biz=Mzk0MDQyNTY4Mw==&mid=2247496716&idx=1&sn=6687271ae521f89cb80abedbdac87569

```
商汤科技 2026-04-29 11:02 法国 
 SenseNova U1：商汤日日新系列原生理解生成统一模型开源 
 今天，我们正式发布并开源商汤日日新 SenseNova U1 系列 原生理解生成统一模型。 
 它基于商汤于今年三月份自主研发的 NEO-unify架构 ，在单一模型架构上统一了多模态理解、推理与生成。 
 NEO-unify架构 彻底摒弃了主流的拼接式，去除了视觉编码器（VE）和变分自编码器（VAE），重新构建了统一的表征空间，并且深入融入每一层计算中，从而实现 从模态集成向原生统一的范式跨越 。 
 SenseNova U1系列模型能够将语言与视觉信息作为统一的复合体直接建模， 实现语言和视觉信息的高效协同，让理解与生成能力同步增强 ， 在保留语义丰富度的同时，维持像素级的视觉保真度。 
 在 逻辑推理与空间智能 等方向上，它能够深度理解物理世界的复杂布局与精细关系；在未来，它还能为 机器人 提供具身大脑，实现在单一模型闭环内完成从复杂环境感知、逻辑推演到精准任务执行的全过程，为推动技术与产业发展提供重要基础与关键引擎。 
 本次开源发布的是 SenseNova U1 的轻量版系列 SenseNova U1 Lite。它包含两个不同规格的模型： 
 SenseNova-U1-8B-MoT ：基于稠密骨干网络 
 SenseNova-U1-A3B-MoT ：基于混合专家（MoE） 骨干网络 
 了解更多信息， 访问 GitHub 
 https://github.com/OpenSenseNova/SenseNova-U1 
 Hugging Face 
 https://huggingface.co/collections/sensenova/sensenova-u1 
 我们也将在近期公布详实的技术报告 。 
 极致高效，以小搏大： 
 开源SOTA，比肩商用 
 效率，是统一模型架构的核心技术优势。 
 传统多模态模型是把视觉编码器和语言骨干通过适配器拼接在一起的。它像一个“说不同语言的人组成的工作组”：有人专门看图，把图像翻译为语言，有人专门理解文字，进行推理，有人把结果再翻译为设计指令，把图画出来。每完成一次任务，信息都要在不同成员之间来回传递。这个过程虽然可行，但难免会有等待、误解和信息损耗。为了弥补这些损耗，模型往往需要做得更大才能达到好的效果。 
 SenseNova U1 是基于统一表征空间构建的，更像是一个从一开始就同时掌握多项技能的人。它不是先看懂图像、再翻译成文字、再交给另一个系统理解，而是在同一套“思考方式”里直接处理图像、文字等不同信息。图像和语言不再是两套系统之间的接力，而是在同一个大脑中自然融合。 
 这样带来的好处是： 信息流转更快捷，理解更直接，生成更高效。 模型不需要依赖单纯堆大参数来弥补中间转换的损耗， 而是通过统一的内部表征，把不同模态的信息以更紧凑、更高密度的方式组织起来 。 
 简单来说，传统架构像是“多人协作、层层转述”；SenseNova U1 更像是“一个全能大脑，直接理解，直接表达”。少了中间转译，信息损耗更低，也能在相对更精简的模型规模下，实现更强的多模态理解与生成能力。 
 实验结果验证了我们的想法。在涵盖图像理解、图像生成与编辑、空间智能和视觉推理的多项基准测试中 ，SenseNova U1 Lite均达到同量级开源模型SOTA水平 ，为统一多模态理解与生成树立了新的标杆。甚至 仅凭8B-MoT的较小规格 ， 就能达到甚至超越部分大型商业闭源模型 ，展现出全维度多领域的统治力。 点击可查看单图↓ 
 图像理解基准 
 测试结果 
 图像生成基准 
 测试结果 
 视觉推理基准 
 测试结果 
 以下两组对比图更直观地展现了 SenseNova U1 Lite 在效率上的突出优势。在通用的图像生成测试中（上图），SenseNova U1 Lite不但在 图像生成质量上比肩 Qwen-Image 2.0 Pro或 Seedream 4.5 等大型闭源模型 ，达到商业级水准，还在 推理响应速度上有显著优势 。 即使在极具挑战性、开源模型一直做不好的复杂信息图生成任务中（下图），SenseNova U1 Lite 也表现出商业级的水准，对复杂信息图的排版和文字有很强的控制力。 
 Generation Latency vs. Averaging Performance on OneIG (EN, ZH), LongText (EN, ZH), BizGenEval (Easy, Hard), CVTG and IGenBenc 
 Generation Latency vs. Averaging Performance on Infographic Benchmarks, i.e., BizGenEval (Easy, Hard), and IGenBench 
 我们正在沿着当前的技术路径继续 Scale，计划在未来推出体量更大的模型。我们相信，基于高效的原生架构，可以以低得多的计算成本达到国际顶尖模型的水平。 
 业内首创： 
 连续性图文创作输出 
 凭借NEO-unify架构的优势， SenseNova U1在业内首个实现连续性的图文创作输出 。并且只需要单次单模型调用，就能输出更高质量的作品，相比传统范式，实现了效率的大幅提升。 
 SenseNova U1 所具备的原生图文理解生成能力，能天然将图像和文本底层融合信号完整的保留上下文中，区别于过去只能利用多模型串联勉强实现，它的图像间风格具备明显的高一致性，能在统一表征空间进行高效连贯思考。 
 下面两个案例中，SenseNova U1 通过连贯高保真度的图文交错思考输出。 
 任务一：五分熟牛排做法：SenseNova U1 可以通过思考和规划产生分步的过程，并且给每一步输出对应的图像展示。各个步骤的图示表现出极高的一致性。 
 上下滑动查看更多，点击可查看原图 
 任务二：绘制一个钢铁侠图案。它可以从扫描草稿出发，逐步进行连续创作，最终做出一个完成度很高的图像。每一步创作的过程对于前一步的结构和细节都做了精准的保持 —— 一个统一表征的共享上下文在其中发挥了关键作用。 
 上下滑动查看更多，点击可查看原图 
 全网开源，即刻可用 
 开源部署 
 GitHub ： 
 https://github.com/OpenSenseNova/SenseNova-U1 
 Hugging Face ： 
 https://huggingface.co/collections/sensenova/sensenova-u1 
 欢迎调用 SenseNova U1 Skill 
 https://github.com/OpenSenseNova/SenseNova-Skills 
 浏览海量样例库，获取Prompt编写指南，化繁为简（繁杂文->有趣图），让您的Agent成为信息图生成高手 
 在线体验与接入 
 即将上线 办公小浣熊 
 我们相信，原生统一的多模态智能是通往 AGI 的必经之路。未来，我们还将持续推动开源生态建设，并发布更大参数规模的 U1 系列模型。迎社区广大用户和开发者提出宝贵建议，共同定义智能交互的未来。 
 本文由 Hugging Face 中文社区内容共建项目提供，稿件由社区成员投稿，经授权发布于 Hugging Face 公众号。文章内容不代表官方立场，文中介绍的产品和服务等均不构成投资建 议。了解更多请 关注公众号 
 如果你有与开源 AI、Hugging Face 相关的技术和实践分享内容，以及最新的开源 AI 项目发布，希望通过我们分享给更多 AI 从业者和开发者们，请通过下面的链接投稿与我们取得联系: https://hf.link/to ugao 
 跳转微信打开
```

---

## 2. 社区供稿丨无需编解码器，NEO-unify如何打造原生视觉语言理解与生成

- 日期: 2026-04-03 11:05
- 链接: https://mp.weixin.qq.com/s?__biz=Mzk0MDQyNTY4Mw==&mid=2247496707&idx=1&sn=f6709484e7fb6808079243d4a5687892

```
商汤科技 2026-04-03 11:05 法国 
 无需编解码器，NEO-unify如何打造原生视觉语言理解与生成 
 今天，商汤科技发布一篇最新技术博客 NEO-unify: 原生架构打造端到端多模态理解与生成统一模型（NEO-unify: Building Native Multimodal Unified Models End to End） 
 这篇博客深入解读 NEO-unify ： 一项旨在从底层统一多模态理解与生成的端到端原生架构。 
 当前，多模态模型普遍采用“视觉编码器（VE）用于理解，变分自编码器（VAE）用于生成”的组合式设计。这套范式虽行之有效，却也内在割裂了感知与创造，常面临模块协同与效率权衡的挑战。 
 我们能否更进一步，让AI像人一样，直接从最原始的像素和文字中，统一地进行学习、理解与生成？这正是 NEO-unify 尝试回答的根本问题。它摒弃了传统的VE与VAE，首次构建了一个真正的端到端原生统一模型，在同一个架构内直接处理像素与文本，并在此基础上协同完成理解与生成任务。初步研究成果令人振奋， 该设计在保持强大语义理解与细节恢复能力的同时，显著提升了训练与计算效率。 
 这项技术将如何为生成式AI打开新的想象？让我们一同展开探讨。 
 《NEO-unify ：原生架构打造端到端多模态理解与生成统一模型 》 
 英文博客地址： 
 https://huggingface.co/blog/sensenova/neo-unify 
 中文博客地址： 
 https://www.sensetime.com/cn/news-detail/51170543?categoryId=72 
 当前多模态智能架构困境 
 长期以来，多模态研究已形成一种默认范式：视觉编码器（Vision Encoder, VE） 负责感知与理解，而变分自编码器（Variational Autoencoder, VAE） 则用于内容生成。近期的一些工作尝试构建共享编码器，但这种折衷往往引入新的结构性设计权衡。 
 由此回到 第一性原理：构建一体化模型直接处理原生输入，即像素本身与文字本身。商汤科技联合南洋理工大学 ，提出一种全新的架构范式： NEO-unify（preview ），一个原生、统一、端到端的多模态模型架构。它不仅越过了当前视觉表征的争论，也摆脱了预训练先验和规模定律瓶颈的限制。最关键的是： 不需要 VE，也不需要 VAE 。 
 我们正扩大规模、持续迭代。更多模型与开源成果，将很快与大家见面。 
 NEO-unify原生一体化架构新范式 
 NEO-unify 第一次迈向真正的端到端统一框架 ，能够直接从近乎无损的信息输入中学习，并由模型自身塑造内部表征空间。首先，引入 近似无损的视觉接口 ，用于统一图像的输入与输出表示；其次，采用 原生混合Transformer （Mixture-of-Transformer，MoT）架构，使理解与生成能够在同一体系中协同进行；最终，通过 统一学习框架实现跨模态训练 ：文本采用自回归交叉熵目标，视觉通过像素流匹配进行优化。 
 模型效果 
 1. 定量结果分析 
 2. 生图效果展示 
 技术发现 
 1. 无编码器设计能够同时保留抽象语义与细粒度表征 
 [图像重建任务] 
 我们先前的工作 NEO （Diao et al., ICLR 2026）表明，原生端到端模型同样能够学习到丰富的语义表征。在此基础上，我们进一步观察到一个有趣的现象：即使在 冻结理解分支 的情况下，独立的生成分支仍然能够从表示中抽取并恢复 细粒度的视觉细节 。 
 基于这一发现，我们训练了 NEO-unify（2B） 。在 初步 9 万步预训练 后，模型在 MS COCO 2017 上取得 31.56 PSNR 和 0.85 SSIM ，而 Flux VAE 的对应指标为 32.65 和 0.91 。这一结果表明，即使不依赖预训练 VE 或 VAE ， 近似无损的原生输入 仍能够同时支持高质量的语义理解与像素级细节保真。 
 域外图像重建（2B NEO-unify，理解分支冻结） 
 [图像编辑任务] 
 据此，我们进一步开展探索： NEO-unify 将所有全模态条件信息统一输入到理解分支，而生成分支仅负责生成新的图像。 
 即使在 冻结理解分支 的情况下， NEO-unify（2B） 仍展现出强大的图像编辑能力，同时显著减少了输入图像令牌的数量。在使用开源生成与图像编辑数据集并进行 初步 6 万步混合训练 后，模型在 ImgEdit 基准上取得 3.32 的成绩，且理解分支在整个训练过程中 保持冻结 。 
 小规模数据验证（2B NEO-unify，理解分支冻结） 
 ImgEdit提示词编辑（2B NEO-unify，理解分支冻结） 
 2. 无编码器架构与 MoT 主干高度协同大幅降低内在冲突 
 借助预训练的理解分支与生成分支， NEO-unify 使用相同的中期训练（MT）与 监督微调（SFT） 数据进行联合训练。 即使在较低的数据比例和损失权重下，理解能力依然保持稳定，而生成能力则收敛很快。二者在 MoT 主干中协同提升，整体冲突极小。 
 3. 无编码器架构，展现更高数据训练效率 
 此外，我们首先进行 web-scale 预训练，随后在多样且高质量的数据语料上依次进行中期训练（MT） 和 监督微调（SFT）。 与 Bagel 模型相比，NEO-unify 展现出更高的数据训练效率，在使用更少训练 token 的情况下取得了更优的性能。 
 未来展望 
 这不仅仅是一种模型架构探索，更是迈向下一代智能形态的一步： 
 • 感知与生成交织的闭环 
 • 全模态推理 
 • 视觉推理 
 • 空间智能 
 • 世界模型 
 • … 
 一条新的路线图正在展开：模型不再在模态之间进行转换，而是能够 原生地跨模态思考 。多模态 AI 不再只是连接不同系统，而是构建一个 从未割裂的统一智能体 ，并让所需能力从其内部自然涌现。 
 本文由 Hugging Face 中文社区内容共建项目提供，稿件由社区成员投稿，经授权发布于 Hugging Face 公众号。文章内容不代表官方立场，文中介绍的产品和服务等均不构成投资建 议。了解更多请 关注公众号 
 如果你有与开源 AI、Hugging Face 相关的技术和实践分享内容，以及最新的开源 AI 项目发布，希望通过我们分享给更多 AI 从业者和开发者们，请通过下面的链接投稿与我们取得联系: https://hf.link/to ugao 
 跳转微信打开
```

---

## 3. Transformer 中的专家混合模型 (MoE)

- 日期: 2026-03-27 08:50
- 链接: https://mp.weixin.qq.com/s?__biz=Mzk0MDQyNTY4Mw==&mid=2247496705&idx=1&sn=3fcff1f411c916fbf1434d045d155423

```
原创 Hugging Face 2026-03-27 08:50 美国 
 引言 
 在过去几年里，大规模稠密语言模型的扩展推动了大语言模型 (LLMs) 的主要进展。从早期的模型，比如最初的 ULMFiT (约 3000 万参数) 或 GPT-2 (15 亿参数，当时甚至被认为“过于危险而不宜发布” 🧌) ，再到如今拥有数千亿参数的系统，其核心思路一直很简单： 
 ULMFiT https://nlp.fast.ai/classification/2018/05/15/introducing-ulmfit.html 
 数据越多 + 参数越多 = 性能越好 
 缩放定律 (Scaling laws) 进一步强化了这一趋势，但稠密模型的扩展也存在现实瓶颈： 
 缩放定律 (Scaling laws) https://hf.co/papers/2001.08361 
 训练成本越来越高 
 推理延迟不断增加 
 部署需要大量内存和硬件资源 
 这正是专家混合模型 (MoE) 发挥作用的地方。 
 如果你已经了解 MoE，想直接看在 transformers 中的工程实现，可以直接跳到 。 
 从稠密到稀疏：什么是 MoE？ 
 MoE 模型保留了 Transformer 的主体结构，但会将部分稠密的前馈层替换为一组 专家(experts) 。这里的“专家”并不是指某种特定领域 (比如“数学专家”或“代码专家”) ，而只是一个可学习的子网络。对于每个 token，会由一个 路由器(router) 选择少数几个专家来处理。 
 图 1：在 4 个专家中激活了专家 1 (来源： Maarten Grootendorst ) 
 MoE routing diagram https://hf.co/datasets/huggingface/documentation-images/resolve/main/blog/moe-transformers/moe_routing.png 
 Maarten Grootendorst https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts 
 不同的 token 会根据其隐藏表示激活不同的专家。 
 模型容量取决于总参数量，而推理速度取决于实际参与计算的参数量。 
 这是核心思想。 
 例如 gpt-oss-20b ：它总共有 210 亿参数，但每个 token 只会激活 32 个专家中的 4 个。加上共享部分后，每个 token 实际使用大约 36 亿参数。在一台内存带宽约 800GB 的 M3 Ultra Mac 上，可以粗略估算生成速度为： 
 gpt-oss-20b https://hf.co/openai/gpt-oss-20b 
 800 / (3.6 × 2) (bfloat16，每个参数 2 字节) 
 结果约为 111 tokens/s ，而实际测得约为 115 tokens/s ，与估算非常接近。 
 这说明模型在运行时的计算量类似一个 36 亿参数模型，但性能却接近 210 亿参数模型。 
 (注：如果使用该模型原生的 mxfp4 量化内核，速度还会更快。) 
 MoE 的优势主要体现在： 
 更高的计算效率 
 在相同的训练 FLOPs 预算下，MoE 通常优于稠密模型。 
 图 2：稠密模型 vs MoE 的训练曲线 (来源： OLMoE ) 
 MoE vs Dense training graphs https://hf.co/datasets/huggingface/documentation-images/resolve/main/blog/moe-transformers/faster_training.png 
 OLMoE https://hf.co/papers/2409.02060 
 这意味着更快的迭代速度和更高的扩展效率。 
 天然适合并行计算 
 专家本身构成了计算图中的结构边界。由于不同 token 会使用不同专家，可以在专家维度上进行并行 (后文会介绍) 。 
 行业广泛采用 
 最近几周发布的 MoE 开源模型包括 Qwen 3.5 、 MiniMax M2 、 GLM-5 、 Kimi K2.5 。 
 Qwen 3.5 https://hf.co/collections/Qwen/qwen35 
 MiniMax M2 https://hf.co/collections/MiniMaxAI/minimax-m2 
 GLM-5 https://hf.co/collections/zai-org/glm-5 
 Kimi K2.5 https://hf.co/collections/moonshotai/kimi-k25 
 这一趋势在 2025 年 1 月 DeepSeek R1 发布后明显加速，其基础来自更早的 DeepSeek V2 。更早的代表还有 2023 年 12 月发布的 Mixtral-8x7B 。 
 DeepSeek R1 https://hf.co/deepseek-ai/DeepSeek-R1 
 DeepSeek V2 https://hf.co/deepseek-ai/DeepSeek-V2 
 Mixtral-8x7B https://hf.co/mistralai/Mixtral-8x7B-v0.1 
 图 3：两年内 transformers 中 MoE 模型的增长趋势，DeepSeek R1 是一个重要拐点 
 timeline https://hf.co/datasets/huggingface/documentation-images/resolve/main/blog/moe-transformers/moe_2y_timeline.png 
 闭源模型同样在使用 MoE。ChatGPT 长期被 猜测 采用稀疏架构，而开源的 gpt-oss 系列则明确采用了这种方式。 
 猜测 https://x.com/soumithchintala/status/1671267150101721090 
 gpt-oss https://hf.co/collections/openai/gpt-oss 
 如果你想更深入了解 MoE，建议阅读 这篇博客 并观看我们最近发布的 关于路由机制的 YouTube 视频。 。 
 这篇博客 https://hf.co/blog/moe 
 关于路由机制的 YouTube 视频。 https://youtu.be/CDnkFbW-uEQ 
 Transformers 与 MoE 
 当前生态中的大多数工具 (如模型加载、设备分配、量化和执行后端) 最初都是为 稠密 模型设计的，而 MoE 对这些假设提出了挑战。 
 要让 MoE 在 transformers 中成为 一等公民(first-class citizens) ，意味着不仅仅是添加新的模型类，还需要对模型加载流程、执行机制以及分布式抽象进行重新设计。接下来我们将重点介绍 transformers 库是如何逐步演进，以支持稀疏架构的： 
 [权重加载重构] 
 [专家执行后端] 
 [专家并行] 
 [使用 transformers 训练 MoE] 
 权重加载重构 
 AutoModelForCausalLM.from_pretrained("model_id") 会下载并将模型权重加载到 PyTorch 模型中。对于稠密模型来说，这个过程相对直接：checkpoint 中的每个张量，通常都能一一对应到运行时模块中的某个参数。 
 AutoModelForCausalLM.from_pretrained("model_id") https://hf.co/docs/transformers/main/en/model_doc/auto #transformers .AutoModelForCausalLM.from_pretrained 
 但对于 MoE，情况会更复杂。在大多数 MoE 的 checkpoint 中，每个专家都是单独序列化保存的。如果你查看 DeepSeek-V3 的 checkpoint 索引 ，会看到类似这样的键： 
 DeepSeek-V3 的 checkpoint 索引 https://hf.co/deepseek-ai/DeepSeek-V3/raw/main/model.safetensors.index.json 
 model.layers.3.mlp.experts.0.gate_proj.weight 
 ... 
 model.layers.3.mlp.experts.255.gate_proj.weight 每个专家都有自己的一组权重矩阵。本质上来说，以 DeepSeek-V3 为例，就是把 256 个 (编号从 0 到 255) 小型前馈网络并排保存下来。 但在运行时，GPU 执行的是优化过的内核。现代 MoE 内核，比如 grouped GEMM 和融合式 MoE 实现 ，都被设计成通过 一次操作同时处理所有专家 ，而不是逐个专家循环执行。 
 grouped GEMM 和融合式 MoE 实现 https://hf.co/kernels-community/megablocks 
 为了高效做到这一点，就需要把所有专家的权重打包成一个连续张量 (contiguous tensor) 。 
 这就产生了不匹配： 
 Checkpoint： 256 个独立张量 
 运行时： 1 个打包后的张量 
 weight loading refactor 的作用，就是用一种系统化的方式来弥合这种差距。 
 weight loading refactor https://github.com/huggingface/transformers/pull/41580 
 通过引入通用的 WeightConverter ，思路从： 
 WeightConverter https://hf.co/docs/transformers/main/en/weightconverter 
 checkpoint 已经匹配运行结构，只需逐键复制 
 转变为： 
 checkpoint 只是张量的序列化来源。加载本质上是一个 转换流水线 ，它会把这些张量转换成我们需要的运行时布局。 
 使用 WeightConverter 进行动态加载 
 这次重构引入的核心抽象，是通过 WeightConverter 实现的 动态权重加载(dynamic weight loading) 。 
 WeightConverter https://hf.co/docs/transformers/main/en/internal/weight_converter 
 WeightConverter 允许我们定义如下映射关系： 
 source key patterns → target key(s) + operations 基础操作 (如切分、拼接等) 可以灵活组合。其中，有两个操作在 MoE 场景中特别常用： 
 MergeModulelist https://github.com/huggingface/transformers/blob/main/src/transformers/core_model_loading.py ：用于将一组张量合并为一个张量。例如，可以将 MergeModulelist 和 Concatenate 组合使用，把 MoE 中多个专家的权重堆叠起来，并打包成一个统一的张量。 
 WeightConverter( 
 [ "block_sparse_moe.experts.*.w1.weight" , "block_sparse_moe.experts.*.w3.weight" ], 
 "mlp.experts.gate_up_proj" , 
 operations=[ 
 MergeModulelist(dim= 0 ), 
 Concatenate(dim= 1 ), 
 ], 
 ) SplitModulelist https://github.com/huggingface/transformers/blob/b71de73468429eb02da18caa50e9b5200400a4ed/src/transformers/core_model_loading.py #L208 ：用于将一个张量拆分回一组张量。例如，可以把已经堆叠在一起的专家权重重新拆分成各个独立的专家。 
 WeightConverter( 
 "mlp.experts.down_proj" , 
 "block_sparse_moe.experts.*.w2.weight" , 
 operations=[SplitModulelist(dim= 0 )], 
 ) 张量的延迟实例化 
 这次重构不仅改进了“可以做 哪些 转换”，还优化了“这些转换 如何 被调度执行”。 
 加载器会先扫描一次 checkpoint 的所有 key，并将其与转换规则进行匹配，然后按每个 converter 对张量进行分组。一旦某个 key 被确定需要使用，就会被注册为一个 “ future ”，并通过线程池进行实际加载。只有当所需依赖全部准备就绪后，对应的转换操作才会执行。例如， MergeModulelist 必须等某一层的所有专家权重都加载完成后，才会开始合并。 
 这样可以减少重复扫描和内存峰值。 
 基准测试：权重加载流程的改进 
 为了评估新的权重加载流程带来的提升，我们对 transformers 的 v4 和 v5 版本进行了基准测试。重点关注的是大型 MoE 模型的加载速度，因为这通常是训练和推理中的一个瓶颈。 
 测试所用代码分支如下： 
 v4 分支： https://github.com/ariG23498/transformers/tree/bench-v4 
 v5 分支： https://github.com/ariG23498/transformers/tree/bench-v5 
 https://github.com/ariG23498/transformers/tree/bench-v4 https://github.com/ariG23498/transformers/tree/bench-v4 
 https://github.com/ariG23498/transformers/tree/bench-v5 https://github.com/ariG23498/transformers/tree/bench-v5 
 示例代码： 
 from transformers import AutoModelForCausalLM 
 model_id = "Qwen/Qwen1.5-110B-Chat" 
 model = AutoModelForCausalLM.from_pretrained(model_id) 两个相关的环境变量： 
 HF_ENABLE_PARALLEL_LOADING ：启用基于线程的分片并行加载 
 HF_DEACTIVATE_ASYNC_LOAD ：关闭新的异步加载流程 (v5 的回退选项) 
 测试结果 
 模型： Qwen/Qwen1.5-110B-Chat GPU： 1× A100 (80GB) 
 版本 
 策略 
 加载方式 
 时间 
 v4.57.6 
 auto 
 线程池 
 66.24s 
 v4.57.6 
 auto 
 顺序 
 67.29s 
 v4.57.6 
 TP 
 — 
 OOM 
 v5 
 auto 
 异步 (默认) 
 20.71s 
 v5 
 auto 
 同步 
 45.3s 
 v5 
 TP 
 异步 
 10.1s 
 v5 
 TP 
 同步 
 19.28s 
 图 4：加载性能对比(v4 vs v5) 
 benchmark https://hf.co/datasets/huggingface/documentation-images/resolve/main/blog/moe-transformers/loading_benchmark.png 
 这种加速并不仅仅来自“增加线程数量”。 
 而是由 单次扫描路由(Single-pass routing) 、 异步实例化(Async materialization) 和 感知转换的调度 (Conversion-aware scheduling) 共同作用的结果。这些机制一起避免了不必要的中间张量创建和内存峰值，同时还能在加载阶段完成专家打包和投影融合。 
 量化在其中的作用 
 通过这次重构，我们现在可以先构建好运行时的模型结构，然后再将权重转换并填充到这个结构中。同时，也可以选择在这个转换流程中加入量化步骤，使量化成为权重加载流程的一部分。 这一点非常关键，因为只有当专家已经以统一且可预测的打包结构存在时，“按专家进行量化”才有实际意义。 
 这种端到端的处理流程在此前是无法实现的，而现在已经作为一个对用户开放的 API 提供出来。 
 专家执行后端 
 当专家权重被打包后，接下来问题是： 
 如何高效地执行专家路由？ 
 在专家混合 (MoE) 模型中，每个 token 会被路由到不同的专家。这意味着在运行时需要完成一系列操作：将 token 分发到对应的专家权重、以高效方式执行投影计算、应用路由权重，然后再对结果进行汇总和重排。 
 这些问题正是 Experts Backend system (在 PR #42697 中引入) 要解决的。该系统提供了一种 可插拔的执行架构 ，将专家计算与具体模型实现解耦。也就是说，不再需要在每个 MoE 模型中写死某一种调度策略，而是可以在运行时为专家层动态选择合适的后端实现。 
 Experts Backend system https://hf.co/docs/transformers/experts_interface 
 PR #42697 https://github.com/huggingface/transformers/pull/42697 
 这一机制是通过装饰器模式实现的： 
 @use_experts_implementation 该装饰器会对专家类进行封装，并自动将计算分发到所选择的后端执行。 
 目前提供了三种后端实现： 
 eager 逐个遍历被选中的专家，并分别执行投影计算。主要用于结果验证和调试。 
 batched_mm 基于 torch.bmm 实现。它会为每个 token 复制对应专家的权重，然后通过一次批量矩阵乘法 (batched GEMM) 完成计算。适用于 batch 较小、GPU 计算能力强且显存充足的场景。 
 torch.bmm https://docs.pytorch.org/docs/stable/generated/torch.bmm.html 
 grouped_mm 基于 torch._grouped_mm 实现。它会先按照专家 ID 对 token 进行排序和分组，然后通过一次 grouped GEMM 完成计算。这种方式在大 batch 或显存受限的情况下表现更好。 
 torch._grouped_mm https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.grouped_mm.html 
 图：专家后端示意 
 专家并行 
 专家混合 (MoE) 模型的参数规模可以达到数千亿级别 (远远超出单张 GPU 的承载能力) 。专家并行 (Expert Parallelism，EP) 通过将专家分布到多个设备上来解决这一问题。每个设备只加载分配给自己的那部分专家，负责对应的计算，并在最后参与结果的汇总。 
 由于每个 token 实际只会激活少数几个专家，这种方式可以在不增加计算成本的前提下，将模型扩展到更大的参数规模。 
 专家并行可以通过 enable_expert_parallel 来启用： 
 import torch 
 from transformers import AutoModelForCausalLM, AutoTokenizer 
 from transformers.distributed.configuration_utils import DistributedConfig 
 distributed_config = DistributedConfig(enable_expert_parallel= True ) 
 model = AutoModelForCausalLM.from_pretrained( 
 "openai/gpt-oss-120b" , 
 dtype= "auto" , 
 distributed_config=distributed_config, 
 ) 启动： 
 torchrun --nproc-per-node N script.py 其中 N 应能整除专家数量，通常也对应 GPU 数量。 
 当 enable_expert_parallel=True 时，模型会从标准的张量并行 (Tensor Parallel, TP) 策略切换为专家并行 (Expert Parallel, EP) 策略，并采用专门的切分 (sharding) 方式。 
 EP 的核心组件包括： 
 GroupedGemmParallel https://github.com/huggingface/transformers/blob/b71de73468429eb02da18caa50e9b5200400a4ed/src/transformers/integrations/tensor_parallel.py #L934 沿着专家维度 ( dim=0 ) 对权重进行切分，使每个设备只加载 num_experts / num_devices 的专家权重。 
 RouterParallel https://github.com/huggingface/transformers/blob/b71de73468429eb02da18caa50e9b5200400a4ed/src/transformers/integrations/tensor_parallel.py #L977 将全局专家索引映射为本地索引，屏蔽不属于当前设备的专家，确保每个设备只使用本地专家进行计算，并通过 all-reduce 在设备之间汇总部分计算结果。 
 使用 Transformers 训练 MoE 
 MoE 在推理扩展方面表现出色，但在训练阶段要复杂得多。 
 主要挑战包括：参数规模极其庞大、专家之间的分布式通信复杂，以及需要处理路由过程中的不稳定性。为了解决这些问题，我们与 Unsloth 合作，实现了更高效的 MoE 训练方案： 
 训练速度提升约 12 倍 
 显存占用降低超过 35% 
 支持约 6 倍更长的上下文 
 相比 v4，总体加速达到 12–30 倍 
 在实现上，我们利用了 Expert Backend 抽象，统一采用 PyTorch 的 torch._grouped_mm API，并结合自定义的 Triton grouped-GEMM 和 LoRA 内核。Unsloth 在 Transformers (以及 TRL) 的优化基础上进一步提升了整体性能。 
 详情可参考： Unsloth 官方指南 
 Unsloth 官方指南 https://unsloth.ai/docs/new/faster-moe 
 总结 
 随着稀疏架构的不断发展，我们也希望 transformers 库能够持续演进，与之保持同步。如果你正在使用 MoE，或尝试新的稀疏模型思路，我们非常欢迎你的反馈。欢迎告诉我们你希望在 transformers 中看到哪些新的抽象、算子 (kernel) 或工作流程。 
 英文原文: https://huggingface.co/blog/moe-transformers 
 原文作者: Aritra Roy Gosthipaty, Pedro Cuenca, merve, Ilyas Moutawwakil, Arthur Zucker, Sergio Paniego, Pablo Montalvo 
 译者: Luke, Hugging Face Fellow 
 阅读原文 
 跳转微信打开
```

---

## 4. 在 Hugging Face Hub 上引入 Storage Buckets

- 日期: 2026-03-21 10:05
- 链接: https://mp.weixin.qq.com/s?__biz=Mzk0MDQyNTY4Mw==&mid=2247496668&idx=1&sn=471bdd6ff36ca38275b7a237be057501

```
原创 Hugging Face 2026-03-21 10:05 美国 
 Hugging Face 的 Models 和 Datasets 仓库非常适合用来发布最终产物。但在生产级机器学习流程中，会持续产生大量中间文件 (如 checkpoints、optimizer states、处理后的数据分片、日志、trace 等) 。这些文件变化频繁，可能同时来自多个任务，而且通常并不需要进行版本控制。 
 Storage Buckets 正是为这种场景设计的：一种类似 S3 的可变对象存储。你可以在 Hub 上浏览它，用 Python 脚本操作，或通过 hf CLI 管理。由于它们基于 Xet 构建，对于在不同文件之间共享大量内容的机器学习产物来说，存储和传输都会更加高效。 
 Xet https://hf.co/docs/hub/en/xet 
 为什么要构建 Buckets 
 当你处理以下场景时，很快就会发现 Git 并不是一个理想的抽象： 
 训练集群在训练过程中持续写入 checkpoints 和 optimizer states 
 数据流水线对原始数据集进行迭代式处理 
 Agent 系统存储 trace、记忆以及共享知识图谱 
 这些场景的存储需求其实非常一致：能够快速写入、按需覆盖、同步目录、删除过期文件，并保持系统持续高效运行。 
 Bucket 是 Hub 上的一种非版本化存储容器。它位于用户或组织的命名空间下，使用标准的 Hugging Face 权限系统，可以设置为私有或公开，并且有可在浏览器中访问的页面。同时也可以通过类似 hf://buckets/username/my-training-bucket 这样的地址在程序中访问。 
 为什么 Xet 很重要 
 Buckets 构建在 Xet 之上，这是 Hugging Face 的基于数据块 (chunk) 的存储后端，而这一点比看起来更关键。 
 Xet https://hf.co/docs/hub/en/xet 
 Xet 并不会把文件当作整体的二进制块来处理，而是会将内容拆分为多个 chunk，并在不同文件之间进行去重。例如： 
 上传一个与原始数据高度相似的处理后数据集？很多 chunk 已经存在。 
 保存连续的训练 checkpoint，其中大部分模型参数保持不变？同样可以复用已有 chunk。 
 Buckets 在上传时会自动跳过已经存在的数据块，从而减少带宽消耗、加快传输速度，并提高存储效率。 
 这与机器学习工作负载非常契合。训练流水线通常会生成大量相互关联的产物，例如原始数据与处理后的数据、连续 checkpoint、Agent trace 以及其衍生摘要等，而 Xet 正是为利用这种数据重叠而设计的。 
 对于 Enterprise 用户，计费是基于 去重后的存储量 ，因此共享 chunk 可以直接减少实际计费空间。去重不仅提升速度，也能降低成本。 
 预热 (Pre-warming) ：让数据更接近计算资源 
 Buckets 存储在 Hub 上，这意味着默认是全球可访问的存储。但并不是所有工作负载都能接受跨区域读取数据的延迟。对于分布式训练和大规模数据流水线来说，存储位置会直接影响吞吐量。 
 Pre-warming 可以把“热点数据”提前放到更靠近计算资源所在的云服务商和区域的位置。这样一来，就不需要在每次读取数据时都跨区域传输。你只需要声明数据应当在哪个位置可用，Buckets 就会在任务启动前把数据准备好。 
 这在以下场景中特别有用：例如训练集群需要快速访问大型数据集或 checkpoint，或者在多区域架构中，不同阶段的流水线运行在不同云环境时。 
 目前我们首先与 AWS 和 GCP 合作，未来还会支持更多云服务提供商。 
 快速开始 
 使用 hf CLI，你可以在 2 分钟内创建并使用一个 bucket。首先安装并登录： 
 curl -LsSf https://hf.co/cli/install.sh | bash 
 hf auth login 为你的项目创建一个 bucket： 
 hf buckets create my-training-bucket --private 假设你的训练任务将 checkpoint 写入本地目录 ./checkpoints ，可以把这个目录同步到 Bucket： 
 hf buckets sync ./checkpoints hf://buckets/username/my-training-bucket/checkpoints 对于大规模传输，你可能希望先查看会发生什么。 --dry-run 会打印执行计划，而不会真正进行操作： 
 hf buckets sync ./checkpoints hf://buckets/username/my-training-bucket/checkpoints --dry-run 你也可以把同步计划保存到文件中，之后再执行： 
 hf buckets sync ./checkpoints hf://buckets/username/my-training-bucket/checkpoints --plan sync-plan.jsonl 
 hf buckets sync --apply sync-plan.jsonl 完成后，可以通过 CLI 查看 bucket 内容： 
 hf buckets list username/my-training-bucket -h 或者直接在 Hub 上浏览： https://hf.co/buckets/username/my-training-bucket . 
 整个流程非常简单：创建 bucket，把工作数据同步进去，在需要时查看它，而真正需要发布的内容再放入带版本控制的仓库中。 对于一次性操作，可以使用 hf buckets cp 复制单个文件，或使用 hf buckets remove 删除过期对象。 
 在 Python 中使用 Buckets 
 以上功能同样可以通过 Python 使用 huggingface_hub 实现 (从 v1.5.0 开始支持) 。API 的使用方式也类似：创建、同步、查看。 
 huggingface_hub https://github.com/huggingface/huggingface_hub 
 v1.5.0 https://github.com/huggingface/huggingface_hub/releases/tag/v1.5.0 
 from huggingface_hub import create_bucket, list_bucket_tree, sync_bucket 
 create_bucket( "my-training-bucket" , private= True , exist_ok= True ) 
 sync_bucket( 
 "./checkpoints" , 
 "hf://buckets/username/my-training-bucket/checkpoints" , 
 ) 
 for item in list_bucket_tree( 
 "username/my-training-bucket" , 
 prefix= "checkpoints" , 
 recursive= True , 
 ): 
 print(item.path, item.size) 这使得 Buckets 可以很方便地集成到训练脚本、数据流水线或任何需要以编程方式管理产物的服务中。Python 客户端还支持批量上传、选择性下载、删除以及 bucket 迁移等更精细的操作。 
 Buckets 也可以在 JavaScript 中使用 @huggingface/hub (从 v2.10.5 开始支持) ，因此你也可以在 Node.js 服务或 Web 应用中集成 Buckets。 
 @huggingface/hub https://www.npmjs.com/package/@huggingface/hub 
 文件系统集成 
 Buckets 还可以通过 HfFileSystem 使用，这是 huggingface_hub 中一个兼容 fsspec 的文件系统接口。这意味着你可以像操作普通文件系统一样，对 Bucket 中的内容进行列出、读取、写入以及使用 glob 模式匹配文件。同时，任何支持 fsspec 的库都可以直接访问 Buckets，无需额外适配。 
 fsspec https://filesystem-spec.readthedocs.io/ 
 from huggingface_hub import hffs 
 # List files in a bucket directory 
 hffs.ls( "buckets/username/my-training-bucket/checkpoints" , detail= False ) 
 # Glob for specific files 
 hffs.glob( "buckets/username/my-training-bucket/**/*.parquet" ) 
 # Read a file directly 
 with hffs.open( "buckets/username/my-training-bucket/config.yaml" , "r" ) as f: 
 print(f.read()) 由于 fsspec 是 Python 远程文件系统的标准接口，因此像 pandas、Polars 和 Dask 这样的库可以直接使用 hf:// 路径从 Buckets 读取或写入数据，而无需额外配置： 
 import pandas as pd 
 # Read a CSV directly from a Bucket 
 df = pd.read_csv( "hf://buckets/username/my-training-bucket/results.csv" ) 
 # Write results back 
 df.to_csv( "hf://buckets/username/my-training-bucket/summary.csv" ) 这样你就可以在不改变代码读写方式的情况下，将 Buckets 集成到现有的数据工作流程中。 
 从 Buckets 到带版本的仓库 
 Buckets 是一个高效且可变的存储空间，用来存放那些仍在不断变化中的产物。当某些内容变成稳定的交付结果后，通常就应该放入带版本控制的模型仓库或数据集仓库中。 
 在未来的规划中，我们将支持 Buckets 与仓库之间的双向直接传输：例如将最终的 checkpoint 权重提升到模型仓库，或者在数据流水线完成后，把处理好的数据分片提交到数据集仓库。 这样一来，工作层 (用于处理中的数据) 与发布层 (用于最终成果) 既保持分离，又能无缝衔接，形成一个完整的 Hub 原生工作流程。 
 启动合作伙伴 
 在向所有用户开放 Buckets 之前，我们与一小部分合作伙伴进行了私有测试。 
 非常感谢 Jasper、Arcee、IBM 和 PixAI 在早期版本测试中提供的帮助。他们发现了许多问题，并提出了大量反馈，直接推动了这个功能的完善。 
 总结与资源 
 Storage Buckets 为 Hub 补上了一个关键的存储层。它为机器学习中那些 高吞吐、可变的数据 提供了原生的存放位置，比如 checkpoint、处理后的数据、Agent trace、日志，以及所有在最终定稿之前仍然有价值的中间产物。 
 由于 Buckets 构建在 Xet 之上，它不仅比把所有内容都强行用 Git 管理更易用，也更适合 AI 系统中常见的这类相互关联的数据。这带来的好处包括：更快的传输速度、更高效的去重能力，以及在 Enterprise 方案中基于去重后存储量的更优计费方式。 
 如果你已经在使用 Hugging Face Hub，Buckets 可以让你的更多工作流程都留在同一个平台上。如果你来自 S3 风格的对象存储环境，Buckets 也提供了熟悉的使用模式，同时更适配 AI 产物，并能无缝过渡到 Hub 上的最终发布流程。 
 Buckets 已包含在现有的 Hub storage plans 中。免费账户提供入门存储空间，而 PRO 和 Enterprise 计划提供更高额度。详细信息请查看 storage page 。 
 Hub storage plans https://hf.co/docs/hub/en/storage-limits #storage -plans 
 storage page https://hf.co/storage 
 了解更多并亲自尝试： 
 Buckets guide 
 Hub documentation 
 CLI Installation guide 
 CLI guide 和 reference 
 Example Bucket on the Hub 
 Storage pricing 
 Buckets guide https://hf.co/docs/huggingface_hub/en/guides/buckets 
 Hub documentation https://hf.co/docs/hub/storage-buckets 
 Installation guide https://hf.co/docs/huggingface_hub/en/installation 
 guide https://hf.co/docs/huggingface_hub/en/guides/cli 
 reference https://hf.co/docs/huggingface_hub/en/package_reference/cli 
 Example Bucket on the Hub https://hf.co/buckets/julien-c/my-training-bucket 
 Storage pricing https://hf.co/pricing #storage 
 英文原文: https://huggingface.co/blog/storage-buckets 
 原文作者: Lucain Pouget, Eliott Coyac, Adrien Carreira, Victor Mustar, Julien Chaumond, Quentin, Lhoest, Pierric Cistac, Sylvestre Bcht, Hugo Larcher, Rajat Arya, Di Xiao, Assaf Vayner 
 译者: Luke, Hugging Face Fellow 
 阅读原文 
 跳转微信打开
```

---

## 5. LeRobot v0.5.0 正式发布

- 日期: 2026-03-11 09:23
- 链接: https://mp.weixin.qq.com/s?__biz=Mzk0MDQyNTY4Mw==&mid=2247496647&idx=1&sn=6cb078e922305485765f2059438d1b2b

```
原创 Hugging Face 2026-03-11 09:23 美国 
 自 v0.4.0 以来，项目已经合并了 200+ 个 PR，并迎来了 50 多位新贡献者。 
 自 v0.4.0 以来，项目已经合并了 200+ 个 PR ，并迎来了 50 多位新贡献者 。因此 LeRobot v0.5.0 成为目前规模最大的一次发布 —— 几乎在所有方向上都实现了扩展：支持更多机器人 (包括首个类人机器人) 、更多策略模型 (包括回归的自回归 VLA) 、更快的数据集处理、可以直接从 Hub 加载的仿真环境，以及基于 Python 3.12 与 Transformers v5 的现代化代码库。无论你是在仿真环境中训练策略，还是在真实硬件上部署，v0.5.0 都提供了大量新能力。 
 TL;DR 
 LeRobot v0.5.0 新增 Unitree G1 类人机器人完整支持 (全身控制模型) ，并引入新的策略，包括 Pi0-FAST 自回归 VLA 和 Real-Time Chunking (实时分块) 用于实现更快响应的推理。同时还加入 流式视频编码 ，消除了录制任务之间的等待时间。 
 此外，本版本还推出了 EnvHub ，允许直接从 Hugging Face Hub 加载仿真环境；集成 NVIDIA IsaacLab-Arena ；并对代码库进行了全面现代化升级，包括 Python 3.12+、Transformers v5 以及第三方策略插件系统 。 
 硬件：支持的机器人数量再创新高 
 LeRobot v0.5.0 大幅扩展了支持的硬件设备，从机械臂、移动机器人到完整的类人机器人。 
 Unitree G1 Humanoid 
 本次发布中最重要的硬件新增是： 对 Unitree G1 类人机器人的完整支持 。这是 LeRobot 第一次集成类人机器人，而且支持非常全面： 
 运动能力 (Locomotion) ：可以行走、导航并在环境中移动。 
 操作能力 (Manipulation) ：能够执行精细的物体操作任务。 
 远程操控 (Teleoperation) ：通过直观的遥操作界面远程控制 G1。 
 全身控制 (Whole-Body Control, WBC) ：同时协调行走和操作，实现复杂的真实世界任务。 
 G1 的加入标志着 LeRobot 在通用机器人方向迈出了重要一步 —— 从桌面机械臂扩展到 完整身体的具身智能系统 。你可以按照 文档 自己尝试。 
 文档 https://hf.co/docs/lerobot/unitree_g1 
 OpenArm & OpenArm Mini 
 我们新增了对 OpenArm 机械臂以及其配套 OpenArm Mini 遥操作设备的支持。OpenArm 是一款性能出色的机械臂，并且已经实现完整的 LeRobot 集成，而 Mini 则作为它的自然遥操作设备。 
 OpenArm https://openarm.dev 
 两者都支持 双臂配置 (bi-manual) ，可以构建双机械臂系统，从而完成更复杂的操作任务。更多信息可查看 文档 。 
 文档 https://hf.co/docs/lerobot/openarm 
 更多机器人 
 硬件生态仍在持续扩展： 
 Earth Rover ：LeRobot 首次支持移动机器人，可用于户外导航和地面移动任务。 
 OMX Robot ：新增的机械臂平台，支持可配置夹爪参数和校准功能。 
 SO-100/SO-101 统一实现 ：我们将 SO-100 和 SO-101 的实现整合到一个更简洁的代码库中 (包括双臂配置) ，减少重复代码，更易维护，同时保持原有功能。 
 Earth Rover https://shop.frodobots.com/products/miniplus 
 OMX Robot https://ai.robotis.com/omx/hardware_omx.html 
 CAN 总线电机 
 通过 CAN (Controller Area Network) 总线 新增了对电机控制器的支持，从而能够接入更高性能的执行器： 
 RobStride ：基于 CAN 的电机控制器，适用于高扭矩应用。 
 Damiao ：另一种 CAN 总线电机控制器，进一步扩展兼容硬件范围。 
 RobStride https://github.com/RobStride/Product_Information 
 这意味着 LeRobot 现在不仅支持 Dynamixel 和 Feetech，也能够驱动更多 专业级执行器 。 
 策略模型：不断扩展的模型库 
 本次发布为 LeRobot 新增 6 种策略或技术 ，进一步推动开源机器人学习的发展。 
 Pi0-FAST：自回归 VLA 
 Pi0-FAST 将自回归的 Vision-Language-Action (VLA) 模型 引入 LeRobot，并采用 FAST (Frequency-space Action Sequence Tokenization) 方法。 
 与 Pi0 使用的 flow-matching 方法不同，Pi0-FAST 使用 基于 Gemma 300M 的自回归动作专家模型 ，生成离散化的动作 token，实现： 
 FAST Tokenization ：动作被 token 化，便于自回归解码，使用专门的 FAST action tokenizer 。 
 灵活解码 ：可以通过温度参数和最大解码步数，在速度与质量之间进行权衡。 
 兼容 RTC ：可与 Real-Time Chunking 结合，实现更快速的推理。 
 FAST action tokenizer https://hf.co/lerobot/fast-action-tokenizer 
 lerobot-train \ 
 --policy.type=pi0_fast \ 
 --dataset.repo_id=lerobot/aloha_sim_insertion_human \ 
 --policy.device=cuda Real-Time Chunking (RTC) 
 Real-Time Chunking 是来自 Physical Intelligence 的推理阶段技术，可以显著提升 flow-matching 策略的响应速度。 
 Physical Intelligence https://www.pi.website 
 传统方法需要等一个完整动作序列生成后再重新规划，而 RTC 会 持续融合新的预测与正在执行的动作 ，使机器人行为更加平滑、响应更快。 
 RTC 不是独立策略，而是一个增强模块，可用于 Pi0 系列、SmolVLA 与 Diffusion 等策略。 
 启用方式： 
 --policy.rtc_config.enabled= true 在真实机器人部署中 (对延迟敏感的场景) ，这是一个非常重要的改进。更多技术细节见 论文 和 文档 。 
 论文 https://hf.co/papers/2506.07339 
 文档 https://hf.co/docs/lerobot/rtc 
 Wall-X 
 Wall-X 是一个新的 VLA 策略，基于 Qwen2.5-VL 构建，并使用 flow-matching 进行动作预测。 
 Qwen2.5-VL https://hf.co/collections/Qwen/qwen25-vl 
 它将 Qwen2.5-VL 的强大视觉语言理解能力与 flow-matching 控制头结合，实现 跨机器人形态控制 (cross-embodiment control) 。 
 pip install lerobot[wall_x] 
 lerobot-train \ 
 --policy.type=wall_x \ 
 --dataset.repo_id=lerobot/aloha_sim_insertion_human X-VLA 
 X-VLA 将 基于 Florence2 的 VLA 模型 引入 LeRobot。 
 该模型基于 Microsoft 的 Florence-2 视觉语言模型 ，为机器人学习提供了另一种基础模型选择，进一步增加模型多样性。 
 查看 训练指南 和 基础模型 。 
 训练指南 https://hf.co/docs/lerobot/xvla 
 基础模型 https://hf.co/lerobot/xvla-base 
 pip install lerobot[xvla] 
 lerobot-train \ 
 --policy.type=xvla \ 
 --dataset.repo_id=lerobot/bimanual-so100-handover-cube SARM 
 SARM (Stage-Aware Reward Modeling) 用于解决机器人学习中一个非常困难的问题： 长时序任务 (long-horizon tasks) 。 
 传统方法通常使用单一线性进度信号，而 SARM 会 同时预测任务阶段以及阶段内进度 ，从而更准确地描述任务进展。 
 这种方式可以显著提高复杂多步骤操作任务的训练效果。更多信息请查看 文档 。 
 文档 https://hf.co/docs/lerobot/sarm 
 PEFT 支持 
 现在你可以使用 LoRA 等 PEFT 方法对大型 VLA 模型进行微调 ，而无需修改核心训练流程。 
 PEFT 配置在策略层进行管理，可以用较少算力将大型基础模型适配到特定机器人和任务。 
 详情见 文档 。 
 文档 https://hf.co/docs/lerobot/peft_training 
 lerobot-train \ 
 --policy.type=pi0 \ 
 --policy.peft_config.use_peft= true \ 
 --dataset.repo_id=lerobot/aloha_sim_insertion_human 数据集：录制更快，训练更快 
 本次发布对数据集处理流程进行了重大优化，使 数据采集和训练速度显著提升 。 
 流式视频编码 
 过去在录制数据集时，每个 episode 结束后都需要等待视频编码完成。 
 现在不需要等待了。 
 通过 Streaming Video Encoding (流式视频编码) ，视频帧会在采集时实时编码，实现 episode 之间零等待时间 。 
 系统还支持 自动检测硬件编码器 ，如果 GPU 提供视频编码能力，会自动使用。 
 dataset = LeRobotDataset.create( 
 repo_id= "my/dataset" , 
 fps= 30 , 
 video_backend= "auto" , 
 streaming_encoding= True , 
 ) 图像训练速度提升 10 倍，编码速度提升 3 倍 
 在底层实现中，我们修复了数据访问瓶颈，并重构了图像处理流程： 
 图像训练速度提升 10 倍 ：优化图像变换流程并修复隐藏的数据访问瓶颈。 
 编码速度提升 3 倍 ：默认启用并行编码，并根据数据类型动态调整压缩级别。 
 更高 CPU 利用率 ：录制和数据集创建时资源使用更加高效。 
 新的数据集工具 
 数据集编辑工具也持续增强： 
 子任务支持 ：可以在 episode 中标注子任务，支持层级任务学习。 
 图像转视频 ：将现有图像数据集转换为视频格式，提高存储效率，并支持多个 episode 合并到同一视频文件。 
 更多编辑操作 ：新增 info 数据集检查功能、任务修改工具，以及对拆分、合并、特征编辑等操作的修复。 
 更多配置选项 ：可自定义视频编码格式、容差设置和元数据缓冲大小。 
 EnvHub：从 Hub 加载仿真环境 
 EnvHub 让 LeRobot 可以 直接从 Hugging Face Hub 加载仿真环境 。 
 过去需要在本地安装环境并手动注册，现在只需要指定 Hub 仓库即可： 
 自动下载环境代码 
 自动注册到 Gymnasium 
 直接用于训练和评估 
 Hub 环境使用 HubEnvConfig ，会下载并执行远程 make_env 函数： 
 lerobot-train \ 
 --env.type=hub \ 
 --env.hub_path= "username/my-custom-env" \ 
 --policy.type=act 这大大降低了分享自定义仿真环境的门槛。只需打包环境并上传到 Hub，其他人就能直接使用。 
 更多信息见 文档 。 
 文档 https://hf.co/docs/lerobot/envhub 
 示例教程： LeIsaac x LeRobot EnvHub tutorial 
 LeIsaac x LeRobot EnvHub tutorial https://hf.co/docs/lerobot/envhub_leisaac 
 NVIDIA IsaacLab-Arena 
 我们还集成了 NVIDIA IsaacLab-Arena ，为 LeRobot 带来 GPU 加速仿真 。 
 IsaacLab-Arena 提供了一系列基于 NVIDIA Isaac Sim 的操作任务环境，并支持大规模并行环境实例，从而加速强化学习训练。 
 该集成包括： 
 专门的前处理和后处理流程 
 与 LeRobot 训练流程完全兼容 
 详情见 文档 。 
 文档 https://hf.co/docs/lerobot/envhub_isaaclab_arena 
 代码库：现代化基础设施 
 本版本对代码库进行了全面升级： 
 Python 3.12+ ：LeRobot 现在要求 Python 3.12 作为最低版本，从而能够使用更现代的语法并获得更好的性能。 
 Transformers v5 ：项目已经迁移到 Hugging Face Transformers v5 ，以保持与最新模型生态的兼容。 
 第三方策略插件 ：类似于 v0.4.0 的硬件插件系统，现在也可以把自定义策略注册为可安装的插件包，例如： pip install lerobot_policy_mypolicy ，然后通过 --policy.type=mypolicy 使用，无需修改核心库代码。具体方法可以参考 文档 。 
 远程 Rerun 可视化 ：可以使用 Rerun 远程可视化机器人的遥测数据，并支持图像压缩，从而实现更节省带宽的数据流传输。 
 安装流程改进 ：新增 uv 的 安装说明 ，同时进一步明确了安装步骤，并优化了依赖管理。现在顺序安装流程也在文档中有清晰说明。 
 文档版本管理 ：文档现在支持版本化，可以始终查阅与你当前安装版本对应的文档。 
 PyTorch 版本更新 ：更新了 PyTorch 的版本范围，以支持 NVIDIA Blackwell GPU 。 
 文档 https://hf.co/docs/lerobot/bring_your_own_policies 
 安装说明 https://hf.co/docs/lerobot/installation 
 社区与生态 
 Discord 社区升级 ：对 Discord 社区进行了更新，优化了频道结构，使这个最活跃的社区交流平台更加清晰、有序。 
 GitHub README、模板与自动标签 ：更新了 README，新增 issue 和 PR 模板、贡献指南，以及自动化标签系统，让社区成员更容易参与和贡献。 
 ICLR 2026 论文录用 ：LeRobot 论文已被 ICLR 2026 接收。 
 ICLR 2026 https://openreview.net/forum?id=CiZMMAFQR3 
 LeRobot Visualizer 更新 ：可视化工具进行了升级，新增数据集可视化徽章，并改进了整体功能。 可以在这里体验 
 可以在这里体验 https://hf.co/spaces/lerobot/visualize_dataset?path=%2Fimstevenpmwork%2Fthanos_picking_power_gem%2Fepisode_0 
 LeRobot Annotation Studio ：推出了一个 HuggingFace Space，用于给数据集中的每个时刻添加自然语言子任务标注，让数据标注更加方便。 查看项目 
 查看项目 https://hf.co/spaces/lerobot/annotate 
 最后 
 除了上述重点功能之外，v0.5.0 还包含： 
 数百个 bug 修复 
 文档改进 
 CI/CD 优化 
 大量开发体验提升 
 从更严格的类型检查到更健壮的测试基础设施，我们正在持续加强 LeRobot 的基础架构，以支持未来更大规模的发展。 
 我们也要向 整个社区表示衷心感谢 —— 所有贡献者、用户和合作伙伴都在推动 LeRobot 不断进步。每一次 bug 报告、PR 和讨论都让这个项目变得更好。 
 更多内容即将到来 🤗 从这里开始： https://github.com/huggingface/lerobot 
 https://github.com/huggingface/lerobot https://github.com/huggingface/lerobot 
 — LeRobot 团队 ❤️ 
 很快就会有一个重大惊喜发布，敬请期待！👕 
 英文原文: https://huggingface.co/blog/lerobot-release-v050 
 原文作者: Steven Palma, Pepijn Kooijmans, Jade Choghari, Caroline Pascal, Khalil Meftah, Martino Russi, Nicolas Rabault, Michel Aractingi, Virgile BATTO, Thomas Wolf 
 译者: Luke, Hugging Face Fellow 
 阅读原文 
 跳转微信打开
```

---

## 6. 社区供稿丨Ling-2.5-1T，普惠智能，即时响应

- 日期: 2026-02-16 20:10
- 链接: https://mp.weixin.qq.com/s?__biz=Mzk0MDQyNTY4Mw==&mid=2247496392&idx=1&sn=244eda1ff0435a9122dc8bfda77b93ac

```
百灵大模型 2026-02-16 20:10 法国 
 以下文章来源于：百灵大模型 
 百灵大模型 分享蚂蚁百灵大模型研发进展 
 蚂蚁集团发布 Ling-2.5-1T 
 今天，我们发布并开源 Ling-2.5-1T 。 
 深度思考模型（thinking model）拉升智能上限，即时模型（instant model）则凭效率与效果的平衡 拓宽智能覆盖 ，它让 AGI 不只更强，也更普惠。作为百灵家族最新的旗舰级即时模型，Ling-2.5-1T 在 模型架构、token 效率、偏好对齐 等维度全面升级，期待为用户带来 更优质的普惠智能体验 。 
 万亿参数与百万上下文 ：Ling-2.5-1T 具有 1T 总参数（激活 63B），预训练语料从前代的 20T 扩展至 29T，凭借高效的混合线性注意力架构与精细的数据策略优化，模型能够以高吞吐处理长达 1M token 的上下文。 
 更高的 token 效率 ：引入“正确性 + 过程冗余”复合奖励机制，进一步拓展了即时模型效率与效果的平衡边界。在相同 token 效率条件下，Ling-2.5-1T 的推理能力显著超越前代，接近需消耗约 4 倍输出 token 的前沿思考模型水平。 
 精细化偏好对齐 ：通过引入双向强化学习反馈、Agent-based 指令约束校验等精细化对齐策略，使 Ling-2.5-1T 在创意写作、指令遵循等偏好对齐类任务上相比前代模型实现大幅提升。 
 高效的原生智能体交互 ：基于大规模高保真交互环境进行 Agentic RL 训练，Ling-2.5-1T 可适配 Claude Code、OpenCode、OpenClaw 等主流智能体产品。在通用工具调用基准 BFCL-V4 上达到开源领先水平。 
 我们全面评估了 Ling-2.5-1T 在 知识、推理、智能体交互、指令遵循、长文本处理 等多个权威基准评测上的表现。Ling-2.5-1T 与前代模型 Ling-1T 对比，实现了全方位的能力提升，是百灵家族当前最强大的即时模型。在与主流的大尺寸即时模型 （DeepSeek V3.2、Kimi K2.5、GPT 5.2） 对比中，Ling-2.5-1T 在复杂推理、 指令遵循能力具有明显优势。 
 高效智能 
 Ling-2.5-1T 延续了演进式思维链（Evolutionary CoT）的后训练方法，并将强化学习奖励升级为兼顾“正确性”与“过程冗余”的复合指标。在 AIME 2026 这一最新高难数学基准上，它在平均输出约 5890 token 的情况下显著超越前代，逼近平均消耗 15k–23K token 的前沿思考模型。通过“由浅入深”的激活策略，长链条推理被高效折叠为直觉式响应，进一步拓展了即时模型效率与效果的平衡边界。 
 Ling-2.5-1T 的高效推理能力 
 拓展了即时模型效率与效果的平衡边界 
 偏好对齐 
 针对生成式模型常见的“空洞辞藻”与“机械文风”问题，Ling-2.5-1T 在 RLHF 阶段引入了 双向强化学习 反馈机制。在惩罚端，联合专家构建细粒度惩罚项，针对逻辑谬误、事实幻觉及机械文风实施精准扣分，确立质量红线；在奖励端，摒弃长度导向，构建基于有效信息增益的奖励模型。在此机制下，模型显著抑制了泛泛而谈的说教倾向，实现高信息密度与逻辑真实性的输出。 
 另外，Ling-2.5-1T 对指令遵循能力进行了系统性重构。我们构建了 Agent-based 校验机制 ，针对细粒度约束，编写了由 Rubric（评分规则）与 Code（代码断言）构成的硬性校验奖励。在 IFEval 等指令遵循基准测试中，Ling-2.5-1T 在多重约束下的执行准确率与逻辑一致性显著提升。 
 智能体交互 
 Ling-2.5-1T 基于自主研发的大规模高保真交互环境进行 Agentic RL 训练，模型内化了多步规划与工具执行策略。在 Claude Code、OpenCode 等 Agentic Coding 框架适配时，模型的意图理解与操作连贯性显著提升，并在 BFCL-v4、Terminal-Bench 等基准测试中得到了效果验证。 
 万亿混合线性架构与百万上下文窗口 
 Ling 2.5 架构在 Ling 2.0 架构基础上引入了 混合线性注意力机制 。通过增量训练方式，将Ling 2.0架构的 GQA 升级为 1:7 的 MLA + Lightning Linear 结构。具体而言，我们基于此前发布的 Ring-flash-linear-2.0 技术路线，将部分 GQA 层改造为 Lightning Linear Attention，以显著提升长程推理场景下的吞吐能力。为进一步压缩 KV Cache，我们将其余 GQA 层近似转换为 MLA，并对其中的 QK Norm、Partial RoPE 等特性进行了针对性适配，以增强 Ling 2.5 架构在混合注意力架构下的表达能力。 
 Ling 2.5 架构 
 改造后，Ling-2.5-1T 的激活参数量从 51B 提升至 63B。但在混合线性注意力架构的支持下，其推理效率相比 Ling-1T 仍实现了大幅提升。即便与激活参数仅为 32B 的 KIMI K2 架构相比，1T规模下的 Ling 2.5 架构在长程推理场景下的吞吐依然具有显著优势；且 生成长度越长，吞吐优势越明显 。 
 单机8卡H20-3e，batch size = 64， 
 不同 生成长度 下的 解码 吞吐（decode throughput）对比 
 单机8卡H200，batch size = 64， 
 不同 生成长度 下的 解码 吞吐（decode throughput）对比 
 在架构改造之后，我们对 Ling-2.5-1T-base 进行了基于 9T 优质语料 的持续预训练，重点强化了预训练基座的 世界知识覆盖 与 智能体交互 的基础能力。同时，凭借混合线性注意力架构在长文本处理上的极高计算效率与可扩展性，我们将上下文窗口扩展训练至 256K tokens ，并通过 YaRN 外推稳定支持最高 1M tokens 的超长上下文处理能力。 
 此前，社区对混合线性注意力在超长上下文推理的有效性仍存在一定争议。针对这一问题，我们对 Ling-2.5-1T 开展了系统性的超长上下文基准评测。结果显示，Ling-2.5-1T 在对比采用 MLA 和 DSA 架构的大型即时模型（如 Kimi K2.5、DeepSeek V3.2）时，在多项超长上下文任务中展现出效果优势；同时也可以看到，与领先的闭源 API 模型（如 GPT-5.2、Gemini 3 Pro）相比，仍存在一定差距，后续版本将持续推进相关能力的进一步提升。 
 Ling-2.5-1T 的大海捞针测试， 
 在 1M tokens 的上下文窗口内均表现优异 
 不同模型 16K ~ 1M tokens 上下文窗口 
 在 RULER 与 MRCR 基准上的对比 
 长文本基准对比 
 （Ruler 与 MRCR 为 16K~256K tokens 的平均分） 
 案例展示 
 写作 
 高效获取信息，也能感受到贴心陪伴，收获一份会心一笑的轻松与愉悦。 
 指令遵循 
 关于《知识产权质押纠纷》的案例，展示了模型可以在严格遵循10余项关于内容框架、内容细节、格式、字数等指令下，有条理的连续回答若干法律问题。 
 长文本 
 Berkeley Lights 公司 2019H2 与 2020H1 财报对比的案例，展示了模型可以对一篇数值密集型的金融财报进行信息抽取汇总，并能对重点财务衍生指标进行复杂计算，并得到财报的深度分析结论。 
 可视化 
 PPT 
 一句话完成PPT演示文稿，自动完成 LLM 原理的内容梳理与 HTML 代码构建。 
 Prompt: 帮我用 HTML 生成一个介绍 LLM 基本原理的 PPT，画风要有科技感，术语严谨学术性强，16:9 的页面。 
 翻牌游戏 
 霓虹发光、阴影、玻璃质感提升沉浸感，动态噪声与慢速渐变动画营造复古未来感。兼具视觉艺术性与现代前端技术的结合。 
 请设计一个具有蒸汽波（Vaporwave）风格的精美记忆翻牌网页游戏应用，具体要求如下： 1. 核心玩法 标准记忆翻牌玩法 玩家每次翻开两张卡片，若图案一致则消除 直至所有卡片配对完成游戏结束 2. 视觉设计 蒸汽波主题：紫粉渐变背景、霓虹网格、日落元素 主色调：霓虹粉（ #FF77FF）、青蓝（#00FFFF）、深紫背景 卡片采用玻璃拟态（Glassmorphism）效果 背景可加入轻微动态噪声或慢速渐变动画 3. 卡片设计 卡片正面为蒸汽波风格图标（雕塑、磁带、棕榈树等） 翻转动画使用 3D rotateY 已配对卡片变为半透明并锁定 当前翻开的卡片添加霓虹外发光效果 4. 交互增强 错误配对时卡片轻微左右晃动 成功配对触发粒子闪光效果 支持点击与键盘操作（Enter / Space） 5. 难度系统 简单：4×4（8 对） 中等：6×6（18 对） 困难：8×8（32 对） 6. 辅助功能 步数计数与用时统计 一键重开 移动端自适应布局 7. 布局要求 顶部标题区 + 中央卡片区 + 底部控制栏 单 HTML 文件实现. 
 票房预测（可视化报表） 
 Ling-2.5-1T 模型内置掌握蚂蚁开源可视化框架 AntV ，我们使用该框架的 G2 报表能力，多维度呈现 2026 年春节档票房预测，包括口碑关联分析、排片资源分布、受众流向等复杂业务场景；视觉上采用毛玻璃拟态化设计，打造春节档专属视觉氛围。 
 生成一个春节主题的《电影票房数据预测》Dashboard. 要求包含以下内容：\n口碑-票房关联散点（Point Chart）：横轴为豆瓣/猫眼评分，纵轴为票房，气泡大小代表排片量。\n多片逐日增长曲线（Multi- line Chart）：展示 TOP 5 影片的日增票房，采用曲线平滑处理，带发光滤镜。\n排片率动态占比（Stacked Rose Chart）：南丁格尔玫瑰图，展示 24 小时内各片排片资源的变化。\n黄金场次渗透率（Bullet Chart）：子弹图，展示电影在 18 : 00 - 21 : 00 黄金档的填充率。\n受众重叠度分析（Venn/Chord Chart）：虽G2需转换，可用和弦图展示同时关注两部电影的观众流向。\n票房预测偏差图（Interval Chart）：区间柱状图，展示AI预测票房与实际票房的差值。\n\n已知 2026 年春节贺岁档的电影有这些：《飞驰人生 3 》《熊出没·年年有熊》《镖人：风起大漠》《惊蛰无声》《星河入梦》《熊猫计划之部落奇遇记》 《重返·狼群》（重映）《消失的我》《夜王》. 
 Code 
 Flappy Bird 
 从需求到可执行程序，一条指令完成轻量级应用 。 仅用“编写一个可直接运行的清新风 Flappy Bird 游戏”作为需求，接入 Code Agent 即可自主完成从游戏设计、代码实现到安装部署的全过程，交付完整可执行项目，而不仅是代码片段。 
 Prompt：请你写一个能够直接运行的 Python Flappy Bird 小游戏，游戏画面风格需要是小清新风的。 
 Agentic 能力 
 Mini Alipay 
 从需求到可运行项目，仅需一次会话。在 Code Agent 驱动下，我们仅用一条涵盖前后端架构与新春主题的复杂需求，持续工作 40 分钟，直接产出一个架构完整、功能可用的 MiniAlipay 项目。这不再是代码片段演示，而是一个真正具备完整功能模块、可独立部署运行的生产级应用原型。 
 Prompt：请你写一个 minialipay，前后端分离架构 + 内存数据库存储，支持基础的用户登录、转账等功能，并且有新春特色的集五福功能，欢庆春节主题。 
 Opencode 接入（skills） 
 能够调用正确的 Skills，完整执行内部系统开发指令，Agent 自动化完成从基础架构搭建到多品牌主题逻辑的代码实现，将需求描述直接转化为具备导航、搜索及动态换肤功能的可运行原型。 
 设计一个完整的内部系统，需满足以下复杂需求： 
 1. 构建一个首页，包含导航、搜索、主题切换用户界面，提供现代化交互体验与可扩展的前端架构。 
 2. 实现多套品牌化主题，允许不同部门使用独立配色与字体，同时保持整体设计的一致性与可维护性，支持动态切换与定制。 
 验证标准：完成一个可演示的最小原型，集成上述多数核心能力，并通过测试验证关键链路的正确性。 
 Minecraft 机器人任务执行 
 精准执行空间构建指令，Agent 自动化完成从底层铺设到顶层收缩的数百次方块放置，将自然语言直接转化为游戏内的实体建筑。（使用的 Agent 框架 
 https://github.com/mindcraft-bots） 
 用砂岩创建一个长宽高为16 *16* 8的金字塔，第一层长宽为16 *16，第二层为14* 14，每叠加一层长宽都减2块,依次叠加 
 局限性与未来计划 
 Ling-2.5-1T 已实现高吞吐解码与领先的超长上下文处理能力，并初步具备智能体交互能力，为通用智能体时代奠定基础。但在复杂智能体交互和长程任务上，它仍落后于前沿模型。下一版本将聚焦真实世界复杂任务的长程执行与交付效率优化，同时持续提 升 Token 效率，以 在效率与效果间取得更优平衡。 
 欢迎通过以下方式下载、访问和使用 Ling-2.5-1T 。 
 🤗 Hugging Face： 
 https://huggingface.co/inclusionAI/Ling-2.5-1T 
 🤖 ModelScope ： 
 https://modelscope.cn/models/inclusionAI/Ling-2.5-1T 
 Ling Studio （ https://ling.tbox.cn/chat ） 与 ZenMux （ https://zenmux.ai/ ） 的 Chat 体验页和 API 服务将在近期上线。 
 本文由 Hugging Face 中文社区内容共建项目提供，稿件由社区成员投稿，经授权发布于 Hugging Face 公众号。文章内容不代表官方立场，文中介绍的产品和服务等均不构成投资建 议。了解更多请 关注公众号 
 如果你有与开源 AI、Hugging Face 相关的技术和实践分享内容，以及最新的开源 AI 项目发布，希望通过我们分享给更多 AI 从业者和开发者们，请通过下面的链接投稿与我们取得联系: 
 https://hf.link/to ugao 
 阅读原文 
 跳转微信打开
```

---

## 7. 社区供稿丨Ring-2.5-1T，思更深，行更远

- 日期: 2026-02-13 18:30
- 链接: https://mp.weixin.qq.com/s?__biz=Mzk0MDQyNTY4Mw==&mid=2247496390&idx=1&sn=de692b3223ee980961bfabfcc92ef1b7

```
百灵大模型 2026-02-13 18:30 法国 
 以下文章来源于：百灵大模型 
 百灵大模型 分享蚂蚁百灵大模型研发进展 
 蚂蚁集团发布并开源混合线性架构的万亿参数思考模型 Ring-2.5-1T 
 今天，我们发布并开源首个混合线性架构的万亿参数思考模型 Ring-2.5-1T 。 
 作为迈向通用智能体时代的关键步骤，我们将混合线性注意力架构在预训练和强化学习上均进行了大规模扩展，一方面利用高效的 1：7 MLA + Lightning Linear Attention 架构来提升模型的思考效率和探索空间，另一方面通过 扩展强化学习和智能体环境规模 来提升模型的思考深度和长程执行能力。 
 相比此前发布的 Ring-1T，Ring-2.5-1T 在 生成效率、思考深度、长程执行 上均有大幅提升： 
 高效生成 ：得益于高比例的线性注意力机制，在超过 32K 生成长度下，访存规模降低 10 倍以上， 生成吞吐提升 3 倍以上 ，尤其适合深度思考和长程执行的任务。 
 深度思考 ：在 RLVR 基础上引入 dense reward 来反馈思考过程的严谨性，使得 Ring-2.5-1T 同时实现 IMO 2025 和 CMO 2025 的金牌水平 （自测）。 
 长程执行 ：通过大规模 fully-async agentic RL 训练，显著提升针对复杂任务的长程自主执行能力，使得 Ring-2.5-1T 可以轻松适配 Claude Code 等智能体编程框架和 OpenClaw 个人 AI 助理。 
 深度思考与长程执行 
 为评估 Ring-2.5-1T 的深度思考和长程执行能力，我们选取了具有代表性的开源思考模型 （DeepSeek-v3.2-Thinking、Kimi-K2.5-Thinking） 和闭源API （GPT-5.2-thinking-high、Gemini-3.0-Pro-preview-thinking-high、Claude-Opus-4.5-Extended-Thinking） 作为参考。 Ring-2.5-1T 在 数学、代码、逻辑等高难推理任务 （IMOAnswerBench、AIME 26、HMMT 25、LiveCodeBench、ARC-AGI-V2） 和 智能体搜索、软件工程、工具调用等长程任务执行 （Gaia2-search、Tau2-bench、SWE-Bench Verified） 上均达到了 开源领先水平 。 
 我们还额外测试了深度思考模式（heavy thinking mode），通过在推理过程中扩展并行思考与总结，实现测试时扩展，从而有效提升推理的深度与广度。 
 在 IMO 2025（满分 42 分）中，Ring-2.5-1T 获得 35 分，达到金牌水平；在 CMO 2025（满分 126 分）中取得 105 分，显著高于金牌线（78 分）及国家集训队入选线（87 分）。对比 Ring-2.5-1T 与 Ring-1T 的答题结果可以发现，前者在推理逻辑严谨性、高阶数学证明技巧使用以及答案表述完整性方面均有明显提升。我们现已公开 Ring-2.5-1T 在 IMO 2025 与 CMO 2025 中的详细解答，完整内容可通过以下链接查看： https://github.com/inclusionAI/Ring-V2.5/tree/main/examples 
 此外，在挑战性的智能体搜索 GAIA2-search 任务中，Ring-2.5-1T 达到开源 SOTA 水平。GAIA2 环境强调跨应用工具协作与复杂任务执行能力，Ring-2.5-1T 在规划生成与多步工具调用上的效率与准确性均表现突出。 
 万亿规模的混合线性注意力架构 
 在通用智能体时代， 深度思考（deep thinking） 与 长程执行（long-horizon agent） 正成为语言基座的基本工作范式。这一转变对基座模型在长程推理解码效率上的架构能力提出了极高要求。作为迈向智能体模型（agentic model）架构的关键一步，Ling 2.5 架构在 Ling 2.0 架构基础上引入了 混合线性注意力架构 。通过增量训练方式，将 Ling 2.0 架构 的 GQA 升级为 1:7 的 MLA + Lightning Linear 结构。具体而言，我们基于此前发布的 Ring-flash-linear-2.0 技术路线，将部分 GQA 层改造为 Lightning Linear Attention，以显著提升长程推理场景下的吞吐能力。为进一步压缩 KV Cache，我们将其余 GQA 层近似转换为 MLA ，并对其中的 QK Norm 、Partial RoPE 等特性进行了针对性适配，以增强 Ling 2.5 架构 在混合注意力架构下的表达能力。 
 1T规模下的 Ling 2.5架构 
 改造后，Ring-2.5-1T 的激活参数量从 51B 提升至 63B。但在混合线性注意力架构的支持下，其 推理效率相比 Ling 2.0 仍实现了大幅提升 。即便与激活参数仅为 32B 的 KIMI K2 架构相比，1T 规模下的 Ling 2.5 架构在长程推理场景下的吞吐依然具有显著优势；且 生成长度越长，吞吐优势越明显 。 
 单机 8 卡 H20-3e ，batch size = 64 ， 
 不同 生成长度 下的 解码 吞吐（decode throughput）对比 
 单机 8 卡 H200 ，batch size = 64 ， 
 不同 生成长度 下的 解码 吞吐（decode throughput）对比 
 手搓案例 
 我们将 Ring-2.5-1T 接入到 Claude Code 中，为测试其长程软件开发能力，我们通过如下的 prompt 要求其自动开发一个微型版操作系统（TinyOS）。 
 1. 系统启动流程： 
 - 使用 GRUB 作为引导加载程序，遵循 Multiboot 标准 
 - 编写 boot.asm 汇编文件设置基本的 CPU 模式（32 位保护模式） 
 - 从汇编跳转到 main.c 的 kernel_main 函数 
 2. 核心功能实现： 
 - 屏幕输出：实现简单的字符显示功能（如清屏、打印字符串） 
 - 中断处理：设置基本的 GDT 和 IDT，处理键盘输入中断 
 - 内存管理：实现最基本的内存分页初始化 
 - 键盘支持：能够接收键盘输入并回显到屏幕 
 3. 代码结构： 
 - 提供完整的 linker.ld 链接脚本 
 - 提供 Makefile 用于编译和生成 ISO 镜像 
 - 每个关键函数都要有清晰的注释说明 
 4. 代码要求： 
 - 确保代码简洁、模块化，避免不必要的复杂性 
 - 优先实现可工作的最小功能集 
 - 为后续扩展预留接口 
 请先输出完整的代码文件列表和简要说明，然后提供每个文件的完整代码。 
 生成的所有代码必须能直接编译运行，并给出具体的编译和测试方法。 
 你需要保证可以使用 qemu 来实际运行这个操作系统。 
 Ring-2.5-1T 在 Claude Code 中运行了 2 小时 8 分钟，最终完成了上述任务，详细记录如下视频： 
 我们尝试继续让 Ring-2.5-1T 丰富 TinyOS 的功能，输入如下 prompt： 
 好的，现在你继续开发，实现好 bash 的功能，使得使用 qemu 可以登录到一个 bash 命令界面，以执行一些简单的命令，比如 ls、pwd、cat 等。 
 最终开发的 TinyOS 如下视频所示： 
 我们也将 Ring-2.5-1T 接入到个人 AI 助理 OpenClaw，帮助阅读 AI infra 文献，并用 JAVA 代码展示技术逻辑。 
 局限性与未来计划 
 这一版本模型在 token efficiency 与指令遵循方面仍存在不足，在面向更真实、更复杂任务的长程执行与实际交付能力上，也仍有较大的优化空间。我们将在后续版本中持续改进上述能力，并非常期待来自社区的使用反馈与建议。目前，Ring-2.5-1T 的训练仍在持续推进中。完整技术报告将在下一版本发布后正式公开。 
 此外，需要说明的是，上述 GAIA2 榜单评测采用的是社区广泛使用的 OpenAI function call 格式，而非原始的 ReAct 格式。相关评测配置与方案将提交至 GAIA2 的 GitHub 仓库，供社区进行更广泛、可复现的对比与评测。 
 欢迎大家访问我们的开源仓库和体验页面进行下载使用 
 🤗 Hugging Face： 
 https://huggingface.co/inclusionAI/Ring-2.5-1T 
 🤖 ModelScope ： 
 https://modelscope.cn/models/inclusionAI/Ring-2.5-1T 
 Ling Studio （ https://ling.tbox.cn/chat ） 与 ZenMux （ https://zenmux.ai/ ） 的 Ring-2.5-1T Chat 体验页和 API 服务将在近期上线。 
 本文由 Hugging Face 中文社区内容共建项目提供，稿件由社区成员投稿，经授权发布于 Hugging Face 公众号。文章内容不代表官方立场，文中介绍的产品和服务等均不构成投资建 议。了解更多请 关注公众号 
 如果你有与开源 AI、Hugging Face 相关的技术和实践分享内容，以及最新的开源 AI 项目发布，希望通过我们分享给更多 AI 从业者和开发者们，请通过下面的链接投稿与我们取得联系: 
 https://hf.link/to ugao 
 阅读原文 
 跳转微信打开
```

---

## 8. 社区供稿丨感知无界·创造有形：百灵全模态 Ming-flash-omni-2.0 焕新生活想象

- 日期: 2026-02-11 21:01
- 链接: https://mp.weixin.qq.com/s?__biz=Mzk0MDQyNTY4Mw==&mid=2247496385&idx=1&sn=ea4e8769928357c84e2c6abde9845c4f

```
百灵大模型 2026-02-11 21:01 法国 
 以下文章来源于：百灵大模型 
 百灵大模型 分享蚂蚁百灵大模型研发进展 
 百灵全模态 Ming-flash-omni-2.0发布 
 马年将至，百灵 Ming-flash-omni-2.0 正式焕新登场！在这个辞旧迎新的时刻，让我们先请出 Ming-flash-omni-2.0 为大家送上一份特别的“马年祝福”！ 
 Ming-flash-omni-2.0 速览 
 本次发布的 百灵全模态大模型 Ming-flash-omni-2.0 ，基于 Ling-2.0 （MoE 架构，100B-A6B）架构训练。相比之前发布的 Preview 版本，Ming-flash-omni-2.0 实现了全模态能力的代际跃迁，无论是在复杂的视觉理解、充满情感的语音交互，还是极具创意的图像编辑上，Ming-flash-omni-2.0 的实测表现均已跻身 开源领先 水准。 
 长期以来，多模态大模型领域存在一个难题：通用的“全模态大模型”（Omni-MLLMs）往往在特定领域的表现不如“模态专用大模型”（Specialist MLLMs）。Ming-omni 系列的研发初衷，正是为了填补这道鸿沟。从 Lite 版本到 Flash Preview，我们验证了模型规模对性能的提升作用；而从 Preview 到如今的 2.0 版本，我们通过海量数据的精细化打磨，进一步触达了性能的天花板。Ming-flash-omni-2.0 的诞生证明了：一个统一架构的全模态模型，完全可以既是博学的通才，又是特定模态的专家。 
 特色能力 
 Ming-flash-omni-2.0 兼具领先的通用泛化性能与深度的领域专长，特别是在视觉百科知识力、沉浸式语音生成及高动态图像创作领域，展现出极强的专业竞争力。 
 视觉百科：看懂万物，更懂你所见 
 Ming-flash-omni-2.0 不仅仅是看见图像，更能调动背后的专家级知识库，实现“所见即所知”。它能： 
 懂自然：精准识别花草鸟兽，从珍稀植物的品种溯源、濒危动物的特征识别，科普知识随手可得； 
 懂生活：从解析地方名菜风味到全球地标的精准匹配，满足好奇心与实用性； 
 懂专业：文物古玩精准辨识，识别年代、器型与工艺细节，成为工作中的高效助手。 
 当博学的“百科全书”叠加了极致的“视觉捕捉”，Ming-flash-omni-2.0 展现出了极强的时空语义理解能力: 
 可控语音生成：有情绪，有温度，声临其境 
 告别机械的电子音，Ming-flash-omni-2.0 让声音充满了表现力。它不仅能说话，还能根据你的指令调整情绪、语调甚至背景氛围。 
 让文字拥有温度与情绪 ：你可以通过指令控制方言、语速、情感，同时支持普通话、粤语、四川话的自然切换。 
 千人千面的声音定制 ：支持基于自然语言描述的音色定义（涵盖年龄、性别、情感质感等维度），想要特定的音色？只需一段自然语言描述即可生成对应风格的音色，或者从内置的 100+ 精品音色与经典角色音色中挑选，它都能精准还原、自然演绎。 
 全能的声音艺术家 ：Ming-flash-omni-2.0 作为业界首个将语音、音效和背景音乐生成融为一体的模型，实现了三类声学信号统一自回归 + 连续音频表征来生成，营造出声临其境的听觉体验。 
 以下展示了 Ming-flash-omni-2.0 沉浸式的语音合成效果： 
 图像创作：所想即所见，光影随心变 
 Ming-flash-omni-2.0 实现全能型图像处理能力，大幅提升生图、改图及分割的性能表现，赋予了你对画面的绝对掌控权。 
 氛围感重构 ：拒绝千篇一律的游客照。一句话，就能把平平无奇的照片变成“节日大片”或“故事感写真”，只需一句简单的指令——如烟花、海鸥、日出日落、花瓣雨、落叶纷飞、毛毛细雨或漫天飞雪，模型便能在 完美保持人物与场景特征一致性 的同时，为画面自然注入沉浸式的环境氛围。 
 “任意门”般的场景合成 ：想去阿尔卑斯滑雪？无需P图高手，模型能精准理解你的指令，将人物无缝融入全新的背景中。 
 智能的“橡皮擦” ：无论是杂乱的人群还是多余的物体，它都能精准移除，并自动补全背景细节，还原照片最纯净的美。 
 通过融合 Ming-flash-omni-2.0 的语音与图像生成能力，还可以实现“音画一体”的创作体验。所见有形，所感有声，让视觉的张力与听觉的温情在此刻深度交织。 
 技术深解：Ming-flash-omni-2.0 如何实现突破？ 
 我们整理了驱动 Ming-flash-omni-2.0 性能飞跃的核心技术细节。 
 全模态感知的强化 
 像素级细粒度感知 : 针对易混淆的图像（如珍稀动植物），我们引入了亿级高质量数据，并采用“难例挖掘”策略，通过将相似样本拼接为多图布局进行对比学习，促进模型在对比学习中学会分辨微小的特征差异。 
 音频细粒度感知增强 : 引入高质音频-文本数据，对语音的年龄、性格、风格、语速、语调、职业、情绪、方言等维度进行精细标注，强化 Ming-flash-omni-2.0 对人声和音色的感知和可控生成能力。 
 结构化知识对齐 : 通过引入知识图谱，将图像实体、音频描述与结构化的专家知识对齐，确保模型不仅“看到”，更能“懂得”。 
 视频时序建模 : 引入 Time-Interleaved VideoRoPE 机制，就像给视频帧打上了精准的时间戳，显著增强了模型对动态事件的捕捉能力。 
 泛音频统一生成框架 
 Ming-flash-omni-2.0 作为业界首个全场景音频统一生成模型，可在同一条音轨中同时生成语音（Speech）、环境音效（Audio）与音乐（Music）。针对语音、音效与音乐在频带分布及序列长度上的显著差异的难题，我们提出了异构音频信号联合建模方案： 
 低帧率/高保真连续表征 ：自研 12.5Hz 超低帧率连续语音 Tokenizer ，实现了对高频 Audio/Music 信号的高保真重构。该机制不仅降低了特征冗余，更在统一的潜在空间内实现了异构音频信号的标准化表征。 
 Patch-based 压缩与曝光偏差缓解 ：引入 Patch-by-Patch 四帧压缩策略 ，将生成序列长度进一步缩减。这一设计有效缩短了自回归建模的路径，显著缓解了超长音频生成任务中常见的曝光偏差累积问题，通过非对称的 DiT head condition 和 patch size 解决多种类型音频统一建模。 
 极低频推理优化 ：在推理阶段，模型实现了 3.1Hz 的业界极低推理帧率 。这不仅极大降低了计算开销，而且使模型在保持高音质输出的同时，具备了实时的生成速度与极致的计算效率。 
 视觉生成、编辑和分割的深度融合 
 Ming-flash-omni-2.0 首创将 生成、编辑、分割 融入单一原生模型，实现架构级深度统一的同时，模型在生成、编辑及分割的典型指标上均达领先水平，并兼顾了生成图像的视觉真实感。 
 原生单流与动态感知 ：采用单流设计，在统一 Token 空间内利用 全量注意力机制 打通三大任务，并引入基于 动作标签的平衡采样 策略，针对高动态场景（如旅拍）实现任务间深度对齐。这一融合有效消除了复杂动作生成的僵硬感，确保了人物体态的自然与画面的动态张力。 
 扩散模型强化学习鲁棒性优化 ： 针对强化学习易出现的“奖励欺骗”问题，构建 三重稳健机制。 
 1） 冷启动 ：利用确定性的“编辑式分割”任务建立模型的基础 空间认知与定位能力 ； 
 2） 统一奖励空间建模 ：集成多维度评价指标，防止模型因过度优化单一奖励而陷入 过拟合或退化解 ； 
 3） 离线分布正则化 ：通过引入约束项，确保生成内容始终锚定在真实图像分布内，大幅提升结果的视觉保真度。 
 后续规划 
 Ming-flash-omni-2.0 代表了我们在全模态模型探索上的阶段性进展，在多项核心指标上取得了突破。但与大模型普遍存在的幻觉挑战类似，当前版本在知识准确性、特定 IP 内容的识别与生成，以及英文音色克隆的逼真度方面仍有提升空间。此外，指令遵循能力也需进一步优化，以更好地支持复杂任务的精准执行。未来我们将持续优化 Ming-Omni 系列，向全模态智能的深水区挺进，在多任务融合中实现新的智能涌现。 
 开源相关信息 
 Ming-flash-omni-2.0 模型权重和推理代码已开源： 
 🤗 Hugging Face ： 
 https://huggingface.co/inclusionAI/Ming-flash-omni-2.0 
 🤖 ModelScope ： 
 https://www.modelscope.cn/models/inclusionAI/Ming-flash-omni-2.0 
 📦 GitH ub ： 
 https://github.com/inclusionAI/Ming 
 本文由 Hugging Face 中文社区内容共建项目提供，稿件由社区成员投稿，经授权发布于 Hugging Face 公众号。文章内容不代表官方立场，文中介绍的产品和服务等均不构成投资建 议。了解更多请 关注公众号 
 如果你有与开源 AI、Hugging Face 相关的技术和实践分享内容，以及最新的开源 AI 项目发布，希望通过我们分享给更多 AI 从业者和开发者们，请通过下面的链接投稿与我们取得联系: 
 https://hf.link/to ugao 
 阅读原文 
 跳转微信打开
```

---

## 9. 社区供稿丨MiniCPM-o 4.5开源：「眼耳口」并用，模型交互从「一问一答」变为「即时自由对话」

- 日期: 2026-02-06 12:03
- 链接: https://mp.weixin.qq.com/s?__biz=Mzk0MDQyNTY4Mw==&mid=2247496380&idx=1&sn=05e1ea252681a9588a9dd315455f2e19

```
OpenBMB 开源社区 2026-02-06 12:03 法国 
 面壁智能开源新一代全模态旗舰模型 MiniCPM-o 4.5 
 今天，我们开源了新一代全模态旗舰模型 MiniCPM-o 4.5 ！作为原生全双工的全模态大模型，MiniCPM-o 4.5 让人机交互再上新台阶——通过 「边看、边听、主动说」 的全模态能力， 让 AI 告别死板的“对讲机”回合制交互 ， 成为行业 首个「 即时 自由对话」的大模型 ， 感知不中断、对话不死板、提醒无需问 。同时仅依靠 9B 的小身材，将行业高刷视觉理解、端到端语音对话等最先进的模型能力「All in One」，让 AI 真正开启类人感知与沟通交互的新时代。 
 MiniCPM-o 4.5 已在 GitHub、Hugging Face 等平台开源，结合面壁自研的行业首个开源的流式全模态模型高效端侧推理框架 llama.cpp-omni ，让模型部署更加简单、稳定、高效。此外，基于统一系统软件栈众智 FlagOS 的跨平台能力，MiniCPM-o 4.5 在天数智芯、华为昇腾、平头哥、海光、沐曦等 6 款芯片上均获得端到端推理性能提升。我们也为开发者提供了免部署的线上体验版本，欢迎大家一起探索 MiniCPM-o 4.5 的更多能力新玩法、应用新场景。 
 ➤ MiniCPM-o 4.5 亮点一览 
 再次刷新端侧全模态能力上限 ：全模态、视觉理解、文档解析、语音理解和生成、声音克隆能力达到领先水平，以及最佳推理效率和最低推理开销。 
 开启全模态全时感知： 视觉、音频、文本不同模态输入输出不阻塞，即使在模型输出时，也在「看」和「听」，不丢失任何信息。 
 从“回合制”交互升级为“即时自由对话”： 通过随时保持对外感知，模型可以以最合适的时机、最恰当的内容实时回复。 
 语音自然、情感饱满： 显著提升全模态端到端语音生成的音色、拟人度、声音表现力，声音克隆支持自由定制音色，且长语音合成更加稳定。 
 原生全双工技术首创 ： 
 采用端到端的全模态架构，结合全双工多模态实时流机制、主动交互机制、可配置语音建模设计，造就了 MiniCPM-o 4.5 与人一样自然的交互能力与体验。 
 ➤ 模型链接 
 GitHub： 
 🔗 https:// github.com/ OpenBMB/MiniCPM-o 
 HuggingFace： 
 🔗 https://huggingface.co/openbmb/MiniCPM-o-4_5 
 ModelScope： 
 🔗 https://www.modelscope.cn/models/OpenBMB/MiniCPM-o-4_5 
 魔乐： 
 🔗 https://modelers.cn/models/OpenBMB/MiniCPM-o-4_5Gitcode： 
 🔗 https://ai.gitcode.com/OpenBMB/MiniCPM-o-4_5 
 体验链接-全双工全模态模式： 
 🔗 https://huggingface.co/spaces/openbmb/minicpm-omni 
 体验链接-图文对话模式： 
 🔗 http://211.93.21.133:18121/ 
 最强端侧全模态「看听说」全面领先 
 持续刷新能力上限 
 沿袭面壁小钢炮一贯的“高密度”特点，MiniCPM-o 4.5 仅靠 9B 参数，在全模态、视觉理解、文档解析、语音理解和生成、声音克隆等方方面面，均做到了全模态模型 SOTA 水准！ 
 左滑查看更多内容 
 MiniCPM-o 4.5 不仅在模型能力密度上再上台阶，也一直致力于追求大模型的极致「能效比」，通过更低的显存占用、更快的响应速度，确保在提供 SOTA 级全模态表现的同时，实现了最佳的推理效率和最低的推理开销。 
 全双工「眼耳口」并用 
 告别「对讲机式」死板交互 
 去年，MiniCPM-o 2.6 让端侧大模型实现了持续看、实时听、自然说的能力。今年，我们再次带来了革命性升级——让全模态模型具备「边看、边听、主动说」的全双工与主动交互能力。 
 传统的单工模型犹如“对讲机”一般，当模型回答时，无法接收外部信息，只能「说完再看、说完再听」，犹如人在说话时，捂住眼睛和耳朵，无法达到和人一样正常交互体感的同时，也极大的可能丢失最为关键的信息。 
 “眼观六路、耳听八方” 
 MiniCPM-o 4.5 实现「边看、边听、主动说」，在任何情况下都随时保持「看」和「听」的感知 。结合让大模型对高清视频的理解能力，以及灵敏、机智的辨音能力，让大模型不放过任何的关键细节，也不会被冗杂的信息干扰。 
 “随机应变、伺机而动” 
 相较于大多数多模态模型仍依靠 VAD （Voice Activity Detection，语音活动检测） 等外部工具及工程化方式实现控制说话， MiniCPM-o 4.5 原生全双工模型 的另一项优势是在保持感知的同时， 可以自身 根据 环境的动态变化实时反应，以最合适的时机、最恰当的内容回复 ，让大模型对于 信息的感知与传递永远不会慢半拍 。 
 自然说 语音全新升级 
 带来情绪饱满、超拟人听感 
 实现和人一样的感知与交互能力，带来的不仅仅是持续的「看」和「听」，还需要更加稳定、自然、情绪饱满的「说」。 
 MiniCPM-o 4.5 通过新的模型设计和数据方法，让语音生成的音色、拟人度、声音表现力等方面获得了全方位的提升，在音频输出过程中，会自动选择最为合适的语气、音色，带来如真人般的声音效果。 
 值得一提的是，MiniCPM-o 4.5 也极大地解决了长语音合成中音色不统一、语气不自然、效果不稳定难题，超长语音生成依旧保持稳定。 
 在声音克隆上，MiniCPM-o 4.5 提供了更多的声音选择，可以基于几秒的声音样本克隆定制新音色，并基于克隆音色进行角色扮演的语音对话。 
 模型架构介绍 
 MiniCPM-o 4.5 采用了端到端的全模态架构，并创新的加入了全双工多模态实时流机制、主动交互机制、可配置语音建模设计，造就了 MiniCPM-o 4.5 与人一样自然的交互能力与体验。 
 端到端全模态架构。 各模态的编码器/解码器与大语言模型通过稠密特征以端到端的方式进行紧密连接。这种设计实现了更好的信息流转与控制，有助于在训练过程中充分挖掘和利用丰富的多模态知识。 
 全双工多模态实时流机制。 
 MiniCPM-o 4.5 将离线模态编码器/解码器转化为支持流式输入/输出的在线全双工版本。语音解码器采用文本与语音 token 交错建模的方式，支持全双工语音生成（即与新输入实时同步），同时也提升了长语音（如超过 1 分钟）生成的稳定性。 
 时分复用： MiniCPM-o 4.5 在毫秒级时间线上同步所有输入和输出流 ，并利用时分复用机制在语言模型主干中进行统一建模。该机制将并行的全模态流划分为微小周期性时间片内的顺序信息组，从而实现高效的全模态流式处理。 
 主动交互机制。 语言模型模块会持续监控输入的视频和音频流，并以 1Hz 的频率自动决策是否发言。这种高频决策能力结合全双工特性，是实现主动提醒、主动评论等“主动交互”能力的关键。 
 可配置语音建模设计 。 MiniCPM-o 4.5 延续了 MiniCPM-o 2.6 的多模态系统提示词设计，同时包含文本系统提示词和音频系统提示词（用于指定音色）。这使得模型在推理阶段能够通过简单的参考音频实现声音克隆和角色扮演。 
 模型如何使用 
 MiniCPM-o 4.5 可通过多种方式轻松部署和使用： 
 (1) 通过 llama.cpp 和 Ollama 在本地设备上实现高效的 CPU 推理； 
 (2) 提供 16 种不同大小的 int4 和 GGUF 量化模型； 
 (3) 通过 vLLM 和 SGLang 实现高吞吐、内存高效的推理； 
 (4)通过统一系统软件栈众智 FlagOS实现 MiniCPM-o 4.5 多芯片后端支持。用户可基于众智 FlagOS 公开镜像 “开箱即用”多芯版 MiniCPM-o 4.5，或者基于 vLLM-plugin-FL 启动多芯版 MiniCPM-o 4.5； 
 (5) 使用 LLaMA-Factory 对新领域和任务进行微调； 
 (6) 提供在线网页演示。我们还同步推出了高性能的 llama.cpp-omni 推理框架及配套的 WebRTC Demo，可在 PC 等本地设备上实现全双工多模态实时流体验。 
 ➤ 体验链接 
 🔗 https://huggingface.co/spaces/openbmb/minicpm-omni 
 本文由 Hugging Face 中文社区内容共建项目提供，稿件由社区成员投稿，经授权发布于 Hugging Face 公众号。文章内容不代表官方立场，文中介绍的产品和服务等均不构成投资建 议。了解更多请 关注公众号 
 如果你有与开源 AI、Hugging Face 相关的技术和实践分享内容，以及最新的开源 AI 项目发布，希望通过我们分享给更多 AI 从业者和开发者们，请通过下面的链接投稿与我们取得联系: 
 https://hf.link/to ugao 
 阅读原文 
 跳转微信打开
```

---

## 10. 社区供稿丨迈向AI4S 2.0，上海AI实验室开源书生万亿科学大模型Intern-S1-Pro

- 日期: 2026-02-05 12:03
- 链接: https://mp.weixin.qq.com/s?__biz=Mzk0MDQyNTY4Mw==&mid=2247496375&idx=1&sn=89e0b8d1518178225d64044f93f85d8b

```
Shanghai AI Lab 2026-02-05 12:03 法国 
 上海AI实验室开源书生万亿科学大模型Intern-S1-Pro 
 2月4日，上海人工智能实验室开源基于 “通专融合”技术架构SAGE 打造的 万亿参数科学多模态大模型 Intern-S1 - Pro ，为AI4S从“工具革命”的 1.0阶段迈向以“革命的工具”驱动科学发现的2.0时代，提供创新的系统性开源基座。 
 作为当前全球开源社区中参数规模最大的科学多模态模型，Intern-S1-Pro的核心科学能力实现了质的跃升，高难度综合学科评测稳居AI4S领域国际领先水平，复杂数理逻辑推理能力达奥赛金牌水平，面向真实科研流程的智能体能力位居开源模型第一梯队。 
 此次发布的Intern-S1-Pro是通过SAGE实现 “可深度专业化通用模型” 的关键实践。该模型基于混合专家架构（MoE），共拥有512个专家，总参数达1T，每次调用仅激活8个专家、22B参数。其通用能力和科学能力协同演进，并在底层架构实现了两大核心突破：在SAGE的基础模型层，通过引入 傅里叶位置编码 ① 并 重构时序编码器 ，赋予模型统一理解从微观生命信号到宏观宇宙波动的“物理直觉”；通过高效 路由机制 ，系统攻克了训练万亿参数MoE模型在稳定性与算力效率上的瓶颈，为超大规模模型的训练提供了关键的工程基础。 
 与此同时，Intern-S1-Pro验证了从原创模型架构到国产算力基座自主技术的 完整 链路，为构建开放共享的AGI4S基础设施奠定了坚实底座。通过开源开放， Intern-S1-Pro 旨在降低全球科研门槛，与学术界和产业界共同推动以通用人工智能驱动科学发现的范式革命。 
 在线体验链接： 
 https://chat.intern-ai.org.cn/ 
 GitHub链接： 
 https://github.com/InternLM/Intern-S1 
 HuggingFace链接： 
 https://huggingface.co/internlm/Intern-S1-Pro 
 ModelScope链接： 
 https://www.modelscope.cn/models/Shanghai_AI_Laboratory/Intern-S1-Pro 
 Intern-S1-Pro在评测基准中的表现：通用能力表现出色，科学能力达国际领先水平。 
 创新底层架构： 
 突破万亿参数科学模型边界 
 上海人工智能实验室主任、首席科学家周伯文提出： 可深度专业化通用模型（Specializable Generalist）是实现AGI的可行路径 ，其关键挑战在于：专家化模型在训练过程中需要低成本、能规模化的密集反馈；能够持续不断地学习与主动探索，并具备为同一个问题提供多视角、多种解决方案的能力；并能引入对物理世界规律的考量，兼顾多项差异化能力的学习效率与性能。 
 Intern-S1-Pro通过多项SAGE 基础模型层 的技术创新，拓宽了模型应用边界、提升了超大规模训练可行性，推进了可深度专业化通用模型的探索。 
 为构建能更深层次理解物理世界规律的科学大模型，研究团队引入了 傅里叶位置编码（FoPE） 并 重构时序编码器 。 FoPE为 AI 赋予双重视角 ：既能像看“粒子”一样捕捉 文字之间的相对距离 ，又能像分析“波”一样把握 科学信号的 整体规律与频率。科学数据与语言的差异还体现在多尺度上，基于能自动适应数据密度的时序编码器，模型首次能统一处理从寥寥数个到百万级采样的各类信号，支持的分析对象从天文、地理直接拓展至生理信号、生物声学等领域，从而实现感知能力的重大跃迁。 
 为了高效训练承载这些能力的万亿参数超大规模模型，研究团队革新了其内部的“路由机制”。传统方法存在训练低效和算力浪费两大痛点。新技术通过 “ 路由稠密估计 ” ，让模型在高效运行的同时能进行更充分的学习，提升了稳定性；进而通过 “ 分组路由 ”策略，像智能交通系统一样使海量计算芯片实现负载均衡，避免了资源闲置。通过算法与系统的协同创新，同时攻克了超大规模模型训练在“学习效率”和“资源调度”上的核心瓶颈，为高效、稳健地训练下一代万亿参数模型提供了关键基础。 
 通过上述底层架构的创新，Intern-S1-Pro不仅在规模上刷新了科学多模态模型的参数规模上限，也为SAGE架构所提出的“通用能力与专业能力协同演进”提供了可落地的实现路径。 
 科学能力再进化，通用能力协同演进 
 得益于创新的底层架构设计与万亿参数超大规模训练策略，Intern-S1-Pro的科学能力进一步升级。 
 在国际数学奥林匹克IMO-Answer-Bench和国际物理奥林匹克IPhO2025两大权威基准测试中，Intern-S1-Pro均展现出竞赛级别的解题能力。 
 在AI4S关键垂类领域，Intern-S1-Pro成功构建了一个跨越化学、材料、生命、地球、物理五大核心学科的全谱系能力矩阵，涵盖100多个专业子任务，不仅在Mol-Instruction、Biology-Instruction等单学科垂类评测中表现优异，更在SciReasoner等高难度的综合学科评测基准中，取得了与闭源商业大模型及垂类SOTA模型相当，甚至更优的成绩， 稳居AI4S领域的第一梯队 。 
 在基础理解维度，Intern-S1-Pro基于高精度多模态感知能力，能够精准解析复杂的分子结构图及各类实验图表，深入到逻辑推理层面 ，Intern-S1-Pro能够处理高阶科学问答，如反应条件推断、理化性质预测，精准捕捉数据背后的因果规律等。随着理解与推理能力的持续增强，Intern-S1-Pro的能力边界不断向真实科研场景延伸，其应用范围从微观层面的化学逆合成、蛋白质序列生成，拓展至宏观尺度的遥感图像分析等复杂任务。通过XLRS-Bench等真实科研场景评测，模型展现出从“解题”迈向“解决问题”的科研生产力价值，为前沿科学探索提供了坚实支撑。 
 同时，借助通专融合技术路线，Intern-S1-Pro在通用能力与专业科学能力上实现协同进阶：在图文跨模态理解、科学图表逻辑推理、多场景视觉感知，以及高质量自然语言生成和复杂指令精准遵循等核心维度， Intern-S1-Pro均 稳居开源模型阵营第一梯队 ，展现出扎实而全面的综合实力 。 
 通过通专融合的训练策略，Intern-S1-Pro不仅补齐了传统前沿模型在专业推理上的短板，还实现了多模态与文本通用能力的均衡发展，真正将通用能力与专业科学能力的协同演进落到实处，为科研场景下复杂问题的理解、推理与应用提供了可靠支撑。 
 在智能体能力方面，Intern-S1-Pro实现了从“静态任务规划”到“动态环境交互”的跨越式进阶。在以动态环境与复杂交互为核心的Tau-2评测中达到了国际一流水平，为赋能复杂科学智能体打下了坚实基础。 
 筑牢 “算力-算法”一体化基座 
 在规模、性能提升的同时，Intern-S1-Pro构建了原创的 “算力-算法”一体化基座 。模型从架构设计之初，便与昇腾计算生态确立联合研发路线，实现了从最底层的算子、编译优化到上层的训练、推理框架的深度全栈适配。 
 研发团队攻克了大规模训练中精度对齐、超长序列强化学习稳定性、硬件性能极致释放等一系列核心技术难题，基于XTuner V1训练框架的精细优化与LMDeploy推理引擎的高效部署，结合先进的内存管理与并行策略，确保了万亿参数模型训练的高效与稳定。通过创新的全异步强化学习框架等技术的应用，大幅提升了训练效率，降低了研发成本与门槛，此外，Intern-S1-Pro还与沐曦联合研发利用模型加速算子适配，为开放共享、面向未来的AGI4S基础设施奠定了坚实基础。 
 高质量开源赋能创新生态 
 自2023年书生大模型首次发布以来，上海AI实验室已逐步构建起丰富的书生大模型家族，包括 科学多模态模型Intern-S1 、 大语言模型书生·浦语InternLM 、 多模态模型书生·万象InternVL 、 强推理模型书生·思客InternThinker 等。同时首创并开源了面向大模型研发与应用的全链路开源工具体系，覆盖数据处理、预训练、微调、部署、评测与应用等关键环节，包含训练框架XTuner、部署推理框架LMDeploy、 评测框架OpenCompass 、 高效文档解析工具MinerU ，以及思索式AI搜索应用MindSearch等在内的核心工具已全面开源，形成覆盖数十万开发者参与的活跃开源社区。 
 自发布以来，Intern-S1多次登顶HuggingFace全球多模态榜单，累计下载超41万次，并获得近200家科研机构和企业的合作申请。其卓越的跨模态科学理解能力不仅为科研提供了高效工具，也通过开源降低了全球科研团队迈入AGI for Science的门槛。未来，在研究范式创新及模型能力提升的基础上，上海AI实验室将推进Intern-S1及其全链条工具体系持续开源，支持免费商用，同时提供线上开放服务，与全球合作伙伴共建更加开放、高效的科学AI生态。 
 案例展示 
 本文由 Hugging Face 中文社区内容共建项目提供，稿件由社区成员投稿，经授权发布于 Hugging Face 公众号。文章内容不代表官方立场，文中介绍的产品和服务等均不构成投资建 议。了解更多请 关注公众号 
 如果你有与开源 AI、Hugging Face 相关的技术和实践分享内容，以及最新的开源 AI 项目发布，希望通过我们分享给更多 AI 从业者和开发者们，请通过下面的链接投稿与我们取得联系: 
 https://hf.link/to ugao 
 阅读原文 
 跳转微信打开
```

---
