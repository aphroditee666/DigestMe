# Visual Studio Blog

> 分类: 大厂技术博客
> URL: https://devblogs.microsoft.com/visualstudio/feed/
> 抓取: 10 篇

---

## 1. TypeScript 7 Beta Now Enabled by Default in Visual Studio 2026 18.6 Insiders 3

- 日期: 2026-04-30 17:08
- 链接: https://devblogs.microsoft.com/visualstudio/typescript-7-beta-now-enabled-by-default-in-visual-studio-2026-18-6-insiders-3/

```
TypeScript 7 Beta Now Enabled by Default in Visual Studio 2026 18.6 Insiders 3 
 In Visual Studio 2026 18.6 Insiders 3 we have updated the built-in TypeScript SDK to TypeScript 7 Beta (native preview) . The TypeScript SDK provides the compiler and language service used for TypeScript and JavaScript support in Visual Studio. This update impacts any project that uses the built-in SDK, including TypeScript projects, ASP.NET Core projects with npm packages, and any TypeScript or JavaScript files you are editing. If your project doesn’t have a specific TypeScript version installed, Visual Studio will use the new native compiler by default. In this post we will go over what this change means for you, how to use a different version of TypeScript if needed, and the known issues we are currently working on. You can download the latest Insiders release with the link below. 
 Download Visual Studio 2026 Insiders 
 What is the TypeScript 7 native preview? 
 TypeScript 7 is a native port of the TypeScript compiler and tools . This is a significant change that brings native execution speed and shared-memory parallelism to the TypeScript compiler and language service. We have seen compile time improvements of up to 10x for large code bases, along with substantially reduced memory usage. If you are working with large TypeScript or JavaScript projects, you should see a noticeable improvement across your entire development experience. 
 In addition to faster compile times, the TypeScript language service has significant performance improvements as well. We have seen that the time to load projects has decreased roughly 8x. The improvements are not limited to load times; you should see a general speed improvement across the board with any features which interact with the TypeScript language service. Some of the Visual Studio features that benefit from these improvements include. 
 IntelliSense and completions. Code completions and parameter info should appear faster, especially in large projects where you may have previously noticed a delay. 
 Find All References. Searching for references across your solution is significantly faster. 
 Go to Definition. Navigating to definitions is more responsive. 
 Error diagnostics. Squiggles and error lists update more quickly as you type. 
 Project load times. Opening TypeScript and JavaScript projects in Visual Studio should be noticeably faster, with load times decreasing by roughly 8x. 
 If you are working with large code bases, you should see a noticeable improvement to your entire development experience. You will spend less time waiting for the IDE to respond and more time being productive working on your applications. 
 For more details on TypeScript 7 and the performance improvements, see the Announcing TypeScript 7.0 Beta blog post. 
 Using a different TypeScript version 
 Visual Studio ships with a built-in version of the TypeScript compiler and language service for cases where the project doesn’t specify a specific version to be used. Starting with this release, that built-in version is TypeScript 7 Beta. If you prefer to use a different version, you can install it in your project and Visual Studio will always use the project-local version over the built-in one . 
 Disabling TypeScript 7 native preview 
 If you want to go back to using the previous TypeScript language service, you can disable the native preview in Visual Studio. Go to Tools > Options > Preview Features and search for “native preview”. Uncheck the Enable JavaScript/TypeScript Native Language Service Preview option and restart Visual Studio. 
 Using TypeScript 6.x (GA) 
 To use the current stable release, install the typescript package in your project. 
 npm install -D typescript@^6.0.0 Using a specific TypeScript 7 native preview version 
 If you want to pin to a specific version of the native preview, install the @typescript/native-preview package. 
 npm install -D @typescript/native-preview@beta In both cases, Visual Studio will detect the version in your node_modules and use that instead of the built-in SDK. 
 Known issues 
 TypeScript 7 brings significant performance improvements to Visual Studio, and we are continuing to refine the experience. Below are the known issues that we are actively working on. This is not an exhaustive list. 
 IntelliSense. You may notice completions not appearing in some cases. In .cshtml files, the TypeScript completion list may not appear inside a <script> tag. When accepting a completion for the last argument of a function, the closing parenthesis may be removed. Pressing Ctrl+Space can work around this. 
 Code Actions & Refactoring. Quick fixes (Ctrl+.) are not available yet. Only Copilot AI-based suggestions may appear. The Organize Imports command (Ctrl+R, Ctrl+G) is also not available. 
 Navigation & Search. The navigation bar dropdowns at the top of the editor do not show document symbols. Find All References (Shift+F12) shows a flat list without semantic grouping (read/write/declaration), and cross-file references may be incomplete. Code search results may show mismatched titles and descriptions. 
 CodeLens. Reference counts (e.g., “19 references”) do not appear above interface and class declarations. 
 Hover tooltips. Hover tooltips are missing the symbol icon and have different text coloring compared to the previous language service. 
 Snippets. Insert Snippet (Ctrl+K, Ctrl+X) does not work in JavaScript files. 
 JSDoc. Typing /** above a function with parameters does not auto-generate the JSDoc template with @param entries. 
 Formatting. Unchecking “Format on open block {” in Tools > Options > Text Editor > JavaScript/TypeScript > Formatting does not take effect. 
 Task List. If a TypeScript file contains both a TODO comment and a variable named “TODO”, the Task List may incorrectly show duplicate tasks. 
 File and folder rename. Renaming a file or folder in a TypeScript project does not consistently update import paths in other files. 
 File watching. When files are modified outside of Visual Studio, changes are not detected until the file is opened and modified inside the IDE. Errors from external edits will not appear in the Error List. 
 We appreciate your feedback as we work toward full parity. 
 Reporting feedback 
 If you have feedback on the TypeScript compiler, or language service, the best place to file feedback is the typescript-go GitHub repo . 
 If you are running into an issue that is specific to Visual Studio, you can share feedback with us via Developer Community : report any bugs or issues via report a problem and share your suggestions for new features or improvements to existing ones. 
 We would love if you could try out the new experience and let us know how it’s working for you. Please try it out and share your feedback with us. 
 The post TypeScript 7 Beta Now Enabled by Default in Visual Studio 2026 18.6 Insiders 3 appeared first on Visual Studio Blog .
```

