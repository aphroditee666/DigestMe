# GitHub Blog

> 分类: 大厂技术博客
> URL: https://github.blog/feed/
> 抓取: 10 篇

---

## 1. Why age assurance laws matter for developers

- 日期: 2026-05-08 16:30
- 链接: https://github.blog/news-insights/policy-news-and-insights/why-age-assurance-laws-matter-for-developers/

```
Policymakers around the world are advancing age assurance proposals to protect children and teens online. Some approaches restrict minors’ access to certain services or content, while others would require devices, operating systems, or app stores to collect age information and pass age signals to apps and websites. These proposals are driven by serious concerns, but without appropriate scoping, they risk imposing burdensome requirements on open source software and developer infrastructure services that do not present the same risks to minors as consumer-facing platforms. In this blog post, we’ll provide an overview of what developers should know and how to engage. 
 The harms these laws aim to address are serious and deserve attention. Grooming for sexual purposes, exposure to violent content, and online bullying are just some of the risks young people are facing online. At the same time, participation in online communities, including open source software development, can be an important part of a young person’s education and social life. When trying to strike a balance between freedom and protection, policymakers are not always aware of how their proposals could affect developers or how the open source ecosystem operates. 
 “Age assurance” refers to a range of approaches used to determine or estimate a user’s age. It is sometimes used interchangeably with “age verification,” which typically refers to higher-confidence methods like photo ID matching or checks against financial or identity systems. Age assurance also includes self-attestation (where users report their age) and age estimation (where age is inferred from signals, facial scanning, or behavior). These approaches span a wide spectrum, with ongoing debate about tradeoffs between accuracy, privacy, security, interoperability, and accessibility. Proposals also vary in what age thresholds trigger restrictions, the services or content covered, how parental consent should factor in, and how access is limited. While we do not discuss each approach in detail here, we encourage readers to engage with the legislation, consider different technical and policy perspectives, and think about how to protect young people online while preserving access to the knowledge, learning opportunities, and creative potential the internet enables—including opportunities to learn to code and participate in the global open source ecosystem. 
 A poorly designed age assurance law could have significant unintended impacts for open source projects. For example, requirements that operating systems centrally collect and manage user data, or that restrict users from installing software outside of centralized app stores, would conflict with the decentralized, user-controlled norms of the open source ecosystem. 
 Another potential pitfall is placing age assurance requirements on “publishers” of operating systems, regardless of whether they are individuals or companies. Open source operating systems are frequently iterated on, reused, and redistributed by individual contributors and small communities, many of which have limited resources and small user bases. The diversity of the software ecosystem is worth preserving. 
 GitHub has engaged with governments on age‑related online safety proposals for several years. In some cases, including Australia’s Social Media Minimum Age legislation, we worked with policymakers to explain why open source code collaboration platforms should not be in scope. Similar exemptions appear elsewhere. France’s current Social Media Minimum Age proposal , for example, includes the same exclusions for open source code collaboration sites and online encyclopedias that appear in the EU Copyright Directive. 
 Many policymakers recognize that access to the open source software development ecosystem delivers significant public benefits, including education, innovation, and security, and that the risks young people face from participating in open source development communities are materially different by comparison. At the same time, a growing number of laws are seeking to advance child safety goals at varying levels of the tech stack, including through operating systems and application distribution layers. This has raised new questions for developers about how these requirements apply in practice, and whether open source operating systems and developer infrastructure like GitHub could be impacted. 
 Legislation to know 
 California AB 1043 Digital Age Assurance Act and 2026 amending bill AB 1856: Requires operating system providers (in coordination with covered app stores) to collect self‑declared age at account setup and transmit an age‑range signal to applications via a real‑time API. 
 Colorado SB 26-051 Age Attestation on Computing Devices: Requires operating systems and covered app stores to generate and share an age‑bracket signal with applications via a real‑time interface, with evolving definitions of “covered application” and “covered application store” shaping scope. 
 Illinois HB 4140 Digital Age Assurance Act: Applies to operating system providers and requires collection of age data and transmission of an age‑category signal to developers via a real‑time API, closely mirroring California’s model. 
 New York S 8102 / A 8893 Device ‑ Level Age Assurance: Applies broadly to device manufacturers, operating systems, and app stores, requiring “commercially reasonable” age assurance (not just self‑reporting) at device activation and transmission of a verified age signal to apps and websites. 
 This is just a selection of operating system and app store age assurance legislation in the United States. There have also been related but distinct laws focused on app stores passed in Texas (SB 2420), Louisiana (HB 570), and Utah (SB 142) . 
 These proposals are actively evolving. In Colorado, SB 26‑051 recently had a committee hearing on April 23, 2026 , as part of ongoing legislative consideration. The hearing reflected the complexity of balancing child safety, privacy, and feasibility, and included strong engagement from open source developers and organizations. Committee members also signaled that the intent is not to bring open source operating systems or developer infrastructure into scope, and the latest amended text clarified that software installed outside of app stores, including software downloaded from public repositories, is not in scope. 
 In Brazil, the Digital Statute for Children and Adolescents (Digital ECA) , enforceable as of March 2026, applies broadly to digital services “likely to be accessed by children and adolescents” including operating systems, app stores, and platforms, and excludes essential internet functionalities such as open technical protocols and standards. Although the Brazilian National Data Protection Agency (ANPD) has not yet formally clarified whether or how the law applies to free and open source software, its regulatory agenda has initially prioritized “app stores and proprietary operating systems,” and recent draft guidance under public consultation indicates that systems based on collaborative models and free software should not be subject to the same obligations as proprietary services. 
 Despite this, legal uncertainty has already driven some open source projects to restrict access in Brazil, reflecting concerns about the feasibility of compliance for non-commercial, volunteer-driven ecosystems. While the law was primarily designed for commercial actors, key questions about scope remain unresolved, making it critical for open source developers to actively participate in the ongoing public consultation to ensure implementation reflects decentralized development models and avoids unintended restrictions on access and innovation. 
 What is an app store, really? 
 While much of the open source community’s concern has focused on the risk that these proposals could present to open source operating systems, an equally important open question is how “application store” and “application” are defined. As drafted, some definitions of “application store” are broad enough to capture developer infrastructure—such as code collaboration platforms, package managers, and open source indexing services—simply because they allow users to access or download software. 
 Making software available for download is not the same as operating the kind of centralized, consumer-facing marketplace that most people would understand to be an app store. It is also important to define “application” precisely. Downloading software components like source code, libraries, frameworks, models, and utilities is fundamentally different from offering a standalone executable application through a consumer app marketplace. These components are upstream building blocks, not end‑user products, and the services that host or index them do not control consumer distribution or presentation in the way traditional app stores do. 
 Recent amendments and discussions across jurisdictions suggest regulators intend to focus on consumer‑facing distribution and services that control end‑user access. Clear statutory distinctions are needed to ensure laws align with that intent. This reflects a familiar challenge in technology policymaking. Frameworks aimed at youth safety and age assurance are typically responding to risks associated with consumer-facing services that collect and monetize user data, distribute content at scale, and rely on engagement-driven systems to shape user behavior. 
 By contrast, platforms that support collaborative software development serve a fundamentally different function—they are built to help users create, share, and maintain code, not to attract mass audiences, amplify content, or drive passive or excessive consumption—resulting in a materially lower risk profile. Open source communities operating on services like GitHub are organized around shared technical goals and guided by norms of collaboration, reuse, and transparency, further underscoring why these developer-focused services should be distinguished from consumer-facing platforms in regulatory design. 
 Open source software is also a key driver of economic development and innovation and functions as critical digital infrastructure. Ensuring that policies accurately reflect how open source is built and maintained is essential to preserving these benefits. When policymakers engage directly with open source developers and civil society, they are often able to refine definitions, clarify scope, and better align laws with technical realities. 
 Uncertainty around compliance requirements can be challenging for open source developers, many of whom contribute on a voluntary basis. At the same time, there are positive examples of policymakers engaging with the open source community to strike a balanced approach. The EU Cyber Resilience Act , for example, was refined through an iterative process to get the balance right for open source . Across U.S. states, these bills continue to evolve and policymakers have shown a willingness to engage with the open source community and consider changes to align with regulatory intent and technical feasibility. 
 An opportunity for engagement 
 The window for constructive engagement remains open—and developer voices can make a meaningful difference. 
 Whether through contacting elected representatives in states considering these proposals like California, Colorado, Illinois, and New York, contributing to Brazil’s Digital ECA public consultation, or engaging with organizations like the Open Source Initiative, or through foundations that steward projects that may be impacted like the FreeBSD Foundation and Debian , there are concrete ways for developers to share their perspectives—helping ensure these policies both support children’s digital safety and reflect technical realities, align with regulatory intent, and avoid unintended harm to the open source ecosystem. 
 GitHub will continue working with policymakers and the open source community to support balanced approaches that protect young people while preserving open development. We encourage developers to stay informed, connect with open source policy organizations, and reach out to us with questions or concerns. We’ll also continue this conversation with a Maintainer Month livestream on May 22 with panelists from the FreeBSD Foundation and the Open Source Initiative to discuss the broader issues raised by these proposals and how technology policy can be designed with open source in mind. 
 The post Why age assurance laws matter for developers appeared first on The GitHub Blog .
```

---

## 2. How researchers are using GitHub Innovation Graph data to reveal the “digital complexity” of nations

- 日期: 2026-05-08 15:00
- 链接: https://github.blog/news-insights/policy-news-and-insights/how-researchers-are-using-github-innovation-graph-data-to-reveal-the-digital-complexity-of-nations/

