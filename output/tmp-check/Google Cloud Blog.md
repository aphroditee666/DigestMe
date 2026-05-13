# Google Cloud Blog

> 分类: 大厂技术博客
> URL: https://cloudblog.withgoogle.com/rss/
> 抓取: 20 篇

---

## 1. Ship code within minutes with the Gemini CLI DevOps Extension

- 日期: 2026-05-08 19:00
- 链接: https://cloud.google.com/blog/topics/developers-practitioners/ship-code-within-minutes-with-the-gemini-cli-devops-extension/

```
With AI coding tools like Antigravity and Claude Code, I can build a working web app in record time. But deploying it? That's where I'd historically lose the rest of the afternoon to Dockerfiles, IAM bindings, and YAML. So I'd take the shortcut most developers take: I just wouldn't do it. The app would stay on my laptop, and my work would never ship. 
 This is the classic tension between the inner loop : the fast, local cycle of writing and testing code, and the outer loop : containerization, CI/CD pipelines, and production infrastructure. Most developers are productive in one but not the other, and the gap between them is where projects stall. 
 The Gemini CLI Extension for CI/CD bridges this gap. It handles both quick deployments and full pipeline generation from a single terminal interface. Let me show you how. 
 Building the Cosmic Guestbook App 
 To demonstrate this workflow, we need an app. Let's start from an empty directory and use our agent to "vibe code" a brand new project: the Cosmic Guestbook . 
 We want a full-stack architecture: a React frontend and a Node.js Express backend API. Instead of scaffolding this by hand, we can ask our agent to jumpstart the app: 
 code_block <ListValue: [StructValue([('code', '"Build a \'Cosmic Guestbook\' web app. I need a dynamic Node.js Express backend and a React frontend utilizing Vite. Make the frontend look like a beautiful, glassmorphic sci-fi interface."'), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac0ae6a90>)])]> 
 Within moments, our agent scaffolds the backend/ directory with server.js and the frontend/ directory with a fully styled React app. We now have a functioning, two-tier web app sitting on our laptop. 
 Installing the Extension 
 But code on a laptop isn't shipping. To get this guestbook online, we need to equip our chosen environment with the CI/CD extension. Regardless of your setup, start by ensuring that you have the gcloud CLI installed and authenticate using Application Default Credentials: gcloud auth application-default login . 
 Now, install the extension in your preferred development environment: 
 For Gemini CLI 
 Run the following command directly in your terminal: 
 code_block <ListValue: [StructValue([('code', 'gemini extensions install https://github.com/gemini-cli-extensions/cicd'), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac0ae66d0>)])]> 
 For Claude Code 
 Add the marketplace and install the plugin directly from the terminal: 
 code_block <ListValue: [StructValue([('code', '# 1. Add the Marketplace\r\nclaude plugin marketplace add https://github.com/gemini-cli-extensions/cicd.git\r\n\r\n# 2. Install the Plugin\r\nclaude plugin install cicd'), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac0ae6310>)])]> 
 For Antigravity and agents supported by npx skills 
 You can enable the extension's MCP Server as custom MCP and add skills to your workspace: 
 code_block <ListValue: [StructValue([('code', '# Add the Skills\r\nnpx skills add https://github.com/gemini-cli-extensions/cicd --global --all --agent antigravity'), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac0ae6cd0>)])]> 
 How It Works 
 The CI/CD extension is a powerful three-tier system designed to translate your intent into secure, production-ready infrastructure in all these agent environments: 
 Skills : Specialized AI skills like google-cicd-deploy and google-cicd-pipeline-design are defined in the extension. These instruct your AI agent (Gemini CLI, Claude Code, or Antigravity) on how to think—helping it analyze your code, ask the right questions, and handle errors gracefully. 
 CI/CD MCP server : Running in the background is a specialized Go-based Model Context Protocol (MCP) server. This server provides a suite of tools that gives your agent the hands it needs to actually manipulate Google Cloud: everything from scanning for secrets to provisioning Cloud Run services. 
 Local knowledge base : To ensure the most accurate answers, the system includes a pre-indexed retrieval-augmented generation (RAG) database containing verified architecture patterns, which lets the agent ground its design decisions in the source of truth. 
 Your chosen AI assistant orchestrates these tools and patterns into a cohesive deployment lifecycle. 
 The Inner Loop 
 When you're building a prototype or testing a new feature, you don't need a massive, multi-environment CI/CD pipeline. You just need a public URL to test your webhook or show a stakeholder. This is the inner loop, and it needs to be fast. 
 The traditional approach involves manually writing a Dockerfile , authenticating with a container registry, building the image, pushing it, and finally deploying it. The CI/CD extension turns this into a single natural language prompt: gemini "Deploy this application to Google Cloud using the google-cicd-deploy skill" . If you're using Claude Code, you can prompt it exactly the same way via claude -p "Deploy this application..." , and in Antigravity, simply type your deployment request. 
 When you run this prompt, your AI agent analyzes your local workspace to figure out the best deployment approach. 
 Step 1: Pre-Deployment Security Scan 
 Leaked secrets are one of the most common and expensive security failures in software. GitGuardian's 2025 State of Secrets Sprawl report found 23.8 million new credentials exposed on public GitHub in a single year; 70% of secrets that were leaked in 2022 are still active today. It happens fast: you hardcode a database password during local testing, forget to remove it, and push. 
 The extension catches this before it becomes a problem. Before any code leaves your machine, it runs a secret check across your workspace. If it finds a Stripe API key or a database credential sitting in your source, the agent halts the deployment and warns you. No secrets ship to the cloud by accident. 
 If you accidentally commit a database password or a Stripe API key while hacking on localhost, your assistant catches it and prevents the deployment. This is what true shift-left security looks like in practice. 
 Step 2: Application Analysis & Containerization 
 Next, your agent checks your package.json or go.mod to figure out your framework. It automatically decides whether to use Google Cloud Storage (for static sites) or Cloud Run (for dynamic services). 
 If you're building a dynamic service that doesn't have a Dockerfile, the extension leverages Google Cloud's buildpacks to containerize it for you on the fly. 
 Step 3: Clarification and Deployment 
 Conversational agents don't blindly guess how you want your app configured. Before making any changes to your Google Cloud environment, the assistant pauses the flow to ask prioritizing questions based on what it found during its analysis. 
 For our Cosmic Guestbook, I didn't specify a region or whether the service should be public. The assistant paused and asked me about it: 
 "I have completed the analysis and prepared the application for a unified deployment to Cloud Run. Since the Node.js buildpack requires a single entry point, I created a root package.json with a custom build script that builds the React frontend and allows the Express backend to serve it statically. 
 Additionally, the secret scan completed successfully, and no sensitive credentials were found. 
 Before we deploy using the Cloud Run source deployment option (buildpacks), I need to clarify a few deployment parameters: 
 Region/Location: The gcloud defaults do not specify a location. Which Google Cloud region would you like to deploy to (e.g., us-central1 , europe-west1 )? 
 Access: Should this application be publicly accessible or private? 
 Service Name: I propose naming the service cosmic-guestbook . Does that sound good to you?" 
 This conversational pause ensures that even in the fast inner loop, you retain complete control over your cloud architecture. After you confirm the details, the agent pushes the code live and returns the public URL: 
 code_block <ListValue: [StructValue([('code', '# Final Output:\r\nYour application is now live and publicly accessible at the following URL:\r\nhttps://cosmic-guestbook-xxxxxxxx-uc.a.run.app'), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac0ae6b50>)])]> 
 Behind the scenes, the deployment is handled automatically via cloudrun.deploy_to_cloud_run_from_source . 
 The Outer Loop 
 A scrappy deployment prompt is perfect for a Tuesday afternoon prototype, but you can't run a production system from your laptop. Eventually, you need the rigors of the outer loop: automated testing, source control integration, and formal continuous deployment. 
 Writing cloudbuild.yaml files and provisioning the necessary infrastructure (like Artifact Registry repositories or GitHub connections through Developer Connect ) is notoriously tedious and error-prone. With the google-cicd-pipeline-design skill, your AI agent acts as your personal platform engineering consultant. 
 Instead of writing YAML from scratch, you have a conversation. Your agent will ask you about your testing strategy and where you want to deploy, and then it autonomously provisions the required Google Cloud infrastructure. 
 Step 1: Architectural Design & Feedback 
 You start the process directly in your conversational interface: 
 code_block <ListValue: [StructValue([('code', '# Prompt your agent to kick off the design process:\r\ngemini "Design a CI/CD pipeline using the google-cicd-pipeline-design skill"\r\n# OR\r\nclaude -p "Design a CI/CD pipeline using the google-cicd-pipeline-design skill"'), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac0ae6a00>)])]> 
 Your assistant doesn't work in a black box. It retrieves common CI/CD patterns from its knowledge base. With the most relevant knowledge in hand, it proposes a concrete plan in YAML for you to review. 
 Step 2: Infrastructure Provisioning 
 After you approve the plan, the assistant works sequentially through the required infrastructure steps. For example, it might first create a registry for your containers. 
 code_block <ListValue: [StructValue([('code', '// Example MCP call to provision the registry\r\n{\r\n "name": "create_artifact_repository",\r\n "arguments": {\r\n "repository_id": "demo-app-repo",\r\n "location": "us-central1",\r\n "format": "DOCKER"\r\n }\r\n}'), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac0ae6130>)])]> 
 It might then set up a Git connection so that Cloud Build can read your source code. 
 Step 3: Pipeline Generation & Trigger 
 Finally, the agent generates the actual cloudbuild.yaml file that defines the pipeline stages (test, build, deploy). Here's a snippet of a generated configuration from the repository that highlights the initial build steps: 
 code_block <ListValue: [StructValue([('code', 'steps:\r\n # Step 1: Install tools (like the linter) and clean the cache.\r\n - name: \'golang:1.24\'\r\n id: \'Install Tools\'\r\n entrypoint: \'sh\'\r\n args:\r\n - \'-c\'\r\n - |\r\n set -e\r\n export PATH=/workspace/bin:$$PATH\r\n echo "Installing golangci-lint..."\r\n go install github.com/golangci/golangci-lint/cmd/golangci-lint@v1.64.8\r\n echo "Cleaning module cache..."\r\n go clean -modcache\r\n env:\r\n - \'GOPATH=/workspace\'\r\n dir: \'devops-mcp-server\''), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac0ae6100>)])]> 
 With the pipeline defined, we need a way to execute it automatically. The agent finishes by creating a Cloud Build trigger . The trigger acts as the glue between your GitHub repository and Cloud Build, ensuring that every push to the main branch automatically fires off the cloudbuild.yaml steps. 
 code_block <ListValue: [StructValue([('code', '// Example MCP call setting the trigger\r\n{\r\n "name": "create_build_trigger",\r\n "arguments": {\r\n "trigger_name": "main-branch-deploy",\r\n "filename": "cloudbuild.yaml",\r\n "branch_pattern": "^main$"\r\n }\r\n}'), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac0ae65b0>)])]> 
 Security And Control 
 AI-assisted infrastructure generation sounds incredible, but it's reasonable to ask: is it safe? 
 The extension operates strictly within the permissions of your local Application Default Credentials (ADC) . It can't do anything that you can't do. Because it uses the Model Context Protocol (MCP) , every action that it takes, from creating an Artifact Registry to modifying a Cloud Build trigger, runs through strongly typed, verifiable tools. 
 If you don't like a step in the proposed pipeline, you tell your agent to change it. You're always the "Editor-in-Chief" of your infrastructure. We strongly recommend that you adhere to the principle of least privilege for both your local ADC and any service accounts that are used by the generated pipelines. 
 When Dev and Ops Converge 
 The friction between wanting to write code and needing to ship it is finally dissolving. We're moving past the era where deep expertise in YAML formatting was a prerequisite for putting an app on the internet. 
 By handling the boilerplate of both the scrappy inner loop and the automated outer loop, conversational AI lets developers focus on the business logic that actually matters. 
 Next Steps 
 If you want to experience this convergence yourself, here are your immediate next steps: 
 Get the tools : Install the CI/CD Extension for Gemini CLI . 
 Deploy the inner loop : Take an existing side project (or ask your chosen agent to scaffold a new one like our Cosmic Guestbook ) and prompt it to deploy to Google Cloud to instantly see it live on Cloud Run or Cloud Storage. 
 Automate the outer loop : Run a design command against a repository that you're ready to productionize, and watch your agent generate your cloudbuild.yaml and provision your infrastructure. 
 Stop wrestling with configuration files and start shipping. Let me know what you build by reaching out on LinkedIn , X , or Bluesky !
```

---

## 2. With faster node startup for GKE, say goodbye to cold-start latency

- 日期: 2026-05-08 16:00
- 链接: https://cloud.google.com/blog/products/containers-kubernetes/gke-node-startup-gets-faster/

```
We’ve rolled out a significant update to Google Kubernetes Engine (GKE) that solves one of the most annoying problems in cloud infrastructure: cold start latency . GKE now has up to 4x faster node startup times compared to previous versions for qualifying nodes, allowing customers to provision quickly and efficiently. This isn't a setting you have to toggle or a config file you need to patch. It’s an architectural upgrade to how we provision infrastructure, meaning your nodes just start faster, out of the box. This translates directly into enhanced agility and cost-efficiency for your cloud operations with a significant impact on a wide range of use cases, from rapid deployment of models for AI inference to dynamic scaling of accelerated and general-purpose nodes. 
 The problem we set out to tackle: the "cold start" tax 
 If you run workloads with fluctuating demand, especially AI inference or batch processing, you know the pain of waiting for a new node to spin up. When demand spikes, your autoscaler requests a node. Then you wait. To avoid that wait, and the resulting latency for your users, many teams resort to over-provisioning, keeping expensive nodes running "just in case." You end up paying for idle compute just to buy yourself insurance against startup lag. That insurance is especially expensive when it comes to scarce accelerators. 
 The solution: a complete rework of node provisioning 
 To address this, we rebuilt the provisioning logic for VMs and GKE nodes. At a high level, we are using a combination of intelligent compute buffers, specially designed fast-starting virtual machines, and a new control plane architecture that allows VMs to resize instantly without rebooting. While the technical details are complex, the benefit to you is simple: your GKE clusters now scale inherently faster and are more efficient, allowing you to shift precious resources to where they are needed. 
 What this means for you 
 Less over-provisioning: Because nodes come online faster, you can trust your autoscaler to react in real-time rather than keeping a buffer of idle nodes. 
 Better AI inference: For models running on GPUs, faster node provisioning reduces the time between a request spike and the model serving traffic. 
 No "Ops" overhead: This works automatically. You don't need to change your Terraform or YAML files to take advantage of it. 
 Availability 
 The accelerated provisioning is live right now for workloads running in GKE Autopilot — including Autopilot workloads running inside Standard clusters — using the following hardware: 
 NVIDIA L4 (G2 nodes) 
 NVIDIA A100 (A2 nodes) 
 NVIDIA RTXPRO6000 (G4 nodes) 
 NVIDIA H100 (A3 nodes) 
 Autopilot "General Purpose" Compute 
 Coming soon, we will continue to roll this out to more machines, including the following, so stay tuned: 
 NVIDIA H200 (A3 ultra nodes) 
 NVIDIA B200 (A4 nodes) 
 Cloud TPUs 
 How to try it 
 If you already use GKE Autopilot on the supported instance types, you’ve probably  already noticed the improvement. 
 And if you’re running a GKE Standard cluster, you can now use Autopilot specifically for these workloads without migrating your whole cluster. Just point your Pods to the Autopilot ComputeClass , and they will inherit these startup speeds while living alongside your standard nodes. 
 You can read the full technical documentation on fast-starting nodes here . 
 What's next 
 Learn how you can leverage these new improvements to improve your workload responsiveness with these resources. 
 Quicker workload startup with fast-starting nodes 
 Autopilot container-optimized compute platform 
 Autopilot mode workloads in GKE Standard 
 Autopilot container-optimized compute platform
```

---

## 3. Gemini 3.1 Flash-Lite is now generally available on Gemini Enterprise Agent Platform

- 日期: 2026-05-07 18:00
- 链接: https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available/

