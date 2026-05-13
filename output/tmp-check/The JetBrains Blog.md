# The JetBrains Blog

> 分类: 大厂技术博客
> URL: http://blog.jetbrains.com/feed/
> 抓取: 12 篇

---

## 1. The MPS 2026.1 Early Access Program Has Started

- 日期: 2026-05-07 14:46
- 链接: https://blog.jetbrains.com/mps/2026/05/the-mps-2025-2-eap-has-started-2/

```
The MPS 2026.1 Early Access Program (EAP) is kicking off today. Download the first 2026.1 EAP release and give it a try! 
 DOWNLOAD MPS 2026.1 EAP 
 Along with numerous bug fixes, this build introduces several key improvements. 
 Migration to IntelliJ Platform 2026.1, JDK 25, and Kotlin 2.3 
 This MPS 2026.1 EAP build completes the jump to the current generation of the IntelliJ Platform. The runtime is JDK 25, and the embedded Kotlin version is 2.3.0. Additionally, MPS now builds and ships its own kotlinx-metadata-klib / kotlin-metadata-jvm artifacts from the Kotlin repository at the matching 2.3.0 tag, restoring the KLib-based Kotlin stubs support that the last public kotlinx-metadata-klib:0.0.6 could no longer provide. 
 Ability to check ICheckedNamePolicy against specific natural languages 
 MPS now uses the IntelliJ Platform’s natural language support, provided by Grazie. This means you can check whether string values in instances of ICheckedNamePolicy , such as intentions, actions, or tools, have proper capitalization according to the rules of a specific natural language. 
 Thanks to this change, you can install natural language support for select languages into MPS, and the IDE will detect the language used in strings and verify that individual words are capitalized correctly. You can also bypass the language detection mechanism and specify your desired language explicitly. 
 In addition to the default Title-case capitalization rules, MPS offers three other options: 
 Sentence-case , which follows the IntelliJ Platform’s rules 
 Inherited , which uses the capitalization rules of the closest ancestor ICheckedNamePolicy 
 No capitalization rules 
 Binary operations can be split into multiple lines 
 In the editor, you can now split long lines with binary operations. A dedicated intention action lets you toggle between the single-line and multi-line layouts for a given BinaryOperation . 
 New boolean editor style: read-only-inspector 
 The new read-only-inspector style enforces the read-only property on all editor cells in the inspector. When this style is applied to a cell in the main editor, the inspector becomes read-only for the inspected node when the cell with this style is selected. The new style has the following properties: 
 It is disabled by default. 
 The style is inheritable and overridable, just like the read-only style. 
 It has no effect on main editor cells. 
 The read-only style set by this mechanism can be overridden in any cell farther down the inspector editor cell tree. 
 Transitive dependencies in Build Language 
 Build Language no longer requires every transitively-reachable build script to be listed in dependencies . This means that a build script, BuildA , that depends on BuildB can now reach BuildC through BuildB (provided that BuildB depends on BuildC ) without having to list BuildC explicitly. The generator emits ${artifacts.BuildC} Ant properties for such cases, and these properties can be supplied from the outer build tool (Gradle, Maven, etc.). 
 This lets you split large builds into smaller ones without forcing every user to update the dependency lists. For example, a single platform build script can wrap a growing set of external libraries used across sub-projects. 
 More reliable migrations via recorded dependencies 
 Migration code previously decided which migrations to apply based on the actual module dependencies and used languages collected at migration time, but it would read versions from the dependency snapshot recorded in the module descriptor. That mismatch could cause migrations to use a different view of the world than the one the module was last modified against. 
 In this 2026.1 EAP build, the migration machinery consistently uses the dependencies and used languages recorded in the module descriptor at the moment of last modification, not the currently observable state. The migration checker was refactored accordingly. It now reuses information already collected for the migration process instead of recomputing it on demand. 
 Improved Java stubs 
 A cluster of long-standing Java-stubs bugs has been fixed, visibly improving the accuracy of BaseLanguage stubs produced for imported .jar files and Java Sources model roots: 
 MPS-33174 – Classes with InnerClasses attributes are now correctly transformed to BaseLanguage stubs (open since 2021). The signature’s inner-class information and parameterized owner types are preserved, so fields and methods of inner classes of generic outer classes now show the proper type instead of collapsing to the outer class. 
 MPS-39375 – Type variables in generic methods of inner classes are now handled, so methods referencing type variables of the outer class no longer show java.lang.Object in place of the real type variable. 
 MPS-39007 – The spurious Java imports annotation is present error no longer appears on every root of a Java source stub model. 
 MPS-39565 – Java source stub roots no longer disappear on changes to the containing module’s properties, so references from project code to those roots stay intact when module properties are changed. 
 Modernized project lifecycle 
 With MPSProject having moved from a legacy IntelliJ IDEA ProjectComponent to a project service, MPS-aware features need a reliable way to be notified about MPSProject becoming available and going away. 
 This build introduces a dedicated mechanism for managing MPSProject startup and shutdown activities, giving MPS control over the sequencing, grouping, ordering, and threading of those activities. This was something the platform’s ProjectActivity / MPSProjectActivity could not offer. 
 How it works: Implementors register against the jetbrains.mps.project.lifecycleListener extension point (declared in MPSCore.xml ) via a ProjectLifecycleListener.Bean with a listenerClass and an optional integer priority . The LifecycleEventDispatch.java inside MPSProject can fire: 
 projectReady (non-blocking) 
 projectDiscarded (blocking) 
 asyncProjectClosed (non-blocking) 
 Wayland by default 
 MPS now offers Wayland as the default display protocol on supported Linux systems. When running in a Wayland-capable environment, MPS automatically switches to a native Wayland backend instead of relying on X11 compatibility layers, bringing it in line with modern Linux desktop standards. 
 This transition improves overall integration with the system, providing better stability across Wayland compositors, proper support for input methods and drag-and-drop, and more consistent rendering – especially on HiDPI and fractional scaling setups. While the user experience remains largely familiar, some differences (such as window positioning or decorations) may be noticeable due to Wayland’s architecture. X11 is still fully supported and can be used as a fallback when needed, ensuring compatibility across all Linux environments. 
 You can review the complete list of fixed issues here . 
 Your JetBrains MPS team
```

---

## 2. Kotlin Ecosystem Mentorship Program: Results and Winners

- 日期: 2026-05-07 14:45
- 链接: https://blog.jetbrains.com/kotlin/2026/05/kotlin-ecosystem-mentorship-program/

