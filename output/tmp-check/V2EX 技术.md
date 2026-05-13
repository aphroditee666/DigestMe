# V2EX 技术

> 分类: 技术社区
> URL: https://www.v2ex.com/feed/tab/tech.xml
> 抓取: 30 篇

---

## 1. 想折腾一个 AI 主机，请行家出手

- 日期: 2026-05-09 17:02
- 链接: https://www.v2ex.com/t/1211566#reply10

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
40.35
13.66
V2EX
›
Local LLM
想折腾一个 AI 主机，请行家出手
davidyin
·
1h 27m ago
via Android · 175 views
打算自组一 AI 主机，用于本地 llm 。 可用于 kiro IDE 的，gitlab duo 。
可行性有多大，能否代替订阅的那些 ai 服务？
配置有没有推荐的，各 AI 行家请出手相助。
AI
主机
本地
10 replies
•
2026-05-10 02:04:24 +08:00
1
qfdk
PRO
1h 21m ago via iPhone
看了明矾系列的 到现在没下手... 要不要等等 mac mini ？ 说不定有新科技？ 本来打算买 m4 ， 后来一拉配置，直接充 cc 了. 我 m1 跑 llm 吐字都不如我打的快... 也这里蹲一个吧
2
qfdk
PRO
1h 21m ago via iPhone
看了明矾系列的 到现在没下手... 要不要等等 mac mini ？ 说不定有新科技？ 本来打算买 m4 ， 后来一拉配置，直接充 cc 了. 我 m1 跑 llm 吐字都不如我打的快... 也这里蹲一个吧
3
yusf
1h 18m ago
老老实实买用 api 吧
4
davidyin
OP
1h 16m ago via Android
@
yusf
订阅很方便，只是有洁癖，不想自己的东西暴露到外面。
希望都在局域网内。
5
yusf
1h 11m ago
@
davidyin
https://www.bilibili.com/video/BV1zmSoBnEYM
看下这个 up 的本地部署体验
6
davidyin
OP
1h 7m ago via Android
@
yusf
Mac 不考虑。基本没有用苹果的产品。
对于性价比敏感。
7
davidyin
OP
55 mins ago via Android
现在有个初步的配置清单：
RTX 4070 SUPER 12GB
Intel i5 14600K
Asus TUF B760
DDR5 32GB(2*16gb)
SSD 1TBx2
看看合适吗？
8
AastroLula
40 mins ago
还是考虑买 api 吧,当然实在有钱可以折腾玩玩,如果 op 是需要正式干活可能 anthropic 博客里提的用聪明的大模型指导小模型是个算是能用的方案,但是这块一来需要折腾很久,二来还是得买外面的 api. 我之前也是想搞本地大模型折腾玩玩,后来发现纯粹是垃圾佬的馋瘾上来了,再说现在啥都涨价的买了也是大冤种,如果 op 想买 aimax 395 算是个选择吧,当然有特殊需求部署几 b 模型能用上也是好事,12g 显存骗骗哥们还行,别把自己骗了,以上是我的一点想法
9
devzhangyu
34 mins ago
可以看看这个项目
https://github.com/AlexsJones/llmfit
1. 找出你的硬件能运行哪些模型
2. 估算某个模型配置需要什么硬件
3. 硬件模拟，可查看哪些模型适合目标硬件
10
ntedshen
27 mins ago
降价期间屯硬件，那 bro 你很勇哦（
4070s 有没有 4060ti 好使我不知道。。。
但是 14600k 和 d5 的意义在哪？
11
Livid
MOD
PRO
26 mins ago
@
davidyin
瓶颈是显存。
可以看一下 DGX Spark 系列的产品。
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1073 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 39ms ·
UTC 18:30
·
PVG 02:30
·
LAX 11:30
·
JFK 14:30
♥ Do have faith in what you're doing.
❯
```

---

## 2. 什么都没干， codex 剩余额度还在往下掉

- 日期: 2026-05-09 15:15
- 链接: https://www.v2ex.com/t/1211560#reply2

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
V2EX
›
OpenAI
什么都没干， codex 剩余额度还在往下掉
jerrylau5
·
3h 12m ago
· 368 views
下午过了五小时打开 codex ，5 小时额度直接到 98%了，懵逼
啥都没干，一小时之后重新打开，给干到 95%，周额度也掉了一两个点，更懵逼了，
这额度怎么还漏水偷电啊
额度
消耗
漏水
2 replies
•
2026-05-10 01:45:39 +08:00
1
kakarotto726
1h 8m ago
今天发现，网页版 gpt 的使用，也会消耗 codex 的额度。
2
hsir
42 mins ago
何止这样，现在如果你使用 API ，还会遇到 Cache hit 始终 0% 的问题，钱流失就像流水一样，严重怀疑 OpenAI 故意的：
https://github.com/openai/codex/issues/20301
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1065 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 27ms ·
UTC 18:28
·
PVG 02:28
·
LAX 11:28
·
JFK 14:28
♥ Do have faith in what you're doing.
❯
```

---

## 3. vibe coding 在崩溃的边沿疯狂摩擦

- 日期: 2026-05-09 17:15
- 链接: https://www.v2ex.com/t/1211567#reply9

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
• 请不要在回答技术问题时复制粘贴 AI 生成的内容
111.78
V2EX
›
程序员
vibe coding 在崩溃的边沿疯狂摩擦
crocoBaby
·
1h 14m ago
· 188 views
近一个月开始已经完全放弃手写代码了，全程使用 vibe coding ，随着使用屎山开始压不住，然后强逼自己按模块拆服务，勉强能保持维护的程度，这完全是架构师的时代，普通程序员有点 hold 不住，ai 越写越飘，有种把控不住自己项目的感觉了
vibe
代码
架构
9 replies
•
2026-05-10 01:41:13 +08:00
1
qfdk
PRO
1h 8m ago via iPhone
我之前写项目 都是 nodejs 然后项目都是一个风格. 基本的 contoller utils middleware 啥的 都已经抽成公共了. 业务逻辑 自己写，剩下前端适配交给 vibe 毕竟 后端不敢给他放飞自我. 否则会补丁叠补丁... 相当于你送给猴子🐒了一把 ak47...
2
383394544
1h 5m ago
不写 plan 和 spec 吗 不用 git 保存代码上下文吗 不建本地文档库吗
3
jko123
1h 3m ago
ai 帮我写的授权流程已经完全超出我的能力范围了，这种情况下，我自己都不懂，ai 就越写越乱，最后还是还原回来较简单的版本
4
383394544
1h 2m ago
传统的 确认需求 → 约定 schema → 约定 api 接口 → 实现后端 → 写文档 → 实现前端 → 迭代 流程在 agentic enginnering 时代只会更重要，别说得好像以前就不是架构师的时代一样 ── AI 会放大个人的能力，同时也会放大个人的短板。你以前的技术债才是现在压垮你的东西，vibe coding 只是加速。
5
crocoBaby
OP
59 mins ago via iPhone
@
qfdk
前端也一样不行，已经开始放飞自我了，明明很简单的一个实现，非要绕几圈堆屎山，但确实能跑
6
crocoBaby
OP
56 mins ago via iPhone
@
383394544
确实是规划这一块能力缺失了，plan 的前提就是架构师那样完全规划好了，我这种属于是打补丁了
7
crocoBaby
OP
56 mins ago via iPhone
@
jko123
就是这个 feel ，超出了能力范围，已经把控不住项目了，出了 bug 都很难定位
8
qfdk
PRO
51 mins ago via iPhone
@
crocoBaby
前端我给他限制死了组合. 比如用 xx 组件 前提是得有. 反正 nodejs 配合 ejs 这样的已经跑熟悉了. 撸一个后台分分钟. 不过我不会让他写我看不懂的代码...
然后定期你要让他检查下能拆就拆
9
qfdk
PRO
48 mins ago via iPhone
顺便讲一下 我一开始 vibe 了个爆仓机器人.... 有了血的教训.... 跟数字有关的还是要多多调教
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1072 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 354ms ·
UTC 18:29
·
PVG 02:29
·
LAX 11:29
·
JFK 14:29
♥ Do have faith in what you're doing.
❯
```

---

## 4. 爪云平替? RESVRL 容器托管重磅上线！支持 ClawCloud 一键迁移！

- 日期: 2026-05-09 15:47
- 链接: https://www.v2ex.com/t/1211564#reply6

```
各位 V2EX 论坛 云服务爱好者、开发者、运维小伙伴们，大家好！ 
 随着爪云容器托管正式停运，不少朋友陷入两难：精心部署的应用无处安置、原有免费福利戛然而止、手动迁移配置繁琐还容易丢数据、想找靠谱平替又怕不稳定、性价比不达预期。 
 深知大家迁移刚需与运维痛点，RESVRL 容器托管专属服务正式全面开业上线！前身为 KarenCloud 多年技术沉淀升级，专为爪云停运用户量身打造，不只是简单平替，更是更稳定、更易用、更安全、更低门槛的全面升级版，主打爪云应用一键迁移、零门槛容器托管、全场景稳定运行，完美帮你解决业务接续、迁移繁琐、运维操心等所有难题！ 
 ## 核心优势直击痛点，专注容器托管更专业 
 无多余噱头，所有功能围绕容器托管刚需打造，适配个人开发者、小型团队、日常测试、轻量业务部署全场景，好用省心、低成本易上手： 
 ### 爪云专属一键迁移，业务无缝不中断 
 平台原生支持从 ClawCLoud 一键迁移，自研专属迁移适配能力，无需手动导出镜像、重新配置环境、调试端口与数据，简单授权即可自动同步全部应用配置、镜像文件、运行参数。全程可视化操作，小白也能独立完成，快速完成全量迁移，业务近乎零中断，彻底告别手动迁移的繁琐与出错风险。 
 ### 极简可视化操控，小白零基础免运维 
 摒弃复杂命令行与晦涩底层配置，搭载统一可视化控制台，容器创建、镜像管理、资源监控、网络配置、应用生命周期管理全部一键搞定。不用专业运维基础，注册即可上手，把精力专注放在业务开发上，底层运维全权交给平台。 
 ### 全系 RAID1 磁盘冗余，筑牢数据安全底线 
 全系标配全程 RAID1 磁盘阵列架构，实时双盘冗余备份，从硬件底层杜绝单点数据丢失风险。搭配免费自动数据备份、专业 DDoS 防护，平台所有操作全程留痕可查，全方位守护容器业务与数据安全。 
 ### 灵活组网 + 平滑扩容，适配全阶段需求 
 拥有超强灵活网络组网能力，支持自定义网段、内网互通、跨机组网、弹性子网划分。支持单机轻量化起步，后续业务升级、节点扩容可平滑横向拓展，无需更换平台、无需重新部署，从个人测试到项目生产、小型集群部署都能完美适配。 
 ### 原生 K8s 集群 + 自研可视化面板 
 原生支持 Kubernetes 集群部署，搭配纯自研 K8s 可视化管理面板，不用复杂命令行，集群创建、节点管理、应用编排、资源调度一站式可视化操作，新手也能轻松玩转容器集群运维。 
 ### 安全态势全方位防护，智能拦截网络风险 
 平台搭载重磅安全态势防护功能，实时可视化监控容器与虚拟机恶意攻击行为；内置智能 AI 流量分析引擎，自动识别异常访问、恶意爬虫及攻击流量，自动拦截封禁，从源头规避网络风险，全天候守护容器业务安全。 
 ### 自研 AI 助手 + 7×24 小时售后全程兜底 
 内置 RESVRL 自研 AI 智能助手，深度融入容器托管全流程：提供全流程操作指引、快速排查容器故障、解决网络组网冲突、智能分析账单优化资源开支。同时配备专业售后团队 7×24 小时在线值守，90% 工单极速响应，迁移咨询、容器运维、集群搭建各类问题都能第一时间高效解决。 
 ### 无套路售后承诺，使用更安心 
 郑重保障：所有产品 24 小时内无违规使用，均可申请全额原路退款，无隐藏条款、无套路捆绑；全系标配免费数据备份与专业 DDoS 防护，双重守护容器业务稳定运行。 
 ## 开业盛典多重福利，致谢所有用户厚爱 
 沿用 RESVRL 开业专属福利，限时开启、诚意拉满，爪云迁移新老用户均可参与，福利不套路、可直接抵扣消费！ 
 ### [福利一：全场通用优惠券 限时申领] 
 年付专属 8 折循环优惠券，优惠码：`HELLO_RESVRL_CUSTOM`、`HELLO_RESVRL_PLAN`，即日起至 10 月 1 日有效，虚拟机、容器托管续费同享优惠； 
 进官方交流群联系管理员，可免费领取账户专属赠金，直接充值余额，无套路可全额抵扣容器托管、云主机所有消费。 
 ### [福利二：幸运抽奖 超值云资源免费送] 
 参与规则：在本帖回复 「 RESVRL 开业大吉，运维省心安全护航」，截图后进群私聊管理员即可参与抽奖，重复回复无效，每人仅限一次中奖资格； 
 开奖时间：2026 年 5 月 15 日 21:00 准时开奖 
 奖品明细 
 一等奖（ 3 名）：2 核 4G 50G 配置虚拟机全年免费使用权，也可任选兑换 500 元账户余额 
 二等奖（ 5 名）：同配置虚拟机 3 个月免费使用权，也可任选兑换 200 元账户余额 
 三等奖（ 20 名）：容器托管服务 1 个月免费使用权，也可任选兑换 50 元账户余额 
 参与奖（不限量）：所有回帖参与并完成新用户注册的伙伴，均可免费领取容器托管 20 元代金券，无门槛直接使用 
 ### [福利三：邀请有礼 双向共赢 多邀多返] 
 成功邀请 1 位好友注册并下单购买虚拟机 / 容器托管套餐，邀请方与被邀请方均可领取全套餐通用 7 折优惠券； 
 同时邀请方额外享受被邀请方订单 20% 现金返利，多邀多返、上不封顶！ 
 ## 关于我们｜ RESVRL 团队 专注做好容器与云服务 
 我们是 RESVRL 团队，由原 KarenCloud 团队全新升级打造，深耕虚拟机、容器托管、K8s 集群虚拟化领域多年，历经近一年封闭内测迭代。始终秉持稳定、便捷、高性价比的核心理念，此次重点打磨容器托管服务，就是为了给爪云迁移用户、广大开发者提供一个长期靠谱、省心稳定的优质选择。 
 我们依托 Rust 与 Libvirt 纯自研虚拟化底层，不止做基础容器托管，更可提供企业定制化私有云、专属容器集群、K8s 私有化搭建、安全态势私有化部署等一对一服务，适配个人运维、项目部署、企业办公多元场景。 
 坚持不做短期割韭菜服务，以极致稳定的线路、底层硬件安全架构、可视化简易操作、AI 智能排障、极速售后响应，做大家云上托管路上值得信赖的坚实伙伴。 
 ## 联系我们 即刻开启爪云无缝迁移 
 官方官网： https://resvrl.com 
 业务咨询 / 技术反馈： contact@shimmersoft.com 
 商业合作：可洽谈企业私有云、容器集群、K8s 私有化定制部署等业务 
 官方交流群：1078817626 
 初心不改，步履不停。RESVRL 将以专业的容器托管服务、一键迁移能力、安全稳定的底层架构、完善的售后与 AI 运维加持，陪每一位用户安心托管应用、轻松搞定云上运维。 
 再次感谢大家的信任与支持，祝各位使用顺畅、万事顺意！ 
 —— RESVRL 团队 敬上
