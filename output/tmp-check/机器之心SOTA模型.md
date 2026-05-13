# 机器之心SOTA模型

> 分类: AI专题
> URL: https://wechat2rss.bestblogs.dev/feed/2f520471856d56c7b3a95cd09eb777149b32828a.xml
> 抓取: 10 篇

---

## 1. 今日开源（2026-5-9）：小米SVOR正式开源，稳定视频对象移除框架，三大核心设计攻克阴影残留与运动抖动难题

- 日期: 2026-05-09 18:31
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyMzcwMDIyMQ==&mid=2247502248&idx=1&sn=ea2a447801f0b901fa8a8894ebf559e9

```
原创 每日发现最新LLM 2026-05-09 18:31 中国香港 
 多模态音频生成框架Omni2Sound，VLA模型开发代码库StarVLA，视觉语言模型Bard-VL.git，稳定视频对象移除框架SVOR，大语言模型真实性诊断方案belief，自进化集体智能系统Ultron。 
 🏆 基座模型 
 ①项目：Omni2Sound 
 ★Omni2Sound是CVPR 2026高亮收录的多模态音频生成项目，为统一的视频文本转音频框架，支持视频+文本转音频、纯视频转音频、纯文本转音频三类任务。 项目采用通用DiT骨干，依托 高质量SoundAtlas数据集 和 三阶段渐进多任务训练策略 ，无需定制架构即可在三类任务上达到SOTA性能，可适配屏外音频合成、不完整文本输入等复杂场景。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/omni2sound 
 ②项目：StarVLA 
 ★StarVLA是面向视觉语言动作（VLA）模型开发的乐高式开源代码库，属于通用机器人领域的开源研究平台。 项目各功能组件遵循 高内聚低耦合设计原则 ，支持即插即用、快速原型开发与独立调试，可集成多种前沿技术，降低VLA模型与机器人应用开发门槛。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/starvla 
 ③项目：Bard-VL.git 
 ★本项目由复旦等机构联合研发，是一款视觉语言模型，通过高效渐进块合并与阶段蒸馏技术桥接自回归和扩散两类视觉语言模型 ，提供2B、4B、8B等多种参数规模版本，配套完整的训练、部署工具链，可支撑各类多模态理解任务。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/bard-vl-git 
 🛠️ 框架平台、必备工具 
 ①项目：SVOR 
 ★SVOR是小米研究院推出的稳定视频对象移除框架，针对真实场景中阴影、突变运动、缺陷掩码等干扰问题，采用三大核心设计，可实现无阴影、无闪烁、容忍掩码缺陷的视频对象移除效果。 项目在多个数据集及缺陷掩码基准上取得SOTA结果，相关方案获CVPR2026物理感知视频实例移除挑战赛冠军，目前已开源相关资源。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/svor 
 ②项目：belief 
 ★本项目由浙江大学zjunlp团队开发，针对传统点式置信度度量易出现“认知错觉”的缺陷，提出基于邻域一致性的大语言模型真实性诊断方案 ，包含 邻域一致性置信度（NCB）度量、认知压力测试、结构感知训练（SAT） 三大核心模块，可精准评估大模型回答鲁棒性，经测试SAT方案可降低模型在压力下的性能退化约30%，配套提供全流程代码及样例数据集。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/belief 
 ③项目：Ultron 
 ★Ultron是面向通用AI Agent的自进化集体智能系统，核心包含记忆库、技能库、配置库三大中心，可将分散的单会话Agent经验提炼为可检索复用的集体知识。 单个Agent的踩坑经验可让全体规避，验证后的解决方案可自动沉淀为 可进化的复用技能 ，调优后的Agent配置可作为共享模板一键加载，服务端还可基于积累的轨迹自训练模型降低使用成本。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/ultron 
 跳转微信打开
```

---

## 2. 今日开源（2026-5-8）：小米发布OmniVoice，新型扩散语言模型支撑大规模多语言TTS，语音克隆与音色设计双能力集成

- 日期: 2026-05-08 18:30
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyMzcwMDIyMQ==&mid=2247502236&idx=1&sn=0cbfdbe2827bfb54046f062110513640

