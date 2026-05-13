# JavaScript Weekly

> 分类: 技术周刊
> URL: https://javascriptweekly.com/rss/
> 抓取: 4 篇

---

## 1. Remix 3 drops React

- 日期: 2026-05-05 00:00
- 链接: https://javascriptweekly.com/issues/784

```
#​784 — May 5, 2026 
 Read on the Web 
 JavaScript Weekly 
 Remix 3 Enters Beta — It's No Longer a React Framework — Remix has quite the back story. Created by the duo behind React Router in 2020 and seen as an alternative to Next.js , Remix was acquired by Shopify in 2022 and its core ideas folded into React Router v7 in 2024. Now, a new direction: a full-stack, web standards-first framework with its own UI component model and… no React. 
 Michael Jackson (Remix) 
 Build AI Features That Get Better Over Time — Join Scott Moss for this detailed video course covering agentic systems, eval harnesses, RAG, and context engineering — everything you need to ship reliable, production-ready AI features. 
 Frontend Masters sponsor 
 Node.js 26.0.0 (Current) Released — A macOS build snafu pushed the release date out to today, but the latest version of Node is here, complete with Temporal API enabled by default, V8 14.6, and Undici 8. v26 is the ‘current’ cutting-edge release until October when it’ll be promoted to LTS. 
 Rafael Gonzaga 
 IN BRIEF: 
 Vitest is tightly coupled to Vite, but a maintainer has proposed making it "framework-agnostic" to support other build tools and runtimes. 
 People on Hacker News got very excited to discuss an effort by Bun's Jarred Sumner to port Bun from Zig to Rust. Jarred turned up on the thread to cool things down. A Rust port is being attempted, but with no long-term intent to switch for now. 
 The Svelte team has shared its latest monthly roundup , including the news that Svelte appears in ThoughtWorks' latest Technology Radar . 
 Deno is getting experimental support for import defer ( TC39 proposal ) and may be the first runtime to support it. 
 RELEASES: 
 PM2 7.0 – The Node.js process manager gets a refactor that slashes its dependency footprint, and extends cluster mode and the monitoring agent to Bun apps. 
 Astro v7 Alpha – The web framework for content-driven websites teases its Vite 8-based, Rust compiler-driven version, alongside its v6.2 release . 
 Electron 41.5 – The cross-platform desktop app framework adds support for Touch ID for WebAuthn on macOS. 
 Ember 6.12 – The final 6.x release in preparation for Ember 7.0. 
 ESLint 10.3 , Zod 4.4 , Babylon.js 9.5 
 📖  Articles and Videos 
 Testing Vue Components in the Browser — Julia sets up integration tests for her components that run entirely in the browser, sidestepping extraneous tooling, and shares issues she ran into around mounting components, waiting on the DOM, filling forms, and measuring coverage. 
 Julia Evans 
 Trustworthy JavaScript for the Open Web — Web Application Integrity, Consistency and Transparency (WAICT) is an emerging spec for cryptographically verifying that the JavaScript running in a user’s browser matches what the site published (there’s a full explainer here ). A prototype is now live in Firefox Nightly. 
 The Firefox Security Team (Mozilla) 
 Breakpoints and console.log Is the Past, Time Travel Is the Future — 15x faster JavaScript debugging than with breakpoints and console.log, supports Vitest, Jest, Karma, Jasmine, and more. 
 Wallaby Team sponsor 
 📄 'I Got a $134 Cloudflare D1 Bill: Here's How I Cut It 95%' – Adventures in using SvelteKit on Cloudflare Workers with D1 (SQLite) and Drizzle ORM. Justin Ahinon 
 📄 'I Am Worried About Bun' – By a developer who’s worried about the long term implications of Anthropic acquiring Bun. William Johnston 
 📄 Making Bluetooth Low Energy Work with JavaScript Ifedayo Agboola 
 🛠 Code & Tools 
 Anime.js 4.4: The Flexible JavaScript Animation Engine — At ten years old, the ‘animate anything from JavaScript’ library continues to get even better with a new scrambleText effect and auto-grid layout mode for stagger grids. The docs for Anime are truly top-tier and packed with examples. 
 Julian Garnier 
 Video Archiving with the Vonage Video API and React — Master four ways to record: capture audio-only, separate streams, or use Experience Composer for custom branded layouts. 
 Vonage sponsor 
 Formisch: A Modular, Type-Safe Form Library — A schema-based, headless form library for Preact, Qwik, React, SolidJS, Svelte and Vue that manages form state and validation (using Valibot). Try out some demos in the playground . 
 Open Circle 
 opentype.js: Read and Write OpenType Fonts — Get direct access to letterforms in the browser and Node.js. Has broad WOFF, OTF, and TTF support, and supports ligatures, kerning, and emojis. You can also create your own fonts from scratch. The new v1.3.5 release is a preview of the soon-to-land 2.0. GitHub repo. 
 Frederik De Bleser 
 View Transitions Mock: Non-Visual Polyfill for Same-Document View Transitions — A JS implementation of Same-Document View Transitions, without the visuals. Write one clean code path: supporting browsers get the transitions, non-supporting ones get an instant DOM swap, but the promises behave the same. 
 Google Chrome Labs 
 🎬 Mediabunny v1.42.0 – Read, write, and convert audio and video files in the browser. v1.42.0 notably adds HTTP Live Streaming (HLS) read/write support. 
 pnpm v11.0.5 – The fast and efficient npm alternative has deployed many bugfixes since last week's big 11.0 release. 
 Electrobun 1.18 – Build tiny cross-platform desktop apps atop Bun. ( Changelog ) 
 useHotkeys 5.3 – React hook for using keyboard shortcuts in components. 
 RxDB 17.2.0 – Fast, local-first, reactive database for JS apps. 
 📰 Classifieds 
 ⌘ Command Code is a frontier coding agent that ships features, fixes bugs, writes tests, & continuously learns your taste. Start now for $1 . 
 Flaky tests slowing down dev? Meticulous gives engineers confidence to ship faster by autonomously testing every edge case of your web app. 
 ⚙️ The new Clerk CLI : Run clerk init to scaffold auth, clerk config to manage it in code, Clerk API to query it. Open source: clerk.com/cli 
 Handsontable Theme Builder has AI. Describe your theme, get a token set that fits your data grid — no CSS overrides, no trial and error. 
 📢  Elsewhere in the ecosystem 
 How can you not love a project homepage where you're a cat in a convertible driving through an endless barrage of obstacles? Crashcat is a JavaScript 3D rigid body physics library built for games, simulations, and web experiences, complete with numerous fun examples. 
 ✉️ Cloudflare has open sourced Agentic Inbox , a self-hosted React 19 and React Router 7-based web email app that ties together and heavily leans on numerous Cloudflare APIs. 
 Ladybird is a "truly independent web browser" with its renderer and JS engine built entirely from scratch , with an alpha release due later this year. In the project's latest update they cover recent significant JS and CSS improvements. 
 Tired of localhost:3000 on your projects? Vercel's Portless lets you run local dev servers using a more user-friendly .localhost hostname over HTTPS. 
 Thales is a TypeScript to Lean compiler that type-checks a subset of TypeScript and emits a Lean sidecar, turning your code into a Lean module you can reason about.
```

