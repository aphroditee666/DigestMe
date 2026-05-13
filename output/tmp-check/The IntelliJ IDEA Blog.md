# The IntelliJ IDEA Blog

> 分类: 大厂技术博客
> URL: http://blogs.jetbrains.com/idea/feed/
> 抓取: 12 篇

---

## 1. IntelliJ IDEA 2025.3.5 is Out!

- 日期: 2026-05-06 17:11
- 链接: https://blog.jetbrains.com/idea/2026/05/intellij-idea-2025-3-5/

```
We’ve just released IntelliJ IDEA 2025.3.5. This version includes performance improvements for Spring projects – specifically for users who haven’t yet updated to v2026.1: 
 Searches for declared Spring beans are no longer triggered during typing or completion, ensuring code completion works smoothly in Spring-based projects. [ IDEA-378966 ] 
 You can update to this version from inside the IDE, using the Toolbox App , or using snaps if you are a Ubuntu user. You can also download it from our website . 
 For a comprehensive overview of the fixes, see the release notes . If you spot any issues, let us know via the issue tracker . 
 Happy developing!
```

---

## 2. Java Annotated Monthly – May 2026

- 日期: 2026-05-05 12:33
- 链接: https://blog.jetbrains.com/idea/2026/05/java-annotated-monthly-may-2026/

```
April flew by. The pace of tech development didn’t slow, and the flow of news and knowledge didn’t either. 
 This month, Emily Bache joins us to share some sharp finds about AI agents and test-driven development. Java stays busy with fresh updates and practical tips, and Kotlin keeps pushing forward right next to it. The AI section is, as usual, packed with things worth your attention. 
 You’ll also find upcoming events to plan for and a few ideas to challenge your thinking. 
 Featured Content 
 Emily Bache 
 Emily Bache is an independent consultant, YouTuber, author, and Technical Coach, with over 25 years of experience working with Java and other programming languages and tools. She works with developers, training and coaching effective agile practices like refactoring and test-driven development. Emily has written two books about software development and contributed to several others. Emily founded the Samman Technical Coaching Society in order to promote technical excellence and support coaches everywhere. 
 It’s my pleasure to bring to your attention some interesting content that appeared in April. The huge change that is sweeping through our industry right now is the adoption of AI coding agents, which many people are using instead of hand-coding changes to software. One of the most important new skills to master is designing a “harness” for your AI tool, and this month Birgitta Böckeler has published the best reference I’ve seen so far about what that is and a mental model for how to think about it. Chris Parsons has also published an extensive guide titled How I use AI to Code , which is a really great resource for experienced developers looking to create their own harness and mentor others to do the same. 
 Perhaps as a contrast, I’d also like to highlight Michael Taggart’s introspective experience report on his use of AI. He wrestles with his conscience over using these tools at all. An interesting metaphor for AI-assisted coding came up in an article by Drew Breunig – we run the risk of building a Winchester Mystery House . After you read that, listen to Kevlin Henney’s talk Being the Human in the Loop , where he takes a look at the engineering skills we still need – ones that could perhaps prevent the kind of thing Drew writes about from happening. 
 I have a particular interest in test-driven development, which, as a technical coach, is a big part of what I teach to others. I wrote an initial assessment of what TDD looks like these days , based on interviews with several practitioners I trust who are all using agentic AI. For those of you who’d like to see me in action writing code,  I have a demo of a narrow integration test for an outbound port in a hexagonal architecture , in Kotlin. 
 Java News 
 Catch what shipped and track what’s next: 
 Java News Roundup 1 , 2 , 3 , 4 
 Newsletter: Java 26 Is Now Available | JDK 27 Heads-Ups 
 Quality Outreach Heads-up – JDK 27: Obsolete Translation Resources Removed 
 Update Your JDK, Read More Code, and Talk to Your Users: Interviews From VoxxedDays Amsterdam (#93) 
 Java Tutorials and Tips 
 Steal these tricks: 
 Analysing Crashed JVMs – Inside Java Newscast #109 
 Oracle’s Java Verified Portfolio and JavaFX: What It Actually Means 
 10 Things I Hate About Java by Adele Carpenter 
 Is AI Ruining Java Open Source? – Andres Almiray | The Marco Show 
 Java 26: Updates You Must Know 
 Java and Gen AI: JVM Agents With Embabel by Rod Johnson (Spring Creator) 
 A Bootiful Podcast: Java Developer Advocate Ana-Maria Mihalceanu 
 Does Java Really Use Too Much Memory? Let’s Look at the Facts (JEPs) 
 Thread-Safe Native Memory in Java: VarHandle Access Modes Explained 
 Episode 54 “How JDK 26 Improves G1’s Throughput” [AtA] 
 You Must Avoid Final Field Mutation – Inside Java Newscast #110 
 How the JVM Optimizes Generic Code 
 The Curious Case of Enum and Map Serialization 
 Avoiding Final Field Mutation 
 Kotlin Corner 
 Kotlin kontra Java – Part 1 – Ecosystem 
 Kotlin Professional Certificate by JetBrains – Now on LinkedIn Learning 
 Introducing Koog Integration for Spring AI: Smarter Orchestration for Your Agents 
 Reliable AI Agents Using Domain Modeling With Koog in Java 
 AI 
 Cut the hype, test the tools, and boost your flow: 
 How We Built a Java AI Agent by Connecting the Dots the Ecosystem Already Had 
 Stateful Continuation for AI Agents: Why Transport Layers Now Matter 
 A Bootiful Podcast: Mark Kropf on AI Orchestration 
 Embabel Tools & MCP Servers: Supercharge Your Java AI Agents 
 Adversarial AI: Understanding the Threats to Modern AI Systems 
 Why Java Developers Over-Trust AI Dependency Suggestions 
 A GitHub Agentic Workflow 
 ACP Java SDK: Building IDE Agents in Java 
 Spring AI Agentic Patterns (Part 7): Session API – Event-Sourced Short-Term Memory with Context Compaction 
 Beyond RAG: Architecting Context-Aware AI Systems With Spring Boot 
 Spring AI Agentic Patterns (Part 6): AutoMemoryTools – Persistent Agent Memory Across Sessions 
 5 Best Practices for Working with AI Agents, Subagents, Skills, and MCP 
 Deepfakes, Disinformation, and AI Content Are Taking Over the Internet 
 MCP in the Java World: Bringing Architectural Strategy to LLM Integrations 
 Languages, Frameworks, Libraries, and Technologies 
 Explore new tools and technologies, and revisit the old ones: 
 This Week in Spring 1 , 2 , 3 , 4 
 Article: Beyond RAG: Architecting Context-Aware AI Systems With Spring Boot 
 Six and a Half Ridiculous Things to Do With Quarkus 
 The Spring Team on Spring Framework 7 and Spring Boot 4 
 A Bootiful Podcast: The Legendary Craig Walls 
 Enabling Reflection-Free Jackson Serializers by Default 
 Understanding Performance 
 A Bootiful Podcast: A Bootiful Podcast: Dr. Venkat Subramaniam and James Ward on Intelligent Kotlin and So Much More 
 The Road to Docker Official Images for Java: The Azul Zulu Story 
 Spring Debugger New Power: Where Should I Click to Demystify Spring Boot Magic? 
 Conferences and Events 
 Join the crowd online or offline: 
 JAX – Mainz, Germany or Online, May 4–8 
 Devoxx UK – London, United Kingdom, May 6–7; JetBrains will have a booth at the event. Also, come and listen to our JetBrains speakers: Marit van Dijk , Cheuk Ting Ho , and Simon Vergauwen . The Spring documentary will premiere there, followed by a panel with Josh Long , Steve Poole , and Marit van Dijk . 
 GeeCon – Kraków, Poland, May 14–15; Marit van Dijk is speaking and moderating a panel on Java to discuss what excites each of them most about Java in 2026. 
 JAlba – Edinburgh, Scotland, May 14–16 
 JNation Conference – Coimbra, Portugal, May 26–27; Anton Arhipov and Marit van Dijk from JetBrains are the speakers. 
 JCON Slovenia – Portorož, Slovenia, May 27–29 
 Culture and Community 
 Where do you stand on these topics? 
 Panel: Building a Culture That Works 
 How to Do What You Love and Make Good Money 
 Do Things That Don’t Scale 
 Encoding Team Standards 
 Beyond the Hype: Is AI Taking the Fun out of Software Development? 
 And Finally… 
 One last thing before you close the article. Don’t skip it! 
 Using Spring Data JPA With Kotlin 
 Using Spring Data JDBC With Kotlin 
 Speeding up Interactive Rebase in JetBrains IDEs 
 From Java to Wayland: A Pixel’s Journey 
 That’s it for today! We’re always collecting ideas for the next Java Annotated Monthly – send us your suggestions via email or X by May 20. And don’t forget to check out our archive of past JAM issues for any articles you might have missed!
```

---

## 3. Teaching an AI Agent to Debug Flaky Tests

- 日期: 2026-05-04 09:14
- 链接: https://blog.jetbrains.com/idea/2026/05/teaching-an-ai-agent-to-debug-flaky-tests/