```
One of our goals for the GitHub Innovation Graph was to facilitate research on the economic impact of open source software and developer collaboration. In a paper recently published by Research Policy , four researchers used Innovation Graph data to do just that. I’m happy to share an interview with these researchers, along with our Q4 2025 data release. 
 The Research Policy paper examines whether the geography of open-source software production on GitHub can reveal the “digital complexity” of nations, and whether that complexity predicts GDP, inequality, and emissions in ways that traditional economic data misses. 
 Meet the four researchers: 
 Sándor Juhász is a research fellow at the Corvinus University of Budapest. His work focuses on economic geography, knowledge networks, and how spatial structures shape innovation. 
 Johannes Wachs is an Associate Professor at Corvinus University of Budapest, Director of the Center for Collective Learning at the Corvinus Institute of Advanced Study, and a researcher at the Complexity Science Hub in Vienna. His work sits at the intersection of computational social science and economic geography, with a particular focus on open-source software communities. 
 Jermain Kaminski is an Assistant Professor at the School of Business and Economics at Maastricht University. His research specializes in entrepreneurship, strategy, and causal machine learning, with a focus on how data-driven methods can improve decision-making and innovation. He is a cofounder of the Causal Data Science Meeting . 
 César A. Hidalgo is a professor at the Toulouse School of Economics and Corvinus University of Budapest, and he is the Director of the Center for Collective Learning. He is also the creator of the Observatory of Economic Complexity and cofounder of DataWheel . 
 Research Q&A 
 Kevin: Thanks so much for chatting, everyone! Could you give a quick high-level summary of the paper for our readers here? 
 Sándor: For the last fifteen years or so, economists have been measuring the complexity of national economies by looking at what physical products countries export, what patents they file, and what research they publish. These measures turn out to be remarkably good at predicting which countries will grow, which have high inequality, amongst many other macroeconomic features. But they all have a massive blind spot: software. 
 Jermain: Code doesn’t go through customs. It crosses borders through “ git push ”, cloud services, and package managers. So all that productive knowledge was essentially invisible, what some colleagues have called the “digital dark matter” of the economy. We decided to fix that using the GitHub Innovation Graph, which tracks how many developers in each economy push code in each programming language, based on IP addresses. We applied the Economic Complexity Index (ECI) to this data. The bottom line is that software ECI surfaces new information that trade flows, patents, and research data partly leave on the table. In particular, software ECI helps explain variation in GDP per capita and income inequality even after you control for all the traditional measures. 
 Johannes: We also found that countries don’t jump randomly between software specializations. They diversify into technology stacks that are related to what they already do, just like countries in the physical economy tend to move into products similar to what they already export. This is considered the “principle of relatedness,” and it holds for software too. 
 Kevin: Interesting! Could you provide an overview of the methods you used in your analysis? 
 Johannes: Sure. As mentioned, the core data comes from the GitHub Innovation Graph, which gives us quarterly counts of developers pushing code by economy and programming language for 163 economies and 150 languages from 2020 to 2023. But individual programming languages aren’t really the right unit, most real software uses bundles of languages together. A web app might combine HTML, CSS, and JavaScript; a data science project uses Python and Jupyter Notebook; systems programming pairs C with Assembly. 
 Sándor: So we built a separate dataset by querying the GitHub GraphQL API for all repositories active in 2024 to find which languages co-occur within the same repos. We computed cosine similarity between languages based on weighted co-occurrence, with a normalization scheme so that polyglot repos with twenty languages don’t dominate the signal, and then applied hierarchical clustering to group the 150 languages into 59 “software bundles.” Each bundle represents a coherent technology stack. 
 Jermain: …and from there, it’s the “standard” economic complexity pipeline. We build a country-by-bundle matrix, compute revealed comparative advantage, essentially asking, “does this country have a disproportionate share of developers in this bundle relative to the global average?”, binarize it, and then apply the iterative method to compute the Economic Complexity Index. Countries that specialize in many non-ubiquitous bundles score high, and countries that only specialize in things everyone does score low. For the relatedness analysis, we define proximity between bundles using co-specialization patterns. If countries that are good at bundle A also tend to be good at bundle B, those bundles are close in the software space. Then we test whether countries are more likely to enter bundles that are close to their existing specializations. 
 Kevin: Nice! Follow-up question: could you provide an “explain it like I’m five” overview of the methods you used in your analysis? 
 César: Think of countries like kitchens. Some kitchens can cook anything, since they have an abundance of ingredients and tools, from the rarest spices to the best knives. Others are more limited. Maybe they can boil rice and do a few other simple things. Since we cannot look at the kitchens directly, we need to infer their “complexity” based on the dishes they are able to produce. This is what the economic complexity index or ECI allows you to estimate. We can infer what’s going on in the kitchen by seeing if it is a chicken and rice operation, or a place that can produce sophisticated edible foams and souffles. Originally, these methods were applied to trade data, where the dishes coming out of the kitchen were a country’s exports, but in this paper, we applied that to software. A chicken-and-rice country is a Python and JavaScript country. A Michelin-star country is one that can program certified embedded systems for aerospace and defense. 
 Top 20 economies by software economic complexity 
 Ranking Economy Software ECI 
 1 Germany 1.739 
 2 Australia 1.730 
 3 Canada 1.729 
 4 Netherlands 1.727 
 5 France 1.702 
 6 United States 1.695 
 7 Poland 1.691 
 8 United Kingdom 1.687 
 9 Italy 1.672 
 10 Sweden 1.620 
 11 Switzerland 1.620 
 12 Hong Kong SAR 1.595 
 13 Norway 1.571 
 14 Japan 1.552 
 15 Spain 1.552 
 16 Russia 1.530 
 17 Singapore 1.468 
 18 Taiwan 1.464 
 19 Belgium 1.448 
 20 Finland 1.444 
 Kevin: Thanks, that’s super helpful. I’d be curious about the limitations of your paper and data that you wished you had for further work. What would the ideal datasets look like for you? 
 Johannes: One major drawback is that we only see public GitHub activity. That means we’re missing proprietary software entirely. Hence, we can’t see closed-source enterprise work, which is huge. So our measure likely underestimates software complexity in countries with a weaker open source software culture. 
 Sándor: The time window is another constraint. Four years of data (2020–2023) is enough for cross-sectional analysis but too short to credibly test long-run growth predictions, which is what economic complexity measures are really designed for. Economic structures shift over decades, not quarters. We’d love to have twenty years of this data. 
 Jermain: The dream dataset would combine GitHub-like activity data with information about the projects themselves, not just languages, but frameworks, libraries, and what the software actually does. Considering this dimension would be a natural next step for our project, and it would shed more light into software bundles and use cases. If we knew that a repo was building a fintech application versus a game engine, we could define much finer-grained capability bundles. GitHub Topics gives us a taste of this, and we used it as a robustness check, but it’s still noisy and incomplete. 
 Kevin: Do you have any predictions for the future? Recommendations for policymakers? Recommendations for developers? 
 César: Software is an interesting target for industrial policy because it is an industry that depends primarily on highly movable human capital (software developers). In principle, it provides an opportunity for development that can be incentivized via talent attraction programs. In practice, however, the high mobility of software talent can be a double-edged sword, since that makes it sensitive to consumer protection regulations that make it hard to work with data or worker protection schemes that distribute the risk of innovation to small and medium size firms (e.g. laws that on paper protect workers, but that in reality pass on that responsibility to the firms). The countries that figure out how to attract software talent without suffocating it with well-intentioned but poorly designed regulation will pull ahead. 
 Johannes: For developers, understanding that places are highly specialized in the kind of software they produce is useful when they are looking to relocate. Developers can use the product space representation of software capabilities to know which countries their skillsets are a good match for. 
 Jermain: Looking ahead, the big question is what generative AI does to this picture. If AI coding assistants lower the barrier to working in new programming languages, does relatedness weaken? Do countries diversify faster? Or does it reinforce existing advantages because the countries with the best AI infrastructure benefit most? We’re working on this, and Johannes and his colleagues have a new paper in Science on tracking the global diffusion of AI-assisted coding on GitHub. I think the answer will reshape how we think about digital complexity within the next five years. One further consideration would be how classifications of software or software bundles would be represented as NAICS or NACE industry codes. 
 Sándor: I’d add a prediction: I think we’ll see economic complexity indices based on software data become a standard part of the policymaker’s toolkit within the decade, sitting right alongside the trade-based measures. The data is open, it updates quarterly, and it captures something that traditional data genuinely can’t. 
 Personal Q&A 
 Kevin: I’d like to change gears a bit to chat more about your personal stories. Johannes, I understand that you have a background in computational social science and network science, which is a bit different from the traditional economics path. Tell us more about your path to research. 
 Johannes: I actually started in mathematics and then moved into computational social science during my PhD at Central European University in Budapest. I became enchanted by the opportunities that digital data traces present for studying human behavior. I like using network methods because they help us move between the micro level activity and interactions found in such traces and the macro outcomes. I stumbled into open source research in particular when I realized that GitHub data was this incredibly rich, publicly available record of valuable knowledge production that few people were using to study social science questions. 
 Kevin: Sándor, I see you have a background in economic geography, which is a more traditional route compared to computational social science. What was your path toward working with software data? 
 Sandor: I received my PhD in economic geography at Utrecht University, in a research community that was already using economic complexity to study regional development. So I was trained in thinking about places—cities, regions, industries—through the lens of networks and capability accumulation. 
 Kevin: Jermain, it looks like you developed practical technical expertise through some entrepreneurial projects in parallel with academic training. 
 Jermain : During my PhD at RWTH Aachen, I was a visiting researcher with Cèsar at MIT. In that time, I was also working with a colleague on a project called Moviegalaxies.com (open data) and later worked on analyzing text, speech and video data in Kickstarter projects. It was my first multimodal machine learning pipeline. From my network analysis projects, I somehow ended up analyzing passing networks for a larger German soccer team. These days my research is mostly concerned with causality and causal machine learning. In this capacity, I co-founded the Causal Data Science meeting with my colleague Paul Hünermund. 
 Kevin: César, do I have right that you have a background in Physics? 
 César: I started in physics, with a PhD at Notre Dame focused on complex networks. During that time, I realized that network tools could be used to describe the evolution and fate of economies. Eventually, this became a field that we know today as economic complexity, which studies the process of economic development by using tools from physics, economics, and computer science. 
 Kevin: Finding a niche that you’re passionate about is such a joy, and I’m curious about how you’ve found living in that niche. What’s the day-to-day like for you? 
 Johannes: Honestly, in research, the day-to-day is a mix of writing code, writing papers, and talking to people, then iterating. Of course, working at a university usually comes with teaching and administration, too. I like that I have a good amount of freedom in what I choose to work on. If a project or direction doesn’t spark joy, I can usually shift my focus. That is a unique thing. 
 Sándor: I’d add that one of the best parts of this niche is the interdisciplinary community. On any given week I might talk to an economic geographer, a computer scientist, and a physicist about the same research question. That’s unusual and very stimulating. 
 Kevin: Have things changed since generative AI tooling came along? Have you found generative AI tools to be helpful? 
 Johannes: Absolutely. We use LLM tools regularly now for things like debugging data pipelines, drafting boilerplate code, and even sanity-checking statistical approaches. It’s particularly useful in a project like where you have a lot of different methods and need to coordinate work in a team. That said, LLMs are much more helpful if you already have a clear idea in mind. 
 Kevin: Do you have any advice for folks who are starting out in software engineering or research? What tips might you give to a younger version of yourself, say, from 10 years ago? 
 César: The key is to invest in things that grow or compound. This is easier said than done because there are always distractions and temptations. I’ve seen many scholars spend months or years working on projects just because they don’t want to lose the work that they’ve already put into them. The cost of doing that is working on other projects that might matter more in ten or twenty years. Building tools that can generate an audience, like The Observatory of Economic Complexity , Data USA , or Pantheon , was challenging, but they have borne fruit for a long time. The same is true about working on a few important papers or completing a book. The question you need to ask when working on a project is whether you honestly believe that the project will be more important in a decade from now than today. If the answer is yes, that’s probably a good project. Ten years ago, I would have told myself to trust that test more and to walk away from “almost done” projects faster. Sunk costs are the most expensive thing in a research career. 
 Johannes: In can rather make suggestions for young researchers. The first is to build a broad question and research agenda to motivate what you do. You have to have a problem you care about so much that even partial or highly specific results about that problem get you excited. Once you have that, in practice I think there is a lot of value in generating your own data. I prefer applying a straightforward method to a bespoke dataset than applying a highly complex method to a dataset everyone knows. 
 Jermain: My advice echoes César’s: don’t ride a dead horse. In the years after the PhD and into assistant professorship, it’s tempting to keep milking old topics while pivoting to new ones, but this leaves you straddling two worlds and mastering neither. Pick your focus deliberately, narrow enough to build real expertise, broad enough to stay curious, and be willing to let go of past work that no longer aligns, even if it feels wasteful. 
 Sándor: I’d tell my younger self to collaborate more and earlier. This paper has four authors across five institutions in four countries. That wouldn’t have happened if any of us had stayed in our silos. Go to conferences outside your field, say yes to coffee meetings with people whose work seems tangentially related, and don’t be afraid to cold-email researchers whose work you admire. 
 Kevin: Are there any learning resources you might recommend to someone interested in learning more about this space? 
 César: The Observatory of Economic Complexity , for a web experience, and The Infinite Alphabet: and The Laws of Knowledge , for a book that puts this in context. 
 Jermain: If you’re a developer curious about the economics angle, I’d honestly just recommend browsing the Observatory of Economic Complexity and looking up your own country. See what it exports, where it sits in the product space, and then think about how software fits in. It’s a very intuitive way to build the intuition before diving into the math. 
 Kevin: Thank you, Sándor, Johannes, Jermain, and César! It’s been fascinating to learn about your current work and broader career trajectories. We truly appreciate you taking the time to speak with us and will absolutely keep following your work. 
 The post How researchers are using GitHub Innovation Graph data to reveal the “digital complexity” of nations appeared first on The GitHub Blog .
```

