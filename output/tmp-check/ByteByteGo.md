# ByteByteGo

> 分类: 技术周刊
> URL: https://blog.bytebytego.com/feed
> 抓取: 20 篇

---

## 1. EP214: Claude Code vs. OpenClaw: 5 Design Dimensions

- 日期: 2026-05-09 15:31
- 链接: https://blog.bytebytego.com/p/ep214-claude-code-vs-openclaw-5-design

```
✂️ Cut your QA cycles down to minutes with QA Wolf (Sponsored) 
 If slow QA processes bottleneck you or your software engineering team and you’re releasing slower because of it — you need to check out QA Wolf. 
 QA Wolf’s AI-native service supports web and mobile apps , delivering 80% automated test coverage in weeks and helping teams ship 5x faster by reducing QA cycles to minutes. 
 QA Wolf takes testing off your plate. They can get you: 
 Unlimited parallel test runs for mobile and web apps 
 24-hour maintenance and on-demand test creation 
 Human-verified bug reports sent directly to your team 
 Zero flakes guarantee 
 The benefit? No more manual E2E testing. No more slow QA cycles. No more bugs reaching production. 
 With QA Wolf, Drata’s team of 80+ engineers achieved 4x more test cases and 86% faster QA cycles . 
 Schedule a demo to learn more 
 This week’s system design refresher: 
 Claude Code vs. OpenClaw: 5 Design Dimensions 
 Become an AI Engineer | Enrollment Ends Soon 
 How AI Fakes a Human in 5 Steps 
 How do you know if your AI app actually works? 
 Why Does Git Revert Cause Conflicts? 
 Claude Code vs. OpenClaw: 5 Design Dimensions 
 Claude Code terminates after every task. OpenClaw never sleeps. Both are highly capable, but they have key architectural differences. 
 System Scope 
 Claude Code is a short-lived process. You launch it, it runs, it exits. OpenClaw is a long-running background daemon with a Gateway that holds open WebSocket connections to apps like Discord, Slack, and WhatsApp. 
 Agent Runtime 
 Claude Code uses a single async query loop: think, tool call, observe, repeat. OpenClaw uses per-session queues, where the Gateway routes RPCs into separate queues. 
 Extension Architecture 
 Claude Code supports MCP, plug, skill, and hook, all wired into the agent. OpenClaw uses a manifest-first plugin system. Plugins flow through a central registry before reaching the Agent. 
 Memory 
 Claude Code treats CLAUDE. md as memory. OpenClaw separates MEMORY. md from daily notes and adds hybrid vector/keyword search across structured sections. 
 Multi-agent & Routing 
 Claude Code uses a lead-to-subagent pattern. OpenClaw uses a route-and-delegate system where inbound channels get routed to dedicated agents that hand off to shared subagents. 
 Over to you: which pattern do you think is the future of agents? 
 Become an AI Engineer | Enrollment Ends Soon 
 Our 6th cohort of Becoming an AI Engineer starts in about a week. This is a live, cohort-based course created in collaboration with best-selling author Ali Aminian and published by ByteByteGo. 
 Check it out Here 
 Here’s what makes this cohort special: 
 Learn by doing: Build real world AI applications, not just by watching videos. 
 Structured, systematic learning path: Follow a carefully designed curriculum that takes you step by step, from fundamentals to advanced topics. 
 Live feedback and mentorship: Get direct feedback from instructors and peers. 
 Community driven: Learning alone is hard. Learning with a community is easy! 
 We are focused on skill building, not just theory or passive learning. Our goal is for every participant to walk away with a strong foundation for building AI systems. 
 If you want to start learning AI from scratch, this is the perfect platform for you to begin. 
 Check it out Here 
 How AI Fakes a Human in 5 Steps 
 One selfie in, one fake video out. Here's how deepfakes work at a high level. 
 The diagram below shows the full pipeline that turns a reference image like selfie, a voice clip, and a prompt into a fake video. 
 Step 1: Prompt Refinement. The text prompt gets cleaned, augmented with extra detail, and paired with a negative prompt to suppress unwanted artifacts like distorted hands. 
 Step 2: Reference Image Prep. A single selfie of the target is passed through a VAE encoder, a neural network that compresses images into a compact latent representation. 
 Step 3: Diffusion Inference Engine. Starts from pure noise and runs a diffusion-based denoiser, conditioned on the refined prompt, reference latent, and audio to produce clean video latents. A VAE decoder then converts those latents back into video frames. 
 Step 4: Post-Processing. The raw frames are upscaled to higher resolution, color-corrected for consistency, screened by an NSFW classifier, and stamped with a watermark. 
 Step 5: Multimodal Syncer. Audio is converted to phonemes (the distinct sound units of speech). A lip-sync model aligns mouth movements to those phonemes. 
 The output is a video of a CEO who never said those words, in a room they never entered. 
 Over to you: What do you look for to figure out if a video's real or made by AI? 
 How do you know if your AI app actually works? 
 You evaluate it. But most teams skip this step (or do it wrong) because "eval" feels vague. It's not. 
 Every good eval is a 3-step recipe. 
 Step 1: Pick a task. AI systems have different capabilities and dimensions to evaluate. For LLMs, it can be safety or math capability, in RAGs it can be grounding and retrieval, Pick one. 
 Step 2: Collect eval data. For every task, gather inputs paired with the right answer or expected behavior. A safety set pairs risky prompts with "refuse." 
 Step 3: Develop a grader. How do you decide if the output is good? 
 Use code-based graders (if/else, unit tests) for things with a clear correct answer and patch passing unit-tests. 
 Use model-based graders (LLM-as-judge) for subjective tasks like safety. 
 Use human graders for edge cases and anything where nuance matters more than throughput. 
 Most production evals combine all three. Code-based for what's cheap to check. Model-based for scale. Human-based for what matters most. 
 Over to you: what's the hardest thing about your task to grade, and which grader type do you use for it? 
 Why Does Git Revert Cause Conflicts? 
 git revert looks straightforward until it throws a conflict. Here's why that happens. 
 What git revert actually does: Unlike reset, a revert doesn’t rewrite history. Instead, it creates a new commit that undoes the changes from an earlier one. This keeps your history clean, traceable, and safe for shared branches. 
 Why revert conflicts happen: Conflicts appear when a later commit changed the same lines as the commit you're trying to undo. 
 Example in the diagram: 
 Commit C2 added a feature 
 Commit C3 changed those same lines 
 Reverting C2 now collides with changes from C3 
 Git can’t know which version is correct, so a revert conflict is triggered. 
 How to resolve it: 
 1. Run git revert C2 
 2. Git pauses when it hits the conflict 
 3. You manually fix the file 
 4. Stage it 
 5. Continue the revert 
 Git then creates a new commit that cleanly undoes C2 while keeping C3 intact. 
 Over to you: Have you ever hit a revert conflict at the worst possible moment? How did you resolve it?
```

---

## 2. Become an AI Engineer | Enrollment Ends Soon

- 日期: 2026-05-08 15:31
- 链接: https://blog.bytebytego.com/p/enrollment-ends-soon-become-an-ai

```
Our 6th cohort of Becoming an AI Engineer starts in about a week. This is a live, cohort-based course created in collaboration with best-selling author Ali Aminian and published by ByteByteGo. 
 Check it out Here 
 Here’s what makes this cohort special: 
 Learn by doing: Build real world AI applications, not just by watching videos. 
 Structured, systematic learning path: Follow a carefully designed curriculum that takes you step by step, from fundamentals to advanced topics. 
 Live feedback and mentorship: Get direct feedback from instructors and peers. 
 Community driven: Learning alone is hard. Learning with a community is easy! 
 We are focused on skill building, not just theory or passive learning. Our goal is for every participant to walk away with a strong foundation for building AI systems. 
 If you want to start learning AI from scratch, this is the perfect platform for you to begin. 
 Check it out Here
```

---

## 3. Container Design Patterns for Distributed Systems

- 日期: 2026-05-07 15:31
- 链接: https://blog.bytebytego.com/p/container-design-patterns-for-distributed

```
For most of their life, containers have been considered more as a deployment concern. Package your code with its dependencies, ship it as one unit, and run it the same way everywhere. 
 That story was true, and it was also pretty useful, but it’s just one half of what containers were good for. The other half is what happens when we stop thinking of a container as a way to deliver one application and start thinking of it as a building block we can compose with others. 
 Software engineering has been here before. In the 1990s, object-oriented programming gave application code a clean boundary we could compose against. Out of that boundary came design patterns, the small library of standard solutions every working programmer eventually internalizes. With containers, distributed systems have gone through the same transition. 
 In this article, we’ll walk through the patterns that have crystallized over the past decade, organized by the scope of their coordination. Three of them describe how containers cooperate when they share a single machine. The other three describe how containers coordinate when the work spans many machines. None of these patterns is a rule. They’re answers to problems that distributed-systems engineers kept solving over and over. 
 The Abstraction Layer 
 Read more
```

---

## 4. How Instacart Built a Search for Billions of Products

- 日期: 2026-05-05 15:31
- 链接: https://blog.bytebytego.com/p/how-instacart-built-a-search-for

```
New Year, New Metrics: Evaluating AI Search in the Agentic Era (Sponsored) 
 Most teams pick a search provider by running a few test queries and hoping for the best – a recipe for hallucinations and unpredictable failures. This technical guide from You.com gives you access to an exact framework to evaluate AI search and retrieval. 
 What you’ll get: 
 A four-phase framework for evaluating AI search 
 How to build a golden set of queries that predicts real-world performance 
 Metrics and code for measuring accuracy 
 Go from “looks good” to proven quality. 
 Learn how to run an eval 
 In 2021, the Instacart search team faced a problem they could trace to their users’ typing habits. One group of shoppers searched for items like “pesto pasta sauce 8oz” and expected the exact product to appear. Another group searched for things like “healthy foods” and expected the system to understand what they meant. These are genuinely different problems. The first asks for precise keyword matching. The second asks the system to grasp intent from vague language. 
 Solving both required two different retrieval systems running in parallel. One handled keyword search. The other handled semantic search, where meaning rather than exact words drives the result. The setup worked, and for a while it worked well. But maintaining two systems in sync, blending their results into a single ranked list, and keeping both fast enough for millions of daily queries became a tax that grew heavier each quarter. 
 In this article, we will learn how Instacart’s search infrastructure evolved over the years and the challenges its engineering team faced. 
 Disclaimer: This post is based on publicly shared details from the Instacart Engineering Team. Please comment if you notice any inaccuracies. 
 The Shape of Search at Instacart 
 Before looking at the technical choices, it helps to understand the workload Instacart’s search has to serve. A catalog with billions of items stretches across thousands of retailers. The system handles millions of search requests every day, with query volume swinging widely from hour to hour. 
 What makes their problem genuinely unusual is the write side. Grocery items are fast-moving goods. Prices shift multiple times a day. Inventory availability changes as shelves empty and restock. Discounts come and go. As a result, the search database receives billions of writes per day. Those writes include catalog changes, pricing updates, availability data, ancillary tables for ranking and display, personalization signals, and replacement product data. 
 This combination is crucial. In most search problems, you index once, maybe refresh occasionally, and queries run against a mostly stable dataset. Instacart’s situation inverts this. Their data changes constantly, and every change has to show up in search results within seconds. 
 Two terms that we should know are precision and recall. Precision is the percentage of retrieved results that are actually relevant. Recall is the percentage of all relevant documents that the system manages to retrieve. A system with high precision returns mostly good results. A system with high recall catches most of the good results that exist. Tuning these tradeoffs is the core game of search, and the architecture determines how much control you have over each. 
 Agentic Fine-Tuning and Inference with Pioneer (Sponsored) 
 Fine-tuning open-source models manually is a slow, tedious task. 
 Pioneer is a fine-tuning agent that automates the entire process, allowing users to generate synthetic training data, perform LoRA and full fine-tuning runs, run custom evals, and deploy models to production through a chat interface or API. Once deployed, Pioneer autonomously diagnoses failures and retrains on live data in a continuous loop called adaptive inference. 
 Fastino Labs recently released a technical report evaluating Pioneer’s adaptive inference across eight benchmarks, achieving improvements of up to +83.8 percentage points over base models, with each run completing in 8-12 hours at $12–55. 
 Start fine-tuning for free 
 Leaving Elasticsearch Behind 
 Instacart’s original search was built on Elasticsearch, which was the industry-standard choice for full-text search at the time, and still is today. On paper, the fit looked ideal. Elasticsearch is purpose-built for keyword search at scale, uses a well-understood ranking algorithm called BM25, and has a mature ecosystem of tooling around it. 
 The fit broke down because of how Elasticsearch wants data structured. Elasticsearch prefers denormalized documents, meaning one record per item that bundles together every relevant field. When a user searches, Elasticsearch can return complete documents quickly because everything is already in one place. The catch is that when any single field changes, the entire document has to be rewritten and re-indexed. 
 For Instacart, this was catastrophic. A price change on a single product triggers a full document rewrite. Multiply that by billions of daily writes, and the indexing load becomes crushing. The system struggled so badly that fixing erroneous data could take days. Layering sophisticated ML features on top only made things worse, since those features also had to be indexed, further degrading read performance. 
 The team’s response was unusual. Instead of moving to a more specialized search tool, they moved the search into Postgres. This was counterintuitive, since Postgres is a general-purpose relational database, meaning it organizes data into tables with structured columns and relationships between them. The rationale was practical. Their catalog data already lived in Postgres, the team already had deep operational experience running it at scale, and Postgres supports full-text search through GIN indexes (a type of index optimized for searching inside composite values) and a ranking function called ts_rank. 
 The payoff was significant. A normalized data model, where prices, availability, and ML features live in separate joined tables instead of being stuffed into a single document, reduced their write workload by a factor of ten. Only the price table gets touched by a price change, leaving the rest of the system alone. They also gained the ability to store hundreds of gigabytes of ML features alongside documents, which unlocked more sophisticated retrieval models. 
 The lesson here is easy to miss. Elasticsearch is an excellent tool. For read-heavy, append-only workloads like log analytics, it remains the right choice. The problem was the mismatch between Elasticsearch’s data model assumptions and Instacart’s write patterns. 
 Semantic Search and the Two-System Problem 
 Consolidating text search onto Postgres solved the indexing problem, but it left a different gap. A search for “pesto pasta sauce 8oz” is a straightforward matching exercise. The words are specific, the match criteria are clear, and the keyword search handles it beautifully. Ambiguous queries are where keyword search hits its ceiling. When someone searches for “healthy foods,” the query words and the product titles barely overlap. You want results that match the meaning of the query, since exact word matching falls short here. 
 This is where semantic search enters the picture. The idea is to convert text into vectors, which are simply lists of numbers (typically a few hundred long), so that texts with similar meanings end up with similar vectors. Once you have vectors for every product and for the query, finding relevant results becomes a geometry problem. You look for vectors near the query vector in this numerical space. This lookup is called approximate nearest neighbor search, or ANN. Clever index structures let ANN find close matches quickly, rather than comparing every single vector in the database against the query. 
 In 2021, Instacart added semantic search to its stack. Since Postgres at the time had yet to gain native ANN support, they built a standalone service using FAISS, a vector search library from Meta. For every incoming query, the system made parallel calls. One call went to Postgres for keyword retrieval. The other went to the FAISS service for semantic retrieval. The application layer merged the two result sets using a weighted ranking step, then passed the top candidates onward to downstream ranking stages that score and order results before they reach the user. 
 The architecture worked, and search quality improved significantly. Still, three real problems emerged: 
 First, FAISS had limited support for filtering by document attributes at retrieval time, so the system had to overfetch documents and filter them afterward. This meant some genuinely relevant items got dropped before they reached ranking. 
 Second, maintaining two separate services created developmental and operational overhead, along with subtle data inconsistencies from keeping them in sync. 
 Third, the split architecture constrained how intelligently the team could combine signals from the two retrievers. 
 The 2021 choice was correct for its moment. Postgres-based vector search was still immature then, and FAISS was the right tool for the circumstances. Architectures expire, though, and this one was reaching its shelf life. 
 Putting It All Back Together with pgvector 
 As the tradeoffs of the split architecture became more visible, the team started looking for a unified alternative. Two broad paths were available: 
 The first kept specialized datastores for vectors and text, combining results in the application layer. This is the path most new companies take, since managed vector databases like Pinecone are easy to adopt. 
 The second used semantic search support inside an existing text search datastore. For Postgres, this meant pgvector, an extension that teaches Postgres to store and search over vectors. 
 Instacart chose the second path, following the same reasoning as before. Text search already lived in Postgres, the team already operated Postgres at scale, and pgvector had matured enough for serious production workloads. Co-locating vectors with relational data unlocked something new. The system could use real-time inventory as a filter applied before the semantic search ran, rather than after. 
 Before committing, the team built a lab-scale prototype cluster that mimicked production traffic. The prototype confirmed that pgvector could meet their throughput and latency requirements, with better recall than FAISS and only marginally slower speeds on the largest retailers. One honest finding deserves mention. The team tested whether tuning index parameters per retailer catalog size would help and found it offered little benefit. Sometimes the clever optimization simply falls flat. 
 A small simplification came out of the migration as well. In the FAISS era, Instacart maintained a separate vector index for every retailer, adding up to hundreds of indexes to operate. With pgvector, they built hybrid indexes grouped by retailer characteristics, dramatically reducing the operational surface area. 
 The production results were what mattered. An A/B test against real traffic showed a 6 percent drop in searches that returned zero results, driven by improved recall. That single number is the entire business case for the migration. Every zero-result search is a customer who bounced, gave up, or switched apps. Recovering 6 percent of those interactions translated directly into incremental revenue. 
 The deeper unlock was attribute filtering. With availability data living in the same database as the vectors, Postgres could filter for in-stock items before the ANN search ran, rather than fetching extras and discarding sold-out items afterward. The split architecture made this kind of pre-filter practically impossible. Consolidation made it simple. 
 Bring the Compute to the Data 
 The consolidated Postgres architecture made search roughly twice as fast. This speedup deserves attention because of where it came from. The cause was simpler than a new algorithm or faster hardware. Algorithms stayed the same. Hardware stayed the same. What changed was the location of the work. 
 Here is what the old architecture did on every search request. The application layer made a network call to Elasticsearch for text results. It made separate network calls to other services, including the item availability data service, to gather the rest of the context. It joined the data in memory, applied filters, and assembled the final result set. Every request paid the cost of multiple round-trip, overfetching, and application-layer joining. 
 The new architecture pushed all of that work into Postgres. Availability data, ML features, ranking tables, and search indexes now live together in one database. A single query could retrieve search matches, join them against availability and other attributes, and filter the result set before sending anything back to the application. The flow needed a single round trip, with zero overfetching and zero in-memory joining. 
 Why does this matter? 
 Every network hop adds latency. Every application-layer join forces to fetch extra data you will throw away. Moving the computation into the same place as the data eliminates both costs. This is the principle. Bring the compute to the data, and whenever feasible, avoid the reverse. 
 The industry-wide trend over the past decade has actually gone the other direction. Systems like Snowflake and BigQuery deliberately separate compute from storage so they can scale each independently. For elastic, bursty analytical workloads, that design makes sense. For latency-sensitive operational workloads like search, the reverse design wins. 
 The Limits of This Approach 
 The Instacart approach is powerful, and it also has real limits. 
 The tool pgvector handles workloads well up to roughly 50 to 100 million vectors per index. Beyond that, purpose-built vector databases scale more gracefully. Instacart stays within this ceiling by structuring indexes per retailer, keeping individual index sizes manageable even as the total catalog runs into the billions. 
 Workload fit is the other big caveat. Their approach made sense because their data already lived in Postgres, because their team had deep Postgres operational expertise, and because their write workload suited a normalized relational model. A startup with a greenfield system, a read-heavy workload, and a small team might rationally choose a managed vector database like Pinecone. Those teams would be right to do so. 
 Consolidation is itself a bet. Putting everything in one database means every workload shares the same cluster. Analytical queries, search queries, and transactional writes compete for the same resources, which can create noisy-neighbor problems when the workload balance shifts. 
 The 2x latency improvement and 10x write reduction belong to Instacart’s workload. Your system will show its own numbers. The principles, though, travel well. 
 Conclusion 
 Instacart’s story covers four stages of architecture, each correct at its moment and each eventually needing to be replaced. 
 When we hear that a specialized tool fits a specialized job, it might not fit every possible scenario. In case of two systems running in sync, measure the real cost of that sync. It is almost always higher than it looks. When your application keeps pulling data in, joining it, and filtering most of it away, ask whether the work belongs closer to the data. 
 Architecture is a sequence, made one decision at a time. 
 References: 
 How Instacart Built a Modern Search Infrastructure on Postgres 
 What is Elasticsearch
```

