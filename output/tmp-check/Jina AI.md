# Jina AI

> 分类: AI专题
> URL: https://wechat2rss.bestblogs.dev/feed/ff2c5468828ebe7236afd6c1d128e219774487c2.xml
> 抓取: 10 篇

---

## 1. 2026 年做搜索就是做 Agent Memory

- 日期: 2026-04-22 14:30
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyODIxMjczMA==&mid=2247503411&idx=1&sn=3a7e276345f92af2d03370fe1e5259ff

```
原创 Jina AI 2026-04-22 14:30 新加坡 
 “大家今天还用 grep+md 做记忆召回，说明我们几年来语义搜索就没做好” 
 4 月 18 日，Elastic 中国 AI 搜索技术大会在北京召开。以下内容整理自 Elastic 全球副总裁肖涵，原 Jina AI 创始人兼 CEO 在会上的演讲。肖涵讲述了 AI 搜索的发展历程以及为什么说在 2026 年做 AI 搜索基本就是在做智能体记忆 ( Agent Memory )。本文以第一人称呈现。 
 欢迎大家来到 Elastic 第一次在中国办这么大的技术研讨会。我是肖涵，北京人，大家可以先放松一下，欢迎来到我的家乡。 
 先简单介绍一下自己， 以及我和 Elastic、尤其是和搜索的一些渊源，也帮大家回忆一下搜索这些年的发展。 
 我最早接触搜索是 2009 年，在 惠普实验室（HP Labs） 实习，拿 Lucene 做分词，做信息抽取。那时候叫 IE，不是 Internet Explorer，是 Information Extraction。还做了一些 LDA、主题模型这类东西。2009 年贝叶斯那套非常火，跟今天 Transformer 的地位差不多。 
 后来我去德国读博，做的就是贝叶斯机器学习。等我 2014、2015 年博士毕业出来，发现贝叶斯没什么人搞了，大家都在用 TensorFlow 做深度学习。又过了几年，Transformer 出来，把深度学习的架构统一了。 
 2018 年我回国，在深圳腾讯 AI Lab 做了两年搜索，做的是微信"搜一搜"背后的多模态和中文搜索。2020 年疫情的时候出来创业，成立了 Jina AI，专门做多模态搜索。 
 当时我立的 flag 是"颠覆 Elastic"。结果绕了一圈，2025 年 10 月被 Elastic 收购了。现在我在 Elastic 担任全球副总裁，专门负责 AI，主要是搜索底座模型的研发。 
 今天要讲的主题是智能体记忆。 
 先问一下在座有谁用过小龙虾？举个手。嗯，量不小，一看就是在中国，大家都很爱学习。那用过超过一个月的？少一些。超过两个月的？更少了。 
 那我相信大家都遇到过一个问题：用这类智能体，用一两次是尝鲜，但当你用了一周、两周之后，你是希望它越来越聪明的，随着你用它越久、它越记得住你的事。可惜目前这套记忆机制很不完善。 
 智 能体记 忆的痛点 
 讲一个两周前我自己的真实例子。 
 我跟小龙虾说："我之前做了一个 911 的图表，你发给我一下。"911 是保时捷的一款跑车。然后它(我给它起名叫"小牛马")跟我说没找到，问我 911 是指恐袭还是别的东西。 
 我当时第一反应是模型降智了，或者被 fallback 到什么垃圾模型上去了。我特地查了一下，发现跑的是 Claude Opus 4.6，当时最好的模型。不是模型的问题。 
 那我就开始 debug。我问它：你刚刚用的什么搜索？怎么判断你记忆里没有这件事的？ 
 它说它用了 Grep 做关键词匹配，又用 Memory Search 做向量语义搜索，把 Memory Markdown、Session Log、文件系统都扫了一遍。 
 方法上看着没问题。那接下来 debug 的点就是： 你到底用的什么 Query？ 
 它告诉我，第一次的 Query 是 911 chart graph visualization 。它不知道 911 是什么，直接把我的中文翻译成英文去搜了，发生了一次 multilingual query 的转译。第二次更离谱，Query 变成了 September 11th chart visualization Twin Towers attack ，直接搜成恐袭了。 
 这两个 Query，我的记忆库里当然都找不到。 
 后来我换了一个说法，"帮我把 992.2 的图表发给我"。992.2 是 911 这代车型的代号。一下就找到了，3 月 29 号做的。 
 所以就算你记忆系统整条链路都对， 只要第一步 Query 构造错了，整个检索就是废的 。而且这种事情从我 1 月份开始用到今天，一直在发生。 
 记忆，是今天 Agent 的一个很大的痛点。 
 回顾搜索的发展脉络 
 我们回顾一下，搜索是怎么走到"做智能体记忆"这一步的。 
 2009 年刚做搜索的时候，关键词就是 BM25、TF-IDF、倒排索引，Lucene 背后那套东西。 
 2015 年之后， 向量搜索逐渐进入视野，最早是 Spotify 搞过一个，名字我都快忘了，然后是 Facebook 的 Faiss，Milvus，Elastic，这是第一批把 Vector Search 做出来的。但大家很快发现向量搜索也有问题：速度是一个，过度召回是另一个。向量搜索有个毛病，就是哪怕 Query 和文档完全不相关，只要分数差不多它就召回了。关键词搜索会零召回，向量搜索太柔，语义上都太柔化。所以后来大家把两者结合，做混合搜索。 
 2018 年 Transformer 统一了深度学习架构，BERT 成为把文本编码成向量的标配。 
 2022 年 11 月 ChatGPT 发布，RAG 起来，搜索和生成越走越近。我 2022 年写过一篇小随笔， 搜索是过拟合的生成，生成是欠拟合的搜索 。 它们 俩其实是对偶的。 
 2025 年还有一个时间点。春节前正月初一，DeepSeek 发布了 R1，非常火。它那套 reasoning 加 test-time compute 的范式让大家意识到，搜索可以边搜边 reasoning，再不断搜，最后生成一份很长的报告， 这就是 Deep Research 。2、3 月份 Google、OpenAI、Perplexity 都在做，包括后来做得比较好的 MiroMind。 
 2026 年呢？自从 OpenCloud 发布之后，大家对 Agent 的期待变了。不再是生成一份报告就结束，而是希望我一旦启动这个 Agent，它能连续干三四个小时，没人管、没人介入，它自己在那跑。 
 Jina AI by Elastic 搜索底座三件套 
 Jina AI 从 2020 年成立到现在六年，做的事情一句话讲完： 我们在做搜索的底座 。我们在观察这条进化路线上哪些东西是不变的。最后沉淀下来三套模型，Embedding、Reranker、还有一个 Reader (或者叫 Small Language Model)。 
 Embedding 大家都知道，就是向量，把文本或者图片转化成向量，然后用 cosine 余弦距离去匹配。 
 V1 ：默默无闻。 
 V2 ：2023 年 10 月发布，在海外引起了比较大的轰动，因为当时它是第一个开源的、支持 8K 上下文的模型，你能一次编码 8000 个 tokens，是第一家做开源长文本向量模型的，当时都是英语。之后我们还有很多双语版本。 
 V3 ：我们把所有双语版本都砍掉统一，重新训练了一个多语言的 embedding 模型。到现在仍然非常好用，在 Hugging Face 上月下载量大概在 500 万。 
 V4 ：2025 年发布的一个多模态 embedding 模型，可以同时编码图片和文本。有人说多模态模型 CLIP（OpenAI 的 CLIP）2022 年就搞了，你 2025 年才搞一个多模态的模型？其实它俩不一样。CLIP 用的是对齐训练，而 V4 的多模态是一个真正的多模态，它把图片拆成小的 patch，和语言一起放到一个大的语言编码器中编译成向量，而不是像 CLIP 那样有一个图片模态、一个文本模态，然后两个模态之间对齐。 
 V5 ：我们今年在加入 Elastic 之后，和 Elastic 一起研发的向量模型。V5 的性能和大小非常好。我们发布了两个版本：一个是 V5 text Nano，只有 2.39 亿参数；一个是 V5 Small，6.77 亿参数。相对于 V4 的大小（38 亿），小了很多。当然 38 亿对于大语言模型来说只是非常小的 toy example，但对于搜索任务我们要求的是快，在快的基础上做到精准。v5 的特点就是参数小，但性能强。 
 可以看到即便我们现在用更小的模型，其实可以达到更高的性能。V5 目前是文本领域做多语言搜索能够做到最好的。可以看到它是一个 Frontier model（前沿模型）。 
 放到 Pareto Frontier（帕累托前沿） 上看，横轴是参数量，纵轴是任务分数，越靠左上越好，V5 目前在最左上那个角上。它是文本领域多语言搜索目前能做到最好的前沿模型。这个模型已经被 SIGIR 2026 录取了。 
 另一个我们做的是 Reranker。重排器有些人不太理解：我都有 Embedding 做语义搜索了，为什么还要 Reranker？你一次排好不就完了？ 
 Jina Reranker v3: 全新“列式”重排器，0.6B参数刷新文档检索SOTA 
 原因是搜索是一个多层级联的 Pipeline。到最后一步，我们希望更细致地挖掘 Query 和候选文档之间字和字级别的相似度，也就是 token level 的语义匹配。Embedding 是把整篇文章压缩成一个向量，压缩过程必然有损失；Reranker 保留了每个 token 上的向量，因此可以把 Query 的每个 token 和 Document 的每个 token 两两对比。它的计算量比 Embedding 大，但粒度也更细。 
 Jina Reranker V3 是第一个真正意义上的长文本重排器 ， 支持 131K 上下文 ，这篇工作获得了 AAAI 2026 FrontierIR Workshop Best Paper。除此之外我们还有一个 m0 版本，做多模态重排。 
 Jina Reader 相信很多人在用 Agent 的时候都碰过。对很多人来说，Reader 甚至比我们的模型更出名。这个今天下午 Reader 的作者会专门上台讲，我就按下不表。Reader 为什么是永远的神，YYDS。 
 长时程任务与智能体记忆 
 回到智能体搜索、长任务这件事。 刚才说了 Deep Research 是 2025 年的一个重点，它就是一个 Loop。 Agent 就是一个 Loop，在三个状态之间循环：Search、Read、Reason。 
 2026 年今天讨论最多的、你去问智谱、MiniMax 这些厂商，PR 稿里必提的一个词就是：他们的模型如何支持 long-horizon task。长时程任务，就是 Agent 能自主运行多长时间，三四小时、三四天没人管它还能接着干。有个叫 METR 的 Benchmark 专门衡量每一个大模型放在一个环境中自主解决任务的最大时间长度。目前大约是 4 到 5 个小时，这个趋势在不断上升。 
 你让一个 agent 工作 4 个小时，中间它要搜索几百次、读几百个文档、在失败路径上回退几十次。这些经历不可能全部塞进 context window。它必须有一个地方去存、去查、去更新。 
 逻辑就很清楚了：当 Agent 的目标变成长时程任务， 持久记忆就不再是可选项，是命门 。 
 记忆该如何表征？ 
 这就引出了很多问题。最基本的问题就是：记忆该如何表征（representation）？ 
 很多人忽视了 在机器学习里最大的一个问题，其实不是方法，而是表征。 机器学习的顶会之一 ICLR 的全称就是 International Conference on Learning Representations，表征学习国际会议。顶会以"表征"命名，你就知道这个概念在整个 AI 领域的位置。 
 我们用了很多年才发现，BERT 是对语义的一个非常好的表达，它给"一段文本应该长什么样"这件事找到了一个好的 representation。当表征就位。Vector Database 才成立。向量数据库存的就是这种表征。 
 所以当我们要做智能体记忆，第一个问题不是"用什么数据库"，而是：记忆的 representation 到底是什么? 基于这种 representation，我该怎么去做 CRUD？ 
 一条聊天记录，一个事实三元组，一张知识图谱？还是一段向量，一个时间戳+事件对，还是模型权重本身？ 不同的答案，会催生完全不同的系统。这也是今天智能体记忆领域最混乱的地方，大家在不同的表征上各自开工，谁也说服不了谁。 
 而且即便选定了表征，还有三个问题要回答。 
 第一：基于这种表征。怎么做 CRUD，这是做数据库的人熟悉的。第二，如何在不破坏对话效率的前提下，把知识从对话里抽出来变成可检索的资产。这件事要难得多，因为对话是实时的，提取是有成本的，抽多了慢，抽少了漏。第三，也是我自己最在意的。记忆能不能跨模型迁移? 
 我今天用智谱，明天我不粉了，变黑粉了，投奔 MiniMax，我希望我的记忆能搬过去照常运行。所以记忆应该和上层模型解耦。 
 我们今天从生物学的角度强行关联一下，看一下人是怎么完成记忆的。大家知道这是什么吗？这是刀盾狗（Doge），现在非常火的一个生物。 
 人脑的记忆是分层的。 当一个新概念进来，先有视觉输入，前额叶皮层判断值不值得记，海马体负责编入，睡眠会强化记忆，最后它变成一种长时程的技能，重新烧录到新皮层。 
 我们可以强行做一个映射。 我说两次"强行"，是因为 我本人并不太赞成把人脑的东西硬搬到 AI 上 ，碳基和硅基的运行方式可以完全不一样。但如果强行对应：海马体对应 RAG 的实时检索，新皮层对应微调或预训练模型，前额叶就是当前的 Context Window。 
 什么 时候该忘？ 选择性遗忘 
 讲智能体记忆还有一个特别重要的问题： 什么时候该忘？ 
 举个例子，我第一次用小龙虾的时候，把我六年创业的事一口气全喂给它。结果它经常把我六年前想过、早就放弃的一个事情拿出来问我。但人是会变的，有些事我忘了，有些事我不做了。 
 这个问题其实 Andrej Karpathy 有一段很精准的描述。他说： 现在我们看到的 agent 系统都有一个最致命的问题，就是它不会选择性遗忘。 
 如果系统不做选择性遗忘，最后一定是乱的。大脑不遗忘会超负荷；Agent 不遗忘，也会被自己的历史拖垮。 
 目前 Agent 记忆有几个缺陷：一是遗漏，就是 911 那个例子；二是失真，也就是幻觉( hallucination) ；三是幻觉继承。 
 这时候会有一个非常有意思的事情： 冷启动悖论 。反而是当你用一个新模型或新 agent 的时候，感觉会非常好，因为你知道这是一个全新的 agent，对它的期待非常低，所以用起来还挺顺手。而当你使用时间越来越长的时候，你期待这个 agent 变得越来越好，但它并没有，因为它的记忆体设计得非常差。这就导致它的用户留存时间会非常短， 用户对 AI 的信任被长期蚕食。整个行业的节奏被记忆这件事拖住。 
 市面上智能体记忆产品的分类 
 我梳理了一下， 目前做智能体记忆的产品，开源加闭源至少有十几家。 再加上老牌数据库公司 PingCAP(做 mem9)、Milvus 也在做，以及平台内置的方案：ChatGPT 的用户记忆、Claude.ai 的知识库、Claude Code 和 Codex 的文件系统。 
 这么多产品，怎么区分它们？我用一句话概括： Source of Truth 在哪？ 这是区分所有记忆产品的第一性原则。沿着这个原则，可以分成三大类： 
 第一类是数据库派 ，向量数据库、SQL、Key-Value 存储。对话经过 LLM 抽取 facts，存进向量库或图谱，检索时注入上下文。 结构化程度高，查询效率好，但"一条记忆应该长什么样"这件事由 schema 锁死，灵活性有限。 
 第二类是文件派 ，Markdown、纯文本。Agent 读文件、工作、写回文件、不断累积。优势是透明可编辑、可版本化，缺陷是文件会膨胀，需要 intelligent forgetting。代表是小龙虾、MemSearch。 
 第三类是模型派 ，真相就是大模型权重或上下文本身。模型自决定记什么、忘什么、整合什么。优势是零配置、自适应，缺陷是完全黑盒、不可审计。代表是 Letta、ChatGPT。 
 我们刚才看到三大类别，目前所有记忆体基本可以按这三类划分。当然还有一些结构化存储、扁平化存储、主动管理和被动管理，这可以从另一个坐标轴对所有产品进行分类。 
 行业共识：主流的记忆工作流 
 虽然流派不同，但主流工作流有高度共识，我稍微总结了一下，我们今天看到的大部分智能体记忆框架基本上都 follow 这个工作流： 
 从聊天记录中，通过大模型提取事实或记忆结构 
 将这些记忆结构 ： 
 要么转化成 向量 
 要么转化成 知识图谱 
 要么用一些 时序数据库 （时序非常重要，因为就像我刚才说的，你需要选择性遗忘） 
 基于时序数据库、知识图谱和向量库做混合检索 
 检索完之后你还无法直接呈现到上下文中 ，要解决两个问题： 
 冲突 ：当检测出两个记忆相互矛盾的时候，该怎么解决？ 
 随时间的衰减 ： 旧记忆权重怎么降？ 
 大部分主流框架基本 follow 这个设计理念。当然并不是每一个框架都采用所有技术，有些只选择做几个，有些则全链都做。 
 小龙虾记 忆结构详解 
 既然现场这么多人用过小龙虾，我们具体拆一下它的结构。 它是典型的文件派。 
 它的真相源是一个 memory 文件夹，里面按天组织 Markdown 日记。另外有一份 memory.md 主文件,存长期记忆，包括用户画像；还有一份 soul.md。存它自己的"灵魂画像"，也就是它对自己是谁、自己怎么做事的内部表征。 
 从这些真相源派生出两个索引：SQLite FTS5 做 BM25 关键词检索，LanceDB 做向量检索。在索引之上做混合检索，用 RRF 融合、MMR 去重、再加时间衰减。对外暴露两个接口： memory_search 和 memory_get 。 
 在此之上，它还模仿了人类的睡觉习惯：有深度睡眠、浅度睡眠、REM（Rapid Eye Movement，快速眼动）。在这三个基础上设置一套机制。 
 这些是仿生学的概念，总体来说它设置了一套机制，能保证不是每一条记忆都完全被升级到长期记忆上，而是通过设置阈值、判断条件来提升一部分记忆。 
 模型派：真相在模型里 
 除了文件派，还有模型派。 这是我个人比较看好的方向。 也许到某个点，大家发现 Transformer 架构本身就把记忆问题解决了，直接 The bitter Lesson ，力大出奇迹。 
 目前已经看到这个趋势，比如千问 3.5 的 MoE 模型已经可以扩展到 1M token， 在一个 24G 显存的 GPU 上可以流畅运行。如果我的全部记忆能被压进或者直接装进 1M 窗口，那我就不需要分层设计了，直接用模型本身做召回。 
 还有一家公司是 EverMind AI，他们最近把上下文推到了 100M token，你可以直接在 KV cache 中存 100M token。他做这个事情是因为：如果不做特殊的架构处理，上下文越长召回质量越差。所以 EverMind 这家初创公司在 Attention 机制上做了特殊设计，搞了一个叫 MSA（Memory Sparse Attention，记忆稀疏注意力） 的东西，保证它在超长 100M 上仍然有非常好的召回效果。 
 Benchmark 
 学术圈对智能体记忆已经做了不少 benchmark，我简单点一下。这个很重要， 我们做一个任务的时候，和民科最大的区别就是：我们要跑 Benchmark，验证完效果才去说这个东西有用。 
 目前主要的数据集有 LongMemEval(500 问，测五大能力：信息提取、多会话推理、知识更新、时序推理、安全拒答)、MABench(ICLR 2026，测精确检索、测试时学习、长程理解、冲突解决)、MemoryArena、LOCOMO、EverMemBench(首个多方协作基准，100 万 + tokens)、清华的 MemoryBench(首个用户反馈持续学习基准)。 
 目前在做记忆体测试的时候，这些是主流的 Benchmark。大家可以发现：上下文越长，记忆体效果越差；多会话推理、冲突解决目前都是非常难的问题。 
 Evermind 还提过一个我觉得特别有意思的问题： 今天我们讨论的记忆，不管是小龙虾还是别的，都假设 Agent 是一个一对一的个人助理，这是相对简单的场景。但如果把 Agent 丢进一个群聊里呢？它该记谁的？怎么分别记每个人的？ 所以记忆的未解决问题还非常多。 
 这里列出一些关键论文。 
 我们看今天的 RAG（包括混合召回）之所以不够用，是因为它本身没有状态、没有层级，至少在做 embedding、做 keyword search 的时候，它并不包含状态，也不包含时间关系。它是一个非常扁平的召回模型，所以这种模型并不擅长做记忆。这已经是目前的共识，所以才有很多图数据库、时序数据库想介入进来一起把 agent 记忆模型做好。 
 基础设施构建 
 如果我们今天看所有的智能体叙事框架，底层一定要有： 
 向量检索 （必需），尤其是 多语言向量检索， 比如刚才 911 的事情，中文需要翻译成英语，不能说中文搜不到英语的内容。跨语言搜索能力一定要有。 
 重排器和 Reader ：可能需要，有时可能不需要。 
 在此之上有存储和搜索，包括 Elasticsearch 中的向量数据库。可以看到 Jina 和 ES（Elastic）基本上包含了整个搜索的底座 。 
 另外再号召一下： Elasticsearch 和 Jina 融合之后，我们对于智能体记忆的底层有了一个非常全面的覆盖。 我希望大家能够利用 Elasticsearch 去构造自己的智能体记忆框架。 
 能力 
 Jina + Elastic 怎么覆盖 
 向量语义检索 
 Jina Embeddings v5（677M / 239M） 
 BM25 关键词搜索 
 Elasticsearch 原生支持 
 稠密 + 稀疏混合 
 Elasticsearch 原生 RRF 
 精排重排序 
 Jina Reranker v3（131K 上下文） 
 网页和文档理解 
 Jina Reader 
 多模态向量化 
 Jina Embeddings v4（文本 + 图像 + PDF） 
 元数据和多租户 
 Elasticsearch index / alias 
 目前 Elastic 还没覆盖的，是知识图谱遍历，以及如何把大模型放到架构中做事实抽取(extraction)。 
 Hot Take 
 1. 统一范式还没 出现 。 我在做智能体记忆调研的时候发现：其实统一的范式并没有形成。有些人从仿生学角度看这个问题，有些人从自己的使用习惯、工作效率上看这个问题。这非常像 2017 年 Transformer 没出来之前的深度学习，百花齐放的状态，包括 CNN、RNN、LSTM，这些东西百花齐放。 
 2. 纯文本派是躺平。 不想构建任何模型，也不想构建任何仿生学层级，基本靠 grep、keyword search。这几年 search 发展太快了，从 RAG 到 deep research，很多人已经疲惫到说："反正一切终究会被大模型吃掉，那你又何必去奋斗呢？反正到最后你就躺三个月，没准大模型出来就已经把这个实现了。" 我个人认为这是一种躺平，这种想法是有一定天花板的，而且天花板是显而易见的。 
 3. Unlearning 是一笔多年的技术债，该还了 。 目前所有系统都是只增不减，实际上是一笔技术债。我当时做机器学习的时候，2009 年大家就讨论过 机器遗忘(Machine Unlearning) ：怎么把已经训练的、已经学到的东西忘掉？一个现实类比就是 "刷抖音这号废了，重新开号吧"。推荐系统一旦被污染就无法恢复，本质就是它不会遗忘。智能体记忆面临完全一样的问题：噪声一旦写入，就永久污染所有后续检索。 
 4. 推荐系统会因为智能体记忆重新火起来。 智能体记忆的核心是个性化：记住用户偏好、行为模式、历史决策。这跟推荐系统做了二十年的事完全一样。小红书、抖音、淘宝这些推荐系统做得好的公司，凭借经验和先天优势，可能会在这个智能记忆体的时代发挥出来。 
 这就是我今天的演讲。希望对大家有所帮助，也希望让大家对智能体记忆的发展脉络和未来走向有了一个整体的认识。 
 另外再号召一下： Elasticsearch 和 Jina 融合之后，我们对于智能体记忆的底层有了一个非常全面的覆盖。 我希望大家能够利用 Elasticsearch 去构造自己的智能体记忆框架。 
 谢谢大家。 
 跳转微信打开
```

