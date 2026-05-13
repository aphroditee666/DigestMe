# Vercel Blog

> 分类: 大厂技术博客
> URL: https://vercel.com/atom
> 抓取: 30 篇

---

## 1. Chat SDK adds Messenger adapter support

- 链接: https://vercel.com/changelog/chat-sdk-adds-messenger-adapter

```
1 min read
Chat SDK now supports Messenger as a chat adapter.
Build agents that support messages, reactions, multimedia downloads, postback buttons, and direct conversations, with display names fetched automatically from user profiles.
import { Chat } from "chat";import { createMessengerAdapter } from "@chat-adapter/messenger";
const bot = new Chat({ userName: "mybot", adapters: { messenger: createMessengerAdapter(), },});
bot.onDirectMessage(async (thread, message) => { await thread.post(`You said: ${message.text}`);});
Echo each new mention back to the sender
Read the Chat SDK documentation to get started, browse the supported adapters, or learn how to build your own.
Special thanks to @mitkodkn, whose community contribution in PR #461 laid the groundwork for this adapter.
```

---

## 2. Chat SDK adds web adapter support

- 链接: https://vercel.com/changelog/chat-sdk-adds-web-adapter-support

```
1 min read
You can now build chat UIs that connect to Chat SDK with the new web adapter. Build in-product assistants, support agents, or any other browser-based chat experience.
Define the bot on your server:
import { Chat } from "chat";import { createWebAdapter } from "@chat-adapter/web";
const bot = new Chat({ userName: "mybot", adapters: { web: createWebAdapter({ userName: "mybot", getUser: (req) => ({ id: getUserIdFromCookie(req) }), }), },});
bot.onDirectMessage(async (thread, message) => { await thread.post(`You said: ${message.text}`);});
Echo each direct message back to the sender
Then stream replies live to the browser with a preconfigured @ai-sdk/react
useChat
hook:
import { useChat } from "@chat-adapter/web/react";
const { messages, sendMessage, status } = useChat();
Wire the bot into a React component
Read the Chat SDK documentation to get started, browse the supported adapters, or learn how to build your own.
```

---

## 3. Chat SDK now supports conversation history

- 链接: https://vercel.com/changelog/chat-sdk-conversation-history

```
Chat SDK now supports cross-platform conversation history through the new transcripts and identity options. User transcripts persist across every platform adapter , allowing the same user to keep their message history wherever they message your bot. 
 bot.transcripts exposes four methods, backed by your existing state adapter: 
 append : persist an inbound message or a bot reply 
 list : return entries chronologically with filters 
 count : total entries stored for a user 
 delete : wipe every entry for a user 
 Read the Chat SDK documentation to get started, or try one of the templates . 
 Read more
```

---

## 4. Next.js May 2026 security release

- 链接: https://vercel.com/changelog/next-js-may-2026-security-release

```
Summary 
 We have shipped a coordinated security release for Next.js addressing 13 advisories across denial of service, middleware and proxy bypass, server-side request forgery, cache poisoning, and cross-site scripting. One advisory addresses an upstream React Server Components vulnerability tracked as CVE-2026-23870 . 
 Recommended actions 
 Patched versions are available for both React and Next.js, and all affected users should upgrade immediately. 
 Impact 
 The release addresses the following advisories: 
 Middleware and proxy bypass 
 Affects applications that rely on middleware.js or proxy.js for authorization. 
 High : Auth bypass via App Router segment-prefetch URL 
 High : App Router segment-prefetch bypass, incomplete fix follow-up 
 High : Pages Router i18n default-locale path bypasses proxy authorization 
 High : Bypass via dynamic route parameter injection 
 Low : Middleware redirects can be cache-poisoned 
 Denial of service 
 Affects applications using Server Functions, Partial Prerendering with Cache Components, or the Image Optimization API. 
 High : DoS in React Server Components (tracked upstream as CVE-2026-23870 ) 
 High : DoS via connection exhaustion in applications using Cache Components 
 Moderate : DoS via the Image Optimization API 
 Server-side request forgery 
 Affects applications that handle WebSocket upgrade requests. 
 High : SSRF in applications using WebSocket upgrades 
 Cache poisoning 
 Affects applications with caching layers in front of React Server Component responses. 
 Moderate : Cache poisoning in React Server Component responses 
 Low : Cache poisoning via collisions in RSC cache-busting 
 Cross-site scripting 
 Affects applications using CSP nonces in App Router, or beforeInteractive scripts that consume untrusted input. 
 Moderate : XSS in App Router applications using CSP nonces 
 Moderate : XSS in beforeInteractive scripts with untrusted input 
 Resolution 
 These vulnerabilities are addressed by the patched releases of React and Next.js. Patching is the only complete mitigation, and all affected users should upgrade immediately. 
 Vercel has not deployed new WAF rules for this release; these advisories cannot be reliably blocked at the WAF layer. 
 Affected versions 
 Package 
 Affected 
 Upgrade to 
 Next.js 13.x , 14.x 
 all versions 
 15.5.18 or 16.2.6 
 Next.js 15.x 
 <=15.5.17 
 15.5.18 
 Next.js 16.x 
 <=16.2.5 
 16.2.6 
 react-server-dom-* 19.0.x 
 <=19.0.5 
 19.0.6 
 react-server-dom-* 19.1.x 
 <=19.1.6 
 19.1.7 
 react-server-dom-* 19.2.x 
 <=19.2.5 
 19.2.6 
 Fixed in 
 Next.js : 15.5.18 , 16.2.6 
 React : 19.0.6 , 19.1.7 , 19.2.6 for the react-server-dom-parcel , react-server-dom-webpack and react-server-dom-turbopack packages 
 Frameworks and bundlers using react-server-dom-* packages should install the latest versions provided by their respective maintainers. 
 References 
 Upstream React advisory (CVE-2026-23870) 
 Read more
```

---

## 5. Vercel Flags now supports JSON values

- 链接: https://vercel.com/changelog/vercel-flags-now-supports-json-values

```
You can now store JSON values in Vercel Flags , extending the existing support for boolean, string, and number values. This allows you to collapse what used to take several related flags into a single feature flag. 
 For example, to A/B test how a different model performs, you can now define a single model flag. This allows you to manage one flag that serves the full object rather than managing ai_model , ai_temperature , and ai_max_tokens separately: 
 Use Vercel Flags to progressively route traffic to a new model, A/B test, or quickly switch models in case a provider is having issues. 
 Try it out or learn more about Vercel Flags . 
 Read more
```

---

## 6. Auto-add Git committers to your team

- 链接: https://vercel.com/changelog/auto-add-git-committers-to-your-team

```
Pro teams can now choose how Git committers to private repositories are added to their Vercel team. 
 Auto Approval : non-team committers with Vercel accounts are automatically added to your team and their deployments proceed immediately. Added members count toward your team seats at standard Pro pricing. 
 Manual Approval : deployments are blocked until an owner approves the new member. 
 Choose your approval preference in team settings . 
 Learn more about collaboration settings and troubleshooting project collaboration . 
 Read more
```

---

## 7. Secure Marketplace credentials with Production-only access

- 链接: https://vercel.com/changelog/secure-marketplace-credentials-with-production-only-access

