# InfoQ

> 分类: 技术社区
> URL: http://www.infoq.com/rss/rss.action
> 抓取: 15 篇

---

## 1. Fonttrio Launches as Open-Source Font Pairing Registry for shadcn/ui

- 日期: 2026-05-09 09:46
- 链接: https://www.infoq.com/news/2026/05/fonttrio-shadcn-fonts/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
Fonttrio, a new open-source font pairing registry built specifically for shadcn/ui projects, has launched with 49 curated font combinations that can be installed with a single CLI command. Created by developer Dima Kapish, the tool aims to eliminate the time-consuming process of selecting, pairing, and configuring fonts for web applications built on the popular component framework.
The tool leverages the registry:font
type introduced in shadcn CLI v4, allowing developers to install a complete typography system, including heading, body, and monospace fonts, along with CSS variables and a full typography scale, through one command:
npx shadcn@latest add <https://www.fonttrio.xyz/r/editorial.json>
Once installed, fonts are configured via next/font
in Next.js applications, CSS custom properties are set up in globals.css
, and a typography scale covering h1 through body text is applied automatically. The generated CSS variables follow a straightforward pattern:
--font-heading
--font-body
--font-mono
The launch attracted immediate attention from the shadcn/ui ecosystem. shadcn, the creator of shadcn/ui, responded on X saying:
This is amazing. Using the registry for font distribution. One click install. Congrats on the launch
The post received nearly 98,000 views and over 1,000 likes.
One Instagram creator highlighted a broader concern within the community around shadcn:
The shadcn-ification of apps is becoming a real problem. Everything is starting to look the same. Same components. Same layouts. Same vibe.
They acknowledged typography as an area to help break this and specifically called out Fonttrio.
Fonttrio enters a space with established alternatives, though none offer the same level of framework integration. Fontjoy uses machine learning to generate font pairings and offers adjustable contrast sliders, but produces recommendations rather than installable packages. Fontpair provides curated Google Font combinations with visual previews, but also lacks CLI integration. Neither tool generates CSS variables, typography scales, or framework-specific configurations.
For developers looking to adopt Fonttrio in existing shadcn/ui projects, installation requires shadcn CLI v4 or later. The shadcn team also introduced partial preset application in April 2026, allowing developers to selectively apply only fonts from a preset using npx shadcn@latest apply --preset <code> --only font
.
The full Fonttrio documentation, including an installation guide and API reference, is available alongside the source code on GitHub, where the project has already accumulated 377 stars at time of writing.
Fonttrio is an open-source project built by Dima Kapish for the shadcn/ui community. It is written primarily in TypeScript and distributed via the shadcn registry system, a mechanism that allows third-party tools and configurations to be shared and installed through the shadcn CLI. The registry approach represents a broader trend in the ecosystem toward composable, community-driven tooling that extends the core framework.
```

---

## 2. Cloudflare Ships Dynamic Workflows, Bringing Durable Execution to Per-Tenant and Per-Agent Code

- 日期: 2026-05-09 09:31
- 链接: https://www.infoq.com/news/2026/05/cloudflare-dynamic-workflows/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
Cloudflare has released Dynamic Workflows, an MIT-licensed library that extends the company's durable execution engine so that workflow code can be different for every tenant, agent, or request at runtime.
Previously, Cloudflare Workflows required workflow code to be part of the deployment, one binding, one class, per deploy. Dynamic Workflows removes that constraint, letting a platform route every create() call to a different tenant's code and have the engine dispatch run(event, step) back to that same code when the workflow executes seconds, hours, or days later. Dan Lapid and Luís Duarte from the Cloudflare engineering team write:
Say you're building an app platform where the AI writes TypeScript for every tenant. Say you're running a CI/CD product where each repository has its own pipeline. Say you're using an agents SDK where each agent writes its own durable plan. In every one of these cases, the workflow is different for every tenant, every agent, every request. There is no single class to bind.
The library is roughly 300 lines of TypeScript. A Worker Loader sits between the Workflows engine and the tenant's code (a Dynamic Worker), routing execution to the right tenant when the engine wakes up. When a tenant calls env.WORKFLOWS.create(...), it looks like a normal Workflow binding. Behind the scenes, the Worker Loader wraps the call with tenant metadata, the Workflows engine persists the payload, and when the engine later wakes to execute a step, the metadata routes execution back to the correct tenant's code. Workflow IDs, pause/resume, retries, hibernation, step.sleep('24 hours'), and step.waitForEvent() all work unchanged.
import { createDynamicWorkflowEntrypoint, DynamicWorkflowBinding, wrapWorkflowBinding } from '@cloudflare/dynamic-workflows';
export { DynamicWorkflowBinding };
function loadTenant(env, tenantId) {
return env.LOADER.get(tenantId, async () => ({
compatibilityDate: '2026-01-01',
mainModule: 'index.js',
modules: { 'index.js': await fetchTenantCode(tenantId) },
env: { WORKFLOWS: wrapWorkflowBinding({ tenantId }) },
}));
}
export const DynamicWorkflow = createDynamicWorkflowEntrypoint(
async ({ env, metadata }) => {
const stub = loadTenant(env, metadata.tenantId);
return stub.getEntrypoint('TenantWorkflow');
}
);
The CI/CD use case is where the architectural implications become most concrete. The blog post walks through a complete pipeline where the pipeline code lives in the customer's repository as a TypeScript WorkflowEntrypoint. The platform loads it dynamically, and each step runs with full durable execution semantics. The post lines up four Cloudflare primitives working together: Artifacts provides Git-native versioned storage with lazy tree hydration and instant fork() per CI run. Dynamic Workers run lightweight steps (lint, typecheck, bundle) in sandboxed isolates that boot in milliseconds. Dynamic Workflows hold the run together with durable, retryable steps that hibernate for free during approval waits. And Sandboxes handle the heavy steps that need a full operating system, with snapshot-based warm starts in seconds.
Cloudflare contrasts this with the ceremony of traditional CI, where allocating a VM, pulling a base image, cloning the repo, and installing dependencies can burn a minute or more before any actual work begins. The Dynamic Workflows stack skips all of that ceremony because the repo doesn't move, and the compute comes to it.
The broader platform thesis is explicit. Dynamic Workers solved the compute layer for multi-tenant dynamic code. Durable Object Facets solved the storage layer by giving each dynamically-loaded app its own isolated SQLite database. Dynamic Workflows now solves the durable execution layer. Cloudflare states that every binding Workers currently exposes is heading for a dynamic counterpart: queues, caches, databases, AI bindings, and MCP servers will all eventually be dispatchable per tenant, per agent, per request, at zero idle cost. If realized, this collapses the infrastructure cost of running a multi-tenant platform dramatically: idle tenants cost approximately nothing, active tenants share hardware through isolate-level multi-tenancy. In Cloudflare's framing, a platform that used to cap at thousands of paying customers can now reasonably serve tens of millions.
For agent platforms specifically, Dynamic Workflows means an agent can literally write its own run(event, step) function as a durable plan, where every step is independently retryable, every sleep hibernates for free, and every waitForEvent pauses indefinitely for human approval. The agent writes the plan. The platform runs it. Neither needs to know ahead of time what the plan looks like.
The competitive context for per-tenant durable execution is thin. Temporal and Inngest provide durable execution engines, but neither offers the dynamic per-tenant code loading at the isolation level that Dynamic Workflows enables. AWS Step Functions supports dynamic state machines but requires pre-defined task definitions. The combination of runtime code loading, V8 isolate-level isolation, and edge distribution is currently unique to Cloudflare's stack.
@cloudflare/dynamic-workflows is available on npm now, built on top of Dynamic Workers (open beta on the Workers Paid plan). The repository includes a working example with an interactive browser playground.
```

---

## 3. AWS Improves Aurora Serverless: 45% Faster Ramp-Up, 30% Higher Throughput

- 日期: 2026-05-09 06:56
- 链接: https://www.infoq.com/news/2026/05/aurora-serverless-v4/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
AWS recently updated Amazon Aurora Serverless with a new platform version that improves scaling behavior and runtime efficiency. According to the cloud provider, capacity can now scale up about 45% faster during demand spikes, and database performance improves by up to 30% through better resource scheduling and workload-aware scaling decisions.
Platform version 4 introduces improved runtime efficiency and a smarter scaling algorithm, enabling faster capacity scaling and higher database performance for Aurora Serverless clusters.
Generally available for four years, Amazon Aurora Serverless is an on-demand, automatically scaling configuration for Aurora that adjusts database capacity based on application demand. Supporting MySQL and PostgreSQL, Aurora Serverless scales down to zero capacity when not in use, adjusting capacity in small increments of 0.5 ACUs to match workload changes.
A HammerDB TPROC-C benchmark was used to measure performance across three Aurora Serverless platform versions with 1,024 virtual users. The results compare New Orders per Minute (NOPM) for each version and report the percentage change relative to the preceding platform version. Jiaming Yan, senior software development engineer at AWS, Ashok Kurakula, software development engineer III at AWS, and Nashad Safa, senior software engineer at AWS, write:
For both database engines supported on serverless, Aurora MySQL and Aurora PostgreSQL, platform version 4 delivers 27-34% higher NOPM compared to platform version 3.
Source: AWS blog
A Sysbench benchmark compared three Aurora Serverless clusters running platform versions 2, 3, and 4, with identical capacity settings ranging from 0.5 to 256 ACUs and faster scaling enabled. After loading 250 tables totaling 16 GB, a read-heavy workload executed 50 million queries with 512 threads. Evaluating the CloudWatch ServerlessDatabaseCapacity
metric to compare capacity across versions, Yan, Kurakula, and Safa conclude:
Platform version 4 delivers 27% faster completion with 28% lower cost than platform version 3, and 41% faster completion with 42% lower cost than platform version 2.
Corey Quinn, chief cloud economist at The Duckbill Group, writes in his newsletter:
Aurora Serverless scaling up 45% faster and down to zero, which is coincidentally where my enthusiasm for "serverless" databases that still bill in ACU fractions tends to land. Genuine improvements at no extra charge, though, which either means competitive pressure is working or someone in Seattle accidentally approved the wrong PRFAQ.
According to the announcement, the enhanced scaling algorithm benefits workloads where multiple tasks compete for resources, such as busy web applications and API services. Pini Dibask, principal database solutions architect at AWS, comments on LinkedIn:
What makes this especially interesting (...) is that Database Savings Plans which was announced at re:Invent 2025 offers Aurora Serverless the highest discount of any AWS database service (35% discount), combined with the performance gains of Platform Version 4 (which should translate into lower ACU consumption), the cost equation for Aurora Serverless has fundamentally shifted.
The update to the latest platform version applies automatically to new clusters and is available to existing clusters via the ServerlessV2PlatformVersion
parameter.
```

---

## 4. How GitHub Is Securing Agentic Workflows in Modern CI CD Systems

- 日期: 2026-05-08 14:38
- 链接: https://www.infoq.com/news/2026/05/github-agentic-workflows/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
GitHub has detailed the security architecture behind its agentic workflows, outlining a defense-in-depth approach to safely integrate autonomous AI agents into CI/CD pipelines. The design emphasizes isolation, constrained execution, and auditability to mitigate risks introduced by AI-driven automation.
Agentic workflows extend traditional automation by enabling AI agents to interpret intent, make decisions, and execute tasks within GitHub Actions. While this introduces productivity gains, it also expands the attack surface, including risks such as prompt injection, privilege escalation, and unintended actions. Industry discussions increasingly highlight that these systems require security models beyond deterministic automation.
As Jeremiah Snee noted in a GitHub Community discussion,
Continuous AI works best when used alongside CI/CD, extending automation to tasks that traditional pipelines struggle to express.
Pravin Chandankhede noted in a LinkedIn discussion, highlighting the core challenge agentic workflows address,
By design, agents are non-deterministic. They consume untrusted inputs, reason over live repository state, and can act autonomously at runtime.
At the core of GitHub’s design is a layered model built on isolation. Agents run in sandboxed, ephemeral environments with tightly restricted permissions, preventing persistence and limiting potential blast radius. Workflows operate in read-only mode by default, and any write operation must pass through controlled safe outputs, such as pull requests or issue comments, ensuring that all changes remain transparent, reviewable, and subject to approval before being applied.
As Florin Lungu noted,
GitHub's agentic workflows prioritize security through isolation, constrained outputs, and comprehensive logging.
A key principle is preventing secret exposure to agents. In shared runner environments, agents can access environment variables, configuration files, and runtime state, making prompt injection a serious risk. For example, a malicious input could trick an agent into reading credentials from local files or logs and exfiltrating them through external calls or repository artifacts. GitHub mitigates this by isolating agents in dedicated containers with restricted network egress, while routing sensitive credentials such as API tokens through trusted proxies and gateways outside the agent boundary.
A second layer constrains agent capabilities. Tool access is explicitly allowed, limiting which APIs or systems an agent can invoke, while network isolation reduces the risk of data exfiltration. This reflects a broader shift toward minimizing implicit trust in agent behavior.
GitHub agentic workflows security architecture (Source: GitHub Blog Post)
To further limit unintended impact, GitHub stages workflows and restricts write operations to controlled outputs. Agents can only propose changes, which are buffered and analyzed post-execution, ensuring that modifications are validated and policy-compliant before being committed.
As noted by Eddie Aftandilian, Head of Platform Engineering at XBOW, in a LinkedIn post,
These guardrails are what make it possible to bring agentic automation into real production repositories.
Observability forms the final pillar. GitHub logs activity across trust boundaries, including network traffic, model interactions, tool usage, and sensitive runtime actions. This enables full execution traceability, supports forensic analysis, and provides a foundation for enforcing future policy and information flow controls.
```

---

## 5. Presentation: Leadership in AI-Assisted Engineering