```

---

## 5. 最近发现有大量的海外机房 ip 在爆破，遂把自己的所有海外服务器都配置了 GEOIP 白名单

- 日期: 2026-05-09 05:46
- 链接: https://www.v2ex.com/t/1211442#reply18

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
Recommended Services
›
Amazon Web Services
›
LeanCloud
›
New Relic
›
ClearDB
1
V2EX
›
云计算
最近发现有大量的海外机房 ip 在爆破，遂把自己的所有海外服务器都配置了 GEOIP 白名单
Magnetic
·
12h 43m ago
· 1916 views
限制只能使用中国 ip 才能访问，这样会减少被暴力攻击的频率吗
geoip
白名单
攻击
18 replies
•
2026-05-10 01:31:13 +08:00
1
x86
12h 29m ago
禁 ping ，改默认端口，禁密码登入
2
realpg
PRO
10h 44m ago
2
从 2005 年起，我管理的服务器 ssh 都已经限制死了不只是中国，而是本省运营商的宽带和专线 IP 池。
基本没有扫描现象
特殊情况外出，用 port trigger 触发自动临时开门，telnet 顺序触发两个 TCP 端口后，本 IP 加入临时白名单
3
zCoCo
10h 19m ago
限制国内可以减少一部分 我跟 2 楼思路差不多，从 GeoLite 获取所在省份的地址段，用 iptables 或者 nftable 搭配 ipset 配置端口策略，ssh 爆破再没遇到过
4
bigtwo
10h 14m ago
同 2 楼，之前用 fwknop2 敲击开门，但感觉不好用，去年底用 ai 自己写了个三方敲击开门，平常关闭非必要端口，要用的时候全自动敲击再重连
5
haukuen
10h 13m ago
我是禁 ping 且三次登录失败永封 ip,其实禁 ping 就基本遇不到爆破了，以前没禁的时候每天都会多不少被 ban 掉的 ip
6
SpiritLingPub
10h 11m ago
禁 ping ，改默认 SSH 端口，不使用 SSH 时直接使用云服务器防火墙禁掉 SSH 登录，物理断开
7
cocalrush
8h 31m ago
怎么发现被爆破呢
8
SoulFlame
8h 26m ago
@
cocalrush
#7 日志
9
crocoii
6h 49m ago via Android
改端口，能破 99.9999 的攻击。
10
cocalrush
6h 28m ago
@
SoulFlame
嗯看到了，之前把所有改成密钥登录了，爆破理论上无效
11
94nb
5h 42m ago
我是禁海外 ip ，ssh 只允许私钥登录，流量达到 xxx 关机
12
herozzm
4h 57m ago
如何禁海外登录，还维护一份海内外的 ip 库？
13
pxw2002
4h 11m ago
linux 改成 3389 端口
14
Magnetic
OP
3h 51m ago via iPhone
@
herozzm
直接让 ai 帮你搞，用 nftables 然后前置 geoip 白名单做入站，出站不限制，ssh 端口要留意，别把自己锁外边了
15
Magnetic
OP
3h 43m ago via iPhone
@
pxw2002
改端口是必须的，但是会有脚本扫，如果装了 fail2ban ，脚本扫到会瞬间拉满 f2b ，然后把 cpu 撑爆，这是最恶心的
16
xqzr
1h 31m ago
管理端口（如 SSH ）关闭 IPv4 侦听，减少 99% 扫描
17
RW5kZXJBdmFyaXRp
1h 6m ago
@
Magnetic
把 icmp 包的处理方式改成 drop 呢？ ssh 配置端口敲门，成功之前全部 drop
18
383394544
59 mins ago
ssh 端口限 ipv6 访问 + 套一層 cloudflare tunnel + 限 cf ip 访问源站能減少很多问题。本地 v4 或 v6 到 cloudflare 的 edge ，然后 tunnel ipv6 回源到你的源站。
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1073 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 56ms ·
UTC 18:30
·
PVG 02:30
·
LAX 11:30
·
JFK 14:30
♥ Do have faith in what you're doing.
❯
```

---

## 6. 千问推出了 PC 语音输入，功能和 typeless 差不多