```
In the Kotlin Ecosystem Mentorship Program pilot, mentors and mentees worked together on real Kotlin open-source projects to make their first meaningful community contribution. Four pairs successfully completed the two-month program, and one eligible pair was randomly selected in the prize drawing to receive the grand prize – a trip to KotlinConf 2026 in Munich! 
 Congratulations to the winners: 
 Mentor: Ruslan ( yet300 ) 
 Mentee: Clare Kinery ( kinerycl ) 
 Project: bitchat-android 
 Join the KEMP Slack channel 
 Ruslan’s and Clare’s collaboration focused on the Android client of BitChat, where Clare contributed UI and UX improvements that brought the Android experience closer to platform conventions and enhanced overall polish and accessibility. 
 Clare submitted and merged two pull requests: PR #680 and PR #682 . Her work improved BitChat’s voice note styling, camera and audio controls, dark/light theme support, visual hierarchy, and press interaction feedback. 
 Ruslan shared that Clare adapted quickly to the codebase and was able to work independently after the initial alignment. Their collaboration started with a kickoff call and continued asynchronously through chat and GitHub. 
 “Clare demonstrated strong problem-solving skills, attention to detail, and a solid understanding of UI/UX principles”, said Ruslan. 
 For Clare, the biggest takeaway was not just the code itself, but understanding the realities of open-source collaboration. 
 “As a developer who had never contributed to open source before, the biggest thing I learned was how open-source collaboration actually works. This program made it feel approachable and far less intimidating than I ever expected. I genuinely don’t think I would have taken that leap without it”, she commented. 
 Other participants 
 We received 80 mentee applications and 29 mentor applications – a clear sign of strong community interest in this kind of initiative, so we plan to continue the program. 
 For this pilot, we selected ten pairs. Eight remained active through the middle of the program, and four completed it successfully. These successful pairs contributed across different parts of the Kotlin ecosystem and Kotlin-related projects, including the Android UI, developer tooling, documentation, CI/CD, and multiplatform libraries. 
 We also want to recognize the other pairs who successfully completed the program: 
 Mentor: Mohamed Rejeb 
 Mentee: Kaustubh Deshpande 
 Project: Calf 
 Kaustubh contributed across several areas of the project, including dependency updates and CI/CD automation. 
 Mentor: Nikita Vaizin 
 Mentee: Anshul Vyas 
 Project: FlowMVI 
 Anshul fixed a bug in the metrics module and contributed to the migration guide that helps developers move from MVVM to FlowMVI. 
 Mentor: Adetunji Dahunsi 
 Mentee: Yu Jin 
 Project: heron 
 Yu Jin worked on improvements related to input handling and developer-facing issues, with a focus on making the project easier to use and maintain. 
 What we learned 
 Here are a few valuable takeaways from the participants’ feedback: 
 Clear task scoping matters. Start with work that is concrete, manageable, and reviewable within the program timeline. 
 Asynchronous mentorship can work well, but only when expectations are explicit, and collaborators align early on communication style, task size, and review cycles. 
 The program creates value on both sides. Mentees gain confidence, workflow knowledge, and real experience. Mentors get fresh contributions, a chance to improve onboarding in their own projects, and a reminder that open source becomes healthier when maintainers make room for new contributors. 
 Thank you to all mentors and mentees who joined the first Kotlin Ecosystem Mentorship cohort! We’re especially grateful to the maintainers who opened their projects to newcomers and invested time in guidance, reviews, and support. 
 Congratulations again to Ruslan and Clare, who were selected in the KotlinConf trip prize drawing, and to all four pairs who successfully completed the program. 
 To stay updated on future programs, join the KEMP Slack channel . See you there!
```

---

## 3. Make Your Plugin Remote Development-Ready

- 日期: 2026-05-07 12:00
- 链接: https://blog.jetbrains.com/platform/2026/05/make-your-plugin-remote-development-ready/

```
Remote development is changing how plugins should be built for JetBrains IDEs. The IDE is no longer a single local process: users interact with a frontend client, while the backend can run on another machine, in Docker, or in the cloud. This model is becoming increasingly important because it supports powerful remote environments, better security, and more flexible development workflows. In the case of JetBrains IDEs running backend and frontend processes simultaneously, we say they are operating in split mode . 
 For plugin developers, it is therefore not only crucial that they consider how their plugin works, but also where each part of it should run. Some extensions continue to work as they are, but UI, typing-related features, and anything sensitive to latency can become slow or behave incorrectly if they are not designed with client-server architecture in mind. 
 The new recommended approach is to think in terms of frontend, backend, and shared functionality, and make sure each part of the plugin runs on the side it belongs. The suggested plugin architecture works in both client-server IDE and monolithic IDE, so plugin authors don’t need to implement support twice. 
 To help with that, we now provide guidance for building split-mode-aware plugins in JetBrains IDEs. It explains the terminology, motivation, architecture, and how to run, debug, and test in split mode. It walks through the practical steps as well: structuring plugin modules, moving code to the appropriate side, and connecting the frontend and backend to each other. 
 To help you put your best foot forward in this brave new “split mode” world, we’ve prepared the following materials: 
 A high-level video overview . 
 A plugin template featuring proper module structures and demo feature implementation to use as a reference. 
 Documentation articles covering the most important aspects of plugin development, as well as a step-by-step guide on how to approach the splitting process 
 A link to the JetBrains Platform forum , where you can ask any questions regarding the development process and browse existing answers..
```

---

## 4. Python Unplugged on PyTV: Key Takeaways From Our Community Conference

- 日期: 2026-05-07 11:27
- 链接: https://blog.jetbrains.com/pycharm/2026/05/python-unplugged-on-pytv-key-takeaways-from-our-community-conference/