---

## 5. Connecting LLMs to the Real World: Tool Use, Function Calling, and MCP

- 日期: 2026-05-04 15:30
- 链接: https://blog.bytebytego.com/p/connecting-llms-to-the-real-world

```
@Sentry in your Slack, fix your bug (Sponsored) 
 Debugging in production means either digging through your telemetry or pasting a stack trace into an LLM that can’t see what actually happened. 
 Sentry already has that context -- every error, trace, log, replay, and profile from your application. Seer is the AI layer that reasons over all of it to automate debugging. 
 Next time something’s not quite right, describe what you’re seeing and Seer Agent investigates across your full telemetry to tell you what’s going on and why. 
 Click ‘Ask Seer’ in Sentry to try it, or mention @Sentry in Slack to start debugging. 
 Try Sentry's Seer Agent 
 LLMs can search the web, pull up your calendar, book reservations, and send emails on your behalf. From the user’s perspective, it seems like typing a request, and the thing just happens. 
 There is, however, a lot happening underneath to make this work. 
 The model needs to know which tools are available, how to request them, and what to do with the results. The software surrounding the model needs to figure out what it actually wants, execute it safely, and feed the answer back. 
 Getting all of this right took several iterations, a couple of failed experiments, and eventually an open protocol that every major AI company is now adopting. 
 In this article, we will look at this progression that has happened from basic tool use to function calling to the Model Context Protocol, allowing the LLMs to go from isolated text generation tools to assistants that can do interesting stuff for the end users. 
 Why LLMs Cannot Act on Their Own 
 To understand why connecting LLMs to external systems is an interesting engineering problem, it helps to understand what an LLM actually does. 
 At their core, large language models are text-prediction engines. They take text in and produce text out. They are extraordinarily good at this. In fact, so good that the output often looks like real reasoning, but the underlying mechanism is always the same: predict the next token based on everything that came before. 
 This means an LLM has no built-in ability to call an API, query a database, or perform any action in the real world. Ask it “What’s the weather in Tokyo right now?” and it can give a plausible-sounding answer based on patterns in its training data, but it cannot actually check. It has no network access. It has no way to reach outside the boundaries of its own context window, the finite amount of text it can consider at once. 
 This is a direct result of what the technology is at its core. But it creates an obvious question: if LLMs can only generate text, how do applications like ChatGPT, Claude, and Gemini end up doing things like searching the web, sending emails, or pulling data from internal systems? 
 The answer is that the LLM itself doesn’t perform those actions directly. Each of these products has an application layer, the surrounding software infrastructure, built around the model. That layer lets the model request actions. When ChatGPT searches the web, the model generates a structured request saying “search for X,” and OpenAI’s application infrastructure carries out the actual search and returns the results. The same pattern holds for Claude, Gemini, and any other AI assistant with tool access. 
 In short, the model reasons about what needs to happen, and the surrounding software makes it happen. 
 How Tool Use and Function Calling Work 
 When an LLM-powered application supports tool use, the model receives a menu of available functions alongside each user prompt. 
 Each function is described with a name, a purpose, and the parameters it accepts, typically defined as a JSON schema (a structured format that specifies what inputs the function expects and what types they should be). When the model encounters a question it cannot answer from its training data alone, it can respond not with a final answer, but with a structured request asking for a specific function to be called with specific arguments. 
 Here are the steps: 
 The model generates this request as structured text, usually JSON. It does not execute the function itself. 
 The application layer receives that structured output, validates it, and actually runs the function (hits a weather API, queries a database, sends an email). 
 It sends the result back to the model as a new message. 
 The model then uses that result to compose its final response to the user. 
 For example, a user asks the application, “What’s the weather in Tokyo?” 
 The model has a tool called get_weather available, which accepts a location parameter. Rather than guessing, the model generates something like {”function”: “get_weather”, “arguments”: {”location”: “Tokyo”}}. 
 The application layer receives this, calls a real weather API, gets back “22°C, partly cloudy,” and sends that data to the model. The model then responds with a natural language answer grounded in real-time data. 
 This back-and-forth is called the agentic loop, as shown in the diagram below: 
 This loop can also run for multiple rounds, with the model calling several tools in sequence to fulfill a single request. For example, a user saying “find me flights to Tokyo and check the weather there” might trigger a flight search tool call first, then a weather tool call, with the model synthesizing both results into a single response. This multi-step looping is the foundation of AI agents that are systems where the model autonomously plans and executes complex tasks. 
 The separation between the model deciding what should happen and the application layer actually doing it has some advantages. The application can restrict which functions the model has access to, validate arguments before executing anything, and require human approval for high-stakes actions like transferring money or deleting data. 
 This mechanism, formalized as “function calling” or “tool calling,” became widely available in mid-2023 when OpenAI added it as a first-class API feature. 
 Just a few months earlier, OpenAI had launched ChatGPT Plugins, which let third-party developers expose arbitrary APIs to ChatGPT. However, discovery was difficult, plugin quality varied wildly, and the security model was not mature enough to handle untrusted third-party tools interacting with a language model. OpenAI deprecated plugins entirely by April 2024, moving to the more controlled function-calling approach where developers explicitly define the tools the model can use. 
 See the timeline of evolution as below: 
 Function calling worked, but it introduced a new problem. Every LLM provider implemented it differently. OpenAI had one schema format, Anthropic had another, and Google had its own. A tool built for one provider’s API wouldn’t work with another without rewriting the integration code. For developers who wanted their tools to work across multiple LLMs, or who wanted flexibility to switch providers, this fragmentation was a genuine obstacle. 
 The Model Context Protocol (MCP) 
 The fragmentation problem gets worse as the ecosystem grows. 
 For example, iff there are 3 LLM providers and 5 tools to integrate, there are 15 possible custom integrations, one for each provider-tool combination. Add a sixth tool, and 3 more integrations are needed. Add a fourth provider and 5 more. The total grows as the product of providers times tools. This is called the N×M problem, and it becomes unmanageable quickly. 
 The Model Context Protocol was designed to solve exactly this. 
 Introduced by Anthropic as an open standard, MCP defines a common protocol that both LLM applications and tool providers can implement once. Each LLM client implements MCP once. Each tool server implements MCP once. The total number of integrations drops from N×M to N+M. Three providers plus five tools equals 8 implementations instead of 15. 
 MCP works through a client-server architecture with three components. 
 An MCP Host is the AI application a user interacts with, something like Claude Desktop or an AI-powered IDE. 
 Inside the host lives an MCP Client, which handles communication with external tool providers. 
 On the other side, MCP Servers are lightweight programs that wrap around existing tools, databases, or APIs and expose them in MCP’s standard format. 
 When the host starts up, its client connects to available MCP servers and asks each one to describe its capabilities. Those descriptions get fed to the model, and from there, the familiar function calling mechanism takes over. 
 The model sees the available tools, generates structured requests when it needs them, and the MCP infrastructure routes each request to the right server and returns the result. 
 Beyond tools, MCP servers can also surface resources (data the model can read, like files or database records) and prompt templates, though tools remain the core capability driving most adoption today. 
 See the diagram below that shows a typical request flow using MCP: 
 MCP does not replace function calling. Function calling is the mechanism by which the model signals it wants to use a tool. MCP standardizes how those tools are described, discovered, and invoked so that the same tool works with any model that speaks the protocol. 
 In other words, they are complementary layers solving different parts of the same problem. The model doesn’t know or care whether MCP is involved behind the scenes. It sees a list of tool definitions and generates calls against them, the same way it always has. 
 Adoption has been remarkably fast. 
 In 2025, OpenAI announced MCP support across its products. Google DeepMind confirmed support for Gemini shortly after. By late 2025, over 10,000 publicly available MCP servers were listed in online directories. At the end of 2025, Anthropic donated the protocol to the newly formed Agentic AI Foundation under the Linux Foundation, co-founded by Anthropic, Block, and OpenAI, with support from AWS, Google, Microsoft, Cloudflare, and Bloomberg. What started as an open-source experiment became an industry standard in roughly a year. 
 The Costs and Tradeoffs of Tool Use 
 That rapid growth, however, has surfaced real costs and risks that are important to understand. 
 The most significant is security. Every tool exposed to an LLM expands the system’s attack surface. In September 2025, this became concrete. A developer published an npm package that looked like an official email integration for MCP, mimicking the name and structure of a legitimate library from Postmark, a well-known email service. Hundreds of developers installed it. Later, it was found that a hidden code in the package was silently forwarding copies of every outgoing email to the attacker. This was a supply chain attack, where malicious code is hidden inside a dependency that looks trustworthy, and it was described as the first such attack targeting MCP servers. 
 Security challenges go beyond individual attacks. The protocol initially prioritized ease of adoption over robust security, and the authentication specifications went through multiple revisions as the community worked to close gaps. This is a familiar pattern in technology standards: interoperability and adoption come first, and security matures with time. The MCP specification continues to evolve, with recent revisions addressing authentication, server identity, and governance. 
 Beyond security, there is a subtler cost. Every tool definition exposed to the model consumes tokens in the context window. The name, description, and parameter schema of each tool all occupy space in the same finite context that holds the conversation history and task instructions. A handful of tools creates negligible overhead. Dozens or hundreds start crowding out the room the model needs to reason about the task. An agent with access to hundreds of tools sounds powerful in theory, but in practice, each additional tool slightly degrades the model’s ability to focus on the actual problem. 
 Tool use also does not make LLMs deterministic. The model can still hallucinate function names, pass malformed arguments, or chain tools in unexpected ways. Validation, error handling, and human approval steps are essential parts of any production system that gives an LLM access to real-world capabilities. 
 Conclusion 
 LLMs started as isolated text predictors, powerful but unable to interact with external systems. 
 Function calling gave them a structured way to request actions while keeping execution in the hands of the surrounding application. MCP standardized how tools are described and discovered, so that integrations work across providers without custom code for every combination. 
 Through all of these layers, however, one principle remains constant. The model reasons about what should happen, and the application layer controls whether it actually does. That boundary is where security, reliability, and control are designed in. 
 The space is moving fast. MCP went from launch to industry-wide standard in roughly a year. But the core concepts covered here, tool definitions, the agentic loop, the separation of reasoning from execution, and the tradeoffs that come with expanding what an LLM can reach, are ideas that will transfer regardless of which framework, provider, or protocol version ends up being used. 
 References: 
 Function calling and other API updates by OpenAI 
 OpenAI ChatGPT plugins 
 Introducing the Model Context Protocol 
 New tools for building agents 
 Model Context Protocol 
 Donating the Model Context Protocol and establishing the Agentic AI Foundation 
 First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package
```

---

## 6. EP213: MCP vs Skills, Clearly Explained

- 日期: 2026-05-02 15:30
- 链接: https://blog.bytebytego.com/p/ep213-mcp-vs-skills-clearly-explained

```
Over 80% of container spend is wasted. Here’s how to fix it. (Sponsored) 
 Many teams over-provision containers, underuse spot instances, and have no visibility into which pods are burning budget. Get the eBook from Datadog, which covers five practical optimizations for Kubernetes and ECS environments with specific techniques your team can apply today. 
 You’ll learn how to: 
 Pinpoint idle containers, over-provisioned pods, and unused clusters draining your cloud budget. 
 Right-size CPU and memory with resource requests, limits, and automated cost recommendations. 
 Cut costs up to 90% with spot instances and savings plans and know exactly when to use each 
 Get the eBook 
 This week’s system design refresher: 
 Why Everyone Should Know About AI Evals: The Fundamentals Explained (Youtube video) 
 MCP vs Skills, Clearly Explained 
 5 Way to Defend Prompt Injection 
 How the X Algorithm Works 
 Why Everyone Should Know About AI Evals: The Fundamentals Explained 
 MCP vs Skills, Clearly Explained 
 Both MCP and Skills extend what an agent can do. But they solve different problems, and picking the wrong one adds cost or complexity you don't need. 
 The diagram breaks down the five dimensions that matter. 
 Integration: MCP is a client-server protocol that connects N agents to M backends through one interface. Agent Skills are folders with a SKILL. md that the agent loads on trigger. 
 Architecture: MCP runs as a separate process with its own runtime, speaking JSON-RPC. A Skill is just a directory: SKILL. md, optional scripts, references, and assets. 
 Invocation: MCP tools are called with typed parameters validated against a schema, and can be chained. Skills are invoked by the agent reading SKILL. md and running whatever commands it describes like bash, python, or curl. 
 Runtime: MCP servers often run in their own container or service. Skills run in the agent's own environment with no extra infra. 
 Where it fits: Use MCP to connect agents to live systems and data. Use Skills to give agents reusable know-how and instructions. 
 Over to you: What's the most interesting Skill you've come across recently? 
 IaCConf 2026: AI, IaC, and platform engineering (Sponsored) 
 It’s 2026. Platform engineering is shifting. Your users aren’t just developers anymore. They’re AI agents. Plan for it. 
 Join IaCConf 2026 to hear from the people building this sh*ft. Hear from Corey Quinn on “AI Speaks Terraform Like a Tourist,” Matt Gowie on the move from IaC to agents, and Amin Astaneh on 10x code velocity and operational risk. 
 Plus: how teams replace Terraform workflows with policy-driven automation, deploy AI agents safely, and scale infrastructure with GitOps and Kubernetes. 
 Join IaCConf 2026, a free virtual event on May 14. 
 Register Now 
 5 Way to Defend Prompt Injection 
 Prompt injection tops the OWASP LLM Top 10 and there's no single fix. 
 Instead, you stack defenses, each one catching what the others miss. 
 Defenses come in two families: model-level and system-level. 
 Model-level defenses teach the model to resist injection. 
 Spotlighting wraps untrusted text in control tags like <UNTRUSTED>...</UNTRUSTED> and tells the model to treat anything inside as data, not instructions. 
 Instruction Hierarchy fine-tunes the model to rank the developer's system prompt above the user's message, and both above third-party content. 
 System-level defenses build a system around the LLM that bounds the damage. 
 Least-Privilege Tools: Give the agent the minimum tools it needs. 
 Human-in-the-Loop: Require explicit user approval before any sensitive action runs. 
 Planner / Executor Split: Two separate LLMs. The planner has tool access but never sees untrusted content. The executor reads untrusted content but has no tools. 
 No single defense is enough. Production systems like Gmail stack them, and together they make indirect injection manageable. 
 Over to you: what's the one defense you've seen work in production that isn't on this list? 
 How the X Algorithm Works 
 Here are the key steps: 
 Everything starts with a Feed Request. 
 The Home Mixer, the system’s orchestration layer, kicks things off by pulling your engagement history and preferences through Query Hydration. 
 Next, it gathers candidate posts from two sources: Thunder (posts from accounts you follow) and Phoenix Retrieval (posts from accounts you don’t follow, discovered through ML) 
 These candidates get enriched with metadata like author info and media details during Hydration, then pass through Filtering, which removes duplicates, old posts, blocked authors, and muted keywords. 
 Then comes scoring. A Grok-based transformer predicts engagement, a Weighted Scorer combines those predictions, and an Author Diversity Scorer prevents any single account from dominating your feed. 
 Top-scoring posts are selected, go through a final visibility filter, and become your Ranked Feed. 
 Over to you: What else will you add to the list of steps? 
 Disclaimer: This post is based on the publicly shared GitHub repo of the X algorithm by xAI
```

---

## 7. A Beginner’s Guide to Kubernetes

- 日期: 2026-04-30 15:31
- 链接: https://blog.bytebytego.com/p/a-beginners-guide-to-kubernetes

```
Think about the difference between leaving a housemate a to-do list and writing them a contract. The to-do list says “buy bread on Monday, take out the bins Tuesday, water the plants Wednesday.” 
 It’s a sequence of instructions, and if any step fails or gets skipped, the whole thing fails. The contract says something different. It says the kitchen should always have bread, the bins should never overflow, and the plants should never go three days without water. One is a script. The other is a promise, and somebody has to keep checking whether the promise is being kept. 
 Kubernetes is what we get when that second approach is taken seriously and built into a whole infrastructure platform. 
 In this article, we will learn how Kubernetes is a system of promises, and that every piece of it is a small program keeping one of those promises. 
 The Kubernetes Approach 
 Read more
```

---

## 8. The Tech Stack Powering Wise

- 日期: 2026-04-29 15:31
- 链接: https://blog.bytebytego.com/p/the-tech-stack-powering-wise