---

## 2. 肖涵：2026 年的 AI 搜索就是智能体记忆 | Elastic 中国 AI 搜索技术大会

- 日期: 2026-04-09 15:32
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyODIxMjczMA==&mid=2247503335&idx=1&sn=d99d929117e4cb3d0cda681df3d4c1f9

```
原创 Jina AI 2026-04-09 15:32 日本 
 一场智能体记忆的深度拆解，4/18 北京见！ 
 智能体记忆（Agent Memory）成为了 2026 年 AI 基础设施的新战场。Mem0、Zep、Letta、HydraDB……十几款产品在过去半年密集涌现，几乎每周都有新玩家入场。与此同时，Claude Code 用一个纯文本文件 CLAUDE.md 做记忆，Cursor 用 .cursor/rules 管理项目上下文，这些看似原始的方案反而成了开发者日常最依赖的记忆工具。 
 智能体记忆这个概念并不算什么创新，它本质上就是我们过去几年反复讨论的个性化检索、用户画像、上下文管理。但在 2026 年，它突然获得了前所未有的紧迫感。 
 原因很简单： 智能体能干的活 变长了，但记性没跟上。 
 前沿智能体能自主完成的任务时长每 7 个月翻一倍，今天已经到了小时级别。你可以让一个 agent 花四个小时帮你做完一件极其复杂的事：调研、比对、写方案、跑数据、做决策。然后你关掉窗口。下次打开，它依然不记得你的偏好，得到的结论，踩过的坑。 
 于是行业开始给 AI 加记忆。但加完之后发现了一个更棘手的问题：它不光记不住该记的，还忘不掉该忘的。Karpathy 前阵子发推说的就是这件事，两个月前的一个随意提问，会被 AI 永远当成你的深层兴趣反复提及。这和刷抖音刷废了号是一个道理，推荐系统的画像一旦被污染就很难恢复。 
 要么完全不记，要么不加区分地全记。缺的是中间那层，像人脑一样，有选择地记住重要的，自然地遗忘过时的。 
 这标志着与传统搜索需求的重大转向。2025 年的关键词是 Deep Research：用更长的推理时间换更深的搜索结果，用户学会了等待。但到了 2026 年，问题已经不是怎么找到，而是找到了怎么记住。 
 搜索解决的是单次查询的精准度，记忆解决的是跨会话的知识连续性。二者看似不同，实则是同一条技术路线的自然延伸：数据怎么表示、怎么检索、怎么随时间演化。 
 从 Jina AI 到 Elastic，我们在搜索底座上积累了六年，五代共 26 个向量模型和重排器和小型语言模型。当我们把视角从怎么检索延伸到怎么记住时，发现这不是跨界，是沿着同一条线走到了下一个路口。 
 遗忘比记住更难 
 我们把市面上十几款智能体记忆产品拆了一遍之后，最大的感触不是哪家做得好，而是一个所有人都在回避的问题： 怎么遗忘。 
 这不是个别产品的 bug，这是整个赛道的结构性缺陷。 
 人脑的记忆系统有一个被工程师严重忽视的机制： 遗忘不是记忆的失败，而是记忆的核心功能。 海马体每天都在主动清理不再被访问的突触连接，新皮层会在睡眠期间重新整合记忆、淘汰冗余。没有遗忘的记忆系统不是完美的记忆系统：它是一个被噪声淹没的垃圾场。 
 但现在市面上的产品几乎都在回避这个问题。写入容易，清理极难。一条错误的记忆一旦进入系统，就会在后续的每次检索中被反复召回、被引用、被强化。时间越长，污染越深，最终整个记忆库的可信度都会坍塌。这跟机器遗忘（Machine Unlearning）在深度学习中的困境一模一样：至今没有完美解决。 
 少数几家产品已经开始尝试仿生衰减：让不再被访问的记忆像生物记忆一样自然退化，权重逐步降低，直到被回收。这个方向我们认为是对的，但目前的实现还非常粗糙。 在 2026 年的智能体产品里，遗忘是最被低估的风险，也是最值钱的能力。 
 说来也巧， 这跟我们 2025 年做 DeepSearch 时的经验完全呼应 。当时我们发现，答案评估必须独立于答案生成：让同一个模型既生成又自评，效果很差。智能体记忆也是如此：记忆的写入和记忆的质量评估，如果不做成两个独立的过程，脏数据就会在系统里安营扎寨。 
 三条技术路线 
 拆完十几款产品之后，我们发现它们大致收敛到三条技术路线：用知识图谱做结构化记忆的，让大模型自己管记忆的，以及老老实实做存储管道的。 
 每条路线都有自己的优雅之处，也都有自己不愿意公开讲的致命弱点。 
 比如，图谱派的生态最成熟，但写入链路长到让人肉疼；大模型自管理派的思路最漂亮，但把记忆管理交给一个会产生幻觉的系统这件事，你品品；管道派最简单可控，但面对两条互相矛盾的记忆时，它分不清哪条该留、哪条该扔。 
 不过三条路线也已经形成了一些强共识。有五件事几乎所有人都在做，还有两件事正在成为新的分水岭：谁先做好谁就有护城河。 
 具体哪五件、哪两件？各自的架构取舍到底怎么选？这些肖总会在现场展开讲。 
 你以为你的 AI 记住了 
 我们把 LongMemEval、MABench、MemoryArena 几个主流基准测试的结果对齐之后，发现了一个跨基准的一致模式： 
 单条提取容易，跨会话推理难。 
 记住用户在某次对话中提到的一个具体事实，大部分产品都能做到。但把分散在多个会话中的信息关联起来做推理：比如用户上周说喜欢日料、这周说在减肥、然后问今晚吃什么：准确率会直接跳水。同一个测试里，产品之间的得分差距接近一倍。也就是说， 你以为你的 AI 记住了，其实它记了个寂寞。 
 具体的数据、产品间的对比、以及我们从中推导出的技术趋势判断：这些留到现场说。这里只提一个值得思考的问题： Claude Code 的 CLAUDE.md 用纯文件做记忆，不用向量、不用图谱、不用 LLM 抽取：这到底是想明白了，还是想开了？ 
 来现场听完整拆解！ 
 以上只是 Elastic VP of AI 肖涵博士将带来分享的冰山一角。完整的分享会覆盖： 
 搜索范式的六次跃迁 ，以及为什么最后一跳落在记忆 
 10+ 款主流产品的架构全景对比 ：图谱派、大模型自管理派、管道派的设计取舍和工程代价 
 三个基准测试的关键数据 ，以及它们揭示的行业真相 
 几个未来技术趋势的判断 ：包括为什么推荐系统会因为智能体记忆重新火起来 
 这是一场把论文、产品、Benchmark 拉到同一张图上的高密度分享。做 agent 产品或者搜索基础设施的，一定不能错过。 
 活动信息 
 整场大会是 Elastic 今年在中国最大的技术活 动，也是 Jina AI 团队今年第一次做这么系统的公开技术分享 。搜索、可观测、安全等 产品线都有深度内容；只要关心 Elastic 技术栈，一整天都有可听的东西。 
 📅 2026 年 4 月 18 日（周六） 
 📍 北京 · 北辰洲际酒店 
 🎫 活动 免费 ，快来 扫码报名！ 
 一天下来你能带走：Elastic VP of AI 肖涵的硬核分享，Reader 作者亲自拆解日均处理 3000 亿词元的背后工程细节，一场关于龙虾的圆桌，以及在展位上跟 Jina 团队面对面聊你的具体问题，如果聊得投缘，我们也在招人。 
 我们也建了一个微信交流群，活动前后有任何问题都可以在群里聊。 
 完整议程 
 跳转微信打开
```

---

## 3. 4·18 北京 Elastic AI Tech Day｜搜索基座模型议程（含 Jina 模型与 Reader）

- 日期: 2026-03-26 07:30
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyODIxMjczMA==&mid=2247503325&idx=1&sn=0891a31f63c213a0fded29bc2fc74422

```
原创 Jina AI 2026-03-26 07:30 新加坡 
 4月18号(周六)，北京线下见！ 
 这半年来，大家问我们最多的一个问题是：Jina AI 现在怎么样了？ 
 这半年里，我们的模型迭代继续加速。Jina Embeddings 已经迭代到五代目， v5 成为 Elasticsearch 语义检索的默认向量模型 。Jina Reranker v3 获得了 AAAI-2026 FrontierIR Workshop Best Paper 。Reader 的技术栈在更大规模的工程体系里持续演进，越来越多 RL 训练团队把它当作默认的网页读取层。 
 以前你可能单独调用 Jina API 就能把检索跑起来；现在，同一条能力链可以更自然地落在 Elastic 的生产级搜索平台 上。Jina 官方 API 照常演进，但与 Elasticsearch 的集成路径，也成了很多团队更省心的默认选项。 
 我们做的依然是 搜索底座模型 （Reader、Embeddings、Reranker） ，只是面向更大规模的生产场景，有了更完整的平台与更多工程资源来承载。 
 这些进展，文字只能讲个梗概，我们更想当面和大家聊聊细节。 
 4 月 18 日，Elastic AI Tech Day，北京 
 这是 Elastic 今年在中国最大的技术活 动，也是 Jina 团队今年第一次做这么系统的公开技术分享 。搜索、可观测、安全等 产品线都有深度内容；只要关心 Elastic 技术栈，一整天都有可听的东西。 
 对一直关注 Jina 的 朋友，我们特别划了 几道重点 。 
 1. 肖涵：搜索 AI 的技术演进与思考 
 听过肖总分享的人常有同感：不绕弯子、判断直接、信息密度高。 
 这场他会聊：搜索作为 AI 基础设施会往哪走、近半年行业与系统层面发生了什么变化、一线训练与发布模型的真实体会，以及站在平台视角看，下一步最值得押注的工程问题是什么。 
 2. 王彦龙：Jina Reader 技术架构分享 
 Reader 是我们最受欢迎的 API， 日均处理约 3 000 亿 token ， 很多头部模型训练团队把 Reader 当成默认的网页读取层。 r.jina.ai 前缀一加，网页就能转成适配 LLM 的输入，但其实背后的工程量超乎想象。 
 读网页从最简单的 GET 请求到复杂的无头浏览器渲染，中间是一整条工程光谱：IP 池、出口带宽、proxy 调度、并发与隔离、PDF 与版式文档…… 每一层都能单独聊半小时。Reader 目前是领域内速度最快、吞吐量最大、边边角角考虑最全面的产品。 
 这场分享会讲：Reader 怎么处理 复杂网页 、如何扛住日均千亿级 token 的高并发、凭什么成为许多 RL 数据管线的默认读取层；PDF 这一路踩过哪些工程坑，才让 PDF 祖师爷 Adobe 团队都愿意采购。 
 这也是 Reader 作者 王彦龙第一次做完整技术栈的公开分享 。做 RAG、Agent、LLM 数据工程，或 RL/RLHF 训练数据采集、需要大规模可靠网页来源的团队，都建议来听。 
 3. 肖涵 · 圆桌对谈：开源、商业与开发者成长 
 当 autoresearch 让 AI 自主 加速 研发循环，当模型迭代能够以天以单位时，公司和个人靠什么才跟得上节奏？开发者该押注当下的版本答案，还是押注可迁移的能力？ 
 从开源声量到商业变现，从产品取舍到创业生死，肖总始终在第一线做大量决策。如果你对未来的职业方向感到迷茫，或者正在为公司的技术路径头疼，推荐来听。 
 4. Jina AI by Elastic 联合展位 
 Jina 从 2020 年起步，中间调整过两次方向，最后 All in 搜索底座模型。中文社区一直是我们非常重要的一部分：很多小伙伴从 Neural Search 神经搜索框架时期就开始关注；很多开发者在 GitHub / Hugging Face 上给过模型反馈，在群里讨论 API 的报错怎么修。 
 现在 Jina 的能力已经跑在 Elastic 的平台与集成路径上。大家关心的 模型更新节奏、API 与集成方式、开源规划 等等，我们团队在会场设了展位，期待和大家当面聊、当面叙旧。 
 活动信息 
 📅 2026 年 4 月 18 日（周六） 
 📍 北京 · 北辰洲际酒店 
 🎫 活动 免费 ，快来 扫码报名！ 一天下来你能带走：肖涵对搜索 AI 下一步的方向判断，Reader 作者亲自拆解日均处理 3000 亿词元的背后工程细节，一场关于开发者怎么不掉队的圆桌，以及在展位上跟 Jina 团队面对面聊你的具体问题，如果聊得投缘，我们也在招人。 
 我们也建了一个微信交流群，活动前后有任何问题都可以在群里聊。 
 完整议程 
 阅读原文 
 跳转微信打开
```