```
What happens when a global community with a love for Python meets a splash of 90s nostalgia? You get Python Unplugged on PyTV , our first-ever fully online community conference. 
 On March 4, 2026, Python Unplugged on PyTV set out to capture the magic of a full, in-person conference experience for people watching remotely all over the world – and it worked. 
 Thousands of attendees tuned in live, with even more watching later on demand. Viewers enjoyed live talks, expert panels, Q&As, hallway-style discussions, and even an interactive quiz. 
 Speakers from across the Python ecosystem traveled to Amsterdam, the birthplace of Python, with some journeying over 10 hours to take part in the event. Meanwhile, the PyCharm team brought the whole experience to life with a fully produced studio setup, 90s-inspired visuals, and an infectious energy that carried through the entire seven-and-a-half-hour broadcast. 
 With 13 insightful talks covering everything from AI and data science to web development and open-source sustainability, there was no shortage of ideas, perspectives, and cutting-edge discussions. 
 If you didn’t catch every session or just want an overview of the day, this recap highlights our standout moments from Python Unplugged on PyTV . 
 Watch the recap video 
 Want to see the highlights from Python Unplugged on PyTV ? Watch the full recap video below. 
 JetBrains’ Dr. Jodie Burchell, Data Scientist and Python Advocacy Team Lead; Cheuk Ting Ho, Data Scientist and Developer Advocate; and Will Vincent, Python Developer Advocate, discuss the key talking points from the day. 
 Need a quick overview? Here are the highlights 
 If you’d rather get the key takeaways in a written format, we’ve broken down the biggest insights from the day below. From the evolving role of AI to the importance of the Python community, these are the moments that stood out most from Python Unplugged on PyTV . 
 Highlight 1: Python is not just for beginners 
 Python’s reputation as a beginner-friendly language is well deserved, but it only tells part of the story. Python is a full-stack ecosystem capable of supporting complex, production-ready applications across a wide range of industries. 
 A key takeaway here was the importance of moving beyond the basics. In his How to Learn Python session, Mark Smith, Head of Python Ecosystem at JetBrains, explained how, once foundational concepts are in place, developers need to engage with Python more holistically. That means building real-world projects, exploring existing codebases, and understanding how Python is used in production environments. Ultimately, this is what bridges the gap between learning and mastery. 
 Interestingly, this also means being intentional about how you use modern tools while learning. In our recap video, Cheuk noted: “What I liked about this talk was the tip to turn off the AI features while you’re learning.” 
 The point isn’t to avoid AI entirely, but to ensure it doesn’t replace the hands-on experience needed to develop your own Python expertise. 
 Highlight 2: The continuing role of community in Python 
 Python’s success has always been rooted in its community, and that remains as true as ever. Georgi Ker, Director and Fellow at the PSF; Una Galyeva, Head of AI at Geobear Global; and Jessica Greene, Senior ML Engineer at Ecosia, showcased this in their How PyLadies Is Shaping the Future of Python discussion. 
 PyLadies is an international mentorship group focused on helping more women become active participants and leaders in the Python community. The success of initiatives like PyLadies highlights how inclusive spaces can broaden participation and shape the future of the language. 
 As Will noted in our recap video, “Being part of the community is not just the code. It’s the conferences, it’s the people, it’s the live events – that’s what makes Python special.” 
 Python depends on a culture of shared responsibility, and contributors play a vital role. As AI brings more people into the ecosystem, preserving these values becomes even more important. Travis Oliphant, creator of NumPy , touched on this in his insightful session, Community is More Than Code: People Are What Make Python Thrive, and Why That Will Continue in an AI-Enabled Era . 
 There’s also a strong link between community and innovation, as Carol Willing, Core Developer at JupyterLab, explained in her session, Conversation, Computation, and Community: Key Principles for Solving Scientific Problems With Jupyter Notebooks and AI Tools . Tools like Jupyter have thrived in part because they enable conversation, collaboration, and knowledge sharing among people. 
 Highlight 3: AI poses both a threat and an opportunity for Python open source 
 AI is fundamentally changing how developers interact with open source. 
 On the positive side, AI coding tools lower the barrier to entry and allow more people to contribute. However, this increased accessibility comes with trade-offs. Maintainers are now dealing with a higher volume of contributions, many of which require significant review or refinement. Deb Nicholson, Executive Director at the PSF, discussed this trade-off in more detail in her session, AI Practitioners Are Only Getting Half the Goodness of Python . 
 This shift places additional pressure on those responsible for maintaining open-source projects. While AI can accelerate development, it also risks introducing poorly structured or low-quality code at scale. 
 Paul Everitt, Developer Advocate at JetBrains; Georgi Ker, Director and Fellow at the PSF; and Carol Willing, Core Developer at JupyterLab, pondered this in their Open Source in the Age of Coding Agents discussion. Ultimately, AI can’t replace the human systems that sustain open source. Trust, collaboration, and shared ownership remain essential, and arguably become even more important as contribution volumes increase. The real challenge lies in ensuring communities remain healthy and resilient as they scale. 
 Highlight 4: AI has also revolutionized how Python practitioners work 
 Beyond its impact on open source, AI is transforming day-to-day development workflows. 
 As Marlene Mhangami, Senior Developer Advocate at Microsoft Agentic, explained in her A Practical Guide to Agentic Coding session, coding is emerging as a new paradigm in which developers delegate tasks to AI systems capable of planning, executing, and refining code. This means the developer’s role is moving toward orchestration and validation, requiring new skills in guiding and evaluating AI outputs. 
 At the same time, development is becoming more conversational and exploratory. In environments like Jupyter, AI tools help users iterate faster, test ideas more easily, and move more fluidly between thinking and coding. 
 AI is also having a tangible impact on frameworks like Django, as discussed by Sheena O’Connell, Board Member at the PSF, in her talk, Powering Up Django Development With Claude Code . AI tools can speed up development in Django by handling repetitive tasks such as boilerplate generation and debugging. However, this comes with a caveat – developers must remain critical and treat AI as a collaborator, not a source of truth. 
 For beginners, AI can be a powerful learning aid, but over-reliance can limit deeper understanding. Building projects, reading code, and actively solving problems remain essential for developing real expertise. 
 Highlight 5: The importance of open-source AI 
 The open-source AI ecosystem is expanding rapidly, bringing with it a growing landscape of models, datasets, and tools. 
 This openness drives collaboration, transparency, and innovation, making it easier for developers to experiment and build on existing work. At the same time, it introduces challenges around fragmentation and long-term sustainability. 
 As Merve Noyan, ML Engineer at Hugging Face, explained in her Open-Source AI Ecosystem session, platforms like Hugging Face play a key role in organizing this ecosystem and making it more accessible, while Python continues to connect tools, communities, and technologies. 
 Highlight 6: Context is key for effective AI agents 
 As AI systems become more advanced, the way they interact with their input data is becoming increasingly important. Tuana Çelik, Developer Relations Engineer at LlamaIndex, covered this in detail in her insightful Orchestrating Document-Centric Agents With LlamaIndex talk. 
 LlamaIndex enables developers to build document-centric AI agents that retrieve, index, and reason over large collections of information. By structuring how documents are ingested and queried, it provides the LLM with much more context for the text it is processing, helping produce more accurate, context-aware responses. 
 This is particularly valuable in knowledge bases and enterprise assistants, where understanding relationships between pieces of information is as important as accessing the data itself. 
 Highlight 7: How Polars is refining high-performance data processing 
 Polars is pushing Python data processing toward a more scalable, production-ready future, as Polars creator Ritchie Vink explained in his Towards Query Profiling in Polars session. 
 Its high-performance, lazy execution model allows queries to be optimized automatically behind the scenes. However, this level of abstraction can make it harder for developers to fully understand performance. 
 To address this, there’s a growing need for better tooling, particularly around query profiling. By exposing execution plans, memory usage, and bottlenecks, developers can make informed decisions and build more efficient data workflows. 
 With features like streaming execution, Polars is helping bridge the gap between local data processing and large-scale systems. 
 As Jodie highlighted in the recap discussion, this shift is bringing more advanced data concepts into everyday Python workflows. She commented, “It’s really interesting to see more big data ideas coming to local Python data processing.” 
 Highlight 8: The power of typing in modern Python 
 Typing in Python continues to evolve, with a growing focus on flexibility rather than rigid enforcement. Open-source Django projects creator Carlton Gibson shed more light on this during his talk, Static Islands, Dynamic Sea: Some Thoughts on Incremental Typing . 
 The talk highlighted how developers are increasingly adopting an incremental approach. By creating “static islands” within a dynamic codebase, they can improve reliability, maintainability, and tooling without sacrificing Python’s core strengths. 
 In our recap video, Will agreed with this sentiment, adding, “It doesn’t have to be all-or-nothing. We don’t have to turn Python into something that it’s not.” 
 This approach is particularly useful in large frameworks like Django, where typing can help define clearer boundaries while still preserving developer ergonomics. 
 Highlight 9: The Django renaissance: Debunking aging myths 
 Django remains a modern, actively developed framework, as Django Fellow Sarah Boyce revealed in her session, Django Has a Marketing Problem: Debunking the Myths That Won’t Die . 
 Many of the criticisms that it’s outdated or unscalable don’t reflect the current reality. In practice, Django continues to evolve and power a wide range of applications. 
 The challenge is less about Django’s capabilities and more about perception, as the Django community was called to champion its strengths, ongoing evolution, and real-world impact. 
 Shifting this narrative will be key to ensuring its continued relevance and adoption in the years ahead. 
 What’s next for Python Unplugged on PyTV ? 
 Python Unplugged on PyTV was our first step in reimagining what a fully online community conference can look like, and the response was incredible. 
 Looking at the numbers, more than 5,500 people joined us during the livestream. Since then, we’ve had a further 110,000 watch the event recording, showing just how global and engaged the Python community really is. 
 We’d love to bring Python Unplugged on PyTV back next year. What would you like to see more of? Who should we invite as speakers? Are there topics we didn’t cover that you’d love to explore? 
 Drop your suggestions in the comments and help shape the future of Python Unplugged on PyTV .
```

---

## 5. How to Make Code Highlighting-Friendly

- 日期: 2026-05-07 09:15
- 链接: https://blog.jetbrains.com/scala/2026/05/07/how-to-make-code-highlighting-friendly/

