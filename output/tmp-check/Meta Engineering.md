# Meta Engineering

> 分类: 其他
> URL: https://engineering.fb.com/feed/
> 抓取: 9 篇

---

## 1. How Meta Is Strengthening End-to-End Encrypted Backups

- 日期: 2026-05-01 16:00
- 链接: https://engineering.fb.com/2026/05/01/security/meta-strengthening-end-to-end-encrypted-backups/

```
The HSM-based Backup Key Vault 
 Meta’s HSM-based Backup Key Vault provides the foundation for end-to-end encrypted backups for WhatsApp and Messenger. The system allows people to protect their backed-up message history with a recovery code, ensuring that the recovery code is stored in tamper-resistant hardware security modules (HSMs) and is inaccessible to Meta, cloud storage providers, or any third party. The vault is deployed as a geographically distributed fleet across multiple datacenters, providing resilience through majority-consensus replication. 
 Late last year, we made it easier to end-to-end encrypt your backups using passkeys , and now we continue to strengthen the underlying infrastructure that protects password-based end-to-end encrypted backups with two updates: over-the-air fleet key distribution for Messenger and a commitment to publishing evidence of secure fleet deployments. 
 Over-the-Air Fleet Key Distribution 
 To verify the authenticity of the HSM fleet, clients validate the fleet’s public keys before establishing a session. In WhatsApp, these keys are hardcoded into the application. To support Messenger — where new HSM fleets need to be deployed without requiring an app update — we built a mechanism to distribute fleet public keys over the air as part of the HSM response. Fleet keys are delivered in a validation bundle that is signed by Cloudflare and counter-signed by Meta, providing independent cryptographic proof of their authenticity. Cloudflare also maintains an audit log of every validation bundle. The full validation protocol is described in our whitepaper, “ Security of End-To-End Encrypted Backups .” 
 More Transparent Fleet Deployment 
 Transparency in the deployment of our HSM fleet is essential to demonstrating that the system operates as designed and that Meta cannot access users’ encrypted backups.  We will now publish evidence of the secure deployment of each new HSM fleet on this blog page, further cementing our leadership in the space of secure encrypted backups . New fleet deployments are infrequent — typically no more than every few years — and we are committed to demonstrating to our users that each new fleet is deployed securely, which any user can verify by following the steps in the Audit section of our whitepaper. 
 Read the Whitepaper 
 For the complete technical specification of the HSM-based Backup Key Vault, read the full whitepaper, “ Security of End-To-End Encrypted Backups .” 
 The post How Meta Is Strengthening End-to-End Encrypted Backups appeared first on Engineering at Meta .
```

---

## 2. Modernizing the Facebook Groups Search to Unlock the Power of Community Knowledge

- 日期: 2026-04-21 16:00
- 链接: https://engineering.fb.com/2026/04/21/ml-applications/modernizing-the-facebook-groups-search-to-unlock-the-power-of-community-knowledge/

```
We’ve fundamentally transformed Facebook Groups Search to help people more reliably discover, sort through, and validate community content that’s most relevant to them. 
 We’ve adopted a new hybrid retrieval architecture and implemented automated model-based evaluation to address the major friction points people experience when searching community content. 
 Under this new framework, we’ve made tangible improvements in search engagement and relevance, with no increase in error rates. 
 People around the world rely on Facebook Groups every day to discover valuable information. The user journey is not always easy due to the amount of information available. As we help connect people across shared interests, it’s also important to engineer a path through the vast array of conversations to surface as precisely as possible the content a person is looking for. We published a paper that discusses how we address this by re-architecting Facebook Group Scoped Search . By moving beyond traditional keyword matching to a hybrid retrieval architecture and implementing automated model-based evaluation , we are fundamentally innovating how people discover, consume, and validate community content. 
 Addressing the Friction Points in Community Knowledge 
 People struggle with three friction points when searching for answers in community content – discovery, consumption, and validation. 
 Discovery: Lost in Translation 
 Historically, discovery has relied on keyword-based (lexical) systems. These systems look for exact words, creating a gap between a person’s natural language intent and the available content. For example, consider a person searching for “small individual cakes with frosting.” A traditional keyword system might return zero results if the community uses the word “cupcakes” instead. As the specific phrasing doesn’t match, that person misses out on highly relevant advice. 
 We needed a system where searching for an “Italian coffee drink” effectively matches a post about “cappuccino,” even if the word “coffee” is never explicitly stated. 
 Consumption: The Effort Tax 
 Even when people find the right content, they face an “effort tax.” They often have to scroll and sort through many comments before finding consensus. Imagine someone searching for “tips for taking care of snake plants.” To get a clear answer, they have to read dozens of comments to piece together a watering schedule. 
 Validation: Decision Making with Community Knowledge 
 People often need to verify a decision or validate a potential purchase using trusted community expertise. For instance, consider a shopper on Facebook Marketplace viewing a listing for a high-value item, such as a vintage Corvette. They want authentic opinions and advice about the product before purchasing, but that wisdom is typically trapped in scattered group discussions. The person needs to unlock the collective wisdom of specialized groups to evaluate the product effectively, but digging for these validation signals manually is not easy. 
 A person searches for “tips for taking care of snake plants,” needing trusted instructional advice. A discussion in the Groups module powered by the modernized hybrid retrieval architecture highlights key tips and community favorites. The Solution: A Modernized Hybrid Retrieval Architecture 
 We engineered a hybrid retrieval architecture that powers a discussions module on Facebook Search. This system runs parallel pipelines to blend the precision of inverted indices with the conceptual understanding of dense vector representations. We addressed the limitations of legacy search by restructuring three important components of our infrastructure. 
 The following workflow illustrates how we modernize the stack to process natural language intent: 
 Parallel Retrieval Strategy 
 We modernized the retrieval stage by decoupling the query processing into two parallel pathways, ensuring we capture both exact terms and broad concepts: 
 Query Preprocessing: Before retrieval, user queries undergo tokenization, normalization, and rewriting. This is important for ensuring clean inputs for both the inverted index and the embedding model. 
 The Lexical Path (Unicorn): We utilize Facebook’s Unicorn inverted index to fetch posts containing exact or closely matched terms. This ensures high precision for queries involving proper nouns or specific quotes. 
 Simultaneously, the query is passed to our search semantic retriever (SSR). This is a 12-layer, 200-million-parameter model that encodes the user’s natural language input into a dense vector representation. We then perform an approximate nearest neighbor (ANN) search over a precomputed Faiss vector index of group posts. This enables the retrieval of content based on high-dimensional conceptual similarity, regardless of keyword overlap. 
 L2 Ranking With Multi-Task Multi-Label (MTML) Architecture 
 Merging results from two fundamentally different paradigms — sparse lexical features and dense semantic features — required a sophisticated ranking strategy. The candidates retrieved from both the keyword and embedding systems are merged in the ranking stage. Here, the model ingests lexical features (like TF-IDF and BM25 scores) alongside semantic features (cosine similarity scores). 
 Next, we moved away from single-objective models to a MTML supermodel architecture. This allows the system to jointly optimize for multiple engagement objectives — specifically clicks, shares, and comments — while maintaining plug-and-play modularity. By weighting these signals, the model ensures that the results we surface are not just theoretically relevant, but also likely to generate meaningful community interaction. 
 Automated Offline Evaluation 
 Deploying semantic search introduces a validation challenge: Similarity scores are not always intuitive in high-dimensional vector space. To validate quality at scale without the bottleneck of human labeling, we integrated an automated evaluation framework into our build verification test (BVT) process. 
 We utilize Llama 3 with multimodal capabilities as an automated judge to grade search results against queries. Unlike binary “good/bad” labels, our evaluation prompts are designed to detect nuance. We explicitly programmed the system to recognize a “somewhat relevant” category, defined as cases where the query and result share a common domain or theme (e.g., different sports are still relevant in a general sports context). This allows us to measure improvements in result diversity and conceptual matching. 
 The modernized hybrid retrieval architecture. Impact and Future Work 
 The deployment of this hybrid architecture has yielded measurable improvements in our quality metrics, validating that blending lexical precision with neural understanding is superior to keyword-only methods. According to our offline evaluation results, the new L2 Model + EBR (Hybrid) system outperformed the baseline across search engagement with the daily number of users performing search on Facebook compared to baseline. 
 These numbers confirm that by integrating semantic retrieval, we are successfully surfacing more relevant content without sacrificing the precision users expect. While modernizing the retrieval stack is a major milestone, it is only the beginning of unlocking community knowledge. Our roadmap focuses on deepening the integration of advanced models into the search experience: 
 LLMs in Ranking: We plan to apply LLMs directly within the ranking stage. By processing the content of posts during ranking, we aim to further refine relevance scoring beyond vector similarity. 
 Adaptive Retrieval: We are exploring LLM-driven adaptive retrieval strategies that can dynamically adjust retrieval parameters based on the complexity of the user’s query. 
 Read the Paper 
 Modernizing Facebook Scoped Search: Keyword and Embedding Hybrid Retrieval with LLM Evaluation 
 The post Modernizing the Facebook Groups Search to Unlock the Power of Community Knowledge appeared first on Engineering at Meta .
```

---

## 3. Capacity Efficiency at Meta: How Unified AI Agents Optimize Performance at Hyperscale

- 日期: 2026-04-16 16:00
- 链接: https://engineering.fb.com/2026/04/16/developer-tools/capacity-efficiency-at-meta-how-unified-ai-agents-optimize-performance-at-hyperscale/