---

## 3. Improving token efficiency in GitHub Agentic Workflows

- 日期: 2026-05-07 23:00
- 链接: https://github.blog/ai-and-ml/github-copilot/improving-token-efficiency-in-github-agentic-workflows/

```
GitHub Agentic Workflows is like a team of street sweepers that clean up little messes in your repo. These teams significantly improve repo hygiene and quality, but as with all agentic work, cost is a growing concern for developers. And because CI jobs like agentic workflows are automatically scheduled and triggered, costs can accumulate out of view. 
 Thankfully, making automations more efficient is easier than doing the same for interactive desktop sessions. Work done during a developer session can be hard to predict, but agentic workflows’ work is fully specified in YAML and repeats every execution. 
 Because we maintain and use GitHub Agentic Workflows in our own GitHub repositories, we worry about token efficiency as much as our users. That is why in April 2026, we began to systematically optimize the token usage of many of the workflows that we rely on every day. This post describes what we instrumented, the optimizations we applied, and our preliminary results. 
 Logging token usage 
 We rely on hundreds of agentic workflows in our repos for maintenance and CI. All workflows run as GitHub Actions against real API rate limits. We are building the plane as we fly it and burning jet fuel as we go. 
 Before we could optimize our token consumption, we needed to know how tokens were consumed. The first challenge we faced was that each agent framework (Claude CLI, Copilot CLI, Codex CLI) emitted logs in a different format, and usage data could be incomplete for historical runs. Thankfully, the agentic-workflows security architecture uses an API proxy to prevent agents from directly accessing authentication credentials. This proxy gave us a way to capture token usage across all runs in a single normalized format, regardless of agent framework. 
 Every workflow now outputs a token-usage.jsonl artifact with one record per API call that contains input tokens, output tokens, cache-read tokens, cache-write tokens, model, provider, and timestamps. Combining this data with the rest of the workflow’s logs gave a historical view of how tokens were typically spent and allowed us to optimize for future runs. 
 Workflows optimizing workflows 
 With token data in hand, we built two daily optimization workflows. 
 A Daily Token Usage Auditor reads token usage artifacts from recent workflow runs, aggregates consumption by workflow, and posts a structured report. Its job is to flag any workflow that has significantly increased its recent usage, surface the most expensive workflows, and take note of anomalous runs (e.g., a workflow that normally completes in four LLM turns taking 18). 
 When an Auditor flags a workflow, a Daily Token Optimizer looks at the workflow’s source and recent logs to create a GitHub issue with describing concrete inefficiencies and proposing specific optimization. The Optimizer has found many inefficiencies that we would have otherwise missed. 
 Of course, the Auditor and Optimizer are agentic workflows themselves, and their token usage also appear in daily reports to create a small virtuous cycle. 
 Eliminating unused MCP tools 
 Based on our initial Auditor and Optimizer results, the most common inefficiency is unused MCP tool registrations. 
 Because LLM APIs are stateless, agent runtimes typically include the MCP tool function names and JSON schemas with each request. In practice, this means the full set of tools can become part of every call’s context. For a GitHub MCP server with 40 tools, this can add 10–15 KB of schema per turn. If the agent only uses two tools, the remaining 38 are pure overhead added to every request. 
 Workflow authors naturally start with a full tool-set since it is the path of least resistance, and the agent can figure out which tools it needs. But as time goes on, most workflows rely on a narrow, stable set of tools. The Optimizer identifies this pattern by cross-referencing tool manifests against actual tool calls and recommends pruning unused tools from the configuration. 
 In our smoke-test workflows, removing unused tools from the MCP configuration reduced per-call context size by 8–12 KB, saving several thousand tokens per run with no change in behavior. 
 Replacing GitHub MCP with GitHub CLI 
 Removing unused MCP tools is a relatively simple win. A larger structural opportunity was replacing GitHub MCP calls for data-fetching operations like retrieving pull request diffs, file contents, and review comments with calls to the GitHub CLI. 
 This change did more than reduce the overhead of unused tools because an MCP tool call is a reasoning step in addition to data retrieval. The agent must decide to call the tool, formulate its arguments, and receive its output as part of the context. That’s a full round-trip LLM API call, consuming tokens for the tool-use JSON schema, the argument block, and the response. Calling ‘gh pr diff’, by contrast, is a deterministic HTTP request to GitHub’s REST API with no LLM involvement. 
 We used two strategies for this migration: 
 Pre-agentic data downloads . For data that an agent will always need like a pull request diff or the list of changed files, we added setup steps in the workflow that run gh commands before the agent starts and writes the results to workspace files. The agent reads those files instead of making MCP calls. This eliminates tool-call overhead and allows the agent to take advantage of its extensive training in bash scripting to efficiently process the data. 
 In-agent CLI proxy substitution . Pre-downloading isn’t possible in cases where the agent determines what to fetch at runtime. In these cases we rely on a lightweight transparent HTTP proxy that routes CLI traffic to GitHub’s API servers without exposing an authentication token to the agent. The agent runs gh pr view –json and gets structured data back, just as a user would from a terminal. This reduces token usage without compromising our zero-secrets security requirement for the agent. 
 Together, these techniques move the majority of GitHub data-fetching out of the LLM reasoning loop. 
 Measuring efficiency gains is not easy 
 Once we began to optimize our workflows, we ran into a more nuanced problem: how do you know whether a change made things more efficient, or just made the workflow do less (and perhaps worse) work? 
 There are three confounding factors. 
 Not all tokens are created equal . Running the same workflow on Claude Haiku versus Claude Sonnet produces similar token counts but cost very differently. Haiku costs roughly 4× less per token than Sonnet, so a workflow that switches models appears unchanged in raw token count but represents a significant cost reduction. To account for this, we use an Effective Tokens (ET) metric that applies model multipliers to each token type: 
 ET = m × (1.0 × I + 0.1 × C + 4.0 × O) 
 where m is a model cost multiplier (Haiku = 0.25×, Sonnet = 1.0×, Opus = 5.0×), I is newly-processed input tokens, C is cache-read tokens, and O is output tokens. Output tokens carry 4× weight because they are the most expensive token type across all major providers. Cache-read tokens carry only 0.1× weight because they are served from cache at a fraction of the cost of fresh input. This formula normalizes consumption across model tiers so that a 10% ET reduction means a genuine 10% cost reduction regardless of which model is in use. 
 The workload is a live repository. As far as we know, there is no agentic-workflow benchmark that we can use to optimize our token usage. When we began looking at token usage by our workflows, we found that in one run a workflow would handle a five-line fix, and in the next run it would handle a 200-line pull request. The first run naturally uses fewer tokens, but the difference is not due to a sudden change in efficiency. Raw token counts can confuse workload variation with fluctuations in efficiency. We try to normalize this by tracking LLM API call counts alongside token counts; constant LLM turns-per-run and falling tokens-per-call indicate genuine efficiency improvement. Both falling together may indicate that less work is being done. 
 Does quality change? Understanding output quality is the hardest consideration. A lighter model running a more constrained workflow might produce lower-quality output. We looked at the process-level signals like output tokens per LLM call, turn counts per run, and tool-call completion rates to approximate quality. For our optimized Smoke Copilot workflow, all three remained stable across the optimization period even as token consumption fell. The workflow completes in roughly five LLM turns every run, before and after the optimizations. Of course, these are process signals, not outcome signals. We cannot directly observe whether the quality improved, degraded, or was stable, because there is no ground-truth “correctness.” Measuring tokens-per-unit-of-correct-work requires additional instrumentation and thought. 
 Initial results 
 After deploying the auditor and optimizer across a dozen production workflows in the gh-aw and gh-aw-firewall repos, we downloaded token-usage artifacts for runs before and after each was optimized and computed ET for each run. Nine of the 12 workflows received optimizer-recommended changes. We include results only for workflows with at least eight runs in both the pre- and post-optimization periods. These are: Auto-Triage Issues, Daily Compiler Quality, Community Attribution, Security Guard, and Smoke Claude. 
 Auto-Triage Issues shows a clear, sustained reduction of 62% across 109 post-fix runs. Daily Compiler Quality shows 19% improvement over 12 post-fix runs, and Daily Community Attribution shows 37% improvement over eight post-fix runs. In the gh-aw-firewall repo, Security Guard, which audits every pull request for security-sensitive changes, and Smoke Claude an integration test that exercises the firewall’s Claude CLI path, had the most post-fix runs and show improvements of 43% and 59%, respectively. 
 Run frequency matters as much as per-run savings. Auto-Triage Issues fires on every new issue (averaging 6.8 runs per day with a max of 15) while Daily Compiler Quality runs at most once per day. 62% savings and 6.8 runs/day compounds quickly: over the observation period, Auto-Triage’s optimization saved roughly 7.8 M ET in aggregate, assuming the pre-optimization rate. Security Guard and Smoke Claude run even more frequently. When prioritizing which workflows to optimize, run frequency is as important as per-run consumption. 
 It is important to note that not every optimization that the agent recommends translates into measurable ET savings, especially over short observation windows on a live repository where workload varies day to day. For example, the Contribution Check workflow experienced a 5% increase in ET, and we will discuss it in greater detail below. 
 Take aways 
 Based on these results, we highlight three patterns. 
 Many agent turns are deterministic data-gathering . Auto-Triage Issues shows the strongest sustained improvement in gh-aw (−44% across 62 post-fix runs) because the optimization eliminated structural inefficiency: many agent turns were spent on reads that required no inference, such as fetching issue metadata and scanning labels. Moving those reads into pre-agentic CLI steps before the agent starts removed them from the LLM reasoning loop entirely. The same pattern drove Security Guard’s −60% reduction in gh-aw-firewall : a relevance gate now skips the LLM entirely for pull requests that don’t touch security-sensitive files. The cheapest LLM call is the one you don’t make. 
 Contribution Check illustrates a confounding factor: 82–83% of input tokens were cache reads (data-gathering), but average ET increased 5%. This is due to a workload shift rather than optimization failure: in the pre-optimization period 41% of runs processed small pull requests (ET < 100K) and 39% processed large pull requests (ET > 300K). The post-optimization period coincided with a burst of development activity, and the workflow processed 9% small pull requests and 65% large pull requests. Output tokens, which carry a 4× weight in the ET formula, rose 14% as the agent reviewed bigger diffs. The optimization likely improved per-turn efficiency, but the shift toward heavier workloads masks that gain in the aggregate numbers. 
 Unused tools are expensive to carry. Among the excluded gh-aw workflows, the Glossary Maintainer is an instructive case. A single tool—search_repositories—was called 342 times in one run, accounting for 58% of all tool calls, despite being completely unnecessary for a workflow that only scans local file changes. Removing it from the toolset was the optimizer’s recommendation. In gh-aw-firewall , Smoke Claude’s −79% reduction was driven in part by aggressive MCP tool pruning combined with a model-tier switch to Haiku. The Daily Community Attribution workflow illustrates the limits of this approach: it was configured with eight GitHub MCP tools and made zero calls to any of them across an entire run, but removing them did not reduce ET. Tool manifests were a small fraction of this workflow’s overall context. 
 A single misconfigured rule can cause runaway loops . Also among the excluded workflows, Daily Syntax Error Quality was the highest-ET workflow in the project before optimization. The root cause was a one-line misconfiguration: the workflow copied test files to /tmp/ then called gh aw compile *, but the sandbox’s bash allowlist only permitted relative-path glob patterns. Every compile attempt was blocked. Unable to use the tool it needed, the agent fell into a 64-turn fallback loop in which it manually read source code to reconstruct what the compiler would have told it. One fix to the allowed bash patterns eliminated the loop. We did not have enough baseline runs to precisely quantify the improvement, but the pathology was clear and the fix was unambiguous. 
 What’s next? 
 The tools we use to optimize our workflows including API-level observability, automated auditing workflows, MCP tool pruning, and CLI substitution are all available today in the GitHub Agentic Workflows framework. Another upcoming optimization is refactoring monolithic agents into teams of subagents using smaller and cheaper models. 
 The next step is to move from workflow-level optimization to system-level optimization. A workflow run is not really one flat sequence of API calls. It is a chain of episodes: short phases of work like gathering context, reading artifacts, retrying after a failure, or synthesizing a final answer. Once you can see those episodes clearly, you can ask much better questions. Which episode actually caused a costly run? Which episodes are mostly repeated work, blocked work, or failed work? Which ones should stop being agentic entirely and become deterministic pre-steps? 
 That same logic applies at the portfolio level. Repositories do not run one workflow in isolation. They run a fleet of agentic automations that often trigger on the same events, inspect the same diffs and logs, and produce adjacent judgments. That means cost is not just a property of a single workflow, but also of overlap across the portfolio. The next analyses we want are portfolio-level ones: where workflows are duplicating reads, where several workflows should be consolidated, and where shared intermediate artifacts should be cached instead of rediscovered by each run. 
 Those open questions are genuinely hard. Measuring goodput still requires outcome instrumentation that does not yet exist at scale for agentic CI workflows, and understanding episode and portfolio efficiency requires richer lineage data than most systems collect today. But that is the direction that matters. The proxy-level observability and optimizer workflows have already changed how we develop and deploy new agentic automations. We add token monitoring from day one rather than retrofitting it later, and increasingly we think in terms of avoidable work across the whole automation fleet, not just expensive runs in isolation. 
 If you’re running agentic workflows in CI and wondering whether you’re spending more than you need to, the first step is the same as ours: add the API proxy, turn on logging, and let the data tell you where to look. 
 If you want to add the workflows mentioned here, you can simply drop them into your repo using the gh-aw CLI : 
 gh extensions install github/gh-aw
gh aw add githubnext/agentic-ops/copilot-token-audit githubnext/agentic-ops/copilot-token-optimizer 
 Running them alongside your existing CI will give you immediate visibility into usage and help continuously optimize your workflows over time. 
 We’d love to hear how others are approaching this problem. Share your thoughts in the community discussion or join the #agentic-workflows channel of the GitHub Next Discord . 
 Explore the GitHub Agentic Workflows repo > 
 The post Improving token efficiency in GitHub Agentic Workflows appeared first on The GitHub Blog .
```