```
This article introduces the notion of highlighting complexity and provides recipes for making your code highlighting-friendly, resulting in faster, more efficient highlighting. 
 Code style is not just for style – it impacts the physical world! The benefits of highlighting-friendly code include: 
 Better responsiveness 
 Optimized CPU usage 
 Efficient memory usage 
 Cooler system temperatures 
 Quieter operation 
 Longer battery life 
 While monads are burritos, you shouldn’t be frying eggs on your laptop! 
 Consider highlighting complexity 
 Imagine you’ve written this function to compute Fibonacci numbers using naive recursion: 
 def fib(n: Int): Int =
 if (n <= 1) n
 else fib(n - 1) + fib(n - 2) It is predictably slow, but you wouldn’t blame Scala for that. The issue is more fundamental and not specific to the programming language. However, this doesn’t mean that the function cannot be made fast. There is a way to adjust the code so it outputs exactly the same sequence much more efficiently. 
 The same is true for highlighting code. If highlighting is slow, the IDE is not always to blame. Some code is inherently difficult to analyze. However, this doesn’t mean that highlighting cannot be fast. Minor code tweaks can make highlighting significantly more efficient , even if the code stays essentially the same. 
 So far, so good. However, while algorithmic complexity is “CS 101”, developers rarely think about highlighting complexity . (The two differ: Code might run slow but be easy to highlight, or run fast but be difficult to highlight.) Even if you study compiler construction, it’s primarily not about performance, and parts that are about performance refer to compilers rather than source code. Furthermore, batch-compiling code is not the same as editing code. 
 Following software engineering best practices may often speed up highlighting. It’s also useful to do in general: keeping your classes and methods small and focused, preferring clarity over cleverness, etc. However, these principles are mostly about cognitive complexity . In contrast to algorithmic complexity, cognitive complexity often correlates with highlighting complexity. Still, they are not the same and sometimes can differ significantly. 
 When writing code, you should also consider highlighting complexity. If you ignore algorithmic complexity, your code will perform poorly. If you ignore cognitive complexity, your code will be difficult to understand. If you ignore highlighting complexity, your code will take a long time to compile or highlight and will consume excessive resources in the process. 
 Good code should be good in all respects. Fortunately, the principles for making your code highlighting-friendly are simple and easy to apply in practice. (Most of the recipes are not Scala-specific and can be useful for other languages as well.) 
 Separate code into modules 
 Most Scala programmers divide code into packages, but fewer divide code into modules. There’s one and the same reason for both. 
 In contrast to a language like C, Scala supports packages, and most Scala projects naturally use them. Modules, however, are a concept of IDEs and build tools rather than the programming language, so they are used less often. Even the Java Platform Module System is mostly about compiled classes and JARs rather than source code. 
 Modules limit the scopes of bindings and introduce an explicit graph of dependencies – otherwise, any source file could, in principle, depend on any other source file. This limits the scope of incremental compilation and analysis, which makes compilation faster, reduces peak resource consumption, and allows modules to compile in parallel. 
 Likewise, modules improve the performance of highlighting – an IDE can search for entities and invalidate caches more efficiently. Moreover, this improves the UX by making autocomplete and auto-import more relevant, reducing clutter. Another benefit is that you can compile (or recompile) only part of a project when running an application or a unit test in one of the modules (even if other modules don’t compile cleanly). 
 Packages are often natural boundaries for modules. If there’s only a single module in your project, or if some modules are too large, consider extracting one or more packages into a separate module . Since the refactoring doesn’t affect packages as such, this should be backward-compatible. Furthermore, you can still package the classes into a single JAR – the refactoring is for the source code, but not necessarily the bytecode. 
 Note that you must use true modules – using multiple directories or multiple source roots is not the same thing. (See multi-project builds for sbt.) 
 Put classes in separate files 
 The Scala compiler doesn’t limit how many classes you can add to a source file (or how you name that file). This can be useful, but you shouldn’t overuse this capability. 
 If you modify only one class in a source file, the Scala compiler cannot compile that class separately – it has to compile the entire source file. The same is generally true for IDEs: You open a file rather than a class in an editor tab, which analyzes the entire file. (However, you can use incremental highlighting to overcome this limitation.) 
 Furthermore, when each class has a file with a dedicated name, it’s easier to find classes and navigate around the project, even without an IDE. You should put classes into corresponding files the same way you put packages into corresponding directories. 
 Another reason is import statements. While each class requires its own set of imports, defining multiple classes in a single file merges these imports and makes them common. This can slow down the resolution of references. (If there are many imports and imported entities that, in turn, depend on many imports, then there could be a combinatorial explosion.) 
 If you notice many relatively large classes in a single file, consider extracting classes into separate source files . It’s easy to do and doesn’t affect backward compatibility. (Obviously, companion classes and sealed class hierarchies should remain in the same file.) 
 Define classes in packages rather than objects 
 In Scala, packages and object s are similar, and there are even package object s! This makes it possible to put classes in object s rather than package s. However, there are good reasons to avoid that. 
 First, since each object is contained in a single source file, multiple classes in an object implies multiple classes in a file, which, as we’ve already seen, is not ideal. 
 Second, this also affects compiled code, not just source files. While every class is compiled to a separate JVM .class file, as if they were defined in a package , there’s only one outline for the object – pickles or TASTy. As a result, both the compiler and IDE have to process multiple classes even if they need to access only one. 
 Thus, you should normally define classes in package s rather than object s . Leave object s for methods, variables, and type s. (And in Scala 3, even top-level definitions can reside in a package .) 
 Favor small classes and methods 
 Yes, yes, you already know this. But there’s a twist. When you normally think of “small”, you often think of “simple”. For example, if a class contains only a few methods with descriptive names, the class looks simple, and you don’t have to analyze the code of these methods to understand what they do. 
 This luxury, however, doesn’t apply to compilers or IDEs. If you open the file, the entire contents will be analyzed, and if the methods (and consequently the class) are large, the analysis will consume time and resources. 
 Consider splitting large classes and methods into smaller ones, even if they are simple . For highlighting, “lines of code” matter; even a single class or method can be too much if it’s very large. 
 This also applies to generated sources: If a source file is generated and other sources depend on it, you don’t need to look into that code, but IDEs and compilers still do. When generating code, divide the output into smaller parts – files, classes, and methods; don’t mix everything into one blob. 
 Depend on interfaces rather than classes 
 It’s good to “program to an interface” in general, and this can also help with highlighting. 
 Suppose there is a large class with a few methods that comprise its API. Even if you access only the API, reading the source file requires parsing the entire class, including all the implementation details. And even if you specify the types explicitly, resolving the corresponding references requires processing many imports. 
 Therefore, if a class is very large, consider extracting an interface instead of referencing the class directly . 
 Avoid wildcard imports 
 Using named imports rather than wildcard imports is a well-known best practice. It makes code more readable – you can clearly see where symbols come from. It also makes your code more robust. (Otherwise, code might stop compiling after a library adds a class that conflicts with another imported class.) And there’s less clutter – autocomplete will show only relevant symbols that are actually in use. 
 Furthermore, named imports can speed up code analysis . When resolving identifiers, each wildcard import has to be checked, and import expressions might, in turn, depend on wildcard imports above. There might be imports from objects, which themselves depend on imports elsewhere. All of that is not limited to the file being highlighted. Even if your code depends only on signatures in other files, because paths in the type annotations are not absolute, the analysis still has to process imports in those files. 
 Wildcard imports are especially problematic for implicits . Because implicits are, well, implicit, and might require other implicits, searching for them can be computationally intensive. And if implicits are imported using a wildcard, then both the usage and the import are implicit. This complicates the task even more – not only does the analysis need to find some vague entity, but it also has to look in a blurry scope. 
 Therefore, prefer specific imports to wildcard imports . Convert existing wildcards to named imports. In Scala 2, consider importing implicits by name . Although given imports in Scala 3 are an improvement, they are effectively wildcard imports and thus rely on good library design. To be on the safe side, prefer by-type imports to plain given imports . (And if you’re designing a library, define implicits in a separate package or object.) 
 Prefer imports to mixins 
 It’s possible to use inheritance instead of imports. We can see this even in Java: Every TestCase is also Assert , so you can access methods such as assertEquals without having to import them. This might seem convenient. However, this is effectively a forced wildcard import, with all the usual drawbacks. It’s better to import Assert.assertEquals selectively (or import Assert.* , as an option). 
 Furthermore, the approach with subclassing or mixing in trait s is slower compared to regular wildcard imports. Analysis has to take inheritance and linearization, as well as overloading and overriding, into account. And if you modify the trait , classes that use it have to be recompiled. 
 If some definitions are effectively static, put them in an object rather than a trait , so that clients import rather than inherit them. 
 Declare classes and methods private 
 There are many good reasons to minimize the accessibility of classes and methods: to distinguish between API and implementation, to maintain source and binary compatibility, to prevent clutter in autocomplete, and to reduce cognitive load. 
 What’s less known is that declaring classes and methods private , whenever possible, improves the performance of compilation and highlighting . Incremental compilers don’t include private members when determining APIs and thus don’t need to store and compare them. In the process of resolving references, IDEs can skip inaccessible elements faster. When you write “Foo”, you already know which Foo is implied. However, you might be surprised by how much computation resolving a reference often involves. Declaring unsuitable Foo s inaccessible helps make analysis faster. 
 The Scala plugin can help by automatically detecting declarations that can be private . 
 Specify types of public or complex definitions 
 Each non-local definition should either be private or have a type annotation. Definitions that are accessible to clients comprise an API. APIs are boundaries of abstraction and thus must be explicit; clients shouldn’t have to study the implementation – the right-hand side – to understand the signature – the left-hand side. In contrast to implementations, APIs must be stable and must not depend on the contents of the right-hand side. Type annotations make APIs both explicit and stable. 
 Type annotations greatly help incremental computations. When signatures are stable, fewer classes need to be recompiled after a code modification. Likewise, more caches can be reused when you edit code in an IDE, making highlighting faster and reducing resource consumption. 
 Thus, it’s best to always specify the types of non-private members explicitly . Note that you should specify the type even if there’s overriding because the inferred type might be more specific, at least in Scala 2. (For example, if a superclass method returns Seq[Int] and the subclass method is just = List(1) , the type of the latter would be List[Int] , which might affect clients that use the subclass directly.) You should also specify the types of protected members , not just public ones – subclasses are also clients. (As an exception, you may omit types when the right-hand side is both simple and stable, e.g., a literal. That said, having the type spelled out explicitly is often better, both for humans and compilers.) 
 Furthermore, explicit types can benefit even private and local definitions. While an incremental compiler recompiles the entire file, an IDE can invalidate caches more gradually and within a narrower scope. Thus, add type annotations to private members if they are complex – this can make editing code more efficient. Also, specify the types of complex local variables . (Sometimes you may first need to extract a method or introduce a variable to specify the type.) 
 Code Style | Type Annotation in the Scala plugin requires type annotations for public and protected members – they are automatically added by refactorings and code generation, and are checked by the corresponding inspection. However, there are exceptions for simple expressions, and they are not required for private or local definitions, regardless of complexity. You can make these settings stricter to be on the safe side. 
 Favor standard language features over macros 
 The concept behind macros might seem tempting – you do computations at compile time rather than at runtime. However, “compile time” is also “highlighting time”, which is true regardless of whether you use a compiler or an IDE when editing code… unless you always write everything in one go, without any assistance. So, macros might interfere with writing and editing code , making feedback slower and consuming more resources. Note that this applies not just to defining a macro, which requires a feature flag, but also to using macros, which doesn’t require a feature flag. 
 Macros are rarely actually needed. Take, for example, Lisp: The syntax is very limited, and the language is dynamic, so no static analysis is performed anyway. Scala, however, is a very expressive language as it is, and it’s statically typed. In Scala, the standard language features are sufficient for most tasks. In such a case, macros only make static analysis, as well as understanding code, more difficult. Thus, when writing code, reach for the standard language features first: type parameters, implicit parameters, etc. Macros are supposed to be the last resort, not a go-to solution. 
 This can be generalized: Don’t use complex language features just “because you can”, only when they are really needed; prefer the least powerful solution that solves the problem. For more details on this topic, see Lean Scala by Martin Odersky. 
 Apply these principles to AI-generated code 
 Even if you use AI to generate 100% of your code, you still read that code. (Right?) Therefore, producing highlighting-friendly code is as relevant as ever – the code is generated in a data center but is highlighted on your machine. This also improves incremental compilation, reducing system load when using agents. Moreover, it prevents context stuffing (when a model loads irrelevant information), which improves accuracy and reduces costs. 
 The first thing you can do is lead AI by example , because models tend to propagate existing conventions and coding styles. In a new project, you can explicitly add recommendations to AGENTS.md . Last but not least, you can always refactor your code , whether it’s written by a human or AI. 
 Summary 
 That said, the performance of your IDE is also important. We’re constantly working on improving the performance of both IntelliJ IDEA and the Scala plugin, and there are tips for improving performance that you can apply in practice. However, just as no amount of compiler optimizations can fix the example with naive recursion, highlighting may sometimes require assistance from your side. 
 As with everything, highlighting complexity is not the only factor; you need to balance different considerations. But often, there’s no contradiction: Clean code improves highlighting complexity, and improving highlighting complexity results in cleaner code. In any case, it’s useful to always consider highlighting complexity and having the recipes at hand . 
 For more details, see the corresponding ticket in YouTrack . It also lists features that can help you apply the refactorings more easily. If you find them useful, vote for the tickets so we know there is demand. 
 If you have any questions, feel free to ask us on Discord . 
 Happy developing! 
 The Scala team at JetBrains
```