- 日期: 2026-05-08 12:40
- 链接: https://www.infoq.com/presentations/ai-assisted-engineering/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
Introduction
Justin Reock: I am Justin Reock. I'm the Deputy CTO at DX. We are the engineering intelligence platform based on a lot of research that you're probably familiar with, from Microsoft and Google Productivity Lab, and the University of Victoria, British Columbia. If you've heard of DORA and SPACE and the DevEx framework, that's a lot of what we focused on, and we basically built a platform around it. The presentation that I have for you today is built around this larger playbook, which is a playbook for senior executives, based on research, interviews, trends that we've seen, and then research from other organizations that we partner with, like the DORA community, for instance. We put a much larger explanation of all that into this guide, and then we built this presentation around it. We're going to cover a lot of highlights from that research.
What is the Current Impact of AI?
What is the current impact of AI? What are we even seeing? Nobody seems to know. Google, on the one hand, is telling us that their engineers are about 10% more productive as a result of using AI. They are, of course, a very engineering productivity-focused organization in the first place. However, we also had this now infamous METR Study, that had some problems with it. It was a small sampling of engineers, but it was still a pretty well-executed study that showed a 19% decrease in overall productivity in this particular experiment. Again, problems with this study. There were some engineers who had never used Cursor before, which was the tool that they were using in this study. What I think is pretty interesting is that every engineer in this study felt like they were more productive, like their qualitative data actually showed, no, I think I actually am getting more done. The data bore out that that wasn't true. We need to manage perceptions and reality. We have to measure, and we have to really be diligent about how this technology is working for us.
Our friends at the DORA community produced this report a few months ago, where they found these modest but at least positively leaning impacts to overall productivity and the developer experience. Twenty-five percent increase in AI adoption equated to a 7.5% increase in overall documentation quality. That was the biggest impact. A 3.4% increase in code quality, so modest, but at least not heading in the opposite direction. 3.1% increase in overall code review speed. A 1.3% increase in overall approval speed. On these averages, when we look at this data, again on an average, we find modest but positively leaning impact. DX, we can sample lots of data. We have samples from both qualitative and quantitative metrics that we pull from systems and that we pull from surveys and things like that. We thought, can we correlate this data? Will we see the same thing? What you're looking at here is the Change Confidence Developer Experience Index driver that we use. This is a qualitative measure, basically saying how confident do I feel when I put a change that I'm not going to break stuff? This is calculated on what's called a top box Likert score.
If you're familiar with survey engineering or at least have taken surveys, you've probably answered something that the possible answers for you are like always, very often, sometimes. The top box scoring means the percentage of people who answer always or very often. The two positive answers that you can have on that survey question. For change confidence, we found that moderate to heavy AI users, so this is either weekly or daily use of AI to help with engineering, led to a 2.6% average gain in change confidence. Similar to what DORA is seeing, positive leaning but modest impact. Code maintainability, another qualitative metric. How much cognitive load do I have to put into just understanding the code that I have in front of me? We found that the code became 2.2% more maintainable with AI users versus non-AI users.
The DORA metric for change failure rate. Who's familiar with DORA and the DORA metrics? This is the percentage at which when we add something value adding to the product, do we break it? Do we have to back it out? You want to be low on this one. We saw a 0.11% reduction overall here from using AI. It doesn't sound all that significant until you realize that the industry benchmark for change failure rate is like 4%. It is somewhat meaningful.
We have had lots of conversations with companies that are seeing things going in both directions. This can't necessarily be too accurate. We thought, what would happen if we broke this data out per company? Here's what we saw. Each bar represents a single company. The impact that, in this case, again, change confidence has had to their individual developer qualitative experience. Look at this. It's so noisy. It's all over the place. We have some companies seeing more than a 20% gain in change confidence, while others seeing more than a 20% decrease. The average, when we filter on average, we're not seeing the full picture. We're not seeing the full story. We need to look at this and actually look at a per company basis for this impact. Similar pattern for code maintainability. The same thing here. Some people getting messier and sloppier code. Others getting tighter, better code. Then here's change failure rate.
The top bar here, which you don't want to be on, you want to be on the bottom part of this graph, is 2%. Two percent against the industry benchmark of 4% means shipping as many as 50% more defects than you were shipping before. A lot of variability, a lot of volatility. Just like always, the future is here, but it is not evenly distributed, which is absolutely true for the ROI that we see with AI. Some organizations are seeing positive impacts, but others are really struggling, and even seeing negative impacts. We know that top-down mandates are not working very well. A decrease overall in psychological safety. People will game the system.
If the whole point is just 100% AI utilization, that really tells us nothing. We need to strive to understand impact as a multidimensional and longitudinal study of metrics that we get from organizations. We'll talk a bit about measurement. We found some patterns, maybe antipatterns, in organizations that were seeing poor results here. There was generally a lack of overall education and enablement. That seems very important. Not just providing good education, but also providing time to experiment in safe environments in which to do so, safe from both the systems in a psychological sense.
Often, organizations will just turn the tech on, and then just expect users to just magically be proficient. Just like any other technology, this does require learning. There is a learning curve. We've seen a very distinct learning curve, in fact, where whether you're a junior engineer or a senior engineer, whether you're a large enterprise or a smaller, scrappy software startup, going from no adoption of AI to light adoption of AI almost universally results in both quality and productivity deficiency. You see both go down. Then as you move into more moderate and heavy adoption, we balance off, and then even end up higher than we were before. We do see gains, but we see a clear, distinct learning curve that we have to prepare for in the meantime.
This is from that same DORA report. This is a Bayesian Posterior Distribution of AI. What does that mean? Effectively, the way to interpret this graph, these are qualitative signals. This dotted line down the middle effectively is our net zero impact. We have a bunch of different possible strategies over here on the left. More yellow mass to the right means that we've seen a more net positive impact when implementing some of these strategies. A sharp peak, like we see, for instance, with mandatory training, shows confidence in the data. Clear AI policies is number one. This has the largest distribution of mass over to the right. Being very clear about what we can do with this technology, giving time to learn, also very important. To break down some of these top ones, like again, clear AI policy, 90% indicator that this is strong, positive benefit by putting good, clear policies in place.
Shortly right after that one is our giving time to learn. Alleviating displacement worries at 80%. We're going to talk about why this is so important, that as leaders, we make sure that we're very clear and transparent, that we're looking at this technology now as a way to augment individual productivity, not replace engineers. This is a throughput story, not a cost cutting story. There's lots of data to back that up. We want to encourage AI in workflows. For most organizations, generating code is not the bottleneck. There's other bottlenecks throughout the SDLC that we should be looking at and seeing if we can creatively apply AI to help with that. Being very transparent about what we plan to do. Then, yes, offering mandatory training, but not just training where, ok, here's some material and go look at it, and if you don't look at it, you're going to get in trouble or whatever. Actually, being able to tie that to time to experiment in sandboxes and really learn how this technology functions. That's hopefully a lot of what we're getting from this conference.
Distinct Strategies, as Leaders
As leaders, we have some pretty distinct strategies that we can employ. We should, of course, look at integrating across the SDLC. We're going to look at some really interesting use cases that we've uncovered from various companies who have had success deploying agents to deal with real issues in production. We need to unblock usage. Too often I hear, we'd love to use Cursor or some tool, but we're worried about data exfiltration. A lot of work has been done to make sure that it's safer and more compliant to use these tools. There's creative things we can still do, like self-hosting models. We tend to throw giant frontier foundational models at every problem when there's actually a lot of problems we can solve with smaller and even open models. We need to have open discussions about the metrics that we're gathering. We need to be very clear about why we're gathering the metrics in the first place, or else people will just game the system, good old Goodhart's Law.
Then we need to be clear about what we found and what we're going to improve as a result of those findings. We have to reduce the fear of AI. I will show you data. There's tons of data out there suggesting that this technology is not, and may not ever, be ready to fully replace human engineers. There's also plenty of compelling data that talks about how we can augment productivity of engineering organizations. We can get more value out of those engineering organizations.
Companies like Zapier, for instance, which I'll look at later, are actually hiring faster and at a greater volume than they ever have, because they know that they can get a higher return on investment out of a single engineer. I love that attitude. They've actually cranked up hiring as a result of this. Compliance and trust. We do need to be able to trust these outputs. We need to be able to not destroy our change confidence as a result of using this technology. We need to, as leaders, tie this to employee success. We have the opportunity here to help our employees gain new skill sets that are likely to last them for the rest of their career. Really good context engineering. Really good prompt engineering. Understanding how to build agents. These are definitely skills that are going to behoove us for years to come. This tech doesn't seem to be going anywhere.
Reducing the Fear of AI
We need to frame AI as a force multiplier for performance. Something that can augment and accelerate. We need to remind engineers that these tools are not there to replace jobs. They're there to transcend what we could do before. We've known that psychological safety is incredibly important for a long time. A decade ago now, Google launched Project Aristotle, which was a study that tried to figure out like, what are the characteristics of highly performant organizations? What do high-performing organizations have? Named Aristotle because he was famous for saying that the whole is greater than the sum of its parts. They assumed they had a hypothesis that the recipe for really successful teams was going to be some combination of hiring high-performing engineers, having very experienced managers, and having basically unlimited access to compute. All of which were easy for Google to obtain. They were completely wrong.
Overwhelmingly, psychological safety was the most important characteristic for high-performing teams. I think that that really applies now in this climate of a lot of uncertainty, especially amongst junior developers and people just entering the job market, and whether they're going to get replaced with this technology that they're helping to build and train. This is SWE-bench. Who looks at SWE-bench like every day, checking capabilities of models right now? You can't always trust the benchmarks, but this is a decent benchmark site that has a number of different specific benchmarks where certain models are looked at, open and closed models. They're ranked by how well they perform in these benchmarks.
The highest performing benchmark in the most rigorous test is like 44%. In other words, it can complete about 44% of the tasks that are given to it without human in the loop. That doesn't mean without validation. It just means that it's doing the job. That does not an employee replacement strategy make. Those numbers are way too low. It's also very interesting that if you look longitudinally, the highest performer a year and a half ago was at 34%. We were surging at first in our abilities with this stuff. It's definitely starting to taper off. There's plenty of reasons for that. The underlying algorithms for these things really haven't changed since the 1950s. We've just been able to throw a lot more silicon, a lot more compute, get really creative about things like agent-to-agent, RAG, and MCP, and all that stuff. The point is it may never be in a spot to be able to replace humans. It's certainly not there now.
Some of you may be familiar with this more recent study called the GenAI Divide done by the MIT NANDA group. They found that 95% of AI pilots fail in the study that they looked at. There's a lot of investigation happening. General-purpose LLMs are the darker bar here, whereas embedded task-specific, in other words, agentic solutions are in the paler blue. Lots being investigated, lots being piloted, but only 5% of these have been successfully implemented at this point. That's a pretty high failure rate. It doesn't mean that we aren't getting better at this stuff. It just means that we are years off from really looking at this as some sort of cost-cutting engineering replacement strategy. Let's not forget, throughput is the most important component in a high-performing team. Anybody who's familiar with the Theory of Constraints, who read Eli Goldratt's, "The Goal", or if you didn't read The Goal, but maybe you read "The Phoenix Project", which is The Goal, should be familiar with that concept that we shouldn't prioritize cost, we should prioritize throughput. Throughput is the job of the machine of business. We can improve our throughput by applying AI in intelligent ways and increasing the throughput and individual productivity of engineers by using it.
Transparency - Set Clear Intent and Expectations
We need to be really transparent about why we're putting AI strategies in place. We need to frame it, again, as a way to augment, not replace. We need to proactively address these fears. We shouldn't wait as leaders for regrettable attrition or for low productivity because people aren't at their most creative and innovative because they're a little scared. We need to proactively say, here's what we're doing. You're not going to lose your job. Please help us let you learn about this stuff. Let us augment the capabilities of this business. We need to be open about the metrics that we're collecting, why we're collecting them. That this is, again, not for stack ranking based on how great you are with AI, but really more trying to figure out, are these investments, these not insignificant investments that are being made in AI, actually moving the needle? Are they doing what they're supposed to do? That's why we should be collecting these metrics.
If we get into the business of incentivization, or weaponization, or top-down mandates, we end up running smack into something called Goodhart's Law. Who's familiar with Goodhart's Law? A few of you who have looked at productivity theory before. Goodhart's Law says that when a measure becomes a target, it ceases to be a good measure. In other words, we'll game, we'll play to the metric. If I need to do 100% utilization in my company of AI, then a lot of engineers are just going to update their README file on a Monday and call it, yes, I'm using AI. They were not actually moving the needle for productivity.
One of my favorite parables about Goodhart's Law is something called Cobra Effect. Anybody ever heard of the Cobra Effect? A few of you are like me, you're big developer experience productivity nerds. I come from the South. We say if you're studying developer experience, you can't swing a dead cat without coming across Goodhart's Law. Cobra Effect, so you had an emperor. That emperor had a problem with venomous cobras. Decides to come up with an incentivization program. You bring me 100 dead cobras, I'll give you some money. Here we are with a metric that is being incentivized. We need to bring 100 dead cobras and we'll get some money. What do you think people did? People got clever, started farming cobras. That's right. Started farming, slaughtering, and bringing to the emperor, getting their money. The emperor got wind of this gamification, shuts down the program and all those farmers release all those cobras. The problem gets a lot worse. We have to be very clear about why we're collecting these metrics, what we're going to do with them, and not try to focus on some single metric like 100% daily utilization across the company.
Metrics
How do we do that? What should we be looking at? There are a lot of different metrics we can look at. I know a lot of you are familiar with DORA metrics. Who's familiar with SPACE framework? SPACE built on the success of DORA by bringing in additional qualitative metrics, metrics like developer satisfaction, collaboration. What was important was that the authors of that study said that in order to really understand developer experience, we have to look at a constellation of metrics in tension with one another. We have to look at metrics across oppositional dimensions to get a real picture of what's happening with productivity. We can do that with AI.
Our two main throttles are going to be our speed measurements and then our quality and maintainability measurements. We want to make sure that we're balancing any gains that we're getting from higher speed with long-term maintainability and quality. We just want to make sure that we're moving faster without creating a bunch of slop. There are metrics that we can look at. These are oppositional metrics of speed and quality that we can use to determine this. We want to collect metrics in multiple ways. We want to do a mixed-method approach and gather both system metrics, quantitative or hard metrics, as well as qualitative metrics. We want to be able to gather that context. At DX, we like to use a lot of health metaphors, the qualitative metric or the context being, ok, I'm going to the doctor because I don't feel well. Doctor, I don't feel well. Then they take your pulse and they take your oxygen and they take your temperature, and they're like, everything's fine. Yes, but I don't feel well. Something's wrong. We have to have the context of these system metrics that we gather. We want to collect system data. We can get this from admin APIs and things like that, the telemetry metrics that are starting to come out from some of these enterprise solutions.
We also want to be able to conduct periodic surveys. Surveys are hard. We have worked very hard at DX to be able to get most of our customers with an average of 90% or higher participation rates in surveys that are really well engineered, that frame developer experience as much more of a systems problem than a people problem, which it is. That's how we're able to drive more honesty in the qualitative results. Just because you've conducted a survey, you really also need to pay attention to where are there metrics in this survey, where there was an incentive to game the metric, in which case you'll get some dishonest signals, in other words, useless signals. Was the participation rate high enough? Ninety percent or higher is pretty good, but most organizations have difficulty achieving that. They need to be well-engineered surveys. They need to guard against survey fatigue. They need to guard against Goodhart's Law and gamification. You should do experience sampling as well, gathering one or two small bits of data, mixed workflow, and then looking at that data longitudinally.
Really then we have three classes of metrics that we can be looking at for measuring impact. We have our telemetry, again, the data coming out of Copilot API, or Cursor API, or Claude API. This data is really just showing us what's happening, like who's using the tech, maybe how many PRs are being augmented with AI, but it's really just showing us utilization. Again, that doesn't really say much. One hundred percent utilization across the company doesn't tell us anything in terms of real speed or real quality. This is where experience sampling comes in. This is a little bit better for quantifying ROI. This could be something as simple as adding one field to a PR form that says I use AI to work on this PR, or I enjoyed using AI to work on this PR. We gather a small sample of data that we can look at longitudinally.
Then of course our self-reported data, our survey data, but we have to be careful here that we're guarding against survey fatigue, that we're not running these too often. We can only run them periodically as a result of that. Really, you should be running these on a period where however long it takes in your culture to be able to see improvement. If you're not using these metrics to try to improve things, there's no point in gathering the metrics in the first place. The audience for those metrics and what they plan to do with those metrics in terms of improving the state of things for developers, that's a leading indicator of productivity. If you're just throwing stuff up on a dashboard just to put it on a dashboard, you're really like, there's no point. The period for running these surveys really should be the length of time that it tends to take in your culture for positive change or improvements to be enacted and noticed. That way you're always driving metrics up. That gets people excited to see the results. That gets people excited to take part.
We can look across these three different types of metrics. In other words, these AI metrics, our foundational developer experience and developer productivity metrics are still what matter the most. Despite all this hype and everything that's been happening over the last year, year and a half, this is still about improving developer experience and hopefully as a result of that, improving developer productivity. The problem is we as an industry didn't really know how to define those things well even before the AI boom hit. We weren't even really sure exactly what we should be looking at, how we should be defining things. There was a lot of misalignment, especially amongst leaders and individual contributors of what productivity even means.
Then we threw AI at the thing. We hadn't even finished that initial discussion. These AI metrics tell us what's happening, but these core metrics tell us whether these investments are working. Putting this stuff in place, is it actually improving quality or is it making it worse? Are we actually moving faster? Have we increased our throughput? Are we getting more features out to market? Can we respond to the needs of our customers more quickly? These foundational metrics are still what matter the most. These top companies are looking at a few different things, and we worked with a bunch of companies to show the metric framework that I'm about to display after this. We looked for commonality across these companies, what was important to them in terms of the metrics that they were tracking.
Microsoft is looking at adoption. Sure, but you want to use those adoption metrics to correlate them to impact metrics, to create cohorts of users that you can then slice and say, weekly active users of Copilot are showing such and such increase in weighted PR throughput, or such and such increase in PR revert rate, or such and such decrease or increase in change failure rate. That we want to correlate that utilization, and that's exactly what they do. They look at system velocity, developer satisfaction, change failure rate. They have a great metric that I could probably do a whole talk on, but there's a great white paper about it too called, a bad developer day. They gather telemetry from all across the platform and have tried to quantify what makes a bad day for a developer.
If you look at Microsoft Bad Developer Days, there's a whole white paper on it. It's really interesting, but they correlate that metric with the AI utilization metrics that they're gathering. Dropbox, similar stuff. We're looking at adoption and engagement. We're looking at developer sentiment. We're looking at velocity. We're looking at engineering hours saved, percentage of AI code that is generated. That number is somewhere around 23% by our most recent reckoning. Then, Booking.com. Daily active users, time saved per day, PR throughput, developer CSAT, change failure rate, starting to see some patterns here.
Where we found overlap, actually working with closer to 20 companies, we drop them into what we call our DX AI Measurement Framework. If you're familiar at all with the work that DX has done, our last big measurement framework that we introduced was called the Core 4. It is a distillation of DORA, SPACE, and the DevEx metric framework all into one framework called the Core 4. If you're doing Core 4, you're doing DORA, you're doing SPACE, and you're doing DevEx. We very much took that same sort of format and put together these oppositional metrics of utilization, impact, and cost. We prescribed some metrics here based on what we'd seen from other companies. You can use this as both a way to measure how AI is working within the organization and as a bit of a maturity curve.
Most organizations start over on the left with utilization, looking at things like daily active users, weekly active users, percentage of PRs that are AI-assisted, percentage of committed code that's AI-generated, and then overall tasks that have been assigned to agents. We're starting to see more and more creative uses of backend platforms like OpenTelemetry that people can use to push metrics around what agents are actually doing. Then we move from utilization to impact. These are the metrics that really matter. These tell us what's happening in the organization. These are things like AI-driven time savings. We're looking at some Core 4 metrics here, like PR throughput. We use a special PR throughput metric called TrueThroughput, which effectively looks at the overall complexity of the PR that's being put through.
Again, I can't stress enough that you never want to hyper-index or over-index on any one of these single metrics. PR throughput on its own doesn't tell you very much. I can update the README file 10 times a week, my PR throughput could look great. We need to be able to make sure that we understand the complexity and the value of those changes as part of that. Perceived rate of delivery. Code maintainability, there we are again. Change confidence. Change fail percentage. Then, yes, cost. Except I do like to point out that we're about 15 years after the last major hype cycle, and we're still figuring out how to calculate our cloud costs. I also hear that there's people burning through thousands of dollars' worth of tokens a day, so we probably do need to do something. This is, again, the DX AI Measurement Framework. There's more information if you want to look at survey templates. You don't have to use the platform to be able to use this metric set. Happy to talk about how you can calculate a lot of this on your own.
Compliance and Trust
What about compliance and trust? How are we going to be able to trust these outputs coming from this tech? There's actually a lot of levers to pull. I'm going to focus on a couple of the more technical ones. There's obvious stuff too, like testing has never been more important. It's another reason why we have to keep humans in the loop. Even with really cool adversarial validation loops and everything like that, we still need to make sure that our competent humans are the ones who are looking at these things before we actually put them into production. We do also have some interesting levers we can pull.
The first one is creating a feedback loop for your system prompts. Different platforms have different names for the same thing here, like Copilot calls it a system prompt, Cursor calls this Cursor Rules, Claude calls this Agent Markdown. This is effectively just a set of rules that accompanies every prompt that gets fed in to the model that can help guide the way that the model is supposed to act. This is where a lot of people put some guardrails in. We need more than just being able to provide, if we want security guardrails, that goes well beyond just a system prompt, so let's be clear there. This is a good way of making sure that the model is semantically and stylistically accurate with the way that we write code in our organization.
The main takeaway here is to put together the feedback loop. Maintaining the system prompt, applying the system prompt, that's pretty straightforward. What's most important is making sure that there's someone or a group gatekeeping feedback when these models misbehave, when they do something wrong. Whether that's part of your QE team, whether that's part of your AI center of excellence, doesn't really matter. Whether the feedback is gathered through a Slack channel or source control or tickets, doesn't matter. You just need to establish this so that when the models misbehave, there's someone gatekeeping all that feedback, keeping the system prompt up to date and keeping it applied. Lots of good approaches for this. You can see on the right here, very simple example of how the model's been using Spring Boot versions that are too old for the organization, Spring Boot 2.6 or earlier. It's sometimes providing code that has deprecated methods. It's providing code snippets that have syntax errors. We're using a little bit of meta-prompting and we're saying that your new rules are to make sure that you're always providing code snippets that are Spring 3.0 or higher, that you're not sending me code that has syntax errors, that they're syntactically valid.
Then I'm also giving it some meta-prompting about how I want it to behave in terms of its output, every time I want it to provide relevant explanations. If it's uncertain, don't just try to please me like I know you like to do, but instead just give me some methods and approaches. Don't give me bogus code and don't include any references to internal proprietary API. Again, simple system prompt here, but the big takeaway is setting up a feedback loop, making sure that someone's gatekeeping feedback when the model's misbehaved so that you can keep this up to date. It's going to go stale quickly. Rules change all the time. It's important that you have someone accountable for making sure that this stays up to date based on feedback that you're getting.
Determinism and Non-Determinism
Understanding determinism and non-determinism. Especially with agents, you have a lot of opportunity to control what's called the temperature of the prompt and the answer that's coming out of the model. Temperature equals heat equals entropy equals randomness. That's how they've connected dots to that. Effectively, when a token is being decided on for its next output, it doesn't just pick one token. It's got a matrix of tokens that have a probability associated with it.
Then a certain amount of randomness is applied to which token actually gets selected. That randomness is effectively the temperature. You have control over that. A lower temperature means that the model will probably produce more deterministic output. Whereas a higher temperature makes the model "more creative", or that it will explore different paths with the tokens that it's outputting. Also, certainly makes it more error prone. There are times where you may want a more non-deterministic output from the agent of the model, especially like a brainstorming feedback loop or something like that, or content generation. Then when we're doing strict code generation, especially combined with a specific system prompt, we might want a lower determinism here. You can see a very simple example of how this can change outputs. This was done in LM Studio, which is a great place to experiment with temperature and the way that it affects output from models. Similar stuff in Ollama or Docker Model Runner, or any of those platforms that let you run models locally and experiment with them.
In this case, I gave it a low temperature. Because of that selection logic, you want to pick a number between 0 and 1. Don't pick 0, don't pick 1, weird stuff will happen. Some of you have probably played with that already. A decimal somewhere between 0 and 1 is where you want to set your temperature setting. In this case, we set something relatively low, 0.0001. I asked it to create a JavaScript method to render a gradient of colors from blue to red. It didn't give me a JavaScript method, which is fine, but with this low temperature, it gave me the exact same solution in both cases, character for character. It gave me a little HTML block and started manipulating style to start building this.
The actual output obviously goes on a lot further from this slide, this is truncated. Look at what happens when I set a high temperature, so 0.9 in this case. I still only get one JavaScript method here on output B, so it didn't do exactly what I asked. Look at these two solutions. Technically, for what I wanted it to do, rendering the gradient from blue to red, these are both valid solutions. They're just wildly different approaches. On the left, I get an HTML block and I start manipulating style and CSS and all that stuff. On the right, just straight up JavaScript, manipulating a canvas object. Both valid solutions, just much different. You can start seeing where a combination of a system prompt and a decent, appropriate temperature setting can help you get more deterministic or less deterministic, but more closer stylistically and semantically to the use case that you're working on by combining those two things together.
Guardrails - Protect Quality and Trust
Again, guardrails. We want to make sure that we do have clear validation steps, absolutely requiring human review. We need to train not just on how to do good prompt engineering and context engineering and inference pipelines and building agents and all that wonderful stuff, but we also need to teach bias and security training. We need to spot hallucinations. We need to spot biased answers. Then, as I mentioned before, we need to create these feedback loops for making sure that we're able to update our system prompts, gathering feedback from how these models are actually behaving in the wild so we can control them and make them better.
Employee Success - DX GenAI Study Overview
All the data is showing us that engineers that learn to leverage this technology really well are going to outperform those who resist adoption. I'm all about psychological safety, but here's the deal, AI is not coming for your job, but somebody really good at AI might take your job. Using this as a way to increase our skill sets in this emerging technology, and as leaders, encouraging our employees to learn these skill sets and giving them the time and giving them the materials and giving them the safe experimentation beds is giving them an opportunity to learn new skills that will probably benefit them for the rest of their careers. We also remember back from the DORA graph at the beginning there that time to learn was positively associated. We want to provide both education and time to learn.
One of the things that DX did was we put together a prompt engineering guide effectively, but we did it our way. We conducted a study. We interviewed a bunch of S-level, so SVP or higher engineering leaders who had rolled out, at this point, coding assistants to thousands of engineers and were seeing positive impacts to KPIs. We just asked them what they were doing in terms of what best practices they were encouraging and things like that. Then we went directly to engineers. We found engineers that were saving at least an hour a week using this technology, and we asked them to just stack rank their top five most valuable use cases.
Then we put together a guide with coding examples and prompt examples and all of that thing according to what we discovered. It's available for you here, 65-page PDF. Again, goes through what we discovered in this study in terms of high-value use cases and best practices with coding examples and prompting examples. Proud to say that we've had feedback that this has become required reading in certain engineering teams, so hopefully this is one way that we can help drive that employee success and provide some good materials. Lots of great materials out there. I think what I like about this guide is that we didn't just arbitrarily pick some use cases and things. We actually drove the way that we do with studies and research and things like that.
I won't go through the whole study. I think it's really interesting that engineers overwhelmingly picked stack trace analysis as the most valuable use case. I've been writing code professionally since the late '90s. It was a lot of Java code. There was a lot of lines of stack trace, I remember going through line by line. This is just first-class behavior now in the tools like Cursor and agent mode, for instance. If a build breaks, it's going to look at the stack trace. No question that this is a high-value use case. Refactoring existing code. Generating the mid-loop of a function or something. We have to start philosophically asking ourselves, what is toil now? I know that so many of us are like, I became an engineer because I like to write code. I enjoy writing code. Me too. When we're getting paid to write code, and it's like our job, and we have the technology to be able to write that code more effectively, I think we do bear some responsibility to do things as efficiently as we can.
If you're working on a passion project, an open-source project, by all means, write every line of code, if you want to, if you enjoy that. When we're writing code professionally, I think the story is a little bit different. That's the top 10 list that came directly from engineers. We've also found that good utilization of AI according to all these different policies that we've called out has had a significant impact on dev ramp-up. Engineers in general are becoming valuable much more quickly to the organization. We like this metric called time to 10th PR. Again, not in a gamified sense, how quickly can we spit out 10 PRs? It's really more about, how long does it take for a new engineer in a project or in an organization to reach the 10th accepted merged PR? It's an interesting metric for onboarding. We see that we've cut this in half when we're doing a good job with AI in the organization.
Unblock Usage
Unblocking usage. Start where engineers can apply this technology safely. Prioritize the most high impact workflows. Again, remove bottlenecks to experimentation. Think about self-hosted models. We have good infrastructure for this stuff now, like Bedrock and Fireworks AI. We can run smaller open models locally. I've got my little 5080 gaming rig. That thing takes gpt-oss-20b, runs it great. I can do all kinds of interesting things with it. We don't always need to practice on the frontier models, and a lot of times that's like fishing with dynamite. We want to champion a culture of innovation. We want to partner with compliance early, like on day one. We often assume that we're going to get shut down, like we're not allowed to do a thing that we want to do. If you just go talk to the compliance folks, sometimes it's fine. Or sometimes they already have a gateway or something like that that you can use to creatively move around what you thought was an impossible constraint. Think creatively around barriers. Use synthetic datasets. Anonymize data. Do what you can with better prompt engineering to sidestep some of these perceived constraints.
Integrate Across the SDLC
Finally, we want to integrate across the SDLC. Mentioned before, yes, we're saving some time with code generation, but even the most recent DORA report on the State of DevEx says that engineers in scaled organizations still only get maybe five to six hours a week to sit down and actually write code. There are so many other time sinks that they face. Code generation is not usually the bottleneck. An hour saved on something that isn't the bottleneck, it's worthless, according to Eli Goldratt, Theory of Constraints, again. We did this study, this is 135,000 engineers, and we looked at biggest time sinks for them. We compared that to overall annualized AI time savings. This pale bar in the middle is time savings through AI. Not insignificant, it's good. It's like 3.4 hours a week is what we found. Look at what eclipses this: interruption frequency, sources of context switching, meeting heavy days. Or start compounding the other time sinks, like dev environment toil, build and test cycle time.
When we compare those things and we start putting them together, these savings are absolutely being eclipsed by these other areas in the SDLC, these other parts of software development that have nothing to do with writing code. We need to be mindful of that. We need to get creative about that. We need to find the bottleneck and fix the bottleneck. Some companies are doing really well with this. Morgan Stanley has been very open. They have a Wall Street Journal article, a Business Insider article, talking about an agent that they created called DevGen.AI. They have a ton of legacy code laying around: mainframe, natural, COBOL, Perl. I've written a lot of Perl, but apparently, it's legacy now. They have an agent that can look at a bunch of context, look at a bunch of code, and create effectively reverse engineered specs that they can hand directly to developers. It's not a full end-to-end modernization solution, but it's getting rid of a lot of the reverse engineering part of the effort. They're saving almost 300,000 hours annually by eliminating that reverse engineering step.
Zapier, one of my favorite stories. They're already a very automation-heavy culture, but they started opening up effectively a framework, a platform for being able to introduce agents. They can put together agents and have them out and running after just a little bit of testing within a couple of days. They have more bots than humans at Zapier. They've done stuff like reduce daily standups from five times a week down to two times a week, which is impressive. They've moved their onboarding time from 30 minutes down to 2 weeks. They've had some real successes. Like I mentioned before, they're hiring more than they ever have because they know that they can make a single engineer more productive and valuable more quickly, and that they can get anywhere from 10% to 15% greater throughput out of that single engineer. This is the right attitude. We can augment. We can get more out of an individual engineer so we should hire more to increase and unlock more throughput. Canva is using an agent for PRD generation. Project managers can use natural language to get epics and stories into Jira, or prototypes into Figma. That's great on its own, but it's also generating these PRDs in a language that's very friendly to developers based on a lot of context in the organization, which removes another friction point of actually engineers being able to understand what it is that PMs want them to do instead of a lot of back and forth over the feedback that's in that PRD.
Interesting use case there, too. Faire has automated lower sophistication change code reviews like config changes and one-liners and stuff like that, but it still represents about 3,000 PRs a week right now, or code reviews a week. They're just triggering off of GitHub Actions. Then they're putting the feedback directly in the PR comments, right where engineers are. You get instant feedback on your changes and things coming from the agent right there in the PR, which eliminates some of the steps needed in code review. Doesn't eliminate the full review, but a lot of that first pass stuff gets handled by an agent.
Spotify gave us the North Star for DevOps and the early beginnings of platform engineering with the Spotify model. Now they're calling this Spotify 2.0, which is effectively using agents across the SDLC to improve things even more. They've got a lot of great stuff that they're doing, but one thing is with incident management, which is really helping SREs. SREs, often the first few critical minutes of an incident, gathering all the context data, runbook instructions and things like this, can eat up valuable time. Now they just get this information in Slack instantly from an agent when an incident is detected, looking at runbooks and context and things like that. It's helping them with 90% of the incidents at Spotify right now. Hopefully some good food for thought about how we can use agents throughout the SDLC.
Next Steps
Next steps, distribute the AI guide as a reference for integrating AI into development workflows. Determine a method for measuring. Please use oppositional metrics across multiple dimensions, and don't hyper-focus on a single metric or even a single dimension, for instance, utilization. Then track and measure AI adoption and iterate on best practices and use cases. Again, if you're not using the data to continuously improve developer experience, then you're not using it as best as you can. Here's that playbook again.
Questions and Answers
Participant 1: I was just wondering, since you were talking about psychological safety and also ramp-up time to become productive, if you had any wisdom that you found in your findings about early career software engineers who only have like zero or one years of experience and whether the science has anything particular about them, because I know it's a big issue now. They're not being hired as frequently. Wondering if you have a comment on that.
Justin Reock: What's the impact on new engineers, zero to one years of experience? Is there research on this? Yes, in fact, on our website, we have our most recent AI impact report where we look at a lot of the spread between junior engineers and senior engineers and how they're being augmented.
The onboarding is pretty much consistent between both junior and senior engineers in terms of the impact to better onboarding. The curve is really similar. Junior engineers are using the technology more, which is another reason why I think that we should really be treating junior devs as very valuable resources because you're not somebody like me, an OG developer who's been writing code since the '90s. I had to build new muscle to really get used to integrating this stuff and to become reflexive about it in my own workflows. There's still a lot of work that I have to do. There's a lot to unlearn, a lot of calcification that happens when we've been developing for a long time. Junior developers see higher utilization faster. However, over time, senior engineers are actually saving the most time. I do think that it's because just with that experience, you're going to be able to recognize problems with the code and things like that.
Overall, we see benefits to both, but I really think that, especially as a junior, you should be asking these questions. You deserve a good developer experience. You deserve an optimized developer experience. Again, developer experience is a systems problem more than it is a people problem. The engineering leaders that you're interviewing with are the ones that are responsible for giving a good system that makes you do your best work. In the interview process, you want to ask those questions. Like, what is the attitude towards AI adoption? Listen for keywords like augmentation and success and things like that, and listen for a good focus and investment on developer experience, because, ultimately, that's going to reduce your own friction, toil, cognitive fatigue, burnout, and then help you ramp up faster.
See more presentations with transcripts
```

---

## 6. Cloudflare Launches “Artifacts” Beta, Introducing Git-Like Versioning for AI Agents

- 日期: 2026-05-08 12:00
- 链接: https://www.infoq.com/news/2026/05/cloudflare-artifacts-ai-agents/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
Cloudflare has announced the beta release of Artifacts, a new system designed to bring Git-style version control to AI agents, enabling developers to track, manage, and evolve agent-generated outputs with the same rigor as traditional code. The launch addresses a growing challenge in AI development: how to reliably manage the outputs, state, and behavior of increasingly autonomous agents operating in production environments.
Artifacts introduces a structured way to store and version agent outputs, such as generated code, configurations, or intermediate reasoning steps, allowing teams to trace changes, compare versions, and roll back when needed. Much like Git transformed software development, Cloudflare aims to provide similar guarantees for AI-driven workflows, where outputs are often non-deterministic and difficult to reproduce.
As AI agents become more capable, they are increasingly tasked with generating and modifying assets over time. However, unlike traditional software systems, these outputs are often ephemeral, lacking clear lineage or auditability. Artifacts addresses this by creating a persistent, versioned record of agent activity, enabling developers to understand how outputs evolve and ensuring that changes can be reviewed and governed.
The system is particularly relevant for teams building multi-step or autonomous workflows, where agents may iteratively refine outputs or interact with external systems. By capturing each step as a versioned artifact, developers gain visibility into both the final result and the process that produced it, an essential requirement for debugging, compliance, and trust.
Cloudflare positions Artifacts as a foundation for collaborative AI development, where multiple agents and humans can interact with shared outputs. Teams can review changes, enforce policies, and integrate artifact management into existing workflows, bringing AI development closer to established software engineering practices.
This also introduces a layer of governance and accountability, addressing concerns around the unpredictability of AI systems. By making outputs traceable and reversible, Artifacts helps organizations manage risk while still benefiting from the speed and flexibility of agent-driven automation.
The release reflects a broader shift in the industry as AI systems move from isolated tools to stateful, evolving components of production systems. Traditional tooling has struggled to keep up with this shift, particularly when it comes to tracking and managing non-deterministic outputs.
By applying version control principles to AI artifacts, Cloudflare is tackling a key gap in the AI development lifecycle: the lack of reproducibility and control. This is especially critical in enterprise environments, where auditability and compliance are essential.
Artifacts signals an emerging paradigm where AI outputs are treated as first-class assets, requiring the same level of management as source code. As organizations adopt more advanced AI workflows, the need for tooling that supports versioning, collaboration, and governance will only grow.
Other platforms are beginning to address the same problem - bringing structure, versioning, and governance to AI-generated outputs - but approach it from different angles depending on where they sit in the stack.
For example, OpenAI and Anthropic have introduced capabilities within their respective ecosystems (such as tool usage tracking and conversation state management) that allow developers to retain context and replay interactions, but these are typically tied to prompt/response histories rather than full artifact versioning. Similarly, orchestration frameworks like LangChain and LlamaIndex provide ways to persist intermediate steps and workflows, enabling some level of traceability, but they often rely on external storage or logging systems rather than offering a native, Git-like version control model for outputs.
On the more engineering-centric side, platforms such as Weights & Biases and Databricks focus on experiment tracking and data/version lineage, particularly for machine learning models and datasets. While these tools provide strong reproducibility and audit trails, they are typically optimized for model training workflows rather than dynamic, agent-driven output generation.
Cloudflare's Artifacts sits in a slightly different space, closer to software development practices, by treating AI outputs as version-controlled assets, aiming to unify traceability, collaboration, and rollback capabilities in a way that mirrors traditional code workflows but is purpose-built for autonomous agents.
```