```
If you’ve been connected to the internet for a while, you’ve surely heard of AI Agent Skills . They teach your agent to do this and that. You might have even used or written a couple of them yourself. 
 If you aren’t yet familiar with them, the idea is simple: Instead of prompting instructions for a specific task each time, you define them once and reuse them later. A Skill is an AI equivalent of a knowledge base article: a plain text document that lives in a discoverable location and describes steps, a set of conventions, or domain-specific knowledge. 
 Most Skills you see in the wild are for simple things like enforcing code style or commit message conventions. But they can be much more powerful than that. In this article, we’ll combine AI Skills, good old developer tools, and a bit of creative thinking to address a notoriously challenging task: making AI deterministically find the root cause of flaky tests. 
 The problem 
 Quoting the TeamCity CI/CD guide : 
 Flaky tests are defined as tests that return both passes and failures despite no changes to the code or the test itself. 
 Flakiness undermines the whole point of tests: When a test fails, you can’t tell whether something is actually broken. You can’t fully rely on the test results, and at the same time, you can’t ignore them. This wastes both human and infrastructure resources. 
 And as if the underlying bugs weren’t difficult enough on their own, flaky tests often have this property of failing once in several thousand runs, making them extremely hard to reproduce and debug. 
 Example project 
 For the example project, let’s take the webshop demo from this article: Your Programs Are Not Single-Threaded . It is a Spring Boot project, in which one of the services has a TOCTOU (time-of-check to time-of-use) problem: It checks a condition and then acts on it, but another thread can change the state in between. In this particular case, it may sometimes cause duplicate invoice numbers and also makes the corresponding test flaky. 
 Here’s the problematic test: 
 @SpringBootTest
class InvoiceServiceTest {

 @Autowired
 private OrderService orderService;

 @Test
 void firstTwoOrdersGetInvoiceNumbersOneAndTwo() {
 CompletableFuture<Invoice> alice = CompletableFuture.supplyAsync(
 () -> orderService.checkout("Alice", BigDecimal.TEN));
 CompletableFuture<Invoice> bob = CompletableFuture.supplyAsync(
 () -> orderService.checkout("Bob", BigDecimal.TEN));

 String num1 = alice.join().getInvoiceNumber();
 String num2 = bob.join().getInvoiceNumber();

 assertEquals(Set.of("INV-00001", "INV-00002"), Set.of(num1, num2));
 }
} The test creates two orders concurrently and checks that the resulting invoices get numbers INV-00001 and INV-00002 . Because of a bug in InvoiceService , it can either pass or fail randomly. 
 Note: If you’re using IntelliJ IDEA, you can test whether a test is actually flaky by using the Run until failure option in the test runner. Leave the suspect spinning for some time and see if it eventually fails. 
 If we knew nothing about the underlying bug, and only had the test, is there a tool that could help us find the root cause? Or can we make one ourselves? Furthermore, could we delegate both building and using the tool to AI? 
 The intuition 
 Let’s come up with some intuition for this class of problem. 
 To produce two kinds of results, the execution must follow different code paths. The difference might be minimal, possibly just one extra method call or one if branch taken instead of another. But it has to be there; otherwise, the result would be consistent. So, if we could record the code path for a passing run and a failing run and then compare them, the diff should at least point us in the right direction. And ideally, by following the call tree, we could find the place where execution splits. This line must be exactly where the flakiness originates. 
 Does this reasoning make sense? Let’s put it to the test. 
 Build the tools 
 What tool can we use for recording code paths? While not designed specifically for tracing, a test coverage tool can give us the information we’re after. 
 There are a couple of Java coverage tools to choose from, such as JaCoCo and IntelliJ IDEA’s coverage tool . We’ll go with IntelliJ IDEA’s, because it includes a hit counting feature that is very useful. We may need this extra granularity because the flakiness might stem not only from what is executed, but also how many times . 
 Run coverage from the command line 
 IntelliJ IDEA’s coverage tool has a familiar UI, but we need a way to launch it programmatically. Fortunately, coverage can also be collected from the command line by attaching the coverage agent to the JVM via Maven Surefire : 
 mvn surefire:test \
 -Dtest=com.example.webshop.service.InvoiceServiceTest \
 "-DargLine=-Didea.coverage.calculate.hits=true \
 -javaagent:\$AGENT_JAR=\$IC_FILE,true,false,false,true,com.example.webshop.*" The -Didea.coverage.calculate.hits=true flag tells the agent to record invocation counts per line rather than just a boolean hit/not-hit mask. After the test finishes, the results are written to a binary .ic file. 
 So far so good, but we need the report in a human (and AI)-readable format. 
 Add text output 
 Luckily, the IntelliJ coverage agent is open-source. Let’s clone the project and ask AI to add a text reporter that converts binary reports to plain text. 
 The agent creates a new class called TextCoverageStatistics . After we build the project and run the reporter against our .ic file, we get something like this: 
 === Coverage Summary ===

 Instructions: 236/618 38,2%
 Branches : 0/20 0,0%
 Lines : 56/150 37,3%
 ...

=== Per-Class Coverage ===

Class Lines Line% Methods Meth%
--------------------------------------------------------------------------------------------
...
com.example.webshop.service.InvoiceNumberGenerator 4/4 100,0% 2/2 100,0%
com.example.webshop.service.InvoiceService 10/10 100,0% 3/3 100,0%
com.example.webshop.service.OrderService 6/6 100,0% 2/2 100,0%
... The first part of the report gives a high-level overview: How many lines, branches, and methods were covered across the entire project. Below that, there’s a per-class breakdown showing the same metrics for each class individually. 
 Then it is followed by per-line hit counts for each class: 
 --- com.example.webshop.service.InvoiceService ---
 Line Hits Branch
 19 2
 20 1
 22 2
 23 2
 24 2
 ... For every line that the coverage agent instrumented, we see how many times it was executed and whether any branches were taken. The actual report is longer, but you get the idea. Now we have a text representation of which lines were executed, and exactly how many times. 
 This is the raw material we need for the diff. So far, so good! 
 Diff the reports 
 Supposedly, the obtained reports contain the necessary information, and a very determined developer could peruse them and find the bug. But we’re not here for mundane tasks like that, right? 
 Let’s upgrade the tool so that it gets multiple report variations and presents the diff. The most controllable way would be to do one “brick” at a time, but I think we’re safe to delegate the entire thing to AI here, including the automation: 
 The resulting script runs the test in a loop until both of the following happen: 
 We get at least one passing and one failing run. 
 The specified number of runs have passed. 
 Both conditions are important because test failures can be very rare, and the specified number of runs might not be enough. At the same time, there can be finer grained variations within pass and fail runs, so we might want to catch those too. 
 After the reports are collected, the script summarizes the lines that have variations between the runs. Here’s what it looks like: 
 Collected 20 runs: 12 pass, 8 fail

Lines that vary across runs:

 Invoice:29 Hits(1,2)
 Invoice:31 Hits(1,2)
 Invoice:32 Hits(1,2)
 InvoiceNumberGenerator:15 Hits(1,2)
 InvoiceService:19 Hits(1,2) Branch(1/2)
 InvoiceService:20 Hits(1,2)
 InvoiceService:22 Hits(1,2)
 InvoiceService:24 Hits(1,2) All variations have the same pattern: the difference is not which lines were executed, but how many times . As we expected, the hit counting feature of IntelliJ IDEA’s coverage agent proved useful! 
 The varying lines point at a lazy initialization block in InvoiceService and its downstream effects in InvoiceNumberGenerator and Invoice . The variation in hit counts means that the initialization sometimes runs more than once, which shouldn’t happen. That’s exactly where the flakiness comes from. 
 If you missed the article that describes the problem, here’s why double initialization causes this bug. The createGenerator() method queries the database for the last used invoice number and creates a counter starting from that value. When two threads both enter the if (generator == null) block before either finishes, each reads the same number from the database and creates its own generator starting from the same value. The result is duplicate invoice numbers. 
 The coverage diff has pointed us at the very same TOCTOU race discussed in more detail in the previous article. But, what is novel in our current approach is that it doesn’t solely rely on human expertise and is easily accessible for AI. 
 Turning it into a Skill 
 Now, I’d say that AI-assisted modifications to open-source tools that help you solve the task at hand, all within minutes, are amazing on their own. But let’s keep our eyes on the bigger picture. 
 Here’s what we’ve done so far: We started with an intuition: Flaky tests take different code paths, and coverage analysis can reveal where they diverge. Then we turned that intuition into a concrete, repeatable procedure. Does this warrant a knowledge base article, or an AI Agent Skill, perhaps? Yes! 
 In the same agent session, let’s ask the agent to: 
 Make sure all the scripts are self-contained and runnable. 
 Document the entire procedure in a SKILL.md file, step by step, so that another agent can follow it without any prior context. 
 The agent packages everything and writes a guide that describes when to apply the Skill, what tools are needed, and what steps to follow. The only follow-up during review was to align the Skill with the specification . The original Skill written by the agent lacks meta in frontmatter. Agents are good at sorting out Skills that omit minor details, but meta is important for discoverability. Without it, a Skill might not be picked up by an agent in the first place. 
 Testing the Skill 
 To verify that the Skill actually works, let’s start a fresh agent session. No warm-up, no hints. Instead, let’s deliberately phrase it in a very general way, something like “find and fix the cause of flakiness in InvoiceServiceTest “. 
 The agent matches the Skill description from SKILL.md with the problem description, discovers the instructions, and executes them: It runs the coverage script, reads the diff, and identifies the race condition. Instead of guesswork, it follows the established steps and arrives at the same conclusion every time. That’s about as deterministic as generative AI can get! 
 Summary 
 The changes that we’ve made to the coverage agent are already published with the new version 1.0.774 . And the Skill is available here . 
 In this article, we started with an intuition about flaky tests, built custom tooling around an open-source coverage agent, used it to find a race condition, and packaged the entire procedure into a reusable AI Skill. You can use this Skill for finding flaky tests in your own projects, but I hope this post conveys the bigger idea. 
 AI Skills allow you to teach agents to solve virtually anything, as long as you can stack text interfaces together. Many hard programming problems can be broken down into simpler ones and solved using familiar tools. And with AI orchestrating all this, we can even make the process enjoyable. As was the case long before AI, curiosity is the only real prerequisite. 
 Have you been inspired to solve a tough problem in your own work? Would you like to share the Skills you wrote or find most useful? Let us know in the comments! 
 Happy debugging!
```

---

## 4. IntelliJ IDEA 2026.1.1 Is Out!

- 日期: 2026-04-23 13:04
- 链接: https://blog.jetbrains.com/idea/2026/04/intellij-idea-2026-1-1/

```
IntelliJ IDEA 2026.1.1 has arrived with several valuable fixes. 
 You can update to this version from inside the IDE, using the Toolbox App , or using snaps if you are a Ubuntu user. You can also download it from our website . 
 Here are the most notable updates included in this version: 
 It’s once again possible to set up a WSL Python SDK. [ IJPL-240728 ] 
 Emmet in remote development now works as expected. [ IJPL-168255 ] 
 Gradle sync no longer fails due to a class cast error involving InternalIdeaModule and org.gradle.tooling.model.ProjectModel . [ IDEA-386409 ] 
 The IDE now correctly connects to the WildFly admin process after server startup, restoring deployment and the Open browser after launch option. [ IDEA-387483 ] 
 The IDE no longer fails to locate the WSL 2 JDK. [ IJPL-222935 ] 
 Double-clicking an Ant target in the Ant tool window now runs the target and shows the build output in the Messages tool window. [ IDEA-387507 ] 
 Search for context actions and code completion in large Spring projects are now more responsive and faster. [ IDEA-378966 ] 
 The IDE now correctly supports creating a run configuration for a local WebLogic server. [IDEA-387617 ] 
 The Find and Replace action now works as expected when pressing Enter . [ IJPL-240373 ] 
 To find out more details about the issues resolved, please refer to the release notes . 
 If you encounter any bugs, please report them to our issue tracker . 
 Happy developing!
```

---

## 5. Using Spring Data JDBC With Kotlin

- 日期: 2026-04-09 11:46
- 链接: https://blog.jetbrains.com/idea/2026/04/using-spring-data-jdbc-with-kotlin/