---

## 6. IntelliJ IDEA 2025.3.5 is Out!

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

## 7. Developer Ecosystem Survey 2026 – Take Part in One of the Largest Developer Studies

- 日期: 2026-05-06 14:21
- 链接: https://blog.jetbrains.com/research/2026/05/developer-ecosystem-survey-2026-take-part-in-one-of-the-largest-developer-studies/

```
Since 2017, we’ve been checking in with developers around the world to better understand how the industry is evolving and where software development is headed next. 
 This year marks the tenth edition of the Developer Ecosystem Survey , and we’d love for you to take part. 
 When we launched the first survey, Kotlin was just emerging, and AI coding tools were still years away. Today, they are part of everyday development. 
 Every year, tens of thousands of developers share their experiences, helping create one of the most comprehensive pictures of the tools, technologies, and challenges shaping modern development. The survey insights are widely used across the developer community – from researchers and industry analysts to teams building developer tools. 
 Whether you’re building large-scale systems, mobile apps, games, or experimenting with side projects, your perspective matters . 
 Set aside about 30 minutes , grab a drink, get comfortable, and tell us about your experience as a developer. 
 TAKE THE SURVEY 
 Have your say and get a chance to win one of these prizes: 
 MacBook Pro 16″ 
 USD 1,000 Amazon Gift Card or alternative 
 USD 150 JetBrains Merchandise Store voucher 
 One-year JetBrains All Products Pack subscription 
 A guaranteed 30% discount for an individual JetBrains license 
 The more developers who participate, the clearer the picture we can build of today’s software development ecosystem. When you’re done, you’ll receive a personal referral link to share with friends and colleagues. The participants who bring in the most responses via their referral link will receive an additional prize . 
 As always, we’ll publish the results in detailed infographics and reports , and we’ll release the anonymized raw data for anyone who wants to explore the findings further. 
 Thank you for helping us capture a snapshot of where development is headed in 2026 – and for being part of the global developer community that has supported this initiative for the past decade.
```

---

## 8. Stop Sending IDE-Catchable AI Code Errors to Review

- 日期: 2026-05-05 13:16
- 链接: https://blog.jetbrains.com/ai/2026/05/stop-sending-ide-catchable-ai-code-errors-to-review/