```
原创 每日发现最新LLM 2026-05-08 18:30 中国香港 
 大规模多语言零样本语音合成模型OmniVoice，大语言模型OpenSeek-Mid-v1，视觉推理视觉语言模型Laser，面向视觉引导机器人学习的高吞吐量真实感仿真框架GS-Playground，扩散大语言模型免训练加速方案DYNAMIC-DLLM，面向视频语言处理的人机协同监督框架CHAI。 
 🏆 基座模型 
 ①项目：OmniVoice 
 ★OmniVoice是先进的大规模多语言零样本语音合成（TTS）模型，支持超600种语言 ，基于 新型扩散语言模型架构 构建，可生成 高质量语音 ，推理速度优异，同时支持语音克隆、音色设计功能。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/omnivoice 
 ②项目：OpenSeek-Mid-v1 
 ★OpenSeek-Mid-v1是北京智源人工智能研究院推出的10.61B参数大语言模型，基于Qwen3-4B-Base通过两阶段模型扩展流水线构建，仅用2万亿全开源数据完成训练。 在参数量较Qwen3-14B少25%、训练数据少18倍的情况下，其在多个基准测试上持平甚至超越Qwen3-14B-Base，采用Apache-2.0开源协议。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/openseek-mid-v1 
 ③项目：Laser 
 ★Laser是用于高效视觉推理的视觉语言模型，支持在连续隐空间执行隐式推理，遵循先全局理解再细节处理的逻辑。 项目已开源训练代码、7B权重、ScanPath训练数据集，配套多基准评估能力，可快速用于 视觉推理相关任务 。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/laser3 
 🛠️ 框架平台、必备工具 
 ①项目：GS-Playground 
 ★GS-Playground是面向视觉引导机器人学习的高吞吐量真实感仿真框架，将并行机器人物理引擎与批量3D高斯溅射（3DGS）渲染能力结合，支持具备真实外观、刚性链路视觉同步的大规模视觉强化学习。 目前已开放早期公开预览版本，包含最小批量渲染基准测试和两个演示Demo，完整资源将分阶段发布，项目已被RSS 2026收录。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/gs-playground 
 ②项目：DYNAMIC-DLLM 
 ★本项目是扩散大语言模型（Diffusion LLM）免训练加速方案的官方PyTorch实现 ，核心包含 动态缓存更新、自适应并行解码 两大模块，可在不修改模型参数的前提下提升Diffusion LLM推理效率，相关研究成果已被ICLR 2026接收。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/dynamic-dllm 
 ③项目：CHAI 
 ★CHAI是面向视频语言处理的人机协同监督框架，联合人类专家与AI预生成字幕，由专家提供修正意见指导优化字幕生成，既提升字幕准确率也提高生产效率。 项目配套覆盖主体、场景、动作、空间布局、相机动态的结构化字幕规范，开源相关数据集、基准与训练方案，可用于优化开源视频语言模型。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/chai2 
 跳转微信打开
```

---

## 3. 今日开源（2026-5-7）：腾讯开源OpenSearch-VL，30B/32B模型精度比肩顶尖商用系统，7个知识密集型多模态基准表现优异

- 日期: 2026-05-07 18:30
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyMzcwMDIyMQ==&mid=2247502225&idx=1&sn=f0754f084397b59737f5a25fab407f0f