---

## 2. SDK-Style Support for Extension Projects

- 日期: 2026-04-29 14:00
- 链接: https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/

```
Starting in Visual Studio 18.5 , you can create and build Visual Studio extensions (VSIX) using an officially supported SDK-style project. This brings VSIX projects into the modern build and deployment pipeline, improving incremental build performance and making the build → deploy → debug workflow more reliable. Install the Visual Studio extension development workload to get the templates and tooling and try it out for yourself! 
 Note: Extensions written using the modern VisualStudio.Extensibility framework already supports SDK-style projects today. This update extends the same SDK-style experience to VSSDK-based Visual Studio extensions. 
 What We Are Adding: 
 Official SDK-style support for projects that produce VSSDK-based extensions. 
 Build time reductions of up to 75%! We’ve added end-to-end incremental build support including Fast Up To Date Check and up to date deployment logic. Through internal adoption, we see a reduction of up to 75% in build time in large solutions for small changes or changes confined to a single sub project. 
 Updated in-box templates: SDK-style by default, with the familiar project items (tool windows, classifiers, commands, etc.). 
 Project Usage 
 Creating a project is done the same way you are used to, using the “VSIX Project” or “Empty VSIX Project” template: 
 This will yield a much more compact csproj than before: only 20 lines: 
 <Project Sdk="Microsoft.NET.Sdk">

 <PropertyGroup>
 <TargetFramework>net472</TargetFramework>
 <Nullable>enable</Nullable>
 <LangVersion>14</LangVersion>

 <!-- VSIX settings -->
 <VSSDKBuildToolsAutoSetup>true</VSSDKBuildToolsAutoSetup>
 <VsixDeployOnDebug>true</VsixDeployOnDebug>
 <GeneratePkgDefFile>true</GeneratePkgDefFile>
 </PropertyGroup>
 <ItemGroup>
 <ProjectCapability Include="CreateVsixContainer" />
 </ItemGroup>

 <ItemGroup>
 <PackageReference Include="Microsoft.VisualStudio.SDK" Version="17.14.40265" ExcludeAssets="runtime" />
 <PackageReference Include="Microsoft.VSSDK.BuildTools" Version="18.5.38461" />
 </ItemGroup>
</Project> Does it impact my extension? 
 If you create a new extension, you will automatically get full SDK-Style support. 
 Your existing MPF style extension will continue to work should you choose not to migrate. This update adds an official SDK-style option; it doesn’t force a conversion. 
 You can update your project to an SDK-style project file to take advantage of these features. 
 Vsixmanifest files included in SDK-style projects now open by default in the XML editor. The old designer is still available through the ‘Open With’ menu. 
 Migration In Brief 
 I migrated an extension from Mads Kristensen as an example: Convert to SDK-style project by matthew-j-clark · Pull Request #6 · madskristensen/SelectedWhitespace · GitHub 
 If you have any XAML, you need to add: `<UseWpf>true</UseWpf>`to your csproj. 
 You must mark your extension as deployable in your SLN or SLNX file if you want it to deploy when you hit F5. You can do this in your SLNX like this: <Project Path="src/SelectedWhitespace.csproj">
    <Deploy Solution="Debug|Any CPU" />
  </Project> 
 When available, you can do this in the project configuration: 
 <VSSDKBuildToolsAutoSetup>true</VSSDKBuildToolsAutoSetup> will setup most sensible defaults for you and reduce the size of your csproj. This will setup options like CreateVsixContainer as true, and the legacy DeployExtension to false. 
 <VsixDeployOnDebug>true</VsixDeployOnDebug> Should be added to your csproj if you will add it to other solution files to ensure the deploy checkbox is set automatically. 
 Agentic conversion 
 We’re experimenting with ways of making this as easy as possible for you. To that end, we’ve added an agent skill to the vs-agent-plugins repository you can use in conjunction with the Modernize agent. Let us know whether this workflow is helpful, or if you have a different agentic workflow in mind for extension development. 
 Reference projects 
 Here are a few extensions that are already converted, so you can use them as references. 
 Smart Screen 
 Command Explorer 
 Postfix Templates 
 Whitespace Visualizer 
 We want to hear from you! 
 Please send us feedback and issues you encounter in Developer Community . Thank you, and happy extending! 
 The post SDK-Style Support for Extension Projects appeared first on Visual Studio Blog .
```

---

## 3. Visual Studio April Update – Cloud Agent Integration

- 日期: 2026-04-28 19:00
- 链接: https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/