```
We’re sharing insights into Meta’s Capacity Efficiency Program, where we’ve built an AI agent platform that helps automate finding and fixing performance issues throughout our infrastructure. 
 By leveraging encoded domain expertise across a unified, standardized tool interface these agents help save power and free up engineers’ time away from addressing performance issues to innovating on new products. 
 We’ve built a unified AI agent platform that encodes the domain expertise of senior efficiency engineers into reusable, composable skills. These agents now automate both finding and fixing performance issues, recovering hundreds of megawatts (MW) of power and compressing hours of manual regression investigation into minutes, enabling the program to scale MW delivery across a growing number of product areas without proportionally scaling headcount. 
 On defense, FBDetect , Meta’s in-house regression detection tool, catches thousands of regressions weekly; faster automated resolution means fewer megawatts wasted compounding across the fleet. On offense, AI-assisted opportunity resolution is expanding to more product areas every half, handling a growing volume of wins that engineers would never get to manually. Together, this is how Meta’s Capacity Efficiency Program keeps growing MW delivery without proportionally growing the team. The end goal is a self-sustaining efficiency engine where AI handles the long tail. 
 Here’s how it works and where we’re headed: 
 Efficiency at hyperscale requires both offense (proactively finding optimizations) and defense (catching and mitigating regressions that make it to production); AI can accelerate both. 
 We’ve built a unified platform where standardized tool interfaces combine with encoded domain expertise to automate investigation on both sides. 
 These AI systems are now the infrastructure for the Capacity Efficiency program, which has recovered hundreds of megawatts of power, enough to power hundreds of thousands of American homes for a year. 
 Automating diagnoses can compress ~10 hours of manual investigation into ~30 minutes, while AI agents fully automate the path from efficiency opportunity to ready-to-review pull request. 
 Introducing the Capacity Efficiency Program 
 When the code you ship serves more than 3 billion people, even a 0.1% performance regression can translate to significant additional power consumption. 
 In Meta’s Capacity Efficiency organization, we see efficiency as a two-sided effort: 
 Offense: searching for opportunities (proactive code changes) to make our existing systems more efficient, and deploying them. 
 Defense: monitoring resource usage in production to detect regressions, root-cause them to a pull request, and deploy mitigations. 
 These systems worked well and have played an important role in Meta’s efficiency efforts for years. However, actually resolving the issues they surface introduces a new bottleneck: human engineering time. 
 This human engineering time can be spent on any of the following activities: 
 Querying profiling data to find opportunities to optimize hot functions. 
 Reviewing an efficiency opportunity’s description, documentation, and past examples to understand the best approach for implementing an optimization. 
 Checking recent code and configuration deployments that could have caused a step change in resource usage. 
 Looking through recent internal discussions about launches that might have been related to a regression. 
 Many engineers at Meta use our efficiency tools to work on these problems every day. But no matter how high-quality the tooling is, engineers have limited time to address performance issues when innovating on new products is our top priority. 
 We started asking: What if AI could handle investigation and resolution? 
 Offense and Defense Share the Same Structure 
 The breakthrough was realizing that both problems share the same structure: 
 This meant we didn’t need two separate AI systems. We needed one platform that could serve both. 
 We built it on two layers: 
 MCP Tools : These are standardized interfaces for LLMs to invoke code. Each tool does one thing: query profiling data, fetch experiment results, retrieve configuration history, search code, or extract documentation. 
 Skills : These encode domain expertise about performance efficiency. A skill can tell an LLM which tools to use and how to interpret results. It captures reasoning patterns that experienced engineers developed over years, such as “consult the top GraphQL endpoints for endpoint latency regressions” or “look for recent schema changes if the affected function handles serialization” 
 Together, tools and skills promote a generalized language model into something that can apply the domain expertise typically held by senior engineers. The same tools can power both offense and defense. Only the skills differ. 
 Defense: Catching Regressions Before They Compound 
 FBDetect is Meta’s in-house regression detection tool that can catch performance regressions as small as 0.005% in noisy production environments. It analyzes time series data like this: 
 When FBDetect finds a regression, we immediately attempt to root-cause it to a code or configuration change; this is a vital first step to understand what happened. It’s done primarily with traditional techniques such as correlating regression functions with recent pull requests. After a root cause is determined, engineers are typically notified and expected to take action, such as optimizing the recent code change. We’ve added an additional feature to make this faster: 
 AI Regression Solver 
 Our AI Regression Solver is the newest and most promising component of FBDetect, which produces a pull request to fix forward the regression automatically. Traditionally, root-causes (pull requests) that created performance regressions were either rolled back (slowing engineering velocity) or ignored (increasing infrastructure resource use unnecessarily). 
 Now, our in-house coding agent is activated to do the following: 
 Gather context with tools: find the symptoms of the regression, such as the functions that regressed; look up the root cause (a pull request) of the regression, including the exact files and lines changed. 
 Apply domain expertise with skills: use regression mitigation knowledge for the particular codebase, language, or regression type. For example, regressions from logging can be mitigated by increasing sampling. 
 Create a resolution: produce a new pull request and send it to the original root cause author for review. 
 Offense: Turning Opportunities Into Shipped Code 
 On the offensive side, “efficiency opportunities” are proposed conceptual code changes that are believed to improve performance of existing code. We built a system where engineers can view an opportunity and request an AI-generated pull request that implements it. What used to require hours of investigation now takes minutes to review and deploy. 
 The pipeline mirrors the defensive AI Regression Solver: 
 Gather context with tools: The AI agent looks up: Opportunity metadata. 
 Documentation explaining the optimization pattern. 
 Examples showing how similar opportunities were resolved. 
 The specific files and functions involved. 
 Validation criteria for confirming the fix works. 
 Apply domain expertise with skills: use expert engineers’ knowledge on a specific type of efficiency opportunity, encoded into a skill. For example, memoizing a given function to reduce CPU usage. 
 Create resolution: produce a candidate fix with guardrails, verify syntax and style, confirm it addresses the right issue. Surface the generated code in the engineer’s editor, ready to apply with one click. 
 Importantly, we use the same tools as defense: profiling data, documentation, code search. What differs is the skills . 
 One Platform, Compounding Returns 
 Our unified architecture with shared tools and data sources has been a clean abstraction. Each existing and new agent has an easy way to gather context about performance with the interfaces we’ve made, without the need to reinvent the wheel. 
 This post focused on our first use cases: performance regressions and opportunities. Within a year, the same foundation powered additional applications: conversational assistants for efficiency questions, capacity planning agents, personalized opportunity recommendations, guided investigation workflows, and AI-assisted validation. Each new capability requires few to no new data integrations since they can just compose existing tools with new skills. 
 Impact 
 The results of the Capacity Efficiency program are significant: We’ve recovered hundreds of megawatts of power. The AI systems for both offense and defense contribute to supporting this effort. 
 But the deeper change is in how offense and defense reinforce each other: Engineers who spent mornings on defensive triage now review AI-generated analyses in minutes. Engineers using our efficiency tools can now get AI-assisted code instead of starting from scratch. The daunting question of “where do I even start?” has been replaced by reviewing and deploying high-impact fixes. 
 The post Capacity Efficiency at Meta: How Unified AI Agents Optimize Performance at Hyperscale appeared first on Engineering at Meta .
```

---

## 4. Post-Quantum Cryptography Migration at Meta: Framework, Lessons, and Takeaways

- 日期: 2026-04-16 14:59
- 链接: https://engineering.fb.com/2026/04/16/security/post-quantum-cryptography-migration-at-meta-framework-lessons-and-takeaways/