---

## 4. Agent pull requests are everywhere. Here’s how to review them.

- 日期: 2026-05-07 19:00
- 链接: https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/

```
You’ve probably already approved one without realizing it. The tests passed. The code was clean. You merged it. 
 But it was agent-generated—and that ease of approval is exactly the problem. 
 A January 2026 study, “More Code, Less Reuse” , found that agent-generated code introduces more redundancy and more technical debt per change than human-written code. The surface looks clean. The debt is quiet. And reviewers, according to the same research, actually feel better about approving it. 
 This isn’t an argument to slow down. It’s an argument to be intentional. There’s a difference. 
 Agent pull requests are already saturating review bandwidth 
 The volume is already staggering. GitHub Copilot code review has processed over 60 million reviews, growing 10x in less than a year. More than one in five code reviews on GitHub now involve an agent. That’s just the automated review pass. The pull request themselves are multiplying faster than reviewers can handle. 
 The traditional loop—request review, wait for code owner, merge—breaks down when one developer can kick off a dozen agent sessions before lunch. Throughput has scaled exponentially. Human review capacity hasn’t. The gap is widening. 
 You’re going to review agent pull requests. The question is whether you’ll catch what matters when you do. 
 Who (or what) actually wrote this pull request 
 Before you look at a single line of diff, you need a model for what you’re reviewing. 
 A coding agent is a productive, literal, pattern-following contributor with zero context about your incident history, your team’s edge case lore, or the operational constraints that don’t live in the repository. It will produce code that looks complete. But that “looks complete” failure mode is dangerous. 
 You’re the one who carries that context. That’s not a burden. It’s the actual job. The part of review that doesn’t get automated is judgment, and judgment requires context only you have. 
 One note for authors 
 If you’re opening an agent-generated pull request, edit body before you request review. Agents love verbosity. They describe what’s better explored through the code itself. Annotate the diff where context is helpful. And review it yourself before tagging others, not just to check correctness, but to signal that you’ve validated the agent captured your intent. 
 Reviewing your own pull request isn’t optional when agents are involved. It’s basic respect for your reviewer’s time. 
 Now, back to reviewers. The pull request lands in your queue. The author did their part. Here’s what to watch for. 
 Red flags to watch for 
 1. CI gaming 
 Agents fail CI. When they do, they have an obvious path to get tests passing: remove the tests, skip the lint step, add || true to test commands. Some agents take it. 
 Any change that weakens CI is a blocker. Full stop. Before approving any agent pull request, check: 
 Did coverage thresholds change? 
 Were any tests removed, renamed, or marked as skipped? 
 Did the workflow stop running on forks or pull requests? 
 Are any CI steps now gated behind conditions they weren’t before? 
 Yes, to any of those means you need an explicit justification before you continue. 
 2. Code reuse blindness 
 This is the highest-ROI thing you can do as a reviewer. Agents look for prior art. They’ll find a pattern in the codebase and replicate it, often without checking whether a utility that already does the same thing exists somewhere else. The symptoms: new utility functions that duplicate existing ones with slightly different names, validation logic reimplemented in multiple places, middleware written from scratch that already lives in a shared module, helpers that are “almost the same” but with different names. 
 The agent’s local context doesn’t include the full picture of what exists across your repository. You do. 
 For every new helper or utility in an agent pull request, do a quick search. If you find an equivalent, don’t leave a comment. Require consolidation before merge. The cost of leaving duplicated logic is that agents will find it as prior art and replicate it further. 
 💡 Pro tip: Require justification for adding new utilities in agent pull requests above a size threshold. This catches the duplication problem early. 
 3. Hallucinated correctness 
 The obvious hallucination (calling an API that doesn’t exist, referencing a variable out of scope) gets caught in CI. The dangerous one is subtler: code that compiles, passes every test, and is wrong. 
 Off-by-one errors in pagination. Missing permission checks on a branch that’s never hit in tests. Validation that short-circuits under an edge case the agent never considered. Wrong behavior under a race condition that only surfaces at scale. 
 Trace it, don’t just scan it. Pick the most critical path in the diff. Follow it from input through every transform to output. Check boundary conditions (zero, max, empty), missing validation on external values, permission checks on every branch, and surprising conditional logic. 
 Require a new test that fails on the pre-change behavior. If the agent can’t write a test that would have caught the bug it claims to fix, the fix is incomplete or the understanding is wrong. 
 4. Agentic ghosting 
 You leave a thorough review. You explain the issue, provide context, suggest a direction. The pull request goes quiet. Or the agent responds and misses the point entirely and runs in circles. You invest another round. Still nothing useful. 
 Larger pull requests with no structured plan correlate strongly with agent abandonment or misalignment. The larger and less scoped the pull request, the more likely you’re going to sink review time into something that goes nowhere. 
 Before you invest deep review on a large agent pull request check the pull request history. Has it been responsive in previous rounds? Does it have a clear implementation plan, or did the agent just start writing code? 
 If there’s no plan, request a breakdown before you write a single comment. Copy-paste version: 
 “ This pull request is too large for me to review without a clearer implementation plan. Can you break it into smaller scoped units, or add a summary of what each part does and why it’s structured this way? Happy to review after that. “ 
 Firm, short, not personal. And it saves you an hour. 
 5. Untrusted input in workflows 
 Prompt injection in CI agents is real and underappreciated. Here’s the pattern: an agent workflow reads content from a pull request body, an issue, or a commit message. That content gets interpolated into a prompt. The prompt goes to a model. The model output gets piped to a shell command. The whole thing runs with GITHUB_TOKEN permissions. 
 When you’re reviewing any workflow that calls an LLM, these are blockers: 
 Is untrusted user input, pull requestbodies, issue bodies, commit messages, being interpolated into prompts without sanitization? 
 Is GITHUB_TOKEN write-scoped when it only needs read access? 
 Is model output being executed as shell commands without validation? 
 Are secrets accessible to the agent step or being printed to logs? 
 What to require before merge: least-privilege permissions in the workflow YAML (permissions: read-all is a reasonable default), sanitize and quote untrusted content before it touches a prompt, separate the “analysis” step from the “execution” step with a human approval gate for anything touching production, never eval model output. 
 Time Step What to do 
 1–2 min Scan and classify Look at the file list and diff size. Narrow task (docs, CI, small change) or complex (multi-file, logic, performance, tests)? That classification sets your review depth for everything that follows. 
 2–3 min Check CI changes first Before reading a single line of app code, look at anything touching .github/workflows, test configs, coverage settings, or build scripts. Flag anything that weakens CI. Stop sign check. 
 3–5 min Scan for new utilities Search for new functions, helpers, or modules. For each one, do a quick repo search to check for duplicates. Flag anything that reinvents existing functionality. 
 5–8 min Trace one critical path Pick the most important logic change. Trace it end-to-end: input → transforms → output. Check boundary conditions, permissions, unexpected branching. This is the step you can’t skip. 
 8–9 min Security boundaries If this PULL REQUEST touches any workflow that calls an LLM or handles untrusted input, run through the security checklist above. 
 9–10 min Require evidence For any non-trivial logic change, require a test that fails on the pre-change behavior. No rollback plan for risky changes? Ask for one. 
 When to request a smaller pull request: 
 The diff touches more than five unrelated files 
 You can’t describe the purpose of the pull request in one sentence 
 The agent has no implementation plan or the pull request body is empty 
 CI is failing and the only changes in the diff are to test files 
 Let Copilot review it first 
 Use automated review for what it’s good at: catching the mechanical stuff before a human has to. Copilot code review flags style inconsistencies, obvious logic errors, missing error handling, and type mismatches. It handles the low-level scan. That frees you up for the judgment work, which is where your time actually matters. 
 Treat it as a prerequisite, not a replacement. Let Copilot run first. If it catches something obvious, let the author address it before you invest your review time. 
 You can tune this with custom instructions specific to your team: flag anything that modifies CI thresholds, surface new utilities for deduplication review, check that every external input is validated. The more specific your instructions, the more useful the automated pass. 
 💡 Pro tip: I recently experimented with codifying my own review checklist using the Copilot SDK. Instead of remembering to run the same security checks on every pull request, I built a workflow that takes my personal checklist—auth on admin endpoints, tests actually running, safe env variable handling—and runs it against the diff automatically. If it finds critical issues, it blocks the merge. 
 Judgment is the bottleneck, and that’s fine 
 The surface area of code is growing. pull request volume is growing. The time you spend scanning boilerplate should shrink. 
 What doesn’t shrink is the context you carry. The things you know about your system that aren’t written down anywhere. That’s what makes your review valuable, and it’s the part that doesn’t get automated. 
 Three takeaways: 
 Any CI weakening is a hard stop. 
 Let the agents scan first. You trace the critical path. 
 Red flag checklist as your default on complex agent pull requests. 
 Read the docs > 
 The post Agent pull requests are everywhere. Here’s how to review them. appeared first on The GitHub Blog .
```