```
GitHub Copilot in Visual Studio is becoming more agentic with every release. This update brings cloud agent integration front and center, letting you start remote coding sessions without leaving the IDE. Custom agents now support user-level definitions that travel with you across projects, C++ code editing tools for agent mode are generally available, and a new Debugger Agent that validates fixes against real runtime behavior. 
 Download Visual Studio 2026 to try everything in this update. 
 Cloud agent integration 
 Cloud agents run on remote infrastructure for scalable, isolated execution, and you can now start new sessions directly from Visual Studio. Select Cloud from the agent picker in the Chat window, describe the work you need help with, and the cloud agent takes it from there. 
 The workflow starts by asking for permission to open an issue in your repository, then creates a pull request to address it. While the cloud agent prepares the PR, you can keep working on other tasks in Visual Studio or close the IDE entirely and come back later. When the PR is ready, you get a notification with options to View PR or Open in browser . 
 Cloud agent in Visual Studio is currently powered by Copilot coding agent . To use it, make sure you are in a GitHub repository and that Copilot has permission to create issues in that repository. This is a different way of working that frees you up to focus on the parts of your project that need your full attention. 
 Build your own custom agents 
 Custom agents launched last month with support for repository-based .agent.md files. This update extends the story with user-level agents that travel with you across projects. 
 User-level agents are stored in %USERPROFILE%/.github/agents/ by default. You can change this location in Tools > Options > GitHub > Copilot > Copilot Chat > Custom agents user directory . Creating new agents is also easier now: click the + button in the agent picker and follow the prompts. 
 Everything you could do with repository-based agents still works: workspace awareness, code understanding, tools, model selection, and MCP connections to external knowledge sources like internal documentation, APIs, and databases. The community has been sharing agent configurations on the awesome-copilot repository if you are looking for starting points. We’d love to see what you build. 
 C++ code editing tools for agent mode 
 C++ Code Editing Tools for GitHub Copilot agent mode are now generally available by default. These tools give Copilot language-aware navigation of your C++ codebase, helping it map out class inheritance hierarchies and follow function call chains when refactoring or modifying code. 
 To get started, open a C++ project with IntelliSense configured and enable the tools using the Tools icon in Copilot Chat. The two available tools are get_symbol_call_hierarchy and get_symbol_class_hierarchy . 
 Once enabled, Copilot uses these tools automatically. For example, you can ask Copilot to analyze the major classes in a file and it will use get_symbol_class_hierarchy to trace inheritance and usage relationships across your codebase. 
 If you work with large C++ codebases, these tools make a real difference. They work best with AI models that support tool-calling, so check the model comparison page to see which ones are compatible. 
 Agentic Issue to Resolution 
 Debugging with static analysis only gets you so far. The new Debugger Agent workflow validates bugs against real runtime behavior, walking you through a complete loop from understanding the issue to verifying the fix through live execution. 
 Start from a GitHub or Azure DevOps issue, or describe the bug in natural language. Switch to Debugger mode using the dropdown in the lower-left corner of the chat, and the agent maps the problem to your local source code. From there, it works through a structured process: creating a minimal reproducer, generating failure hypotheses, instrumenting your app with tracepoints and conditional breakpoints, running the debug session to analyze live telemetry, and suggesting a precise fix at the exact failure point. 
 You can interact with the agent during the debugging process to provide additional context, discuss your theory, or refine the fix in real time. This is debugging that works with you, not just for you. 
 IntelliSense takes priority over Copilot 
 Seeing IntelliSense and Copilot completions at the same time can be distracting. We heard your feedback , and the editor now prioritizes the IntelliSense completion list, showing only one suggestion at a time. 
 https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2026/04/vs18.5_intellisense-priority.mp4 
 When IntelliSense is active, Visual Studio temporarily suppresses Copilot completions so you can focus on your current selection. After you dismiss or commit the IntelliSense selection, Copilot completions resume automatically. This behavior is enabled by default, so just update and code as you normally do. 
 Customizable Copilot keyboard shortcuts 
 You can now customize the keyboard shortcuts for accepting Copilot inline suggestions. Whether you want to change the key for accepting a full suggestion, the next word, or the next line, it is all available in standard keyboard settings. 
 Head to Tools > Options > Environment > Keyboard and search for the commands: Edit.AcceptSuggestion , Edit.AcceptNextWordInSuggestion , or Edit.AcceptNextLineInSuggestion . Remove the existing binding and assign your preferred shortcut under the Inline Suggestions Active scope. 
 Your new shortcut appears throughout the editor hint bar, so you always know which key to press. 
 From our entire team, thank you for choosing Visual Studio! For the latest updates, resources, and news, check out the Visual Studio Hub and stay in touch. 
 Happy coding! The Visual Studio team 
 The post Visual Studio April Update – Cloud Agent Integration appeared first on Visual Studio Blog .
```

---

## 4. From AI to .NET: 20 VS Live! Las Vegas Sessions You Can Watch Now

- 日期: 2026-04-16 15:00
- 链接: https://devblogs.microsoft.com/visualstudio/from-ai-to-net-20-vs-live-las-vegas-sessions-you-can-watch-now/

