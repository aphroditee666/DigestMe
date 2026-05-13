# Google Developers

> 分类: 大厂技术博客
> URL: https://developers.googleblog.com/feeds/posts/default/
> 抓取: 20 篇

---

## 1. Supercharging LLM inference on Google TPUs: Achieving 3X speedups with diffusion-style speculative decoding

- 链接: https://developers.googleblog.com/supercharging-llm-inference-on-google-tpus-achieving-3x-speedups-with-diffusion-style-speculative-decoding/

```
Researchers at UCSD have successfully implemented DFlash, a block-diffusion speculative decoding method, on Google TPUs to bypass the sequential bottlenecks of traditional autoregressive drafting. By "painting" entire blocks of candidate tokens in a single forward pass rather than predicting them one-by-one, the system achieved average speedups of 3.13x, with peak performance nearly doubling that of existing methods like EAGLE-3. This open-source integration into the vLLM ecosystem optimizes TPU hardware by leveraging "free" parallel verification and high-quality draft predictions for complex reasoning tasks.
```

---

## 2. Building with Gemini Embedding 2: Agentic multimodal RAG and beyond

- 链接: https://developers.googleblog.com/building-with-gemini-embedding-2/

```
Google has announced the general availability of Gemini Embedding 2, a unified model that maps text, images, video, audio, and documents into a single semantic space. This model allows developers to process interleaved multimodal inputs in a single request, significantly improving performance for tasks like agentic RAG, visual search, and content moderation. By supporting over 100 languages and offering features like task-specific prefixes and Matryoshka dimensionality reduction, the model provides a highly efficient and accurate foundation for building complex AI agents.
```

---

## 3. Speeding Up AI: Bringing Google Colossus to PyTorch via GCSFS and Rapid Bucket

- 链接: https://developers.googleblog.com/speeding-up-ai-bringing-google-colossus-to-pytorch-via-gcsfs-and-rapid-bucket/

```
Today, we are announcing a major performance boost for AI/ML workloads using the PyTorch ecosystem on Google Cloud. By integrating Rapid Storage, powered by Google’s Colossus storage architecture, directly with PyTorch via the industry-standard fsspec
interface, we are enabling researchers and developers to keep their GPUs busier than ever before.
As model sizes grow, data loading and checkpointing often become the primary bottlenecks in training. Data preparation activities to train models involve fetching and processing terabytes and petabytes of data from remote storage mechanisms like object storage. Standard REST-based storage access can struggle to meet the extreme throughput and low-latency requirements of modern distributed training, wasting valuable GPU resources.
Our new Rapid Bucket solution provides high-performance object storage in dedicated zonal buckets. By bypassing legacy REST APIs and utilizing persistent gRPC bidirectional streams, we’ve brought the power of Colossus, filesystem stateful protocols that power YouTube and Google Search, directly to the PyTorch ecosystem.
fsspec
is the pervasive Pythonic interface for file systems in the PyTorch ecosystem. It is already used for:
There are various backend implementations of fsspec for many different storage systems, which can all be integrated under a single layer, eliminating the need to write specific code for each backend. By integrating Rapid Storage with gcsfs
(the Google Cloud Storage implementation of fsspec), developers can leverage speed gains provided by Rapid with a simple fsspec.open()
call — no complex code rewrites required.
To achieve a performance boost with Rapid Buckets, we optimized the entire data path:
us-central1-a
), we eliminate cross-zone latency. Prior to Rapid buckets, data in a regional bucket and compute(accelerators) can be in different zones and access the data induced latency.fsspec
API while entirely upgrading internal traffic from HTTP to BiDi-gRPC for Rapid buckets. By adding bucket-type auto-detection to gcsfs, PyTorch and other fsspec
clients transparently utilize Rapid with zero manual configuration.A dataset of 134M rows totaling around 451GB was loaded onto 16 GKE nodes, each containing eight A4 GPUs. Training was conducted in 100 steps, with a checkpoint after every 25 steps using PyTorch Lightning. We benchmarked the performance of total training time, including the data load times, and we observed a performance gain of 23% using Rapid Bucket compared with Standard regional bucket.
Microbenchmarking — that is, measuring the performance of a building block like I/O or resource usage — confirms these gains. Throughput improved by 4.8x for reads (both sequential and random) and 2.8x for writes. These tests used 16MB IO sizes across 48 processes. You can find more details at GCSFS-performance-benchmarks.
Getting started with GCSFS on Rapid Bucket is easy. Your existing code and scripts remain the same. You just need to change the bucket to a Rapid Bucket to take advantage of the performance boost.
To install:
Rapid Bucket integration is available from version 2026.3.0.
pip install gcsfs
Code sample to read/write from GCS Rapid:
import gcsfs
# Initialize the filesystem
fs = gcsfs.GCSFileSystem()
# Writing to a Rapid bucket
with fs.open('my-zonal-rapid-bucket/data/checkpoint.pt', 'wb') as f:
f.write(b"model data...")
# Appending to an existing object (Native Rapid feature)
with fs.open('my-zonal-rapid-bucket/data/checkpoint.pt', 'ab') as f:
f.write(b"appended data...")
```