- 日期: 2026-05-08 23:51
- 链接: https://www.v2ex.com/t/1211319#reply36

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
• 请不要在回答技术问题时复制粘贴 AI 生成的内容
V2EX
›
程序员
千问推出了 PC 语音输入，功能和 typeless 差不多
MuyuQ
·
18h 39m ago
· 2309 views
巨头随手做的东西，就把一个创新赛道里的参赛者挤死大半。
比功能，巨头随便投入点人力就能碾压。
比营销，根本不是一个量级。
比财力，比模型，这都没法比啊。。
说的就是上半年国内蛮火的闪电说。
更何况后面还有豆包的语音输入法蓄势待发。
语音
巨头
竞争
36 replies
•
2026-05-09 23:53:05 +08:00
1
MuyuQ
OP
18h 35m ago
有一篇爱范儿的广告可以大概了解下。
https://www.ifanr.com/1664830
2
Moonkin
17h 49m ago via Android
这是啥新鲜玩意吗？把人说的话 stt ，文本送个本地小模型润色，不就行了。。。我有什么漏了的地方吗？
3
ktyang
17h 22m ago
也不搞个 linux 的
4
ChrisV5
17h 18m ago
有的，core 没啥技术含量，各家都有 tts 和 llm 。但是输入法的集成开发有很多很多细节。虽然 vibe coding 很快，但是都架不住生产级别的 bug 。有一定的工程量。
5
hxzhouh1
17h 12m ago
闪电说挺好用的，支持本地模型，自定义 api ，简单、纯粹。
6
ko20
16h 58m ago
诶，就没有哪家做一个 linux 这方面好用的客户端吗？目前 debian13+gnome48 用下来没一个满意的
7
capric
16h 48m ago
原理是 asr(语音识别)，llm 语义重组排版等
有意思的是前向修正，比如你说“不对，不对”，它要理解你是否定前面说的
另外评价标准也很意思，不是错字率而是意图达成率(是否需要手动编辑)
typeless 开源替代
https://github.com/cjpais/handy
https://github.com/sypsyp97/light-whisper
https://github.com/tover0314-w/opentypeless
8
MuyuQ
OP
16h 35m ago
@
ChrisV5
是的。但开源的几个项目用起来都各有各的难受。目前最强还是 type less ，但是那玩意儿付费太贵了点。
@
capric
几个开源项目我也看过，维护是个问题，修 bug 不积极。而且差距还是挺明显的。
@
hxzhouh1
闪电说模型肯定没法和大厂比，自定义功能还是挺好用的。闪电说的优势是搭配豆包流式语音识别，但是等豆包也推出语音输入法的时候闪电说就没什么优势了。 闪电说的付费是 AI 助手，但这个方向肯定打不过千问和豆包。
9
ChrisV5
16h 1m ago
@
MuyuQ
#8 因为我自己也手搓了一个，拿 rime + 豆包 asr + deepseek llm 。
有些小问题，我自己能忍。但是发出去的话，bug 一堆。
10
cutecore
15h 41m ago
豆包语音输入法发布都快半年了，官网 PC 版本还是敬请期待呢
哪个输入法先出 linux 版本，我就支持哪一个
11
hxzhouh1
15h 19m ago
@
ChrisV5
#9 您好，请问一下 rime 如何接入 豆包 asr 呢？
12
ChrisV5
15h 17m ago
@
hxzhouh1
#11 rime 的核心是开源的啊。拿 vibe coding 怼就行。大概跑一个 40 分钟的任务，就能跑起来吧。。
13
ganbuliao
15h 16m ago
豆包的语音输入法 pc 有内测版本 我已经用一个月了
很爽 就等豆包正式发布了
14
winnerczwx
15h 15m ago
1
@
Moonkin
想法和产品还是有差距的
15
iorilu
12h 53m ago
这个就等巨头产品了
除非是必须走本地
16
auhah
12h 44m ago
@
ChrisV5
闪电说/typeless 都没走输入法路子，输入法相关的坑也不用踩啊。。。看上去主要功能就一条线，触发录音，丢给模型，回填内容
17
ChrisV5
12h 35m ago
@
auhah
回填内容没你想的这么简单，输入框的状态是非常不稳定的，他们走剪贴板，现在是个应用都读写改剪贴板。
18
emberzhang
12h 27m ago
豆包输入法 macOS 测试版我也试了下，问题在于它真是安装为一个输入法了，要把输入法切换到它的时候才能输入，如果状态栏的输入法切换到系统自带，就无法激活豆包的语音输入
闪电说，lazytyper 这些压根就没按输入法安装，也就不用管系统限制
19
lel020
12h 20m ago
我希望语音输入归语音输入，输入法归输入法，语音输入法就很坑爹，挤占了输入法的位置，但作为输入法又垃圾的不行，
20
AIXAPI
12h 16m ago
感觉这类产品的技术栈（ ASR+LLM 润色）门槛不高，但工程细节拉满，比如实时流处理、语义纠错、输入法集成，大厂砸资源做出来的体验确实是个人项目比不了的。期待后面豆包的版本，也看看开源社区能不能跟上。
21
madowenzy
12h 12m ago
@
ganbuliao
Mac 端吧，Win 应该还没有
22
HeyWeGo
12h 5m ago
豆包的语音在 win 上的有办法用，v2 的人才提供的方法
23
iorilu
11h 59m ago
@
HeyWeGo
怎么用呢, 有链接吗
24
yeh
11h 35m ago
我和
https://v2ex.com/t/1202162
这位老哥一样，参考
https://github.com/yetone/voice-input-src
，codex 生成了一个 macos 下的来 vibe coding ，之后自己用的过程中发现了几个边界问题，补全了下边界，现在还挺稳的。
输入端是 dji mic mini
25
vvv222eeexxx
11h 29m ago
@
ganbuliao
可否共享一下，让大家先睹为快？
26
Oo0
10h 53m ago
我也等个 Linu 版
27
ebushicao
10h 39m ago
智谱也有这个输入法，但本质就是语音转文字再用模型处理一下，我直接文字表达然后让模型处理一下效果应该会更好，毕竟文字输入还能检查一下，语音输入但凡讲多点就容易出错，而且涉及到一些专有名词的时候很容易错误，即便这种输入法都支持添加名词。
28
raycool
8h 49m ago
豆包输入法怎么还不发布 mac 端的
29
XTTX
8h 41m ago
@
ganbuliao
平时用来替代 cli 打字好用么？
30
ganbuliao
7h 3m ago
豆包的有需要可以试试
6ZO+5o6lOiBodHRwczovL3Bhbi5iYWlkdS5jb20vcy8xN25DYUU2cTlHMjllaERSMlF6MTEydz9wd2Q9MVljNwrmj5Dlj5bnoIE6IDFZYzc=
31
ganbuliao
7h 0m ago
5oiR55So5aS45YWL572R55uY5YiG5Lqr5LqG44CMRG91YmFvSW1lSW5zdGFsbGVyX3YwLjUuNy56aXDjgI3vvIzngrnlh7vpk77mjqXljbPlj6/kv53lrZjjgILmiZPlvIDjgIzlpLjlhYtBUFDjgI3vvIzml6DpnIDkuIvovb3lnKjnur/mkq3mlL7op4bpopHvvIznlYXkuqvljp/nlLs15YCN6YCf77yM5pSv5oyB55S16KeG5oqV5bGP44CCCumTvuaOpe+8mmh0dHBzOi8vcGFuLnF1YXJrLmNuL3MvYjRmODkzZGQ0MDljCuaPkOWPluegge+8mnBGZjM=
32
qW7bo2FbzbC0
6h 54m ago
@
ganbuliao
#31 这个怎么用，官网没法下载 pc 版的
33
MuyuQ
OP
6h 13m ago
@
qW7bo2FbzbC0
https://base64.us/
用这个转一下
34
MuyuQ
OP
5h 47m ago
@
ganbuliao
有 PC 版吗？ 第二个链接失效了。第一个是 mac 版。感谢
35
JackalZhao
2h 55m ago
@
MuyuQ
实际用了下，2s 以上的转录延迟，根本无法接受。Typeless 也用了，延迟也是一言难尽。
你要是体验一下最新的 CapsWriter-Offline ，就能体会到真正的得心应手了，我就是作者，在 Windows 上的语音输入体验是无敌的程度。
@
AIXAPI
正符合你所说的工程细节拉满。启用 LLM 润色功能后，延迟也比 Typeless 更低。
36
rizon
2h 37m ago via Android
目前还没遇到比 typeless 更好用的，如果有人用过千问这个可以说下对比 typeless 是否更好。
现在我用 typeless 的一个问题是以前可以直连，后来直连经常连不上，只能走 vpn 了，虽然也不是什么大问题吧
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1072 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 83ms ·
UTC 18:30
·
PVG 02:30
·
LAX 11:30
·
JFK 14:30
♥ Do have faith in what you're doing.
❯
```

---

## 7. 现在 giffgaff 应对 codex 登录时要求验证手机号的问题是否可行

- 日期: 2026-05-09 06:34
- 链接: https://www.v2ex.com/t/1211463#reply34

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
V2EX
›
OpenAI
现在 giffgaff 应对 codex 登录时要求验证手机号的问题是否可行
willxiang
·
11h 51m ago
· 1959 views
此前没有 gg 卡，五一节后 codex 端登录账号（多个账号中的其中一个，bug 价充的一个月 plus ）发现弹手机号验证了。
现在买一张 gg 卡激活后用来接码是否有必要
giffgaff
Codex
验证
34 replies
•
2026-05-09 23:19:32 +08:00
1
justtokankan
11h 24m ago
蹲个体验啊，因为我也想买一个想，不知道成本和体验咋样
2
ksgt00857913
11h 11m ago
接码平台接一个不香吗
3
willxiang
OP
11h 5m ago
@
justtokankan
买了一个，还没到货，主要担心激活问题以及后续保号问题，怕被封
4
willxiang
OP
11h 4m ago
@
ksgt00857913
接码频率可能不止一次，下一次是否还能拿同一个号码接，这个无法保证啊。
5
justtokankan
10h 59m ago
@
willxiang
哪里买的啊？ 到货后记得分享一下使用啊，同需
6
willxiang
OP
10h 49m ago
@
justtokankan
#5 东哥那买的，等我到货了试一下，没问题了再更新情况
7
zhouu
10h 48m ago
可行啊，我 gg 还注册了 claude 用的挺稳
8
willxiang
OP
10h 42m ago
@
zhouu
好的感谢，请问你的 gg 卡使用多久了
9
TtNnTt
10h 40m ago
接码平台的话，下次验证还需要相同的手机号码怎么办？
10
ychbest
10h 12m ago
过了，就是 gg 卡激活等了挺久的，注册 what's app 就能接码了，挺丝滑
11
coolsun19
10h 7m ago
打车问下 gg 卡哪里渠道有卖啊？
12
laov2
10h 4m ago
gg 卡目前没事，就怕后面会不会不支持了，因为 gg 卡属于虚拟运营商。
13
zan0723
9h 56m ago
@
TtNnTt
只能继续找之前的接码平台啊~所以其实更建议用长期稳定的号码来接码，临时号码不够稳定~
14
CNN
9h 54m ago
1
@
coolsun19
https://github.com/ssnhd/sim
15
refear99
9h 45m ago
先检查自己梯问题，我注册都不要手机号
机场的 ip 比较脏，就会触发手机号验证
16
MuSeCanYang
9h 37m ago
@
refear99
你用的哪家的机啊
17
willxiang
OP
9h 30m ago via Android
@
refear99
账号已经风控了，找了干净的节点测试了，还是要验证码
18
AK2022
9h 14m ago
GG 卡已经用了 4 年了，codex 可用。保号的话记得半年以内发一次短信或者保证有话费变动就行。注册 whatsapp 会概率封号，这个无法避免。
19
debuggeeker
9h 13m ago
我也有这个想法，等楼主测试一波，然后反馈。主要是打算长期用 GPT ，我目前账号已经使用 8 个月了，中间使用了 team 几个月，有 3 个月官方的订阅，目前还没弹验证码
20
lujiaosama
9h 9m ago
@
AK2022
封号是指 WHATSAPP 封号还是注册第三方应用比如 GPT 这种封号？
21
refear99
7h 59m ago
@
willxiang
公用的就没有干净的，自建精品线路才是最稳妥的
22
v00O
7h 53m ago
下午试了一下，+44 的 giffgaff ，验证码是对的，验证不通过
23
Kizishao
7h 51m ago via iPhone
@
zhouu
登录用的那的 IP ？美/英？
24
willxiang
OP
7h 17m ago
@
refear99
#21 是自建的，一两个人用的那种
25
ftfunjth
6h 53m ago
@
v00O
是不是机场太脏了，所以没跳 whatapps 。我自己用 giffgaff 跳 whatsapp 验证通过了
26
MuyuQ
6h 3m ago
你们如果有外版 esim 的话，就不用去买实体卡了。直接在线网申就行。
27
zhouu
5h 52m ago
@
Kizishao
日本
28
zhouu
5h 52m ago
@
willxiang
#8 4 个月了吧
29
ivae
5h 22m ago via iPhone
亲测可以，正好我的 giffgaff 今天刚收到激活的，注册了 whatsapp 和 codex 验证都没问题
30
ivae
5h 19m ago via iPhone
成本的话，卡 45 ，充值 10 英镑激活，使用的是招商双币信用卡
31
willxiang
OP
4h 12m ago
@
ivae
#30 请问参考的哪个教程步骤，我等卡到了也试试
32
ivae
3h 46m ago via iPhone
@
willxiang
https://jcn11fio79id.feishu.cn/wiki/Q61XwF2tBiN3xwkJXuDc1XNTnYf
可以参考这个，写的非常详细
33
ivae
3h 44m ago via iPhone
1
@
ivae
卡不是这家买的，这家偏贵，只是教程比较详细
34
AK2022
3h 6m ago
@
lujiaosama
WHATSAPP ，其他账号注册还没发现问题，可能我用的场景少。
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1062 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 63ms ·
UTC 18:26
·
PVG 02:26
·
LAX 11:26
·
JFK 14:26
♥ Do have faith in what you're doing.
❯
```