```
In March 2026, developers came together at VS Live! Las Vegas for a full week of technical learning, hands-on exploration, and a lot of great conversations about where software development is headed next. From AI-assisted development to modern .NET, cloud-native apps, and developer productivity, one thing was clear: the pace of change is not slowing down. 
 If you were not able to attend, or if you want to revisit some of the strongest content from the event, we are now publishing 20 sessions from VS Live! Las Vegas on the Visual Studio YouTube channel. 
 We are releasing about two sessions per day, so you can watch them at your own pace and jump into the topics that matter most to you. 
 What you’ll find in this series 
 These sessions reflect the topics developers are focused on right now, including: 
 AI and Copilot-powered development 
 Modern .NET and C# 
 Cloud-native apps and Azure 
 Developer productivity and tooling 
 Real-world architecture and engineering 
 You’ll hear directly from Microsoft engineers helping build these tools, along with industry experts who are using them to solve real problems and ship real applications. 
 A few sessions to check out 
 This lineup includes a strong mix of practical guidance, technical depth, and forward-looking keynotes. 
 Keynotes 
 The Road to Visual Studio 2027: Building a Faster, Smarter IDE – Mads Kristensen 
 Knowledge is the Key: The Path for AI Applications – Jerry Nixon and Drew Skwiers-Koballa 
 Featured sessions 
 AI’s Not Magic: A Developer’s Guide to Using AI Tools Without the Hype – Brian A. Randell 
 Building an AI Agent to Work with Your Own Data – Jerry Nixon 
 Building Intelligent .NET Applications: From AI to Implementation – Jon Galloway 
 What’s New in C# – Jason Bock 
 Building RESTful Services with ASP.NET Core – Philip Japikse 
 GitHub Actions in Action – Marcel de Vries 
 The Forgotten Features of Visual Studio You NEED In Your Life! – Mads Kristensen 
 Fast Focus: Caching Options in .NET – Jason Bock 
 VS Code and Visual Studio, Better Together – Brian A. Randell 
 Modernizing .NET Applications Faster with Visual Studio – Jon Galloway 
 What I like about this set of sessions is that it is not just theory. These talks focus on real-world scenarios, whether you are exploring AI in existing apps, modernizing older .NET solutions, improving performance, or just looking for better ways to work day to day. 
 Start watching 
 Whether you are catching up on what you missed or diving in for the first time, this is an easy way to experience some of the best content from VS Live! Las Vegas on your own schedule. 
 VS Live! Las Vegas YouTube Playlist 
 We will continue publishing sessions daily, so check back often and subscribe to the Visual Studio YouTube channel to stay up to date. 
 Want the full VS Live! experience? Attend in person 
 Watching online is a great way to learn, but there is still nothing like attending a VS Live! event in person. You get the sessions, the hands-on labs, the hallway conversations, and direct access to speakers, product experts, and fellow developers. 
 If you are a Visual Studio subscriber, you may already have access to exclusive event pricing through my.visualstudio.com . Just sign in, head to the Benefits page, and look for the Visual Studio Live! Events tile to get your priority code. Depending on the event, that can save you up to $900 on registration. 
 If you are not a subscriber, you can still save. As a Visual Studio Blog reader, use priority code VSLMS at checkout to save up to $600 . 
 Each event includes a full week of expert-led sessions and hands-on labs, plus the chance to connect directly with the people behind Visual Studio, .NET, Azure, and GitHub Copilot. 
 Upcoming VS Live! events 
 Microsoft HQ (Redmond) | July 27 to 31, 2026 
 San Diego | September 14 to 18, 2026 
 Live! 360 Orlando | November 15 to 20, 2026 
 Las Vegas | March 22 to 26, 2027 
 Explore All VS Live Events 
 The post From AI to .NET: 20 VS Live! Las Vegas Sessions You Can Watch Now appeared first on Visual Studio Blog .
```

---

## 5. Azure MCP tools now ship built into Visual Studio 2022 — no extension required

- 日期: 2026-04-15 17:30
- 链接: https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/

```
Azure MCP tools now ship built into Visual Studio 2022 — no extension required 
 Azure MCP tools are now built into Visual Studio 2022 as part of the Azure development workload — no separate extension to find, install, or update. You can enable over 230 tools across 45 Azure services directly in GitHub Copilot Chat and manage Azure resources, deployments, and diagnostics without leaving your IDE. If you already have the Azure development workload installed, you’re one click away from getting started. 
 What changed 
 Previously, using Azure MCP tools in Visual Studio 2022 required you to install the “GitHub Copilot for Azure (VS 2022)” extension from the Visual Studio Marketplace, walk through the VSIX installer dialog, and restart Visual Studio. If something went wrong, you had to uninstall and reinstall the extension entirely. That friction added up. 
 Starting now, Azure MCP tools ship as part of the Azure development workload in Visual Studio 2022. There’s no separate extension to manage. When you install or already have the Azure development workload, the Azure MCP Server is available directly in GitHub Copilot Chat. You enable it once, and it stays enabled across sessions. 
 This change means fewer installation steps, no version mismatches between the extension and the IDE, and a single update path through the Visual Studio Installer. The Azure MCP Server version gets updated with regular Visual Studio releases, so you always receive the latest tools as part of your normal update cycle. 
 Note: VS-specific tools available in Visual Studio 2026 are not included in Visual Studio 2022. 
 What you get 
 The Azure MCP Server surfaces over 230 tools across 45 Azure services through GitHub Copilot Chat. These tools interact with various Azure services to support developers across the entire development lifecycle. Key scenarios include: 
 Learn — Ask questions about Azure services, best practices, and architecture patterns. 
 Design & develop — Get recommendations for Azure services and configure your application code. 
 Deploy — Provision resources and deploy your application directly from the IDE. 
 Troubleshoot — Query logs, check resource health, and diagnose issues in production. 
 The tools appear in all tools mode within GitHub Copilot Chat. You pick which tools to enable, and Copilot calls them automatically when your prompts relate to Azure. 
 See it in action 
 Here are a few examples that show how you can use the Azure MCP tools directly from GitHub Copilot Chat in Visual Studio 2022. Each prompt triggers one or more Azure MCP tool calls behind the scenes. 
 Explore your Azure resources 
 List my storage accounts in my current subscription. Copilot calls the Azure MCP tools to query your subscriptions and storage accounts, then returns a list of your storage accounts with their names, locations, and SKUs — right in the chat window. No portal tab needed. 
 Deploy your app 
 Deploy my ASP.NET Core app to Azure. Copilot identifies your project, walks you through creating an App Service resource, and initiates the deployment via azd. You can track progress directly in the chat output. 
 Diagnose issues 
 Help diagnose my App Service resource. Copilot uses AppLens and resource health tools to analyze your App Service, check for availability issues, and surface actionable recommendations — all without leaving the IDE. 
 Query your logs 
 Query my Log Analytics workspace for exceptions. Copilot generates and runs a KQL query against your Log Analytics workspace, returning recent exceptions with timestamps, messages, and stack traces. You can refine the query in follow-up prompts to narrow down the root cause. 
 These are just a few examples. With over 230 tools across 45 Azure services, you can learn about Azure features, provision resources, deploy applications, and troubleshoot issues — all from a single chat window in Visual Studio 2022. 
 How to enable Azure MCP tools 
 The Azure MCP tools ship with the Azure development workload in Visual Studio 2022 version 17.14.30 or higher, but are disabled by default . Follow these steps to enable them: 
 Update Visual Studio 2022 — Open the Visual Studio Installer and make sure you’re running version 17.14.30 or higher. If not, select Update . 
 Install the Azure development workload — In the Visual Studio Installer, select Modify for your Visual Studio 2022 installation and check the Azure development workload. Select Modify again to apply. 
 Launch Visual Studio 2022 — Open or create a project, then open GitHub Copilot Chat . 
 Sign in — Make sure you’re signed in to both your GitHub account (for Copilot) and your Azure account (for resource access). 
 Enable the Azure MCP Server — In the Copilot Chat window, select the Select tools button (the two wrenches icon). Find Azure MCP Server in the list and toggle it on. 
 Once enabled, the Azure MCP tools are available in every Copilot Chat session. You don’t need to re-enable them after restarting Visual Studio 2022. 
 Things to know 
 Keep these details in mind: 
 Azure MCP tools are disabled by default — you need to enable them manually in the Select tools dialog. 
 Tools specific to Visual Studio 2026 are not available in Visual Studio 2022. 
 Tool availability depends on your Azure subscription permissions — if you can’t perform an action in the Azure portal, you can’t perform it through MCP tools either. 
 This feature requires an active GitHub Copilot subscription and an Azure account. 
 The Azure MCP Server version is updated with regular Visual Studio releases. 
 Learn more 
 GitHub Copilot for Azure Documentation 
 Azure MCP Server Documentation 
 Azure MCP Server Repo 
 Share your feedback through Help > Send Feedback in Visual Studio 2022 or file issues on the Azure MCP Server GitHub repository . 
 The post Azure MCP tools now ship built into Visual Studio 2022 — no extension required appeared first on Visual Studio Blog .
```