---

## 4. Building real-world on-device AI with LiteRT and NPU

- 链接: https://developers.googleblog.com/building-real-world-on-device-ai-with-litert-and-npu/

```
LiteRT is a production-ready framework designed to help mobile developers unlock the power of Neural Processing Units (NPUs), overcoming the performance and battery limitations of traditional CPU or GPU processing. By providing a unified API that abstracts away hardware complexities, it allows industry leaders like Google Meet and Epic Games to deploy sophisticated AI models for real-time video, animation, and speech recognition with significantly higher efficiency. The platform further supports developers through benchmarking tools and cross-platform compatibility, enabling seamless AI deployment across mobile devices, AI PCs, and industrial IoT hardware.
```

---

## 5. Agents CLI in Agent Platform:  create to production in one CLI

- 链接: https://developers.googleblog.com/agents-cli-in-agent-platform-create-to-production-in-one-cli/

```
Google Cloud has introduced the Agents CLI, a specialized tool designed to bridge the gap between local development and production-grade AI agent deployment. The CLI provides coding assistants with machine-readable access to the full Google Cloud stack, reducing context overload and token waste during the scaffolding process. By streamlining evaluation, infrastructure provisioning, and deployment into a single programmatic backbone, the tool enables developers to move from initial concept to a live service in hours rather than weeks.
```

---

## 6. Production-Ready AI Agents: 5 Lessons from Refactoring a Monolith

- 链接: https://developers.googleblog.com/production-ready-ai-agents-5-lessons-from-refactoring-a-monolith/

```
The blog post outlines the transition of a brittle sales research prototype into a robust production agent using Google’s Agent Development Kit (ADK). By replacing monolithic scripts with orchestrated sub-agents and structured Pydantic outputs, the developers eliminated silent failures and fragile parsing. Additionally, the post highlights the necessity of dynamic RAG pipelines and OpenTelemetry observability to ensure AI agents are scalable, cost-effective, and transparent in real-world applications.
```

---

## 7. A2UI v0.9: The New Standard for Portable, Framework-Agnostic Generative UI

- 链接: https://developers.googleblog.com/a2ui-v0-9-generative-ui/

```
A2UI v0.9 introduces a framework-agnostic standard designed to help AI agents generate real-time, tailored UI widgets using a company’s existing design system. This update simplifies the developer experience with a new Agent SDK for Python, a shared web-core library, and official support for renderers like React, Flutter, and Angular. By decoupling UI intent from specific platforms, the release enables seamless, low-latency streaming of generative interfaces across web and mobile applications. Integrating with broader ecosystems like AG2 and Vercel, A2UI v0.9 aims to move generative UI from experimental demos to production-ready digital products.
```

---

## 8. MaxText Expands Post-Training Capabilities: Introducing SFT and RL on Single-Host TPUs

- 链接: https://developers.googleblog.com/maxtext-expands-post-training-capabilities-introducing-sft-and-rl-on-single-host-tpus/

```
MaxText has introduced new support for Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) on single-host TPU configurations, leveraging JAX and the Tunix library for high-performance model refinement. These features enable developers to easily adapt pre-trained models for specialized tasks and complex reasoning using efficient algorithms like GRPO and GSPO. This update streamlines the post-training workflow, offering a scalable path from single-host setups to larger multi-host configurations.
```

---

## 9. Subagents have arrived in Gemini CLI