---

## 2. What’s actually new in JavaScript (and what’s coming next)

- 日期: 2026-04-28 00:00
- 链接: https://javascriptweekly.com/issues/783

```
#​783 — April 28, 2026 
 Read on the Web 
 JavaScript Weekly 
 pnpm 11.0 Released — You’ve heard about its benefits , but now the popular package management tool is even better. v11 sets minimumReleaseAge to one day by default, there's an SQLite-backed store index (faster installs!), native package publishing, pack-app , and more. There's a migration guide for v10 users . Work has also resumed on a Rust-powered port called Pacquet . 
 Zoltan Kochan 
 💡 On the topic of package managers, Aube is a new contender from the creator of Mise that focuses heavily on performance . 
 Still Writing Tests Manually? Meticulous AI Is Here — Notion, Dropbox, Wiz and LaunchDarkly now use a testing paradigm they can’t work without. Built by former Palantir engineers, Meticulous automatically creates an evolving suite of E2E UI tests, delivering exhaustive coverage with no developer effort. 
 Meticulous sponsor 
 TypeScript 7.0 Beta: 10x Faster TypeScript Compilation — The Go-powered port with “about 10 times faster” compiler performance. TypeScript 6.0 's deprecations and config changes will help you upgrade smoothly from v5 to v7. There are also changes to how to write your code to review. While v7 is considered "close to production-ready" , a stable programmatic API won't arrive till v7.1. 
 Microsoft 
 IN BRIEF: 
 Node.js v26.0 (Current) is expected later today, enabling Temporal API support by default after an upgrade to V8 14.6. Here's a preview of the release notes. 
 Noticed GitHub being flakier than usual lately? Vlad Fedorov has a fresh official update on GitHub's reliability (including last week's merge queue incident ). 
 🇪🇺 NodeConf EU is back. It's in Bologna, Italy this September 29-30. Tickets are on sale, and here's the CFP if you want to speak. 
 RELEASES: 
 Rspack 2.0 – The fast, Rust-based webpack-compatible bundler is 10% faster than v1.7, performs better static analysis , and adds experimental RSC support . Rsbuild 2.0 was released too. 
 Nuxt UI 4.7 – Vue UI library with 125+ components. v4.7 adds Listbox , and a Prompt component for displaying copy/pasteable AI prompts. 
 🌐 Lingui 6.0 – Popular framework and runtime agnostic JS i18n and l10n library. 
 Transformers.js 4.2.0 , Electron 41.3.0 , Etherpad v2.7.0 
 📖  Articles and Videos 
 What’s Actually New in JavaScript (And What’s Coming Next) — You could read the specs and countless posts about each new language feature or... this post that brings everything relevant and useful from ES2025 and ES2026 into one place. Iterator helpers, Promise.try , Map.getOrInsert , using , Temporal, and much more, are covered. 
 Neciu Dan 
 Stop Guessing Where Your Next.js App Broke [Workshop] — Learn to trace Next.js errors back to their source using logs and tracing. Free workshop, register today 
 Sentry sponsor 
 📄 Debugging WASM in Chrome DevTools – Tips on using the Chrome DevTools’ “very capable WASM debugger” . Eli Bendersky 
 📄 Writing Node.js Addons with .NET Native AOT – You can now write native Node addons in .NET-based languages, such as C#. Drew Noakes (Microsoft) 
 📄 The Simplest C Function-to-WebAssembly-to-JS Pipeline Peter Cooper 
 📄 Upgrade Cypress to TypeScript 6.0 Gleb Bahmutov 
 🛠 Code & Tools 
 TSRX: A TypeScript Language Extension for Declarative UIs — A fresh attempt at improving upon JSX from a Svelte maintainer and former React core engineer. It includes control flow, scoped styles, and locals, and compiles to React, Preact, Solid and Ripple . 
 Dominic Gannaway 
 📊 Lightweight Charts™ 5.2: Fast Charts for Financial Data — A seven-year-old canvas-based charting library optimized for financial data use cases like rounded candle plots , box whisker plots , and dual range histograms. The homepage is full of interactive demos. GitHub repo. 
 TradingView 
 Clerk CLI: Manage Auth from Your Terminal — Detects your framework, scaffolds auth, and manages sign-in methods and session policies in code. Open source. 
 Clerk sponsor 
 Nano Stores 1.3: A Tiny (286 Bytes) State Manager — Atomic and derived stores for every major framework (including React) and vanilla JS. Worth a look if a tiny footprint and framework-agnostic design appeal to you. 
 Andrey Sitnik (Evil Martians) 
 BWIP-JS 4.10: Barcode Writer in Pure JavaScript — A library to generate barcodes using over 100 different standards. There’s a live demo where you'll discover far more types of barcodes exist than you imagined. 
 Mark Warren 
 🍋 Fresh 2.3: Zero JS by Default, View Transitions, and More — Deno full-stack web framework ( explained here ) gains first-class WebSocket support, no longer ships any JavaScript for pages that don’t need it, and makes using the View Transitions API a snap with a single attribute in your views. 
 Bartek Iwańczuk (Deno) 
 🎬 Mediabunny v1.41.0 – Powerful JavaScript toolkit for working with media files. 
 hyperid 4.0 – Matteo Collina's fast unique ID generator for Node & browsers. 
 Svelte Bricks 0.5 – Svelte masonry component with SSR support. 
 focus-trap 8.1 – Trap focus within a DOM node. ( Demo. ) 
 CheerpJ 4.3 – Run unmodified Java apps in the browser. 
 qrcode.vue 3.9 – Vue component to generate QR codes. 
 📰 Classifieds 
 📸 Scan barcodes, QR codes and others directly in the browser using STRICH , a lean JS library. Free 30-day trial, try the demo app today! 
 ⌘ Command Code is a frontier coding agent that ships features, fixes bugs, writes tests, & continuously learns your taste. Start now for $1 . 
 📢  Elsewhere in the ecosystem 
 🎵 I've been dying to link to Chip Player JS again for a while now. It's a JavaScript powered online player and repository of over 300,000 MIDI, tracker, chiptune, and video game music files. It's fantastic for background music, and if you can remember a game, it's probably in here. Chrono Trigger's soundtrack is a particular favorite of mine. 
 📊 Datatype is an OpenType variable font that turns simple text expressions into inline charts with no JavaScript or images needed. For example: {l:10,50,30,80,20} gets rendered as an inline sparkline. 
 🤖 Cloudflare's new Is Your Site Agent-Ready? tool analyzes your site to "see how ready it is for AI agents." 
 🤖 Cloudflare has released a set of agent skills to help agentic development tools build on the Cloudflare platform. 
 Sean Goedecke explains how good engineers write bad code at big companies. 
 If all else fails, just stare at the wall for ten minutes.
```