```
Today, we’re thrilled to announce that Gemini 3.1 Flash-Lite, our fastest and most cost-efficient Gemini 3 series model yet, is now generally available . 
 Designed for ultra-low latency, high-volume tasks, and unmatched cost-efficiency, Flash-Lite is already transforming how applications are built at scale. Fast, iterative, and scalable, it joins our comprehensive suite of Pro and Flash models to provide the exact combination of intelligence, speed, and cost required for the most demanding production deployments. 
 Developers and enterprises have noted that the model provides the precision required for agentic tasks like tool calling and orchestration, coupled with the cost-efficiency needed to run automated pipelines at scale. 
 Here’s a look at how some of them have been driving value. 
 Software development and engineering 
 Engineering teams require models that can keep pace with real-time coding environments. With the GA of Gemini 3.1 Flash-Lite, developers are unlocking the instant responsiveness necessary for complex code completion, seamless UX design, and agentic developer tools. 
 “Integrating Gemini 3.1 Flash-Lite has transformed the responsiveness of our IDE AI assistant & Junie agent. The balance of high intelligence and minimal latency makes it the perfect model for real-time developer support." — Vladislav Tankov, Director of AI at JetBrains 
 Customer experience and high-volume service 
 For enterprise customer service operations, handling massive volumes of interactions requires models that can scale affordably without sacrificing reasoning capabilities. 
 Gladly runs customer service for some of the most demanding retail brands in the world. The core of its text-channel AI agent runs on Flash-Lite. By handling millions of customer-facing calls each week across channels like SMS, WhatsApp, and Instagram, they achieved roughly 60% lower costs than comparable thinking-tier models on the same token mix. 
 The model powers every step of the agent lifecycle — from selecting tools and classifying playbooks to deciding when to escalate to a human — all while maintaining a p95 latency around 1.8s seconds for fully reply generation and sub-second p95 for classifiers and tool calls, alongside a ~99.6% success rate under heavy concurrent load. 
 Gladly uses Flash-Lite for millions of weekly customer service interactions 
 Creative pipelines and gaming 
 In the fast-paced creative and gaming industries, multimodal capabilities and ultra-low latency are essential for keeping users engaged and content pipelines flowing. Flash-Lite is empowering platforms to process rich media and generate hyper-personalized environments. 
 Astrocade lets anyone create games by describing what they want in natural language. They integrated Flash-Lite to serve a rapidly growing global user base. 
 For every incoming game request, it performs a multimodal safety check — analyzing both text and images — before the building agents even start their work. It further supports their global community through inline comment translation, allowing players in different countries to “riff” on the same game. And as part of their asset generation pipeline, it helps refine the final prompts to ensure consistently high-quality thumbnails. 
 Astrocade uses Flash-Lite to refine prompts for game thumbnail generation 
 The creative platform krea.ai has also seen positive results by using Flash-Lite as a prompt enhancer in their Nodes tool. By taking a user’s rough idea and expanding it into a full image generation prompt pipeline, the model provides a level of detail that is “weirdly creative” for its price point. 
 These outputs move the needle on image production, providing a level of reliability and scale that was previously cost-prohibitive for sophisticated prompt engineering. 
 Financial services and data operations 
 In the world of finance and enterprise product development, efficiency is just as critical as accuracy. Gemini 3.1 Flash-Lite gives financial analysts and product managers the ideal balance of intelligence, low latency, and cost-effectiveness to run modeling and latency-sensitive applications. 
 OffDeal uses Flash-Lite to power “Archie,” an AI agent that investment bankers use for real-time research, data lookups, and task execution during Zoom calls. In these scenarios, bankers often need to surface financials mid-conversation. OffDeal found that Flash-Lite was the only model capable of meeting the response times needed for genuinely instant answers without forcing a tradeoff on quality. 
 Beyond live calls, they also use Flash-Lite as a triage layer for inbound and outbound email traffic. By answering structured questions about messages in parallel, such as whether an email is an automated response or in relation to an active deal, Flash-Lite determines which downstream AI agents get invoked and with what context. 
 For high-volume, latency-sensitive workflows on the financial operations platform Ramp, Flash-Lite has become a key component: 
 “Gemini is a core part of the model stack we use across applications at Ramp. As indicated in our benchmarks, we see Gemini lead the pareto fronts in terms of costs, latency and intelligence—providing a great tradeoff between the three and making it well-suited for latency sensitive applications. Gemini 3.1 Flash-Lite has been especially valuable, powering many of our highest-volume, latency-sensitive features without compromising on quality.” – Anton Biryukov, Applied AI Engineer, Ramp 
 Market intelligence platform AlphaSense integrates Flash-Lite to deliver data insights: 
 "Gemini 3.1 Flash-Lite provides great balance of speed, cost and performance, allowing AlphaSense to scale our advanced data processing and deliver high-quality intelligence across every layer of our data stack” – Chris Ackerson, Senior Vice President of Product, AlphaSense 
 Get started 
 Read the docs for Gemini 3.1 Flash-Lite and learn about our latest pricing structure . Learn more about the Gemini Enterprise Agent Platform , the new standard for enterprise agent development.
```

---

## 4. New Bigtable in-memory tier for sub-millisecond read latency

- 日期: 2026-05-07 16:00
- 链接: https://cloud.google.com/blog/products/databases/scaling-real-time-performance-with-bigtable-in-memory-tier/

```
In the high-stakes world of digital infrastructure, speed isn't just a metric — it’s currency. At Google Cloud Next ‘26 we announced the Bigtable in-memory tier , a breakthrough for our fully managed cloud database service that delivers: 
 Sub-millisecond read latency for time-sensitive data 
 ~10x higher point read throughput per dollar , dramatically reducing TCO 
 Hotspot resistance , supporting up to 120,000 queries per second on a single row without breaking a sweat. 
 For more information see Bigtable performance documentation . Now, let's look at the impact Bigtable in-memory tier can have on your workload performance and operational processes. 
 The cache-miss nightmare: A familiar story 
 Imagine it’s 2:00 AM. Your promotional campaign just went viral, and traffic is spiking. Your database architecture, meanwhile, is a house of cards: a primary database struggling to keep up and a separate caching layer acting as a shield. 
 Suddenly, you're hit with a hot key problem: everyone is trying to access the same viral content. Your cache node saturates. You’re forced to upgrade to larger nodes or add read replicas. You and your team are exhausted. Not only are you managing two different systems, maintaining a complex cache-aside logic (and praying the data in the cache stays in sync with the database), but you also need to respond to the actual incident. To do so, you overprovision CPU to handle the peak, and add more RAM so that everything fits in memory, as well as to avoid cache-aside complexity. Now you’re paying premium prices for warm data that doesn't actually need to be in memory. And while your hypothetical throughput-per-dollar looks great on paper, 90% of your resources sit idle most of the time. 
 Enter Bigtable’s in-memory tier 
 The Bigtable in-memory tier ends this cycle. By bringing data tiering across RAM, SSD, and HDD into a single, unified service with a hybrid storage architecture, we've removed the middleman. 
 The result? You get the raw throughput and speed of a cache with the durability and scale that Bigtable was designed for. When that viral spike hits, Bigtable automatically moves hot rows into memory to handle the load. No CPU spikes, no performance degradation. If the traffic grows, so does your Bigtable cluster by giving you more in-memory read capacity. You no longer need to overpay for idle RAM or cache nodes; Bigtable intelligently manages your data, keeping only the hot data in memory and ensuring data consistency between in-memory tier and SSD storage. 
 The TCO benefits are tangible, but maybe the most important part is the peace of mind that comes with it — and that’s priceless. 
 A peek behind the curtain 
 Almost every database server uses memory to give CPU fast access to latency-sensitive, frequently accessed data such as indexes and Bloom filters. You might be wondering, what makes this announcement different? 
 The secret lies in Remote Direct Memory Access (RDMA), a high-performance networking technology that allows computers to transfer data directly from one machine's memory to another without involving either the system's operating system or CPU. Our architecture uses RDMA to provide a high-speed, direct path to server memory, and as a result, throughput and latency of in-memory tier isn’t bound by server CPU, translating to impressive benefits. Much like Data Boost enables direct disk access for heavy workloads such as ML training, RDMA provides high-speed, direct memory access for real-time processing. 
 Imagine you’re running a popular social media site where 98% of users have fewer than 250 followers, while your most popular users have over 100 million. 60% of users post less than once a week, and the top 10% of users generate 80% of the content. And while a typical post receives 500 impressions, popular ones receive tens of millions. 
 To efficiently address this use case you will want data tiering that will likely look like this: 
 Memory: Content from profiles of users with large followings 
 SSD: Recent content, active user profiles 
 HDD: Older content, inactive user profiles 
 Luckily this is very easy to accomplish in Bigtable. Simply enable in-memory for your cluster and use a memory-enabled application profile when issuing your database requests to automatically manage the hot data lifecycle. You can also set an age-based policy to tier cold data to infrequent access. With this setup, when a piece of content is read, it gets promoted to the memory tier from persistent storage and stays there until it is evicted to make room for more recently read items. It is hands-free; even if a post from 5 years ago makes a viral comeback all of a sudden, you don’t have to worry about it. 
 But let’s say you want more fine-grained control of what you cache. You have a list of popular content creators and want to limit memory usage to only that small subset of their posts. Simply route the traffic for those users via the memory-enabled app profile, and for the rest of the content use an app profile that isn’t memory-enabled. 
 The cache-miss nightmare, revisited 
 Let’s rewind and replay our cache-miss scenario, but with Bigtable’s in-memory tier enabled. It’s 2:00 AM Sunday morning. Your promotional campaign just went viral, and traffic is spiking, you need to serve an additional 80K reads per second for the next hour. You don’t get paged. You wake up at 11 AM to the sound of birds chirping and enjoy a peaceful breakfast. It’s a beautiful day. The only sign that traffic spiked between 2-3 AM is that your bill shows an extra $0.40 charge. 
 Power laws govern distribution of requests for applications in a wide range of industries so scenarios like this are not limited to social media. For example, stock exchanges trade several thousands of securities but the top 30 most active stocks typically represent more than 40% of the total daily trading volume. At the same time, the most recent data points (last trade, ask/bid price) are requested frequently with an expectation of low latency responses, while historical data is accessed much less frequently, and has a rather forgiving latency budget. Let’s break down this example into Bigtable data tiers: 
 Memory: Most recent price of securities for most sought out stocks 
 SSD: Recent history, aggregated metrics (hourly, daily, monthly etc.) 
 HDD: Older data, raw events like individual trades 
 The list of possible use cases for this capability is long. Automated trading systems access latest prices from memory, while retail investors build their candlestick charts from data on SSD, and quants access historical data on HDD using Data Boost to backtest their models. All in one database, without interfering with each other. You can replace financial time series with telemetry data, sensor networks, digital twins and the story wouldn’t be much different. 
 Nor does using Bigtable’s in-memory tier interfere with other enterprise features like high availability, scaling, auditing, governance, and access controls, which typically introduce significant overhead. Achieving sub-millisecond latency despite these enterprise requirements is extremely impressive. By optimizing our clients and network, we’ve also successfully reduced p50 SSD latencies to below 2 milliseconds. 
 Get started with Bigtable Enterprise Plus 
 The Bigtable in-memory tier is available exclusively as part of the new Bigtable Enterprise Plus edition , which offers many additional features and is designed for organizations that demand the highest levels of performance, and management efficiency. 
 Elevate your stack to Bigtable Enterprise Plus and in-memory capabilities today so you can stop managing infrastructure and start building the future! 
 Learn more 
 Learn more about Bigtable Enterprise Plus edition and its capabilities beyond the in-memory tier. Try it out by heading over to Google Cloud console and creating new clusters upgrading existing ones. 
 If you’re new to Bigtable, you can now experience Google’s pioneering NoSQL database with the new Bigtable Free Trial . Get a dedicated Enterprise Edition node, 500GB storage, and a guided tour of Bigtable. 
 For more detailed information on getting started, technical specifications, and regional availability, visit the official Bigtable product page .
```

---

## 5. How BASF manages thousands of supply chain decisions with AlphaEvolve’s agentic algorithms

- 日期: 2026-05-07 16:00
- 链接: https://cloud.google.com/blog/products/ai-machine-learning/how-basf-manages-thousands-of-supply-chain-decisions-with-alphaevolve/

```
The agricultural and crop protection supply chain is one of the most intricate networks in the world. It takes up to two years to turn active ingredients into the final products farmers need, and a single change in weather or regulations can disrupt everything. Planners at BASF Agricultural Solutions navigate this reality daily across 180 production sites. To understand how local decisions ripple across their entire global network, BASF turned to AlphaEvolve on Google Cloud to build a digital twin of their supply chain. 
 Planning across a two-year lead time 
 BASF Agricultural Solutions manages a network with over 5,000 distinct value chains. Creating a single end product requires a bill of materials that can be over 30 levels deep, moving across different production sites and regions. 
 Currently, human planners make thousands of local decisions every day. They decide what to produce, when to produce it, and how much safety stock to hold. Because the network is so large, a planner can’t easily see how a localized decision affects the rest of the global supply chain. 
 This scale can lead to additional working capital and inventory and or cause production imbalances. Traditional mathematical models struggle to capture the dynamic reality of the network that planners navigate based on years of experience. 
 Building a foundation for decision support 
 AlphaEvolve is an evolutionary coding agent that generates and refines algorithms autonomously. In collaboration with Google Cloud and prognostica GmbH , BASF’s objective was not to replace human decision-making, but to establish a new model for decision support that helps planners handle the real-world complexity of the production network. 
 The team gave AlphaEvolve a foundational "seed" program. This initial code established a standard planning logic that translated demand forecasts into production schedules, serving as a functional baseline before introducing dynamic, network-wide coordination. From there, they fed the model three years of historical data, including inventory levels, market demand, and actual production outputs. AlphaEvolve then generated variations of the code, mutating the logic to see if it could simulate a supply chain that matched the real-world historical data. 
 Measuring what good looks like in initial tests 
 For AlphaEvolve to improve, it needed a specific goal. The evaluation function scored every new piece of generated code on one primary metric: how closely the simulated inventory levels and production decisions matched the actual historical reality recorded by BASF. 
 The latest AlphaEvolve runs delivered more than 80% relative improvement in accuracy compared to the initial seed model. With further adjustments, the team expects to push performance even higher — bringing the model to a level of accuracy not achieved with other approaches and making it actionable for operational use. 
 The results 
 The evolved planning logic delivered immediate, measurable improvements over the initial seed model. The final algorithm successfully mirrored the actual historical performance of the supply chain, significantly reducing the error rate compared to the initial seed. 
 “We had several attempts to build a digital twin for our complex supply network using deterministic models, and all of them failed,” said Dr. Goetz Krabbe, vice president for global supply chain at BASF. “By using AlphaEvolve, we cannot only map the complex network based on system data, but at the same time understand and copy the human decisions that drive our daily operations. This gives us a highly accurate and easy to maintain data driven digital twin of the entire network. Using it we can optimize our inventory levels and respond to market volatility with confidence while avoiding stockouts." 
 What the evolved algorithm actually does 
 By running thousands of experiments, AlphaEvolve developed a clear, human-readable algorithm that explains how the BASF network truly operates. It automatically discovered factually correct, domain-specific supply chain rules that explain the observed production outputs and inventory levels for the tested product value chain: 
 Production consolidation: The algorithm learned to group production amounts together, accurately mapping how planners optimize plant time. 
 Dynamic safety stocks: It introduced safety stock parameters to handle volatile and seasonal demand patterns, helping to strictly manage capital costs while preventing out-of-stock situations. 
 Network-wide coordination: The model successfully mapped the dependencies between different production tiers, providing a clear foundation for optimizing asset utilization globally. 
 What's next 
 The initial simulations showed that evolutionary AI can accurately model large-scale, dynamic supply chains. BASF’s objective is to create a digital twin of their entire global production network as a new foundation for simulation, decision support, scenario forecasting and optimization. This will allow the team to continuously simulate operations, identify hidden bottlenecks before they affect throughput, and optimize asset utilization across all global facilities. 
 This project was a collaboration between the BASF SE team including: Benjamin Priese, Michael Arlt, Debora Morgenstern and Tobias Hausen as well as Manuel Doerr and Thomas Christ from Prognostica GmbH Würzburg, and the AI for Science team at Google Cloud including (but not limited to): Kartik Sanu, Laurynas Tamulevičius, Nicolas Stroppa, Chris Page, Srikanth Soma, John Semerdjian, Skandar Hannachi, Vishal Agarwal and Anant Nawalgaria as well as Christoph Tittelbach from the Google account team and partners at Google DeepMind
```

---

## 6. Pioneering AI-assisted code migration: How Google achieved 6x faster migration from TensorFlow to JAX

- 日期: 2026-05-06 16:00
- 链接: https://cloud.google.com/blog/topics/developers-practitioners/6x-faster-migration-from-tensorflow-to-jax/

