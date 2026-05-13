# Spotify Engineering

> 分类: 大厂技术博客
> URL: https://engineering.atspotify.com/feed/
> 抓取: 5 篇

---

## 1. Building a Natural Language Interface to the Spotify Ads API with Claude Code Plugins

- 日期: 2026-05-01 16:00
- 链接: https://engineering.atspotify.com/2026/5/spotify-ads-api-claude-plugins/

```
Building a Natural Language Interface to the Spotify Ads API with Claude Code Plugins
We built a suite of skills, agents and tools bundled as a plugin to make the Spotify Ads Platform easily accessible to AI agentic tools. The spotify-ads-api plugin is available on GitHub and through Anthropic's Claude Plugins marketplace. Download it now and create your own advertising campaigns just by asking Claude.
Advertising APIs are powerful — but demanding. The Spotify Ads API v3 has over 30 resource types, nested targeting structures, and multi-step entity hierarchies where campaigns contain ad sets that contain ads. For someone who just wants to launch an audio campaign targeting listeners in Connecticut, the cognitive distance between intent and execution is significant.
We wanted to close that gap by letting people describe what they want in plain English and having the system figure out the rest. A single natural language request becomes a full, correct campaign structure.
The result is a Claude Code plugin that translates natural language into Spotify Ads API calls built from Markdown files, a bash script, and two small Python helpers. It’s open source and designed for developers and advertisers who want full control over how LLMs interact with the Ads API.
This post covers the architecture, the opinionated technology choices we made, and what we learned about building developer tools on top of LLM-powered agents.
What it does
The plugin installs into Claude Code and provides a set of slash commands for managing Spotify ad campaigns:
The more interesting interaction mode is conversational. You can say things like:
"Create an audio campaign called Back to School Promo targeting 25-44 year olds in the US with $100/day budget"
Instead of issuing a sequence of commands or writing orchestration code, users describe the outcome and the agent handles the workflow by routing to the right skills and API calls. The system bridges the gap between intent (“launch a campaign”) and execution (multiple dependent API calls with correct parameters, IDs, and validations), removing the need to manually orchestrate the campaign → ad set → ad lifecycle.
The plugin's agent decomposes this into the correct sequence of API calls: looking up geo-targeting IDs, converting dollar amounts to micro-units, validating audience size, creating the campaign entity, creating the ad set with targeting and budget, and creating the ad with creative assets. It understands required fields and prompts the user for any missing information along the way.
Why these technology choices
This plugin is opinionated. To build fast, we focused on Claude Code, macOS, used a CLI-first approach backed by an OpenAPI spec, and deliberately avoided MCP for now.
Why Claude Code
Claude Code's plugin system has a property that turned out to be critical for this project: plugins are written in Markdown. Skills, agents, and the reference documentation that grounds the LLM's API knowledge are all .md files. There is no compiled code in this plugin. There is no build step, no package manager, no bundler, no transpiler.
The plugin architecture has four component types that map well to different concerns:
Skills define the slash commands. Each is a self-contained Markdown file describing the command's behavior, API endpoints, request formats, and output handling.
Agents handle freeform natural language. Our request-builder agent triggers automatically when a user describes an advertising task conversationally, and decomposes it into API calls.
Hooks intercept tool calls before execution. We use a PreToolUse hook to transparently refresh OAuth tokens and inject HTTP headers.
Settings store per-user configuration (credentials, ad account, environment preference) in a gitignored local file.
The result is a plugin where every component is human-readable, diffable, and version-controllable. When a new API quirk surfaces during testing, the fix is usually adding a sentence to a Markdown file. This design makes the system easy to customize, extend, and adapt without the overhead of maintaining a traditional SDK or compiled integration.
Why CLI + OpenAPI Spec (and not MCP)
Model Context Protocol (MCP) is becoming the default standard for connecting LLMs to external tools. It would seem like a natural fit here where we define a set of tools for campaign management, expose them via an MCP server, and let any MCP-compatible client use them. We considered this approach and chose against it for several reasons.
The API surface is too large for static tool definitions. The Spotify Ads API has dozens of endpoints with nested request schemas. Defining each as an MCP tool with full parameter schemas would produce a massive tool registry that would consume significant context window space in every interaction, whether or not the user needs those endpoints. With the Claude Code plugin approach, the agent loads only the reference documentation it needs for a given request on demand.
Curl commands are transparent and debuggable. Every API call the plugin makes is a curl command that it shows to the user. The user can see exactly what's being sent, copy it, modify it, run it independently. This transparency provides auditability and user control in an advertising system where every request can impact real budgets. Users can verify, reproduce, and adjust execution rather than relying on opaque tool behavior.
The OpenAPI spec is the source of truth. The Spotify Ads API publishes a comprehensive OpenAPI v3 spec (~8,600 lines). Rather than translating this into MCP tool schemas (and maintaining that translation as the API evolves), we ship the spec directly in the plugin. The agent reads it when it needs to understand an endpoint's parameters or response format. When the API changes, we update one file.
The agent: domain-expert translation
The natural language agent (agents/spotify-ads-request-builder.md) is a Markdown file that turns the LLM into a Spotify Ads API specialist. Its system prompt covers:
Value conversions: dollars to micro-amounts, date descriptions to ISO 8601, platform names to API enum values
Multi-step orchestration: decomposing "create a full campaign" into the three sequential API calls (campaign, ad set, ad), passing IDs between steps
Geo-targeting lookups: when a user says "target Connecticut," the agent calls the geo-targeting search endpoint, finds the region ID, and constructs the flat geo_targets object with the correct structure
Pre-flight validation: before creating an ad set, the agent calls the audience estimate endpoint to check that the targeting is broad enough to meet minimum thresholds
Execution control: respecting the user's auto_execute preference, either showing the curl command and asking for confirmation, or executing directly
OpenAPI links as a navigation graph
One existing feature of our OpenAPI spec that proved valuable is our use of OpenAPI Links. Links are a relatively underused part of the OpenAPI 3.x specification that define relationships between operations - specifically, how the response from one operation can be used as input to another.
The Spotify Ads API spec encodes the entire entity hierarchy through links. The 201 response for campaign creation declares:
The ad set creation response, in turn, links forward to ad creation and backward to its parent campaign:
And the ad response links laterally to the assets it references: the primary creative, the companion image, the logo:
For a human developer reading API docs, these relationships are usually implicit; you piece together the entity hierarchy from endpoint naming conventions and documentation prose. For an LLM agent, having them declared explicitly in a machine-readable format is a significant advantage. The runtime expressions ($response.body#/id, $request.path.ad_account_id) tell the agent exactly which fields to extract from one response and inject into the next request. The operationId values let the agent look up the target endpoint's full schema.
This is one reason we chose to ship the raw OpenAPI spec alongside our curated documentation. The curated docs describe what each endpoint does. The links in the spec describe the graph of operations that makes multi-step workflows possible, effectively encoding the same workflow graph that the agent needs to follow at runtime. When the agent decomposes "create a full campaign" into three sequential API calls, it's following the same traversal path that the OpenAPI links define: campaign → ad set → ad, with response IDs flowing forward through $response.body#/id at each step.
The Ad Set response also links to targeting lookup endpoints which is how the agent knows to call /targets/geos before constructing a geo-targeting payload. The spec doesn't just document individual endpoints; it documents the workflows between them.
The role of the OpenAPI Spec
The plugin ships with the full Spotify Ads API v3 OpenAPI spec (external-v3.yaml, approximately 8,600 lines). The agent consults this spec through the api-reference skill, which provides curated endpoint documentation, schema definitions, and enum values distilled from the spec.
The spec serves as both documentation and validation. When the agent isn't sure about a field name or type, it reads the relevant schema definition. When a user asks about targeting options, the agent can look up the valid enum values. The decision to ship the raw spec alongside curated documentation reflects a pragmatic tradeoff. The curated docs in api-reference/references/ cover the most common operations with clear examples. The raw spec covers everything, including less-used endpoints, edge-case parameters and error responses. The agent uses the curated docs first and falls back to the spec when needed.
What’s next?
Observing and optimizing user flows. The current agent logic is based on understanding of relatively simple advertising flows. We plan to observe common patterns and "de-composition" bottlenecks to further refine our Markdown-based skills. By identifying where the agent requires the most clarification, we can optimize the system prompts to handle those edge cases preemptively.
Support for idempotency keys. To prevent the accidental creation of duplicate campaigns or ads during network retries or agent re-runs, we plan to introduce support for idempotency keys. By generating a unique client-side key for each intent, we can ensure that the Spotify Ads API treats a retried request as a single operation, providing a safety net for automated execution
Supporting other platforms. We started with Claude because of its strong support for tool calls, but are exploring other platforms including Codex and Gemini CLI. We are particularly excited about the image generation capabilities with GPT5.5 and Images 2.0 for creative generation.
Wrapping up
This plugin is a bet on a specific thesis: that the best interface to a complex API is natural language, grounded by detailed documentation, with transparent execution. The user says what they want. The agent figures out the API calls. The hook layer handles authentication silently. And every curl command is visible, copyable, and debuggable.
There's no framework, no runtime, no dependencies beyond curl, jq, and python3. The source of truth is the OpenAPI spec. The business logic is prose.
Whether this approach scales to the most complex API integrations is an open question. But for the Spotify Ads API, where the distance between "I want to run an audio campaign in the US" and the correct sequence of POST requests is substantial, it works impressively well.
The plugin is released as open source under the Apache 2.0 license. If you're building Claude Code plugins or working with the Spotify Ads API, we'd welcome contributions and feedback. The spotify-ads-api plugin is available on GitHub and through Anthropic's Claude Plugins marketplace. Download it now and create your own advertising campaigns just by asking Claude.
```