```
This post was written together with Thorben Janssen , who has more than 20 years of experience with JPA and Hibernate and is the author of “Hibernate Tips: More than 70 Solutions to Common Hibernate Problems” and the JPA newsletter. 
 Spring Data JDBC provides a simple and predictable persistence model. It focuses on aggregate roots, constructor-based mapping, and clear rules for reading and writing data. If you enjoy working with explicit data flows and want full control over your SQL, Spring Data JDBC might be the perfect framework for your project. 
 And with Kotlin, everything becomes so much easier. Its focus on immutability, null safety, and concise data structures aligns nicely with Spring Data JDBC’s design. In this article, you will see how to model aggregates, store and retrieve data, use value objects, handle child entities, and define custom queries using Kotlin. 
 Kotlin’s strengths for JDBC-based persistence 
 Before looking at concrete examples, it helps to understand why Kotlin fits so well into this programming model. 
 Data classes keep your aggregates concise. They define constructor parameters, implement the equals() , hashCode() , and toString() methods, and encourage immutable states. Spring Data JDBC provides strong support for constructor-based mapping and handles immutable aggregates with ease, significantly reducing boilerplate code. 
 Kotlin’s type system also reduces many common mistakes. Nullability is explicit, so you can see immediately which fields may not contain a value. Constructor-based mapping becomes more reliable because there is no silent conversion of null values into empty strings or default primitives. 
 Lightweight value classes allow you to express domain concepts without adding noise. An email address, a customer number, or a price becomes a first-class concept in your model. And Spring Data JDBC can, of course, map them without requiring any additional boilerplate code or mapping annotations. 
 Kotlin also simplifies custom query projections, because data classes work very well with constructor mapping. Default parameters, named arguments, and collection operations make aggregate updates straightforward. 
 All these features create a natural fit for Spring Data JDBC and Kotlin. 
 Defining an aggregate root with Kotlin 
 An aggregate is a pattern introduced by domain-driven design (DDD) concepts. It consists of one or more entities that are handled as a unit when reading or writing them to the database. The aggregate root is the primary object of the aggregate. You address it when referencing the aggregate or when fetching it from the database. 
 Let’s start with a simple aggregate that only consists of the aggregate root. Each instance is stored as a record in your database whenever you decide to persist or update it. There is no hidden state and no proxying. 
 The following data class represents a person. The @Table annotation is optional, but it clearly marks the class as an entity. This helps IntelliJ IDEA to provide you with the most suitable tooling when building your persistence layer. 
 The @Id annotation marks the field as the object’s identifier. The @Sequence annotation is optional and tells Spring Data to retrieve a value from the database sequence when persisting a new object. And because this happens after you created a new Person object in your code, the ID field has to be nullable. 
 If you want, you can define all other fields as non-nullable. 
 @Table
data class Person(
 @Id
 @Sequence(sequence = "person_seq")
 val id: Long? = null,
 val firstName: String,
 val lastName: String
) As you can see in the code snippet, you don’t need to provide any additional mapping annotations. By default, Spring Data JDBC maps the class to a database table with the same name and each field to a column with the same name. You can change this mapping by annotating your class with @Table and a field with @Column . But most teams try to avoid that to keep their entities easy to read and understand. 
 By default, Spring Data JDBC uses the primary constructor to create and hydrate entity instances. You can also annotate a constructor with @PersistenceCreator if you want Spring Data JDBC to use it instead. This is an excellent match for Kotlin’s data classes, because all non-primary-key fields can be immutable, mandatory, and have default values. This helps you avoid uninitialized properties and the need for no-argument constructors that you might be familiar with in Spring Data JPA and other persistence frameworks. 
 After you define the aggregate, you have to create a repository to manage it. 
 Creating repositories and defining queries 
 Spring Data JDBC uses repository interfaces to define data access operations. The simplest way to define a repository is to extend Spring Data JDBC’s CrudRepository . 
 interface PersonRepository : CrudRepository<Person, Long> {} This provides you with basic methods, including save() , findById() , and deleteById() . 
 You can also add your own queries using Spring Data JDBC’s derived query methods. These are methods whose names describe the query that Spring Data JDBC should execute. The framework parses the method name, creates the appropriate SQL statement, and maps the query result. 
 And if you need more control over the executed query statement, you can define a method, annotate it with @Query , and provide your own SQL statement. Spring Data JDBC handles the rest! 
 Here are a few examples. 
 interface PersonRepository : CrudRepository<Person, Long> {
 fun findByLastName(lastName: String): List<Person>

 @Query("select * from Person p where p.last_name = :lastName")
 fun getByLastName(lastName: String): List<Person>
} You can also return Kotlin data class projections. This works well when you want to read specific columns but not the entire aggregate, or when you want to transform your data into a different structure. 
 The following PersonName data class and findPersonNameById repository method show a typical example. 
 data class PersonName(
 val id: Long,
 val name: String
)

interface PersonRepository : CrudRepository<Person, Long> {
 @Query("select p.id, p.first_name || ' ' || p.last_name as name FROM Person p where p.id = :id")
 fun findPersonNameById(id: Long): PersonName
} Spring Data JDBC executes the defined query and maps the query result to the constructor parameters of the PersonName class. This keeps the projection code clean and allows you to avoid manual mapping. 
 2025-12-09T21:59:12.572+01:00 DEBUG 7484 --- [SDJWithKotlin] [ main] o.s.jdbc.core.JdbcTemplate : Executing prepared SQL statement [select p.id, p.first_name || ' ' || p.last_name as name FROM Person p where p.id = ?]
2025-12-09T21:59:12.595+01:00 INFO 7484 --- [SDJWithKotlin] [ main] c.t.j.k.s.SpringDataJdbcKotlinTests : PersonName(id=401, name=Jane Smith) Persisting and loading aggregates 
 Working with repositories is straightforward. Each call interacts directly with the database. There is no state tracking or implicit updates. This makes the behavior easy to understand and gives you full control over the executed statements. 
 @Service
@Transactional
class PersonService(private val personRepository: PersonRepository) {
 fun createNewPerson(firstName: String, lastName: String): Person {
 // add additional validations and/or logic ...
 return personRepository.save(
 Person(
 firstName = firstName,
 lastName = lastName
 )
 )
 }

 fun updateLastName(id: Long, lastName: String): Person {
 val person = personRepository.findById(id).orElseThrow()
 val updated = person.copy(lastName = lastName)
 return personRepository.save(updated)
 }
} The only logic Spring Data JDBC provides when you call the save() method is a check to see if the identifier is null . If it is, the record is inserted. Otherwise, an update is executed. Since all fields are immutable, you’re always working with complete and consistent objects. 
 Using Kotlin value objects in your aggregate 
 Real-world aggregates often contain values that deserve their own type. Using Kotlin, you can model them using value classes, and Spring Data JDBC supports them out of the box. 
 If your value class only wraps one value, you should annotate it with @JvmInline . This activates a Kotlin-specific optimization removing the performance overhead of a wrapper class by replacing it with its inlined value at runtime. 
 @JvmInline
value class Email(val value: String)

data class Person(
 @Id
 @Sequence(sequence = "person_seq")
 val id: Long? = null,
 val firstName: String,
 val lastName: String,
 val email: Email
) As you can see, Kotlin’s value and data classes make the code very easy to read and quick to write. 
 Doing the same in Java requires much more code, an additional mapping annotation and Spring Data JDBC’s embedded entity concept. 
 @Table
public class Person {

 @Id
 @Sequence(sequence = "person_seq")
 private Long id;

 private String firstName;

 private String lastName;

 @Embedded.Nullable
 private Email email;

 public Long getId() {
 return id;
 }

 public void setId(Long id) {
 this.id = id;
 }

 public String getFirstName() {
 return firstName;
 }

 public void setFirstName(String firstName) {
 this.firstName = firstName;
 }

 public String getLastName() {
 return lastName;
 }

 public void setLastName(String lastName) {
 this.lastName = lastName;
 }

 public Email getEmail() {
 return email;
 }

 public void setEmail(Email email) {
 this.email = email;
 }
}

public class Email {

 private String email;

 public Email(String email) {
 this.email = email;
 }

 public String getEmail() {
 return email;
 }

 public void setEmail(String email) {
 this.email = email;
 }
} Java doesn’t know value classes. Spring Data JDBC tries to compensate for this by introducing the concept of an embedded entity . 
 You define an embedded entity by creating a Java class with a set of properties. In this example, that’s the Email class with its email property. To use the Email class as a property type, you have to annotate it with @Embedded . Spring Data JDBC then applies the same mapping we covered in the example demonstrating Kotlin’s value class. It maps the email field to a database column with the same name, enabling you to use it in all your queries. 
 So, it looks like you have to write more code and use an embedded entity in Java to get the same result as you got with a simple value class in Kotlin. But it’s actually worse than that. In Kotlin, you can annotate your simple value classes with @JvmInline and get the previously described optimizations. These don’t exist in Java. As a result, your embedded class mapping not only requires more code – it also carries a much greater performance overhead. 
 Now, let’s get back to our Kotlin-based examples. 
 Spring Data JDBC maps the value object based on its wrapped value and doesn’t require any additional mapping annotations. 
 You can even use the value class as a parameter type in your derived or custom queries. 
 interface PersonRepository : CrudRepository<Person, Long> {
 fun findByEmail(email: Email): Person?
} 2025-12-09T22:03:49.340+01:00 DEBUG 14665 --- [SDJWithKotlin] [           main] o.s.jdbc.core.JdbcTemplate               : Executing prepared SQL statement [SELECT "person"."id" AS "id", "person"."email" AS "email", "person"."last_name" AS "last_name", "person"."first_name" AS "first_name" FROM "person" WHERE "person"."email" = ?]
2025-12-09T22:03:49.363+01:00  INFO 14665 --- [SDJWithKotlin] [           main] c.t.j.k.s.SpringDataJdbcKotlinTests      : Person(id=401, firstName=Jane, lastName=Smith, email=Email(value=a@b.com)) Modeling one-to-many relationships 
 Aggregates can contain collections of child entities. Spring Data JDBC stores each of these entity types in separate tables. 
 data class Company(
 @Id
 var id: Long,
 val name: String,
 val employees: List<Employee>
)

data class Employee(
 @Id
 var id: Long,
 var name: String
) When you read the aggregate, Spring Data JDBC always fetches the entire aggregate with all child entities. And it handles all write operations the same way. When persisting or updating an aggregate, it writes the entire aggregate with all its entities to the database. This fits well with Kotlin’s immutable list types, but requires some attention when defining your aggregates to avoid performance issues. 
 Transactions and practical considerations 
 Spring Data JDBC integrates with Spring’s transaction management. A transactional boundary ensures that all write operations within the aggregate are applied consistently. 
 Kotlin reduces many typical pitfalls. Properties must be initialized, nullability is clear, and immutable data helps avoid accidental side effects. When updating an aggregate, you create a new instance with the correct state as opposed to modifying an existing one. This results in a predictable and maintainable persistence layer. 
 Conclusion 
 Spring Data JDBC offers a clear and simple approach to relational persistence. You work with aggregates that are written and read as complete units, and you always know which statements are executed. Kotlin supports this style through immutable data structures, value classes, nullability rules, and concise syntax. 
 If you design your aggregates carefully and treat each instance as a complete snapshot of its state, you can build applications that remain easy to understand and maintain. The combination of Spring Data JDBC and Kotlin gives you a persistence stack that stays simple even as your application grows. 
 To learn more about persistence with Kotlin, check out our two previous articles in this series: 
 How to Avoid Common Pitfalls with JPA and Kotlin 
 Using Spring Data JPA with Kotlin 
 About the author 
 Thorben Janssen 
 Thorben Janssen is a consultant and trainer who helps teams build better persistence layers with JPA and Hibernate. An international speaker with more than 20 years of experience in JPA and Hibernate, Thorben is the author of the best-selling book Hibernate Tips: More than 70 solutions to common Hibernate problems . 
 He also writes on thorben-janssen.com about various persistence topics, and to help developers improve their skills, he founded the Persistence Hub.
```

---

## 6. Java Annotated Monthly – April 2026

- 日期: 2026-04-06 11:10
- 链接: https://blog.jetbrains.com/idea/2026/04/java-annotated-monthly-april-2026/