---

## 8. 发现这两天 chatgpt plus 用 codex 的 GPT5.5 现在上下文只有 258K 了吗？

- 日期: 2026-05-09 14:40
- 链接: https://www.v2ex.com/t/1211554#reply4

```
上个月 claude 降智后，换成 chatgpt plus ，GPT5.5 用起来很爽，而且有 fast 模式，和 ops 一样爽。最近两天感觉也降智了，普通模式慢了很多，经常卡住，上下文也从 1M 跳到了 258K 。
```

---

## 9. 写了个 Docker 容器无痛迁移工具

- 日期: 2026-05-09 09:05
- 链接: https://www.v2ex.com/t/1211508#reply11

```
支持增量迁移，自动识别 Compose depends_on 按依赖顺序恢复，以及 volume 和挂载卷。 
 背景是最近要把我的 Lightsail 和腾讯云，阿里云服务都迁移到 Hetzner 。 
 三家零零散散跑了十几个容器，有些是 Docker compose 启动，有些配置了 network ，手动迁移太痛苦了。 
 使用方式很简单： 
 mico pack # 打包所有运行中的容器（以及镜像/配置/卷/网络配置）为一个 .zst 压缩包 
mico unpack mico.zstd # 在目标服务器一键恢复，按依赖顺序自动重建 有需要的可以试试。 
 https://github.com/Ray-D-Song/mico
```

---

## 10. 最便宜的云服务器方案是什么？

- 日期: 2026-05-08 02:49
- 链接: https://www.v2ex.com/t/1211093#reply81

```
如果我理解正确的话，你对外暴露的基本就是查，写操作都在你管理员这边。
那似乎可以只部署在本地，只有查询走 VPS ，你本地每几分钟同步数据到 VPS ，VPS 只是静态站。。。甚至可以 GitHub ，不过客户应该打不开
GitHub.io 。
（纯本地也可以 ddns ，不过只能 ipv6 ）
如果可以的话，也可以考虑做个安卓 app ，webview ，这样基本不用改。本地页面有了，只差一点数据。可以通过 p2p 找到你，同步 JSON 就行。所以你需要的是个 tracker 。。。有没有搞头？
```

---

## 11. 自己搭建的中转站

- 日期: 2026-05-09 10:37
- 链接: https://www.v2ex.com/t/1211527#reply1

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
• 请不要在回答技术问题时复制粘贴 AI 生成的内容
0.01
V2EX
›
程序员
自己搭建的中转站
maky
·
7h 50m ago
· 567 views
有喜欢的老铁可以注册使用哦～
https://passionevery.art/
中转站
注册
使用
1 replies
•
2026-05-09 22:42:07 +08:00
1
needpp
3h 46m ago
你这个价格没有优势啊； 另外一般都是赠送$50 ?
user: hello886
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1067 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 29ms ·
UTC 18:28
·
PVG 02:28
·
LAX 11:28
·
JFK 14:28
♥ Do have faith in what you're doing.
❯
```

---

## 12. 吕布骑狗新招

- 日期: 2026-05-09 08:39
- 链接: https://www.v2ex.com/t/1211498#reply7

```
安装过 Claude 后，可以再安装一个 aivo 
 装好之后执行 
 echo "alias a1m='aivo claude -k aivo -m aivo/starter --1m'" >> ~/.profile && source ~/.profile 这样就是一个吕布骑狗的新招了 
 a1m 我用它日常开发，觉得完全够了，分享给大家
```

---

## 13. Claude 也开始做这种通用的 office agent 了。。这不是抄的 Kimi?

- 日期: 2026-05-09 10:34
- 链接: https://www.v2ex.com/t/1211526#reply0

```
今天刷推的时候，发现 Claude 也开始做这种通用的 office agent 了。这个跟 Kimi 的 office agent 好像，也不知道谁抄谁的。 
 https://imgur.com/a/uL1EoPs 
 但是有一说一，我之前尝试过 Kimi 的，感觉成本太高了，49 块用不了几次，而且效果也没那么好，可能用的还是传统的 RAG ，在实际的解析中很容易丢失信息、张冠李戴。 
 因为当时读博对这方面有很频繁的需求，要是真用他们的估计得破产，（你们知道土博有多穷吧，真的是用到破产都毕不了业）所以自己手搓了一个 AI 填表工具，用起来挺智能的，即使到今天我也能拍胸脯说，解析效果比 Kimi 和 Claude 要好，而且成本只有 Claude 的 1/10 ，还不用翻墙去看 Anthropic 的脸色。 
 链接我先放这了，有需要的老哥自取：
SnapFill： https://www.gosnapfill.cn/landing?utm_source=v2ex 
 简单说一下它的功能啊： 
 首先，它能识别包括 PDF 、Word 、Excel 、PPT 在内的多种格式，让 AI 真正读懂文档，并分清哪个空格对应哪个字段。 
 其次，自研的表格算法能切实解决空间定位，让数据实现高精度的物理填入。 
 最后，自带的文档解析引擎还能提供可靠的长效记忆，让你生成自己的知识库，保存好资料，下次类似的表格还能用它填，免得重新录入。 
 至于为什么能做到这么便宜填表质量还更好呢，是因为我们当时在开发一个 AI 原生的解析引擎，它跟传统的 RAG 不同，不是简单的按字数暴力切片而是自带逻辑树去对齐文档，就像知识图谱一样完整地保留了文档的层级结构，所以解析出来的结果更完整。这个我后面会开源出来，大家可以关注一下。 
 总之，开发成功了之后，我就把它放到了 SnapFill 的底层，这样的解析路线出来的结果，自然更靠谱，用来填表也更准确了。 
 有了 SnapFill ，填表的时间从半个小时以上瞬间降至 5 分钟，而且数据 100%可溯源，大大减少了 AI 的幻觉问题，提高了填表的精确度。这样做起科研来也更省心了，不用再花大量的时间在那些枯燥的表格上，只需要专注做正事就好，其他的交给 AI 。 
 如果你也有这样降本增效的需求，不如试试看吧，尤其是填表量越大，效果越明显，信我：SnapFill： https://www.gosnapfill.cn/landing?utm_source=v2ex
```

---

## 14. Codex 推出迁移工具，协助从其他 Agent 一键迁移到 Codex

- 日期: 2026-05-09 01:06
- 链接: https://www.v2ex.com/t/1211328#reply23

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
• 请不要在回答技术问题时复制粘贴 AI 生成的内容
V2EX
›
程序员
Codex 推出迁移工具，协助从其他 Agent 一键迁移到 Codex
1
shineonme
·
17h 25m ago
· 3473 views
网址：
https://chatgpt.com/codex/switch-to-codex/
工作原理：
Codex 应用会自动检测来自其他代理的现有配置
显示全局和项目级别的配置、技能、插件以及其他可复制的设置。
Codex 启动一个新聊天以完成迁移过程。
Codex
迁移
配置
23 replies
•
2026-05-09 18:01:53 +08:00
1
momuou
17h 10m ago
现在 codex 有啥便宜实惠的订阅方式嘛
2
designerly
17h 5m ago
为啥我没看到这个功能
3
shineonme
OP
17h 1m ago
@
designerly
在 Setting - General - Import work from other AI Apps
4
TonyMontana
16h 55m ago
1
Codex YYDS ，性能、价格、体验，平衡的神！
5
XTTX
16h 38m ago
1
从 claude 3 就开始用到了 opus 4.7, 一个星期前换了 Codex. 现在我完全不想换回去，codex 可以直接调用 image 2, 无敌。
6
yangxiaopeipei
16h 35m ago
不支持 cursor ？
7
QAZXCDSWE
16h 30m ago
拆家了
8
ZhaokunZhang
16h 30m ago
他要是开一个账号数据迁移就好了。我想把小号迁移到大号里。
9
gzy0217
16h 0m ago
感觉架构设计上，codex 跟 cc 还是有一段距离，只要有 cc 在，就不用 codex
10
shineonme
OP
15h 44m ago
@
gzy0217
是有差距，不过这类东西两天一更新，指不定哪天就变样了；对我而言，这个 App 用了就不想回 Cli 了，现在也有了 SSH 远程开发的功能，所以基本没再打开过 Cli 版本的
11
fkdtz
15h 15m ago
感觉最近 codex 风评反超 claude code
12
chaleaochexist
14h 52m ago
但是我账号黑了.... 用 visa 订阅 plus 拒绝了. 只能用免费版了.
13
cfancc
14h 48m ago
可以迁对话的话就太好了
14
ufan0
14h 47m ago
@
chaleaochexist
Apple Gift Card 稳定奔放
15
fennu2333
14h 46m ago
我测过让他帮我把一个 cc 的插件迁移到 codex ，写得一塌糊涂😂
16
qwwe01
12h 57m ago
@
gzy0217
感觉可以先试下使用 codex ，没有哪里感觉不如 cc
17
FringJX
12h 9m ago
各个国家有各个国家的“外卖”大战
18
defunct9
12h 6m ago
之前用 duck mail 撸了几百个 GPT Free 号，还是很稳，就靠这个续命了。
19
Shelios
11h 18m ago
好啊，claude code 额度用完了，正好迁移到 codex 继续跑
20
4seasons
11h 16m ago
@
FringJX
#17 星球大战和宠物猫打架还是有区别的😂
21
mxiangyu
10h 39m ago
现在 codex 有合适的中专吗？
22
gzy0217
10h 27m ago
1
@
qwwe01
都买了 100 刀的订阅。现在我的习惯是用 cc 澄清需求，写 plan ，让 codex review ； task / impl / review 都是这个流程。一个写，一个 Review
曾经尝试反过来，发现 codex 写的惨不忍睹
23
teaguexiao
8h 29m ago
用 cc 写、codex review 这个流程确实不错，cc 对上下文理解更深，codex 跑得快适合验证。两个互补比押注一个靠谱。
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1071 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 100ms ·
UTC 18:31
·
PVG 02:31
·
LAX 11:31
·
JFK 14:31
♥ Do have faith in what you're doing.
❯
```