---

## 7. Article: Implementing the Sidecar Pattern in Microservices-based ASP.NET Core Applications

- 日期: 2026-05-08 09:00
- 链接: https://www.infoq.com/articles/asp-net-core-side-car/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
Key Takeaways
- The sidecar pattern decouples cross-cutting concerns from the business logic components, thereby enhancing maintainability and reducing complexity.
- Sidecars can be built alongside your microservices, but they can be built using a different technology than the one used to build your microservices.
- Sidecars can be reused across multiple services to provide out-of-the-box support for configuration, logging, tracing, and publish-subscribe messaging.
- The sidecar pattern can help reduce coupling between components and enhance the scalability, maintainability, and efficiency of microservices-based applications without adding complexity.
- While sidecars are well-suited for providing out-of-the-box support for implementing cross-cutting capabilities, you may often prefer not to use them for ultra-latency sensitive workloads to avoid additional network hops and resource overhead.
Today's applications require monitoring, logging, configuration, etc. Each of these concerns can be implemented as a component or a service. These cross-cutting concerns can be tightly integrated into the application. While this tight coupling ensures effective use of shared resources, an outage in any of these components can take your application down. Enter the sidecar design pattern.
The sidecar design pattern helps keep dynamic services (i.e., microservices) fueled with the resources and data they need while keeping them lightweight and free from the burden of carrying large amounts of internal logic. In this article, we'll examine the sidecar design pattern, its benefits, and learn how to implement it in a microservices-based application. We’ll also discuss common issues you typically face with the sidecar and how to mitigate them.
Prerequisites
You should have Visual Studio, ASP.NET Core, and Docker installed in your system to work with the code examples discussed in this article. Note that when you install Visual Studio on your computer, ASP.NET Core can also be installed at the same time using the Visual Studio Installer.
Download Visual Studio and Docker Desktop. You will also need Elastic Search, which we will install from NuGet.
What is Microservices Architecture?
A microservice architecture comprises a conglomeration of services built using disparate languages and technologies. Managing the dependencies for these language-specific interfaces often adds significant complexity. Moreover, because of their dispersed nature, the microservices architecture introduces several challenges.
When building a distributed microservices-based application, addressing cross-cutting concerns such as logging, authentication, and authorization can be challenging. Here is exactly where the sidecar pattern can help.
What is the Sidecar Design Pattern?
The sidecar pattern helps isolate and encapsulate application components by deploying them into a separate process or container. "Sidecar" is the term for this design pattern because it resembles a sidecar connected to a motorbike. Essentially, the sidecar design pattern helps you build applications that comprise disparate components and technologies.
The sidecar design pattern is often implemented using containers, with secondary containers, called "sidecars", running alongside the main application.
These sidecar containers provide additional functionality for your application and manage tasks that do not need to be included in the primary application, such as logging, monitoring, configuration, and security.
Figure 1. Sidecar illustration
The sidecar is coupled to a parent application, has a lifetime analogous to its parent's, and is built and disposed of together with its parent. If you're using the sidecar container alongside your primary container that hosts the ASP.NET Core microservices, the primary container will handle the main business functionality of the application, while the sidecar container manages the auxiliary responsibilities, such as the following:
- Logging
- Monitoring
- Distributed tracing
- Security enforcement
- Service discovery
- Routing traffic
- Communication
Why do we need the Sidecar Design Pattern?
Here are the benefits of the sidecar design pattern at a quick glance:
- Reduces complexity by isolating cross-cutting concerns into distinct components that run independently of the primary application.
- Language-agnostic so you can build it in many different programming languages.
- Reduced code redundancy by including all necessary modules and running alongside the microservices.
- Reduced latency by using localhost/shared networking (although sidecars can introduce some latency compared to in-process solutions).
- Enhanced extensibility by attaching a sidecar as a separate process to the same host or subcontainer, allowing applications to be extended as needed.
Challenges in Implementing Logging in Distributed Applications
In this section, we’ll examine the challenges faced in logging in distributed applications and also understand how the sidecar design pattern can help here.
The Problem: Overhead of Logging in Microservices-Based Applications
Logging is a cross-cutting concern often used in applications to capture and store event records during execution. Logging is more commonly used in distributed applications to monitor application behavior at runtime, capture performance-related metadata, and identify issues.
In a typical microservices-based application, however, logging may introduce significant overhead. For example, due to massive volumes of log data across distributed services and increased resource consumption (e.g., CPU, memory, and network) for log collection, aggregation, and transmission to backend components.
As a result, this increases latency while reducing the application's throughput. Additionally, because microservices are ephemeral, aggregating logs can be more challenging in a dynamic environment. You need a correlation ID to correlate your distributed microservices, but that incurs additional processing.
The Solution: Decoupling the Logging Functionality Using the Sidecar Pattern
The sidecar design pattern can help mitigate the described challenges. It helps isolate concerns, formats data per your application's requirements, and minimizes complexity and code redundancy. Leverage the sidecar design pattern to standardize logging in your application, collect metrics, and monitor its health without altering your main application's codebase.
Implementing Distributed Logging in Microservices Architecture Using the Sidecar Pattern
In this section, we’ll examine how we can implement distributed logging in a microservices-based application and how sidecar containers can help collect and consolidate logs for each microservice. To build this application, we’ll take advantage of the following technologies and tools:
- Visual Studio (IDE)
- ASP.NET Core (a web application development framework)
- C# (Programming Language)
- Docker Desktop for Windows (a containerization tool)
- Elasticsearch (from NuGet)
This application represents a typical inventory management system, and comprises two microservices (i.e., the Transactions API and the sidecar API). While the former acts as a producer, sending log messages, the latter consumes them and then sends them to Elasticsearch.
Note that the Transactions API does not call the sidecar API directly. Instead, the Create action method in the Transactions controller sends the log messages to a concurrent queue, which in turn stores them in a text file residing in a shared folder on the local file system. The sidecar API reads these stored messages from the shared folder, processes them, and then sends them to Elasticsearch.
Here is the complete flow of this application at a glance:
- A client calls the HTTP Post endpoint represented by the Create action method on the TransactionsController.
- Instead of writing to disk or sending the message directly to Elasticsearch, the Create action method adds it to a custom concurrent queue.
- The controller returns the HTTP response immediately; log persistence is offloaded to the background service.
- A background service in the TransactionsAPI uses a thread-safe file logger to persist these messages to a text file in a shared folder.
- In the SidecarAPI, another background service reads these stored log messages from the local file system.
- Finally, the SidecarAPI background service sends the log messages to Elasticsearch.
In this application, we'll create the following types:
TransactionsAPI
- TransactionRequest record
- LogLevels enum
- TransactionType enum
- TransactionsController class
- ISidecarMessageQueue interface
- SidecarMessageQueue class
- ThreadSafeFileLogger class
- IThreadSafeFileLogger interface
- TransactionsBackgroundService class
SidecarAPI
- LogMessage record
- LogsController class
- IElasticSearchClientService interface
- ElasticSearchClientService class
- SidecarBackgroundService class
- SidecarSettings class
A typical inventory management system comprises the following entities: Product, Stock, Transactions, Supplier, Customer, and Orders. For simplicity and brevity, we'll use only a Transaction entity in this example. To implement this application, we'll follow these steps:
- Create a blank solution in Visual Studio
- Create the TransactionsAPI ASP.NET Core Web API project and add it to the solution
- Create the SidecarAPI ASP.NET Core Web API project and add it to the solution
- Create the Dockerfile for both the microservices
- Create the Docker Compose file to run the microservices
- Build and run the docker compose stack
Create an Empty Solution
Launch your Visual Studio IDE and select "Blank Solution" as the project template to create a new empty solution that contains no projects. You can name this empty solution "InventoryManagementSystem".
Create the TransactionAPI and the SidecarAPI Projects
Because we will be using two microservices (TransactionsAPI and SidecarAPI) in this example, you should have separate projects for each. Now, follow the steps outlined below to create two new projects in the solution that correspond to each of these microservices:
- Right-click on the solution in the Solution Explorer window and select "Add -> New project…".
- In the "Add a new project" window, select the option "ASP.NET Core Web API" as the project template.
- Click on "Next"
- In the "Configure your new project" window, specify the project name as TransactionsAPI and the location in your computer where you would like the new project to be saved.
- Click on "Next"
- In the "Additional Information" dialog window, specify the version of the framework to be used.
- Select the checkbox "Enable container support" and specify Linux as the Container OS.
- Lastly, click on "Create"
Repeat the same steps to create the SidecarAPI microservice as well. Figure 2 shows how the Solution Explorer should look:
Figure 2: The Solution Explorer showing both projects
Create the TransactionRequest Entity
Create a new record type named TransactionRequest in a file named TransactionRequest.cs in the TransactionsAPI project. This type will be used to store transaction data in the memory. Replace the default generated code using the following piece of code:
public record TransactionRequest
{
public required int TransactionId { get; init; }
[JsonConverter(typeof(JsonStringEnumConverter))]
public required TransactionType TransactionType { get; init; }
public required DateTime TransactionDate { get; init; }
public required int TransactionQuantity { get; init; }
}
Create the TransactionType Enum
To better organize our source code, you can use an enum to represent transaction type (i.e., pending, dispatched, etc.) as shown in the code snippet given below:
public enum TransactionType
{
Pending,
Dispatched,
Shipped,
Delivered,
Cancelled
}
Create the Transaction Microservice
The TransactionsAPI corresponds to the microservice that processes business transactions and generates logs. For the sake of simplicity, the business processing logic hasn't been provided in this example.
Here is how the TransactionsAPI works:
- The client makes an HTTP POST /api/transactions endpoint, passing the required transaction data.
- The action method corresponding to this endpoint sends or adds the transaction messages to an in-memory queue.
- The TransactionBackgroundService runs at regular intervals of time, dequeues these messages, and stores them in a text file in a shared folder.
Create the Thread Safe File Logger
In the TransactionsAPI microservice, we’ll create a file logger to store messages in a text file. To do this, we’ll create two types, an interface named IThreadSafeFileLogger and a class called ThreadSafeLogger that implements the methods of the interface.
The following code listing shows the IThreadSafeFileLogger interface:
public interface IThreadSafeFileLogger
{
Task SendMessageAsync(string message);
Task SendMessageAsync(string level, string message);
}
The following code listing illustrates how the ThreadSafeFileLogger class takes advantage of semaphore to ensure that the file write operation is thread safe, i.e., no two threads can access the critical section in the SendMessageAsync method concurrently.
public class ThreadSafeFileLogger: IThreadSafeFileLogger
{
private static readonly SemaphoreSlim _semaphore = new(1, 1);
private readonly IConfiguration _configuration;
private readonly string _filePath;
public ThreadSafeFileLogger(IConfiguration configuration)
{
_configuration = configuration;
_filePath = _configuration["ApiKeys:FilePath"] ??
throw new InvalidOperationException("Path to file missing ...");
}
public async Task SendMessageAsync(string message)
{
await _semaphore.WaitAsync();
try
{
await File.AppendAllTextAsync(_filePath,
$"{Guid.NewGuid().ToString()} | {message}{Environment.NewLine}");
}
finally
{
_semaphore.Release();
}
}
public async Task SendMessageAsync(string level, string message)
{
await _semaphore.WaitAsync();
try
{
await File.AppendAllTextAsync(_filePath,
$"{Guid.NewGuid().ToString()} | {level} | {message}{Environment.NewLine}");
}
finally
{
_semaphore.Release();
}
}
}
Create a Background Service in the TransactionsAPI Microservice
In the TransactionsAPI microservice, the TransactionBackgroundService class extends the BackgroundService class and implements the ExecuteAsync method. This method would be called at regular intervals, as shown in the following piece of code:
public class TransactionsBackgroundService : BackgroundService
{
private readonly TimeSpan _period = TimeSpan.FromSeconds(5);
private readonly ILogger<TransactionsBackgroundService> _logger;
private readonly IServiceProvider _serviceProvider;
public TransactionsBackgroundService(ILogger<TransactionsBackgroundService> logger, IServiceProvider serviceProvider)
{
_logger = logger;
_serviceProvider = serviceProvider;
}
protected override async Task ExecuteAsync(CancellationToken stoppingToken)
{
using PeriodicTimer timer = new PeriodicTimer(_period);
using IServiceScope scope = _serviceProvider.CreateScope();
var _transactionsMessageQueue = scope.ServiceProvider.GetRequiredService<ISidecarMessageQueue>();
var threadSafeFileLogger = scope.ServiceProvider.GetRequiredService<IThreadSafeFileLogger>();
while (!stoppingToken.IsCancellationRequested &&
await timer.WaitForNextTickAsync(stoppingToken))
{
_logger.LogInformation("Executing PeriodicBackgroundTask");
while (_transactionsMessageQueue.Count > 0)
{
string message = await _transactionsMessageQueue.Dequeue();
await threadSafeFileLogger.SendMessageAsync(message);
}
}
}
}
Create the Sidecar Message Queue in the TransactionsAPI Microservice
We'll also create a custom message queue in the TransactionsAPI microservice project to store log messages generated by the Transactions Controller. The following code listing shows the ISidecarMessageQueue interface that contains the declaration of the Enqueue and Dequeue methods.
public interface ISidecarMessageQueue
{
int Count { get; }
Task Enqueue(string level, string message);
Task<string> Dequeue();
Task ClearAsync();
}
The SidecarMessageQueue class implements this interface as shown in the following piece of code:
public sealed class SidecarMessageQueue: ISidecarMessageQueue
{
private readonly ConcurrentQueue<string> queue = new ConcurrentQueue<string>();
public async Task Enqueue(string level, string message)
{
string str = await BuildMessage(level, message);
queue.Enqueue(str);
}
public async Task<string> Dequeue()
{
if(queue.TryDequeue(out string? message))
{
return message;
}
return string.Empty;
}
private async Task<string> BuildMessage(string level, string message)
{
return $"{level} | {message}{Environment.NewLine}";
}
public int Count => queue.Count;
public async Task ClearAsync()
{
while (queue.TryDequeue(out _)) { }
}
}
Note that in the preceding code listing, although the BuildMessage method does not perform any asynchronous work, the async keyword has been used here intentionally for future extensibility.
Next, add a new API controller named TransactionsController and write the following piece of code in there to replace the auto-generated code:
[ApiController]
[Route("api/[controller]")]
public class TransactionsController : ControllerBase
{
private readonly ISidecarMessageQueue _transactionsMessageQueue;
public TransactionsController(ISidecarMessageQueue transactionsMessageQueue)
{
_transactionsMessageQueue = transactionsMessageQueue;
}
[HttpPost]
public async Task<ActionResult> Create([FromBody]
TransactionRequest transactionRequest)
{
if (transactionRequest.TransactionId <= 0)
{
await _transactionsMessageQueue.Enqueue(LogLevel.Error.ToString(),
"Transaction Id must be > 0.");
return BadRequest();
}
if (transactionRequest.TransactionQuantity <= 0)
{
await _transactionsMessageQueue.Enqueue(LogLevel.Error.ToString(),
"Transaction Quantity must be > 0.");
return BadRequest();
}
bool isTransactionTypeValid = Enum.IsDefined(typeof(TransactionType),
transactionRequest.TransactionType);
if (!isTransactionTypeValid)
{
await _transactionsMessageQueue.Enqueue(LogLevel.Error.ToString(),
$"{transactionRequest.TransactionType} " +
$"is an invalid transaction type");
return BadRequest();
}
await _transactionsMessageQueue.Enqueue(LogLevel.Information.ToString(),
$"Created a new transaction record having transaction Id: " +
$"{transactionRequest.TransactionId}");
return Ok(new
{
success = true,
data = transactionRequest,
id = transactionRequest.TransactionId
});
}
}
As shown in the preceding code snippet, the TransactionsController class contains one HttpPost action method. The HttpPost action method accepts a reference to an instance of TransactionRequest record type as a parameter from the request body and is used to create a new transaction. The method also validates incoming data and sends log messages to the message queue.
The complete source code of the TransactionsController class is available in the source code repository.
Create the Sidecar Microservice
The SidecarAPI microservice reads the application logs stored in the shared folder and forwards them to Elasticsearch. The SidecarAPI also provides a HTTP GET endpoint to query the logs stored in Elasticsearch.
Here is how the SidecarAPI works:
- The SidecarBackgroundService polls the log file at regular intervals (i.e., every five seconds as configured in this example).
- The SidecarBackgroundService parses the log text one line at a time.
- The SidecarBackgroundService uses the ElasticSearchClientService to send these logs to Elasticsearch.
Instead of this implementation of the sidecar pattern, you could use the Distributed Application Runtime (Dapr) to handle cross‑cutting concerns. Dapr is an open-source, event-driven runtime that can be used to implement the sidecar pattern in distributed cloud-native applications using any language and runtime.
Create a new record type named LogMessage in a file named LogMessage.cs in the SidecarAPI project to store log metadata, such as log message, log level, and the timestamp, as shown below:
public record LogMessage
{
public required string Id { get; init; }
public required DateTime Timestamp { get; init; }
public required string Message { get; init; }
}
Next, create a new API controller named LogsController and replace the auto-generated code using the following piece of code:
using Microsoft.AspNetCore.Mvc;
using SidecarApi.Services;
[ApiController]
[Route("api/[controller]")]
public class LogsController : ControllerBase
{
private readonly IElasticSearchClientService _elasticSearchClientService;
private readonly ILogger<LogsController> _logger;
public LogsController(IElasticSearchClientService elasticSearchClientService,
ILogger<LogsController> logger)
{
_elasticSearchClientService = elasticSearchClientService;
_logger = logger;
}
[HttpGet]
public async Task<ActionResult<List<LogMessage>>> Get()
{
try
{
var logs = await _elasticSearchClientService.GetAllLogsAsync();
return Ok(logs.ToList());
}
catch (Exception ex)
{
_logger.LogError(ex, "Failed to fetch logs from Elasticsearch");
return StatusCode(500);
}
}
}
In this example, we have used a custom file logger to log data to a text file. A better alternative would be to use Serilog, an open-source framework used to implement structured logging. By implementing structured logging in this application, the process of querying the data will be simplified. You can also leverage OpenTelemetry to implement observability by emitting traces and metrics and shipping them via a collector to Elasticsearch.
The LogsController contains only one HTTP GET action method. This action method can be used to retrieve all log records stored in Elasticsearch. The complete source code of the LogsController class is available in the source code repository.
Create the SidecarBackgroundService
In the SidecarAPI microservice, we'll consume the messages stored in the shared folder. The following code listing shows the SidecarBackgroundService class that extends the BackgroundService class and implements the ExecuteAsync method, which will execute at pre-defined intervals (every five seconds in this example).
The following code listing shows the SidecarBackgroundService class:
public class SidecarBackgroundService : BackgroundService
{
private readonly TimeSpan _period = TimeSpan.FromSeconds(5);
private readonly IServiceProvider _serviceProvider;
private readonly ILogger<SidecarBackgroundService> _logger;
private readonly IOptions<SidecarSettings> _settings;
private readonly ConcurrentQueue<string> logs = new ConcurrentQueue<string>();
private readonly int _maxBatchSize;
private readonly int _maxCacheDurationInMinutes;
private readonly IMemoryCache _cache;
public SidecarBackgroundService(
ILogger<SidecarBackgroundService> logger, IServiceProvider serviceProvider,
IOptions<SidecarSettings> settings, IMemoryCache cache)
{
_logger = logger;
_serviceProvider = serviceProvider;
_settings = settings;
_maxBatchSize = settings.Value.MaxBatchSize;
_maxCacheDurationInMinutes =
settings.Value.MaxCacheDurationInMinutes;
_cache = cache;
}
protected override async Task ExecuteAsync(CancellationToken stoppingToken)
{
using var timer = new PeriodicTimer(_period);
_logger.LogInformation($"LogShipper started. Monitoring {_settings.Value.LogDirectory}");
while (!stoppingToken.IsCancellationRequested &&
await timer.WaitForNextTickAsync(stoppingToken))
{
await SendMessagesToElasticAsync(stoppingToken);
}
}
private async Task SendMessagesToElasticAsync(CancellationToken cancellationToken)
{
var directory = _settings.Value.LogDirectory;
var logFilePattern = _settings.Value.LogFilePattern;
if (string.IsNullOrWhiteSpace(directory) || string.IsNullOrWhiteSpace(logFilePattern)) return;
if (!Directory.Exists(directory)) return;
var files = Directory.GetFiles(directory, logFilePattern);
foreach (var fileName in files)
{
await using var stream = new FileStream(fileName, FileMode.Open,
FileAccess.Read, FileShare.ReadWrite);
using var reader = new StreamReader(stream);
string? text;
using IServiceScope scope = _serviceProvider.CreateScope();
var _elasticSearchClient = scope.ServiceProvider.GetRequiredService<IElasticSearchClientService>();
while ((text = await reader.ReadLineAsync(cancellationToken)) != null)
{
if (string.IsNullOrWhiteSpace(text))
continue;
string[] message = text.Split('|');
string messageKey = message[0].Trim();
if (!_cache.TryGetValue(messageKey, out _))
{
logs.Enqueue(text);
if (logs.Count > _maxBatchSize)
{
while (logs.TryDequeue(out string? str))
{
string[] data = str.Split('|');
string key = data[0].Trim();
LogMessage logMessage = new LogMessage()
{
Id = data[0].Trim(),
Timestamp = DateTime.UtcNow,
Message = str.Substring(data[0].Length + 1).Trim()
};
await _elasticSearchClient.IndexAsync
(logMessage, cancellationToken);
var cacheEntryOptions = new MemoryCacheEntryOptions() .SetSlidingExpiration(
TimeSpan.FromMinutes(_maxCacheDurationInMinutes));
_cache.Set(messageKey, true, cacheEntryOptions);
}
}
}
}
}
}
}
To enable support for in-memory caching in the SidecarAPI, add the following piece of code in the Program.cs file:
builder.Services.AddMemoryCache();
Create the Elasticsearch Client Service
In the SidecarAPI project, the IElasticSearchClientService interface defines a clear abstraction for all Elasticsearch-related operations, such as indexing and querying documents. The ElasticSearchClientService class implements this interface and encapsulates how the application interacts with Elasticsearch.
Create a new interface named IElasticSearchClientService in a file having the same name and replace the default generated code with the following piece of code:
public interface IElasticSearchClientService
{
Task IndexAsync(LogMessage logMessage, CancellationToken ct);
Task IndexBatchAsync(List<LogMessage> entries, CancellationToken ct);
Task<List<LogMessage>> GetAllLogsAsync();
Task DeleteAsyncRequest();
}
Next, create a new class named ElasticSearchClientService that implements the IElasticSearchClientService as shown in the code listing given below:
public class ElasticSearchClientService: IElasticSearchClientService
{
private readonly ILogger<ElasticSearchClientService> _logger;
private readonly ElasticsearchClient _elasticSearchClient;
private readonly ElasticsearchClientSettings _elasticSearchClientSettings;
public ElasticSearchClientService(
ILogger<ElasticSearchClientService> logger,
IOptions<SidecarSettings> settings)
{
_logger = logger;
_elasticSearchClientSettings = new ElasticsearchClientSettings(
new Uri(settings.Value.Elasticsearch.Url))
.Authentication(
new BasicAuthentication(
settings.Value.Elasticsearch.Username,
settings.Value.Elasticsearch.Password));
_elasticSearchClient = new ElasticsearchClient(_elasticSearchClientSettings);
}
public async Task DeleteAsyncRequest()
{
var today = DateTime.UtcNow.ToString("yyyy.MM.dd");
var indexName = $"application-logs-{today}";
var response = await _elasticSearchClient.Indices.DeleteAsync(indexName);
}
public async Task<List<LogMessage>> GetAllLogsAsync()
{
var today = DateTime.UtcNow.ToString("yyyy.MM.dd");
var indexName = $"application-logs-{today}";
var searchResponse = await _elasticSearchClient.SearchAsync<LogMessage>(
s => s.Indices(indexName).Query(q => q.MatchAll()));
return searchResponse.IsValidResponse ? searchResponse.Documents?.ToList() ??
new List<LogMessage>() : new List<LogMessage>();
}
public async Task IndexAsync(LogMessage logMessage, CancellationToken ct)
{
var today = DateTime.UtcNow.ToString("yyyy.MM.dd");
var indexName = $"application-logs-{today}";
var existsResponse = await _elasticSearchClient.Indices.ExistsAsync(indexName, ct);
if (!existsResponse.Exists)
{
var createResponse = await _elasticSearchClient.Indices.CreateAsync(indexName);
if (!createResponse.IsValidResponse)
{
_logger.LogError("Failed to create index: {Error}", createResponse.DebugInformation);
throw new Exception(createResponse.DebugInformation);
}
}
var indexResponse =
await _elasticSearchClient.IndexAsync(logMessage, idx => idx.Index(indexName));
if (!indexResponse.IsValidResponse)
{
throw new Exception(indexResponse.DebugInformation);
}
}
public async Task IndexBatchAsync(List<LogMessage> entries, CancellationToken ct)
{
if (entries.Count == 0) return;
var today = DateTime.UtcNow.ToString("yyyy.MM.dd");
var indexName = $"application-logs-{today}";
var bulkRequest = new BulkRequest(indexName)
{
Operations = new List<IBulkOperation>()
};
foreach (var entry in entries)
{
bulkRequest.Operations.Add(new BulkIndexOperation<LogMessage>(entry));
}
var response = await _elasticSearchClient.BulkAsync(bulkRequest, ct);
if (!response.IsValidResponse)
{
_logger.LogError("Failed to index logs: {Error}", response.DebugInformation);
throw new Exception($"Elasticsearch error: {response.DebugInformation}");
}
_logger.LogInformation("Indexed {Count} logs to {Index}", entries.Count, indexName);
}
}
Configure the TransactionsAPI
You should register the dependencies of the TransactionsAPI in the Program.cs file as shown in the code snippet given below:
using System.Text.Json.Serialization;
using TransactionsAPI;
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<IThreadSafeFileLogger, ThreadSafeFileLogger>();
builder.Services.AddSingleton<ISidecarMessageQueue, SidecarMessageQueue>();
builder.Services.AddHostedService<TransactionsBackgroundService>();
builder.Services.AddControllers().AddJsonOptions(options =>
{
options.JsonSerializerOptions.Converters.Add(new JsonStringEnumConverter());
});
var app = builder.Build();
app.MapControllers();
app.Run();
The following code snippet shows how you can specify the sidecar configuration metadata in the appsettings.json file of the SidecarAPI project:
"Sidecar": {
"LogDirectory": "/app/logs",
"LogFilePattern": "xapi.log",
"MaxBatchSize": 5,
"MaxCacheEntries": 5,
"Elasticsearch": {
"Url": "http://elasticsearch:9200",
"Username": "elastic",
"Password": "changeme"
}
}
Configure the SidecarAPI
The complete source code of the Program.cs file of the SidecarAPI is given below:
using SidecarApi;
using SidecarApi.Services;
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddMemoryCache();
builder.Services.Configure<SidecarSettings>(
builder.Configuration.GetSection("Sidecar"));
builder.Services.AddScoped
<IElasticSearchClientService, ElasticSearchClientService>();
builder.Services.AddHostedService<SidecarBackgroundService>();
builder.Services.AddControllers();
var app = builder.Build();
app.MapControllers();
app.Run();
Use Containerization
You should take advantage of containers when implementing sidecar design for better isolation, modularity, and reusability. Although the application and the sidecar containers are isolated, they share the same lifecycle, network, and often the same storage as well.
Figure 3: The Application and the sidecar containers in execution
Dockerize the services
You should dockerize both the services by creating a Dockerfile in both the projects we created earlier, i.e., the TransactionsAPI and SidecarAPI. Since you’ve opted for containerization support when creating the two projects, a Docker file will be created in each of them by default.
Here's the source code of the Dockerfile of the SidecarAPI service (i.e., the sidecar).
FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS base
RUN mkdir -p /app/logs && chmod 750 /app/logs
USER $APP_UID
WORKDIR /app
EXPOSE 8081
# This stage is used to build the service project
FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src
COPY ["SidecarApi/SidecarApi.csproj", "SidecarApi/"]
RUN dotnet restore "./SidecarApi/SidecarApi.csproj"
COPY . .
WORKDIR "/src/SidecarApi"
RUN dotnet build "./SidecarApi.csproj" -c $BUILD_CONFIGURATION -o /app/build
# This stage is used to publish the service project to be copied to the final stage
FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "./SidecarApi.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false
# This stage is used in production or when running from VS in regular mode (Default when not using the Debug configuration)
FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SidecarApi.dll"]
The Dockerfile of the Transactions microservice should have the following piece of code:
FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS base
RUN mkdir -p /app/logs && chmod 750 /app/logs # Linux permission
USER $APP_UID
WORKDIR /app
EXPOSE 8080
# This stage is used to build the service project
FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
RUN mkdir -p /app/logs && chmod 750 /app/logs
ARG BUILD_CONFIGURATION=Release
WORKDIR /src
COPY ["TransactionsApi/TransactionsApi.csproj", "TransactionsApi/"]
RUN dotnet restore "./TransactionsApi/TransactionsApi.csproj"
COPY . .
WORKDIR "/src/TransactionsApi"
RUN dotnet build "./TransactionsApi.csproj" -c $BUILD_CONFIGURATION -o /app/build
# This stage is used to publish the service project to be copied to the final stage
FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "./TransactionsApi.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false
# This stage is used in production or when running from VS in regular mode (Default when not using the Debug configuration)
FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "TransactionsApi.dll"]
Docker File and Docker Compose File
A Docker Compose file is a YAML-based configuration file enabling you to declaratively specify how to run multiple containers cohesively. You can use it to configure all your services, networks, and volumes in a single file, instead of running multiple Docker commands to run your Docker containers.
While a Docker file helps you configure and build individual images in an application, a Docker Compose file defines how multiple images can run together cohesively as services in a multi-container application. Docker Compose helps streamline containerised applications. It gives you more granular and simplified control over your containers, makes collaboration and development much more efficient, and lets your applications run easily in whatever environment you need. Essentially, using Docker Compose is a great way to configure all the interdependent services your application needs (databases, message queues, caches, web service APIs, etc.) in a single file. You can then spin up one or more containers with a single command using the Docker Compose command-line tool.
Create the Docker Compose file
To deploy both the containers at the same time, you should create a docker-compose.yml file with the following content inside:
services:
services:
elasticsearch:
image: docker.elastic.co/elasticsearch/elasticsearch:8.15.1
container_name: elasticsearch
environment:
- discovery.type=single-node
- xpack.security.enabled=false
- "ES_JAVA_OPTS=-Xms1g -Xmx1g"
ports:
- "9200:9200"
volumes:
- esdata:/usr/share/elasticsearch/data
networks:
- app-network
healthcheck:
test: ["CMD-SHELL", "curl -f http://localhost:9200/_cluster/health || exit 1"]
interval: 30s
timeout: 10s
retries: 5
start_period: 40s
transactions-api:
build:
context: .
dockerfile: TransactionsApi/Dockerfile
container_name: transactions-api
ports:
- "8080:8080"
environment:
- ASPNETCORE_ENVIRONMENT=Development
- ASPNETCORE_URLS=http://+:8080
volumes:
- ./logs:/app/logs
networks:
- app-network
depends_on:
elasticsearch:
condition: service_healthy
sidecar-api:
build:
context: .
dockerfile: SidecarApi/Dockerfile
container_name: sidecar-api
ports:
- "8081:8081"
environment:
- ASPNETCORE_ENVIRONMENT=Development
- ASPNETCORE_URLS=http://+:8081
volumes:
- ./logs:/app/logs
networks:
- app-network
depends_on:
elasticsearch:
condition: service_healthy
networks:
app-network:
driver: bridge
volumes:
esdata:
Securing the Endpoints
The following code snippet shows how you can add health checks for Elasticsearch in the Program.cs file:
builder.Services
.AddHealthChecks()
.AddCheck<ElasticHealthCheck>("elasticsearch");
You can also use the authentication and authorization provided by the ASP.NET Core to secure the endpoints, as shown below.
[Authorize(Policy = "ReadOnly")]
[HttpGet]
public async Task<ActionResult<List<LogMessage>>> Get()
{
//Code omitted for brevity
}
[Authorize(Policy = "CanDelete")]
[HttpDelete]
public async Task Delete()
{
//Code omitted for brevity
}
We've skipped all this in this example because of simplicity and brevity.
Run the application
Finally, run the Docker Compose file using the following piece of code:
docker-compose up –build
Figure 4 shows the Docker Compose command in execution.
Figure 4: The Docker Compose command in execution
When the TransactionsAPI microservice is in execution, it will generate log messages and then send them to an in-memory collection. A background service will then store these messages in a text file residing in a shared folder. Figure 5 shows how you can invoke the Transactions microservice using Postman.
Incidentally, Postman is a popular API platform used for building, testing, and managing APIs.
Figure 5: Invoking the Create endpoint of the Transactions microservice using Postman
The sidecar microservice will then read the log messages from the text file residing in the shared folder and send them to Elasticsearch.
You can retrieve the logs stored in Elasticsearch by calling the HTTP Get endpoint of the logs controller pertaining to the sidecar microservice, as shown in Figure 6.
Figure 6: Displaying the saved messages in Elasticsearch
Using Kubernetes Pods
You can improve this implementation by using Kubernetes, which can serve as a "runtime fabric" to make it scalable, resilient, and operable in production for your distributed, cloud-native applications. In this implementation, the two microservices, TransactionsAPI and SidecarAPI, will run on separate containers on the same network. They communicate over network addresses and share volumes via bind mounts.
While this will work, an ideal choice here will be an implementation of the sidecar pattern using Kubernetes pods. It should be noted here that the true sidecar pattern resides in Kubernetes Pods, where containers share localhost networking and volumes.
Performance and Scalability Considerations
It should be noted that this implementation adds certain performance and latency overheads. For example, the file I/O operations in the TransactionsAPI service will add an additional overhead because of read and write operations from and to the disk. You should also avoid recreating the indexes every time.
Instead, you can create the index once at startup. You can also send messages to Elasticsearch in a batch IndexBatchAsync to write the messages in a batch thereby improving performance. Lastly, you can use OpenTelemetry in this application to aggressively capture metrics and then analyze them as needed.
Selecting the Right Approach to Implement the Sidecar Pattern
You can implement the sidecar pattern in several ways:
- Custom
A custom sidecar is a good choice when you want a simple approach with total control and flexibility in your sidecar implementation without requiring any external dependencies. - Dapr
Distributed Application Runtime (Dapr), helps you to implement the sidecar pattern with features such as, service-to-service communication, maintain state, and process events in a distributed application environment. This approach will eliminate the need to write your own custom code so you can focus on delivering business value rather than writing boilerplate code. - Serilog with the Elasticsearch sink
This is a good choice if your application is built using .NET and you want to directly manage the structure and format of your logs as well as write them directly to Elasticsearch without the need of an intermediary log aggregator agent. - stdout and the Kubernetes DaemonSet
You can also implement the sidecar pattern using stdout and the Kubernetes DaemonSet which can be useful as a simple, resource efficient technique in small to medium sized cluster environments. A daemonset guarantees that a particular pod runs on each node in a Kubernetes cluster.
The Sidecar Pattern is a Kubernetes Construct
The sidecar pattern is fundamentally a Kubernetes native concept where containers share the same Pod, localhost, and lifecycle. The Docker Compose example is only a useful approximation for local development, but Kubernetes is actually the canonical implementation of the sidecar pattern, while Docker Compose is used only as a local development approach.
Conclusion
Although there are several benefits, the sidecar design pattern, like any software pattern, is only useful when it is correctly implemented. You can extend the application discussed in this article to illustrate how the sidecar container can collect and consolidate logs and monitoring metrics for each microservice, improving the manageability, usability, performance, and functionality of the microservices, and also detecting and troubleshooting runtime issues.
```

---

## 8. Podcast: The AI Joy Gap: Why Some Developers Thrive While Others Struggle

- 日期: 2026-05-08 09:00
- 链接: https://www.infoq.com/podcasts/some-developers-thrive-while-others-struggle/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
In this podcast, Shane Hastie, Lead Editor for Culture & Methods, spoke to Michael Parker, VP of Engineering at TurinTech AI, about bringing joy back to software development in the AI era, the emerging role of "factory architects" who orchestrate AI agents rather than write code directly, and the cultural divide between AI hype and the reality developers face on legacy codebases.
Key Takeaways
- AI is creating a polarization in developer experience - those on greenfield projects see massive productivity gains while those on legacy codebases struggle with AI-generated code that doesn't fit their context.
- Developers are becoming "factory architects" who design and orchestrate AI agents and rules rather than writing code directly, requiring a new mindset and skill set.
- Some high-performing teams are returning to mob programming because team synchronization has become more important than individual code generation speed.
- There is a growing cultural disconnect between engineering leadership who believe the AI hype and developers on the ground who face real limitations with their codebases and tooling.
- As engineering productivity increases, the bottleneck shifts to product discovery — organisations will need faster decision-making processes and more product managers and researchers.
Subscribe on:
Transcript
Shane Hastie: This is Shane Hastie for the InfoQ Engineering Culture Podcast. Today, I'm sitting down half the world away with Mike Parker. Mike, welcome. Thanks for taking the time to talk to us.
Michael Parker: Hi, Shane.
Shane Hastie: My normal starting point in these conversations is, who's Mike?
Introductions [01:12]
Michael Parker: Yes, so I'm the VP of engineering here at TurinTech AI. So, we're a London-based cloud development platform company. We're trying to build a system to bring the joy back into development, and I've been doing that for the last year. Before that, I was at Docker for seven years. So, building out Docker Hub, Docker Desktop, Docker Scout, lots of broad scale developer tools. I'm very interested in developer tools. Before that, I was a backend engineer interested in test-driven development and clean code and all that sort of fun stuff before moving into management. And even before that, I was in game design.
So, I started off in games as a young boy, very keen on building those kinds of things. But now today, I'm very interested in the future of AI tooling and accelerating developers and bringing that joy back into development.
Where Has the Joy Gone in Development? [02:04]
Shane Hastie: So, let's dig into that. Joy back into development. Where has the joy gone? What's happened?
Michael Parker: Yes, it's a really interesting question, and it really depends who you talk to. Some developers are having even more fun than they've ever had, especially if they're working on greenfield code bases, shipping small products, small services, where AI is supercharging their productivity. But there's also a lot of developers that are working on legacy code bases in large enterprises. They might have a lot of in house libraries. They might have ways of working that AI is not necessarily trained on. And getting AI to output code in those environments is very difficult.
And we're almost seeing a polarization of opinion in this space because software development is so varied and a lot of people tend to talk about software development as if it's just one space and it's not. And so, you've got people on the greenfield side saying, "Wow, AI is amazing. You can get 10,000 times productivity increase". And then you've got people on very complicated legacy code bases, locked to old technologies. The AI is just churning out garbage. And these people are not talking enough. I want people to talk more and understand that there's different code bases, there's different companies.
So, I'm mostly focused on the people that are suffering. These code bases where AI doesn't work, how do we make it work better? And to a lot of these developers, what they're finding is that AI has taken over the fun part. And the fun part is a lot of the time deciding on the structure of the code, the architecture, getting things right. And instead we're left with code review. No one likes doing code review. And so, we're sitting there, AI generates some code, it's not right. We review it for ages. We tell it, no, you've done this wrong, you've done that wrong. We write rules, files. They don't listen to the rules.
We try a different model. We try a different package, and then we have to go through all this pain. And often people say it would've been quicker to do it myself and it would've been higher quality. And you're stuck like, "Do I use the new tools?" And especially when your engineering leaders are pushing these things down, they say, everyone has to use AI. And then the developers on the ground are struggling because they can't teach these things to do a good job. And so, I think that's where a lot of the joy has gone.
Making AI Work for Enterprise Developers [04:29]
Shane Hastie: So, for the engineer and the large enterprise that joy is being sucked out of, and you're right, code reviews is the last thing we actually enjoy doing as developers. We want the thrill of the creativity and so forth. How do we make this work?
Michael Parker: I think there's two aspects to this. I think that we need better tools to help AI produce the right code first time round. A lot of the cutting edge AI developers are essentially building their own factory. They're building their own AI agents. A lot of the AI tools today, like Claude Code and Cursor, Copilot, they have huge configurability. You can use subagents, you can use rules, and your rules can set up more subagents, and you can have MCP servers, and you can do prompt engineering. It's kind of a new role. You're not writing the code anymore. You're writing the factory to write the code.
And there's an emerging class of experts who have become expert in building their local factory, their own agents, their own rules, et cetera, et cetera. But very often these things aren't widely shared amongst their team. And so, you have this huge imbalance with some of the AI experts. And then how do you spread that joy to the team? How do you get them upskilling everybody else rather than having their own sort of personal productivity factory? But I'm not convinced that planning more ahead of time before it runs off and writes code is enough.
It's definitely more that we could do there, out of the box, to provide tools, so that you really check what AI is going to do before it does it. And that's helped me immensely. I'm sort of on this side of building the factory, right? So, I've got my own home set up and I'm tweaking my rules and my agents and I'm very clear, don't do anything. Let's decide. Tell me what you're going to do first. And so, I think that's one aspect of it. It's like really nailing the requirements, the technologies, the structure before you write any code. So, better planning tools is number one.
But also when it's finished, I think we need better code review tooling. Our code review tooling isn't really designed for the quantity of code that AI is churning out. It's very hard to say, why did you do this? Why did you do that? Can you move that over here? The whole review interface, I think, needs an update for this AI era. And I think that's true across the board for the full SDLC, by the way. A lot of these things need completely redesigning, including the IDE. But then after code review, even after your code is merged, today's code is going to be out of date tomorrow.
There's always going to be maintenance work and you probably have lots of legacy code. So, we need some systems to keep this code maintained over time. Is it going to be the developers that are doing that? And I speak to a lot of developers, they have a huge amount of maintenance work to do, and this is really boring work. No one wants to upgrade your Python version or your .Net framework or, "Oh, this thing has been deprecated. Oh, I need an extra parameter on this field". And LLMs aren't necessarily trained on every single version of every library.
And if something came out like yesterday, like .Net 10 was released recently and many LLMs are still like, ".Net 10 doesn't exist". I'm like, "Yes, it came out. I need to switch to. .Net 10". So, I think at the end, we need better maintenance agents and tooling to help take away that burden from developers so they can focus on the creativity and the problem solving and building business value and getting back to what I consider the fun part of development and not so much upgrading framework versions or doing code review.
The Pull Request Problem in the AI Era [08:19]
Shane Hastie: One of the things that we hear a lot is that as we generate code using the LLMs, the pull requests are getting bigger, the quantity of code. Now we've spent decades trying to get to smaller, tighter pieces, microservices, time-driven design, make it small, make it tight. Have we broken there?
Michael Parker: Yes, I think we have. And it's an interesting question. Would you rather have one pull request with a hundred changes or a hundred poll requests with one change? When I was writing code, not so much anymore, but I would always open lots of small pull requests and even small refactorings. If I was doing a bug fix and I knew there was some refactoring to do, I would roll back, I would do the refactoring, I would open a pull request, then I would do the bug fix, open a second pull request. And so, a lot of my pull requests were like 10 lines, 50 lines, very easy to review.
And if the test failed, it was obvious exactly what went wrong. Now, does that scale in the world of AI? Maybe. I don't know. It's clear from history, no one's going to review 10,000 line pull requests. Are they going to review 10,000 pull requests? Well, I don't know either. This is very difficult. I think at some point we're going to have to stop reviewing code. I think that's ultimately what's going to happen, but for many companies, they're not ready for that. They're not ready yet. AI is making too many mistakes. It needs too much reviewing. People's factories aren't mature enough.
And we're in this awkward space where some companies and teams, they don't need review, or at least they don't think they need review. And other companies are very much still, you are responsible for every line of code that you write, make sure it's good before I review it. And yes, we're in that transition period and it's going to be ugly for a while, I think. But imagine we could get to the space where we don't have to review code anymore. That would be magical, wouldn't it?
Trust in AI-Generated Code [10:26]
Shane Hastie: Yes. Now we touch on a topic that I know was one of the things you and I touched on before we started recording is trust. How do I trust this code that has been produced, human or AI or some combination thereof?
Michael Parker: Yes, I guess maybe we get philosophical. What does trust really mean? I come from a world of continuous delivery where we merge to production all the time, like multiple times a day, and I'm a big believer in that. Merging and deploying very small changes very quickly. To do that, you need fantastic monitoring systems. So, if something breaks, you know about it immediately. And so, I think you need that anyway. And whether it's a human that breaks it or an AI that breaks it, I don't think it matters. You need to be able to respond to those things, roll it back. I mean, this isn't true for every company, right?
You can't afford to do that if you're building a space rocket. For a lot of people, if they're just building an e-commerce website or some server online, AWS goes down often enough, right? Nothing's perfect. It's fine to merge and deploy some small bugs and then we'll fix it as we go. But I think the bigger question is, if people are submitting code that is not up to standard, then what do teams do about that? And I fall back to engineers being responsible for the code that they submit ultimately. If they want to submit a pull request that's full of bugs, that's not good, right? And they can't just blame AI.
So, I think we have to take some responsibility for the code we submit. And I'm largely happy for them to fix that in any way they like. They can write a better factory, they can get some review tooling, either AI or not. They can split up their pull requests, they can write more tests, they can do some pair programming, they can get some draft code review ahead of time. There's lots of different ways we can improve code quality and a lot of these traditional methods still apply, I think. I guess it depends really what we mean by trust and if there's a wider issue around trust and AI.
From Artisan to Factory Architect [12:43]
Shane Hastie: Coming back to writing the factory, building the factory, I didn't go into software engineering to be a factory worker. I'm an artisan, I'm a craftsperson. How do we bridge that?
Michael Parker: Yes. I think the question is, can you fall in love with crafting the factory? I wouldn't describe a lot of these people as factory workers. I would say they're more factory architects, factory managers. And I think there is joy to be had orchestrating these different agents and systems, but it's one step removed from the ultimate customer that you're trying to serve, right? If the customer is trying to buy your product on an e-commerce site, for example, and you're busy making your agent output better formatted code, you're one sort of abstraction away from the customer. And historically we've been taught that's a bad thing.
We want product-facing teams. The whole agile process was about connecting customers and stakeholders much more tightly with engineering teams. And so, pulling these people away and focusing on the factory could be seen as a step in the wrong direction because they'll lose sight of what we're trying to achieve for the business. But I don't think everyone needs to be a factory architect. I don't think this world is very efficient if we are all building our own factories.
I think we could see an emergence of an AI platform team essentially that are basically building developer tools for engineering organizations and they're rolling out agents and rules and structures, so that everybody else can focus on delivering value.
The AI Platform Team [14:26]
Shane Hastie: So, this is the platform team on steroids?
Michael Parker: I mean, it's a little bit different because like many platform teams, they work on cloud development, and a lot of these factories are being run locally. So, I do think we need a stronger tool set for rolling out local factory configurations. I brainstormed a bit of this when I was at Docker, because Docker containers and images are very interesting as a way of putting out developer tools and you've got a sandbox environment. So, agents aren't going to accidentally delete your hard drive and all this fun stuff that you see happening. But I think there's a gap in the market and in our tooling space there, how do we roll out these tools?
If I write a new rule across all of my projects, how do I give that to you in a seamless way? How do you log on and just have a new set of agents and rules and everything's been upgraded and maybe I can give you a different model or I can use a different model for planning versus coding. I've got these review agents that you can run. All this works quite well in the cloud. And so, I think there's another debate to be had about how much of this should happen in the cloud and how much should happen locally because you don't necessarily want a hundred agents running on your laptop all the time.
And there's another argument to be said like, you want these agents to be working overnight when you're asleep after you turn your laptop off. But local IDEs have been very sticky. Lots of people have tried to build IDEs in the cloud and some people have moved, but lots of people still love their local environment. Even though you have to install a hundred different tools and things don't work all the time and you've got your environment and you've run out of space and you don't have enough around, people still love their local environment. So, it's going to be very interesting to see where this future goes.
Do we have some sort of hybrid methodology where some of these things are running in the cloud, some of the things are running locally? Where does this factory live and what are the interface points?
How AI Is Changing Team Composition [16:21]
Shane Hastie: What's the makeup of the team that is integrating AI today? What's different about teams?
Michael Parker: I think we are seeing a blurring of roles a lot when it comes to product management, design, front end, backend. AI gives this ability for anybody to become not an expert, but knowledgeable enough so they can have the conversation. I did a bunch of game design, but I've not done training on UI design. But if I feel like a UI feels off like the design, I can jump into AI and just have a quick conversation and say, "What's the industry best practices for an input form?" Or like, "I want people to sign up to my wait list. How many fields, should I ask them for their job title and what's that? How's that going to affect people signing up?"
And I can immediately get world-class advice. I mean, if it doesn't hallucinate and it doesn't lie to me, right? Hopefully, it doesn't too much. But that means that everyone can now start participating in conversations, which I think is really interesting. And tools like Lovable, for example, allow product managers to very quickly prototype engineering solutions. So, a product manager can think of a feature and very quickly sketch something out that people can actually click on. And I think this actually brings product management and engineering closer together in some ways because they'll start noticing the edge cases.
So, engineering and product management in my history, it's always been like, "Hey, can you just add this button?" It's like five minutes, right? And engineering's like, "That'll take us a month". And it's like, "What? Why is that going to take a month? Well, have you thought about this and this and this and this?" And it's like, "I don't want to think about this. I'm focused on the customer. The customer has this problem. Please solve it". The danger, of course, is that you build a prototype and you think it's the finished product and it's like, well, I did it in five minutes. Why are you guys taking a week?
Blurring Roles and the Dunning-Kruger Effect [18:19]
So, there's this Dunning Kruger effect that we are also seeing where it's like, "Oh, I can code because I've typed something into Lovable". So, I think there's two sides to the coin on that.
Shane Hastie: So, roles missing, AI tooling becoming part of that. What else is changing in the team environment?
Michael Parker: I guess the role of full stack developers versus pure backend front end developer split is an interesting one. Throughout my career, I've seen both approaches. Before I went into management, I was very much a backend engineer, interested in infrastructure and DevOps and scaling things, really good microservice boundaries and API specs and all that fun stuff. But now we have this ability to churn out code under the right rules, and I think it's becoming more important to make sure our backend is extremely strong. And then that lets you, I guess, vibe code some of the UI elements quickly. And all the UI engineers are going to hate me for saying this, right? So, sorry about that.
But I do think also there's an enhanced need for setting up the framework to allow these tools to work. So, at TurinTech, we've got a heavy focus on what are the patterns we're going to use, what are the libraries going to use, and we choose these things based on what LLMs are trained on, what they're going to be good at. And so, we'll set out with a framework in mind and a code-based style and we'll see if AI can follow that style. And then we feed that feedback back into the loop, right? Is AI good at following these rules? And either we change the rules or we try to change AI. But I think these things do need to work in tandem.
You don't want to be fighting against the training. We haven't seen the end of this. Do we have full stack engineers? Do we have backend? Do we have these factory architects in teams? We're also seeing emergence of researchers and data science engineers inside teams. The other thing to consider is if engineering productivity skyrockets, where is the bottleneck? And then I think the bottleneck becomes your understanding of the customer problem. It used to be the case that you could figure out what customer problem to solve, and then you can spend nine months fixing it.
If that nine months become one month, your discovery process needs complete overhaul. You can't just talk to developers about the same problem for nine months. You've got to make decisions in hours and days, not weeks and months. So, I think there's a knock-on to how you talk to customers, how you collect data, how you make decisions. And then also it shortens the loop for feedback. Engineering has always been the most expensive way of learning. Product management books always talk about stop building things to learn, right? Just draw a diagram on a piece of paper and give it to the customer and say, "Is that what you want? Would that help?" Right?
And then you can get more in that 10 minutes than building the thing for two months. But if that flips on its head and you can build a product in a day or at least a prototype in a day and give them the prototype, that changes discovery. If the bottleneck is product discovery, you're going to need more product managers, more researchers, more designers, and engineering shrinks as a percentage of your workforce, I guess, at that point.
Culture Shifts in Engineering Teams [21:53]
Shane Hastie: This is the engineering culture podcast. What are the culture shifts, the teamwork shifts that are happening with these changes?
Michael Parker: Yes. So, there's some good things and bad things, I think. One of the bad things is that people are becoming a bit more isolated in engineering teams. Everyone has their own setup. Everyone's using AI in different ways. And some teams are handling this really well. I've actually seen the reemergence of mob programming on some high performing teams where because the code is so fast to create, team synchronization is actually becoming more important than the speed at which you generate code. So, I was talking to a development manager a couple weeks ago. They do all of their code on one computer with five people.
They basically live their life in a meeting room discussing the problem, the structure, and then they type in the exact prompt and the plan, and then AI writes the code, and then they all review it, they discuss it, which I love. That brings warmth to my heart. People working together again and talking, having fun. That's how development should be, I think. We all went into this profession because we like computers more than people, but we do need human connection as well. So, I think getting people in a room and working these things through together is a great way of working. But I think lots of teams are not doing that.
A lot of teams are still stuck on their own computers and we're kind of seeing this combination of fear, denial, bargaining, grief. Some people are worried that they're not keeping up with the latest tools and they're maybe embarrassed to ask questions about why AI is going wrong for them or how do I get it working? So, they're more shy about working together and setting up their environment and they see some phenomenal gains from other people and they're worried that they won't compete. And this drives people sort of inwards. So, you're just stuck on your own environment, you're trying to make sense of it, you're trying to read things.
And so, I think we need to break out of that and we need to connect people more. That's the two ends of the spectrum for team culture. I guess the other thing is how leadership communicates and approaches adoption of AI tooling. And we're seeing various takes on this. You've probably seen the extreme end of the spectrum where people are like, "You're going to be fired unless you use AI". Everyone has to go all in, spend a month, all you're doing is learning AI. And that produces a lot of fear and worry from people, right? And this is what these messages are intended to do.
It's really kicking people and saying, "You can't just ignore this, you have to learn". But at the same time, the people on the ground are seeing a lot of the problems that you might not read about on LinkedIn or in podcast. And so, I think there's a growing disconnect between the level of hype believed by some of engineering leadership and the reality on the ground. And that's breeding distrust from both ends, right? Leadership think, God, my developers are so slow, they're not adopting AI. I read on LinkedIn that I can do everything in 30 minutes. Why is this taking a week?
And at the other end of the spectrum, engineering, like, "Have they used AI? Look at our code base. You can't just build the whole thing in JavaScript and Python. I got .NET2 code". It doesn't work. So, I think that's a cultural divide we need to bridge as well.
What Should Our Industry Look Like in Five Years? [25:19]
Shane Hastie: What's the important question I haven't asked you today?
Michael Parker: I guess the important question for us all is, what do we want our industry to look like in five to 10 years? And maybe me and you can't solve that here and now, but I do think it's as important as an industry to see where this is going and agree if we want this or not. And maybe we don't have a choice, but I do think it will end up in a better place. I do think it's possible to build AI systems that help us return to joyful development, offload all of the boring and the mundane work, primarily running in the cloud autonomously, being able to bring teams together.
How do we iteratively get there I think is difficult and everyone's trying to make progress in these areas, but I do think we need to agree what we want our job to be in five years' time. Is our career going to go away? Is it going to change? Are we okay with it? And I guess if not, what do we do instead?
Shane Hastie: Some pretty deep and thought-provoking questions there. Mike, thanks so much for taking the time to talk to us today. If people want to continue the conversation, where can they find you?
Michael Parker: Yes, I've loved this conversation. If anyone wants to talk to me about any of these topics, I'm always interested to hear what people think. You can reach out to me on LinkedIn, search for Michaelparkerdev@TurinTech, and I'm happy to hear from you.
Shane Hastie: Cool. Thank you so much.
Michael Parker: Thank you.
Mentioned:
- Michael Parker on LinkedIn
```