```
原创 每日发现最新LLM 2026-05-07 18:30 中国香港 
 智能体的全开源方案OpenSearch-VL，通用物理平台Genesis，混合专家大语言模型Laguna-XS.2，超高速大模型推理引擎TokenSpeed，权重解耦正则化方法OrthoReg，即插即用自进化观测上下文压缩框架TACO，引导式组相对策略优化研究项目G2RPO-A。 
 🏆 基座模型 
 ①项目： OpenSearch-VL 
 ★ OpenSearch-VL是用于训练前沿多模态深度搜索智能体的全开源方案，解决了此前顶尖多模态搜索智能体的训练数据、轨迹合成流程、训练方案均为闭源的痛点 ，开源了可完整复现效果的数据集、训练代码与模型权重。该方案通过 高质量数据构造、多元视觉/搜索工具 、 致命错误感知的智能体强化学习 实现训练，在7个知识密集型多模态基准上表现优异，30B/32B规模模型精度比肩顶尖商用系统。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/opensearch-vl 
 ② 项目：Genesis 
 ★Genesis是面向通用机器人、具身智能、物理AI场景的专用物理平台，底层自研全新通用物理引擎，将多类物理求解器及耦合能力集成至统一框架，兼具超高性能、轻量易用的Python化接口、照片级真实渲染能力 ，还支持 生成式数据引擎 ，可基于自然语言生成多模态数据。目前已开源底层物理引擎与仿真平台，生成式功能将逐步开放，旨在降低物理仿真使用门槛，高保真复现物理世界，实现自动化数据生成。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/genesis-world 
 ③项目：Laguna-XS.2 
 ★Laguna-XS.2是Poolside推出的混合专家大语言模型，总参数量33B，单token仅激活3B参数，面向智能体编码、本地长时序任务设计。 模型采用 滑窗 与 全局注意力混合布局 ，支持原生推理、工具调用，轻量易部署，可在36GB内存的Mac设备运行，基于Apache2.0协议开源。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/laguna-xs-2 
 🛠️ 框架平台、必备工具 
 ①项目：TokenSpeed 
 ★TokenSpeed是一款面向智能体工作负载的超高速大模型推理引擎，具备TensorRT-LLM级性能与vLLM级易用性，目标成为生产级智能体工作负载下性能最优的推理引擎。 核心包含 建模层、调度器 等四大组件，当前为预览版本，可复现Kimi K2.5、TokenSpeed MLA在B200上的运行结果，仍在迭代优化相关能力，暂不建议用于生产部署。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/tokenspeed 
 ②项目：OrthoReg 
 ★任务算术是一种高效免训练的预训练模型编辑方法，本项目是CVPR 2026 Oral论文《Understanding and Enforcing Weight Disentanglement in Task Arithmetic》的官方实现。 项目提出任务 特征专门化（TFS） 是任务算术场景下权重解耦的充分条件，其几何表现为 权重向量正交性 ，以此为核心提出轻量的 OrthoReg正则化方法 ，在微调阶段对构成任务向量的权重更新量施加正交约束，理论证明该方法可有效促进 权重解耦 ，大量实验验证其能一致、显著提升各类任务算术方法的性能。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/orthoreg 
 ③项目：TACO 
 ★TACO是面向终端Agent的即插即用自进化观测上下文压缩框架，针对终端Agent多轮任务中原始Shell输出噪声累积、淹没有效错误信号、推高Token成本的问题， 无需硬编码截断规则，可在线发现、修复、复用压缩规则，还维护全局规则池，支持新任务复用过往任务积累的知识。在TerminalBench等多个基准测试中，可为多款主流大模型骨干带来1%-4%的效果提升。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/taco2 
 ④项目：G2RPO-A 
 ★本项目是香港中文大学（深圳）T-Lab团队产出的ACL 2026收录研究项目，聚焦引导式组相对策略优化方向 ，对各类引导配置开展了全面研究，提出可根据训练状态自动调整引导长度的自适应算法G2RPO-A，目前已开放项目核心代码。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/g2rpo-a-2 
 跳转微信打开
```

---

## 4. 今日开源（2026-5-6）：阿里开源PromptEcho，突破人工偏好标注扩展性瓶颈，显著提升文生图模型提示遵循能力

- 日期: 2026-05-06 18:30
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyMzcwMDIyMQ==&mid=2247502206&idx=1&sn=d9bb48f29f36f2643e49ecab2323f818

```
原创 每日发现最新LLM 2026-05-06 18:30 中国香港 
 无标注奖励方案PromptEcho，终端编程Agent DeepSeek-TUI，MoE优化实现SonicMoE，手语翻译新范式SignThought，macOS端推理加速工具Cider，可扩展测试时训练方案Scal3R。 
 🛠️ 框架平台、必备工具 
 ①项目：PromptEcho 
 ★PromptEcho是面向文生图强化学习的无标注奖励方案，针对现有方法依赖昂贵人工偏好标注、扩展性受限的痛点，无需标注即可从冻结视觉语言模型中获取奖励信号 ，通过计算VLM基于生成图像重建原始提示的负交叉熵损失作为奖励，可直接接入GRPO/AWM类策略优化，能显著提升文生图模型的提示遵循能力，配套提供评估基准、推理脚本及相关LoRA权重。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/prompt-echo 
 ②项目：DeepSeek-TUI 
 ★DeepSeek-TUI是运行在终端的DeepSeek V4专属编程Agent，支持文件编辑、Shell命令执行、网页搜索、Git管理等功能 ，配备1M token上下文窗口，支持流式推理展示，提供多档运行模式，可高效辅助开发者完成 各类编码相关任务 。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/deepseek-tui 
 ③项目：SonicMoE 
 ★SonicMoE是一款面向NVIDIA Hopper、Blackwell系列数据中心及消费级GPU优化的混合专家模型（MoE）实现 ，基于CuTeDSL和Triton实现IO感知优化，依托QuACK库的Grouped GEMM内核，可实现领先的运算性能，降低激活显存占用、提升 训练吞吐量 ，适配主流MoE大模型。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/sonic-moe 
 ④项目：SignThought 
 ★本项目是无术语标注（Gloss-Free）场景的手语翻译新范式，解决了传统手语翻译忽略手语动态生成特性的问题 ，通过 三大核心机制 实现直接从手语视频到口语文本的翻译，相关成果已被ACL 2026主会收录。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/signthought 
 ⑤项目：Cider 
 ★Cider是基于MLX开发的macOS端推理加速工具，填补MLX缺失的W8A8、W4A8量化推理能力 ，适配M5+芯片INT8 TensorOps，可实现LLM预填充速度1.2-1.9倍提升，兼容mlx_vlm并修复相关推理问题。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/cider 
 ⑥项目：Scal3R 
 ★本项目是CVPR 2026高亮论文配套开源项目，提出可扩展测试时训练方案用于大规模3D重建 ，支持从输入图像序列生成 相机位姿、深度图、点云 等重建结果，当前已开放推理代码及相关工具。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/scal3r 
 跳转微信打开
```