```
AI coding tools might have handed your developers a productivity gain, but they’ve created a problem for your code review process. Pull request volume is up significantly, and the code arriving for review carries error patterns that weren’t common before generative AI. Yet it’s the same people with the same working hours who are in charge of reviewing it all. 
 Most engineering leaders are still working out what to do about it. According to our State of Developer Ecosystem 2025 survey of more than 24,000 developers, the dominant pattern is ad hoc: Developers simply use AI tools as they see fit with little governance from above. 
 Studies report that around 20%–25% of AI code hallucinations are detectable through automated structural and static analysis. Those checks can take place in the environment where the code was written, before a pull request is raised. No governance framework required, no new process layer. 
 The case is straightforward: your reviewers’ judgment is a finite resource. Every structural error that reaches review consumes some of it. Every structural error caught earlier doesn’t. 
 Code review is a decision process – AI just added more decisions 
 DX’s Q4 2025 data on 51,000 developers showed that daily AI users merge 60% more pull requests per week than light users. A 2025 randomized controlled trial across three enterprise companies found that developers who had access to an AI coding assistant completed 26% more tasks per week than those in the control group without access. 
 More code arriving at review means more decisions per reviewer per day. That pressure has a measurable cost. Decades before AI coding tools entered the picture, researchers found that review rate was a statistically significant factor in defect removal effectiveness, even after controlling for developer ability. More time spent per line of code reviewed was consistently associated with a greater number of defects found. 
 Skill alone couldn’t compensate for rushing. Better tooling should – but tools, including modern AI-assisted ones, have yet to close the gap between what a reviewer sees and what a reviewer needs to know: 
 A 2024 study of a company’s AI code review tool found that even with 73.8% of automated review comments acted on, pull request closure time still increased 42%. The commentary was useful, but the burden was not reduced. 
 In 2025, an empirical study of 16 AI code review tools across more than 22,000 comments discovered that their effectiveness varied widely. 
 A January 2026 study revealed that effective review requires much more than a snapshot of what code was added or removed. Reviewers move between issue trackers, documentation, team discussions, and CI reports to understand what a change means in the codebase they are reviewing. 
 Review tools continue to leave it to developers to form the big picture. AI has added to that gap, not closed it. 
 AI is sending a different kind of code to review 
 A 2025 analysis of more than 500,000 code samples found that AI-generated code carries a distinct error profile: unused constructs, hardcoded values, and higher-risk security vulnerabilities that are more common than in human-written code. A separate 2025 study identified defect categories with no real equivalent in human-written code. 
 The error profile is challenging enough. But the way reviewers engage with AI-generated code compounds it. A 2026 study found a reviewers’ blind spot: AI-generated pull requests containing nearly twice the code redundancy drew fewer negative reactions from reviewers than human-written ones. Surface-level plausibility appeared to reduce critical engagement. 
 More volume. New error types. Less scrutiny. What does the delivery data show? 
 A 7.2% reduction in delivery stability for every 25% increase in AI adoption, according to DORA . They attributed this pattern partly to larger changesets: More code generated means bigger batches at review, and bigger batches have consistently predicted instability. Size is the signal. The defect profile and the scrutiny data suggest what is behind it. 
 Have machines catch what machines can 
 Automated structural and static checks don’t involve human judgment calls. But who is putting those checks in place? Even at organizations with mature engineering practices, structural screening didn’t emerge adequately at the individual level: 
 Google , running LLM-powered code migrations across its codebase, found that reviewers needed to revert AI-generated changes often enough that the organization made a deliberate investment in automated verification to reduce that burden. 
 Uber , processing tens of thousands of code changes weekly, found that AI-assisted development was overloading reviewers and built an automated review system that runs before human reviewers engage. 
 In both cases, the fix required an organizational decision. Google and Uber chose to do this at the pipeline level – upstream of pull requests. 
 The right development environment can catch the same category of errors earlier. 
 Put “no-excuses” structural analysis before the pipeline 
 According to the 2025 Stack Overflow Developer Survey , developers use an average of 3.6 development environments. Which ones to use is typically their call. They know their languages and workflows. 
 As an engineering leader, you should know whether at least one of those environments is running deep, no-excuses checks of AI-generated code against what actually exists across the entire codebase in all languages. Many development environments do not; they rely on language-by-language approximations instead. 
 The distinction matters more at the organizational level than at the individual level. A developer working in a single language with a well-configured approximation-based setup may not feel the gap. But the quality of structural analysis across a team is only as consistent as the weakest setup in it. 
 The same studies on AI code hallucinations found that roughly 44% involve errors that no automated check reliably surfaces. That is more than enough for your reviewers to contend with. Protect their capacity for only what they can handle. 
 For every major language your team uses, there is a JetBrains IDE available to maintain a deep structural model of your codebase. Any code that lands in the editor – regardless of which AI tool produced it – is checked against that model. For teams that want enforcement both before and in the pipeline, Qodana extends that same inspection depth into CI/CD. 
 Your reviewers’ judgment is the resource. Structural screening is how you protect it. 
 See how JetBrains for Business supports that symbiosis at scale.
```

---

## 9. Java Annotated Monthly – May 2026

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

## 10. What is dogfooding? How JetBrains builds better developer tools

- 日期: 2026-05-05 08:59
- 链接: https://blog.jetbrains.com/life-at-jetbrains/2026/05/dogfooding-at-jetbrains/

```
Dogfooding in software development means using your own products to build, test, and improve them. At JetBrains, it’s a core part of how we create developer tools like IntelliJ IDEA, YouTrack, and Rider. 
 We don’t rely on assumptions or abstract user personas. We use our tools every day in real workflows, which keeps us close to the problems developers actually face. 
 Our CEO, Kirill Skyrgan, puts it: 
 “You can only build truly great software if you use it yourself. Every feature and every decision comes from firsthand experience.” 
 What is dogfooding in software development? 
 Dogfooding — short for “eating your own dog food” — means putting your product through the same real-world use as your customers. 
 Our engineers, designers, product managers, and even technical writers build their daily workflows around JetBrains tools. We write code in IntelliJ IDEA and track issues and internal project statuses in YouTrack . 
 It’s not about internal compliance – no one forces anyone to use a product. It’s about trust. We use our tools because they help us do our jobs better, and when they don’t, we fix them. 
 This direct connection between building and using keeps us grounded. We don’t chase trends or design for hypothetical users. If something slows us down, we know it likely affects thousands of developers too. 
 Benefits of dogfooding: Faster feedback and better software 
 Dogfooding gives us what every product company dreams of: immediate, unfiltered feedback. 
 Instead of waiting weeks for customer reports, our developers spot issues as they code. 
 When a feature feels unintuitive or a shortcut doesn’t work as expected, the fix often starts that same day or even the same hour. 
 This tight feedback loop turns every JetBrainer into a quality advocate. It shortens the distance between the problem and the solution, helping us catch issues long before they reach users. It also fosters empathy. Using the tools ourselves means we understand not only what users say, but what they experience. We feel the slowdowns, the friction points, and the “why is this like that?” moments – and we care enough to address them. 
 “Those thousands of tiny corrections made over time are what turn a good product into a great one,” Kirill shared. “They come from people who use the tool every day and want it to be better, not for KPIs, but because they genuinely care.” 
 Examples of dogfooding at JetBrains 
 Dogfooding shapes every JetBrains product, often long before release. 
 Rider: From unstable to production-ready 
 One of the best examples of dogfooding in action is Rider , our .NET IDE. Back in 2016, when it was still unstable and full of rough edges, JetBrains developers began using it for their work long before it was officially released. Some days, you couldn’t even type because the editor would crash. But instead of giving up, teams fixed the issues they encountered on the spot. 
 That perseverance turned Rider from an experiment into a world-class IDE. The same principle has shaped countless JetBrains products since. 
 YouTrack: Built and managed in itself 
 Another case is the YouTrack team, who use their own issue tracker to manage every internal project and improvement flows for the product itself. That constant internal use surfaces edge cases and drives continuous refinement. 
 Junie: Shaped before users ever saw it 
 Junie , one of our newer tools, was used internally months before its closed beta. 
 The team started using Junie internally in December 2024, even before it reached closed Beta. From the very beginning, internal feedback played a major role in shaping how the product evolved. Team members quickly identified things that didn’t feel quite right, from small interface quirks to moments where Junie didn’t respond as expected. This early insight helped the team refine the experience long before anyone outside JetBrains ever saw it. 
 One particularly important piece of feedback was that Junie didn’t explain enough about what it was doing. That lack of clarity made some interactions feel confusing. Because the team experienced this themselves, they were able to rethink the product’s communication early on and make it more transparent and helpful. 
 Another area that benefited enormously from dogfooding was Junie’s connection with different work environments used throughout the company. JetBrainers rely on a wide variety of setups in their daily work, and using Junie across these revealed many edge cases the team wouldn’t have spotted otherwise. Each of these discoveries turned into improvements – hundreds of them. 
 How dogfooding improves developer experience and ownership 
 Dogfooding doesn’t just improve products — it changes how teams work. When you use what you build, the distinction between “developer” and “user” disappears. There’s no handoff, no abstraction. 
 That perspective creates stronger ownership. Decisions have immediate, visible impact. Teams see the results of their work in real time. 
 Dogfooding AI tools at JetBrains 
 Our teams use AI-assisted features internally long before release, testing what feels useful, what feels distracting, and what actually improves productivity. 
 This helps us avoid building AI for the sake of trends. We build it because we need it — and we refine it until it works in real development environments. 
 Why dogfooding matters for building better software 
 Dogfooding is how we make sure our tools meet the same high standards our users expect. It keeps us honest, motivated, and connected to the work we do. It’s not always comfortable – finding bugs in your own product rarely is – but it’s the most authentic way we know to build software that truly makes a difference. 
 This is what has kept JetBrains thriving for over two decades: a culture of doers who build, test, and improve from the inside. 
 As one of our technical leads put it: 
 “If I start any new project, the first milestone for it is definitely dogfooding. It’s one of the most important quality gates for the product and a crucial source of high-quality feedback.” 
 Build what you believe in 
 Dogfooding isn’t just a process we follow – it’s a fundamental part of how we work. It helps us stay close to our mission, keep improving, and make sure that when developers everywhere open a JetBrains tool, it feels like it was built by someone who truly understands them. 
 Because it was. 
 If this way of working resonates with you, if you care about the craft, and prefer solving real problems over just chasing trends — you’ll likely feel at home here. Check out our careers page for open roles!
```