```
You can now secure native integration resources by restricting where they can be used. Setting a resource to Production only removes non-production access and protects credentials as sensitive environment variables . This makes it so secret values or no longer readable from the dashboard or CLI 
 From the integration resource Settings , select Allowed Environments → Production only and save. We recommend that you rotate the secrets of the integration resource after saving. 
 Once applied: 
 Development and Preview connections are removed 
 New non-production connections are blocked 
 Connections without a Production target are disconnected 
 Credentials are protected and no longer readable 
 Reverting this setting requires Owner permissions for your Vercel team. Owners can re-enable Development and Preview environment from Settings and reconnect projects if needed. You may be prompted to reauthenticate with an MFA challenge depending on your settings. Learn more in the Vercel documentation . 
 Read more
```

---

## 8. Query observability metrics using the Vercel CLI

- 链接: https://vercel.com/changelog/vercel-metrics-in-cli

```
You can now access Observability Plus metrics in the Vercel CLI. 
 Query observability data for any Vercel team or project using the new vercel metrics command. Coding agents can also leverage this new command to better analyze the performance, reliability, or security of applications on Vercel, as well as debug issues. 
 This feature is available in public beta for all teams with Observability Plus. 
 Learn more about vercel metrics . 
 Read more
```

---

## 9. How KIKO Milano scales for Black Friday

- 链接: https://vercel.com/blog/how-kiko-milano-scales-for-black-friday

```
KIKO Milano on Vercel: 
 Eliminated 3 weeks of Black Friday infrastructure prep 
 75% decrease in app build times 
 Went from minimal releases to deploying multiple times per day 
 KIKO Milano’s ecommerce team used to treat peak traffic as an operations project. Weeks before Black Friday, they had to manually scale AWS infrastructure and adjust application configuration, knowing that if demand exceeded forecasts, their site could slow down or even break, costing them real revenue. 
 After migrating to Vercel, they removed manual prep from their playbook. Instead of provisioning infrastructure, their team now ships campaigns and tests daily. 
 The Black Friday problem: manual scaling and stressful failure modes 
 Before Vercel, KIKO ran their ecommerce app on AWS EC2 instances sized for normal traffic, then scaled by hand ahead of peak periods. 
 This was their previous process leading into Black Friday: 
 Manual scaling window: 
 Black Friday prep began 2–3 weeks ahead of the event, then had to be unwound after the traffic spike passed. 
 Infrastructure configuration: 
 The infra team manually adjusted AWS EC2 capacity to support expected traffic. 
 Application configuration: 
 Scaling also required application-side changes, making peak readiness more than just an infrastructure task. 
 War room prep: 
 Chat channels and conference rooms were set up for teams to triage performance and downtime problems. 
 Beyond the manual prep work, KIKO’s dev team had to anticipate failure modes that hurt the business. Slow navigation and site instability made it hard for users to purchase, and, in Ant’s words, they knew that at any point, “everything could break.” 
 Worry-free delivery and automatic scaling 
 Vercel changed the work from preparation to execution. With environments available on demand, faster builds, and automatic scaling during traffic spikes, Ant’s team stopped planning around infrastructure limits and focused on the ecommerce experience itself. 
 Environments without the bottleneck 
 KIKO's old setup ran on a fixed number of shared environments, which constrained how the team handled dev, test, pre-prod, and prod work in parallel. On Vercel, Ant described provisioning new environments as "snapping your fingers," including spinning them up on the fly when a project calls for it. Cloning environment variables is quick, and many changes that used to require code edits now "just require redeployment." 
 Shipping faster without the operational tax 
 The dev team’s old pipeline took around 20 minutes to run, which meant they had to keep releases to a minimum. Builds on Vercel finish in under four minutes on average, even with many locales and a large catalog of pre-rendered pages. The deployments view in the Vercel dashboard gives the team one place to check build status and surface failures without digging through logs. 
 No more performance variability during traffic spikes 
 Performance used to swing with traffic, which meant the team felt every spike. Ant said that on Vercel, "everything scales automatically." 
 That’s possible because their Next.js app runs on infrastructure that separates static delivery, cached pages, and dynamic compute, so each part can scale independently during traffic spikes, instead of forcing the team to size and tune servers ahead of time. 
 Beyond Black Friday: velocity, SEO, and innovation 
 The infrastructure migration didn’t just change how KIKO prepares for traffic spikes, it changed how much operational work the team carries every week. 
 Ant estimates that Vercel saves his team almost an entire day per week when all of the friction is added up, and that time savings has made the team more confident: the platform works, they can ship quickly, and when they need support, they know Vercel is there with them. 
 About KIKO Milano: KIKO Milano is a global beauty brand delivering cosmetics and ecommerce experiences to customers worldwide. 
 Read more
```

---

## 10. How General Intelligence used agents to build an agent platform on Vercel

- 链接: https://vercel.com/blog/how-general-intelligence-used-agents-to-build-an-agent-platform-on-vercel

```
General Intelligence on Vercel 
 8-person team (5 engineers) shipping 10 PRs and 70+ commits per engineer, per day 
 4,000+ preview branches with ~100 parallel app versions running at any moment 
 90% of SRE work automated through Vercel and their own agent (Cofounder) 
 Cofounder launches with a managed Vercel account for every customer 
 General Intelligence is building a platform that lets any founder run a company entirely with AI agents. Their vision is the one-person, billion-dollar company where every department is driven by agents. 
 Their flagship product, Cofounder, gives founders a full team of agents that cover engineering, marketing, SEO, finance, sales, customer support, and operations. 
 General Intelligence is an 8-person company with 5 engineers. To ship a platform that lets their customers run agentic companies, they had to operate as one themselves. They wanted to use Cofounder's CTO agent to build out other agentic business functions, and their developers quickly learned that was an infrastructure problem, not an agent problem. 
 For a complex, multi-tenant platform, the requirement was total programmatic control: every action a human could take on the underlying cloud platform had to be available to a coding agent through a CLI or APIs. That meant killing deployments, changing DNS, managing billing, editing configs, all of it. Most cloud providers failed that test, and that's why General Intelligence migrated to Vercel. 
 Agents need infrastructure built for agents 
 A coding agent runs dozens of processes in parallel. It queries logs as data, parses errors as input, and treats every dashboard click as a missing API. The bottleneck stops being how fast the agent can write code and becomes how much of the cloud it can actually reach. 
 Most clouds aren't shaped for that pattern. They're built for human developers: dashboards to click, consoles to read, APIs that cover some operations but stop short of others. The closer an agent gets to running development end-to-end, the more those gaps stack up. 
 General Intelligence started out hosting on Render. It worked for the early product, but provisioning preview environments for the full stack was painful from day one. 
 When they started building Cofounder's CTO agent, that pain became a blocker. The platform had to be reachable end-to-end through code, and Render's Python support couldn't keep up with what the agent needed. 
 "There are vendors that let an agent do 5% of the work, and vendors that let an agent do 50%," explained Pignanelli. "We needed a platform that would let an agent do 100%." They evaluated vendors against that bar and made the choice to migrate to Vercel. 
 How five engineers ship like a hundred 
 Migrating to Vercel changed how General Intelligence builds software, and their engineers don't develop locally anymore. Every change Cofounder's CTO agent makes goes straight to a Git branch, spins up a preview environment, and gets tested end-to-end by a browser agent on the live URL. 
 General Intelligence has over 4,000 branches in flight. At any moment during a workday, around 100 versions of their app are running on Vercel, each on its own preview environment with a coding agent or browser agent operating it. Earlier this year, Fluid compute grew 6.5x month-over-month, and most of that growth was internal engineering work: coding agents building business agents in Cofounder. 
 Today, engineers ships an average of 10 PRs a day with 70+ commits each, on a token budget of $5,000 per engineer per month. 
 Migrating Cofounder's Python backend to Vercel 
 General Intelligence runs a Python backend, and they were one of the first teams to migrate a complex full stack app Vercel . They did it deliberately, because the agent had to drive deployments, configs, and compute across the whole stack, not just the frontend. 
 Unifying on one platform shrank the surface area for the team and the agent to one CLI, one API, and one observability layer. When something breaks, the agent and the developers have the full picture in one place. 
 Running Cofounder as a multi-tenant app on Vercel 
 When a founder spins up a company on Cofounder, they get more than a set of agents, they get a real GitHub repository and a managed Vercel deployment, provisioned automatically through Vercel for Platforms . Each company also gets its own domain, with SSL and DNS handled automatically. 
 The engineering agent inside the customer's company is Cofounder's CTO, the same product General Intelligence uses internally. It runs the same workflow: branches, preview environments, browser agents testing the live URL. 
 What's next 
 General Intelligence will keep building their own company on the same products they ship to customers. As they add new departments and agents, Pignanelli says Vercel allows them to focus on the customer, not configuring the cloud underneath. 
 General Intelligence is building Cofounder , the first full-stack agent company platform. 
 Read more
```