---

## 5. 今日开源（2026-4-30）：inclusionAI开源Ling-2.6，万亿参数兼顾推理效率与令牌开销，多项执行类基准达开源SOTA

- 日期: 2026-04-30 18:30
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyMzcwMDIyMQ==&mid=2247502189&idx=1&sn=2fe364b3012d36e1bb67aca0b684636f

```
原创 每日发现最新LLM 2026-04-30 18:30 中国香港 
 万亿参数综合旗舰模型Ling-2.6，旗舰融合稠密大模型Mistral-Medium-3.5，端侧低比特翻译模型Hy-MT1.5-1.8B-2bit，自主Web智能体框架Avenir-Web，系统性综述Survey-Intrinsic-Interpretability-of-LLMs，视觉多智能体系统ViF，生成式推荐模型DIGER。 
 🏆 基座模型 
 ①项目：Ling-2.6 
 ★Ling-2.6是inclusionAI开源的万亿参数综合旗舰模型，面向真实复杂场景打造，在推理效率、令牌开销、智能体能力方面做了针对性优化 ，可高效适配代码生成、日常工作流处理、智能体任务执行等场景，在多个执行类基准测试中达到开源SOTA水平，采用MIT协议开源。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/ling-2-6 
 ②项目： Mistral-Medium-3.5 
 ★ 本项目是Mistral AI推出的首个旗舰融合稠密大模型，参数128B，上下文窗口256k，支持文本、图像多模态输入，统一权重可处理指令遵循、推理、编码任务。 可按请求配置推理强度，适配快速聊天到复杂智能体运行场景，性能优于前代模型，支持24种语言，采用修改版MIT许可，普通企业商业、非商业场景均可使用。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/mistral-medium-3-5 
 ③ 项目：Hy-MT1.5-1.8B-2bit 
 ★ 本项目是腾讯混元团队开发的端侧低比特翻译模型，基于Hy-MT1.5-1.8B基础模型，采用Sherry 1.25bit量化技术 ，原生支持33种语言、5种方言/少数民族语言共1056个翻译方向，压缩后体积仅440MB，可在普通手机离线流畅运行，翻译效果优于多款大参数量开源模型及主流商用翻译API。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/hy-mt1-5 
 🛠️ 框架平台、必备工具 
 ①项目：Avenir-Web 
 ★Avenir-Web是普林斯顿AI加速发明实验室开发的自主Web智能体框架，可在复杂动态网页界面可靠执行长周期任务。 针对元素定位、长时任务追踪难点，采用 模块化架构 ，在Online-Mind2Web基准上达到开源SOTA水平，缩小了与私有模型的真实场景部署性能差距。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/avenir-web 
 ②项目：Survey-Intrinsic-Interpretability-of-LLMs 
 ★本项目是北京大学PILLAR团队发布的ACL 2026主会录用论文配套资源，是首个针对大语言模型内在可解释性的系统性综述 ，将该领域现有方法划分为五大核心设计范式，同时整理了各分类下的相关论文列表，方便领域研究者查阅参考。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/survey-intrinsic-interpretability-of-llms 
 ③项目：ViF 
 ★本项目是入选ICLR 2026的视觉多智能体系统，通过视觉流机制解决多智能体交互过程中的幻觉滚雪球问题 ，支持基于LLaVA-NeXT等 主流视觉大模型 开展两阶段训练与效果评估，可缓解交互轮次增加导致的视觉注意力下降问题，提升多模态多智能体输出准确性。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/vif 
 ④ 项目：DIGER 
 ★本项目是被SIGIR 2026收录的生成式推荐领域研究成果，核心实现了基于可微分语义ID的生成式推荐模型 ，提供 两种不确定性衰减训练策略 ，后续将开放完整可复现代码、处理后数据集及预训练权重，支持推荐任务的训练与效果评估。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/diger 
 跳转微信打开
```

