# This Week in Rust

> 分类: 技术周刊
> URL: https://this-week-in-rust.org/atom.xml
> 抓取: 4 篇

---

## 1. This Week in Rust 650

- 日期: 2026-05-06 00:00
- 链接: https://this-week-in-rust.org/blog/2026/05/06/this-week-in-rust-650/

```
Hello and welcome to another issue of This Week in Rust ! Rust is a programming language empowering everyone to build reliable and efficient software.
This is a weekly summary of its progress and community.
Want something mentioned? Tag us at @thisweekinrust.bsky.social on Bluesky or @ThisWeekinRust on mastodon.social, or send us a pull request .
Want to get involved? We love contributions . 
 This Week in Rust is openly developed on GitHub and archives can be viewed at this-week-in-rust.org .
If you find any errors in this week's issue, please submit a PR . 
 Want TWIR in your inbox? Subscribe here . 
 Updates from Rust Community 
 Official 
 Announcing Google Summer of Code 2026 selected projects 
 Newsletters 
 Rust Trends Issue 77 - Rust Sharpens the Craft 
 Project/Tooling Updates 
 Imgclip: A Cross-Platform CLI for Clipboard ↔ Image File Conversion 
 Connectors: Where AimDB Meets the Real World 
 rkik-nts 1.0.0: a high-level Rust Network Time Security (RFC 8915) client library 
 unix-ancillary 0.2.2 — safe SCM_RIGHTS fd-passing for Rust 
 kache 0.2.0: zero-copy, content-addressed Rust build cache (RUSTC_WRAPPER) 
 Fileman - a cross-platform 2-panel file manager 
 Observations/Thoughts 
 One week of view_types 
 Async Rust never left the MVP state 
 stable specialization in Rust 
 Your Clippy Config Should Be Stricter 
 Your Clippy Config Should Be Stricter-er 
 The Sync bound nobody asked for 
 Cross-platform Rust: Analyzing how WhatsApp, Signal and more are shipping Rust to billions of devices 
 [audio] Netstack.FM episode 37 — dial9: from black box to insight in Tokio 
 Rust Walkthroughs 
 oops, cubic macro! 
 [video] RustCurious lesson 7: Arrays and Slices 
 Writing Middlewares for Rust Lambda Functions 
 Learn Error Handling in Rust By Building a TOML Config Parser 
 Miscellaneous 
 Awesome SQLx Resources 
 Crate of the Week 
 This week's crate is burn , a tensor and deep learning library. 
 Thanks to Jonas for the suggestion! 
 Please submit your suggestions and votes for next week ! 
 Calls for Testing 
 An important step for RFC implementation is for people to experiment with the
implementation and give feedback, especially before stabilization. 
 If you are a feature implementer and would like your RFC to appear in this list, add a call-for-testing label to your RFC along with a comment providing testing instructions and/or
guidance on which aspect(s) of the feature need testing. 
 No calls for testing were issued this week by Rust , Cargo , Rustup or Rust language RFCs . 
 Let us know if you would like your feature to be tracked as a part of this list. 
 Call for Participation; projects and speakers 
 CFP - Projects 
 Always wanted to contribute to open-source projects but did not know where to start?
Every week we highlight some tasks from the Rust community for you to pick and get started! 
 Some of these tasks may also have mentors available, visit the task page for more information. 
 No Calls for participation were submitted this week. 
 If you are a Rust project owner and are looking for contributors, please submit tasks here or through a PR to TWiR or by reaching out on Bluesky or Mastodon ! 
 CFP - Events 
 Are you a new or experienced speaker looking for a place to share something cool? This section highlights events that are being planned and are accepting submissions to join their event as a speaker. 
 Scientific Computing in Rust 2026 | 2026-06-05 | Virtual | 2026-07-08 - 2026-07-10 
 If you are an event organizer hoping to expand the reach of your event, please submit a link to the website through a PR to TWiR or by reaching out on Bluesky or Mastodon ! 
 Updates from the Rust Project 
 504 pull requests were merged in the last week 
 Compiler 
 canonicalize free regions from inputs as placeholders in root univ 
 Library 
 don't reload length in String::push 
 Cargo 
 feat(lints) : Add deny-by-default text_direction_codepoint lints 
 fix(compile) : Where possible, hint about misplaced deps 
 fix(config): [env] relative paths definition 
 fix(config) : normalize included config paths 
 remove curl dependency from crates-io crate 
 Rustdoc 
 fix doc_cfg feature on reexports 
 preserve parent doc cfg for macro_export macros 
 Clippy 
 add a check for some followed by filter 
 fix bad_bit_mask ICE for overloaded bit ops 
 needless_return_with_question_mark trigger in async functions 
 Rust-Analyzer 
 diagnostics : add handler for E0130 
 add AssocItemList add_item editor variant 
 expand glob import on cyclic import fail 
 add diagnostic for E0784 
 allow renaming of elided lifetimes 
 diagnose trait errors 🎉 
 emit a diagnostic for non_exhaustive struct when constructed 
 offer on if-expr with else-if for convert_to_guarded_return 
 support if-else in value on postfix completions 
 add missing exprs to visiting 
 add missing solver lang items 
 add semicolon after expr in stmt for unwrap_branch 
 catch #[rustc_reservation_impl = "reason"] 
 don't fetch diagnostics until proc-macros are loaded 
 don't panic on impl ?Sized for introduce_named_type_parameter 
 fix unwrap_branch in match_arm 
 fix stack overflow on projection display 
 handle empty expr in tuple expr 
 improve prettify_macro_expansion() 
 improve whitespaces for trait item complete 
 infer the expected type as the return type for async blocks defined by async fns 
 port array and ref exprs inference from rustc 
 qualify .new path and no complete generic params 
 remove usage of references_error() in upvar inference 
 show the user's message for #[must_use] 
 use Pattern_White_Space for whitespace handling 
 various fixes for lower_coroutine_body_with_moved_arguments() 
 wrap top level or patterns in parens in convert_match_to_let_else 
 hir-ty: emit diagnostic for unused #[must_use] values 
 ide-diagnostics: emit error for duplicate field in record expression 
 ide-diagnostics: emit error for mismatched array pattern length 
 migrate generate function to SyntaxEditor 
 perf: cache more things that are related to lang items (paren traits, children/sibling assoc types/functions) but are not lang items themselves 
 perf: do not intern AdtDef 
 perf: improve performance of integer-based symbols 
 remove add predicate for Where syntax 
 remove unused a method in edit_in_place 
 replace insert use and insert use as alias with its editor variant 
 use syntaxFactory in generic arg instead of vanilla make 
 Rust Compiler Performance Triage 
 This week's result is pretty much neutral. It looks negative in icount numbers, but that's spurious, wall time remained largely unchanged. Some big performance improvements landed in the new solver, which is not enabled by default, yet. 
 Triage done by @panstromek .
Revision range: ca9a134e..1d72d7e8 
 Summary : 
 (instructions:u) mean range count 
 Regressions ? 
 (primary) 0.6% [0.2%, 1.2%] 106 
 Regressions ? 
 (secondary) 0.7% [0.2%, 2.4%] 67 
 Improvements ? 
 (primary) -0.6% [-1.7%, -0.2%] 66 
 Improvements ? 
 (secondary) -0.6% [-2.8%, -0.0%] 60 
 All ?? (primary) 0.1% [-1.7%, 1.2%] 172 
 1 Regression, 2 Improvements, 9 Mixed; 5 of them in rollups
34 artifact comparisons made in total 
 Full report here 
 Approved RFCs 
 Changes to Rust follow the Rust RFC (request for comments) process . These
are the RFCs that were approved for implementation this week: 
 No RFCs were approved this week. 
 Final Comment Period 
 Every week, the team announces the 'final comment period' for RFCs and key PRs
which are reaching a decision. Express your opinions now. 
 Tracking Issues & PRs 
 Rust 
 Make trait refs & assoc ty paths properly induce trait object lifetime defaults 
 validate #[link_name = "..."] & #[link(name = "...")] parameters 
 Improve precision of Duration-float operations 
 Tracking Issue for unsafe_cell_access 
 Tracking Issue for producing a Result<(), E> from a bool 
 Allow shortening lifetime in CoerceUnsized for &mut 
 Ensure Send/Sync is not implemented for std::env::Vars{,Os} 
 feat(rustdoc): stabilize --emit flag 
 Make Infallible = ! 
 Add lint againts invalid runtime symbol definitions 
 error on empty export_name 
 Check arguments of attributes where no arguments are expected 
 stabilize feature(cfg_target_has_atomic_equal_alignment) 
 fix: fix the capture behavior of if let in closures 
 Resolver: Batched Import Resolution 
 Ensure Send/Sync impl for std::process::CommandArgs 
 Compiler Team (MCPs only) 
 Turn long-deprecated -C options into errors 
 Promote loongarch32-unknown-none* to Tier 2 
 Rust RFCs 
 Propose the concept of a crates.io username for identity 
 Language Team 
 Revise decision process: champion vs FCP decisions 
 No Items entered Final Comment Period this week for Cargo , Language Reference , Leadership Council or Unsafe Code Guidelines . Let us know if you would like your PRs, Tracking Issues or RFCs to be tracked as a part of this list. 
 New and Updated RFCs 
 Initial Rustdoc LaTeX math RFC 
 Project-wide LLM policy 
 Upcoming Events 
 Rusty Events between 2026-05-06 - 2026-06-03 🦀 
 Virtual 
 2026-05-06 | Virtual (Cardiff, UK) | Rust and C++ Cardiff Practical introduction to SIMD 
 2026-05-06 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-05-06 | Virtual (Indianapolis, IN, US) | Indy Rust Indy.rs - with Social Distancing 
 2026-05-07 | Virtual (Berlin, DE) | Rust Berlin Rust Hack and Learn 
 2026-05-07 | Virtual (Nürnberg, DE) | Rust Nuremberg Rust Nürnberg online 
 2026-05-09 | Virtual (Girona, ES) | Rust Girona Learning Rust the Hard Way: Building a TUI Chess Game 
 2026-05-12 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Second Tuesday 
 2026-05-12 | Virtual (London, UK) | Women in Rust 👋 Community Catch Up 
 2026-05-12 | Virtual (Tel Aviv-yafo, IL) | Code Mavens 🦀 - 🐍 - 🐪 Introduction to database access using Rust SQLx 
 2026-05-17 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Rust Deep Learning: Third Sunday 
 2026-05-19 | Virtual (Washington, DC, US) | Rust DC Mid-month Rustful 
 2026-05-20 | Hybrid (Vancouver, BC, CA) | Vancouver Rust Mouse Control with Rust 
 2026-05-20 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-05-21 | Hybrid (Seattle, WA, US) | Seattle Rust User Group May, 2026 SRUG (Seattle Rust User Group) Meetup 
 2026-05-21 | Virtual (Berlin, DE) | Rust Berlin Rust Hack and Learn 
 2026-05-21 | Virtual (Charlottesville, VA, US) | Charlottesville Rust Meetup Tock OS Part #4 - Capsule coding in QEMU! 
 2026-05-26 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Fourth Tuesday 
 2026-05-26 | Virtual (London, UK) | Women in Rust Lunch & Learn: Seeing Into Your Code - A Practical Guide to Tracing in Rust 
 2026-05-27 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-06-03 | Virtual (Indianapolis, IN, US) | Indy Rust Indy.rs - with Social Distancing 
 Africa 
 2026-05-12 | Johannesburg, ZA | Johannesburg Rust Meetup Rust by Example - Flow of Control 
 Asia 
 2026-05-13 | Malaysia, MY | Rust Meetup Malaysia Rust Meetup May 2026 
 2026-05-14 | Seoul, KR | Seoul Rust (Programming Language) Meetup Seoul Rust Meetup 
 2026-05-16 | Bangalore, IN | Rust Bangalore May 2026 Rustacean meetup 
 Europe 
 2026-05-06 | Köln, DE | Rust Cologne Rust in May: Rust for Starters, Part 2 
 2026-05-06 | Milano, MI, IT | Rust Language Milan Rust Milan @ Python Milano: Python or Rust? Yes! 
 2026-05-06 | Oxford, UK | Oxford ACCU/Rust Meetup. Building LLMs from scratch 
 2026-05-07 | Edinburgh, UK | Rust and Friends Rust May Talks: Aetherus + Bevy 
 2026-05-11 | Augsburg, DE | Rust Meetup Augsburg Rust Meetup #19 : Tiago Manczak - Game On with Rust & Pico 
 2026-05-13 | Girona, ES | Rust Girona Rust Girona Hack & Learn 05 2026 
 2026-05-14 | Switzerland, CH | PostTenebrasLab Rust Meetup Geneva 
 2026-05-18 - 2026-05-23 | Amsterdam, NL | RustWeek 2026 RustWeek 2026 
 2026-05-18 | Milano, MI, IT | Rust Language Milan RustWeek 2026 
 2026-05-19 | Aarhus, DK | Rust Aarhus Hack Night 
 2026-05-19 | Amsterdam, NL | RustNL RustWeek 2026 announcement 
 2026-05-19 | Leipzig, DE | Rust - Modern Systems Programming in Leipzig Cross-Building & Cross-Testing 
 2026-05-19 | London, UK | Women in Rust RustWeek lunch meetup 
 2026-05-21 | Amsterdam, NL | RustNL RustWeek Hackathon 
 2026-05-22 | Amsterdam, NL | RustNL Bike tour around Utrecht 
 2026-05-26 | Dortmund, DE | Rust Dortmund Rust Dortmund Meetup - Agentic Programming - May 
 2026-05-26 | Manchester, UK | Rust Manchester Rust Manchester May Code Night 
 2026-05-29 | Berlin, DE | Rust Berlin Rust Berlin Talks: The next generation 
 North America 
 2026-05-07 | New York, NY, US | Rust NYC Rust NYC: Reversing the Great Firewall and Geospatial Rust 
 2026-05-07 | Saint Louis, MO, US | STL Rust Open Project Night 
 2026-05-09 | Boston, MA, US | Boston Rust Meetup Back Bay Rust Lunch, May 9 
 2026-05-14 | Mountain View, CA, US | Hacker Dojo RUST MEETUP at HACKER DOJO 
 2026-05-14 | Portland, OR, US | PDXRust From Radio Waves to Pixels - Real-Time Visualizations with Rust and WebAssembly 
 2026-05-14 | San Diego, CA, US | San Diego Rust San Diego Rust May Meetup - Back in person! 
 2026-05-16 | Boston, MA, US | Boston Rust Meetup Lechmere Rust Lunch, May 16 
 2026-05-19 | San Francisco, CA, US | San Francisco Rust Study Group Rust Hacking in Person 
 2026-05-20 | Hybrid (Vancouver, BC, CA) | Vancouver Rust Mouse Control with Rust 
 2026-05-20 | San Francisco, CA, US | Bay Area Rust Meetup Bay Area Rust Meetup 
 2026-05-21 | Hybrid (Seattle, WA, US) | Seattle Rust User Group May, 2026 SRUG (Seattle Rust User Group) Meetup 
 2026-05-21 | Nashville, TN, US | Music City Rust Developers Community Meetup 
 2026-05-23 | Boston, MA, US | Boston Rust Meetup Allston Rust Lunch, May 23 
 2026-05-27 | Austin, TX, US | Rust ATX Rust Lunch - Fareground 
 2026-05-28 | Atlanta, GA, US | Rust Atlanta Rust-Atl 
 2026-05-28 | Los Angeles, CA, US | Rust Los Angeles Rust LA: Rust in Embedded & Autonomous Systems at Parallel Systems in DTLA 
 2026-05-30 | Boston, MA, US | Boston Rust Meetup Central Cambridge Rust Lunch, May 30 
 Oceania 
 2026-05-14 | Melbourne, AU | Rust Melbourne Rust Melbourne - May 2026 
 2026-05-26 | Barton, ACT, AU | Canberra Rust User Group May Meetup 
 South America 
 2026-05-13 | Montevideo, UY | Rust Meetup Uruguay Rust Uruguay meetup de Mayo 
 If you are running a Rust event please add it to the calendar to get
it mentioned here. Please remember to add a link to the event too.
Email the Rust Community Team for access. 
 Jobs 
 Please see the latest Who's Hiring thread on r/rust 
 Quote of the Week 
 From a business standpoint, we should have reasonable confidence that it’ll stick around and be healthy for more than 10 years. We’d also like a robust ecosystem of code and tools that we can rely on, and experts we can hire. 
 – David Anderson on the tailscale blog 
 Thanks to Ivan Fraixedes for the suggestion! 
 Please submit quotes and vote for next week! 
 This Week in Rust is edited by: 
 nellshamrell 
 llogiq 
 ericseppanen 
 extrawurst 
 U007D 
 mariannegoldin 
 bdillo 
 opeolluwa 
 bnchi 
 KannanPalani57 
 tzilist 
 Email list hosting is sponsored by The Rust Foundation 
 Discuss on r/rust
```