```
It’s safe to say March was defined by one thing: Java 26. In this issue of Java Annotated Monthly, we’ve curated a rich selection of articles to help you get the full picture of the release. Marit van Dijk joins us as the featured guest author, bringing her expertise to help you navigate the changes with confidence. Alongside our Java 26 coverage, you’ll find our regular roundup of AI developments, Spring updates, Kotlin news, industry trends, and community reads that caught our eye. 
 Featured Content 
 Marit van Dijk 
 Marit van Dijk is a Java Champion and Developer Advocate at JetBrains with over 20 years of software development experience. She’s passionate about building great software with great people, and making developers’ lives easier. 
 Marit regularly presents at international conferences and shares her expertise through webinars, podcasts, blog posts, videos, and tutorials. She’s also a contributor to the book 97 Things Every Java Programmer Should Know (O’Reilly Media). 
 March held a lot of interesting things for Java. First of all, there was the Java 26 release on March 17. You can read all about Java 26 in IntelliJ IDEA on the blog, and find more links on Java 26 in the Java sections below. 
 Also in March, JavaOne took place in Redwood Shores, USA. During the community keynote, our colleague Anton Arhipov talked about 25 years of IntelliJ IDEA . In case you missed it, we also did a Duke’s Corner podcast and a Foojay podcast on the same topic. And of course, the IntelliJ IDEA documentary was released this month. Also at JavaOne, we announced that Koog is coming to Java , if you want to try JetBrains’ Koog AI agent with Java instead of Kotlin. 
 IntelliJ IDEA 2026.1 was just released. Of course we have Java 26 support from day one, as well as improvements to the debugger for virtual threads, support for new Kotlin features, Spring Data and Spring Debugger features, new AI features, and more. You can read all about it on the blog or watch our release video . 
 The release of Java 26 also means that Piotr Przybył and I updated our talk, Learning modern Java the playful way , for Java 26. You can watch the recording from Voxxed Days Amsterdam , or catch us at multiple events around Europe. 
 Java News 
 Check out all the Java news highlights in March: 
 Java News Roundup 1 , 2 , 3 , 4 , 5 
 Java 26: What’s New? 
 HTTP Client Updates in Java 26 
 Java Performance Update: From JDK 21 to JDK 25 
 Quality Outreach Heads-up – JDK 27: Removal of ‘java.locale.useOldISOCodes’ System Property 
 Episode 51 “Unboxing Java 26 for Developers” 
 Java 27 – Better Language, Better APIs, Better Runtime 
 Foojay Podcast #92: Java 26 Is Here: What’s New, What’s Gone, and Why It Matters in 2026 
 Java 26 in definitely UNDER 3 minutes 
 JDK 26 Security Enhancements 
 Java Tutorials and Tips 
 You can never have too many tips for getting more out of Java: 
 Java 26 for DevOps 
 Java 26 Is Here, And With It a Solid Foundation for the Future 
 Closed-world assumption in Java 
 JavaScript (No, Not That One): Modern Automation with Java 
 Redacting Sensitive Data from Java Flight Recorder Files 
 Foojay Podcast #91: 25 Years of IntelliJ IDEA: The IDE That Grew Up With Java 
 Vulnerable API usage: Is your Java code vulnerable? 
 Java 26 is boring, and that’s a good thing 
 Episode 49 “LazyConstants in JDK 26” 
 Empty Should be Empty 
 Testing Elasticsearch. It just got simpler 
 A Bootiful Podcast: Cay Horstmann, legendary Java professor, author, lecturer 
 Episode 50 “Towards Better Checked Exceptions” 
 How is Leyden improving Java Performance? 1, 2 , 3 
 Java Is Fast. Your Code Might Not Be. 
 Data Oriented Programming, Beyond Records 
 Evolving the Java Language: An Inside Perspective 
 Hybrid search with Java: LangChain4j Elasticsearch integration 
 Secure Coding Guidelines for Java 
 Estimating value of pi (π) using Monte Carlo Simulation and Vector API 
 Javable: generate Java-friendly wrappers for Kotlin with KSP 
 Kotlin Corner 
 Stay sharp with the latest Kotlin news and practical tips: 
 Kotlin 2.3.20 Released 
 Amper 0.10 – JDK Provisioning, a Maven Converter, Custom Compiler Plugins, and More 
 The klibs.io source repository was made public . 
 Building a Deep Research Agent with Koog — Teaching Your Agent to Think in Phases 
 Koog Comes to Java: The Enterprise AI Agent Framework From JetBrains 
 Introducing Tracy: The AI Observability Library for Kotlin 
 KotlinConf’26 Speakers: In Conversation with Josh Long 
 AI 
 Plenty of AI reads this month. Pick what catches your eye: 
 Intelligent JVM Monitoring: Combining JDK Flight Recorder with AI 
 AI coding skills from the engineers who build the JVM ecosystem 
 Vibe Coding, But Production-Ready: A Specs-Driven Feedback Loop for AI-Assisted Development 
 Busting AI Myths and Embracing Realities in Privacy & Security 
 Shaping Jakarta Agentic AI Together – Watch the Open Conversation 
 how i automated my life with mcp servers 
 10 things i hate about ai 
 Writing an agent skill 
 Hacking AI – How to Survive the AI Uprising 
 Stop Fighting Your AI: Engineering Prompts That Actually Work 
 Four Patterns of AI Native Development 
 Interactive Rubber Ducking with GenAI 
 The Oil and Water Moment in AI Architecture 
 Look Inside a Large Language Model to Become a Better Java Developer 
 A Senior Engineer Tries Vibe Coding 
 How We Built a Java AI Agent by Connecting the Dots the Ecosystem Already Had 
 Languages, Frameworks, Libraries, and Technologies 
 Spring updates and more tech news, all in one place: 
 This Week in Spring 1 , 2 , 3 , 4 
 Data Enrichment in MongoDB 
 Supercharge your JVM performance with Project Leyden and Spring Boot by Moritz Halbritter 
 A Typo Led to the Creation of Spring Cloud Contract • Marcin Grzejszczak & Jakub Pilimon • GOTO 2026 
 A Bootiful Podcast: Neo4j legend Jennifer Reif 
 A Bootiful Podcast: Spring Messaging Legend Soby Chacko 
 Blending Chat with Rich UIs with Spring AI and MCP Apps 
 Java Microservices(SCS) vs. Spring Modulith 
 Moving beyond Strings in Spring Data 
 Quarkus has great performance – and we have new evidence 
 Modeling One-to-Many Relationships in Java with MongoDB 
 Clean Architecture with Spring Boot and MongoDB 
 Conferences and Events 
 Pick your next events to attend: 
 Spring I/O – Barcelona, Spain, April 13–15; Come say hi at the JetBrains booth and join the community run ! 
 Java Day Istanbul – Istanbul, Türkiye, April 17–18; Anton Arhipov is a speaker. 
 JCON EUROPE – Cologne, Germany, April 20–23; Marit van Dijk will talk about learning modern Java the playful way. 
 Great International Developer Summit – Bengaluru, India, April 21–24; Join Siva Katamreddy’s talk on Spring AI + MCP. 
 Devoxx France – Paris, France, April 22–24; Check out the talks by Anton Arhipov and Marit van Dijk . 
 Devoxx Greece – Athens, Greece, April 23–25; Marit van Dijk is a speaker. 
 Voxxed Days Bucharest – Bucharest, Romania, April 28–29; And if you haven’t caught Marit van Dijk during this busy month of hers, here’s the last chance to hear her speak in April. 
 Culture and Community 
 Your go-to section to slow down and think about the industry, self-growth, and more: 
 Mindful Leadership in the Age of AI 
 Can we still make software that sparks joy? 
 Information Flow: The Hidden Driver of Engineering Culture 
 Beyond the Code: Hiring for Cultural Alignment 
 Build a Spaced Repetition Flashcard API with Spring Boot & MongoDB (Part 1) 
 Where Do Humans Fit in AI-Assisted Software Development? 
 Green IT: How to Reduce the Impact of AI on the Environment 
 Does Language Still Matter in the Age of AI? Yes — But the Tradeoff Has Changed 
 IntelliJ IDEA: The Documentary | An origin story 
 The Software Architect Elevator 
 And Finally… 
 Top picks from the IntelliJ IDEA blog: 
 What’s fixed in IntelliJ IDEA 2026.1 
 Java 26 in IntelliJ IDEA 
 IntelliJ IDEA’s New Kotlin Coroutine Inspections, Explained 
 Cursor Joined the ACP Registry and Is Now Live in Your JetBrains IDE 
 Sunsetting Code With Me 
 Koog Comes to Java: The Enterprise AI Agent Framework From JetBrains 
 AI-Assisted Java Application Development with Agent Skills 
 Core JavaScript and TypeScript Features Become Free in IntelliJ IDEA 
 That’s it for today! We’re always collecting ideas for the next Java Annotated Monthly – send us your suggestions via email or X by April 20. Don’t forget to check out our archive of past JAM issues for any articles you might have missed!
```

---

## 7. Using Spring Data JPA with Kotlin

- 日期: 2026-03-30 11:30
- 链接: https://blog.jetbrains.com/idea/2026/03/using-spring-data-jpa-with-kotlin/