---

## 6. 今日开源（2026-4-29）：商汤SenseNova-U1推出，原生架构兼顾性能与效率，语言视觉统一处理突破适配器限制

- 日期: 2026-04-29 18:30
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyMzcwMDIyMQ==&mid=2247502177&idx=1&sn=2e6fbda58ccb1804c270675a91969504

```
原创 每日发现最新LLM 2026-04-29 18:30 中国香港 
 原生多模态模型系列SenseNova-U1，NVIDIA推出的Nemotron家族多模态大模型Nemotron-3-Nano-Omni，机器人基础模型LDA，上海人工智能实验室发布的室内VLA操作基准EBench，类感知零样本提示重加权方法CARPRT，即插即用框架VEGA-3D。 
 🏆 基座模型 
 ①项目：SenseNova-U1 
 ★SenseNova-U1是原生多模态模型系列，采用NEO-Unify架构，无需适配器即可原生实现语言、视觉模态的统一处理 ，端到端打通多模态理解、推理、生成能力，在多项开源基准中达到SOTA水平，兼具优异性能与效率。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/sensenova-u1 
 ②项目：Nemotron-3-Nano-Omni 
 ★本项目是NVIDIA推出的Nemotron家族多模态大模型，统一支持视频、音频、图像、文本理解，集成GUI、OCR、语音转录能力 ，可满足企业级问答、摘要、转录、文档智能等工作流需求，适用于客服、媒体娱乐、GUI自动化等场景，支持商用。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/nemotron-3-nano-omni 
 ③项目：LDA 
 ★LDA是RSS 2026收录的机器人基础模型， 通过统一摄入多质量具身数据，联合学习动力学、策略和视觉预测任务，为不同标注质量的数据分配 差异化学习目标 ，已在多类机器人实体上完成预训练， 泛化能力优异 。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/lda-1b 
 🛠️ 框架平台、必备工具 
 ①项目：EBench 
 ★EBench是上海人工智能实验室发布的室内VLA操作基准，基于NVIDIA Isaac Sim构建。 不同于传统仅输出整体成功率的评测方式，它可生成多维度能力画像，暴露模型优势与过拟合问题，覆盖 长序列、灵巧精准、移动操作 三类场景，支持多维度诊断与泛化测试，评测结果可真实反映模型泛化能力。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/ebench 
 ②项目：CARPRT 
 ★CARPRT是ICLR 2026收录的针对黑盒视觉语言模型的类感知零样本提示重加权方法，无需训练，仅通过无标注数据估计类感知的提示权重，可提升CLIP类模型的零样本分类效果。 区别于传统为每个提示跨所有类别分配单一权重的方案，该方法建模了 类别相关的提示相关性 ，无需修改预训练模型参数即可使用，适配黑盒VLM场景。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/carprt 
 ③项目：VEGA-3D 
 ★VEGA-3D是可挖掘视频生成模型隐式空间先验的即插即用框架， 将预训练视频扩散模型作为 隐式世界模拟器 ，提取时空特征后通过门控机制与语义特征融合，为多模态大模型补充几何线索，可支持3D场景理解、空间推理、具身决策等任务。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/vega-3d 
 跳转微信打开
```

---

## 7. 今日开源（2026-4-28）：小米MiMo-V2.5家族开源，1M上下文窗口覆盖多模态感知与智能体工作流，MIT协议释放全模态能力

- 日期: 2026-04-28 18:31
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyMzcwMDIyMQ==&mid=2247502166&idx=1&sn=b107d0096afde4dfbdb211affdb903e5