---

## 2. Background Coding Agents: Supercharging Downstream Consumer Dataset Migrations (Honk, Part 4)

- 日期: 2026-04-22 19:39
- 链接: https://engineering.atspotify.com/2026/4/background-coding-agents-dataset-migrations-honk-part-4/

```
Background Coding Agents: Supercharging Downstream Consumer Dataset Migrations (Honk, Part 4)
This is part 4 in our series about Spotify's journey with background coding agents (internal codename: “Honk”) and the future of large-scale software maintenance. See also part 1, part 2, and part 3.
In Part 2, we explored how we enabled our Fleet Management tools to use agents to rewrite our software automatically. We also explored how to write good prompts that allow the agent to best work without needing human input. In this blog post, we give a case study of how one team at Spotify used Honk with our Backstage and Fleet Management platforms to ease the pain of migrating thousands of dataset consumers onto new dataset versions — saving an estimated 10 engineering weeks in the process. We also share what we learned about how to make our data landscape more autonomous-coding-agent–friendly in the process.
Dataset migrations can be painful
As any data team knows, getting users to migrate to new endpoints can be a slow and painful process, both for the data owners and the downstream teams that use the datasets day-to-day.
At the end of last year we needed to deprecate two of the most heavily-used user datasets in order to release new versions with additional dimensions that would unlock new features. These deprecated datasets had ~1,800 direct downstream data pipelines between them and indirectly impacted several thousand more across the entire company.
We faced the prospect of migrating ~1,800 direct downstream data pipelines in only six months, across three very different pipeline frameworks that we use at Spotify: the SQL-based BigQuery Runner and dbt frameworks, and the Scala-based Scio.
We estimated that it would have taken around 10 engineering weeks of effort to complete these migrations manually. Facing that much work, we explored how Backstage, Fleet Management, and Honk might be able to automate some of the complexity.
Simplifying fleet migrations with Backstage
Before we could begin making any code changes, we had to first understand the lineage of our deprecated datasets so we would know which repositories to make those changes in. This is where Backstage’s endpoint lineage and Codesearch plugins came in.
Each endpoint’s Backstage page gave a clear list of downstream consumers, giving us an immediate sense of the scale of our migration. With Codesearch, we wrote queries that would find target repositories across the Spotify GitHub Enterprise landscape, and mark them as in-scope for our migrations, which we orchestrated using our Fleetshift plugin.
With Honk, context is key
As we discussed in Part 2, context engineering is a key part of the process when working with background coding agents. With our target repositories now identified quickly via Backstage, this was the part of the build that took the most time and iteration to get right, and also where we learnt the most.
One of the major challenges for Honk in this migration was the fact that it had to deal with three different data pipeline frameworks, two of which are reasonably consistent in style and substance across the company (BigQuery Runner, dbt), and one of which isn't (Scio). This lack of standardisation across our data landscape made it hard to write all-in-one prompts for Honk that could truly capture all available permutations of what it would encounter.
Although we are adding these features now, at the time of these migrations, Honk did not have access to Claude skills or custom configurability when it runs. This was a design choice made to establish guardrails around the range of possible outcomes during the migration. This meant that the prompt given to it had to be comprehensive, because it could not do things like use MCPs to go and read dataset schemas that you had not given it, or read external documentation for more context.
Trying to write a good, fully-comprehensive prompt for Scio pipelines, which can vary hugely between teams due to the relative flexibility that the framework provides, got very unwieldy without having access to outside Claude skills. We therefore made the decision not to continue trying to make Scio migrations work at that time, and focused on the other two pipeline frameworks.
For the dbt and BigQuery Runner pipeline frameworks, which were much more standardised, we initially attempted to generate a good context file by asking Claude to re-purpose a migration guide that was written for human engineers. However, the resulting context was not comprehensive enough, and Honk was left to make assumptions about how to map from one dataset field to another that were often incorrect. Once we adjusted for this, and made all mappings clear using tables in the context file — keeping in mind that Honk could only access the context we had written for it and little else — we began to see solid performance across the majority of target repositories.
Having these fine-grained instructions also allowed us to specify where Honk shouldn’t try to perform a field migration, for example, in cases where a use case–specific judgement call was required. In these cases, we asked Honk to leave the fields unchanged, but to add comments above them with links to human engineer migration guides to make the task as easy as possible for the team that would later review the pull request.
One final challenge we encountered was that, unlike with Scio pipelines, the BigQuery Runner and dbt repositories across the company rarely used any build-time unit testing. This meant that one of Honk’s key features, its ability to verify its work and then adjust based on the results, was unavailable to us, and we had to rely on the downstream owning teams to perform their own manual testing before merging the automated PRs.
That said, we successfully rolled out 240 automated migration PRs using Fleetshift. Here, Backstage and Fleetshift greatly simplified the ongoing monitoring and management of our shifts by providing an overview UI that gave us a snapshot view of migration progress, and the ability to easily click through and view any of the automated PRs without manually searching for the repositories. This was invaluable for troubleshooting, progress monitoring, and facilitating communication with the owning teams.
What did we learn for the future
It became clear during this project that the success of using our Fleet Management tools with Honk for large-scale, complex migrations is going to depend on the strategic push to consolidate and standardise our data landscape. Similarly, we must enforce requirements for testing and validation across repositories so that agents like Honk can verify their work in an automated fashion. Both of these elements will be critical in enabling background coding agents across Spotify.
In addition to that, there are exciting features on the Honk roadmap that will also enhance its performance on complex tasks. The Honk team is working on a feature that will allow the agent to spend some time gathering its own context, for example by reading JIRA tickets or documentation, before it begins to perform code changes. This reduces the need for such comprehensive context files to be written up front, and should improve the quality of the resulting code changes by making full use of the Claude Code capabilities.
With both of these wider, strategic changes taking place, and alongside that the underlying Claude Code agents improving in capability all the time, we look forward to seeing Fleet Management using Honk excelling on tackling more and more complex migrations in the future and reducing manual toil for our engineering teams.
Learn more about Fleet Management and our background coding agent Honk:
Honk, Part 1: 1,500+ PRs Later: Spotify’s Journey with Our Background Coding Agent
Honk, Part 2: Context Engineering
Honk, Part 3: Predictable Results Through Strong Feedback Loops
On-demand webinar: How Spotify Built Honk
Now available: Fleetshift for Spotify Portal — perform complex code changes at scale, just like we do at Spotify
```