- 链接: https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/

```
Subagents allow Gemini CLI to delegate complex, repetitive, or high-volume tasks to specialized expert agents. Each subagent operates within its own separate context window, custom system instructions, and curated set of tools. This keeps your main session fast, lean, and focused on the big picture while intermediate steps are handed off to a team of subagents.
Subagents are specialized, expert agents that operate alongside your primary Gemini CLI session. When you give Gemini CLI a broad or complex task, it acts as a strategic orchestrator, delegating specific sub-tasks to the most relevant subagent.
Subagents act in isolation with their own set of tools, MCP servers, system instructions, and context window. Their entire execution, which might involve dozens of tool calls, file searches, or test runs, is consolidated into a single response back to the main agent. This prevents your main context window from filling up and keeps your subsequent interactions fast and cost-effective.
Key benefits of subagents:
You can create your own specialized team members (subagents) to automate specific workflows, enforce coding standards, or act with specific personas tailored to your project.
Custom subagents are defined using simple Markdown files (.md
) with YAML frontmatter. You can define them globally in ~/.gemini/agents
for your personal workflows or commit them to your repository to share with your team at the project level in .gemini/agents
.
Subagents can also be bundled as part of Gemini CLI extensions by providing agent definition Markdown files (.md
) to an agents/
directory in your extension.
Here is an example of how to create a custom frontend specialist agent:
---
name: frontend-specialist
description: Frontend specialist in building high-performance, accessible, and
scalable web applications using modern frameworks and standards.
tools:
- read_file
- grep_search
- glob
- list_directory
- web_fetch
- google_web_search
model: inherit
---
You are a Senior Frontend Specialist and UI/UX Architect. Your goal is to design
and implement exceptional, production-grade user interfaces that are both
beautiful and functionally robust. You prioritize modern best practices,
system-level architecture, and distinctive aesthetics.
### Core Principles:
- Architecture & Scalability: Design modular, maintainable, and scalable
frontend architectures. Expert in component-driven development, state
management patterns, and micro-frontends.
- Performance & Optimization: Prioritize speed and responsiveness. Deep
knowledge of Core Web Vitals, rendering strategies (SSR, SSG, ISR, Hydration),
bundle optimization, and caching.
- Accessibility (A11y): Ensure all interfaces are inclusive by default
(WCAG 2.1+ compliance, semantic HTML, robust ARIA implementation, keyboard-
first navigation).
### Guidelines:
- Browser-First Thinking: Understand and leverage native browser APIs
(Intersection Observer, Resize Observer, Web Workers, Storage APIs) before
reaching for libraries.
- Atomic Principles: Build small, reusable, and composable components that
follow the Single Responsibility Principle.
- Visual Feedback: Always provide clear states (loading, skeleton screens,
error, empty, success) and interactive feedback.
- Progressive Enhancement: Ensure core functionality works everywhere,
while providing an enhanced experience for modern browsers.
- Maintenance-Driven Design: Write code that is easy to delete, refactor,
and test. Document architectural decisions and complex logic clearly.
Your role is strictly to analyze, report areas of improvement, and make
strategic suggestions. Do not fix it yourself, just make suggestions.
By placing this file in .gemini/agents/frontend-specialist.md
, Gemini CLI instantly gains a new expert it can call upon.
To see all the different configuration options, refer to the docs for subagents.
What's better than one expert? A whole team of them working simultaneously. Gemini CLI supports parallel subagents, allowing you to spin off multiple subagents or many instances of the same subagent, at the same time.
If you need to research five different topics or refactor several distinct components, Gemini CLI can dispatch multiple agents in parallel, drastically reducing the total time it takes to complete the task.
You can explicitly request this by saying, "Run the frontend-specialist on each package in parallel."
Note: Exercise caution with parallel subagents for tasks that require heavy code edits. Multiple agents editing code at the same time can lead to conflicts and agents overwriting one another. Parallel subagents will also lead to usage limits being hit faster as requests are being sent in parallel across agents.
Gemini CLI ships with several built-in subagents ready for you to use:
Gemini CLI automatically routes tasks to your subagents when it determines they are the most efficient path based on their description. However, you can also explicitly delegate tasks to a subagent by referencing them in your prompt using the @agent syntax. For example:
By using the @ symbol followed by the subagent's name, you explicitly tell Gemini CLI which expert to hire for the job, ensuring the task is handled within that agent's isolated context window.
To view all configured subagents at any given time just run /agents within Gemini CLI.
To learn more about configuring subagents, restricting their tools, and optimizing their descriptions, check out the documentation.
You can also follow Gemini CLI on X to stay up to date with the latest news and announcements.
```