```
AI coding agents are rapidly becoming ubiquitous across the software industry, fundamentally changing how developers write, test, and debug daily code. While these tools excel at localized, self-contained tasks, applying them to massive, systemic codebase migrations requires an entirely new approach. 
 Google is already addressing this challenge by incorporating AI into many migration workflows: x86 to ARM (enabling workloads on Google Axion processors); int32 to int64 identifiers (to avoid running out of ids); JUnit3 to JUnit4 (for testing); and Joda-Time to java.time (a modern time library). However, AI model migration represents a whole new level of complexity that requires even more advanced methods for AI-assisted migration. 
 Translating a production-grade machine learning model from one framework to another, for example, from TensorFlow (TF) to JAX, is not a simple syntax update. It is a long-horizon task that requires untangling thousands of lines of code, managing complex states across multiple files, and preserving precise mathematical equivalence. Generic, single-agent coding assistants typically struggle under this weight — they frequently lose context over long workflows, hallucinate APIs, or fail to produce buildable code across an entire repository. 
 Google’s AI and Infrastructure team has pioneered a new approach to this industry-wide problem. The result is 6x faster model migration, a milestone Sundar highlighted in the recent Google Cloud Next keynote . In this post, we share how we deployed specialized, multi-agent AI systems to migrate some of Google’s largest-scale production models from TF to JAX. 
 Accelerating the transition from TF to JAX 
 For many teams at Google — and across the industry — the future of scalable machine learning is being built on JAX. Designed around a functional, stateless paradigm, JAX is heavily optimized for modern Tensor Processing Unit (TPU) infrastructure and XLA compilation, making it the bedrock of the modern AI stack. 
 Evolving to this future presents a monumental challenge. Thousands of production models are built on TensorFlow, a framework characterized by object-oriented, stateful layer initialization and static execution graphs. Manually migrating these models to JAX requires a fundamental rethinking of how layers interact, and how state is explicitly managed. Across large organizations, this type of migration alone represents hundreds (if not thousands) of software engineering (SWE) years — time better spent on researching new architectures and driving product innovation. 
 Overcoming this challenge with AI started as an ambitious experiment within Google’s AI and Infrastructure team, but has evolved into a repeatable blueprint for addressing complex engineering problems across the company. 
 Moving beyond single-agent coding 
 Our early experiments with agentic code translation showed promise for simple models. However, when faced with the realities of a Google-scale migration — complex, production-grade models spanning multiple files and thousands of lines of code — generic, single-agent setups struggled. They could not balance high-level structural rules with low-level execution details, resulting in a variety of failures, such as overwriting critical files or skipping necessary functionality. To overcome these common challenges inherent to enterprise migrations, we developed a highly specialized multi-agent architecture that consists of: 
 The Planner agent: Using deterministic, compiler-based static analysis, the Planner maps out the codebase's entire dependency tree. It then works alongside other agents to break the migration down into a discrete, step-by-step plan, helping ensure the migration happens logically from the "leaf nodes" (layers without unmigrated dependencies) upward. 
 The Orchestrator agent: This agent acts as the project manager. It dynamically groups plan steps into manageable chunks to keep the context window focused, injects the necessary domain knowledge, and handles failure recovery if a step doesn't build. 
 The Coder agent: Built as a reasoning and acting agent, the Coder is the workhorse. Integrated directly into our internal IDE tools, it has the ability to read files, write code, run builds, and execute unit tests. Crucially, it operates in a "test-and-fix" loop, self-correcting until it produces a compilable, verifiable component in the target language. 
 Figure: Multi-agent AI system for complex code migrations. Process diagram describing the multi-agent system used to migrate legacy model code to JAX. Image generated with Gemini Nano Banana 2. 
 Scalable validation and dynamic Playbooks 
 Generative AI models are only as good as the context they are provided. Because source and target architectures rarely map 1-to-1, we engineered a scalable, hierarchical system of Playbooks. 
 These Playbooks range from general repository instructions to highly specific "golden examples" distilled from successful manual migrations. By feeding the Orchestrator a client-specific Playbook (for instance, one tailored to YouTube's unique ranking model infrastructure), the system avoids generic hallucinations and strictly adheres to internal coding standards. This Playbook architecture is framework-agnostic, meaning it can be adapted to guide migrations between any two programming languages or frameworks. 
 Furthermore, we instituted rigorous quality metrics to ensure the generated code is actually production-ready: 
 Quantitative verification: For each unit of code, we verify correctness mathematically. In the case of the TF-to-JAX migration, the system utilizes algorithmic gradient ascent to find the maximum error between the original TF layer and the new JAX layer, mathematically verifying functional equivalence. 
 Qualitative evaluation: We also evaluate the migrated code against a set of qualitative standards. In the case of the TF-to-JAX migration, we deploy a blind-audit LLM Judge that scores the migrated code against a framework-agnostic architectural checklist, so that critical, domain-specific logic is completely captured. 
 Redefining migration velocity 
 By deploying this multi-agent system, we dramatically alter the economics of software migration. 
 In our evaluations on real-world, highly complex YouTube models (featuring thousands of lines of code, hundreds of layers, and deep metric dependencies), the multi-agent system achieved a 6.4x to 8x speedup over performing the migration manually. What traditionally took several  SWE-months can now be reduced to only a few weeks of AI-assisted code generation, followed by expert human review. 
 The system effectively handles the boilerplate, identifies target idioms, maps the dependencies, and generates the unit tests, allowing engineers to act as reviewers and architects rather than manual translators. 
 Looking ahead into the AI-assisted era 
 AI is transforming the pace of technological innovation. Without using AI to accelerate our ability to conduct large-scale migrations, it will become increasingly difficult for organizations to adopt the latest breakthroughs and maintain the security, reliability, and performance of their systems. 
 Our work migrating machine learning implementations from one ML framework to another demonstrates that by combining deterministic static analysis, strict testing loops, and specialized multi-agent architectures, we can safely automate some of the most complex software engineering challenges in the industry. A detailed description of the process is published in our technical paper . 
 This work is the result of collaboration across Google. We thank key contributors: Stoyan Nikolov, Niyati Parameswaran, Bernhard Konrad, Moritz Gronbach, Niket Kumar, Ann Yan, Varun Singh, Yaning Liang, Antoine Baudoux, Xevi Miró Bruix, Daniele Codecasa, Madhura Dudhgaonkar, Elian Dumitru, Alex Ivanov, Christopher Milne-O’Grady, Ahmed Omran, Ivan Petrychenko, Assaf Raman, Stefan Schnabl, Yurun Shen, Maxim Tabachnyk, Niranjan Tulpule, Amin Vahdat, and Jeff Zhou.
```

---

## 7. The Blueprint: Translating stream-of-conscious speech into responsive, actionable task lists

- 日期: 2026-05-06 16:00
- 链接: https://cloud.google.com/blog/topics/startups/the-blueprint-doist-stream-of-consciousness-ai-task-list-creation/

```
Welcome to The Blueprint, a new feature where we highlight how Google Cloud customers are tackling unique and common challenges across industries using the latest AI and cloud technologies. We hope to inspire others looking to innovate in their work . 
 Founded in 2007, Doist is a pioneer in async and remote-first work on a mission to simplify life’s complexities through apps like Todoist for task management and Twist for team communication. 
 The challenge: 
 We launched Ramble to take our popular Todoist application to the next level by capturing non-stop, stream-of-consciousness talking. Our inspiration was that scene from The Devil Wears Prada where Miranda Priestly rapid-fires a dozen tasks at her assistant. We asked: What if anyone could capture tasks that way? No typing, no careful formatting. Just talk and let Todoist do the organizing. That use case became our north star. 
 At the outset, we identified four big technical hurdles: 
 We needed fast and accurate real-time communication with tool-calling capabilities. 
 Multilingual suppor t at scale but with great support for slang, accents, and more. 
 As traditional assertion-based testing would not work for our platform, we would have to find a way to achieve non-deterministic output testing and semantic validation. 
 Reliable, flawless handling of audio across browsers . 
 The solution: 
 We built Ramble using Gemini Enterprise Agent Platform and its previous iteration, Vertex AI; specifically, we’re using Agent Platform to access the Gemini Flash models . We chose these over other options primarily due to the quality of Google's state-of-the-art models and its clear terms and assurances about preserving privacy. 
 Gemini’s Live API (accessed via Agent Platform) powers Ramble’s core real-time interactions and key capabilities, including native audio streaming, proactive tool calling, session resumption, and multilingual understanding. 
 Ramble sends the raw PCM audio directly to the model without pre-transcription. Gemini handles language detection, speech recognition, and semantic understanding in a single pass, reducing latency. It then invokes our purposefully designed tools ( addTask , editTask , deleteTask , etc) autonomously as the user speaks, without waiting for explicit commands. 
 The APIs in Agent Platform provide resumption tokens that let users pause and continue sessions, which is essential for mobile users who might switch apps or lose connectivity. 
 The end result is a clear, concise list of the tasks, regardless of how many, how inconsistently, or how confusingly they may have been rambled by the user. 
 The architecture: 
 The outcome: 
 Ramble has come to rely on the quality of Google’s AI models, particularly the reasoning and near-instant audio-processing capabilities of Gemini Flash. Other platforms and models offer similar capabilities, and we did bake in support for them, but none hit our internal quality bar as consistently as Gemini. When it came to a user's unstructured “rambling” and the need to fill in gaps, Gemini turned out to be the most intelligent of all the models we explored. The result was the clearest and most consistent breakdown of tasks, which was the exact magical user experience we wanted to create. 
 After an early rate-limit incident caused by unexpectedly high usage during alpha testing, we developed a deeper, more proactive partnership with Google, ensuring long-term sustainability and the support necessary for our high API usage. Since then, it's been easy for us to connect directly with Google Cloud staff, including engineers, when issues arise. 
 Here at Doist, Ramble took off both in a qualitative and quantitative sense. It’s become a hallmark experience that incentivizes us to explore tasteful applications of AI that can enhance our existing product experience, both in the B2C space as well as B2B. Beyond task creation, we’re considering several opportunities across the productivity journey, from capture to planning and even automation. 
 The details: 
 We structured our back-end to enable future voice-powered features. The architecture includes a provider-agnostic streaming layer; a dictation module for one-way audio; Ramble (our “brain dump” module); and a conversation module to support streaming bi-directional audio and future conversational features. 
 This layered design means we can ship new voice features with minimal additional infrastructure work. It also enables provider flexibility; although we’re using Gemini Enterprise Agent Platform in production, our abstraction layer also easily supports other solutions. 
 In addition to helping us tackle three of our four key technical challenges, Agent Platform delivered some nice surprises. First, session resumption was easier than we expected. We initially thought maintaining conversation state across reconnections would require complex server-side session management. But once we understood Agent Platform’s resumption token approach (the token is provided by the API and changes with each context update), implementation was straightforward across all platforms. 
 Second, context injection worked on the first try. We spent considerable time designing how to provide user context (projects, labels, preferences) to the model. We explored complex retrieval strategies and dynamic context windows. In the end, the simple "v1" approach—just passing most of the user's metadata in the system prompt—worked remarkably well. 
 For testing, we combined structural validation (task count, priority levels, date presence, etc) with semantic validation (did the model understand the user's intent?) following the LLM-as-judge approach. A second Gemini model evaluates whether the output semantically matches the expected outcome. Native speakers from our global team recorded real-world scenarios in their languages and local accents (15+ language variations and over 100 recordings total), with each scenario having expected semantic outcomes (e.g., "should create 3 tasks: one about calling family, one about shopping, one about exercise on Saturday at 11 AM"). 
 We then created a defined pass-rate threshold for the test suite overall, while also monitoring per-language performance to catch regressions. This approach lets us evaluate new model versions systematically, understanding not just overall performance but also which specific languages might see improved or degraded experiences, and make data-informed decisions. 
 Ultimately, Ramble is a resounding success in helping our users handle the chaos of day-to-day life. It joins the ranks of Todoist’s Quick Add — our existing natural-language task input — in providing yet another way to capture tasks that is the best in its category.
```

---

## 8. What's new in IAM: Security, governance, and runtime defense

- 日期: 2026-05-06 16:00
- 链接: https://cloud.google.com/blog/products/identity-security/whats-new-in-iam-security-governance-and-runtime-defense/

```
The AI era demands a fundamental shift in security, and that includes identity and access management (IAM). Traditional controls simply aren’t built for autonomous AI agents that interact with sensitive data at machine speed, a reality we address with our new IAM advancements for the agentic enterprise era. 
 Engineered as built-in Google Cloud capabilities to secure the rapidly-expanding world of AI agents, at Google Cloud Next we introduced a new security and governance paradigm for managing agent identity and access. This comprehensive framework focuses on foundational Agent Identity and an Agent Gateway with Identity-Aware Proxy , while integrating robust agent access management, agent guardrails, and runtime defense to enable a secure cloud environment for your organization. 
 Security and governance for agents. 
 Agent Identity 
 AI agents require verifiable identities to operate securely and with accountability. Agents on Google Cloud can now receive a dedicated Agent Identity : a new, first-class principal type distinct from human identities or generic service accounts. 
 Built on the open Secure Production Identity Framework For Everyone (SPIFFE) standard , these identities are cryptographically protected, strongly attested, and automatically provisioned. Agent Identity allows you to recognize agents whether they are operating autonomously or on behalf of a user. 
 With Agent Identity, agents are recognized as an independent identity type, allowing you establish strong governance and agent-specific authorization rules. 
 To support this, we are announcing the following updates: 
 Agent Identity for Agent Runtime is now generally available, and Agent Identity for Gemini Enterprise Agent Platform is in preview, granting first-class identity to agents across these platforms. 
 Agent Identity Auth Manager is in preview, streamlining complex OAuth flows for agents acting on behalf of users by securely handling credentials and tokens. 
 Certificate Manager support for Agent Identity certificates is also in preview, providing a single pane of glass for managing all agent-related certificates. 
 Agent Gateway 
 Agent Gateway enables policy enforcement for all agent-to-agent and agent-to-tool connections. Because AI agents behave non-deterministically, all agent traffic on Google Cloud can now be routed through the Agent Gateway. This centralized flow allows you to enforce strict policies that prevent agents from accessing unauthorized or undesired third-party endpoints. 
 To extend Zero Trust enforcement to agents and AI systems, the following capabilities are also available in preview: 
 Identity-Aware Proxy (IAP) for Agents : IAP integrates with Agent Gateway, providing default-on, identity-centric security. It enforces granular access control policies using IAM, based on agent identities and rich contextual attributes derived from the model context protocol (MCP). 
 Context-Aware Access (CAA) for Agents : CAA evaluates contextual signals such as device health, IP address, and location for agent identities before granting access to resources. 
 Agent access management 
 Managing agent access and the operations they can perform is critical to address dormant permissions. Our defense-in-depth approach to agent access management ensures agents only have the privileges they need. To help enforce least privilege access, Agent Identity is now fully supported across Google Cloud's policy, monitoring, and governance solutions. 
 IAM Allow and Deny policies for Agent Identity are now generally available, letting you control which agents can access specific resources. 
 Principal Access Boundary (PAB) for Agent Identity is now in preview. PAB acts as a protective additional layer, setting hard limits on the resources a specific agent or group of agents can never access, regardless of other permissions they might inherit. 
 Unified Access Policy (UAP) for Agent Identity is coming soon. These new access policies act as a rulebook for AI agents, allowing granular control over agent access to tools, APIs, and resources. Policies can be based on the Agent Identity, the effect (allow or deny), the operation, and specific conditions. They can even mandate human-in-the-loop (HITL) approvals for sensitive actions, ensuring critical decisions have human oversight. 
 All these policy types support the new Agent Identity nomenclature, including hierarchy-aware constructs built on SPIFFE's trust domain and namespace model. This means you can govern agents individually or as groups using the same familiar policy mechanisms already in use for human and service account identities. 
 Agent guardrails 
 Beyond providing strong access management capabilities, we must also ensure that AI agents can not exfiltrate data at runtime or pull in unauthorized external data. VPC Service Controls (VPC-SC) support for Agent Identity as first-class principals in ingress and egress rules is now in preview, allowing you to prevent data exfiltration and letting you control the data traversing in and out of your perimeter. 
 Additional enterprise-wide guardrails are available to enforce that only specific resource configurations are allowed in your cloud environment: 
 Organization Policies : Administrators can enforce constraints, such as restricting agent creation to specific regions or preventing agents from creating public IP addresses. 
 Custom Organization Policies : Cloud administrators can tailor constraints to unique agent behaviors and compliance requirements. 
 To help enterprises continuously monitor and secure AI agents, our new Agent Security dashboard for Agent Platform , in preview, offers agentless discovery, vulnerability scanning, runtime threat detection, and graph-based risk discovery. 
 Key capabilities of this platform include: 
 Agent security posture: Provides secure-by-design templates and Google-recommended controls for building agentic applications. 
 Agent vulnerability scanning : Identifies weaknesses in agent packages and skills, catching flaws before deployment. 
 Agent asset discovery : Delivers an organization-wide inventory of all AI agents and their associated assets. The inventory process will soon differentiate between shadow AI agents and sanctioned AI agents in your organization. 
 Collectively, these capabilities help to ensure that agents are secure by design and continuously monitored. 
 Runtime defense 
 While agent access management and guardrails can help you manage permissions and prevent data exfiltration, runtime defense controls can provide an additional protection layer addressing runtime security risks and ensuring AI agents function as intended. 
 Model Armor provides real-time protection for user, model, and agent interactions to protect against runtime risks such as prompt injection, tool poisoning, and sensitive data leakage across Google Cloud services and Gemini Enterprise Agent Platform. It now provides inline protection for Agent Gateway , Agent Runtime , Google Cloud MCP servers , Langchain (in preview) and Firebase (generally available) to help developers add runtime guardrails and sanitization of agent traffic and interactions without the need to change code. 
 These integrations expand Model Armor's existing inline protections for Agent Platform models, Gemini Enterprise, Apigee, Google Kubernetes Engine inference gateway and load balancers, as well as API interfaces. 
 Beyond agents: Additional IAM capabilities announced at Next '26 
 We’re rolling out a comprehensive suite of new capabilities to manage identity, access, and governance at scale. We’re simplifying user provisioning with SCIM support for Workforce Identity Federation, streamlining Gemini Enterprise onboarding, and ensuring strong machine identities with Managed Workload Identity . 
 We’re also making access management smarter and more secure with the general availability of Gemini-powered IAM Role Picker , Fine-Grained Access Control for BigQuery , and enhanced Privileged Access Manager insights . To mitigate access risks and further strengthen security, we have introduced a VPC Service Controls violation analyser , integrated Identity-Aware Proxy with Cloud Run , mandated multi-factor authentication for specific cohorts , and extended Context-Aware Access to service accounts. 
 To help you organize and centralize control over your expanding cloud footprint, Custom Organization Policy now supports over 130 Google Cloud products and services . 
 Learn more 
 These updates represent a significant leap in how we help you manage your agentic cloud ecosystem, but what hasn’t changed is our commitment to building a secure foundation for your organization. We continue to fortify Google Cloud’s security platform, ensuring that you have a robust and trustworthy environment for all your workloads, including those powered by AI. 
 By centralizing control and automating identity governance, you can scale your AI initiatives with the confidence that your most critical data remains protected. To learn more, view the Next '26 session recording for an overview of these announcements. For a closer look at how to implement these security best practices in your own organization, please check out our documentation . 
 Related Article 
 Next ‘26: Redefining security for the AI era with Google Cloud and Wiz 
 Today at Google Cloud Next, we’re showcasing how we can help you defend against threats at machine speed, protect AI and multicloud envir... 
 Read Article
```