```
This post was written together with Thorben Janssen , who has more than 20 years of experience with JPA and Hibernate and is the author of “Hibernate Tips: More than 70 Solutions to Common Hibernate Problems” and the JPA newsletter. 
 Spring Data JPA is based on the Jakarta Persistence specification and was originally designed for Java. That often raises the question of whether it is a good fit for Kotlin projects. 
 The short answer is yes! 
 You can use Spring Data JPA with Kotlin without any issues and enjoy Kotlin’s compact syntax and language features, like null safety and extension functions, when writing your business code. 
 And doing all of that is so quick and easy could explained in this short blog post. Let’s use Spring Data JPA with Kotlin to define and use a simple persistence layer. 
 Required dependencies 
 The easiest way to get started is to use the “New Project” wizard in IntelliJ. Once you select Kotlin and Spring Data JPA, the basic setup is done for you. That includes configuring the Kotlin no-arg and all-open plugins. They ensure that your Kotlin classes fulfill Jakarta Persistence’s requirements for non-final classes and parameterless constructors. You also get the kotlin-reflect dependency, which is required by Spring. 
 On the next page, you can select the Spring Boot Starter modules and other dependencies you want to use. In this example, that’s Spring Data JPA and the PostgreSQL database driver. 
 Adding Kotlin to an existing project 
 If you already have a Java-based Spring Boot project with the required dependencies, you can simply add a Kotlin class to it. Starting with version 2026.1 Intellij IDEA automatically adds the plugins plugin.spring and plugin.jpa to your build configuration and configure the all-open plugin. 
 In case you’re using an older IDEA version, you have to add the following configuration yourself. 
 plugins {
   kotlin("plugin.spring") version "2.2.20"
   kotlin("plugin.jpa") version "2.2.20"
}

allOpen {
   annotation("jakarta.persistence.Entity")
   annotation("jakarta.persistence.MappedSuperclass")
   annotation("jakarta.persistence.Embeddable")
} Database and logging configuration 
 After defining your project’s dependencies, you need to set up the database connection in your application.properties file, and you can provide your preferred logging configuration. 
 The following settings connect to a local PostgreSQL database and activate detailed Hibernate logging. The logging configuration instructs Hibernate to log the executed SQL statements and all bind parameter values. This information is extremely helpful during development and debugging, but it generates a lot of output. So, please make sure to use a different logging configuration in production. 
 spring.datasource.url=jdbc:postgresql://localhost:5432/postgres

spring.datasource.username=postgres
spring.datasource.password=postgres

logging.level.root=INFO
logging.level.org.hibernate.SQL=DEBUG
logging.level.org.hibernate.orm.jdbc.bind=TRACE Modelling entities 
 You can then start modeling your entities in Kotlin. The Jakarta Persistence specification defines a few requirements for entity classes. As we explained in a recent article on common best practices , some of these requirements don’t align well with Kotlin’s data classes. But you will not run into any issues and enjoy Kotlin’s concise syntax if you define your entity classes as regular Kotlin classes and annotate the fields you want to persist. 
 It’s a general best practice to avoid exposing your entity classes and their technical dependencies in your API. Most teams introduce a second non-entity representation of their data for that. Using Kotlin, you can easily model those classes as a data class. Doing that requires additional mapping code to convert your data between the different formats. You could, of course, do that in your business code. But it’s much more comfortable to add a set of converter functions to your entity class or select the data class directly from the database. You will see an example of the second approach later in this article. Let’s concentrate on the entity class for now. 
 Here is a simple Person entity. It maps the person’s first and last name, along with a many-to-one relationship to the company they work for. 
 The PersonData class represents the same information. You can use it in your API without exposing any technical details of your persistence layer. To make using this class as comfortable as possible, the Person entity class provides 2 functions with the required mapping code. 
 @Entity
class Person(
 @Id
 @GeneratedValue
 var id: Long? = null,

 var firstName: String? = null,

 var lastName: String? = null,

 @ManyToOne(fetch = FetchType.LAZY)
 var company: Company? = null,

 @Version
 var version: Integer? = null
) {
 fun createPersonData(): PersonData {
 return PersonData(
 id = id!!,
 firstName = firstName ?: "",
 lastName = lastName ?: "",
 version = version
 )
 }

 companion object {
 fun createPersonFromData(data: PersonData): Person {
 return Person(
 id = data.id,
 firstName = data.firstName,
 lastName = data.lastName,
 version = data.version
 )
 }
 }
}

data class PersonData(
 val id: Long,
 val firstName: String,
 val lastName: String,
 val version: Int
) The functions 
 The Company entity follows the same approach: 
 @Entity
class Company(
 @Id
 @GeneratedValue
 var id: Long? = null,

 var name: String = "default",

 @Version
 var version: Integer? = null
) After you modeled your entity classes, you can start defining your repositories. 
 Designing and using a repository 
 Spring Data JPA’s repository abstraction works the same way in Kotlin as it does in Java. You extend one of the provided repository interfaces, such as JpaRepository or CrudRepository, and Spring Data provides you with an implementation. 
 These repositories define a set of standard methods for fetching entities by primary key, persisting new entities, and removing existing ones. They also integrate with Spring’s transaction handling, so that you can use the @Transactional annotation on your business or API layer to define the transaction handling. 
 Here is an example of a simple PersonRepository definition. It inherits all standard methods defined by the JpaRepository. Let’s see how to add your own query methods in one of the following examples. 
 interface PersonRepository : JpaRepository<Person, Long> {} To make it even easier, IntelliJ IDEA can create the repository for you automatically. Just start typing repository name in the service and IDEA will suggest creating it: 
 With this repository in place, you can focus on your business logic. That’s especially convenient in Kotlin because constructor injection and concise function definitions keep your classes short and focused. 
 @Component
@Transactional
class PersonController (
 private val personRepository: PersonRepository) {
 fun createNewPerson(person : Person): Person {
 // add additional validations and/or logic ...
 return personRepository.save(person)
 }
} In this example, Spring injects a PersonRepository instance and joins an active transaction or starts a new one before entering the createNewPerson method. If it started a new transaction, it also commits it after completing this method call. And the PersonRepository, together with the Jakarta Persistence implementation, provides the required code to create and execute a SQL INSERT statement that stores the provided Person object in the database. 
 2025-11-16T16:02:53.988+01:00 DEBUG 10104 --- [SDJWithKotlin] [ main] org.hibernate.SQL : select next value for person_seq
2025-11-16T16:02:54.012+01:00 DEBUG 10104 --- [SDJWithKotlin] [ main] org.hibernate.SQL : insert into person (company_id,first_name,last_name,version,id) values (?,?,?,?,?)
2025-11-16T16:02:54.014+01:00 TRACE 10104 --- [SDJWithKotlin] [ main] org.hibernate.orm.jdbc.bind : binding parameter (1:BIGINT) <- [null]
2025-11-16T16:02:54.014+01:00 TRACE 10104 --- [SDJWithKotlin] [ main] org.hibernate.orm.jdbc.bind : binding parameter (2:VARCHAR) <- [John]
2025-11-16T16:02:54.014+01:00 TRACE 10104 --- [SDJWithKotlin] [ main] org.hibernate.orm.jdbc.bind : binding parameter (3:VARCHAR) <- [Doe]
2025-11-16T16:02:54.014+01:00 TRACE 10104 --- [SDJWithKotlin] [ main] org.hibernate.orm.jdbc.bind : binding parameter (4:INTEGER) <- [0]
2025-11-16T16:02:54.015+01:00 TRACE 10104 --- [SDJWithKotlin] [ main] org.hibernate.orm.jdbc.bind : binding parameter (5:BIGINT) <- [2] You might know all of this from using Spring Data JPA with Java. Kotlin does not change any of this behavior, and you also get all the benefits from using Kotlin when implementing your business logic. 
 Let’s take a look at another example. 
 Fetching and updating an existing entity follows the same pattern. The updateLastName function loads the entity by its primary key and changes the lastName. That’s all you have to do. The Jakarta Persistence implementation finds that modification during its next dirty check and updates the database automatically. 
 @Component
@Transactional
class PersonController (
 private val personRepository: PersonRepository) {
 fun updateLastName(id : Long, lastName : String): Person {
 var person = personRepository.findById(id).orElseThrow()
 person.lastName = lastName
 return person
 }
} As you can see, Kotlin’s concise syntax helps keep the business logic easy to read, and Spring handles all the boilerplate code for you. That makes implementing your application very comfortable. 
 Adding your own queries 
 In addition to the standard methods provided by Spring Data JPA’s repositories, you need to define queries that fetch the data used in your business code. You can do that in 2 ways, both of which work fine with Kotlin. 
 The first and most convenient option is to use derived query methods . Spring analyzes the method name, derives the corresponding JPQL query, and binds the method parameter values. This is a good choice when your query is simple and only requires one or two bind parameters. 
 You can add a derived query method directly to your repository. Or In IDEA, you can start typing a desired method name and use autocompletion to have it automatically added to your repository. 
 You can see a typical example in the following code snippet. The findByLastName method fetches all Person entities with a lastName equal to the provided one. 
 interface PersonRepository : JpaRepository<Person, Long> {
 fun findByLastName(lastName: String): List<Person>
} If your query becomes more complex, you should instead annotate your repository method with a @Query annotation . That allows you to write your own JPQL query and gives you full control over the executed statement. You can use joins, grouping, or any other JPQL feature you need. 
 Here you can see the same query statement as in the previous example. But this time, using a @Query annotation instead of Spring Data’s derived query feature. 
 interface PersonRepository : JpaRepository<Person, Long> {
 @Query("select p from Person p where p.lastName = :lastName")
 fun getByLastName(lastName: String): List<Person>
} When you call one of these methods, Spring Data JPA uses Jakarta Persistence’s EntityManager to instantiate a Query, set the provided bind parameters, execute the query, and map the result to a managed Person entity object. 
 2025-11-16T16:47:20.949+01:00 DEBUG 16193 --- [SDJWithKotlin] [ main] 
org.hibernate.SQL : select 
p1_0.id,p1_0.company_id,p1_0.first_name,p1_0.last_name,p1_0.version from person p1_0 
where p1_0.last_name=?
2025-11-16T16:47:20.952+01:00 TRACE 16193 --- [SDJWithKotlin] [ main]
org.hibernate.orm.jdbc.bind : binding parameter (1:VARCHAR) <- [Doe] But entities are not the only projection you can use. For many use cases, a read-only DTO projection that only fetches the required information is more efficient. And Kotlin’s data classes are a great way to model such a DTO. 
 If you only want to show the first and last names of multiple people along with the company they work for, you could use the following PersonWithCompany data class. 
 data class PersonWithCompany(
 val firstName: String,
 val lastName: String,
 val company: String
) In the next step, you can define a repository method that returns a List of those objects. If you annotate that method with a @Query annotation and provide a JPQL query that returns 3 fields with matching names, Spring Data JPA automatically maps each record to a PersonWithCompany object. 
 interface PersonRepository : JpaRepository<Person, Long> {
 @Query("select p.firstName, p.lastName, c.name as company from Person p join p.company c")
 fun findPersonsWithCompany(): List<PersonWithCompany>
} As you can see in the log output, using a data class as your query projection combines the convenience of Kotlin data classes in your business code with the performance benefits of fetching only the required information from the database. 
 2025-11-16T16:59:42.260+01:00 DEBUG 22541 --- [SDJWithKotlin] [ main]
org.hibernate.SQL : select p1_0.first_name,p1_0.last_name,c1_0.name from 
person p1_0 join company c1_0 on c1_0.id=p1_0.company_id
2025-11-16T16:59:42.278+01:00 INFO 22541 --- [SDJWithKotlin] [ main] c.t.j.k.s.SDJWithKotlinApplicationTests : PersonWithCompany(firstName=Jane,
lastName=Doe, company=Mighty Business Corp) Provide your own repository method implementations 
 If you need more flexibility than Spring Data JPA’s @Query annotation provides, you can also add your own method implementations to a repository. You do that by creating an interface that defines only the methods you want to implement, letting your repository extend that interface, and providing an implementation of that interface. This is called a fragment repository. 
 In this example, the PersonFragmentRepository defines the searchPerson method that expects a PersonSearchInput parameter. 
 interface PersonFragmentRepository {
 fun searchPerson(searchBy : PersonSearchInput): List<Person?>?
}

data class PersonSearchInput(
 val firstName : String?,
 val lastName : String?,
 val worksForCompany : String?
) {} In the next step, you have to implement the PersonFragmentRepository . The name of your class should be the interface name with the postfix Impl . Spring Data then automatically detects this class, wires it into your repository, and delegates all calls to the searchPerson method to your class. 
 The goal of the following searchPerson implementation is to check which fields of the PersonSearchInput object are set and consider only those fields in the query’s WHERE clause. This is a typical implementation for complex search dialogs, where users can choose which information to search for. 
 override fun searchPerson(searchBy: PersonSearchInput): List<Person?>? {
 val cBuilder = em.criteriaBuilder
 val cQuery = cBuilder.createQuery(Person::class.java)
 val person = cQuery.from(Person::class.java)
 val wherePredicates = mutableListOf<Predicate>()

 searchBy.firstName?.let {
 wherePredicates.add(cBuilder.equal(person.get<String>("firstName"), searchBy.firstName))
 }
 searchBy.lastName?.let {
 wherePredicates.add(cBuilder.equal(person.get<String>("lastName"), searchBy.lastName))
 }
 searchBy.worksForCompany?.let {
 val company = person.join<Person, Company>("company")
 wherePredicates.add(cBuilder.equal(company.get<String>("name"), searchBy.worksForCompany))
 }

 cQuery.where(*wherePredicates.toTypedArray())
 return em.createQuery(cQuery).resultList
} 
 As you can see in the code snippet, the searchPerson method uses Jakarta Persistence’s Criteria API to define a query based on the fields set on the provided PersonSearchInput object. 
 It first gets a CriteriaBuilder and uses it to create a CriteriaQuery that returns Person objects. It then defines the FROM clause and creates a List of Predicates . For each field of the PersonSearchInput object that’s not null, an equal predicate gets added to the wherePredicates List . 
 Thanks to Kotlin’s concise syntax and null handling, defining those Predicates is straightforward. Only the handling of the company name requires a little attention. If that field is set, you have to add a join to the Company entity before you can define the equal predicate. 
 You can then use the wherePredicates List to define the WHERE clause, execute the query, and return the result. 
 After you define the PersonFragmentRepository and implement it, you can use it in your repository definition. Let’s add it to the PersonRepository , which you already know from previous examples. It now extends Spring Data JPA’s JpaRepository and the PersonFragmentRepository . 
 interface PersonRepository : JpaRepository<Person, Long>, PersonFragmentRepository {
 fun findByLastName(lastName: String): List<Person>

 @Query("select p from Person p where p.lastName = :lastName")
 fun getByLastName(lastName: String): List<Person>

 @Query("select p.firstName, p.lastName, c.name as company from Person p join p.company c")
 fun findPersonsWithCompany(): List<PersonWithCompany>
} When you use this PersonRepository in your business code, Spring Data JPA provides the implementations of all methods defined by the JpaRepository . It also generates the implementations of the 3 query methods. Only the calls to the searchPerson method get delegated to your PersonFragmentRepositoryImpl class. 
 Summary 
 As you’ve seen in this article, Kotlin works well with Spring Data JPA. You can model your entities and define repositories in the same way you would in a Java application. Kotlin’s concise syntax often makes these parts of your code easier to read and maintain without changing any persistence behavior. If you follow the established Jakarta Persistence best practices for Kotlin , you get a smooth development experience and an efficient persistence layer. 
 To learn more about persistence with Kotlin, check out two other articles in this series: 
 How to Avoid Common Pitfalls with JPA and Kotlin 
 Using Spring Data JDBC With Kotlin 
 About the author 
 Thorben Janssen 
 Thorben Janssen is a consultant and trainer who helps teams build better persistence layers with JPA and Hibernate. An international speaker with more than 20 years of experience in JPA and Hibernate, Thorben is the author of the best-selling book Hibernate Tips: More than 70 solutions to common Hibernate problems . 
 He also writes on thorben-janssen.com about various persistence topics, and to help developers improve their skills, he founded the Persistence Hub.
```