```
We’re sharing lessons learned from Meta’s post-quantum cryptography (PQC) migration to help other organizations strengthen their resilience as industry transitions to post-quantum cryptography standards. 
 We’re proposing the idea of PQC Migration Levels to help teams within organizations manage the complexity of PQC migration for their various use cases. 
 By outlining Meta’s approach to this work — from risk assessment and inventory through deployment and guardrails — we hope to contribute practical guidance that helps accelerate the broader community’s efforts to move toward a post-quantum future. 
 Our goal is to help others navigate this transition effectively, efficiently, and economically so they can prepare for a future where today’s public‑key encryption methods may no longer be sufficient. 
 Research indicates that quantum computers will eventually break conventional public-key cryptography, creating security risk for many digital systems across industry. Although experts estimate this could happen within 10–15 years, sophisticated adversaries could collect encrypted data today , anticipating a future where quantum computers can decrypt it — a strategy known as “store now, decrypt later” (SNDL). This means sensitive information could be eventually at risk even if quantum computers are still years away. 
 Recognizing this threat, organizations like the US National Institute of Standards and Technology (NIST) and the UK’s National Cyber Security Centre (NCSC) have published migration guidance that discusses target timeframes (including 2030) for prioritizing post-quantum protections in critical systems. This guidance recognizes that complexity and missing or incomplete technical capabilities are important factors impacting PQC migration plans. 
 For example, the first industry-wide PQC standards, such as ML-KEM (Kyber) and ML-DSA (Dilithium), have now been published by NIST, with additional algorithms like HQC on the way. Notably, Meta cryptographers are co-authors of HQC , one of the newly selected PQC algorithms, reflecting our commitment to advancing global cryptographic security. These standards provide organizations with robust options for defending against SNDL attacks, and Meta seeks to share relevant progress and insights to help the broader community navigate the transition to a PQC-secure future. 
 At Meta we have taken a proactive approach to ensure that we are prepared to meet the threat challenges posed by quantum computers and SNDL. With billions of people around the globe relying on our platforms and applications every day, we continue to maintain strong security and data protection standards. As part of this, we have already begun deploying and rolling out post-quantum encryption across our internal infrastructure over a multi-year process to ensure that we uphold our security and privacy commitments now and into the future. 
 Meta’s PQC Migration Goals 
 We’ve adopted a robust and comprehensive PQC migration strategy that aspires to the following principles to ensure a seamless transition: 
 Effectiveness : Withstanding quantum adversaries and protecting against potential threats. 
 Timeliness : Timely deploying of protection mechanisms aligned with evolving standards. 
 Performance : Minimizing overhead and ensuring that the new cryptographic solutions do not compromise system performance or user experience. 
 Cost Efficiency : Avoiding unnecessary expenditure by adopting a strategic approach that balances investment with risk mitigation. 
 PQC Maturity Levels – How Every Organization Can Assess Post-Quantum Readiness 
 PQC migration is a gradual, complex, multi-year process. It can be helpful to think about PQC migration in terms of what we call PQC Migration Levels. The levels are laddered in terms of how rapidly they allow an organization to respond to a quantum threat. The shorter the time to react to a relevant quantum event the better. A relevant quantum event can be related to advancements in quantum computing development, standards publications, or the establishment of new industry practices. 
 PQ-Enabled , the level at which full quantum protection is effectively achieved, is the platinum standard that organizations should aim for each one of its applications and use cases. However, any organization looking to increase its resilience to quantum threats can take steps on its way to PQ-Enabled. Even starting the migration process by setting the level of minimally acceptable success at PQ-Ready may have benefits. At this level companies that may not have budgeted for near-term enablement can feel motivated (and rewarded) for building the necessary building blocks to complete risk mitigation in the future. 
 PQ-Enabled : The ultimate goal for every use case. Organizations succeed by implementing and deploying a post-quantum secure solution. At Meta, for example, we have begun deploying PQ protections across significant portions of our internal traffic . 
 PQ-Hardened : Organizations succeed by implementing all post-quantum protections currently available in the literature, but due to the absence of PQ primitives in the literature, the team (and the industry in general) is not capable of fully mitigating the quantum threat. For instance, efficient post-quantum Oblivious Pseudorandom Functions (OPRFs) are not yet available and therefore use cases relying on this type of primitive could only achieve PQ Hardened level. 
 PQ-Ready : Organizations start to succeed by implementing a post-quantum secure solution suitable to the use case. However, due to costs, prioritization, or other factors, its enablement is not currently feasible. This is not an desirable end goal given the fact it is not yet protecting the use case against quantum attacks, but it does reduce the time to react when compared to lower levels. 
 PQ-Aware : The organization has been made aware that quantum computers threaten their use case and have already completed an initial assessment of what it takes to eventually reach PQ readiness. However, the team has not started to design the PQ protections yet. 
 PQ-Unaware : The organization is not aware of the upcoming quantum threat, placing them at the most undesirable position in the PQC Maturity Level ladder. 
 An Overview of Meta’s PQC Strategy 
 The proposed strategy is defined as a sequence of steps. Some of them may overlap in time with others but the goal here is to give an indication about the different workstreams organizations may have to embark on as part of their PQC readiness. 
 Prioritization Definition to establish a qualitative criteria to differentiate types of applications at high, moderate, and low priority among the types of use case impacted by possible quantum attacks. This approach helps prioritize which use cases should be migrated first. 
 Build a Cryptographic Inventory to have a full picture on the cryptography usage across the organization and identify applications at risk. 
 Address External Dependencies for the migration of the selected applications to PQC (e.g., publication of PQC standards, PQC-HSMs, PQC mature implementations). 
 Implement PQC Components to be eventually integrated into use cases. 
 Implement PQC Guardrails by changing crypto standards, disallowing the creation of new keys and usage of affected APIs. 
 Integrate PQC Components to protect the use cases against the quantum threat. 
 A. Prioritization 
 We have created a criteria that allows us to classify any application into different prioritization levels. To this end, we analyze various aspects that influence such a prioritization. 
 High-Priority Applications 
 Susceptible to attacks that can be initiated now without the existence of a quantum computer (offline attacks) and efficiently completed later (SNDL attack by means of Shor’s algorithm). Any application using quantum vulnerable public-key encryption and key exchange primitives falls into this category. Among high-risk applications, we differentiate the ones that have no external dependencies (can be migrated right away), from the ones that have external dependencies and thus may need to wait until these dependencies are resolved. 
 Medium-Priority Applications 
 Susceptible to attacks that can only be initiated with a quantum computer in the future when a sufficiently powerful quantum computer is available (online attacks) and which will be efficiently performed (Shor’s algorithm). 
 We differentiate these two categories based on their capability of upgrading their security mechanism: Medium-high risks are hard to patch (e.g., applications that have public keys baked into hardware) and medium-low risks are those that are possible to patch (e.g., software upgrades). The patching capability is particularly relevant for applications with long lifespans (i.e., time for development + time deployed in the field). Any application using quantum vulnerable digital signatures falls into this category. 
 Low-Priority Applications 
 Susceptible to inefficient quantum attacks only (Grover’s attack). As presented in many academic publications (e.g., Gheorghiu and Mosca, 2025 ), the enormous resource requirements to run such an attack (which even raises doubts about whether such an attack will ever be feasible) make them the lowest risk. Any application using symmetric cryptography with inadequate parameters falls into this category. 
 The table below summarizes the proposed criteria. 
 Proposed post-quantum prioritization. B. Build a Cryptographic Inventory 
 Cryptography algorithms’ strength decays with time, as depicted in the chart below. Since the inception of cryptography, we have seen multiple ciphers and algorithms rise and fall with regards to security and adoption rate. The continuous need to replace cryptographic algorithms requires at the very minimum an understanding of where cryptography is being used. The problem is cryptography is ubiquitous, and finding all instances of a cryptographic primitive in a large infrastructure and codebase is inherently challenging. 
 Adapted from “ Getting Ready for the Post-Quantum Transition .” Brian LaMacchia. Microsoft Research. December 9, 2020. The process of mapping all the usages of cryptography within an organization is called Crypto Inventorying. For a company-wide PQC migration strategy, it represents a critical prerequisite for the completion of the work. This can be built applying two complementary strategies. 
 Automated Discovery : We leverage monitoring tools, such as our Crypto Visibility service, to autonomously map cryptographic primitives used in production. This provides high-fidelity data on active usage within our primary libraries. 
 Reporting : Because monitoring cannot capture every edge case or shadow dependency, we supplement automation with developer reporting. This process captures cryptographic intent for new architectures and uncovers legacy usage in systems outside standard monitoring paths. 
 C. Address External Dependencies 
 Besides the organization’s commitment, the PQC migration is a process that requires certain external prerequisites to be met. Next, we describe what needs to be unblocked so that a company-wide PQC migration is feasible. We also identify the main unblocking actors – the organization itself is always highly encouraged to engage in these processes. 
 Dependency Main Unblocking Actor 
 Community-vetted PQC standards Standardization Bodies (NIST, IETF, ISO, etc) 
 PQC Support in Hardware HSM, CPU, and other Hardware Vendors 
 Production-level PQC implementations Crypto Engineering Community 
 External Dependencies for PQC Migration. Community-Vetted PQC Standards 
 The cryptography community has been actively participating in the PQC standardization processes. As a result, NIST has recently published the first PQC standards: FIPS 203 , FIPS 204 , and FIPS 205 , and announced a second list of algorithms to be standardized. Meta has been actively contributing, co-authoring some of the standardized algorithms (e.g., HQC ), and a few other candidates (e.g., BIKE and Classical McEliece ). 
 In addition, IETF has also published two RFCs specifying PQC schemes, and ISO another PQC standard . Many other standards are still needed, in particular those targeting higher-layer protocols. There are some preliminary drafts being written such as IETF Draft #1 and IETF Draft #2 . They address specific components of the TLS mechanism (e.g., the key encapsulation step). A considerable amount of work is still needed to finalize the drafts and cover other portions of the TLS stack, such as PQC X.509 certificates and PQC PKI in general. Most Meta products rely on TLS so lifting this roadblock is of utmost importance to effectively protect our systems. 
 PQC Support in Hardware 
 In some instances, organizations may have dependencies on external hardware vendors because some applications rely on hardware support (e.g. HSM and CPU). In cases like this it’s important that organizations align with their vendors as they plan for PQC migration. Meta, for example, is working closely with its hardware vendors on community-vetted, standardized PQC strategies. 
 Production-Level PQC Implementations 
 Most cryptography-related vulnerabilities are not due to any flaws in the algorithms, but instead in their implementations, which may contain bugs or subtle side-channel vulnerabilities. Getting all these things right isn’t trivial. The good news is that the cryptography community has already been working on this front for quite some time. 
 Since 2019, the Open Quantum Safe consortium, part of the Linux Foundation Post-Quantum Cryptography Alliance , has been developing LibOQS , a PQC cryptography library. LibOQS is starting to be integrated by industry organizations. Meta supports and is actively working with LibOQS leads, including fixing bugs in the library and continuously providing feedback. We’re committed to continuing fostering these strategic collaborations. 
 D- Design PQC-Secure Components 
 Algorithms Selection 
 Post-quantum cryptography is a comparatively new field, and therefore organizations should not deviate from what reputable public standardization bodies are recommending. As mentioned above, the NIST PQC Standardization competition has recently published the first PQC standards. For building the underlying PQC secure building blocks, we encourage organizations to consider adopting the NIST PQC selected algorithms, namely: 
 Key exchange / Key encapsulation: ML-KEM ( NIST FIPS 203 ) 
 Digital Signatures: ML-DSA ( NIST FIPS 204 ) 
 In addition to the algorithms listed above, NIST also selected two additional signature algorithms: SPHINCS+ and Falcon. Compared to Dilithium, the former has considerably larger signature sizes while the latter requires float pointing arithmetic. These drawbacks make their adoption considerably harder than the (already somewhat challenging) deployment of ML-DSA. 
 In terms of security strength, both ML-KEM and ML-DSA are defined with different parameter sets, each parameterization offering a different performance x security profile. For ML-KEM, in general we suggest teams to consider adopting ML-KEM768 achieving NIST Security Level 3, although exceptions can be granted for ML-KEM512 achieving NIST Security Level 1 (as endorsed by NIST PQC FAQ ) in case ML-KEM768 performance is prohibitive for a particular use case. The same applies for ML-DSA, preference for ML-DSA65 but exceptions could be allowed for ML-DSA44 considering performance constraints. 
 HQC has been recently selected by NIST for standardization. It is developed based on different math than ML-KEM, which is important if weaknesses are discovered in ML-KEM or its modular lattices approach, ensuring that an alternative method for PQC protection can still be deployed to protect organizations from SNDL attacks. NIST is currently drafting the HQC standard. 
 E – Implement PQC Guardrails 
 Besides migrating existing applications, we should also prevent applications from being designed with quantum vulnerable cryptographic algorithms in mind. This can be done by adding friction to any new use case trying to use quantum vulnerable algorithms. 
 Update internal cryptography guidelines documents to warn teams about the risks of adopting quantum vulnerable public-key cryptography, and the need to eventually migrate to PQC. 
 Discourage the creation of new quantum vulnerable keys . If the organization controls the tools to generate keys, those tools should warn teams when they request the creation of new quantum vulnerable keys. This wouldn’t fully prevent teams from generating such keys using other interfaces but would likely require them to engage with the internal crypto team. 
 Discourage the usage of affected APIs . If the organization benefits from a centrally managed source code repository with tightly controlled building system (e.g., Buck system ), it can create rules that prevent the usage of potentially affected APIs (e.g., RSA or ECDH APIs), and thus warn teams during code review if they try to use them. 
 F- Integrate PQC Components 
 The deployment of PQC-based solutions generally follows one of two paths: replacement (swapping classical for PQC) or hybrid (combining both). 
 While replacement reduces bandwidth and complexity, it relies entirely on newer PQC standards that are still maturing. The recent cryptanalysis (and invalidation) of algorithms like SIKE (final-round candidate running in the NIST PQC standardization process) underscores the importance of relying on thoroughly time-vetted, standardized algorithms during this period of transition to maintain robust security. 
 To mitigate this, we prioritize the hybrid approach by layering a PQC primitive on top of an established classical one, designed so that the combined system should remain at least as secure as the current standard. An adversary would need to break both layers to compromise the system, providing a critical safety net. 
 Final Remarks 
 Sharing our strategy and learnings doesn’t mean the process is complete. Hardening Meta’s systems — and any other organization’s systems — to post‑quantum cryptography takes years of phased work across protocols, products, and infrastructure as standards and implementations and threats mature. We’ll continue to expand coverage, extend protections, and share progress, and we’ll keep raising the bar to ensure we’re following the rigorous security practices consistent with evolving industry standards. 
 The information in this article is shared for informational purposes only and does not constitute professional, technical, or legal advice, nor does it constitute a guarantee of any particular security outcome. Organizations should conduct their own assessments and consult qualified professionals before making cryptographic implementation decisions. 
 Acknowledgements 
 This work reflects a broad, cross-company effort. We’re grateful to colleagues across Meta who are helping shape our post-quantum cryptography migration strategy and turn it into practice—through system design, implementation, deployment planning, measurement, and ongoing operations. In particular, we’d like to acknowledge the invaluable contributions and collaboration from teams across: Transport Security ( Sheran Lin , Jolene Tan , Kyle Nekritz , Ameya Shendarkar ) , WhatsApp ( Sebastian Messmer, Maayan Sagir Hever, Julian Maingot, Alex Kube, Ronak Patel ), Facebook/Messenger ( Emma Connor, Jasmine Henry ), Infrastructure ( Dong Wu, Grace Wu, (Seattle) Weiyuan Li, Yue Li , Shay Gueron Grunbaum , Xiaoyi Fei ) , Reality Labs ( Marcus Hodges ) , Hardware ( Hendrik Volkmer, Vijay Sai Krishnamoorthy ) and the Payments team ( Hootan Shadmehr , Hema Pamarty, Ryan DeSouza ) . We also thank Chris Wiltz and the many additional engineers, researchers, program managers, and reviewers — across Security, Product, and Policy — whose feedback improved both the technical clarity and the practical guidance in this post. 
 The post Post-Quantum Cryptography Migration at Meta: Framework, Lessons, and Takeaways appeared first on Engineering at Meta .
```