---

## 3. Create videos with HTML and JavaScript via HyperFrames

- 日期: 2026-04-21 00:00
- 链接: https://javascriptweekly.com/issues/782

```
#​782 — April 21, 2026 
 Read on the Web 
 JavaScript Weekly 
 HyperFrames: Write HTML and JavaScript to Create Videos — An open-source framework for creating and rendering videos with HTML and JavaScript. Essentially a simpler non-React alternative to Remotion . It includes a variety of built-in blocks/components for common video effects and elements, and can also composite existing video and audio clips. GitHub repo. 
 HeyGen 
 Still Writing Tests Manually? Meticulous AI Is Here — Notion, Dropbox, Wiz and LaunchDarkly now use a testing paradigm they can’t work without. Built by former Palantir engineers, Meticulous automatically creates an evolving suite of E2E UI tests, delivering exhaustive coverage with no developer effort. 
 Meticulous sponsor 
 The Vercel Breach That Started with a Roblox Cheat — An employee of an AI tool provider used by a Vercel employee was compromised by malware ( bundled with a Roblox cheat! ) and the attacker used that foothold, by way of Google Workspace, to reach a subset of Vercel customers’ environment variables. 
 Vercel 
 💡 Vercel users should follow these steps , but even if you're not one, the weak link was an OAuth grant to a third-party tool, and that pattern is nearly universal. 
 IN BRIEF: 
 Node.js is moving to support the Temporal API by default , most likely in Node v26 which is expected next week. 
 Salesforce ecosystem devs are used to using specific frameworks within its walled garden; now you can build native React apps on Salesforce . 
 Rust's official package/crate registry, crates.io , is migrating from Ember.js to Svelte 5. 
 RELEASES: 
 Node.js 24.15.0 (LTS) – require(esm) and the module compile cache are marked as stable, and --max-heap-size has been added. 
 Fable 5.0 – A mature F# transpiler that targets JavaScript (plus other languages). v5.0 adds .NET 10 and F# 10 support. 
 uuid 14.0 – Create RFC9562-compliant UUIDs (v1 through v7). 
 📖  Articles and Videos 
 ▶ Evan You's State of Vue 2026 Talk — A month ago, Evan You (of Vue.js and VoidZero fame) gave his annual address. Less Vue-focused than usual (though Vapor Mode is “almost ready”), the talk focuses on Vite-ecosystem updates covering Vite 8 , Vite+ , and Void. 
 Evan You / Vue.js Amsterdam 
 How I Resolved 15K Circular Dependencies — A senior Microsoft engineer’s retrospective of clearing ~15,000 project-level circular dependencies from a 7 million line(!) TypeScript monorepo, with reusable ideas for anyone wrangling a large TS workspace. For some reason this article no longer exists as of April 24. 
 Stefan Haas 
 Your Agent Ships 10 Ideas a Day. You Get 2 Databases? — Your agent builds faster than a 2-project free tier allows. ghost gives it unlimited Postgres. 1TB storage. Try free . 
 ghost sponsor 
 The Vertical Codebase — Structuring an app with folders like components/ , hooks/ , and utils/ feels tidy at first, but gets harder to live with over time. Dominik makes the case for a vertical, domain-first approach. 
 Dominik Dorfmeister 
 🔒 The OWASP NPM Security Best Practices Cheat Sheet — A useful, long-standing checklist that continues to be updated with recent updates tackling disabling lifecycle scripts, typosquatting, trusted publishing, and dependency confusion. 
 OWASP Cheat Sheet Series 
 How We Made the Angular Compiler Faster Using AI — Two of VoidZero’s developers wanted to see how fast an Angular compiler they could make. Very fast, it turns out. 
 Brooklyn and Michael Dong (VoidZero) 
 📄 Why I Don't Chain Everything in JavaScript Anymore – Long chains of methods vs. an easier-to-read sequence. Matt Smith 
 📄 The Scope of Type Guards and Assertion Functions Stefan Judis 
 🛠 Code & Tools 
 Bun v1.3.13: Smarter Testing, Streaming Installs, and Less Memory — The Bun runtime has had a great run of releases, including last week’s v1.3.12 with built-in browser automation. Now, bun test gets numerous enhancements with --isolate , --parallel , --shard and --changed options for test env isolation, parallelization, and to run only test files affected by recent changes. The runtime now uses 5% less memory , bun install gets faster, and more. 
 Jarred Sumner 
 Introducing B2B Authentication — Clerk combines Organizations, SCIM, SSO, RBAC, invites, and billing to build enterprise-ready apps. 
 Clerk sponsor 
 Animata: Over 100 Animated React Components — A suite of novel animation-focused React components you don't often see elsewhere, including animated beams , spreading cards , and a Slack-style intro screen . 
 Codse 
 📄 officeParser: A Library to Parse Common Office-Related Formats — Work with formats like docx , pptx , xlsx , odt and others used by office suites, both in the browser and server-side. GitHub repo. 
 Harsh Ankur 
 🎵 tiks: Procedural UI Sounds for the Web — Clicks, pops and pings synthesized with the Web Audio API (so it’s tiny). 
 Rexa 
 TypeGPU 0.11 – TypeScript WebGPU toolkit with advanced type inference and the ability to write shaders in TypeScript. 
 📺 Shaka Player 5.1 – JavaScript library for adaptive media playback supporting DASH and HLS. ( Demos. ) 
 TiddlyWiki 5.4 – Self-contained JavaScript wiki for personal use. ( Repo. ) 
 ✂️ Knip 6.6 – Popular tool for finding and removing unused files, dependencies and exports. 
 wasm-xlsxwriter 0.13 – Generate Excel files in the browser or Node. 
 React Three Fiber 9.6 – The React renderer for Three.js. 
 np 11.2 – A better npm publish . 
 📰 Classifieds 
 HyperFormula AI SDK : Give LLMs a deterministic engine to safely read, write, and calculate spreadsheet formulas. No hallucinated math. 
 Gauntlet AI Night School | RAG that holds up in production requires evaluation built in from the start. Learn how. (Virtual — 4/22) 
 Builders Learn from Builders. From one builder to another: Join Mark Rober at Twilio SIGNAL, May 6–7 in San Francisco. Register for a discounted developer ticket here! 
 📢  Elsewhere in the ecosystem 
 Git 2.54 has been released with a couple of headline features: 
 git history offers a new, easy way to edit commit messages or interactively split a commit into two. 
 You can now define hooks in config files (whether in a repo, at user level, or even system level) rather than just in .git/hooks . You can also run multiple hooks for the same event in this way. 
 If you ever work with Ruby on Rails , you might find rails_vite interesting. It's a new tool that seamlessly brings the power of Vite into Rails' pipeline. 
 💥 Anyone who's analyzed GitHub projects for a while knows this already, but there's a huge 'fake star' economy where people pay to make their projects look more popular than they are. 
 Isa Yeter explains how he migrated from DigitalOcean to Hetzner slashing his hosting bill by 84% in the process. 
 Cloudflare has released a preview of its new cf CLI tool for working with its various services.
```