---

## 6. Stop Hunting Bugs: Meet the New Visual Studio Debugger Agent Workflow

- 日期: 2026-04-15 16:00
- 链接: https://devblogs.microsoft.com/visualstudio/stop-hunting-bugs-meet-the-new-visual-studio-debugger-agent/

```
We’ve all been there: a bug report lands in your inbox with a title like “App crashes sometimes” and zero reproduction steps. Your morning, which was supposed to be spent building new features, is now a forensic investigation. You’re setting scattershot breakpoints, staring at the call stack, and trying to guess what the original reporter was thinking. 
 Debugging isn’t just about fixing code; it’s about reducing uncertainty . Today, we’re taking a massive leap toward solving that problem by introducing a new, upgraded, guided workflow within our existing Debugger Agent in Visual Studio. 
 Ending the “Guessing Game” with a Guided Debugger Loop 
 Let’s be honest: traditional debugging is full of friction. You manually parse a vague report, hunt for the right file, and spend twenty minutes just trying to see if you’re in the right ballpark. This new workflow flips the script, transforming the Debugger Agent from a chatbot into an interactive partner plugged directly into your live runtime . 
 To get started, simply open your solution in Visual Studio, switch to Debugger mode in Copilot Chat, and point it to the problem with a GitHub/ADO URL or a quick sentence like: 
 “The app crashes when saving a file.” 
 The workflow is interactive and powered by runtime debugging, meaning the Agent doesn’t just read your code; it feels how it’s running. It immediately builds a mental model of the failure and walks you through a structured, real-time process: 
 Hypothesis & Preparation: The Agent analyzes the issue and proposes a root cause. If the reasoning looks solid, it sets intelligent breakpoints and prepares to launch your project. 
 Note: If your project can’t be started automatically, just manually start your code, attach the debugger, and tell the Agent you’re ready. 
 Active Reproduction: The Agent stays “on the line” while you trigger the bug, watching the runtime state as you move through the repro steps. 
 Real-Time Validation: As breakpoints hit, the Agent evaluates variables and the call stack to systematically confirm its hypothesis or eliminate potential causes. 
 The Final Fix: Once the root cause is isolated, the Agent proposes a solution. If you approve, it applies the fix and reruns the session to validate the resolution. 
 This iterative flow is designed to keep you “in the zone.” By handling the manual setup and state analysis, the Agent lets you move from a bug report to a verified fix with significantly less mental context switching. 
 Our Vision: Foundational Quality and Beyond 
 18.5 GA releases deliver the foundational experience of the guided workflow, specifically optimized for high-value, reproducible scenarios like exceptions, logic inconsistencies, and state corruption . 
 As we look forward, we are already evolving this foundation to be even more robust. Our goal is to progressively automate the end-to-end workflow, maturing the Debugger Agent into a comprehensive, seamless debugging companion that anticipates your needs. 
 Debug Smarter, Not Harder 
 The new workflow in the Debugger Agent represents a fundamental shift in how we think about IDEs. We’re excited to see how you use this in your own workflows whether you’re untangling a complex race condition in a multi-threaded service or simply trying to figure out why a UI element isn’t updating as expected. 
 Stay connected with the Visual Studio team by following us on Twitter @VS_Debugger , Twitter @VisualStudio , YouTube, and LinkedIn. 
 The post Stop Hunting Bugs: Meet the New Visual Studio Debugger Agent Workflow appeared first on Visual Studio Blog .
```