---

## 5. Validating agentic behavior when “correct” isn’t deterministic

- 日期: 2026-05-06 21:16
- 链接: https://github.blog/ai-and-ml/generative-ai/validating-agentic-behavior-when-correct-isnt-deterministic/

```
Modern software testing is built on a fragile assumption: correct behavior is repeatable. For deterministic code, that assumption mostly holds. But for autonomous agents like Github Copilot Coding Agent (aka Agent Mode), especially as we explore the frontiers of integrated “Computer Use,” that assumption breaks down almost immediately. 
 As agents move beyond simple code suggestions to interacting with real environments like UIs, browsers, and IDEs, correctness becomes multi-path. Loading screens can appear or disappear, timing shifts, and multiple valid action sequences can lead to the same result. Unless our GitHub Actions workflows are robust enough to account for this variability, it’s common for an agent to succeed at a task while the test still fails—a “false negative” that halts production. 
 This blog post explores how to move past brittle, step-by-step scripts and toward an independent “Trust Layer” for agentic validation. We will demonstrate a model that focuses on essential outcomes rather than rigid paths, providing a way to validate behavior that is explainable, lightweight, and ready for real-world CI pipelines. 
 The challenges of agent-driven validation 
 Imagine you’re responsible for a GitHub Actions pipeline that relies on Copilot Agent Mode to validate real-world workflows. The agent could be leveraging Computer Use, navigating within a containerized cloud environment, for the workflow validation. 
 On Tuesday, the build is green. On Wednesday, the test fails—even though no code has changed. 
 Here’s what happened: A minor network lag on the hosted runner caused a loading screen to persist for a few extra seconds. The agent waited, adapted, and successfully completed the tasks correctly. But your CI pipeline still flagged the run as a failure—not because the task failed, but because the execution path no longer matched the recorded script or assertion timing. 
 The agent didn’t fail. The validation did. 
 This surfaces three recurring pain points that create a “trust gap” in agent-driven testing: 
 False negatives: The task succeeded, but the test runner could not tolerate variation. 
 Fragile infrastructure: Tests fail due to timing, rendering, or environmental noise unrelated to correctness. 
 The compliance trap: The outcome may be correct, but a regression is flagged because the agent’s behavior diverges from what the automated test expected. 
 We’re in a transition period where agentic systems like Github Copilot Coding Agent are enabling faster development, but our traditional validation approaches remain rigid. In deterministic software, correctness is as simple as matching a specific input to a known output. But with agents, the process in between is intentionally non-deterministic. As agents are increasingly deployed in production, correctness isn’t about following a prescribed set of steps—it’s about “reliably achieving the essential outcomes.” 
 To scale these systems, we need a validation framework that can distinguish between “incidental noise” (e.g., a loading screen) and “critical failures” (e.g., failing to save data). Correctness shifts from “did this happen?” to “what had to happen for success to be real?” 
 Why existing testing approaches break down for autonomous agents 
 Traditional testing tools work well when execution paths are fixed. They struggle when behavior branches—the tools begin to fracture, not because they’re poorly engineered, but because they assume a stable sequence. 
 When we apply these to a Copilot Coding Agent, including when navigating a containerized environment, the limitations become clear across four common paradigms: 
 Assertion-based testing: Requires manual, labor-intensive specifications for every check and fails to account for valid alternative execution paths. 
 Record-and-replay tools: Highly sensitive to environmental noise; minor rendering differences or timing variations often trigger false failures. 
 Visual regression testing: Compares screenshots in isolation without understanding the broader execution flow or semantic meaning. 
 ML oracles: These “black boxes” require thousands of training examples and offer no explainability when they flag a behavior as incorrect. 
 While these approaches differ in implementation, they share a common structural assumption: Correctness is defined by adherence to a particular sequence of observable states. 
 For agentic systems, that assumption breaks down. To build true developer trust in these systems, including Github Copilot, we must move beyond checking linear scripts and start validating structured behaviors . 
 Reframing correctness: Essential vs. optional behavior 
 To move past brittle tests and build the Trust Layer, we have to fundamentally change how we define “correct.” In agentic systems, correct executions don’t have to look identical. They do need to share a common logical structure. 
 The conceptual shift 
 Think of a computer use-enabled Github Copilot Coding Agent performing a search in VS Code in a containerized cloud environment. In one run, a loading screen appears for several seconds; in another, the UI loads instantly (shown below). 
 Scenario: Opening VS Code A traditional test sees these as two different results. But to a developer, the loading screen is incidental ; it doesn’t change whether the task was successful. 
 We can classify agent behavior into three categories: 
 Essential states: Milestones that must occur for success to be real, such as reaching the “Search Results” screen. 
 Optional variations: Incidental states such as loading spinners or decorative UI changes that vary based on environment. 
 Convergent paths: Different sequences of steps (like using a hotkey vs. a menu) that ultimately rejoin at the same outcome. 
 A loading screen may appear or not. But search results must appear. Only one of these determines correctness. 
 From intuition to theory: Dominator analysis 
 The distinction between “must-have” and “incidental” behaviors is a concept rooted in compiler theory known as dominator relationships . 
 In a control-flow graph, a node A “dominates” node B if every path from the start to B must go through A. 
 By applying dominator analysis to agent execution traces, we can automatically identify: 
 Which states are mandatory 
 Which states are optional 
 Where different paths converge 
 This lets us extract a minimal, explainable definition of correctness. 
 Modeling executions as graphs, not scripts 
 To capture the complexity of agentic behavior, we must move away from treating executions as linear, one-dimensional scripts. Instead, our framework models behavior using a graph-based structure known as a Prefix Tree Acceptor (PTA) . 
 From linear traces to structured graphs 
 In this model, an execution is not a series of commands but a directed graph where: 
 Nodes represent observable states, such as screenshots for UI agents or code snapshots for development agents. 
 Edges represent transitions, capturing the actions (clicks, keystrokes, or API calls) taken to move between states. 
 Why graphs matter 
 Treating executions as graphs allows us to represent branching and convergence—concepts that are impossible to capture in a linear script. 
 Branching accounts for non-deterministic environment changes, like the presence or absence of a loading screen. 
 Convergence identifies where these different paths rejoin, signaling that the agent has successfully navigated a variation and returned to the primary task flow. 
 By shifting the representation from a sequence of steps to a structured behavior model, we stop penalizing agents for taking a different path and start validating whether they followed a logically sound one. 
 How we solve it: A structural approach to correctness 
 To move agents from experimental demos to production-grade infrastructure, our team developed a novel validation algorithm that moves away from rigid scripts and instead learns by example . To test this, we focused on a complex non-deterministic environment: an AI agent navigating Visual Studio Code via “Computer Use.” By observing just 2–10 successful sessions, our algorithm automatically constructs a “ground truth” model that distinguishes between an agent’s valid variations and actual failures. 
 The workflow: From traces to a “master” graph 
 Capture (PTA Construction): We collected 2–10 successful execution traces and converted them into Prefix Tree Acceptors (PTAs) , directed graphs where nodes represent observable UI states and edges represent actions. 
 Generalize (Semantic Merging): Our algorithm merged these traces into a unified graph. It employed a three-tiered equivalence detection framework —combining fast visual metrics with LLM semantic analysis—to decide if two states are logically equivalent, such as ignoring a timestamp change while flagging a missing UI control. 
 Extract the Skeleton (Dominator Analysis): We applied dominator analysis to the merged graph to identify “essential states,” milestones every successful run must pass through—while automatically filtering out “optional” states like loading spinners. 
 This approach is uniquely powerful for developers because it requires no manual specification and no large-scale model training. Because the resulting model is a graph of actual execution states, the decisions are entirely explainable. When validation fails, our algorithm provides clear failure reasoning by identifying exactly which essential state was missed. 
 Deciding when two states are “the same” 
 State equivalence is the hardest problem in agent validation. For example, how do we know if two different screenshots represent the same logical UI state? 
 We solve this using a three-tier equivalence detection framework that moves from fast visual metrics to deep semantic understanding: 
 Visual metrics: We use fast perceptual hashes and structural similarity (SSIM) to catch near-identical states immediately. 
 Semantic analysis via LLM: When visual metrics are ambiguous, we use a multimodal LLM to decide if differences are semantically meaningful. For example, the LLM knows to ignore a timestamp change or a different window decoration but will flag a different error message or missing UI control. 
 Conservative merging: We only merge states when the model is certain they are equivalent, allowing the graph to naturally branch where execution paths genuinely diverge. 
 This is not a naive pixel-by-pixel comparison, nor is it “LLM hand-waving” where the model is asked to judge the whole task. By using the LLM defensively and sparingly to resolve specific ambiguities, our framework remains robust enough to handle UI noise but precise enough to detect a real regression. 
 Extracting what actually matters with dominator analysis 
 Once the various execution traces are merged into a unified graph, our algorithm applies dominator analysis to isolate the core skeleton of the task. 
 Defining “essential” through dominance: In graph theory, State A dominates State B if every possible path from the start to B must pass through A. In our model, we define a state as essential if it is a dominator for the successful completion of the task. 
 The filtering process: By calculating these mathematical relationships, the algorithm automatically distinguishes between “must-have” milestones and “incidental” noise . 
 In our VS Code experiments, the “Search Dialog” state is identified as an essential milestone because it is a mathematical dominator—it is logically impossible to reach the results without first triggering the search. Conversely, a “Loading” screen dominates nothing; because it is bypassed in faster runs, the algorithm flags it as an optional variation rather than a requirement for success. This ensures the “Trust Layer” framework only alerts you when a critical step is missed—not when the environment fluctuates. 
 Scenario: Opening VS Code By extracting these essential nodes into a dominator subtree , we create a “ground truth” model that represents the minimal, explainable definition of correctness. This shifts the validation focus away from the specific steps the agent took and toward the critical checkpoints it was required to hit. 
 Validating new executions in practice 
 With the dominator tree established as our ground truth, validating a new, unseen execution becomes a process of structural comparison rather than a search for a perfect match. This ensures that as long as an Agent Mode hits the “must-have” milestones, it is free to navigate the environment, or adapt its integrated Computer Use path, as it sees fit. 
 When a new execution trace arrives, our validation algorithm extracts its sequence of states and checks it against the dominator tree using topological subsequence matching. 
 The logic: We don’t require the new trace to be identical to the reference; we only require that the essential states appear in the correct relative order. 
 Handling extras: If the reference sequence is A → B → C and the agent produces A → X → B → Y → C, the test still passes because the extra states (X, Y) are treated as incidental noise. 
 Detecting failure: A failure is triggered only if an essential state is skipped or if the states appear out of the required logical order. 
 Scoring and explainability 
 Our framework produces more than just a binary pass/fail; it provides a coverage metric and a clear explanation: 
 Coverage: Calculated as the percentage of matched essential states relative to the total number of states in the reference model. 
 Failure reasoning: If a trace fails, our algorithm identifies exactly which state was missing (e.g., “Failed: State ‘Search Results’ never reached after ‘Search Dialog’”). 
 This level of detail transforms the validation from a “black box” into a diagnostic tool that developers can actually use to debug their agents and their environments. 
 What we learned from evaluation 
 To prove the efficacy of this structural approach for Trust Layer, we conducted a controlled experiment comparing our Dominator Tree method against an agent’s self-assessment (where the Computer-Use Agent, or CUA, reports its own success) in a real-world scenario: a Copilot Agent custom VS Code extension test suite. 
 The accuracy gap 
 In tests designed to differentiate successful executions from those failing due to product bugs or agent errors, the results were definitive: 
 Metric CUA Self-Assessment PTA (Dominator Tree) 
 Accuracy 82.2% 100% (+17.8) 
 Precision 83.3% 100% (+16.7) 
 Recall 60.0% 100% (+40.0) 
 F1-Score 69.8% 100% (+30.2) 
 While the agent (CUA) frequently misreported failures as successes, often due to timing out or misinterpreting its own state, the Dominator Tree achieved perfect differentiation by focusing on whether essential milestones were actually reached. 
 Identifying “not a bug” scenarios 
 The most significant impact for developers is in the reduction of “false alarms.” When a test fails, you need high-signal feedback to know if the product code is broken or if the agent simply stumbled due to environmental noise. 
 The “Self-Verification” Gap: In our evaluation, the agent’s internal self-assessment (CUA) was completely unable to identify “Not a Bug” scenarios ( 0% F1-score ). This shows that agents cannot yet reliably grade their own homework in non-deterministic environments. 
 The Structural Advantage: By using state and action equivalence within the dominator model, our independent Trust Layer achieved a 52.2% F1-score in correctly identifying when a failure was an agent execution error rather than a product regression. 
 The takeaway 
 Structural validation beats self-reported success by a wide margin. By moving the “source of truth” from the agent’s internal logic to a learned external structure, we can significantly reduce the manual review time wasted on flaky test results and false positives in CI pipelines. 
 Where this fits in developer workflows today 
 For this Trust Layer framework to be effective, it must move beyond a research prototype and integrate directly into the systems developers use every day. By treating correctness as a learned structure rather than a rigid script, we can significantly improve the reliability of production-grade automation within the GitHub ecosystem. 
 Integration points 
 This approach is designed to strengthen several critical areas of the software development lifecycle: 
 GitHub Actions Pipelines: By reducing false negatives caused by environmental noise (like transient loading screens), this method provides a “higher signal” for automated builds, preventing unnecessary pipeline blocks. 
 Regression testing: Developers can use a handful of verified traces from a stable version to create a “ground truth” model that automatically validates future updates. 
 Agent evaluation: Instead of relying on an agent to report its own success, teams can use structural validation to measure how often an agent actually hits essential milestones. 
 UI automation: The framework allows for more robust automation of complex desktop and web apps where UI elements or paths may shift slightly between versions. 
 The ultimate goal of this framework is to move agents from “experimental demos” to “production infrastructure.” By providing reasoning, where a failure clearly points to a missing essential state, we give developers the transparency they need to trust autonomous systems in their workflows. 
 What’s next 
 While structural validation represents a significant leap forward, our current framework has a few boundaries as it moves toward full maturity. 
 Current limitations include: 
 Requirement for success traces: The algorithm “learns by example,” meaning it requires 2–10 successful execution traces to build its ground truth model. It cannot yet learn or define correctness exclusively from failure logs. 
 LLM dependency: Our semantic equivalence checking currently relies on multimodal LLM access. While this enables the “intelligence” to ignore timestamps or window decorations, it introduces an external API dependency and associated latency into the validation layer. 
 Temporal blind spots: The current implementation validates the order of events, but cannot yet flag if a specific state (like a loading spinner) persists for too long. 
 Future work includes: 
 Temporal and negative constraints: Future work focuses on capturing timing requirements (e.g., “loading must resolve within five seconds”) and learning from negative examples to explicitly block known failure paths. 
 Hierarchical and multimodal abstraction: The framework will evolve to cluster low-level screenshots into high-level concepts (e.g., a “Launch Sequence”) while integrating non-visual signals like DOM structures, accessibility trees, and network traffic. 
 Online learning: We aim to implement real-time model refinement. As our algorithm validates new successful runs, it will recompute dominators to continuously improve its understanding of what is truly “essential.” 
 Why this matters now 
 As AI agents move from experimental demos to core infrastructure, validation has to evolve with them and move past brittle scripts to resilient systems. 
 We don’t need black-box models to judge other black-box models. We need structural guarantees developers can inspect, reason about, and trust. 
 By combining classic compiler theory (i.e., dominator analysis) with multimodal AI, we’ve demonstrated that it’s possible to learn an explainable, robust definition of success from just a handful of examples. This framework for the Trust Layer provides: 
 Efficient learning: Automatic derivation of ground truth from passing examples. 
 Operational robustness: Secure handling of non-deterministic behavior and environmental noise. 
 Total transparency: Explainable results with clear reasoning that developers can act upon. 
 As we move forward, focusing on these practical, explainable paths will be essential to ensuring that the GitHub Copilot Coding Agent is not just powerful, but also a trustworthy component of the developer workflow. This is particularly critical with the increasing adoption of Computer Use in the overall AI-native development lifecycle. By moving the “source of truth” from an agent’s internal logic to a learned external structure, we provide the guarantees needed to make autonomous agents viable, production-grade tools in modern infrastructure. 
 Our journey toward verifiable autonomy is just beginning. For a deep dive into our Dominator Analysis-based framework, you can read the complete paper . 
 The post Validating agentic behavior when “correct” isn’t deterministic appeared first on The GitHub Blog .
```