---

## 4. 从多模态大模型中「拆」出音频向量模型

- 日期: 2026-03-12 15:03
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyODIxMjczMA==&mid=2247503286&idx=1&sn=1d5c4cfbdaea7820d020635e5b21efb9

```
原创 Jina AI 2026-03-12 15:03 新加坡 
 把任意多模态大模型变成小型音频向量模型 
 Google 最近发了 Gemini Embedding 2，他们第一个原生多模态向量模型。文本、图像、视频、音频、文档，全部映射到同一个 3072 维向量空间。 这是 Omn i Embedding（全模态向量模型）的大趋势：一个架构吃下所有模态 ，从 jina-embeddings-v4 到 Omni-Embed-Nemotron 再到 Omni-5，大家都在往这个方向收敛。 
 去年 EMNLP BoF 上我讲过：Omni 模型是 2026 年 Dense Retrieval 的胜负手。 真正引起我们注意的是音频。大多数人听到多模态 Embedding 首先想到的是图像，顶多再加个视频。音频是被遗忘的模态：数据难采、标注难做、做的人少。 
 过去一段时间，我们 Jina AI 团队恰好在 啃这块硬骨头 ： 如何在 1.2B 规模内做出高性能的音频向量模型？这也 是我们通向全模态愿景的关键一步。 
 趁着 Gemini Embedding 2 发布 的 节点，把我们一路上踩的坑和学到的东西分享给大家。 
 音频向量是什么 
 音频向量就是把一段音频压成一个定长向量。输入原始波形，模型输出一个稠密向量（通常 768 到 3072 维），编码了这段声音的语义内容。语义相似的两段音频，向量也相近；一段音频和它的文本描述，在共享向量空间中距离很短。这是 Omni Embedding 拼图里的一块：一旦音频能和文本、图像映射到同一个向量空间，跨模态检索就打通了。 
 2022 年以来的主流方案是 Contrastive Language-Audio Pretraining（CLAP），本质上就是把 CLIP 搬到音频域。思路很直接：一个音频编码器，一个文本编码器，中间用对比学习拉近配对的音频-文本、推远不配对的。LAION-CLAP 在这个基础上用 630K 对数据加 Feature Fusion 做了放大。当前最强变体（Elizalde et al., 2023）在 4.6M 对数据上训练，音频编码器横跨 22 种音频任务，配合自回归解码器，250M 参数量在 AudioCaps 上做到 42.0 cvR@5。 
 CLAP 的问题在哪？它从零开始学习音频和文本之间的对齐。这意味着你需要海量的配对数据去建立跨模态桥梁，460 万数据对不是白烧的。 
 我们走了一条完全不同的路： 把已经听懂音频的多模态 LLM，直接改造成 Embedding 模型。 桥梁已经在预训练中建好了，我们要做的只是把它从生成模型重塑为向量模型。 
 模型架构 
 先说输入输出。输入是原始音频波形，从 WAV/MP3/FLAC 解码后重采样到 16kHz 单声道。音频编码器先转成 128-bin log-mel 频谱图，再处理成特征 token 序列，大约每秒 150 个 token。一段 10 秒音频约 1500 token。最大输入 30 秒，更长的需要切片。输出是单个稠密向量，维度在 896 到 3584 之间，取决于 LLM backbone 的规模。 
 起点是 Qwen2.5-Omni，一个原生音频理解的多模态 LLM。三个组件： 
 音频编码器（约 0.6-0.8B 参数）：把波形转成特征向量，中间有一个约 4.5M 参数的线性投影层。这个投影层虽小，却至关重要，它是音频特征空间到 LLM 表示空间的桥梁，负责把音频编码器输出的特征维度对齐到 LLM 的输入维度。 
 LLM backbone（0.5-7B 参数）：每个 Transformer 层约 0.2B 参数，同时处理音频特征和文本 token。 
 池化层：对最后一层 hidden state 做 mean pooling，输出最终向量。 
 两个模态共享同一个 LLM backbone。这不是我们做的对齐，是 Qwen2.5-Omni 在预训练时就建立的。音频特征和文本 token 经过同一堆 Transformer 层处理，在表示空间里天然就有一定程度的对齐。我们要做的是把这种隐式对齐显式化为一个向量模型。 
 架构对比 左边是标准做法，端到端微调整个 MLLM（3-7B 参数）。右边是我们的模块化组合做法，把预训练音频编码器接到一个更小的 LLM backbone 上。共享 backbone 同时处理音频特征和文本 token，在同一个向量空间中生成 Embedding。 
 训练目标是 InfoNCE 对比损失。两个模态各自独立编码，双向计算 loss 后取平均： 
 def training_step (audio_batch, text_batch) : 
 audio_embeds = model.encode_audio(audio_batch) # [B, D] 
 text_embeds = model.encode_text(text_batch) # [B, D] 
 audio_embeds = F.normalize(audio_embeds, dim= -1 ) 
 text_embeds = F.normalize(text_embeds, dim= -1 ) 
 sim = audio_embeds @ text_embeds.T / temperature # [B, B] 
 labels = torch.arange(len(sim), device=sim.device) 
 loss = (F.cross_entropy(sim, labels) + 
 F.cross_entropy(sim.T, labels)) / 2 
 return loss 训练数据 
 五个音频-文本配对数据集，共 181K 样本： 
 数据集 
 样本量 
 说明 
 AudioSetStrong 
 108K 
 时序标注事件，GPT 生成字幕（AudioSet 子集） 
 FSD50K 
 41K 
 人工标注声音事件，200 类 
 Clotho 
 19K 
 音频字幕，详细描述 
 UrbanSound8K 
 9K 
 城市声音分类 
 MACS 
 4K 
 城市声学场景 
 CLAP 用了完整 AudioSet（200 万+音频）加上其他来源，总计 460 万对。我们只用了 AudioSetStrong 约 10 万条，数据量差了 25 倍。 
 为什么能少这么多？因为 CLAP 需要从零建立跨模态对齐，460 万对数据大部分精力花在教模型"什么声音对应什么文字"。而我们的起点是一个已经听懂音频的 MLLM，跨模态的桥已经造好了，训练只需要把这座桥从"生成"重新校准到"向量检索"。这是一个 fine-grained calibration，不是 from-scratch alignment。 
 def load_sample (audio_path, caption) : 
 waveform, sr = torchaudio.load(audio_path) 
 waveform = torchaudio.transforms.Resample(sr, 16000 )(waveform) 
 audio_inputs = processor.feature_extractor( 
 waveform, sampling_rate= 16000 , return_tensors= "pt" 
 ) 
 text_inputs = processor.tokenizer(caption, padding= True , return_tensors= "pt" ) 
 return audio_inputs, text_inputs 四条路，三条半死胡同 
 我们的目标很明确：参数量压到 1.2B 以下，性能超过 CLAP。我们试了四种做法，前三种各有各的问题，在第四种拿到了结果，但过程本身比结果更有价值。 
 路径一：全模型微调 
 Qwen2.5-Omni-7B 直接在音频-文本对上做对比学习微调，结果不出意外地好：AudioCaps T2A cvR@5 = 63.2，Clotho T2A = 39.2。这个分数远超 CLAP 的 42.0，证明了思路本身是对的。 但 7B 参数量摆在那里，推理成本和延迟都不现实。这条路的价值是给后面所有实验画了一条上限。 
 值得对比的是其他团队的类似尝试：Tevatron 2.0 也做全模型微调，但只用 AudioCaps 一个数据集，AudioCaps 上拿了 61.2，Clotho 上暴跌到 11.9。单数据集训练在分布内表现好看，出了分布立刻垮掉，这是向量模型老生常谈的问题了。还有 ColQwen-Omni，在视觉文档任务上微调、零音频数据，纯靠跨模态迁移拿到了 37.4。逼近 CLAP 但没超过。零数据能做到这一步，本身也说明 MLLM 的跨模态对齐的能力。 
 路径二：层剪枝 
 既然 7B 太大，能不能直接砍层？每个 Transformer 层约 0.2B 参数，从 28 层砍到 10 层就剩 3.5B，砍到 5 层剩 2.3B。 
 随 Transformer 层数减少的性能变化。 AudioCaps（红线）从 20 层的 63.2 降到 5 层的 56.0 cvR@5。所有配置仍然高于 CLAP baseline（虚线）。但即使砍到 5 层（2.3B 参数），离 1B 目标差了一倍多。 
 层数 
 参数量 
 AudioCaps T2A cvR@5 
 Clotho T2A cvR@5 
 20 
 5.8B 
 63.2 
 39.2 
 10 
 3.5B 
 58.2 
 36.5 
 5 
 2.3B 
 56.0 
 36.0 
 性能下降是平滑的，说明信息在各层间分布比较均匀，没有哪几层是可以无痛摘掉的。 
 另外一个有意思的观察是 Batch size（32、64、128）几乎没有影响最终性能。大 batch 在训练初期有优势，但后期可能过拟合负样本分布，batch 128 在 2K 步时 Clotho NDCG 打到 31.3，到 10K 步反而掉到 29.3。 这说明在数据量有限的情况下，大 batch 带来的 hard negative 数量优势敌不过分布偏移的风险。 
 层剪枝的根本限制是：音频编码器本身就有 0.6-0.8B，加上投影层和 Embedding 层的固定开销，即使 LLM backbone 砍到零，模型也至少 1B 起步。此路不通。 
 路径三：纯文本模态迁移 
 这个思路更激进：完全不用任何音频-文本配对数据，只用纯文本 NLI 数据集（MultiNLI、SNLI、FEVER、SciFact）做微调。逻辑是这样的，MLLM 预训练时已经建立了音频和文本的对齐，那我只训练文本侧的向量质量，音频侧应该能搭上便车。 
 在完整 7B 上，这个赌注居然赢了：AudioCaps 46.1，超过了 CLAP 的 42.0。零音频训练数据，纯靠文本 NLI 就能做出一个比 CLAP 更好的音频向量模型，这本身就很说明问题，MLLM 预训练建立的跨模态对齐做得很深，不是表面功夫。 
 但在剪枝后的 10 层模型上，同样的做法直接塌了：cvR@5 = 5.9，几乎等于随机。 
 这里的 insight 很重要： 跨模态对齐不是一个集中存储在某几层的对齐模块，而是分布在整个网络的每一层中。 28 层的完整网络里，每一层都参与了音频和文本表示的渐进对齐。你砍掉大部分层，对齐就碎了。文本侧靠 NLI 数据还能补回来，但音频侧没有任何数据兜底，直接归零。 
 这条路教会我们的是：模态迁移的可行性和模型压缩的可行性是矛盾的。你不能同时既要又要。 
 路径四：模块组合 
 前三条路的共同问题是都从同一个 7B 模型出发往小了做。 路径四我们换了一个思路：不从大模型上减，从小组件上加。 从一个模型里摘出音频编码器，从另一个模型里拿一个小 LLM backbone，拼在一起，甚至可以跨模型家族拼装。 
 为什么这也能行呢? 因为 Qwen2.5-Omni 的训练分了三阶段：1. 冻结 LLM，只训练音频/视觉编码器的投影层；2. 全参数解冻联合训练；3. 扩展到 32K 上下文。 
 关键在于第一阶段，音频编码器学会了如何把波形转成 LLM 能读懂的 token。这种说 LLM 语言的能力是通用的，不绑定某一个特定的 LLM。所以我们大胆假设： 一个在第一阶段训练好的音频编码器，应该能直接插到任何 Qwen 系列的小 LLM 上。 
 我们测试了四种组合： 
 配置 
 音频编码器 
 LLM 
 参数量 
 M1 
 Qwen3-Omni（0.6B，stage-1 之前） 
 Qwen2.5-0.5B 
 1.1B 
 M2 
 Qwen3-Omni（0.6B，stage-1 之前） 
 Qwen2.5-3B 
 3.6B 
 M3 
 Qwen2.5-Omni-3B（0.8B，stage-3 之后） 
 Qwen2.5-3B 
 3.8B 
 M4 
 Qwen2.5-Omni-3B（完整） 
 完整 3B 
 3.8B 
 实现细节上有个坑，Qwen3-Omni 用的是 Qwen3OmniMoePreTrainedModel ，standalone Qwen3 用的是 Qwen3ForCausalLM ，两者的模型壳子不一样。我们的做法是初始化一个维度匹配的 Omni 模型壳子，然后把权重拷贝到对应位置。 
 各配置在 AudioCaps 和 Clotho T2A cvR@5 上的表现 用 stage-3 之后对齐更好的音频编码器效果更好（M3 vs M2：AudioCaps +4.2）。LLM 预训练的 stage 2-3 对 Embedding 质量影响不大（M3 vs M4 在误差范围内）。 
 结果里有三个发现： 
 第一，M1（1.1B）在 AudioCaps 上就打到了 49.7，超过 CLAP 的 42.0 整整 18%。 我们目标达成：参数量 1.1B，低于 1.2B 的目标线，性能大幅领先 CLAP，并且只用了 CLAP 1/25 的训练数据。 
 第二，音频编码器的对齐质量决定上限。 M3 用的是第三阶段之后完整训练过的音频编码器，M2 用的是 stage-1 之前的初始版本，两者 LLM backbone 相同（Qwen2.5-3B），但 M3 在 AudioCaps 上比 M2 高了 4.2 个点。这说明音频编码器在多阶段训练中获得的对齐精度直接传导到了最终的 Embedding 质量。 
 第三，LLM 的 stage 2-3 训练对 Embedding 质量几乎没有影响。 M3（拼装的 LLM）和 M4（原装完整 3B）的性能在误差范围内。这也意味着 LLM backbone 在 stage 2-3 学到的那些能力：更好的指令跟随、更长的上下文处理，对向量化任务没有贡献。向量模型需要的是表示能力，不是生成能力。 
 评测 
 音频 Embedding 的评测本质上就是看检索质量：给一段文本 query，能不能找到对的音频？ 
 难点在于对的定义因数据集而异。 
 AudioCaps 的描述很具象（"一个男人说话，然后门关上了"），这种描述和声学特征是一一对应的，模型只要记住声学 pattern 就能得分。 
 而 Clotho 的描述更抽象（"安静的氛围中远处有隆隆声"）。这需要模型理解场景级别的语义，而不只是频谱特征。一个只记住表面声学特征的模型在 AudioCaps 上跑分好看，到 Clotho 上就原形毕露。 我们最看重的是跨描述风格的泛化能力，这才能反映模型真正理解了什么。 
 CV-Recall@5（cvR@5）：对每个文本 query，看 top-5 结果中是否命中正确音频。二值打分，所有 query 取平均。这是 MTEB 音频检索的标准 metric。 
 def evaluate_cvr_at_k (model, dataset, k= 5 ) : 
 audio_embeds = model.encode_audio(dataset.audio_clips) 
 text_embeds = model.encode_text(dataset.text_queries) 
 sim = F.normalize(audio_embeds) @ F.normalize(text_embeds).T 
 hits = 0 
 for i in range(len(dataset.text_queries)): 
 top_k = sim[:, i].argsort(descending= True )[:k] 
 if dataset.ground_truth[i] in top_k: 
 hits += 1 
 return hits / len(dataset.text_queries) 三个评测集均来自 MTEB：AudioCaps（视频衍生，人工字幕）、AudioSetStrong（时序标注，GPT 描述）、Clotho（多样化，抽象字幕）。CLAP 用了完整 AudioSet（200 万+），我们只用了 AudioSetStrong 约 10 万条，这在一定程度上解释了 CLAP 在该 benchmark 上的优势。 
 所有配置在 AudioCaps、AudioSetStrong、Clotho T2A 检索上的横向对比 红色虚线为 CLAP baseline。模块组合方案（绿色）以远远更小的模型尺寸取得了有强竞争力的结果。全量微调的 7B 模型（深蓝）是性能上限。 
 应用场景 
 传统的音频检索里，输入文字找音效当然是最直接的场景。 但更值得关注的是音频 Embedding 在 Agentic 系统中的角色。当语音成为 Agent 的主要输入方式时，第一步往往是 ASR 转文字再处理。 但 ASR 有延迟、会丢失语气语调信息、还依赖转写质量。如果 Agent 能直接对语音输入做向量化，根据语义相似度分发到正确的工具或子 Agent，就跳过了 ASR 这个瓶颈。不是所有语音输入都需要逐字转写，很多时候你只需要知道"这段话的意图是什么"。 
 工业场景里的声音事件分类也是一个被低估的方向。设备异响检测、安防系统、智能家居，这些场景需要的不是转写，而是"这个声音像什么"，这正是 Embeddings 的强项。 
 更远一步看，当 Omni Embedding 做成了，文本、图像、音频、视频都在一个向量空间里，Agent 就获得了一个统一的感知接口。不管输入是什么模态，都转成向量后统一检索、比较、推理。这是多模态 Agent 能真正 scale 的前提。 
 而这一切有个硬性前提： 模型要够小，能在端侧跑。 语音交互容不下云端传输带来的延迟损耗，而且语音数据的隐私敏感度远高于文本。所以高性能的小模型不是加分项，而是入场券。这也是我们把目标定在 1.2B 以下的原因。 
 结论 
 预训练 MLLM 是做新模态 Embedding 最大的杠杆。 它一次性提供了跨模态对齐、强文本编码器和能力不错的音频编码器。 
 模块化组合是目前最有前景的方向。 从不同模型、不同训练阶段里拆出组件自由拼装，我们在音频向量任务上验证了可行性。实验结果也指向了一个清晰优先级：音频编码器的对齐质量是第一位的（stage-3 vs pre-stage-1 差了 4.2 个点），LLM backbone 的生成能力对向量化任务没有贡献（stage 2-3 训练前后没有差异）。这也意味着构建向量模型时，选组件的优先级是：编码器对齐 > LLM 的表示能力 > LLM 的其他能力。 
 跨模态迁移和模型压缩不能既要又要。 文本模态迁移在完整 7B 上漂亮地跑通了（46.1 vs CLAP 42.0），但在 10 层剪枝模型上直接归零（5.9）。对齐分布在整个网络中，压缩就碎。 
 AudioCaps 领跑不代表问题解决了。 我们模型在 AudioCaps 上大幅领先 CLAP，但在更依赖抽象语义的 Clotho 榜单上只是持平。暴露了模型的场景级语义理解不够。只看 AudioCaps 你会觉得模型已经很好了；加上 Clotho 就知道还差得远。 
 这项工作是我们迈向 Omni Embedding（全模态向量模型）的关键一步，模块化组合让我们找到了无需大规模烧数据即可开启新模态的方法，但 Clotho 的结果提醒我们：光靠复用预训练组件还不够，数据质量和多样性仍然是底层硬约束。 
 接下来我们会探索 MoE 架构把激活参数压到 500M 以下，尝试模块组合和模态迁移的深度结合，引入 WavCaps、MusicCaps 和语音数据集做数据扩充，重点补上抽象描述的短板。 
 我们开源社区见！ https://github.com/jina-ai/audio-embedding-kickstarter 
 阅读原文 
 跳转微信打开
```