---

## 7. Take full control of your floating windows in Visual Studio

- 日期: 2026-04-07 14:00
- 链接: https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/

```
If you work with multiple monitors like I do, you’ve probably grown to love floating tool windows and documents in Visual Studio. Being able to pull out Solution Explorer, the debugger, or your code files onto a second (or third) screen can be a huge productivity boost. 
 But there’s always been a bit of friction with how these floating windows behave. 
 By default, floating windows are “owned” by the main Visual Studio window. That means they don’t show up as separate buttons in your Windows taskbar, they disappear when you minimize the main IDE, and they always stay on top of everything else — even when you don’t want them to. 
 For some workflows that’s exactly what you want. For others, it gets annoying fast. 
 Fortunately, there’s a little-known setting that lets you decide exactly how much control Visual Studio has over your floating windows. 
 The setting is here: Tools > Options > Environment > Windows > Floating Windows 
 You’ll see this dialog: 
 The dropdown is labeled “These floating windows are owned by the main window” and gives you three choices: 
 None 
 Tool Windows (the default) 
 Documents and Tool Windows 
 Changing this one setting can completely transform how you work with floating windows. 
 My favorite scenario: PowerToys FancyZones 
 This setting really shines when you combine it with Microsoft PowerToys and its excellent FancyZones feature . 
 I like to set it to None and then use FancyZones to create custom layouts across my monitors. Suddenly all my floating tool windows and documents behave like normal application windows — they appear in the taskbar, stay visible even if I minimize the main Visual Studio window, and I can snap them perfectly into my FancyZones layouts without them forcing themselves to the front all the time. 
 It feels much more natural and gives me the clean multi-monitor setup I’ve always wanted. 
 When to choose each option 
 None : Maximum independence. Everything gets its own taskbar entry and full window behavior. Perfect for heavy multi-monitor users with PowerToys. 
 Tool Windows : A nice middle ground — keep your documents floating freely while tool windows stay tied to the IDE. 
 Documents and Tool Windows : The classic Visual Studio behavior. 
 Pro tip: Combine this with the Ctrl + double-click trick on any tool window title bar (see our earlier post on easily docking and floating tool windows ) for lightning-fast layout switching. No restart required. 
 Have you played with this setting before? What option do you prefer: None, Tool Windows, or the default? Let me know in the comments. I’m always curious how other developers set up multi-monitor workspaces. 
 Happy coding! 
 The post Take full control of your floating windows in Visual Studio appeared first on Visual Studio Blog .
```

---

## 8. Bookmark Studio: evolving bookmarks in Visual Studio

- 日期: 2026-04-01 14:09
- 链接: https://devblogs.microsoft.com/visualstudio/bookmark-studio-evolving-bookmarks-in-visual-studio/

```
Bookmarks in Visual Studio have always been a simple, reliable feature. Many developers use them regularly, and over the years we’ve heard consistent feedback from those users. Bookmarks were useful, but there were a few core gaps that kept them from being as effective and relevant as they could be. 
 Navigation was one of the biggest pain points. You could move between bookmarks, but there was no easy way to jump directly to a specific bookmark using the keyboard. That made bookmarks harder to rely on once you had more than a few. Another common request was sharing. Bookmarks worked well for personal, local navigation, but there was no good way to share them with teammates or reuse them across repos, branches, or pull requests. 
 That feedback is what led to Bookmark Studio , a new experimental Visual Studio extension that builds on the existing bookmark experience by filling in those missing pieces, without changing how bookmarks fundamentally work. 
 Faster, more intentional navigation 
 One of the core additions in Bookmark Studio is slot‑based navigation . 
 Bookmarks can be assigned to slots 1 through 9 and jumped to directly using simple keyboard shortcuts like Alt + Shift + 1 through Alt + Shift + 9 . This makes bookmarks feel more deliberate and easier to rely on when you want fast access to a handful of important locations. 
 New bookmarks are automatically assigned the next available slot when possible, so fast navigation often works without any extra setup. Bookmark Studio also integrates with Visual Studio’s existing bookmark commands, which means your current shortcuts and muscle memory continue to work as expected. 
 A single place to work with bookmarks 
 Bookmark Studio also adds a dedicated Bookmark Manager tool window. 
 The manager shows all bookmarks in one place and makes it easy to browse, search, and navigate between them. You can filter by name, file, location, color, or slot, and jump directly to a bookmark with a double‑click or keyboard navigation. It’s designed to make bookmarks easier to revisit, especially when switching context or coming back to code later. 
 Optional structure, when you need it 
 Another piece of feedback we heard was the need for just a bit more organization. 
 With Bookmark Studio, bookmarks can have labels, colors, and folders. None of this is required, and you can keep using bookmarks exactly as you do today. But when you’re debugging, refactoring, reviewing code, or exploring unfamiliar areas of a codebase, that extra context can make bookmarks more useful and easier to reason about. 
 All bookmark metadata is stored per solution, so it stays with your work across sessions. 
 Bookmarks you can share and reuse 
 Bookmarks are often most valuable when they capture intent, not just location. 
 Bookmark Studio makes it easy to export bookmarks as plain text, Markdown, or CSV. That means you can include bookmarks in pull requests, share investigation paths with teammates, or move useful bookmark sets between repos. Instead of being a purely personal tool, bookmarks can become a lightweight way to communicate context and decisions. 
 Bookmarks that stay put as code changes 
 Bookmark Studio tracks bookmarks as text moves during editing, so they stay attached to the relevant code instead of drifting to the wrong line. This makes bookmarks more dependable during active development, especially when files are changing frequently. 
 A focused improvement, not a reinvention 
 Bookmark Studio doesn’t try to replace tasks, TODO comments, or issue tracking. It doesn’t introduce a new workflow you have to learn. Instead, it fills in the gaps that many bookmark users have pointed out over time, making bookmarks easier to navigate, easier to share, and more useful as part of everyday development. 
 If you already use bookmarks in Visual Studio, Bookmark Studio should feel familiar within minutes. And if you’ve ever wished bookmarks could do just a little more, this extension is worth a look. 
 You can download Bookmark Studio today from the Visual Studio Marketplace . As always, feedback and pull requests are welcome on the GitHub repo . 
 The post Bookmark Studio: evolving bookmarks in Visual Studio appeared first on Visual Studio Blog .
```