---

## 5. Escaping the Fork: How Meta Modernized WebRTC Across 50+ Use Cases

- 日期: 2026-04-09 16:00
- 链接: https://engineering.fb.com/2026/04/09/developer-tools/escaping-the-fork-how-meta-modernized-webrtc-across-50-use-cases/

```
At Meta, WebRTC powers real-time audio and video across various platforms. But forking a large open-source project like WebRTC within our monorepo presents unique challenges – over time, an internal fork can drift behind upstream, cutting itself off from community upgrades. 
 We’re sharing how we escaped this “forking trap” – from building a dual-stack architecture that enabled safe A/B testing across 50+ use cases, to the workflows that now keep us continuously upgraded with upstream. 
 This approach improved performance, binary size, and security – and we continue to use it today to A/B test each new upstream release before rolling it out. 
 At Meta, real-time communication (RTC) powers various services, from global Messenger and Instagram video chats to low-latency Cloud Gaming and immersive VR casting on Meta Quest. To meet the performance demands of billions of users, we spent years developing a specialized, high-performance variant of the open-source WebRTC library. 
 Permanently forking a big open-source project can result in a common industry trap. It starts with good intentions: You need a specific internal optimization or a quick bug fix. But over time, as the upstream project evolves and your internal features accumulate, the resources needed to merge in external commits can become prohibitive. 
 Recently, we officially concluded a massive multiyear migration to break this cycle. We successfully moved over 50 use cases from a divergent WebRTC fork to a modular architecture built on top of the latest upstream version – using it as a skeleton while injecting our own proprietary implementations of key components. 
 This article details how we engineered a solution to solve the “forking trap,” allowing us to build two versions of WebRTC simultaneously within a single library for the sake of A/B testing, while living in a monorepo environment, with continuous upgrade cycles of the library that’s being tested. 
 The Challenge: The Monorepo and the Static Linker 
 Upgrading a library like WebRTC can be risky, especially when upgrading while serving billions of users and introducing regressions that are hard to rollback. This also eliminates the possibility of a one-time upgrade, which could break some users’ experiences due to the variety of devices and environments we are running at. 
 To mitigate this, we prioritized A/B testing capabilities in order to run the legacy version of WebRTC alongside the new upstream version with clean patches and apply our features in the same app while being able to dynamically switch users between them to verify the new version. 
 Due to application build graph and size constraints, we also prioritized finding a solution to statically link two WebRTC versions. However, this violates the C++ linker One Definition Rule (ODR), causing thousands of symbol collisions, so we turned to finding a way to make two versions of the same library coexist in the same address space. 
 Furthermore, Meta is using a monorepo and we don’t want to undergo the same process over and over again. This motivated us to find a solution to maintain custom patches for open-source projects in a monorepo environment, while being able to pull new versions from upstream and apply the patches over and over again. 
 This led us to focus on solving two challenges: 
 We desired A/B testing capability. To achieve that, we built two copies of WebRTC in the same library due to application constraints. 
 With no feature branches in monorepo, how do we track patches and rebase them? Other libwebrtc-based OSS projects usually do this by applying a set of stored patch files sequentially on top of the clean repo on each library upgrade. Due to scalability concerns, we explored more nuanced options. 
 Solution 1: The Shim Layer and Dual-Stack Architecture 
 To address the A/B testing capability, we chose to build two copies of WebRTC within the same app. However, doing this statically within the same overarching call orchestration library creates unique challenges. To tackle this, we built a shim layer between the application layer and WebRTC. It is a proxy library that sits between our application code and the underlying WebRTC implementations. Instead of the app calling WebRTC directly, it calls the shim API. The shim exposes a single, unified, version-agnostic API. 
 The shim layer holds a “flavor” configuration and dispatches each call to either the legacy or latest WebRTC implementation at runtime. This approach – shimming at the lowest possible layer – avoids a significant binary size regression that duplicating the higher-layer call orchestration library would have caused. Duplication would have resulted in an uncompressed size increase of approximately 38 MB, whereas our solution added only about 5 MB – an 87% reduction. 
 Next, we’ll look at the hurdles introduced by this dual-stack architecture and how we resolved them. 
 Solving Symbol Collisions 
 Statically linking two copies of WebRTC into a single binary produces thousands of duplicate symbol errors. 
 In order to ensure every symbol in each flavor is unique, we leveraged automated renamespacing: We built scripts that systematically rewrite every C++ namespace in a given WebRTC version, so the webrtc:: namespace in the latest upstream copy becomes webrtc_latest:: , while the legacy copy becomes webrtc_legacy::. This rename was applied to every external namespace in the library. 
 But not everything in WebRTC lives in a namespace – global C functions, free variables, and classes that were left outside namespaces intentionally or accidentally also collide. 
 For those, we moved what we could into namespaces and manipulated the symbols of the rest (like global C functions) with flavor-specific identifiers. 
 Macros and preprocessor flags presented a subtler problem. Macros like RTC_CHECK and RTC_LOG can be used outside of WebRTC in wrapper libraries, so including both versions’ headers in the same translation unit triggers redefinition errors. 
 We addressed this through a combination of strategies: 
 Removing spurious includes. 
 Renaming rarely-used macros. 
 Sharing internal WebRTC modules across versions where possible, like rtc_base . This last approach had the added benefit of reducing both binary size and the surface area of code that needed shimming. 
 Backward Compatibility 
 Renamespacing every symbol in WebRTC would break every external call site. Our focus was to keep existing code working without disruption. Some call sites are built with a constant WebRTC flavor, and not dual-stack. 
 Our initial approach was to forward-declare every used symbol from the new namespace and wire it to the old one. This worked, but produced a large fragile header file that required a high level of maintenance. 
 We iterated to a better solution: bulk namespace imports using C++ using declarations. By importing an entire flavor namespace into the familiar webrtc:: namespace, we achieved a concise declaration header where new symbols are handled automatically, with no binary size implications since these are pure compiler directives. External engineers continue writing code exactly as before – the wiring happens in parallel, where we migrate only external call sites we care about. 
 Flavoring: Runtime Version Dispatch 
 With the shim layer wrapping both WebRTC versions, the next question was: How do we dispatch to the correct version at runtime? Each adapter and converter needs to instantiate the right underlying object – webrtc_legacy:: or webrtc_latest:: , based on a global configuration flag. 
 We addressed this with a template-based helper library. Shared logic (which constitutes a large portion of the adapter code) is written once. Version-specific behavior is expressed through C++ template specializations. This keeps the code DRY while supporting backward compatibility with single-flavor builds during the transition period. A global flavor enum, set early in each app’s startup sequence, determines which flavor to activate. 
 We use directional adapters as intermediary objects that implement the unified API and dispatch to the underlying WebRTC object, or vice versa. We use directional converters as utility functions to translate structs and enums between the shim and WebRTC type systems. 
 Left: Used to expose internal WebRTC classes to external callers. Right: Used to inject custom components into WebRTC. Shim Generation 
 The shim layer itself required adapters and converters. With a large number of objects to shim across dozens of APIs – each requiring an abstract API definition, adapter and converters implementations, and unit tests – the estimated manual effort was huge! 
 We turned to automation. Using abstract syntax tree (AST) parsing, we built a code generation system that produces baseline shim code for classes, structs, enums, and constants. The generated code is fully unit-tested and easy to extend. This increased our velocity from one shim per day to three or four per day while reducing the risk of human error. For simple shims where the API is identical across versions, the generated code required close to zero manual intervention. For more complex cases – API discrepancies between versions, factory patterns, static methods, raw pointer semantics, and object ownership transfers – engineers refined the generated baseline. 
 Wiring and Building Dual-Stack Apps 
 With the shim layer in place, we began the painstaking work of rewiring all application references from direct WebRTC types to their shim equivalents. For example, webrtc::Foo became webrtc_shim::Foo . This introduced object ownership complexities and the potential for subtle bugs around null handling and memory management. We mitigated this through comprehensive unit testing that replicated problematic scenarios of ownership transfer and object lifetime, supplemented by end-to-end testing for particularly risky diffs. 
 We then worked iteratively toward building full apps in dual-stack mode, starting with small targets and working up. Each iteration surfaced new issues: missing shims, incorrectly flavored objects, and new macro or symbol collisions. 
 Some internal components that were injected into WebRTC from outside posed a particular challenge due to their deep dependencies on WebRTC internals. Since shimming these components would mean proxying WebRTC against itself, we instead “duplicated” them using C++ macro and Buck build machinery – dynamically changing namespaces at build time, duplicating the high-level build target, and exposing symbols for both flavors through a single header. 
 Once finished, we had our internal app, as well as some external applications, all building and running audio and video calls in dual-stack mode for both legacy and latest flavors. 
 Over 10,000 lines of shim code were added, and hundreds of thousands of lines were modified across thousands of files. Despite the scope, careful testing and review meant no major issues. 
 Using this approach, we were able to A/B test the legacy WebRTC release against the latest one, app-by-app, mitigate regressions, ship, and delete the legacy code. Today, the shim approach is used in some applications so we can continuously upgrade the internal WebRTC code with the latest upstream updates. 
 Solution 2: The Feature Branches 
 Since we use a monorepo without widespread support for branches , we sought a way to track patches over time that would be continuously rebased on top of upstream. Our clear requirement was that each patch would have a clearly delineated purpose and owning team. 
 We had two choices here: We could track patch files checked into source control and reapply them one by one in the correct order, or we could track patches in a separate repository that supported branching. 
 In the end we chose to go with tracking feature branches in a separate Git repository. One of the reasons for this was to establish a good pipeline for making it very easy to submit feature branches and fixes upstream. 
 By basing them on top of the libwebrtc Git repo, we could easily reuse existing upstream Chromium tools for building, testing, and submitting (`gn`, `gclient`, `git cl`, and more). 
 For each upstream Chromium release (such as M143 which has tag 7499 in git), we create a “base/7499” branch. Then, for each of our patches (e.g. “debug-tools”) we create a “debug-tools/7499” branch on top of the base/7499 commit. During a version upgrade, we merge forward all feature branches, debug-tools/7499 gets merged into debug-tools/7559, hw-av1-fixes/7499 into hw-av1-fixes/7599, and so on. 
 Once all features are merged forward with resolved conflicts and working builds + tests, we merge all the feature branches sequentially together to create the release candidate branch r7559. 
 Some nice benefits from this approach are that it is highly parallelizable if there are many branches, it automatically preserves all Git history/context, and it is well-suited for future improvements in LLM-driven auto-resolution of merge conflicts. Additionally, the feature branches make it easy to submit the branch as a whole as an upstream contribution into OSS. 
 The Result: Continuous Upgrades 
 This architecture allowed us to ship a binary containing both the old and new WebRTC stacks. We launched webrtc/latest on version M120 and have since progressed to M145. Instead of being years behind, we now stay current with the latest stable Chromium releases, ingesting upstream upgrades immediately. 
 Key Engineering Wins 
 Performance : We saw CPU usage drop by up to 10% and crash rates improve by up to 3% across major apps. 
 Binary Size : The new upstream version is more efficient, resulting in a 100-200 KB (compressed) size reduction depending on the app. 
 Security : We eliminated deprecated libraries (like usrsctp) and fixed security vulnerabilities present in the legacy stack. 
 All the above drove observable user engagement improvements while running on a modern stack. 
 This project proves that even in a complex monorepo environment with various constraints, it is possible to modernize technical debt without a complete rewrite. The shim layer with dual-stack approach offers a blueprint for any organization looking to escape the forking trap. 
 Future Work: AI-Driven Maintenance 
 With the migration complete, we are entering a new era of maintenance. While we are now “living at head,” we still apply internal patches on top of upstream. To manage this efficiently, we are leveraging tools to automate our workflows: 
 Build Health: We are developing agents to automatically fix build errors in our Git branches. 
 Conflict Resolution: When rebasing our patches on new WebRTC releases, we encounter merge conflicts. We are training AI agents to resolve the majority of these conflicts automatically, leaving only the most complex architectural changes for human engineers. 
 Acknowledgements 
 This work was accomplished by a small team of engineers who recognized the value of this strategic project and dove in head-first despite its complexity. They brought creative ideas and solutions, did the heavy lifting, and ultimately drove the project to completion in the face of unexpected blockers and unique challenges along the way: Dor Hen, Guy Hershenbaum, Jared Siskin, Liad Rubin, Tal Benesh, and Yosef Twaik. 
 The post Escaping the Fork: How Meta Modernized WebRTC Across 50+ Use Cases appeared first on Engineering at Meta .
```