---

## 5. Jina AI 何意味

- 日期: 2026-03-11 16:31
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyODIxMjczMA==&mid=2247503242&idx=1&sn=22e209aee5ff30e556ad36d68fdb52b7

```
：
，
。
视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
```

---

## 6. 从向量里逆向出原始文本和模型来源

- 日期: 2026-03-09 16:26
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyODIxMjczMA==&mid=2247503203&idx=1&sn=94a7df037e479f9de24959bb88e8fe4a

```
原创 Jina AI 2026-03-09 16:26 新加坡 
 不就是一堆浮点数嘛，能看出什么？87% 识别出模型，81% 还原文本。 
 🔬 在线 Demo: embedding-inversion-demo.jina.ai 
 📊 技术报告: jina.ai/news/embedding-fingerprints 
 📊 技术报告: jina.ai/news/embedding-inversion 
 📄 论文: arxiv.org/abs/2602.11047 
 💻 代码: github.com/jina-ai/embedding-fingerprints 
 用户把文本发到我们的 API，我们返回一串浮点数。没有标签，没有水印，没有任何元数据告诉你它从哪来、用的什么模型。大多数人看到这串数字，反应都是"不就是一堆浮点数嘛，能看出什么？" 
 过去两周，我们做了两项研究，发现能看出的东西远比想象中多： 
 模型溯源 ：我们训练了一个仅有 80 万参数的小模型。光看一串浮点数，就能判断出这是哪个模型生成的，准确率高达 87%，覆盖 68 个模型和任务组合。 
 文本逆向 ：我们用掩码扩散模型，直接从向量中反推出原始文本。Token 级还原准确率达到了 81%。 
 也就是说，向量不仅携带语义，还带着生成它的模型的基因， 以及原始文本的大量信息残留。 
 demo: https://embedding-inversion-demo.jina.ai/ 
 向量溯源：这串数字是谁生成的？ 
 当有人给你一个 1024 维的向量，你能判断它是 BGE-M3 生成的，还是 jina-embeddings-v3 ，还是 Qwen3-Embedding 吗？ 
 再往前走一步: 同一个模型，你能分辨推理时用的是 retrieval 指令还是 classification 指令吗？ 
 直觉上这似乎不可能。向量就是一堆数字，模型之间的差别应该体现在语义空间的几何结构上，而不是数值本身的分布细节。 但实验结果直接推翻了这个直觉。 
 不同模型产生的浮点数，在统计上有非常显著的差异。值域范围、各小数位数字出现的频率、维度间的相关模式...... 这些特征拼在一起，构成了模型独特的 数字指纹 。这有点像笔迹鉴定，同一段话让不同人抄写，内容一样，但笔画的力度、倾斜和连笔方式都会无意间暴露书写者的身份。 
 把浮点数当文本来读 
 这个方法最反直觉的地方在于输入表示。我们没有把向量当成一堆浮点数，而是把每个数字转成了字符串，像处理文本一样，逐个字符拆开喂给模型。 
 如下图所示， -0.1234 会变成 token 序列 [CLS] - 0 . 1 2 3 4 ，维度之间用 [SEP] 隔开。整个词汇表极简，只有 15 个 Token：数字 0 到 9、负号、小数点、几个特殊分隔符。 
 位级别分词（Digit-level Tokenization） 为什么不使用更直观的量化分桶（Binning）：把数据范围划分为 256 个区间（bin），一个维度对应一个 Token，这样 1024 维的向量只需 1024 个 Token 就能表达完。 
 因为量化需要预设边界，而不同模型的数值分布天差地别：有的集中在 0 附近，有的铺满整个 [-1, 1] 区间，同一个模型不同维度的分布也完全不同。任何固定的分桶方案，都会在某些模型上造成严重的分辨率损失，掩盖掉最关键的特征。 
 所以我们选了最“无假设”的方案：位级别分词（Digit-level Tokenization）。虽然这会让一个 1024 维向量膨胀成 7700 个 Token 的长序列，但它原样呈现了数字的每一位，保留了所有的统计痕迹，不预设规律，让模型自己去学习其中的统计特征。 
 比如某些模型在特定位上出现数字 7 的频率更高，或者某些维度的排列模式更独特。这些看似无意义的微观特征，恰恰构成了模型的数字指纹。 
 模型架构 
 分类器本身是个 4 层 Transformer，128 维，4 个注意力头，总共约 80 万参数 。用 RoPE 做位置编码，SwiGLU 做 FFN，RMSNorm 归一化。CLS token 池化后投影到 68 个输出类别。 
 模型架构图，比 GPT-2 小 150 倍，但对 15 token 词汇表的分类任务完全够用。 80 万参数是什么概念？比 GPT-2 小两个数量级。 但这个任务词汇表只有 15 个 token，分类目标是 68 个类别，瓶颈不在模型大小，而是如何从 7700 个 token 的长序列里提取出能区分 68 个类别的统计特征。 
 训练数据方面，我们准备了一万条多语言文本，分别送入 25 个以上的模型，配合不同 task prefix 编码，产生 68 个类别。 每类 7000 条训练样本，3000 条验证样本。 
 这 68 个类别不只是 68 个模型。其中包含了同一个模型搭配不同 instruction prompt 的组合，比如 jina-embeddings-v5-text-small 配 retrieval 指令和配 classification 指令算两个不同类别。如果分类器能区分它们，说明仅仅换一个 instruction prompt，就足以在输出数值上留下可检测的痕迹。 
 在这些类别中，最难的分组是 1024 维度，包含 32 类模型，分类器无法通过序列长度投机取巧，必须纯粹依赖数值模式。 
 维度 
 类别数 
 示例模型 
 384 
 8 
 BGE-small， E5-small， MiniLM， GTE-small 
 512 
 2 
 BGE-small-zh 
 768 
 24 
 BGE-base， E5-base， jina-embeddings-v5-text-nano， Nomic， INSTRUCTOR， LaBSE 
 1024 
 32 
 BGE-M3， E5-large， jina-embeddings-v3， jina-embeddings-v5-text-small， Qwen3-0.6B， Snowflake， mxbai 
 1536 
 2 
 GTE-Qwen2-1.5B 
 68 类分类，87% 准确率 
 我们在 A100 上跑了 14 个 Epoch，处理了大约 430 亿个 Token。 
 14 个 epoch 的训练和验证曲线 最终，训练准确率达到了 87.3%，验证准确率为 86.0%。两条曲线贴得很近，说明模型真的学到了真实的数值规律，而不是在死记硬背训练集。 
 87% 准确率，随机猜的话是 1.5%。比瞎猜好 59 倍。 
 68 类验证集混淆矩阵，每类 3000 样本，共 20.4 万样本。对角线越亮说明分类越准确。 观察这 20.4 万个样本的混淆矩阵，能看到几个有趣的现象：GTE-large、LaBSE、Paraphrase MiniLM 等模型被 100% 准确识别。跨系列的区分（如 BGE vs Jina）非常容易，模型底层的架构和训练方法留下的指纹最深。最难分辨的是同一个基础模型搭配不同的任务前缀。 
 最让人意外的是， 同一个模型、完全相同的权重，仅仅是推理时换了一个 instruction prompt，输出的数值分布就会产生可检测的差异。 jina-embeddings-v5-text-small 在 5 个不同 task prefix 之间达到了 92% 的区分准确率。任务适配（Task adaptation）不只是在语义空间里挪了个位置，它实际上改变了数值的统计分布。 
 这件事有非常直接的用途。接手了一个向量数据库但不知道当初用的什么模型？ 取出一条向量送进分类器就能识别。 怀疑某个 API 声称用的是 model A 但实际偷偷换成了 model B？向量指纹可以验证。向量模型的提供商悄悄升级了版本？指纹同样会暴露这个变化。 
 从向量逆向文本 
 如果识别模型来源只是让人意外，那接下来的事就有点狠了：从向量里逆向出原始文本。 
 给你一个 1024 维的向量，还原出生成它的那段文本。 
 这不是全新的问题。2023 年 Morris 等人做的 Vec2Text 用 T5 编解码器（Encoder-Decoder） 在 32 token 的序列上做到了 92% 的 精确匹配（Exact Match） 。但那个方法有个根本限制：它需要反复调用目标模型的 API 进行迭代修正，动辄 20 多轮，推理成本直接翻了一个数量级。 
 我们的目标更激进: 只看向量本身，不碰目标模型，一次性把文本还原出来。 
 用掩码扩散逆向出文本 
 我们将这个问题重新定义为一个条件掩码扩散 （Conditional Masked Diffusion） 问题。 
 从一个全 [MASK] 的序列开始，模型在每一步同时预测所有位置的 token，逐步替换成真实词汇。整个过程只需要 8 步。不是从左到右一个个生成，而是所有位置并行去噪。 
 步骤 8/8  [MASK] [MASK] [MASK] [MASK] [MASK] 
 步骤 6/8  [MASK] quick [MASK] [MASK] [MASK] 
 步骤 3/8  The   quick brown [MASK] jumps 
 步骤 1/8  The   quick brown fox   jumps 去噪过程: 从全掩码出发，每一步同时预测所有位置，8 步内完成还原。 
 我们通过 自适应层归一化 （Adaptive Layer Normalization， AdaLN ) 将目标向量注入到 Transformer 的每一层。向量先经过一个投影层，然后在每一层生成缩放（Scale）和位移（Shift）参数，用来调制层归一化的输出。时间步也通过同样的机制注入。 两个信号相加，模型同时知道"当前去噪到了哪一步"和"目标向量长什么样"。 
 条件掩码扩散语言模型的架构。上半部分是训练流程: 输入文本经 embedding encoder 编码后，通过 MLP 投影注入 Transformer。下半部分是去噪过程: 从全掩码序列出发，逐步还原。 
 这个设计一举解决了 Vec2Text 的两个问题。第一，推理时完全不需要接触原始模型，向量是唯一的输入。第二，所有位置并行预测，避免了自回归从左到右的误差累积。而且 AdaLN 的条件注入方式天然不挑编码器：不管目标向量来自什么模型、什么维度，过一遍投影 MLP 就能注入同一个 Transformer。 
 底座模型我们选用了 22 层、3.8 亿参数的多语言 BERT。在冻结预训练权重后，我们只训练投影层、AdaLN 模块和输出层，实际训练参数量约 1.9 亿。训练数据是 mC4 的 200 万条多语言样本，统一截断到 32 个 token。 
 # 训练核心伪代码 
 for text, embedding in dataloader: 
 t = uniform( 0 , 1 ) # 随机采样时间步 
 masked = random_mask(text, t) # 按比例随机掩码 
 cond = mlp_project(embedding) # 投影 embedding 
 logits = model(masked, t, cond) # 条件预测 
 loss = cross_entropy(logits[masked_pos], text[masked_pos]) 训练流程: 随机掩码 + 条件去噪。噪声调度用 log-linear schedule，集中在后期掩码，前期保留结构。 
 81% 的 Token 级还原准确率 
 我们分别在三个主流模型上进行了实测，还原率都很惊人。 
 编码器 
 Token 还原率 
 向量维度 
 Qwen3-Embedding-0.6B 
 81.3% 
 1024 
 EmbeddingGemma-300m 
 78.8% 
 768 
 jina-embeddings-v3 
 76.0% 
 1024 
 三个编码器上的 token 还原准确率，使用 顺序贪心解码（Sequential Greedy Decoding） ，序列长度 32 token。每个编码器单独训练。 
 四个编码器配置的训练准确率曲线。所有模型在 50K 步后趋于收敛。 
 为了看清这个数字的含金量，我们设定了一个基准对照组：让一个普通的语言模型在完全不看向量的情况下盲猜文本。它能写出非常流畅的句子（BLEU 分数很高），但 Token 准确率只有 2.1%。随机 token 更惨，0.02%。 
 "能说人话"和"说对的话"是两回事。 模型必须从向量中真正提取语义信息，才能在最低的编码器上也做到 76% 的还原。 
 在解码策略上，我们测试了五种方案。 表现最好的是 欧拉 + 重掩码（Euler + Remasking）： 模型每一步去噪后，都会自我检视一遍，把置信度最低的 5% 重新掩码，交给下一步去修正。 相当于把 Vec2Text 的外部修正循环内化到了扩散过程里。 
 实验证明 5% 是一个最优平衡点，比例太多丢掉正确的预测，太低则修正力度不够。 
 解码策略 
 jina-v3 
 Qwen3 
 Gemma 
 顺序贪心（Sequential Greedy） 
 0.715 
 0.585 
 0.621 
 欧拉采样（Euler Sampling） 
 0.667 
 0.556 
 0.604 
 欧拉 + 重掩码（Euler + Remasking） 
 0.665 
 0.584 
 0.595 
 两阶段（Two-Stage） 
 0.667 
 0.591 
 0.605 
 不同解码策略在 10 种语言上的平均余弦相似度。需要注意，这里衡量的是还原文本与原始文本的向量相似度，而非 Token 级准确率。两个指标下的最优策略不完全一致。综合来看，Sequential Greedy 在大多数编码器上表现得最为稳健，是目前最可靠的还原主力。 
 一个 1024 维的 float32 向量只有 4KB。但这 4KB 足以让一个扩散模型还原出 32 个 token 中超过 80% 的内容。 
 向量并非不可逆 
 在很多人的认知中，向量是一道天然的脱敏屏障：文本转化为高维坐标后，原始信息便不可回溯。 很多系统也都宣称：“我 们只存向量，不存原文，所以用户隐私是绝对安全的。” 
 这两项研究动摇的正是这个假设。 向量不是不可逆的哈希，而是一个有损但信息密度极高的压缩表示。模型的身份、原始文本的内容，都编码在里面，提取的门槛也在不断降低。 
 指纹研究（Fingerprint）证明了每个模型编码语义的数值风格各不相同，区分度高到一个 80 万参数的小模型就能认出 68 个来源。逆向研究（Inversion）则证明了这些数字里编码的原始信息，足够扩散模型还原出 80% 以上的内容。 两个工作串联起来，先用指纹分类器锁定编码器，再用对应的逆向模型还原文本，就构成了一条完整的攻击链路。 
 对模型开发者来说， 这些发现迫使我们直面一个此前被忽视的问题：向量模型的安全边界到底在哪里？过去我们把精力都投在提升语义检索性能上，但从来没认真想过这些向量在安全性上到底暴露了多少。 
 我们是否该在训练中引入某种信息瓶颈？在保留检索能力的同时，降低向量的可逆性，或者至少让模型的数值指纹不再那么容易被识破？ 
 当然，硬币有另一面。在 API 提供商可以悄悄换模型的世界里， 能从数值本身验证模型来源， 本身就是一种有价值的审计能力。 
 两个项目的代码和在线 demo 均已开源： 
 🔬 在线 Demo: embedding-inversion-demo.jina.ai 
 💻 代码仓库: github.com/jina-ai/embedding-fingerprints 
 阅读原文 
 跳转微信打开
```