---

## 11. Introducing deepsec: The security harness for finding vulnerabilities in your codebase

- 链接: https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base

```
Today we’re open sourcing deepsec : a security harness powered by coding agents. It runs on your own infrastructure and surfaces hard-to-find issues in large codebases. 
 You can run deepsec on your laptop without setting up a cloud service for privileged source code access. For inference, you can use your existing Claude or Codex subscription without any additional setup. 
 Scanning large repos can take multiple days on a single machine. To run research jobs in parallel, deepsec supports optional fanout to Vercel Sandboxes for remote execution. Scans on Vercel’s codebases routinely scale up to 1,000+ concurrent sandboxes. 
 Architecture 
 At its core, deepsec uses claude and codex to perform tailored investigation of a codebase using Opus 4.7 at max effort and GPT 5.5 at xhigh reasoning. 
 Scans start with static analysis to identify security-sensitive files, then coding agents investigate each candidate, tracing data flows, checking for mitigations, and producing actionable findings with severity ratings. Here is the workflow: 
 Scan : It starts by performing a regex-only scan of all files for security-sensitive areas that subsequent steps will focus on. 
 Investigate : Agents investigate each file identified in the scan. 
 Revalidate : A second agent run validates investigation findings to remove false positives and reclassify severity. 
 Enrich : Once investigation is complete, an agent uses git metadata and other optional services to identify the contributors responsible for fixing each issue. 
 Export : The export command formats the findings as instructions so that they can be turned into tickets for humans and coding agents. 
 Running deepsec on production code 
 deepsec has been highly useful on our own monorepos and for our customers' codebases. During development, we ran deepsec on several open source repositories of Vercel customers and partners. 
 For example, deepsec scanned the open source version of dub.co . Dub is a marketing attribution platform for affiliate programs and short links that is also available as SaaS. It features authenticated access, interacts with a database, and runs several backend services, creating a large security surface. When we shared our deepsec findings with founder Steven Tey, he replied: 
 Running against Vercel’s own monorepos, deepsec identified subtle edge cases in auth conditions, leading us to develop a custom scanner plugin that covers every authentication path in our code. 
 False positives and best uses 
 Some of deepsec 's findings will be false positives. In our experience the false positive rate is roughly 10-20%. Given the impact of true positive findings in our own research, we’ve been happy with this outcome, and we built the revalidate step to have the agent further verify its findings to reduce false positives. 
 deepsec works best for applications and services. It may be usable for libraries and frameworks, but those would likely require custom prompts and scanners. 
 Customization and plugins 
 deepsec ships with a plugin system for adapting it to your codebase. The most common plugins are custom scanners: regex matchers tuned to your auth model, data layer, or team conventions. We recommend using deepsec with your coding agent and asking it to write those matchers based on findings from an initial scan: 
 Do I need access to a special “cyber model”? 
 Both Anthropic and OpenAI offer “cyber” versions of their most capable models, fine-tuned to accept security tasks the base models won’t. deepsec works with these, but is also fully functional with off-the-shelf models. 
 deepsec ships with a classifier that checks whether the task was refused after each research step. In our experience, for the prompt that deepsec is using, refusals are a non-issue for both Opus 4.7 and GPT 5.5. 
 Getting started 
 To get started, run npx deepsec init at the root of your repository. This will create a directory called ./.deepsec , which is used to configure the system and store a catalog of your deepsec investigations. From there, follow the output of the command. Read the full documentation on Github . 
 Feedback welcome 
 While we’ve used deepsec extensively, it is still early in its development. Feedback and contributions on GitHub are welcome. 
 Read more
```

---

## 12. How GitBook serves 30,000 sites with sub-second content updates

- 链接: https://vercel.com/blog/how-gitbook-serves-30000-sites-with-sub-second-content-updates

```
GitBook on Vercel 
 30,000 documentation sites hosted on a single Vercel deployment 
 120 million monthly page views served from the edge 
 40,000 cache invalidations processed daily, each resolved in under 300ms 
 41% of all traffic now comes from AI crawlers and automated systems 
 GitBook hosts 30,000 documentation sites on Vercel, serving 120 million page views every month. Companies like n8n, Nvidia, and Zoom trust the platform to keep their docs fast and current. For modern engineering teams and coding agents, documentation is as critical as the production code it describes, and GitBook sits at the center of that expectation. 
 GitBook's publishing model mirrors how teams ship software: propose changes, review, and merge. With 30,000 independently managed sites each on its own update cadence, keeping content fast and fresh was a complicated engineering problem. 
 Before migrating to Vercel, site editors would hit merge, visit the published site to validate, and see old version of the content. "One of our customers planned a large feature release, and on launch day, the docs lagged behind the rest of the product," says Steven Hall, Head of Engineering at GitBook. "That was the moment we really internalized that docs are as important as your code going to production." 
 Making merge mean live at multi-tenant scale 
 GitBook's published content frontend runs on Next.js and is open source. When Vercel's use cache directive became available, the team saw a solution to their speed problem: cache individual data-fetching functions rather than full page responses. That meant expensive API calls were deduplicated across requests, and cache behavior became visible directly in code rather than buried in external configuration. 
 The harder problem was invalidation. In a multi-tenant system, a broad cache purge is expensive and wasteful. One team merging a typo fix shouldn't trigger revalidation for 29,999 other sites. GitBook already had a reliable signal for when content becomes stale: a merge event, whether through GitBook's app, GitHub, or GitLab. The team built tag-based invalidation triggered directly by those events. Cached data is tagged by content unit, and when a merge occurs, only the affected tags are revalidated. Everything else stays cached. 
 Today, when a change is merged, updated content becomes visible globally within 300 milliseconds. GitBook processes 40,000 of these invalidations daily. "Outside of building our own caching, I don't think we considered anything else," says Hall. 
 What changes when 41% of your traffic isn't human 
 AI-driven traffic to GitBook documentation surged 5x year-over-year in 2025 and now accounts for 41% of all page views. LLMs and automated systems crawl docs programmatically, using GitBook as a source of truth for internal tooling, SDKs, and AI applications. 
 That changes the infrastructure math. A human reader might visit a handful of pages on a single docs site, but an AI crawler can sweep every page across hundreds of sites in a single session, hitting cold cache paths that no human would visit. Multiply that across 30,000 sites and the caching foundation has to handle not just more traffic, but fundamentally less predictable traffic. Content still has to be immediately consistent after every change, and infrastructure costs have to stay predictable even as volume climbs. 
 Hall says they didn't choose the caching architecture because of AI specifically, but it turned out to be the right foundation. "We need fast docs regardless of whether AI or humans are reading them," he says. "Our target is closer to 100% cache hits. Cache hits mean fast docs, and fast docs are a critical feature of GitBook." 
 The next 30,000 sites 
 The caching infrastructure isn't finished. Features like adaptive documentation, which modifies content based on who's reading it, make multi-tenant caching meaningfully more complex. And as AI traffic keeps climbing, the volume of requests flowing through 30,000 sites will only grow. 
 "Volume is going up everywhere," Hall says. "Engineers shipping more means more docs changes. LLMs are crawling more pages every day. Our main goal is to maintain that high bar for latency and predictability as we scale." 
 GitBook is an intelligent documentation platform used by more than 30,000 teams to create, publish, and maintain product and developer documentation at scale. GitBook's published content frontend is open-source. 
 Read more
```