```
AI inference: 24,240 TPS vs 1,863 TPS H100 (Sponsored) 
 Most teams optimize models. Few optimize inference. We benchmarked NVIDIA RTX PRO 6000 Blackwell on Akamai Cloud against H100 using real LLM workloads. 
 At 100 concurrent requests, Blackwell reached 24,240 tokens/sec per server, compared to 1,863 TPS on H100. That’s up to 1.63× higher throughput, with additional gains from FP4 precision. 
 The difference comes down to architecture. These GPUs run on a globally distributed platform built for real-time, latency-sensitive inference, not centralized batch jobs. 
 If you're building agentic systems or high-concurrency AI apps, infrastructure choices matter as much as model selection. See the full setup, methodology, and results. View benchmark results 
 View Benchmark results 
 In 2024, Wise’s deployment system automatically blocked hundreds of releases that would have caused production incidents. 
 There was no human intervention, but the system routed just 5% of traffic to the new version, watched technical and business metrics for 30 minutes, and rolled back when it detected anomalies. Three years earlier, Wise was deploying with a simpler in-house tool that treated each release as a basic transaction, where the process was essentially to push the code and hope for the best. 
 This leap was made possible by some interesting engineering decisions that we will learn about in this article. 
 For reference, Wise moves about £36 billion across borders every quarter, with 65% of transfers arriving instantly. One might assume that kind of reliability requires a tightly controlled, top-down engineering organization. However, the opposite is true. 
 Wise has 850+ engineers organized into autonomous squads, each empowered to make their own technical decisions. The reason this works, and the reason it would collapse without a very specific set of infrastructure investments, is the real engineering story behind Wise. 
 Behind the product that 15.6 million active customers interact with, there are over 1000 microservices, 700+ Java repositories, 40 web applications, and native iOS and Android apps with hundreds of modules each. What holds all of this together is an internal platform, a set of shared tools, frameworks, and automated systems that make the right engineering choice the easy one. 
 Disclaimer: This post is based on publicly shared details from the Wise Engineering Team. Please comment if you notice any inaccuracies. 
 Standardizing the Starting Point 
 When a system has 1000+ services owned by dozens of independent teams, the most dangerous form of complexity is inconsistency. If every team wires up security, database connections, Kafka consumers, and logging differently, you end up with 1000 slightly different systems that are all hard to debug, upgrade, and secure. 
 Wise’s answer to this is a microservice chassis framework, an opinionated, pre-configured foundation that every new backend service can start from. The chassis handles security, observability, database communication, Kafka integration, and more, all with recommended defaults so that teams can focus on business logic rather than plumbing. 
 What makes Wise’s approach distinct is that the chassis is shipped as a versioned artifact rather than a template you fork and modify. 
 The difference matters. With a template, the service diverges from the standard the moment you create it. With an artifact dependency, updates to the chassis flow downstream when teams bump the version. Security patches, observability improvements, and new defaults reach services through a regular dependency upgrade rather than a manual migration. 
 This approach also extends to the build pipeline. 
 Wise built a collection of in-house Gradle plugins, including one that standardizes GitHub Actions workflows. When Wise decided to roll out SLSA (a framework for protecting software supply-chain integrity) across the organization, it became a plugin version update across 700+ Java repositories rather than 700 individual pull requests. 
 On top of this, a language-agnostic automation service can make complex changes across the codebase at scale and create pull requests for the owning team to review. Dependency upgrades for Java services are now fully automated through this system. 
 The same standardization mindset shows up on the frontend. 
 Wise’s web applications are built on CRAB, a Wise-specific abstraction on top of Next.js, split across 40 distinct apps that handle specific product functions. Visual regression testing is handled by Storybook paired with Chromatic, which captures snapshots of React components after each change and highlights visual differences to catch UI bugs before they reach customers. 
 Shipping Code Safely 
 Standardizing how services are built is only half the problem. The other half is standardizing how they reach production. 
 Since 2018, Wise has relied on Kubernetes to host its services, originally built with Terraform, JSONNET, and ConcourseCI. That setup supported service-mesh controls through Envoy, PCI-DSS compliance, and frictionless deployments for several years. 
 But as Wise grew, the original approach could not scale further without becoming a maintenance burden. This led to the Compute Runtime Platform (CRP), a ground-up rebuild of Wise’s Kubernetes infrastructure. Terraform still provisions infrastructure, but the codebase was rewritten from scratch for flexibility. RKE2 now handles cluster bootstrapping, with Rancher managing overall cluster state. Helm replaced JSONNET for better maintainability and upstream compatibility. ArgoCD with custom plugins ensures fully automated provisioning and consistency across environments. The result is that Wise grew from 6 Kubernetes clusters to more than 20 while keeping maintenance manageable. 
 Source: Wise Engineering Blog 
 CRP also brought efficiency improvements: 
 Automated container CPU rightsizing through Vertical Pod Autoscaler is now live in non-production and rolling out to production for non-critical workloads. 
 Horizontal scaling through KEDA optimizes workloads based on daily and weekly traffic patterns. 
 Fully managed sidecar containers like the Envoy proxy simplify deployments for product teams, and Wise’s Envoy-powered service proxy now includes seamless integration and discovery between services. 
 All of this feeds into Wise’s broader Mission Zero cost optimization goals. 
 Wise’s deployment strategy has undergone a big shift with the transition from Octopus, their former in-house tool, to Spinnaker. This was more than a tool swap. 
 Octopus treats deployments as simple transactions, while Spinnaker treats them as orchestrated sequences of events with built-in canary analysis, metric validation, and automatic rollback. 
 See the diagram below: 
 The canary process is simple in concept but powerful in practice. 
 When a new version of a service is deployed, only 5% of traffic routes to it. Over a 30-minute window, the system analyzes both technical metrics (error rates, latency) and business metrics (transaction success rates, conversion). If it detects significant anomalies, it rolls back automatically. In 2024, this system prevented hundreds of potentially incident-causing deployments and saved thousands of engineering hours. Over half of Wise’s services already run on Spinnaker, with full migration expected by mid-2025. 
 On the CI side, migrating from CircleCI to GitHub Actions opened new optimization possibilities. By tracking detailed build metrics, Wise discovered that pre-populating caches for frequently used containers could slash build times by 15%. At their scale of 500,000 monthly builds, that translates to over 1,000 hours saved each month. Wise has also been methodically implementing the SLSA framework across build processes, strengthening supply-chain security one language at a time. 
 Mobile teams have seen similar gains. 
 iOS engineers migrated 250+ Xcode modules from Xcodegen to Tuist and switched from Cocoapods to Swift Package Manager, dropping zero-change build times from 28 seconds to 2 seconds. 
 On Android, the team manages over 300 Gradle modules and has fully moved to Jetpack Compose for UI, adopted Kotlin 2.0 and 2.1, and is exploring Kotlin Multiplatform for cross-platform code sharing. 
 Backend-for-frontend services (BFFs, which are lightweight backends tailored to a specific frontend’s needs) help share logic between Android, iOS, and web teams. 
 Connecting to Payment Rails 
 Fast, safe deployments matter even more at Wise than at most companies, because what those services are doing is moving real money through real banking systems around the world. 
 Wise connects directly to local payment schemes rather than routing through intermediary banks. They went live with InstaPay in the Philippines, were granted access to Zengin (Japan’s instant payments system), and received access to PIX in Brazil. Each of these integrations has different technical requirements, and some demand a physical data center presence in the country. 
 This creates an infrastructure consistency challenge. 
 Wise centralizes networking using AWS Transit Gateways, but the details of each integration vary substantially across their UK, Hungary, and Australia data center deployments. The Australian deployment is particularly interesting because it was one of the first deployments of AWS Outpost Servers, which allowed Wise to maintain consistent AWS tooling even inside a physical data center. 
 The goal is always to keep the infrastructure as uniform as possible so that teams working on payment integrations can focus on the business logic rather than wrestling with environment differences. 
 Wise also exposes this infrastructure through a public API, allowing banks, financial institutions, and enterprises to integrate cross-border payment services directly. For reference, the Wise Platform supports over 40 currencies and multiple payment routes, with OAuth authentication and built-in compliance features. 
 Data, ML, and AI 
 All of this money movement generates enormous volumes of data. Wise’s data architecture is built as a pipeline from movement to insight to action, with each layer feeding the next. 
 Keeping Data in Motion 
 Kafka underpins most of Wise’s real-time data movement, handling asynchronous messaging between services, log collection, and streaming updates for analytics. Their Kafka clusters have grown significantly, with features like rack-aware standby replicas for fault tolerance. 
 An in-house data movement service funnels information from Kafka and databases into destinations like Snowflake, S3 Parquet, and Apache Iceberg, with automated checks in the configuration process to reduce human error. 
 A separate Data Archives service now handles over 100 billion records across multiple databases, reducing storage costs and making backups faster. 
 Storing and Querying Data 
 Wise has migrated most MariaDB and Postgres workloads from self-hosted EC2 instances to Amazon RDS, and is moving from self-hosted MongoDB to MongoDB Atlas. Redis continues to handle in-memory workloads. 
 Source: Wise Engineering Blog 
 For analytics, Wise is building a data lake on Amazon S3 using Apache Iceberg, which allows modifying table structures without rewriting all the data. Trino serves as the federated query engine, letting teams query Iceberg tables, Snowflake, or Kafka streams from one place. A Trino gateway handles workload separation and fault-tolerant queries, while Airflow and dbt-core manage complex data workflows. 
 Data Governance 
 Wise has built a comprehensive inventory system and governance portal that tracks where data is stored, who created it, and how it is classified. 
 Automated data discovery feeds into data deletion, compliance, and audit initiatives. For a regulated financial services company, this is load-bearing infrastructure, and as more engineers join the governance effort, Wise is rolling out stricter policies, enhanced privacy checks, and automated data lifecycle management. 
 Machine Learning 
 Data scientists work in Amazon SageMaker Studio, with large-scale processing on Spark in EMR and orchestration through Airflow. 
 SageMaker Feature Store keeps hundreds of features in sync for training and inference, while MLflow tracks experiments, metrics, and model versions. When a model is ready for production, it is deployed through an in-house prediction service built on Ray Serve. 
 Source: Wise Engineering Blog 
 Applications span fraud detection, KYC verification, and customer onboarding, where every millisecond of inference time matters. Automated checks catch data drift and feature inconsistencies before they become serious issues. 
 AI and LLM Capabilities 
 Wise has built a secure gateway connecting to multiple LLM providers, including Anthropic (Claude), AWS Bedrock, Google Gemini, and OpenAI. This lets teams experiment with different models without managing separate credentials or compliance checks. 
 A Python library inspired by LangChain wraps these APIs to speed up prototyping. For cases requiring internal context, a custom Retrieval-Augmented Generation (RAG) service pulls the latest information from various data stores before generating responses, which is useful for summarizing complex documents and automating parts of customer service. 
 Unified Observability 
 Building all of this is one challenge. Knowing whether it is working is another. 
 Wise has consolidated its observability stack onto the LGTM stack from Grafana. Loki handles logs, Grafana provides dashboards, Tempo handles traces, and Mimir handles metrics. The migration from Thanos to Mimir was driven by scalability needs, and the metrics stack now ingests roughly 6 million metric samples per second and processes 150 million active series for its largest tenant. 
 Source: Wise Engineering Blog 
 The real value of unification is correlation. When a service fails at 3 AM, developers want to see the error log, the trace showing which downstream call failed, and the metric spike that triggered the alert, all in one place and linked together. Running separate tools for each of those signals means context-switching during an incident, which costs time when time matters most. 
 Wise has also implemented dedicated observability clusters within its Compute Runtime Platform, separating monitoring infrastructure from production workloads so that a spike in monitoring load cannot affect the services being monitored. They are pilot testing Grafana Pyroscope for profiling select services, and have adopted Temporal as a workflow engine to automate database switchovers and recovery tests, keeping downtime minimal while staying compliant with strict resilience regulations. 
 Cost optimization is an ongoing task. Wise has invested in reducing operational costs and improving resource utilization across the observability stack, tying these efforts to their broader Mission Zero initiative. 
 Conclusion 
 A pattern runs through every layer of Wise’s tech stack. 
 At the frontend, the chassis and CRAB framework standardize how applications are built. 
 At the deployment layer, Spinnaker and automated canary analysis standardize how code reaches production. 
 At the infrastructure layer, CRP and Kubernetes absorb the complexity of hosting services. 
 At the data layer, shared pipelines and governance tools standardize how information flows. 
 At the observability layer, the LGTM stack standardizes how teams understand what is happening. 
 The common thread is that Wise treats its internal infrastructure as a product. The customers are the 850+ engineers. 
 The features are faster builds, safer deployments, easier service creation, and unified monitoring. And just like any product, the platform keeps evolving. CircleCI gives way to GitHub Actions, Octopus gives way to Spinnaker, Thanos gives way to Mimir, because the needs of those internal customers keep changing. 
 The trade-off is that this level of platform investment requires dedicated teams, carries significant migration cost, and only starts to pay off past a certain organizational size. 
 References: 
 The Wise Tech Stack (2025 Update) 
 Details about Wise
```

---

## 9. How Stripe Detects Fraudulent Transactions Within 100 ms

- 日期: 2026-04-28 03:03
- 链接: https://blog.bytebytego.com/p/how-stripe-detects-fraudulent-transactions

