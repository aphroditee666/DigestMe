# Spring Blog

> 分类: 大厂技术博客
> URL: http://spring.io/blog.atom
> 抓取: 4 篇

---

## 1. Spring AI 1.0.7, 1.1.6, 2.0.0-M6 Available Now

- 日期: 2026-05-08 00:00
- 链接: https://spring.io/blog/2026/05/08/spring-ai-1-0-7-1-1-6-2-0-0-M6-available-now

```
On behalf of the Spring AI engineering team and everyone who has contributed, I'm happy to announce that Spring AI 1.0.7 , 1.1.6 , 2.0.0-M6 have been released and are now available from Maven Central. 
 These releases deliver important improvements, stability enhancements, and bug fixes across multiple release streams. 
 Release Summary 
 These releases include a combined total of 143 improvements, bug fixes, and documentation updates . See individual release notes: 1.0.7 | 1.1.6 | 2.0.0-M6 
 In addition, the releases contain security fixes for CVE-2026-41705 , CVE-2026-41712 and CVE-2026-41713 . 
 The focus of these releases includes: 
 Improvements : 42 enhancements across all releases 
 Stability : 13 bug fixes addressing community-reported issues 
 Documentation : 35 improvements to help developers 
 Security : 53 dependency upgrades for enhanced security 
 Thanks to all those who have contributed with issue reports and pull requests. 
 Version-Specific Highlights 
 Spring AI 1.0.7 
 Overview: 
 PromptChatMemoryAdvisor has been deprecated. Users should migrate to the updated chat memory advisor APIs that require explicit conversation IDs. 
 ⚠️ Breaking Changes: 
 Chat memory advisors now require an explicit conversation ID to be supplied. Previously, a default or implicit ID may have been used, which could cause incorrect memory scoping across conversations. Callers must now provide a conversation ID explicitly. 
 View complete release notes → 
 Spring AI 1.1.6 
 Overview: 
 PromptChatMemoryAdvisor has been deprecated. Users should migrate to the updated chat memory advisor API that requires an explicit conversation ID. This deprecation is part of a broader effort to improve conversation context management. 917f62e 
 ⚠️ Breaking Changes: 
 Chat memory advisors now require an explicit conversation ID to be supplied. This is a behavioral change that affects how chat memory is scoped and managed. Applications relying on implicit conversation IDs must be updated to supply an explicit ID. 
 View complete release notes → 
 Spring AI 2.0.0-M6 
 Overview: 
 Deprecated properties have been added to OpenAiChatProperties to maintain backward compatibility with the previous AbstractOpenAiOptions extension. Users should migrate to the new configuration approach. f271fdc 
 Setter methods have been removed from PostgresML embedding options and Stability AI image options classes, as well as from common ChatOptions (internalToolExecutionEnabled, outputSchema). These options should now be configured through the builder pattern or constructors. Affected: PostgresMlEmbeddingOptions, StabilityAiImageOptions, and common ChatOptions. a0ad1c7 , 741a6cc , #5957 
 Two vector store integrations (SAP HANA DB and Infinispan) have been removed from the Spring AI project. Users of these modules should plan migration to supported vector store alternatives. 35b659e 
 Continued polish of null-safety annotations across the codebase using the JSpecify standard, improving IDE support and static analysis for nullability. 65f9c67 
 The AssistantMessage builder has been refactored to properly support inheritance, enabling subclasses to extend the builder fluently. 2622d03 
 OpenAI Java SDK is updated to 4.34.0 
 Anthropic Java SDK is updated to 2.30.0 
 ⚠️ Breaking Changes: 
 PromptChatMemoryAdvisor has been removed. Chat memory advisors now require an explicit conversation ID to be provided, improving predictability and eliminating ambiguous implicit state management. Applications using PromptChatMemoryAdvisor or relying on implicit conversation IDs must be updated. c3c7c86 , 
 The class OpenAiConnectionProperties has been renamed to OpenAiCommonProperties to better reflect its purpose as shared configuration across OpenAI integrations. 
 OpenAI properties classes (e.g., OpenAiChatProperties, OpenAiEmbeddingProperties) no longer extend AbstractOpenAiOptions. This changes the class hierarchy and may affect code that relied on the options being available directly on properties classes. 
 Key Improvements: 
 Enhanced functionality with 18 improvements 
 Documentation updates with 30 improvements 
 Updated dependencies for better security and performance 
 View complete release notes → 
 🙏 Contributors 
 Thanks to all contributors who made these releases possible: 
 Arpan Chakraborty (@ArpanC6) 
 chabinhwang (@chabinhwang) 
 Eddú Meléndez (@eddumelendez) 
 Emile Plas (@emileplas) 
 Eric Bottard (@ericbottard) 
 Ilayaperumal Gopinathan (@ilayaperumalg) 
 Daniel Garnier-Moiroux (@Kehrlann) 
 KoreaNirsa (@KoreaNirsa) 
 Nicolas Krier (@nicolaskrier) 
 Sébastien Deleuze (@sdeleuze) 
 Soby Chacko (@sobychacko) 
 Thomas Vitale (@ThomasVitale) 
 Christian Tzolov (@tzolov) 
 Yaner (@yaner-here) 
 What's Next 
 The Spring AI team continues to focus on improving AI application development with Spring Boot. Based on the momentum from these releases, upcoming versions will build on these foundations with enhanced capabilities and developer experience improvements. 
 For the latest updates and to contribute to the project, visit our GitHub repository or join the discussion in our community channels. 
 Resources 
 Project Page | GitHub | Issues | Stack Overflow 
 Documentation: 1.0.7 Docs | 1.1.6 Docs | 2.0.0-M6 Docs
```

