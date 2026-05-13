# Golang Weekly

> 分类: 技术周刊
> URL: https://golangweekly.com/rss/
> 抓取: 4 篇

---

## 1. 11 security fixes land in Go

- 日期: 2026-05-08 00:00
- 链接: https://golangweekly.com/issues/600

```
#​600 — May 8, 2026 
 Read the Web Version 
 Go Weekly 
 Go 1.26.3 and Go 1.25.10 Released with 11 Security Fixes — The headline issue is a module-proxy checksum bypass that lets untrusted proxies serve altered modules and Go toolchains, but areas as diverse as net/mail , go bug , net/http and html/template also get fixes. The proxy bug was found by an LLM, and over on Bluesky, Russ Cox apologized for its long-term presence. 
 Go Security Team 
 Azure HorizonDB at POSETTE: An Event for Postgres 2026 — Explore 44 talks about Azure HorizonDB, PostgreSQL-backed app development, Postgres performance & AI, Postgres 19 and more at POSETTE 2026, a free & virtual developer event, happening 16-18 Jun. Don’t miss your favorites - use Add to Calendar . 
 Microsoft | AMD sponsor 
 How Figma Built the Bouncer It Needed for Postgres in Go — Figma’s database team built their own Postgres connection pooler in Go on top of jackc/pgx and backpressure . It’s not open source (yet) but they go deep into the design here, complete with plentiful illustrations. 
 He, Goh, and Baid (Figma) 
 THREE GO PROPOSALS: 
 Felix Geisendörfer has proposed adding an rss profile type to runtime/pprof to broaden the view of overall physical memory usage. 
 Cherry Mui proposed enabling AMD64 architecture-specific SIMD intrinsics by default. There's still work to do, though, so it's not going to happen till Go 1.28. 
 Neal Patel has suggested go doc gets a -test option to include symbols from test files in documentation, such as may be useful for LLM agents. 
 Notes From Optimizing CPU-Bound Go Hot Paths — Lessons learned from optimizing CPU-bound hot paths while porting Brotli to pure Go, including how Go’s abstractions can impact performance in hot loops, what does and doesn’t get inlined, and some workarounds. 
 Andrii Berezhynskyi 
 One Database. Zero Pipelines. Full Postgres — Extend Postgres: hypertables, 95% compression, continuous aggregates. Analytics on live data. $1000 credit to start . 
 Tiger Data (creators of TimescaleDB) sponsor 
 📄 Hoisting Wire Plumbing Out of Your Go Handlers – Write your Go handler plumbing once, not once per endpoint. Redowan Delowar 
 📄 A Gopher Meets a Crab – A Go developer's tale of spending time trying to "fit Rust into a Go-shaped brain." Paul Hinze 
 🛠 Code & Tools 
 Solod v0.1: Go Ergonomics, Practical Stdlib, Native C Interop — For the past few months, Anton has been working on this system-level language with a Go syntax and no runtime. v0.1 has ports of key parts of the stdlib like io , bytes , fmt , os , time , and strings . This post includes benchmarks and examples, including how Solod can interface with SQLite. 
 Anton Zhiyanov 
 💡 There are some parallels in the Ruby world, where Ruby's creator, Matz, is working on Spinel , a compiler that similarly compiles a subset of Ruby to C. 
 Boring: A Single-Binary SSH Tunnel Manager — 
An SSH tunnel manager that "just works": single binary, TOML config, ssh_config compatibility, automatic reconnects, and a TUI for starting/stopping tunnels on demand. 
 Florian Becker 
 mvm: A Fresh Take on an 'Interpreter' for Go — Six years ago we first featured yaegi (Yaegi is Another Elegant Go Interpreter), a Go interpreter suitable for embedding into other apps. mvm , from the creator of yaegi, is a new take on the idea, instead compiling Go to bytecode for a VM to run. 
 Marc Vertes 
 💡 There's a web-based playground where you can give mvm a spin. 
 go-githubapp: A Go Library for Building GitHub Apps — A simple framework for building GitHub Apps that handle GitHub webhooks. 
 Palantir 
 📷 imagemeta v1.0 – Extract EXIF and XMP metadata from JPEG, HEIC, AVIF, TIFF and RAW camera images. 
 gotreesitter 0.16 – Pure-Go tree-sitter runtime (no Cgo). v0.16 adds native UTF-16 parsing/editing. 
 postgresparser 1.2 – ANTLR-based pure-Go PostgreSQL-dialect SQL parser. 
 go-github 86.0 – Go client library for GitHub's REST API (v3). 
 📰 Classifieds 
 CodeRabbit : Your team's second brain. Now in Slack. One agent for your entire SDLC to keep context and cut review time. Trusted by 6M+ repos. 
 ⚙️ Go finally has an AI agent framework that isn't a Python port . Agents as http.Handler s, orchestrate LLMs & Claude Code. Open source. agentfield.ai .
```