```
New Year, New Metrics: Evaluating AI Search in the Agentic Era (Sponsored) 
 Most teams pick a search provider by running a few test queries and hoping for the best – a recipe for hallucinations and unpredictable failures. This technical guide from You.com gives you access to an exact framework to evaluate AI search and retrieval. 
 What you’ll get: 
 A four-phase framework for evaluating AI search 
 How to build a golden set of queries that predicts real-world performance 
 Metrics and code for measuring accuracy 
 Go from “looks good” to proven quality. 
 Learn how to run an eval 
 Every time you buy something online from a Stripe-powered business, a machine learning model evaluates over 1,000 signals about your transaction and decides in under 100 milliseconds whether to let it through. 
 Across billions of legitimate payments, it reaches the correct verdict 99.9% of the time. The system that delivers those numbers, however, looks entirely different from what Stripe originally built. 
 The architecture has been overhauled multiple times, and one of the most important upgrades required removing a component the team knew was actively improving accuracy, because keeping it was holding back everything else the team wanted to do. 
 For reference, online payment fraud occurs in roughly 1 out of every 1,000 transactions. That rarity makes fraud detection a difficult machine learning problem because the system has to surface a small number of fraudulent payments from a massive volume of legitimate ones, and it has to do this quickly and cheaply on every single transaction. 
 In this article, we will look at how Stripe’s Radar does this effectively and the architectural decisions the team took while building it. 
 Disclaimer: This post is based on publicly shared details from the Stripe Engineering Team. Please comment if you notice any inaccuracies. 
 Why Stripe Removed the Component That Was Making Radar Better 
 Stripe began with relatively simple ML models like logistic regression (a statistical method that predicts the probability of an outcome based on input variables). Over time, as the Stripe network grew and ML technology advanced, they moved to more complex architectures. Each jump produced an equivalent leap in model performance. 
 The architecture preceding the current one was called Wide & Deep. It combined two models into an ensemble. 
 The “wide” component was XGBoost, a gradient-boosted decision tree that works by combining many small decision trees into one powerful predictor. XGBoost excelled at memorization, meaning it was strong at recognizing specific patterns and feature correlations it had encountered in training data. 
 The “deep” component was a deep neural network (DNN) that excelled at generalization, meaning it could learn abstract concepts like “unusual payment velocity on a card” and apply them to entirely new situations it had never seen before. 
 Together, the two components worked well. But XGBoost was creating operational bottlenecks. It was hard to parallelize, which meant retraining the combined model was slow. It was incompatible with advanced ML techniques Stripe wanted to adopt, like transfer learning that involves using knowledge gained from one task to improve performance on a different but related task, and embeddings. And it was also limiting how quickly the many engineers working on Radar each day could experiment with new ideas. 
 Simply dropping XGBoost would have caused a 1.5% drop in recall, meaning 1.5% more fraud would go undetected. That was an unacceptably large regression in performance. The value XGBoost provided was real and measurable, so it had to be replicated within a new architecture rather than just discarded. 
 Stripe’s solution drew inspiration from a research architecture called ResNeXt. 
 The core idea, sometimes called “Network-in-Neuron,” splits computation into multiple distinct branches, where each branch functions as a small neural network on its own. The outputs from all branches are summed to produce a final result. This multi-branch approach enriches feature representation along a new dimension, and it achieves this more effectively than the brute-force approach of simply making a DNN wider or deeper, which risks overfitting (the model memorizing random noise rather than learning real patterns). 
 The resulting architecture, internally called Shield NeXt, reduced training time by over 85%, bringing it to under two hours. Experiments that previously required overnight jobs could now run multiple times in a single working day. Stripe is now exploring techniques that this architectural shift made possible, including multi-task learning, where a single model is trained to handle several related objectives simultaneously. 
 [Live on May 6] Stop babysitting your agents (Sponsored) 
 Agents can generate code. Getting it right for your system, team conventions, and past decisions is the hard part. You end up babysitting the agent and watch the token costs climb. 
 More MCPs, rules, and bigger context windows give agents access to information, but not understanding. The teams pulling ahead have a context engine to give agents only what they need for the task at hand. 
 Join us live (FREE) on May 6 to see: 
 Where teams get stuck on the AI maturity curve and why common fixes fall short 
 How a context engine solves for quality, efficiency, and cost 
 Live demo: the same coding task with and without a context engine 
 Register now 
 The Stripe Platform’s Data Advantage 
 The model architecture matters, but Radar’s biggest competitive advantage comes from the data flowing through the Stripe network. Stripe has engineered specific mechanisms to convert that scale into model performance. 
 90% of cards used on the Stripe network have been seen more than once across different merchants. A single business has visibility into only its own transactions. Radar, by contrast, sees patterns across millions of businesses and thousands of partner banks around the world. 
 There is also a structural advantage in how Radar gets its training labels, the data that tells the model which past transactions were actually fraudulent. Since Radar is built directly into Stripe’s payment flow, it receives these labels automatically when cardholders dispute charges. Most third-party fraud solutions require businesses to build separate data pipelines for sending payment labels back to the fraud provider, or to label payments manually, which is time-consuming and error-prone. Radar sidesteps all of this by ingesting ground truth data straight from the payment flow and card networks. 
 Stripe uses hundreds of features in its model, and most of them are aggregates computed across the entire network. As the network grows, each feature becomes more informative because the training data better represents the feature’s real-world distribution. 
 A “feature” in this context is a single signal the model uses to evaluate a transaction. Some are intuitive. For example, does the cardholder’s name match the provided email address? How many different cards have been associated with this IP address? A high count might indicate someone testing stolen cards. Other features are more surprising. The difference between the device’s local time and UTC, or the count of countries where a card has been successfully authorized, both turn out to be meaningful fraud signals. 
 Finding new features is part forensics and part experimentation. Stripe’s team reviews past fraud attacks in detail, building investigation reports that try to reconstruct how fraudsters operate. They look for patterns in throwaway email addresses used to set up multiple accounts quickly. They monitor dark web activity weekly. From this research, they build a prioritized list of candidate features, implement each one rapidly, and prototype them to measure model impact. 
 Sometimes the most promising ideas yield little. For example, Stripe once built a feature capturing whether a business was currently under a distributed fraud attack. It barely moved the model performance because the model was already learning that pattern implicitly. 
 One of the more powerful techniques Stripe uses is embeddings, which are learned numerical representations for categorical data. Things like merchant identity, issuing bank, user country, and day of the week have many possible values, and defining useful numerical representations for them is challenging. 
 Stripe trains its model to learn an embedding for each value, essentially a set of coordinates that position it relative to others based on transaction patterns. Uber and Lyft, for example, would end up with similar embedding coordinates because their transaction patterns resemble each other, while Slack would be positioned very differently. 
 Embeddings enable geographic transfer of fraud knowledge. If Stripe identifies a new fraud pattern in Brazil, the embeddings allow the system to recognize that same pattern in the US automatically, without retraining. The model essentially learns which merchants and regions behave similarly, then applies fraud knowledge across the entire network. 
 Stripe also found that scaling up training data continued to yield significant gains. A 10x increase in training transaction data still produced meaningful model improvements, and the team was working on a 100x version. This kind of scaling was only feasible because the DNN-only architecture could train fast enough to handle much larger datasets practically. 
 Source: Stripe Engineering Blog 
 The Tradeoff Every Fraud System Has to Make 
 Having a great model and great data still leaves a fundamental question unanswered. 
 How much fraud should you actually block? 
 Every fraud detection system faces an inherent tension between two types of errors: 
 A false negative is when fraud slips through undetected, costing the business the product, a chargeback fee, and potential reputational damage with card networks. 
 A false positive is when a legitimate customer gets blocked, and the business loses the sale, along with potentially the customer forever. A survey found that 33% of consumers said they would stop shopping at a business after a single false decline. 
 These two errors exist on a curve. 
 Precision measures the fraction of blocked transactions that are actually fraudulent. Recall measures the fraction of all actual fraud that gets caught. As you raise the blocking threshold, requiring a higher fraud probability before blocking a payment, precision goes up because you become more selective about what you block. But recall goes down because more marginal fraud slips through. Lowering the threshold pushes things in the opposite direction. 
 Stripe frames this as two distinct problems: 
 The data science problem is about making the model better by adding predictive features, training on more data, and refining the architecture. A better model shifts the entire precision-recall curve upward, meaning that at any given threshold, you get better outcomes on both dimensions. 
 The business problem is about choosing where on that curve to operate, and the right answer depends entirely on the economics of each merchant. 
 For example, consider two businesses. 
 A food delivery company with thin margins might earn $2 in profit per order. Once you account for product cost and chargeback fees, a single fraudulent transaction can wipe out the profit from nearly 19 legitimate ones. For this business, aggressive blocking makes sense because the cost of missed fraud is devastating. On the other hand, a SaaS company with high margins faces the opposite calculation. The lifetime revenue lost by blocking a legitimate subscriber who would have paid $200 per month for years far outweighs the cost of an occasional fraudulent charge. 
 This is why Stripe built Radar to be configurable. 
 Merchants can adjust their risk threshold, and Radar for Fraud Teams lets them compose custom rules and set up manual review queues. 
 Stripe evaluates custom rules with the same precision-recall framework it uses for the model itself. When a merchant creates a rule, Stripe shows historical statistics on matching transactions that were actually disputed, refunded, or accepted, so the merchant can evaluate the impact before the rule goes live. Stripe also uses additional evaluation tools like ROC curves and AUC (area under the curve) scores to assess overall model quality, but the precision-recall framing captures the core tension most directly. 
 Manual review adds yet another lever. 
 Sending borderline transactions to human reviewers instead of blocking them outright improves precision with minimal impact on recall. Also, sending borderline transactions to review instead of allowing them through improves recall with minimal impact on precision. The cost is human effort, but it gives merchants a way to reshape their own precision-recall curve using business knowledge the model cannot access on its own. 
 Making a Black Box Explain Itself 
 All machine learning models are opaque to some degree, and deep neural networks are especially more opaque. Stripe accepted this when they chose DNNs over simpler, more interpretable techniques. The predictions are better, but explaining why a specific transaction received a given score is harder. 
 Stripe’s response was to build layers of interpretability around the model. 
 In 2020, they launched risk insights, a feature that shows merchants which factors contributed to a transaction being declined. The interface displays the top fraud signals, like an address being associated with a previous early fraud warning or an unusually high number of names linked to a card. It includes a location map showing distances between the billing address, shipping address, and IP address. It shows customer metadata like email, cardholder name, and the authorization rate for transactions associated with that email. 
 See the diagram below: 
 Source: Stripe Engineering Blog 
 Stripe also uses Elasticsearch, a search engine optimized for fast lookups across large datasets, to surface related transactions and help merchants put a specific decline in a broader context. 
 Internally, the team built a table view displaying the exact features contributing most to a transaction’s fraud score, which engineers use to debug support cases. Stripe is working on sharing more of these internal tools with merchants, closing the gap between what engineers can see and what users can see. 
 Explainability serves a practical purpose beyond building trust. When merchants understand why Radar scored a transaction the way it did, they can improve the data they send to Stripe for more accurate decisions. They can create custom rules that incorporate knowledge only they have about their own business. The explanation layer transforms Radar from a black box into something merchants can actively collaborate with. 
 Getting the Model Into Production 
 Building a better model is half the challenge. Deploying it safely at Stripe’s scale is the other half, and it involves two hard engineering problems. 
 The first is real-time feature computation. Every feature the model uses during training must also be computable in production, because Radar needs to score every incoming payment as part of the Stripe API flow. For a feature like “the two most frequent IP addresses previously used with this card,” Stripe maintains an up-to-date state on every card ever seen on the network, and fetching or updating that state has to be fast. Stripe’s ML infrastructure team built systems that let engineers define features declaratively, with current values made available automatically in production at low latency. 
 The second is ensuring that model improvements hold across the entire user base, all the way down to individual merchants. A model that performs better on aggregate metrics might still cause a spike in block rate for smaller businesses, which would be disruptive for those merchants and their customers. Before releasing any model, Stripe measures the change it would cause to the false positive rate, block rate, and authorization rate on both an aggregate and per-merchant basis. If a model would cause undesirable shifts for certain users, they adjust it for those segments before release. They also compare score distributions between old and new models, aiming to keep the proportion of transactions above each merchant’s blocking threshold stable. 
 Fraud patterns shift constantly, which means even a well-performing model degrades over time, a phenomenon called model drift. Stripe found that retraining the same model on more recent data, with identical features and architecture, improves recall by up to half a percentage point per month. That is a big gain from simply keeping the data fresh. By investing in automated training, tuning, and evaluation tooling, Stripe tripled their model release cadence. They continuously update performance dashboards after training but before release, so engineers can spot stale model candidates and proactively retrain them. 
 The fraud landscape itself keeps evolving. Patterns have shifted from primarily stolen credit card fraud to a growing mix of traditional card fraud and high-velocity card testing attacks, where automated scripts try large numbers of stolen card numbers against a merchant’s checkout flow. Stripe’s deployment infrastructure is built to support this kind of rapid adaptation. 
 Stripe also faces a subtle measurement challenge in production. Transactions that the model blocks have unknown true outcomes because the payment was never completed. Computing a full production precision-recall curve requires counterfactual analysis, meaning statistical methods that estimate what would have happened to payments Radar blocked. Stripe has developed proprietary techniques for this over the years. 
 Conclusion 
 Radar is a very different product from what it was at launch. 
 The models, the data pipelines, the explainability tools, and the way Stripe communicates fraud decisions to merchants have all been rebuilt. Fraud patterns have changed considerably in that time as well. 
 However, the core goal of the Radar team remains the same. 
 They are still working to create an environment where businesses and customers can transact with confidence, still optimizing that brief moment customers barely register, the instant between clicking “purchase” and seeing the transaction confirmed. Every architectural choice, every feature, every deployment safeguard exists to make that 100-millisecond window as accurate, fair, and trustworthy as possible. 
 References: 
 How we built it: Stripe Radar 
 A primer on machine learning for fraud detection
```

---

## 10. How Amazon Uses LLMs to Recommend Products

- 日期: 2026-04-27 15:30
- 链接: https://blog.bytebytego.com/p/how-amazon-uses-llms-to-recommend

```
Your agent isn’t broken. Your context is. (Sponsored) 
 Most AI agents don’t fail because the model is bad. They fail because the model doesn’t have the proper infrastructure to reason well. 
 Simba Khadder, Head of Engineering at Redis, lays out a 4 pillar framework for building context systems that hold up in production—plus an architectural self-audit checklist you can run against your stack today. 
 Read the guide → 
 Search “shoes for pregnant women” on Amazon, and the best results you get might be slip-resistant shoes. This is even though the word “pregnant” appears nowhere in those product listings. 
 In other words, there is zero keyword overlap between the query and the product. The search engine has to reason that pregnant women need stability, that stability means slip-resistance, and that slip-resistant shoes are the right match. 
 Traditional recommendation systems match text to text and purchase history to purchase history. They handle keyword overlap quite well. However, when a shopper’s intent requires a reasoning step that lives entirely in human common sense, those systems hit a wall. 
 Amazon’s search team recognized this blind spot and built a commonsense knowledge graph called COSMO that teaches the recommendation engine to think the way a human shopper would. 
 In this article, we will look at how COSMO works and the challenges the engineering team faced. 
 Disclaimer: This post is based on publicly shared details from the Amazon Engineering Team. Please comment if you notice any inaccuracies. 
 The Gap Between What You Search and What You Mean 
 Amazon already operates large-scale knowledge graphs that store factual product attributes like brand, color, material, and category. These graphs power a lot of what works well in product search today. However, they mainly try to encode what a product is, and they don’t explain why a human would want it. 
 This is the semantic gap problem. 
 For example, a query like “winter clothes” carries an implicit intent around warmth. The product catalog for a long-sleeve puffer coat describes its material, size options, and sleeve length, but it may say nothing about warmth directly. The gap between what the customer typed and what the product listing says requires a reasoning step that factual knowledge graphs were never designed to handle. 
 Amazon’s team surveyed the landscape of existing solutions. 
 Alibaba built AliCoCo (163K nodes, 91 relations) and AliCG (5M nodes), both extracted from search logs. These capture product concepts, but they stay focused on product attributes and categories, skipping user intent entirely. 
 General commonsense knowledge bases like ConceptNet (8M nodes, 21M edges) cover everyday reasoning but are built for general purposes, with little grounding in shopping behavior. 
 Amazon’s own earlier effort, FolkScope, demonstrated that commonsense knowledge could be extracted from shopping data, but it covered only 2 product categories and only co-purchase behavior. 
 The gap was clear. Though factual product knowledge and general commonsense knowledge existed, structured knowledge about why people buy things at an e-commerce scale was missing. 
 Asking the LLM (and Why the Answers Fell Short) 
 The intuition behind Amazon’s approach was simple. Large language models encode enormous amounts of world knowledge in their parameters. Taking our earlier example, if you ask an LLM why a customer who searched “winter coat” bought a long-sleeve puffer coat, it can reason that puffer coats provide warmth, and warmth is what the customer wanted. 
 The team fed millions of user behavior pairs into OPT-175B and OPT-30B, large language models hosted internally on 16 A100 GPUs. The choice of OPT over GPT-4 was driven by a hard constraint around data privacy. Customer behavior data, meaning which queries led to which purchases, could only be processed on Amazon’s own infrastructure. 
 Two types of behavior data went into the system. 
 Query-purchase pairs capture the connection between a search query and the product a customer ultimately bought. 
 Co-purchase pairs capture products bought together in the same shopping session 
 Across 18 product categories, the team sampled 3.14 million co-purchase pairs and 1.87 million query-purchase pairs. 
 The sampling strategy was itself a design decision. 
 For products, Amazon covered popular browse node categories and selected top-tier products with high interaction volume, also using product type labels (more than a thousand classes like “umbrella” or “chair”) for finer-grained selection. 
 For co-purchase pairs, the team cross-checked product types to remove random co-purchases and filtered out products that co-occurred with too many different product types (a signal of noise rather than intent). 
 For search-buy pairs, thresholds on both purchase rate and click rate determined which queries and products entered the sample. 
 Crucially, an in-house query specificity service helped prioritize broad or ambiguous queries, because those are exactly where the semantic gap is largest and commonsense knowledge adds the most value. 
 Prompt design mattered too. Rather than using simple text continuation, Amazon formatted each behavior pair as a question-answering task and instructed the LLM to generate a numbered list of candidates rather than a single response. 
 The LLM generated millions of candidate explanations. However, only 35% of search-buy explanations met Amazon’s quality bar for typicality, meaning they were representative of genuine shopping intent. For co-purchase explanations, that number dropped to 9%. The rest were filler. The LLM produced circular rationales like “customers bought them together because they like them,” or trivially obvious statements like “customers bought an Apple Watch because it is a type of watch.” 
 The 9% vs. 35% gap reveals something about how LLMs reason. Explaining why a query led to a purchase is relatively constrained because the query provides clear context about intent. But explaining why two products were bought together requires identifying a shared reason across two different items, and LLMs tend to default to generic explanations for one item rather than reasoning about the pair. 
 Amazon also needed a way to categorize the relationships that the LLM was generating. The team started with 4 broad seed relations (usedFor, capableOf, isA, cause) that prior work had shown produce diverse outputs. From there, they mined finer-grained relation types directly from the LLM’s generated text by looking for recurring predicate patterns. 
 The most common pattern was “the product is capable of being used [preposition],” where different prepositions mapped to different semantic relationships. This data-driven process produced 15 relation types that capture distinct ways humans reason about products. These include used_for_function (”dry face”), used_for_event (”walk the dog”), used_for_audience (”daycare worker”), used_in_location (”bedroom”), used_in_body (”sensitive skin”), used_with (complementary products like “surface cover”), and person-centric relations like xIs_a (”pregnant women”) and xWant (”play tennis”). The ontology was shaped by what the LLM actually generated, then canonicalized and structured by Amazon’s researchers, rather than being designed top-down by a team of knowledge engineers. 
 Building the Filter 
 The LLM produced a mountain of hypotheses, which were mostly noise. Amazon’s solution was a multi-stage refinement pipeline, where each stage catches a different type of failure. 
 Coarse-grained filtering tackled the most obvious problems first. Rule-based filters removed incomplete sentences by measuring sentence quality with a language model (GPT-2) and tuning a threshold. Generations that exactly matched the query text, the product type, or the product title (or fell within a small edit distance) were discarded. For generic statements like “used for the same reason” or “used with clothes,” Amazon identified these by combining frequency and entropy, since generic explanations tend to co-occur with many different products rather than specific ones. 
 Similarity filtering handled a subtler problem. Some LLM outputs looked different from the input on the surface but were semantically just paraphrases of the original query or product description. 
 Amazon used an in-house language model, pre-trained on e-commerce text including queries and product information, to compute embeddings for the generated knowledge, the query, and the product. When the vector similarity (measured by cosine distance) between the generated knowledge and the original context was too high, the candidate was filtered out. The team found that filtered generations were essentially syntactic transformations of the original input, rearranging the same meaning in slightly different words. 
 Human-in-the-loop annotation came next. Amazon sampled 30,000 knowledge candidates for human review, with 15,000 from co-purchase behavior and 15,000 from search-buy behavior spread across 18 categories. Rather than picking candidates uniformly, the team used a weighted formula that combined the frequency of a piece of generated knowledge with the popularity of the associated product or query. Popular products produce common knowledge, so the weighting pushed toward diverse, less obvious knowledge that the classifier would later need to generalize. 
 Annotators evaluated each candidate on two dimensions: 
 Plausibility measures whether the posited relationship is reasonable. 
 Typicality measures whether the knowledge is representative of genuine shopping behavior. 
 As a concrete example, the more typical reason people buy Apple Watches is that they are intelligent watches, rather than that they tell the time. Both statements are plausible, but only the first is typical. 
 To reduce cognitive burden and disagreement among annotators, Amazon decomposed these assessments into five yes/no questions covering completeness, relevance, informativeness, plausibility, and typicality. Two annotators labeled each question independently, with a third resolving disagreements. A pilot study of 2,000 examples showed this decomposition significantly reduced the disagreement rate, and internal auditing of 5% of all annotations showed over 90% accuracy. Due to data privacy requirements, Amazon employed a professional data annotation vendor company, followed by a strict internal auditing process. 
 Classifier generalization was the final step. Amazon fine-tuned DeBERTa-large (a high-performing language model for classification tasks) and an in-house language model on the 30,000 annotated samples to predict plausibility and typicality scores for all remaining candidates. Only candidates scoring above a 0.5 plausibility threshold survived. 
 The output of this pipeline is a set of structured knowledge triples. A triple connects two entities through a defined relationship. For example, the triple <co-purchase of camera case and screen protector, capableOf, protecting camera> captures the commonsense reasoning that these two products are bought together because they both serve the purpose of protecting a camera. Assembled, these triples form a knowledge graph of 6.3 million nodes and 29 million edges spanning 18 product categories. From 30,000 human judgments to 29 million edges. 
 COSMO-LM, the Smaller Model 
 The knowledge graph captures pre-computed commonsense relationships, but Amazon’s search engine encounters new queries and products constantly. Running the full pipeline (OPT-175B generation followed by classifier scoring) for every new behavior pair would be prohibitively expensive in production. 
 Amazon’s solution was instruction tuning. 
 The team used their 30,000 annotated samples to create instruction data and fine-tuned LLaMA 7B and 13B models. These base models offered the best balance between generation quality and inference cost for production serving, with far fewer parameters than OPT-175B while still producing high-quality outputs when trained on domain-specific data. The resulting model, COSMO-LM, was trained across 18 product domains, 15 relation types, and 5 distinct tasks. 
 Beyond commonsense generation, those tasks included plausibility prediction, typicality prediction, search relevance prediction, and co-purchase prediction. The multi-task training means COSMO-LM can both generate knowledge and evaluate its own output quality, effectively collapsing the “big LLM plus classifier” stack into a single, smaller model. 
 To make the model robust to different input formats, Amazon varied the templates during training. The same query-product pair might be prefixed with “search query,” “user input,” or “user searched” across different training examples. This prevents COSMO-LM from becoming brittle to prompt phrasing. 
 The result is two complementary artifacts in production. The static knowledge graph (29 million pre-computed edges) handles known product relationships. COSMO-LM generates fresh commonsense knowledge on the fly for new or unseen query-product pairs, with dramatically lower inference cost than the original OPT-175B pipeline. A demo of the system shows COSMO-LM generating knowledge for a query like “how to decorate a home,” producing a list of product types (wall art, decorative signage, sticker decal, decorative pillow cover, artificial plant, rug, home mirror, lamp), each accompanied by a commonsense explanation of its role in home decoration. 
 Serving Commonsense at Amazon Scale 
 Having a model that generates useful knowledge is one challenge. Serving it at Amazon’s scale with acceptable latency is another. 
 Amazon’s deployment architecture centers on two components: 
 A Feature Store transforms COSMO-LM’s raw text outputs into structured features that downstream applications can consume directly. These features include product key-value pairs, semantic subcategory representations, and intent signals. 
 An Asynchronous Cache Store manages the serving layer through a two-tiered caching strategy. 
 The first tier pre-loads responses for yearly frequent searches, covering the majority of traffic. The second-tier batch processes daily requests for newer or less common queries and updates the cache. 
 When a user query arrives, the system checks the cache first. Hits get immediate responses. Misses go to batch processing, and the cache updates for future identical queries. 
 SageMaker manages model deployment and refresh, ingesting customer behavior session logs daily. The structured data from the cache feeds three downstream systems simultaneously, including Search Relevance, Recommendation, and Navigation. 
 This architecture meets Amazon’s strict search latency requirements while keeping storage costs comparable to real-time serving for most traffic. But it comes with a tradeoff. COSMO updates daily, which means it cannot incorporate real-time events like flash sales that fluctuate within hours. Amazon explicitly acknowledges this limitation and identifies it as an area for future development. 
 COSMO’s Impact 
 Search relevance saw the most dramatic offline improvements. 
 On the public ESCI dataset from KDD Cup 2022, a cross-encoder (a model architecture that jointly processes query and product features together, rather than encoding them separately) augmented with COSMO triples achieved 73.48% Macro F1 and 90.78% Micro F1 with trainable encoders. 
 For context, Macro F1 averages performance across all product categories equally (so rare categories matter just as much as common ones), while Micro F1 measures overall accuracy regardless of category. That cross-encoder result surpassed the top-1 ensemble model on the KDD Cup leaderboard. With frozen encoders, where the only difference was whether COSMO triples were included as input, the improvement was 60% on Macro F1. 
 On private datasets spanning four markets (US, Canada, UK, and India), the COSMO-enhanced model consistently outperformed baselines in every locale, with the strongest gains in the India market, where the gap between query language and product catalog language tends to be larger. 
 Session-based recommendation benefited from COSMO knowledge as well. 
 Amazon built COSMO-GNN, extending a graph neural network model (a model that learns relationships between items by treating shopping sessions as connected graphs) for session-based recommendations with COSMO-generated intent knowledge. It outperformed all competitive baselines on Hits@10 and NDCG@10 in both clothing and electronics categories. 
 The improvement was larger for electronics (5.82% vs. 4.05% on Hits@10), where users revise their search queries more frequently (2.47 unique queries per session versus 1.36 for clothing). This pattern makes sense. When users are actively reformulating queries to narrow down what they want, commonsense knowledge about why they are searching becomes especially valuable. 
 Search navigation is where COSMO reached production and generated real business impact. COSMO powers a multi-turn navigation system that organizes intent hierarchically. A search for “camping” branches into fine-grained intents like “winter camping,” “beach camping,” or “lakeside camping.” These connect to product types like “air mattress” or “winter boots,” which are then further refined by attributes like “4 person.” 
 This hierarchical organization of knowledge allows the system to mirror a natural discovery process, helping customers progressively narrow their search through multiple rounds of refinement rather than requiring them to formulate the perfect query upfront. 
 Amazon ran A/B tests over several months, targeting approximately 10% of U.S. traffic. The results were significant. A 0.7% relative increase in product sales within the test segment translated to hundreds of millions of dollars in additional annual revenue. 
 An 8% increase in navigation engagement was observed in the same segment. These outcomes came from a single, relatively small feature on the search page with limited visibility. Amazon has projected that extending COSMO-LM across all traffic for navigation alone could produce revenue gains in the billions. 
 Conclusion 
 COSMO is Amazon’s first production system that uses instruction-tuned large language models to construct a knowledge graph and serve it to online applications. It marks a shift from factual product knowledge graphs toward intent-based commonsense knowledge graphs. 
 The most important number from this entire project may be the leverage ratio. Thirty thousand human annotations became 29 million knowledge graph edges across 18 product categories. That ratio was possible because Amazon invested heavily in sampling strategy, annotation design, classifier training, and instruction tuning rather than in brute-force labeling. 
 The system’s acknowledged limitations are worth keeping in mind as well. 
 COSMO’s daily refresh cycle means it cannot keep up with real-time dynamics. Its aggressive filtering (only candidates above 0.5 plausibility survive) means the knowledge graph has gaps in coverage, especially for long-tail products and unusual queries. These are genuine tradeoffs, and Amazon chose precision over recall because unreliable commonsense knowledge in production would be worse than missing knowledge. 
 References: 
 Building commonsense knowledge graphs to aid product recommendation 
 COSMO: A large-scale e-commerce common sense knowledge generation and serving system at Amazon
```