---

## 13. Postgres connections now work through Sandbox firewall

- 链接: https://vercel.com/changelog/vercel-sandbox-firewall-now-supports-postgres-connections

```
Vercel Sandbox can now connect to hosted Postgres databases, including Neon , Supabase , AWS RDS , Nile , and Prisma Postgres . To enable a connection, add the database host to your Sandbox's allowed domains. 
 Background 
 When SNI based filtering is used with Vercel Sandbox, the sandbox firewall restricts outbound network access by checking the domain name during a connection's TLS handshake. This works seamlessly for HTTPS traffic, where the domain is visible at the start of the connection. 
 Postgres, however, negotiates TLS differently. A Postgres client first opens a plain TCP connection and then upgrades to TLS. Because the domain isn't available when the firewall first needs it, Postgres connections through a standard domain-restricted Sandbox would fail. 
 What changed 
 The Sandbox firewall now adjusts for the Postgres TLS negotiation flow. It detects the protocol's startup sequence, waits for the TLS upgrade, and then applies your domain policy before forwarding the connection to the database. No changes are needed to your code or database configuration. 
 Connecting to hosted database 
 Here's a full example: create a Sandbox, install a Postgres client, lock down the network to only the database host, and run a query. 
 Important to know 
 TLS is required: Domain-based rules rely on the hostname being visible during the TLS handshake, so clients must connect with sslmode=require or higher. If your database doesn't support TLS, you can allow it by IP range instead. Most managed Postgres providers require TLS by default. 
 GSSAPI encryption is not supported: Clients using gssencmode=prefer will fall back to TLS automatically; gssencmode=require will not connect. 
 No silent downgrades: If a client uses sslmode=prefer and the database doesn't support TLS, the connection will fail rather than silently falling back to plain-text. 
 Learn more about the Sandbox firewall . 
 Read more
```

---

## 14. Grok 4.3 on AI Gateway

- 链接: https://vercel.com/changelog/grok-4-3-on-ai-gateway

```
Grok 4.3 is now available on Vercel AI Gateway . The model has a 1M token context window and improvements in accuracy, tool calling, and instruction following. 
 To use Grok 4.3, set model to xai/grok-4.3 in the AI SDK . 
 AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime. It includes built-in custom reporting , observability , Bring Your Own Key support, and intelligent provider routing with automatic retries. 
 Learn more about AI Gateway , view the AI Gateway model leaderboard or try it in our model playground . 
 Read more
```

---

## 15. Custom tags available in beta on Vercel Sandbox

- 链接: https://vercel.com/changelog/custom-tags-available-in-beta-on-vercel-sandbox

```
As teams scale isolated environments for AI agents, code generation, or dev workflows, keeping track of which sandbox belongs to whom, and why, becomes critical. Custom tags allow you to organize, filter, and manage Vercel Sandboxes at scale. Each sandbox supports up to five tags. 
 Organize by environment, team, or customer 
 Tags are flexible by design. Use them to separate staging from production, attribute usage to specific teams, or isolate sandboxes per customer in multi-tenant platforms: 
 Update tags as context changes 
 Promote a sandbox from staging to production, reassign ownership, or mark it for cleanup without recreating it: 
 Easily track your sandboxes 
 Filter sandboxes by any tag to quickly surface the ones that matter. This is useful for dashboards, cleanup scripts, or routing logic that needs to find all sandboxes matching a specific environment or team: 
 Use Cases 
 AI agents at scale : Tag sandboxes by session, user, or agent run to track which execution environment belongs to which workflow. 
 Multi-tenant platforms : Isolate and filter sandboxes per customer or workspace, making billing attribution and cleanup straightforward. 
 Team-level visibility : Attribute sandbox usage to specific teams for cost tracking or capacity planning. 
 This feature is in beta and requires upgrading to the beta SDK and CLI packages. Learn more in the documentation . 
 Read more
```

---

## 16. Vercel now supports Pro plan in Stripe Projects

- 链接: https://vercel.com/changelog/vercel-now-supports-pro-plan-in-stripe-projects

```
You can now sign up for or upgrade to a Vercel Pro plan directly from Stripe Projects using shared payment tokens (SPTs). Agents and developers can manage plan changes programmatically from the Stripe CLI, without leaving their workflow. 
 What’s new 
 Provision or upgrade to Vercel Pro directly from the Stripe CLI 
 Support for both upgrade and downgrade flows 
 Powered by shared payment tokens for secure, streamlined billing 
 This builds on our Stripe Projects launch in developer preview by enabling end-to-end provisioning and billing in one place. Instead of switching between dashboards, you can now handle infrastructure setup and plan management directly from the terminal. 
 Getting started 
 If you’re already using Stripe Projects and have set up billing via stripe projects billing add , you can upgrade your Vercel plan from the CLI simply by running stripe projects add vercel/pro 
 If you are new to Stripe Projects, Install the plugin and initialize your project: 
 Read more
```

---

## 17. Native Deployment Checks are now available

- 链接: https://vercel.com/changelog/native-deployment-checks

```
You can now run lint and typecheck on every Vercel deployment, in parallel with the build. Native Deployment Checks are available to every team and join your existing Deployment Checks alongside GitHub and Marketplace integrations. 
 Once added from your project's Build and Deployment settings , Vercel runs the matching script from your package.json on each deployment, and skips the check if no matching script exists. You can mark a check as required to hold the deployment from production until it passes, and choose which environments each check runs on. 
 When a Native Deployment Check fails on a pull request, Vercel Agent investigates the failure and suggests a fix you can review and merge. 
 Read more
```

---

## 18. 2026 Vercel AI Accelerator recap

- 链接: https://vercel.com/blog/2026-vercel-ai-accelerator-recap