---

## 9. Google named a Leader in the 2026 Gartner® Magic Quadrant™ for Cyberthreat Intelligence Technologies

- 日期: 2026-05-06 16:00
- 链接: https://cloud.google.com/blog/products/identity-security/google-named-a-leader-in-the-2026-gartner-magic-quadrant-for-cyberthreat-intelligence-technologies/

```
At Google, we see firsthand how cyber threats can outpace traditional defense mechanisms — and how agentic threat intelligence can help bridge the gap. We have a vision for agentic defense where autonomous AI agents, powered by Gemini and fed by our unmatched threat visibility, can reason through complex malware and preemptively neutralize threats at scale. This evolution can help security teams shift from anticipating risks to autonomously disrupting attack chains in real-time, effectively out-maneuvering adversaries before they can strike. 
 We are proud to announce that Gartner has named Google a Leader in the 2026 Magic Quadrant for Cyberthreat Intelligence Technologies . We believe this recognition validates our unique ability to unify Mandiant’s unparalleled incident response, VirusTotal’s massive, crowd-sourced threat repository, Google’s infrastructure visibility, and Gemini integration into a unified operational ecosystem. 
 Given the scale of the aforementioned platforms and operations, and being at every stage of the kill chain - from early deep dark web chatter to IR breach investigations - allows us to provide agents with a distinctive knowledge substrate to autonomously pre-empt threats. 
 Google a Leader in the 2026 Magic Quadrant for Cyberthreat Intelligence Technologies based its Completeness of Vision and Ability to Execute. 
 Built for enterprises and organizations that require large-scale visibility, Google Threat Intelligence can help transform how teams operationalize insights. Gemini can help analysts synthesize vast amounts of intelligence so they can take decisive action. 
 By protecting billions of devices and mailboxes daily, spending over 500,000 hours investigating incidents in 2025, and leveraging insights from hundreds of global threat experts, Google provides a level of breadth and depth in threat visibility that helps organizations stay ahead of even the most sophisticated global actors. Our multisignal approach provides early warning on both broad and targeted attack techniques. 
 We are also bringing dark web intelligence into the AI era by using the latest Gemini models to dramatically increase accuracy by forgoing keyword lists that are often a source of chronic toil, induced by as much as 90% false positives. 
 Conversely, our internal tests show Google Threat Intelligence can analyze millions of daily external events – with 98% accuracy. This high accuracy rating helps ensure that security teams are alerted to the most relevant threats and drastically reduces the noise of false positives. 
 To empower security teams exactly where they work, we have turnkey integration with Google Security Operations to enable automated rule generation and closed-loop policy enforcement. We maintain an open architecture with a vast ecosystem of partners to ensure that every organization can uplift its security operations regardless of its existing tech stack. This includes robust integrations with hundreds of security vendors enabling you to take action quickly on active and potential threats. 
 To complement our technology, we provide the human expertise needed to navigate the complex threat landscape. For organizations facing more challenging scenarios, Mandiant Threat Intelligence services help security teams navigate complex scenarios through direct collaboration with our global experts. This expertise is also codified in-product into off-the-shelf prompts, no-code agents and a native agentic skills layer. This combination of automated intelligence and human expertise allows organizations to have confidence in the intelligence they are using and the actions they are taking. 
 Delivering measurable value for security teams 
 Google Threat Intelligence delivers a measurable impact on the speed and scale of modern defense. Customers have identified 139% more threats proactively and made their CTI teams 46% more efficient . These gains enable teams to move beyond manual triage and focus on high-value investigations. 
 By accelerating detection engineering, Google Threat Intelligence identifies malicious infrastructure before it is used in campaigns. This transition allows defenders to anticipate adversary maneuvers and disrupt attack chains earlier, reducing threat dwell time and organizational risk. 
 Executing on our vision 
 We are very pleased that Gartner recognized us as a Leader in cyberthreat intelligence technologies. We feel we continue to push the boundaries of what is possible in threat research such as being the first ones to bring malware analysis to the AI era , the first ones to bring dark web to the agentic era and we continue to deliver the autonomous decision advantage to preemptively neutralize the right threats with the right action and the right context. 
 To learn more about Google’s position as a Leader, you can download the full 2026 Gartner® Magic Quadrant™ for Cyberthreat Intelligence Technologies here . 
 Source: The 2026 Gartner® Magic Quadrant™ for Cyber Threat Intelligence Technologies, Jonathan Nunez, May 4th, 2026 G00839252 
 GARTNER® is a registered trademark and service mark of Gartner, Inc. and/or its affiliates in the U.S. and internationally, and MAGIC QUADRANT is a registered trademark of Gartner, Inc. and/or its affiliates and are used herein with permission. All rights reserved. This graphic was published by Gartner, Inc. as part of a larger research document and should be evaluated in the context of the entire document. The Gartner document is available upon request from Google. Gartner does not endorse any vendor, product or service depicted in its research publications, and does not advise technology users to select only those vendors with the highest ratings or other designation. Gartner research publications consist of the opinions of Gartner research organization and should not be construed as statements of fact. Gartner disclaims all warranties, express or implied, with respect to this research, including any warranties of merchantability or fitness for a particular purpose.
```

---

## 10. Fitting the future: How Breuninger boosted sales with its "be your own model" AI

- 日期: 2026-05-06 16:00
- 链接: https://cloud.google.com/blog/topics/retail/how-breuninger-boosted-sales-with-its-be-your-own-model-ai/

```
“How will this look on me?” It’s the question every online fashion shopper asks, and one that most retailers still can’t answer well. 
 Breuninger, a fashion and lifestyle company based in Germany, thought emerging generative media models could be a good fit for this fashion conundrum. Working with Google Cloud, they built a virtual try-on experience that lets shoppers see high-end fashion on their own bodies using a simple selfie. 
 From trusted tester to live product 
 The project began when the Google Cloud team in Germany invited Breuninger to join the Trusted Tester Program for the Virtual Try-On (VTO) API. Breuninger’s data team in Germany worked directly with Google’s engineers in California, testing and refining the technology in three stages: 
 Catalog enrichment : The team first explored the VTO API to dress professional models in different outfits. This helped Breuninger to cover a greater variety in user tests without having to plan new photoshoots. 
 Body type selection : They then added a feature that let users choose from different body types to see how clothes would drape on a silhouette similar to their own. 
 The 'Be your own model' breakthrough : User feedback showed that customers did not just want to see a model; they wanted to see themselves. 
 The product owner at Breuninger noted that this close collaboration allowed the team to share user feedback with developers in real time. This speed helped them move from using pre-selected models to a user-first, selfie-based approach. 
 Three levels of virtual try-on 
 The project revealed three levels at which retails can adopt VTO, depending on how much personalization they want to offer: 
 Approach 
 Interaction 
 Use case 
 Level 1: Catalog enrichment 
 Offline batch processing 
 Dress standard models in new collections at scale to update product pages without manual shoots. 
 Level 2: Body type selection 
 Online on-request 
 Offer predefined models for users to choose from, similar to the virtual try-on feature on Google Shopping. 
 Level 3: 'Be your own model' 
 Online personalized 
 The most personal experience where users upload a selfie to see themselves in specific items or full outfits. 
 Building for scale with Flutter 
 Scaling a personalized experience required more than just an AI model. Selfies come in wildly different lighting and quality, so the team built preprocessing tools to make sure the final images met Breuninger’s brand standards. This project also accelerated Breuninger’s move to a Flutter-based platform. The VTO feature was the first module built by a self-sufficient product team using this new structure, which helped the team move from a vision to a live launch in only three months. 
 Real results during the holiday season 
 During a six-week A/B test over Black Week and the holiday season, the team found that shoppers who used the virtual try-on converted at a higher rate and generated a stronger contribution margin than those who didn't. Customer surveys reinforced the numbers: shoppers responded well to the high image quality and the personalized experience. Perhaps most telling, the team found that VTO became a tool for building style confidence — helping customers feel sure about a purchase before they made it. 
 What’s next 
 The pilot’s success has set up a broader rollout and international expansion, with physical fit and sizing support on the roadmap. Breuninger continues to refine the experience based on how customers actually use it in everyday shopping — the same user-first approach that shaped the project from the start. 
 To explore how generative AI can help your business create similar experiences, visit Google Cloud's Virtual Try-On solution . You can also try the feature yourself in the Breuninger app . 
 This work wouldn’t have been possible without the contributions from peers at both Breuninger, and Google Cloud. Thanks to Markus Peetz, Jorina Hilser, Martin Csengeri, Jay Deutinger, Sofia Widmayer, David Schowalter, Tobias Götze, Eric Karge, Abdul Mateen, Besnik Brahimi, Oliver Fesseler, and Lisa Beutner from Breuninger, and Khanh LeViet, Jorj Ismailyan, and Matt Chaban from Google Cloud.
```

---

## 11. Public sector momentum and mission impact at Google Cloud Next ‘26

- 日期: 2026-05-05 21:00
- 链接: https://cloud.google.com/blog/topics/public-sector/public-sector-momentum-and-mission-impact-at-google-cloud-next-26/

```
The agentic era is here, and the public sector is at the forefront of leading this transformation. 
 At Google Cloud Next ’26, it was clear that academia and public sector organizations are no longer just exploring the possibilities of AI; they are actively scaling it across their organizations to drive tangible mission impact. From the main stage to the show floor, we featured over 40+ inspiring public sector customers and partner speakers who shared how AI and agents are empowering their workforces, unlocking new levels of productivity, and transforming how services are delivered. 
 Let’s take a closer look at the public sector sessions and activations that brought the agentic era to life at Google Cloud Next '26. 
 The blueprint for agentic transformation 
 We were honored to bring together some of the brightest minds in government, technology, and public service to share how they are shaping the future of public service. During a spotlight session on “Agentic transformation in the public sector”, we heard from Karen Dahut, CEO of Google Public Sector alongside Ted Ross, CIO, City of Los Angeles, Jeremy Walsh, Chief AI Officer, The U.S Food and Drug Administration (FDA), and Pavan Pidugu, Chief Digital and Information Officer, The U.S. Department of Transportation (DOT). These leaders shared their blueprints for scaling AI and agents across their organizations to boost productivity, drive impact and advance their missions. As these leaders demonstrated, successfully scaling AI and agents means being willing to disrupt the status quo, treating agents as force multipliers, and driving human-centered adoption that transforms everyday workflows. You can catch the full spotlight session here and a brief recap of the session here . 
 Transforming public service with AI and agents 
 Beyond the main stage, we heard from over 25 Google Public Sector customer and partner speakers during breakout sessions who showcased how AI and agents are transforming every facet of the public sector. From architecting resilient transportation networks and building the AI-ready campuses of tomorrow, to accelerating scientific breakthroughs and advancing healthcare outcomes, attendees gained actionable insights for the agentic era. You can watch the recordings for select public sector breakout sessions here: 
 Building the AI-ready and intelligent campus of tomorrow, today 
 From silos to synergy: Architecting the AI-powered governments of tomorrow 
 Transform community services and outcomes with AI 
 Dedicated programming for the public sector 
 At Next ’26, we expanded our specialized programming and peer to peer engagement opportunities for public sector attendees. We hosted dedicated programming on the sidelines of Next for National Security and Accelerated Research to provide learning and engagement opportunities for our customers across a range of topics including our AI-optimized infrastructure and latest Gemini model and agentic innovations. Through our Partner Summit programming, we shared how we are building the foundation for AI across the public sector through our partner ecosystem. 
 Hands-on innovation at the Google Public Sector hub 
 The best way to learn about agentic AI is to experience it firsthand. To that end, we introduced a first of its kind Mission Talks activation at our Main Street Beacon Theater where we hosted 28 sessions with live demonstrations showcasing how agents can be deployed to solve mission-critical challenges. Added to that, at the Google Public Sector Hub on the expo show floor, attendees rolled up their sleeves and created hundreds of agents across a wide range of use cases, underscoring the immense interest and readiness to build with this powerful technology. 
 Let’s build what’s next 
 The momentum we saw at Google Cloud Next ’26 is just the beginning. Whether you are looking to scale your use case across the organization, empower your internal champions, or are just getting started, Google Public Sector can help provide a clear path to drive impact and advance your mission. We invite you to keep the momentum going and register for our Best of Next webinar for the public sector where you can catch key public sector highlights from the event. The agentic era is yours to lead - and we can’t wait to build what’s next, together.
```

---

## 12. Five must-have guides to move agents into production with Gemini Enterprise Agent Platform

- 日期: 2026-05-05 16:00
- 链接: https://cloud.google.com/blog/topics/developers-practitioners/five-guides-to-building-and-scaling-production-ready-ai-agents/

```
Building AI agents that work well in a demo is one thing, but running them in production requires serious infrastructure. 
 At Google Cloud Next '26, we introduced Gemini Enterprise Agent Platform to help developers build, deploy, scale, govern, and optimize  autonomous AI agents. From managing long-running state and enforcing security with the Agent Governance Stack, to orchestrating complex workflows using Agent Development Kit, these tools help you treat your agent fleet with the same rigor as your engineering organization. Here is a look back at our five-part series covering the architecture patterns and best practices you need to move your agents into production. 
 1. Agent design patterns for long-running AI agents 
 Developers spend weeks perfecting prompt engineering, tool calling, and response latency. But none of that  matters when your agent loses its reasoning chain over a five-day task. At Next 26, we announced that Agent Runtime now supports long-running agents that maintain state for up to seven days. 
 In this article, we’ll share five essential agent design patterns for building long-running agents with Agent Runtime. You’ll learn how to implement checkpoint-and-resume mechanisms to recover from failures without starting over. We also cover how to build delegated approval workflows where the agent pauses for human review while consuming zero compute resources. 
 Read the full guide on long-running agents here . 
 2. The agent governance stack 
 A misconfigured SaaS tool leaks data passively, but a misconfigured agent takes bad actions actively. The pattern we saw with shadow IT in 2015 is repeating itself with AI agents. 
 To manage this risk, we explain why you must treat your agent fleet with the same rigor as  your engineering organization. We outline a five-layer governance stack designed to provide your r security team with precise visibility and control. The foundation begins with Agent Identity, assigning every agent a unique cryptographic badge to isolate access. From there, we explore how to use Agent Registry for centralized tool governance and Agent Gateway to enforce natural language security policies across your fleet. The stack concludes with behavioral anomaly detection and a unified security dashboard to monitor your overall risk. 
 Read the full guide on the agent governance stack here . 
 3. Must-have multi-agent orchestration patterns in ADK 
 Building a single AI skill is relatively straightforward, but orchestrating multiple skills across different agents is notoriously difficult. With the new updates to Agent Development Kit (ADK), we introduced graph-based workflows, collaborative agents, and a formalized skills framework to solve these orchestration failures. 
 Our third guide details five multi-agent orchestration patterns you can use to build reliable systems. You will find code examples for building hybrid graphs that combine hard-coded business rules with flexible AI reasoning. We also show how to use the coordinator-specialist pattern to avoid building monolithic, unpredictable agents. The guide concludes with deep dives into skill composition, cross-language pipelines, and secure sandboxed executors for running arbitrary code. 
 Read the full guide on ADK multi-agent patterns here . 
 4. Deep dive: How A2A and MCP work togethe r 
 Organizations will rarely build every AI agent they need entirely from scratch. The real value comes when agents built by different teams, in different languages, and across different organizations can securely discover and collaborate with each other. 
 In our final guide, we explore five integration patterns using the Agent-to-Agent (A2A) and Model Context Protocol (MCP) standards. You will see how Agent Cards allow agents to publish their capabilities so coordinator agents can find them through the Agent Registry. We also show how MCP acts as a universal tool bridge to connect your agents to databases and enterprise systems without custom integration code. The article finishes with strategies for cross-organization federation that involves agents from different organizations collaborating on shared tasks using the Agent Gallery in Gemini Enterprise and building ambient event meshes for agents that react to events continuously in the background, without waiting for user requests. 
 Read the full guide on agent interoperability here . 
 5. Atomic agent blueprints on Google Cloud’s Agent Garden 
 Building multi-agent systems from scratch presents complex design challenges, including finding the optimized design pattern for your use-case, orchestration failures and evaluation loops. You can spend weeks reinventing the wheel, trying to get your agents to be ready for production - or you can start with architectures that already work, with our new Atomic Agents in Agent Garden. 
 Read the full guide to learn about pre-built Agent Blueprints in Agent Garden 
 Watch the complete Agent Platform explainer 
 To see these architectural patterns in practice, watch this technical walkthrough of the Gemini Enterprise Agent Platform. This deep dive covers the complete agent lifecycle, showing you exactly how to move from initial code to a secure, scalable AI Agents in production. 
 What is Gemini Enterprise Agent Platform? 
 Dive into the code with Agent Platform samples on GitHub 
 Access our curated repository of code samples and tutorials for the Gemini Enterprise Agent Platform. This GitHub repository provides practical examples for the entire agent lifecycle, giving you the exact code needed to build, scale, govern, and optimize your autonomous fleets. 
 Get started with Gemini Enterprise Agent Platform 
 Moving agents into production requires both robust infrastructure and the flexibility to choose the right reasoning engine for the task. The Gemini Enterprise Agent Platform bridges this gap, allowing you to build, govern, and scale autonomous workflows with complete enterprise control. 
 Through first-class integration with Model Garden, your agent fleet has direct access to more than 200 leading models. You can route tasks to the best available option, whether that is a first-party model like Gemini 3.1 Pro or Lyria 3, an open model like Gemma 4, or third-party models like Anthropic’s Claude, Opus, Sonnet or Haiku. 
 Visit Agent Platform in the Google Cloud console to explore new features and start building today.
```