---

## 9. OpenAI Introduces Websocket-Based Execution Mode to Reduce Latency in Agentic Workflows

- 日期: 2026-05-07 14:48
- 链接: https://www.infoq.com/news/2026/05/openai-websocket-responses-api/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
OpenAI has introduced a WebSocket-based execution mode for its responses API to improve the performance of agentic workflows used in coding agents and real-time AI systems. The change replaces the traditional HTTP request-response pattern with a persistent, bidirectional connection between client and server, targeting latency and coordination overhead in multi-step reasoning workflows. According to OpenAI, early production use shows up to 40% latency reduction and improved throughput in high-concurrency scenarios.
The update addresses a growing bottleneck in agentic systems where each step in a workflow, such as tool calls, intermediate reasoning, and follow-up queries, previously required separate HTTP requests. As inference speeds improved, these repeated network round-trip times became a dominant source of latency and operational complexity.
Traditional HTTP Flow (Source: OpenAI Blog Post)
The WebSocket-based execution mode uses a long-lived, bidirectional connection to enable continuous data exchange without repeated handshakes. This supports streaming responses, faster tool execution, and more efficient coordination of multi-step workflows. It aligns with event-driven design patterns in distributed systems, where maintaining state across interactions improves responsiveness and throughput. The change reflects a broader focus on the transport layer in agentic systems, where communication patterns and connection management influence overall performance, as discussed in an AI Agent Transport Layer.
Ofek Shaked, a Vibe coder, described the change as,
WebSockets for agent state is such an obvious but huge win. No more cold starts killing your multi-tool chains.
OpenAI reported up to 40% latency reduction in early production use, along with sustained throughput of around 1,000 transactions per second and bursts up to 4,000 TPS. These results indicate that transport-level optimizations can significantly impact end-to-end AI system performance alongside model-level improvements.
Gabriel Chua, DX engineer @ OpenAI, stated
You can warm up the connection by sending your system prompt and tool definitions first. It's Zero Data Retention (ZDR) compatible.
Adoption has been immediate among developer tooling and coding agent platforms. Vercel integrated the WebSocket mode into its AI SDK and reported up to 40% latency reduction. Cline observed a 39% improvement in multi-file workflows, while Cursor reported gains of up to 30%. These results highlight how system-level optimizations outside the model itself are increasingly shaping real-world AI performance.
Agent Workflow Evolution with Persistent Sessions (Source: OpenAI Blog Post)
From an implementation perspective, developers integrate the WebSocket mode by replacing multiple HTTP calls with a single persistent session. This reduces repeated connection setup and simplifies orchestration logic across multi-step workflows. It also improves support for streaming use cases such as incremental code generation and interactive reasoning, where partial outputs can be consumed as they are produced.
Kevin Cho, an engineer at Microsoft, noted that the approach reflects:
Going back to the original software stack problems. websockets and stateful connections.
The shift introduces new system design considerations, including connection lifecycle management, backpressure under high concurrency, and reliability in distributed systems, aligning with established stateful system patterns.
OpenAI released the feature in alpha after a two-month cycle to selected partners, including Codex. Codex has since migrated most Responses API traffic to WebSocket mode, indicating production readiness.
```

---

## 10. Presentation: Engineering at AI Speed: Lessons from the First Agentically Accelerated Software Project

- 日期: 2026-05-07 14:07
- 链接: https://www.infoq.com/presentations/engineering-ai/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
Transcript
Adam Wolff: I'm Adam Wolff. I'm an engineer on the Claude Code team. Today I want to talk, not about Claude Code and how to use it, but instead about how we build Claude Code using Claude Code. This is a case study of what happens if you give a team Claude Code and you orient your project around it. When I told Faye what I wanted to talk about, I told her I'm going to talk about how simple Claude Code is and how that enables us to move fast. Then I started doing some spelunking in our repository. You'll see, these stories are anything but simple. They're actually quite complicated. Even the simple things end up being complicated by the time we ship them.
The point is not necessarily about what's simple or complex. It's about the way that AI has changed the bottlenecks in the Software Development Life Cycle, where implementation used to be the big piece. You would have to spend a lot of time up front figuring out what you're trying to build and how you're going to build it. Now it's usually better to charge ahead and let your users and your development process tell you what to build. I'm going to tell a few stories and trace through how some modules in Claude Code evolved.
The last story is about shipping something and removing it in like two weeks, something that I've never seen before. I'm excited to share some of these stories with you. Any Claude Code users here? If you haven't tried it, I highly recommend it. I'm proud of it. I think it's a great product. Claude Code is one of the heaviest users of Claude Code. We calculate that 90% of the code that we ship to production is written by or with Claude. We also ship continuously internally. We have a very engaged user base within Anthropic. We try to ship daily, on weekdays, externally. Very fast releases, very robust feedback channels. The users really depend on this tool. We hear from them when we break something or when they have a feature request.
Scope (Three Stories)
Today I'm going to share three stories from the development of Claude Code. They each evolved differently. I think they show how AI doesn't solve these problems that we have as software developers. Everything ends up being pretty complicated at the end. It does change the way we should think about these problems and where some of the bottlenecks that we're trying to speed up are. In each one of these stories, let's keep an eye on the following things. Why did we have to ship to find out the real requirements? What architecture choices really mattered in the end? How did we know when we had to press through the pain versus turn around? Because everything you do is going to have some pain involved. The question is, when is that pain too much? How does it tell you you're going in the wrong direction?
Episode I - Rebuilding Input
To start off, I'm going to tell the story about the cursor class in Claude Code. I chose a picture of a slide rule here, one, because I could find ASCII clip art for it, but two, because the slide rule is where we get the word cursor. The part that moves on the slide rule was originally called the cursor. That's how we ended up with that name for the blinking thing where your text goes in a computer program. Here's the problem from our point of view. We're going to run Claude. We know from the get-go that we want to have all these special behaviors when you type special characters in Claude. You can see, I can go into this fancy menu by typing a slash command. I can also @ mention a file name. We're going to have to look on your disk.
Then I want to be able to tab complete that. There's a lot we want to do when we take your input. We know that we're going to need to intercept each keystroke to get these behaviors. Unfortunately, these behaviors are quite complicated. There's a lot of them. The conventional wisdom is you do not want to rebuild input. If you've used React and you've used a controlled component for text input, you know some of the perils that you end up with here. There's a lot of behaviors that users expect that are not built in. I'll just show you, I have this really short program where I'm going to use Readline, which is like the old C library for taking user input. It goes back to Emacs days and the very beginnings of Linux. Let's run this program now. I can type, obviously, into here. There are a lot of other behaviors. I can hit Ctrl-A, that takes me to the beginning. Ctrl-E takes me to the end. If I go here and Ctrl-K and kill, I can do Ctrl-Y and paste that back. Ctrl-H, that's a classic. I can say, obviously, dogs. I can keep going here. There's a lot of functionality. What are we going to do about this when we totally replace the input with something that is under our control? It doesn't seem like a real choice here. We know we want to have these behaviors. We know that this program is mostly going to be about taking input from the user. We need this control. We go ahead and build this virtual cursor class.
To do this, we need to do our own wrapping. Word wrapping, if you've ever done it, is hard. You need to backtrack to have a proper word wrapping algorithm. You can't tell just by looking at the next character whether you're going to wrap or not. It's a tricky implementation. We build this cursor class. It's like 300 lines. The most important thing about it is that it's fully testable. We can render it in a way that we can make an assertion about how the cursor appears in the string. It's also immutable inside. It's got this fluent interface. The way it works is you operate on the cursor, and you get a new cursor. That obviously helps with concurrency and makes it more testable. This is one of my first contributions to Claude Code. I was pretty happy with it. It fixed some bugs with wrapping and its input. Very clean API. Super nice test coverage. There were bugs at first, but we worked them out, and thought, this thing is pretty good.
Then, I felt sure we were on the right track when two months later, we were going to ship externally. Right as part of the first release, my friend on the team implemented Vim mode. I'm a diehard Vim user. I just thought this was awesome because this is something you really can't do easily if you use something like Readline. The tests are what really made this possible. You can see here how this testability was easily extensible to Vim mode. This all shipped in one PR. It wasn't simple. It was maybe an additional amount of code that was bigger than the original implementation, covered by a gazillion tests. It wasn't that hard. If you've used Claude Code, you know the AI really helps with this kind of development, especially when it can run the tests and then tweak the implementation. It goes pretty fast. This was a case of our architectural choices really paying off.
Two months later, we're starting to see international adoption. This is where we learn why everyone tells you not to rebuild input, or one reason not to rebuild input. I can answer that succinctly now. I can tell you Unicode is the reason not to rebuild input. This is one tricky case where we have these special characters that are double wide, A B C, the second row here. It turns out that in Unicode, there's an arbitrary mapping between the number of code points you have, the number of characters you have, and the number of columns you have. All of those things can vary arbitrarily in Unicode.
The first thing we need to add here is grapheme clustering. Instead of just breaking on character boundaries, we need to use grapheme clusters and identify those as the word boundaries. We introduce it. Again, we have comprehensive tests. This goes in pretty quickly. It's complicated, but it's not so bad. We ship this, and now we're starting to work with the international users. We're starting to use it more. We get this bug report that when I hit the End key, the cursor doesn't actually go to the end of the line.
This turns out to be another issue with Unicode. Now we have two forms where we can represent the same string in different ways. This is another example of Unicode being tricky. You can have a Unicode code point that is just the accent. It combines with the previous thing. What do we need to do? We need to normalize the whole cursor class to all be NFC, one representation everywhere. This is a major refactor. We move a bunch of functionality inside this new class that we developed. We hide details of the interface. We add a bunch of consistency stuff. Again, it's really not that bad. It's another refactor. It's another few hundred lines of code, a lot more tests. Claude Code is a superstar here. This is just what it does so well.
This goes on for a while. Claude Code starts doing more and more stuff in the background. Typing is slowing down more and more. This is another reason why people are wary of taking input, because we're running a bunch of JavaScript every time the user presses a key. We're a long way from the cursor blinking in sync with the hardware, which is where the terminal started. We go back and look at this code that we've written. We're like, this is not very optimized. Basically, we're eagerly doing all this computation, no matter what is happening. If you hit the left key, we don't need to relay out all of the text, but we do. Optimization pass. Again, my same friend who implemented Vim mode went back and did this optimization pass. He said, "I got nerd sniped hard", which I just love.
Basically, in a day or so, totally and thoroughly optimizes this class. Again, now using a benchmark in addition to the test, it goes really fast. We get it much faster. I'll just show you what this code looks like. Claude helped me. I wrote a very simple demonstration here where you can see eager cursor always wraps in the constructor. Lazy cursor doesn't do anything in the constructor. When you render, you check what you might need to do to layout. Now I can show this silly little demo. I can show you, obviously, by deferring work, that's one of the few true optimizations you can make, is doing less work. It works here. We get it nice and fast. This is a story that I'm going to call a huge win. We did something you're not supposed to do. We re-implemented input. We shipped a bunch of bugs but we fixed them fast. We now have this total control over input. It went super well. The next question is like, ok, that's a great win for you guys, I'm happy for you, what does it look like when this doesn't go quite as well? The next two stories are all about that.
Episode II - Reimagining Shell
This next one is about Claude's shell. If you've used Claude, you know that Claude uses, we call it the Bash tool. It can actually be Bash or Zsh, because so many people use Zsh. This next story is about how we went about implementing this. It's a sunny day. I wake up. It's like, time to do some work on Claude's shell. How hard can it be? You just need to send a command to Bash and then have it process it and get the result. Turns out very hard. I'll just walk you through some of these complications that we faced.
First, let me give a little demo of where we ended up. This is how Claude works now. If I tell Claude like, run a few Bash commands, see what's going on in this repository, Bash is really the way it relates to the world. You'll see it'll think for a little bit, and now it just runs like 8 zillion Bash commands. You'll also note that they all kind of run at the same time. That's actually really important, and I'll come back to that. That's not where we started. Where we started was a class I literally called persistent shell. It was the most naive possible implementation of this abstraction. I'm typing into a terminal. I type commands, I get the response. I want Claude to conceptually do the same thing. I give Claude a persistent shell. It can run one command at a time. We will wait for the output of that command and then process the next one. It turns out that actually getting this concurrency right and guaranteeing this kind of sequential operation and recovering from faults is quite difficult. That turned out to be pretty complicated, but it was doable. One of the benefits here is that the environment persists.
If Claude changes directory, of course, you've changed directory in the shell. What else is going to happen? If Claude exports a new value for an environment variable, that will stay there. It has problems. Those are obvious when we start building this thing called batch tool, which allows us to execute tools in parallel. This has turned out to be very important for agent performance. We didn't really know this going in. Persistent shell is now the bottleneck. Even if the batch tool can execute commands concurrently, persistent shell will make them all serial and slow us down.
We know we have to pivot. What are we going to do? The obvious answer is like, somehow, we have to take this persistent shell and make it more transient. We delete the original implementation of persistent shell. It's a lot of code that I've laboriously crafted, but we'll get rid of it. We replace it with just something I called shell. I referred to it as transient shell at the time. The result is like, wow, it's a lot faster. I don't have to belabor this point. Anyone who's ever programmed a computer knows doing things in parallel is faster than doing them sequentially. Again, this is another one of these optimizations that like, this actually makes a difference. It's very important. What are we going to do? It's not obvious how to get output out of a shell. We need to support a lot of things here. Claude can write a bad bash command. It can write a command that opens a quote and never closes it. We don't want to crash just because Claude sent us a bad shell command. We also want to make sure we don't corrupt the shell.
Then, also, Node makes this much harder. I hate to say this, because I love Node and I love TypeScript. Python is a little better for these kinds of things. When you use things like pipes and file descriptors, it's much closer to the real syscalls. Node emulates a lot of this stuff. Let me just give a quick example of that. Two problems here. One is that you can tell Node to spawn within a shell, which is fine, but it's a lot slower. We already said, we're trying to speed things up. This makes it like two times as slow to spawn with a shell. The other thing is like, in C or in Python, I can create a pipe and then hook it up later, which is really valuable with these kinds of concurrency and especially error recovery. Can't do that in Node. You have to have your pipe ready and hook it up before you spawn, which really constrains the implementation. We tried a gazillion different ways of doing this. We tried writing to stdout. We tried talking to it over stdin. We tried pulling file descriptors. There's a lot of ways to do this.
In the end, we found something that works and we implemented it. In the spirit of Claude Code, I just shipped it internally. It was missing a really important feature. It was missing the user's environment. Because we're spawning here, we're not getting all of your bash_profile, bashrc, or zshrc, or whatever. We also had to re-implement working directory tracking, which is, again, tricky. You have to see where you ended up at the end of the spawn command and record that in the program. Getting this wrong really confuses Claude, it really confuses the users as well. Also, we lost this environment variable persistence, important behavior change. This didn't work at all. I turned it on for maybe a day. People were like, you can't do this. It turns out that the way people customize their shell is a non-negotiable part of their user environment. Claude needs to be able to run all your aliases. It needs to inherit all your environment variables. Or, basically, it doesn't work with your project. This is one of these things where, like, you discover the requirements by poking at them. We poked and got poked back.
We need to figure out, how do we recover the user's environment for these transient shells? Again, not obvious. This is a moment when it's like, maybe we're on the wrong path here. Do we definitely want to do this, make up some way of capturing the user's environment? I think we made the right choice here. The reason why is because we'd already felt the benefits of the architecture. We saw that we were faster. We saw that the implementation was simpler when we got rid of this queue. Our bet was that this is worth it. It was not easy.
We come up with this idea of a snapshot. What we're going to do is we're going to start the user's environment once and then try to capture it. Then we will replay a script that creates that environment every time we spawn a command. Hopefully, it'll be nice and fast. There's a lot of rough edges here. If you've ever worked with shells and bash and Zsh, bash is 60 or 70 years old now? It's got a lot of hairs on it. It's pretty quirky that you can have special characters and aliases. You can have aliases that refer to functions, that refer back to aliases. There's an order where you have to dump out this environment to get it to come out correctly. There's all kinds of error conditions where if you have a problem while you're trying to capture this environment, you sure as heck don't want to capture the problems. This was like, what are we talking about here? A seven-month journey of finding out real problems caused by real users using their real shells.
Again, very hard to discover at a requirements phase. Just going to walk you through some of this real pain that I live through. People have very funky shell configs where you make a choice at the beginning, and then it loads different versions of their shell. They alias something so that you always get asked when you try to remove something. This is a real problem for Claude. It can't really deal with this kind of interactive stuff yet. There are edge cases everywhere. You can have funky Heredoc stuff. You can have functions, again, that rely on input. The differences between Bash and Zsh are enough to make this hairy. This is where we ended up. We ended up with a snapshot implementation. The way it works is like, we're going to declare a temp file. We are going to start the user shell. Then once we have that thing running, we're going to dump the aliases and declare the functions. We'll do this all in the right order. It took three weeks to come up with exactly how this was going to work, of iterating, trying stuff with our users internally. These snapshots were hard.
The interesting thing is at the end of the day, all the smoke clears, dust settles, it was still simpler than persistent shell. We did make the right architecture choice. A big part of the reason here is that snapshots are composable with this transient shell. The nice thing about it is that, yes, there's a bunch of complexity in the snapshot, but it's all in its own file. I think we all know that modular complexity is much better than tangled hairball complexity. We're looking for more evidence that this was the right design. It came when we wanted to do sandboxing. There's a lot of reasons why you don't want to trust Claude to run any old command. You also want to try to avoid permission prompts if you can. We developed a snapshot abstraction. The nice thing about this transient shell is that it plugs in really well. You can always wrap a command using another command. argv is the original form of Linux composability or Unix philosophy. You can do this LD_PRELOAD thing on Linux. I don't want to say that sandbox was simple or easy. It wasn't. It's like 3,000 lines of really hairy stuff, but the integration with shell was simple. It goes in really nicely.
This is a case where we had to make tradeoffs. Our original requirements were that we had to have a persistent shell. We realized that that actually puts us in too much of a box. We need to emulate a persistent shell, but we don't really want to use that abstraction. In this case, I think the speed that we gained, both for the user in terms of parallelism and for the developer in terms of composability, were worth it. I also want to say, look, the first story about cursor was all about tests. There are times when tests are a godsend. They're exactly what you need to move fast. Not in this case. Persistent shell had a ton of tests. We just had to delete them because the abstraction was wrong. It's not as simple as just write tests. It never is, unfortunately. This is the architecture that emerged. You can see, it's really nice. We can get our snapshot from one place, our sandbox from another. These things do not overlap at all. They don't need to know about each other.
Then when we spawn, we can use the sandbox and the snapshot together. This is composability. This is the architecture that wins, even when the requirements are a little off, the implementation's a little hairy. The point here is that we had to experiment to find this. The persistent shell that we started with was like what you'd naively think of, given these requirements. I'm naive. That's what I thought of. It didn't really work. Through experimentation, we landed on this funky design where you have a transient shell, you take a snapshot. Claude and I racked our brain. We couldn't think of another example where this technique is really used, obviously. I'm sure people will think of it now that I've mentioned it. It was found through trial and error, pretty much. It balances all of these competing requirements. I'm going to emphasize this point about experimentation and point out that when you have an experiment, you have to consider the possibility of failure.
Episode III - Reversing SQLite
This last story is a little bit about an experiment that failed and what that looks like in this age of AI. This is a story about trying to ship SQLite as a persistence layer for the conversations that you have in Claude Code. Let's just illustrate this behavior real quick. I'm going to do Claude resume, and I get a list of conversations that I've been having with Claude about this project. You can see I pick one and it comes up, and now I'm ready to continue the conversation. When we started this, I just refactored this abstraction to use JSONL files. That's important, JSON, not JSONL. We could just append to an existing session file all the messages and changes that were happening. It worked fine. It actually did not have a problem. That is smell number one, it was working fine.
There's all this quality lore around SQLite. Also, I was raised at a time when people are like, don't store your stuff in files, put it in databases. The database is for data. SQLite has this sterling reputation. I didn't look that far into it. I was like, ok, SQLite, it's super well tested. It's been around forever, ships everywhere all the time, must be really good. We were also looking at using Drizzle on top of SQLite. Drizzle is an ORM in TypeScript. This thing is batteries included, super nice. You write your schema in code. It's got migrations in it. We want migrations because actually one problem we've already seen is that as the schema for tool calls evolves, we have trouble loading old conversations. We don't want to just crash when we try to load your old conversation that has an old version of the tool call in it. I'm thinking like, this is really going to help us migrate the data forward. Also, we were emboldened. We've had all the success using Claude to make these really bold changes and put stuff in. I was like, yes, let's try it. Let's see what can happen. When we say we were emboldened, I should say I was emboldened.
This is a story of 15 days that I'm never getting back. I'm not totally sorry I did it, even though I think you'll see that I could have seen some of these things coming. Starts off, we're going to launch this persistence thing. Users have been demanding this resume feature. I was holding it back because I wanted to try this database implementation. We finally go to ship it. I merged the first commit with this beautiful Drizzle schema. It's got foreign key constraints and indexes. I'm quite proud of it, you can imagine. Immediately, it has to be reverted. I totally broke the developer environment. I had a messed up dependency. This was like the very first sign that I was on the wrong track. Eventually, I cleaned that up. I merged it later that day, and we were off to the races. After less than a week, there's this GitHub issue blowing up. People are having trouble just starting Claude Code when they get this new version.
The reason is that the SQLite dependency is a native dependency in the npm ecosystem. I didn't know that much about this before I started. I don't know about you, but this is my first time distributing an npm-based app. Usually, I use Node and npm just to put something on my server. In this case, we're giving everyone an npm-based app and asking them to run it. There's this dependency called Better-SQLite. If it works for your OS and architecture, we can find the right distribution, it works great. If we can't find that, we crash. That's terrible. I went as far as, on your system, trying to rebuild Better-SQLite, if possible. Weirdly, npm totally allows this, which I was like, I shouldn't be allowed to do this. Just hilariously, this actually involved using node-gyp, GYP is Generate Your Project, which is actually a Python thing. Again, another sign I was deeply on the wrong path is when I'm checking PYTHONPATH, trying to rebuild this module for your system natively. This went nowhere. A lot of trouble. Better-SQLite author gets involved. We're really struggling here. We decide, I'm going to make this optional. Just see if we can press through the pain.
If we can run Better-SQLite, we will also give you the resume feature. If we can't, you just don't get resume. We'll see if we can make this work for a little while. Then, we also add diagnostic warnings to try to help people understand what's going on. Because once you make a feature optional, but they didn't choose whether to make it optional, that's pretty complicated and confusing. There's a lot of UI work to do on all of this. The day I knew it was over was when my friend is merging this multiprocess PR, and he didn't use the database. I was like, this is the whole reason we wanted SQLite was so that we could have safe multiprocess. He points me to some deep buried pages in the SQLite documentation about all the funky limitations of SQLite with multiprocess. It's actually a little mindboggling to confront some of these constraints. I'll try to illustrate them for you.
Once I saw this, I was like, this is just not worth it. Like, we're pressing through the pain, and for what? I posted in Slack, we're taking this thing out. I'd set it up so it was able to cleanly revert. I'd also already made it so that it was optional. We're now just over two weeks taking this feature out that we just shipped. I'd never seen anything like this before. In a way, this is the most startling example of engineering at AI speed, I believe.
Here's what we discovered through this process. In some cases, shipping revealed these problems. In other cases, this was poor due diligence on my part. There was a foundational issue here that I just didn't really recognize until after I shipped. I worked at Robinhood before I worked at Anthropic. At Robinhood, I loved the database. I just found that it was my rock. We could ship screwed up application code, and the database would protect us. It protected us with concurrency guarantees, and it protected us with data integrity guarantees. However, the constraints of a financial firm are completely different from the constraints of a developer tool like this. The worst thing that can happen with Claude Code is you go to start it, and it doesn't start. I don't know about you, but I can't really do anything anymore if Claude isn't there to help me. People got pretty upset when Claude crashed. This is a case where availability totally trumps consistency. For a financial firm, it's exactly reversed.
The other thing that I just didn't know is that native dependencies basically don't work in the npm ecosystem. You can install them on your server, that's fine. If you need to distribute something, I would say just don't do it. pnpm, which is a very popular package manager, just doesn't really work with this. Again, this is a case where the user's running it on their app. If they can't start, we don't even get visibility into what's happening. The next thing is SQLite is an odd beast. I came from the world of Postgres. I thought SQLite is SQL. How different is it? I definitely learned the difference between the SQL spec and the nice features of Postgres. Let me just show you one example here. SQLite's locking is not like Postgres locking. Postgres can lock individual rows and tables. SQLite locks the whole database when you write to it. Here's one example. We're going to begin two transactions, and we're going to both read and write in the two transactions.
First transaction reads, second transaction reads. First transaction writes, second transaction goes to write and fails because the first transaction has already written a row. This is not retriable. This is not something that SQLite will handle for you. This becomes application code that you now need to deal. What are you going to do? How many times are you going to retry this? Users have 15, 20 versions of Claude Code open at a time on their terminal. This can get sticky really fast. Sometimes these sessions are days old. We might have three version skew, all three running against the same database. I'll talk about some of those problems as well.
I was really excited about migration. This is one reason why I thought SQLite would be a good answer for us. It turns out migration is also really tricky, especially when you're doing it on a machine that you don't have observability into and you don't really control. Basically, we need to do migration at startup. You start Claude Code, the last thing in your mind is that your data's going to get migrated. Even the slowdown is problematic, but there's something much worse here. You can't add constraints to a SQLite table.
In Postgres, you can just slap an extra foreign key on there. In my initial implementation of this schema, I forgot to add ON DELETE CASCADE. That just really bothered me, of course, so I needed to go fix it. I made a little demo here just to show you that when you run a migration, you actually have to turn off all of the constraints in SQLite. It can't really handle this. You turn off all the foreign key constraints, you have to delete and recreate your table, or I should say, first you recreate it, then you delete your table. While all the constraints are turned off, you can put bad data in your database. You actually don't even get the integrity guarantee that you sought originally. This is a bit of a contrived example, but there are other real-world cases that make this really hairy.
Then, the very last thing is like, this turned out to be super ironic. I work on the auto-installer, some of the greasy innards of Claude Code. The whole thing I wanted from this was safe multiprocess. It turns out that like, this actually makes multiprocess more dangerous. It's very easy to write bugs where you have two different versions of Claude Code and one overwrites or does something unexpected because there's a new version that has changed the schema. I know there's ways to build tooling and there are ways to train developers to not confront these problems, but they're very common. In this case, I just made a little example where one version is running against one schema and a new version is running against a new schema.
If the old version does anything like SELECT * and then writes back, it'll write bad rows. It'll overwrite data that the new version's written. It's not as simple as just making sure your schema's backwards compatible. You also have to be really careful about what you ever do in your application code. It takes a very mature software project to have real guards against this. You need a lot of intelligence about what's possible and not in SQL. Let's dump all that. We'll go back to JSONL. It works everywhere. This is what we use to this day. It's deeply imperfect. If you try to resume in Claude Code, you often end up with funky situations where you don't quite see what you expected to see. There's still some problems with this, and a lot of them are caused by data integrity issues, but at least you can start, and that's the most important thing. Was this a mistake? I think it would have been. It definitely would have been, but given how fast all this went, I'm glad we tried it. I'm not saying that SQLite is bad. I think we'll probably end up using it in Claude Code, but probably not for this, probably for something like settings and probably something with a schema that is really not expected to change.
Synthesis
Let's try to put all this together. What can we learn about engineering in the age of AI? In all of these cases, we learn things by shipping. Starting off, we were told that rebuilding input was a bad idea, but it wasn't. It was exactly the right idea, even though we didn't see all these Unicode messy edges coming. For shell, yes, user environments are really tricky, and we try to support all of them, and we do it imperfectly, but the tradeoffs here are worth the pain. In SQLite my main takeaway is like, don't ship a native dependency to npm. That's just too hard. The architecture here is really what determines the outcome of these projects. Cursor architecture was everything self-contained, no dependencies. That's amazing. That's amazing for Claude. It's amazing for the developer. You can rip through this stuff, even when it gets complicated. Shell is all about the dependencies.
In that case Claude didn't help us quite as much. Also, Claude's idea about what would work in the Node ecosystem, that tended to be wrong. Then in SQLite this is like a fundamental miss on, what are we trying to safeguard here? Availability is more important than consistency in this app. How do we know when we're on the right path? All of the development was painful here. These Unicode bugs that kept popping up, that did not feel good, even though I'm presenting it as a win. For shell, it wasn't ever clear that we were on the right path. Even the solution we have now feels a little hacky. With SQLite, it just got worse and worse every step. From the very get-go, it was pain and it just multiplied. You can have different outcomes when you experiment. I've got to underline that point. If you're not having failures when you experiment, you're not experimenting enough. That's one of the expected outcomes. In some ways, like a clean failure is a little easier to deal with than this situation with shell where you muddle along and it's not obvious that you're on the right path.
Either way, the core insight here is that you can test your architectural decisions. Thinking about this, I really realized like this is different. We used to spend a lot of time debating, design docs, design discussions, extensive requirements, POCs. We had to do this because we knew that the actual implementation would be really expensive. That was the bottleneck. That's what we're optimizing for. Now we can throw this away and we can find out. You'll see in two of these cases, both in the Cursor case and in the SQLite case, the outcome defied conventional wisdom. The conventional wisdom says SQLite is where you should put your data, but that turned out to be not true for us. In the traditional loop, you spend time on these requirements because you know this thick middle part is going to be the implementation and you want to save that. That's what you don't have, is developer hands to do this stuff. In the new world, the implementation is not the bottleneck.
In a day, you can pretty much pump out any feature with Claude Code's help. The question is, what's it going to take to get that in production? Then, how are you going to collect feedback on that to guide your next step? The only real advantage you can have in this world is the speed at which you learn. It's really not the speed at which you ship.
What are you going to do about AI, especially for a project that's fully AI enabled? One thing that we can all do is we can always ship faster. I learned this back in my days all the way at Facebook. I've held it with me ever since. Shipping speed is the key to having good software. The reason why is that, if you're going to get better, you're going to need to change. The faster you can change, the faster you can get better. Remember how I said Claude Code ships all the time? That is not a side point here. That is the point. That is what enables us to move really quickly. The other thing is like, CLI is a really useful form factor for this. It's much easier to deal with. It's much better for Claude to program. It's easier for the user to program, and for the AI to collaborate with you. I would ask, not all of us have the luxury of shipping a CLI, but what can you do to simplify your dependencies, remove ornamentation, and give power in place of like filigree? What's your playbook going to be?
First thing is, optimize your delivery cadence. You want to try to get to continuous deployment. That is the gold standard. We'd like to do that, not just internally, but for some of our external users as well. We're just trying to reduce the cycle time. That is the most important, biggest lever. Second thing is like, do put things in that make it easy to reverse course. If you're experimenting, you're going to have things that need to go backwards, so feature flags, modular architecture, wherever you can find it. Then the last thing is, we invest really heavily in our build, release, and distribution. If you ship a bad release, ideally all you have to do is move a pointer to get back to a good known state. You do not want to have heavy processes for backing out a bad change, if you're moving this fast.
The last thing is, you have to unship. Instead of spending a lot of time on your product roadmap, and making sure that each feature makes sense in your whole product suite, I would say just ship everything, and then edit later. It actually requires a lot of suppression of ego. Because at the end of the day, you and your friend might ship very similar features, and you're going to have to decide, is one better, or do these have to come together? I think you can see that in Claude Code. We have a bunch of overlapping features. We're still figuring out how they all play together.
What's next for Claude Code? I think we have this basic loop running, but the AI is quickly driving the implementation cost to zero, especially as the model gets better. Really, any change I can think of, I can prototype by the end of a single day. The new bottleneck is really not about this. It's actually about the longer loops that we all experience as part of the whole Software Development Life Cycle. This is things like using AI to generate actionable insights from bug reports. It's about having very sensitive evals so that when you make a small prompt change, you can detect whether this is helping or hurting you.
The last one is just continuing to invest in the way that you build, release, and distribute. Making sure your CI runs really fast. Making sure that you have multiple releases a day, if you can. These are the things that you really need to work at this speed. Claude Code is a special case here. We're always dogfooding our own product, and it really guides our intuitions about what the right things are. It also has this compounding effect. I did want to take a moment and say, all of us need to be dogfooding. If you're not using AI, not just to accelerate your development, but to accelerate all of your development processes, how you write a design doc, how you interpret feedback, all of these things, even like your planning process, these things are all optimizable with AI. I really hope everyone here is working on figuring out how to best apply this technology, because, again, this is where the new bottlenecks are.
The Takeaway
Different stories here. I wanted to get here and tell you like, it's really simple. Just keep your code really simple. Obviously, I did a bunch of spelunking that proves that it's not really that simple. That's not the point here. The point is that when the implementation cost goes to zero, the feedback loop becomes everything. Optimizing that feedback loop is the way that you can work at AI speed.
Questions and Answers
Participant 1: I didn't get the SQLite. Did you guys catch it before rolling to production or users actually started to report issues and they have to roll back the SQLite migration?
Adam Wolff: We had to take it out. We had it in the product. We shipped it for about two weeks and then we removed it.
Participant 1: Did you do something about not getting issues like that for their own production, or testing on different operating systems, different combinations?
Adam Wolff: Yes. Our test coverage is limited. We have a very strong security environment at Anthropic. It's pretty hard to set up something like a Windows machine. We do test with Windows, but it's tricky. On our developer machines, it was hard to tell how much of a problem that these native dependencies would cause.
Participant 2: I wasn't quite clear on, was the reason for you to take out SQLite because the other developer found somewhere in the documentation that that was not the right thing to do or did you see some users being impacted by the use of SQLite as well?
Adam Wolff: It's a combination of things. To be clear, it's not just like, here's a bug in SQLite that is not workaroundable. It's more just like, when you look closely at what you get from this abstraction, it's not giving you what you really wanted, which was safety. Sure, I could sit down and we could puzzle it through and write some code that tests it out, but that's not what I wanted. What I wanted was something bulletproof that would make it easier to deal with multiprocess concurrency, and this was not hitting that far.
Participant 3: When you're switching back from SQLite to JSONL, you mentioned there are some limitations and issues. Could you talk more about like, what are some of the challenges that you see and what are some of the things that you guys have done to solve these problems?
Adam Wolff: The conversation is actually more complicated than you might think. It's a DAG. It is not linear, because you can go backwards in the conversation and branch. There are a bunch of ways you can do that. The basic data integrity guarantee that you want is that each message has one and only one parent. We can't actually make that guarantee, and you'll see bugs in the resume menu because of this. The other thing that just bothers me, I haven't really seen it in practice, but the other problem that you have is like, you actually aren't guaranteed that file writes are atomic. We're appending to a file. If those messages get too long, they could get buffered and interleaved, and you could end up corrupting lines in your file. I still don't know how big a problem this is in practice, but I know that's a landmine that's waiting for us for sure.
Participant 4: How do you use the tools, your relationship between yourself and the AI generating your code? Because, clearly, you're making a lot of these architectural decisions. You're driving the simplicity, or you're driving the features. When you go out to implement one of these features, do you just give it a prompt and let it run, or do you shape the whole process?
Adam Wolff: There's a lot of technique that comes with using these agentic tools, and the main point I want to make is that my technique is always evolving. Just a couple weeks ago, I did a little experiment where I had Claude look at all of the saved conversations in the .claude directory, and point out what prompts lead to lots of autonomous work, and what prompts don't, and how do I know when a conversation's reaching a dead end? Claude actually had a bunch of good points it made. If you give a design requirement along with a constraint and the reason why, you get much better output than if you just say, do this thing. It also said whenever I get to the point where I'm saying it's not working, I should just quit the conversation, because you need to take a new approach.
If you just find yourself saying, "We tried that, it didn't work". You're not going to get very far. You need to have a fresh approach. The meta here is you need to keep trying to evolve this and keep trying to use the tool better. Personally, I usually start by saying, "Claude, we're working on persistence for these conversations. Let's brainstorm some ways this could work. What should our steps be?" I usually have an idea in mind and I guide the conversation, but I also like to shape that process. The techniques will keep evolving as the model frontier moves, but the important thing is to stay awake to what you're doing. It's really easy to basically have a bad or abusive relationship with Claude. You need to really think about how you're treating Claude and how Claude's treating you.
Participant 5: How have your failures shaped your prompting practices in how you approach new problems?
Adam Wolff: Sometimes I will be looking at main and I'll be like, what is this crap code? How did it end up in here? Then everybody else is like, it's my PR? Because like, it's very hard to force yourself to review every single thing that Claude writes. I also have gotten in little lazy places where I stopped using my editor, I tried to use Claude even to make simple variable renames and stuff like that. That's a mistake, I think. There are a lot of cases where you can be faster doing something yourself or changing one part and then having Claude come back and do the rest. I've definitely had data spelunking episodes where Claude and I both hallucinated that we had some gigantic bug that was slowing us down. Then this led me on a wild goose chase. I've become a little more skeptical. I look for multiple signals that I'm on the right path.
Participant 6: You have described a great way how to develop very fast with AI, but you also worked at Robinhood, in finance. How do you see methods like these where you unship things and just try things out in something like the finance world where you have a lot more compliance and red tape to work with?
Adam Wolff: I haven't thought in depth about this. The one thing I'll say is like, there's so much we build that is not the product we ship to production, and all of those things can be optimized with AI. Every single thing you do can be assisted by AI, whether it's having a custom Slack bot, or having a really nice PR review process, or automated deployment scripts, you name it. Probably, if I were in finance, the very first things I'd go after would be all of the internal tools. Those are less under the enthrall of compliance. There's so much juice there in terms of what's actually time consuming when you work in finance. So much of it is these human processes that can be accelerated with AI.
See more presentations with transcripts
```