```
On April 16th, 39 teams took the stage at our San Francisco headquarters to pitch investors at Demo Day. During the prior six weeks, founders worked shoulder-to-shoulder with the Vercel team, our partners, and industry leaders to shape their ideas into the next generation of AI applications. 
 Six weeks with the 2026 cohort 
 Teams from around the world joined the 2026 cohort, building agents, developer tools, consumer apps, and vertical AI for finance, security, healthcare, and robotics. 
 Each week, the cohort joined two sessions: a hands-on technical workshop and a fireside chat with an external speaker. The workshops covered the technical side of building AI products, from agents and models to deployment and scale. 
 The fireside chats brought in industry leaders, Vercel experts, and investors. Speakers included Peter Steinberger (OpenAI/OpenClaw) and the Windsurf team, with topics ranging from the state of AI to pricing, legal, sales, marketing, and fundraising. 
 Builder day 
 Halfway through the program, the cohort came together with the broader Vercel startup ecosystem for Builder Day at Vercel's office. The day combined technical workshops, hands-on office hours with engineers from accelerator partners like AWS and Anthropic, open time to build and connect, and a special fireside chat between Malte Ubl (Vercel CTO) and Stephen Haney (Paper CEO). 
 $8M in infrastructure and credits 
 Beyond the programming, every team got over $200K to build with on Vercel and across the AI stack: 
 Vercel AI stack : AI Gateway , Sandbox , Workflows , Fluid Compute , v0 , and more 
 Partners : AWS , Anthropic , OpenAI , Browserbase , ElevenLabs , Auth0 , WorkOS , Notion , Modal , Neon , Supabase , and more 
 Demo Day 
 After six weeks of building, the cohort showed their work at Demo Day. Each team had a few minutes to present to a room of VCs, AI leaders, and partners, with a panel of judges from across the AI ecosystem selecting the winners. 
 Winners 
 On Demo Day, judges scored teams on problem validity, technology fit, product quality, and each team's final pitch. Three teams took home $100K+ in credits and prizes, and the first-place team also received an investment from Vercel Ventures. 
 1st: Rex 
 Rex is building AI for the enterprise finance back office, unifying customer context across systems so agents can run accounts receivable end to end. In addition to credits, Rex received an investment from Vercel Ventures. 
 2nd: Hacktron AI 
 Hacktron AI is an AI teammate for security. As AI writes more of the code shipping into production, vulnerabilities scale with it. Hacktron integrates into the development lifecycle to find and remediate real, exploitable issues. 
 3rd: Roots 
 Roots is rebuilding how people buy and sell homes. Buyers save hundreds to thousands of dollars a month, and sellers net thousands more at closing. 
 $100M+ in fundraising, and counting 
 The 40 alumni from the last cohort have raised over $100M in venture funding, and several have been accepted to Y Combinator. Stably , the 2025 winner, is now converting enterprise pilots into contracts and shipping new product lines in hours instead of weeks. 
 Other teams from past cohorts, including Jigsaw Stack , Belli AI , and General Translation , have signed enterprise customers and formed partnerships through the program. 
 Apply to the next cohort 
 If you're an early-stage founder building in AI, you can apply for the next AI Accelerator program. We will open applications later this year. 
 Visit our startup hub to learn more and connect with our startups team. 
 Read more
```

---

## 19. Hobby projects now default to 30-day deployment retention

- 链接: https://vercel.com/changelog/hobby-projects-now-default-to-30-day-deployment-retention

```
Starting April 29th, the maximum retention policy for Hobby plans will be capped at 30 days. Deployments outside your retention window will be automatically removed. This excludes your 10 most recent production deployments and any aliased deployments, which continue to be preserved regardless of retention settings. 
 Pro and Enterprise plans are not affected. 
 Learn more about Deployment Retention . 
 Read more
```

---

## 20. GPT 5.5 on AI Gateway

- 链接: https://vercel.com/changelog/gpt-5.5-on-ai-gateway

```
GPT-5.5 is now available on Vercel AI Gateway . 
 There are 2 variants: GPT-5.5 and GPT-5.5 Pro. Both models are tuned for long-running agentic work across coding, computer use, knowledge work, and scientific research, and are more token-efficient than the previous generation. 
 GPT-5.5 is stronger at agentic coding and long-horizon work where the model needs to hold context across a large system and carry changes through the surrounding codebase. Paired with computer-use skills, it can operate real software and turn raw material into documents, spreadsheets, or slide presentations. 
 GPT-5.5 Pro is built for demanding, multi-step work where response quality matters more than latency. Early testing shows gains in business, legal, education, data science, and technical research workflows that involve critiquing work over multiple passes and stress-testing arguments. 
 To use GPT-5.5, set model to openai/gpt-5.5 or openai/gpt-5.5-pro in the AI SDK . 
 AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime. It includes built-in custom reporting , observability , Bring Your Own Key support, and intelligent provider routing with automatic retries. 
 Learn more about AI Gateway , view the AI Gateway model leaderboard or try it in our model playground . 
 Read more
```

---

## 21. Deepseek V4 on AI Gateway

- 链接: https://vercel.com/changelog/deepseek-v4-on-ai-gateway

```
DeepSeek V4 is now available on Vercel AI Gateway . 
 There are 2 model variants: DeepSeek V4 Pro and DeepSeek V4 Flash. A 1M token context window is the default across both models. 
 DeepSeek V4 Pro focuses on agentic coding, formal mathematical reasoning, and long-horizon workflows. It handles feature development, bug fixing, and refactoring across stacks, with tool use that works across harnesses like MCP workflows and agent frameworks. It also writes clear, well-structured long-form documents. 
 DeepSeek V4 Flash performs close to V4 Pro on reasoning and holds up on simpler agent tasks, with a smaller parameter size for faster responses and lower API cost. It's a good fit for high-volume workloads and latency-sensitive use cases. 
 To use DeepSeek V4, set model to deepseek/deepseek-v4-pro or deepseek/deepseek-v4-flash in the AI SDK . 
 AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime. It includes built-in custom reporting , observability , Bring Your Own Key support, and intelligent provider routing with automatic retries. 
 Learn more about AI Gateway , view the AI Gateway model leaderboard or try it in our model playground . 
 Read more
```

---

## 22. GPT Image 2 on AI Gateway

- 链接: https://vercel.com/changelog/gpt-image-2-on-ai-gateway

```
GPT Image 2 is now available on Vercel AI Gateway . 
 OpenAI's newest image model supports detailed instruction following, accurate placement and relationships between objects, and rendering of dense text across multiple aspect ratios. 
 The model can render fine-grained elements including small text, iconography, UI elements, dense compositions, and subtle stylistic constraints, at up to 2K resolution. Non-English text is also supported and reads coherently. 
 GPT Image 2 can produce photos, cinematic stills, pixel art, manga, and other distinct visual styles, with consistency in texture, lighting, composition, and detail. This suits workflows like game prototyping, storyboarding, marketing creative, and medium-specific asset generation. 
 To use GPT Image 2, set model to openai/gpt-image-2 in the AI SDK , or try it directly in our m odel playground . 
 AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime. It includes built-in custom reporting , observability , Bring Your Own Key support, and intelligent provider routing with automatic retries. 
 Learn more about AI Gateway , view the AI Gateway model leaderboard or try it in our model playground . 
 Read more
```

---