---

## 13. Introducing Agent Gateway ISV ecosystem for security and governance

- 日期: 2026-05-05 16:00
- 链接: https://cloud.google.com/blog/products/identity-security/introducing-agent-gateway-isv-ecosystem-for-security-and-governance/

```
Managing agents and their actions can quickly grow in complexity and introduce security risks unique to AI. To address these challenges, at Google Cloud Next we announced Agent Gateway to provide simple, secure, and governed connectivity across all user-to-agent, agent-to-agent, and agent-to-tools interactions. 
 As part of Gemini Enterprise Agent Platform , Agent Gateway provides a programmable data plane for your AI agents. It connects easily with a wide array of security providers, giving your team the flexibility to inject custom logic and third-party security controls directly into the request path. 
 To support the agentic enterprise in today’s multicloud and multi-AI world , we’re partnering with leading identity and AI security providers to integrate with Agent Gateway and help ensure that your security posture remains as flexible as the agents you’re building. 
 Agent Gateway partner ecosystem for agent security and governance. 
 Broadcom : Agentic AI introduces high-speed, autonomous data exchanges across LLMs, tools, and other agents, dramatically expanding the risk of data exfiltration through new, unmonitored leakage points. To counter this, Symantec and Google Cloud are partnering to integrate Symantec Data Loss Prevention (DLP) scanning as a service extension for the Agent Gateway, which serves as the network-level enforcement point for all agent traffic. This integration enables real-time inspection and enforcement of existing DLP policies across agent communications — including LLM inference requests and MCP tool calls — without requiring any changes to application code. 
 Check Point : Securing your AI transformation across both employee adoption and runtime innovation, Check Point’s AI Defense Plane can discover and govern sanctioned and unsanctioned, shadow AI usage. AI Defense Plane’s runtime protections integrate with Agent Gateway to provide low-latency inspection of prompts, responses, and tool interactions — preventing agent manipulation, sensitive data leakage, and tool misuse, so organizations can confidently scale AI. 
 Cisco : Integrating Cisco AI Defense with Agent Gateway can help enforce runtime protections for every AI interaction, including those that use model context protocol (MCP). These guardrails can help mitigate threats like prompt injection and data exfiltration, and agent-specific risks like tool exploitation and misuse. 
 CrowdStrike : Extending the AI-native CrowdStrike Falcon platform into the Agent Platform including Agent Gateway ecosystem can help CrowdStrike deliver guardrails, visibility, and control as agentic AI systems move from experimentation into production. Integrations including CrowdStrike Falcon AI Detection and Response (AIDR) and CrowdStrike Falcon Shield can provide secure operation of agents across the ecosystem. 
 Exabeam : Delivering behavior‑driven security analytics at enterprise scale, Exabeam New‑Scale Analytics is purpose‑built to secure Google AI and Agent Platform environments. Exabeam can ingest and analyze telemetry from Agent Platform including Agent Gateway, applying behavioral analytics to identify anomalous and high‑risk AI agent activity. Together, Google provides the AI infrastructure and controls, and Exabeam delivers the enhanced behavioral intelligence, governance, and continuous security oversight required to operate AI agents safely at scale. 
 F5 : F5 AI Guardrails provides runtime protection for agents against data leakage, harmful outputs, and adversarial attacks. Integrated via Agent Gateway, it enforces data security and policy controls to ensure agent interactions remain governed and compliant across all models. 
 Netskope : Netskope One DLP On Demand with Agent Gateway inspects data at the precise moment it moves through your AI workloads and enforces the data security policies your team has already built. By embedding DLP in their architectures, organizations can govern sensitive data generated and routed by AI agents without creating new configurations, ensuring data security evolves alongside cloud and AI innovations. 
 Okta : Okta for AI Agents provides centralized identity governance and access control for Agent Gateway. With Okta as the identity layer, Google’s policy engine can defer access decisions to Okta, enabling organizations to govern which users and agents can access specific agents and tools. Agents created in Google Cloud can also be automatically registered in Okta, keeping identity and governance policies in sync. 
 Palo Alto Networks : Deploying Palo Alto Networks Prisma AIRS as an AI security layer with Agent Gateway can provide the real-time security and governance necessary to oversee agentic interactions and intercept adversarial attacks on AI before they can compromise the system. This architectural integration can help ensure that as you scale your autonomous agents, every agentic action is validated against enterprise safety and security policies, providing comprehensive operational integrity without hindering the speed of innovation. 
 Ping Identity : Ping Identity integrates with Agent Gateway to bring runtime identity and real-time, fine-grained authorization to agent and tool traffic. The integration with Agent Gateway ensures every request is continuously verified based on user, agent, context, and policy, rather than relying on static credentials. Together, they provide centralized, consistent governance and visibility across all agent interactions without requiring changes to application code. 
 Saviynt : Saviynt provides identity security and governance that helps enterprises govern every identity — human, non-human, and AI — across cloud environments. Saviynt’s integration with Agent Gateway provides live identity intelligence for every AI agent access request, evaluating intent, data sensitivity, and organizational policy in real time before access is granted. This ensures AI agents remain purpose-bound and continuously governed, with high-risk actions surfaced for human oversight and a defensible audit trail for compliance. 
 Silverfort : Silverfort provides identity security for agentic workloads by extending its patented Runtime Access Protection (RAP) to agent platforms, automatically discovering AI agents, mapping each to its human owner, and surfacing risks such as overprivileged access and stale credentials. By integrating directly with Agent Gateway, Silverfort can authenticate and authorize every agent-to-resource request at runtime, blocking unauthorized actions before they reach downstream systems. 
 Thales (Imperva) : Thales provides advanced web application and API security for the Agent Platform, including security for client‑to‑agent traffic leveraging Agent Gateway. Imperva for Google Cloud (IGC), currently in preview, deploys natively in Google Cloud, eliminating the need for external software-as-a-service (SaaS) integrations and avoiding traffic redirection outside of Google’s infrastructure. 
 Zscaler : Providing runtime protection and governance for AI apps, models, and agents, Zscaler AI Guard can help enable real-time inspection of prompts and responses to detect malicious inputs like prompt injections and prevent sensitive data leakage through advanced content moderation and data protection detectors. The Zscaler AI Guard integration with Agent Gateway can help ensure that agentic workflows remain secure, compliant, and aligned with enterprise security policies. 
 As enterprises build and deploy a wide range of agents and agentic use cases, Agent Gateway supports a wide variety of agentic security controls tailored to your unique operational needs. Our approach can help your business meet compliance and governance requirements, while offering the freedom to use your choice of security provider. 
 To learn more about how our partners can elevate your Google Cloud experience, reach out to our team for a personalized consultation and discover the power of an open, integrated approach.
```

---

## 14. Cloud Engineer’s AI Toolkit: Sign up Now for a Developer Workshop Near You!

- 日期: 2026-05-05 15:00
- 链接: https://cloud.google.com/blog/topics/developers-practitioners/cloud-engineers-ai-toolkit-sign-up-now-for-a-developer-workshop-near-you/

```
The world of AI is rapidly shifting from experimental Large Language Models to an era of Agentic AI. In the agentic era, autonomous software agents act on behalf of employees and consumers—driving a fundamental change in commerce and business operations. This transition presents a critical new challenge: how to securely build , deploy , and govern agents at enterprise scale. 
 That’s why we’re hitting the road across North America for a series of hands-on workshops designed to move you past the theory and into production. This isn't a sit-and-listen lecture; it’s a "bring your laptop and build" session. You will gain hands-on experience for the exact skills required to transition your organization into this new agentic era. Whether you're looking to harden your Kubernetes clusters for AI or transform your data warehouse into a powerful engine for autonomous agents, this program will equip you with the practical toolkit used by leading enterprises. 
 Who should attend 
 This program is designed for Platform and Security Engineers, as well as Data Practitioners. 
 For Platform and Security Engineers 
 If you’re a Platform, Security, or DevOps Engineer , this is your toolkit for securing and scaling the next generation of workloads. 
 What you need: Foundational knowledge of GKE and containerization. 
 What you’ll do: Master defense-in-depth strategies, secure inference endpoints, and automate cluster operations using natural language. 
 For the Data Practitioners 
 Calling all Data Engineers, Analysts, and Scientists . If you’re ready to bridge the gap between traditional analytics and Agentic AI, this track is for you. 
 What you need: Some cloud experience and basic SQL. A little Python knowledge goes a long way, but we’ll guide you through the rest! 
 What you’ll do: Build governed pipelines, unlock multimodal insights from unstructured data, and deploy autonomous agents that turn dashboards into action. 
 What you’ll build 
 The labs are designed to take you from raw infrastructure to a full-stack agentic application. 
 Track 1: GKE + Data 
 AI-Augmented Ops: Use Gemini and MCP servers to manage clusters with natural language instead of manual slogging. 
 Secure Sandboxing: Deploy AI agents in hardware-isolated environments to safely execute AI-generated code. 
 Massive Scale: Use GKE to process massive datasets and create complex knowledge graphs. 
 Track 2: Data Engineering & Analytics 
 Governed Ingestion: Use Spark and Knowledge Catalog to build a unified, governed data layer for business-ready insights. 
 Conversational Analytics: Integrate vector search and multimodal data (images/logs) to create a "talk to your data" experience. 
 Graph-Powered Agents: Use BigQuery Graph, Knowledge Catalog and the Agent Development Kit (ADK) to build agents that understand complex relationships. 
 Note: These sessions are interactive. You must bring your own laptop and power cable to participate. 
 Ready to build? 
 While theoretical knowledge is valuable, nothing beats hands-on experience guided by Google experts. Registration is officially open for the upcoming sessions listed below. Come build with us! Note that different dates host different tracks. 
 Track Location Date Registration 
 GKE + Data New York, NY May 26, 2026 Register Now 
 GKE + Data Austin, TX June 2, 2026 Register Now 
 GKE + Data Sunnyvale, CA June 9, 2026 Register Now 
 GKE + Data Seattle, WA June 11, 2026 Register Now 
 GKE + Data Toronto, ON June 24, 2026 Register Now 
 Data Engineering & Analytics Toronto, ON June 25, 2026 Register Now 
 Data Engineering & Analytics Chicago, IL June 30, 2026 Register Now
```

---

## 15. Agent Factory Recap: How Gemma 4 Taught Itself Physics

- 日期: 2026-05-05 11:54
- 链接: https://cloud.google.com/blog/topics/developers-practitioners/agent-factory-recap-how-gemma-4-taught-itself-physics/

```
In this episode of The Agent Factory, Vlad Kolesnikov and I sat down with Omar Sanseviero from the Developer Experience team at Google DeepMind. We explored the groundbreaking release of Gemma 4: a new family of open models designed to bring high-level intelligence and agentic capabilities directly to consumer hardware and mobile devices. Since the launch last month, Gemma 4 had over 50 million downloads! 
 This post guides you through the key ideas from our conversation. Use it to quickly recap topics or dive deeper into specific segments with links and timestamps. 
 Gemma 4 - What is it? 
 Gemma 4 is the latest generation of open models from Google DeepMind, built on the same foundational research as Gemini 3. The family is designed to deliver exceptional "intelligence per parameter" across a range of deployment scenarios, from mobile phones to powerful workstations.The Gemma 4 model family now spans three distinct architectures: 
 Small Sizes (E2B & E4B): Optimized for ultra-mobile, edge, and browser deployment (such as Pixel or Chrome). 
 Dense (31B): A powerful 31-billion parameter model that provides server-grade performance for local execution on consumer GPUs. 
 Mixture-of-Experts (26B MoE): A highly efficient architecture designed for high-throughput tasks and advanced reasoning. 
 With the shift to an Apache 2 license , these models provide developers and startups with the flexibility to build, modify, and commercialize applications while maintaining full control over their infrastructure. 
 Omar Sanseviero on how Gemma 4 changes the landscape for agent developers 
 Timestamp: 1:40 
 Omar highlighted that Gemma 4 brings "very high intelligence per parameter," making it possible to run agentic workflows entirely offline. We saw examples of multiple Gemma instances running locally to generate SVGs ( 1:53 ) and an Android-based agent picking specific skills, like playing the piano, to complete tasks ( 2:45 ). As Omar noted, "This means that you can run very powerful things with very little hardware overhead...even in the phone that you have in your pocket." 
 The Factory Floor 
 Building a Local Food Tour Agent 
 Timestamp: 5:29 
 We showcased a food tour agent powered by Gemma 4 using the Agent Development Kit (ADK) and a Google Maps MCP server. We demonstrated how a local model can handle complex, multi-step reasoning tasks. 
 The agent identified the best ramen spots in Seattle under a $30 budget. 
 It verified that the locations were within walking distance of each other. 
 It processed search results to provide specific tips on what to order and what to avoid. 
 Autonomous Python Code Execution 
 Timestamp: 8:03 
 In this demo, we pushed Gemma 4’s coding capabilities to the limit by asking it to express itself through animation. Using a sandbox execution environment, the model performed the following: 
 Wrote Python code using the Matplotlib library. 
 Attempted to build a physics engine to simulate a bouncing ball. 
 Self-corrected when the initial execution environment lacked certain CPU features, finding an alternative path to successfully generate the animation. 
 Demonstrated a deep understanding of real-world physics and gravity through code. 
 The Shift to Apache 2 Licensing 
 Timestamp: 4:05 
 A major theme of the conversation was the community-driven decision to move Gemma 4 to an Apache 2 license. This change provides developers and startups with maximum flexibility to build, modify, and commercialize applications. Omar emphasized that this was a direct response to developer feedback, aiming to unlock a new wave of innovation in the open models ecosystem. 
 Developer Q&A 
 Architectural Decisions and Mixture of Experts (MoE) 
 Timestamp: 17:23 
 Omar explained the technical shifts that make Gemma 4 so efficient. For the first time, the Gemma family includes a Mixture of Experts (MoE) architecture, which optimizes for extremely low latency in production. Additionally, the smaller E2B and E4B models utilize per-layer embeddings to remain "cheap" to run on GPUs. For vision tasks, the model now supports variable aspect ratios, allowing it to understand images of various sizes more accurately than previous fixed-resolution versions. 
 Comparing Gemma to Gemini 
 Timestamp: 19:51 
 When asked how Gemma stacks up against its larger sibling, Gemini, Omar clarified that they serve different purposes. While Gemini excels at massive-scale tasks and deep "world knowledge" due to its size, Gemma is the "best open model that can run on a single consumer GPU." It is specifically optimized for instruction following, coding, and agentic use cases where local deployment or fine-tuning is required. 
 Fine-Tuning for Specialized Industries 
 Timestamp: 21:10 
 The conversation touched on the importance of "Sovereign AI" and privacy. Because Gemma is an open model, developers in regulated industries, like healthcare or finance, can fine-tune the model on their private data and deploy it within their own air-gapped infrastructure. This gives developers full control over their data and the model's specialized expertise. 
 Conclusion 
 Gemma 4 marks a turning point for agentic development, proving that you don't always need a massive cloud cluster to build something smart. Whether it's running a physics simulation on a laptop or a travel guide on a phone, the barrier to entry for high-performance AI has never been lower. We are entering an era where the "conductor" of the AI orchestra can be any developer with a single GPU and a great idea. 
 Your turn to build 
 Now that you've seen what Gemma 4 can do, it's time to start building. Check out the resources in our show notes, the food tour agent , the coding agent , explore the ADK support , and try running Gemma 4 on your local machine or on Cloud Run . We can't wait to see what agents you create! 
 Watch more of The Agent Factory → Reinforcement learning & fine-tuning on TP... 
 Subscribe to Google Cloud Tech → https://goo.gle/GoogleCloudTech 
 Connect with us 
 Shir Meir Lador → LinkedIn , X 
 Vlad Kolesnikov → Linkedin , X 
 Omar Sanseviero → Linkedin , X
```

---

## 16. Scaling data and AI with Managed Service for Apache Airflow

- 日期: 2026-05-04 18:00
- 链接: https://cloud.google.com/blog/products/data-analytics/managed-apache-airflow-scaling-data-and-ai-workloads/

