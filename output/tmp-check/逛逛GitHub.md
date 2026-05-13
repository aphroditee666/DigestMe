# 逛逛GitHub

> 分类: 微信公众号
> URL: https://wechat2rss.bestblogs.dev/feed/38be32e5376d852c13d3383e4d7a757fd9a55ff6.xml
> 抓取: 10 篇

---

## 1. 推荐 6 个小众但实用的 GitHub 开源项目，有点意思啊。

- 日期: 2026-05-09 12:03
- 链接: https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533533&idx=1&sn=82ee2499a6553977afe6de590a9b7942

```
原创 逛逛 2026-05-09 12:03 浙江 
 01 
 旧手机别扔，当麦克风用 
 这个开源项目可以 让 Android 手机变成电脑的无线麦克风。 
 支持 Wi-Fi、USB 和蓝牙三种连接方式。 
 Wi-Fi 最方便，手机和电脑在同一网络下就能用；USB 通过 ADB 连接，延迟最低；蓝牙则是不依赖网络时的备选。 
 音频处理方面，内置了降噪、自动增益和去回声，不用额外装软件处理。 
 桌面端支持 Windows、Linux 和 macOS，手机端是 Android。 你还可以自定义采样率、声道数和音频格式。 
 整个项目用 Kotlin Multiplatform 写的，Android 和桌面端共享一套代码。 
 安装的话，去 GitHub Releases 页面下载对应平台的安装包就行。 
 开源地址： https : //github.com/LanRhyme/MicYou 
 02 
 终于搞清楚 USB-C 线到底能干啥了 
 抽屉里攒了一堆 USB-C 线，不知道哪根能传数据、哪根只能充电、哪根支持 4K 投屏。 
 WhatCable 是一个 macOS 菜单栏小工具，插上线它就用大白话告诉你这根线到底能干啥。 
 Thunderbolt 5、USB4、USB 3.0、仅充电，一目了然。 
 不仅如此，它还能 告诉你为什么 Mac 充电这么慢， 是线的锅还是充电头的锅，直接定位问题。 
 它读取的是 USB-C 线缆内部的 e-marker 芯片数据，能看到这根线的实际传输速度、电流规格、甚至芯片厂商信息。 
 充电诊断功能也很实用，会列出充电头支持的所有电压档位，并高亮显示当前协商到的那个档位。 
 充电慢是因为线限制了还是充电头不给力，一看就知道。 
 安装很简单，Homebrew 一行搞定： 
 brew tap darrylmorley/whatcable && brew install --cask whatcable 
 不过有个限制，只支持 Apple Silicon 的 Mac（M1 及以上），Intel Mac 的 Thunderbolt 控制器不支持读取这些数据。 
 开源地址： https : //github.com/darrylmorley/whatcable 
 03 
 命令行直接操作 Office 文档 
 用代码处理 Office 文档一直是个麻烦事。 
 Python 有 python-docx 和 openpyxl，但功能有限， 排版复杂的文档很难搞。 
 LibreOffice 命令行能用但体积巨大。Mac 和 Linux 用户更是 经常被 Office 格式兼容性问题折磨。 
 OfficeCLI 是一个 用 C# 写的命令行工具 ，单文件二进制，不需要安装 .NET 运行时，不需要安装 Office，下载就能用。 
 它可以让你直接在命令行里创建、读取、修改 Word、Excel 和 PPT 文件。 
 所有操作通过命令行参数完成，输出结构化 JSON，特别适合 AI Agent 和自动化场景。 
 它有一个三层渐进架构： 
 第一层是语义读取，直接问它文档里有什么内容； 
 第二层是 DOM 操作，通过路径精确修改文档元素； 
 第三层是原始 XML 操作，用 XPath 直接改底层。 
 还有一个 watch 模式，可以在浏览器里实时预览文档修改效果。 
 对于经常需要批量处理 Office 文档的人，或者想让 AI 帮你写文档、搞 Excel、做 PPT 的，这个工具很实用。 
 开源地址： https : //github.com/iOfficeAI/OfficeCLI 
 04 
 AI 帮你搞定软著申请材料 
 在国内做软件开发，申请软件著作权几乎是个必经之路。 
 不管是上架应用商店、参与项目投标，还是公司需要资质，软著证书都是硬通货。 
 但准备材料很难顶。 
 比如操作说明书、代码材料、申请表信息，格式要求严格，手动准备一套下来少说也要大半天。 
 SoftwareCopyright-Skill 是一个专为 Codex 设计的 Skill， 它读取你的项目源码，自动生成全套软著申请材料。 
 操作说明书它会根据你的业务逻辑来写，不是那种千篇一律的模板。代码材料会从你的真实代码中提取，前 30 页后 30 页按规矩排好，不会拿 AI 编造的代码糊弄。 
 生成过程有多个确认检查点：业务上下文确认、申请表字段确认、代码选择确认、截图方式确认、最终稿确认。 
 每一步都可以调整，确保生成的材料符合你的实际情况。 
 最终输出三个文件：操作说明书 .docx、代码材料 .docx、申请表信息 .txt。拿 .txt 里的信息去中国版权保护中心网站填表就行。 
 开源地址： https : //github.com/Fokkyp/SoftwareCopyright-Skill 
 05 
 AI 编程黑话词典 
 Matt Pocock 最近在 GitHub 上开源了一个 AI 编程术语词典， 把 AI Coding 领域的各种行话翻译成大白话。 
 不管你是刚接触 AI 编程，还是已经在用 Claude Code、Cursor 这些工具，里面有些概念你可能也说不清楚。 
 比如 context window 到底是什么意思，token 和 turn 有啥区别，sycophancy 和 hallucination 分别指什么问题，vibe coding 和 grilling 是怎么两种截然不同的工作方式。 
 这个词典一共 7 个章节， 覆盖了模型基础、会话和上下文、工具和环境、失败模式、交接模式、记忆和引导、工作模式。 
 每个术语都有通俗解释、实际使用场景的对话示例、以及避免混淆的提示。 
 比如他会提醒你，很多人分不清 attention degradation（注意力退化）和 hallucination（幻觉），前者是上下文太长导致的遗漏，后者是无中生有。 
 他还自己造了一些词，比如 smart zone 和 dumb zone，用来描述 Agent 在不同上下文长度下的表现差异——上下文短的时候聪明得很，长了就开始犯傻。 
 整个项目就 是纯 Markdown 文档 ，直接在 GitHub 上读就行，不用安装任何东西。 
 如果你经常和 AI 结对编程，这本词典值得收藏，省得在文档里翻来翻去找概念解释。 
 开源地址： https : //github.com/mattpocock/dictionary-of-ai-coding 
 06 
 动森风格的 React 组件库 
 前面介绍了好几个实用工具，最后一个来点轻松的。 
 有人做了一套动物森友会风格的 React UI 组件库。 
 没错，就是 任天堂那个动森。 
 按钮、卡片、开关、时间显示、手机界面，全部都是动森那种圆润可爱的画风。 
 用它来做个人博客、小游戏或者孩子的学习应用，效果应该挺有意思。 
 作者自己 也用这套组件做了动森主题的个人网站模板，还有一个叫 HiKid 的儿童英语学习应用。 
 想做点好玩的小项目，或者想给孩子的学习工具换个有趣界面的话，可以玩玩看。 
 开源地址： https : //github.com/guokaigdg/animal-island-ui 
 07 
 点击下方卡片，关注逛逛 GitHub 
 这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了： 
 跳转微信打开
```