---

## 8. AI-Assisted Java Application Development with Agent Skills

- 日期: 2026-03-26 13:21
- 链接: https://blog.jetbrains.com/idea/2026/03/ai-assisted-java-application-development-with-agent-skills/

```
Agent-assisted development is quickly becoming a common mode of software development. New techniques are emerging to help LLMs generate code that matches your preferences and standards. 
 One common approach is to create an AGENTS.md , CLAUDE.md , or GEMINI.md file with project details, build instructions, and coding guidelines. The AI agent loads this file into context on every request. 
 This has two drawbacks: 
 It consumes tokens on every request, increasing cost. 
 Loading too much context into an LLM degrades its effectiveness. 
 Agent Skills is a new initiative that solves both problems by managing context progressively and extending AI agent capabilities on demand. 
 What are Agent Skills? 
 Agent Skills is an open standard introduced by Anthropic, to extend AI agent capabilities with specialized knowledge and workflows. 
 Consider a use case where you want an AI to generate presentations using your company’s slide template and design guidelines. You can package those assets (the PPT template, font files, and design rules) into a skill . The agent then uses that skill to generate slides that match your standards automatically. 
 A skill is a folder containing a SKILL.md file. This file includes metadata ( name and description at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, templates, and reference materials. 
 skill-name/
├── SKILL.md # Required: instructions + metadata
├── scripts/ # Optional: executable code
├── references/ # Optional: documentation
└── assets/ # Optional: templates, resources The format of a SKILL.md file is: 
 ---
name: name-of-the-skill
description: Skill description.
license: Apache-2.0
metadata:
 author: author/org
 version: "1.0"
compatibility: Requires git, docker, jq, and access to the internet
---

Skill Content In a SKILL.md file, name and description are required fields, and you can add optional fields like licence , metadata , compatibility , etc. You can explore more about the Skill Specification here . 
 How do Agent Skills manage context? 
 At startup, agents load only the metadata (name and description) of installed skills. When you ask the agent to perform a task, it finds the relevant skill and loads only that SKILL.md into context. 
 This progressive loading keeps context minimal and pulls in additional information only when needed, unlike a monolithic CLAUDE.md that loads everything upfront. 
 What can be a skill? 
 Skills extend AI capabilities across a wide range: from coding guidelines for a specific library, to step-by-step workflows with reference documents and helper scripts. 
 For example, you can create a skill that: 
 Specifies which library APIs to use and which anti-patterns to avoid. 
 Bundles reference documentation in a references/ directory. 
 Includes helper scripts in a scripts/ directory. 
 Case Study: Implementing Spring Data JPA Pagination 
 Suppose you ask an AI agent to implement a Spring Boot REST API endpoint that returns a paginated list of Post entities along with their Comment collections. 
 Without guidance, the agent is likely to produce one of these common mistakes: 
 N+1 SELECT problem — lazy-loading comments trigger a separate query per post. 
 In-memory pagination — using JOIN FETCH with pagination loads all rows into memory, then paginates in the application layer. 
 You can check out the sample code from the GitHub repository https://github.com/sivaprasadreddy/agent-skills-demo 
 Let us see how an AI Agent might generate code when asked to implement a REST API endpoint to return paginated posts along with comments. 
 Without any specific guidelines or skills, the AI Agent generated the following implementation: 
 @RestController
@RequestMapping("/api/posts")
class PostController {
 private final PostService postService;

 PostController(PostService postService) {
 this.postService = postService;
 }

 @GetMapping
 PagedResult<PostDto> getPosts(
 @RequestParam(name = "page", defaultValue = "1") int pageNo,
 @RequestParam(name = "size", defaultValue = "10") int pageSize) {
 return postService.getPosts(pageNo, pageSize);
 }

}

@Service
@Transactional(readOnly = true)
public class PostService {
 private final PostRepository postRepository;

 public PostService(PostRepository postRepository) {
 this.postRepository = postRepository;
 }

 public PagedResult<PostDto> getPosts(int pageNo, int pageSize) {
 Sort sort = Sort.by(Sort.Direction.ASC, "id");
 Pageable pageable = PageRequest.of(pageNo <= 0 ? 0 : pageNo - 1, pageSize, sort);
 Page<PostDto> postPage = postRepository.findAllWithComments(pageable).map(PostDto::from);
 return PagedResult.from(postPage);
 }

} If you run the application and invoke the GET /api/posts endpoint, you will get the results, but in the logs you will find the below WARNING : 
 HHH000104: firstResult/maxResults specified with collection fetch; applying in memory This essentially means, Hibernate will load all the entities into memory and then apply pagination. This will result in poor performance and even OutOfMemory exceptions if there are a large number of rows in the posts table. 
 A Spring Data JPA skill prevents both issues by giving the agent explicit guidelines and a working code example. 
 Spring Data JPA Agent Skill 
 Create a spring-data-jpa/SKILL.md file with the following content: 
 ---
name: spring-data-jpa-skill
description: Implement the persistence layer using Spring Data JPA in Spring Boot applications.
---

Follow the below principles when using Spring Data JPA:

1. Disable the Open Session in View (OSIV) filter: 
spring.jpa.open-in-view=false
2. Disable in-memory pagination: 
spring.jpa.properties.hibernate.query.fail_on_pagination_over_collection_fetch=true

3. Avoid the N+1 SELECT problem: use JOIN FETCH to load associated child collections in a single query.
4. Avoid in-memory pagination: when loading a paginated list of parent entities with child collections:
 * First, load only the parent IDs using pagination
 * Then, load the full entities with their child collections using JOIN FETCH for those IDs
 * Assemble the final Page from the paginated IDs and the loaded entities

## Pagination with child collections example:

PostRepository.java

public interface PostRepository extends JpaRepository<Post, Long> {

 @Query("select p.id from Post p order by p.id")
 Page<Long> findPostIds(Pageable pageable);

 @Query("select distinct p from Post p left join fetch p.comments where p.id in :ids")
 List<Post> findAllByIdInWithComments(@Param("ids") Collection<Long> ids);
}

PostService.java

@Service
public class PostService {
 private final PostRepository postRepository;

 public PostService(PostRepository postRepository) {
 this.postRepository = postRepository;
 }

 @Transactional(readOnly = true)
 public Page<Post> findPosts(Pageable pageable) {
 Page<Long> idsPage = postRepository.findPostIds(pageable);
 if (idsPage.isEmpty()) {
 return Page.empty(pageable);
 }
 List<Post> posts = postRepository.findAllByIdInWithComments(idsPage.getContent());
 return new PageImpl<>(posts, pageable, idsPage.getTotalElements());
 }
} How to use Agent Skills? 
 Agent Skills work with Claude Code, Codex, Gemini CLI, JetBrains Junie, and other agents. Install a skill at the project level or user level depending on your preference. 
 Agent Project-Level User-Level 
 Junie .junie/skills/ ~/.junie/skills/ 
 Claude Code .claude/skills/ ~/.claude/skills/ 
 Codex .agents/skills/ ~/.agents/skills/ 
 Gemini CLI .gemini/skills/ (or) .agents/skills/ ~/.gemini/skills/ (or) ~/.agents/skills/ 
 To use the Spring Data JPA skill with Claude Code: 
 Copy the spring-data-jpa/ directory into {project-root}/.claude/skills/ . 
 Ask Claude Code to implement a paginated REST API endpoint. 
 Claude Code discovers the skill automatically and follows the guidelines. 
 As you can see, Claude Code automatically discovered the Spring Data JPA skill and generated the following implementation following the guidelines given in the skill. 
 @Service
public class PostService {
 private final PostRepository postRepository;

 public PostService(PostRepository postRepository) {
 this.postRepository = postRepository;
 }

 @Transactional(readOnly = true)
 public Page<Post> findPosts(Pageable pageable) {
 Page<Long> idPage = postRepository.findPostIds(pageable);
 if (idPage.isEmpty()) {
 return Page.empty(pageable);
 }
 List<Post> posts = postRepository.findAllByIdInWithComments(idPage.getContent());
 return new PageImpl<>(posts, pageable, idPage.getTotalElements());
 }
} With this implementation, only the Post IDs of the desired page will be loaded first, and then a list of posts along with their comments will be fetched in a separate query. This will fix the pagination in-memory issue. 
 Using Agent Skills with Junie 
 You can use the JetBrains Junie Agent to generate code which automatically loads the necessary skills from .junie/skills and directory. 
 The Junie agent loaded spring-data-jpa skill based on the given task and applied the guidelines. You can also observe that Junie automatically runs the relevant tests to verify the generated code is working or not and iterate until the tests are passed. 
 In the sample repository https://github.com/sivaprasadreddy/agent-skills-demo , you can find the following branches to try out the spring-data-jpa Agent Skill: 
 main : Starting point to try implementing the mentioned usecase without any skills. 
 in-memory-pagination-issue : Usecase implementation generated by AI that results in in-memory pagination issue. 
 skills : With spring-data-jpa skill to try implementing the mentioned usecase. 
 Summary 
 If the AI agent is generating code with any anti-patterns or not following team coding standards and conventions, instead of fixing issues one-by-one with follow-up prompts, consider creating a skill to provide those as guidelines. 
 To explore more on Agent Skills, please refer to the following resources: 
 https://agentskills.io/ 
 https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview 
 https://developers.openai.com/codex/skills/ 
 https://geminicli.com/docs/cli/skills/ 
 https://junie.jetbrains.com/docs/agent-skills.html
```