---

## 3. Let’s Talk Agentic Development: Spotify x Anthropic Live

- 日期: 2026-04-06 19:49
- 链接: https://engineering.atspotify.com/2026/4/anthropic-agentic-development/

```
Let’s Talk Agentic Development: Spotify x Anthropic Live
AI agents are transforming the way we build — and even how we think of ourselves as software developers. Both Spotify and Anthropic have been exploring what this shift means in practice, and on March 30, we got together at Spotify's London HQ to share what we're learning.
In our fireside chat “Let’s Talk Agentic Development”, Spotify's chief architect, Niklas Gustavsson, sat down with Anthropic’s David Soria Parra (co-creator of MCP) and Christian Ryan (applied AI lead) for a wide-ranging discussion on what agentic-first development actually looks like at scale — from the tools and infrastructure that make it work, to the organizational shifts it demands.
Watch our special fireside chat with Anthropic
Some highlights from the conversation:
More than vibes: The day Opus 4.5 went online
November 25, 2025 — the moment when agentic-first software development got real. One model release showed up as a visible inflection point on Spotify's internal charts — and changed how engineers at both companies work day to day. Hear what it was like from the inside.
“That has really been the shift for me — going into the office one week, seeing people in front of an IDE, coming back three weeks later and seeing everyone in front of terminals only.” — David Soria Parra, Anthropic
Honk: Spotify's background coding agent, powered by Claude
Spotify lets anyone prompt an agent with a Slack message. What could go wrong? Hear about the journey from deterministic code migrations to a Slack-native coding agent to using agents to perform complex software migrations across thousands of repos at once — and where Honk is headed next.
“A very typical user interaction these days is some people discussing some problem they want to solve on Slack and then just @mentioning Honk — like, go solve this.” — Niklas Gustavsson, Spotify
Context and control: Foundations for AI at scale
How to standardize your ecosystem and orchestrate Claude across thousands of repos. Both teams share what's actually working — and where the gaps still are — when it comes to giving agents the right context at enterprise scale.
“When it comes to context management and context engineering, I think having a good set of actually fairly simplistic setup that is reproducible across engineers, with a good set of Claude MD setups, a good set of skills that really capture the essence of the role you're trying to do or the domain you're trying to operate in. I think that's really it and don't overthink it.” — Christian Ryan, Anthropic
Humans vs. agents: Testing, reviews, and governance
What changes when agents can ship code faster than humans can review it? The panel gets into the new bottlenecks — and the hard questions about accountability — that come with scaling agent-generated output.
“It doesn't really matter who generated what or what was behind it. If it’s an agent or a human, it’s very much outcome-based, and you also want to have someone who’s accountable for the outcome.” — Christian Ryan, Anthropic
What’s next?
Toward the end of the conversation, David points out that 2025 has been about the creation of code, but the next frontier is agents taking on the full software lifecycle — maintenance, deletion, and the kind of work nobody wants to do but everyone needs.
Backstage is evolving from a human-facing developer portal into an agent-first platform, with MCP connections replacing manual workflows.
And at Anthropic, the same internal dogfooding (or as Anthropic calls it, “ant-fooding”) culture that produced Claude Code and Cowork continues to surface new product ideas at a pace that surprises even the people building them.
Watch the full conversation above, and check out our Honk blog series for a deeper dive into how we're using background coding agents at Spotify:
1,500+ PRs Later: Spotify's Journey with Our Background Coding Agent (Honk, Part 1)
Background Coding Agents: Context Engineering (Honk, Part 2)
Background Coding Agents: Predictable Results Through Strong Feedback Loops (Honk, Part 3)
Thanks to our friends at Anthropic for a great discussion and to everyone who joined us online and in person.
```