---

## 15. 基于 AI 的 Chrome 爬虫辅助插件

- 日期: 2026-05-09 03:34
- 链接: https://www.v2ex.com/t/1211407#reply13

```
基于 AI 的 Chrome 爬虫辅助插件，自动监听网络请求并解析 API 逻辑。 
 之前爬虫每次都去抓 API 然后丢给 AI 分析，很麻烦，写了个 Chrome 插件，直接去抓请求，然后丢给 AI 分析这个接口是做什么的，以及一些字段分析。 
 功能 
 自动抓取 ：实时捕获浏览器 Fetch/XHR 请求及其 Response 。 
 AI 接口分析 ：一键分析接口功能，自动推断字段含义及业务逻辑。 
 语义解析 ：让 AI 解释复杂的 JSON 结构，告别手动盲猜字段。 
 计划 
 多语言生成 ：一键生成 Python (requests/httpx), Go, Node.js 爬虫代码。 
 类型定义导出 ：自动生成 TypeScript Interface, Go Struct, Pydantic Models 。 
 批量文档 ：导出整个页面的接口清单及文档。 
 代码模板定制 ：支持用户自定义生成的爬虫代码格式。 
 项目仓库 
 https://github.com/wangyi12358/auto-scrape-ai
```

---

## 16. DeepSeek V4 Pro：处于前沿的首个中文模型

- 日期: 2026-05-09 01:37
- 链接: https://www.v2ex.com/t/1211341#reply14

```
https://foodtruckbench.com/blog/deepseek-v4-pro 
 5 次运行全部成功。中位数投资回报率（ ROI ）高达 +1,257%。中位数净资产达 $27,142 。
首个跻身 Opus 4.6 、GPT-5.2 和 Grok 4.3 （最新版）同等 ROI 梯队的中国模型；
在所有受测的高级模型中，其运行表现最为出色且稳定性最高。
```

---

## 17. Serverless 里怎么处理需要建立长连接的外部资源？

- 日期: 2026-05-09 04:17
- 链接: https://www.v2ex.com/t/1211420#reply9

```
最近在 Cloudflare Workers 上接外部 Redis / Valkey ，发现传统 Node 服务那套“建一个 Redis client 然后复用连接”的思路不太行 
 Worker 会冷启动、冻结、恢复或回收，模块级 client 虽然能复用，但不像常驻进程里的连接池那么可靠。实际遇到的现象是：client 看起来 ready ，但 Redis 命令经常 timeout ，后续还会引发一些连带错误。尤其是从 cloudflare 阿姆斯特丹机房到 digital ocean 班加罗尔机房的连接质量差得离谱，已经超时到无法忍受了 
 我现在的临时处理是：Serverless 侧不直接维护 Redis TCP 连接，改成通过 HTTP 访问 Redis ，把连接池放到更适合常驻运行的地方。现在从 cloudflare 全球机房，到 racknerd 洛杉矶机房的 redis 代理，到 digital ocean 旧金山机房里的真实 redis 。虽然绕路更多了，但是基本不超时了 
 Worker -> HTTP -> Redis proxy -> Redis
但自建 Redis proxy 也挺麻烦，平台原生的 redis 资源又很贵 
 想请教大家：Serverless / Edge Runtime 里访问 Redis 、数据库、MQ 这类需要连接的外部资源，大家一般是直接连、HTTP API / proxy ，还是尽量改用平台原生存储？这种情况下有没有什么最佳实践？
```

---

## 18. Claude Code 最近总是在修复代码缩进

- 日期: 2026-05-09 02:14
- 链接: https://www.v2ex.com/t/1211362#reply10

```
RT 
 最近在使用 CC 的时候， 
 完成编码任务后 CC 总是会不停地纠结代码的缩进问题， 
 哪怕我明确告诉它使用 formatter 来做代码样式修复就行了， 
 它还是会不停的检查这个，而且是通过各种 bash 、py 命令来读取指定行的 tab/space 代码 
 烦得很啊，换不同的模型还是一样。 
 大家有没有同感？
```

---

## 19. Rebased, 一个 git 客户端

- 日期: 2026-05-09 02:19
- 链接: https://www.v2ex.com/t/1211364#reply17

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
›
Pro Git
›
Atlassian Git Tutorial
›
Pro Git 简体中文翻译
›
GitX
Advertisement
V2EX
›
git
Rebased, 一个 git 客户端
nathanw
·
16h 12m ago
· 1855 views
将 IntelliJ IDEA 内置的 Git 客户端剥离出来，做了一个精简版。
对于习惯了 IntelliJ 的 Git 的用户估计会是一个好的选择。
https://github.com/detachhead/rebased
rebased, fork, 这些 app name 取得也挺好的。
当然，作者不是我。
git
IntelliJ
精简版
17 replies
•
2026-05-09 23:31:00 +08:00
1
S1ahs3r
15h 34m ago
作者貌似在本论坛，发过
2
chenluo0429
15h 17m ago via Android
我在用，怎么说呢？聊胜于无。
基本上就是基于 idea 改了改，一样的卡顿，内存也没有显著变少，交互和界面还是那个老一套，连设置都是原来的。整体来说和打开一个 idea 没啥太大区别。
3
pa4swordforget
15h 15m ago
用腾讯 ugit 不就好了，我感觉非常好用
4
Matthew168
15h 7m ago
1
在用 Fork, 感觉还行
5
Ravenddd
14h 57m ago
一直用 Fork,感觉很好用,就是 AI 生成不支持自定义模型,只能自带的 OpenAI
6
dinjufen
14h 55m ago
一个 git 客户端占 500 兆内存
7
AIXAPI
14h 55m ago
太懂了！ IDEA 里的 Git 操作是真的顺手，但每次开 IDE 只为了处理个 rebase / 冲突太笨重了，这个剥离版简直是刚需。
8
WenbinFAN
14h 2m ago
@
AIXAPI
重复以上内容
9
HotieCutie
13h 32m ago
可以像原 idea 样直接跳到修改位置的源码进行编辑吗？
10
liubaicai
13h 21m ago
372 MB ，这合理吗
11
PrettyJack
13h 10m ago
@
liubaicai
JAVA 开发的，大一点也很合理吧
12
putaozhenhaochi
12h 28m ago
没人用 rust 重写吗 /dog
13
zktree
11h 54m ago via iPhone
x 上，看到有人推荐用了下，还是原来的味道，IDEA 太重了
14
yjxjn
8h 16m ago
Fork 以及 SourceGit ，这 2 个很不错。
15
faimin
5h 34m ago
@
yjxjn
+1
16
LeviAkerman
3h 46m ago
@
putaozhenhaochi
同期望有人 rust 重写一个哈哈哈， 这个还是占用内存很大
17
jqtmviyu
3h 0m ago
用 sourcegit, 占用少.
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1071 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 133ms ·
UTC 18:31
·
PVG 02:31
·
LAX 11:31
·
JFK 14:31
♥ Do have faith in what you're doing.
❯
```

---

## 20. claude 投资方面的 skill 推荐

- 日期: 2026-05-09 06:26
- 链接: https://www.v2ex.com/t/1211460#reply5

```
op 的 claude 每周都有 20%用不完，目前就装了两个 skills： 
 andrej-karpathy-skills@karpathy-skills 
 superpowers@superpowers-dev 
 主要用来做代码 review ，代码重构，目前使用效果挺好。 
 今天突发奇想，有没有关于理财方面的 skill ，配合每日复盘，生成复盘文档，推送到 github ，配合 vercel 页面展示。 推送 github ，vercel 页面展示，这个结合 claude desktop 提问，已经搞定。请教大家有哪些好用的 skills ，不局限于理财方面。 
 欢迎各位大佬分享自己使用方面觉得非常好用的点，我现在就是只拿来代码 review 、代码重构，感觉玩的不花。
```

---

## 21. BoxLite —— 2K star 纪念，非常感谢 V2EX 这个社区和朋友

- 日期: 2026-05-09 06:30
- 链接: https://www.v2ex.com/t/1211461#reply2

```
一开始 BoxLite 只是想作为一个嵌入式 library ，内核是 rust 写的 micro-VM 
 现在 BoxLite 已经进化到可以嵌入，可以本地化部署，可以集群部署 
 记得一开始不懂 V2EX 的规则，发的帖子侵入性太强，不过社区的包容性非常强，社区的朋友立马指出了 
 今天 BoxLite 进入 2k star ，很大的功劳要归功于 V2EX 社区一开始的支持～
```

---

## 22. 前端 harness 有搞头吗？后端用 supabase 的数据库，直接纯前端操作！

- 日期: 2026-05-09 03:31
- 链接: https://www.v2ex.com/t/1211404#reply6

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
• 请不要在回答技术问题时复制粘贴 AI 生成的内容
V2EX
›
程序员
前端 harness 有搞头吗？后端用 supabase 的数据库，直接纯前端操作！
powerless
·
14h 59m ago
· 1128 views
前端
后端
supabase
6 replies
•
2026-05-09 17:50:31 +08:00
1
8355
14h 57m ago
账号密码写在前端吗
2
powerless
OP
14h 55m ago
@
8355
差不多这个意思，密码加密在前端，用环境变量 SUPABASE_USER_SECRET 来控制生成的规则。
3
powerless
OP
14h 54m ago
操作流程也是全部放前端，数据库有 rls 策略去控制哪些人可以增删改查
4
horizon
14h 51m ago
nextjs 全栈啊。。
5
rogerer
12h 40m ago
和 harness 的关系是什么？
6
XTTX
8h 40m ago
和 supabase 的关系是什么？ 纯前端的意思是没有 api
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1071 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 60ms ·
UTC 18:31
·
PVG 02:31
·
LAX 11:31
·
JFK 14:31
♥ Do have faith in what you're doing.
❯
```