---

## 7. jina-embeddings-v5-text：0.6B 参数下最好的多语言向量模型

- 日期: 2026-02-21 09:07
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyODIxMjczMA==&mid=2247503129&idx=1&sn=6873b943a413cc54629c162bd0dd7725

```
原创 Jina AI 2026-02-21 09:07 北京 
 五代目向量模型 0.2B & 0.6B MMTEB 霸榜，再破小模型性能天花板！ 
 jina-embeddings-v5-text 岁在丙午，开年即战。 Jina AI 的五代目向量模型 春节期间正式发布。 1B 参数内世界第一，全面刷新向量模型的性能天花板！ 
 jina-embeddings-v5-text-small （677M 参数）：MMTEB 67.0 排名第8 ，MTEB 英文 71.7，全面超越流行的 qwen3-embedding-0.6b 
 jina-embeddings-v5-text-nano （239M 参数）：MMTEB 65.5 排名第11 ，MTEB 英文 71.0 
 我们的五代目也同时发布了 vLLM, GGUF 和 MLX 版本 ，为本地端运行提供最大的支持。 
 2026年2月21日的 MMTEB 多语言排行榜 消息来源：Hugging Face 
 资源链接： 
 HF 🤗 https://huggingface.co/collections/jinaai/jina-embeddings-v5-text 
 魔搭 🧙 https://modelscope.cn/organization/jinaai 
 技术报告 📖 https://arxiv.org/abs/2602.15547 
 API 💻 https://jina.ai/embeddings/ 
 Small 版本 支持 32K token 上下文 （nano 为 8K）、 4 个任务专用 LoRA 适配器 （检索、文本匹配、分类、聚类），以及从 1024 到 32 维的 Matryoshka 维度截断 。 
 Nano 版本 仅 239M 参数，检索质量却能匹配参数量两倍于它的同类模型。 
 和前几代模型对比，v5-text-small 在检索任务上与 jina-embeddings-v4 （3.8B）持平，体积只有后者的 1/5.6 ；在所有任务上全面超越 jina-embeddings-v3 （572M），参数量相当。 
 特性 
 v5-text-small 
 v5-text-nano 
 基座模型 
 Qwen3-0.6B-Base EuroBERT-210m 
 参数量 
 677M 239M 
 向量维度 
 1024 
 768 
 上下文长度 
 32,768 
 8,192 
 语言数 
 119（Qwen3 tokenizer） 
 15+（EuroBERT tokenizer） 
 池化方式 
 Last-token 
 Last-token 
 LoRA 适配器 
 4 个（检索、文本匹配、分类、聚类） 
 Matryoshka 维度 
 32-1024 
 32-768 
 MMTEB 分数 
 67.0 65.5 
 MTEB 英文 
 71.7 71.0 
 许可证 
 CC BY-NC 4.0 
 Benchmark 性能表现 
 MMTEB 多语言评测 v5-text-small 在 MMTEB 多语言评测上取得 67.0 （131 个任务、9 种任务类型的平均分），超出同量级第二名 Qwen3-0.6B（指令版，64.3） 2.7 分 。nano 模型以 239M 参数取得 65.5，超越了多个参数量两倍于它的模型。 
 small 在中文评测上得分 73.7 ，优于 v3 和 Gemma-300M。Qwen3-0.6B 在中文单项上更强（76.3），这不意外，Qwen3 底座本身有大量中文预训练数据。但 v5-text-small 胜在均衡，中文以外语言覆盖和任务泛化能力更广。 
 MTEB 英文 在 MTEB 英文评测里， v5-text-small 以 71.7 领跑所有 1B 以下多语言模型 （41 个任务、7 种任务类型平均），其后是 KaLM-mini-v2.5 （71.3）和 v5-text-nano （71.0）。239M 的 nano 与 494M 的 KaLM 表现相当，但参数量不到后者一半。nano 在检索（58.8）和重排序（49.2）上超越了所有 500M 以下的竞品。 
 检索任务 v5-text-small 在五个检索 benchmark（MTEB 多语言、MTEB 英文、RTEB、BEIR、LongEmbed）的任务级平均分达到 63.28 ，在所有 4B 以下的模型中最高，与 jina-embeddings-v4 （3.8B，63.62）几乎持平， 但体积仅为后者的 1/5.6 。 
 其中，RTEB（面向企业检索场景的 benchmark）得分 66.84，BEIR（大规模英文零样本评测）得分 56.67，均超越了同量级的 Qwen3-0.6B。500M 以下模型中，nano（61.43）超越了 Gemma-300M（59.66）和 KaLM-mini-v2.5（56.58），在 BEIR 的分数更是该量级最高。 
 模型架构 
 v5-text 采用 decoder-only 骨干网络，通过 last-token pooling （取序列末尾 EOS token 的隐藏状态）生成向量，取代了传统的 mean pooling。和 Qwen3-Embedding、EmbeddingGemma 等近期模型的选择一致，也更契合 decoder-only 架构的特性。 
 四个轻量级 LoRA 适配器注入每一层 Transformer，分别对应检索、文本匹配、分类和聚类，用户在推理时按需切换。这一设计延续自 jina-embeddings-v3 ，用独立适配器替代指令微调，化解多任务间的优化冲突。 
 对于非对称检索任务，通过文本前缀区分输入角色：query 使用 "Query:" 前缀，document 使用 "Document:" 前缀。文本匹配、分类、聚类任务统一使用 "Document:" 前缀。 
 此外，模型支持 Matryoshka Representation Learning（MRL），可对向量维度进行截断，从 1024 维到 32 维，以满足不同效率需求。 
 上下文长度方面，small 支持 32K tokens，nano 支持 8K tokens。前者相较 v3 的 8K 扩展了 4 倍。 
 快速开始 
 Elastic Inference Service 
 生产环境首选的接入方式是由 Elastic Inference Service（EIS）提供的推理服务，内置弹性伸缩，在 Elastic 部署中直接生成向量，无需自行管理推理基础设施。 
 PUT _inference/text_embedding/jina-v5 
 { 
 "service" : "elastic" , 
 "service_settings" : { 
 "model_id" : "jina-embeddings-v5-text-small" 
 } 
 } 详见 EIS 文档： https://www.elastic.co/docs/explore-analyze/elastic-inference/eis 
 Jina Embedding API 
 Jina 官方托管 API，按 token 计价，开箱支持任务选择、维度截断和批量处理，无需 GPU。 
 curl https://api.jina.ai/v1/embeddings \ 
 -H "Content-Type: application/json" \ 
 -H "Authorization: Bearer YOUR_API_KEY" \ 
 -d '{ 
 "model": "jina-embeddings-v5-text-small", 
 "task": "retrieval.query", 
 "dimensions": 1024, 
 "input": ["What is knowledge distillation?"] 
 }' 请前往 jina.ai/embeddings 获取 API Key。 
 Hugging Face + sentence-transformers 
 本地部署，完整控制推理流程。模型权重已在 Hugging Face 公开，原生兼容 sentence-transformers。 
 from sentence_transformers import SentenceTransformer 
 import torch 
 model = SentenceTransformer( 
 "jinaai/jina-embeddings-v5-text-small-retrieval" , 
 model_kwargs={ "dtype" : torch.bfloat16}, 
 ) 
 query_emb = model.encode( "What is knowledge distillation?" , prompt_name= "query" ) 
 doc_embs = model.encode([ "Knowledge distillation transfers..." , "Venus is..." ], prompt_name= "document" ) 
 similarity = model.similarity(query_emb, doc_embs) vLLM 
 适合高吞吐生产场景。vLLM 原生支持 v5-text 的 last-token pooling。 
 from vllm import LLM 
 from vllm.config.pooler import PoolerConfig 
 model = LLM( 
 model= "jinaai/jina-embeddings-v5-text-small-retrieval" , 
 dtype= "float16" , 
 runner= "pooling" , 
 pooler_config=PoolerConfig(seq_pooling_type= "LAST" , normalize= True ), 
 ) 
 outputs = model.encode([ "Query: climate change impacts" ], pooling_task= "embed" ) 面向 llama.cpp 和 MLX 等本地推理场景，每个任务适配器的 LoRA 权重已预先合并到基座模型中，生成独立的完整权重文件。每个任务（检索、文本匹配、分类、聚类）各对应一个独立仓库，推理时无需额外加载 LoRA，开箱即用。 
 llama.cpp (GGUF) 
 在 CPU 或边缘设备上运行量化模型，我们为每个模型提供 14 种 GGUF 量化方案，从 F16 到 IQ1_S，覆盖不同精度需求。 
 llama-server -hf jinaai/jina-embeddings-v5-text-small-retrieval-GGUF:Q4_K_M \ 
 --embedding --pooling last -ub 32768 MLX 
 面向 Apple Silicon 的原生推理。所有任务适配器均提供全精度、4-bit 和 8-bit 量化版本。 
 import mlx.core as mx 
 from tokenizers import Tokenizer 
 from model import JinaEmbeddingModel 
 import json 
 with open( "config.json" ) as f: 
 config = json.load(f) 
 model = JinaEmbeddingModel(config) 
 weights = mx.load( "model-4bit.safetensors" ) 
 model.load_weights(list(weights.items())) 
 tokenizer = Tokenizer.from_file( "tokenizer.json" ) 
 texts = [ "Query: What is machine learning?" ] 
 embeddings = model.encode(texts, tokenizer) 从 Hugging Face 下载： jinaai/jina-embeddings-v5-text-small-retrieval-mlx （文本匹配、分类、聚类适配器同样可用）。 
 训练方法 
 两个模型均从 Qwen3-Embedding-4B （一个参数量大得多的成熟向量模型）蒸馏而来。small 版本以 Qwen3-0.6B-Base 为骨干，nano 以 EuroBERT-210m 为骨干。训练过程结合了两路互补的监督信号： 
 第一 阶段：向量蒸馏（Embedding Distillation） 
 核心目标是让小模型（学生）无需指令模板，就能逼近 4B 教师模型的向量空间。 
 蒸馏阶段的训练数据涵盖超过 300 个数据集、30+ 种语言 的文本对。这一策略在标注数据稀缺的语言和任务上尤其有效， 教 师模型提供的监督信号弥补了标注数据的不足。 
 针对 v5-text-small，我们还进行了额外的 长上下文训练 ：使用专门构造的长文本数据集，降低训练时的 RoPE θ 值并扩大最大序列长度，获得更好的长文本外推能力。 
 第二阶段：任务专用对比学习（Task-specific Contrastive Loss） 
 蒸馏完成后冻结骨干权重，为四个任务类别分别训练 LoRA 适配器，每个适配器使用不同的损失函数和训练数据。 
 检索适配器在标注的 query-document 对上使用 InfoNCE loss，配合 hard negative mining 和 in-batch negatives，同时保留蒸馏损失，防止适配器训练偏离骨干已建立的向量空间。 
 消融实验表明，两种方法的组合稳定优于任一单独使用：MTEB 英文检索上，组合方案达到 60.1 nDCG@10 ，纯蒸馏 58.6，纯对比学习仅 54.3（同一骨干网络）。 
 训练中还引入了 GOR（Generalized Orthogonal Regularization，广义正交正则化） ，让向量在各维度上分布更均匀。GOR 对 benchmark 分数提升有限，其核心价值在于： 二值量化几乎无损 ，对于内存受限的部署环境下，这是个关键特性。 
 在训练过程中，我们还有几个重要发现： 
 蒸馏和对比学习的互补性远超预期。从 loss 组合中拿掉任何一个组件，全线性能立刻下降，没有冗余项。 
 任务专用 LoRA 适配器以几乎可忽略的参数开销，表现优于多任务联合训练。 
 GOR 正则化对 benchmark 提升有限，但能让二值量化几乎无损，移除 GOR 后，量化劣化增加超 50%。对实际部署的意义远大于全精度场景下那点边际收益。 
 结语 
 2026年，向量模型正在发生巨大的角色转型。 
 过去，向量模型作为独立的召回单元。今天，大模型在 Agentic 工作流中把向量模型当做小工具调用从而完成检索、记忆管理和分类。OpenClaw、OpenViking 等项目把向量模型当作 Agent 上下文管理的核心记忆层。 向量模型正在从搜索引擎的固定后端变成上下文窗口里的灵活小工具：去重、过滤、压缩 token，一切只为更好的 Context。 
 在这种范式下， 单次调用的推理成本和延迟跟 Benchmark 分数一样重要 。端侧检索、页内搜索、边缘部署，都要求模型塞进严苛的内存预算。Matryoshka 维度让一个模型同时覆盖高精度检索和超快近似搜索，无需重新训练；配合 GGUF 量化压到 1–2 bit，生产环境下向量服务的实际内存开销直降一个数量级。 
 v5-text 就是为这个趋势而生的：够小、够快、够准。 
 我们正在开发 jina-embeddings-v5-multimodal ，将同一架构扩展至视觉与跨模态检索。早期实验验证，在不损失文本性能的前提下对齐视觉编码器完全可行。敬请期待！ 
 阅读原文 
 跳转微信打开
```

---

## 8. 一文读懂 VLM 背后的视觉编码器

- 日期: 2025-12-31 18:53
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyODIxMjczMA==&mid=2247503100&idx=1&sn=6e75ff0c57a6738713e7efc0d1934c5d

```
Jina AI 德国 
 #科研论文解读 #视觉语言模型解析 
 论文地址：https://jina.ai/pdf/vision-encoder-survey.pdf 
 2025 年的最后一天，“多模态”无疑是今年模型的最大特点。24年底 OpenAI 和 Anthropic 的 Computer Use 让模型学会了操作界面，25年底 Claude Code 中开启 --chrome 后模型对着屏幕一顿疯狂截图。开源领域，从年初 DeepSeek-VL2 和 Qwen2.5-VL 到年底 DeepSeek-OCR，Qwen3-VL 和 InternVL 3.5 掀起新一轮的比赛。2026年，围绕着 GUI 自动化的 Agentic 应用势必井喷。这些能力的背后，都围绕一个基本问题：视觉语言模型 (VLM) 到底是怎么“看”图的？ 
 在发布 Jina VLM 后，我们静下心来把市面上70多个 VLM 拆开来看，发现了一件有意思的事：语言模型早就卷到千亿参数了，但视觉编码器这边，主流选择还是那几个：老炮儿 CLIP，Qwen2-VL 用6亿参数的 NaViT，LLaVA-OneVision 和 DeepSeek-VL2 都押注4亿参数的 SigLIP，InternVL 自研的 InternViT。有意思的是，4亿参数的 SigLIP 2 在很多数任务上打得过60亿参数的大块头。Scaling Law 不是万能的，怎么训，训什么才是关键。 
 在我们这篇30页的《Vision Encoders in Vision-Language Models》综述里，终于把视觉编码器的来龙去脉彻底讲清楚了：三种训练路线怎么选、分辨率该不该动态处理、多个编码器能不能拼着用、“无编码器”架构靠不靠谱。做多模态模型的可以拿来当选型参考，想搞懂技术演进的也能从中找到脉络。 
 最后，感谢大家这一年的陪伴，祝各位元旦快乐，2026我们接着舞。[烟花] 
 跳转微信打开
```

---

## 9. Jina-VLM：可在笔记本上跑的多语言视觉小模型

- 日期: 2025-12-09 12:01
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyODIxMjczMA==&mid=2247503043&idx=1&sn=a7038927b00f3993ae1afe77222f1c27