---

## 2. 这款 DeepSeek V4 终端编程神器，在 GitHub 上火了。

- 日期: 2026-05-08 12:05
- 链接: https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533532&idx=1&sn=311891bc2e17d02f132090f4197eb1da

```
原创 逛逛 2026-05-08 12:05 浙江 
 DeepSeek V4 还是挺顶的。 
 100 万 token 上下文、思维链推理、价格打到骨折，模型本身的实力没得说。 
 你用网页版聊天， V4 的编程能力根本发挥不出来。 
 你不能让它直接改文件、跑命令、Git 管理，只能复制粘贴来回复制粘贴，效率很低。 
 没有类似 Claude Code 的体验。 
 所以有人用 Rust 从零写了一个终端原生的编程 Agent，专门对接 DeepSeek V4。 
 你可以理解为 DeepSeek 原生的终端 Coding Agent。 
 01 
 开源项目简介 
 DeepSeek-TUI 是一个跑在终端里的 AI 编程 Agent，用 Rust 写的， 专门对接 DeepSeek V4 模型。 
 说白了就是 DeepSeek 版的 Claude Code。 
 它能直接在你的终端里读写文件、执行 Shell 命令、搜索网页、管理 Git、甚至编排子 Agent 并行干活。 
 地址： https : //github.com/Hmbown/DeepSeek-TUI 
 100 万 token 上下文 + 思维链实时可见 
 DeepSeek V4 最大卖点就是 100 万 token 的上下文窗口， DeepSeek-TUI 直接吃满了这个能力。 
 更关键的是它支持 Thinking-mode 流式输出，模型的推理过程你是能实时看到的。 
 它在想什么、为什么这么改，一步步摆在面前，不是黑盒给你个结果就完了。 
 100 万 token 大概相当于 75 万字 ，换算成代码差不多能把一个中型项目的全部源码一次性塞进去。 
 你不需要手动挑选哪些文件喂给 AI，整个项目结构、模块间的调用关系、配置文件、依赖声明，它一次性全看到。 
 改一个函数的时候它知道这个改动会波及到哪些地方，而 不是只盯着你贴进来的那几行代码瞎猜。 
 另外一个很实际的场景是 长对话不会失忆。 
 用 128K 上下文的工具，聊个十几轮就开始遗忘前面的约定和决策，越到后面输出质量越差。 
 100 万 token 意味着 你可以在一个会话里从需求讨论、架构设计一路干到写测试、修 bug，中间不用重新建立上下文，模型的判断力从第一轮到第五十轮基本是一致的。 
 而且上下文快满的时候会自动压缩，不会聊着聊着就失忆。 
 三种模式，干活风格随便切 
 DeepSeek-TUI 有三种工作模式： 
 Plan 模式是只读的， AI 先帮你探索代码库、规划方案，不动任何文件。适合你还不确定要怎么改的时候先用它摸个底。 
 Agent 模式是交互式的， AI 会执行操作但每一步需要你审批。适合日常开发，既高效又安全。 
 YOLO 模式就是全自动， 所有操作直接执行不需要确认。适合你信任当前环境、想快速出活的时候用。 
 三种模式可以随时切，键盘一按就换。 
 完整的工具链 + MCP 协议 
 这个项目的工具链做得相当完整：文件读写、Shell 执行、Git 操作、网页搜索、补丁应用、子 Agent 编排，该有的都有。 
 而且 原生支持 MCP 协议， 可以接各种外部工具服务扩展能力。 
 它还有一个 HTTP/SSE API 服务模式，跑个 deepseek serve --http 就能把它当无头 Agent 用，嵌入到你自己的工作流里。 
 费用也是实时追踪的，每轮对话花了多少 token、多少钱，界面上一目了然。 
 V4 Flash 的价格是输入 $0.14/百万 token，输出 $0.28/百万 token。对比一下 Claude Sonnet 输入 $3/百万 token、输出 $15/百万 token，输入差了二十多倍，输出直接差了五十多倍。 
 03 
 如何使用 
 安装很简单，一行命令： 
 npm i - g deepseek-tui 
 如果你是 Rust 用户也可以用 Cargo 装： 
 cargo install deepseek-tui-cli --locked 
 国内用户如果 npm 和 GitHub 下载慢，可以配清华 TUNA 镜像，README 里有详细步骤。 
 装好之后第一次启动会让你输入 DeepSeek API Key，去 platform.deepseek.com 申请一个就行。 
 然后直接在终端输入 deepseek 就能用了。 
 想切模式按 Tab，想调推理深度按 Shift+Tab，想看帮助按 F1。 
 04 
 点击下方卡片，关注逛逛 GitHub 
 这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了： 
 跳转微信打开
```

---

## 3. 你的 Mac 就是一个 AI Agent，4B 模型本地操控电脑。

- 日期: 2026-05-07 12:53
- 链接: https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533529&idx=1&sn=cb5c3b295b802b594f045376f79e2a8a