---

## 2. A Bootiful Podcast: Daniel Garnier-Moiroux on his new book 'Testing Spring Boot Applications'

- 日期: 2026-05-07 00:00
- 链接: https://spring.io/blog/2026/05/07/a-bootiful-podcast-daniel-garnier-moiroux

```
Get ahead
VMware offers training and certification to turbo-charge your progress.
Learn moreHi Spring fans! In this installment I'm thrilled to have had the opportunity to sit down and talk to Daniel Garnier-Moiroux and talk about "Testing Spring Boot Applications," from Manning!
#testing #springboot #java #kotlin #springframework
```

---

## 3. This Week in Spring - May 5th, 2026

- 日期: 2026-05-05 00:00
- 链接: https://spring.io/blog/2026/05/05/this-week-in-spring-may-05-2026

```
Hi, Spring fans! Welcome to another installment of This Week in Spring ! It's May 5th, 2026, and I'm in Mainz, Germany, for the legendary JAX conference! It's been infinitely far too long since I've been at this amazing show, and I'm oh-so happy to be back here! Tonight, after my two talks here, I'm off to London, UK, for the equally amazing Devoxx UK show! It's bound to be a ton of fun! 
 In last week's installment of A Bootiful Podcast , I talked to Ronald Dehuysser about his group's new JobRunr-powered OpenClaw-like thing. 
 Have you seen that we have a handy new Releases section on the blog? There, you can find quick and to-the-point information about all the new Spring project releases. There are incalculable many! Speaking of, here are some you might've missed from two weeks ago! 
 Spring AI 1.0.6, 1.1.5, 2.0.0-M5 are available now 
 Spring Shell 4.0.2 is out , including renewed support for compiling Spring Shell applications, powered by the Spring component model, into GraalVM native images! 
 Spring Modulith 2.1 RC1, 2.0.6, and 1.4.11 released 
 Spring Boot 4.1.0 RC1 available now 
 Spring Boot 4.0.6 available now 
 Spring Boot 3.5.14 available now 
 Spring Authorization Server 1.5.7 available now 
 Spring for Apache Pulsar 1.2.17 and 2.0.5 are available now 
 Spring for Apache Kafka 4.1.0 RC1, 4.0.5, and 3.3.15 available now 
 Spring AI Recipe: building a graph-based agentic workflow 
 This is a nice look at database locks and ways to optimize them with HikariCP 
 This third-party event sourcing library looks interesting, and seems to offer a nice integration with Spring Boot 
 A nice discussion around the place of LLMs in a Java architecture 
 A nice article looking at the power of the new @Retryable support in Spring Framework 7 and Spring Boot 4
```

---

## 4. Spring Office Hours Podcast: S5E14 - Spec Driven Development with Simon Martinelli

- 日期: 2026-05-04 00:00
- 链接: https://spring.io/blog/2026/05/04/spring-office-hours-podcast-S5E14

```
Join Dan Vega and DaShaun Carter for the latest updates from the Spring Ecosystem. In this episode, Dan and DaShaun are joined by Java Champion, Vaadin Champion, and Oracle ACE Pro Simon Martinelli to talk about Spec-Driven Development. With AI reshaping how we write code, Simon makes the case that requirements, not code, should be the single source of truth. We will explore what Spec-Driven Development looks like in practice, how it fits into a Java and Spring workflow, and how teams can use it to move from use case to running code with AI in the loop. You can participate in our live stream to ask questions or catch the replay on your preferred podcast platform. 
 Show Notes 
 Simon Martinelli on LinkedIn 
 Simon Martinelli on X 
 Spec-Driven Development: How AI Changed Everything (And Nothing) by Simon Martinelli at Spring I/O 2026
```

---