---

## 9. Visual Studio March Update – Build Your Own Custom Agents

- 日期: 2026-03-31 16:00
- 链接: https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/

```
This month’s Visual Studio update gives you new ways to customize GitHub Copilot. Custom agents allow you to build specialized Copilot agents tailored to your team’s workflow, backed by the tools and knowledge sources that matter to your project. Alongside that, agent skills bring reusable instruction sets, and a new find_symbol tool gives agents language-aware navigation across your codebase. 
 Beyond agents, we’re continuing to invest in the diagnostics experience with Copilot-powered profiling directly from Test Explorer and real-time perf tips during debugging. Security gets a boost too, with Copilot now helping you fix NuGet vulnerabilities right from Solution Explorer. 
 Download Visual Studio 2026 Insiders to try these features today. 
 Build your own custom agents 
 Want Copilot to follow your team’s coding standards, run your build pipeline, or query your internal docs? Custom agents make that possible. They’re specialized Copilot agents defined as .agent.md files in your repository, with full access to workspace awareness, code understanding, tools, your preferred model, and MCP connections to external knowledge sources. 
 Drop an .agent.md file into .github/agents/ in your repo, and it shows up in the agent picker ready to use. 
 A few things to keep in mind: if you don’t specify a model, the agent uses whatever you’ve selected in the model picker. Tool names can vary across GitHub Copilot platforms, so check the tools available in Visual Studio to make sure your agent works as expected. The awesome-copilot repo has community-contributed agent configurations you can use as starting points. 
 Use agent skills 
 Skills are picked up automatically from several locations in your repository (such as .github/skills/ ) or your user profile (such as ~/.copilot/skills/ ). Each skill lives in its own directory with a `SKILL.md` file that follows the Agent Skills specification . When a skill is activated, it appears in the chat so you know it’s being applied. 
 Check out the awesome-copilot repo for community-shared skills, and look for more user-friendly flows for browsing and creating skills inside Visual Studio in upcoming releases. 
 Find_symbol tool for agent mode 
 Copilot’s agent mode now has language-aware symbol navigation. The new find_symbol tool lets the agent find all references to symbols across your project and access metadata like type information, declarations, and scope. This means when you ask Copilot to refactor a method or update a parameter across call sites, it can actually see your code’s structure rather than guessing from text. 
 Enable the tool, and Copilot uses it automatically when answering questions or suggesting code changes. The difference is noticeable: instead of searching for text patterns, the agent navigates your code using language services. 
 Supported languages include C++, C#, Razor, and TypeScript, plus any language with a supported LSP extension installed. For best results, use AI models that support tool-calling. Learn more at AI model comparison . 
 Enterprise MCP governance 
 MCP server usage in Visual Studio now respects allowlist policies set through GitHub. Admins can specify which MCP servers are allowed within their organizations. When an allowlist is configured, only approved servers can be connected. If you try to use an unauthorized server, you’ll see an error explaining the restriction. This helps organizations control which MCP servers process sensitive data and maintain compliance with security policies. 
 Profile Tests with Copilot 
 Ever wanted to profile a specific test without wrestling with profiler configuration? There’s now a Profile with Copilot command right in the Test Explorer context menu. 
 When selected, the Profiling Agent automatically runs the chosen test and analyzes its performance, combining CPU usage and instrumentation data to deliver actionable insights. By default, it uses Instrumentation profiling and is currently supported in .NET. If you need deeper analysis, you can launch the selected test directly from the Copilot chat window and choose additional profiling tools. 
 Perf tips powered by live profiling 
 Performance optimization now happens while you debug, not after. As you step through code, Visual Studio shows execution time and performance signals inline for each step. When you spot a slow line, just click the Perf Tip and ask Copilot for optimization suggestions on the spot. 
 The Profiler Agent captures runtime data during debugging automatically: elapsed time, CPU usage, and memory behavior. Copilot uses this data to pinpoint performance hot spots and suggest targeted fixes. This keeps optimization part of your regular debugging workflow instead of something you tackle later. 
 Fix vulnerabilities with Copilot 
 Spotted a NuGet package vulnerability? Copilot can now help you fix it directly from Solution Explorer. When a vulnerability is detected, you’ll see a notification with a Fix with GitHub Copilot link. Click through, and Copilot analyzes the vulnerability, recommends and implements targeted dependency updates that keep your packages secure without disrupting your workflow. 
 No more manual vulnerability research or hunting down correct package versions. You address security issues right when they’re discovered. 
 HTML rich copy/cut 
 Need to paste code into a presentation, an Azure DevOps work item, or a web-based document? Visual Studio now supports HTML clipboard format when cutting or copying code from the editor. Syntax highlighting and formatting carry over when you paste into HTML-based applications. It’s turned on by default. To customize, go to Tools > Options > Text Editor > Advanced where you can toggle Copy rich text on copy/cut and set the max length. 
 From our entire team, thank you for choosing Visual Studio! For the latest updates, resources, and news, check out the Visual Studio Hub and stay in touch. 
 Happy coding! 
 The Visual Studio team 
 The post Visual Studio March Update – Build Your Own Custom Agents appeared first on Visual Studio Blog .
```