---

## 11. Meet the Finalists: JetBrains x Codex Hackathon

- 日期: 2026-05-04 16:12
- 链接: https://blog.jetbrains.com/ai/2026/05/meet-the-finalists-jetbrains-codex-hackathon/

```
Put a capable coding model inside a developer’s primary workspace, and the IDE stops being a place where you write code. It becomes a place where you direct an agent, watch how it reasons, manage what it pays attention to, and decide when its output is worth shipping. That was the defining theme of the inaugural JetBrains x Codex Hackathon: across roughly 40 submissions over a single weekend, teams explored what it actually means to build with AI natively inside the IDE – not bolted on top of it. The six finalists came up with some of the most compelling answers. 
 🥇 First Place: hyperreasoning – Aditya Mangalampalli 
 Most coding agents call the model once and hope for the best. As Aditya puts it: “LLMs spend a lot of time thinking in circles.” Hyperreasoning replaces the single shot with something closer to a search: the system drafts several possible approaches to a task, then a learned controller decides which to expand, which to cut, and which to verify against tests. Compiler errors and failing tests feed back into how the controller weighs its options. 
 Inside the IDE, a tool window renders the search live, so you can watch which paths the controller explored before settling on one. The argument the project makes is that a smaller local model wrapped in this kind of verified search loop can hold its own against much larger frontier models at meaningfully lower cost — with the IDE serving as the place where reasoning becomes visible and directable, rather than a black box that returns code. 
 🥈 Second Place: Scopecreep – Bhavik Sheoran, Kenneth Ross, Roman Javadyan, Joon Im 
 Hardware bring-up is a tool-juggling exercise: schematic viewer in one window, vendor apps for the oscilloscope and power supply in others, a terminal talking to the device, a spreadsheet collecting results. Scopecreep collapses that into a single JetBrains tool window. Hand it a circuit schematic and an agent works through testing the board – picking signals worth measuring, capturing the readings, and producing a report. 
 The design choice worth noticing: when the agent decides a probe needs to be placed, the session pauses and shows the engineer exactly where to put it. The engineer places the probe physically and clicks Resume. It’s the right call for real instruments on a real bench – autonomous, where a computer can be trusted, human-in-the-loop, where the work touches the physical world. 
 🥉 Third Place: mesh-code – Ayush Ojha, Coco Cao, Kush Ise, AL DRAM 
 Switch machines mid-task, and your coding agent starts over. mesh-code fixes that by giving agents shared memory of an in-progress project – what’s been tried, what’s been decided, what’s still pending – so a session that begins on one laptop can continue from another, with whichever agent happens to be available. Codex is one of the agents that can plug in. 
 Latent Signal – Periscope 
 Long agent sessions accumulate dead weight: tool outputs nobody needs anymore, dead ends, context that was useful ten turns ago and isn’t now. Periscope, built on Wes McKinney’s open-source agentsview, is a JetBrains plugin that shows what’s actually filling up an agent’s working memory turn by turn – and recommends what to do about it, whether that’s continuing, rewinding to a better branching point, compacting, forking, or handing off entirely. It works with Codex and most other coding agents, and everything stays local. 
 SecureLoop – Abhiram Sribhashyam, Rahul Marri, Peyton Li 
 Security incident response is still mostly copy-paste: stack trace into a chat window, repo context explained by hand, a fix written and committed in the hope it’s safe. SecureLoop turns that into a controlled loop inside JetBrains. When something breaks in production, the agent gathers the relevant code, the project’s security rules, and the state of its dependencies, then asks Codex for a structured diagnosis and a proposed fix. That fix runs through automated checks before any pull request opens. 
 The PR opens automatically. The merge does not. SecureLoop surfaces everything that informed the decision – the diff, the policy it bumped into, the test that proved the patch – inside the IDE for the developer to approve or reject. As the team put it: “Codex fully makes the PR ready for you, and it remains human-in-the-loop where you have to approve or deny.” 
 The team’s bigger thesis is a security-policy.md file that lives in the repo alongside README.md, spelling out a project’s specific rules for handling secrets, errors, and risky patterns. Coding agents read it before suggesting changes, so the question stops being “what’s a good fix?” and becomes “what’s an acceptable fix under this codebase’s rules?” 
 Pinpoint – Het Patel 
 Frontend feedback delivered through a chat window is unavoidably vague. “Move that element” or “change that color” leaves the agent guessing which element you actually mean. Pinpoint takes that piece of the ambiguity off the table: developers drop pins directly on a live page, attach a comment to each, and send the whole batch to the agent with precise on-page context attached. The agent now knows exactly which element you meant – even if it still has to figure out what change you want. 
 The project ships in two pieces: one for annotating web pages in a browser, and a desktop companion for marking up anything visible on screen – useful when the interface in question isn’t a web page. 
 What the finalists show 
 Looking across these six projects, a clear pattern emerges. Codex embedded in the IDE isn’t just a faster way to write code – it’s a reasoning layer you can watch think, a structured output engine you can direct, a participant in workflows that span hardware instruments, production alerts, shared session state, and context windows. And the IDE becomes the place where all of that comes together: visible, controllable, and version-controlled. 
 That’s the possibility these teams spent a weekend proving out, and it’s only the beginning. 
 View the full submission gallery .
```