---

## 9. IntelliJ IDEA 2026.1 Is Out!

- 日期: 2026-03-25 14:28
- 链接: https://blog.jetbrains.com/idea/2026/03/intellij-idea-2026-1/

```
IntelliJ IDEA 2026.1 is here, and it comes packed with an array of new features and enhancements to elevate your coding experience! 
 You can download this latest release from our website or update to it directly from inside the IDE, via the free Toolbox App , or using snap packages for Ubuntu. 
 As always, all new features are brought together on the What’s New page , with detailed explanations and demos. 
 Explore the What’s New page 
 In addition to the What’s New page, our developer advocates got together to discuss and demonstrate the key updates. If you prefer watching to reading, check it out. 
 IntelliJ IDEA 2026.1 brings built-in support for more AI agents, including Codex, Cursor, and any ACP-compatible agent, and delivers targeted, first-class improvements for Java, Kotlin, and Spring. The release also advances IntelliJ IDEA’s mission to provide support for the latest languages and tools from day one. 
 Please note that some AI features may work differently or be unavailable in your region. Learn more . 
 Any agent, built-in: 
 ACP Registry: Browse and install AI agents in one click. 
 Git worktrees: Work in parallel branches and hand one off to an agent while you keep moving in another. 
 Database access for AI agents: Let Codex or Claude Agent query and modify your data sources natively. 
 Intelligence in the platform: 
 Quota-free next edit suggestions: Propagate changes throughout a given file with IDE-driven assistance. 
 Spring runtime insight: Inspect injected beans, endpoint security, and property values without pausing execution. 
 Kotlin-aware JPA: Detect and fix Kotlin-specific pitfalls in Jakarta Persistence entities. 
 First-class language support: 
 Java 26: Enjoy day-one support, including preview features. 
 Kotlin 2.3.20: Enjoy day-one support, including experimental features. 
 C/C++ in IntelliJ IDEA: Access first-class C/C++ coding assistance for multi-language projects. 
 Support for JavaScript without an Ultimate subscription. 
 Productivity and environment: 
 Expanded command completion, now with AI actions, postfix templates, and config file support. 
 Better performance for large-scale TypeScript projects. 
 Native Dev Container workflow: Open containerized projects as if they were local. 
 Along with new features, 2026.1 delivers numerous stability, performance, and usability improvements across the platform. These are described in a separate What’s Fixed blog post . 
 As always, your feedback plays an important role in shaping IntelliJ IDEA. Tell us what you think about the new features and help guide future improvements. 
 Join the discussion on X , LinkedIn , or Bluesky , and if you encounter any issues, please report them via YouTrack . 
 For full details of the improvements introduced in version 2026.1, refer to the release notes . 
 Thank you for using IntelliJ IDEA. Happy developing!
```

---

## 10. What’s fixed in IntelliJ IDEA 2026.1

- 日期: 2026-03-25 10:48
- 链接: https://blog.jetbrains.com/idea/2026/03/whats-fixed-intellij-idea-2026-1/

```
Welcome to the overview of fixes and improvements in IntelliJ IDEA 2026.1. 
 In this release, we have resolved over 1,000 bugs and usability issues , including 334 
 reported by users . Below are the most impactful changes that will help you work with greater confidence every day. 
 Performance 
 We continue to prioritize reliability, working to improve application performance, fix freezes, optimize operations, and cover the most common use cases with metrics. Using our internal tools, we identified and resolved 40 specific scenarios that caused UI freezes. 
 However, internal tooling alone cannot uncover every issue. To identify additional cases, we enabled automatic error and freeze reporting in EAP builds. By collecting this data, we gain a real, unfiltered picture of what’s going wrong, how often it happens, and how many users are affected. This allows us to prioritize fixes based on real impact rather than guesswork. 
 As always, we prioritize your privacy and security. When using EAP builds, you maintain full control and can disable automatic error and freeze reporting in Settings | Appearance & Behavior | System Settings | Data Sharing . Thank you for helping us build better tools! 
 Terminal 
 Version 2026.1 enhances your productivity by streamlining the experience offered by the terminal, a crucial workspace for developer workflows involving CLI-based AI agents. 
 First, we fixed the Esc behavior – it is now handled by the shell instead of switching focus to the editor, so it does not break the AI-agent workflow. Additionally, Shift + Enter now inserts a new line , making it easier to write multi-line prompts and commands directly. This behavior can be disabled in Settings | Advanced Settings | Terminal . 
 We also improved the detection of absolute and relative file paths in terminal output, allowing you to open files and folders with a single click in any context. When you encounter compilation or build errors, or submit a task to an AI coding agent, you can jump directly to the referenced file and review or fix issues faster. 
 Link navigation is activated by holding Ctrl (or Cmd on macOS) and clicking – just like in external terminals. 
 JVM language support 
 Better Kotlin bean registration support 
 Kotlin’s strong DSL capabilities are a perfect fit for Spring Framework 7’s BeanRegistrar API. In 2026.1, we’ve made working with programmatic registration as productive as annotation-based configuration. 
 The IDE ensures complete visibility into your application structure thanks to the Structure tool window, providing better endpoint visibility, intuitive navigation with gutter icons, integrated HTTP request generation, and path variable support. 
 New Kotlin coroutine inspections 
 To help maintain code quality, we’ve introduced a set of new inspections for the Kotlin coroutines library, covering common pitfalls. 
 Read more about coroutine inspections in this article . 
 Scala 
 Working with sbt projects inside WSL and Docker containers is now as smooth as working with local projects. We’ve also improved code highlighting performance and sped up sbt project synchronization. 
 To reduce cognitive load and provide a more ergonomic UI, we’ve redesigned the Scala code highlighting settings. A new Settings page consolidates previously scattered options, making them cleaner, more intuitive, and easier to access. 
 You can now disable built-in inspections when compiler highlighting is sufficient, or configure compilation delay for compiler-based highlighting. Settings for Scala 2 and Scala 3 projects are now independent, and the type-aware highlighting option has been integrated with the rest of the settings. 
 You can read more about these updates this article . 
 Spring 
 Spring support remains a core focus for IntelliJ IDEA. We are committed to maximizing reliability and reducing friction in your daily development. 
 In this release, we made a dedicated effort to address issues related to running Spring Boot application from the IDE. There are now even fewer reasons to run your application in the terminal – just run it in the IDE and use the debugger when you need deeper insights. 
 Spring Boot 4 API versioning support 
 This is a new Spring Boot feature, and we keep improving its support based on your feedback. In this version, we added .yml files support for version configuration, fixed false positives and added a couple of useful inspections, so you get an instant feedback about issues without running the app. 
 Flyway DB Migrations 
 To ensure a reliable and distraction-free experience, the IDE now verifies migration scripts only when a data source is active, eliminating false-positive errors when the data source is disconnected. 
 At the same time, Flyway scripts got correct navigation to the table definitions, and SQL autocompletion for any files and tables defined in them. 
 User interface 
 With IntelliJ IDEA 2026.1, we’ve continued to prioritize ultimate comfort and an ergonomic UI, ensuring your workspace is as accessible and customizable as your code. 
 The long-awaited ability to sync the IDE theme with the OS is now available to Linux users, bringing parity with macOS and Windows. Enable it in Settings | Appearance & Behavior | Appearance . 
 The code editor now supports OpenType stylistic sets . Enjoy more expressive typography with your favorite fonts while coding. Configure them via Editor | Font , and preview glyph changes instantly with a helpful tooltip before applying a set. 
 Windows users who rely on the keyboard can now bring the IDE’s main menu into focus by pressing the Alt key . This change improves accessibility for screen reader users. 
 Version control 
 We continue to make small but impactful improvements that reduce friction and support your everyday workflow. 
 You can now [coming in 2026.1.1 update] amend any recent commit directly from the Commit tool window – no more ceremonies involving interactive rebase. Simply select the target commit and the necessary changes, then confirm them – the IDE will take care of the rest. 
 In addition to Git worktrees, we’ve improved branch workflows by introducing the Checkout & Update action, which pulls all remote changes. 
 Furthermore, fetching changes can now be automated – no need for a separate plugin. Enable Fetch remote changes automatically in Settings | Git . 
 In-IDE reviews for GitLab merge requests now offer near feature parity with the web interface. Multi-line comments , comment navigation , image uploads , and assignee selection when creating a merge request are all available directly in the IDE, so you can stay focused without switching to the browser. 
 The Subversion, Mercurial, and Perforce plugins are no longer bundled with the IDE distribution, but you can still install them from JetBrains Marketplace . 
 Databases 
 We’ve enhanced the Explain Plan workflow with UI optimizations for the Query Plan tab, an additional separate pane for details about the execution plan row, inner tabs that hold flame graphs, and an action to copy the query plan in the database’s native format. 
 JetBrains daemon 
 IntelliJ IDEA 2026.1 includes a lightweight background service – jetbrainsd – that handles jetbrains:// protocol links from documentation, learning resources, and external tools, opening them directly in your IDE without requiring you to have the Toolbox App running. 
 Sunsetting of Code With Me 
 As of version 2026.1, Code With Me will be unbundled from all JetBrains IDEs and will instead be available as a separate plugin on JetBrains Marketplace. Version 2026.1 will be the last IDE release to officially support Code With Me as we gradually sunset the service. 
 Read the full announcement and timeline in our blog post . 
 Enhanced AI management and analytics for organizations 
 We are working hard to provide development teams with centralized control over AI and built-in analytics to understand adoption, usage, and cost. As part of the effort, we’ve introduced the JetBrains Console . It adds visibility into how your teams use AI in practice, including information about active users, credit consumption, and acceptance rates for AI-generated code. 
 The JetBrains Console is available to all organizations with a JetBrains AI subscription, providing the trust and visibility required to manage professional-grade development at any scale. 
 That’s it for this overview. 
 Let us know what you think about the fixes and priorities in this release. Your feedback helps us steer the product so it works best for you! 
 We’d also love to hear your thoughts on this overview and the format in general. 
 Update to IntelliJ IDEA 2026.1 now and see how it has improved. Don’t forget to join us on X , Bluesky , or LinkedIn and share your favorite updates. 
 Thank you for using IntelliJ IDEA!
```

---

## 11. Core JavaScript and TypeScript Features Become Free in IntelliJ IDEA

- 日期: 2026-03-19 11:43
- 链接: https://blog.jetbrains.com/idea/2026/03/js-ts-free-support/