---

## 23. 分析一个技巧让同事不知道我使用了 ai ： git 忽略本地改动文件，实现不提交

- 日期: 2026-05-09 02:51
- 链接: https://www.v2ex.com/t/1211377#reply14

```
git 库中不存在的文件 
 可以修改 项目路径下的 .git/info/exclude 添加忽略规则，和 .gitignore 效果一致，但是不会被提交到 git 
 已经被提交的文件 
 例如如果你使用了我的 vite-plugin-pilot 插件 ，而不想被人知道的话可以通过如下命令实现 
 ## 添加忽略
git update-index --skip-worktree ./vite.config.ts
## 撤销
git update-index --no-skip-worktree <文件路径>
# 或
git update-index --no-assume-unchanged <文件路径>
```

---

## 24. gpt5.5 突然来一句“调度仍是 interval_global / 30s 亚洲 AV”，真 TM 搞笑

- 日期: 2026-05-08 18:14
- 链接: https://www.v2ex.com/t/1211313#reply17

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
V2EX
›
OpenAI
gpt5.5 突然来一句“调度仍是 interval_global / 30s 亚洲 AV”，真 TM 搞笑
jfie132
·
1 day ago
· 4074 views
我让 codex 帮我调试，结束时突然来了个"亚洲 AV"，不知道哪里出问题了。
调度
搞笑
亚洲
17 replies
•
2026-05-09 13:53:25 +08:00
1
manbamentality
22h 50m ago
4o 时代已有先例：
GPT-4o: 给主人留下些什么吧？ - 蒋炎岩的文章 - 知乎
https://zhuanlan.zhihu.com/p/697685138
2
moefishtang
20h 5m ago via Android
难以想象训练集里混了什么（
3
v400127
18h 47m ago via Android
彩票也很多
4
paranoiagu
18h 26m ago via Android
我也发现了，在写 html 的时候过程中出现类似的，然后最后会去掉。
5
x86
18h 11m ago
4
怪温馨的，提示我不要久坐编码，该看片放松了。
6
Vegetable
17h 5m ago
你应该回复他：倒是提醒我了
看他能不能接住梗
7
rammiah
17h 2m ago
使用英文提问也有吗？
8
106npo
17h 0m ago via Android
说明用上正版 GPT 了。
这么多年了，你第一次见么，是不是以前用的都是盗版的 😂
9
nc
16h 59m ago
Codex 使用英文情况下从未遇到该情况，就是中文语料问题。
10
yazinnnn0
16h 47m ago
这倒提醒我了.jpg
11
snylonue
16h 44m ago
tokenizer 的问题
12
cbythe434
16h 12m ago
你让他细说下亚洲 AV
13
miniliuke
16h 7m ago
不是外文版的会出现地精、小精灵这些玩意吗......只不过在系统提示词中强行抑制了......感觉 ai 还是会莫名其妙犯个蠢
14
106npo
16h 4m ago
@
miniliuke
两者原因还是不太一样,地精是后训练阶段奖励模型的问题.
中文这个是预训练之前确定 tokenizer 时就出的问题
15
Doloroso
15h 37m ago
我用 claude, 给的中文提示词,回复中用英文很正常, 但是进程结束 用韩语通知我,太高看我了
16
Perry
15h 30m ago via iPhone
为什么是 30 秒不是 30 分钟
17
fzzff
12h 37m ago
遇到过, 卸载掉 superpower 等技能就没再出现了, 怀疑是技能安装渠道有问题导致技能被投毒
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1071 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 73ms ·
UTC 18:31
·
PVG 02:31
·
LAX 11:31
·
JFK 14:31
♥ Do have faith in what you're doing.
❯
```

---

## 25. 异机备份方案

- 日期: 2026-05-09 02:32
- 链接: https://www.v2ex.com/t/1211369#reply11

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
V2EX
›
数据库
异机备份方案
yjd
·
15h 58m ago
· 1018 views
需求，定时把 a 机器数据库复制一份到 b 机器
我在想有没有一种每次连接自动采用随机密码连接后同步数据后断开，下次连接又是随机密码。
防止 a 被侵入破坏，进而连接到 b 也破坏了 b 数据。
如果人工入侵那可能会去逆向这个同步工具找出算法。
比如遇到勒索一般是一套工具自动化处理不会去做到这步。
备份
同步
随机
11 replies
•
2026-05-09 17:47:35 +08:00
1
langhuishan
15h 37m ago
群晖备份有版本控制。
2
x86
15h 29m ago
快照，备份快照
3
yjd
OP
15h 18m ago
@
x86
底层快照有一份了。还想同步一份文件到另一台机器。
4
lancelee01
15h 3m ago
如果改成 b 自动拉取 a 的备份文件，是不是就不怕 a 的密码泄露影响 b 了 doge
5
lancelee01
15h 0m ago
1
自动采用随机密码连接后同步数据后断开，下次连接又是随机密码。这个不太可行，假设 a 是服务端，密码是 1 ，b 作为客户端是需要知道密码的，否则连接 a 是无法通过 a 的认证的。因此 a 变化密码后，需要下发给 b ，下发存储本身是有风险的。
6
cslingjun
14h 53m ago
搞个中转，上传到 oss 这种呢
7
aarones
14h 47m ago
b 可以登陆 a ，不代表 a 可以登陆 b ，比如有 NAT 就不行，随机密码搞复杂了，只需要备份存储方拉取备份文件就行
8
yjd
OP
14h 39m ago
@
lancelee01
只能自有一套伪随机的机制，比如内部先自带密钥通讯协商后再建立连接。我目的是防被自动化工具二次感染。
因为最近中了勒索。万幸是备份数据用的那套系统自己的压缩格式，结果勒索识别一看不是数据库就没被破坏😂
不过你提的 b 机器自动过来拉取是个好方案👍，就用这个了。
下一步是找个稳定的商业级备份工具。
9
yjd
OP
14h 37m ago
@
cslingjun
我就备份到局域网另一台机器上。现在是 a 机器系统本地备份一份。a 机器底层 esxi 也弄快照。
b 机器凌晨自动备份一份文件。b 机器底层也定时快照
10
realpg
PRO
10h 37m ago
说点不好听的大实话：
能中勒索的人，建议别管理服务器，专业的事儿给专业的人干
11
yjd
OP
8h 43m ago
@
realpg
数据备份和防护确实有欠缺。通过那套系统进来。我一直知道有漏洞容易被黑。一直没上心。
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1071 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 38ms ·
UTC 18:31
·
PVG 02:31
·
LAX 11:31
·
JFK 14:31
♥ Do have faith in what you're doing.
❯
```

---

## 26. 锤子找钉子的项目分享：假想企业本地部署后不用人工洗库接入 llm 的中间层。

- 日期: 2026-05-09 03:15
- 链接: https://www.v2ex.com/t/1211391#reply1