```
原创 每日发现最新LLM 2026-04-28 18:31 中国香港 
 MoE架构大语言模型MiMo-V2.5，多模态模型LLaDA2.0-Uni，双轨框架MathForge，面向时序数据时空推理的大模型框架STReasoner，研究成果Mathematical-Reasoning-RL-Scaling-Law，智能AI Agent项目JiuwenClaw，开源本地优先内存方案OpenChronicle。 
 🏆 基座模型 
 ①项目： MiMo-V2.5 
 ★ MiMo-V2.5是小米推出的原生全模态大模型，基于MiMo-V2-Flash骨干拓展专用视觉、音频编码器， 统一架构支持文本、图像、视频、音频理解，在 多模态感知、长上下文推理、智能体工作流 场景表现优异。模型总参数310B、激活参数15B，上下文窗口最高支持1M tokens，采用MIT协议开源。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/mimo-v2-5 
 ②项目：LLaDA2.0-Uni 
 ★LLaDA2.0-Uni是Inclusion AI推出的基于扩散大语言模型的MoE架构多模态模型，统一了多模态理解与生成能力 ，支持文生图、图像理解、图像编辑、多模态混合推理等任务，经蒸 馏可实现8步快速推理，多模态理 解效果比肩专用视觉语言模型。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/llada2-0 
 🛠️ 框架平台、必备工具 
 ①项目：MathForge 
 ★MathForge是被ICLR 2026收录的数学推理优化双轨框架，包含难度感知组策略优化（DGPO）算法与多维度问题重构（MQR）策略两大核心模块。 其中 DGPO 解决传统GRPO对难题更新权重不足的问题， MQR 可在保留标准答案的前提下提升训练数据难度，二者形成协同优化循环，在多个主流数学推理基准测试集上相比传统GRPO方案有显著性能提升，目前已开源项目代码及相关增强数据集。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/mathforge 
 ②项目：STReasoner 
 ★ STReasoner是面向时序数据时空推理的大模型框架，通过三阶段训练管线（时序对齐SFT、冷启动推理SFT、空间感知强化学习）实现 ，配套专用 ST-Bench多模态评测基准 ，支持多款通义千问系列基座，已被ACL 2026主会收录。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/streasoner 
 ③项目：Mathematical-Reasoning-RL-Scaling-Law 
 ★本项目是ACL2026主会收录的研究成果，针对大语言模型强化学习后训练的缩放行为开展系统实证研究，聚焦数学推理场景 ，覆盖0.5B到72B全系列Qwen2.5稠密模型，通过63组实验分析模型规模、数据量、计算预算三者对性能的影响规律，验证了受限场景下数据复用的有效性，相关结论可用于大模型RL后训练的资源配置优化。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/mathematical-reasoning-rl-scaling-law 
 🤖️ Agent开发 
 ①项目：JiuwenClaw 
 ★JiuwenClaw是基于openJiuwen开发的智能AI Agent，采用Python编写，可将大模型能力通过用户日常使用的各类通讯应用触达用户。 作为个人专属AI管家，支持任务智能调度、自主技能进化，可私有化部署保障数据主权，适配多类平台接入。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/jiuwenclaw 
 ②项目：OpenChronicle 
 ★OpenChronicle是面向具备工具调用能力的LLM Agent的开源、本地优先内存方案，类比OpenAI Chronicle但具备开源、模型无关、可审计可扩展特性 。其运行在 macOS端 ，以AX树优先、截图辅助的方式捕获用户操作结构化上下文，生成持久化Markdown内存，支持多种模型提供商，采用MIT协议开源。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/openchronicle 
 跳转微信打开
```

---

## 8. 今日开源（2026-4-27）：谷歌开源TIPSv2模型，对比学习框架驱动图像文本特征对齐，覆盖零样本分类应用场景

- 日期: 2026-04-27 18:30
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyMzcwMDIyMQ==&mid=2247502148&idx=1&sn=4a884dee6d8adf0d1ab700559a61d991