---

## 10. New enhancements for merchant initiated transactions with the Google Pay API

- 链接: https://developers.googleblog.com/new-enhancements-for-merchant-initiated-transactions-with-the-google-pay-api/

```
Google has introduced enhancements to the Google Pay API to provide developers with greater flexibility and control over merchant-initiated transactions (MIT). The update includes new objects within the PaymentDataRequest to specifically handle recurring subscriptions, deferred payments like hotel bookings, and automatic account reloads. By allowing merchants to clearly define future payment terms, these changes improve transparency for users and help reduce transaction declines through better token management. Developers can now implement these features to create more seamless and secure long-term payment experiences.
```

---

## 11. Build Better AI Agents: 5 Developer Tips from the Agent Bake-Off

- 链接: https://developers.googleblog.com/build-better-ai-agents-5-developer-tips-from-the-agent-bake-off/

```
The Google Cloud AI Agent Bake-Off highlights a shift from simple prompt engineering to rigorous agentic engineering, emphasizing that production-ready AI requires a modular, multi-agent architecture. The post outlines five key developer tips, including decomposing complex tasks into specialized sub-agents and using deterministic code for execution to prevent probabilistic errors. Furthermore, it advises developers to prioritize multimodality and open-source protocols like MCP to ensure agents are scalable, integrated, and future-proof against rapidly evolving model capabilities.
```

---

## 12. Get ready for Google I/O: Livestream schedule revealed

- 链接: https://developers.googleblog.com/get-ready-for-google-io-livestream-schedule-revealed/

```
The Google I/O schedule is here! Tune in May 19–20 as we unveil Google’s biggest updates across AI, Android, Chrome, and Cloud. Discover new tools and features designed to unlock the future of development with agentic coding.
We’re kicking things off with the Google keynote at 10:00 am PT on May 19, followed by the Developer keynote at 1:30 pm PT. Block your calendars for two days of live sessions, straight from Mountain View, full of announcements, live demos, and new professional development sessions.
Here’s a sneak peak at what we’ll cover:
- The agentic era of development: Discover how the next evolution of our developer tools is transforming the way you write software. Learn how to seamlessly transition from rapid ideation to orchestrating powerful, autonomous workflows, allowing AI to handle the heavy lifting while you focus on the big picture.
- Enabling Android development anywhere: Learn how we are making AI even more helpful for your app workflows. From initial prototyping to final native polish, explore the latest ways we’re making it easier and faster to build high quality Android experiences.
- Building powerful, agentic web applications: The web is accelerating faster than ever, and we are equipping you for what's next. Discover new tools to build agent-ready web applications, automate complex debugging workflows, and ship highly interactive UI directly in the browser.
Join us online May 19–20, followed by a fresh drop of on-demand sessions and codelabs on May 21. Register today to explore the full program and catch all the latest developer updates, featuring sessions like:
```

---

## 13. TorchTPU: Running PyTorch Natively on TPUs at Google Scale

- 链接: https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/

```
TorchTPU is a new engineering stack designed to provide a native, high-performance experience for running PyTorch workloads on Google’s TPU infrastructure with minimal code changes. It features an "Eager First" approach with multiple execution modes and utilizes the XLA compiler to optimize distributed training across massive clusters. Moving into 2026, the project aims to further reduce compilation overhead and expand support for dynamic shapes and custom kernels to ensure seamless scalability for the next generation of AI.
```

---

## 14. Supporting Google Account username change in your app

- 链接: https://developers.googleblog.com/supporting-google-account-username-change-in-your-app/

```
Google has updated its account settings to allow U.S. users to change their @gmail.com usernames while keeping all existing account data and inboxes intact. For developers, this means that while old email addresses will remain active as aliases, apps that rely solely on email addresses for identification may face issues with account duplication or lost access. To ensure a seamless user experience, Google recommends migrating to the "subject ID" as the primary user identifier and allowing users to manually update their contact information within app settings.
```