```
锤子找钉子的项目分享：假想企业本地部署后不用人工洗库接入 LLM 的中间层 
 我问 AI ，企业数字化差什么？ 
 他说最难的是数据清洗，库太多，数据录入不规范，字段命名乱。ai 要靠猜。 
 所以花了两周写了个中间层，想解决"企业多个数据库接 LLM 时字段乱、权限乱、口径乱"的问题。写了 7000 行 Python 、134 个测试、3 份架构 spec 。然后意识到：我没有用户，没有真实场景验证，可能从头到尾在解决一个我想象出来的问题。 
 发出来给大家看看，也许有人真遇到过这个痛点，也许大家帮我确认这就是个锤子找钉子。 
 想解决什么问题 
 企业内部通常有好几个数据库：销售用 MySQL 、财务用 PostgreSQL 、HR 用 SQL Server 。现在老板说要接 LLM 让业务人员自然语言查数据。 
 直接接会遇到这些问题： 
 问题 举例 
 字段名无意义 aa 字段是单价， hj 是合计，LLM 猜不出来 
 同名不同义 销售库的"金额"是回款，财务库的"金额"是开票 
 权限失控 销售员能查到成本和利润率 
 没有 SQL 审查 LLM 生成的 SQL 可能 DROP TABLE 
 敏感数据裸奔 手机号身份证明文返回 
 我的想法是在数据库和 LLM 之间加一层，把这些脏活自动化： 
 企业数据库群（ MySQL/PG/SQLite/Oracle/达梦）
 ↓
┌─────────────────────────────────┐
│ KaiwuBridge │
│ 自动理解字段含义（不用人工标注） │
│ 权限控制 + SQL 审查 + 数据脱敏 │
│ 跨库字段自动对齐 │
└─────────────────────────────────┘
 ↓
任意 LLM （本地 Ollama / DeepSeek / GPT ） 核心卖点是 不用人工洗库 ——传统做法是 DBA 花几周给每个字段写注释、建数据字典，我想用 LLM+统计方法自动搞定。 
 实现了什么 
 1. 自动理解字段含义（图传播方案） 
 不是简单让 LLM 看字段名猜含义，而是： 
 数据画像 ：统计每个字段的分布、空值率、唯一值比例 
 代数关系检测 ：自动发现 单价 × 数量 ≈ 合计 这种关系 
 建图 ：把字段、外键、代数关系建成一张依赖图 
 图传播 ：LLM 在图上迭代 3-5 轮，每轮看邻居字段的描述来修正自己的理解 
 这样即使字段名是 aa ，系统也能通过"aa × 整数字段 ≈ hj"推断出 aa 是单价。 
 灵感来自 2026 年 3 月的 DBAutoDoc 论文，核心思想是 schema 理解本质上是图结构问题。 
 2. 七层安全防线 
 物理层（只读账号）→ SQL 白名单（只允许 SELECT ）→ 注释绕过防护 →
字段级权限（ LLM 看不到=查不到）→ 行级过滤 RLAC （华东员工只看华东数据）→
数据脱敏（手机号自动打码）→ 动态脱敏（按角色返回不同精度） 3. 解耦架构（三个接口） 
 GET /v1/context — Agent 获取 schema+权限+映射+歧义信号
POST /v1/execute — Agent 提交 SQL ，中间层负责安全检查+执行+脱敏
POST /v1/chat/completions — OpenAI 兼容接口（兼容层） Agent 层和数据层彻底分离。Agent 只管生成 SQL ，中间层只管安全执行。 
 4. 跨库字段自动对齐 
 bge-m3 embedding + Wasserstein 分布距离 
 主动学习：优先推送置信度 0.6-0.8 的模糊案例给人审核（信息价值最高） 
 用户确认/拒绝后自动提取规则，不是调阈值 
 5. 告警过滤 
 同一个错误短时间内反复出现且从未成功 → 自动压制，不打扰用户。管理员可以看到"僵尸规则"列表。 
 6. Schema Linking （ LLM 路由） 
 企业可能有几十张表、几百个字段，不可能全塞给 LLM 。需要根据用户问题精准定位到相关的 2-3 张表。 
 做法参考了 SchemaGraphSQL （ ACL ARR 2025 ）： 
 建图 ：把所有表作为节点，外键关系+跨库映射作为边 
 LLM 实体提取 ：一次调用从问题中提取关键实体，映射到相关表 
 BFS 扩展 ：在图上从相关表出发走 2 跳，把 JOIN 需要的关联表也带上 
 精选子集 ：最多给 LLM 看 5 张表的 schema ，而不是全量几十张 
 这样 LLM 生成 SQL 时只看到精选的、和问题相关的表，不会被无关表干扰，生成准确率显著提升。 
 零样本、不需要 embedding 模型、不需要训练。一次 LLM 调用搞定路由。 
 功能全景（经过几次迭代后的当前状态） 
 从最初只有"连数据库+调 LLM"，到现在塞了一堆功能。用一张表说清楚每个模块干什么： 
 功能模块 解决什么问题 什么场景用 原理/技术 
 数据画像 ( profiler.py ) 字段名无意义时无法理解数据 scan 时自动运行，给每个字段建统计档案 空值率/唯一值比例/数值分布/高频值采样 
 代数关系检测 ( profiler.py ) aa×bb≈cc 这种隐含业务关系人看不出来 同表内数值字段三元组枚举 numpy 向量化计算，5%误差容忍度 
 图传播引擎 ( graph_propagation.py ) 单看一个字段猜不出含义，需要上下文 scan --semantic 时替代逐字段 LLM 生成 建依赖图→LLM 迭代 3-5 轮→邻居描述作为 context 精化 
 Schema Linking 路由 ( schema_graph.py ) 几十张表不能全塞给 LLM 每次用户提问时自动触发 外键图+LLM 实体提取+BFS 2 跳扩展，精选≤5 张表 
 跨库语义匹配 ( matching.py ) 不同库的"金额"可能是不同概念 scan 后自动两两匹配，生成 pending 映射 bge-m3 embedding + Wasserstein 分布距离 
 主动学习 ( matching.py RuleExtractor) 人工审核效率低，不知道先审哪个 管理界面展示待审核映射时排序 优先推送置信度 0.6-0.8 的案例（信息价值最高） 
 SQL 白名单审查 ( security.py ) LLM 可能生成 DROP TABLE 每次执行 SQL 前强制检查 sqlparse 语法树分析，只放行 SELECT/WITH 
 字段级权限 ( permissions.py ) 销售员不该看到成本字段 schema 发给 LLM 前过滤 配置 denied_columns ，物理移除字段 
 行级过滤 RLAC ( executor.py ) 华东员工只能看华东数据 SQL 执行时 CTE 子查询包装注入 WHERE 不依赖 LLM"自觉"，执行层强制注入 
 数据脱敏 ( security.py + executor.py ) 手机号身份证不能明文返回 结果返回前自动处理 正则打码 + 按角色动态精度（ full/partial/round ） 
 告警过滤 ( alert_filter.py ) 同一个错误反复弹出烦死人 兼容层执行失败时判断 滑动窗口频率统计，≥5 次且 0 成功→压制 
 歧义检测 ( server.py ) "销售额"在两个库都有，用哪个？ /v1/context 接口返回歧义信号 语义名片匹配+多库来源检测，含 confidence 
 数据新鲜度 ( executor.py ) 查到的数据可能是上周的 执行成功后附加提示 查 MAX(updated_at)，超 24 小时警告 
 映射导入导出 ( admin.py ) DBA 想在 Excel 里批量维护映射关系 管理后台 CSV 上传下载 CSV 解析 + LLM 验证层（检查明显错误） 
 持续学习 ( admin.py + matching.py ) 用户反馈应该让系统越来越准 confirm/reject 映射时自动触发 贝叶斯更新阈值 + 规则提取（不只是调参） 
 解耦接口 ( server.py ) Agent 层和数据层耦合在一起不好扩展 Agent 自己生成 SQL 时用 context+execute REST 分离：context 只给数据，execute 只管执行 
 一共 22 个 Python 模块，7015 行代码。说实话写到后面自己都觉得功能堆太多了。 
 测试和结果 
 代数关系检测 
 用 100 行模拟订单数据测试： 
 召回率：100%（ 2/2 个标注关系全部检测到） 
 误报率：0%（编码字段没有被误判为代数关系） 
 语义匹配基线（诚实报告） 
 用 10 对手工标注的跨库字段对测试： 
 **负例拒绝率：100%**（不相关字段不会被误匹配） 
 **正例召回率：0%**（裸英文字段名在 bge-m3 上语义分全部低于阈值） 
 这个 0%是预期的——证明了图传播层的必要性。裸字段名 sales_amount 和 revenue 的 embedding 相似度只有 0.67 ，低于 0.85 阈值。需要图传播先生成中文描述（"每笔订单的含税销售金额"），再做匹配才有意义。 
 但我还没有在真实数据库上跑过完整流水线。 
 安全测试 
 65 个安全测试覆盖：SQL 注入（含注释绕过）、JWT 伪造、越权访问、频率限制、数据脱敏。全部通过。 
 总计 
 134 passed, 0 failed, 21 warnings 技术栈 
 Python 3.12 + FastAPI + SQLAlchemy 2.0 
 sentence-transformers (bge-m3) 做 embedding 
 numpy/scipy 做统计验证 
 SQLite 存元数据（零部署） 
 支持 MySQL / PostgreSQL / SQLite / SQL Server / Oracle / 达梦 / 人大金仓 
 全部依赖 Apache 2.0 / MIT / BSD ，可商用。 
 为什么说是锤子找钉子 
 写完之后冷静下来想了几个问题： 
 1. 谁是用户？ 
 我假想的场景是"中型企业，有 3-5 个业务数据库，想让业务人员自然语言查数据"。但我没有找到一个具体的企业说"我需要这个"。 
 2. 真实场景下这个问题存在吗？ 
 也许存在，但解决方案可能不是我想的这样： 
 大企业有数据中台团队，人工建数据字典不是问题 
 小企业可能就一个 MySQL ，不需要跨库对齐 
 中型企业可能更需要的是 BI 工具而不是自然语言查询 
 3. "不用人工洗库"这个卖点成立吗？ 
 图传播方案理论上能自动理解字段含义，但： 
 需要 LLM （本地 7B 模型够不够？需要 API 调用？） 
 准确率未在真实脏数据上验证 
 企业可能宁愿花一周人工标注也不愿意信任自动化结果 
 4. 过度工程了吗？ 
 7000 行代码、图传播、主动学习、告警过滤、动态脱敏……如果第一个用户只需要"连 MySQL + 权限控制 + 调 DeepSeek"，那 90%的代码都是提前优化。 
 如果你遇到过这个问题 
 想听听大家的看法： 
 是我想的这么简单么数字化落地?LLM + 优化层 计入数据库，就 AI 落地么？ 
 真实企业数字化落地最难攻克什么？ 
 这个方向值得继续做吗？还是应该 pivot 成更具体的东西（比如只做 SQL 安全审查层）？ 
 代码在本地，如果有人感兴趣可以开源。也欢迎直接告诉我这是个伪需求，省得我继续往里面投时间。 
 参考的论文和开源项目 
 来源 用在哪 怎么用的 
 SchemaGraphSQL (ACL ARR 2025) Schema Linking 路由 核心思想：用外键关系图+LLM 实体提取+BFS 路径搜索做 schema linking ，零样本不需要训练。我直接实现了这个方案 
 DBAutoDoc (2026.03) 图传播引擎 核心思想：schema 理解是图结构问题，通过依赖图迭代传播语义修正直到收敛。我简化了实现，没用原文的 GNN ，直接 LLM 迭代 
 LLM-FK (2025) 外键发现思路 三 agent 协作（ Interpreter/Refiner/Verifier ）的思路启发了我的约束发现设计，但我没实现多 agent ，只用了统计方法 
 Valentine 跨库匹配 baseline schema matching 的开源 benchmark ，参考了它的评估方法论（ precision/recall on labeled pairs ） 
 ALITE 约束发现 用数据分析发现函数依赖和包含依赖的思路，我简化成了代数关系检测（ A×B≈C ） 
 sentence-transformers embedding 计算 直接用的 bge-m3 模型做字段语义向量化 
 FastAPI Web 框架 OpenAI 兼容接口 
 SQLAlchemy 数据库连接 多数据库统一适配层 
 sqlparse SQL 安全审查 语法树分析，白名单验证，表名提取 
 部分论文 ai 搜的，，，，
说实话，论文读了不少，但真正落地时大幅简化了。DBAutoDoc 原文用的是 GNN 做图传播，我直接用 LLM 迭代替代了（因为目标场景是企业内部几十张表，不是几千张表的学术 benchmark ，LLM 迭代 3-5 轮完全够用）。 
 技术细节：Python 3.12 / FastAPI / SQLAlchemy / bge-m3 / 图传播架构 / 134 测试全绿 
 附仓库（为了避免说推广仓库的，所以放最后）： https://github.com/val1813/kwb
```

---

## 27. 关于我用阿里云 ESA Pages 中遇到的 bug 们。

- 日期: 2026-05-09 02:31
- 链接: https://www.v2ex.com/t/1211368#reply0

```
假如源站已经有 HSTS Header ，然后在 ESA 中也设置了 HSTS 会导致 header 中有两个 HSTS Header ，然后 https://hstspreload.org/ 碰到双重 header 就会报错 
 https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/build-pages 文档里面写的 "notFoundStrategy": "404Page" 会返回静态托管目录的 404.html 文件及 404 Not Found 状态码。但是同一个文档下面的图又说 404Page 策略会返回 200 状态码，第一次见到这种 Pages 服务 
 我在 ESA 里面设置 修改响应头 对 ESA Pages 是没用的，但很奇怪的是，只要我同时设置了缓存规则，就又有用了 
 没法给 apex @ 域名添加 ESA Pages ，说没法和 MX 记录共存，但是其实是有 CNAME 拉平这个功能的。 
 其他的也不算 bug 了，但基础功能缺失，例如没有类似 Cloudflare Pages Headers File 的功能，导致只能在 ESA 里面修改响应头。还有 esa-cli 的 deps 里面有 react-dom 这种浏览器才需要的包之类的。
```