---

## 10. Unlock More Power in Your Development Workflow: Syncfusion for Visual Studio Subscribers

- 日期: 2026-03-24 15:00
- 链接: https://devblogs.microsoft.com/visualstudio/syncfusion-for-visual-studio/

```
A few months ago, I was talking with a developer who said something that stuck with me: 
 “I love building apps. I just don’t love rebuilding the same UI controls over and over again.” 
 That’s the reality for a lot of teams. You want to focus on your business logic, your architecture, your differentiation. Instead, you burn cycles wiring up grids, charts, document exports, dashboards, and signing workflows. 
 If you’re a Visual Studio subscriber, there’s a benefit waiting for you that can change that: Syncfusion . 
 And it’s included at no additional cost for eligible subscribers. 
 Let me walk you through why this one matters. 
 Why Syncfusion? 
 Syncfusion delivers a comprehensive suite of: 
 1,600+ UI components 
 Cross-platform controls for .NET, JavaScript, XAML, MAUI, Blazor, and more 
 Document processing SDKs for PDF, Word, Excel, and PowerPoint 
 Data visualization and analytics tools 
 Digital signature APIs 
 In short, it helps you ship polished, enterprise-grade applications faster, without reinventing the wheel. 
 Depending on your Visual Studio subscription level, you get 6 to 12 months of access to powerful editions of these tools . 
 For Visual Studio Professional & Enterprise Subscribers 
 If you’re on Visual Studio Professional or Enterprise, here’s what’s included. 
 Essential Studio Enterprise Edition 
 Duration: 12 months 
 This is the full suite. 
 1,600+ UI controls across platforms 
 High-performance grids, charts, schedulers, data visualization 
 Cross-platform development for web, desktop, and mobile 
 Document Solutions SDKs for PDF, Word, Excel, and PowerPoint processing 
 No need for Microsoft Office or Adobe installed 
 Potential 15% renewal discount after the benefit term 
 If you’re building line-of-business apps, SaaS products, internal dashboards, or customer solutions, this can dramatically accelerate your delivery timeline. 
 BoldSign – E-Signature API 
 Enterprise Subscribers | 12 months 
 Modern applications increasingly require digital signing workflows. BoldSign gives you: 
 12-month subscription 
 Unlimited templates 
 API access 
 Audit trails and team management 
 50 API document credits included 
 Additional usage at $0.75 per document 
 Auto-renews at $5/month unless canceled 
 This is ideal for integrating secure, automated signing directly into your application workflows. 
 Bold BI 
 Professional & Enterprise | 6 months 
 Need dashboards and analytics without building everything from scratch? 
 Bold BI includes: 
 120+ data source connectors 
 AI-powered analytics 
 Scheduling and export capabilities 
 Unlimited users 
 GDPR, SOC 2, and HIPAA compliance 
 If you’ve ever built custom reporting and thought, “There has to be a faster way,” this is it. 
 For Visual Studio Dev Essentials Members 
 If you’re part of Visual Studio Dev Essentials , you’re not left out. 
 Essential Studio UI Edition 
 Duration: 6 months 
 A curated subset of Syncfusion’s UI components designed for cross-platform app development. 
 1,600+ high-performance components 
 Full source code 
 Priority support 
 Perfect for Visual Studio Community and VS Code developers building serious applications. 
 Syncfusion Succinctly Series 
 Ongoing access 
 You also get access to 20 curated developer eBooks covering: 
 C# 
 Python 
 JavaScript 
 Azure 
 Git 
 Docker 
 Machine Learning 
 And more 
 This benefit does not expire. 
 Acceptable Use Guidelines 
 You can use these benefits to build: 
 Internal tools 
 Customer solutions 
 Demos and proofs of concept 
 Reference implementations 
 You cannot: 
 Redistribute the libraries 
 Share license keys 
 Use them for unrelated personal redistribution projects 
 As always, check the detailed terms when activating your benefit. 
 A Quick Note on Eligibility 
 These benefits apply to eligible Visual Studio Enterprise and Professional subscribers, as well as Dev Essentials members, depending on the specific offer and duration. 
 Exclusions include certain subscription types such as Enterprise FTE, NFR, MVP, RD, MAICPP, MPN, ISV, Bug Bounty, MCT, Student Ambassadors, Alumni, Xbox NFR Basic, Azure DevOps Tools for Teaching, Startups, We. Comms, and Open Source Heroes. 
 Learn more about benefit eligibility details here . 
 Don’t Leave This on the Table 
 I’ve said this before about subscriber benefits: you’re already paying for the subscription. The worst thing you can do is not activate what’s included. 
 Between: 
 1,600+ UI components 
 Enterprise-grade document SDKs 
 Embedded e-signature APIs 
 Production-ready analytics dashboards 
 This is thousands of dollars in tooling, available to you right now. 
 If you’re a Visual Studio subscriber, sign in at: 
 my.visualstudio.com/benefits 
 Activate your Syncfusion benefit and start building faster. 
 The post Unlock More Power in Your Development Workflow: Syncfusion for Visual Studio Subscribers appeared first on Visual Studio Blog .
```

---