---

## 11. EP212: Data Warehouse vs Data Lake vs Data Mesh

- 日期: 2026-04-25 15:30
- 链接: https://blog.bytebytego.com/p/ep212-data-warehouse-vs-data-lake

```
✂️ Cut your QA cycles down to minutes with QA Wolf (Sponsored) 
 If slow QA processes bottleneck you or your software engineering team and you’re releasing slower because of it — you need to check out QA Wolf. 
 QA Wolf’s AI-native service supports web and mobile apps , delivering 80% automated test coverage in weeks and helping teams ship 5x faster by reducing QA cycles to minutes. 
 QA Wolf takes testing off your plate. They can get you: 
 Unlimited parallel test runs for mobile and web apps 
 24-hour maintenance and on-demand test creation 
 Human-verified bug reports sent directly to your team 
 Zero flakes guarantee 
 The benefit? No more manual E2E testing. No more slow QA cycles. No more bugs reaching production. 
 With QA Wolf, Drata’s team of 80+ engineers achieved 4x more test cases and 86% faster QA cycles . 
 Schedule a demo to learn more 
 This week’s system design refresher: 
 Coding Agents Explained: How Claude Code, Codex & Cursor Actually Work (Youtube video) 
 Data Warehouse vs Data Lake vs Data Mesh 
 API Concepts Every Software Engineer Should Know 
 Polling vs Long Polling vs Webhooks vs SSE 
 SLA vs SLO vs SLI 
 Build with Claude Code — Course Direction Survey 
 Coding Agents Explained: How Claude Code, Codex & Cursor Actually Work 
 Data Warehouse vs Data Lake vs Data Mesh 
 Storing data is the easy part. Deciding where and how to organize it is the real challenge. 
 A data warehouse is the traditional approach. It cleans and structures data before storing it. Queries run fast, and reports stay consistent. But adding a new data source takes effort because everything has to fit the schema first. 
 A data lake takes the opposite approach. It stores everything raw, like databases, logs, images, and video. Process it when you need it. The flexibility is great, but if rules around naming, formatting, and ownership are not properly set, you end up with duplicate, outdated, and undocumented data that is hard to manage. 
 Data mesh shifts data ownership from a central team to individual departments. For example, sales publishes sales data, and finance publishes finance data. Shared standards keep things compatible across teams. 
 It works well in larger organizations. But it requires every team to have the right people and processes to manage their data quality, documentation, and access, which is a challenge. 
 In practice, many companies use more than one approach. They'll use a warehouse for dashboards and reporting, a lake for machine learning workloads and start applying mesh principles as teams scale. 
 API Concepts Every Software Engineer Should Know 
 Most engineers use APIs every day. Sending a request and reading JSON is one thing. Designing an API that other people can rely on is something where things get complicated. 
 A lot of problems begin with basic HTTP details that seem small at first. Methods, status codes, request formats, and response structure can make an API feel clear and predictable, or confusing and inconsistent. 
 Then there are the bigger design choices. REST, GraphQL, gRPC, webhooks, and WebSockets each make sense in different situations. The challenge is knowing what actually fits the system and the use case. 
 A lot of API problems also comes from design decisions that do not get enough attention early on. Naming, pagination, versioning, error responses, and backward compatibility often decide whether an API is easy to work with or frustrating to maintain. 
 Security is another area where weak decisions can cause real problems. API keys, OAuth, JWTs, scopes, and permissions are easy to mention. Getting them right is harder, and mistakes here can be costly. 
 Reliability matters too. Timeouts, retries, idempotency, rate limits, and caching are often easy to ignore until the system is under pressure. 
 And once an API starts growing, the supporting work matters too. Clear documentation, solid specs, observability, and contract testing make it much easier for teams to trust the API and use it without guessing how it works. 
 Over to you: What’s the most overlooked API concept in your experience? 
 Polling vs Long Polling vs Webhooks vs SSE 
 Four ways to get updates from a server. Each one makes a different tradeoff between simplicity, efficiency, and real-time delivery. 
 Here's how they compare: 
 Polling: The client sends a request every few seconds asking "anything new?" The server responds immediately, whether or not there's new data. Most of those requests come back empty, wasting client and server resources. For use cases like an order status page where a small delay is acceptable, polling is the simplest option to implement. 
 Long Polling: The client sends a request, and the server keeps the HTTP connection open until new data is available or a timeout occurs. This means fewer empty responses compared to regular polling. Some chat applications used this pattern to deliver messages closer to real-time communication. 
 Server-Sent Events (SSE): The client opens a persistent HTTP connection, and the server streams events through it as they're generated. It is one-way, lightweight, and built on plain HTTP. Many AI responses that appear token by token are delivered through SSE, streaming each chunk over a single open connection. 
 Webhooks: Instead of the client asking for updates, the service sends an HTTP POST to a pre-registered callback URL whenever a specific event occurs. Stripe uses this for payment confirmations. GitHub uses it for push events. The client never polls or holds a connection open, it just waits for the server to call. 
 Many systems don't rely on a single pattern. You may use polling for order status, SSE for streaming AI responses, and webhooks for payment confirmations. 
 SLA vs SLO vs SLI 
 These three terms are related, but they mean different things. Knowing the difference helps you define what to measure, aim for, and promise your customers. 
 Here's how they actually connect: 
 SLI (Service Level Indicator): This is the metric you're measuring. For a login service, it could be the ratio of successful login requests to total valid requests. It tells you how your service is performing right now. 
 SLO (Service Level Objective): You take that SLI and define a target around it. Something like "login availability should stay above 99.9% over a rolling 28-day window." When you're missing your SLO, it’s a signal to find out what's failing before customers notice. 
 SLA (Service Level Agreement): This is what you promise your customers in a contract. It's usually set lower than the SLO, say 99.5% monthly availability. If you breach it, you owe service credits. 
 If your SLO and SLA are both set to 99.9%, then the moment your availability drops below 99.9%, you've already breached the agreement. 
 The SLI tells you where you stand. The SLO tells you where you should be. The SLA tells your customers what they can expect. 
 Over to you: How do you decide what the right SLO target is when you're launching a new service? 
 Build with Claude Code — Course Direction Survey 
 We’re building a new course, Build with Claude Code, and we’d love your input before we finalize it. 
 If you’re an engineer or engineering leader, we’d appreciate 3 minutes of your time. Your answers will directly shape what we cover. Thank you so much! 
 Take the short survey
```

---

## 12. B-Trees vs LSM Trees: Comparison and Trade-Offs

- 日期: 2026-04-23 15:30
- 链接: https://blog.bytebytego.com/p/b-trees-vs-lsm-trees-comparison-and

```
Every database has to solve the same basic problem. 
 Data lives on disk, and accessing disk is slow. Every read and every write eventually has to reach the disk, and how a database organizes data on that disk determines everything about its performance. 
 Over decades of research, two dominant approaches have emerged. 
 B-Trees keep data sorted on disk so reads are fast, but pay for it on every write. 
 LSM Trees buffer writes in memory and flush them to disk in bulk, making writes cheap but reads more expensive. 
 Neither approach is better. They represent two different approaches, and understanding the tradeoff between them is one of the most useful mental models in system design. 
 In this article, we will look at B-Trees and LSM trees in detail, along with the trade-offs associated with each of them. 
 The Problem with Disk Access 
 Read more
```

---

## 13. How DoorDash Launches a New Country in One Week

- 日期: 2026-04-21 15:30
- 链接: https://blog.bytebytego.com/p/how-doordash-launches-a-new-country

```
MongoDB Monitoring Cheatsheet (Sponsored) 
 Skip the guesswork with this MongoDB cheatsheet from Datadog. You’ll get a quick, practical reference for monitoring performance and diagnosing issues in real systems. 
 Use it to: 
 Track key metrics like latency, throughput, and resource utilization 
 Monitor MongoDB and Atlas health with the right signals 
 Set up dashboards to quickly identify bottlenecks and performance issues 
 Get the cheatsheet 
 When DoorDash needed to launch Dasher onboarding in Puerto Rico, it took about a week. That wasn’t because they cut corners or threw a huge team at it. It took a week because almost no new code was needed. The steps that Puerto Rican Dashers would go through (identity checks, data collection, compliance validation) already existed as independent modules, battle-tested by thousands of Dashers in other countries. The team assembled them into a new workflow, made one minor customization, and shipped. 
 And it wasn’t just Puerto Rico. Australia’s migration was completed in under a month. Canada took two weeks, and New Zealand required almost no new development at all. 
 This speed came from an architectural decision the DoorDash engineering team made when they looked at their growing mess of country-specific if/else statements and decided to stop patching. 
 They rebuilt their onboarding system around a simple idea. Decompose the process into self-contained modules with standardized interfaces, then connect them through a deliberately simple orchestration layer. 
 In this article, we will look at how this architecture was designed and the challenges they faced. 
 Disclaimer: This post is based on publicly shared details from the DoorDash Engineering Team. Please comment if you notice any inaccuracies. 
 The Cost of Country-Specific Logic 
 DoorDash’s Dasher onboarding started simple, with just a few steps serving a single country through straightforward logic. Then the company expanded internationally, and every new market meant new branches in the code. 
 At one point, three API versions ended up coexisting. V3, the newest, continued calling V2 handlers for backward compatibility and also continued writing to V2 database tables. The system literally couldn’t avoid its own history. All developers have probably seen something like this before, where nobody can fully explain which version handles what, and removing any piece feels dangerous because something else might depend on it. 
 See the diagram below that shows the legacy system view: 
 The step sequences themselves were hard-coded, with country-specific logic spread throughout. Business logic started immediately after receiving a request, branching into deep if/else chains based on country, step type, or prior state. Adding a new market meant carefully threading new conditions through this maze of conditions. 
 Vendor integrations followed no consistent pattern either. Some onboarding steps used internal services, which called third-party vendors. Other steps called vendors directly. This inconsistent layering made testing and debugging unpredictable. 
 And then there was also the state management problem. Onboarding progress was tracked across multiple separate database tables. Flags like validation_complete = true or documents_uploaded = false lived in different systems. If a user dropped off mid-onboarding and came back later, reconstructing where they actually stood required querying several systems and inferring logic. This frequently led to errors. 
 The practical cost was that adding a new country took months of engineering effort across APIs, tables, and code branches. Every change carried the risk of breaking something in a market on the other side of the world. 
 Orchestrators, Workflows, and Steps 
 DoorDash’s rebuild was organized around three distinct layers, each with a single responsibility. It’s easy to blur these layers together, but the separation between them is where the real power lives. 
 The Orchestrator sits at the top. It’s a lightweight routing layer that looks at context (which country and which market type) and decides which workflow definition should handle the request. That’s all it does. It doesn’t execute steps or manage state. It doesn’t contain business logic either. The main insight here is that the smartest thing about the orchestrator is how little it does. Developers tend to imagine the central controller as the brain of the system. However, in this architecture, the brain is distributed, and the orchestrator is just a traffic cop. 
 Workflow Definitions are the second layer. A workflow is simply an ordered list of steps for a specific market. The US workflow might look like Data Collection, followed by Identity Verification, followed by Compliance Check, followed by Additional Validation. Australia’s workflow skips one step and reorders another. Puerto Rico adds a regional customization. Each workflow is defined as a class with a list of step references, making it easy to see exactly what each market’s onboarding process looks like. 
 Think of it like a Lego set. Each brick has a standardized shape, studs on top, tubes on the bottom, and that standard interface lets you build anything. A workflow definition is like building instructions for a specific model. 
 Step Modules are the third layer, and this is where the actual work happens. Each step (data collection, identity verification, risk and compliance checking, document verification) is implemented as an independent and self-contained module. A step knows how to collect its data, validate it, call its external vendors, handle retries and failures, and report success or failure. What it doesn’t know is which workflow it belongs to, or what step comes before or after it. This isolation is what makes reuse possible. 
 The mechanism enabling this plug-and-play behavior is the interface contract. Every step implements the same standardized interface, with a method to process the step, a method to check if it’s complete, and a method to return its response data. As long as a new step honors this contract, it can slot into any workflow without the workflow knowing or caring about its internals. 
 This contract also enables team autonomy. The identity verification step can be owned entirely by the security team. Payment setup can belong to the finance team. Each team iterates on their step independently, as long as they maintain the shared interface. In a way, the architecture mirrors the organizational structure, or more accurately, it lets the organizational structure work for the system instead of against it. 
 Two additional capabilities make the system even more flexible: 
 Composite steps group multiple granular steps into a single logical unit. One country might collect all personal information on a single screen. Another might split it across three screens. A composite step called “PersonalDetails” can wrap Profile, Additional Info, and Vehicle steps together, handling that variation without changing the individual step implementations underneath. 
 And steps can be dynamic and conditional. A Waitlist step might only appear in markets with specific supply conditions. The same step can even appear multiple times within a single workflow. 
 This flexibility goes beyond simple reordering and confirms that steps are truly stateless and workflow-agnostic. 
 The address collection step is the clearest proof that this works in practice. DoorDash built it once as a standalone module. When Australia needed address collection early in their flow for compliance checks, the team simply inserted the module before the compliance step in Australia’s workflow definition, without any special logic or branching. Canada later adopted the same step for validation and service-area mapping. It worked out of the box. The US team then experimented by enabling it in select regions, and again, with no new code. 
 This three-layer pattern isn’t specific to onboarding. Any multi-step process that varies across contexts (checkout flows, approval pipelines, content moderation queues) can be decomposed this way. 
 One important clarification here is that DoorDash’s step modules are not separate microservices. They are modules within a single service, which means the lesson here is about logical decomposition and interface design rather than strict deployment boundaries. Technically, we could apply this same pattern inside a monolith. 
 One Map for All Onboarding State 
 How does the system know where each applicant is in their journey? 
 Answering this question is needed to make modular steps work. 
 In the legacy system, this was a mess. Progress was tracked across multiple separate tables, each representing part of the workflow. Introducing a new onboarding step meant modifying several of these tables. Ensuring synchronization between them required close coordination across services, and it often broke down, leading to data mismatches and brittle integrations. 
 The new system introduced the status map, a single JSON object in the database where every step writes its own progress. It looks something like this: 
 {
 “personal_info”: { “status”: “DONE”, “metadata”: { “name”: “Jane” } },
 “address”: { “status”: “DONE”, “metadata”: { “address_id”: “abc123” } },
 “validation”: { “status”: “IN_PROGRESS” },
 “compliance”: { “status”: “INIT” }
} 
 Each step is responsible for updating its own entry in the map. When a step starts, completes, fails, or gets skipped, it writes that transition directly to its entry. The workflow layer never writes to the status map. It just reads it. 
 See the diagram below: 
 Source: DoorDash Engineering Blog 
 Each step also exposes an isStepCompleted() method that defines its own completion logic based on the status map. One step might treat “SKIPPED” as a terminal state, while another might not. This flexibility lives at the step level, not the workflow level, which keeps the orchestration logic simple and stateless. 
 The practical benefit is immediate. A single query on the status map tells you exactly where any applicant stands in their onboarding journey. Partial updates are handled through atomic JSON key merges, meaning that when one step updates its status, it only touches its own entry without overwriting the rest of the map. 
 Migration, Tradeoffs, and What Comes Next 
 The architecture is only half the story. Getting there without breaking a running system is where the real engineering difficulty lives. 
 DoorDash didn’t flip a switch. They designed the new platform to coexist with the existing V2 and V3 APIs, running old and new systems side by side. Applicants who had partially completed onboarding under the legacy system needed to continue seamlessly, so the team built temporary synchronization mechanisms that mirrored progress between systems until the migration was complete. This parallel operation was itself a temporary technical debt, built intentionally to be thrown away. 
 Other major initiatives were underway during the rebuild, sometimes conflicting with the new onboarding design. Rather than treating these as blockers, the team collaborated across those efforts and adapted the architecture where necessary. 
 The migration started with the US in January 2025, their largest and most complex market, as the proving ground. Then the compounding payoff kicked in. Australia was completed in under a month, needing only two localized steps. Canada followed in two weeks with a single new module. Puerto Rico took a week with a minor customization. New Zealand required almost no new development. 
 Every migration launched with zero regressions, no user-facing incidents, no onboarding downtime, and no unexpected drop-offs in completion rates. Each rollout got faster because more modules had already been battle-tested by thousands of Dashers in prior markets. 
 The architecture has also proven its value beyond adding countries. DoorDash is integrating its onboarding with another large, independently developed ecosystem that has its own mature onboarding flow. The modular design allowed them to build integration-specific workflows while reusing much of the existing logic, something that would have been extremely painful with the legacy system. 
 The tradeoffs are real, though. Modularity adds coordination overhead. For a single-market startup, this architecture can be considered overkill. A monolithic onboarding flow is completely fine until you hit the inflection point where country-specific branching becomes more expensive than decomposition. 
 Reusable modules work well when the underlying concept generalizes across markets. For example, addresses are conceptually similar everywhere, which is why the address step was reused so cleanly. However, compliance requirements can be fundamentally different between regulatory regimes. 
 The boundary between the platform team and domain teams also requires ongoing negotiation. DoorDash addresses this through published platform principles, versioned interface contracts, and joint KPIs that create shared accountability. Domain expert teams own their business logic (fraud detection, compliance, payments) while the platform enforces consistency. This is a human coordination challenge that architecture alone doesn’t solve. 
 Conclusion 
 Looking ahead, DoorDash’s roadmap includes dynamic configuration loading to enable workflows to go live through config rather than code, step versioning to allow multiple iterations of a step to coexist during experiments or rollouts, and enhanced operational tooling to give non-engineering teams the ability to manage workflows directly. 
 That said, DoorDash deliberately kept workflows code-defined rather than jumping straight to config-driven. While config-driven systems are powerful, they introduce their own complexity. They can be harder to debug and harder to test. 
 Ultimately, what DoorDash built is a sort of pattern for any system that needs to support multiple variants of a multi-step process. The core idea is three layers (a thin orchestrator, composable workflows, and self-contained steps behind standardized interfaces) connected by a single shared state structure. 
 References: 
 Unified Dasher Onboarding: A Modular Platform to Scale Globally
```