---

## 11. Applying Best Simple System for Now for Software Design

- 日期: 2026-05-07 11:43
- 链接: https://www.infoq.com/news/2026/05/best-simple-system-design/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
Choosing between building up technical debt and missing delivery deadlines is a false dichotomy, Daniel Terhorst-North argued in his talk Best Simple System for Now at GOTO Copenhagen. Programmers love to generalize rather than solve the immediate problem at hand, which can make future changes difficult. Instead, we need to build the skills and instincts for keeping things simple.
Many programmers think they continually have to make a trade-off, racking up technical debt to meet a deadline or pushing back on deadlines imposed by management or commercial folks so they can have the time to "do it right":
With the right trade-offs and design decisions, you can have a shippable product all the time, while keeping the quality bar high enough.
The Best Simple System for Now (BSSN) fulfils three characteristics, Terhorst-North explained:
- It has no extraneous or speculative code, just what is needed for now ("Simple"). The design is "future-proof" in the sense that changes are easy because it is so simple, not because we put extension points wherever we thought things might change.
- It meets all the current requirements ("for Now"), while carefully ignoring or deferring any future needs.
- Any code that is there is written to a suitable standard ("Best"). For production code, this means telemetry, automated tests, API documentation, automated path to live, etc. For "sketches" where you are exploring ideas, the bar can be lower. But in either case, there is no excuse for poor naming, unnecessary complexity—large source files, unwieldy methods or functions, poor file structure, etc.—that "good habits" cannot take care of.
Terhorst-North referred to a description of the skills a witch needs by Terry Pratchett in one of his Discworld fantasy novels Wintersmith:
First Sight and Second Thoughts, that’s what a witch had to rely on: First Sight to see what’s really there, and Second Thoughts to watch the First Thoughts to check that they were thinking right.
Designing for now involves first sight: seeing what is really there, Terhorst-North said:
Do we need a rules engine, or is this just half-a-dozen if-statements in a trenchcoat? Is Azure-hosted kubernetes the right deployment platform for your internal web app with its 10 users?
Programmers love to generalize, which introduces layers of complexity that we have learned to ignore. We have lost our first sight, Terhorst-North argued. This can make future changes difficult, especially if they are in a direction we did not anticipate.
The advice from Terhorst-North for keeping things simple is to just try it, knowing you will get it wrong time and again. You will overthink, over-code, and overindex in one direction or another while you build the skills and instincts of keeping things absurdly simple.
Mostly bad habits and learned behaviours inhibit people from designing simple systems that focus on the essence, Terhorst-North explained:
As a programmer with decades of experience, I have a huge ego, and I am convinced I know a lot about programming, so I find it difficult to admit that I will be close-but-wrong whenever I try to predict the future direction of a product or codebase.
Even though he tries to adhere to BSSN habits whenever he writes code, he still finds himself overthinking or over-engineering a solution "just in case", Terhorst-North said:
The only way through this that I have found is to practice, practice, practice! In my case, I find I am a lot more honest when I am pairing; my pair stops me from gold-plating, or challenges my assumptions about where we are going next, in a way that keeps me on track.
Before he knows it, he is neck-deep in yet another optimization they will never need, or adding another interface or flex point that will never be exercised, Terhorst-North concluded.
InfoQ interviewed Daniel Terhorst-North about the best simple system for now.
InfoQ: You advised against anticipating the future in any way. Why?
Daniel Terhorst-North: This is the crux of designing for now. A product could change in all kinds of ways at any time and for any reason. I call these "dimensions of change".
Here are some examples:
- Many additional types of report but we chose a domain-specific reporting tool with huge domain flexibility that can’t connect to all these additional data sources
- Many variants of the same report, but adding a new variant is expensive and time-consuming because we locked that down "for performance reasons"
- Increased report complexity because compliance needs data provenance, but this will massively slow down report generation because we optimized for scale rather than detail
- We want a dashboard instead, so the "report" is going to be evaluated dynamically
These are not hypothetical; all of these have happened to me! Whichever of these possible futures we predict or preempt in our design, we are making trade-offs against the others and introducing complexity entirely speculatively.
My position is that the key to real "flexibility" and "scalability" is to keep things as simple as possible so you can pivot towards the next change, whatever it is.
InfoQ: What can be done to keep our systems simple and best?
Terhorst-North: I advocate for "fake it ’til you make it", or rather, "act your way to a new way of thinking". You cannot convince someone that it is possible to continually keep a system simple, nor can you convince them that any future change will be easier the simpler the codebase is; they have to experience it for themselves, several times. Ironically, the more experienced the engineer, the harder they find it to believe that they should not be anticipating the next dimension of change. After all, isn’t that the point of all that experience?
I no longer obsess about whether I have the "right" design. I am confident enough in my habits—TDD, version control, refactoring, "sketching" code—that I know I can back out any poor decisions quickly enough and set off in a different direction. I have also taught myself to not believe my inner monologue when it tells me it "knows" what is coming next.
```

---

## 12. Google Announces GKE Agent Sandbox and Hypercluster at Next '26, Positioning Kubernetes as AI Agent

- 日期: 2026-05-07 10:06
- 链接: https://www.infoq.com/news/2026/05/gke-agent-sandbox-hypercluster/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
Google has announced several major updates to Google Kubernetes Engine (GKE) at Cloud Next '26, headlined by GKE Agent Sandbox for secure agent code execution and GKE hypercluster for managing up to a million accelerator chips from a single control plane. Drew Bradstock, senior director of orchestration and Kubernetes product management, and Gari Singh, GKE group product manager, write:
Kubernetes has rapidly become the operating system for the AI era, with GKE now powering AI workloads for all of our top 50 customers on the platform, including the largest frontier model builders.
The framing reflects a broader industry trend. Multi-agent AI workflows have surged 327% in recent months, according to Databricks, and 66% of organizations now rely on Kubernetes to power generative AI applications and agents, per CNCF data.
GKE Agent Sandbox provides kernel-level isolation for untrusted agent code execution using gVisor, the same sandboxing technology that secures Gemini. Google claims 300 sandboxes per second at sub-second latency and up to 30% better price-performance when running on Axion compared to other hyperscale clouds. Agent Sandbox launched as a Kubernetes SIG Apps subproject at KubeCon NA 2025 and introduces three new Kubernetes primitives: Sandbox (the core workload resource), SandboxTemplate (the security blueprint), and SandboxClaim (a transactional resource for requesting execution environments from higher-level frameworks like ADK or LangChain). Warm pools of pre-provisioned pods reduce cold start latency to under one second.
Lovable, whose platform supports 200,000+ new AI-generated projects daily, is running production workloads on Agent Sandbox. Fabian Hedin, co-founder of Lovable, noted:
GKE's cutting-edge sandboxing capabilities allow us to reliably scale to hundreds of secure sandboxes per second, ensuring we can seamlessly empower builders, even during massive, unpredictable demand.
The agent sandbox space is becoming a three-way competition between approaches. Cloudflare recently shipped Sandboxes GA using container-based isolation on its edge network, alongside V8 isolate-based Dynamic Workers for lighter workloads. E2B uses Firecracker microVMs. Notably, as Alex Gkiouros, a Google Cloud Ambassador and staff architect, observed, GKE Agent Sandbox is currently the only native agent sandbox offering among the three major hyperscalers. Google's broader bet is that Kubernetes itself should be the agent runtime, with gVisor providing isolation as an open-source Kubernetes primitive rather than a proprietary platform feature. That open-source angle is the key differentiator: any Kubernetes cluster can run Agent Sandbox, not just GKE.
GKE hypercluster, now in private GA, addresses a different scaling problem. As AI training demands grow, organizations fragment their infrastructure into hundreds of disconnected clusters, creating operational overhead. Hypercluster lets a single, conformant GKE control plane manage a million chips distributed across 256,000 nodes spanning multiple regions. Security relies on Google's Titanium Intelligence Enclave, a hardware-attested, "no-admin-access" model where proprietary model weights and prompts remain cryptographically sealed from platform administrators.
Gkiouros noted a practical concern worth weighing in:
A single GKE control plane managing a million chips across regions sounds wonderful until you think through blast radius and change management. Private GA is the right place for it.
On the inference side, two improvements ship concrete performance gains. Predictive Latency Boost in GKE Inference Gateway uses ML-driven routing to reduce time-to-first-token latency by up to 70%, replacing heuristic guesswork with real-time capacity-aware scheduling. This capability is built on llm-d, which recently became an official CNCF Sandbox project. Automatic KV Cache storage tiering across RAM, Local SSD, and Google Cloud Storage solves long-context memory bottlenecks, with Google reporting a 50% throughput gain for 10K prompts offloaded to RAM and a nearly 70% throughput improvement for 50K prompts offloaded to SSD.
Additional updates include RL Scheduler for optimizing reinforcement learning workloads, RL Sandbox for kernel-isolated reward evaluation, and intent-based autoscaling on custom metrics, which reduces HPA reaction times from 25 seconds to 5 seconds by sourcing metrics directly from pods rather than external monitoring stacks.
```