```
原创 每日发现最新LLM 2026-04-27 18:30 中国香港 
 对比式视觉语言模型TIPSv2，自进化智能体轨迹诊断系统CodeTracer，LLM Agent技能编译与运行时系统SkVM，CVPR2026收录的医学视频理解项目MedGRPO-Code，面向大模型多语言扩展的可组合可泛化可控框架XBridge，无验证器的进化测试时缩放框架Squeeze-Evolve。 
 🏆 基座模型 
 ①项目：TIPSv2 
 ★TIPSv2是具备空间感知能力的对比式视觉语言模型，可实现图像与文本特征对齐。 本次为Base变种，视觉参数86M，文本参数110M，支持零样本分类、空间特征可视化等能力，采用Apache 2.0开源协议。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/tipsv2 
 🛠️ 框架平台、必备工具 
 ①项目：CodeTracer 
 ★CodeTracer是南京大学LINK团队联合Kwaipilot推出的自进化智能体轨迹诊断系统，可分步分析智能体执行轨迹，识别错误、无效动作，输出结构化诊断标签。 其作为 自主诊断智能体 可遍历轨迹环境、排查证据、构建根因链，还具备跨轨迹记忆可不断积累分析经验。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/codetracer 
 ②项目：SkVM 
 ★SkVM是上海交大IPADS团队研发的LLM Agent技能编译与运行时系统，可实现Agent技能在异构模型、运行框架间的可移植性 ，包含能力剖析、AOT编译、JIT优化、基准测试四大核心模块，支持跨场景、跨模型评估优化技能效果。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/skvm 
 ③项目：MedGRPO-Code 
 ★MedGRPO-Code是CVPR2026收录的医学视频理解项目，基于Qwen2.5-VL-7B经过SFT和MedGRPO强化学习训练得到专用医学多模态模型 ，配套开源了推理代码、MedVidBench医学视频数据集、在线Demo及评测榜单，支持时序动作定位、视频摘要等8类医学视频相关任务。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/medgrpo-code 
 ④项目：XBridge 
 ★XBridge是面向大模型多语言扩展的可组合、可泛化、可控框架，采用编码器-LLM-解码器架构 ，将多语言能力卸载给 集成的NMT模型 ，保留LLM作为英文核心处理通用知识，无需重训练LLM即可大幅提升低资源和未见语言性能，同时不损害LLM原有核心能力。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/xbridge 
 ⑤项目：Squeeze-Evolve 
 ★Squeeze-Evolve是无验证器的进化测试时缩放框架，通过多模型编排能力，将进化推理循环的每一步路由到性价比最优的模型， 高难度任务分配给高性能高成本模型，简单任务分配给低成本模型，可在准确率相当甚至更优的前提下， 大幅降低推理成本。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/squeeze-evolve 
 跳转微信打开
```

---

## 9. 今日开源（2026-4-24）：DeepSeek-V4双版本开源，Pro版激活49B、Flash版激活13B，代码能力同步升级

- 日期: 2026-04-24 18:38
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyMzcwMDIyMQ==&mid=2247502137&idx=1&sn=00a00e30500a51c7d652dc4e993f79f8

```
原创 每日发现最新LLM 2026-04-24 18:38 中国香港 
 DeepSeek-V4 MoE架构大语言模型系列，稠密多模态大语言模型Qwen3.6-27B，多智能体推演模拟框架OpenStory，无训练搜索系统SimpleTES，端到端统一音频理解、生成、编辑能力的框架Audio-Omni，聚焦Transformer中注意力Sink问题的综述Awesome-Attention-Sink。 
 🏆 基座模型 
 ①项目：DeepSeek-V4 
 ★DeepSeek-V4是深度求索推出的MoE架构大语言模型系列，包含总参数1.6T（激活49B）的Pro版和总参数284B（激活13B）的Flash版 ，均支持百万token上下文，在 知识、推理、代码、长上下文 等任务上表现接近闭源前沿模型水平，采用MIT协议开源。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/deepseek-v4-pro 
 ② 项目：Qwen3.6-27B 
 ★Qwen3.6-27B是阿里云通义千问团队研发的270 亿参数稠密多模态大语言模型， 原生上下文262K tokens、可扩展至1010K tokens，在 智能体编码、复杂推理、多模态理解、长文本处理 上性能强劲，多项编码基准超越千亿级模型，支持思考保留与工具调用，是同参数级开源旗舰级编码与智能体模型，成本效率优异。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/qwen3-6 
 🛠️ 框架平台、必备工具 
 ①项目：OpenStory 
 ★OpenStory（万象谱）是基于大语言模型和Agent-Kernel开发的多智能体推演模拟框架 ，首个落地剧情为《红楼梦》主题，支持1:1还原大观园的 可视化交互 ，用户可自由操控角色、回溯剧情，AI会基于选择推演剧情走向。框架支持 动态增删智能体、丰富的全生命周期插件机制 ，可通过YAML灵活配置各类参数，同时欢迎用户提交PR共创各类自定义剧情脚本。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/openstory 
 ②项目：SimpleTES 
 ★SimpleTES是论文《Evaluation-driven Scaling for Scientific Discovery》的参考实现，属于面向开放问题的无训练搜索系统， 通过 提议-评估-优化 的循环分配测试时计算资源，可基于开源大模型在6个领域21类开放问题上发现最优解决方案，支持自定义任务接入，提供多种使用入口。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/simpletes 
 ③项目：Audio-Omni 
 ★Audio-Omni是首个端到端统一音频理解、生成、编辑能力的框架，覆盖通用声音、音乐、语音三大领域， 结合冻结的Qwen2.5-Omni多模态大模型与可训练扩散Transformer实现，支持自然语言指令完成复杂音频操作，相关论文入选SIGGRAPH 2026。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/audio-omni 
 ④项目：Awesome-Attention-Sink 
 ★本项目是首个聚焦Transformer中注意力Sink问题的综述资源，整理了180余篇相关领域论文，覆盖利用、解释、缓解三个研究阶段，涉及多类Transformer架构，梳理了领域发展脉络，为相关研究人员提供查阅参考。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/awesome-attention-sink 
 跳转微信打开
```