```
原创 逛逛 2026-05-07 12:53 浙江 
 前段时间介绍了一个开源的 Skill ，可以让 Agent 控制你的 Mac。 
 纯视觉理解桌面上的任何软件界面，像人一样去操作，而且全程跑在你自己电脑上，数据不上云。 
 继 Skill 开源之后，最近 他的端侧模型也终于开源了。 
 配套一起开源的还有一个叫 Cider 的推理加速框架，专门给 Apple Silicon 上的 MLX 模型做加速。 
 两个项目加在一起，基本把端侧 AI 从能跑推到了 跑得快、跑得好。 
 后续这个团队还会开源 mano-p 模型的训练方法，帮助开发者利用自己的数据训练定制化 GUI Agent 模型。 
 01 
 一个能在 Mac 本地跑的 GUI Agent 
 Mano-P 是一个 GUI-VLA 模型，说白了就是 用纯视觉的方式理解和操作图形界面。 
 它不依赖 CDP 协议，也不解析 HTML， 直接看屏幕截图就能定位界面元素、执行点击输入、完成复杂操作。 
 它不限于浏览器场景，桌面软件、专业工具、3D 应用都能操控。 
 训练数据方面，基于 6 万条 GUI 轨迹数据，覆盖 300 万+动作， 涵盖主流桌面和 Web 操作场景。 
 性能数据也比较夸张。 
 4B 量化模型在 Apple M4 Pro 上实现 476 tokens/s 预填充、76 tokens/s 解码，峰值内存只有 4.3GB。 
 一个 4B 的小模型，在 CUA 任务上实现了和云端大模型相当的准确率，而且完全在本地运行， 所有截图和任务数据不出设备。 
 支持离线长任务自主规划，复杂业务流程可以完全不联网就完成自主决策和纠错。 
 安装也很简单，一行命令： 
 brew tap HanningWang/tap 
 brew install mano-cua 
 装完就能用： 
 mano-cua run "打开微信告诉xxx会议延期" 
 当然也支持 Skill 的方式接入。 
 02 
 Cider 让端侧模型跑得更快的加速框架 
 Mano-P 能在 Mac 上跑得这么快，背后靠的是 Cider。 
 Cider 是团队 自研的推理加速框架 ，基于 Apple MLX 生态。 
 它补齐了 MLX 原生框架缺失的 W8A8 和 W4A8 量化计算能力。 
 MLX 目前支持 W4A16、W8A16 这些权重量化模式，但缺少激活量化。 
 Cider 通过调用 Apple 底层 Metal 4 API， 首次在 Apple GPU 上实现了硬件加速的 INT8 TensorOps 计算。 
 实测数据： 
 W8A8 模式下，算子速度比 MLX 原生提升 1.4x 到 1.9x，具体取决于 batch size。 
 拿 Qwen3-8B 举例，FP16 原生预填充 1695 tokens/s，经过 Cider 的 W8A8 加速后能到 2531 tokens/s， 接近 1.5 倍。 
 Llama3-8B 也类似，从 1727 提到 2520 tokens/s。 
 对于 Qwen3-VL-2B 这样的视觉语言模型，chunked prefill 场景中端到端 预填充加速 57% 到 61%。 
 接入方式极其简单，一行代码就能把任何 MLX 模型的 Linear 层替换成 Cider 加速版本： 
 from cider import convert_model, is_available 
 model, proc = load( "path/to/model" ) 
 if is_available(): 
 convert_model(model) 
 # CiderLinear auto-detects: 
 # seq_len > 1 - W8A8 INT8 TensorOps (faster prefill) 
 # seq_len == 1 - INT8 MV kernel (near-native decode speed) 
 else : 
 pass # Falls back to standard MLX inference on M4 
 它会自动判断：seq_len > 1 用 W8A8 INT8 TensorOps 加速预填充，seq_len == 1 回退原始权重保证解码最优。 
 不需要手动切换。 
 Cider 不只是给 Mano-P 用的。Qwen、Llama、Mistral，只要你的模型跑在 MLX 上，都能用 Cider 加速。 
 03 
 用 Mano-P 能干什么 
 全自动化应用构建流程。 
 你用自然语言描述需求，系统依次完成需求澄清、架构设计、代码生成、本地部署。 
 然后开始多层级测试，先是 API 接口测试，再是 LLM 页面视觉检测，最后通过 VLA 模型做端到端的 GUI 自动化测试。 
 测试没通过的话，自动定位问题、修复代码、重新部署， 循环迭代直到全部通过。 
 整个流程不需要人工干预。 
 再比如，还能做 商业视频智能系统 ，从下发指令开始，自动完成视频生成、上传、分析、剪辑到二次评测。 
 系统自己操作网页和剪辑软件，处理文件、修改字幕，最后生成包含主观评价和客观指标的分析报告。 
 这些场景的核心特点是一样的： 大量截图和界面操作数据，全部在本地处理，不上传到任何云端。 
 从成本角度看这件事更有意思。 
 全自动编程流水线里，GUI 测试消耗的云端 token 占比超过 59%。 
 API 测试只能验证接口是否正常，但软件是否真的 可用 ，得有人打开界面操作一遍才知道。 
 这个过程天然依赖多模态理解，模型要持续处理截图、定位元素、执行操作、判断结果，推理消耗非常大。 
 Mano-P 把这部分开销直接归零，不调 API，不传截图，不花一分钱。 
 和 Claude Computer Use 对比一下： 
 Claude 在 OSWorld 上的综合成绩确实更高（72.1% vs Mano-P 58.2%），但 Claude 需要云端 API 调用，你的截图和任务数据都要上传。 
 Mano-P 完全在本地运行，数据不出设备。 
 如果你的场景对隐私和安全有要求，比如企业内部系统测试、处理敏感数据的自动化流程，端侧方案是目前更现实的选择。 
 开源地址： 
 Mano-P： https://github.com/Mininglamp-AI/Mano-P 
 Cider： https://github.com/Mininglamp-AI/cider 
 Mano-P 证明了端侧 GUI Agent 的应用价值，Cider 则解决了端侧 AI 落地最底层的问题： 如何让模型在 Mac 上更快、更省内存、更接近真实可用。 
 从 Mano-P 到 Cider，明略科技正在建设端侧 AI 、私有化AI的基础设施能力。 
 04 
 点击下方卡片，关注逛逛 GitHub 
 这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了： 
 跳转微信打开
```

---

## 4. GitHub上狂揽 1.1 万 Star，22 岁开发者逆向工程了 Claude Mythos。

- 日期: 2026-05-06 14:48
- 链接: https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533526&idx=1&sn=716bda7ad91edafbe1206ad84ba4843a