```
Modern Java development often involves web technologies. To make this workflow more accessible and smoother, we’re making some core JavaScript, TypeScript, HTML, and CSS features – previously included with the Ultimate subscription only – available for free in IntelliJ IDEA v2026.1. 
 JavaScript, TypeScript, HTML, CSS, and React Support 
 Enjoy a comprehensive set of features for building modern web applications: 
 Basic React support , including code completion, component and attribute navigation, and React component and prop rename refactorings. 
 Full syntax highlighting for JavaScript, TypeScript, HTML, and CSS, ensuring better readability and usability of frontend code inside the IDE. 
 Reliable code completion to write code faster and with fewer errors across both backend and frontend parts of your web application. 
 Advanced import management automatically handles JavaScript and TypeScript imports as you code, adds missing references when pasting code, and cleans up unused ones with Optimize Imports – helping you save time, reduce errors, and keep your codebase clean. 
 Smooth code navigation via dedicated gutter icons for Jump to… actions, recursive calls, TypeScript source mapping, and more. 
 Code Intelligence and Code Quality 
 Improve and maintain your web code with built-in intelligence and quality tools: 
 Core web refactorings: Make changes to your code with reliable Rename refactorings and actions ( Introduce Variable , Introduce Constant , Change Signature , Move Members , and more). 
 Quality control : Identify potential issues early with built-in inspections, intentions, and quick fixes, and get improvement suggestions as you code. 
 Code cleanup : Keep your codebase clean with JavaScript and TypeScript duplicate detection, making it easier to spot and eliminate redundant code. 
 Integrated workflows 
 Now it’s easier to manage, maintain, and secure your web projects from within a single environment. 
 Create new web projects quickly by using the built-in Vite generator. 
 Keep your codebase consistent and clean with integrated support for Prettier, ESLint, TSLint, and StyleLint. 
 Execute NPM scripts directly from package.json . 
 Monitor your project dependencies and identify known security vulnerabilities early. 
 Enjoy building your web applications with IntelliJ IDEA, and happy developing! 
 If you need more advanced tools (dedicated debugger, test runners, test UI tooling, support for all frontend frameworks including Angular, Vue, advanced refactorings, and more) for full-stack application development, you can try them with the Ultimate subscription trial. The trial provides 30 days of full access – no credit card required.
```

---

## 12. IntelliJ IDEA’s New Kotlin Coroutine Inspections, Explained

- 日期: 2026-03-19 10:00
- 链接: https://blog.jetbrains.com/idea/2026/03/intellij-idea-s-new-kotlin-coroutine-inspections-explained/

```
This article was written by an external contributor. 
 Marcin Moskała 
 Marcin is a highly experienced developer and Kotlin instructor, founder of Kt. Academy, an official JetBrains partner specializing in Kotlin training. He is also a Google Developers Expert and a well-known contributor to the Kotlin community. Marcin is the author of several widely recognized books, including Effective Kotlin , Kotlin Coroutines , Functional Kotlin , Advanced Kotlin , Kotlin Essentials , and Android Development with Kotlin . 
 Website 
 Every technology has its misuses, and different ecosystems use different approaches to prevent them. In the Kotlin ecosystem, I believe the philosophy has always been to make APIs so good that correct usage is simple and intuitive, while misuse is harder and more complicated. This differs from JavaScript, which has plenty of legacy practices (like using == instead of ===, or var instead of let/const ) and relies more on warnings. However, not everything can be enforced by good design, and Kotlin also uses warnings to guide developers in writing better code. 
 Today, IntelliJ IDEA introduces a set of new inspections for the Kotlin coroutines library. I’ve seen these issues in many codebases and addressed them through my books, articles, and workshops. These patterns often show up, so let’s walk through why they are problematic and how to handle them correctly. 
 Note: These inspections are also available in Android Studio. You can check how IntelliJ IDEA versions map to Android Studio versions here . 
 awaitAll() and joinAll() 
 Available since IntelliJ IDEA 2025.2 
 If you use map { it.await() } , IntelliJ IDEA will suggest awaitAll() . If you use forEach { it.join() } , it will suggest joinAll() . Why? These alternatives are cleaner, and awaitAll() is also more efficient and better represents waiting for multiple tasks, as it waits for all elements concurrently rather than one after another. 
 awaitAll() also behaves more efficiently in the presence of exceptions. Imagine awaiting 100 coroutines, and the fiftieth throws an exception. awaitAll() will immediately rethrow the exception, unlike map { it.await() } , which would wait for the first 49 coroutines before throwing the exception. In most cases, this behavior cannot be observed because of other exception propagation mechanisms. 
 currentCoroutineContext() over coroutineContext 
 Available since IntelliJ IDEA 2025.2 
 All suspending functions can access the context of the coroutine in which they are called. Traditionally, this was done via the coroutineContext property. The problem is that CoroutineScope , which is implicitly available in coroutine starters, such as launch, coroutineScope , and runTest , has a property with the same name. This can be confusing and lead to issues. Consider the following example: 
 This code tests the mapAsync function and checks whether it correctly propagates context from the caller to the transformation. It is incorrect. Within the transformation, we could read the caller context from the coroutineContext , but not in this situation. This lambda is defined inside runTest , and the coroutineContext property from CoroutineScope (provided by runTest ) takes priority over the top-level coroutineContext property. This kind of mistake is quite common, which is why the currentCoroutineContext() function was introduced to read the context of the coroutine that runs a suspending function. You should use it instead of coroutineContext . 
 runBlocking inside a suspending function 
 Available since IDEA 2025.2 
 Using runBlocking inside suspending functions is a serious issue. It blocks the calling thread, which defeats the purpose of coroutines. 
 So what can you use instead? That depends on what you want to achieve. In most cases, you don’t need it. If you need to create a coroutine scope, use coroutineScope { … } . If you need to change context, use withContext(ctx) { … } . 
 Watch out for situations where a suspending function calls a regular function that uses runBlocking. Opt for making this function suspend to avoid making a blocking call. 
 Unused Deferred 
 Available since IntelliJ IDEA 2025.3 
 This inspection appears when you use async without ever using its result. In such cases, you should use launch instead. This is the key difference between launch and async : async returns a result and is expected to await this result, while launch produces no result. 
 Because of this, exception handling differs. async doesn’t call CoroutineExceptionHandler because it is expected to throw an exception from await and propagate it this way. 
 Job used as an argument in a coroutine starter 
 Available since IntelliJ IDEA 2025.3 
 I’ve been looking forward to this inspection for years! Using Job as an argument to a coroutine starter causes issues, and it’s something I’ve seen in many projects. I covered this anti-pattern in my book and workshops, but it still appears quite often. This inspection should help clarify the correct approach. Let’s look at why Job shouldn’t be used as an argument for a coroutine. 
 The key misunderstanding here is that Job cannot be overridden by an argument. If you use any other context, it will be used in the coroutine and its children, but not Job . Every coroutine creates its own job. A job contains a coroutine’s state and relations – it cannot be shared or enforced from outside. The Job that is used as an argument isn’t going to be a job of this coroutine. Instead, it overrides Job from the scope and becomes a parent. This breaks structured concurrency. 
 For example: Using withContext(SupervisorJob()) { … } behaves very differently from supervisorScope { … } . 
 supervisorScope creates a child coroutine of the caller of this function, and it uses a supervisor job (it doesn’t propagate its children’s exceptions). On the other hand, withContext(SupervisorJob()) creates a regular coroutine, which is a child of SupervisorJob and has no relation to the caller. 
 Consider the code below. An exception in the first launch propagates to withContext (which uses regular Job ), cancels the other child coroutines, and is then rethrown. SupervisorJob() has no effect. In some cases, it can even be harmful, as it breaks structured concurrency. If the caller of withContext(SupervisorJob()) is cancelled, that cancellation won’t propagate, which will result in a memory leak. 
 import kotlinx.coroutines.*

val handler = CoroutineExceptionHandler { _, e ->
   println("Exception:  ${e.message}")
}

fun main(): Unit = runBlocking(handler) {
   // DON'T DO THAT!
   withContext(SupervisorJob()) {
       launch {
           delay(1000)
           throw Error("Some error")
       }
       launch {
           delay(2000)
           println("AAA")
       }
   }
  println("Done")
}
// (1 sec)
// Exception in thread "main"... Using supervisorScope would prevent this problem: 
 import kotlinx.coroutines.*

val handler = CoroutineExceptionHandler { _, e ->
   println("Exception:  ${e.message}")
}

fun main(): Unit = runBlocking(handler) {
  supervisorScope {
      launch {
          delay(1000)
          throw Error("Some error")
      }
      launch {
          delay(2000)
          println("AAA")
      }
  }
  println("Done")
}
// (1 sec)
// Exception:  Some error
// (1 sec)
// AAA
// Done A Job used as an argument breaks the relationship with the caller. In the case below, updateToken won’t be related to the caller of getToken : 
 suspend fun getToken(): Token = coroutineScope {
   val token = tokenRepository.fetchToken()
   launch(Job()) { // Poor practice
       tokenRepository.updateToken(token)
   }
   token
} This is generally discouraged, as it breaks structured concurrency. The standard approach would be to sequentially call updateToken : 
 suspend fun getToken(): Token {
   val token = tokenRepository.fetchToken()
   tokenRepository.updateToken(token)
   return token
} If we really want to detach updateToken from getToken , a better practice would be to start the launch on a different scope, like the backgroundScope we define in our application for background tasks. With this approach, the new coroutine is still attached to a scope, just a different one: 
 suspend fun getToken(): Token {
   val token = tokenRepository.fetchToken()
   backgroundScope.launch { // Acceptable
       tokenRepository.updateToken(token)
   }
   return token
} suspendCancellableCoroutine instead of suspendCoroutine 
 Available since IntelliJ IDEA 2025.3 
 To suspend a coroutine, use suspendCancellableCoroutine . Its predecessor, suspendCoroutine , does not support cancellation and should be avoided. 
 suspendCancellableCoroutine is a low-level API rarely used in application code, but often used by libraries that support suspending calls. 
 Suspicious implicit CoroutineScope receiver 
 Available since IntelliJ IDEA 2025.3, but this inspection is disabled by default and must be enabled manually. 
 Implicit receivers within lambdas can be confusing. In the above example, async calls are executed on the scope created by coroutineScope because collectLatest doesn’t provide its own scope. This can lead to memory leaks. When a new value reaches collectLatest , it should cancel processing of the previous one. In this example, it cannot cancel the async coroutines, as they are attached to coroutineScope , not to collectLatest . To avoid this, define coroutineScope inside collectLatest , not outside it. This inspection highlights such cases to prevent these issues. 
 Simpler operations for flow processing 
 Available since IntelliJ IDEA 2026.1 (currently in EAP) 
 You may already know these from collection or sequence processing: 
 If you use filterNotNull after map, you’ll get the suggestion to use mapNotNull . If you use filter { it is T } , the IDE will suggest using filterNotNull<T> . 
 These suggestions are now also available for flows! 
 Summary 
 IntelliJ IDEA continues to help you write better code – not only by advancing its AI tools and agents, but also by improving the core development experience. There are still many inspections I would love to see in the IDE, but the current set already brings significant value.
```

---