---

## 13. Leading Open Source Author Calls for Verification over Trust in Software Supply Chains

- 日期: 2026-05-07 07:00
- 链接: https://www.infoq.com/news/2026/05/stenberg-curl-verification-trust/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
In a blog post published in March 2026, Daniel Stenberg, creator and lead developer of curl, makes the case that the software industry's default position of trusting well-known components is no longer adequate. Stenberg argues that users and organisations should actively verify the software they consume, and he uses curl's own practices as a concrete example of how that can be done.
Curl runs in an estimated tens of billions of devices, making it one of the most widely deployed software components in existence. Stenberg lists a range of scenarios in which a project at that scale could be compromised, including a malicious contributor merging tainted code, a breached committer unknowingly distributing modified releases, an extorted team member making unwanted changes, or a hacked distribution server serving altered tarballs. He notes that these scenarios can occur independently or in rapid sequence, and that the consequences of a successful attack on a project of curl's reach could be severe.
"Software and digital security should rely on verification, rather than trust. I want to strongly encourage more users and consumers of software to verify curl. And ideally require that you could do at least this level of verification of other software components in your dependency chains."
- Daniel Stenberg
The curl project has put in place an extensive set of controls intended to make the git repository the authoritative and auditable source of truth. These include enforcing a consistent code style, banning the use of certain C functions deemed difficult to use safely, imposing a ceiling on function complexity, requiring human and automated review of all pull requests, and prohibiting binary blobs and most uses of base64-encoded content, both of which could be used to conceal malicious payloads. Stenberg also describes more than 200 CI jobs that run on every commit, builds using strict compiler settings that treat warnings as errors, continuous fuzzing via Google's OSS-Fuzz project, and mandatory two-factor authentication for all committers. Each of these is designed to make any deviation from expected behaviour visible to anyone following the project.
On top of those internal controls, Stenberg makes the case for a wider verification ecosystem. He explains that the project provides signed release artefacts and a dedicated verify page on the curl website, so that independent users can check that a release contains only what is in the git repository and that it was signed by the release manager. He acknowledges that he cannot know who those users are, or whether they currently exist, but argues that even a small number of independent verifiers is enough to provide a meaningful check: one of them can raise the alarm if anything looks wrong.
"If even just a few users verify that they got a curl release signed by the curl release manager and they verify that the release contents is untainted and only contains bits that originate from the git repository, then we are in a pretty good state."
- Daniel Stenberg
Stenberg ends his post with a direct recommendation to require this verification for all dependencies, stating that "software and digital security should rely on verification, rather than trust". Community discussion from before April 2025 echoes this position in several ways. On LinkedIn, practitioners in security and platform engineering have argued that the XZ Utils backdoor, discovered in 2024 and involving a long-running effort to insert malicious code via a trusted contributor, showed the limits of reputation-based trust, such as in this post from Cameron Stihel and this post from Ryan Johnston. The attack, which targeted the liblzma component by gaining the confidence of maintainers over time before inserting code changes, is precisely the kind of scenario Stenberg describes in his list of threat vectors.
One of the structural tools now available for expressing exactly what a piece of software contains is the Software Bill of Materials. In a talk at QCon London 2026 covered by InfoQ, Viktor Petersson, founder of sbomify, argued that teams are running out of time to adopt SBOMs. He cited the EU Cyber Resilience Act, which opens its first enforcement window in September 2026 and requires full SBOM compliance by December 2027, and warned that its consequences go beyond fines: "CRA is not about fines. They can actually block sales. Your products can be blocked from the European market." US Executive Order 14028, in force since 2021, makes SBOMs a procurement condition for software sold to the federal government, and the FDA requires them for medical devices.
Petersson's talk addressed the full lifecycle of SBOM production, including the step that most teams skip: signing. He was direct that this is a mistake, and that the specific tooling matters less than the act of signing itself, as this provides a verifiable chain of custody. Petersson was blunt: "Any signing is better than no signing. Do sign your SBOMs in your pipeline, not on somebody's machine." This connects directly to Stenberg's argument: curl already provides signed release artefacts and details the verification steps clearly, giving consumers the chain of custody that Petersson describes as the goal.
CI/CD pipeline are also a potential weak point. InfoQ covered the compromise of a widely used GitHub Action in April 2025, which highlighted how a single malicious or compromised action can expose secrets and build artefacts across many projects simultaneously. The incident reinforced calls for tighter controls on third-party actions, pinning dependencies to specific commit hashes, and monitoring for unexpected changes in CI tooling. Stenberg's approach addresses this directly: the curl CI jobs are configured to access the source repository read-only and are checked with the zizmor tool to reduce the risk of insecure job configuration.
Petersson also pointed to the lifecycle challenge, noting that a real product often has dozens of SBOMs that change on every CI run and that regulators can request the SBOM for a specific past release. He compared current practice to software development before version control: "Dealing with SBOMs today feels like managing source code in the 90s, with patches sent over email." This governance issue leans into Stenberg's broader point. The tooling to produce, sign, and verify software artefacts exists, and the regulatory pressure to use it is building, so organisations should close the loop by verifying what they consume.
```

---

## 14. LinkedIn Consolidates Hiring Data Pipelines to Power AI Driven Talent Systems

- 日期: 2026-05-06 14:15
- 链接: https://www.infoq.com/news/2026/05/linkedin-unified-hiring-platform/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
LinkedIn has introduced a unified integrations platform designed to standardize and reconcile hiring data across disparate systems, improving data quality, partner onboarding speed, and enabling downstream AI applications. The multi-year effort consolidates fragmented recruitment data pipelines into a consistent and scalable foundation for talent products and AI-driven features.
Recruiting at LinkedIn operates at a significant scale, ingesting data from applicant tracking systems, career sites, and job boards. These sources often produce inconsistent schemas and incomplete records, creating challenges for downstream analytics and product features. The platform addresses this by introducing a unified data model and integration layer that standardizes ingestion, reconciliation, and delivery of hiring data across systems.
Gaurav Sisodiya, engineering lead at LinkedIn, highlighted the design approach in a post, stating,
We designed for coexistence, not replacement.
According to LinkedIn, the platform has reduced partner onboarding time by 72% while expanding data coverage and improving completeness. This allows external partners and internal systems to integrate without requiring custom transformations, replacing previously siloed pipelines with a shared infrastructure.
We developed a unified integrations platform to standardize, reconcile, and deliver hiring data at scale.
At a high level, the architecture is organized into three layers: standardization, orchestration, and enhancement. The standardization layer normalizes incoming data from heterogeneous sources into a consistent schema, abstracting differences across applicant tracking systems and job platforms. The orchestration layer manages workflows for ingestion, validation, and reconciliation, coordinating data movement and enforcing quality checks. The enhancement layer processes normalized data to address gaps, deduplicate records, and augment signals before making them available to downstream systems.
High-level architecture (Source: LinkedIn Blog Post)
Aditya Hegde, engineering at LinkedIn, described the underlying workflow in a post:
Under the hood: Temporal-orchestrated workflows, Kafka streams, record persistence in Espresso, multi-mode orchestration, and declarative schema/ID mapping enable replayable, bidirectional sync and safe evolution.
This structured data foundation enabled LinkedIn engineers to build a perception and action interface for the Hiring Assistant. Standardized hiring data allows AI systems to interpret signals across candidate profiles, job requirements, and recruiter interactions. The system aggregates signals and translates them into recommendations, automation, and decision support within recruiter workflows.
Ritvik Kar, product at LinkedIn, noted the importance of system reliability, stating,
This is key without a highly reliable, observable, stable system that can deliver on high data availability and consistency across read and write, there’s no way for our customers to trust our platform and do their work seamlessly.
LinkedIn reports that the unified platform reduces duplication across integration pipelines and simplifies maintenance by centralizing data processing. The approach also improves data consistency for downstream analytics and AI systems that depend on shared hiring data across multiple sources.
```