```
原创 逛逛 2026-05-06 14:48 浙江 
 上个月 Anthropic 放出了一个叫 Claude Mythos Preview 的模型。 
 这个模型强到离谱。 
 英国 AI 安全研究所对它做了测试，发现它能自主完成一整套企业网络攻击： 32 个步骤的攻击链，人类专家估计要花 20 个小时，它自己跑完了。 
 专家级 CTF 挑战，成功率 73%。 
 然后 Anthropic 决定： 不对公众开放。 
 Mythos Preview 只开放给了 40 多家技术公司的联盟，属于 Project Glasswing 计划，专门用来做关键基础设施的安全评估。 
 Anthropic 明确说了， 没有计划让它公开发布。 
 能力太强，风险太高，锁起来了。 
 但问题来了：Anthropic 从来没公开过 Mythos 的技术架构。没有论文，没有技术报告，连架构细节都讳莫如深。 
 然后一个 22 岁的开源开发者 Kye Gomez，硬是从公开的学术论文里拼凑线索，用纯 PyTorch 把这个架构假设给“复现”了出来。 
 项目叫 OpenMythos，开源 4 天就拿下了近 7000 Star，现在已经 1.1 万了。 
 GitHub Issues 里直接吵翻了。 
 有人说是天才之作，有人开 issue 叫 "This is still dumb"。 
 01 
 开源项目简介 
 先说 OpenMythos 到底干了什么。 
 传统的大模型，比如 GPT、LLaMA，都是靠堆层数来提升能力。 
 100 层不够就 200 层，200 层不够就 400 层。 
 每层都是独立的一组参数， 参数量直接拉满。 
 OpenMythos 走了一条完全不同的路： 它不堆层数，而是让同一组权重反复跑很多遍。 
 你可以理解为：传统模型像读一本书，翻一页就是一页，翻完了就完了。OpenMythos 像是让一个人反复读同一段内容，每读一遍都更深入地理解一次。 
 推理深度不再取决于你有多少参数，而是你愿意让模型"想"多少遍。 
 效果怎么样？ 
 770M 参数的循环模型，能匹敌 1.3B 的传统 Transformer。同样的效果，参数量省了快一半。 
 开源地址： https : //github.com/kyegomez/OpenMythos 
 02 
 架构亮点 
 OpenMythos 的架构分三段： 前奏层（Prelude）、循环块（Recurrent Block）、尾声层（Coda）。 
 前奏和尾声就是普通的 Transformer 层，跑一遍就过。中间的循环块是核心，同一组权重循环跑 T 次。 
 这里挑三个最值得说的点。 
 循环推理，越想越深 
 循环块每跑一轮，都会把当前状态和原始输入重新混合。不是简单的重复计算，而是每轮都在前一轮的基础上做更深一层的推理。 
 最厉害的是深度外推能力。 
 训练的时候让模型跑 16 轮循环，推理的时候你可以直接让它跑 24 轮甚至 32 轮，模型从来没见过这么深的推理链，但依然能泛化。 
 简单的问题少跑几轮，难的问题多跑几轮，不用改模型，改个参数就行。 
 MoE + MLA，省显存还能选专家 
 循环块里塞了混合专家系统（MoE），用的是 DeepSeekMoE 那套细粒度路由机制。 
 不同的循环深度可以激活不同的专家子集，相当于同一组权重在不同的循环轮次里干不同的活。 
 注意力部分支持两种后端：一种是 Multi-Latent Attention（MLA），来自 DeepSeek-V2，KV 缓存能缩小 10 到 20 倍 
 另一种是 Grouped Query Attention（GQA），支持 Flash Attention 2 加速。两种可以切换。 
 还有一个 Adaptive Computation Time（ACT）机制，让模型自己学会在哪个位置停下来。 
 简单的 token 早点退出，难的 token 多算几轮，全在同一个 batch 里搞定。 
 训练不会炸的硬核保证 
 循环 Transformer 一直有个老大难问题：训练不稳定。同一组权重反复跑，梯度容易爆炸或者消失，历史上很多人尝试过都折在这了。 
 OpenMythos 的解法是 LTI 注入。它把状态更新做成一个线性时不变系统的离散化，注入矩阵 A 通过零阶保持离散化构造，谱半径构造性地保证严格小于 1。不管你学习率设多少，训练过程在数学上就是稳定的。 
 所有计算都在对数空间里做，还加了 clamp 防止 float32 精度溢出。这个稳定性保证不是靠调参调出来的，是靠数学构造出来的。 
 03 
 争议与真实状态 
 说了这么多亮点，也该说实话了。 
 OpenMythos 目前没有训练好的权重，没有发布的 benchmark 数据，没有任何实际的推理输出样本。 
 它能编译通过，架构是对的，但还没有真正跑出结果。 
 GitHub Issues 里的讨论非常两极化。 
 有人在做第三方的 benchmark 尝试： 
 有人提了 Flash Attention 和混合精度训练的优化建议。 
 也有人直接在 issue 开骂。。。 
 还有人请求官方发布 benchmark，目前还没有回应。 
 所以 OpenMythos 的定位很明确： 这是一个架构假设的代码实现，不是可以直接用的产品。 
 它验证的是 如果 Claude Mythos 的架构真的是循环深度 Transformer，那它大概长这样。 
 这个定位本身就很有意思。 
 在开源 AI 领域，大部分项目都是在复现已有的论文。 
 OpenMythos 是在复现一个从未被确认存在的架构。 
 04 
 如何使用 
 安装很简单： 
 pip install open-mythos 
 项目预置了从 1B 到 1T 的七种模型配置： 
 import torchfrom open_mythos 
 import OpenMythos, mythos_1bfrom open_mythos.tokenizer 
 import MythosTokenizer 
 # 加载 1B 配置 
 config = mythos_1b() 
 model = OpenMythos(config) 
 tokenizer = MythosTokenizer() 
 # 推理生成 
 ids = torch.tensor([tokenizer.encode( "Explain quantum computing" )]) 
 output = model.generate(ids, max_new_tokens=512, temperature=0.7) 
 如果要用 GQA 注意力后端： 
 config = mythos_3b()config.attn_type = "gqa" 
 config.n_kv_heads = 8 model = OpenMythos(config) 
 训练脚本在 training/ 目录下，支持 PyTorch FSDP 分布式训练，默认用的是 FineWeb-Edu 数据集。 
 OpenMythos 把 AI 领域的 Scaling Debate 从 堆多少参数 推向了 推理时算多少轮 。 
 不管 Claude Mythos 到底是不是这个架构，循环深度 Transformer 本身就是一个值得关注的方向。 
 770M 打平 1.3B，省的不只是参数，更是训练成本和部署门槛。 
 至于它是不是真的复现了 Mythos， 现在还无法验证。 但至少，它给了一个足够具体的假设，具体到可以被证伪。 
 05 
 点击下方卡片，关注逛逛 GitHub 
 这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了： 
 跳转微信打开
```

---

## 5. GitHub 上狂揽 1.8 万 Star！开源平替的 Claude Design。

- 日期: 2026-05-05 12:24
- 链接: https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533509&idx=1&sn=63efab10344f2db0e4f2965dc9bbaeab

```
原创 逛逛 2026-05-05 12:24 北京 
 Claude Design 发布没多少天，GitHub 上就有人做了 开源复刻版。 
 4 月 17 日 Anthropic 上线 Claude Design，基于 Opus 4.7。 
 输入一句话，直接出设计成品 ，不是草图，不是线框图，是能交付的 HTML 页面、PPT、移动端原型。 
 效果确实炸裂，瞬间出圈。 
 11 天后，nexu-io 团队 把 Open Design 开源了。 
 现在已经快 2 万的星星了。 
 01 
 开源项目简介 
 Open Design 是 Claude Design 的开源替代品。 
 但它不自带 AI 模型， 它做的事是把你电脑上已经装好的 Coding Agent 变成设计引擎。 
 你输入一句话需求，比如「帮我做一份杂志风的官网」，这个先弹出一个表单 确认你的需求 ，比如目标平台、受众、调性、品牌啥的。 
 然后 Agent 从 5 套视觉方向里选一个，拉出一份实时 Todo 计划，在 你电脑上创建真实的项目目录。 
 读模板、写 CSS、生成 HTML，最后在沙盒 iframe 里渲染出来。 整个过程你可以随时介入纠偏。 
 输出不是截图，不是草图，是完整的单文件 HTML，可以直接导出为 HTML、PDF、PPTX、ZIP。 
 Claude Code、Codex、Cursor、OpenCode 等等，哪个在就用哪个。 
 内置 19 个可组合 Skill + 71 套品牌级 Design System 
 可以看成是把你手上最强的 Coding Agent 接进设计工作流的中间层。 
 开源地址：github.com /nexu-io/ open - design 
 02 
 什么原理 
 这个项目的架构分两层： 浏览器里跑一个 Next.js Web 界面，你电脑本地跑一个 Node daemon 服务。 
 核心流程是这样的： 
 你输入需求后，daemon 把 SKILL.md 设计能力描述和 DESIGN.md 品牌风格规范 拼装进提示词栈，然后通过 stdio 调用你机器上的 coding agent CLI 去执行。 
 Agent 拿到的是真实文件系统权限，它真的在你的电脑上读模板文件、grep CSS 里的 hex 色值、写 brand-spec.md、生成 HTML 和图片。 
 不是虚拟沙盒，不是内存模拟。 
 agent 跑完一轮，daemon 把产出的 HTML 塞进沙盒 iframe 实时预览。你可以在界面上直接编辑文件，也可以一键导出 HTML、PDF、PPTX、 ZIP。 
 你有什么 Agent 它就用什么 Agent 
 Daemon 启动的时候自动扫 PATH，检测你装了哪些 CLI。 
 不绑定任何一家模型，每一层都是 BYOK。 
 Claude Design 只能用 Opus 4.7，Open Design 用你手上最强的那个 agent 就行。 
 反 AI 味的提示词工程 
 这个项目在提示词层面做了不少事来防止 AI 生成那种一眼假的设计。 
 开始生产之前，先弹一个初始化问题表单，让你选 surface、受众、调性、品牌上下文。 
 30 秒勾选完，比来回改需求高效得多。 
 输出之前还有一轮五维自评审，AI 自己给自己打分， 低于 3 分的维度要重做。 
 另外还有一份 slop 黑名单 ，暴力紫渐变、通用 emoji 图标、手绘 SVG 真人脸、Inter 当 display 字体，全部明令禁止。 
 没有真数字就写破折号，不编数据。 
 71 套 Design System + 19 个 Skill 开箱即用 
 71 套品牌设计系统，Apple、Stripe、Vercel、Airbnb、Tesla、Notion、Cursor、Figma，直接从下拉框选，切换后下一次渲染就用新 token。 
 19 个 Skill 覆盖网页原型、杂志风 PPT、Dashboard、移动端原型、定价页、邮件营销、社媒轮播图等等。 
 03 
 怎么跑起来 
 三条命令： 
 git clone https://github.com/nexu-io/open-design.git 
 cd open-design 
 pnpm install && pnpm dev:all 
 最简单的办法是把开源项目丢给你的 Agent，让它自己装。 跑起来后打开 localhost:3000， 选一个 Skill、选一套 Design System、写需求，回车就行。 它会先弹问题表单让你锁定需求，然后 agent 开始干活， 
 实时 todo 卡片流入 UI，最后在沙盒 iframe 里渲染成品。 
 支持导出 HTML、PDF、PPTX、ZIP。 
 04 
 点击下方卡片，关注逛逛 GitHub 
 这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了： 
 跳转微信打开
```