```
Orchestration is no longer just about moving data; it is about governing enterprise intelligence. To reflect our deep commitment to and embrace of open-source software, we shared earlier that Cloud Composer is now officially Managed Service for Apache Airflow . 
 We announced a massive leap forward in our orchestration capabilities, fundamentally reimagining how data teams operate in the AI era. With four major launches, we are embedding AI directly into your workflows to democratize access, accelerate productivity, and power your most demanding MLOps. 
 1. Apache Airflow 3.1 is now Generally Available 
 We announced Apache Airflow 3.1 in General Availability to power your most demanding AI and MLOps workloads. This release combines the significant foundation of Airflow 3.0 with the recent community innovations of 3.1 . 
 Key capabilities include: 
 Decoupled architecture: A robust separation between the entire Airflow system and the execution layer for better scalability and enhanced security. 
 DAG versioning: Native support for automated DAG versioning, retaining the historical structure and run history. 
 Powerful managed backfills: A redesigned backfill system that is now a first-class citizen, fully managed by the scheduler. 
 Event-driven scheduling and data assets: Enhanced capabilities for triggering workflows based on assets as well as external events, like messages arriving in a message queue. 
 Human-in-the-Loop (HITL) and deadline alerts: Pause execution for human decision-making via the UI, and set proactive time-based thresholds for critical pipelines. 
 And many more… 
 2. Agentic troubleshooting with Data Engineering Agents 
 Managing complex pipelines just got significantly easier. The Data Engineering Agent is now embedded directly in your Managed Airflow dashboard to quickly analyze logs, identify root causes, and suggest fixes. 
 Rapid resolution: By integrating Gemini Cloud Assist Investigations 1 , you can leverage AI to troubleshoot DAG Run failures and receive personalized fix proposals directly in the console. 
 Reduced MTTR: This agentic approach helps minimize Mean Time to Repair (MTTR) by eliminating manual log parsing. Furthermore, troubleshooting is now elevated to the DAG execution level—rather than just the task level—providing a holistic view of pipeline health. 
 3. Orchestration pipelines and deployment automation framework 
 You no longer need to be an Apache Airflow expert to harness its power. Orchestration pipelines are a core component of our new cross-product Deployment Automation Framework, allowing you to create end-to-end data pipelines efficiently. 
 Declarative orchestration: Define your entire pipeline—including the orchestration logic, infrastructure configuration, and dependencies—in simple, human-readable YAML files. 
 Cross-product bundles: These YAML definitions are easily deployed as a complete bundle to the cloud. For example, without knowing Airflow syntax, a user can quickly create and deploy a comprehensive data integration pipeline across dbt, Spark, DTS, and more. 
 Unified IDE experience: Alongside automated validation and deployment via GitHub actions, the Google Data Cloud extension makes agentic authoring and troubleshooting the centerpiece of your workflow. You can now rely on powerful AI agents to build and debug pipelines directly in your IDE, with the ability to visually inspect the agent-generated DAGs for complete oversight. 
 Crucially, this declarative approach breaks down the traditional silos between advanced Python developers and data analysts. By shifting to human-readable YAML, we are fostering a more inclusive data culture where a wider range of practitioners can independently author, understand, and manage critical data workflows. 
 4. MCP Server for Managed Airflow (Public Preview) 
 To further bridge the gap between AI and orchestration, we are launching the Managed Airflow MCP Server in Public Preview. 
 Agentic tooling: This server provides tools like list_environments , get_dag_run , and get_task_instance to fetch critical information about your environments. 
 Seamless integration & reduced context-switching: Both humans and agents can use these tools to simplify task management. Most importantly, this drastically reduces the context-switching developers face when debugging complex DAGs. By bringing environment and task data directly into your preferred interfaces, you can troubleshoot faster without constantly pivoting between different consoles. 
 Embrace the future of data orchestration 
 With these launches, we are fundamentally lowering the barrier to entry for orchestration while simultaneously raising the ceiling for what power users can achieve. By taking away the infrastructure burden and providing native, agentic tooling, data teams can stop wrestling with boilerplate code and start focusing primarily on deriving insights and driving business value. 
 Whether you are a seasoned Data Engineer building dynamic Python DAGs or a Data Analyst defining straightforward YAML pipelines, Managed Service for Apache Airflow is built for you. 
 Get Started Today Ready to experience the next generation of data pipeline orchestration? Create a new environment in the Google Cloud Console , explore the Google Cloud Data Agent Kit extension , and start building your agentic future today. 
 1. Availability might be limited ( details )
```

---

## 17. Firestore at Next '26: Unlock agentic development, search and MongoDB compatibility

- 日期: 2026-05-04 16:00
- 链接: https://cloud.google.com/blog/products/databases/firestore-agentic-ai-search-and-mongodb-compatibility/

```
In the era of AI agents, the distance between a big idea and a working application has never been shorter. As we lean more heavily on agents to help us build applications, a critical question remains: can your database infrastructure keep up? 
 With its virtually limitless scalability and high availability, Firestore , Google Cloud’s fully managed document database, is a great fit for emerging agentic applications. And at Google Cloud Next ‘26, we leveled up Firestore for AI-driven apps even further, with: 
 Tighter agentic AI integrations: New native integrations with AI Studio and third-party coding agents mean your LLMs and database now speak the same language. 
 Full-text search and expressive queries: Differentiated search capabilities and pipeline operations mean agents and users are able to find exactly what they need within your data. 
 Enhanced MongoDB compatibility: Now it’s easier than ever to bring existing MongoDB workloads into the Firestore ecosystem. 
 In this blog, we’ll take a closer look at our announcements from Next ‘26. But first, here’s a Firestore refresher. 
 The case for Firestore 
 Whether you’re an enterprise leader looking to empower your workforce to build their own productivity tools, or a founder sketching out the next big thing on a napkin, you need to be able to prototype at the speed of thought, pivot the moment you get user feedback, and do it all without breaking the bank — or the database. 
 When it comes to selecting a database, you need to worry about: 
 Scaling: Can the database survive a viral traffic spike? 
 Budget efficiency: Does the solution scale to zero during inactivity to reduce your costs? 
 Iteration speed: Will frequent tweaks in your agent prompts be slowed by expensive database schema migrations to fulfill those requests? 
 We designed Firestore to address these exact concerns. Firestore has always been an easy way to achieve rapid, automatic, elastic database scaling, with its serverless architecture that also provides sub-second provisioning. Meanwhile, Firestore’s document model makes it easy and fast to iterate on your data structures — no breaking schema changes, no downtime, just flow. 
 At the same time, accelerating development velocity shouldn’t mean compromising on enterprise governance. Firestore offers an industry-leading 99.999% SLA and ACID-compliant transactions, all while benefiting from the rigorous security and privacy oversight, fundamentally inherent to Google Cloud. 
 Companies like FlutterFlow are already reaping the benefits. 
 “As an AI-native company dedicated to democratizing web and mobile development, Firestore has served as the foundational database powering FlutterFlow as we scaled from zero to over 3 million users across more than 150 countries. Over the past five years, we have experienced zero outages while serving more than 750 billion reads and 75 billion writes. We are true believers in Firestore.” - Abel Mengistu, CEO and Co-founder, FlutterFlow 
 With that background, here’s what’s new in Firestore from Next ‘26. 
 1. Accelerating application development through agentic AI integrations 
 We embedded Firestore directly into the AI creative process. Through new native integrations with AI Studio , developers can now build and provision fully functional full-stack applications with an integrated Firestore database and added authentication from a single natural language prompt. This integration is driving incredible momentum on Firestore, bringing the overall Firestore developer base to 750,000 monthly active developers and over 10M hosted databases. 
 With just one natural language prompt, developers can now leverage Gemini through AI Studio to create and set up full-stack apps equipped with Firestore as the database. 
 We also enhanced the ability to integrate Firestore with preferred third-party AI agents, including Claude Code, Cursor, and Codex. With the general availability of Firestore Skills and Firestore remote MCP service , connecting to popular external agents is even more straightforward. 
 To further enhance productivity, we introduced natural language querying in the Google Cloud console , in preview. This leverages Gemini Code Assist to convert simple natural language queries into complex, MongoDB-compatible queries. 
 Write queries in natural language using Gemini Code Assist. 
 2. Differentiated search and queries 
 Building sophisticated, data-rich AI agents requires a database with modern search and query capabilities. Our reimagined query engine on Enterprise edition , featuring pipeline operations , is now generally available, and delivers hundreds of new query capabilities, positioning Firestore as a premier service for expressive applications. 
 A major addition is built-in full-text search , now available in preview. Firestore full-text search leverages Google search technology, ensuring users who perform a search receive precise results using high-quality relevance models that support more than 40 languages. Moreover, alternative hybrid database and search setups can produce search results that aren’t reflective of actual database data, because their search indexes only use eventual consistency. In contrast, Firestore search indexes are strongly consistent with transactional data, for more accurate search results. Crucially, this native functionality inherits Firestore’s serverless architecture, drastically reducing the operational friction of managing separate search infrastructure. 
 Integrate full-text search capabilities into your applications with the new search() stage, leveraging your existing Firestore document data. 
 We also introduced geospatial queries capabilities in preview, enabling developers to build location-aware applications that can easily find nearby points of interest. 
 code_block <ListValue: [StructValue([('code', "// Find nearby restaurants\r\nfirestore.pipeline().collection('restaurants')\r\n .search({\r\n query: field('location')\r\n .geoDistance(new GeoPoint(38.989177, -107.065076))\r\n .lessThan(1000 /* m */)\r\n });"), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac2cfa130>)])]> 
 This release also includes the highly requested JOIN functionality , in general availability. Implemented via subqueries, pipeline operations enable lookups across diverse collections . Additionally, we launched a preview of built-in data manipulation operators to facilitate the bulk normalization, sanitization, and backfilling of documents within your collections. 
 code_block <ListValue: [StructValue([('code', '// Retrieve all reviews less than 2 stars for a given restaurant\r\nconst pipeline = db.pipeline()\r\n .collection("restaurants")\r\n .define(field("__name__").as("restaurant_id"))\r\n .select("__name__", db.pipeline().collection("reviews")\r\n .where(field("parent_restaurant_id").equals(variable("restaurant_id"))\r\n .where(field("rating").lessThan(2))\r\n .select("review", "rating"))\r\n .toArrayExpression()\r\n .as("negative_reviews"));'), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac2cfa340>)])]> 
 We're also provided deeper observability insights through enhanced usage monitoring, including usage by collection through a new Usage Insights feature in preview. 
 Debug Firestore usage with a breakdown by collection using Usage Insights. 
 Finally, Firestore will soon be integrated with Knowledge Catalog , providing you with deeper insights into how your data models evolve at the collection level. 
 3. Enhanced MongoDB compatibility and scalability 
 We continue to broaden Firestore’s appeal for enterprise workloads with enhanced MongoDB compatibility , making it easier for you to migrate and build on Firestore. 
 To boost MongoDB compatibility, Firestore now supports larger documents up to 16MiB , removing traditional barriers for complex data migrations and high-volume workloads. 
 To enable real-time data movement, we launched highly scalable change streams to synchronize changes from Firestore to services like BigQuery at scale. This feature is built to handle virtually any volume of read and write operations, giving you the piece of mind that change streams will seamlessly scale alongside database production traffic. 
 Easily create a new MongoDB compatible change stream to listen to data changes in a collection or database in real-time. 
 We also improved data lifecycle management, giving developers the ability to efficiently manage data deletion by dropping a collection and using more flexible time-to-live (TTL) time offsets for automatic data expiration — all while ensuring these administrative operations never impact the database's production traffic. 
 code_block <ListValue: [StructValue([('code', 'db.receipts.drop();'), ('language', ''), ('caption', <wagtail.rich_text.RichText object at 0x7faac2cfa1c0>)])]> 
 Get started on Firestore 
 These new capabilities are now available with the Firestore Enterprise edition , available in both Native and MongoDB compatibility modes. Developers can begin incorporating these advanced capabilities into your intelligent, agentic applications today.
```

---

## 18. Chrome Enterprise introduces new integrations for healthcare

- 日期: 2026-05-04 10:48
- 链接: https://cloud.google.com/blog/products/chrome-enterprise/chrome-enterprise-introduces-new-integrations-for-healthcare/

```
The healthcare landscape is undergoing a massive transformation. As electronic health records (EHRs) and critical applications move to the web, the browser has become the new frontline for patient care and data security. Healthcare organizations need a solution that supplies clinicians with fast, familiar access to the tools they need, while providing advanced layers of protection for sensitive patient data. 
 Enter Chrome Enterprise Premium.* Chrome Enterprise provides a secure, simple, and seamless browsing experience that now integrates with key healthcare solutions, allowing clinicians to focus on what matters most: delivering excellent patient care. 
 Elevate clinician workflows, protect patient data 
 Chrome Enterprise Premium extends the familiar Chrome browser with enterprise-grade security and management capabilities, addressing the unique challenges of the healthcare environment. 
 Protect Patient Data: With advanced data loss prevention (DLP) and threat protection, Chrome Enterprise Premium helps safeguard sensitive patient information. Features like real-time URL scanning, advanced phishing and malware protection, and controls to prevent unauthorized copy/paste, printing, or screen captures of sensitive data, help healthcare organizations reduce the risk of data breaches. 
 Empower Clinicians: Provide your clinical teams with a fast and intuitive browser they already know and love. Chrome Enterprise Premium offers a secure and familiar interface, reducing the learning curve and allowing clinicians to access all their apps and patient data from a single, trusted point. 
 Streamline Compliance: Simplify security reviews and compliance audits with comprehensive reporting and forensics. Gain deep visibility into potential security risks, user activity, and data transfers to support your HIPAA compliance efforts and support audit readiness. 
 Secure browsing with new trusted healthcare partnerships 
 To create a truly seamless experience, we are proud to announce our growing integration work with leading healthcare technology providers: 
 Epic : Collaborating to ensure a high-performance experience for Epic’s Hyperspace for Web. By optimizing Chrome’s management and security policies specifically for Epic’s architecture, we enable healthcare providers to run their EHR natively. This is designed to significantly reduce the lag of traditional virtualization, providing the maximum stability and speed required to keep clinical workflows moving without interruption. 
 Imprivata : Enhancing the clinician experience doesn't mean compromising security. Imprivata is collaborating with Google on Chrome Enterprise Premium (CEP) to deliver end-to-end passwordless authentication, which will help reduce the burden of clinician logins. 
 AuthX : Moving to the cloud means leaving behind the complex infrastructure of the past. With AuthX and Chrome, specialized identity management is built for the modern web, enabling clinicians to jump between applications with speed and confidence while reducing the total cost of ownership. 
 Citrix : When clinicians spend less time navigating between systems and more time with patients, that’s a better outcome for everyone. Chrome and Citrix together unify web, SaaS, and virtualized workflows into a single, secure experience, so your teams get the performance they need without adding complexity to your environment. 
 Announcing our secure browser offer for healthcare organizations 
 To help healthcare organizations experience the benefits of a secure browser, we are introducing a specialized offer for eligible organizations.** This offer includes: 
 Extended 6-month trial 
 No-charge seats available for the duration of the trial 
 $5,000 in services funding upon conversion 
 High-touch technical onboarding with experts from Google and Epic 
 An added line of defense for continuity of care 
 For healthcare organizations today, multiple lines of defense remain critical. In addition to secure browsing capabilities to proactively prevent threats and risks, Chrome Enterprise and ChromeOS can be combined to offer critical disaster recovery capabilities in the event of outages or other disruptions. Chrome OS and Chrome Enterprise can provide a pathway to rapidly restore access to critical Epic disaster recovery solutions, especially in situations where your Windows endpoint devices or app deployment solution are unavailable. 
 The future of clinical work is here 
 The transition to modern, web-based healthcare is just beginning. With Chrome Enterprise Premium and our expanding ecosystem of partners, we are committed to providing healthcare organizations with the tools they need to protect patient data, empower their clinicians, and streamline their path to the web. 
 To learn more about how Chrome Enterprise Premium can transform your organization, visit our website or contact a sales rep today . 
 *Chrome Enterprise Premium features and partner integrations are subject to change. Some features may require an internet connection or additional subscriptions. 
 **Promotion is available to eligible organizations with a minimum of 1,000 users. Terms and conditions apply
```

---

## 19. What’s new with Google Cloud

- 日期: 2026-05-01 16:00
- 链接: https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/