---

## 2. This Week in Rust 649

- 日期: 2026-04-29 00:00
- 链接: https://this-week-in-rust.org/blog/2026/04/29/this-week-in-rust-649/

```
Hello and welcome to another issue of This Week in Rust ! Rust is a programming language empowering everyone to build reliable and efficient software.
This is a weekly summary of its progress and community.
Want something mentioned? Tag us at @thisweekinrust.bsky.social on Bluesky or @ThisWeekinRust on mastodon.social, or send us a pull request .
Want to get involved? We love contributions . 
 This Week in Rust is openly developed on GitHub and archives can be viewed at this-week-in-rust.org .
If you find any errors in this week's issue, please submit a PR . 
 Want TWIR in your inbox? Subscribe here . 
 Updates from Rust Community 
 Newsletters 
 The Embedded Rustacean Issue #70 
 Scientific Computing in Rust #17 (April 2026) 
 Project/Tooling Updates 
 lean-ctx: A Context Runtime for AI Coding Agents 
 Zed is 1.0 
 Niri v26.04 
 Announcing Symposium 
 menhera-cooldown: The crates.io Cooldown Proxy 
 cargo-cooldown 0.3.0: a Cargo wrapper for supply-chain cooldowns 
 Nutype 0.7.0 
 AimDB: Reactive Pipelines as the Engine of the Data-First Architecture 
 pyscan v2.1.0: Python Dependency Vulnerability Scanner 
 flodl 0.5.3 
 Blade XR Asteroids 
 Observations/Thoughts 
 Bugs Rust Won't Catch 
 A Gopher Meets a Crab 
 Using Rust to Build a $1 Handheld Gaming Console 
 All databases will eventually be (re)written in Rust 
 [video] Rust India Conference 2026 — Full Talk Recordings 
 [audio] Helsing with Jon Gjengset 
 Rust Walkthroughs 
 Build a JSON Parser in Rust from Scratch 
 device-envoy-esp: Making Embedded ESP32 Fun: With Rust, Embassy, and Composable Device Abstractions 
 Rust Projects - Write a Redis Clone - Version 2.0.0 
 [video] Rust Parallelism with Rayon - Use ALL CPUs 
 Research 
 Performance of Rust language 
 Miscellaneous 
 awesome axum 
 Crate of the Week 
 This week's crate is dithr , a buffer-first dithering and halftoning library. 
 Thanks to pbkx for the self-suggestion! 
 Please submit your suggestions and votes for next week ! 
 Calls for Testing 
 An important step for RFC implementation is for people to experiment with the
implementation and give feedback, especially before stabilization. 
 If you are a feature implementer and would like your RFC to appear in this list, add a call-for-testing label to your RFC along with a comment providing testing instructions and/or
guidance on which aspect(s) of the feature need testing. 
 No calls for testing were issued this week by Rust , Cargo , Rustup or Rust language RFCs . 
 Let us know if you would like your feature to be tracked as a part of this list. 
 Call for Participation; projects and speakers 
 CFP - Projects 
 Always wanted to contribute to open-source projects but did not know where to start?
Every week we highlight some tasks from the Rust community for you to pick and get started! 
 Some of these tasks may also have mentors available, visit the task page for more information. 
 If you are a Rust project owner and are looking for contributors, please submit tasks here or through a PR to TWiR or by reaching out on Bluesky or Mastodon ! 
 CFP - Events 
 Are you a new or experienced speaker looking for a place to share something cool? This section highlights events that are being planned and are accepting submissions to join their event as a speaker. 
 EuroRust 2026 | 2026-05-04 (extended) | Barcelona, Spain | 2026-10-14 – 2026-10-17 
 NDC Techtown | 2026-05-03 | Kongsberg, Norway | 2026-09-21 to 23. 
 Scientific Computing in Rust 2026 | 2026-06-05 | Virtual | 2026-07-08 - 2026-07-10 
 If you are an event organizer hoping to expand the reach of your event, please submit a link to the website through a PR to TWiR or by reaching out on Bluesky or Mastodon ! 
 Updates from the Rust Project 
 480 pull requests were merged in the last week 
 Compiler 
 AliasTerm refactor 
 add on_unmatch_args diagnostic attribute 
 eliminate CrateMetadataRef 
 fix performance regression introduced in #142531 by excluding Storage{Live,Dead} from CGU size estimation 
 prefer -1 for None 
 prevent deref coercions in pin! 
 streamline CrateMetadataRef construction in provide_one! 
 Library 
 constify Vec comparisons 
 exposing Float Masks 
 fix heap overflow in slice::join caused by misbehaving Borrow 
 generalize IO Traits for Arc<T> where &T: IoTrait 
 maintain CStringArray null-termination even if Vec::push panics 
 move std::io::RawOsError to core::io 
 implement more traits for field-representing types 
 Cargo 
 clean: do not error if explicitly specified target-dir does not exist 
 compile : stabilize build.warnings 
 compile : ignore unused deps if also transitive 
 compile : Log all ignored unused externs 
 Clippy 
 manual_assert_eq : new lint 
 new module style lint: inline_modules 
 needless_ifs : handle vertical tab as whitespace to avoid false negative 
 inline_modules : fix the rust version the lint was introduced in 
 make unused_format_specs catch width issues 
 fix from_over_into false positive with conflicting blanket From impl 
 fix wrong question_mark suggestion when match arm body is a destructuring assignment 
 Rust-Analyzer 
 add .new postfix completion based on expected type (rust-lang/r… 
 add unwrap_block , offer unwrap_block and unwrap_branch 
 handle if matches!() for replace_if_let_with_match 
 offer on compound assign for replace_arith_op 
 offer on non-block matcharm for unwrap_branch 
 when renaming a field, rename variables in constructors as well 
 fix trait auto import appearing again when trait already been imported as _ 
 avoid prelude paths when imports.preferPrelude is false 
 define the ABI of functions inside extern blocks as the ABI of the extern block 
 fix closure capture hints being misplaced for async closures 
 generate-method skips trait impl blocks when picking insertion site 
 keep the same nonce when cloning a RootDatabase 
 make InferenceResult::binding_mode() fallible 
 mark enum variants as deprecated when their parent enum is deprecated 
 no complete where kw after qualified path 
 offer on ! for apply_demorgan_iterator 
 offer on is_some_and etc. for apply_demorgan_iterator 
 parse return #[attr] expr 
 parse impl restrictions after the visibility 
 pass proc_macro_cwd to Analysis::from_single_file() 
 suppress infer vars in monomorphization 
 migrate replace qualified name with use to SyntaxEditor 
 perf: optimize allocation strategies of output/parser/event 
 remove generate impl non syntax factory variant 
 Rust Compiler Performance Triage 
 Relatively few perf-affecting changes this week. Perf report is more positive
than users should see due to the -Zincremental-verify-ich related
improvements in #155473 . 
 Triage done by @simulacrum .
Revision range: 9ab01ae5..ca9a134e 
 1 Regression, 5 Improvements, 3 Mixed; 3 of them in rollups
32 artifact comparisons made in total 
 Full report here 
 Approved RFCs 
 Changes to Rust follow the Rust RFC (request for comments) process . These
are the RFCs that were approved for implementation this week: 
 No RFCs were approved this week. 
 Final Comment Period 
 Every week, the team announces the 'final comment period' for RFCs and key PRs
which are reaching a decision. Express your opinions now. 
 Tracking Issues & PRs 
 Rust 
 Consider Result<T, Uninhabited> and ControlFlow<Uninhabited, T> to be equivalent to T for must use lint 
 Switch the destructors implementation for thread locals on Windows to use FLS 
 Stabilize VecDeque::truncate_front 
 Derives Copy for ffi::FromBytesUntilNulError 
 Tracking Issue for ExitCodeExt on Windows 
 remove forever-deprecated and hidden f64 methods 
 Cargo 
 Remove curl dependency from crates-io crate 
 Compiler Team (MCPs only) 
 Make stable hashing names consistent 
 replace box_patterns in the compiler with deref_patterns 
 Create a new Tier 3 target: powerpc64le-unknown-none 
 Rust RFCs 
 RFC: Inheriting of default-features in Cargo 
 Rust Foundation Maintainer Fund 
 build-std: explicit dependencies 
 Unsafe Code Guidelines 
 Should validity of a reference depend on the contents of memory in any way? 
 No Items entered Final Comment Period this week for Language Reference , Language Team or Leadership Council . Let us know if you would like your PRs, Tracking Issues or RFCs to be tracked as a part of this list. 
 New and Updated RFCs 
 Bounded Trait Casting 
 Named Fn trait parameters 
 Upcoming Events 
 Rusty Events between 2026-04-29 - 2026-05-27 🦀 
 Virtual 
 2026-04-29 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-05-01 | Virtual (Nürnberg, DE) | Rust Nuremberg Hacker's Hike 0x1 
 2026-05-02 | Virtual (Kampala, UG) | Rust Circle Meetup Rust Circle Meetup 
 2026-05-03 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Rust Deep Learning: First Sunday 
 2026-05-05 | Virtual (Tel Aviv-yafo, IL) | Code Mavens 🦀 - 🐍 - 🐪 Rust code reading and open source contribution 
 2026-05-06 | Virtual (Cardiff, UK) | Rust and C++ Cardiff Practical introduction to SIMD 
 2026-05-06 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-05-06 | Virtual (Indianapolis, IN, US) | Indy Rust Indy.rs - with Social Distancing 
 2026-05-07 | Virtual (Berlin, DE) | Rust Berlin Rust Hack and Learn 
 2026-05-07 | Virtual (Nürnberg, DE) | Rust Nuremberg Rust Nürnberg online 
 2026-05-12 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Second Tuesday 
 2026-05-12 | Virtual (London, UK) | Women in Rust 👋 Community Catch Up 
 2026-05-17 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Rust Deep Learning: Third Sunday 
 2026-05-19 | Virtual (Washington, DC, US) | Rust DC Mid-month Rustful 
 2026-05-20 | Hybrid (Vancouver, BC, CA) | Vancouver Rust Mouse Control with Rust 
 2026-05-20 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-05-21 | Hybrid (Seattle, WA, US) | Seattle Rust User Group May, 2026 SRUG (Seattle Rust User Group) Meetup 
 2026-05-21 | Virtual (Berlin, DE) | Rust Berlin Rust Hack and Learn 
 2026-05-21 | Virtual (Charlottesville, VA, US) | Charlottesville Rust Meetup Tock OS Part #4 - Capsule coding in QEMU! 
 2026-05-26 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Fourth Tuesday 
 2026-05-26 | Virtual (London, UK) | Women in Rust Lunch & Learn: Seeing Into Your Code - A Practical Guide to Tracing in Rust 
 2026-05-27 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 Asia 
 2026-05-13 | Malaysia, MY | Rust Meetup Malaysia Rust Meetup May 2026 
 2026-05-16 | Bangalore, IN | Rust Bangalore May 2026 Rustacean meetup 
 Europe 
 2026-04-29 | Copenhagen, DK | Copenhagen Rust Community Rust meetup #67 
 2026-04-29 | Paris, FR | Paris Rustaceans Rust Meetup in Paris 
 2026-04-30 | Berlin, DE | Rust Berlin Rust Berlin Talks: The next generation 
 2026-04-30 | Manchester, GB | Rust Manchester Rust Manchester April Talk 
 2026-05-02 | Augsburg, DE | Rust Munich and Rust Augsburg Augsburger Linux-Infotag 2026: Gemeinschaftsstand Rust Augsburg und Rust München 
 2026-05-04 | Amsterdam, NH, NL | Rust Developers Amsterdam Group Rust Meetup @ JetBrains 
 2026-05-04 | Frankfurt, DE | Rust Rhein-Main Writing a stock portfolio simulation in Rust with Leptos 
 2026-05-05 | Olomouc, CZ | Rust Moravia 5. Rust Moravia Meetup (Ukaž testy!) 
 2026-05-06 | Milano, MI, IT | Rust Language Milan Rust Milan @ Python Milano: Python or Rust? Yes! 
 2026-05-06 | Oxford, UK | Oxford ACCU/Rust Meetup. Building LLMs from scratch 
 2026-05-07 | Edinburgh, UK | Rust and Friends Rust May Talks: Aetherus + Bevy 
 2026-05-13 | Girona, ES | Rust Girona Rust Girona Hack & Learn 05 2026 
 2026-05-14 | Switzerland, CH | PostTenebrasLab Rust Meetup Geneva 
 2026-05-18 - 2026-05-23 | Amsterdam, NL | RustWeek 2026 RustWeek 2026 
 2026-05-19 | Aarhus, DK | Rust Aarhus Hack Night 
 2026-05-19 | Leipzig, DE | Rust - Modern Systems Programming in Leipzig Cross-Building & Cross-Testing 
 2026-05-19 | London, UK | Women in Rust RustWeek lunch meetup 
 2026-05-21 | Amsterdam, NL | RustNL RustWeek Hackathon 
 2026-05-22 | Amsterdam, NL | RustNL Bike tour around Utrecht 
 2026-05-26 | Dortmund, DE | Rust Dortmund Rust Dortmund Meetup - Agentic Programming - May 
 2026-05-26 | Manchester, UK | Rust Manchester Rust Manchester May Code Night 
 North America 
 2026-04-30 | Atlanta, GA, US | Rust Atlanta Rust-Atl 
 2026-04-30 | Mountain View, CA, US | Hacker Dojo RUST MEETUP at HACKER DOJO 
 2026-05-02 | Boston, MA, US | Boston Rust Meetup Alewife Rust Lunch, May 2 
 2026-05-07 | Saint Louis, MO, US | STL Rust Open Project Night 
 2026-05-09 | Boston, MA, US | Boston Rust Meetup Back Bay Rust Lunch, May 9 
 2026-05-14 | Portland, OR, US | PDXRust From Radio Waves to Pixels - Real-Time Visualizations with Rust and WebAssembly 
 2026-05-14 | San Diego, CA, US | San Diego Rust San Diego Rust May Meetup - Back in person! 
 2026-05-16 | Boston, MA, US | Boston Rust Meetup Lechmere Rust Lunch, May 16 
 2026-05-19 | San Francisco, CA, US | San Francisco Rust Study Group Rust Hacking in Person 
 2026-05-20 | Hybrid (Vancouver, BC, CA) | Vancouver Rust Mouse Control with Rust 
 2026-05-20 | San Francisco, CA, US | Bay Area Rust Meetup Bay Area Rust Meetup 
 2026-05-21 | Hybrid (Seattle, WA, US) | Seattle Rust User Group May, 2026 SRUG (Seattle Rust User Group) Meetup 
 2026-05-21 | Nashville, TN, US | Music City Rust Developers Community Meetup 
 2026-05-23 | Boston, MA, US | Boston Rust Meetup Allston Rust Lunch, May 23 
 2026-05-27 | Austin, TX, US | Rust ATX Rust Lunch - Fareground 
 Oceania 
 2026-05-14 | Melbourne, AU | Rust Melbourne Rust Melbourne - May 2026 
 2026-05-26 | Barton, ACT, AU | Canberra Rust User Group May Meetup 
 South America 
 2026-05-13 | Montevideo, UY | Rust Meetup Uruguay Rust Uruguay meetup de Mayo 
 If you are running a Rust event please add it to the calendar to get
it mentioned here. Please remember to add a link to the event too.
Email the Rust Community Team for access. 
 Jobs 
 Please see the latest Who's Hiring thread on r/rust 
 Quote of the Week 
 Sometimes, the best projects are the ones you never thought you could build. 
 – Chris Dell on his blog 
 Another week bereft of any quote suggestions. llogiq is glad to have found this anyway. 
 Please submit quotes and vote for next week! 
 This Week in Rust is edited by: 
 nellshamrell 
 llogiq 
 ericseppanen 
 extrawurst 
 U007D 
 mariannegoldin 
 bdillo 
 opeolluwa 
 bnchi 
 KannanPalani57 
 tzilist 
 Email list hosting is sponsored by The Rust Foundation 
 Discuss on r/rust
```