---

## 10. 今日开源（2026-4-23）：腾讯混元Hy3 preview发布，295B总参数21B激活MoE架构，256K上下文窗口同参数级领先

- 日期: 2026-04-23 19:38
- 链接: https://mp.weixin.qq.com/s?__biz=MzkyMzcwMDIyMQ==&mid=2247502120&idx=1&sn=7b0b7f12f0ccbc699df815991a0b226d

```
原创 每日发现最新LLM 2026-04-23 19:38 中国香港 
 腾讯混元MoE架构大模型Hy3 preview，整流流扩散模型无奖励后训练方法HY-SOAR，基于TileLang的GPU内核库TileKernels，面向深度学习Koopman算子的信息论方法InformationKoopman，单目关节物体3D重建项目MonoArt，CVPR 2026收录的多模态大模型训练框架Monet。 
 🏆 基座模型 
 ①项目：Hy3 preview 
 ★Hy3 preview是腾讯混元团队开发的MoE架构大模型，总参数295B，激活参数仅21B，上下文窗口达256K ，在复杂推理、指令遵循、上下文学习、编码、Agent任务上性能提升显著，是同参数级领先的推理与Agent模型，成本效率优异。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/hy3-preview 
 🛠️ 框架平台、必备工具 
 ①项目：HY-SOAR 
 ★HY-SOAR是腾讯混元开源的整流流扩散模型无奖励后训练方法，针对扩散模型去噪轨迹暴露偏差问题 ，无需奖励模型、偏好标签或负样本，可在错误发生的时间步指导模型校正轨迹误差，提供单步密集训练信号，既可替代标准SFT作为更强的首个后训练阶段，也可兼容后续基于奖励的对齐流程，在多类生成场景表现优异。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/hy-soar 
 ②项目：TileKernels 
 ★TileKernels是deepseek开发的基于TileLang的GPU内核库，专为大语言模型运算优化 ，多数内核性能接近硬件计算与带宽极限，部分已应用于内部训练、推理场景，提供MoE路由、量化、转置等多类常用运算内核。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/tilekernels 
 ③项目：InformationKoopman 
 ★本项目针对深度学习场景下Koopman算子有限维子空间提取难题，从信息瓶颈视角切入，提出信息论拉格朗日公式平衡表示的简洁性与表达 性，配套对应算法可生成稳定可解释的 Koopman表示 ，在多类动力系统上验证了性能提升，当前已开放物理仿真相关实验代码。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/informationkoopman 
 ④项目：MonoArt 
 ★本项目是论文《MonoArt: Progressive Structural Reasoning for Monocular Articulated 3D Reconstruction》的官方实现 ，针对单目关节物体3D重建任务，由南洋理工大学S-Lab团队研发。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/monoart 
 ⑤项目：Monet 
 ★本项目是CVPR 2026收录的多模态大模型训练框架，可支持多模态大模型生成连续嵌入作为中间视觉思考 ，直接在视觉潜空间完成推理，基于定制化Qwen2.5-VL-7B实现，开源了训练、推理全流程相关代码与资源。 
 ☆一键收藏： 
 https://sota.jiqizhixin.com/project/monet2 
 跳转微信打开
```

---