---

## 2. Three new Go proposals

- 日期: 2026-05-01 00:00
- 链接: https://golangweekly.com/issues/599

```
#​599 — May 1, 2026 
 Read the Web Version 
 Go Weekly 
 Zero-Config Go Heap Profiling — Go’s runtime samples heap allocations automatically, but the linker disables this in apps that don’t import runtime/pprof or net/http/pprof . This tour of runtime.mbuckets and /proc/<pid>/mem is a good read if you’ve wondered where pprof data actually lives, or how to grab a heap profile from a process you can’t redeploy. 
 Nikolay Sivko 
 You Chose Go for Simplicity. Then Added a Pipeline — A second database means sync lag, drift, and infrastructure that only grows. TimescaleDB extends Postgres with hypertables, 95% compression, and continuous aggregates. Run analytics on live data, no second system. Start building for free . 
 Tiger Data (creators of TimescaleDB) sponsor 
 🎉 GopherCon 2026: August 3-6 in Seattle, WA — Tickets for this year’s GopherCon are now available, including for a variety of workshops from folks like Bill Kennedy and Johnny Boursiquot. The conference agenda is filling out nicely, too, but the final reveal of all the main talks isn’t till next week. 
 GopherCon 
 NEW GO PROPOSALS: 
 Go co-designer Robert Griesemer has made a proposal to add a StringLen function to go/constant . 
 Should error message text be explicitly excluded from the Go 1 compatibility promise? The proposer cites a comment in net/http saying an error message can't be changed as evidence of the current ambiguity. 
 🔒 Neal Patel of the Go security team proposes adding 'profiles' to crypto/tls that bound what the rest of tls.Config 's vast array of settings can do. 
 Gojit: A Revived JIT Compiler in Go — Go’s AOT compilation makes JIT unnecessary in most cases, but what if you’re writing an emulator or interpreter that would benefit? This post revives a 2014 experiment for modern Go and solves the problem of letting JIT-generated code call back into Go functions without crashing the GC. Aaron explains more ▶️ in this five-minute video. 
 Aaron Balke 
 Swissing a Table — A look at building a Swiss table (the idea behind Go’s new map implementation ), one concept at a time, with benchmarks to see what effect each new technique has. The bit-twiddling section near the end is a highlight. 
 Phil Pearl 
 Orchestrate LangChain Agents for Production with Orkes — Learn how to run, scale, and monitor AI agents reliably in production with Orkes Conductor. 
 Orkes sponsor 
 FastCGI: 30 Years Old and Still the Better Protocol for Reverse Proxies? — FastCGI is 30, and still offers some advantages over HTTP. And Go’s standard library supports it too, making the change a single line if you want to give it a try. 
 Andrew Ayer 
 📄 Choosing a Go Logging Library in 2026 – Rounds up Slog, Zerolog, Zap, and others. Dash0 
 📄 Building a Userspace TCP-Over-UDP Stack in Pure Go – Built for a P2P AI agent network stack called Pilot Protocol . Philip Stayetski 
 📄 It's A Lock: sync.Mutex in Go – A clear, beginner-friendly walk through sync.Mutex . John Arundel 
 📄 Peeking Into Go Struct Tags Redowan Delowar 
 🛠 Code & Tools 
 Plow 1.4: A High-Performance HTTP Benchmarking Tool — Uses fasthttp under the hood and offers both a TUI and Web-based UI for measuring results. Also available via Homebrew or as a Docker container. 
 ddc et al. 
 Rapid 1.3: Property-Based Testing Library — Checks that properties you define hold for a large number of automatically generated test cases. If a failure is found, the failing case is automatically minimized before presentation. This example on the Go Playground shows off the core idea. 
 Gregory Petrosyan 
 Limen: A Composable Authentication Library — A plugin-first authentication library that ships with the essentials (session management, cookie handling, rate limiting, security primitives) but then lets you compose the rest of the stack where you need username/password, OAuth 2.0, 2FA, etc. GitHub repo. 
 Brian Iyoha 
 MongoDB Go Driver 2.6 – The official MongoDB driver adds support for Intelligent Workload Management (IWM) and ingress connection rate limiting. 
 Go-MySQL-Driver 1.10 – MySQL driver for database/sql . The first notable release in a year and now modernized for Go 1.22+. 
 bleve 2.6 – Long-standing text/numeric/geo-spatial/vector indexing library. 
 Chroma 2.24 – Pure Go syntax highlighter. Adds/updates several lexers. 
 rqlite 10.0 – Go-powered, SQLite-backed fault-tolerant database. 
 fsnotify v1.10.0 – Cross-platform filesystem notifications library. 
 ✉️ gog 0.14 – CLI interface for Gmail, Calendar, Drive, etc. 
 Fiber 3.2 – Express-inspired web framework. 
 📰 Classifieds 
 🐰 Cut code review time & bugs in half. Get instant code review feedback. Trusted across 3M+ repos & 100K+ open-source projects. Try it for free . 
 ⚙️ Go finally has an AI agent framework that isn't a Python port . Agents as http.Handler s, orchestrate LLMs & Claude Code. Open source. agentfield.ai .
```