---

## 6. Trust But Canary: Configuration Safety at Scale

- 日期: 2026-04-08 18:25
- 链接: https://engineering.fb.com/2026/04/08/security/trust-but-canary-configuration-safety-at-scale-meta-tech-podcast/

```
As AI increases developer speed and productivity it also increases the need for safeguards. 
 On this episode of the Meta Tech Podcast, Pascal Hartig sits down with Ishwari and Joe from Meta’s Configurations team to discuss how Meta makes config rollouts safe at scale. Listen in to learn about canarying and progressive rollouts, the health checks and monitoring signals used to catch regressions early, and how incident reviews focus on improving systems rather than blaming people. 
 They also talk about how data and AI/machine learning are slashing alert noise and speeding up bisecting when something goes wrong. 
 Download or listen to the episode below: 
 You can also find the episode wherever you get your podcasts, including: 
 Spotify 
 Apple Podcasts 
 Pocket Casts 
 The Meta Tech Podcast is a podcast, brought to you by Meta, where we highlight the work Meta’s engineers are doing at every level – from low-level frameworks to end-user features. 
 Send us feedback on Instagram , Threads , or X . 
 And if you’re interested in learning more about career opportunities at Meta visit the Meta Careers page. 
 The post Trust But Canary: Configuration Safety at Scale appeared first on Engineering at Meta .
```

---

## 7. How Meta Used AI to Map Tribal Knowledge in Large-Scale Data Pipelines

- 日期: 2026-04-06 16:00
- 链接: https://engineering.fb.com/2026/04/06/developer-tools/how-meta-used-ai-to-map-tribal-knowledge-in-large-scale-data-pipelines/

```
AI coding assistants are powerful but only as good as their understanding of your codebase. When we pointed AI agents at one of Meta’s large-scale data processing pipelines – spanning four repositories, three languages, and over 4,100 files – we quickly found that they weren’t making useful edits quickly enough. 
 We fixed this by building a pre-compute engine: a swarm of 50+ specialized AI agents that systematically read every file and produced 59 concise context files encoding tribal knowledge that previously lived only in engineers’ heads. The result: AI agents now have structured navigation guides for 100% of our code modules (up from 5%, covering all 4,100+ files across three repositories). We also documented 50+ “non-obvious patterns,” or underlying design choices and relationships not immediately apparent from the code , and preliminary tests show 40% fewer AI agent tool calls per task. The system works with most leading models because the knowledge layer is model-agnostic. 
 The system also maintains itself. Every few weeks, automated jobs periodically validate file paths, detect coverage gaps, re-run quality critics, and auto-fix stale references. The AI isn’t a consumer of this infrastructure, it’s the engine that runs it. 
 The Problem: AI Tools Without a Map 
 Our pipeline is config-as-code: Python configurations, C++ services, and Hack automation scripts working together across multiple repositories. A single data field onboarding touches configuration registries, routing logic, DAG composition, validation rules, C++ code generation, and automation scripts –  six subsystems that must stay in sync. 
 We had already built AI-powered systems for operational tasks, scanning dashboards, pattern-matching against historical incidents, and suggesting mitigations. But when we tried to extend it to development tasks, it fell apart. The AI had no map. It didn’t know that two configuration modes use different field names for the same operation (swap them and you get silent wrong output), or that dozens of “deprecated” enum values must never be removed because serialization compatibility depends on them. 
 Without this context, agents would guess, explore, guess again and often produce code that compiled but was subtly wrong. 
 The Approach: Teach the Agents Before They Explore 
 We used a large-context-window model and task orchestration to structure the work in phases: 
 Two explorer agents mapped the codebase, 
 11 module analysts read every file and answered five key questions, 
 Two writers generated context files, and 
 10+ critic passes ran three rounds of independent quality review, 
 Four fixers applied corrections, 
 Eight upgraders refined the routing layer, 
 Three prompt testers validated 55+ queries across five personas, 
 Four gap-fillers covered remaining directories, and 
 Three  final critics ran integration tests – 50+ specialized tasks orchestrated in a single session. 
 The five questions each analyst answered per module: 
 What does this module configure? 
 What are the common modification patterns? 
 What are the non-obvious patterns that cause build failures? 
 What are the cross-module dependencies? 
 What tribal knowledge is buried in code comments? 
 Question five was where the deepest learnings emerged. We found 50+ non-obvious patterns like hidden intermediate naming conventions where one pipeline stage outputs a temporary field name that a downstream stage renames (reference the wrong one and code generation silently fails), or append-only identifier rules where removing a “deprecated” value breaks backward compatibility. None of this had been written down before. 
 What We Built: A Compass, Not An Encyclopedia 
 Each context file follows what we call “compass, not encyclopedia” principle –  25–35 lines (~1,000 tokens) with four sections: 
 Quick Commands (copy-paste operations). 
 Key Files (the 3–5 files you actually need). 
 Non-Obvious patterns. 
 See Also (cross-references). 
 No fluff, every line earns its place. All 59 files together consume less than 0.1% of a modern model’s context window. 
 On top of this, we built an orchestration layer that auto-routes engineers to the right tool based on natural language. Type, “Is the pipeline healthy?” and it scans dashboards and matches against 85+ historical incident patterns. Type, “Add a new data field” and it generates the configuration with multi-phase validation. Engineers describe their problem; the system figures out the rest. 
 The system self-refreshes every few weeks, validating file paths, identifying coverage gaps, re-running critic agents, and auto-fixing issues. Context that decays is worse than no context at all. 
 Beyond individual contextual files, we generated a cross-repo dependency index and data flow maps showing how changes propagate across repositories. This turns “What depends on X?” from a multi-file exploration (~6000 tokens) into a single graph lookup (~200 tokens) – in config-as-code where one field change ripples across six-subsystems. 
 Results 
 Metric Before After 
 AI context coverage ~5% (5 files) 100% (59 files) 
 Codebase files with AI navigation ~50 4,100+ 
 Tribal knowledge documented 0 50+ non-obvious patterns 
 Tested prompts (core pass rate) 0 55+ (100%) 
 In preliminary tests on six tasks against our pipeline, agents with pre-computed context used roughly 40% fewer tool calls and tokens per task. Complex workflow guidance that previously required ~two days of research and consulting with engineers now completes in ~30 minutes. 
 Quality was non-negotiable: three rounds of independent critic agents improved scores from 3.65 to 4.20 out of 5.0, and all referenced file paths were verified with zero hallucinations. 
 Challenging the Conventional Wisdom on AI Context Files 
 Recent academic research found that AI-generated context files actually decreased agent success rates on well-known open-source Python repositories. This finding deserves serious consideration but it has a limitation: It was evaluated on codebases like Django and matplotlib that models already “know” from pretraining. In that scenario, context files are redundant noise. 
 Our codebase is the opposite: proprietary config-as-code with tribal knowledge that exists nowhere in any model’s training data. Three design decisions help us avoid the pitfalls the research identified: files are concise (~1,000 tokens, not encyclopedic summaries), opt-in (loaded only when relevant, not always-on), and quality-gated (multi-round critic review plus automated self-upgrade). 
 The strongest argument: Without context, agents burn 15–25 tool calls exploring, miss naming patterns, and produce subtly incorrect code. The cost of not providing context is measurably higher. 
 How to Apply This to Your Codebase 
 This approach isn’t specific to our pipeline. Any team with a large, proprietary codebase can benefit: 
 Identify your tribal knowledge gaps . Where do AI agents fail most? The answer is usually domain-specific conventions and cross-module dependencies that aren’t documented anywhere. 
 Use the “five questions” framework . Have agents (or engineers) answer: what does it do, how do you modify it, what breaks, what depends on it, and what’s undocumented? 
 Follow “compass, not encyclopedia . “ Keep context files to 25–35 lines. Actionable navigation beats exhaustive documentation. 
 Build quality gates . Use independent critic agents to score and improve generated context. Don’t trust unreviewed AI output. 
 Automate freshness . Context that goes stale causes more harm than no context. Build periodic validation and self-repair. 
 What’s Next 
 We are expanding context coverage to additional pipelines across Meta’s data infrastructure and exploring tighter integration between context files and code generation workflows. We’re also investigating whether the automated refresh mechanism can detect not just stale context but emerging patterns and new tribal knowledge forming in recent code reviews and commits. 
 This approach turned undocumented tribal knowledge into structured, AI-readable context and one that compounds with every task that follows. 
 The post How Meta Used AI to Map Tribal Knowledge in Large-Scale Data Pipelines appeared first on Engineering at Meta .
```

---

## 8. KernelEvolve: How Meta’s Ranking Engineer Agent Optimizes AI Infrastructure

- 日期: 2026-04-02 19:59
- 链接: https://engineering.fb.com/2026/04/02/developer-tools/kernelevolve-how-metas-ranking-engineer-agent-optimizes-ai-infrastructure/