---

## 15. Presentation: AI-First Software Delivery: Balancing Innovation with Proven Practices

- 日期: 2026-05-06 11:12
- 链接: https://www.infoq.com/presentations/ai-first-practices/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

```
Transcript
Wes Reisz: My current project, I am on what is called an AI-first software delivery project for Thoughtworks. What that means is we're shifting left AI in all we're doing with the SDLC. What I'm going to be talking about today primarily is focused on coding agents and how we're leveraging them. Before I get into that story, I should back up a bit. At Thoughtworks, we're a consultancy. We typically go into companies, partner with teams. We use their infrastructure, we use their environment, and we build software there. I'm challenged with shifting left AI with this team that we're in. The team's about 16, it's not a very large team. I'm using the infrastructure that's present with the client. I'm using a lot of the systems that are there. A lot of times we have to uplift the client.
All the time, I'm constantly asked why I'm not using a full multi-agentic approach with how we're delivering software. What this talk is really about is how I answer that question. Specifically in the context of meeting the client where they're at, meeting customers where they're at, understanding our level of domain knowledge with the environment that we're operating in and the tools that we're working on. This talk is specifically about that particular journey and how I try to answer that question.
Background
My name is Wes Reisz. I am a technical principal, technical partner at Thoughtworks. Again, what that means is I get to change clients all the time. It's a lot of fun. I usually go about 9 to 12 months with a client. About three months ago, we picked up a new client. This particular one is a large state in the U.S. What we're doing is building a knowledge graph. We're looking at different rules, regulations. We're ingesting those rules and regulations and building a knowledge graph with a deep research agent to be able to allow some of their systems to be able to interact with a modern UI, AI type interface. That's what we're building. To do that, we're using an AI-first software delivery approach. We're shifting AI as left as we can when it comes to building. What that means is we're using specifically Claude Sonnet 4.5 with Cursor, in my team to be able to use an approach that's very AI first. I'll go through some of that here today.
This is the entire talk. AIFSD, AI-first software delivery is not a one-size-fits-all. Choose your approach based on a few things. The two things that I'm going to talk about in particular are code longevity and automated verification. These are two axes within a two-by-two that I'll use to help answer this question of why I use a supervised approach with coding agents and not an unsupervised multi-agentic approach with the team that I'm at for the client that I'm working with now.
The second key takeaway is use a structured approach when working with LLMs. Has anybody ever heard of RIPER-5 by chance? RIPER-5 is an approach that you can put the LLM in a partnering mode, by giving it different instructions. I'm going to go through RIPER-5, and I'm going to specifically show how we're partnering, how our teams are working with the LLM and not stepping back and waiting till after the code has been written and only looking at a PR. We're using our practices that Thoughtworks believes in which is pair programming. We're using continuous delivery. We're partnering with the LLM in this RIPER-5 approach. I'll talk about that. Then, last but not least, AI doesn't replace engineering discipline. You've heard that through talks throughout the entire day. What it does though is amplify your practices. If you have bad underlying foundations, AI will absolutely amplify those. If you have good ones, it'll amplify those as well. These are the key takeaways. This is what I'll be talking about today.
Outline
The agenda is specifically about considerations for AIFSD. This is that two-by-two model that I was talking about. How I try to answer that question is, why aren't you using this approach, or why are you using that approach? My goal for this talk, regardless of where you're at in your journey with AI, for you to be able to leave, go back to your shop and be able to apply techniques that I'm talking about. Whether that's you haven't touched agentic development or whether you're building agentic solutions today. I want you to be able to take some things back to be able to take to your shop. I will talk about engineering rigor, engineering discipline coupled with AI. Then I'm going to put it all together and show implementing an MCP server using the RIPER-5 approach that I specifically talked about.
Considerations for AIFSD
Considerations for AIFSD. You cannot be anywhere right now in the software industry and not see slides like these. This is an IDC slide that says by 2029, 26% of the worldwide IT spend will be spent on agentic AI. 26% is $1.3 trillion. I don't know about you, but I can't get my mind around what $1.3 trillion looks like. I just can't actually think of something that size. The way I try to put this in perspective, if you think of a $100 bill, just a simple $100 bill U.S., it's about 6 inches large.
If you were to take that $100 bill and stack them end to end, $1.3 trillion would circle the earth 50 times. That's a lot of money being spent on agentic AI. Have you seen MIT's report that says 95% of AI projects fail to deliver on ROI? We're spending $1.4 trillion on it, yet 95% are failing? What's going on? What is happening if this is the case? What I would propose is that we're not always modeling, we're not always mapping our use of agentic AI to where we are as a company, or we're meeting our client, our company, where we're at when we're applying these solutions. What I did is I put together a two-by-two model to answer that question that I described before.
I'm going to show that, but before I do, I want to acknowledge the fact that when you look up here, you will disagree with something. I promise you, you will. I disagree with something that's up here. That's ok, because models are nothing but a map for us to have a conversation, to be able to establish common dialogue. My map, my model that I use is this. This is a simple two-by-two, and on the y-axis you see longevity. How long will this code live? Is it short-lived, or is it long-lived? Is it going to be in production? Is it going to be facing the customer for some period of time? Down on the x-axis, I talk about degree of automated verification. Specifically, can you verify the thing that you're writing? If you can't, we need to do things in a more supervised approach.
Once you've established domain knowledge, you can do things more in an unsupervised approach. Let's walk through these different quadrants here. In the bottom left is exploratory development, aka vibe, the misquoted vibe coding that came from March? It seems like it's been around forever. March of 2025, Andrej Karpathy said this now famous tweet that's misquoted, but it talks about vibe coding. I vibe every single day.
If I'm talking to a client, and they're telling me about a problem, I let them talk to my product person for a few minutes, and then I start trying to put a solution together. Then I go, is this what you meant? The best answer they can give me is, "No, not at all. That's completely wrong. Please don't ever do that again". Great, I'll put it away, and I won't do it again. I got great information about it. I was able to get immediately what they're looking for or not looking for in that particular case by just doing a simple experiment. POCs, doing a small R&D, all these things I use just to be able to understand the scope of something that I'm doing. I do it every single day. Do I put it in production? No, of course not. I use it as a way of gathering information, looking at data maybe, or spinning some information in a way that I can do it. It's a valid approach for me to be able to gather information, but it's not how I go about delivering software in a client environment.
In this case, it's short-lived, and I lead it. I'm very human-centric. That's that lower left quadrant. Let's move to the right across that bottom for that degree of automated verification heading on the y-axis into domain sensing. These are things where I use deep research agents. We've all gone out there and used one of the LLMs to be able to do deep research. I can do those outside the firewall. I can also do them inside the firewall to understand legacy codebases, to understand a problem when I'm coming into a client cold to be able to understand what I'm coming into. What are their boundaries? How do they think of domain-driven design? Where are their seams? Where can I introduce seams? What types of patterns do they use? I can use background domain sensing agents in those particular cases to understand the environment that I'm working in so that I can begin to make choices. This is information for me. It's not necessarily going to be around a long time other than the fact I'm gaining information with this. That's degree of automated verification. It still needs to be safe, so we have high degree of auto verification.
Before we move to that top left quadrant, this is the area that I'm going to primarily be talking about today in this talk. This is about supervised and unsupervised coding agents in particular. On the team that I'm working on now, we're specifically focused on supervised coding agents. Why? Because three months ago, I put this team together. We came to a client to solve a particular problem. We know very little about the domain. We have to understand how to evaluate the domain before we can start to really build autonomous coding agents that go off and do things. We have to be able to understand how to do it safely, put guardrails around them, how to establish identity to those things. All these things have to be done so we take a very supervised approach to it. As we've now started to gain domain experience, we're moving to the right with unsupervised agents. We're beginning to do background tasks with simple code validators, doing things like checking our specifications that I'll do. We're starting to build these things.
As we go forward, we'll be able to move more and more into unsupervised agents. The key that I'm trying to get here is that AIFSD, how we approach delivering software, isn't a one-size-fits-all solution. Just because everything isn't an unsupervised agent doesn't mean you're not using AIFSD. I put this quadrant together to understand different tools, different techniques that you may have in each one of these particular areas. This is how I try to answer the question about why aren't you using a fore agentic loop in building your software today? I answer it because I don't have enough domain knowledge to build the degree of automated verifications. I need to do it safely. As I gain that, I'm able to do more of it. The bottom line, the TL;DR here is AIFSD is not a one-size-fits-all solution. You fit the solution to the domain that you're working in. Choose your approach. The two things that I use, there's other ones that you could potentially use. As I said, you may use other things on the x and y-axis, but understand what are the things that you want to do. What are the options that you have? Then pick the approach that works best for your particular environment.
Engineering Discipline and AI
The next thing I wanted to talk about is engineering discipline and AI. One of the things that's missing when we work with LLMs is the predictability. To be quite honest, if we had predictability, if we had determinism, why would we use them in the first place? The whole point of it is that it is not giving us the same thing every time. If it was, we'd call it a pure function. We'd give it something, and we'd just get the same output every time. The very fact that an LLM can give us something that is non-deterministic in nature is the power of what we're doing. We need to be able to map that up into a structured way for us to be able to deliver in something that is repeatable, even if non-deterministic.
The first thing that I'll talk about is spec-driven development. Everybody's coalesced around spec-driven development these days. A colleague of mine, Birgitta Bockeler, out of Germany, she wrote a blog post on martinfowler.com, where she dove into some of the spec-driven kits that are out there, like Kiro, Spec Kit, Tessl. These are all definitely ones that you can use to be able to adopt. What I'm going to approach today is just simple Markdown files with specification that you can use at your shop Monday morning. This is nothing special that you can do. You absolutely can use tools like these, but you don't have to to get started on an AIFSD approach.
In this blog post, she also talked that when we say spec-driven development, we actually mean different things. There are three different approaches, spec-first, spec-anchored, and spec-as-a-source. Spec-first is where you create a spec and generate the code from it. Spec-anchored is you create a spec and it informs the creation, you keep the spec around. Spec-first, you get rid of it. Spec-anchored, you keep it around and then you use it to inform the code that you're writing. Then spec-as-a-source, the code is a byproduct. You're only actually updating the spec-as-a-source. I haven't had tremendous success personally with spec-as-a-source. I use spec-first where we generate it and then code is the thing that we produce. That's the approach that my team currently uses.
I did a podcast with a couple of engineers that are speaking here at QCon AI, and Prince Valluri from LinkedIn made this comment about the spec that really resonated to me. He said, a spec is the contract between the developer and the LLM. That made total sense to me. If you're going to be interacting with an LLM to generate code, the spec allows you to define that contract. Clearly, the boundaries are what you're looking for, what you're trying to get from this particular execution with the LLM. Good contracts need good rules. What do you put in a spec to make it good? This goes back to December of last year. These are a couple of the founders for Databricks, Ion Stoica and Matei Zaharia. Matei actually spoke at QCon AI a few years back, the last one that we had. What they talk about in this particular paper is some of the things that should go into a specification to make it really useful. There are five things in particular that I try to focus on. I don't use this on every single spec, but I try. This is what I attempt to do with each of my specifications.
The first one is a proof carrying output. What can you put in a spec that it can verify itself, that it can say that it is correct? For this, I do think like end-to-end tests. When I create something, I'll have a test that gets created that end-to-end validates what the actual specification did. Step-by-step verification, the first part is step-by-step. One of the things we know as software developers is to break problems down into smaller pieces. What this tells me is break things down into smaller problems and then verify as you go through. What I read when I see this is steps and then BDD. I introduce behavior-driven development into our specification so that we can actually test, before we actually write the code, the behavior that we're looking for. Why do I say it that way? You've all worked with an LLM and you've had it generate tests. When you have it generate tests after the code is written, it tends to fit the test to the code and they become incredibly brittle.
If you start with things like BDD up front in your specification, you've done that before. It's test first. This is the approach that we're trying to use to some effect. Execute and verify is the verify step. Once you create the code, verify your outputs are doing what it's supposed to be doing. Pre-conditions, post-conditions, very familiar to us. What must be true for this to start? What must be true for it to stop? Then statistical verification is these things are non-deterministic. We've all heard the stories even today that run it six times, you'll get six different outputs. That is true. How do we still deal with validating what we have when we get this type of output? Statistic verification are things that we can add. That's one that I don't tend to do a lot of. The first four, I do quite a bit of. These are things that I try to put in our specification to give us a more repeatable behavior when using an LLM to help us in AI-first software delivery that generates code with coding agents.
You've all written code where you wanted to do something really simple and you're working with an LLM. Because your rules files, because of maybe other things that you have in place, it goes really deep. You get layers and layers of abstraction, and you're just trying to understand the problem space or just trying to do something really simple. It's taking you too far. What's missing is being able to put the LLM into the mode that you're in, the mental model that you're in when you're working with the LLM to put you both on the same level when you're interacting with it. What we use to help us with that is something we call RIPER-5. Actually, we did name it. It comes from a blog post around earlier this year, March 2025, someone named robotlovehuman, whoever that is, posted this out on the Cursor forums. This is something we picked up. What RIPER stands for is Research, Innovate, Plan, Execute, and Review. What we do with this approach is we take a specification that we just talked about. We put our well-defined things that are in it that I talked about, the five different things at the bottom that we want to do.
Then we go into a research mode which is basically a way of passing instructions to the LLM that says your goal is to gather context right now, read files, but don't code. Your job is to really focus on understanding. Ask me clarifying questions about what needs to be done so that I can provide feedback and I update the specification for it. That's research. From the research phase, it goes into innovate, and that's where you say, give me three options. How might I go about implementing this? Then you use those three options to be able to pick one, add that back into your specification.
From that, I go into plan. Plan is where we take that specification, break it down into individual tasks just like you would prior to AI and a scrum team with your team, and saying, here's a story. What are the different things I need to do to implement this so that anybody could pick up that story? You task it out, but you use the LLM to help you do that. Once you've tasked those out, you plan each of those tasks, you execute, and then you review. That's the RIPER-5 model. I'm talking about doing this in a supervised mode. I'm specifically talking that upper left quadrant where developers are pairing with the LLM to do this. This process could absolutely be used when we shift to the right on that using an unsupervised approach. This is the model that we follow in putting the LLM into modes that we're operating at, whether that's with a background agent or whether that's in the foreground.
What's as important here is what you can do with RIPER-5 are the things that you're forbidden to do. This is actually a really big, important point. When you're in this research stage and you're gathering information, you're understanding the codebase, you're having the questions asked of you to provide feedback, you also want to forbid it what it can't do. It cannot suggest, it cannot plan, and it cannot code. At this point, all you're doing is research. Innovate, you're forbidden to plan, do decisions or code. In the planning, that's when you are forbidden to implement code. It's only when you get to execute when you actually write the code. In that point, you're forbidden from deviate. What's interesting about this is you see the tools today like Cursor actually adopting these too. They've introduced debug mode.
About a month before that, you formally saw plan, to plan and act. That's what this is doing. It's putting the LLM in that mindset, so that it's working with you as you're interacting with it. It's not jumping ahead and creating that fully abstracted solution where you've lost the solution in the weeds that's actually being implemented. Then, finally, in the review, you're forbidden from skipping checks. This is where you validate that what was created is what the plan actually was. This allows you to look for drift and say, this is what you wanted to do, that contract. This was your contract. This is what actually got implemented, and what's the difference. That's what review gives us. That's the RIPER-5 mode that we leverage on our team.
What does that look like in practice? It starts off with the rules file. Again, for this particular project, we decided to standardize in Cursor. The examples you'll see here are mostly in Cursor, but these completely apply to Claude Code or to Windsurf, or any of the other tools that are out there. It just may be AGENTS.md versus the rules file that are here. Up here, this is my rules, my commands. This is in a submodule that I have and I basically have the team check it out. It's available so that we can share it. You can also share these things inside of the Cursor environment, but we didn't want to specifically do that because we might have wanted to shift at some point to something else. This is where we set things up.
The next part is where we develop our specification that we're going to actually implement. From there, we go to that research that I showed you. Research is where we ask questions. Innovate is where we go through about different options for the implementation.
Then plan and task is where we break down that specification into individual tasks and then plan those tasks. Then from there, we execute and then we review. That's the process that we follow with RIPER-5. Nate Schutta is one of my colleagues at Thoughtworks. I showed him this as doing a prep for the talk. He said, you know what really resonates with me about that is that process that you just showed. I don't know that it has anything to do with AI. That's how I work anyway. That's exactly the approach that I work when I'm doing a specification. That's exactly how I work when I'm writing code. I understand the story. I break it down. I do some research. I do some innovation of how I might do this. It may not be a formal step, it's just something that I'm doing.
Then I break it down into what I need to do, and then I execute it and I check it. That's how I work. What I really like about this RIPER-5 is it codifies the way we already work. It allows us to do things to be able to work with an LLM or even build multi-agentic systems that leverage the same type approach.
We talked about RIPER-5. We talked about the four quadrants, about understanding where you're at. The next piece is what I said at the very beginning, that AI is a powerful tool. It amplifies your practices, good or bad. You need to make sure that your foundation is solid, and if it's not, you can cause a lot of troubles and issues. For example, we can generate code much faster than we can actually review. Things can scale exponentially with defects if we're not putting engineering rigor into our process. Architecture boundaries can leak because maybe we don't have the evaluations in the system enough to verify that we're having good boundaries between the systems that we're building and we get leaky abstractions. We need to understand enough of the domain to be able to make sure we're building the system right before we just build on purely based outputs. You can get into traceability issues in regulated environments, things like that. You want to be able to have guardrails to be able to put things in place. I work for Thoughtworks.
One of the things that we practice is something called our sensible defaults. Sensible defaults is whenever we set up one of these accounts and we go in with a new contract, we start with these defaults. This is our starting point. We may not use all of this because we're meeting a client where they're at. They may have some kind of environment that doesn't allow us to do continuous deployment. This is our sensible defaults. This is where we start from. Everybody shares these same beliefs. There are things like continuous integration, test-driven development, pair development. Let's talk about pair development. I get asked a lot, why are you pairing? The LLM is your pair. No, the LLM generates output based on the average of what it's trained on. The LLM is a tool that we use to help us. Also, what we're finding is that when we generate code, it is exhausting reviewing the amount of code that can get generated. The specifications are like 5 to 1 in the amount of specification and planning that goes into the code that actually gets written.
If you're doing all of that, it's exhausting reviewing it all. Pairs help us get through that to make sure that we're reviewing things correctly and we're getting the right output that we're doing. We also use trunk-based development. We're shifting that quality left and making sure we commit to main. Those type of practices, pair programming is what we continue to practice.
Other things there, building security to the left, automating builds, deployment pipelines, I mentioned continuous delivery, managing debt, and then of course, building for production is our goal. All of that gives us these things for fast feedback, repeatability, simplicity, and ultimately can tie directly to business metrics like the DORA metrics that we're all familiar with, MTTR, deployment frequency, lead time, and change failure rate. The second thing here is that AI doesn't replace engineering discipline, it amplifies it. What are your sensible defaults? Whatever those are, we have to continue to invest in them. We have to make sure whether it's a supervised or unsupervised agentic workflow, that we're building this on solid foundations so that we amplify those foundations.
Put it Together: Implementing
Let's put this together into an example. This is a workshop that I did at QCon London back in March. What this basically did is after every one of the talks during the conference, it would upload into S3, run a set of Step Functions that would transcribe the talk, break it down, put it into a vector database. It basically created naive RAG. You could ask questions. It was just a simple tool call. In this case I used ChatGPT, created a simple tool call where you could go in and say, what were the key takeaways from the platform engineering talk that was earlier today? You can see here, it makes a simple call. It's just a simple tool call, it's a simple API call. All it does is go back, it's a dense retriever. Types, sends this thing that you're seeing here off to the server, comes back, passes email, API keys, and things like that. Dumps that back into the LLM and gives me back a response. Very simple little tool call. Works great, but it's a one-shot. It does a single call that goes against the vector database. Very nice thing for QCon. What I wanted to do for this little demo is, let's take this and put it into an MCP server.
As an MCP server, now we get multi-turn. Now I can actually give a tool over to the LLM and say, here is a tool that you can get information about QCon to answer questions for it. Let's do that. I'm going to use this RIPER-5 approach to be able to walk through this and show you what that might look like. First off, this is just the README file. It has a ton of information because it's a public repo shared. It has how to set up the MCP server. You can see in Cursor how to configure that. Here at the bottom, it talks about how to set up a dev environment. There's some AIFSD principles that we try to follow. This talks about the RIPER-5 stuff that I just showed you a few minutes ago.
Then, here, we'll go down and we'll show how inside Cursor you can set this up, so that Cursor will operate with these RIPER-5. It gives you that planning type mode, but with each of the five steps. It also goes through here and talks about how you can do that submodule, set up rules, commands. These are things that, again, you probably saw in some of the talks about how to configure some of these things. This walks through some of the particular steps. That is the README file.
Let's jump ahead now and actually look at a specification. If we go into the specification, I used a free Jira account and named it SCRUM-5, whatever. This is the specification that I created. You can see architecture components. You can see acceptance criteria. Notice I did not use BDD here. Definition of done. Implementation tag. This is information that when I went through the research and innovate stage, I added to the specification based on the questions that were asked to me. All this is, is a simple Markdown file. That's all this is. It's capturing what I intend to do and establishing the contract of what I actually want to build. From here, now I want to go through and break this down into the tasks that I want to actually do. I've done research. I've done innovate. Now I want to go into plan.
The first step in doing that is to break these down into tasks. If you look here, it's just a file that lists each of the tasks. There's configuration. There's setup for the API. There's MCP server setup. There's testing. There's documentation. You see some of the dependencies for each one of these steps that are going to go through. Some different milestones that it created. A critical path. Success criteria. All this is the stuff we do intuitively when we're actually writing this. This is just breaking it down into a process that can be followed by an LLM and then ultimately by an agentic loop.
Once we've done that, and we've broken these down into all these individual tasks that we want to do, you go into a planning stage. That planning stage plans out what's going to be done. Remember, I said that in this stage we're using a supervised approach, which means my developers review this, verify what's here, and that first step up there in task 1, for example, this was a Python project. It didn't do a virtual environment. That wasn't part of anything that we specified. Our developers adjust the plan and say, no, I want a virtual Python environment before we get started and then have it start again. This allows us to put feedback and control and own each of the steps or the tasks along the way, even though we're using an LLM to be able to generate the code. From here you see the code that's actually generated.
If you look, of that code that's there, there's about 5, 6 files. Those are about 50 lines each. There's very few code that was actually generated. It's about 10 to 1 on the amount of things that were specification and planning versus the amount of code that's generated. I think this is a not-so-subtle point. Software is not just about creating for loops. It's the thinking that has to go in to create this MCP server so that I can actually pull this information in. It's about 10 to 1 on the code that's actually generated. LLMs do amazing things, but just generating fast code is not going to help us in creating production caliber software.
What does this look like, if we put it into it? This is Cursor. Up here I've registered the MCP server. Now I'm asking that exact same question that I did before. What are the key takeaways from the platform engineering talks at QCon London 2025? I went ahead and told it to use the MCP server that I just created just for clarity. It goes into thinking mode and it says, let me get some information. It could have done a better job of dumping that there to the screen. It goes through and does the first turn, asks another question. It's thinking using this tool. I only had one endpoint here, but there's other ones I could have added. It's going through here asking these questions. It got the platform talks first, then it asked for the key takeaways. This one's asking Lesley Cordero's talk about scaling organizations. This one is Rachael Wonnacott talking about autonomy and fit for platform engineering teams.
Then now it's like, I have enough information. I can put this together. Now it assembles the things and puts this back together. It's an MCP server that's actually implemented with RIPER-5 in here. This example is a toy. It's for a QCon that was there. Depending on where you are in your journey with AI, imagine if this was your architecture decision records. Imagine if this was the PRs that have been sent to the system. What if this had engineering context about what you're trying to build, and you're making this available to developers? I'm doing a migration, upgrading Java, something like that, and I want to see what were the files that were last touched. I can look at those things, validate what's there. Not only can I do that, as I start to move into those fully autonomous workloads, I can use those with my agents to have shared context. These are some of the foundations of memory that you can build with just a simple MCP server like this. That's what a tool like this can give you with this type of approach, all using RIPER-5 across that top line of that two-by-two.
Approaches to AI for Your Team
What did I talk about? I talked about considerations for AIFSD. I talked about engineering discipline, and that AI amplifies your engineering discipline that you're using. Then I put it together with an example of MCP server. That's what we went through. What does this mean for your team? If you start at the bottom, engineering discipline has never been more important. The things that we've built over the last 25, 30 years in software, we continue to need, we have to have that. If we don't, the pace that we're able to implement things today can cause dramatic issues for us if we're not building on solid foundations. Continuous delivery, pair programming, trunk-based development, continuous integration. These are practices that continue to be important, never more important than it has been today. I showed you a two-by-two model that used how long the code's going to be around, longevity, against your ability to do verifications, specifically around the domain knowledge of what you understand.
Then different tools and techniques within AIFSD that fit into those different quadrants. What is it your enterprise looks at? What are the tools that you have available? What's important for you? I use that model to be able to describe when and how I go into a supervised or unsupervised approach with coding agents with my teams. Then I use something called RIPER-5 to be able to implement AIFSD. This puts a very rigorous process using the LLM in a mindset that engineers can relate to so that we're operating the same way and the LLM is working with us. This is how I would recommend going forward. On that choose the right AI mode that you're working in, it's not a one-size-fits-all.
Today, the teams that I'm working with have only been operating together for three months in this enterprise, so we're taking a very supervised approach. We're starting to implement unsupervised agents now to be able to do things like check our specification. The speaker from Qodo talked about validating our rules were actually tested, because the LLM may not always execute our rules even though we put them there. Even though I defined it, make it echo that back out so developers can check it. What if I can take that and actually test that with an agent to be able to validate that those absolutely ran with testing? We're working on autonomous agents now to be able to do these things as part of our pipelines, as part of what we're delivering. What I want to focus on here is that it's ok that you're on that continuum. It doesn't have to be a one-size-fits-all that you're all doing continuous autonomous agents.
Key Takeaways
Four key takeaways for this talk. AIFSD is not a one-size-fits-all solution. Choose your approach based on code longevity, or degree of automated verification, those are the two that I use. Use a structured approach when working with an LLM, like RIPER-5. AI doesn't replace engineering discipline, it amplifies the practices. Focus on what are your sensible defaults to be successful.
Questions and Answers
Participant 1: Are you finding success with this approach in large existing codebases?
Wes Reisz: This particular project is Greenfield that we're using. This one I'm specifically applying here. I haven't applied it to a large codebase, but that sensing down there at the bottom specifically is where I have used legacy codebases to understand what we're getting into, like what we're walking into. I've used that in that particular one. RIPER-5 in particular, no. However, remember what I said that RIPER-5, that's how I work when I worked in software. It's not any different. In that research made, that stage, you define a specification of what you want to do, then you research it.
You look at the codebase, and you can tell it as part of your commands to understand what patterns that they're using in the codebase. Then ask me questions on how I might apply this into the codebase to get some feedback on it, and then look at what are some options that I might do. Feed that back to the specification, adjust the specification to make it match, and then keep iterating with it. I see no reason why I wouldn't, but in transparency, I've started this three months ago specifically with this particular team, and it's been really successful.
Participant 2: I like how you summarize what many of us are eventually converging into, and giving it names. That's great for conversation. One aspect that I struggle a lot when going through this process, is actually boredom, because I have to wait for the agent to think, and then generate the content, and then update the definitions, and then generate the code. Have you been able to fully automate any of these transitions?
Wes Reisz: You're interacting with a thinking LLM, at least in the one that I was just showing. It does have some slowness. One interesting thing is that review stage in there. What we can do is generate code, have it review, and look for drift. Then from that drift, be able to do updates back to the specification, if you want to keep that drift, so that the specification picks it up. That shortcuts a bit of the always going back to the specification to regenerate the code length of time. That's a practice that's been able to understand that we want these things, and then update the specification.
Other things I don't particularly love, but latest version of Cursor with agent mode, you can be able to run things more like in the flow, in a chatter face. That seems to allow you to parallelize things a little bit better. Done multiple. I talked to the Cursor team about that same question, and they specifically recommended at that time multiple tabs. Not a big fan of that, because the cognitive load on top isn't great. You could see, even in that specification that I had, it had dependent paths, and the reason why I keep that there is because we're moving towards getting more autonomy and being able to develop agents that can do each of these stages. As we do that, we'll use that to be able to parallelize. We're still getting to that stage where I can do it. That will be my hope on how we streamline some of that slowness. Yes, there is a wait stage.
Participant 3: I do know different Claude's work better in different stages for different processes.
Wes Reisz: Yes. Research is thinking. I use Claude Sonnet for code generation. They leapfrog, though. Primarily for code generation right now, I use Claude Sonnet. I've told my Google folks that Gemini 3 is much better. We'll see. I haven't got there yet. Claude Sonnet is what I use for code generation. I use Gemini for some research things. That's probably just more of a personal preference. I don't have a list I can give you, though, other than Claude Sonnet is what I have found to be my preferred code generation model.
Participant 4: I saw that you say you have 10 to 1 for the specs versus the code, which feels like it takes a lot of time. Do you have a sense whether the output you're generating is faster, is higher quality? Is it more feature-filled? Is it based on intuition, or do you have actual numbers? What dimensions is this improving the software process?
Wes Reisz: On this particular project, I don't, because it's three months, and we don't have DORA yet effectively in place to be able to have real metrics. I have intuition from developers that they feel faster. You've heard in some of the talks that that feeling can actually be wrong when you actually look at metrics, so I don't have a lot in there. We are doing developer surveys to get some of that stuff. On another project, they didn't use RIPER-5, but they used a very similar approach. They are fully instrumented with DORA metrics, and they were, in production, doing continuous delivery. They have actual metrics on what their developer productivity was while holding MTTR the same, using not RIPER-5, but a very similar research, plan, execute, and review type vocabulary that they use, so very similar. On my particular project, for the one that we're running right now, I haven't got the DORA stuff in place to give you a good, firm engineering answer.
Participant 5: Never heard of RIPER-5, but I find myself following the exact same workflow, like you said, without it. When you split up into tasks, for the one example that you were showing, I saw on the Cursor tab on the left that there was nine different .md files, one for each task. I was wondering if that was AI doing something in the meanwhile while it was working, or if you specifically split up the tasks into one .md file each, and if you find improvements with that.
Wes Reisz: I specifically split it out into each individual task so that we have that context, and I have different pairs that might pick up tasks, because they're atomic tasks that should be accomplished on their own. Generally, we find that we don't do that, but the goal as we ramp velocity is that multiple people can pick up different tasks to be able to implement, so I keep them atomic for that reason.
Participant 6: What recommendations could you give to the teams who use Brownfield projects, and these projects are distributed, one example, in several repos, GitHub repositories, or microservices, where we have many microservices, some of them live in the same repo, others in other repos, and even for humans, it can be hard to reason about.
Wes Reisz: What tools do I recommend for a model?
Participant 6: Which frameworks, not tools, but what recommendations in general can you give to the teams who work with microservices, for example?
Wes Reisz: There was a whole talk from Sepehr that actually went through Claude Code and went through Cursor, and specifically talked about some of those. I'd point you to his, because he broke down different ones really well. I specifically focused tooling on Cursor for what I was doing. I have used it, not specifically with RIPER-5, but against monorepos and individual repos. I do, at times, when I have to mount several projects, for example, to be able to look at infrastructure for if I have things separate. Yes, Cursor's what I tend to use. His talk was really good. I'd take a look at that one. He's got a lot of tips and techniques on different tools.
Participant 6: Can we use RIPER-5 for, say, microservices?
Wes Reisz: Absolutely. Yes, RIPER-5 is a logical construct. It has nothing to do with any framework. In the slide, when you get them, there's a repo there. This repo, in the README file, it'll show the rules on how to put the instructions, the LLM, what is meant for research. Whatever tool you're using, you load it into the settings for that tool. I go through how to do that in Cursor here, but you can do the same thing in any tool that you're using. It's totally up to you how you do it. I've seen some RIPER-5 specifically created for Claude Code that you can just clone the repo, but yes, it has nothing to do with the tool I use. I just happen to show Cursor.
Participant 7: I'm curious if you have an example on supervised processing?
Wes Reisz: Not in this particular one.
See more presentations with transcripts
```

---