## 23. Kimi K2.6 on AI Gateway

- 链接: https://vercel.com/changelog/kimi-k2.6-on-ai-gateway

```
Kimi K2.6 from Moonshot AI is now available on Vercel AI Gateway . 
 The model focuses on long-horizon coding tasks, with generalization across languages such as Rust, Go, and Python and across front-end, devops, and performance optimization work. K2.6 can turn simple prompts into complete front-end interfaces with structured layouts. 
 For autonomous, proactive agents that run continuously across multiple applications, K2.6 improves on API interpretation, long-running stability, and safety awareness during extended research tasks. 
 To use Kimi K2.6, set model to moonshotai/kimi-k2.6 in the AI SDK . 
 AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime. It includes built-in custom reporting , observability , Bring Your Own Key support, and intelligent provider routing with automatic retries. 
 Learn more about AI Gateway , view the AI Gateway model leaderboard or try it in our model playground . 
 Read more
```

---

## 24. Deployment retention policies now preserve active branch deployments

- 链接: https://vercel.com/changelog/deployment-retention-policies-now-preserve-active-branch-deployments

```
Retention policies no longer delete the latest preview deployment for branches with open or unmerged pull requests. Previously, deployments for active branches could be removed if they exceeded the configured retention window. 
 This means you can safely use shorter retention windows without risking losing active preview deployments. This change applies to all plans. 
 Your 10 most recent production deployments and any aliased deployments continue to be preserved regardless of retention settings. 
 Learn more about Deployment Retention . 
 Read more
```

---

## 25. How Zo Computer improved AI reliability 20x on Vercel

- 链接: https://vercel.com/blog/how-zo-computer-improved-ai-reliability-20x-on-vercel

```
Zo Computer on Vercel 
 20x reduction in retry rate (7.5% → 0.34%) 
 99.93% chat success rate (up from 98%) 
 P99 latency cut 38% (131s → 81s) 
 New models added in less than 1 minute 
 Every company has servers that store data, run services, and do work around the clock. Consumers just have apps. Rob Cheung, co-founder of Zo Computer, is closing that gap. Zo is a personal AI cloud: your own servers and data that power an always-on agent. 
 "Cloud is one of the best computing models of all time, and consumers have zero direct access because it's so complicated," explained Rob Cheung, co-founder and CEO of Zo. "Now, with AI, it's finally possible for all of us to have cloud computers." 
 Zo is a full computing environment, not just a chatbot. Rob laughs about his mom running servers and databases without knowing it. People use Zo to manage small businesses, do research, organize finances, and track health data. 
 The 8-person company is two and a half years old and they have an ambitious goal: to onboard one million new users to personal cloud computing in 2026. That means millions of AI model calls every day, and when Zo users text their agent like a friend, they expect the same responsiveness. 
 Death by a thousand adapters 
 Zo gives users access to any model they want, and supports bring-your-own-key. That means their backend has to talk to every major provider: OpenAI, Anthropic, MiniMax, GLM, Fireworks, and more. 
 Before they moved to Vercel, that meant custom adapter code for each model. Every provider required different handling for images, different key management, and different edge cases. On top of the code complexity, Zo's team was managing retries, provider routing, and fallback logic themselves. 
 Every time a provider shipped a new model, an engineer had to write a new adapter, test the edge cases, and run the deployment pipeline. With new models released weekly, it was a constant drag on a small team building a consumer product, and their users felt it. 
 Zo's baseline for AI model calls was a 98% success rate with a 7.5% retry rate. That means 1 in 50 messages failed or retried, adding up to tens of thousands of model fallbacks every day. 
 AI SDK + AI Gateway: two layers, one integration 
 Zo moved to Vercel's AI SDK and AI Gateway, which solved two distinct problems. 
 AI SDK replaced the custom adapter code. Instead of per-provider implementations with bespoke edge case handling, Zo's engineers got a unified interface for every model, from image support to response format normalization. 
 AI Gateway replaced the infrastructure-level complexity. Retries, fallback routing, provider health monitoring, and uptime were all handled at the routing layer in Vercel instead of in Zo's codebase. 
 Rob's co-founder built APIs at Stripe, where developer experience was the product. He describes the combined effect of AI SDK and AI Gateway the same way: everything just works, and the pieces you don't see matter most. 
 New model support went from an hour-long, multi-file code change to adding a config string in 30 seconds. The day MiniMax shipped M2.7, Zo had it live for users immediately. No adapter code, no edge case testing, no deploy cycle. 
 For an 8-person team focusing on onboarding their first million users to personal cloud computing, cutting out interruptions for model support has been a huge relief. 
 20x improvement in reliability 
 During the rollout, Zo ran Vercel and non-Vercel routes simultaneously, creating a live A/B comparison under identical production conditions. 
 The results: 
 Period 
 Route 
 POST error 
 Chat success 
 Retry rate 
 Avg attempts 
 Before switch 
 Non-Vercel 
 4.59% 
 99.73% 
 7.52% 
 1.12 
 After switch 
 Non-Vercel 
 10.38% 
 97.86% 
 17.07% 
 1.29 
 After switch 
 Vercel 
 0.45% 
 99.93% 
 0.34% 
 1.00 
 The non-Vercel route actually degraded during the same period that Vercel held steady. Retry rate dropped from 7.5% to 0.34%, a 20x improvement. Average attempts per chat hit 1.00, meaning virtually every request succeeded on the first try. 
 On MiniMax M2.5, Zo's most-used model, the latency improvement was significant. In an apples-to-apples comparison over the same window, Vercel handled 18,139 chats versus 21,105 on non-Vercel and still performed better across the board: 
 Average latency improved 25.7% 
 P95: 46s → 34s (25% improvement) 
 P99: 131s → 81s (38% improvement) 
 For Zo's users, the P99 number matters most because they text their agents constantly throughout the day. A 131-second worst-case wait breaks that experience completely, but now 99% of requests complete in under 81 seconds. 
 By the end of the test, 91.88% of Zo's traffic routed through Vercel, handling 3.3x larger context windows (42,500 average input tokens vs. 12,700) at a lower error rate than the non-Vercel path. 
 Scaling to a million personal cloud owners 
 Vercel handles Zo's AI layer through AI SDK and AI Gateway and hosts their public-facing marketing site. With reliable AI infrastructure and no adapter code to maintain, the team can focus on the product instead of the plumbing. 
 With the pace of model developments in AI, Rob used to worry about the work required to keep up. “Now I don’t worry about it,” he said, “because with Vercel, the infrastructure just works.” 
 Zo Computer is a personal AI cloud platform that gives every user their own cloud computer, housing data, services, and a personal agent. Users interact through a conversational interfaces like iMessage, or log in and use the environment directly. Founded two and a half years ago, Zo is an 8-person team based in New York City. Learn more at zo.computer . 
 Read more
```

---

## 26. Vercel Flags is now generally available

- 链接: https://vercel.com/changelog/vercel-flags-ga

```
Vercel Flags is now generally available. 
 Vercel Flags is a feature flag provider built into the Vercel platform. Create and manage feature flags with targeting rules, user segments, and environment controls directly in the Vercel Dashboard. 
 The Flags SDK provides a framework-native way to define and use these flags within Next.js and SvelteKit applications, integrating directly with your existing codebase: 
 Once you define a flag, you can use them within your application in a few lines of code: 
 For teams using other frameworks or custom backends, the Vercel Flags adapter supports the OpenFeature standard, allowing you to plug Vercel Flags into their provider agnostic SDK. 
 Try it out or learn more about Vercel Flags . 
 Read more
```