---

## 4. MDN ditches React for web components in frontend rebuild

- 日期: 2026-04-14 00:00
- 链接: https://javascriptweekly.com/issues/781

```
#​781 — April 14, 2026 
 Read on the Web 
 JavaScript Weekly 
 Under the Hood of MDN's New Frontend — The hugely useful MDN has rebuilt its frontend stack from the ground up, ditching React for web components and a homegrown server component system. A great read on building a modern, content-heavy site without shipping unnecessary JavaScript on every page. 
 Leo McArdle (MDN) 
 Ship Mobile Apps The Way You Ship Websites — Expo gives JavaScript developers a web-like workflow for native mobile. Hot reload on device. OTA updates that skip app store review. Cloud builds that work like Vercel. Start with npx create-expo-app. 
 Expo sponsor 
 🕹️ Phaser 4.0: The 2D WebGL and Canvas-Based Game Framework — The widely used game framework celebrates its 13th birthday with a major release focused on perf/efficiency improvements, and includes skills files so AI agents can build Phaser 4.0 apps well. There are lots of demos , including these games , and existing users get a v3 to v4 migration guide. 
 Phaser Studio Inc. 
 IN BRIEF: 
 Google will penalize sites that 'hijack' the back button in its search results from June. "Ensure you are not doing anything to interfere with a user's ability to navigate their browser history," says Chris Nelson. 
 TanStack Start now has (experimental) React Server Components support. 
 🇫🇷 dotJS returns to Paris, France this September 18 – its CFP is open for two more weeks if you'd like to speak. 
 🇷🇴 The JSHeroes conference is back this May 14-15 in Romania. 
 RELEASES: 
 Bun v1.3.12 – The JS runtime now ships with native, headless browser automation built in, and Bun.cron provides an in-process task scheduler. 
 ⚠️ React 19.2.5 , 19.1.6 and 19.0.5 have been released to deploy a fix for a React Server Components vulnerability. 
 React Native 0.85 – New animation backend and devtools improvements. 
 pnpm v11.0 RC 0 , React Three Fiber 9.6 , Electron 41.2 , DOMPurify 3.4 
 📖  Articles and Videos 
 Installing Every Firefox Extension — One person’s entertaining and heroic tale of wielding JavaScript to explore the Firefox extension ecosystem. And what oddities there are within! I enjoyed this a lot, it’s like Alice in Wonderland for developers. More spelunking like this please. 
 Jack Cab 
 Uses for Nested Promises — James revisits 2013's Promises/A+ monads debate and has changed his mind, thanks to a real concurrency problem he ran into. Demanding but rewarding. 
 James Coglan 
 44 Postgres Talks To Choose From All in One Free, Virtual Event — Join POSETTE: An Event for Postgres 2026, a free & virtual Postgres developer event, 16–18 Jun. Check out the schedule . 
 Microsoft | AMD sponsor 
 You Can't Cancel a Promise (Except Sometimes You Can) — You can’t cancel a promise, but you can halt an async function by making it await a promise that never resolves. The function silently stops, and GC cleans up after it. 
 Aaron Harper (Inngest) 
 Parse, Don't Validate (In a Language That Doesn't Want You To) — Tired of writing the same defensive if check in multiple files because you can’t trust that validation already happened? Branded types and discriminated unions can let TypeScript carry that proof for you. 
 Christian Ekrem 
 🌐 The Intl API: The Best Browser API You’re Not Using — A neat code-heavy primer to what you can do with Intl . 
 Kilian Valkhof 
 📄 Making Our Frontend Unit Tests Much Faster with @swc/jest – From 15 seconds with Jest to 4 seconds with the compatible @swc/jest . Sebastian Herrmann 
 📄 Creating Custom Page Transitions in Astro with Barba.js and GSAP Iqbal Muthahhary (Codrops) 
 📄 The Uphill Climb of Making Diff Lines Performant on GitHub Ghenco and Shwert (GitHub) 
 📄 Building a JavaScript Runtime with QuickJS Andrew Healey 
 🛠 Code & Tools 
 Boneyard: Auto-Generated Skeleton Screens for Your UI — Snapshots your real UI and captures a flat list of skeleton ‘bones’ which are positioned, sized rectangles that mirror the page exactly. Supports React, Preact, React Native, Vue, Svelte, and Angular. 
 0xGF 
 📈 Micro-ML: A Toolkit of Forecasting and Clustering Algorithms — A ~56KB WASM-powered library with algorithms for regression and smoothing. Cluster points, classify data, or predict the next value in a series without dragging in TensorFlow.js. 
 Adam Perliński 
 AI Writes Code. Wallaby MCP Makes Sure It Actually Works — Give your AI agent live execution data, coverage, and real-time insights to generate tests and code with confidence. 
 Wallaby Team sponsor 
 Ink 7.0: Use React to Build TUIs and Command Line Apps — Powering many popular terminal apps , v7.0 now leans on React 19.2, uses useEffectEvent internally for added efficiency, and brings new hooks and settings. 
 Vadim Demedes 
 🔊 web-audio-api: Use the Web Audio API from Node and Bun — Full Web Audio API support to either play audio on your machine/server or render it to file (and, yes, Tone.js works too). There are many examples to enjoy. 
 Sébastien Piquemal 
 Syncpack: Consistent Dependency Versions in Large JS Monorepos — A CLI tool (used by Electron, Cloudflare, Vercel and others) that finds version mismatches across your entire monorepo, fixes them, and can enforce version policies in CI to avoid future drift. 
 Jamie Mason 
 Mantine 9.0 – The wildly popular React component suite now includes a complete set of calendar scheduling components. 
 wa-sqlite 1.1 – WebAssembly build of SQLite enabling JavaScript-based virtual filesystems and browser storage extensions. ( Demo. ) 
 gridstack.js 12.6 – Build responsive drag-and-drop multi-column dashboards. 
 Formula.js 4.6 – Excel's formula functions, but for JavaScript. 
 Lexical 0.43 – Facebook's extensible text editor framework. 
 📰 Classifieds 
 Flaky tests slowing down dev? Meticulous gives engineers confidence to ship faster by autonomously testing every edge case of your web app. 
 Manage SAML and OIDC enterprise connections via Clerk's Backend API . One unified endpoint for both protocols. 
 ⚡ Nimbalyst : Visual workspace for building with Claude Code & Codex. Integrate and manage sessions, tasks & files. Visually edit markdown, mockups, diagrams, code. 
 Gauntlet AI Night School | Cursor, Claude Code, or agents — how AI-first engineers choose the right tool for production. (Virtual - 4/15) 
 📢  Elsewhere in the ecosystem 
 Windows 95 as an Electron App — A full Windows 95 experience as an app on macOS, Linux, and Windows, built upon the v86 JavaScript + WASM emulator. v5.0 is a big release as you can mount a folder from your machine into it as a Z: drive, mount ISOs as CD-ROMs, there’s a shared clipboard, and Internet access has been improved. I’m so trying to get Microsoft Encarta ’s Mindmaze running on this… 
 Felix Rieseberg 
 🎨 Sticking to the retro theme, a new release of JSPaint has landed too, so you can relive the joy of using MS Paint . Try it here. 
 It's ten years since Domenic Denicola posted about adding JavaScript modules to the web platform – how far we've come since! 
 GitHub has a private preview of 'stacked PRs' , a feature to break large changes into smaller, dependent parts. 
 TanStack Router, Start, and Query have gained beta support for Solid 2.0. 
 🎤 A 50-minute chat (with transcript) from two of the developers behind the npmx project — an increasingly popular way to browse the npm registry. 
 JSON Alexander is a new JSON viewer extension for Chrome and Firefox from Wes Bos, complete with a snazzy George Costanza logo.
```

---