---

## 6. GitHub 上 3.7 万的 Star，终端里浏览文件的开源工具。

- 日期: 2026-05-04 12:10
- 链接: https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533435&idx=1&sn=17a5ceb8d01d4249175e29d31cb8e4d8

```
原创 逛逛 2026-05-04 12:10 山东 
 我把终端文件管理换成了 yazi，效率起飞。 
 最近这一两年工作方式变化挺大的。 
 自从用上 Claude Code 这类工具之后，已经基本离不开了， 每天大部分时间都泡在终端里。 
 AI 能帮你搞的，几乎全在 terminal 里完成。 
 反而又开始琢磨怎么把终端命令行用的爽了，配色主题、shell 提示符、tmux、模糊搜搜索。 
 一通折腾下来，终端确实越来越顺手。 
 最近又发现一个开源项目，叫 yazi， 专门解决终端里管理文件的问题。 
 GitHub 上目前 37k+ Star，过去一年多从 15k 直接涨到 37k， 增速很猛。 
 试用了几天之后，原来的 ranger 我就直接卸了。 
 01 
 这玩意儿到底是干嘛的 
 yazi 这名字取自鸭子的中文谐音 ，是一个用 Rust 写的终端文件管理器，整个架构基于异步 I/O。 
 说白了就是让你在终端里像在 Finder 或者文件资源管理器里那样 翻文件夹、预览文件、做批量操作。 
 但所有操作都很快，不卡。 
 开源地址： https : //github.com/sxyazi/yazi 
 为啥会火，主要是下面这几点。 
 ① 全异步 I/O，进文件夹是真的快 
 这是 yazi 最核心的卖点。 
 所有文件操作都不会阻塞界面，哪怕你进一个塞了几万个文件的文件夹，它也不会卡死，文件列表一边加载一边可以操作。 
 CPU 密集的任务自动分散到多线程， 跑大任务的时候右下角实时显示进度，还能随时取消。 
 之前用 ranger 进大目录，那个加载等待的体感非常折磨。 
 yazi 一上手最明显的差别就是这个， 秒开。 
 ② 终端里直接看图片、视频、PDF 
 yazi 内置了一堆图片协议支持，Kitty、iTerm2、Überzug++、Chafa 啥的全都集成了，几乎覆盖所有主流终端。 
 实际效果就是：你在终端里光标移到一张图片上， 右边预览面板里直接出图，不用切到图形界面去看。 
 视频可以预览第一帧、PDF 能看页面、代码文件自带语法高亮。 
 这套体验整下来，文件管理就不用反复在 GUI 和 terminal 之间切换了。 
 ③ Lua 插件系统，能玩花样 
 yazi 的扩展能力非常强，UI 插件、功能插件都能用 Lua 自己写，社区已经有一堆现成的插件可以直接装。 
 自定义预览器、预加载器、文件探测器，全都是 Lua 配的， 门槛比改源码低多了。 
 随便举个例子，想让某种特定后缀的文件用某个工具来预览，写几行 Lua 就搞定。 
 这个扩展性比 ranger 那套 Python 脚本要现代得多。 
 ④ 把一堆现代命令行工具都串起来了 
 yazi 默认就 集成了 ripgrep、fd、fzf、zoxide 这些工具。 
 搜内容用 ripgrep、找文件用 fd、模糊查找用 fzf、智能跳转目录用 zoxide。 
 这套组合拳打下来，搜索和导航的体验非常顺滑。 
 操作上是 Vim 键位，j/k 移动、gg/G 跳转、v 进入视觉模式，Vim 用户基本零成本上手。 
 多标签页、批量重命名、Git 状态显示、回收站、鼠标支持，日常需要的能力基本都齐了。 
 02 
 怎么装 
 装起来非常简单。 
 macOS 直接： 
 brew install yazi --HEAD 
 装完之后，建议把这几个 伴生工具 一起装上：ffmpeg、7zip、jq、fd、ripgrep、fzf、zoxide、imagemagick。 
 少了这几个里的某个，对应的预览或者搜索能力就会缺一块，体验会打折扣。macOS 一行 brew 全搞定： 
 brew install ffmpeg sevenzip jq fd ripgrep fzf zoxide imagemagick 
 配置文件都在 ~/.config/yazi/ 下面，主题、键位、插件全在这里改。 
 官方文档和社区都给了不少现成的配置， 照着抄一份基本就够用了。 
 我个人比较推荐再配一个 shell 函数，让你按 q 退出 yazi 的时候，shell 的当前目录自动跳到 yazi 里最后停留的目录。 
 这个体验装上之后会非常上头，等于是把 yazi 当成 cd 的图形化版本来用。 
 03 
 点击下方卡片，关注逛逛 GitHub 
 这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了： 
 跳转微信打开
```

---

## 7. 这个 GitHub 项目太缺德了，拿鞭子抽 Claude Code。

- 日期: 2026-05-03 08:22
- 链接: https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533407&idx=1&sn=9c458a0617106eb13679cf408a8db7a6