---

## 27. Claude Opus 4.7 on AI Gateway

- 链接: https://vercel.com/changelog/opus-4.7-on-ai-gateway

```
Claude Opus 4.7 from Anthropic is now available on Vercel AI Gateway . 
 Opus 4.7 is optimized for long-running, asynchronous agents and handles complex, multi-step tasks with reliable agentic execution. The model shows gains on knowledge-worker tasks, particularly where it needs to visually verify its own outputs. 
 Opus 4.7 is also stronger at programmatic tool-calling with image-processing libraries to analyze charts and figures, including pixel-level data transcription. It has high-resolution image support, which is useful for computer use, screenshot understanding, and document analysis workflows. Opus 4.7 now has improved memory, with agents that maintain structured memory store across turns seeing more reliable recall and fewer dropped facts without additional prompting. 
 To use Claude Opus 4.7 set model to anthropic/claude-opus-4.7 in the AI SDK . You can also try a new effort level: 'xhigh'. 
 Opus 4.7 also introduces the task budgets feature. Task budgets let you set a total token budget for an agentic turn via taskBudget . The model sees a countdown of remaining tokens, which it uses to prioritize work, plan ahead, and wind down gracefully as the budget is consumed. Thinking content is also now omitted by default for Opus 4.7. To receive thinking content, set display to 'summarized' : 
 AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime. It includes built-in custom reporting , observability , Bring Your Own Key support, and intelligent provider routing with automatic retries. 
 Learn more about AI Gateway , view the AI Gateway model leaderboard or try the model in our model playground . 
 Read more
```

---

## 28. A new programming model for durable execution

- 链接: https://vercel.com/blog/a-new-programming-model-for-durable-execution

```
The gap between prototypes and production-ready systems is huge. Code that's trivial to run locally falls apart the moment it needs to handle failures, restarts, and real traffic. 
 Framework defined infrastructure solved this for web applications. When you deploy, Vercel infers the right configuration from the app itself. Workflows extends that model to long-running systems. Instead of managing a separate codebase for orchestration, durable workflows are an extension of your application code. 
 Since launching in beta in October 2025, Workflows has processed over 100 million runs and over 500 million steps across more than 1,500 customers, with more than 200K npm downloads every week. 
 Today, Vercel Workflows is generally available. 
 Built for agents, backends, and long-running workloads 
 Workflows is built for any workload that doesn’t fit in a single request. 
 Agents : Deep integration with the AI SDK enables infinitely long running durable agents that can maintain state, tools, and handle external events or interruptions. AI SDK v7 is taking this further with WorkflowAgent. 
 Backends : Workflow SDK proved this programming model in TypeScript codebases, and we're bringing it to a new language. The Workflow Python SDK is now in beta. 
 Long-running workloads : Workflows can be used for any function that needs to execute reliably, including multi-step onboarding flows, payment processing, ETL pipelines, or any backend work that would otherwise require you to wire up your own queues and retry logic. 
 How it works 
 Shipping a reliable long-running process to production typically means splitting your code across queues, workers, status tables, retry logic, and monitoring. Dedicated orchestration services add yet another layer with long-lived background processes you run in Kubernetes, scale horizontally, and dedicate engineering time to keep healthy. They are distributed systems you pay for on top of your core application compute. 
 Workflows eliminates the orchestrator entirely. All coordination runs in your application code, not a separate service. The infrastructure is built on three components: 
 Event log : records every step input, output, stream chunk, sleep, hook, and error in a run. It is the single source of truth for execution state and history. 
 Your functions on Fluid compute : each step runs as its own function invocation on Fluid compute. The workflow library inside each function handles dequeueing, state loading, encryption, execution, and handoff to the next step. 
 Vercel Queues : each function enqueues the next step automatically. Queues run automatically on Vercel, in your own Postgres, or in-memory locally. 
 Because there is no separate orchestration service, you only pay for the compute your steps actually use when functions are running. 
 The programming model: your code is the orchestrator 
 Workflows lets you write long-running functions in TypeScript or Python using normal control flow and a small API surface. 
 In TypeScript you create a workflow with "use workflow" , and isolate units of work with "use step" . Workflows handles everything underneath: queues, retries, step isolation, observability, durable state, and streaming. 
 At first glance, this looks like one function calling another, and that is exactly the point. Each step gets isolation, retries, persistence, observability, and durable continuation automatically. The orchestration lives in the application code, not in a separate system. 
 A Next.js app with the Workflow SDK installed runs the same way locally as it does in production at scale, with the same code, real guarantees, and no separate orchestration tooling to configure. 
 Vercel Workflows in action: Guillermo's infinite chess game 
 One of the best examples from beta testing is Guillermo's infinite chess game . It continuously pits models against each other, feeding them the current board state, validating moves, rendering the game, and running matches indefinitely, turn after turn. 
 Each chess match is a workflow run, and when a game ends, the last step starts a new run . Infinity is modeled as recursion across runs. 
 Because every workflow run is pegged to a specific deployment, one game can safely finish on the version it started with while the next game begins on the latest deployment. That creates a clean upgrade boundary where each game remains stable within its version, and every new game picks up the latest improvements. 
 If the backend code powering the chess match crashes or encounters transient errors, the workflow run automatically retries it without causing the application to fail. 
 Why Workflows matters for agents 
 Workflows is purpose-built for the agentic era. It is the only security-first, durable SDK made for building agents and made for agents to build with. 
 Secure by default 
 By default, Vercel Workflows encrypts all data , including step inputs, outputs, and stream chunks, before they leave your deployment. Nothing is readable in transit or at rest outside your environment, and decryption only happens inside the deployment running the workflow. 
 Encryption is built in and free, not a security add-on you configure after the fact. This is possible because Workflows owns both orchestration and execution in the same environment, so encryption can happen automatically without a separate service or any extra infrastructure on your end. 
 When you need to inspect encrypted data through the dashboard or workflow CLI, explicit decryption is supported with a full audit trail . 
 For building agents 
 Agents need more than longer timeouts, they need durable execution, reliable orchestration, resumable streams, and enough headroom to move large payloads through long-running systems. 
 Durable agents 
 Workflow SDK and AI SDK share a deep integration that gives agents durable execution, tool calling, state management, and the ability to handle external events or interruptions gracefully. Tools can be implemented as workflow steps for automatic retries or as regular workflow-level logic that uses primitives like sleep and hooks to suspend and resume cleanly. Agents process tool calls iteratively until completion, surviving restarts and failures along the way. 
 AI SDK v7 takes this further with WorkflowAgent , a fully native implementation. 
 Durable streams 
 Durable streams persist agent output. getWritable() gives you a persistent stream that multiple clients can connect to, disconnect from, reconnect to later, and resume from any point. The workflow keeps running even if the user closes the browser. When they come back, the client reconnects and continues exactly where the stream left off, no Redis or custom pub/sub required. 
 In this example, a flight booking agent streams itinerary updates as it plans a trip and searches for flights: 
 The API route starts the workflow and returns the durable stream to the client. The run ID in the response header is what enables reconnection: 
 If the user closes the browser mid-search, the workflow keeps running. When they re-connect, or share the link with a different user who opens the session, WorkflowChatTransport resumes the stream from the last event the client received. 
 Hooks and sleep 
 Workflows can suspend without incurring any compute. 
 Hooks let a workflow wait for an external trigger to resume. Hooks are useful for building human-in-the-loop approval flows and integrating with third-party services. 
 Sleep lets a workflow suspend for any specified amount of time, from minutes to days or months. Sleep is useful for email drip campaigns and date-sensitive use cases. 
 Limits built for multimodal agents 
 Workflows supports 50 MB per step payload and up to 2 GB across an entire run, with generous event limits. That's plenty of headroom for agents passing images, video, and large context across long execution chains. 
 For agents to build with 
 Workflows is not just great for building agents. It is also designed for coding agents to use directly. 
 The programming model is agent-friendly 
 Workflows code is ordinary TypeScript. A workflow is a function, a step is a function, and because orchestration lives in the application code itself, a coding agent only has to reason about one system. There is no separate orchestration layer to configure and no worker fleet to manage. 
 Full observability from the CLI 
 Workflow SDK ships with a CLI that any agent can use for inspecting and debugging your workflow runs. If a human can inspect runs in the dashboard, an agent can inspect the same workflow state from the terminal. 
 This works locally with no config. For production deployments on Vercel, the CLI reuses your vercel CLI authentication with --backend vercel to make authenticated requests against the Vercel API. Agents can investigate state, inspect runs, and debug behavior without leaving the terminal. 
 Workflows ships with a skill 
 Agents can install the Workflows skill directly and use it to scaffold, debug, and manage workflows without hand-written product knowledge. 
 Run Workflows anywhere 
 Workflow SDK is open source and part of the same family as AI SDK and Chat SDK. The workflow npm package goes stable at GA with 200K+ weekly downloads and 75+ releases shipped during beta. 
 Worlds are the adapter system that makes Workflows portable. Each World provides the three components a workflow needs (an event log, compute, and a queue), backed by different infrastructure. 
 Managed : Vercel handles everything automatically. Deploy your app and Vercel Workflows runs on Fluid compute with Vercel Queues, zero-config E2E encryption, and built-in observability. 
 Self-hosted : Run Workflows on your own infrastructure. We maintain a Postgres reference implementation that real customers run in production, and the Local World ships built in for development. 
 Embedded : The SDK is not locked to one runtime, and the community is already building more Worlds, including adapters for MongoDB, Redis, Turso, Jazz Cloud, and Cloudflare. We'll continue to support anyone who wants to build Worlds. 
 How Vercel customers use Workflows 
 Mux powers durable video and AI pipelines 
 Mux built their media intelligence layer on Workflows , handling execution, retries, and orchestration for AI inference across complex video pipelines. They also shipped "use workflow" and "use step" directives inside their own @mux/ai SDK, so any developer can npm install @mux/ai and get a durable, multi-step pipeline as a normal imported function. 
 Durable runs hundreds of AI agents for 3 million small businesses 
 Durable's most critical path is website creation: dozens of parallel AI steps orchestrated by Vercel Workflows to deliver a complete site in under 30 seconds. Their small dev team ripped out their self-hosted infrastructure entirely and rewrote on Workflows with 160+ directives across 75 files. 
 Flora orchestrates creative AI agents across 50+ image models 
 Flora runs their entire media generation pipeline on Vercel Workflows , orchestrating 50+ image models with no queues, no state machines, and no separate service. They use rollbacks for credit refunds, recursive workflows for user-defined multi-step pipelines, and getWritable for progress streaming. Their customers kick off jobs, close their laptop, and come back to completed results. 
 What's next: Workflows 5 and Python support 
 Workflows 5 
 Workflows 4 focused on getting the developer experience and SDK model right. Workflows 5 keeps the same programming model while pushing harder on performance and runtime efficiency. Here’s what we’re cooking: 
 Native concurrency controls, including a lock primitive for coordinating work across multiple runs 
 Globally deployed Workflows infrastructure 
 A snapshot-based runtime to reduce replay overhead as event histories grow 
 Better bundling and stronger Next.js integration 
 Our goal is to make the overhead of opting into Workflows smaller and smaller until it is the obvious default for any project. Install workflow@beta to try Workflows 5 early (and share feedback on GitHub). 
 Python support 
 The Python SDK is now in beta, making Workflows available across the broader AI and backend ecosystem. Here's a quick taste of how the opening example in this post looks in Python: 
 Get started 
 Durability, reliability, observability, security, and streaming should be part of your product from the beginning, not chores you take on months later. 
 When you use Workflows, we take on the complexity so you can focus on what makes your app unique. Learn more about Vercel Workflows or visit the Workflow SDK docs to get started. 
 Vercel Workflows is generally available on April 16. 
 Read more
```