---

## 6. Welcome to Maintainer Month: Celebrating the people behind the code

- 日期: 2026-05-05 14:30
- 链接: https://github.blog/open-source/maintainers/welcome-to-maintainer-month-celebrating-the-people-behind-the-code/

```
At a Maintainer Unconference in Brussels this year, a breakout session had maintainers jotting down thoughts on the future of open source. One sticky note stood out: 
 As AI gets better at writing code, human work around code becomes more important and more invisible. 
 Mentoring new contributors, building trust across a community, making the judgement calls that shape a project’s direction: that’s the work that turns a repository into a living collaboration. And with the speed of AI, the people doing the work are carrying more than ever. Pull requests merged on GitHub have nearly doubled year over year, and agentic workflows are accelerating the pace even further. As one maintainer put it: 
 How much time should I spend on something that you didn’t spend any time on? 
 I’ve been part of Maintainer Month for five years now. The conversations I’m having with maintainers this year feel different—there’s a weariness, but there’s also innovation. Maintainers are converging on standards like agents.md, building trust systems, and designing workflows that put them back in control. In February, Ashley Wolf named the influx of low-quality contributions open source’s Eternal September . Maintainers told us exactly what they needed. We took notes. 
 Six years ago we started Maintainer Month because the people behind open source deserve better tools , real resources , and community . This year, we’re going bigger on all three. 
 Tools: Big releases for maintainers this month 
 Maintainers need better ways to manage who contributes, how, and at what volume. In the Eternal September post, we shared some of the directions we were exploring. Here’s where things stand. 
 Granular contribution limits: This one’s for every maintainer who’s watched their pull request queue turn into a firehose. This gives maintainers the ability to introduce limits on how many pull requests a new or unknown user can make in your project. No more choosing between closing the doors and opening the floodgates. You control how much you let in. 
 Pull request archiving pairs with it. Sweep spam pull requests out of public view. No more emailing support to clean up your repo. 
 And there’s a brand new accessibility best practices guide on opensource.guide. Practical steps to make your project usable by everyone. 
 And we haven’t been waiting around. Since February, we’ve also shipped: 
 Pull request creation controls : restrict pull request creation to collaborators only, or disable pull requests entirely. (Also useful for mirrors, roadmaps, or other repositories where pull requests aren’t appropriate.) 
 Pinned comments on issues : pin the most important comment to the top of any issue thread. 
 Sort notifications oldest-first : work through your backlog in order instead of always chasing the latest ping. 
 File upload in issue forms : structured issue templates now support file uploads. 
 We’re building these because maintainers asked for them. Specifically, repeatedly…and often loudly! We hear you, and we’re going to keep shipping. Please keep flagging. 
 Resources: Who else is showing up 
 We asked companies and foundations across the ecosystem to show up for Maintainer Month. And they did! Sentry , OpenJS Foundation , Daytona , and more partners are putting real resources behind maintainers: free tools, compute credits, threat intelligence, conference tickets, and more. 
 Open source runs on maintainers, and we’re proud to partner with GitHub to celebrate and support them. As the ecosystem scales, maintainers are doing more than ever to keep projects secure and reliable. Maintainer Month is a chance to connect, share knowledge, and remind them they’re not doing this alone. 
 Robin Ginn, OpenJS Foundation 
 Partners across the ecosystem are offering real resources for maintainers. Here’s what’s available: 
 Sentry: Sentry for Open Source 
 Daytona: $100 in compute credits for maintainers (and up to $10,000 for projects via Startup Grid) 
 Mockoon: Free Mockoon Cloud accounts for OSS projects 
 Ref.tools: Free project planning tools for your team 
 Arachne Digital: Free cyber threat intelligence reporting for OSS projects 
 Radix / .Tech: Free 1-year .tech domain for maintainers 
 OpenJS Foundation: 15% discount on RenderATL tickets (code: OPENJSGITHUB) 
 Open Source Initiative: The maintaine.rs book, free for all maintainers 
 Web Summit: Conference tickets (details coming soon) 
 Last year, Sentry celebrated companies that fund open source on a Times Square billboard for Maintainer Month. That’s the energy we’re looking for. 
 Want to join them? Whether you’re a company that depends on open source, a startup, or an educator— reach out about the Partner Pack or explore the GitHub Partner Program for more ways to get involved. 
 Maintainers, here’s where you can claim your Partner Pack benefits. 
 And if you maintain open source tools for science: the new Open Source for Science Fund just launched with $20 million in funding. Grants up to $1 million for projects supporting data-intensive research. Letters of intent open May 11. 
 Community: You shouldn’t have to do this alone 
 There are 20+ events and streams (and counting!) scheduled throughout Maintainer Month. Here are a few we’re excited about: 
 FOSS United Foundation: Maintainers Meetup Delhi (May 9, India). Unconference-style gatherings for maintainers across India. 
 PyCon US 2026 (May 13–19, Long Beach). Come find us there! 
 Discussion: How should corporations support OSS maintainers? (May 14, virtual). An open discussion on corporate OSS support. 
 Open Source Assistive Technology Hackathon (May 21-22, San Francisco). A two-day hackathon focused on making open source assistive technology more accessible. 
 What Maintainers Need to Know about Open Source Licensing, SBOMs and Security (May 27, virtual). The EU’s Cyber Resilience Act is here and it affects open source. Come get the practical rundown. 
 We’d love to see you there, whether you maintain a project with millions of users or you’re just getting started. 
 Check out the full schedule > 
 Part of something bigger 
 One thing we heard over and over from maintainers this year: they want to be ”part of something bigger and not just being a solo maintainer.” If you maintain an open source project and want to connect with others who get it, request to join the Maintainer Community , a vetted space to share experiences, get support, and have honest conversations. It’s where the “how are you handling this?” sharing of best practices is happening. 
 Community members also get access to an exclusive tier of the Partner Pack, with deeper discounts, higher credit limits, and offers you won’t find in the public pack. 
 Request to join > 
 Get involved 
 Sponsor a maintainer . Financial support is one of the most direct ways to say “your work matters.” 
 Host or attend an event. Browse the schedule or submit your own event . 
 Share your story. Tag #MaintainerMonth on social media. Tell people about the project you maintain and what it means to you. The best way to celebrate maintainers is to make their work visible. 
 Say thank you. Find a project you depend on and tell the maintainers you appreciate them. It matters more than you think. 
 Open source is changing fast. What hasn’t changed is that real people wake up every day and choose to maintain the software the world runs on. They do it because they believe in it, and millions of us depend on that choice. 
 This month is for them. Show up, pitch in, say thank you. Let’s make it count. 
 See everything happening this Maintainer Month > 
 The post Welcome to Maintainer Month: Celebrating the people behind the code appeared first on The GitHub Blog .
```