```
This is the second post in the Ranking Engineer Agent blog series exploring the autonomous AI capabilities accelerating Meta’s Ads Ranking innovation. The previous post introduced Ranking Engineer Agent’s ML exploration capability , which autonomously designs, executes, and analyzes ranking model experiments. This post covers how to optimize the low-level infrastructure that makes those models run efficiently at scale. We introduce KernelEvolve, an agentic kernel authoring system used by Ranking Engineer Agent and generally applicable to a range of AI models beyond Ads Ranking. 
 Summary 
 Meta operates a large fleet of heterogeneous hardware — NVIDIA GPUs, AMD GPUs, Meta’s custom MTIA silicon chips, and CPUs. Using this hardware effectively and efficiently requires developing software that translates high-level model operations into efficient, chip-specific instructions called optimized kernels. Authoring and optimizing kernels must be done for each new chip generation and ML model architecture. Beyond standard kernel operators like general matrix multiplications (GEMMs) and convolutions covered by vendor libraries, production workloads require many custom operators across ranking models. With the number of models and number of hardware types and generations, hand-tuning by kernel experts doesn’t scale. 
 To address the volume of performance optimization work required by the increasing number of models X number of hardware types & generations, we built KernelEvolve , an agent to optimize performance used by Meta’s Ranking Engineer Agent . It enables: Faster development : Compresses weeks of expert engineering time optimizing kernels, including profiling, optimizing, and cross-hardware debugging, into hours of automated search and evaluation, freeing engineers for other work. 
 Better  performance : Over 60% inference throughput improvement for the Andromeda Ads model on NVIDIA GPUs and over 25% training throughput improvement for an ads model on Meta’s custom MTIA silicon chips. 
 Broad applicability : Optimizes across public and proprietary hardware including NVIDIA GPUs, AMD GPUs, MTIA chips and CPUs , generating kernels in high-level DSLs like Triton, Cute DSL, and FlyDSL, as well as low-level languages including CUDA, HIP, and MTIA C++. 
 KernelEvolve treats kernel optimization as a search problem: a purpose-built job-harness evaluates each candidate kernel, feeds diagnostics back to the LLM, and drives a continuous search over hundreds of alternatives, exceeding the performance of human expert generated kernels. 
 More details are available in the paper, “ KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta ,” which will appear at the 53rd International Symposium on Computer Architecture (ISCA) 2026 . 
 Every day, Meta serves billions of AI-powered experiences, from personalized recommendation to generative AI assistants, on a global infrastructure including diverse hardware from NVIDIA, AMD, and Meta’s custom MTIA silicon chips. Behind every training or inference request lies a layer of highly optimized low-level hardware kernels:  small programs that translate high-level model operations into instructions a specific chip can execute efficiently. As AI models grow more complex and the hardware landscape diversifies, the number of kernels scales across hardware platforms, model architectures and operator types, resulting in thousands of configurations that can no longer realistically be tuned by human experts, creating a critical bottleneck that delays hardware enablement and performance tuning and slowing model iteration cycles that drive critical advances in ML technology and its applications. 
 Today, we are sharing KernelEvolve , an agentic AI system that improved ads model inference throughput by 60% in hours of experimentation, a task that would take human experts weeks. KernelEvolve autonomously generates and optimizes production-grade kernels for heterogeneous hardware used in training and inference, including NVIDIA GPUs, AMD GPUs, Meta’s custom MTIA silicon, and CPUs. Unlike typical large language model (LLM)-based agents that perform one-shot code generation, KernelEvolve treats kernel optimization as a search problem. It explores hundreds of alternative kernel implementations to identify a solution that often matches or exceeds human expert performance, and does so in hours instead of weeks. In Meta’s production environment, KernelEvolve is optimizing code that serves trillions of daily inference requests. 
 KernelEvolve represents a fundamental shift in how we think about the relationship between AI software and hardware. Where kernel development was once a manual, expert-driven process that struggled to keep pace with hardware and model evolution, KernelEvolve makes it continuous and automated — adapting as each changes. As Meta continues to diversify its AI hardware portfolio, the ability to rapidly generate optimized kernels for new chips  substantially reduces the engineering effort required to integrate heterogeneous hardware for training and inference. 
 The Challenge: The Bottleneck of Explosive Kernel Growth 
 We’re seeing explosive kernel growth because the total number of kernels scales with the product of three factors: {hardware types and generations X model architectures X number of operators}. This product results in thousands of unique kernel configurations that must be written, tested, and maintained. Hand-tuning each kernel doesn’t scale, and kernel experts alone can’t keep up with the pace. 
 Hardware Heterogeneity 
 Meta’s accelerator fleet now spans NVIDIA GPUs, AMD GPUs, and Meta’s custom MTIA silicon, each with fundamentally different memory architectures and hierarchies, instruction sets, and execution models. A kernel that runs optimally on one platform may perform poorly or fail entirely on another. And the complexity doesn’t stop at vendor boundaries. Even within a single hardware family, successive generations introduce architectural changes that require different optimization strategies. Meta’s MTIA roadmap spans four chip generations in two years ( MTIA 300 through 500 ), each introducing new compute capabilities, memory bandwidth characteristics, and numeric data types optimized for evolving workloads. A kernel optimized for one generation will underperform when run on the next generation of the same hardware architecture. 
 Model Architecture Variation 
 Meta’s recommendation models have evolved through three major phases: from early embedding-based deep learning recommendation models, to sequence learning models that process engagement histories with attention mechanisms, to Meta’s Generative Ads Recommendation Model (GEM ), and most recently Meta’s foundation inference model that brings LLM-scale to ads ( Meta Adaptive Ranking Model ) . Each generation introduces operator types the previous generation never needed. Beyond these generational shifts, Meta’s production stack simultaneously serves fundamentally different model families, each with its own unique operators, and a single ads request may traverse multiple families in one serving call. With a vast and growing number of distinct models in production, every new architecture extends the matrix of operators that must be optimized across hardware. 
 Kernel Diversity Beyond Standard Libraries 
 Vendor libraries like cuBLAS and cuDNN cover a set of common operations — GEMMs, convolutions, standard activations — but even these standard operators resist one-size-fits-all solutions. A single operator like matrix multiplication behaves differently across contexts: The optimal kernel for a training batch differs from an inference serving request, and tensor shapes vary widely across ranking stages and ranking models, creating a combinatorial space of configurations that neither human experts nor today’s compiler-based autotuning and fusion can fully cover at scale. Beyond standard operators, production workloads are dominated by a long tail of operators that fall outside library coverage. These include data preprocessing transforms like feature hashing, bucketing, and sequence truncation that prepare raw input for model inference, as well as custom model operators like fused feature interaction layers and specialized attention variants that are unique to Meta’s architectures. 
 None of these custom operators appear in vendor libraries, and many are too workload-specific to warrant a library implementation. Without native accelerator implementations, these operators either fall back to CPU — forcing disaggregated serving architectures with significant latency overhead — or run via unoptimized code paths that underutilize hardware. 
 The problem compounds with hardware diversity. A hand-tuned NVIDIA kernel cannot simply be recompiled for AMD GPUs or MTIA. Each new model architecture extends the tail further, and each new chip multiplies the work required to cover it. 
 How KernelEvolve Addresses These Challenges 
 Each challenge maps to a specific architectural decision: 
 Challenge How KernelEvolve Addresses It 
 Hardware Heterogeneity A retrieval-augmented knowledge base injects platform-specific documentation including architecture manuals, instruction sets, and/or optimization patterns into the generation context. The LLM reasons over this documentation at inference time—no prior training on the target hardware required. A single universal prompting interface eliminates per-platform prompt templates. 
 Model Architecture Variation Tree search explores implementation alternatives for any operator, including novel ones. Successful optimizations are distilled into reusable patterns that transfer across model families—an optimization discovered for one architecture accelerates similar operators in future ones. 
 Kernel Diversity / Long Tail Automated evaluation validates hundreds of candidates in parallel. Search-based optimization replaces the need for hand-tuning, making operators feasible that wouldn’t otherwise justify weeks of manual tuning. 
 KernelEvolve: Searching for Optimal Kernels 
 KernelEvolve approaches this challenge differently from standard AI coding assistants. Rather than prompting an LLM to generate a single kernel and testing it, the system formalizes kernel optimization as a structured search problem across the space of possible implementations. Under the hood, a purpose-built long-running job harness drives each iteration – compiling candidates, evaluating correctness and performance, profiling hardware utilization, and generating analysis reports – all while handling the multi-minute build cycles and infrastructure failures that make native approaches impractical. 
 Figure 1: ​​How a kernel optimization request flows through KernelEvolve’s six components. LLM Synthesizer 
 An LLM generates candidate kernels across multiple programming languages and hardware targets — from high-level DSLs like Triton, TLX , CuTe DSL, and FlyDSL, to low-level backends including CUDA, HIP, and MTIA C++. 
 Rather than using static prompts, the synthesizer constructs dynamic, context-aware prompts that are continuously enriched with runtime diagnostics, hardware constraints, and the historical signals from prior candidate optimization evaluation. This replaces the traditional approach of maintaining separate prompt templates for debugging, performance tuning, and correctness verification with a single adaptive interface that unifies these workflows into a single adaptive interface that drives a continuous, feedback-driven optimization loop. 
 Tree Search Engine 
 The system explores the optimization space using graph-based search algorithms, including Monte Carlo tree search and evolutionary strategies. Each kernel candidate becomes a node in a search tree. The engine selects promising candidates, applies transformations, evaluates results, and decides whether to explore further or backtrack — balancing exploitation of known-good strategies against exploration of novel approaches. 
 Crucially, nodes do not evolve in isolation. Each node carries a configurable memory operator that determines how it draws context from the search tree when generating the next round of candidates. A node may inherit its parent’s optimization trajectory to refine a promising direction, compare against siblings to learn what differentiates high-performing variants, combine insights from both parent and sibling histories, or start with a clean slate to escape local optima. This selective memory mechanism allows the tree search to move beyond simple independent sampling – sibling nodes collaborate by surfacing complementary strategies, parent-child chains preserve and deepen successful optimization paths, and memory-free restarts inject diversity when the search stagnates. 
 Figure 2: How the tree search engine navigates the optimization space to find high-performing kernels. Retrieval-Augmented Knowledge Base 
 To generate optimized code for hardware the underlying LLM was never trained on, KernelEvolve maintains a hierarchical knowledge base organized into three categories: correctness constraints that enforce valid kernel implementations, platform-agnostic optimization guidance covering debugging and tuning strategies, and hardware-specific documentation containing architectural details for each accelerator platform. The system retrieves relevant knowledge dynamically based on runtime signals. For example, a memory bandwidth bottleneck triggers retrieval of memory hierarchy documentation; a compilation error activates debugging guidance. 
 This knowledge base is not static. As the system solves new optimization problems it distills successful strategies into reusable skills — compact optimization patterns and debugging heuristics — that are continuously written back into the knowledge base. This self-evolving skill library acts as a form of in-context reinforcement learning : Each successful exploration enriches the context available to future sessions, enabling the system to solve similar problems faster and with fewer search steps, without requiring model retraining. 
 Automated Evaluation Framework 
 Every generated kernel passes through a rigorous validation pipeline that checks both correctness — bitwise accuracy against reference implementations — and performance. And evaluation goes far beyond a single runtime number. 
 KernelEvolve leverages a stack of profiling tools, each targeting a different level of analysis. TritonBench validates numerical correctness against PyTorch baselines and measures end-to-end speedup across production input shapes. PyTorch Profiler captures system-level execution timelines, including kernel launch overhead and host-device synchronization. For GPU targets, tools like NCU provide kernel-level hardware metrics — occupancy, memory throughput, instruction mix — while Proton delivers intra-kernel instruction-level latency and pipeline behavior. For MTIA targets, MTIA Insight provides comprehensive accelerator-specific instrumentation: PE utilization, fixed-function engine metrics (DPE, SFU, MLU utilization and stall cycles), cache behavior, and per-PE memory bandwidth counters. 
 Rather than treating these tools as standalone steps, KernelEvolve unifies them through a compiler-centric abstraction. The framework composes analysis through job graphs: compiler transforms insert MLIR-level instrumentation, profiling passes collect metrics, and trace synthesis produces structured output. This means the search engine doesn’t just see “kernel A is 1.2x faster than kernel B” — it sees why: whether the bottleneck is memory-bound, compute-bound, or limited by occupancy — and feeds that diagnostic signal back into the LLM synthesizer to guide the next round of candidates. 
 Shared Data Foundation 
 Every optimization session contributes to a shared data foundation. When one engineer’s exploration discovers an effective tiling strategy for a class of operators, that insight becomes available to every future session targeting similar workloads — creating a compounding effect where the system grows more capable with each use. Early adopters perform the hardest exploration; subsequent users inherit much closer to optimal starting points and refine from there. 
 Agentic Reinforcement Learning 
 Every optimization session generates structured training data as a natural byproduct: agentic trajectories capturing the reasoning, code transformations, and evaluation feedback behind high-performing kernels. This domain-specific data is rare and valuable . It encodes optimization intuition that no public dataset contains. 
 We use this data to post-train smaller, specialized models through agentic reinforcement learning, where the reward signal comes directly from measured kernel performance. The result is a virtuous cycle where better models produce better kernels in fewer reasoning tokens and fewer search steps, which in turn generate higher-quality training data. Over successive iterations, this compounding flywheel enables us to self-host increasingly efficient models that are compact enough to run cost-effectively at scale while retaining the optimization capability of much larger frontier models. 
 Enabling Proprietary AI Chips 
 One of the most consequential capabilities of this architecture is its ability to generate optimized code for hardware that does not exist in any public training dataset. 
 Meta’s custom MTIA chips present a unique programming challenge. Because these chips are proprietary, no public LLM has been trained on MTIA code. A standard coding assistant lacks the context to write optimized MTIA kernels because it has never seen MTIA documentation, instruction set details, or programming idioms. 
 KernelEvolve solves this through systematic knowledge injection. We encode MTIA-specific documentation (architecture manuals, instruction set references, memory hierarchy specifications, and optimization patterns) directly into the retrieval-augmented knowledge base. When the system targets MTIA, it retrieves and incorporates this proprietary knowledge into its reasoning, effectively “learning” the hardware in real time. 
 This approach extends to any new accelerator. When a new chip arrives, the engineering cost shifts from writing thousands of kernels by hand to curating a set of hardware documents and injecting them into the knowledge base. The system then autonomously generates optimized kernels for the new platform, ensuring the software stack is ready at the speed of hardware deployment rather than the speed of manual engineering. 
 KernelEvolve’s Impact Across Benchmark and Production 
 KernelEvolve has delivered strong results across both standardized benchmarks and production workloads. 
 Benchmark performance : On KernelBench, a benchmark suite of 250 kernel optimization problems from Stanford spanning three difficulty levels, KernelEvolve achieves a 100% pass rate — all generated kernels are both functionally correct and faster than their PyTorch reference implementations. The system also validates 160 PyTorch ATen operators with 100% correctness across three hardware platforms (480 total configurations). 
 Production speedups : On Meta’s MTIA chips, KernelEvolve’s generated kernels, which spanned compute-bound, memory-bound, and custom operations, achieved speed ups of over 25% training throughput improvement on an ads model. On NVIDIA GPUs, it delivered more than 60% inference throughput improvement over a model with highly optimized kernels including torch.compile and vendor libraries — performance gains that directly translate to serving capacity and infrastructure efficiency. 
 Hardware coverage : The system generates optimized kernels for NVIDIA GPUs, AMD GPUs, Meta’s custom MTIA silicon, and CPUs — from a single unified framework. Rather than maintaining separate prompt templates per platform, the system dynamically retrieves hardware-specific constraints and optimization patterns, adapting to each target through retrieval augmentation rather than manual prompt engineering. 
 Development Velocity 
 Kernel development that previously required weeks of expert effort — profiling, iterating on tiling strategies, debugging edge cases across hardware — now completes in hours through automated search and evaluation. This shifts engineer time from writing low-level code to higher-value work such as designing model architectures, improving training techniques, and defining optimization objectives. 
 How It All Fits Together 
 An engineer specifies a target operator, hardware platform, and performance goals. The system then autonomously: 
 Retrieves relevant hardware documentation and optimization knowledge from the knowledge base. 
 Generates an initial set of kernel candidates using the LLM synthesizer with context-aware prompting. 
 Evaluates each candidate for correctness and performance using distributed benchmarking infrastructure. 
 Feeds results back into the search engine, which selects the most promising candidates and applies further optimizations. 
 Iterates steps 1-4, exploring the search tree until the termination criteria are met — either a performance target is achieved, the search budget is exhausted, or progress stalls. 
 Outputs the best-performing, fully validated kernel, ready for production deployment. 
 The process runs on Meta’s distributed infrastructure, evaluating thousands of candidates in parallel. Persistent storage of search trees and implementations lets the system build on prior results when targeting new model variants or hardware generations. 
 Looking Ahead 
 The same agentic techniques powering KernelEvolve — structured reasoning, retrieval-augmented knowledge, closed-loop evaluation — can be applied to hybrid model search, compiler optimization, memory management, and system configuration. KernelEvolve represents an early step toward the vision of a Ranking Engineer Agent that can continuously optimize its own performance-critical infrastructure. 
 Within REA, ML Exploration discovers better models. KernelEvolve makes them production-ready. Together, they accelerate how quickly ranking improvements reach advertisers. 
 In the next post in the REA series, where we’ll explore other agentic ML optimizations. 
 Read the Paper 
 For more technical details, read our paper, “ KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta ”  from ISCA 2026 . 
 Acknowledgements 
 We would like to thank Ying Wang, Hongsen Qin, Tao Yang, Jia Jiunn Ang, Yujia He, Alicia Golden, Michael Kuchnik, Wei Guo, Yihan He, Jiangyuan Li, Dianshi Li, Chao Xie, Adele Sun, Richard Li, Alec Hammond, Roman Levenstein, Hongtao Yu, Yuanwei (Kevin) Fang,  Kunming Ho, Haishan Zhu, Site Cao, Abdullah Ozturk, Jort Gemmeke, Daniel Wang, Juan Angeles Acuna, Yoram Bachrach, Ming Chen, Terry Chen, Jake Cheng, Wayne Chiang, Wenyuan Chi, Rick Chang, Wyatt Cook, Tri Dao, Barry Dong, Liubov Dmitrieva, Derek Dunfield, Zhou Fang, Rob Fergus, Maxwell Harrison Fisch, Zacharias Fisches, Zach Freeman, Chunli Fu, Vishal Gandhi, Kaustubh Gondkar, Wentian Guo, Han Guo, William Hanwei Liang, Samuel Hsia, Barney Huang, Nicholas Hungria, Martin Josifoski, Jacob Kahn, Shobhit Kanaujia, Drew Lackman, Marek Latuskiewicz, Kristin Lauter, Matan Levi, Evan Li, Yiting Li, Jiang Liu, Alexey Loginov, Yining Lu, Anuj Madan, John Martabano, Anna Mcburney, Keyur Muzumdar, Kelvin Niu, Sandeep Pandey, Uladzimir Pashkevich, Dmitrii Pedchenko, Pedro Pedreira, Varna Puvvada, Preyas Janak Shah, Bidit Sharma, Feng Shi, Stanley Shi, Ketan Singh, Vibha Sinha, Matt Steiner, Gabriel Synnaeve, Oleksandr Stashuk, Jim Tao, Ritwik Tewari, Chris Wiltz, Yao Xuan, Tak Yan, Bill Yoshimi, Xiayu Yu, Abdul Zainul-Abedin, Qing Zhang, and Mingjie Zhu 
 The post KernelEvolve: How Meta’s Ranking Engineer Agent Optimizes AI Infrastructure appeared first on Engineering at Meta .
```