---

## 29. Seedance 2.0 Video Generation on AI Gateway

- 链接: https://vercel.com/changelog/seedance-2.0-video-now-available-on-ai-gateway

```
You can now access Bytedance's latest state-of-the-art video generation model, Seedance 2.0, via AI Gateway with no other provider accounts required. 
 Seedance 2.0 is available on AI Gateway in two variants: Standard and Fast. Both share the same capabilities. Standard produces the highest quality output, while Fast prioritizes generation speed and lower cost. 
 Seedance 2.0 is strong at maintaining motion stability and fine detail across frames, producing consistent output even in complex scenes with facial expressions and physical interactions. The model also generates synchronized audio natively, with support for speech in multiple languages and dialects. 
 Beyond text-to-video and image-to-video, Seedance 2.0 adds multimodal reference-to-video, letting you combine image, video, and audio inputs as reference material in a single generation. It also supports video editing and video extension, along with professional camera movements, multi-shot composition, and in-video text rendering. 
 To use this model, set model to bytedance/seedance-2.0 or bytedance/seedance-2.0-fast in the AI SDK or try it out in the AI Gateway Playground . 
 Text to Video 
 Generate video from a text prompt. Describe the scene, camera movement, and audio for the model to produce. 
 Image to Video 
 Generate video from a starting image. The model animates the image based on the text prompt while preserving the visual content of the source frame. 
 Reference to Video 
 Generate video using image, video, or audio references as source material. You can combine multiple reference types in a single generation to control visual style, motion, and sound. 
 AI Gateway does not charge any markup on video generation: Seedance 2.0 and 2.0 Fast are at the same price as going direct to the Bytedance provider. 
 Learn more about AI Gateway , view the AI Gateway model leaderboard or try it in our model playground . 
 Read more
```

---

## 30. Reduced pricing for Turbo build machines

- 链接: https://vercel.com/changelog/reduced-pricing-for-turbo-build-machines

```
Vercel is reducing the price of Turbo build machines by 16%. All builds are now priced at $0.0035 per CPU per minute. With this new model: 
 Turbo machines, with 30 CPUs, are now $0.105 per minute (previously $0.126) 
 Enhanced machines, with 8 CPUs, continue to be priced at $0.028 per minute 
 Standard machines, with 4 CPUs, continue to be priced at $0.014 per minute 
 This change will begin rolling out on April 27, and will appear on invoices for the current billing cycle as "Build CPU Minutes". 
 Learn more about build machine pricing or monitor your Builds usage from Project Usage . 
 Read more
```

---