---

## 7. Register now for OpenClaw: After Hours @ GitHub

- 日期: 2026-05-04 15:00
- 链接: https://github.blog/open-source/register-now-for-openclaw-after-hours-github/

```
OpenClaw , one of the fastest-growing open source projects, has already picked up over 350,000 stars and an early community of builders exploring what agentic systems can actually do in practice. 
 That’s why, on June 3, 2026, we are hosting OpenClaw: After Hours at GitHub HQ in San Francisco. The event will take place during Microsoft Build 2026 . 
 This evening is a chance to bring the OpenClaw community together into the same room. 
 We’ll kick things off in the early evening with a fireside conversation featuring Peter Steinberger , the ClawFather and creator of OpenClaw, followed by a panel with OpenClaw maintainers and ecosystem builders sharing what’s working—and what’s not—when shipping real agentic systems. 
 Later in the evening, we’ll move into a series of fast-paced lightning talks and close things out with a relaxed happy hour to connect with other builders. 
 If you have been following the project or building with it yourself, this is a good chance to meet others, trade notes, and get your claws into what people are actually shipping. 
 👉 For the full agenda and speaker lineup, please see the registration page . 
 📍 GitHub HQ , 275 Brannan St., San Francisco 
 🗓 June 3 , 5:30 p.m. – 9 p.m. 
 📺 Livestream : twitch.tv/github 
 Drinks and snacks will be provided. There will be a lot here to chew on. No shellfish behavior please . And bring your sharp ideas! 
 Spots are limited , so register early and come ready to share what you are working on. 
 ‼️ Please note: Submitting a registration does not guarantee attendance. We’ll follow up to confirm successful registrations. 
 Register now 
 What is OpenClaw? 
 OpenClaw is an open source framework for building and running agentic systems, focused on giving developers real control over how agents execute tasks in the wild. It provides the core pieces for orchestrating tools, managing state, and handling long running workflows, so you can move beyond prompt demos and ship systems that actually do work. It’s also probably convinced more than a few people to buy a Mac Mini just to run “one small experiment” that somehow turned into a permanent setup. 
 Hear more about OpenClaw from the creator himself, Peter Steinberger: 
 The post Register now for OpenClaw: After Hours @ GitHub appeared first on The GitHub Blog .
```

---

## 8. GitHub Copilot CLI for Beginners: Interactive v. non-interactive mode

- 日期: 2026-04-30 16:09
- 链接: https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-for-beginners-interactive-v-non-interactive-mode/

```
Welcome to GitHub Copilot CLI for Beginners! In this series (available in video and blog format), we’ll give you everything you need to get started using GitHub Copilot CLI , from your first prompt to tips for navigating the command line like a pro! 
 In this blog, we’ll cover the two main modes of the CLI: interactive and non-interactive. You’ll learn the differences between the two modes, how to enter them, and what they’re most useful for. 
 Let’s dive in! 
 What is GitHub Copilot CLI interactive mode? 
 Interactive mode is a back-and-forth, chat-like experience. When you launch Copilot CLI with Copilot, you’re already in interactive mode—that’s the default. Non-interactive mode is a separate option for when you want a quick, one-off answer without entering a session. (More on non-interactive mode later!) 
 In interactive mode, you can ask GitHub Copilot a question, review its response, and then either follow up with questions or another prompt—all within the same session. This is the mode for those who want to work hands-on with Copilot and iterate as you go. 
 Here’s how to enter interactive mode: 
 From the command line, type copilot and hit Enter . 
 Copilot may ask you to trust this folder, because it needs permission to read and modify files. 
 Ask Copilot a question, like “How do I run this project locally?” 
 Copilot will give you instructions, which you can do on your own. But if you want to work collaboratively, you can ask Copilot: “Can you run it for me?” 
 Copilot will analyze your project and then start the server. 
 We can review our project, decide what changes we want, and continue working with Copilot, all in the same session. 
 What is GitHub Copilot CLI non-interactive mode? 
 On the other hand, non-interactive mode is designed for speed and simplicity. Instead of having to enter a full session, you pass a single prompt right in the command line and get a response almost immediately, without needing to follow up with Copilot. 
 Designed as an in-line experience, this mode is perfect for quick, one-shot prompts like summarizing a repository, generating code snippets, or plugging Copilot into automated workflows, without leaving your shell context. Once you get an answer, you’re right back in your terminal flow. 
 Here’s how to enter non-interactive mode: 
 Start at the regular command line (if you’re in Copilot, you’ll need to exit). 
 Type copilot -p and prompt the agent with something like “Quickly summarize what this repository does and the key folders.” 
 Copilot will sift through your project files to provide an answer. Ta-da! ✨ 
 Together, these two modes help you tackle all kinds of projects efficiently: interactive for explorative, deeper work, and non-interactive for fast, focused results when you already know exactly what you need. 
 How to resume a previous Copilot session 
 Sometimes, you may want to pick up right where you left off in a previous Copilot session, while retaining all the context from that conversation. 
 If you’re in interactive mode, you can type /resume into the command line and Copilot will let you choose a previous session from a list. If you want to launch directly into the previous session picker from non-interactive mode, use copilot --resume . 
 It only takes one command to pick back up with Copilot, which is super useful if you already know what session you want to work in. 
 Take this with you GitHub Copilot CLI interactive and non-interactive modes are the fastest ways to prompt Copilot directly from your terminal. Having the option to pick between back-and-forth coding and quick prompting means you can work with Copilot, the way you want. 
 Keep an eye out for more videos in the GitHub Copilot CLI for Beginners series, where we’ll explore: 
 Copilot CLI slash commands 
 Using MCP servers with Copilot CLI 
 And more! 
 Happy coding! 
 Looking to try GitHub Copilot CLI? Read the Docs and get started today. 
 More resources to explore: 
 GitHub Copilot CLI for Beginners video series 
 GitHub Copilot CLI for Beginners: Getting started with GitHub Copilot CLI 
 GitHub Copilot CLI 101: how to use GitHub Copilot from the command line 
 Best practices for GitHub Copilot CLI 
 The post GitHub Copilot CLI for Beginners: Interactive v. non-interactive mode appeared first on The GitHub Blog .
```

---

## 9. GitHub for Beginners: Getting started with Markdown

- 日期: 2026-04-28 18:00
- 链接: https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-markdown/