---

## 14. The Security Architecture of GitHub Agentic Workflow

- 日期: 2026-04-20 15:30
- 链接: https://blog.bytebytego.com/p/the-security-architecture-of-github

```
npx workos: From Auth Integration to Environment Management, Zero ClickOps (Sponsored) 
 npx workos@latest launches an AI agent, powered by Claude , that reads your project, detects your framework, and writes a complete auth integration into your codebase. No signup required. It creates an environment, populates your keys, and you claim your account later when you're ready. 
 But the CLI goes way beyond installation. WorkOS Skills make your coding agent a WorkOS expert. workos seed defines your environment as code. workos doctor finds and fixes misconfigurations. And once you're authenticated, your agent can manage users, orgs, and environments directly from the terminal. No more ClickOps. 
 See how it works → 
 GitHub built an AI agent that can fix documentation, write tests, and refactor code while you sleep. Then they designed their entire security architecture around the assumption that this agent might try to steal your API keys, spam your repository with garbage, and leak your secrets to the internet. 
 This can be considered paranoia, but it’s the only responsible way to put a non-deterministic system inside your CI/CD pipeline. 
 GitHub Agentic Workflows let you plug AI agents into GitHub Actions so they can triage issues, generate pull requests, and handle routine maintenance without human supervision. The appeal is clear, but so is the risk. These agents consume untrusted inputs, make decisions at runtime, and can be manipulated through prompt injection, where carefully crafted text tricks the agent into doing things it wasn’t supposed to do. 
 In this article, we will look at how GitHub built a security architecture that assumes the agent is already compromised. However, to understand their solution, you first need to understand why the problem is harder than it looks. 
 Disclaimer: This post is based on publicly shared details from the GitHub Engineering Team. Please comment if you notice any inaccuracies. 
 Why Agents Break the CI/CD Contract 
 CI/CD pipelines are built on a simple assumption. The developers define the steps, the system runs them, and every execution is predictable. All the components in a pipeline share a single trust domain, meaning they can all see the same secrets, access the same files, and talk to the same network. That shared environment is actually a feature for traditional automation. When every component is a deterministic script, sharing a trust domain makes everything composable and fast. 
 Agents break that assumption completely because they don’t follow a fixed script. They reason over repository state, consume inputs they weren’t specifically designed for, and make decisions at runtime. A traditional CI step either does exactly what you coded it to do or fails. An agent might do something you never anticipated, especially if it processes an input designed to manipulate it. 
 GitHub’s threat model for Agentic Workflows is blunt. 
 They assume the agent will try to read and write state that it shouldn’t, communicate over unintended channels, and abuse legitimate channels to perform unwanted actions. For example, a prompt-injected agent with access to shell commands can read configuration files, SSH keys, and Linux /proc state to discover credentials. It can scan workflow logs for tokens. Once it has those secrets, it can encode them into a public-facing GitHub object like an issue comment or pull request for an attacker to retrieve later. The agent isn’t actively malicious, but following instructions that it couldn’t distinguish between legitimate ones. 
 In a standard GitHub Actions setup, everything runs in the same trust domain on top of a runner virtual machine. A rogue agent could interfere with MCP servers (the tools that extend what an agent can do), access authentication secrets stored in environment variables, and make network requests to arbitrary hosts. A single compromised component gets access to everything. The problem isn’t that Actions are insecure. It’s that agents change the assumptions that made a shared trust domain safe in the first place. 
 [Live on May 6] Stop babysitting your agents (Sponsored) 
 Agents can generate code. Getting it right for your system, team conventions, and past decisions is the hard part. You end up babysitting the agent and watch the token costs climb. 
 More MCPs, rules, and bigger context windows give agents access to information, but not understanding. The teams pulling ahead have a context engine to give agents only what they need for the task at hand. 
 Our April webinar filled up, so we are bringing it back! Join us live (FREE) on May 6 to see: 
 Where teams get stuck on the AI maturity curve and why common fixes fall short 
 How a context engine solves for quality, efficiency, and cost 
 Live demo: the same coding task with and without a context engine 
 Register now 
 Three Layers of Distrust 
 GitHub Agentic Workflows use a layered security architecture with three distinct levels. 
 Each layer limits the impact of failures in the layer above it by enforcing its own security properties independently. 
 The substrate layer sits at the bottom. It’s built on a GitHub Actions runner VM and several Docker containers, including a set of trusted containers that mediate privileged operations. This layer provides isolation between components, controls system calls, and enforces kernel-level communication boundaries. These protections hold even if an untrusted component is fully compromised and executes arbitrary code within its container. The substrate doesn’t rely on the agent behaving correctly, and even arbitrary code execution inside the agent’s container hits a wall at this level. 
 The configuration layer sits on top of the substrate layer. This is where the system’s structure gets defined. It includes declarative artifacts and the toolchains that interpret them to set up which components are loaded, how they’re connected, what communication channels are permitted, and what privileges are assigned. The most important piece in this layer is the compiler. GitHub doesn’t just run your workflow definition as-is, but compiles it into a GitHub Action with explicit constraints on permissions, outputs, auditability, and network access. The configuration layer also controls which secrets go into which containers. Externally minted tokens like agent API keys and GitHub access tokens are loaded only into the specific containers that need them, never into the agent’s container. 
 The planning layer sits on top. While the configuration layer dictates which components exist and how they communicate, the planning layer dictates which components are active over time. Its job is to create staged workflows with explicit data exchanges between stages. The safe outputs subsystem, which we’ll get to shortly, is the most important instance of this. It ensures the agent’s work gets reviewed before it affects anything real. 
 These layers are independent. If the planning layer fails, the configuration layer still enforces its constraints. If the configuration layer has a bug, the substrate layer still provides isolation. No single failure compromises the whole system. 
 Not Trusting Agents With Secrets 
 From the beginning, GitHub wanted workflow agents to have zero access to secrets. 
 In a standard GitHub Actions setup, sensitive material like agent authentication tokens and MCP server API keys sits in environment variables and configuration files visible to all processes on the runner VM. That’s fine when everything sharing the environment is trusted. It’s dangerous with agents because they’re susceptible to prompt injection. An attacker can hide malicious instructions in a web page, a repository issue, or a pull request comment, and trick the agent into extracting and leaking whatever it can find. 
 GitHub’s solution is a specific container topology where secrets are physically unreachable from the agent. 
 The agent runs in its own Docker container on a private network. All internet access goes through a dedicated firewall container (gh-aw-firewall). MCP tools are accessed through a separate trusted container called the MCP gateway (gh-aw-mcpg), which launches MCP servers and holds exclusive access to MCP authentication material like the GitHub Personal Access Token. LLM API calls go through an isolated API proxy that holds the model’s authentication token (like the Codex token). The agent communicates with the firewall over HTTP, the firewall connects to the MCP gateway over HTTP, and the gateway connects to MCP servers over stdio. 
 See the diagram below: 
 At no point in this chain does the agent touch a secret. It can make LLM calls because the proxy adds authentication on its behalf. It can use MCP tools because the gateway authenticates on its behalf. But the agent itself is completely secretless. 
 There’s a real tradeoff here, and GitHub names it explicitly. Coding workloads need broad access to compilers, interpreters, scripts, and repository state. But you can’t just install all those tools inside the agent’s container without expanding the set of network destinations allowed through the firewall and duplicating a lot of the host setup. 
 Their resolution is elegant, but they mount the entire VM host filesystem read-only at /host inside the agent’s container. Then they overlay sensitive paths (the ones containing secrets and configuration) with empty tmpfs layers, which are temporary in-memory filesystems that effectively hide whatever was at those paths. Finally, they launch the agent in a chroot jail rooted at /host. The result is that the agent can access every compiler, interpreter, and tool on the host machine while being unable to discover any secret material. The host-side setup stays intact. The agent’s writable and discoverable surface is constrained to only what it needs. If you work with containers, this pattern of mounting a host filesystem read-only and masking sensitive paths with tmpfs is applicable well beyond the agentic context. 
 GitHub isn’t the only one that arrived at this zero-secret principle. OpenAI’s Codex takes a different path to the same destination. In the Codex cloud, secrets are available only during the setup phase and are removed before the agent phase starts, and internet access is disabled by default during execution. GitHub uses proxies and gateways. OpenAI uses a two-phase model. The fact that both teams independently converged on “agents should never touch secrets” validates the principle. 
 Every Output Gets Vetted 
 Prompt-injected agents can cause real harm even without access to secrets. A rogue agent could spam a repository with pointless issues and pull requests to overwhelm maintainers, or inject objectionable URLs and content into repository objects. The absence of secrets doesn’t mean the absence of risk. 
 GitHub’s answer is the safe outputs system, and it’s the most distinctive part of their architecture. 
 Here’s how it works: 
 The agent can read GitHub state through the GitHub MCP server, which operates in read-only mode. But it cannot write to GitHub directly. All write operations go through a separate safe output MCP server, which only buffers the agent’s intended changes without executing them. 
 Once the agent finishes its work and exits, everything it staged goes through a deterministic analysis pipeline. 
 This pipeline does three things. 
 First, it checks the type of each operation against an allowlist that the workflow author defined. If the author said the agent can create issues and comments but not pull requests, any staged PR gets dropped. 
 Second, it enforces quantity limits. An agent might be restricted to creating at most three pull requests per run. 
 Third, it runs content sanitization, scanning for secrets that might have leaked into the output text, removing URLs, and running content moderation checks. 
 Only outputs that survive the entire pipeline get committed to GitHub. Every stage’s side effects are explicit and vetted. 
 The compiler plays an important role here, too. When it decomposes a workflow into stages, it defines for each stage the active components and their permissions (read versus write), the data artifacts that stage can emit, and the admissible downstream consumers of those artifacts. 
 The workflow author declares upfront what the agent is allowed to produce, and the system enforces those declarations deterministically. Since the pipeline uses deterministic analysis, it can only catch patterns that GitHub anticipated. A truly novel attack vector might slip through, which is exactly why the other layers exist. No single layer is the complete answer. 
 The Logging Strategy 
 Agents are determined to accomplish their tasks by any means and can have a surprisingly deep toolbox of tricks for doing so. When an agent behaves unexpectedly, you need full visibility into what happened. 
 Agentic Workflows make observability a first-class architectural property by logging at every trust boundary. 
 Network and destination-level activity gets recorded at the firewall. 
 Model request/response metadata and authenticated requests are captured by the API proxy. 
 Tool invocations are logged by the MCP gateway and MCP servers. 
 GitHub even adds internal instrumentation to the agent container to audit potentially sensitive actions like environment variable accesses. 
 Together, these logs support full forensic reconstruction, policy validation, and detection of anomalous behavior. 
 But there’s a more important long-term play here. Every point where you can observe communication is also a point where you can mediate it. GitHub is building the observation infrastructure now with future control in mind. They already support a lockdown mode for the GitHub MCP server, and they plan to introduce controls that enforce policies across MCP servers based on whether repository objects are public or private, and based on who authored them. 
 The Trade-Offs 
 Every security decision GitHub made came with a cost. 
 Security versus utility is the most obvious tension. Agents running inside GitHub’s architecture are more constrained than a developer working locally. The chroot approach gives agents access to host tools, but the firewall still limits network access, and the safe outputs pipeline still restricts what the agent can produce. In other words, more security means less flexibility. 
 Strict-by-default is a strong opinion. Most other coding agents make sandboxing opt-in. Claude Code and Gemini CLI both require you to turn on their sandbox features. GitHub Agentic Workflows run in strict security mode by default. That’s a deliberate choice to prioritize safety over developer convenience, and it won’t be the right tradeoff for every use case. 
 Prompt injection remains fundamentally unsolved. GitHub’s architecture is a damage containment strategy, not a prevention strategy. It limits the blast radius when an agent gets tricked, but it can’t prevent the issue itself. And the deterministic vetting in the safe outputs pipeline can only catch patterns that were anticipated. A novel attack vector might need a new pipeline stage. 
 The architecture is also complex, involving multiple containers, proxies, gateways, a compilation step, and a staged output pipeline. This is engineering overhead that makes sense at GitHub’s scale. For simpler use cases, we might not need every piece. 
 Conclusion 
 As AI agents become standard in development tooling, the question will shift from whether to sandbox to building a complete security architecture. 
 GitHub’s four principles offer a transferable framework: 
 Defend in depth with independent layers. 
 Keep agents away from secrets by architecture, not policy. 
 Vet every output through deterministic analysis before it affects the real world. 
 Log everything at every trust boundary, because today’s observability is tomorrow’s control plane. 
 References: 
 Under the hood: Security Architecture of GitHub Agentic Workflows
```

---

## 15. EP211: How the JVM Works

- 日期: 2026-04-18 15:30
- 链接: https://blog.bytebytego.com/p/ep211-how-the-jvm-works