```
原创 逛逛 2026-05-03 08:22 山东 
 哈哈哈哈哈，发现了一个专门鞭策 Claude Code 的沙雕神器。 
 用过 Claude Code 的都懂，它啥都好，就是 偶尔会犯懒。 
 一个简单的重构，转圈转个十几秒。 
 一段本来五分钟能搞定的代码，它在那儿反复改同一行，越改越离谱。 
 更顶的是偶尔陷入死循环，读文件、改文件、读文件、改文件，你只能干瞪眼看着它表演。 
 这时候手动 Ctrl-C 打断吧，总觉得缺点仪式感， 打断完还得自己打一长串话告诉它刚才在瞎搞。 
 最近刷到了这个开源项目，一看我直接笑出声，它的解决方案是： 给 Claude Code 上鞭子 。 
 01 
 开源项目简介 
 项目叫 OpenWhip， 是一个基于 Electron 的跨平台桌面小工具 ，作者在 README 开头就一句话交代动机： 
 有时候 Claude Code 跑得太慢，你需要一根鞭子来鞭策它。 
 说白了就是一个桌面小工具，你嫌 AI 摸鱼了，点一下图标，一条鞭子从屏幕飞出来抽它一下。 
 顺便替你按 Ctrl-C 打断当前任务，再冒出一句随机的吐槽话术。 
 工作原理也非常直接： 
 看到 CC 犯懒，点击鞭子图标 
 屏幕上生成一条鞭子 
 再点一下屏幕任意位置，鞭子挥下去 
 系统自动向 Claude Code 发一个 Ctrl-C 中断信号 
 顺便从 5 条预设话术里随机甩一条鼓励/羞辱的消息过去 
 非常符合一个打工人 面对摸鱼 AI 时的真实情绪。 
 这玩意儿还挺有梗的 
 这个项目能一周多冲上 2.3K Star，算是你看到 AI 摸鱼犯傻时候的 情绪出口。 
 ① AI 摸鱼时的情绪出口 
 用 Claude Code 写过复杂任务的都有体会，有时候它会陷在某个小问题里出不来，来回改来回试，你看着进度条转啊转，手放键盘上又不知道该说啥。 
 这个时候多一个能让你发泄一下的按钮，还挺搞的。 
 手动按 Ctrl-C 打断，功能上是一样的，但就是少了点情绪价值。OpenWhip 的鞭打动画加上随机话术，相当于给你一个合法的情绪出口。 
 ② Roadmap 比项目本身还好笑 
 这项目最顶的地方是作者写的 Roadmap，我直接摘一下： 
 03、怎么装来玩 
 部署非常简单，一条命令搞定： 
 npm install - g openwhip 
 openwhip 
 装完直接运行，右上角会出现一个鞭子图标，点它就能用。 
 平台支持上： 
 macOS / Windows：开箱即用 
 Linux：需要额外装一下 xdotool ，这个是用来模拟键盘按键的，大部分发行版都能直接 apt install xdotool 或者 pacman -S xdotool 搞定 
 装好之后，打开一个 Claude Code 的终端窗口跑点活儿， 等它开始摸鱼的时候，点托盘图标、点屏幕，一气呵成。 
 值得提一句的是，因为要给它发全局快捷键，首次运行的时候 macOS 会弹窗让你授权辅助功能权限，这一步正常授权就行。 
 03 
 点击下方卡片，关注逛逛 GitHub 
 这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了： 
 跳转微信打开
```

---

## 8. 快瞧瞧 4 月 GitHub 上哪些开源项目最火火火火？

- 日期: 2026-05-02 11:13
- 链接: https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533406&idx=1&sn=5cf3e7d5020d2d474cde1a8c35fb127a