---

## 3. This Week in Rust 648

- 日期: 2026-04-22 00:00
- 链接: https://this-week-in-rust.org/blog/2026/04/22/this-week-in-rust-648/

```
Hello and welcome to another issue of This Week in Rust ! Rust is a programming language empowering everyone to build reliable and efficient software.
This is a weekly summary of its progress and community.
Want something mentioned? Tag us at @thisweekinrust.bsky.social on Bluesky or @ThisWeekinRust on mastodon.social, or send us a pull request .
Want to get involved? We love contributions . 
 This Week in Rust is openly developed on GitHub and archives can be viewed at this-week-in-rust.org .
If you find any errors in this week's issue, please submit a PR . 
 Want TWIR in your inbox? Subscribe here . 
 Updates from Rust Community 
 Official 
 crates.io: Help test our new web frontend 
 Announcing Rust 1.95.0 | Rust Blog 
 Foundation 
 RustConf 2026 schedule and registration are live! Early bird ticket prices are available through April 29. 
 Project/Tooling Updates 
 axum-harness: agent-native backend architecture template for Axum — semantic-first, topology-late, multi-agent harness 
 lean-decimal: 2~6X faster than rust_decimal 
 Building Semantic Version Control in Rust 
 Oxanus v1.0 - Job processing library 
 flodl 0.5.2: HuggingFace, in Rust 
 One Sized trait does not fit all 
 tinyboot v0.4.0 Released — The API is Stable 
 Slint 1.16 Released 
 Danube Messaging adds Key-Shared subscriptions 
 Announcing mtp-mount: pure-Rust FUSE mount for MTP devices 
 wrkflw v0.8.0 - Validate and Run GitHub Actions locally. 
 Observations/Thoughts 
 Cryptographic Right Answers: Post Quantum and Rust Edition 
 Learning rust through an LLM to develop a TUI RSS reader (and what I tell my students) 
 What Happens When You Build an Inode-Style Vector in Rust 
 Ownership & Borrowing
versus Reference Counting 
 The Edge of Safe Rust 
 [video] Third Online Func Prog Sweden 2026 
 Rust Walkthroughs 
 [video] Build a Full Stack Twitter Clone web application in Rust (Axum & Leptos) 
 The Impatient Programmer's Guide to Bevy and Rust: Chapter 12 - Let There Be Networking 
 [video] RustCurious lesson 6: Enums and Polymorphism 
 A minimal VMM in Rust with Apple Hypervisor 
 Caching Expensive Functions in Rust with cached 
 Crate of the Week 
 This week's crate is farben , a German-named macro crate for terminal colors. 
 Thanks to Nik Revenco for the suggestion! 
 Please submit your suggestions and votes for next week ! 
 Calls for Testing 
 An important step for RFC implementation is for people to experiment with the
implementation and give feedback, especially before stabilization. 
 If you are a feature implementer and would like your RFC to appear in this list, add a call-for-testing label to your RFC along with a comment providing testing instructions and/or
guidance on which aspect(s) of the feature need testing. 
 No calls for testing were issued this week by Rust , Cargo , Rustup or Rust language RFCs . 
 Let us know if you would like your feature to be tracked as a part of this list. 
 Call for Participation; projects and speakers 
 CFP - Projects 
 Always wanted to contribute to open-source projects but did not know where to start?
Every week we highlight some tasks from the Rust community for you to pick and get started! 
 Some of these tasks may also have mentors available, visit the task page for more information. 
 rust-cookbook - Add Asynchronous section with tokio runtime recipes ( other high impact examples ) 
 wacp-platform - Fix test-only clippy drifts in wacp-runtime/tests.rs + console-db/queries/tests.rs ( other good first issues ) 
 If you are a Rust project owner and are looking for contributors, please submit tasks here or through a PR to TWiR or by reaching out on Bluesky or Mastodon ! 
 CFP - Events 
 Are you a new or experienced speaker looking for a place to share something cool? This section highlights events that are being planned and are accepting submissions to join their event as a speaker. 
 EuroRust | 2026-04-27 | Barcelona, Spain | 2026-10-14 - 2026-10-17 
 NDC Techtown | 2026-05-03 | Kongsberg, Norway | 2026-09-21 to 23. 
 If you are an event organizer hoping to expand the reach of your event, please submit a link to the website through a PR to TWiR or by reaching out on Bluesky or Mastodon ! 
 Updates from the Rust Project 
 542 pull requests were merged in the last week 
 Compiler 
 don't hash DelayedLints 
 refactor FnDecl and FnSig non-type fields into a new wrapper type 
 suggest removing & when awaiting a reference to a future 
 suggest returning a reference for unsized place from a closure 
 Library 
 abort in core 
 constify Index ( Mut ), Deref ( Mut ) for Vec 
 core/num: implement feature integer_cast_extras 
 core::unicode : Replace Cased table with Lt 
 libtest: use binary search for --exact test filtering 
 move std::io::ErrorKind to core::io 
 Rustdoc 
 fix redundant_explicit_links incorrectly firing (or not firing) under certain scenarios 
 preserve doc(cfg) on locally re-exported type aliases 
 Clippy 
 add MSRV check for manual_noop_waker 
 add useless_borrows_in_formatting lint 
 do not propose to refactor when no variant constructor is used 
 do not trigger let_and_return on let else 
 extend byte_char_slices to cover arrays 
 extend zst_offset lint to detect NonNull<T> offset calculations 
 fix a case where collapsible_match suggested a transformation that changes runtime behavior 
 fix cloned_ref_to_slice_refs false negative on to_owned() 
 fix expect_fun_call suggests wrongly for string slicing 
 fix for_kv_map false negative when using iter and iter_mut 
 parenthesize AssocOp::Cast in suggestion when replacement operator is < to avoid parse error 
 useless_conversion : do not lint (a..b).into_iter() (for edition migration) 
 Rust-Analyzer 
 completion : reduce relevance for deprecated items 
 remove duplicate lints 
 allow crate authors to declare that their trait prefers to be imported as _ 
 do not complete unstable items that use an internal feature 
 exclude refs(find all refs) from deps and stdlib 
 support extract variable in macro call 
 add parentheses on record expr for replace_let_with_if_let 
 adjust name of extract_type_alias 
 allow ambiguity in assoc type shorthand if they resolve to the same assoc type, between supertraits this time 
 port call expr type checking and closure upvar inference from rustc 
 respect #[deprecated] attr when deciding if a ModuleDef completion is deprecated 
 some fixes for upvars_mentioned() 
 use ProofTreeVisitor for unsized coercion 
 parse type const items 
 perf: do not check solver's cache validity on every access 
 sync function call args check fudging with rustc 
 Rust Compiler Performance Triage 
 This week was a bit all over the place, but the largest regressions were either
already fixed or they are being investigated. There were also a couple of nice perf. wins. 
 Triage done by @Kobzol .
Revision range: dab8d9d1..9ab01ae5 
 Summary : 
 (instructions:u) mean range count 
 Regressions ❌ 
 (primary) 0.7% [0.2%, 4.6%] 39 
 Regressions ❌ 
 (secondary) 0.6% [0.2%, 1.4%] 31 
 Improvements ✅ 
 (primary) -0.6% [-4.8%, -0.1%] 70 
 Improvements ✅ 
 (secondary) -0.7% [-4.1%, -0.0%] 93 
 All ❌✅ (primary) -0.1% [-4.8%, 4.6%] 109 
 3 Regressions, 4 Improvements, 6 Mixed; 4 of them in rollups
41 artifact comparisons made in total 
 Full report here . 
 Approved RFCs 
 Changes to Rust follow the Rust RFC (request for comments) process . These
are the RFCs that were approved for implementation this week: 
 No RFCs were approved this week. 
 Final Comment Period 
 Every week, the team announces the 'final comment period' for RFCs and key PRs
which are reaching a decision. Express your opinions now. 
 Tracking Issues & PRs 
 Rust 
 Error on invalid macho section specifier 
 Allow trailing self in more contexts 
 Add FCW to disallow $crate in macro matcher 
 Lint unused pub items in binary crates 
 const-stabilize char::is_control() 
 Cargo 
 Stabilize build-dir layout v2 
 feat(compile): Stabilize build.warnings 
 Compiler Team (MCPs only) 
 Promote riscv64gc-unknown-linux-musl to Tier 2 (with Tools) 
 Make stable hashing names consistent 
 No Items entered Final Comment Period this week for Language Reference , Language Team , Leadership Council , Rust RFCs or Unsafe Code Guidelines . 
 Let us know if you would like your PRs, Tracking Issues or RFCs to be tracked as a part of this list. 
 New and Updated RFCs 
 Add contribution policy for AI-generated work 
 Bounded Trait Casting 
 Support heterogeneous try blocks ( try_blocks_heterogeneous ) RFC 
 Upcoming Events 
 Rusty Events between 2026-04-22 - 2026-05-20 🦀 
 Virtual 
 2026-04-22 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-04-23 | Virtual (Amsterdam, NL) | Bevy Game Development Bevy Meetup #13 
 2026-04-23 | Virtual (Berlin, DE) | Rust Berlin Rust Hack and Learn 
 2026-04-24 | Virtual (Nairobi, KE) | RustaceansKenya Transitioning To Rust: The Learning Curve 
 2026-04-28 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Fourth Tuesday 
 2026-04-28 | Virtual (London, UK) | Women in Rust Lunch & Learn: From Protobuf to Production - A Guide to gRPC in Rust 
 2026-04-28 | Virtual (Tel Aviv-yafo, IL) | Code Mavens 🦀 - 🐍 - 🐪 Web development using axum in Rust - part 4 
 2026-04-29 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-05-01 | Virtual (Nürnberg, DE) | Rust Nuremberg Hacker's Hike 0x1 
 2026-05-02 | Virtual (Kampala, UG) | Rust Circle Meetup Rust Circle Meetup 
 2026-05-03 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Rust Deep Learning: First Sunday 
 2026-05-06 | Virtual (Cardiff, GB) | Rust and C++ Cardiff Practical introduction to SIMD 
 2026-05-06 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-05-06 | Virtual (Indianapolis, IN, US) | Indy Rust Indy.rs - with Social Distancing 
 2026-05-07 | Virtual (Berlin, DE) | Rust Berlin Rust Hack and Learn 
 2026-05-07 | Virtual (Nürnberg, DE) | Rust Nuremberg Rust Nürnberg online 
 2026-05-12 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Second Tuesday 
 2026-05-12 | Virtual (London, UK) | Women in Rust 👋 Community Catch Up 
 2026-05-13 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-05-17 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Rust Deep Learning: Third Sunday 
 2026-05-19 | Virtual (Washington, DC, US) | Rust DC Mid-month Rustful 
 2026-05-20 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-05-20 | Virtual (Vancouver, BC, CA) | Vancouver Rust Mouse Control with Rust 
 Asia 
 2026-05-13 | Malaysia, MY | Rust Meetup Malaysia Rust Meetup May 2026 
 Europe 
 2026-04-23 | Aarhus, DK | Rust Aarhus Talk Night and Birthday Party at MFT Energy 
 2026-04-23 | Paris, FR | Rust Paris Rust meetup #85 
 2026-04-24 - 2026-04-26 | Augsburg, DE | Rust Meetup Augsburg Future Week Augsburg: Road to Game Jam – Spielend Bevy und Rust lernen bei Tuxedo Computers 
 2026-04-25 | Stockholm, SE | Stockholm Rust Ferris' Fika Forum #26 
 2026-04-29 | Copenhagen, DK | Copenhagen Rust Community Rust meetup #67 
 2026-04-29 | Paris, FR | Paris Rustaceans Rust Meetup in Paris 
 2026-04-30 | Berlin, DE | Rust Berlin Rust Berlin Talks: The next generation 
 2026-04-30 | Manchester, GB | Rust Manchester Rust Manchester April Talk 
 2026-05-02 | Augsburg, DE | Rust Munich and Rust Augsburg Augsburger Linux-Infotag 2026: Gemeinschaftsstand Rust Augsburg und Rust München 
 2026-05-04 | Amsterdam, NH, NL | Rust Developers Amsterdam Group Rust Meetup @ JetBrains 
 2026-05-04 | Frankfurt, DE | Rust Rhein-Main Writing a stock portfolio simulation in Rust with Leptos 
 2026-05-05 | Olomouc, CZ | Rust Moravia 5. Rust Moravia Meetup (Ukaž testy!) 
 2026-05-07 | Edinburgh, GB | Rust and Friends Rust May Talks: Aetherus + TBA 
 2026-05-13 | Girona, ES | Rust Girona Rust Girona Hack & Learn 05 2026 
 2026-05-14 | Switzerland, CH | PostTenebrasLab Rust Meetup Geneva 
 2026-05-18 | Milano, MI, IT | Rust Language Milan RustWeek 2026 
 2026-05-19 | Aarhus, DK | Rust Aarhus Hack Night 
 2026-05-19 | Amsterdam, NL | RustNL RustWeek 2026 announcement 
 2026-05-19 | Leipzig, SN, DE | Rust - Modern Systems Programming in Leipzig Cross-Building & Cross-Testing 
 2026-05-19 | London, UK | Women in Rust RustWeek lunch meetup 
 North America 
 2026-04-20 - 2026-04-22 | Portland, OR | Tokio TokioConf 2026 
 2026-04-22 | Austin, TX, US | Rust ATX Rust Lunch - Fareground 
 2026-04-22 | New York, NY, US | Rust NYC Rust NYC: Formally Verified Rust & SAT Solvers 
 2026-04-22 | Portland, OR | Apache DataFusion Meetup Portland Apache DataFusion Meetup 
 2026-04-23 | Los Angeles, CA, US | Rust Los Angeles Rust LA April! 
 2026-04-25 | Boston, MA, US | Boston Rust Meetup South Station Rust Lunch, Apr 25 
 2026-04-28 | New York, NY, US | Rust NYC Rust NYC x OpenAI: Safer 'unsafe' & Barnum: The agentic workflow engine. 
 2026-04-30 | Atlanta, GA, US | Rust Atlanta Rust-Atl 
 2026-05-07 | Saint Louis, MO, US | STL Rust Open Project Night 
 2026-05-14 | Portland, OR, US | PDXRust From Radio Waves to Pixels - Real-Time Visualizations with Rust and WebAssembly 
 2026-05-14 | San Diego, CA, US | San Diego Rust San Diego Rust May Meetup - Back in person! 
 2026-05-19 | San Francisco, CA, US | San Francisco Rust Study Group Rust Hacking in Person 
 2026-05-20 | San Francisco, CA, US | Bay Area Rust Meetup Bay Area Rust Meetup 
 Oceania 
 2026-05-14 | Melbourne, AU | Rust Melbourne Rust Melbourne - May 2026 
 If you are running a Rust event please add it to the calendar to get
it mentioned here. Please remember to add a link to the event too.
Email the Rust Community Team for access. 
 Jobs 
 Please see the latest Who's Hiring thread on r/rust 
 Quote of the Week 
 in Rust we pay the price of composition up-front 
 – Nadieril on rust zulip 
 Thanks to Nadieril for the self-suggestion! 
 Please submit quotes and vote for next week! 
 This Week in Rust is edited by: 
 nellshamrell 
 llogiq 
 ericseppanen 
 extrawurst 
 U007D 
 mariannegoldin 
 bdillo 
 opeolluwa 
 bnchi 
 KannanPalani57 
 tzilist 
 Email list hosting is sponsored by The Rust Foundation 
 Discuss on r/rust
```