```
Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. 
 Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . 
 aside_block <ListValue: []> 
 Apr 27 - May 1 
 Master Your Launch: The Apigee Production Go-Live Checklist 
 Ensure a secure launch with the Apigee production guide. Join Nicola Cardace on May 28 to explore security guardrails, including IAM roles, mTLS configurations, and encrypted KVM migrations. Scheduled at 11 AM EDT / 5 PM CEST to support EMEA and AMER teams, this TechTalk provides the technical roadmap you need to flip the switch with absolute confidence. 
 Register for the May 28 Community TechTalk 
 Transforming APIs into Governed Agentic Tools on the Google Cloud Agentic Platform 
 Turn your APIs into secure, governed agentic tools on the Google Cloud Agentic Platform. Join Specialist Christophe Lalevée on May 7 for a technical deep dive into AI productization. Scheduled at 5 PM CEST / 11 AM EDT to maximize coverage for developers across EMEA and AMER, this session explores the integration and governance frameworks required to scale enterprise-ready AI with confidence. 
 Register for the May 7 Community TechTalk 
 Fractional G4 VMs are Generaly Available, providing a highly efficient and cost-effective entry point for AI and graphics workloads. These new configurations, using NVIDIA virtual GPU (vGPU) technology, allow you to leverage the power of the NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs in flexible, smaller increments, so you can right-size your infrastructure to match the specific demands of your applications. By providing more granular access to advanced hardware, fractional G4 VMs let you optimize resource allocation and reduce overhead without sacrificing performance. You can now select from additional GPU slice sizes for your specific needs: 1/2 GPU: Ideal for more intensive tasks such as LLM inference, robotics sensor simulation, and high-fidelity 3D rendering. 
 1/4 GPU: Optimized for mainstream workloads, including mid-range creative design, video transcoding, and real-time data visualization. 
 1/8 GPU: Great for lightweight applications such as remote desktops, productivity tools, and entry-level streaming services. 
 Transitioning AI from a sandbox prototype to an enterprise-grade system is a major hurdle. A monolithic script won't suffice for widespread deployment. To achieve true scale and reliability with Gemini, organizations must adopt service-oriented micro-agent architectures, establish Zero-Trust security, and implement rigorous EvalOps. Master the "Agentic Maturity Ladder" to ensure your AI & Agentic solutions are robust, secure, and ready for the real world. 
 Watch the deep dive and read the developer blog to learn more. 
 ML Development in VS Code with Google Cloud Power: Workbench Extension Now Available 
 Data scientists and developers can now combine the local productivity of VS Code with the scalable infrastructure of Google Cloud. The new Google Cloud Workbench Notebooks extension allows you to connect to and run notebooks on managed cloud environments directly within your local IDE. This integration streamlines the ML lifecycle by eliminating context switching and providing high-performance compute for complex workloads in a familiar interface. As part of our commitment to the developer ecosystem, the extension is fully open-sourced to support community-driven innovation. 
 Install from Marketplace: GoogleCloudTools.workbench-notebooks 
 Contribute on GitHub: colab-enterprise-vscode 
 Apr 20 - Apr 24 
 Announcing the 2026 Google Cloud Partners of the Year 
 Google Cloud is honored to celebrate the winners of the 2026 Partner of the Year awards! These awards recognize an exceptional group of partners across AI, Security, Infrastructure, and more, who have demonstrated a commitment to customer success. From global system integrators to specialized startups, these winners are leveraging the power of Google Cloud to solve complex challenges and drive digital transformation worldwide. Join us in congratulating these organizations for their innovation, collaboration, and impactful results over the past year. 
 See the 2026 Partner Award winners 
 Apr 13 - Apr 17 
 We're excited to announce the Public Preview of Datastream’s metadata integration with Knowledge Catalog . This is the first step in our vision to provide a centralized, "single pane of glass" for all Datastream assets. The enhancement automatically synchronizes Streams, Connection Profiles, and Private Connections, eliminating data silos. It enhances discoverability, allowing you to search for Datastream assets using the same interface as BigQuery tables. Centralized governance is also provided, making your real-time data estate more transparent and easier to manage. 
 Upgrading Apigee OPDK to 4.53 with OS Modernization 
 Modernize your infrastructure using Google’s official, sequential upgrade path. Our Technical expert, Rakesh Talanki outlines how to upgrade Apigee OPDK to v4.53 while migrating to a supported OS (RHEL 8.x/9.x). This guide covers the "build-out" methodology, including multi-data center syncing, to ensure a stable, zero-downtime transition 
 Read the guide 
 Cloud Run Worker Pools and CREMA: Powering Serverless AI at Scale 
 Google Cloud has announced the General Availability of Cloud Run worker pools , a new resource type designed specifically for pull-based, non-HTTP workloads. Unlike traditional Cloud Run services that scale based on request traffic, worker pools provide an "always-on" environment for background tasks like processing message queues or running large-scale AI inference. To support this, Google Cloud also open-sourced the Cloud Run External Metrics Autoscaler (CREMA) . Built on KEDA, CREMA enables queue-aware autoscaling for worker pools, allowing them to dynamically scale based on external signals like Pub/Sub backlog or Kafka lag. 
 Apigee Model Context Protocol (MCP) now Generally Available 
 Expose enterprise APIs as MCP tools for agentic AI applications with the General Availability of MCP in Apigee. This update allows developers to transform APIs into AI-ready tools using OpenAPI Specifications, removing the need for local MCP servers or additional infrastructure. With managed endpoints and semantic search in API hub, you can now provide AI agents with secure, governed access to enterprise data at scale. 
 Explore the MCP overview 
 Apr 6 - Apr 10 
 Community TechTalk: Powering Retail Agents with ADK, UCP & Apigee X 
 Move beyond basic chatbots to secure, transactional AI experiences. Join our Community TechTalk on April 16 to learn how Apigee X and Gemini build a "Trust Layer" for AI shopping assistants using UCP standards. We’ll demonstrate how to block prompt injections with Model Armor and implement cost governance via token limits to secure the path from discovery to purchase. 
 Register for the TechTalk 
 Implement multimodal capabilities in your AI agents 
 Explore three new reference architectures for building sophisticated multi-agent AI systems that can process and analyze multimodal data. To analyze disparate multimodal data and produce a high-confidence classification, see Classify multimodal data . To create a fluid conversational AI that processes audio and video streams in real time, see Enable live bidirectional multimodal streaming . To consolidate fragmented multimodal data into a searchable knowledge graph, see Multimodal GraphRAG resource orchestration . 
 Automate SecOps workflows with an agentic AI system 
 To accelerate incident response and reduce manual toil for your security team, you need a system that can automate remediation playbooks. Our new reference architecture helps you build an AI agent that orchestrates complex triage and investigation workflows across disparate security tools, such as SIEM, CSPM, and EDR, from a single interface. See the full guide to orchestrate security operations workflows . 
 Mar 30 - Apr 3 
 ASEAN Webinar | April 30: Mastering Agentic Governance at Scale with GCP 
 As AI agents move from experimental pilots to core enterprise functions, governance is the critical next step. Join Google Cloud experts Shilpi Puri & Wely Lau for a webinar on April 30th at 11:00 AM SGT to learn how to architect a secure AI Management layer. We’ll explore developing governed MCP endpoints, managing tool access to enterprise data, and operationalizing AI with robust audit logs. The session includes a live demo of these frameworks in action on Google Cloud. 
 RSVP here. 
 Mar 23 - Mar 27 
 Turn your API sprawl into an agent-ready catalog 
 As organizations scale, APIs often become scattered across multiple gateways, creating "blind spots" that hinder AI adoption. To solve this, we’ve introduced two new capabilities for Apigee API hub: a new integration with API Gateway to automatically centralize API metadata into a single control plane, and a specification boost add-on (now in public preview). This add-on uses AI to enhance your API documentation with the precise examples and error codes that AI agents need to function reliably. 
 Read the full blog post to get started. 
 Webinar | April 16: AI Command & Control 
 As AI agents move from experimental pilots to core enterprise functions, governance is the critical next step. Join Google Cloud expert Satyam Maloo for a webinar on April 16th at 11:00 AM IST to learn how to architect a secure AI Management layer. We’ll explore developing governed MCP endpoints, managing tool access to enterprise data, and operationalizing AI with robust audit logs. The session includes a live demo of these frameworks in action on Google Cloud. 
 RSVP here. 
 Modernizing and Decoupling Event Ingestion with Apigee 
 In modern cloud-native architectures, decoupling producers from consumers is critical for building resilient systems. While Google Cloud Pub/Sub provides a scalable backbone, exposing it directly to external clients can introduce security and management overhead. This new guide explores how to leverage Apigee as an intelligent HTTP ingestion point. Learn how to handle security, mediation, and traffic control before messages reach your internal bus using the PublishMessage policy or Pub/Sub API. 
 Read the full guide. 
 Mar 16 - Mar 20 
 Gemini-powered Assistant in BigQuery Studio Gets Context-Aware Upgrades 
 The Gemini-powered assistant in BigQuery Studio has been transformed into a fully context-aware analytics partner, supporting your entire data lifecycle. The new capabilities include intelligent resource discovery, which uses Dataplex Universal Catalog search to find resources across projects and deep dive into metadata using natural language. You can now automate tasks, such as scheduling production-grade queries directly through the chat interface, and instantly troubleshoot long-running or failed jobs with root cause analysis and cost control auditing. 
 Explore the full range of what the assistant can do. 
 Mar 9 - Mar 13 
 Want to use Gemini to develop code and don't know where to start? 
 This article includes a couple of examples of developing code with Gemini prompts; it identified changes that were needed to be made to get the code working. The article also refers to other examples that are available on github. 
 Mar 2 - Mar 6 
 Introducing Gemini 3.1 Flash-Lite, our fastest and most cost-efficient Gemini 3 series model. Built for high-volume developer workloads at scale, 3.1 Flash-Lite delivers high quality for its price and model tier. Gemini 3.1 Flash-Lite can tackle tasks at scale, like high-volume translation and content moderation, where cost is a priority. And it can also handle more complex workloads where more in-depth reasoning is needed, like generating user interfaces and dashboards, creating simulations or following instructions. 
 Starting today, 3.1 Flash-Lite is rolling out in preview to enterprises via Vertex AI and developers via the Gemini API in Google AI Studio . 
 TechTalk: Implementing Device Authorization Grant (RFC 8628) for Apigee 
 Learn how to authorize "headless" devices like Smart TVs or AI agents that lack keyboards and browsers. Join our Community TechTalk on March 19 (5PM CET / 12PM EDT) to go under the hood of Apigee X/Hybrid. We’ll cover the real-world mechanics of state management, polling, and human-in-the-loop security patterns for devices and autonomous agents. 
 Register for the TechTalk 
 Feb 23 - Feb 27 
 Pro-level image generation gets faster and more accessible with Nano Banana 2 
 Nano Banana 2 is our state-of-the-art image generation and editing model. It delivers Pro-level image generation and editing at the speed you expect from Flash — making the quality, reasoning, and world knowledge you loved about Nano Banana Pro more accessible. Learn more about the model here . 
 The Intelligent Path to Compliance: Transforming Regulatory QC with Google Cloud 
 Reducing "Refuse to File" (RTF) risks and submission cycle times is critical for life sciences leaders. Google Cloud’s Regulatory Submission Semantic QC Auditor leverages Gemini and RAG architecture to transform Quality Control from a manual burden into an active, intelligent workflow. 
 By automating semantic cross-referencing, narrative coherence checks, and dynamic guidance-based auditing, this solution ensures rigorous accuracy and auditability. Operating within a secure GxP-ready environment, it empowers teams to detect subtle inconsistencies and generate remediation plans without sacrificing data privacy. 
 Learn more . 
 Stop typing, start interacting! The Gemini Live Agent Challenge is here . Build immersive agents that can help you see, hear, and speak using Gemini and Google Cloud. Compete for your share of $80,000+ in prizes and a trip to Google Cloud Next '26! 
 Submissions are open from February 16, 2026 to March 16, 2026. Learn more and register at geminiliveagentchallenge.devpost.com 
 Feb 9 - Feb 13 
 Introducing Gemini 3.1 Pro on Google Cloud. 
 3.1 Pro is a noticeably smarter, more capable baseline for complex problem-solving. We’re shipping 3.1 Pro at scale, building upon our goal to help you transform your business for the agentic future. Learn more about the model’s capabilities here . Gemini 3.1 Pro is available starting today in preview in Vertex AI and Gemini Enterprise . Developers can access the model in preview via the Gemini API in Google AI Studio , Android Studio , Google Antigravity , and Gemini CLI . 
 Automate Storage Compatibility with GKE Dynamic Default Storage Classes 
 Managing storage across mixed-generation VM clusters in GKE just got easier. With the new Dynamic Default Storage Class , Google Kubernetes Engine automatically selects between Persistent Disk (PD) and Hyperdisk based on a node's specific hardware compatibility. This abstraction eliminates the need for complex scheduling rules and manual pairing, ensuring your volumes "just work" regardless of the underlying infrastructure. By defining both variants in a single class, you reduce operational overhead while maintaining peak performance and cost-efficiency across your entire cluster. 
 Explore automated disk type selection 
 Community TechTalk: AI-Powered Apigee Development with strofa.io 
 Join the Apigee community on February 26 for a deep dive into strofa.io . Guest speaker Denis Kalitviansky will demonstrate how this new AI-powered tool automates and orchestrates Apigee development, from local emulators to large-scale hybrid environments. Discover how to scale your API management and streamline team collaboration using the latest in AI-driven automation. 
 Register now to reserve your spot. 
 Jan 26 - Jan 30 
 Simplify API Governance with Native OpenAPI v3 Support 
 Eliminate integration debt and accelerate deployment velocity with the General Availability of OpenAPI v3 (OASv3) support for API Gateway and Cloud Endpoints. You no longer need to downgrade modern specifications to OASv2. Instead, you can now define API contracts and enforce critical policies—including telemetry, quotas, and security—using native Google-specific extensions directly within your OASv3 files. This update ensures your APIs are secure by design while remaining fully compatible with the modern developer ecosystem and Google Cloud’s AI services. 
 Get started with OpenAPI v3 on API Gateway and Cloud Endpoints. 
 Accelerate API Testing with the New Open Source API Tester 
 Start validating your APIs with API Tester, a simple, YAML-based Test Driven Development (TDD) framework. Designed for the Apigee community, this tool allows you to write human-readable tests, run them instantly via a web client or CLI, and perform deep unit testing on Apigee proxies. With native support for JSONPath assertions and Apigee shared flows, you can verify everything from payload data to internal variables like proxy.basepath without leaving your terminal. 
 Explore the API Tester guide and start testing your proxies today. 
 Secure Sensitive Data with Kubernetes Secrets in Apigee hybrid 
 Enhance security in Apigee hybrid by accessing Kubernetes Secrets directly within your API proxies. This hybrid-exclusive feature keeps sensitive credentials within your cluster boundary and prevents replication to the management plane. It supports strict separation of duties: operators manage secrets via kubectl , while developers reference them as secure flow variables—ideal for high-compliance and GitOps workflows. 
 Implement Kubernetes Secrets in your hybrid proxies. 
 See the Console in a Whole New Light: Dark Mode is Now Generally Available in Google Cloud 
 Elevate your cloud management workflow with Dark Mode, now generally available in the Google Cloud console. We have delivered a modern, cohesive, and accessible experience reimagined for maximum comfort and productivity—especially during extended working hours and low-light environments. Dark Mode can be enabled automatically based on your operating system's preference, or manually through the Settings  -> Appearance menu. 
 Switch to Dark Mode today to enjoy a modern, comfortable, and productive environment! 
 Apigee X Networking: PSC or VPC Peering? 
 Deciding how to connect Apigee X? Watch this video to compare Private Service Connect and VPC Peering. We break down northbound and southbound routing, IP consumption, and how to reach targets on-prem or in the cloud. Learn to simplify your architecture and avoid common networking "gotchas" for a smoother deployment. 
 Watch the video. 
 Jan 19 - Jan 23 
 Bridge the Gap: Excel-to-API Conversion in Apigee Portals 
 Give your customers more ways to connect! This new article by Tyler Ayers explores how to extend the Apigee Integrated Portal to support direct Excel file uploads. By leveraging SheetJS and custom portal scripts, you can enable users to upload spreadsheets, preview data, and submit it directly to your APIs, all without writing a single line of integration code themselves. It’s a powerful way to simplify onboarding for those who aren't yet API-ready. 
 Learn how to build it . 
 Elevate your applications with Firestore’s new advanced query engine 
 We have fundamentally reimagined Firestore with pipeline operations for Enterprise edition. Experience a powerful new engine featuring over a hundred new query features, index-less queries, new index types, and observability tooling to improve query performance. Seamlessly migrate using built-in tools and leverage Firestore’s existing differentiated serverless foundation, virtually unlimited scale, and industry-leading SLA. Join a community of 600K developers to craft expressive applications that maximize the benefits of rich queryability, real-time listen queries, robust offline caching, and cutting-edge AI-assistive coding integrations. 
 Learn more about Firestore pipeline operations.
```

---

## 20. What Google Cloud announced in AI this month

- 日期: 2026-04-30 16:00
- 链接: https://cloud.google.com/blog/products/ai-machine-learning/what-google-cloud-announced-in-ai-this-month/