---

## 3. TinyGo can now compile the TypeScript compiler

- 日期: 2026-04-24 00:00
- 链接: https://golangweekly.com/issues/598

```
#​598 — April 24, 2026 
 Read the Web Version 
 Go Weekly 
 TinyGo 0.41: Go 1.26 Support, ESP32 Wireless, and More — A huge release for the “Go compiler for small places” ! Go 1.26 support arrives, along with wireless support for ESP32 devices, so you can create and run networked services with Go on these tiny devices. There’s also Arduino UNO Q support, and TinyGo can now even compile the TypeScript 7 compiler. 
 The TinyGo Team 
 Write Better Prompts — Join GitHub's Sabrina Goldfarb for this detailed video course on generating higher quality code with AI. Learn practical prompting techniques that work consistently across tools and transform your project ideas into reality. 
 Frontend Masters sponsor 
 The Standard uuid Package Proposal Has Been Accepted; Possibly Coming in Go 1.27 — 
The proposal for a native uuid package has been accepted and the first commit is already in. UUIDs v4 and v7 are supported. Damien Neil's explainer provides a good read on the rationale and design, or you might prefer Redowan Delowar's higher level look . 
 Damien Neil / Go Proposal Review 
 IN BRIEF: 
 A proposal for a new goroutine leak detector profile has been accepted. 
 Discussion about supporting dependency cooldowns in Go is ongoing. 
 Go 1.27 will drop support for macOS 12 (Monterey) . 
 Building a Container from Scratch in Go — A developer wanted to understand how Docker containers work under the hood and set out to build a minimal one in Go from scratch, starting with Linux namespaces. 
 Vedant Gandhi 
 Understanding the Go Runtime: The Network Poller — One of Jesús’s typical deep dives, this time on how Go makes blocking network code not actually block a thread. Covers the parking protocol, epoll/kqueue/IOCP, and the observation that “waiting for goroutines and waiting for I/O are the same waiting.” 
 Jesús Espino 
 Your Agent Hit the 2-Project Limit by Lunch — ghost gives your agent unlimited free Postgres. No 2-project cap, no credit card, one CLI. 1TB storage. Try for free . 
 ghost sponsor 
 📄 Go and Rust Programs Appear to Start Equally Fast (on Some Machines) – The startup difference is on the order of sub-milliseconds. Chris Siebenmann 
 📄 Raftly: Building a Production-Grade Raft Implementation from Scratch – With the curious goal of being designed to fail. Anirudh Sharma 
 📄 Tracing Goroutines in Realtime with eBPF – A beautifully presented article. Ozan Sazak 
 🛠 Code & Tools 
 goshs 2.0: For When python3 -m http.server Doesn't Cut It — A Go-powered, single-binary file server you can rapidly deploy not only to get a quick HTTP/S server running, but WebDAV, SFTP, SMB, DNS, and other protocols too. It can also send notifications via webhooks . ( GitHub repo. ) 
 Patrick Hener 
 TamaGo: Where the Go Runtime Is the Kernel — A framework for compiling and executing Go apps on bare metal processors (AMD64, ARM, ARM64, and RISCV64). Former Go core team member Brad Fitzpatrick has just used this to get Tailscale running on UEFI. 
 The TamaGo Authors 
 TypeScript 7.0 Beta: A 10x Faster Compiler, Thanks to Go — TypeScript 7.0 is a Go-powered native port of TypeScript's compiler boasting “about 10 times faster” performance. Curiously, Microsoft collaborated with the TinyGo team so it can also be compiled with TinyGo 0.41 (featured above) . 
 Microsoft 
 🤖 Kronk: Hardware-Accelerated Local LLM Inference for Go — 
A local-inference runtime for Go apps, wrapping llama.cpp through yzma bindings and exposing an OpenAI-compatible API. Check out the code for wiring up a simple chat mechanism with it. 
 Bill Kennedy (Ardan Labs) 
 RabbitMQ Stream Go Client 1.8 – Official Go client library for RabbitMQ's stream queues. 
 go-github 85.0 – Client library for the GitHub API v3. 
 📄 pdfcpu 0.12 – Go-based PDF processing library. 
 linodego 1.68.0 – Go client for Linode's REST API. 
 💬 slack-go 0.23 – Official Slack API library. 
 📰 Classifieds 
 ⚙️ Go finally has an AI agent framework that isn't a Python port . Agents as http.Handler s, orchestrate LLMs & Claude Code. Open source. agentfield.ai . 
 📢  Elsewhere in the ecosystem 
 Git 2.54 has been released with two headline features: 
 git history offers a new, easier way to edit commit messages or interactively split a commit. 
 You can now define hooks in config files (at repo, user, or system level) rather than only in .git/hooks . You can also run multiple hooks for the same event. 
 Ben Hoyt (creator of GoAWK ) is having fun with an indecisive AI coding agent. Ben gives us a real-world example of taking back the reins. 
 Sanghee Son's friend unplugged his Raspberry Pi so he built a homelab manager in Go called homebutler which provides a CLI and MCP server to monitor and control his homelab's servers and network. 
 Cloudflare has released a preview of its new cf CLI tool for working with its various services.
```