---

## 28. 国产应用有哪个能解压 7-zip.7z 后缀文件的吗？

- 日期: 2026-05-08 14:14
- 链接: https://www.v2ex.com/t/1211296#reply14

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
V2EX
›
Android
国产应用有哪个能解压 7-zip.7z 后缀文件的吗？
jacketma
·
1 day ago
· 2572 views
国产手机 ROM 默认的解不了 .7z 后缀的，只能解 .zip 的。
用 .zip 的加密无法隐藏文件名，改用 .7z 的就可以。但是，在手机上打开 .7z 不方便
解压
文件
手机
14 replies
•
2026-05-09 18:02:21 +08:00
1
psllll
1 day ago
装个文件管理器不就能解压了
比如 mt es
2
IceRovah
1 day ago via Android
mt 管理器是国产的不，刚试了，能压缩也能解压。
3
easylee
1 day ago
@
IceRovah
看到您回复的 mt 管理器，不禁感慨万千，借年轻人的话是“死去的回忆开始攻击我”。
上次用还是十多年前用来搞机，和烧饼同一时代。
当时其方便提权以及签名改包，并且 UI 一直符合最新的 Material 设计，记忆犹新。
4
cybort
1 day ago via Android
为啥非得要国产应用？用 zarchiver 不行吗
5
docx
1 day ago via iPhone
MT+1
6
longlonglanguage
1 day ago
有个浏览器叫做 alook ，解压的时候用它打开，它能解压 7z 的好像。
7
jim9606
23h 49m ago
2
普遍支持 zip 是因为 zip 是 apk/apex 的实际底层格式，android 直接提供相关的稳定 api ，所以系统文件管理器基本都顺手支持 zip 的基础功能(zip64+deflate)
7z 没这待遇，要应用自己带 7z 或者 libarchive 实现。
8
cutecore
17h 39m ago
zarchiver
9
felixlong
17h 6m ago
2
笨蛋。zip 压缩两次就可以隐藏文件名啦。
10
jackOff
16h 58m ago
文件管理器这种东西在国产手机里生存空间几乎为 0 吧？我记得现在不管是 ios,鸿蒙还是安卓都势必要把访问公共文件夹的权限掐死掉，那手机上基本不可能有第三方文件管理器或者啥解压缩软件的生存空间，你只能强制使用手机厂商的文件管理器，解压缩也只能看手机厂商脸色给你适配
11
jacketma
OP
16h 28m ago
@
jim9606
感谢教学
@
felixlong
这么离谱的骚操作，作用非常的离谱😂
12
MisterQ
15h 55m ago
@
jackOff
单就解压这个功能来说，和文件管理器是两回事，并不一定需要访问公共文件夹。就像 iOS 这么严的沙箱，如果一个软件中的文件要用另一个软件打开，一样有众多案例，比如微信收到的 word 文件，选择用 wps 打开，底层逻辑就是把文件拷贝一份过去
13
wednesdayco
9h 14m ago
我说一个暴论：全能解压王！
14
chr0056
8h 29m ago
对啊，找正经个文件管理器就行。
推荐 [NMM File Manager](
https://play.google.com/store/apps/details?id=in.mfile
)
小而美，作者为国人，独立开发者
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1071 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 61ms ·
UTC 18:31
·
PVG 02:31
·
LAX 11:31
·
JFK 14:31
♥ Do have faith in what you're doing.
❯
```

---

## 29. 有没有稳定的 claude 的 max 购买渠道啊....淘宝店推荐也行..

- 日期: 2026-05-08 09:11
- 链接: https://www.v2ex.com/t/1211230#reply27

```
Home
Sign Up
Sign In
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
Sign Up Now
For Existing Member
Sign In
V2EX
›
Claude
有没有稳定的 claude 的 max 购买渠道啊....淘宝店推荐也行..
1
seek2
·
1 day ago
· 2112 views
有没有稳定的 claude 的 max 购买渠道啊....淘宝店推荐也行... 有的淘宝店 买的容易封,不同店家的成品账号还有区别吗
Claude
购买
渠道
27 replies
•
2026-05-09 21:51:07 +08:00
1
mingtdlb
1 day ago
中转站套壳怎么验证？ 4.7 实际是 4.5 4.6
稳定、靠谱的中转站其实还真有需求，我也在看
2
Quik
1 day ago
google play 绑定一下国内的 visa 卡就可以呀，只需要一个安卓手机即可；封号了也是会退款的。
3
AIXAPI
1 day ago
提醒一下，选中转站一定要注意两点：
一是别信标着高版本实际套壳低版本的，跑复杂任务一眼就能露馅；
二是别选风控差的，很容易因为中转 IP 问题导致自己的号被封。
4
nullyouraise
1 day ago
https://item.taobao.com/item.htm?id=901629108972
我买过这个，很稳，店家是用 Google 账号登录+美国信用卡付款的，优点是封号包换包退款，缺点是比官方订阅价贵一倍多，100 刀的 Max5 他卖 1000 ，别看他吹的什么白名单之类的瞎扯的话
5
HFX3389
1 day ago
咱们站内不就很多的中转站推广帖子吗，哦~你说的是 Max 啊，Max 上的话很麻烦的哟，买成品号或者礼品卡就不知道是真钱还是黑钱开的，代充的话还要弄好各种环境问题不然会封号，淘宝买还不会退款，要买还是走商店订阅交点保护费吧
6
LeviAkerman
1 day ago
同有需求，现在 cc 接的 DeepSeek v4pro 有时候用不下去
7
HFX3389
1 day ago
@
nullyouraise
#4 拿来反代然后 1.8 一刀卖出去岂不美哉~
8
zhhmax
1 day ago
我卖 Claude 礼品卡目前没人反馈封号，有不少回头客回购续费的，pro 卖的多，max 也有。美国信用卡付款，自己小心一点用还是挺稳的。当然价格也是在原价的基础上加了一些手续费。
9
HFX3389
1 day ago
@
zhhmax
#8 明盘，我猜 pro 要 200 ，max 5x 要 1000 ，max 20x 要 2000
10
zhhmax
1 day ago
@
HFX3389
#9 贵了，打个八折，这价格简直就是在抢了。
11
yangheng4922
1 day ago
https://shop.xuedingtoken.com/?dist=7MRALF8V
这个目前赢了$6000 左右还挺稳定，走我的链接有 95 折，走分销的话有 7 折
12
yangheng4922
1 day ago
13
czwstc
1 day ago
可以直接美国的实体卡支付。。。这么赚钱的吗？
比如汇丰 US 的储蓄卡。
14
chenqifeng
1 day ago
现在的问题不是买不到，是官方的 cc 封号太厉害了
15
niubilewodev
1 day ago
先用 U 卡套 Apple Pay/Google Pay 试试。
我反正是套着 Google Pay ，已经用到第二个月了。
上个月是 Max 20x ，这个月换成了 Max 5x 。（因为我上个月只用了大约 2700 刀的 API 费用，每周都不到限额的一半）
自己卡支付 > 应用商店订阅 > 淘宝买号 > Claude 礼品卡
自己卡支付被封，还能把钱要回来，淘宝被封还能按天退款，Claude 礼品卡被封那可真是全打水漂了。
16
guhuisec
17h 39m ago
要成品号，可以找我，可稳定充值
17
guhuisec
17h 38m ago
忘了，我的 eHl0aGluaw==
18
ihainan
17h 27m ago
@
Quik
我的 Google Play 第一次订阅 Claude Code Max 5x ，结果封号之后 Google 和 Anthropic 都拒绝退款。
19
milkleeeeee
16h 59m ago
厚脸皮推荐一下我自己的产品，
devrouter.ai
背后接入了多个开业时间长、口碑较好的中转站，然后像 OpenRouter 那样根据稳定性自动路由，近 7 天稳定性 99.9%，可以看看 opus 4.7 的数据
https://devrouter.ai/models/detail?model=claude-opus-4-7
20
Tony2017
16h 30m ago
企业级稳定 API 中转站，可开票，支持 500+ 模型，注册送测试金，欢迎测试
API 中转站地址：
https://ai.levolink.com/
21
XTTX
16h 29m ago
我已经从 cc max 换成了 codex, 个人老号，包括我自己建的美国家宽。 需要的 bGZnZm9yd2FyZA==
22
Quik
14h 14m ago
@
ihainan
#18 我记得 Anthropic 对封号都退款来着。难不成 Google play 的策略和网页订阅的退款策略不一样嘛。
23
ANT1FLAG
12h 17m ago
跑个题，我媳妇儿马上出国学习一阵，国外办张储蓄卡，用来支付能有用吗
24
yy6090
11h 23m ago
@
czwstc
有这种卡卖吗 你知道哪里有吗 相比起 AppStore 里面 购买礼品卡来买好些吗
25
yy6090
11h 21m ago
@
nullyouraise
我去看了下 确实贵 你还在用他家的吗 不会封号的吗
26
nullyouraise
7h 58m ago
@
yy6090
#25 还在用，已经两个月了
27
LuliYanng
4h 40m ago
说实话，没有什么能真正稳定的。。。A\封号不给理由的，不是过了第一关就没事了，没准你哪天用着用着就给你封了。身边不乏朋友用老帐号都被无缘无故封号的
About
·
Help
·
Advertise
·
Blog
·
API
·
FAQ
·
Solana
·
1071 Online
Highest 6679
·
Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 69ms ·
UTC 18:31
·
PVG 02:31
·
LAX 11:31
·
JFK 14:31
♥ Do have faith in what you're doing.
❯
```

---

## 30. AI 编程工具大家实际使用中哪个综合下来最好用？

- 日期: 2026-05-07 06:11
- 链接: https://www.v2ex.com/t/1210849#reply92

```
@
yuankui 第一命令行不利于 diff ，AI 动不动同时改 5 个 10 个文件，命令行的 review 效率太低了，除非你说 AI master 不需要人类 review.
第二 GUI 的交互方式天然并行，你可以在看到 AI 工作过程的同时看其它代码或者 preview staging 、编辑配置、写文档，命令行基本要切窗口，很不跟手
第三需要古法手工修复的时候，复制粘贴要方便得多……
而且我很喜欢 vscode+copilot 的交互，最重要的一点是它同时暂存了 1) git 工作区改动 2) agent 在本次 session 的改动 3) agent 在本轮 prompt 后做出的改动，回滚的层级很灵活而且很直观，可以单行、单文件、单会话控制保留部分
对于工作流已经很固定的稳定项目可能感知不到…… 我还见过有人直接丢给在线 codex 跑，自己直接摸鱼等回来黑盒测试的
```

---