```
原创 Jina AI 2025-12-09 12:01 新加坡 
 又小又强，可本地跑到飞起的多语言视觉小模型 
 今天我们正式发布 Jina-VLM ，这是一款 2.4B 参数量的视觉语言模型（VLM），在同等规模下达到了 多语言视觉问答（Multilingual VQA）任务上的 SOTA 基准 。 
 面对小参数量 VLM 在增强视觉能力时容易牺牲文本表现、以及高分辨率图像推理成本高的问题 ，Jina-VLM 给出了自己的解法：我们引入了 注意力池化（Attention-pooling） ，连接 SigLIP2 视觉编码器与 Qwen3 语言基座，成功在支持 29 种语言的同时，实现了对任意分辨率下自然图片和文档图片（如扫描件、ppt、表图）上的问答、理解、提取任务的高效处理。 
 Jina-VLM 对硬件需求较低，可在普通消费级显卡或 Macbook 上流畅运行。 
 论文 ： https://arxiv.org/abs/2512.04032 
 Hugging Face : https://huggingface.co/jinaai/jina-vlm 
 魔搭社区 ： https://modelscope.cn/models/jinaai/jina-vlm 
 原文链接 ： https://jina.ai/news/jina-vlm-small-multilingual-vision-language-model/ 
 核心性能对比 
 在 VLM 领域，参数量往往决定了性能天花板，但 Jina-VLM 证明了架构优化可以突破这一限制。如下表所示，Jina-VLM 在多项关键基准测试中均优于同量级的 Qwen2-VL 和 InternVL 系列。 
 模型 
 参数量 
 VQA 均分 
 MMMB 
 Multi. MMB 
 DocVQA 
 OCRBench 
 jina-vlm 2.4B 72.3 78.8 74.3 90.6 
 778 
 Qwen2-VL-2B 
 2.1B 
 66.4 
 71.3 
 69.4 
 89.2 
 809 
 Qwen3-VL-2B 
 2.8B 
 71.6 
 75.0 
 72.3 
 92.3 858 
 InternVL3-2B 
 2.2B 
 69.2 
 73.6 
 71.9 
 87.4 
 835 
 InternVL3.5-2B 
 2.2B 
 71.6 
 74.6 
 70.9 
 88.5 
 836 
 不管是在标准的 VQA 任务、多语言多模态理解（MMMB、MMBench），还是在 OCR 和纯文本任务上， Jina-VLM 都是同规格模型里最优级别的表现 ，且同时具备 在 消费级硬件友好 的推理效率。 
 多语言理解 (MMMB SOTA) ：在阿拉伯语、中文、英语、葡语、俄语和土耳其语等 6 大语种的测试中，Jina-VLM 以 78.8 分领跑，展现了卓越的跨语言视觉推理能力（见图 1 & 图 2）。 
 视觉问答 (VQA) ：面对涵盖图表 (ChartQA)、文档 (DocVQA)、场景文本 (TextVQA) 和科学图表 (CharXiv) 等高难度测试中，模型表现稳健（见图 3）。 
 视觉增强，语言无损 ：很多 VLM 在增强视觉能力后会牺牲文本智商。得益于特殊的训练策略，Jina-VLM 在 MMLU（知识）和 GSM-8K（数学）等纯文本任务上，几乎完整保留了 Qwen3 基座的强悍性能（见图 5）。 
 核心挑战 
 在设计 2B 参数量级的 VLM 时，我们面临一个核心的工程矛盾： 看得清（高分辨率）往往意味着算不动（Token 爆炸）。 
 传统的 Vision Transformer (ViT) 处理高密度扫描件、复杂 PPT 时，一般是图像切分为多个图块（Tiles）。按 378×378 来算，一张高清大图（12 切片 + 1 缩略图）会产生近 9500 个视觉 Token。这在 Transformer 架构下，Token 数量的增加会导致计算量呈平方级爆炸。 
 Jina-VLM 将输入端的动态切片与模型端的智能压缩结合起来 ：既保留高分辨率的视觉信息，又把下游语言模型看到的视觉 Token 数量压缩约 4 倍。既看得清，也算得动。 
 Jina-VLM 架构图，展示了从 SigLIP2 视觉编码器 → VL-Connector → Qwen3 语言基座 的数据流 策略 1：动态重叠切片 (Dynamic Overlapping Tiling) 
 为了适配 SigLIP2 的固定输入尺寸，并保留细节，我们采用了 动态重叠切片（Dynamic Overlapping Tiling） 策略。 
 1. 全局缩略图 ：不管原图多大，先生成一张缩略图，让模型能掌握整张图的总体布局。 
 2. 动态滑窗切片 ：利用滑动窗口将原图切分为多个 378×378 的图块（默认最多 12 块）。关键在于， 我们在图块之间预留了 112 像素的重叠区 ，确保跨图块的文字或物体不会因分割而导致特征断裂。 
 这一步解决了“看得清”的问题，但也导致了 Token 数量的激增。解决这一负载压力的关键，在于接下来的视觉-语言连接器（VL-Connector）。 
 策略 2：注意力池化连接器 (Attention-Pooling Connector) 
 这是 Jina-VLM 的核心创新。与业界常见的 Q-Former（破坏空间结构）或平均池化（丢失细节）不同， 我们设计了 2×2 注意力池化 机制，实现了 4 倍无损压缩 ： 
 A. 双层特征拼接 (Layer Concatenation) 
 大多数模型只取视觉编码器的最后一层输出，Jina-VLM 提取并拼接了两层中间特征： 
 第 18 层：提供细粒度的视觉细节，如 清晰的文字边缘/图表曲线。 
 第 24 层：提供高度抽象的语义信息，如物体类别、场景。 
 通过拼接(concat)这两层特征，模型既能理解“这是什么”（语义），也能看清“它长什么样”（细节），为后续处理提供了信息密度极高的输入。 
 但拿着双倍的信息量，Token 不是更多了吗 ？ 
 B. 注意力池化（Attention Pooling） 
 这里是 Jina-VLM 解决视觉 Token 爆炸的关键，我们在连接器中引入了注意力池化机制，实现 4 倍无损压缩： 
 该机制的核心在于 特征的智能聚合 ，其工作流如下： 
 领域划分 ：将 SigLIP2 输出的特征图划分为互不重叠的 邻域（Patch Neighborhoods）。 
 特征聚合 ：模型首先计算这四个 Patch 的特征均值作为 查询向量 (Query) ，通过注意力机制计算 Patch 的权重。如果一个 区域里同时包含有效消息（如 文字/曲线） 和纯白背景时，注意力机制自动赋予前者更高的权重，同时抑制背景噪声。 
 投影对齐 ：聚合后的特征通过带有 SwiGLU 激活函数的 MLP 层投影至 Qwen3 的向量空间。 
 通过这一设计，单个切块(Tile)的输出从 729 个 Token 无损压缩至 182 个。 虽然数量减少，但因为严格保留了 Grid（网格）拓扑结构，模型对文档版面、图表坐标的空间感知能力不会受损。 
 实测数据对比（以 12 Tile 输入为例）： 
 指标 
 优化前 (Baseline) 
 Jina-VLM (With Pooling) 优化效果 
 视觉 Token 数 9477 
 2366 减少 4.0× 
 LLM Prefill 计算量 27.2 TFLOPs 
 6.9 TFLOPs 降低 3.9× 
 KV-Cache 显存占用 2.12 GB 
 0.53 GB 节省 3.9× 
 注：视觉编码器的计算量相对固定，不受 Token 数量影响。我们的优化主要体现在语言模型（LLM）的推理阶段，这个是 VLM 部署成本的大头。 
 训练流程：对抗灾难性遗忘 
 在 VLM 的研发里，业界长期面临一个零和博弈， 模型在努力适应新模态时，往往以牺牲原本的文本推理能力为代价， 这就是 灾难性遗忘（Catastrophic Forgetting） 。 其最直接的表现，就是模型在理解图片后，其多语言能力发生退化 (Multilingual Degradation)，甚至连基础的纯文本逻辑 推理 都变得脆弱。 
 Jina-VLM 采用 两阶段训练 + 持续纯文本注入 （Text-only Data Incorporation） 策略。在覆盖 29 种语言、约 500 万张图像和 120 亿文本 Token 的训练规模下，我们的核心目标是：在最大化视觉语义对齐的同时，严格保全语言基座的通用性能。 
 训练数据中英语占一半，此外还包括中文、阿拉伯语、德语、西班牙语、法语、意大利语、日语、韩语、葡萄牙语、俄语、土耳其语、越南语、泰语、印尼语、印地语、孟加拉语等多种语言。 
 第一阶段：语义对齐 (Alignment) 
 第一阶段的主要任务是把 SigLIP2 的视觉特征映射到 Qwen3 的文本向量空间。训练数据主要来源于 PixmoCap 和 PangeaIns 等高质量字幕数据集。 
 这里最关键的一点是， 我们在训练数据里强制注入了 15% 的纯文本数据。 这么做不是为了灌输新知识，而是为了防止模型在学看图的时候把原来的语言习惯给忘了。 
 配合这个思路，我们对模型的不同部分采用了不同的学习节奏：负责连接视觉和语言的组件（Connector）学习率设得很高，让它快速收敛；而原本的大模型基座学习率压得很低，让它在接受新模态信息时保持稳定，尽量不破坏已有的知识结构。 
 第二阶段：指令微调 (Instruction Tuning) 
 到了第二阶段，我们要提升模型的指令遵循能力，比如在 VQA、OCR 和数学推理等特定任务上的表现。 由于训练数据涵盖学术问答、文档理解、图表推理等多种场景，异构性极高，容易在初期造成梯度不稳定。对此，Jina-VLM 采用了 先分后合的渐进式策略： 
 先使用单源数据，让模型在相对单纯的环境里，快速掌握各类任务的特性（如 OCR 的字符识别、ChartQA 的逻辑推理）。再进行多源数据混合训练，让模型学会融会贯通，处理复杂的跨任务场景。 
 整个过程中， 纯文本的指令数据始终伴随着训练 ，确保模型在处理多模态任务时，其纯文本的推理与知识检索能力不发生退化。 
 训练效果 
 凭借这一精细的训练控制，Jina-VLM 不仅在 MMMB 等多语言视觉榜单上达到 SOTA，更关键的是，在 MMLU（通用知识）和 GSM-8K（数学推理）等纯文本基准测试中，它几乎完整保留了 Qwen3-1.7B 基座的性能，真正实现了 视觉增强，语言无损。 
 快速上手 (Getting Started) 
 1. 使用 Jina API 
 我们在 https://api-beta-vlm.jina.ai 上线了兼容 OpenAI 接口规范的 API 服务， 支持流式输出与 Base64 图像输入。 
 Format 
 Example 
 HTTP/HTTPS URL 
 https://example.com/image.jpg 
 Base64 data URL 
 data:image/jpeg;base64,/9j/4AAQ... 
 通过 URL 处理图像： 
 curl https://api-beta-vlm.jina.ai/v1/chat/completions \ 
 -H "Content-Type: application/json" \ 
 -H "Authorization: Bearer $JINA_API_KEY " \ 
 -d '{ 
 "model": "jina-vlm", 
 "messages": [{ 
 "role": "user", 
 "content": [ 
 {"type": "text", "text": "描述这张图片"}, 
 {"type": "image_url", "image_url": {"url": " https://example.com/photo.jpg "}} 
 ] 
 }] 
 }' 本地图片 (base64) 
 curl https://api-beta-vlm.jina.ai/v1/chat/completions \ 
 -H "Content-Type: application/json" \ 
 -H "Authorization: Bearer $JINA_API_KEY " \ 
 -d '{ 
 "model": "jina-vlm", 
 "messages": [{ 
 "role": "user", 
 "content": [ 
 {"type": "text", "text": "What is in this image?"}, 
 {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,' $(base64 -i image.jpg) '"}} 
 ] 
 }] 
 }' 纯文本查询 
 curl https://api-beta-vlm.jina.ai/v1/chat/completions \ 
 -H "Content-Type: application/json" \ 
 -H "Authorization: Bearer $JINA_API_KEY " \ 
 -d '{ 
 "model": "jina-vlm", 
 "messages": [{"role": "user", "content": "What is the capital of France?"}] 
 }' 流式输出 
 只需添加 "stream": true ，在生成同时接收 Token： 
 curl https://api-beta-vlm.jina.ai/v1/chat/completions \ 
 -H "Content-Type: application/json" \ 
 -H "Authorization: Bearer $JINA_API_KEY " \ 
 -d '{ 
 "model": "jina-vlm", 
 "stream": true, 
 "messages": [{"role": "user", "content": "Write a haiku about coding"}] 
 }' 如果遇到服务冷启动，API 可能会返回如下 503 错误： 
 { 
 "error" : { 
 "message" : "Model is loading, please retry in 30-60 seconds. Cold start takes ~30s after the service scales up." , 
 "code" : 503 
 } 
 } 此时服务正在自动扩容，稍作等待后重试请求即可。 
 2. 通过 命令行工具调用 
 我们的 HuggingFace 仓库包含一个 infer.py 脚本，用于快速测试： 
 # Single image 
 python infer.py -i image.jpg -p "What's in this image?" 
 # Streaming output 
 python infer.py -i image.jpg -p "Describe this image" --stream 
 # Multiple images 
 python infer.py -i img1.jpg -i img2.jpg -p "Compare these images" 
 # Text-only 
 python infer.py -p "What is the capital of France?" 3. 使用 Hugging Face Transformers 
 Jina-VLM 现已开源并集成至 Hugging Face 生态。 
 from transformers import AutoModelForCausalLM, AutoProcessor 
 import torch 
 from PIL import Image 
 # 加载模型 (支持 bfloat16 精度) 
 model = AutoModelForCausalLM.from_pretrained( 
 "jinaai/jina-vlm" , 
 torch_dtype=torch.bfloat16, 
 trust_remote_code= True , 
 device_map= "auto" 
 ) 
 processor = AutoProcessor.from_pretrained( "jinaai/jina-vlm" , trust_remote_code= True ) 
 # 推理示例 
 image = Image.open( "document.png" ) 
 messages = [ 
 { 
 "role" : "user" , 
 "content" : [ 
 { "type" : "image" , "image" : image}, 
 { "type" : "text" , "text" : "这份文档的主题是什么？" } 
 ] 
 } 
 ] 
 inputs = processor.apply_chat_template( 
 messages, add_generation_prompt= True , tokenize= True , return_tensors= "pt" 
 ).to(model.device) 
 outputs = model.generate(**inputs, max_new_tokens= 256 , do_sample= False ) 
 print(processor.decode(outputs[ 0 ], skip_special_tokens= True )) 总结与展望 
 Jina-VLM 强有力地证明了， 通过精妙的架构设计与训练策略，小参数量 VLM 完全可以具备卓越的跨语言视觉理解能力 。我们的注意力池化连接器（Attention-pooling connector）在几乎不牺牲精度的情况下，在将 Token 数量大幅削减 4 倍；而在多模态训练中策略性地混入纯文本数据，则成功保全了模型原本容易发生退化的语言能力。 
 当然， 任何架构设计本质上都是一种 trade-off ： 
 切片机制的代价 ： 超高分辨率场景下，切片数量一上来，计算成本随之线性抬升，这是硬成本。另外， 切片会把一个完整物体切碎，跨切片的对象计数、空间关系和场景一致性都会被削弱。虽然全局缩略图能兜底，但在需要原生细节与全局一致性同时在线的任务上（比如计数）， 原生分辨率方案或许才是更好的解法。 
 多图推理的短板 ： 多图任务的标注数据稀缺 ，导致模型在多图基准测试上的表现略显单薄。另外， 为了更快的 VQA 响应速度，我们在训练中倾向于短链条推理，这在一定程度上限制了模型在 长链路多步推理（CoT）上的表现。 MMLU-Pro 分数的下滑就是这一设计取舍的直观体现。 
 未来的工作，我们将致力于探索更高效的分辨率处理机制，并验证这套多语言训练配方能否成功迁移至更大规模的模型中。 
 阅读原文 
 跳转微信打开
```

---

## 10. Jina AI创业复盘：AI团队的Scaling Law是什么

- 日期: 2025-12-02 12:31
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyODIxMjczMA==&mid=2247503019&idx=1&sn=2b149d7309d86a20fbd07eee4f55d639