---

## 4. This Week in Rust 647

- 日期: 2026-04-15 00:00
- 链接: https://this-week-in-rust.org/blog/2026/04/15/this-week-in-rust-647/

```
Hello and welcome to another issue of This Week in Rust ! Rust is a programming language empowering everyone to build reliable and efficient software.
This is a weekly summary of its progress and community.
Want something mentioned? Tag us at @thisweekinrust.bsky.social on Bluesky or @ThisWeekinRust on mastodon.social, or send us a pull request .
Want to get involved? We love contributions . 
 This Week in Rust is openly developed on GitHub and archives can be viewed at this-week-in-rust.org .
If you find any errors in this week's issue, please submit a PR . 
 Want TWIR in your inbox? Subscribe here . 
 Updates from Rust Community 
 Official 
 Infrastructure Team 2026 Q1 Recap and Q2 Plan 
 Project/Tooling Updates 
 pquantum.dev: Post-Quantum Cryptography in Rust 
 haproxy-spoe-rs: A Rust SPOA Agent Library for HAProxy 
 Fresh 0.2.23: Terminal IDE adds Windows-1251 encoding, customizable status bar, and faster file finder 
 KAIO v0.2.0: Writing GPU Kernels in Rust at 92.5% of cuBLAS 
 RustNet: A Real-Time Network Traffic Analysis TUI 
 AimDB: The Next Era of Software Architecture Is Data-First 
 tailscale-rs v0.2.0: our new Rust library preview 
 Sinbo: a CLI snippet manager, store code snippets locally with fuzzy search, encryption, and shell completions 
 flodl v0.4.0: heterogeneous multi-GPU DDP with faster training and better convergence than solo GPU 
 Observations/Thoughts 
 The acyclic e-graph: Cranelift's mid-end optimizer 
 Rust should have stable tail calls 
 Flat Error Codes Are Not Enough 
 No one owes you supply-chain security 
 Everything Should Be Typed: Scalar Types Are Not Enough 
 Borrow-checking surprises 
 A Roadmap for Building an Extended Standard Library for Rust 
 Okay, what ACTUALLY uses Rust? 
 [audio] Netstack.FM episode 34 — Tokio with Carl Lerche (Ep 5 Remastered) 
 Rust Walkthroughs 
 Untangling Tokio and Rayon in production: From 2s latency spikes to 94ms flat 
 Understanding Traceroute 
 Bringing Rust to the Pixel Baseband 
 Fixing DNS tail latency with a 5-line config and a 50-line function 
 Debloat your async Rust 
 Learn Rust Ownership and Borrowing By Building Mini Grep 
 Profiling Rust: A Flamegraph vs PGO, BOLT, and Native CPU Targeting 
 Bulletproof Rust Web: An opinionated guide to production-grade Axum applications 
 A minimal VMM in Rust with KVM 
 claudectl: Building a TUI Dashboard for AI Coding Agents in Rust 
 [video] Build with Naz : Eliminate busy waiting with Rust Condvar 
 Crate of the Week 
 This week's crate is Myth Engine , a high-performance, cross-platform rendering engine. 
 Thanks to Pan Xinmiao for the self-suggestion! 
 Please submit your suggestions and votes for next week ! 
 Calls for Testing 
 An important step for RFC implementation is for people to experiment with the
implementation and give feedback, especially before stabilization. 
 If you are a feature implementer and would like your RFC to appear in this list, add a call-for-testing label to your RFC along with a comment providing testing instructions and/or
guidance on which aspect(s) of the feature need testing. 
 No calls for testing were issued this week by Rust , Cargo , Rustup or Rust language RFCs . 
 Let us know if you would like your feature to be tracked as a part of this list. 
 Call for Participation; projects and speakers 
 CFP - Projects 
 Always wanted to contribute to open-source projects but did not know where to start?
Every week we highlight some tasks from the Rust community for you to pick and get started! 
 Some of these tasks may also have mentors available, visit the task page for more information. 
 No Calls for participation were submitted this week. 
 If you are a Rust project owner and are looking for contributors, please submit tasks here or through a PR to TWiR or by reaching out on Bluesky or Mastodon ! 
 CFP - Events 
 Are you a new or experienced speaker looking for a place to share something cool? This section highlights events that are being planned and are accepting submissions to join their event as a speaker. 
 EuroRust | CFP open until 2026-04-27 | Barcelona, Spain | 2026-10-14 - 2026-10-17 
 If you are an event organizer hoping to expand the reach of your event, please submit a link to the website through a PR to TWiR or by reaching out on Bluesky or Mastodon ! 
 Updates from the Rust Project 
 519 pull requests were merged in the last week 
 Compiler 
 add #![unstable_removed(..)] attribute to track removed features 
 add suggestion to .to_owned() used on Cow when borrowing 
 avoid stack overflow in FindExprBySpan 
 enable #[diagnostic::on_const] for local impls 
 introduce a #[diagnostic::on_unknown] attribute 
 reduce size of ImportData 
 ty::Alias refactor 
 semantic checks of impl restrictions 
 stabilize s390x vector registers 
 store chunk_domain_size explicitly in Chunk 
 Library 
 add const Default impls for LazyCell and LazyLock 
 constify some Iterator methods 
 constify DoubleEndedIterator 
 constify Step for NonZero<u*> 
 don't leak internal temporaries from dbg! 
 explicitly forget the zero remaining elements in vec::IntoIter::fold() 
 impl const Residual for ControlFlow 
 initial functions to start on transmute v2 
 introduce #[diagnostic::on_move] on Rc 
 make Box/Rc/Arc::into_array allocator-aware (and add doctest) 
 stabilize feature int_lowest_highest_one 
 stabilize feature isolate_most_least_significant_one 
 stabilize feature uint_bit_width 
 Cargo 
 clean: add target directory validation 
 manifest : allow git dependency alongside alternate registry 
 auth : add auth scheme hint to token rejected error for alt registries 
 core : use closest_msg to suggest similar member name for mistyped -p 
 lints : ignore unused_crate_dependencies status 
 toml : force script edition warnings on quiet 
 copy cargo clean target-dir validation tests to clean_new_layout.rs 
 never include use extra-filename in build scripts 
 support target.'cfg(..)'.rustdocflags analogously to rustflags 
 Rustdoc 
 fix pattern types rendering 
 dep-info for standalone markdown inputs 
 inherit inline attributes for declarative macros 
 Clippy 
 fn_to_numeric_cast_any : do not warn cast to raw pointer 
 even more fixes for handling of macros 
 extend manual_filter to cover and_then 
 fix unused_async false positive for stubs with args 
 fix wrong suggestion for println_empty_string with non-parenthesis delimiters 
 truncate constants to target type in comparison 
 Rust-Analyzer 
 changes to build scripts and config.toml should always refresh 
 demoting completion relevance when an inherent impl already exists 
 enhance runnable command placeholders 
 support impl and mut restrictions 
 fix [env] in .cargo/config.toml overriding process environment variables 
 fix rustfmt relative custom command 
 MIR evaluation of sized &T with recursive const fn 
 check coercion, not unification, in "Fill struct fields", as the criteria to use an existing local as the field's value 
 complete variants of hidden enums through public aliases 
 consider the context of the path for ImportAssets 
 diagnose cfged-out crate 
 disable the fix for missing-fields when the fields are private 
 enable vscode suggest in strings 
 fix ref_match position when keyword prefix 
 improve add some on block like expression 
 improve label on add_missing_match_arms assist 
 no complete term expressions on qualified path 
 no deref index-expr for extract_function 
 no imports on type anchor qualified path 
 parse cfg_attr and cfg specially 
 handle token mutability in edit flow as well 
 migrate extract struct from enum variant to new SyntaxEditor and Port whitespace heuristics to SyntaxEditor 
 replace make from generate single field struct from with SyntaxFactory 
 unwrap unnecessary result return type in view_crate_graph 
 Rust Compiler Performance Triage 
 This week was negative, mainly caused by a type system fix and because we had to temporarily revert some attribute cleanups that previously improved performance. 
 Triage done by @panstromek .
Revision range: e73c56ab..dab8d9d1 
 Summary : 
 (instructions:u) mean range count 
 Regressions ❌ 
 (primary) 0.4% [0.2%, 0.7%] 46 
 Regressions ❌ 
 (secondary) 0.5% [0.1%, 2.3%] 102 
 Improvements ✅ 
 (primary) -0.5% [-0.6%, -0.4%] 4 
 Improvements ✅ 
 (secondary) -0.4% [-0.6%, -0.2%] 5 
 All ❌✅ (primary) 0.4% [-0.6%, 0.7%] 50 
 4 Regressions, 1 Improvement, 5 Mixed; 6 of them in rollups
41 artifact comparisons made in total 
 Full report here 
 Approved RFCs 
 Changes to Rust follow the Rust RFC (request for comments) process . These
are the RFCs that were approved for implementation this week: 
 No RFCs were approved this week. 
 Final Comment Period 
 Every week, the team announces the 'final comment period' for RFCs and key PRs
which are reaching a decision. Express your opinions now. 
 Tracking Issues & PRs 
 Rust 
 Verify that penultimate segment of enum variant path refers to enum if it has args 
 deprecate std::char constants and functions 
 impl Default for RepeatN 
 Make std::fs::File Send on UEFI 
 Cargo 
 feat(config): Stabilize resolver.lockfile-path config 
 Compiler Team (MCPs only) 
 Optimize repr(Rust) enums by omitting tags in more cases involving uninhabited variants. 
 Proposal for a dedicated test suite for the parallel frontend 
 Promote tier 3 riscv32 ESP-IDF targets to tier 2 
 Proposal for Adapt Stack Protector for Rust 
 Rust RFCs 
 Propose the Rust Foundation Maintainer fund 
 Leadership Council 
 Fund the Content team (2026 allocation) 
 No Items entered Final Comment Period this week for Language Reference , Language Team or Unsafe Code Guidelines . 
 Let us know if you would like your PRs, Tracking Issues or RFCs to be tracked as a part of this list. 
 New and Updated RFCs 
 No New or Updated RFCs were created this week. 
 Upcoming Events 
 Rusty Events between 2026-04-15 - 2026-05-13 🦀 
 Virtual 
 2026-04-15 | Hybrid (Vancouver, BC, CA) | Vancouver Rust Nushell 
 2026-04-15 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-04-16 | Hybrid (Seattle, WA, US) | Seattle Rust User Group April, 2026 SRUG (Seattle Rust User Group) Meetup 
 2026-04-19 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Rust Deep Learning: Third Sunday 
 2026-04-21 | Virtual (Washington, DC, US) | Rust DC Mid-month Rustful 
 2026-04-22 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-04-23 | Virtual (Amsterdam, NL) | Bevy Game Development Bevy Meetup #13 
 2026-04-23 | Virtual (Berlin, DE) | Rust Berlin Rust Hack and Learn 
 2026-04-24 | Virtual (Nairobi, KE) | RustaceansKenya Transitioning To Rust: The Learning Curve 
 2026-04-28 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Fourth Tuesday 
 2026-04-28 | Virtual (London, UK) | Women in Rust Lunch & Learn: From Protobuf to Production - A Guide to gRPC in Rust 
 2026-04-29 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-05-01 | Virtual (Nürnberg, DE) | Rust Nuremberg Hacker's Hike 0x1 
 2026-05-02 | Virtual (Kampala, UG) | Rust Circle Meetup Rust Circle Meetup 
 2026-05-03 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Rust Deep Learning: First Sunday 
 2026-05-06 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 2026-05-06 | Virtual (Indianapolis, IN, US) | Indy Rust Indy.rs - with Social Distancing 
 2026-05-07 | Virtual (Berlin, DE) | Rust Berlin Rust Hack and Learn 
 2026-05-07 | Virtual (Nürnberg, DE) | Rust Nuremberg Rust Nürnberg online 
 2026-05-12 | Virtual (Dallas, TX, US) | Dallas Rust User Meetup Second Tuesday 
 2026-05-12 | Virtual (London, GB) | Women in Rust 👋 Community Catch Up 
 2026-05-13 | Virtual (Girona, ES) | Rust Girona Weekly coding session 
 Asia 
 2026-04-17 | Bangalore, IN | Rust India Rust India Workshop 
 2026-04-18 | Bangalore, IN | Rust India Rust India Conference 
 2026-05-13 | Malaysia, MY | Rust Meetup Malaysia Rust Meetup Malaysia 
 Europe 
 2026-04-16 | Berlin, DE | Rust Berlin Rust Berlin on location 🏳️‍🌈 - Edition 013 
 2026-04-21 | Leipzig, DE | Rust - Modern Systems Programming in Leipzig Native GUIs with Rust 
 2026-04-23 | Aarhus, DK | Rust Aarhus Talk Night and Birthday Party at MFT Energy 
 2026-04-24 - 2026-04-26 | Augsburg, DE | Rust Meetup Augsburg Future Week Augsburg: Road to Game Jam – Spielend Bevy und Rust lernen bei Tuxedo Computers 
 2026-04-25 | Stockholm, SE | Stockholm Rust Ferris' Fika Forum #26 
 2026-04-29 | Paris, FR | Paris Rustaceans Rust Meetup in Paris 
 2026-04-30 | Manchester, GB | Rust Manchester Rust Manchester April Talk 
 2026-05-02 | Augsburg, DE | Rust Munich and Rust Augsburg Augsburger Linux-Infotag 2026: Gemeinschaftsstand Rust Augsburg und Rust München 
 2026-05-04 | Amsterdam, NH, NL | Rust Developers Amsterdam Group Rust Meetup @ JetBrains 
 2026-05-04 | Frankfurt, DE | Rust Rhein-Main Writing a stock portfolio simulation in Rust with Leptos 
 2026-05-05 | Olomouc, CZ | Rust Moravia 5. Rust Moravia Meetup (Ukaž testy!) 
 North America 
 2026-04-15 | Hybrid (Vancouver, BC, CA) | Vancouver Rust Nushell 
 2026-04-16 | Hybrid (Seattle, WA, US) | Seattle Rust User Group April, 2026 SRUG (Seattle Rust User Group) Meetup 
 2026-04-16 | Mountain View, CA, US | Hacker Dojo RUST MEETUP at HACKER DOJO 
 2026-04-16 | Nashville, TN, US | Music City Rust Developers Community Meetup 
 2026-04-18 | Boston, MA, US | Boston Rust Meetup Harvard Square Rust Lunch, Apr 18 
 2026-04-20 - 2026-04-22 | Portland, OR | Tokio TokioConf 2026 
 2026-04-21 | San Francisco, CA, US | San Francisco Rust Study Group Rust Hacking in Person 
 2026-04-22 | Austin, TX, US | Rust ATX Rust Lunch - Fareground 
 2026-04-22 | New York, NY, US | Rust NYC Rust NYC: Formally Verified Rust & SAT Solvers 
 2026-04-22 | Portland, OR | Apache DataFusion Meetup Portland Apache DataFusion Meetup 
 2026-04-23 | Los Angeles, CA, US | Rust Los Angeles Rust LA April! 
 2026-04-25 | Boston, MA, US | Boston Rust Meetup South Station Rust Lunch, Apr 25 
 2026-04-28 | New York, NY, US | Rust NYC Rust NYC x OpenAI: Safer 'unsafe' & Barnum: The agentic workflow engine. 
 2026-04-30 | Atlanta, GA, US | Rust Atlanta Rust-Atl 
 2026-05-07 | Saint Louis, MO, US | STL Rust Open Project Night 
 South America 
 2026-04-17 | Rio de Janeiro, BR | Meetups Rust RJ Meetup Rust RJ 
 If you are running a Rust event please add it to the calendar to get
it mentioned here. Please remember to add a link to the event too.
Email the Rust Community Team for access. 
 Jobs 
 Please see the latest Who's Hiring thread on r/rust 
 Quote of the Week 
 the amount of times that I spend 15 min in the docs + coding which end up in a monstrous or().flatten().map().is_ok_and() only to get slapped by clippy saying replace your monster with this single function please is way too high 😀 
 – Teufelchen on RIOT off-topic matrix chat 
 Thanks to chrysn for the suggestion! 
 Please submit quotes and vote for next week! 
 This Week in Rust is edited by: 
 nellshamrell 
 llogiq 
 ericseppanen 
 extrawurst 
 U007D 
 mariannegoldin 
 bdillo 
 opeolluwa 
 bnchi 
 KannanPalani57 
 tzilist 
 Email list hosting is sponsored by The Rust Foundation 
 Discuss on r/rust
```

---