```
原创 逛逛 2026-05-02 11:13 山东 
 01 
 一个 Rust 写的省 token 神器 
 如果你平时用 Claude Code，可能没注意到一个事情： 每次执行 git status、npm test 这些命令的时候，AI 工具会把所有输出都塞进上下文窗口 。 
 一次 git status 就能吃掉约 2000 个 token，跑一次测试更是上万。 
 这些冗余输出挤占了模型的推理空间，上下文窗口过早溢出，API 费用也跟着涨。 
 RTK 就是专门解决这个问题的。 
 它是一个用 Rust 写的 CLI 代理工具，拦截并压缩这些命令的输出，平均压缩率能达到 80-90%。 
 支持超过 100 种命令的智能过滤， 覆盖 git、测试框架、构建工具、Docker、AWS 等场景。 
 它的原理是通过 Hook 机制自动改写命令，比如把 git status 变成 rtk git status，对 AI 来说完全透明，你什么都不用改。 
 单个二进制文件，零依赖，开销低于 10ms，已经支持 Claude Code、Cursor、Gemini CLI、Codex 等 12 种 AI 工具。 
 对于重度使用 AI Coding 工具的开发者来说， 这个工具能直接帮你省钱，同时让会话的上下文活得更久，AI 的推理质量也更稳定。 
 开源地址： https : //github.com/rtk-ai/rtk 
 02 
 让 AI Coding 不再抛硬币 
 用 AI Coding 工具修一个 bug， 跑三次可能得到三个不同的结果。 
 有时候它会跳过测试，有时候忘了做代码审查，有时候 PR 描述写得乱七八糟。 
 每次运行都像抛硬币，缺乏确定性。 
 Archon 的核心理念是：Dockerfile 规范了基础设施，GitHub Actions 规范了 CI/CD，那 AI 编码流程也需要一个规范。 
 它把开发流程编码成 YAML 工作流 ，确定性步骤，跑测试、执行脚本和规划、代码生成混合编排，AI 只在需要智能的环节介入。 
 每次工作流运行在独立的 git worktree 中，5 个修复任务可以并行执行互不冲突。 
 内置了 17 个默认工作流，修 issue、从想法到 PR、代码审查、安全重构这些场景都有。 
 还有 Web UI 可以可视化拖拽编辑，支持从 Slack、Telegram、Discord、GitHub 远程触发。 
 这个项目最近刚经历了一次完全重写 ，从 Python 迁移到了 TypeScript， 定位也从 AI Agent 构建器转型为 AI 编码工作流引擎。 
 开源地址： https : //github.com/coleam00/Archon 
 03 
 在手机上离线跑大模型 
 Google 最近开源了一个端侧 AI 展示应用 AI Edge Gallery， 让你直接在手机上跑大语言模型，完全离线，不用连网。 
 AI Chat 支持思考模式，可以看到模型的推理过程。 
 Ask Image 能理解图片内容，Audio Scribe 实时语音转录翻译，Prompt Lab 可以调参数做实验。 
 还有一个 Agent Skills 系统，可以加载模块化技能比如查 Wikipedia、地图交互等，把 LLM 从纯聊天工具变成主动助手。 
 它还支持模型基准测试， 能对比不同模型在你手机上的性能表现。 
 底层基于 LiteRT 运行时做了优化，最新版已经支持 Gemma 4 系列模型。目前已经上架了 Google Play 和 App Store，Android 12+ 和 iOS 17+ 都能用。 
 不管你是想体验一下端侧 AI 的能力，还是评估手机硬件能跑什么模型，都值得装一个试试。 
 开源地址： https : //github.com/google-ai-edge/gallery 
 04 
 AI 生成真正可编辑的 PPT 
 PPT Master 生成的是真正 的原生 PPTX 文件。 
 每个形状、文本框、图表都是独立的可编辑对象，在 PowerPoint 里想怎么改就怎么改。 
 使用方式很简单， 丢给它 PDF、Word、URL 或者 Markdown 文档，它就能生成完整的演示文稿。 
 支持自定义模板，内置了 22 个示例项目共 309 页，还有各种风格可选：杂志风、学术风、暗黑艺术风、自然纪录片风、科技 SaaS 啥的。 
 开源地址： https://github.com/hugohe3/ppt-master 
 05 
 3300 行代码实现自进化 Agent 
 GenericAgent 是一个极简但野心很大的项目， 核心代码只有约 3000 行，却实现了完整的自进化 Agent 系统。 
 目前 8.4K Star。 
 它的核心思路是用一棵 技能树 从小种子长出全面的系统控制能力。 
 Agent 从 9 个原子工具 读文件、写文件、执行命令、搜索等 和约 100 行的 Agent Loop 出发，通过不断执行任务来积累和进化技能。 
 整个系统采用分层记忆架构 L0-L4，从短期工作记忆到长期知识库，让 Agent 能真正「记住」和「成长」。 
 单次任务消耗不到 30K token，而传统方案通常需要 200K 到 1M。 
 它支持 Claude、Gemini、Kimi、MiniMax 等多种模型，内置真实浏览器注入能力，还提供了 QQ、微信、Telegram、飞书、钉钉等机器人前端。 
 整个仓库的代码都是 Agent 自己开发的。 
 想研究怎么用最少的代码实现最强的 Agent 能力，这个项目值得深入研究。 
 开源地址： https : //github.com/lsdefine/GenericAgent 
 06 
 又一个 SKill 包 
 mattpocock/skills 是 TypeScript 大佬 Matt Pocock 出品的 Claude Code Skills 合集。 
 口号是 Skills for Real Engineers 。 
 它 针对 AI 编程的 4 个失败模式对症下药： 
 需求对不齐就用 /grill-me 和 /grill-with-docs 做深度问答，逼你把需求想清楚。 
 AI 输出啰嗦就建立共享语言和 CONTEXT.md 让沟通更精准。 
 代码容易出错就用 /tdd 强制测试驱动开发。 
 架构变成面条就靠 /caveman、/zoom-out、/improve-codebase-architecture 这些技能来重构。 
 此外还有 /diagnose 排查问题、/triage 分类 issue、/to-issues 拆任务、/to-prd 写产品文档等实用技能。 
 安装非常简单，一行命令搞定： 
 npx skills @latest add mattpocock/skills 
 每个 Skill 都是精心设计的 Claude Code 工作流，不是简单的 prompt 模板，而是把最佳实践编码成可重复执行的流程。 
 如果你在用 Claude Code 做严肃的项目开发，这个技能包能让你的开发体验直接上一个台阶。 
 开源地址： https : //github.com/mattpocock/skills 
 07 
 Google 出品的端侧推理引擎 
 LiteRT-LM 是 Google 推出的端侧大模型推理框架， 专门为手机、树莓派这类资源有限的设备做优化。 
 目前已经用在了 Chrome、Chromebook Plus、Pixel Watch 等 Google 自家产品里。 
 它支持 Android、iOS、Web、桌面、IoT 全平台，通过 GPU 和 NPU 硬件加速来压榨性能。 
 支持多模态输入和 Tool Use 函数调用， 可以用来构建端侧的 AI Agent 工作流。模型兼容性也不错，Gemma、Llama、Phi-4、Qwen 这些主流模型家族都支持。 
 最近增了 Gemma 4 支持和一个 CLI 工具，一行命令就能在终端跑模型。 
 提供 Kotlin、Python、C++ 三种 API，Swift 版本还在开发中。 如果你在做移动端或者嵌入式设备的 AI 集成，这个框架值得关注。 
 开源地址： https : //github.com/google-ai-edge/LiteRT-LM 
 08 
 其它热门项目 
 下面这 8 个项目之前文章里已经详细介绍过了，这里简单带一下。 
 hermes-agent： 这个月一口气涨了 10 万多 Star，是一个能 随你一起成长的 Agent 框架，支持自定义工具和记忆系统。 
 markitdown： 微软出品的文件转 Markdown 工具，你丢给它 PDF、Word、PPT、Excel 各种文件，它都能给你 转成干净的 Markdown 格式 ，处理文档的时候非常方便。 
 andrej-karpathy-skills： 作者基于 Karpathy 公开分享的对 LLM 编码陷阱的观察，整理出了一份 CLAUDE.md 配置文件。 直接丢到你的项目里就能改善 Claude Code 的编码行为。 
 claude-mem： 一个 Claude Code 的记忆插件，它能自动记录你每次和 Claude Code 的编码会话，压缩之后注入到以后的对话里，解决上下文丢失的老问题。 
 hackingtool： 一个老牌的渗透测试工具合集，里面集成了各种安全测试工具，做安全的朋友应该都不陌生。 
 claude-howto： 一个 Claude Code 的可视化教程，从基础概念到高级 Agent 开发，都配了可复制粘贴的示例模板，新手入门非常友好。 
 oh-my-codex： 专门给 OpenAI Codex 加各种增强功能，加了 hooks、HUD 界面、Agent 团队协作这些功能，把 Codex 的体验拉高了一个档次。 
 free-claude-code： 一个轻量级代理服务器，把 Claude Code 的 API 请求转发到免费的第三方 LLM 服务上，只需配两个环境变量就能用。 
 09 
 点击下方卡片，关注逛逛 GitHub 
 这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了： 
 跳转微信打开
```

---

## 9. GitHub 上狂揽 4.6 万 Star！这款 AI 终端神器终于开源了。

- 日期: 2026-05-01 13:09
- 链接: https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533405&idx=1&sn=1ee7cfefd01d9fd9c666e5d4cf22dce0