```
原创 Jina AI 2025-12-02 12:31 新加坡 
 从零到被上市公司收购，他最大的遗憾不是技术，而是没能解开AI团队的Scaling Law 
 “满分 10 分，我给这六年打 7 分。” 
 没有吹嘘，也没有谦虚。 
 从创立到出售，差两个月满六年。2025 年 10 月，肖涵把 Jina AI 卖给了美国上市公司 Elastic （NYSE: ESTC）。他率领核心团队加入 Elastic，并担任 VP of AI。 
 六年里，AI 技术的发展速度快到令人窒息：微服务架构失宠，ChatGPT 重塑行业，大模型你追我赶，RAG 几度生死轮回 ，模型的半衰期仅几个月。 不跑着，技术资产半年后价值归零。 
 他跑了六年，中途 Pivot 两次 ：砍掉分散精力的项目，裁撤一半的员工，离开欧洲，重心移向硅谷，All in 搜索底座模型。他说：“当没有壁垒时，极致的聚焦和近乎独裁的执行力，就是唯一的壁垒。” 
 他说这是一场鱿鱼游戏。他活到了最后，但不是没有遗憾。 
 与此同时，我也在这家公司经历着自己的三年。 
 我叫张飒 ，2022 年入职 Jina AI，负责产品运营。上个月随收购从北京搬到新加坡。作为毕业后的第一份工作，Jina AI 是辆刹不住的车。兴奋、疲惫、彷徨、庆幸，四挡双离合。 我见过老板凌晨三点还在提交代码；也记得团队围在一起为第一笔 10 美元击掌相庆；更熟悉那种刚备好的物料因战略调整而作废、刚记牢的卖点因产品迭代要推翻重来的无奈。 
 后来模型被市场认可了，收购消息落定了，我才明白一件事：当时我眼里的折腾，其实是老板在 AI 浪潮里的求生动作。 
 以下是我和 Jina AI 创始人肖涵 的一次长谈，关于他六年创业的得与失。 
 张飒：六年来，您给这段 Ji na AI 创业 经历打几分？满分 10 分的话？ 
 肖涵： 我觉得 7 分的样子吧 。 
 从 2020 年疫情期间开始，我从零组建一个团队，经历了不少波折，到 2025 年 10 月份成功卖给一个美国上市公司。这段创业经历算是我到现在为止比较自豪的事情， 第一次创业就成功退出，也让一直跟着我的团队有了一个比较好的出路 。 不过多少在一些事情上还是有些遗憾。 
 张飒：六年算长么，您觉得？ 
 肖涵：跑的时候其实没感觉，跑完停下来才发现嚯跑了这么久。 
 张飒 ：关于 Jina AI 您最早的记忆是什么 ？ 
 肖涵：记得 2019 年圣诞节前，我在深圳海岸城那边一个酒店行政酒廊里和投资人第一次 pitch(路演)，后来在上海安福路上的 Costa 咖啡厅里，修改 PPT 去给 IC (投委会) 讲。这大概是我关于 Jina 最早的记忆。 
 张飒 ：其实我一直比较好奇，Jina AI 这个名字是怎么来的？ 
 肖涵：我当时是想找一个人工智能的名称，像钢铁侠里 Jarvis 的那种，但同时要满足几个条件： 
 一是要感觉 中性化、女性化一些，更加有亲和力、少一些侵略性 。 第二是要让这个名字在各个语言中读法都大致相同，三是 SEO 要比较好做一些。 
 当时 shortlist 里几个名字，最后选择了 Jina，简单、好记也好读。感觉像是 Jarvis 的女友一样。另外当时做 SEO 的时候发现 Jina 这个名字只有一些韩国人在用，所以觉得 SEO 做起来也比较容易，可以很轻松的排在 Google 搜索的前面。 
 中文名称我叫做 极纳 ，意思是 “极深研几” 、 “海纳百川” ，算是搜索和索引擦上边，同时“极客”也是我们公司文化的一部分。 
 张飒 ：Jina 从 2020 年成立到现在，我们做的事情都有哪些？我有些朋友很早关注 Jina，更多朋友最近两年才关注 Jina，感觉大家对 Jina 的认知并不相同？ 
 肖涵：是的。我们中间有过几次 pivot 也就是“转型”，但总体来说都是围绕 Neural Information Retrieval 这个大的主题中做上下游调整。 
 2020 年 2 月成立到 2023 年 2 月我们一直在做一套软件框架，帮助开发者去更快的实现语义搜索。角色上有点像 Elasticsearch 和后来的 Langchain，LlamaIndex 这些，聚焦在工具链、糖水代码和脚手架上。 
 2023 年是我们比较混乱的一年，因为 2022 年 12 月 ChatGPT 的发布， 我当时察觉到之前做的框架不再被社区关注 。 那时公司内部连续开了好几次全员会，讨论接下来该做什么。 
 所以在 2023 年一年里尝试了两个不同的新方向：一个是走 Wrapper(套壳)路线，通过构建 prompt-based 的生产力工具，我内部称为 Thin Strategy。还有一个方向是走 Search Model 的路线，从训练自己的 Embedding 向量模型开始，夯实搜索的基础技术，我称为 Fat Strategy。 
 2024 年 2 月，我停止了所有的 Wrapper 路线的推进， 一股脑地押在了搜索模型的研发上 ，并重塑了新的叙事逻辑： Search Foundation Models（搜索底座模型） 。 这就是今天大家所看到的 Jina AI—— 从多语言到多模态， 前后四代共 20 个 向量模型 、重排器、Reader 等 搜索侧 小模型，14 篇会议论文，HuggingFace 上每月五百万次的下载量以及 API 上每天超 200 billion tokens 的用量。 
 张飒 ：所以 2023 年是对 Jina 来说重要的一年？ 
 肖涵：是的，2023 年还有 2024 年年初，这两个时间点现在回顾起来都非常重要。 
 2023 年的那一次转型意味着放弃之前的软件框架性工作，完全重新审视 ChatGPT 和 Gen AI 对于搜索业务的影响。这个对于公司花了两年多构建起来的技术栈和文化是一次比较大的冲击，内部从上到下也有很多人不理解为什么不继续坚持下去。同时还要去努力想新的出路。 
 不过 2022 年年底 ChatGPT 的发布对于整个软件业都应该是一次比较大的冲击，基本重新定义了 AI 业务。所以如果有初创公司说我在 2023 年没有任何反思和焦虑我是不相信的， 除非你不读新闻，不闻窗外事，否则很难不对自己所做的工作的价值有所怀疑 。FOMO （错失恐惧症）是我们 2023 年挂在嘴边最多的词。 
 2024 年 2 月那次转型是需要为向量模型、重排器等找到 一个统一的 叙事逻辑 ，从而实现公司产品线上的聚焦，所以也非常重要。 
 张飒 ：2023 年之前 Jina AI 创业一开始做的那套搜索框架是什么呢？ 
 肖涵：我们公司是 2020 年起来的嘛，2020 年当时很流行 Microservice + Orchestration 这一套云原生的技术栈。所以我们当时用 Python 实现了一套相对完整的微服务部署框架，可以使得多模态搜索中涉及到的每一个模块，比如向量化、预处理、打分、索引等等都可以被微服务化及自由的扩容。 
 当时围绕着这个理念开发了很多开源软件，比如 DocArray 等，相当于后来的 Pydantic，让用户设计自己的多模态文档结构以方便搜索。还有一些 Docker 容器化的实现，后来也有被 Replit 的一些设计所参考。 
 其实早在 2021 年我们也有涉及到一些模型层面的研发，不过主要是围绕 BERT，CLIP 这类模型的微调框架，叫 Finetuner， 内置了一些简单的微调策略和 Training loop 的实现，以糖水代码为主，最终效果并不保证。功能和定位上 有点像今天的 SentenceTransformers 那个库。 
 2022 年年底前我们所有的工程项目，试图去囊括整个 AI 搜索的 Ops。靠开源社区的增长计算 ROI，纯研发零收入，用爱发电也是当时很多商业化开源软件初创公司的早期打法。 
 不过总体来说这套框架在 2022 年年底的社区增长开始停滞， 我自己也用的越来越少，2023 年之后基本没有再用过这些框架实现任何东西 。 当时察觉到社区更需要一种轻量级的搜索开发体验，方便大家替换 LLM、迭代 prompt 和 Vibe 测试 RAG 的输出，所以像 Langchain, LlamaIndex 这种就在 2023 年初就非常受欢迎。 
 张飒 ：那您后来用过 Langchain, LlamaIndex 开发么？ 
 肖涵： 没，一次都没。 
 我自从在 2023 年否定了我们公司自己的框架之后， 我就 对所有 胶水和糖水代码丧失了兴趣 ， 也不看好任何框架。尤其是站在 2025 年的今天去看，当大部分代码都可以用大模型直接生成时，学习那些胶水代码和 Opinionated Framework 的必要性也没有了。 
 说白了，除非这些框架和硬件特性强绑定，比如 Google SDK 和谷歌云绑定，CUDA和英伟达的 GPU 绑定， 不然对于开发者来说，完全没有必要去花时间学习一个中间层，无论这个中间层的作者是网红还是谁。 
 张飒 ：您说 2023 年的时候曾经尝试了两个不同的新方向，为什么选择最后做模型呢？ 
 肖涵：我们当时内部分成两组：一部分人在做基于 Prompt 的 AI 的生产力工具，涉及到很多有意思的 Prompt 工程技术。我当时的想法是通过 UI/UX 的方式去呈现一些生产力 API。同时这也第一次开始尝试商业化和营收。我当时带着团队花了不少精力在这些 Webapp 里去嵌入 Paywall，设计 Stripe 支付 API 和用户转化漏斗等等。当第一次看到 Slack 里提示 10 美元收入到账，大家都非常兴奋。 
 我记得我们当时一年做了有五六个 App，虽然这些后来全部被我砍掉了，但是这段商业化的经历和对 Token Economy 的初探对于我后来在为模型设计 Paywall 有不少借鉴和启发。 
 2023 年我们在迷茫期做的 5 个 Gen AI 向的 Web 端应用，旨在通过 Prompt 提高生产力。这些 App 多少带来了新生用户和营收，不过在 2024 年都被一股脑砍掉了。 
 之所以后来没有继续做这个方向， 主要是发现公司内部的基因不太适合做带有 UI 的产品 ， 大家虽然是在每天开发，但每天去用这些 App 的基本没有。我觉得要做到一个好的 App，UI/UX 的设计和细节非常重要，因为它承载了产品的叙事逻辑。 如果自己开发的 App 自己不用，那么很多设计和逻辑问题就很难被发现和优化。 
 总而言之，To C 端 App 的基因和文化在我们公司并不存在，这个和我们招聘对象有关 。 
 第二就是这些 App 虽然多多少少有些营收，但他们之间缺乏一个统一的叙事逻辑。因此从外面看来感觉非常散，弱化了 Jina AI 这个品牌形象，对于一个 startup 来说这是非常致命的。 
 张飒 ：您选择了模型这条路而砍掉 Wrapper Apps 这条路，这个决定在内部执行起来是不是很难？ 
 肖涵：有不少阻力。 
 一方面，Wrapper Apps 这边开发迭代速度快，还各自带着一定营收，对于一个没怎么接触过商业化的团队来说是一个鼓励和教学作用。但问题在于 Wrapper Apps 之间缺乏统一叙事逻辑，看上去像是打一枪换一个地方。 
 另一方面，模型侧讲究慢工出细活，开发速度要比 Wrapper Apps 慢很多，所以两个团队在文化和节奏上很不同。我们在 2023 年 10 月份开源的 jina-embeddings-v2 因为其 8K 长文本 和比肩 OpenAI text-ada002 的性能在 Hacker News 上一夜爆火，出乎我的预料，同时也给了模型团队很大的信心。 
 2023 年末我们公司的一个宣传单，可以看到 Embeddings 的产品线已经初成，但我并没有完全转向模型，而是仍然在推广 PromptPerfect 和 SceneXplain 这两个 AIGC 的 App，原因大概有二：一是搜索底座模型的叙事逻辑尚未形成，二是 AIGC 的有一定营收舍不得放弃。 
 但同时维护两个方向对于一个初创来说并不是一个好故事。最终在 2024 年 2 月，在我到了美国湾区之后，决定完全停止 App 的开发，重新整理团队，优化人员从而完全聚焦在模型层的研发。 
 那几个月里， 我把公司从 60 多人砍到 30 多人，网站上移除了所有 App 的信息，目的只有一个：聚焦。 
 张飒 ：从外部看来，感觉 Jina AI 从 2024 年起像变了一个公司，所以您觉得是因为什么呢？是因为您在美国的原因么？ 
 肖涵：我会说从 2024 年起 Jina AI 变得非常 lean & mean, based, no bullshit 。 
 有了之前 2020-2022 年框架没人爱，2023 年的 App 过于分散的教训，我意识到 初创公司的叙事逻辑非常重要 ： 框架有 Bug 可以改，模型落后了可以追，App 活跃度下降了可以营销，但如果整个公司缺乏一个清晰的叙事逻辑，那崩溃就早已注定。而且逻辑越简单越好，不要搞什么二阶高阶逻辑。 
 这其中有不少我在美国湾区时受到的影响和反思。这也离不开 2023 年圣诞节时我看的几本书： Richard Koch 的《80/20 法则》， Al Ries 的《22 条商规》和 Richard Sutton的《苦涩的教训》 。 
 我意识到公司需要从内到外实现一次重新的聚焦， 要去除掉 80% 的方向、管理、人员、营销去认真寻找那最关键的 20% 。 在湾区时我走访了很多优秀的初创公司，对于他们非常 lean 的团队文化也非常有感触。 
 再加上整个湾区 2024 年初开始在 Elon、Trump、Peter Thiel 还有 Marc Andreessen 的影响下，文化上已经开始偏右和加速主义，我记得当时在湾区听得最多的一个词是 e/acc (有效加速主义） 。整个 24 年 我 还特意把这个 e/acc 作为我 Twitter 和 Slack 的签名档，提醒自己不要被一些虚头巴脑的东西所拖累和浪费时间，要专注有效的创新。不过在 2025 年的今天提 e/acc 词的人要少了很多，估计是大家已经被加速到麻了。 
 总而言之，从 2024 年以来，我就在公司组织上把架构压到最扁平， 去除掉所有的 message-passer 和无效管理层，全员 Heads Down 和 Hands On 。 
 我的目标是把 Jina AI 重新打造成一个搜索领域的 Premium Brand，比如我们要坚持慢工出细活，每发布一个模型的同时要发表一篇学术论文；在研究的静默期， 用高质量的 Blog 去代替一些短平快赚噱头的网络营销 。 
 张 飒：可是训练模型容易么？应该比做应用更难吧？ 
 肖涵：确实难，所以做的人少。 
 尤其是当我们聚焦在高质量的搜索小模型上时，其实竞争对手就变得非常清晰了：Voyage, Google, Cohere, Mixbread, Nomic AI 基本就这么几家。 
 Voyage 和 Cohere 都是闭源模型，Google 和 Cohere 又在想打大模型的仗所以没有 100% 聚焦在搜索小模型上。Mixbread 和 Nomic AI 社区相对比我们小一点，但也提供非常优秀的开源向量模型和重排器。 
 我觉得理清竞对关系很重要。 初创公司绝对不能逃避和害怕竞争，而要直面竞争。但上场前一定要选对竞争对手 ， 不然瞄准错误的对手一顿疯狂输出，完全是浪费精力。 
 从开源社区的角度，千问团队也算是竞争对手之一，他们今年出的开源的 qwen-embedding 和 qwen-reranker 在开源社区中对我们有不小影响。虽说千问并不靠这些模型来赚钱（而我们靠），但在开源社区中还是从我们这拿走了不少关注度。无论是千问还是北京智源的 bge，对我们属于亦敌亦友：有竞争，也有很多被我们学习和借鉴的地方。 
 张飒 ：既然千问也可以做向量模型，Gemini 也可以做向量模型，那 Jina 这种专注从零到一做搜索小模型的公司和大模型公司相比优势又在哪呢？ 
 肖涵：我一直信一句话： 当一个公司没有任何的上下游供应链优势和技术壁垒时，唯一的壁垒来自于其自身高效的运营。 这就是我悲观的 “壁垒底线” ：如果我们什么都不行，那么就通过最大化聚焦和近乎独裁的管理方式让团队跑步前进。 
 我已经准备好了最悲观的打法，但实际情况也没有那么悲观： 
 第一我们多年以来积累了不少高质量的标注数据，团队内部有不少欧洲人，所以对于欧洲多语言召回模型的手工评测和标注有比较多的积累。 
 第二我们有不少的客户群体，这其中包括 Jina Reader 带来的将近 1 万大大小小的付费客户，他们每天贡献了将近 200 billion tokens 的 API 使用量，每天我们收到不少付费客户的反馈和建议，都有效的帮助我们改进模型性能和 API 设计。 
 第三就是多年来在搜索模型训练上的经验积累和对技术进展的敏感度，知道什么时候该 early stop，什么时候该深挖进去，最近有哪些新技术方向，有哪些是噪音。 
 我觉得今天一个模型的 “半衰期”差不多是五六个月 ，也就是说每半年这个模型的价值就减半。一年后这个模型基本就没啥应用价值了，会有更好的模型取代它。所以这个竞争优势也是一个动态变化的过程。 
 我觉得争第一固然很重要，能争到第一是最好的，但 B e always part of the game 不放弃 ，也非常重要：比如我 24 年给团队定的目标是当“百事可乐”，当行业老二，让人记住先。 
 最后一点对于很多技术人员来说可能有点玄乎，就是 模型的调性和品牌价值 。 在模型日新月异的今天，培养用户在品牌上的忠诚度就非常重要，这就是品牌价值。而简单来讲 ， 品牌价值 = 技术 + 营销（比如技术博客、学术论文）+ 客户体验（网站、API） 。 
 比如很多人都说保时捷卡宴就是换壳的大众途锐和奥迪 Q7，因为底盘都差不多。可大家还是喜欢保时捷多一些，因为多年来保时捷偏向运动的底盘发动机调教风格，以及其宣传下的赛车血统的传承和稀缺性。 
 2024 年年底我们发布的年刊《Re·Search》，意在 Rethink Search，也有 Research 的意思。其中 精选了我们 24 年发表的技术博客。这本“小红书”因为其设计风格和扎实的内容给用户留下了很深刻的印象，也强化了 Jina AI 品牌的调性。 
 张飒 ：2024 年秋天我记得当时您接受 Paperweekly 有篇采访是关于搜索小模型的未来，您觉得那些观点今天还适用么？ 
 肖涵： 那是去年九月份的吧 ，到现在一年多，其实大部分仍然适用。 
 比如我当时说 小模型并不是天生小，而是从大模型中蒸馏和剪裁出来的 ， 这就意味着那些大模型厂商如果做起小模型会有不少优势，因为他们知道原厂模型的 vibe，该剪哪裁哪。结果今年就应验了，千问和 Gemini 果然就这么做了。 
 和去年那篇观点不同的是，在 Agentic search、DeepResearch 这种 2025 年新的设计模式的影响下，很多传统的向量召回模型（包括重排器）的使用场景发生了变化。 
 之前这些召回模型更多的是面向数据库的 I/O，动辄数百亿的量。 今天可能更多的是被当做小工具在上下文窗口中做 Context Engineering，比如去重、过滤、压缩 token。 这就需要模型的参数量更小速度更快，也需要模型在一些之前被忽视的任务上（比如 STS 任务，专门为去重）去做优化。 
 张 飒：我们聊聊这次收购吧，最开始您是怎么接触到买方的？ 
 肖涵：我应该是 23 年底第一次和 Elastic 合作。当时他们看到我们的 jina-embeddings-v2 不错，想做个 API Integration，我们就共建了个 Slack Channel 开始互通。 
 24 年我来湾区后，在他们三番办公室见了他们的管理层，随便聊了聊工作生活的话题。今年夏天在美国时，又和他们的管理层聊了不少次，在三番办公室里给他们的创始人、CEO、CPO 等做了几个小时的演讲，觉得相互之间的技术都高度互补，Elastic 的高层对我个人非常友好和信任，于是就开始了这个收购案。 
 总体来说， 前期铺垫、信任基础、方向互补和一定的运气 都 是促成收购非常重要的条件。 
 张飒 ：其实我们很多人对收购没有概念，您能简单讲讲这个过程么？ 
 肖涵：收购非常复杂和繁琐，尤其当买方是美国上市公司，法律规范非常多， 真是收购一次掉层皮 。 一般来讲，这种收购是需要请一个专业投行 M&A 团队去操作，我却比较 lean/吝啬，完全靠自己“手搓”，结果还真搓了出来，也算是一段难忘的经历。 
 对于 Jina AI 而言，这其中包含很多的复杂的因素，包括美国和中国之间的地缘政治（当然还有德国），多个买方之间的博弈，买卖两方的博弈，投资人之间的博弈，还有内部员工之间的博弈。而且由于买方是上市公司，所以收购时间线上还和他们的季度财报和 Analyst Meeting 的举办绑定。 
 所以从我 7 月份签署 LOI (Letter of intent) 到 8 月份准备 data room 做 SPA（股权收购协议），到 9 月份去开始协调 SPA 上各方签署，签署完要马不停蹄的执行交割先决条件，员工或 Relocate 或重签 Offer，再到最终 10 月份在美国纽约的官宣。这几个月来我和我的律师殚精竭虑、跨时区一天好几个会议的沟通，当然买方律师也是一样。其实直到今天，仍然有不少 Post Acquisition 的工作在做，主要是因为 Jina 这几年来在多个国家设有办公室，所以需要一个一个处理。 
 总体而言，我觉得 Jina AI 从架构上 Overengineer 了很多，我们一个不到 30 个人的公司， 因为 公 司架构设计得过于复杂，导致收购起来跟买一个几百人的跨国公司似的 。 
 然而 最累的是处理在收购过程中展现出的一些人性问题 ， 在巨大的时间压力下我一个人代表公司去和内外多方博弈，也是我多年以来承受压力最大的一次经历。 
 张 飒：所以您觉得 Model as Product 的公司的终局就是被收购么？ 
 肖涵：差不多。要么 pivot 去做产品和应用。要么去做通用大模型去拿融资去上市。 
 如果只是做特定领域的小模型，比如搜索，无论是 Voyage 还是 Jina，其实最终都走到了被收购这条路。原因也很简单： 小模型的人才不比大模型人才便宜 ， 毕竟我们要做的是顶尖的小模型，所以人才的钱不能省。现有的 token 计价经济还不足以支撑 GPU 上的推理成本，所以利润很薄。 
 现在回看 24 年年初当我大刀阔斧的砍掉 App 专注小模型时， 在那一刻，Jina 的终局也就收敛到被收购这一条路上 （当然还有倒闭这条路），剩下的就是留给我的时间和能否成功的问题。 
 如果刻意的不暴露营收（因为一旦暴露营收那么估值就基本定了），那就只能通过把故事讲大去拿融资。可是小模型的故事就讲不大， 就如同街边麻辣烫和海底捞，小模型就像麻辣烫，一下班很多人在那买。不是说他没市场，投资人也知道街边麻辣烫香，但投资人还是喜欢投海底捞（大模型）。 
 张飒 ：既然终局是被收购，那您做收入又有什么意义呢？ 
 肖涵：收入还是要做，我觉得有几点。 
 第一就是 PMF 的验证，看看市场到底需不需要这类模型，以及在竞争中是否可以脱颖而出。2023 年之前我们曾追踪过很多社区指标，包括下载量、Github 关注度、社交媒体讨论度等等。后来发现这些指标大多捕风捉影，和 PMF 弱相关，完全没有真金白银来得实在。毕竟用户说你好给你点个赞是一回事儿，肯花钱买你的模型是完全另一回事儿。 
 第二点是培养团队对 Token Economy 的理解：训练时的语料一共是多少 tokens，每个 batch 是多少 token，推理时 token/s 是多少，最大 token 长度是多少，用户输入的 token 中位值是多少，第一个 token 返回的时间是多少，每分钟允许 请求的 最大 token 数量是多少，多模态如图片时怎么计算 token 才合理。只有当公司里每个人对这些数据手到擒来，才能明白 token 的价值到底是多少，整个模型的训练、推理才能更加高效和专业。我们 2024 年初刚开始做 Model API 的 Paywall 时，很多人对免费 Token 的数量和定价完全没有概念，内部曾说免费送十万的 Token 太多了，用户根本用不完。这就是缺乏对 Token Economy 的理解。如今我们每个新 API Key直接送一千万的 Token，保证了用户在进行多模态图片输入和长文本输入时的消费体验。付费阶梯也根据多次优化和重新设计，从而保证推理服务的利润率为正。 
 最后也算是我的一点个人的坚持，我觉得既然是创业做公司，那目的就是要盈利。烧投资人的钱发工资并不是一个特别值得骄傲的事情。我既然把公司转型到了 Model as Product 的模式上，那我就希望竭尽所能的去探究这个模式的极限在哪，它的实际利润到底如何。如果一个团队仅仅是为了纯做技术和社交媒体上的影响力，那还不如在高校里做。 
 张飒 ：那您觉得这几年来，您在 Jina 做对了什么，又做错了什么呢？ 
 肖涵：现在回头看， 我 做对的几点 包括： 
 从第一天就构建一个国际化的团队，这对 Jina 在后期的人才招聘、市场和收购案上都奠定了一个比较好的基础。 
 第二就是身先士卒，事必躬亲。我几年来在 Jina 写的代码数量应该是所有员工里最多的。我曾在内部开玩笑的说， 如果哪天 Jina 倒闭了，那绝对不是因为 CEO 写代码太少了，而是因为写代码太多了 。 
 其实无论是工程研发还是商业化、市场运营、销售客服这些事情我都会亲身参与进来。 我觉得无论多少年，创始人必须要保持一个最大的热情。 如果一个公司的创始人每天开始打卡躺平，无所事事，那公司就彻底玩完。 
 在商业化的探索上，我从 2023 年的零收入开始一点一点做起，到被收购时做到两百万美元的 ARR，作为一个纯 Model as Product 靠卖 API 的初创，在零广告营销全靠口碑自然增长的情况下，我认为这个结果还勉强说的过去。至少从零到 Million ARR 的路我一路蹚了出来，坑踩了个遍，也算后事之师。 
 最后就是持续的学习和思变，根据大环境对公司的及时调整和优化，包括几次在公司组织上和叙事逻辑上的重塑。这些都是我认为正确且必须由创始人牵头的。 
 我 做错 的地方 ： 
 首先我觉得前几年我没有能够让团队足够的聚焦，尤其是在 A 轮融资过后，团队方向过于分散，因此浪费了时间和金钱去追逐了很多没有意义的技术和市场营销。 
 第二，在方向不够聚焦时我选择了扩张团队，希望通过空降 leader 来解决内部产品线和聚焦问题，结果收效甚微。如果这六年来我给公司的所有 leader 打分，10 分我给 2 分：很多 leader 在生存压力和技术快速变化的环境下无法及时跟进和发挥。我没有找到很好的 leader，也没有培养出很好的 leader。 
 这就引出了我这几年创业来的最大遗憾：就是我并没有想明白团队的 S caling Law 。 从 2020 年到 2023 年，团队一直在扩张，可是产出和品牌力却在下降。从 2024 年起，我一直走在精简团队的路上，从 60 人裁撤到 30 人，团队效率和品牌价值得到了颠覆性的提升。 
 但按照这个逻辑推到底， 团队人数和品牌价值根本呈反比！ 
 “小而美”并不应该是终局 ： 如果每家公司都以小为荣，越做越精简，这世上就不会有谷歌和微软这样的巨头。所以如何去 Scale 一个 AI 团队，去把生意做大，这个是我近六年遗憾没能做成的事情。 
 Growth without revenue is disaster, revenue without growth is boring. 我把公司从盲目扩张的 disaster 里捞了出来，之后一直在小心翼翼地避免滑入 boring 。 
 虽说强者不抱怨环境，可我觉得我另一个错误就是 对欧洲和德国抱有太多的期待和幻想。 直到 2024 年我来到美国湾区后， 我发现自己在一个过分平庸的地方浪费了很多宝贵的时间 。 
 对于整个德国和欧洲社会的左和保守，对 AI 纸上谈兵和杞人忧天，劳动法对创业者缺乏理解尊重，及对优秀人才的冷漠无视，这些都让我在 2023 年后对欧洲和德国无比失望。我曾在 2023 年在公司里叫上几个德国同事一起去做一些 lobby 游说，希望多参与到欧洲议会和德国政界来获取关注和资源，一年下来活动参加不少，进展为零。直到有一天我也看明白了，他们邀请我去参加这些议会、党代会完全是把我看做一个 Diversity Guest： 他们不需要我的 Expertise，只需要那张 Asian Face。 
 2025 年春我接受了《华尔街日报》的采访，表达了我对德国和欧洲的彻底失望。 欧洲总以为他们在 AI 的落后是孤立现象，其实不然，是整个社会和经济环境造成的。 报道发表后，引起了不少讨论。但在欧洲这些讨论最终能有多少付诸实践，我不抱以任何期望。 
 很多人总说 American Dream 怎么怎么样，但很多事情确实是我来到美国之后才有了实质的进展。无论塑造 lean & mean 的公司文化，还是 Jina 品牌的重新树立，再到最后被美国上市公司收购：这个地方不仅激励了我，也确实奖励了我的付出。 
 无论如何残酷的竞争与合作，AI 的发展绝对是中美两国的事情，就像鸣人和佐助一样相爱相杀。而欧洲就像小樱——说白了就没她啥事儿。 
 张飒 ：您还会创业吗？ 
 肖涵：创业是刻在骨子的事情，我觉得未来还会。但目前还是需要再积累一下，把事情再琢磨透一些。比如我们都看到这波 AI 带来了生产力上的提升，很多工程师感觉可以创个业变现一波生产力。可是 生产力的提高 ≠ 价值捕获能力提升 ，不代表可以落地生财。 
 有些人可能会说，我今年因为熟练使用 Cursor/Claude Code 做了好几个项目被老板发奖金表扬了。在公司里领工资时，生产力提升能变现，是因为公司已经解决了价值捕获的问题：有现成的客户、销售渠道、品牌信任。你多产出 10%，公司的变现机器能把这 10% 转化成收入，你分到一部分。 
 而在创业独立面对市场时，AI 只增强了供给侧（你能做更多、更快），却没有同步增强需求侧（找客户、建立信任、完成交易）。说白了，生产力是“造东西”的能力，不是“卖东西”的能力。 
 如果所有人都将成倍的生产力直接投放在市场中时，供给集体上升，单位价格反而下降。最后反而也赚不到什么钱。 
 张飒 ：那您现在有什么看好的创业方向么？ 
 肖涵：我去年曾说过我对 AI + 原创游戏挺感兴趣，我觉得在原创游戏中 各种多模态的 落地场景明确：无论是素材、故事线、NPC 逻辑，都可以随着大模型能力的提升而水涨船高。 游戏本身就是一个成熟的商业模型：付费下载、内购、订阅。AI提升的生产力（更丰富的素材、更拟人的 NPC、更个性化的剧情）直接转化成玩家体验，而体验是可以被明码标价的。 
 卡点在于如何塑造一个受欢迎的 IP：经典的 IP 都把握在游戏大厂手里，独立开发者从零塑造一个 IP 又谈何容易。 这个就要谈到 OC 圈（ Original Character, 原创角色），我之前投过的米球岛就是做这个方向的。你可以把它想象成 一个去中心化的 IP 孵化池，用户本身就在为角色赋予情感价值和传播势能。如果 AI 能让 OC 创作的门槛更低、表达更丰富，某种意义上是在加速“ IP 民主化”，不再只有大厂能造 IP。米球岛这个切入点挺聪明的。 
 这两个月兴起的 AI Trading，比如 AlphaArena 拿各种大模型在二级市场中做量化交易，或是在一级市场中为 Sell-side 做投研分析。我觉得也是一个不错的方向。 这个方向最硬核的地方在于： 回报是可量化的、实时的、无需说服任何人的。 你的模型比市场聪明一点点，你就赚到了。不需要品牌、不需要销售、不需要用户增长。市场本身就是最高效的裁判。 
 尤其是 Buy-side 的交易信号捕获，相当于 完全跳过 AI 生产力这一叙事逻辑，而将 AI 的“认知能力”直接映射成 alpha。 这可能是 AI 变现路径里摩擦最小的场景之一 。我最近在和一个出自伯克利和斯坦福的项目 T auric Research 聊，他们开始用 Jina Reader API 做信息获取和舆情分析，然后输入到一个他们自己训练的推理模型中去得到交易信号， 这比“提升生产力”的故事要硬得多，因为下游直接是钱。 
 当然 AI Trading 的竞争也更残酷。 因为所有人都在同一个市场里博弈，你的 alpha 就是别人的负 alpha。 
 张飒 ：最后您能给未来的创业者 一些建议 么？ 
 肖涵：要专注，要强调公司的叙事逻辑。 
 创始团队一定要精简， 不要为了显得好看而凑人头 。 如果你自己很强，那就一个人开干。 如果你自己不强或没思路，那我建议就先别创业。 
 要尽最大努力找到那些聪明的人和 High Achiever，并且和他们在一起工作。 这些人对第一性原则，80/20 等熟记于心，做事 干净利落 ，杀伐果断，从不后悔。这是创业团队所需要的。 
 今年年初，一个 MIT 本科生来柏林找我们实习。乌克兰女生，Sheldon 式的人物，不太擅长社交，但聪明得惊人。我问她：为什么大老远跑来柏林？（潜台词是：你 MIT 的学生，美国机会那么多）她秒答：因为父母在柏林，她想和父母团聚；她投过亚马逊柏林，但对方不肯透露实习内容；而 Jina 明确告诉她是做小模型，正好是她喜欢的方向。于是她就来了。整个回答没有一秒犹豫。 
 后来我又问她：18岁，一个女生，独自从乌克兰去波士顿，会不会害怕？她的回答我至今记得—— 
 “我不怕。害怕的应该是我的父母，因为他们还生活在战争里。” 
 她在柏林待了三个月， 训练出一个超强的jina-code-embeddings ， 写了篇论文，中了 NeurIPS Workshop，然后转身离开。 整个过程干净利落，像她说话的方式一样。 
 12月在 San Diego 举办的 NeurIPS 她也会参加，有在会场的朋友可以替我和她打个招呼。 
 最后，一定要避免和平庸的人在一起消磨时间。 他们的特征很明显：做事拖泥带水，决策犹犹豫豫；竞争来了绕着走，压力来了往回缩。 
 也别想着“我来培养他”或“我再给他点时间看看”，创业是九死一生的游戏，不是大学。你没有时间把一个 60 分的人打磨成 90 分，你只能找到那些本来就是 90 分的人，然后一起拼命。 所以： 
 Don’t pray for an easy life, pray to be a stronger one. 
 （全文完） 
 阅读原文 
 跳转微信打开
```

---