```
Editor’s note : Want to keep up with the latest from Google Cloud? Check back here for a monthly recap of our latest updates, announcements, resources, events, learning opportunities, and more. 
 We hosted Google Cloud Next in Las Vegas on April 22, announcing incredible innovations from Gemini Enterprise Agent Platform to our eight-generation TPUs. We also expanded the Gemini Enterprise app in collaborative ways – now, with new features like Projects, you can work side-by-side with your agents and colleagues. 
 If you missed the livestream, take a look at our Day 1 recap . It’s been incredible to see how customers have been applying AI in thousands of ways — so far, we’ve counted more than 1,300 examples . 
 Top announcements 
 1. Gemini Enterprise Agent Platform: Our new, comprehensive platform to build, scale, govern, and optimize agents. Moving forward, all Vertex AI services and roadmap evolutions will be delivered exclusively through the Agent Platform, rather than as a standalone service, to power the next generation of agent development. 
 The platform is designed around four core pillars — build, scale, govern, and optimize — that allow teams to collaborate seamlessly. Learn more about Agent Platform here . 
 2. Gemini Enterprise app has all the key components to let teams discover, create, share, and run AI agents in a single environment. At Next ‘26, we introduced several new capabilities in the Gemini Enterprise app: 
 Agent Designer uses the same no-code agent designer experience of Agent Platform and lets employees build sophisticated schedule- and trigger-based agents using any enterprise connector. It gives you a virtual flowchart of your agent, allowing you to inspect, test, and approve workflows, ensuring total transparency for executing critical business processes. 
 Long-running agents are designed to execute complex business processes. They can work autonomously in secure cloud sandboxes, giving agents the ability to orchestrate business logic, write code to build custom tools, and complete multi-step work like reconciliation activities or sales prospect sequencing — without needing constant prompting. 
 Inbox in Gemini Enterprise provides a central location to monitor, guide, and help manage all of your agent activity, including your long-running agents. Notifications are intuitively categorized into actionable groups like "Needs your input," "Errors," and "Completed.” 
 Projects create a dedicated space where the agent’s memory is confined to the files and conversations your team adds. By connecting it to data sources including Google Drive, NotebookLM, and Google Group Chats, the agent becomes an expert on a specific topic and can provide team members daily briefings or status updates without digging through months of documents. 
 Skills create simple shortcuts using an “@” mention for repetitive tasks such as applying brand guidelines, formatting a report, and accessing specific data. 
 Canvas gives our customers an interactive editor directly within Gemini Enterprise. It allows teams to easily create and edit Docs and Slides, and even export to Microsoft 365 files, within the same experience. 
 Agent Gallery provides access to third-party agents from partners like Adobe, Atlassian, Lovable, and ServiceNow, and is adding more third-party connectors for Asana, Mailchimp, Workday, and more. These integrations enable your agents to retrieve data and execute tasks with your systems-of-record. 
 3. AI Hypercomputer: Designed specifically for demanding AI workloads, our AI Hypercomputer is an advanced, purpose-built architecture that unites performance-optimized hardware for compute, storage, networking, open software and machine learning frameworks — as well as flexible consumption models — into a single, integrated system. We are announcing innovations at every layer of the AI Hypercomputer: 
 TPU 8t, optimized for training, uses breakthrough Inter-Chip Interconnect (ICI) technology to scale up to 9,600 TPUs and 2 PB of shared, high-bandwidth memory in a single superpod. It achieves 3x the processing power of Ironwood and delivers up to 2x more performance/Watt. 
 TPU 8i, optimized for inference, uses our new Boardfly topology to directly connect 1,152 TPUs in a single pod. It features 3x more on-chip SRAM compared to previous versions to host larger KV caches entirely on-silicon and integrates a specialized Collectives Acceleration Engine. Taken together, TPU 8i delivers 80% better performance per dollar for inference than the prior generation, enabling millions of concurrent agents to run cost-effectively . 
 4. The Agentic Data Cloud: A new data architecture built for the speed and scale of agentic AI. The Agentic Data Cloud delivers an AI-native architecture, allowing agents to perceive, reason, and act on your behalf in real-time, including: 
 Cross-Cloud Lakehouse, standardized on Apache Iceberg, is our Lakehouse that enables you to leave your data in AWS or Azure (coming later this year) while querying it instantly — without the friction of vendor lock-in or the cost of data movement 
 Knowledge Catalog constructs a unified, dynamic context graph of your entire business enabling you to ground agents in all of your business data and semantics. With Smart Storage and the Object Context API, files in Google Cloud Storage are instantly tagged and enriched with metadata before an agent touches them. Then our Knowledge Engine uses Gemini to autonomously tag, define logic and instantly map complex relationships across your entire enterprise, providing the semantic definition your agents have been missing. 
 5. Protecting the agentic enterprise: Security built for the AI era. Our full-stack AI approach, from the chips to the models, gives you a competitive advantage with better integration and velocity to help protect customers. Not only can Google action insights from the world’s largest threat observatory and Mandiant frontline experts, but we also bring cutting-edge insights and breakthroughs from Google DeepMind, to help make your platforms more secure. 
 Agentic defense : Three new agents in Google Security Operations can help hunt threats , engineer detections , and provide context on third parties . You can build your own security agents with remote Google Cloud model context protocol (MCP) server support for Google Security Operations, now generally available. You can also access the MCP server client directly from the Google Security Operations chat interface , available in preview. 
 Protecting AI and cloud apps across any infrastructure with Wiz : Newly expanded AI coverage helps build secure agents across clouds and AI studios. New AI-Bill of Materials in development tools can help secure AI-generated code and mitigate the risk of shadow AI . Learn more . 
 Securing agents and the agentic web : Model Armor can integrate with Agent Gateway, and new Agent Identities provide more layers of defense against shadow AI. Google Cloud Fraud Defense , the next evolution of reCAPTCHA, offers agent-specific capabilities that can help secure the agentic web as well as the entire user and customer journey. 
 Trusted Cloud : We’re simplifying permissions with modern IAM, and advancing Google Cloud security with new capabilities in Security Command Center plus new innovations in data and network security. 
 New partner-supported workflows for Google Security Operations : This new robust cohort of partner integrations includes partners developing their own agentic security operations centers (SOCs). 
 You can catch up on all our security announcements from Next ‘26 here . 
 News you can use 
 Guide to prompting Gemini 3.1 Flash TTS (text-to-speech) : The new TTS model introduces a high level of controllability by allowing you to steer the delivery using more than 200 audio tags. We'll share how to get strong results from the model, whether you are building accessible gaming soundtracks, banking systems, or audiobooks. Learn more about the model here . 
 Ultimate prompting guide for Lyria 3 models : Lyria 3 , Google's family of music-generation models, is designed to give you granular control over vocals, instrumentation, and arrangement. So we spent weeks testing against every musical genre and use case we could imagine. We put together this guide to share exactly what we learned and how you can get the best results. 
 How to find the sweet spot between cost and performance : This guide will walk you through Google Cloud's flexible gen AI infrastructure options, showing you how to find that sweet spot on the efficient frontier between cost and performance. We'll start with the foundational pay-as-you-go (PayGo) models and then explore how to layer on more specialized options to build a robust and cost-effective gen AI strategy. 
 Essential AI and cloud security now on by default : To support the next generation of AI innovators, we are offering on by default essential AI security and cloud security in Security Command Center Standard. 
 Securing AI inference on GKE with Model Armor : Here’s how to secure AI inference on Google Kubernetes Engine with Model Armor and high-performance storage. 
 Cloud CISO Perspectives: AI, security, and the workforce of the future : You can’t bring traditional security to an AI fight, so how do we defend against AI-powered attacks, boost defenders with AI, and secure AI use? Drop in on this RSA Conference fireside chat between Francis deSouza, Google Cloud COO and President, Security Products, and Nick Godfrey, senior director, Office of the CISO. 
 Stay tuned for monthly updates on Google Cloud’s AI announcements, news, and best practices. For a deeper dive into the latest from Google Cloud customers, read our monthly recap, Cool stuff customers built. 
 aside_block <ListValue: [StructValue([('title', '$300 in free credit to try Google Cloud AI and ML'), ('body', <wagtail.rich_text.RichText object at 0x7faac251a2e0>), ('btn_text', 'Start building for free'), ('href', 'http://console.cloud.google.com/freetrial?redirectPath=/vertex-ai/'), ('image', None)])]> 
 March 
 March was a busy month for our AI teams. We launched Gemini Embedding 2, rolled out a highly cost-effective Veo 3.1 Lite model, and officially welcomed the Wiz team to Google Cloud to help redefine security in the AI era. 
 Alongside these launches, we created comprehensive guides to help you get the most out of these models, from prompting formulas for Nano Banana 2, to practical advice for optimizing your TPU training. Here’s a quick look at the latest news and resources to help your team build what’s next. 
 Top hits: 
 Gemini Embedding 2: Our first natively multimodal embedding model: Gemini Embedding 2 is our first natively multimodal embedding model that maps text, images, video, audio and documents into a single embedding space, enabling multimodal retrieval and classification across different types of media — and it’s available now in public preview. 
 Build with Veo 3.1 Lite, our most cost-effective video generation model : This model empowers developers to build high-volume video applications, at less than 50% of the cost of Veo 3.1 Fast, but with the same speed. This rounds out the Veo 3.1 model family, giving developers flexibility based on needs. For Cloud customers, it’s now available on Vertex AI . 
 Here’s a fun bonus: Check out our ultimate prompting guide for Veo 3.1 to get started. 
 Veo 3.1 Lite 
 Welcoming Wiz to Google Cloud: Redefining security for the AI era: Google has completed its acquisition of Wiz, a leading cloud and AI security platform. The Wiz team will join Google Cloud, and we will retain the Wiz brand. With the addition of Wiz, we will provide customers with a comprehensive platform to secure their cloud and hybrid environments, as well as accelerate threat prevention, detection, and response. 
 Gemini 3.1 Flash Live: Making audio AI more natural and reliable: We’ve improved 3.1 Flash Live’s overall quality, making it more reliable for developers and enterprises to build voice-first agents that can complete complex tasks at scale. On ComplexFuncBench Audio, a benchmark that captures multi-step function calling with various constraints, it leads with a score of 90.8% compared to our previous model. 
 News you can use: 
 The ultimate Nano Banana prompting guide: This is a must-read for anyone working with Nano Banana. We spent weeks testing Nano Banana 2 and Nano Banana Pro against every use case we could imagine to test its limits. We put together this guide to share exactly what we learned and how you can get the best results. Here’s an example formula: [Reference images] + [Relationship instruction] + [New scenario] 
 A developer’s guide to training with Ironwood TPUs : In this guide, we hear from Lillian Yu, CPA, CA , Product Strategy and Operation, and Liat Berry, Product Manager, on five strategies within the JAX and MaxText ecosystems designed to help developers refine training efficiency and hit peak performance on Ironwood hardware. 
 How to build production-ready AI agents with Google-managed MCP servers : In this guide, we anchor on a specific example. Cityscape is a demo agent built with Google's Application Development Kit (ADK) that turns a simple text prompt — like "Generate a cityscape for Kyoto" — into a unique, AI-generated city image. Check out the guide to learn more. 
 Stay tuned for monthly updates on Google Cloud’s AI announcements, news, and best practices. For a deeper dive into the latest from Google Cloud customers, read our monthly recap, Cool stuff customers built. 
 February 
 In February, we’re giving developers more reasoning power with Gemini 3.1 Pro and Claude 4.6, and faster creative scaling with Nano Banana 2. We’re also opening up new training programs and step-by-step guides to help you tackle the hardest parts of the AI lifecycle, from capacity planning to mounting defenses against AI-powered attacks. 
 Here’s a rundown of our latest news, tools, and resources to help you build what’s next. 
 Top hits 
 Pro-level image generation gets faster and more accessible with Nano Banana 2 : To build creative that stands out, you need models that naturally integrate into your workflows and scale with ease. Check out our blog to see how this comes to life (and how customers are putting the model to work). 
 Introducing Gemini 3.1 Pro on Google Cloud: Gemini 3.1 Pro is a clear step forward in reasoning, designed to solve tougher problems, giving you the reasoning depth your business needs. Gemini 3.1 Pro is available starting today in preview in Vertex AI and Gemini Enterprise . Developers can access the model in preview via the Gemini API in Google AI Studio , Android Studio , Google Antigravity , and Gemini CLI . 
 Announcing Claude Opus 4.6 and Claude Sonnet 4.6 on Vertex AI: Now generally available on Vertex AI, explore our sample notebook to get started and visit our documentation for comprehensive pricing and regional availability details. 
 New AI threats report: Distillation, experimentation, and integration : John Hultquist, chief analyst, Google Threat Intelligence Group, details what security leaders should know from our newest AI threat report on experimentation, integration, and distillation attacks. 
 News you can use 
 A developer's guide to production-ready AI agents : To help developers work through these challenges, we've published a collection of guides covering the full agent lifecycle. These resources first appeared during Kaggle’s 5 days of AI Agents Intensive , and they’ve proven so popular and useful, we wanted to make sure a wider audience had access, as well. 
 Gemini Enterprise Agent Ready (GEAR) program now available: We opened the Gemini Enterprise Agent Ready (GEAR) learning program to everyone. As a new specialized pathway within the Google Developer Program, GEAR empowers developers and pros to build and deploy enterprise-grade agents with Google AI. 
 Your guide to Provisioned Throughput (PT) on Vertex AI: Check out this deep-dive blog designed to show you the resources available to you today on Vertex AI, and how you can get started capacity planning. 
 How AI can boost defenders, from defense in depth to the cyber kill chain (Q&A) : We know that defenders are also developing powerful AI tools, but what’s still unknown is what it could mean for enterprise software ownership if companies have to constantly mount AI-directed defenses at AI-powered attacks? 
 Stay tuned for monthly updates on Google Cloud’s AI announcements, news, and best practices. For a deeper dive into the latest from Google Cloud customers, read our monthly recap, Cool stuff customers built. 
 Janurary 
 We used to have to learn the language of computers. In 2026, they’re learning ours. 
 We kicked off the year by exploring the future of agentic commerce, where AI agents navigate the web to find and buy products for us. Our leaders call this the " invisible shelf " — a world where commerce isn't tied to a specific website. To make this reality scalable, we announced the Universal Commerce Protocol (UCP), a shared language that allows agents and retailers to understand each other. 
 We brought that same fluency to our creative and technical tools: 
 Updates to Veo 3.1 allow creators to use simple inputs — like reference images — to generate precise, mobile-ready video. 
 Natural language queries: With Comments to SQL in BigQuery, we’re removing the language barrier to data. Engineers can now write queries by describing their intent in natural language, prioritizing the question over the code. 
 Let’s dive in. 
 Top hits 
 1. Gemini Enterprise for Customer Experience (CX): Specifically built for agentic retail, this platform transforms fragmented search, commerce and service touch points into one seamless journey — whether you need a shopping assistant, a support bot, agentic search or help with merchandising. 
 2. We announced Universal Commerce Protocol (UCP): A new open standard for agentic commerce that works across the entire shopping journey — from discovery and buying to post-purchase support. UCP establishes a common language for agents and systems to operate together across consumer surfaces, businesses and payment providers. So instead of requiring unique connections for every individual agent, UCP enables all agents to interact easily. UCP is built to work across verticals and is compatible with existing industry protocols like Agent2Agent (A2A), Agent Payments Protocol (AP2) and Model Context Protocol (MCP). 
 3. We updated Veo 3.1, including improvements to Ingredients to Video and Portrait mode: Veo is getting more expressive, with improvements that help you create more fun, creative, high-quality videos based on ingredient images, built directly for the mobile format. This includes: 
 Improvements to Veo 3.1 Ingredients to Video, our capability that lets you create videos based on reference images. 
 Native vertical outputs for Ingredients to Video (portrait mode) to power mobile-first, short-form video creation. 
 State-of-the-art upscaling to 1080p and 4K resolution 1 for high-fidelity production workflows. 
 These updates are launching in the Gemini app, YouTube, Flow, Google Vids, the Gemini API and Vertex AI. 
 4. Vibe querying with comments-to-SQL: Crafting complex SQL queries can be challenging. Often, engineers simply want to express their data needs in plain English directly within their SQL workflow. That’s why we’re introducing Comments to SQL in BigQuery. This feature makes writing queries using natural language – ‘vibe querying’ – a reality. Learn more in the blog . 
 News you can use 
 Mastering Gemini CLI: Your complete guide from installation to advanced use-cases : We’ve teamed up with DeepLearning.ai and are excited to announce a free course – Gemini CLI: Code & Create with an Open-Source Agent. This course isn’t just for developers; we dive into practical use cases for various tasks such as data analysis, content creation, and personalized learning. 
 How Google SREs use Gemini CLI to solve real-world outages : In this article, we’ll delve into real scenarios that Google SREs are solving today using Gemini 3 (our latest foundation model) and Gemini CLI—the go-to tool for bringing agentic capabilities to the terminal. 
 Getting started with Gemini 3: Deploy your first Gemini 3 app to Google Cloud Run : In this blog, we will show you how to vibe code your first app—which leverages the Gemini 3 Flash Preview model and deploy it as a publicly accessible URL on Google Cloud Run. Google AI Studio lets you go from idea to app quickly by using natural language to generate fully functional apps using the power of Gemini 3. 
 Practical guidance: Building with the Secure AI Framework (SAIF) on Google Cloud : We know that security and data privacy are the top concern for executives when evaluating AI providers, and security is the top use case for AI agents in a majority of industries. To help you build AI boldly and responsibly, here’s our guide to developing AI with the Secure AI Framework (SAIF) on Google Cloud. 
 The truths about AI hacking that every CISO needs to know (Q&A) : How will AI boost threat actors? And what can chief information security officers do about it? Google’s Heather Adkins, vice-president, Security Engineering, explores how securing the enterprise is about to change. 
 Stay tuned for monthly updates on Google Cloud’s AI announcements, news, and best practices. For a deeper dive into the latest from Google Cloud customers, read our monthly recap, Cool stuff customers built. 
 Related Article 
 What Google Cloud announced in AI this month - 2025 
 Learn about the latest announcements, innovations, and guides when it comes to Google Cloud AI. 
 Read Article
```

---