---

## 12. We Gave Agents IDE-Native Search Tools. They Got Faster and Cheaper.

- 日期: 2026-05-04 13:01
- 链接: https://blog.jetbrains.com/ai/2026/05/what-happens-when-you-give-agents-ide-native-seach-tools/

```
We ran the same coding tasks with and without prebundled tooling, across multiple models and languages. Here’s what changed. 
 Eval-driven development 
 IDE-native search reduced latency, cost, and budget overruns. 
 The comparison below uses paired task-level deltas. Aggregate medians and totals are shown for orientation. Budget overruns are tasks that exceeded the USD 0.50 per-task cap. 
 8.33% Median latency reduced 83.11s → 79.03s 
 16.44% P95 latency reduced 268.71s → 213.17s 
 5.60% Total cost reduced USD 44.17 → USD 41.67 
 33.28% Budget overruns reduced 6.67% → 4.44% 
 Why We Built This 
 When coding agents search code, they default to shell tools. grep and find work, but they’re blind to project structure, symbol boundaries, and language semantics. The agent burns tokens sifting through noisy output and making follow-up calls to narrow things down. 
 So we tried something obvious: what if the agent could use the IDE’s own search instead? 
 We built a prebundled skill that pairs a search prompt with a unified MCP tool. One tool, four modes: file search, text search, regex, and symbol lookup. A universal router dispatches calls to the right backend. 
 MCP Tools 
 Functions the agent calls via an MCP server during task execution. IDE-native tools can tap into indices, ASTs, and project models that shell tools cannot see. 
 Skills 
 Packaged agent behaviors: a prompt plus orchestration logic. A skill can work on its own, use tools, or ship bundled with the tools it needs. 
 Nothing ships by default until the eval says it should. We tested four different configurations of this tooling before picking one. 
 Methodology 
 The eval pipeline spins up an MCP server alongside the IDE so the agent has access to the configured tools and skills. We run identical coding tasks with and without tooling, then compare with paired delta analysis. 
 We track four things: quality, latency, cost, and budget discipline. Quality asks whether all tests passed. Latency tracks median and P95 task time. Cost converts token consumption into dollars. Budget discipline tracks how often a single task exceeds the USD 0.50 budget cap. 
 We report improvement deltas only when they pass our significance threshold: p < 0.05, paired test with 95% confidence intervals. Metrics without a significant change are either omitted from the charts or called out explicitly. We tried four configuration variants, selected the one with the best latency and cost tradeoff, then re-ran it on different models and languages to check that the results held. 
 Eval frame 
 Same tasks, same grading, one controlled difference. 
 Quality All-tests-passed rate, checked before performance claims. 
 Latency Median and P95 task duration, compared with paired deltas. 
 Cost Token use converted to dollars across the task set. 
 Budget discipline Share of tasks exceeding the USD 0.50 single-task cap. 
 Results 
 The selected configuration was a prebundled search skill plus a unified IDE-native tool and universal router. Compared with the no-tooling baseline, it reduced latency and cost without producing a statistically significant quality change. 
 Baseline vs. tooling 
 Absolute metrics moved in the right direction. 
 Median latency 
 Baseline 83.11s 
 With tooling 79.03s 
 P95 latency 
 Baseline 268.71s 
 With tooling 213.17s 
 Total cost 
 Baseline USD 44.17 
 With tooling USD 41.67 
 Budget overruns 
 Baseline 6.67% 
 With tooling 4.44% 
 Budget overruns 
 33.28% 
 P95 latency 
 16.44% 
 Median latency 
 8.33% 
 Total cost 
 5.60% 
 No statistically significant change in quality. All shown deltas passed the significance threshold. 
 Trace snapshots 
 The difference is visible in the agent’s path through the project. 
 These are shortened traces from cases that improved in both time and cost. The baseline spends more steps discovering context; the prebundled setup gets to the relevant files faster. 
 Service comments and replies 
 prompt Update service and controller layers for comments and replies. before: no prebundled IDE search agent> list files -> search x2 -> list files x2 agent> jar inspect x5 -> javap -> jar inspect -> javap x5 agent> curl download -> decompile -> search -> find files x2 agent> read 9 files -> edit file x8 -> respond time: 472s after: prebundled skill and unified search agent> read SKILL.md -> search x3 -> read 5 files agent> read FeatureController.java -> read 4 files agent> edit file x2 -> respond time: 127s 
 Jackson key deserializer 
 prompt Preserve detailed error messages from a custom key deserializer. before: broad code walk agent> list files -> search x2 -> read README.md agent> search x5 -> read DeserializationContext.java agent> search x4 -> read StdDeserializer.java agent> search -> read DeserializerCache.java agent> read MapEntryDeserializer.java -> read JsonMappingException.java agent> edit file -> respond time: 150s after: targeted search agent> read SKILL.md -> search x3 agent> read MapDeserializer.java agent> read StdKeyDeserializer.java agent> read DeserializationContext.java agent> edit file -> respond time: 34s 
 Configuration Explorer 
 We tested four tool configurations before choosing the final shape. Lower latency and lower total cost are better, so the lower-left corner of the plot is the target. 
 Configuration search 
 The selected option had the best latency while preserving cost reduction. 
 Median latency, 78s to 84s Total cost, USD 39.50 to USD 45.00 
 Baseline 4 Search Tools Unified Search Tool 4 Tools + Router Unified Tool + Router 
 Cross-Model Validation 
 We re-ran the experiment with GPT 5.4 on Java and Kotlin codebases. The pattern holds: latency and cost both drop. Kotlin saw the biggest cost improvement, with total cost falling 13.48%. 
 Cross-model check 
 The effect held beyond the original run. 
 Codex 5.2 
 Median latency 8.33% 
 Total cost 5.60% 
 P95 latency 16.44% 
 GPT 5.4, Java 
 Median latency 3.75% 
 Total cost 4.07% 
 P95 latency 13.00% 
 GPT 5.4, Kotlin 
 Median latency 6.92% 
 Total cost 13.48% 
 P95 latency not significant 
 Missing bars mean that metric was not statistically significant for that model and language. 
 How Models Adopt Tooling 
 Codex sends 91% of its search calls through the new IDE-native tool. Claude is a different story: Opus uses it for about half its searches, and Haiku only 28%, preferring grep and find instead. 
 This makes sense. Claude already has strong built-in code search, so it leans on what it knows. Codex doesn’t, so it grabs the better tool when one is available. The takeaway: prebundled tooling fills gaps. Where the model already has good search, it adds less. Where search is weak, it makes a real difference. 
 Tool adoption 
 Models do not use new tools at the same rate. 
 Codex 
 91 8 1 
 Claude Opus 
 53 28 19 
 Claude Haiku 
 28 33 39 
 IDE Search grep find 
 What’s Next 
 The eval pipeline works. Now we’re using it. 
 We’re running the same experiment on smaller models next. Our hunch is that they’ll benefit even more, since they have less built-in search capability to fall back on. 
 The current results are strongest on Java and Kotlin. We’re expanding to Python, .NET, and TypeScript with bigger sample sizes. 
 Meanwhile, the winning configuration is being prepared for the integrated IntelliJ IDEA MCP Server, so agent sessions can use IDE-native tooling when the server is enabled. 
 The next step is to turn this feature on by default in upcoming AI Assistant plugin updates. 
 Want to try it before the default rollout? 
 Set these registry keys to true : llm.chat.agent.codex.mcp.idea , llm.chat.agent.skills.settings.enabled , and llm.agents.contrib.bundled.skills.sync.enabled . 
 In AI Assistant, choose Codex for the best results. 
 Ask the agent to find something across the current project. 
 Measure first, ship second, keep measuring after. That’s the whole approach.
```

---