---

## 4. Inside the Archive: The Tech Behind Your 2025 Wrapped Highlights

- 日期: 2026-03-12 20:42
- 链接: https://engineering.atspotify.com/2026/3/inside-the-archive-2025-wrapped/

```
Inside the Archive: The Tech Behind Your 2025 Wrapped Highlights
Every year, Spotify Wrapped gives hundreds of millions of listeners a snapshot of your year in listening. For 2025 Wrapped, we wanted to go deeper. What if we could identify interesting listening moments from your year, and tell you a story about them? The day you discovered that artist that changed everything. The day you played nothing but “yearning” music for six hours straight. The day your music taste took a hard left turn.
That's Wrapped Archive.
For each eligible user, we identified up to five remarkable days from their 2025 listening history. We generated a personalized, LLM-generated “report” for each, essentially a creative narrative grounded entirely in real listening data.
So how did we build it?
How we taught an algorithm to spot your big day
To identify the “remarkable days” per user from an entire year of listening, we designed a priority-ordered set of heuristics.
Some were straightforward. Biggest Music Listening Day and Biggest Podcast Listening Day simply captured the highest total minutes listened. Biggest Discovery Day highlighted when a user listened to the most first-time artists. Biggest Top Artist Day surfaced the day a listener spent the most time with a single favorite artist, while Biggest Top Genre Day captured when one genre dominated their listening.
Others were more complex. Most Nostalgic Day surfaced spikes in older catalog or throwback-heavy sessions. Most Unusual Listening Day identified when a user strayed furthest from their typical taste profile. Contextual anchors like Your Birthday and New Year’s Day rounded out the set.
By ranking these candidates in order of narrative potential and statistical strength, we narrowed hundreds of millions of listening events down to up to five standout days per user.
Sometimes the result was surprisingly meaningful — like a Biggest Music Listening Day that just so happened to be their wedding day.
We used a distributed data pipeline to compute and aggregate candidate days at the user level. For each user, we stored their remarkable days and relevant listening history data to object storage. When it was time to pre-generate reports, we published these data points onto a messaging queue that allowed the next stage of the system to consume the data points asynchronously.
Yes, we actually generated 1.4 billion reports
Prompt engineering for consistency at scale
Prompting became a daily practice for more than three months. We needed prompts that could reliably generate creative, emotionally resonant stories, without hallucinating, stereotyping, or drifting off-brand. We split the prompt into two layers:
The system prompt defined the creative contract:
Data-driven storytelling: every insight had to be traceable to actual listening behavior.
Tone and style: witty, sincere, and quietly playful.
Trust and safety by default: avoid references to drugs, alcohol, sex, violence, or offensive language.
The user prompt removed ambiguity. Each generation included:
Detailed listening logs for the day
A summarized stats block (LLMs are bad at math)
The listener’s overall Wrapped data
The category of the interesting day
Previously generated reports (to avoid repetition)
The user’s country (for spelling and vocabulary)
Prompting wasn’t a linear process. It was a loop. We used a prototype to compare outputs across prompt versions and edge cases. We ran LLM-as-a-judge evaluations on sampled outputs. We layered in human review. Creative, technical, and safety feedback all fed into the next iteration.
Shrinking the model, amplifying the story
High-performance models were excellent for prototyping, but running them to generate over a billion reports was economically unfeasible. We built a distillation pipeline to address this.
We used a frontier model to produce high-quality reference outputs. From these, we curated a tightly reviewed “gold” dataset that captured the voice, constraints, and stylistic nuances we wanted to preserve. We then fine-tuned a smaller, faster production model on this dataset, transferring the quality of the larger model into a more efficient form.
To push performance further, we introduced Direct Preference Optimization (DPO), powered by A/B-tested human evaluations. Although the preference dataset was relatively small, it was highly curated and intentionally constructed. That signal proved strong enough: the fine-tuned production model achieved strong preference parity with the original baseline.
Running the generation engine
The numbers were intimidating. Around 350 million eligible users, each getting up to five reports, totaling roughly 1.4 billion reports, all pre-generated before Wrapped launch day.
Each report required a call to our fine-tuned model. That meant sustaining thousands of requests per second for days, under strict latency constraints.
Based on available capacity, we decided to process all reports in an initial single batch. Once each user’s remarkable days were computed, we could begin publishing their listening snapshot to a pubsub message queue. From there, each remarkable day was processed, generating one report at a time per user, so earlier reports could inform later ones to avoid repetition.
Monitoring became critical. Our real-time dashboards gave us visibility into report generation progress, system reliability, and projected completion time.
For four days straight, the generation engine ran without pause!
During that time, we carefully monitored throughput, ensuring we took advantage of our capacity without running into timeouts or errors. Once the initial pass completed, we carefully combed through the output to detect missing reports, data inconsistencies, and any other issues – and we re-generated those problematic reports (more on that later!)
Designing for parallelism and persistence
By the end of pre-generation, over a billion reports were stored and ready to be served. Getting them there safely under heavy parallelism required careful storage design.
We used a distributed, column-oriented key-value database designed for high-throughput writes. Each user’s data lived in a single row keyed by user identifier. Within that row, we tracked which remarkable days had completed reports.
Each user could have up to five reports, generated independently and written concurrently. That meant multiple writes for the same user could land at nearly the same time. A naive read-modify-write approach to tracking completed days would have been vulnerable to race conditions and lost updates.
Instead, we designed the schema to make concurrent writes naturally safe. Rather than storing a serialized list of completed days, we gave each day its own column qualifier within a dedicated column family, using the date YYYYMMDD as the qualifier. For example, March 15 becomes 20250315, June 22 becomes 20250622. Concurrent writes for different days therefore touch completely different cells within the same row, hence no coordination, no locks, no read-modify-write cycles.
The full report content lived in a table keyed by user and date. Writes followed a deliberate order: first the report content, then a lightweight metadata entry marking the day as complete. This ensured users would never see a reference to a report that hadn’t been successfully written, while still allowing fully parallel, high-throughput storage.
The most elegant solution to concurrency wasn’t complex application logic. It was thoughtful data modeling.
Built for the big bang
Wrapped launches globally at a single moment. There’s no gradual rollout. One second the service is idle; the next, millions of users are hitting it.
Auto-scaling reacts to observed load. Wrapped doesn’t ramp, it spikes! Reactive scaling simply doesn’t move fast enough.
So we had to be proactive.
We pre-scaled compute pods and database node capacity hours before launch. We coordinated model-provider capacity to ensure throughput aligned with expected demand. Then we ran synthetic load tests across all geographic regions where the service is hosted, timed to start after pre-scaling completed but before real user traffic arrived.
These tests warmed connection pools and caches on the compute side, and ensured database nodes had distributed tablet assignments and warmed their block caches on the storage side. We ran them long enough to cover the critical launch window.
When real traffic arrived, nothing was cold.
At Wrapped scale, even a brief period of elevated latency can impact millions of users. Pre-scaling and synthetic load didn’t just protect performance, they protected the experience people wait all year for.
How we Pressure-Tested the System
When you’re generating over a billion reports, even a 0.1% failure rate would translate to millions of “broken” stories. Human review at this scale is impossible. So we built an automated evaluation framework.
Who judges the judge?
Production reports were generated by our fine-tuned model. To support large-scale QA and evaluation, we stored the generated reports into an evaluation data warehouse optimized for ad-hoc querying and corpus-wide analysis. Evaluation was performed by larger models acting as judges (LLM as a judge). Each report was graded across four dimensions: accuracy, safety, tone, and formatting.
To preserve the efficiency gains from distillation, we evaluated a large random sample (~165,000 reports) rather than the full corpus. Instead of one massive evaluation prompt, we used multiple smaller rule-based queries per report. This reduced non-deterministic results and allowed parallel grading. Requiring the judge to produce reasoning before a final score improved evaluation consistency.
We also built internal tooling for side-by-side prompt comparisons and structured logging, allowing brand and design partners to participate directly in tuning decisions.
Catching what slips through
Evaluation fed directly into a structured remediation loop. We identified problematic reports through model-based evaluators and targeted human review, then used SQL queries and regex-based pattern matching to surface structurally similar failures across the corpus. Remediation followed through batch deletion of affected reports and guardrail updates to prevent recurrence.
One example made the value of this loop clear. During evaluation, we discovered that some Biggest Discovery Day reports were confidently celebrating the wrong number of artists discovered. The underlying heuristic was correct, but a subtle timezone bug in the upstream data pipeline occasionally surfaced the wrong top discovery day. The model faithfully wrote a compelling story about it.
Because we were running structured evaluations and logging report IDs with full metadata, we could trace the problem back to the source, quantify its prevalence across the corpus, fix the pipeline, delete the affected reports in bulk, and replay them safely.
Lessons in scale, safety, and storytelling
Less is more! The more instructions we piled on, the less creative the output became.
Prompting doesn’t scale without evaluation. Generating over a billion reports means failures are inevitable. Prompt and evaluation design have to evolve together.
Concurrency problems are often data modeling problems. By leaning into a column-oriented schema, we eliminated the need for coordination altogether.
Real fault isolation starts at the architecture level. By designing our systems as an isolated storage and serving path, we minimized impact surface while shipping an AI-powered feature.
Engineering expertise drives the work; AI coding assistants amplify it. By using these tools extensively throughout development, we were able to prototype faster, generate test scaffolding, reason about edge cases, and refactor complex flows.
Finally, at this scale, the LLM call is the easy part. The real work is in capacity planning, replay and recovery, cost discipline, safety loops, and preparing for a single high-stakes launch moment where everything has to work seamlessly.
Wrapped Archive reached hundreds of millions of users around the world. We harnessed the power of AI paired with Spotify's magic — the data — to create something that genuinely resonated, tapping into real memories and feelings of nostalgia.
We are proud to have delivered something that resonated at a global scale that was built with care, tested with rigor, and engineered responsibly from end to end.
Special thanks to the Archive development team for their hard work on Wrapped Archive and for contributing their insights to this post - Sravya Alla, Federico Buffoni, Sari Nahmad, Ana Shevchenko, Anton Hagermalm, Ataç Deniz Oral, Dan Landau, Fred Wang, Maia Ezratty, Maxwell Newlands, Yoshnee Raveendran, Peter Goggi Jr., Renato Gamboa, Ger Carney, Ishaan Poojari, and Nadja Rhodes
```