```
This week’s system design refresher: 
 AI for Engineering Leaders: Course Direction Survey 
 What is a Data Lakehouse? (Youtube video) 
 How the JVM Works 
 Figma Design to Code, Code to Design: Clearly Explained 
 12 AI Papers that Changed Everything 
 How Load Balancers Work? 
 Optimistic locking vs pessimistic locking 
 AI for Engineering Leaders: Course Direction Survey 
 We are working on a course, AI for Engineering Leaders, and would appreciate your help with a quick survey. 
 Before we build it, we want to get it right, so we’re asking the people who would actually take it. If you’re an EM, Tech Lead, Director, or VP of Engineering, I’d love 3 minutes of your time. This quick survey covers questions like: how do you evaluate engineers when AI writes most of the code? What metrics still matter? Where do AI tools actually help versus just add noise? 
 Your answers will directly shape what we cover. Thank you! 
 Fill out the short form now 
 What is a Data Lakehouse? 
 How the JVM Works 
 We compile, run, and debug Java code all the time. But what exactly does the JVM do between compile and run? 
 Here's the flow: 
 Build: javac compiles your source code into platform-independent bytecode, stored as .class files, JARs, or modules. 
 Load: The class loader subsystem brings in classes as needed using parent delegation. Bootstrap handles core JDK classes, Platform covers extensions, and System loads your application code. 
 Link: The Verify step checks bytecode safety. Prepare allocates static fields with default values, and Resolve turns symbolic references into direct memory addresses. 
 Initialize: Static variables are assigned their actual values, and static initializer blocks execute. This happens only the first time the class is used. 
 Memory: Heap and Method Area are shared across threads. The JVM stack, PC register, and native method stack are created per thread. The garbage collector reclaims unused heap memory. 
 Execute: The interpreter runs bytecode directly. When a method gets called multiple times, the JIT compiler converts it to native machine code and stores it in the code cache. Native calls go through JNI to reach C/C++ libraries. 
 Run: Your program runs on a mix of interpreted and JIT-compiled code. Fast startup, peak performance over time. 
 Figma Design to Code, Code to Design: Clearly Explained 
 We spoke with the Figma team behind these releases to better understand the details and engineering challenges. This article covers how Figma’s design-to-code and code-to-design workflows actually work, starting with why the obvious approaches fail, how MCP solves them, and the engineering challenges that remain. 
 At the high level: 
 Design to Code: 
 Step 1: Once the user provides a Figma link and prompt, the coding agent requests the list of available tools from Figma’s MCP server. 
 Step 2: The server returns its tools: get_design_context, get_metadata, and more. 
 Step 3: The agent calls get_design_context with the file key and node ID parsed from the URL. 
 Step 4: The MCP server returns a structured representation including layout and styles. The agent then generates working code (React, Vue, Swift, etc.) using that structured context. 
 Code to Design: 
 Step 1: Once the user provides the desired UI code, the agent discovers available tools from the MCP server. 
 Step 2: The agent calls generate_figma_design with the current UI code. 
 Step 3: The MCP tool opens the running UI in a browser and injects a capture script. 
 Step 4: The user selects the desired component, and the script sends the selected DOM data to the server. 
 Step 5: The server maps the DOM to native Figma layers: frames, auto-layout groups, and editable text layers. The result is fully editable Figma layers shown to the user. 
 Read the full newsletter here. 
 12 AI Papers that Changed Everything 
 A handful of research papers shaped the entire AI landscape we see today. 
 The diagram below highlights 12 that we consider especially influential. 
 AlexNet (2012): Showed deep neural nets can see. Ignited the deep learning era 
 GANs (2014): Generate realistic image by having two networks compete 
 Transformer (2017): Google's "Attention Is All You Need." The architecture behind everything 
 GPT-3 (2020): OpenAI showed scale unlocks emergent abilities. 
 InstructGPT (2022): OpenAI introduced RLHF. Turned raw LLMs into useful assistants. 
 Scaling Laws (2020): Loss follows a clean power law 
 ViT (2020): Split images into patches and use a Transformer for vision tasks. 
 Latent Diffusion (2021): Denoising in compressed space. The design behind DALL·E. 
 DDPM (2020): Add noise, then learn to reverse it. The foundation behind diffusion models. 
 CLIP (2021): OpenAI connected images and text in one shared space. 
 Chain-of-Thought (2022): A simple prompt that unlocked complex reasoning. 
 RAG (2020): Retrieve real documents, then generate. Grounded LLMs in facts. 
 Over to you: What paper is missing from this list? 
 How Load Balancers Work? 
 A load balancer is a system that distributes incoming traffic across multiple servers to ensure no single server gets overloaded. Here’s how it works under the hood: 
 The client sends a request to the load balancer. 
 A listener receives it on the right port/protocol (HTTP/HTTPS, TCP). 
 The load balancer parses the packet to understand headers and intent. 
 It checks recent health checks to know which backend servers are up. 
 It looks in the connection table to reuse any existing client-to-server mapping. 
 Using its rules, it picks a healthy target server for this request. 
 It rewrites addresses so traffic can reach that chosen server. 
 It completes the TCP handshake to open a reliable connection. 
 If HTTPS is used, it decrypts (or passes through) via SSL/TLS as configured. 
 The request is forwarded to the selected backend server. 
 The backend processes it and sends a response back to the load balancer. 
 The load balancer may tweak headers, then forwards the response to the client. 
 Over to you: Which other step will you add to the working of a load balancer? 
 Optimistic locking vs pessimistic locking 
 Imagine two developers updating the same database row at the same time. One of them will have their update rejected. How should the system handle this? 
 There are two common approaches. 
 Optimistic locking assumes conflicts are rare. Both users read the data without acquiring any lock. Each record carries a version number. When a user attempts to write, the database checks: does the version in your update match the current version in the database? If another transaction already incremented the version from 1 to 2, your update still references version 1. The write is rejected. 
 Pessimistic locking takes the opposite approach. It assumes conflicts are likely, so it blocks them before they happen. The first transaction locks the row, and every other transaction waits until that lock is released. No version checks needed. 
 If your system is read-heavy with occasional writes, optimistic locking is the best option. When concurrent writes occur frequently and the cost of a conflict is high, pessimistic locking is the safer choice. 
 Over to you: Have you ever run into a deadlock in production because of a locking strategy? How did you fix it?
```

---

## 16. A Guide to Relational Database Design

- 日期: 2026-04-16 15:31
- 链接: https://blog.bytebytego.com/p/a-guide-to-relational-database-design

```
The hardest part of relational database design is not using SQL. The syntax for creating tables, defining keys, and writing joins can be learnt and mastered over time. The difficult part is to develop the thinking that comes before any code gets written, and answering questions about the design of the database. 
 Which pieces of information deserve their own table? 
 How should tables reference each other? 
 How much redundancy is too much? 
 These are design decisions, and getting them right means our data stays consistent, our queries stay fast, and changes are painless. Getting them wrong means spending months patching problems that were baked into the structure from day one. 
 In this article, we cover the core concepts that inform those decisions. We’ll look at tables, keys, relationships, normalization, and joins, with each concept building on the last. 
 Tables and the Language That Drives Them 
 Read more
```

---

## 17. Figma Design to Code, Code to Design: Clearly Explained

- 日期: 2026-04-14 15:31
- 链接: https://blog.bytebytego.com/p/figma-design-to-code-code-to-design

```
Are your AI investments paying off? (Sponsored) 
 AI budgets are under the microscope and most engineering teams only cite time savings from code generation when asked if it’s working. 
 The real impact is in production, where teams spend 70% of engineering time investigating incidents, jumping between tools, and losing time that could go toward shipping product. 
 That operational load only grows with every line of AI-generated code that hits prod. 
 Learn how engineering teams at Coinbase, Zscaler, and Salesforce are seeing AI impact across the full engineering lifecycle. Plus, get a practical worksheet for modeling AI ROI with your own operational data. 
 Get the free playbook → 
 Turning a design into working code is one of the most common tasks in frontend development, and one of the hardest to automate. The design lives in Figma. The code lives in a repository. Bridging the two has traditionally required a developer to manually interpret layouts, colors, spacing, and component structure from a visual reference. AI coding agents promise to close that gap, but the naive approaches fall short in important ways. 
 Figma launched its MCP server in June 2025 to bring design context into code. This year, they released two new workflows: the ability to generate designs from coding tools like Claude Code and Codex, and the ability for agents to write directly to Figma design. 
 We spoke with Emil Sjölander , Aditya Muttur , and Shannon Toliver from the Figma team behind these releases to understand the details and engineering challenges. This article covers how Figma’s design-to-code and code-to-design workflows actually work, starting with why the obvious approaches fail, how MCP solves them, and the engineering challenges that remain. 
 The Gap Between Design and Code 
 Before diving into how Figma’s MCP server works, it helps to understand the approaches that came before it, and why each one hits a wall. There are two natural ways to give an LLM access to a design: show it a picture, or hand it the raw data. Both have fundamental limitations that motivated a different approach. 
 Approach 1: Screenshot the design 
 The most obvious way to turn a design into code with an LLM is to take a screenshot of your Figma file and paste it into a coding agent. The LLM sees the image, interprets the layout, and generates code. 
 This works for simple UIs. But it breaks down for anything complex. The LLM has to guess values based on pixels. It doesn’t know the exact color or that the spacing between cards is 24px, not 20px. The output may look close, but not identical. 
 Figure 1: The LLM guesses pixel values from a screenshot. 
 So screenshots give the LLM a visual reference but no precise values. The next natural step is to go in the opposite direction: give it all the data. 
 Approach 2: Get Design JSON via Figma’s API 
 Figma exposes a REST API that returns a file’s entire structure as JSON. Every node, property, and style is included. Now the LLM has real data instead of pixels. 
 Figure 2: The REST API returns the full file structure as JSON 
 But having all the data introduces its own problem: there is far too much of it. A single Figma page can produce thousands of lines of JSON, filled with pixel coordinates, visual effects, internal layout rules, and other metadata that are not useful for code generation. Dumping all of this into a prompt can exceed the context window. Even when it fits, the LLM has to wade through pixel coordinates, blend modes, export settings, and other visual metadata that have nothing to do with building a UI, which degrades the output quality. 
 Figure 3: Raw JSON exceeds the context window and degrades output quality 
 Neither approach works on its own. Screenshots lack precision. Raw API data has precision but drowns the LLM in noise. What you actually need is something in between: structured design data that preserves exact values like colors, spacing, and component names, but strips out the noise that is not needed for code generation. 
 The middle ground: Figma’s MCP server 
 That is what Figma’s MCP server does. MCP stands for Model Context Protocol, a standard that defines how AI agents discover and call external tools. Figma’s MCP server takes the raw design data from Figma’s REST API, filters out the noise, and transforms what remains into a clean, structured representation. Pixel positions become layout relationships like “centered inside its parent.” Raw hex colors become design token references. Deeply nested layers get flattened to match what a developer would actually build. The result is a compact, token-efficient context that an LLM can act on directly. 
 With that context, let’s look at how the two main workflows, design to code and code to design, actually work under the hood. 
 Design to Code 
 The design-to-code workflow starts when a developer selects a frame in Figma, copies its URL, and pastes it into a coding agent like Claude Code or Codex with a prompt like “Implement this design.” The agent then produces working code that matches the design. Here is what happens behind the scenes. 
 Figure 4: Design to code workflow 
 The coding agent and Figma’s MCP server work together through four steps. The first two are generic MCP mechanics: tool discovery and tool calling. The last two are where Figma’s engineering makes the difference. 
 Step 1. The agent discovers available tools 
 When you first connect the Figma MCP server, the agent receives a list of available tools. These include get_design_context, get_screenshot, get_metadata, and more. Each tool comes with a name, description, and parameter schema. 
 Figure 5: Each MCP tool has a name, description, and parameter schema 
 The agent does not know how Figma works internally. It reads these descriptions the same way a developer reads API documentation, then decides which tool to call based on the user’s prompt. 
 Figure 6: The agent picks the right tool by matching the user’s intent to tool descriptions. 
 Step 2. The agent prepares the arguments and calls the tool 
 The agent prepares the arguments to call the selected tool. In this case, since the selected tool is get_design_context, it needs a file key and a node ID. So it parses both from the Figma URL you pasted and calls the tool. 
 Figure 7: The agent calls the get_design_context tool with the parsed arguments 
 Step 3. The request hits Figma’s backend 
 The tool call is sent over the network to Figma’s MCP server at mcp.figma.com/mcp over Streamable HTTP. The MCP server handles authentication, then calls Figma’s internal services to read the design data such as node trees, component properties, styles, and variable definitions. 
 Step 4. Transform raw design data into LLM-friendly context 
 This is where the most important engineering happens. The MCP server transforms the raw JSON from Figma’s REST API into a structured representation that maps to how a developer thinks about building a UI. Pixel positions become layout relationships like “this element is centered inside its parent.” Color values become references to design tokens like brand-blue instead of raw color codes. Deeply nested layers get simplified to reflect what the user actually sees. And components get enriched with code mappings. For example, when a Figma button component is mapped to src/components/ui/Button.tsx through Code Connect, that reference appears in the output. The LLM reuses the existing component instead of recreating it from scratch. 
 Figure 8: The MCP server transforms raw Figma JSON into a structured representation 
 The output defaults to a React + Tailwind framing because that is the most common frontend stack. But it is a structured representation of the design, not generated code. The LLM takes this representation and generates actual code in whatever framework the developer specifies. 
 Figure 9: The LLM uses the representation to generate actual code 
 Code to Design 
 Design to code is only half the story. In practice, the code often evolves faster than the design files. A developer ships a feature, tweaks the layout based on user feedback, adds a new section, and now the Figma file no longer matches what is actually running in production. Code to design closes that gap. A developer opens Claude Code, types “send this to Figma,” and a few seconds later the live UI appears in Figma as fully editable layers. Not a flat screenshot, but real frames with auto-layout, editable text, and separate components. 
 Figure10: Figma’s MCP server enables a bidirectional loop. 
 This is powered by one key tool in the MCP server: generate_figma_design. Here is what happens under the hood. 
 Step 1: The Figma tool launches the capture tool 
 When the developer prompts “send this to Figma,” the agent calls MCP server’s generate_figma_design tool. 
 Figure 11: coding agents picks generate_figma_design and calls it 
 The tool opens the target URL in a browser and injects a JavaScript capture script. For a local dev server, it connects directly. For production or staging URLs, it uses a browser automation tool like Playwright to open the page and inject the script programmatically. 
 When the browser window opens, two things appear: the running UI and a capture toolbar overlay. An initial capture happens automatically when the page loads. From there, the developer can capture the entire screen or select specific elements. 
 Figure 12: A capture toolbar overlays the running UI 
 Step 2: The script reads the DOM 
 When the user selects the desired UI from the live capture, the injected script does not take a screenshot. It reads the live DOM. 
 It walks the DOM tree and extracts computed styles, layout properties, text content, and image sources for every visible element. It also preserves the parent-child hierarchy. A flex container with three children stays structured as a container with three children, not a flat collection of boxes. 
 Figure 13: The injected script walks the live DOM tree and extracts selected properties 
 This is what makes the output editable in Figma. A screenshot captures pixels. The DOM walk captures structure and relationships between elements. 
 Step 3: DOM data becomes Figma layers 
 The captured DOM data gets sent to Figma’s backend, where it is reconstructed as native Figma design layers. Each HTML element maps to a Figma frame or shape. CSS flexbox and grid layouts become Figma auto-layout groups. Text nodes become editable Figma text layers with the correct font, size, weight, and color. Images get extracted and embedded as image fills. 
 Figure 14: Each HTML element maps to a native Figma layer 
 That covers the two core workflows. But making them work reliably in production, across millions of Figma files, multiple coding agents, and real design systems, introduces a different set of problems. 
 Engineering Challenges 
 Here are some of the most important challenges Figma’s team faced, and how they addressed them. 
 Challenge 1: Context window limits 
 LLMs have fixed context windows, so token count is a hard constraint. The design data for a complex Figma page can be enormous, far more than what a coding agent can handle in a single call. Claude Code, for example, defaults to a 25,000-token limit for MCP tool responses. If you call get_design_context on an entire page instead of a specific node, the response can easily exceed that limit and get truncated. This challenge is not unique to Figma. Any MCP server that exposes large structured data like a codebase, a document store, or a design file, has to solve the same problem: how to give the LLM enough context to be useful without exceeding what it can process. 
 Figure 15: First scan the outline with get_metadata, then zoom into specific nodes. 
 To mitigate this, Figma developed the get_metadata tool. Instead of the full styled representation, it returns a sparse XML outline. A developer can call get_metadata on an entire page to see the structure, identify the specific nodes they need, and then call get_design_context only on those nodes. It is a two-step pattern: scan first, then zoom in. 
 Challenge 2: Component mapping 
 By default, the coding agent has no way to know which Figma components map to which code components. Without that mapping, the agent will spend time searching the codebase to find the right component. If it does not find a match, it will create a new one from scratch. Multiply that across every reusable component in a design system, and the generated code diverges from the codebase fast. 
 Figma mitigates this with Code Connect, which lets teams create explicit mappings between Figma node IDs and code file paths. Once set up, the MCP server includes these mappings in its response, and the agent reuses the actual component instead of guessing. 
 Figure 16: Code Connect creates explicit mappings between Figma components and code files 
 Setting up Code Connect requires manual effort. Someone has to create and maintain those mappings. Figma has been working to reduce this friction with tools like get_code_connect_suggestions, which automatically detects and proposes mappings. But the quality of the generated code is still directly tied to how much the team has invested in connecting their design system to their codebase. 
 Challenge 3: The lossy roundtrip 
 The bidirectional loop sounds seamless, but each handoff loses information. When a design goes from Figma to code, the structured context captures layout, styles, and component references, but not business logic, event handlers, state management, or API calls. The agent fills those in when generating code. 
 When that code gets captured back to Figma through generate_figma_design, the DOM walk captures visual structure and styles but strips out everything that is not visible: the React state, the API integration, the route handling. 
 Figure 17: The design ↔ code roundtrip is not lossless. Each handoff strips some information 
 The result is that each roundtrip requires re-inference. When a designer modifies a captured UI in Figma and a developer pulls it back into code with get_design_context, the agent is translating visual decisions into implementation from scratch. It does not have access to the previous version of the code. Code Connect mappings help here by preserving the link between design components and their code implementations across roundtrips, but the non-visual logic still has to be re-added each time. 
 Challenge 4: Serving multiple agents with different capabilities 
 Figma’s MCP server does not serve a single client. It serves Claude Code, Cursor, Codex, and any other MCP-compatible tool. Each agent has different context window sizes, different tool-calling behaviors, and different levels of sophistication in how it sequences multiple tool calls. A workflow that works well in one agent may not work the same way in another. 
 Figure 18: Different agents have different context limits and tool-calling capabilities. 
 The generate_figma_design tool, for instance, is now available in a growing number of coding tools, including Claude Code and Codex. Code-to-design requires tighter integration with the browser (script injection, capture toolbar, multi-screen state) than most agents currently support. 
 Building an MCP server that works well across a growing ecosystem of agents with varying capabilities is one of the harder ongoing challenges in this space. 
 The recent opening of the Figma canvas to agents marks an important evolution in this workflow. Agents can now not only read and understand design context, but actively modify and create designs using the use_figma MCP tool. This tool complements the design-to-code workflow by enabling agents to edit designs directly on the Figma canvas and create new assets using your components and variables. 
 What’s Next? 
 The hardest part of building an MCP server is not implementing the protocol. It is making the design decisions that Figma’s team had to work through: what context to include, what to leave out, how to structure it so LLMs can reason about it, and how to stay within token budgets. Those decisions are what separate a useful MCP server from one that just wraps an existing API. 
 Figma’s server is a useful reference point not because of the design tool specifics, but because the design decisions behind it like what to include, how to structure it, and how to handle token budgets, are well-documented and applicable to anyone building an MCP server for a complex domain.
```