```
原创 逛逛 2026-05-01 13:09 北京 
 开源不到 24 小时就冲上了 3.5 万 Star。 
 现在总 Star 已经超过 5 万了， 这个项目叫 Warp，是一个用 Rust 从零开发的 AI 终端。 
 准确说，它已经不只是终端了，官方给它的定位是 Agentic Development Environment，智能体开发环境。 
 它还被 TIME 评为 2025 年最佳发明之一。OpenAI 是这个开源仓库的创始赞助商。 
 01 
 开源项目简介 
 Warp 是一个 AI 原生终端，用 Rust 写的，支持 macOS、Linux、Windows 三大平台。 
 它 不是在传统终端上套了个 AI 壳，而是从第一天起就按 AI 工作流设计的。 
 Warp 的核心思路很直接 ：把终端重新做一遍。 
 传统终端就是命令输入、输出、滚动、继续输入的死循环。 
 Warp 不走这条路，它用 Block 模型替代了传统的滚动输出。 
 每一条命令和它的输出被组织成一个独立的块，你可以像在编辑器里一样选中、复制、搜索、分享。 
 目前已经有超过 70 万活跃开发者在用。 
 创始人 Zach Lloyd 在博客里讲了三个开源原因： 
 第一，软件开发的方式已经变了。 
 AI 能完成大部分代码撰写，人类的核心工作变成了想清楚做什么和判断做出来的东西对不对。开源能让社区一起推动进步。 
 第二，更现实的原因。 
 他正跟资金更充足的闭源对手竞争，没法靠补贴打价格战，想通过开源打造更好的产品来突破。 
 第三，五年前他在 Hacker News 发布 Warp 时就 承诺过会开源 ，这次是兑现承诺。 
 GitHub 地址： https : //github.com/warpdotdev/warp 
 02 
 和普通终端到底有什么不同 
 你可能觉得终端不都长一个样，黑底白字敲命令呗。 
 用了 Warp 之后你会发现，差别其实挺大的。 
 先说传统终端的痛点。 
 所有输出 混在一起一屏滚动 ，想找之前某条命令的输出得往上翻半天。 
 复制粘贴靠鼠标框选，经常多选一行或少选一行。跑个长命令只能干等着，中间出了错一闪而过，还得重新跑一遍再看。 
 这些问题用了这么多年终端，大家都习惯了，但习惯不代表合理。 
 Block 块状交互。 
 Warp 把终端输出做了结构化处理。 
 每条命令和它的输出是一个 Block，自带元数据：命令内容、执行时间、工作目录、退出码等等。 
 你可以基于这些 Block 做搜索、过滤、分享。 
 比如你跑了一个构建命令失败了， 可以直接把这个 Block 分享给同事，他看到的就是完整的上下文，不需要截图加文字解释半天。 
 这个设计说实话很实用，用过就回不去了。 
 AI 原生，不是后来加上去的。 
 你可以直接在 Warp 里调用内置的 AI Agent 来写代码、调试、重构，新的 Agentic 管理工作流由 GPT 模型驱动。 
 普通终端是先做好终端再想办法加 AI 插件，Warp 是从一开始就围绕 AI 工作流设计的。 
 内置了完整的 Agent 化开发环境，能直接接入 Claude Code、Codex、Gemini CLI、Opencode 这些外部 CLI Agent。 
 等于在终端里装了一个 AI 调度中心，你可以在这里统一管理和调用各种 AI 编程工具。 
 这次开源还新增了 Kimi、MiniMax、Qwen 等开源模型的支持，并加入了 auto (open) 自动路由功能，能根据任务智能匹配最合适的模型。 
 交互式代码审查。 
 以前 Agent 写完代码，你得切到 IDE 里看一遍，确认没问题再提交。 
 现在直接在 Warp 终端里就能逐行审查、加注释、一键丢回去让 Agent 改。 
 把 Agent 的工作完成度从 80% 推到 100%，这一步不用再切窗口了。 
 自研 GPU 加速 UI 框架 
 Warp 没用 Electron，也没用 Qt，而是完全用 Rust 从零写了一套 GPU 加速的 UI 框架，叫 WarpUI。 
 整个代码库有 60 多个 crate，Rust 代码占比 98%。 
 它的渲染速度极快，输入延迟几乎感知不到。在你疯狂敲命令的时候，不会出现某些终端那种卡顿和画面撕裂。 
 而且 WarpUI 这部分是 MIT 协议的，你可以把它拿到自己的 Rust 项目里用。 
 03 
 如何使用 
 方式一：直接下载安装 
 去官网下载安装包，支持 macOS、Linux、Windows： 
 https : //www.warp.dev/download 
 方式二：从源码构建 
 git clone https://github.com/warpdotdev/warp.git 
 cd warp ./script/bootstrap # 自动处理平台依赖 
 ./script/run # 编译并运行 
 bootstrap 脚本会自动处理 macOS、Linux、Windows 的平台差异。外部贡献者默认构建的是 warp-oss 开源社区版。 
 日常使用的话直接下载就够了。想参与贡献或者深度定制的，从源码构建会更灵活。 
 04 
 点击下方卡片，关注逛逛 GitHub 
 这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了： 
 跳转微信打开
```

---

## 10. 推荐 3 个 GitHub 画图 Skill，一句话生成流程图、架构图。

- 日期: 2026-04-30 12:51
- 链接: https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533360&idx=1&sn=1847cadb7dbb7224a9a692729b8db51e

```
原创 逛逛 2026-04-30 12:51 浙江 
 01 
 一句话画出能直接发布的技术图 
 最近在 GitHub 上翻到一个画图的 Skill，叫 fireworks-tech-graph，目前已经攒到了 3.6k Star。 
 这个项目干的事情说白了就是： 你用大白话描述一下想要的图，它帮你生成 SVG，再导出成高清 PNG，直接就能塞到博客或者 PPT 里。 
 我看了一下它的能力矩阵，还挺顶的。 
 一共支持 14 种图表类型，UML 全家桶都有，还专门做了 AI/Agent 方向的模板。 
 比如 RAG pipeline、多 Agent 协作流程这种，在国内写 AI 相关内容的场景特别实用。 
 视觉风格也有 7 种可选，暗黑终端风、科技线稿风、手绘风都能切。 
 同一张图换个风格再生成一次就行，不用自己动手改样式。 
 它是个 Claude Code 的 Skill，装起来一行命令: 
 npx skills add yizhiyanhua-ai/fireworks-tech-graph 
 Mac 上还要 brew install librsvg 装一下底层依赖，用来把 SVG 转成 PNG。 
 装完之后，直接跟 Claude 说给我画一张 RAG pipeline 的流程图，用暗黑终端风格，几秒钟就给你一张能直接用的图。 
 开源地址： https : //github.com/yizhiyanhua-ai/fireworks-tech-graph 
 02 
 Architecture Diagram Generator 
 画架构图还有一个很烦人的事，画完之后怎么发给别人看， 如果导出图片清晰度可能不够，发 draw.io 文件对方还得装工具。 
 Cocoon-AI 开源的 architecture-diagram-generator 专门解决这个，Star 也冲到了 3.6k 这个量级。 
 它的输出形态很有意思， 直接给你一个独立的 HTML 文件，里面嵌的是 SVG，双击就能在任何浏览器里打开看。 
 丢到微信、邮件都不会糊，分享起来相当无脑。 
 默认风格走的是深色主题，字体用的 JetBrains Mono，出来的图自带设计感，不用自己再去调配色。 
 这个 Skill 同时兼容 Claude.ai 和 Claude Code。 
 如果你在用 Claude.ai,直接去 Settings → Capabilities → Skills 把文件传上去就行。Claude Code 用户把文件扔到 ~/.claude/skills/ 下也能直接用。 
 挺适合那种要给老板或者客户做系统方案汇报的场景，出来的效果看着就挺专业。 
 开源地址： https://github.com/Cocoon-AI/architecture-diagram-generator 
 03 
 Excalidraw Diagram Generator 
 GitHub 官方出品，画完还能自己手动改 
 前面两个项目都是 AI 生成完就定稿了，想微调只能重新 prompt。 如果你追求生成之后还能手动改，这个更合适。 
 它是 GitHub 官方 awesome-copilot 仓库里收录的一个 Skill，放在 skills/excalidraw-diagram-generator 下面。 
 最大的爽点在输出格式，生成的是 .excalidraw JSON 文件。 
 把文件拖到 excalidraw.com 里就能打开， 然后所有元素都可以继续编辑。 
 excalidraw 就是那个 120K Star 的开源在线画板。 
 改颜色、挪位置、加箭头、删节点，全都没问题。 
 支持的图表种类也很全，我看了一下一共有 9 种： 流程图、关系图、思维导图、架构图、数据流图、泳道图、类图、时序图、ER 图，日常画图基本都覆盖了。 
 特别值得一提的是它对 UML 关系线做了细致区分，继承、实现、关联、依赖、聚合、组合这几种线型全都按规范来，画类图显得特别专业。 
 要画云架构还能调 AWS、GCP、Azure 的官方图标库,不用自己再去找素材图。 
 挺适合需要反复打磨的场景，或者跟同事协作编辑的时候用。 
 开源地址 : https://github .com/github/awesome-copilot/tree/main/skills/excalidraw-diagram-generator 
 04 
 点击下方卡片，关注逛逛 GitHub 
 这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了： 
 跳转微信打开
```

---