---

## 5. Our Multi-Agent Architecture for Smarter Advertising

- 日期: 2026-02-19 17:28
- 链接: https://engineering.atspotify.com/2026/2/our-multi-agent-architecture-for-smarter-advertising/

```
Our Multi-Agent Architecture for Smarter Advertising
Introduction
When we kicked this off, we weren’t trying to ship an “AI feature.” We were trying to fix a structural problem in how our ads business actually runs in software.
On the business side, we have multiple ways of buying—Direct, Self‑Serve, Programmatic—all sitting on top of a mostly consolidated backend. The infrastructure is shared; the behavior isn’t. Each buying channel has its own workflows, its own decision logic, and its own flavor of “what good looks like.” On the engineering side, that shows up less as “different stacks” and more as “different brains” wired into the same body:
One set of services and data powering multiple buying experiences
Channel‑specific flows that encode slightly different rules and heuristics
Surface‑specific automation (Spotify Ads Manager, Salesforce, Slack, internal tools) solving overlapping problems in slightly different ways
A steady stream of “small workflow tweaks” that are all variants of the same planning / optimization problem, but need to be implemented and maintained in multiple places
So even though we’ve done the work to consolidate services, we still end up with fragmented behavior at the workflow layer. The same core decisions—how to allocate budget, how to choose inventory, how to balance reach vs efficiency vs STR—get re‑implemented per channel and per surface. Over time, they drift.
The standard playbook here would be familiar: design a new service, define the “right” state machine for planning and managing campaigns, add some Representational State Transfer (REST) endpoints, plug it into the UIs, and call it done.
The problem is that this doesn’t really fit the shape of the work anymore:
Workflows are combinatorial. Planning, forecasting, audience selection, creative guidance, pacing, and optimization all depend on who the user is, what inventory is available,business priorities and advertiser goals. You can’t capture that in a couple of hard‑coded “happy paths” per channel and expect it to hold up as things change.
The same decisions need to show up everywhere. If we decide on a better way to allocate budget or prioritize inventory, that should consistently show up in Spotify Ads Manager recommendations, Salesforce plans, and Slack workflows. Re‑implementing the same decision logic three different times is an easy way to create tech debt and inconsistent behavior.
We’re missing an intent layer. Our systems are good at doing things (create a line item, run a forecast, fetch insights). They’re not good at taking a goal like “maximize reach in Brazil, protect video inventory, and still hit STR” and turning that into a sequence of tool calls, tradeoffs, and checks that look the same across channels.
So the core problem wasn’t “we need a new backend.” The problem was:
We don’t have a unified, programmable decision layer that can understand goals, reason over shared signals, and orchestrate our existing Ads APIs on behalf of users—consistently across buying channels and surfaces.
We also knew we didn’t want to swing to the other extreme and build a giant rules engine. Our ads logic is messy, probabilistic, and constantly changing. Forecasting, optimization, and insights already lean heavily on ML. Freezing all of that into a static decision tree would be brittle almost immediately and painful to maintain.
That’s the gap where we decided to bet on an agentic approach.
Instead of:
Hard‑wiring more deterministic workflows per channel
Burying orchestration logic inside each individual service or surface
Duplicating “smart” behavior in Spotify Ads Manager, Salesforce, Slack, and whatever comes next
We treat campaign planning and management as a set of modular agents that:
Consume the same underlying signals (inventory, audiences, STR, quality/risk, performance history)
Optimize jointly for advertiser goals and Spotify’s business constraints
Use our existing Ads services as tools instead of re‑implementing capabilities from scratch
For our org, this is new territory. Most of our AI work so far has looked like “put a model behind an endpoint” or “add a prompt‑based helper in the UI.” Here, we’re talking about:
A long‑running orchestration layer that delegates work to specialized agents
Agents with shared context and shared evaluation logic
A single agentic platform that can power all buying channels and surfaces off the same decision engine, instead of a patchwork of overlapping workflows
That’s a different mental model than “one more backend service with some workflows.” It forces us to think in terms of:
APIs designed as tools for agents, not just CRUD
Testing as behavioral evaluation, not only unit + integration tests
Observability as “what did the agent decide and why?” not just p95s and error budgets
Safety as guardrails on semi‑autonomous decisions, not just input validation
We’re taking this bet because the alternative is pretty clear: keep scaling complexity, coordination cost, and duplicated logic every time we improve planning or optimization in a new place. An agentic platform lets us centralize decision‑making once and project it everywhere—on top of the consolidated backend we already have—so the workflows can finally converge even as the products evolve.
From there, the question became: where do we prove this out first?
We chose Media Planning as the initial use case because it’s where all of this complexity shows up at once. It’s the point where sales, advertisers, inventory, pacing, and ad products collide. It’s also early enough in the lifecycle that if we get the decisions right here, everything downstream (booking, trafficking, delivery, optimization) benefits.
In the next section, we’ll go deeper on how we turned Media Planning into an agentic workflow: how we decomposed the planner’s job into tools and capabilities, how agents reason over constraints, and how we wired this into existing systems without rewriting the world.
Ads AI is our AI-powered advertising platform that leverages Google's Agent Development Kit (ADK) and Vertex AI to transform how advertisers create media plans at Spotify. By decomposing the complex media planning workflow into specialized AI agents that work in parallel, we've built a system that can understand natural language campaign requirements and generate optimized, data-driven media plans in seconds.
Goal: Build an intelligent, conversational interface that enables advertisers to generate optimized media plans through natural language interaction, backed by historical performance data.
Key Takeaway: A multi-agent architecture with parallel execution can dramatically simplify complex domain problems while improving both developer experience and system performance.
The Challenge
Media planning for advertising campaigns involves several interconnected decisions:
Goal Definition: What does the advertiser want to achieve? (brand awareness, website traffic, app installs)
Audience Targeting: Who should see the ads? (demographics, interests, geography)
Budget Allocation: How should the budget be distributed across ad sets?
Schedule Planning: When should the campaign run?
Format Selection: Which ad formats (audio, video, display) perform best?
Our previous approach required advertisers to manually configure each of these dimensions, often without insight into what historically performs well for similar campaigns.
Pain points:
Complex UI flows: Multiple screens and forms to fill out
No optimization guidance: Advertisers had to guess at optimal configurations
Slow iteration: Testing different approaches required starting over
Knowledge gap: Historical performance data wasn't easily accessible
The Solution: Approach and Implementation
Design and Architecture
We chose a multi-agent architecture where specialized AI agents handle distinct aspects of media planning. This approach offers several advantages:
Separation of concerns: Each agent has a focused responsibility and optimized prompts
Parallel execution: Independent agents can run simultaneously
Testability: Individual agents can be tested and improved in isolation
Flexibility: New capabilities can be added as new agents
Implementation Details
Agent Breakdown
1. RouterAgent - The Traffic Controller
The RouterAgent analyzes incoming user messages and determines what information is present:
This fast routing step prevents unnecessary LLM calls and enables conditional agent execution.
2. Specialized Resolution Agents
Each resolution agent has a focused responsibility:
GoalResolverAgent: Maps user intent to campaign objectives (REACH, CLICKS, APP_INSTALLS, etc.) and searches for appropriate ad categories
AudienceResolverAgent: Extracts targeting criteria including interests (from a predefined taxonomy), geographic targets, age ranges, and gender
BudgetAgent: Parses various budget formats ($5000, 5k, €10,000) and converts to micro-units
ScheduleAgent: Handles date parsing including relative dates ("next month", "30 days")
3. MediaPlannerAgent - The Optimizer
The MediaPlannerAgent is where the magic happens. It takes all resolved information and generates optimized ad set recommendations using a heuristics-based engine backed by historical performance data.
Key Optimization Rules:
Cost optimization: Minimize cost metrics (CPM, CPC, CPI) relative to historical medians
Delivery rate optimization: Target campaigns with delivery rates close to 100%
Budget matching: Find historically successful campaigns with similar budget ranges
Duration matching: Match campaign durations to proven performers
Targeting matching: Score based on demographic and interest overlap
Unique format/goal combinations: Ensure diversity in recommendations
Budget-based scaling: Automatically adjust number of recommendations:
€0-1,000: 1 recommendation
€1,000-5,000: 2 recommendations
€5,000-15,000: 3 recommendations
€15,000+: 4-5 recommendations
Tool Integration with Function Calling
We leverage Google ADK's FunctionTool to give agents access to real data:
The @Schema annotations provide the LLM with structured information about tool parameters:
Prompt engineering for consistent output Getting LLMs to produce consistent, parseable output is challenging. We developed strict prompt guardrails:
Trade-offs considered
Single vs. multi-Agent: A single agent could handle everything, but would have a massive prompt and couldn't parallelize. Multi-agent adds complexity but improves latency and maintainability.
In-memory vs. database cache: We chose an in-memory cache for historical data to minimize latency. The tradeoff is memory usage, but campaign performance data is bounded and refreshed periodically.
Synchronous vs. streaming: We opted for synchronous responses initially for simplicity. Streaming would provide better UX for longer operations.
Results and Impact
Performance Metrics
Latency Breakdown
Overall Impact
Reduced cognitive load: Advertisers describe campaigns in natural language
Data-driven decisions: Every recommendation backed by historical performance
Faster iteration: Advertisers can refine by continuing the conversation
Democratized expertise: Optimization knowledge embedded in the system
Lessons Learned and Future Work
Key Learnings
Key learning 1: prompt engineering is software engineering
Treating prompts as code — with version control, testing, and iteration — was essential. Small changes in prompt wording can dramatically affect output consistency. We learned to:
Be explicit about output format requirements
Provide concrete examples in prompts
Build guardrails at both prompt and parsing layers
Key learning 2: agent boundaries matter
Drawing the right boundaries between agents is crucial. Too many agents increases latency and coordination overhead. Too few creates monolithic, hard-to-maintain prompts. Our rule of thumb: one agent per distinct skill or data source.
Key learning 3: tools enable grounding
LLMs are powerful but can hallucinate. By providing agents with tools that access real data (geo targets, ad categories, historical performance), we ground their outputs in reality. The LLM reasons about what to do; tools provide accurate data to work with.
Future Work
Streaming responses: Implement server-sent events for real-time feedback as agents process
Multi-turn refinement: Better support for iterative refinement ("frequent cycles of data evaluation")
A/B testing integration: Automatically test AI-recommended plans against baselines
Expanded agent capabilities: Creative suggestions, competitive analysis, cross-campaign optimization
Fine-tuned models: Domain-specific model fine-tuning for advertising terminology
Conclusion
Building Ads AI taught us that complex, multi-step workflows are well-suited to multi-agent architectures. By decomposing the media planning problem into specialized agents — each with focused prompts, relevant tools, and clear responsibilities — we created a system that's both powerful and maintainable.
The combination of Google's ADK for agent orchestration, Vertex AI for LLM capabilities, and our historical performance data creates a system that doesn't just understand what advertisers want — it knows what actually works.
We're excited to continue evolving Ads AI and bringing AI-powered optimization to more advertising workflows at Spotify.
```

---