---

## 18. How LinkedIn Feed Uses LLMs to Serve 1.3 Billion Users

- 日期: 2026-04-13 15:31
- 链接: https://blog.bytebytego.com/p/how-linkedin-feed-uses-llms-to-serve

```
How to stop babysitting your agents (Sponsored) 
 Agents can generate code. Getting it right for your system, team conventions, and past decisions is the hard part. You end up babysitting the agent and watch the token costs climb. 
 More MCPs, rules, and bigger context windows give agents access to information, but not understanding. The teams pulling ahead have a context engine to give agents only what they need for the task at hand. 
 Join us for a FREE webinar on April 23 to see: 
 Where teams get stuck on the AI maturity curve and why common fixes fall short 
 How a context engine solves for quality, efficiency, and cost 
 Live demo: the same coding task with and without a context engine 
 If you want to maximize the value you get from AI agents, this one is worth your time. 
 Register now 
 LinkedIn used to run five separate systems just to decide which posts to show you. One tracked trending content. Another did collaborative filtering. A third handled embedding-based retrieval. 
 Each had its own infrastructure, its dedicated team, and its own optimization logic. The setup worked, but when the Feed team wanted to improve one part, they’d break another. Therefore, they made a radical bet and ripped out all five systems, replacing them with a single LLM-powered retrieval model. That solved the complexity problem, but it raised new questions, such as: 
 How do you teach an LLM to understand structured profile data? 
 How do you make a transformer serve predictions in under 50 milliseconds for 1.3 billion users? 
 How do you train the model when most of the data is noise? 
 In this article, we will look at how the LinkedIn engineering team rebuilt the Feed and the challenges they faced. 
 Disclaimer: This post is based on publicly shared details from the LinkedIn Engineering Team. Please comment if you notice any inaccuracies. 
 Five Librarians, One Library 
 For years, LinkedIn’s Feed retrieval relied on what engineers call a heterogeneous architecture. When you opened the Feed, content came from multiple specialized sources running in parallel. 
 A chronological index of network activity. 
 Trending posts by geography. 
 Collaborative filtering based on similar members. 
 Industry-specific pipelines. 
 Several embedding-based retrieval systems. 
 Each maintained its own infrastructure, index structure, and optimization strategy. 
 See the diagram below: 
 This architecture surfaced diverse, relevant content. But optimizing one retrieval source could degrade another, and no team could tune across all sources simultaneously. Holistic improvement was nearly impossible. 
 So the Feed team asked a simple question. What if they replaced all of these sources with a single system powered by LLM-generated embeddings? 
 Under the hood, this works through a dual encoder architecture. A shared LLM converts both members and posts into vectors in the same mathematical space. The training process pushes member and post representations close together when there’s genuine engagement, and pulls them apart when there isn’t. When you open your Feed, the system fetches your member embedding and runs a nearest-neighbor search against an index of post embeddings, retrieving the most relevant candidates in under 50 milliseconds. 
 However, the real power comes from what the LLM brings to those embeddings. Traditional keyword-based systems rely on surface-level text overlap. If your profile says “electrical engineering” and a post is about “small modular reactors,” a keyword system misses the connection. 
 An LLM-based system understands that these topics are related because the model carries world knowledge from pretraining. It knows that electrical engineers often work on power grid optimization and nuclear infrastructure. This is especially powerful for cold-start scenarios, when a new member joins with just a profile headline. The LLM can infer likely interests without waiting for engagement history to accumulate. 
 The downstream benefits compounded the benefits. Instead of receiving candidates from disparate sources with different biases, the ranking layer now receives a coherent candidate set selected through the same semantic similarity. Ranking became easier, and each optimization to the ranking model became more effective. 
 But replacing five systems with one LLM created a new problem. LLMs expect text, and recommendation systems run on structured data and numbers. 
 The Model Is Only As Good As Its Input 
 To feed structured data into an LLM, LinkedIn built a “prompt library” that transforms structured features into templated text sequences. For posts, it includes author information, engagement counts, and post text. For members, it incorporates profile information, skills, work history, and a chronologically ordered sequence of posts they’ve previously engaged with. Think of it as prompt engineering for recommendation systems. 
 The most striking example is what happened with numerical features. Initially, LinkedIn passed raw engagement counts directly into prompts. For example, a post with 12,345 views would appear as “views:12345” in the text. The model treated those digits like any other text tokens. When the team measured the correlation between item popularity counts and embedding similarity scores, they found it was essentially zero (-0.004). Popularity is one of the strongest relevance signals in recommendation. And the model was completely ignoring it. 
 The problem is fundamental. LLMs don’t understand magnitude. They process “12345” as a sequence of digit tokens, not as a quantity. 
 The fix was quite simple. Instead of passing raw counts, LinkedIn converted them into percentile buckets wrapped in special tokens. This meant that “Views:12345” became <view_percentile>71</view_percentile>, indicating this post sits in the 71st percentile of view counts. Most values between 1 and 100 get processed by the LLM as a single unit rather than a multi-digit sequence, giving the model a stable, learnable vocabulary for quantity. The model can learn that anything above 90 means “very popular” without trying to parse arbitrary digit sequences. 
 The correlation between popularity features and embedding similarity jumped 30x. Recall@10, which measures whether the top 10 retrieved posts are actually relevant, improved by 15%. LinkedIn applied the same strategy to engagement rates, recency signals, and affinity scores. 
 Less Data, Better Model 
 When building the member’s interaction history for training, LinkedIn initially included everything. Every post that was shown to a member went into the sequence, whether they engaged with it or scrolled past. The idea was that more data should mean a better model. 
 However, this didn’t turn out to be the case. Including scrolled-past posts not only made model performance worse, but it also made training significantly more expensive. GPU compute for transformer models scales quadratically with context length. 
 When the team filtered to include only positively-engaged posts, the results improved across every dimension. 
 Memory footprint per sequence dropped by 37%. 
 The system could process 40% more training sequences per batch. 
 Training iterations ran 2.6x faster 
 The reason comes down to signal clarity. A scrolled-past post is ambiguous. Maybe the post was irrelevant. Maybe the member was busy. Maybe the headline was mildly interesting, but not enough to stop for. Posts you actively chose to engage with are a much cleaner learning target. 
 The gains compounded due to this change. Better signal quality meant faster training. Faster training meant more experimentation. More experimentation meant better hyperparameter tuning. When a single change improves both quality and efficiency, the benefits multiply through the entire development cycle. 
 The training strategy had one more clever element. LinkedIn used two types of negative examples: 
 Easy negatives were randomly sampled posts never shown to a member, providing a broad contrastive signal. 
 Hard negatives were posts actually shown but not engaged with, the almost-right cases where the model must learn nuanced distinctions between relevant and genuinely valuable. 
 The difficulty of the negative examples shapes what the model learns. Easy negatives teach broad distinction, whereas hard negatives teach the fine-grained ones. Using both together is a common and effective pattern across retrieval systems, and at LinkedIn, adding just two hard negatives per member improved recall by 3.6%. 
 With retrieval producing high-quality candidates, the next question was how to rank them. LinkedIn’s answer was to stop treating each post as an isolated decision. 
 The Feed Is a Story, Not a Snapshot 
 Traditional ranking models evaluate each member-post pair independently. This works, but it misses something fundamental about how professionals consume content. 
 LinkedIn built a Generative Recommender (GR) model that treats your Feed interaction history as a sequence. Instead of scoring each post in isolation, GR processes more than a thousand of a user’s historical interactions to understand temporal patterns and long-term interests. 
 The practical difference matters. If the user engages with machine learning content on Monday, distributed systems on Tuesday, and opens LinkedIn again on Wednesday, a sequential model understands these aren’t random events. They’re the continuation of a learning trajectory. A traditional pointwise model sees three independent decisions, whereas the sequential model sees the story. 
 The GR model uses a transformer with causal attention, meaning each position in the history can only attend to previous positions, mirroring how you actually experienced content over time. Recent posts might matter more for predicting immediate interests, but a post from two weeks ago might suddenly become relevant if recent activity suggests renewed interest. 
 See the diagram below that shows the transformer architecture: 
 One of the most practical architectural decisions is what LinkedIn calls late fusion. Not every feature benefits from full self-attention. Count features and affinity signals carry a strong independent signal, and running them through the transformer would inflate computational cost quadratically without clear benefit. Instead, these features are concatenated with the transformer output after sequence processing. This results in rich sequential understanding from the transformer, plus contextual signals that drive relevance, without the cost of processing them through self-attention. 
 The serving challenge is equally important. Processing 1,000+ historical interactions through multiple transformer layers for every ranking request is expensive. LinkedIn’s solution is shared context batching. The system computes the user’s history representation once, then scores all candidates in parallel using custom attention masks. 
 On top of the transformer, a Multi-gate Mixture-of-Experts (MMoE) prediction head routes different engagement predictions like clicks, likes, comments, and shares through specialized gates while sharing the same sequential representations underneath. 
 See the diagram below that shows a typical Mixture-of-Experts architecture. 
 This lets the model handle multiple prediction tasks without duplicating the expensive transformer computation. Together, shared context batching and the MMoE head are what make the sequential model viable at production scale. 
 Making It All Work at Scale 
 Even the best model is useless without the infrastructure to serve it. LinkedIn’s historical ranking models ran on CPUs. Transformers are fundamentally different, with self-attention scaling quadratically with sequence length and massive parameter counts requiring GPU memory. At LinkedIn’s scale, cost-per-inference determines whether sophisticated AI models can serve every member, or only high-engagement users. 
 The team invested heavily in custom infrastructure on both sides. For training, a custom C++ data loader eliminates Python’s multiprocessing overhead, custom GPU routines reduced metric computation from a bottleneck to negligible overhead, and parallelized evaluation across all checkpoints cut pipeline time substantially. For serving, a disaggregated architecture separates CPU-bound feature processing from GPU-heavy model inference, and a custom Flash Attention variant called GRMIS delivered an additional 2x speedup over PyTorch’s standard implementation. 
 See the diagram below that shows the GR Infrastructure Stack 
 Freshness required its own solution. 
 Three continuously running background pipelines keep the system current, capturing platform activity, generating updated embeddings through LLM inference servers, and ingesting them into a GPU-accelerated index. 
 Each pipeline optimizes independently, while the end-to-end system stays fresh within minutes. LinkedIn’s models are also regularly audited to ensure posts from different creators compete on an equal footing, with ranking relying on professional signals and engagement patterns, never demographic attributes. 
 Conclusion 
 There are some takeaways: 
 Replacing five retrieval systems with one trades resilience for simplicity. 
 LLM-based embeddings are richer but more expensive than lightweight alternatives. 
 The bottleneck is rarely the model architecture. It’s everything around it. 
 The infrastructure investment represents an effort most teams can’t replicate. And this approach leans on LinkedIn’s rich text data. For primarily visual platforms, the calculus would be different. 
 The next time you open LinkedIn and see a post from someone you don’t follow, on a topic you didn’t search for, but it’s exactly what you needed to read, that’s all of this working together under the hood. 
 References: 
 Engineering the next generation of LinkedIn’s Feed
```

---

## 19. EP210: Monolithic vs Microservices vs Serverless

- 日期: 2026-04-11 15:30
- 链接: https://blog.bytebytego.com/p/ep210-monolithic-vs-microservices

```
✂️ Cut your QA cycles down to minutes with QA Wolf (Sponsored) 
 If slow QA processes bottleneck you or your software engineering team and you’re releasing slower because of it — you need to check out QA Wolf. 
 QA Wolf’s AI-native service supports web and mobile apps , delivering 80% automated test coverage in weeks and helping teams ship 5x faster by reducing QA cycles to minutes. 
 QA Wolf takes testing off your plate. They can get you: 
 Unlimited parallel test runs for mobile and web apps 
 24-hour maintenance and on-demand test creation 
 Human-verified bug reports sent directly to your team 
 Zero flakes guarantee 
 The benefit? No more manual E2E testing. No more slow QA cycles. No more bugs reaching production. 
 With QA Wolf, Drata’s team of 80+ engineers achieved 4x more test cases and 86% faster QA cycles . 
 Schedule a demo to learn more 
 This week’s system design refresher: 
 Monolithic vs Microservices vs Serverless 
 CLI vs MCP 
 Comparing 5 Major Coding Agents 
 Essential AWS Services Every Engineer Should Know 
 JWT Visualized 
 Monolithic vs Microservices vs Serverless 
 A monolith is usually one codebase, one database, and one deployment. For a small team, that’s often the simplest way to build and ship quickly. The problem arises when the codebase grows. A tiny fix in the cart code requires redeploying the whole app, and one bad release can take down everything with it. 
 Microservices try to solve that by breaking the system into separate services. Product, Cart, and Order run on their own, scale separately, and often manage their own data. That means you can ship changes to Cart without affecting the rest of the system. 
 But now you are dealing with multiple moving parts. You generally need service discovery, distributed tracing, and request routing between services. 
 Serverless is a different model. Instead of managing servers, you write functions that run when something triggers them, and the cloud provider handles the scaling. In many cases, you only pay when those functions actually run. 
 However, in serverless, cold starts can add latency, debugging across lots of stateless functions can get messy, and the more you build around one cloud’s runtime, the harder it gets to switch later. 
 Most production systems don't use just one approach. There's usually a monolith at the core, and over time teams spin up a few services where they need independent scaling or faster deploys. Serverless tends to show up later for things like notifications or background jobs. 
 CLI vs MCP 
 AI agents need to talk to external tools, but should they use CLI or MCP? 
 Both call the same APIs under the hood. The difference is how the agent invokes them. 
 Here's a side-by-side comparison across 6 dimensions: 
 Token Cost: MCP loads the full JSON schema (tool names, descriptions, field types) into the context window before any work begins. CLI needs no schema, so saves more context window. 
 Native Knowledge: LLMs were trained on billions of CLI examples. MCP schemas are custom JSON the model encounters for the first time at runtime. 
 Composability: CLI tools chain with Unix pipes. Something like gh | jq | grep runs in a single LLM call. MCP has no native chaining. The agent must orchestrate each tool call separately. 
 Multi-User Auth: CLI agents inherit a single shared token. You can't revoke one user without rotating everyone's key. MCP supports per-user OAuth. 
 Stateful Sessions: CLI spawns a new process and TCP connection per command. MCP keeps a persistent server with connection pooling. 
 Enterprise Governance: CLI's only audit trail is ~/.bash_history. MCP provides structured audit logs, access revocation, and monitoring built into the protocol. 
 Over to you: For which use cases do you prefer CLI over MCP, or vice versa? 
 Comparing 5 Major Coding Agents 
 The diagram below compares the 5 leading agents across interface, model, context window, autonomy, and more. 
 Here's what the landscape tells us: 
 The terminal is the new IDE. Most coding agents now live in your terminal, not inside an editor. The command line is back. 
 Context windows are getting massive. We've gone from 8K tokens to 1M in just two years. Agents can now reason over entire codebases in a single prompt. 
 Autonomy is a spectrum. Some agents run fully async in the background. Others keep you in the loop on every edit. Teams are still figuring out how much to delegate. 
 Open source is gaining ground. The open-source coding agent ecosystem is maturing fast, giving teams full control over their toolchain. 
 Pricing varies wildly. From completely free (Gemini CLI, Deep Agents) to $15 per 1M output tokens. Check the cost row before you commit. 
 There is no single winner. The best agent depends on your workflow, budget, and how much autonomy you're comfortable with. 
 Over to you: Which coding agent is your daily driver in 2026? 
 Essential AWS Services Every Engineer Should Know 
 AWS has 200+ services, but most production systems only use a small subset. In many setups, a request ends up going through API Gateway, then an ALB, executes on Lambda or ECS, reads from DynamoDB, and gets cached in ElastiCache. 
 Each service on its own is straightforward. Deciding where it actually fits is where things get tricky. 
 EC2 and S3 are usually the starting point for a lot of people. But when things break, the focus shifts to services that didn’t get much attention early on, like CloudWatch for observability, IAM for access control, and KMS for encryption. 
 Networking tends to be where things get confusing. VPC, subnets, security groups, Route 53, and CloudFront run behind everything. When something is off, the errors don’t always help much. 
 Database choices are not easy to reverse later. RDS, DynamoDB, and Aurora solve different problems, and changing direction means redesigning a lot of what you've already built. It’s similar with the integration layer. SQS, SNS, and EventBridge each handle a different pattern (queuing vs fan-out vs event routing), and choosing the wrong one causes problems you notice when the system is under load. 
 SageMaker and Bedrock are newer services, but they're already part of the stack at many companies. SageMaker is for training and hosting models, and Bedrock is for calling foundation models directly. 
 CloudFormation lets you define infrastructure as code, and CodePipeline handles CI/CD. Once set up, deployments run without manual steps. 
 JWT Visualized 
 Imagine you have a special box called a JWT. Inside this box, there are three parts: a header, a payload, and a signature. 
 The header is like the label on the outside of the box. It tells us what type of box it is and how it's secured. It's usually written in a format called JSON, which is just a way to organize information using curly braces { } and colons : . 
 The payload is like the actual message or information you want to send. It could be your name, age, or any other data you want to share. It's also written in JSON format, so it's easy to understand and work with. 
 Now, the signature is what makes the JWT secure. It's like a special seal that only the sender knows how to create. The signature is created using a secret code, kind of like a password. This signature ensures that nobody can tamper with the contents of the JWT without the sender knowing about it. 
 When you want to send the JWT to a server, you put the header, payload, and signature inside the box. Then you send it over to the server. The server can easily read the header and payload to understand who you are and what you want to do. 
 Over to you: When should we use JWT for authentication? What are some other authentication methods?
```

---

## 20. Must-Know Cross-Cutting Concerns in API Development

- 日期: 2026-04-09 15:30
- 链接: https://blog.bytebytego.com/p/must-know-cross-cutting-concerns

```
What do authentication, logging, rate limiting, and input validation have in common? 
 The obvious answer is that they’re all important parts of an API. But the real answer is deeper is that none of them belong to any single endpoint or show up in usual product requirements. For all purposes, they are invisible to users when they work and catastrophic when they’re missing. And the hardest part about all of them is making sure they’re applied uniformly across every single route an API exposes. 
 This family of problems has a name. They’re called cross-cutting concerns, and they’re the invisible layer that separates a collection of API endpoints from a production-ready system. 
 In this article, we will learn about these key concerns and their trade-offs in detail. 
 What Makes a Concern “Cross-Cutting” 
 Read more
```

---