---

## 4. What it takes to add new syntax to Go

- 日期: 2026-04-17 00:00
- 链接: https://golangweekly.com/issues/597

```
#​597 — April 17, 2026 
 Read the Web Version 
 Go Weekly 
 Let’s Add a Conditional Expression to Go — Not a proposal for a real Go feature, but an epic tour through the Go compiler, including the parser, type checker, IR, and the walk desugaring stage, showing what it takes to implement a new syntax feature. Few of us dig this deep, so it’s neat to see it come together. 
 Matvey Korinenko 
 44 Postgres Talks To Choose From in One Virtual Event — POSETTE: An Event for Postgres 2026 is a free & virtual developer event on 16-18 Jun. All 44 talks stream live & will be available later. Join live to take part in discussions with speakers & attendees. Check out the schedule and mark your calendar . 
 Microsoft | AMD sponsor 
 How GitHub Uses eBPF from Go to Improve Deployment Safety — A nice example of Go being used to build kernel-level tooling. Here, they used ebpf-go to create a circular dependency detection system. 
 Gripper and Levenstein (GitHub) 
 watgo: A WebAssembly Toolkit for Go — A zero-dependency, pure Go toolkit for parsing WAT, validating it, and creating WASM binaries (and decode back, too). It comes as a CLI tool and Go library. A must-see for anyone working with WASM in Go. GitHub repo . 
 Eli Bendersky 
 IN BRIEF: 
 The TinyGo team says its next release, due next Tuesday, is a big one, with Go 1.26 support plus full Arduino UNO Q support. 
 The /r/golang subreddit does a weekly thread focusing on 'small projects' – Go-based projects people want to share that don't necessarily meet the usual quality bar for the sub. 
 🎤 The Cup o' Go podcast interviewed Creed Haymond of Epic Games ( Fortnite! ) about Go's role in game infrastructure and how his team is migrating from Spring (Java) to Go. 
 Sky is an Elm-inspired functional language that compiles to Go. 
 Error Translation in Go Services — In layered services, storage errors like sql.ErrNoRows can easily leak into HTTP or gRPC handlers, coupling transport to storage. It’s better to define domain sentinels and translate twice: storage to domain in the repository, domain to wire format in the handler. 
 Redowan Delowar 
 📄 Structuring a Go Service with the Repository Pattern – A worked example of the repository pattern and domain-first project layout. Paweł Grzybek 
 📄 Building Gemma 4 Local-Powered LLM Apps with Go and Yzma Vladimir Vivien 
 📄 Parsing 11 Languages in Pure Go Without CGO Gagan Deep Singh 
 🛠 Code & Tools 
 Garble: A Toolchain to Obfuscate Go Builds — Obfuscation doesn’t guarantee security but if you want your binaries to have “as little information about the original source code as possible,” Garble does its best using these techniques. v0.16 targets Go 1.26 only. 
 Daniel Martí 
 Your go.mod Is Clean. Your Infrastructure Should Be Too — TimescaleDB extends Postgres for analytics on live data. No second database, no pipeline. Try for free . 
 Tiger Data (creators of TimescaleDB) sponsor 
 libopenapi: OpenAPI Parser and Validation Library — Full support for Swagger and OpenAPI 3.0, 3.1, and 3.2. Designed specifically to handle “the largest and most complex specifications you can think of.” 
 Princess Beef Heavy Industries, LLC 
 Hedge: Adaptive Hedged Requests for Cutting Tail Latency — An http.RoundTripper that adaptively fires backup requests when the primary exceeds a per-host p90 latency estimate, with a token-bucket budget to prevent load amplification during outages. A practical take on Google’s The Tail at Scale . 
 Prathamesh Bhope 
 gontainer: A Dependency Injection Container for Go — A small reflection-based DI container from NVIDIA with no dependencies or code generation. You register factory functions and let it wire up your services from their param types. 
 NVIDIA Corporation 
 😬 Spank: Hit Your MacBook and It Yells Back… — A silly experiment using the accelerometer in modern Macs. 
 Tai Groot 
 🔓 piv-go 2.6 – Library for managing PIV keys and X.509 certs on YubiKeys. 
 go-huggingface 0.3.5 – Download files, models & tokenizers from HuggingFace. 
 GitHub MCP Server 1.0 – GitHub's official MCP/API server is written in Go. 
 GoMLX 0.27.3 – Full-featured, accelerated cross-platform ML framework. 
 🤖 yzma 1.12.0 – Integrate Go apps with llama.cpp for local inference. 
 forbidigo v2.3.1 – Go linter for forbidding specified identifiers in code. 
 go-git 5.18 – Extensible pure Go Git implementation library. 
 📰 Classifieds 
 Skip the README archaeology. Flox delivers reproducible dev environments with no system pollution. One command, zero friction. Try it free . 
 Real-time search data for backend engineers who care about reliability and scale. 
 👀 A Go ..od Way to Read Hacker News? 
 Circumflex 4.0: A Terminal-Based Hacker News Client — We first linked to this Bubble Tea -based terminal client for Hacker News in 2022, but it’s come a long way since. v4.0 adds a native comment section view and a built-in ‘reader mode’ for linked items. 
 Ben Sadeh
```

---