---

## 9. Meta Adaptive Ranking Model: Bending the Inference Scaling Curve to Serve LLM-Scale Models for Ads

- 日期: 2026-03-31 16:00
- 链接: https://engineering.fb.com/2026/03/31/ml-applications/meta-adaptive-ranking-model-bending-the-inference-scaling-curve-to-serve-llm-scale-models-for-ads/

```
Meta continues to lead the industry in utilizing groundbreaking AI Recommendation Systems (RecSys) to deliver better experiences for people, and better results for advertisers. To reach the next frontier of performance, we are scaling Meta’s Ads Recommender runtime models to LLM-scale & complexity to further a deeper understanding of people’s interests and intent. 
 This increase in scale & complexity exacerbates a fundamental “inference trilemma”: the challenge of balancing the increased model complexity and associated need for compute and memory with the low latency and cost efficiency required for a global service serving billions of people. To overcome this, we have developed the Meta Adaptive Ranking Model, which effectively bends the inference scaling curve with high ROI and industry-leading efficiency. 
 Adaptive Ranking Model replaces a “one-size-fits-all” inference approach with intelligent request routing. By dynamically aligning model complexity with a rich understanding of a person’s context and intent, the system ensures every request is served by the most effective & efficient model. This allows Meta Ads to maintain the strict, sub-second latency the platform depends on while providing a high-quality experience for every person. 
 Serving LLM-scale models at Meta’s scale required a fundamental rethink of the inference stack, driven by three key innovations: 
 Inference-Efficient Model Scaling : By shifting to a request-centric architecture, Adaptive Ranking Model serves a LLM-scale & complexity model at sub-second latency, enabling a more sophisticated understanding of a person’s interests and intent without compromising the experience. 
 Model/System Co-Design : By developing hardware-aware model architectures that align model design with underlying hardware system and silicon’s capabilities and limitations, Adaptive Ranking Model significantly improves hardware utilization in heterogeneous hardware environments. 
 Reimagined Serving Infrastructure : Leveraging multi-card architectures and hardware-specific optimizations, Adaptive Ranking Model enables O(1T) parameter scaling, allowing us to serve the LLM-scale runtime RecSys models with unprecedented efficiency. 
 By further integrating LLM-scale intelligence into our ads stack, Adaptive Ranking Model delivers a significant increase in ad conversions and advertiser value while maintaining system-wide computational efficiency. This ensures superior performance for businesses of all sizes. Since launching on Instagram in Q4 2025, Adaptive Ranking Model has delivered a +3% increase in ad conversions and +5% increase in ad click through rate for targeted users. 
 Introducing Meta Adaptive Ranking Model 
 Serving LLM-scale & complexity models in a real-time ads recommendation environment requires resolving a fundamental tension between model complexity and system efficiency. Unlike LLM applications such as chatbots, where response times are measured in seconds, an ad recommendation must achieve two uncompromising constraints: 
 Latency impacts user experience: Ads must be chosen and returned with sub-second latency. Scaling ads computation to LLM-scale level and beyond has traditionally been impossible without latency regressions that compromise user experience. 
 Cost efficiency is crucial: Brute force scaling by simply adding hardware is economically unsustainable. Achieving a positive ROI requires unlocking higher model complexity without a corresponding increase in total costs. 
 Adaptive Ranking Model addresses these challenges through a paradigm shift powered by three core innovations across the serving stack: 
 Inference-efficient model scaling: Adaptive Ranking Model achieves a model complexity equivalent to the O(10 GFLOPs) per token used by top-tier LLMs. However, it operates an order of magnitude faster than standard LLM inference, maintaining O(100 ms) bounded latency. 
 Deep model-system co-design : Adaptive Ranking Model is deeply co-designed with the underlying hardware and silicon; we’ve boosted model FLOPs utilization (MFU) to 35% across multiple hardware types. 
 Reimagined serving infrastructure: Adaptive Ranking Model utilizes a multi-card GPU serving infrastructure to break the physical memory limits of single devices. This allows us to scale model parameters to O(1T) , providing a depth of understanding of people’s interests and intent  previously impossible at Meta’s scale. 
 By unifying these innovations, we ensure that the most effective model is used for every request — providing a highly personalized ad experience for people on our platforms and maximizing advertiser value while maintaining system-wide computational efficiency. 
 Inference-Efficient Model Scaling 
 Adaptive Ranking Model introduces model-system innovations that fundamentally redefine inference efficiency. This transformation is built on three technical pillars: 
 Transforming scaling costs from linear to sub-linear by shifting to a request-oriented computation flow that eliminates massive redundancy at LLM-scale. 
 Maximizing structural throughput through architectural refinements that stabilize deep models and minimize internal network bottlenecks. 
 Neutralizing complexity overhead through holistic latency optimization , offloading feature preprocessing to GPUs and streamlining the end-to-end execution path. 
 Transforming scaling costs from linear to sub-linear 
 Traditional models process each user-ad pair independently, creating massive computational redundancy. Adaptive Ranking Model eliminates this through Request-Oriented Optimization, which computes high-density user signals once per request rather than once per ad candidate. This shift, powered by Request-Oriented Computation Sharing and In-Kernel Broadcast optimization, which shares request-level embeddings across ad candidates directly within the GPU kernel, transforms scaling costs from linear to sub-linear while significantly reducing memory bandwidth pressure. 
 Building on this, Request-Oriented Sequence Scaling unlocks the use of long-form user behavior sequences that were previously limited by compute and storage costs. To minimize compute overhead, Adaptive Ranking Model processes heavy sequences once per request and shares the results across all ad candidates. To optimize storage, it replaces redundant data replication with a centralized, high-efficiency key-value store of user logs that are joined with training data on the fly. These optimizations jointly minimize the serving and storage footprints required for global-scale systems. 
 Maximizing Structural Throughput with Wukong Turbo 
 While Request-Oriented Optimization optimizes the computation flow, Wukong Turbo is the optimized runtime evolution of the Meta Ads internal architecture. Building on the Wukong architecture that uses stackable factorization machines, sequence learning and cross-layer attention, Wukong Turbo introduces specific refinements to handle the numeric instability and network overhead that typically arise when scaling deep models.  Specifically, it employs a No-Bias approach to remove unstable terms, boosting throughput without increasing FLOPs or parameter counts. To prevent internal bottlenecks, it utilizes small parameter delegation to reduce network and memory overhead by offloading parameters from Fully Sharded Data Parallel ( FSDP ) to Distributed Data Parallel ( DDP ) alongside sparsity-based simplification that reduces redundant components in the linear layers. These enhancements transform the base architecture into a stable, high-performing system, allowing model complexity to scale while strictly protecting the sub-second inference budget. 
 Neutralizing Complexity Overhead through Holistic Latency Optimization 
 The final stage of this transformation addresses feature preprocessing—a traditional bottleneck leading to client memory pressure and data starvation where the GPU’s compute power remains underutilized while waiting for processed features. Adaptive Ranking Model offloads preprocessing from the client CPU to remote GPU hosts, utilizing compact tuple-based formats and GPU-native kernels that reduce Top-K complexity from O (N log N) to O (N). To further speed up processing, we implemented a holistic strategy of optimized data compression and client-flow restructuring to eliminate thread-pool contention. These multi-layered optimizations successfully neutralized the latency penalty of LLM-scale & complexity, allowing Adaptive Ranking Model to deliver frontier-level personalization at the speed Meta’s global platforms require. 
 Maximizing Efficiency Through Deep Model-System Codesign 
 Meta Ads relies on deep system co-optimization to enable the LLM-scale model complexity within Meta-scale performance constraints. By fundamentally rethinking the boundary between the model and the hardware, we have created a unified inference stack that optimizes computational precision and graph execution to maximize computational ROI by boosting Model FLOPs Utilization (MFU) on heterogeneous hardware. 
 High-Throughput Inference with Selective FP8 Quantization 
 Large-scale models necessitate reduced precision to maintain high-throughput inference, yet a blanket application of low-precision quantization often degrades the nuance required for complex ads ranking. Adaptive Ranking Model overcomes this through a post-training quantization strategy that applies FP8 selectively. Using a micro-benchmark guided selection mechanism, the system deploys FP8 only in layers with high precision-loss tolerance. This targeted approach unlocks the throughput benefits of modern heterogeneous hardware for our most complex models with negligible impact on recommendation quality. 
 Hardware-Aware Graph and Kernel Specialization 
 To minimize the latency caused by redundant memory access and inefficient kernel launches, Adaptive Ranking Model optimizes the execution flow through coordinated graph and kernel specialization. We fuse operators that share inputs to minimize data movement between high-bandwidth memory and on-chip SRAM. Additionally, thousands of small operations are consolidated into compute-dense kernels using techniques like Grouped General Matrix Multiply and horizontal fusion. This precise alignment between the computation graph and modern GPU architectures significantly reduces the memory footprint and increases effective hardware utilization, ensuring that LLM-scale model complexity translates directly into performance. 
 Reimagined Serving Infrastructure for the Reality of LLM-Scale Production 
 Beyond model-system co-optimization, deploying LLM-scale models at scale requires reimagining the underlying serving infrastructure. To neutralize the latency penalty of massive scale, the Adaptive Ranking Model utilizes a specialized stack designed to surpass physical memory limits and ensure Meta-scale production reliability. 
 Trillion Parameter Scale 
 Unlike standard LLMs, recommendation models are driven by predominantly sparse, categorical features. Mapping these IDs to high-dimensional embedding tables creates a critical trade-off where oversized tables lead to overfitting, while undersized tables suffer from hash collisions that degrade model quality. Adaptive Ranking Model enables O(1T) parameter scale through memory optimizations that resolve this tension. The system efficiently allocates embedding hash sizes based on feature sparsity and prunes unused embeddings to maximize learning capacity within strict memory budgets. This is further optimized by unified embeddings, which allow multiple features to share a single embedding table to significantly reduce the memory footprint without sacrificing the ability to learn complex feature interactions. 
 Multi-GPU-Card Embedding Scaling 
 As LLM-scale model embeddings approached the terabyte level, they exceeded the memory capacity of any single GPU. To mitigate this, a multi-card sharding mechanism splits embedding tables into segments distributed across an optimized hardware cluster. By leveraging hardware-specific communication optimizations, the system maintains high throughput and efficient communication between shards. This multi-card architecture achieves performance parity with single-card setups, effectively decoupling model complexity from individual GPU hardware constraints. 
 Runtime Resilience and Reliability 
 Serving trillion-parameter models under high-traffic conditions presents significant reliability challenges, particularly regarding initialization speed and system stability. To ensure production-grade reliability, we developed accelerated model loading that utilizes multi-stream downloading and remote caching to load models in under 10 minutes, minimizing downtime during deployments. Auto-scaling rules based on streaming multiprocessor utilization allows the system to handle fluctuating traffic dynamically. This ensures real-time demand is met without the need for wasteful over-provisioning, maintaining stability across the platform. 
 The Path Forward: Evolving the Adaptive Ranking Model Stack 
 The launch of Adaptive Ranking Model on Instagram marks the first milestone in our journey to bend the inference performance vs cost scaling curve at Meta scale. The roadmap shifts from individual optimizations toward an infrastructure that is increasingly autonomous and responsive to real-time fluctuations in user signal density and request patterns across our global ecosystem. 
 This vision began with evolving inference efficient scaling to unlock deeper complexity and longer behavioral sequences that capture user intent with unprecedented fidelity. To sustain this growth, we are pioneering a new era of inference execution efficiency, leveraging advanced model compression and ultra-low precision quantization methods to allow the most sophisticated LLM-scale models to run efficiently across a diverse global hardware fleet. 
 To eliminate the traditional bottlenecks of manual engineering, we are exploring agentic optimization frameworks to further accelerate kernel performance optimizations. These frameworks will automatically adapt to new hardware and model architectures, ensuring that the most sophisticated AI remains accessible and performant at scale. 
 Furthermore, we’re reimaging the speed of learning through near-instantaneous model freshness, utilizing incremental, in-place weight updates to achieve constant, real-time adaptation. Collectively, these innovations will ensure that the Adaptive Ranking Model continues to power more personal experiences for people while driving superior ROAS for advertisers globally. 
 Acknowledgements 
 We would like to thank:  Jia Jiunn Ang, Ao Cai,Pan Chen, Wenlin Chen, Maomao Ding, Chengze Fan, Lu Fang, Birmingham Guan, Qin Huang, Daniel Molina Hurtado, Santanu Kolay, Ashwin Kumar, Boda Li, Huayu Li, Jiawei Li, Li Li (Ads Ranking), Liyuan Li, Mingda Li, Wenyuan Li, Rocky Liu, Jason Lu, Robert Luo, Yinbin Ma, Anna Mcburney, Sandeep Pandey, Uladzimir Pashkevich, Varna Puvvada, Pranav Sharma, Zijian Shen, Vibha Sinha, Matt Steiner, Chonglin Sun, Weiman Sun, Aaron (Li Bo) Tao, Bina Thakkar, Xiaohan Wei, Nathan Yan, Yantao Yao, Hongtao Yu, Li Yu, Sihan Zeng, Buyun Zhang, Bill Zhao, Alex Zhong, Zhehui Zhou, and the entire V-team team behind the development and productionization of the LLM scale runtime model in Meta’s ads recommendation system. 
 The post Meta Adaptive Ranking Model: Bending the Inference Scaling Curve to Serve LLM-Scale Models for Ads appeared first on Engineering at Meta .
```

---