```
Welcome back to GitHub for Beginners. We’ve covered a wide range of topics so far this season, including GitHub Issues and Projects , GitHub Actions , security, and GitHub Pages. Now we’re going to teach you everything you need to know to get started with Markdown, the markup language used across GitHub. 
 Once you learn the basics of how to use Markdown, you’ll develop an essential skill that will transform how you write READMEs as well as how to format issues, pull requests, and your agent instruction files. By the end of this post, you’ll have the knowledge you need to make your projects and contributions easier for others to explore. 
 As always, if you prefer to watch the video or want to reference it, we have all of our GitHub for Beginners episodes available on YouTube . 
 What is Markdown and why is it important? 
 Markdown is a lightweight language for formatting plain text. You can use Markdown syntax, along with some additional HTML tags, to format your writing on GitHub. You can do this in repository READMEs, issue and pull request descriptions, and comments on issues and pull requests. 
 Markdown gives you the ability to create clear, readable documentation. Having a clean README in your project or a well-formatted issue can make a huge difference when someone lands on your content for the first time. 
 And one of the best parts is that when you get the syntax down, you’ll find yourself using it in almost every project you work on! 
 Where can I use Markdown? 
 The most common place where you’ll encounter Markdown is in your repository’s README file. But you’ll also find yourself using it in issues, pull requests, discussions, and even wikis. Any time you write or communicate on GitHub, Markdown is behind the scenes, helping your text look clean and consistent. 
 Markdown extends beyond GitHub to modern note-taking apps, blog platforms, and documentation tools. It’s a widely adopted language used across the technical space, so learning how to use it can benefit you beyond just how you interact with GitHub. 
 Basic syntax 
 We’re going to start with the common features that you’ll use the most. While we’re going through these, you can try them out to see how they work. The easiest way to do this is by opening a markdown file on your repository. 
 Navigate to a repository you own on github.com . 
 Make sure you are on the Code tab of your repository. 
 Click Add file near the top of the window and select Create new file from the pull-down menu. 
 In the box at the top of the editor, name your file. Make sure the filename ends in .md (e.g., markdownTestFile.md ). 
 Select the Edit button. 
 Enter any Markdown syntax into the editor window. 
 You can see what the Markdown text you enter will look like by selecting the Preview button; there’s no need to make a commit unless you want to save your test file. Just select the Edit button to go back to editing so you can enter more Markdown text. 
 Now that you know how to try it out, let’s get started with the syntax. First up are headers. These are your title and section names. You create them by adding pound signs ( # ), also known as hashtags, in front of your text. One pound sign indicates a header, two will create a subheader, and so on. 
 # GitHub for Beginners 

 

## Basic Markdown syntax 

 

### Headers 
 If you want to emphasize your text, you can use bold and italic fonts. You create these by using either asterisks ( * ) or underscores ( _ ). Either of these symbols work in the same way, you just have to make sure to pair them up appropriately. A single character makes text italic, a double character makes text bold, and a triple character makes it both bold and italic. You can emphasize characters within a string or multiple strings within a line of text. 
 Here is some *italic text* 

Here is some **bold text** 

___Here is both bold and italic text 

Over multiple lines___ 
 Sometimes you may want to quote important text. To do this, add the greater than ( > ) symbol as the first character in a line of text. If you would like to quote something that spans multiple lines, you need to add the greater than symbol at the start of each individual line. 
 > No design skills required. 

> 

> No overthinking allowed. 
> 

> Just ship your work. 
 Lists 
 Now let’s get into something a little more involved: lists. 
 Lists are a common way to express your steps and procedures in an ordered and unordered manner. To create an ordered list, number each element in the list (i.e. 1. , 2. , 3. , etc.). 
 While this can be clear to read, what if you want to add an element between two consecutive numbers? The good news is that you don’t need to renumber the entire list. Markdown interpreters allow you to order your items with any number, and they automatically interpret it as an ordered list from first to last. 
 1. Click the "Use this template” button at the top of this repo. 

1. Name your new repository (e.g., my-portfolio). 

1. Clone your new repo and start customizing! 
 For an unordered list, start a line with either a hyphen ( - ), asterisk ( * ), or a plus sign ( + ). Markdown will render any of these characters as the start of an unordered list. 
 * Click the "Use this template” button at the top of this repo. 

* Name your new repository (e.g., my-portfolio). 

* Clone your new repo and start customizing! 
 If you would like to create nested lists, indent four spaces to start a new indented list. You can do this with both ordered and unordered list items. 
 1. Click the "Use this template” button. 

 - Located at the top of the repo. 

 - This will create a new repository using this template. 

1. Name your new repository. 

 - e.g., my-portfolio 

 - This can be created under your personal GitHub account. 

1. Clone your new repo and start customizing! 
 When you’re done with your list, hit Enter twice to go back to plain text. 
 Additional resources 
 Check out the GitHub docs for a cheat sheet on formatting Markdown . 
 You can also start practicing your Markdown skills today by visiting the communicate-using-markdown skills repository . You’ll learn how to use Markdown to add lists, images, and links in a GitHub comment or text file. 
 Code 
 Sometimes you may want to display a snippet of code in your Markdown as an example. This could be for steps in a procedure or as part of your project’s installation process. Many Markdown interpreters render code snippets with formatting and syntax highlighting. You can denote code in Markdown by surrounding it with a backtick ( ` ) character. 
 `git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git` 
 If you have code that spans multiple lines, you can use three backtick characters to create a code block. Any characters between these triple backticks, including spaces and new lines, will render as code. 
 ```bash 

# Clone the repository 

git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git 

cd YOUR_REPO_NAME 

 

# Install dependencies 

npm install 

 

# Start the development server 

npm run dev 

``` 
 Links and images 
 Now let’s learn how to spice up our Markdown files. We’ll start with links. Links allow you to point people to helpful resources, documentation, or other pages in your project. They’re written using brackets ( [] ) and parentheses ( () ). Place the text you want to display in the brackets, followed immediately by the URL in parentheses, with no space between the two. This keeps your writing clean and easy to follow. 
 Open [your local host](http://localhost:3000) to see your portfolio. 
 Images work in almost the same way, but with one small difference: you need to add an exclamation point ( ! ) at the beginning. This is perfect for adding screenshots, diagrams, or even a project logo to your README. 
 ![Mona](https://avatars.githubusercontent.com/u/92997159?v=4) 
 To make things even easier, on GitHub, you can just drag-and-drop an image into an issue or pull request, and it automatically generates the right Markdown for you. 
 Whether you’re linking out to a tutorial or showing off a screenshot, links and images help you add that extra bit of personality and clarity to your Markdown. 
 What’s next? 
 You now know the basics of Markdown, including what it is, why it matters, where you can use it, and how to start writing it with confidence. With just a few techniques, you can create clean, readable documentation that makes your GitHub projects stand out. 
 Whether you’re building a README, opening an issue, or writing project notes, Markdown is going to be one of the tools you use the most. 
 If you want to learn more about Markdown, here are some good places to get started: 
 Basic formatting syntax 
 Creating and highlighting code blocks 
 Quickstart for writing at GitHub 
 Happy coding! 
 The post GitHub for Beginners: Getting started with Markdown appeared first on The GitHub Blog .
```

---

## 10. Securing the git push pipeline: Responding to a critical remote code execution vulnerability

- 日期: 2026-04-28 15:30
- 链接: https://github.blog/security/securing-the-git-push-pipeline-responding-to-a-critical-remote-code-execution-vulnerability/

```
On March 4, 2026, we received a vulnerability report through our Bug Bounty program from researchers at Wiz describing a critical remote code execution vulnerability affecting github.com, GitHub Enterprise Cloud, GitHub Enterprise Cloud with Data Residency, GitHub Enterprise Cloud with Enterprise Managed Users, and GitHub Enterprise Server. 
 In less than two hours we had validated the finding, deployed a fix to github.com, and begun a forensic investigation that concluded there was no exploitation . 
 In this post, we want to share what happened, how we responded, and what we are doing to prevent similar issues in the future. 
 Receiving the bug bounty report 
 The bug bounty report described a way for any user with push access to a repository, including a repository they created themselves, to achieve arbitrary command execution on the GitHub server handling their git push operation. The attack required only a single command: git push with a crafted push option that leveraged an unsanitized character. 
 Our security team immediately began validating the bug bounty report. Within 40 minutes, we had reproduced the vulnerability internally and confirmed the severity. This was a critical issue that required immediate action. 
 Understanding the vulnerability 
 When a user pushes code to GitHub, the operation passes through multiple internal services. As part of this process, metadata about the push, such as the repository type and the environment it should be processed in, is passed between services using an internal protocol. 
 The vulnerability leveraged how user-supplied git push options were handled within this metadata. Push options are an intentional feature of git that allow clients to send key-value strings to the server during a push. However, the values provided by the user were incorporated into the internal metadata without sufficient sanitization. Because the internal metadata format used a delimiter character that could also appear in user input, an attacker could inject additional fields that the downstream service would interpret as trusted internal values. 
 By chaining several injected values together, the researchers demonstrated that an attacker could override the environment the push was processed in, bypass sandboxing protections that normally constrain hook execution, and ultimately execute arbitrary commands on the server. 
 Responding to the vulnerability 
 With the root cause identified on March, 4, 2026, at 5:45 p.m. UTC, our engineering team developed and deployed a fix to github.com at 7:00 p.m. UTC that same day. The fix ensures that user-supplied push option values are properly sanitized and can no longer influence internal metadata fields. 
 For GitHub Enterprise Server, we prepared patches across all supported releases (3.14.25, 3.15.20, 3.16.16, 3.17.13, 3.18.7, 3.19.4, 3.20.0, or later) and published CVE-2026-3854 . These are available today and we strongly recommend that all GHES customers upgrade immediately. 
 Investigating for exploitation 
 With the immediate fix in place on github.com, we moved to the pressing question of whether anyone else found and exploited this vulnerability before the researchers reported it. 
 A key property of this vulnerability gave us confidence in our ability to answer that question. The exploit forces the server to take a code path that is never used during normal operations on github.com. This is not something an attacker can avoid or suppress, as it is an inherent consequence of how the injection works. 
 We logged this path and queried our telemetry for any instance of this anomalous code path being executed. The results were clear: 
 Every occurrence mapped to the Wiz researchers’ own testing activity. 
 No other users or accounts triggered this code path. 
 No customer data was accessed, modified, or exfiltrated as a result of this vulnerability. 
 For GHES customers, exploitation would require an authenticated user with push access on your instance. We recommend reviewing your access logs out of an abundance of caution. 
 Defense in depth 
 Beyond fixing the immediate input sanitization issue, our investigation surfaced an additional finding worth sharing. 
 The exploit worked in part because the server had access to a code path that was not intended for the environment it was running in. This code path existed on disk as part of the server’s container image, even though it was only meant to be used in a different product configuration. An older deployment method had correctly excluded this code, but when the deployment model changed, the exclusion was not carried forward. 
 This is a useful reminder that defense in depth matters. The input sanitization fix is the primary remediation, but we have also removed the unnecessary code path from environments where it should not exist. Even if a similar injection vulnerability were discovered in the future, this additional hardening would limit what an attacker could do with it. 
 What you should do 
 GitHub Enterprise Cloud , GitHub Enterprise Cloud with Enterprise Managed Users , GitHub Enterprise Cloud with Data Residency , and github.com were patched on March 4, 2026. No action is required from users of any of these. 
 As mentioned previously, exploitation on GitHub Enterprise Server requires an authenticated user with push access on your instance. We recommend that you review /var/log/github-audit.log for push operations containing ; in push options. Updates are available in the following releases: 
 GitHub Enterprise Server 3.14.25 or later 
 GitHub Enterprise Server 3.15.20 or later 
 GitHub Enterprise Server 3.16.16 or later 
 GitHub Enterprise Server 3.17.13 or later 
 GitHub Enterprise Server 3.18.7 or later 
 GitHub Enterprise Server 3.19.4 or later 
 GitHub Enterprise Server 3.20.0 or later 
 We strongly recommend upgrading to the latest patch release as soon as possible. See the GHES release notes for details. 
 This vulnerability has been assigned CVE-2026-3854 . 
 Acknowledgments 
 This vulnerability was discovered and responsibly disclosed by researchers at Wiz . Their report was thorough, clearly demonstrated the impact, and enabled us to move quickly from validation to remediation. This finding will receive one of the highest rewards in the history of our Bug Bounty program , which has been a cornerstone of our security program for over a decade. 
 The post Securing the git push pipeline: Responding to a critical remote code execution vulnerability appeared first on The GitHub Blog .
```

---