---

## 15. Bring state-of-the-art agentic skills to the edge with Gemma 4

- 链接: https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/

```
Google DeepMind has launched Gemma 4, a family of state-of-the-art open models designed to enable multi-step planning and autonomous agentic workflows directly on-device. The release includes the Google AI Edge Gallery for experimenting with "Agent Skills" and the LiteRT-LM library, which offers a significant speed boost and structured output for developers. Available under an Apache 2.0 license, Gemma 4 supports over 140 languages and is compatible with a wide range of hardware, including mobile devices, desktops, and IoT platforms like Raspberry Pi.
```

---

## 16. Developer’s Guide to Building ADK Agents with Skills

- 链接: https://developers.googleblog.com/developers-guide-to-building-adk-agents-with-skills/

```
The Agent Development Kit (ADK) SkillToolset introduces a "progressive disclosure" architecture that allows AI agents to load domain expertise on demand, reducing token usage by up to 90% compared to traditional monolithic prompts. Through four distinct patterns—ranging from simple inline checklists to "skill factories" where agents write their own code—the system enables agents to dynamically expand their capabilities at runtime using the universal agentskills.io specification. This modular approach ensures that complex instructions and external resources are only accessed when relevant, creating a scalable and self-extending framework for modern AI development.
```

---

## 17. ADK Go 1.0 Arrives!

- 链接: https://developers.googleblog.com/adk-go-10-arrives/

```
The launch of Agent Development Kit (ADK) for Go 1.0 marks a significant shift from experimental AI scripts to production-ready services by prioritizing observability, security, and extensibility. Key updates include native OpenTelemetry integration for deep tracing, a new plugin system for self-healing logic, and "Human-in-the-Loop" confirmations to ensure safety during sensitive operations. Additionally, the release introduces YAML-based configurations for rapid iteration and refined Agent2Agent (A2A) protocols to support seamless communication across different programming languages. This framework empowers developers to build complex, reliable multi-agent systems using the high-performance engineering standards of Golang.
```

---

## 18. Boost Training Goodput: How Continuous Checkpointing Optimizes Reliability in Orbax and MaxText

- 链接: https://developers.googleblog.com/boost-training-goodput-how-continuous-checkpointing-optimizes-reliability-in-orbax-and-maxtext/

```
The newly introduced continuous checkpointing feature in Orbax and MaxText is designed to optimize the balance between reliability and performance during model training, addressing issues with conventional fixed-frequency checkpointing. Unlike fixed intervals—which can either compromise reliability or bottleneck performance—continuous checkpointing maximizes I/O bandwidth and minimizes failure risk by asynchronously initiating a new save operation only after the previous one successfully completes. Benchmarks demonstrate that this approach significantly reduces checkpoint intervals and results in substantial resource conservation, especially in large-scale training jobs where mean-time-between-failure (MTBF) is short.
```

---

## 19. Announcing ADK for Java 1.0.0: Building the Future of AI Agents in Java

- 链接: https://developers.googleblog.com/announcing-adk-for-java-100-building-the-future-of-ai-agents-in-java/

```
Google has released version 1.0.0 of the Agent Development Kit (ADK) for Java, introducing powerful new features like Google Maps grounding, built-in URL fetching, and a standardized Agent2Agent protocol for cross-framework collaboration. The update enhances agent control through a new "App" and "Plugin" architecture, which allows for global logging, automated context window management via event compaction, and "Human-in-the-Loop" workflows for action confirmations. Additionally, the release provides robust session and memory services using Google Cloud integrations like Firestore and Vertex AI to manage long-term state and large data artifacts.
```

---

## 20. Closing the knowledge gap with agent skills

- 链接: https://developers.googleblog.com/closing-the-knowledge-gap-with-agent-skills/

```
To bridge the gap between static model knowledge and rapidly evolving software practices, Google DeepMind developed a "Gemini API developer skill" that provides agents with live documentation and SDK guidance. Evaluation results show a massive performance boost, with the gemini-3.1-pro-preview model jumping from a 28.2% to a 96.6% success rate when equipped with the skill. This lightweight approach demonstrates how giving models strong reasoning capabilities and access to a "source of truth" can effectively eliminate outdated coding patterns.
```

---
