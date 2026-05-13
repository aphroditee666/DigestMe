# freeCodeCamp.org

> 分类: 技术社区
> URL: https://www.freecodecamp.org/news/rss/
> 抓取: 10 篇

---

## 1. The Codex Handbook: A Practical Guide to OpenAI's Coding Platform

- 日期: 2026-05-08 23:02
- 链接: https://www.freecodecamp.org/news/the-codex-handbook-a-practical-guide-to-openai-s-coding-platform/

```
This handbook is written for developers, team leads, and admins who want to understand what Codex is, how to set it up, how to use it well, how it differs from general-purpose models, and how pricing works today. 
 It's based on current OpenAI Codex documentation and Help Center articles. Pricing and plan availability change frequently, so treat the pricing section as a snapshot of the current docs and verify against the official links before making procurement decisions. 
 What's new (April 2026): OpenAI released GPT-5.5 and GPT-5.5 Pro on April 23–24, 2026. GPT-5.5 is now the flagship general model and is rolling into Codex surfaces. See the new "GPT-5.5: The Newest Release" subsection in Section 2 , the full benchmark deep dive in Section 11 , and the updated pricing snapshot in Section 7 . 
 Authors: Tatev Aslanyan, Vahe Aslanyan, Jim Amuto | Version: 1.3 — Last updated April 30, 2026 
 Executive Summary 
 Codex is OpenAI's coding agent — not a single model, but a product and workflow layer that wraps OpenAI's frontier models with file access, shell execution, sandboxes, approval flows, and code review. 
 It runs in four surfaces: the CLI, IDE extensions (VS Code, Cursor, Windsurf), the macOS/Windows app, and Codex Cloud for background tasks against GitHub repositories. 
 The product is included with most paid ChatGPT plans (Plus, Pro, Business, Enterprise/Edu) and, for now, Free and Go with stricter rate limits. 
 The model layer beneath Codex shifted in April 2026. GPT-5.5 is the new general flagship, with substantial gains on agentic and long-context benchmarks (MRCR v2 at 1M tokens jumped from 36.6% on GPT-5.4 to 74.0% on GPT-5.5. Terminal-Bench 2.0 reaches 82.7%, and hallucination rate dropped roughly 60% versus prior generations). It's also roughly 2× the per-token cost of GPT-5.4, so picking the right model per task now matters more for budget than it did a quarter ago. 
 For teams adopting Codex, the highest-leverage choices are: 
 Start in the CLI or IDE on small bounded tasks before enabling cloud 
 Use Codex as a pre-merge reviewer in addition to a code generator 
 Keep admin and user access separated through workspace RBAC, and 
 Treat token consumption — not prompt count — as the cost driver. 
 The 30-60-90 day adoption plan in the appendix gives a phased rollout that surfaces friction early. 
 This handbook covers what Codex is, how to set it up, how to use it well, how it compares to Claude Code, GitHub Copilot, and self-hosted alternatives. We'll also discuss what it costs, how to govern it in an enterprise, and where it does and does not fit. You'll find a glossary, security checklist, and worked cost example in the appendix. 
 Table of Contents 
 Here's What We'll Cover: 
 Executive Summary 
 Prerequisites 
 Section 1: What Codex Is 
 Section 2: Where Codex Fits in the OpenAI Ecosystem 
 Section 3: The Core Surfaces 
 Section 4: Getting Started: Install, Set Up, and Your First Task 
 Section 5: How to Use Codex Effectively 
 Section 6: Difference Between Codex and Other Coding Tools 
 Comparison Matrix 
 Section 7: Pricing and Plan Access 
 Worked Cost Example 
 Section 8: Security, Permissions, and Enterprise Setup 
 Section 9: Best Practices for Teams 
 Section 10: Common Workflows and Examples 
 Section 11: Model Specs and Benchmarks (GPT-5.5 Deep Dive) 
 Section 12: Troubleshooting 
 Section 13: FAQ 
 Section 14: When NOT to Use Codex 
 Section 15: Final Recommendations 
 Section 16: Source References 
 Appendix A: 30-60-90 Day Adoption Plan 
 Appendix B: Glossary 
 Appendix C: Admin Security Checklist 
 Appendix D: Changelog 
 Appendix E: Working with Codex in VS Code 
 Prerequisites 
 This handbook is hands-on. To get the most out of it — especially Section 4 , Section 5 , and Section 10 where you'll install Codex and run real tasks — you should have the following in place. 
 Background Knowledge You Should Already Have 
 You don't need to be a senior engineer, but the walkthroughs assume: 
 Comfort using the command line. You can cd into a directory, list files, run git commands, and read shell error messages. If you have never opened a terminal, work through a one-hour shell tutorial first. 
 Basic Git literacy. You understand commits, branches, pull requests, and the difference between staged and unstaged changes. The Codex workflow centers on producing reviewable diffs, so this is non-negotiable. 
 Experience reading code in at least one mainstream language. Codex can work in any language, but the demo repo in Section 4 is a small Python service. If you can read Python, JavaScript, Go, or similar, you'll be fine. 
 A mental model of "what an API call costs." Section 7 's worked cost example assumes you understand that LLM usage is metered by tokens. If "tokens" is a brand-new concept, skim the OpenAI tokenizer page once before reading Section 7 . 
 If you're an engineering manager, procurement lead, or admin and you only need Section 7 , Section 8 , and Section 14 , you can skip the technical prerequisites and jump straight to those sections. 
 Tools and Accounts You Need to Install 
 Before starting Section 4 , have the following ready. Approximate setup time: 15–25 minutes if you're starting from scratch. 
 Tool / Account Why you need it Where to get it 
 A ChatGPT account on Plus, Pro, Business, or Enterprise/Edu Codex is included with these plans. Free and Go work for now but with stricter rate limits chatgpt.com 
 Node.js 18+ and npm The Codex CLI is installed via npm ( npm i -g @openai/codex ) nodejs.org 
 Git 2.30+ Required to clone the demo repo and produce diffs Codex can review git-scm.com 
 A code editor VS Code is the recommended baseline. Cursor and Windsurf also work code.visualstudio.com 
 A GitHub account Required only for Codex Cloud tasks ( Section 8 and Appendix E ) github.com 
 WSL2 (Windows users only) The Codex CLI is experimental on native Windows; WSL is the supported path Microsoft WSL docs 
 Verify Your Environment 
 Run these three commands before you start Section 4 . If any of them fails, fix it first. 
 node --version # should print v18.x or higher
npm --version # should print 9.x or higher
git --version # should print 2.30 or higher What This Handbook Will Not Teach You 
 To set expectations honestly, this handbook does not cover: 
 How to write production-grade Python, JavaScript, or any specific language. We use small examples to demonstrate Codex behavior, not teach syntax. 
 How to design a system architecture from scratch. Section 14 explains why Codex is a poor fit for novel architecture decisions. 
 How to administer GitHub at the organization level. Section 8 covers the Codex-specific GitHub Connector setup, but assumes your GitHub org already exists. 
 LLM internals (attention, RLHF, and so on). We treat the model as a black box with measurable behavior. 
 Section 1: What Codex Is 
 Codex is OpenAI's coding agent. The most important thing to understand is that Codex is not just a single model name. It's a product and workflow layer designed to help people write, review, debug, and ship code faster. In OpenAI's own wording, it's an AI coding agent that can work with you locally or complete tasks in the cloud. 
 That distinction matters. Most people think of AI in one of two ways: 
 A chat model that answers questions. 
 A coding assistant that suggests snippets. 
 Codex is broader than both. It can inspect a repository, edit files, run commands, and execute tests. It can also handle larger chunks of work by taking a prompt or spec and turning it into a task plan, code changes, and reviewable output. 
 For teams, the cloud-based workflow is especially important because it lets Codex run in the background while engineers stay in flow. 
 OpenAI's current docs also place Codex alongside a wider set of developer tools: the API, the Responses API, the Agents SDK, MCP tools, and the Codex app. If you are onboarding a team, the easiest mental model is this: 
 The models are the engine. 
 Codex is the coding product that uses those engines. 
 The CLI, IDE extension, web app, and cloud tasks are the ways you interact with it. 
 Section 2: Where Codex Fits in the OpenAI Ecosystem 
 OpenAI now offers a layered stack: 
 General-purpose frontier models such as GPT-5.5 , GPT-5.5 Pro , GPT-5.4, GPT-5.4-mini, and GPT-5.4-nano. 
 Codex-specific models such as GPT-5.3-Codex, GPT-5.2-Codex, GPT-5.1-Codex, and codex-mini-latest. 
 Product surfaces that package those models into workflows, such as Codex CLI, the Codex app, IDE extensions, cloud tasks, and code review. 
 The practical difference is simple: 
 If you need one-off reasoning, synthesis, or general chat, you may use a general model. 
 If you need an agent that should navigate a repository, change files, run tests, and push toward a concrete code outcome, Codex is the purpose-built surface. 
 OpenAI's current model docs describe GPT-5.4 as the flagship model for complex reasoning and coding. At the same time, Codex-specific model pages describe GPT-5.3-Codex and GPT-5.2-Codex as optimized for agentic coding tasks in Codex or similar environments. That tells you how OpenAI is positioning the stack: 
 GPT-5.4 is the general flagship. 
 Codex-specific models are tuned for coding workflows. 
 Codex the product can switch models depending on the surface and configuration. 
 If you remember nothing else from this section, remember this: Codex is the workflow. Models are the engine. 
 GPT-5.5: The Newest Release 
 OpenAI launched GPT-5.5 on April 23, 2026, with API availability following on April 24, 2026. A higher-tier GPT-5.5 Pro variant shipped alongside it. OpenAI describes GPT-5.5 as their "smartest and most intuitive to use model yet, and the next step toward a new way of getting work done on a computer." 
 For a Codex user, the practical upshot is short: 
 GPT-5.5 is the new general flagship. Anywhere older docs say "GPT-5.4 is the flagship," read GPT-5.5 going forward. GPT-5.4 remains available as a cheaper default. 
 Codex surfaces will switch over. Expect GPT-5.5 to become selectable (and often the default) inside the CLI, IDE, app, and cloud tasks shortly after launch. Verify the active model in your settings. 
 Pricing has shifted. GPT-5.5 sits well above GPT-5.4 on a per-token basis. See Section 7 before approving budgets. 
 The full benchmark breakdown, performance highlights, and per-workload guidance for picking GPT-5.5 vs GPT-5.4 vs Codex-specific models are in Section 11: Model Specs and Benchmarks . Read that section once you have the foundational chapters under your belt. 
 Section 3: The Core Surfaces 
 Codex currently shows up in a few places, and each one is optimized for a slightly different working style. 
 Codex CLI 
 Official docs: developers.openai.com/codex/cli 
 npm package: @openai/codex 
 GitHub repo 
 The CLI is the fastest way to put Codex directly into a terminal session. The docs describe it as OpenAI's coding agent that runs locally from your terminal, can read, change, and run code on your machine, and is open source and written in Rust. 
 Use the CLI when you want: 
 A terminal-first workflow. 
 Fast iteration inside an existing repo. 
 Fine-grained control over approvals and execution. 
 A lightweight path for local coding tasks. 
 IDE Extension 
 Official docs: developers.openai.com/codex/ide 
 VS Code Marketplace listing ( openai.chatgpt ) 
 The CLI docs and Help Center articles point to the IDE extension for VS Code, Cursor, Windsurf, and other VS Code forks. This is the natural fit when your team lives in an editor and wants Codex embedded in the normal coding flow. 
 Use the IDE extension when you want: 
 Codex close to the files you are already editing. 
 Prompting and editing without switching contexts. 
 A bridge between human-driven and agent-driven editing. 
 Codex App 
 Help Center: Using Codex with your ChatGPT plan 
 Download from chatgpt.com/codex 
 OpenAI's Help Center says the Codex app is available on macOS and Windows. It is designed for parallel work across projects, with built-in worktree support, skills, automations, and git functionality. 
 Use the app when you want: 
 Multiple Codex agents running in parallel. 
 Cloud tasks without bouncing between terminal and editor. 
 A project-centric place to assign and monitor tasks. 
 Codex Cloud 
 Official docs: developers.openai.com/codex/cloud 
 Web interface: chatgpt.com/codex 
 Codex cloud is the background execution mode. It runs each task in an isolated sandbox with the repository and environment, and it is intended for reviewable code output rather than direct interactive sessions. 
 Use Codex cloud when you want: 
 Tasks to run while you do something else. 
 Sandboxed execution with reviewable diffs. 
 Automated code review or repository-level workflows. 
 Code Review 
 Help Center: Codex for code review 
 Codex use cases 
 Codex can also review code inside GitHub. OpenAI describes this as a way to automatically review your personal pull requests or configure reviews at the team level. 
 Use code review when you want: 
 A second set of eyes on pull requests. 
 Automated regression or issue spotting before human review. 
 Lightweight review coverage across a team. 
 Section 4: Getting Started: Install, Set Up, and Your First Task 
 This section walks you end-to-end from "nothing installed" to "Codex just fixed a real bug for me." 
 We will use a tiny demo repository you build yourself in two minutes — a small Python price-calculator with one obvious bug and one missing test. That gives you a real, reproducible target you can throw away when you're done. 
 The same walkthrough works for the CLI, the IDE extension, and the app, with notes for each. 
 If you have existing code you would rather use, skip ahead to Step 4 and point Codex at your own repo. The demo is for readers who want a known-good starting point. 
 Step 0: Confirm Access 
 Codex is included with ChatGPT Plus, Pro, Business, and Enterprise/Edu plans. For a limited time, it is also included with Free and Go, with stricter rate limits. 
 If you are in a team or enterprise workspace, access may also depend on workspace settings and role-based controls. Do not assume that a ChatGPT subscription alone guarantees access in a managed environment — confirm with your admin or look in Codex Cloud settings at chatgpt.com/codex . 
 Step 1: Install Codex 
 You have three install paths. Pick one to start; you can add the others later. 
 Option A: The CLI (recommended for first task) 
 The CLI is the most direct way to see how Codex behaves. The official docs note that macOS and Linux are first-class, while Windows is experimental and you should use WSL2 . 
 npm i -g @openai/codex
codex --version If codex --version prints a version number, you are done. 
 Option B: The VS Code Extension 
 In VS Code (or Cursor / Windsurf), open the Extensions panel, search for "Codex" by openai , and install it. Or from a terminal: 
 code --install-extension openai.chatgpt The Codex panel will appear in the right sidebar after install. 
 Option C: The Codex App 
 Download the Codex app for macOS or Windows from chatgpt.com/codex . The app shines when you want parallel tasks, built-in git worktrees, and a project-centric UI. For your very first task it is overkill — start with the CLI or extension. 
 VS Code users: For a step-by-step guide covering all three VS Code entry points (extension, CLI in the integrated terminal, and browser Codex), see Appendix E: Working with Codex in VS Code . 
 Step 2: Authenticate 
 Run codex in a terminal (or open the extension panel). You will be prompted to: 
 Sign in with ChatGPT — recommended. Usage is charged against your plan's included Codex credits. 
 Sign in with an API key — used when you want metered API billing or your workspace policy requires it. 
 If you are unsure, pick ChatGPT sign-in. 
 Step 3: Build the Demo Repo 
 This is the part most quick-starts skip. Instead of pointing Codex at "any repo," let's create a small, self-contained demo repo with a known bug so you can verify Codex actually fixes it. 
 In a terminal, run: 
 mkdir codex-demo && cd codex-demo
git init Now create three files. First, pricing.py — a small pricing calculator with one off-by-one bug and one missing edge case: 
 # pricing.py
def apply_discount(price: float, discount_percent: float) -> float:
 """Apply a percentage discount to a price.

 BUG: The discount is applied as a multiplier of (discount_percent / 10)
 instead of (discount_percent / 100). A 20% discount currently doubles
 the price instead of reducing it.
 """
 if discount_percent < 0:
 raise ValueError("discount_percent must be >= 0")
 return price * (1 - discount_percent / 10)

def cart_total(items: list[dict], discount_percent: float = 0) -> float:
 """Compute the total for a list of cart items after a discount."""
 subtotal = sum(item["price"] * item["quantity"] for item in items)
 return apply_discount(subtotal, discount_percent) Then test_pricing.py — a single passing test plus one that will fail because of the bug: 
 # test_pricing.py
from pricing import apply_discount, cart_total

def test_no_discount_returns_original_price():
 assert apply_discount(100.0, 0) == 100.0

def test_twenty_percent_discount_on_100_is_80():
 # This will FAIL until the bug in apply_discount is fixed.
 assert apply_discount(100.0, 20) == 80.0

def test_cart_total_with_discount():
 items = [
 {"price": 10.0, "quantity": 2},
 {"price": 5.0, "quantity": 1},
 ]
 # Subtotal is 25.0. With 10% off, expected total is 22.5.
 assert cart_total(items, discount_percent=10) == 22.5 And a tiny README.md : 
 # codex-demo

A tiny pricing module used to learn the Codex workflow.

Run tests with: `python -m pytest` Commit the starting state so Codex's diffs are easy to review: 
 git add .
git commit -m "Initial demo: pricing module with a known bug" Confirm the bug is real before you ask Codex to fix it: 
 python -m pytest You should see two failing tests ( test_twenty_percent_discount_on_100_is_80 and test_cart_total_with_discount ). 
 If pytest is not installed: pip install pytest . The full demo needs only Python 3.10+ and pytest. 
 Step 4: Launch Codex and Run Your First Task 
 Now point Codex at the demo repo. 
 From the CLI: 
 cd codex-demo
codex When Codex starts, give it a clear, bounded task. Type this prompt exactly: 
 The test suite has two failing tests. Read pricing.py and test_pricing.py,
identify the root cause, fix the smallest possible thing, then run the tests
to confirm they pass. Explain what you changed and why. Codex will: 
 Inspect pricing.py and test_pricing.py . 
 Recognize the off-by-one bug ( / 10 should be / 100 ). 
 Propose a one-line diff. 
 Ask for approval before modifying the file (in the default approval mode). 
 After you approve, run python -m pytest and report that all three tests now pass. 
 From the VS Code extension: Open the codex-demo folder in VS Code, open the Codex panel in the right sidebar, and paste the same prompt. The diff will appear inline in the editor for you to review and accept. 
 Step 5: Review the Diff 
 This is the most important habit to build early. Even though the fix is one character ( 10 → 100 ), look at the diff before accepting: 
 git diff Read the change. Confirm it matches what Codex described. Run the tests yourself: 
 python -m pytest All three should pass. Commit the fix: 
 git commit -am "Fix off-by-one in apply_discount" You have just completed the full Codex loop: context → task → change → review → verify . Every bigger task is a longer version of this loop. 
 Step 6: Try Two More Bounded Tasks 
 Now that the loop works, try these against the same demo repo: 
 Add an edge case test. Prompt: "Add a test that verifies apply_discount raises a ValueError when discount_percent is negative. Run the tests after." 
 Add a missing safety check. Prompt: " apply_discount does not currently reject discount_percent values greater than 100, which would produce a negative price. Add validation, update the existing tests if needed, and add a new test for the new behavior." 
 Each task is small, has a clear acceptance criterion (the tests pass), and produces a reviewable diff. That is the shape of every good Codex task. 
 Step 7 (Optional): Set Up Codex Cloud 
 Cloud tasks let Codex run in the background while you do other work. They require a GitHub-hosted repository . 
 To enable Codex Cloud against the demo repo: 
 Push codex-demo to a private GitHub repo: gh repo create codex-demo --private --source=. --push (requires the gh CLI). 
 Visit chatgpt.com/codex and connect the ChatGPT GitHub Connector . 
 Allow the codex-demo repository in the connector. Do not grant org-wide access by default — see Appendix C . 
 From the web interface, pick the repo and prompt: "Add type hints to every function in pricing.py and add a CI-style summary of what changed." 
 Wait for the sandbox to finish, review the diff in the browser, and either accept it or open a PR. 
 By default, Codex Cloud sandboxes have no internet access . That is deliberate — admins can allowlist dependency registries and trusted sites if a real workflow needs them. 
 When to Use Which Surface 
 After completing the demo, the surface trade-offs become concrete: 
 CLI — fastest for terminal-heavy local work, scriptable, best for multi-step agentic tasks with explicit approvals. 
 VS Code extension — lowest friction for in-flow editing while you are already in the editor. 
 Codex app — best when you want to run multiple parallel tasks across projects with worktree isolation. 
 Codex Cloud — best for background work, long-running tasks, and PR-style review you can leave running. 
 Most experienced users have all of them installed and pick per task. A single workflow rarely fits every kind of work. 
 What If Something Doesn't Work? 
 If you get stuck during this walkthrough: 
 codex command not found → npm's global bin is not on your PATH. Restart your terminal, or use a Node version manager like nvm. 
 Sign-in keeps failing → confirm the email matches your ChatGPT plan; in enterprise workspaces, your admin must enable Codex. 
 Codex won't modify the file → you may be in a strict approval mode. Approve when prompted, or relax the mode after your first successful task. 
 Windows misbehavior → switch to a WSL2 terminal. Native Windows for the CLI is experimental. 
 The full troubleshooting guide is in Section 12 . 
 Section 5: How to Use Codex Effectively 
 Codex works best when you treat it like a developer you're onboarding rather than a magic prompt responder. The more concrete your task, the better the result. 
 Each tip below has a bad example (what people actually type) and a good example (what produces a useful result). Most use the codex-demo repo from Section 4 so you can run them yourself. 
 Give It a Real Objective 
 A "real objective" means a concrete goal with a verifiable outcome — not a feeling. 
 Bad: 
 Improve this codebase. Codex will pick something to do, but you have no way to know if the result is what you wanted, and the diff will probably touch more than you can review. 
 Good: 
 Refactor cart_total in pricing.py so the iteration logic and the discount
application are in two separate helper functions. Keep the public signature
of cart_total unchanged. Add tests for each helper. Run pytest at the end. This works because there is exactly one acceptance criterion (tests pass with the new structure) and exactly one boundary (public signature unchanged). You can review the diff in 30 seconds. 
 Other shapes that work: 
 "Fix the failing test in test_pricing.py::test_twenty_percent_discount_on_100_is_80 ." 
 "Add a currency: str = 'USD' parameter to cart_total and update the tests." 
 "Review the changes in my last commit for missing edge cases." 
 Provide the Right Context 
 Codex can inspect the repo, but you still need to steer it to the right files and constraints. Without that, it wanders. 
 Bad: 
 Add validation to the pricing module. What kind of validation? On which inputs? What error class? Codex has to guess all of that. 
 Good: 
 Context:
- File: pricing.py
- Function: apply_discount
- Current behavior: raises ValueError for negative discount_percent.
- Desired behavior: also raise ValueError when discount_percent > 100,
 with the message "discount_percent must be between 0 and 100".

Task:
- Add the validation.
- Add a matching test in test_pricing.py.
- Do not change apply_discount's public signature.
- Run pytest after. Notice the structure: what file , current behavior , desired behavior , task , constraints , how to verify . That is the difference between a hopeful prompt and a usable spec. 
 For larger tasks, also include: 
 A link to the issue or spec (Codex can fetch it if web access is enabled). 
 The names of related files even if Codex could find them itself — naming them halves the time-to-first-edit. 
 The name of any test command, build command, or lint that should pass. 
 Ask for Intermediate Thinking When Needed 
 "Intermediate thinking" means asking Codex to plan in writing before it edits files . The default is for Codex to dive straight to code. For anything larger than a single function, that is the wrong default. 
 Without intermediate thinking (the alternative): 
 Refactor pricing.py to support multiple currencies. Codex starts editing immediately. You discover after the fact that it changed the database schema, the API contract, and three test files — and you have no idea whether the design choice it made was the right one. 
 With intermediate thinking: 
 I want to add multi-currency support to pricing.py.

Before editing anything:
1. List the files you expect to touch and why.
2. Outline the approach in 5-10 bullets.
3. Call out any assumptions you are making and any open questions.
4. Identify the riskiest part of the change.

Wait for my approval before making any edits. Now you get a plan you can review, push back on, or scrap entirely — at zero cost to the codebase. After you approve, Codex executes against the plan it just wrote, which makes the resulting diff predictable. 
 Use intermediate thinking whenever the task is: 
 Multi-file or cross-cutting. 
 Architecturally novel for this codebase. 
 Hard to test (so the diff is your only signal). 
 High blast-radius if wrong (auth, payments, data migrations). 
 Prefer Bounded Changes 
 A bounded change is one with all four of these properties: 
 Small surface area — touches one file, one module, or one logical concept. 
 Clear acceptance criterion — there's a specific test, output, or behavior that proves it worked. 
 Reviewable in a few minutes — a human can read the diff and form an opinion without setting aside an hour. 
 Easily revertible — if it goes wrong, git revert undoes it cleanly without breaking anything else. 
 The opposite is an unbounded change : "make the codebase faster," "modernize the API," "add types everywhere." These have no clear endpoint, no easy verification, and no clean revert path. 
 Bounded examples (good): 
 "Add a serialize() method to CartItem that returns a dict suitable for JSON encoding. Add a test." 
 "In apply_discount , replace the magic number 100 with a module-level constant MAX_DISCOUNT_PERCENT ." 
 "The cart_total function takes a discount_percent keyword argument that defaults to 0. Make the default None and treat None as 'no discount.' Update the tests." 
 Unbounded examples (avoid): 
 "Make pricing.py production-ready." 
 "Add proper error handling everywhere." 
 "Improve the architecture." 
 When you catch yourself writing an unbounded prompt, break it into a list of bounded ones before sending. The decomposition itself is most of the work; once you have it, Codex is good at executing each piece. 
 Use Reviews as a Loop 
 Codex is not just for writing code — it is also a useful pre-merge reviewer. The loop is: 
 You (or Codex) write the change. 
 Ask Codex to review it. 
 Fix the issues it finds. 
 Re-run tests. 
 What this looks like in practice: 
 After completing a task in codex-demo , ask Codex to review your own commit: 
 Review the change in my last commit (git show HEAD) for:
- correctness issues (off-by-one, type mismatches, wrong defaults)
- missing tests, especially edge cases
- security concerns (input validation, injection, unsafe defaults)
- maintainability risks (unclear naming, hidden coupling)

Prioritize findings by severity (critical / important / nit). For each
finding, point to the exact line and propose a concrete fix. Do not
modify any files in this turn — just produce the review. You will typically get back a structured response like: 
 CRITICAL: line 14 — apply_discount accepts NaN silently because the type
 check is `discount_percent < 0`, which is False for NaN. Fix: add an
 explicit math.isnan() check before the comparison.

IMPORTANT: test_pricing.py has no test for the boundary discount_percent=100.
 Fix: add a test asserting apply_discount(100, 100) == 0.

NIT: line 8 — the docstring mentions a "BUG" comment that should be removed
 now that the bug is fixed. Then you triage: fix the critical and important findings (often by feeding them back to Codex with "apply the fixes you proposed"), defer or reject the nits, and re-run tests. 
 This converts Codex from a code generator into a quality gate , which is usually the higher-leverage use. A team that uses Codex only as a generator gets faster code; a team that also uses it as a reviewer gets better code. 
 Section 6: Difference Between Codex and Other Coding Tools 
 This is the section that usually matters most to new users, because the category boundaries are easy to blur. 
 Codex Is A Product Layer, Not Just A Model 
 Codex is the product experience and workflow layer. Models are the underlying engines. Put differently: 
 A general model answers questions or writes text. 
 A coding model is tuned more narrowly for software tasks. 
 Codex packages the model inside an agentic coding workflow with files, commands, approvals, sandboxes, and reviews. 
 That matters because users often compare Codex to "another model" when the real comparison is "another coding system." 
 Codex vs OpenAI General Models 
 OpenAI's current models page recommends GPT-5.4 as the flagship model for complex reasoning and coding. That is the general model-side recommendation. 
 Codex-specific pages, on the other hand, describe models like GPT-5.3-Codex and GPT-5.2-Codex as optimized for agentic coding tasks in Codex or similar environments. 
 The practical takeaway: 
 Use GPT-5.4 when you want a top-tier general model. 
 Use Codex-specific models when you want a model optimized for coding workflows inside Codex. 
 Use the Codex surface when you want file edits, shell commands, reviews, and sandboxes, not just text output. 
 Codex vs Claude Code 
 Claude Code is also a terminal-based agentic coding tool. Anthropic's docs describe it as a terminal tool that can make plans, edit files, run commands, create commits, and work with MCP-connected data sources. It is strong if your team already prefers a terminal-first workflow and wants a tightly scriptable developer tool. 
 Codex differs in a few practical ways: 
 Codex spans more surfaces, including CLI, IDE extension, app, cloud tasks, and code review. 
 Codex cloud is built around GitHub-connected task execution and review. 
 Codex is more explicitly positioned as a family of coding workflows, not just a single terminal agent. 
 The practical takeaway: 
 Choose Claude Code if you want a terminal-native workflow with strong composability and you are happy living mostly in the shell. 
 Choose Codex if you want a broader product layer with local, cloud, and app-based workflows that can be shared across a team. 
 Codex vs GitHub Copilot Coding Agent 
 GitHub Copilot coding agent is designed around GitHub's own workflow. GitHub docs describe it as an agent you can assign issues or pull requests to, and it works in the background to create or modify PRs. It lives very naturally inside GitHub-hosted development flows. 
 Codex is different in emphasis: 
 Copilot coding agent is highly GitHub-centric. 
 Codex is broader across terminal, IDE, app, and cloud. 
 Copilot is a strong fit if your team already uses GitHub as the center of gravity for task assignment and review. 
 Codex is a stronger fit if you want a more general coding agent surface that can work across local and cloud workflows. 
 The practical takeaway: 
 Choose Copilot coding agent if your process is already deeply anchored in GitHub issues and pull requests. 
 Choose Codex if you want a wider agent workflow that can run locally, in the IDE, or in Codex cloud. 
 Codex vs Open-Weight and Self-Hosted Models 
 Open-weight or self-hosted models serve a different need. Teams usually reach for them when they want: 
 Full infrastructure control. 
 Custom hosting or air-gapped deployment. 
 More direct control over retention and data boundaries. 
 A lower-cost path at high scale if they already own the hardware and ops stack. 
 The tradeoff is that self-hosted models usually do not give you the same out-of-the-box agentic product experience that Codex does. You have to assemble the orchestration, repo access, sandboxing, approvals, and review loop yourself. 
 That means the real choice is not "Which model is smartest?" It is "How much engineering do I want to spend on the workflow around the model?" 
 The practical takeaway: 
 Choose open-weight or self-hosted models when infrastructure control is the main requirement and you are willing to build the surrounding agent system. 
 Choose Codex when you want the workflow already packaged, especially for day-to-day engineering teams. 
 Codex vs General Chat Models 
 General chat models are best when the task is: 
 A question and answer exchange. 
 Conceptual reasoning. 
 Drafting prose. 
 Summarizing or rewriting text. 
 Codex is better when the task is: 
 Reading and modifying a repository. 
 Running tests. 
 Fixing code. 
 Reviewing pull requests. 
 Coordinating multi-step implementation work. 
 Codex vs API Usage of the Same Models 
 The same model family can behave differently depending on the surface. 
 In the API, you may call a model directly and design your own orchestration. 
 In Codex, the same or similar model may be wrapped in repo access, approval flows, and task execution. 
 That is why some model pages mention that a model is optimized for "Codex or similar environments." The model is tuned for agentic software work, but the workflow surface still matters. 
 Comparison Matrix 
 The prose comparisons above collapse into a single matrix for fast reference: 
 Dimension Codex Claude Code GitHub Copilot Coding Agent Self-hosted / Open-weight 
 Primary surface CLI, IDE, app, cloud CLI (terminal-first) GitHub web/PR/issues Whatever you build 
 Background execution Yes (Codex Cloud sandboxes) Limited; runs locally Yes (GitHub Actions runners) DIY 
 Repository integration GitHub via connector; local repos directly Local; MCP-connected sources Native GitHub DIY 
 Model choice OpenAI models, switchable per surface Anthropic Claude models GitHub-managed (mix of vendors) Any model you can host 
 Approval and sandbox controls Yes, per-surface Yes, per-tool GitHub permission model DIY 
 Parallel agents Yes (app + cloud) Limited Yes (per-PR) DIY 
 Best fit Cross-surface team workflows Terminal-native power users Teams already living in GitHub Air-gapped, custom infra, or cost-sensitive at scale 
 Main tradeoff OpenAI ecosystem lock-in; price tier Less product surface area Heavily GitHub-coupled Significant engineering effort 
 Use the matrix to pick the dominant tool, then layer the others where they fit. Many teams legitimately run two of these in parallel — for example, Codex for cross-surface work and Claude Code for power-user terminal workflows. 
 Which Tool Should A New User Choose? 
 As a rule of thumb: 
 For terminal-first coding and scripting, Claude Code is a strong alternative. 
 For GitHub-native issue and PR automation, GitHub Copilot coding agent fits naturally. 
 For local plus cloud plus app-based team workflows, Codex is the most flexible option. 
 For maximum infrastructure control, self-hosted or open-weight stacks make sense. 
 OpenAI's docs currently list GPT-5.5 as the general flagship, with GPT-5.4, GPT-5.4-mini, and GPT-5.4-nano remaining available below it, while Codex docs and model pages expose Codex-specific variants and model switching inside the CLI. 
 Section 7: Pricing and Plan Access 
 Pricing is the part of Codex most likely to change, so this section should be treated as a snapshot of the current official docs. 
 Plan Access 
 OpenAI's current Help Center says Codex is included with: 
 ChatGPT Plus 
 ChatGPT Pro 
 ChatGPT Business 
 ChatGPT Enterprise/Edu 
 For a limited time, it is also included with Free and Go, though those plans are temporary exceptions and subject to rate limits. 
 Flexible Pricing and Credits 
 The current rate card says Codex pricing changed on April 2, 2026 to align with API token usage instead of purely per-message pricing. The same article explains that: 
 New and existing Plus and Pro customers use the token-based rate card. 
 New and existing Business customers use the token-based rate card. 
 New Enterprise customers use the token-based rate card. 
 Existing Enterprise/Edu and several other legacy plan categories remain on the legacy rate card until migration. 
 This is important because two teams in the same company can be on different pricing logic depending on workspace status and plan vintage. 
 Current Model Pricing Snapshot 
 The current model pages list pricing per 1M tokens in USD. The exact numbers depend on the model you choose: 
 GPT-5.5: \(5 input, \)30 output. New flagship as of April 23, 2026. 
 GPT-5.5 Pro: \(30 input, \)180 output. Higher-tier variant for the most demanding agentic and reasoning workloads. 
 GPT-5.4: \(2.50 input, \)15 output. 
 GPT-5.4-mini: \(0.75 input, \)4.50 output. 
 GPT-5.4-nano: \(0.20 input, \)1.25 output. 
 GPT-5-Codex: \(1.25 input, \)10 output. 
 GPT-5.2-Codex: \(1.75 input, \)14 output. 
 GPT-5.1-Codex-mini: \(0.25 input, \)2 output. 
 codex-mini-latest: \(1.50 input, \)6 output. 
 These model pages also note context windows, output limits, and whether the model is intended for Codex-specific or general API use. For budget planning, remember that longer outputs can cost much more than the input prompt, so task framing matters as much as model choice. 
 Note that GPT-5.5 is roughly 2x the input price and 2x the output price of GPT-5.4, and GPT-5.5 Pro is an order of magnitude above that. OpenAI's framing is that GPT-5.5 is also more token-efficient than GPT-5.4, which can offset some of the headline price difference, but you should measure this on your own workloads before assuming it nets out. For the Codex-specific models, expect the lineup to shift as Codex variants based on GPT-5.5 ship; until then, the Codex-specific models above remain the right choice for purely coding-shaped tasks. 
 What This Means in Practice 
 The real cost depends on: 
 Input size. 
 Cached input. 
 Output length. 
 Whether the task uses fast mode. 
 Which model you select. 
 So if you are planning a team rollout, do not estimate usage from "number of prompts" alone. Estimate based on expected token consumption and task type. 
 Legacy Pricing 
 The legacy rate card still matters for users and workspaces that have not been migrated. The big lesson is that pricing is now tied more closely to model usage than to a simple fixed message count. Anyone budgeting Codex should read the current rate card before setting internal chargeback rules or usage policies. 
 Worked Cost Example 
 Pricing tables are easy to misread. A worked example makes the model selection question concrete. 
 Scenario: A 30-engineer team uses Codex Cloud for automated pull request review. Each engineer opens roughly 4 PRs per week. Each PR review pulls in approximately 30,000 input tokens (the diff plus relevant context files) and produces approximately 3,000 output tokens (the review comments and risk summary). 
 Weekly token volume: 
 Reviews per week: 30 engineers × 4 PRs = 120 reviews 
 Input tokens per week: 120 × 30,000 = 3.6M input tokens 
 Output tokens per week: 120 × 3,000 = 360K output tokens 
 Cost per week by model: 
 Model Input cost Output cost Weekly total Annualized (52 wk) 
 GPT-5.5 (\(5 / \)30) 3.6M × \(5/1M = \)18.00 0.36M × \(30/1M = \)10.80 $28.80 $1,498 
 GPT-5.5 Pro (\(30 / \)180) $108.00 $64.80 $172.80 $8,986 
 GPT-5.4 (\(2.50 / \)15) $9.00 $5.40 $14.40 $749 
 GPT-5-Codex (\(1.25 / \)10) $4.50 $3.60 $8.10 $421 
 GPT-5.1-Codex-mini (\(0.25 / \)2) $0.90 $0.72 $1.62 $84 
 Reading the table: The headline GPT-5.5 sticker shock disappears at this volume — under $1,500/year for 30 engineers' worth of automated review is a rounding error against engineering payroll. GPT-5.5 Pro is 6× more expensive and generally not justified for routine review; reserve it for the small share of reviews where you need its extra capability. The Codex-specific models are dramatically cheaper and are the right default if your reviews are mostly mechanical (style, obvious bugs, missing tests). 
 What this example does not capture: 
 Cached input. OpenAI prices repeated input tokens lower; if your review pulls the same context files repeatedly, real costs are lower than shown. 
 Long-task overhead. Agentic workflows that re-read files or iterate burn many more tokens than a single-shot review. A coding task can easily be 5–10× the tokens of a review. 
 Failure retries. A failed task that gets re-run costs roughly the same as the original. Agent flakiness is a real budget line item. 
 Mixed-model strategies. Most mature teams route cheap tasks (test stubs, doc updates) to a Codex-mini model and reserve GPT-5.5 for repository-wide refactors and PRs that need long-context reasoning. 
 The practical pattern: build the cost model around your actual highest-volume workload (usually PR review or test generation), then size the GPT-5.5 budget separately for the smaller set of tasks that actually benefit from the new capabilities. 
 Section 8: Security, Permissions, and Enterprise Setup 
 Teams care about Codex not just as a productivity tool, but as a controlled software-development system. OpenAI's docs reflect that reality. 
 Local vs Cloud Access 
 Enterprise admins can separately enable: 
 Codex Local 
 Codex Cloud 
 Both 
 Codex Local covers the app, CLI, and IDE extension. Codex Cloud covers hosted tasks, code review, and related integrations. 
 That separation is useful because some organizations want local tooling enabled broadly while keeping cloud tasks restricted to fewer users. 
 Workspace Controls 
 The admin docs say workspace owners can use RBAC to manage access. They can: 
 Set a default role. 
 Create custom roles. 
 Assign roles to groups. 
 Sync groups with SCIM. 
 Manage permissions centrally. 
 This is the right place to build a rollout with least privilege rather than giving every developer broad Codex access by default. 
 GitHub Connector and Repository Access 
 Codex Cloud requires GitHub-hosted repositories. Admins connect the ChatGPT GitHub Connector, choose an installation target, and allow specific repositories. Codex uses short-lived, least-privilege GitHub App tokens and respects repository permissions and branch protection rules. 
 For security teams, that matters because it keeps Codex aligned with the repo access model you already use. 
 Internet Access 
 By default, Codex cloud agents do not have internet access at runtime. That is deliberate. If your task truly needs access to dependency registries or trusted sites, admins can configure allowlists and HTTP method limits. 
 Recommended Governance Pattern 
 The enterprise docs recommend using separate groups for users and admins: 
 A smaller Codex Admin group for people who manage policy and governance. 
 A broader Codex Users group for developers who just need to use the tool. 
 That keeps policy management tight and avoids accidental over-permissioning. 
 Section 9: Best Practices for Teams 
 If you are onboarding a team, you will get much better outcomes if you set expectations up front. 
 Start With Simple, Valuable Tasks 
 Good first-team use cases: 
 Pull request review. 
 Small bug fixes. 
 Test generation. 
 Documentation updates. 
 Codebase navigation and understanding. 
 These are easy to compare against human work and easy to judge for quality. 
 Standardize Task Prompts 
 Give people a shared prompt template. For example: 
 Task: Fix the failing test in X.
Context: The regression started after Y.
Constraints: Do not change public API behavior.
Output: Explain root cause, apply fix, run tests, summarize risks. This makes results easier to review and reduces the "prompt quality lottery" that often hurts team adoption. 
 Use a Review Culture 
 Codex should not replace code review discipline. Treat it as: 
 A first-pass implementer. 
 A pre-review reviewer. 
 A way to reduce repetitive work. 
 The human team should still own architecture, product tradeoffs, and final sign-off. 
 Measure What Matters 
 The metrics that matter are the ones that tell you whether Codex is producing reviewable, mergeable, trustworthy work — not the ones that count activity. Below is each metric, how to actually compute it from data you already have , and the rule of thumb for what "healthy" looks like. 
 1. Time to First Useful Diff 
 Definition: From the moment a Codex task is started, how long until it produces a diff that a human would actually consider applying (after possible small tweaks). 
 How to measure: 
 For CLI/IDE tasks, log the wall-clock time from prompt submission to first diff. The Codex CLI emits structured logs you can parse; a simple wrapper script suffices: 
 start=\((date +%s); codex "<prompt>"; echo "elapsed: \)(( $(date +%s) - start ))s" 
 For Codex Cloud tasks, use the task duration shown in the chatgpt.com/codex dashboard, or pull it from the workspace usage export. 
 Tag each task as "useful" or "discarded" in a shared spreadsheet for the first month. After that, you can sample. 
 Healthy: under 2 minutes for bounded tasks; under 10 minutes for multi-file refactors. If the median is much higher, your prompts probably lack context (see Section 5 ). 
 2. Test Pass Rate on Codex-Generated Changes 
 Definition: Of the diffs Codex produces, what percentage pass the existing test suite on the first try. 
 How to measure: 
 In CI, tag PRs that originated from Codex (a label like codex-authored or a commit-message prefix works). Then run a simple weekly query: 
 SELECT
 COUNT(*) FILTER (WHERE first_ci_run = 'pass') * 100.0 / COUNT(*) AS first_try_pass_rate
FROM pull_requests
WHERE labels @> '{"codex-authored"}'
 AND created_at > NOW() - INTERVAL '7 days'; 
 For local CLI usage, instrument with a wrapper that runs your test command immediately after Codex finishes and records the exit code. 
 Healthy: above 75% for bounded tasks. Below 50% means Codex is making changes without verifying them — usually fixable by adding "run the tests after" to your prompt template (see Section 9 → Standardize Task Prompts ). 
 3. Review Findings Caught by Codex 
 Definition: When Codex is used as a pre-merge reviewer, how many issues does it surface that a human reviewer or CI would have caught anyway, vs. issues only Codex caught, vs. false positives. 
 How to measure: 
 Have human reviewers annotate Codex's review comments with one of three tags: agree-found-it , agree-missed-it , disagree-noise . 
 Track the ratios over time: 
 Useful-finding rate = ( agree-found-it + agree-missed-it ) / total Codex comments. 
 Unique-value rate = agree-missed-it / total Codex comments. 
 A simple GitHub Actions step that posts the Codex review and asks the human reviewer to react with emoji (✅ / ⚠️ / ❌) makes this nearly free to collect. 
 Healthy: useful-finding rate above 70%; unique-value rate above 20%. Unique-value rate is the number that justifies keeping the workflow on — if it is near zero, Codex is duplicating CI and you can disable it without losing anything. 
 4. Tasks Completed Without Human Rewrite 
 Definition: Of all merged Codex-authored changes, what fraction shipped substantially as Codex wrote them (vs. being heavily rewritten by a human before merge). 
 How to measure: 
 Compare the diff Codex initially produced to the diff that actually merged. The simplest proxy: 
 # in the Codex-authored branch:
git diff codex/initial-commit HEAD --shortstat If the post-Codex diff changes more than ~30% of the lines Codex originally wrote, count the task as "rewritten." 
 Track this monthly. The trend line matters more than the absolute number. 
 Healthy: above 60% shipped without major rewrite. Lower than that, and either prompts are under-specified or Codex is being pushed into work it is bad at — re-read Section 14 . 
 5. Developer Satisfaction 
 Definition: Whether the people actually using the tool think it makes them faster and want to keep using it. Hard numbers do not capture this. 
 How to measure: 
 Run a 5-question pulse survey monthly. Keep it short. Suggested questions, all on a 1–5 scale: 
 "Codex saved me time this week." 
 "I trust Codex's diffs enough to review them confidently." 
 "Codex's review comments are usually worth reading." 
 "I would be unhappy if Codex were taken away." 
 "What is the single biggest friction point?" (free text) 
 Track the trend in question 4 specifically. That is the closest equivalent to a product-market-fit signal for an internal tool. 
 Healthy: average score above 3.5/5 on questions 1–4 by month 3 of rollout. If question 4 trends down, the rollout is failing regardless of what the other metrics say. 
 What NOT to Measure 
 These look useful but mislead: 
 Number of prompts sent. Counts activity, not value. A team sending 10× more prompts may be 10× more productive — or 10× more confused. 
 Tokens consumed. Useful for budget, useless for impact. Heavy users are not necessarily good users. 
 Lines of code generated. Same problem as LOC has always had: you reward verbosity. 
 PRs opened by Codex. A Codex-opened PR that nobody merges is a negative outcome dressed up as a positive one. 
 Use the cost data ( Section 7 ) to manage budget. Use the metrics above to manage adoption. 
 Use the Right Surface for the Job 
 CLI for terminal-heavy local work. 
 IDE extension for day-to-day coding. 
 App for parallel project work. 
 Cloud for background tasks and review. 
 That is usually the difference between "this is useful" and "this is annoying." 
 Section 10: Common Workflows and Examples 
 Here are the workflows most teams will actually use. Each one includes a worked example against the codex-demo repo from Section 4 so you can see the full prompt, the kind of output Codex produces, and what to do with it. 
 Workflow 1: Fix a Bug Locally 
 Use when: A test is failing, a behavior is wrong, and the cause is contained to one file or function. 
 Steps: 
 Open the repo in your terminal or IDE. 
 Ask Codex to inspect the failing path. 
 Request a fix and a test. 
 Review the diff. 
 Run the test suite. 
 Worked example: 
 In the codex-demo repo, suppose a teammate just reported: " apply_discount is silently returning a negative price when discount_percent is greater than 100." Verify the bug first: 
 python -c "from pricing import apply_discount; print(apply_discount(100, 150))"
# prints: -50.0 <-- silent negative price, no error raised Now launch Codex and run: 
 Bug: apply_discount(100, 150) returns -50.0 instead of raising an error.
Expected: discount_percent values above 100 should raise ValueError with
the message "discount_percent must be between 0 and 100".

Task:
- Add the validation in pricing.py.
- Add a test in test_pricing.py that asserts ValueError is raised for
 discount_percent=150.
- Keep the existing tests passing.
- Run pytest at the end and report the result. What you get back: a diff that adds if discount_percent > 100: raise ValueError(...) in apply_discount , a new test_invalid_discount_percent_above_100 test, and the pytest output showing all four tests passing. Review with git diff , run python -m pytest yourself to confirm, then git commit -am "Reject discount_percent > 100" . 
 This works best when the bug is bounded and reproducible. If you cannot reproduce it from the command line, Codex usually cannot either. 
 Workflow 2: Review a Pull Request 
 Use when: You (or a teammate) just made a change and want a fast pre-merge sanity check before opening it for human review. 
 Steps: 
 Point Codex at the PR or changed files. 
 Ask for correctness issues, missing tests, and security risks. 
 Compare the findings against human review. 
 Use Codex as a pre-filter before the broader team reviews. 
 Worked example: 
 After completing Workflow 1 above, ask Codex to review your own change before opening a PR: 
 Review the change in my last commit (HEAD) — it added validation to
apply_discount in pricing.py.

Look for:
- correctness issues (off-by-one on the boundary, wrong error type, etc.)
- missing tests (boundary cases like exactly 100, exactly 0, NaN, negative zero)
- security or robustness issues
- API consistency with the existing apply_discount validation style

Prioritize findings as CRITICAL / IMPORTANT / NIT and propose a concrete
fix for each. Do not modify any files in this turn. What you might get back: 
 IMPORTANT: line 14 — the new validation rejects discount_percent > 100 but
 silently allows discount_percent == 100, which makes the price 0. That is
 technically valid but worth a test to lock the boundary. Add:
 test_apply_discount_at_boundary_100_returns_zero

NIT: the new error message says "between 0 and 100" but the existing check
 for negative values says "must be >= 0". Consider unifying the messages
 for consistency. You apply the IMPORTANT fix (often by following up with: "apply the IMPORTANT fix from your review" ), defer or accept the nit, and re-run tests. 
 This is one of the highest-leverage team workflows because it catches obvious problems before a human spends review time on them. See Section 9 → Measure What Matters → Review Findings Caught by Codex for how to track its actual value over time. 
 Workflow 3: Understand a Large Codebase 
 Use when: You are new to a repo (or returning after months away) and need a map before you can safely make changes. 
 Steps: 
 Ask Codex to trace a request flow. 
 Ask for the key modules and entry points. 
 Request a map of the code path before editing anything. 
 Worked example: 
 The codex-demo repo is too small to need this, so imagine a more realistic case: a teammate's repo with app/ , services/ , models/ , api/ , and 80 files you have never seen. Open the repo in Codex and run: 
 I am new to this codebase. Without modifying anything, give me an
orientation:

1. What is the entry point for the HTTP API?
2. Trace what happens when a POST hits /users — list every file the
 request touches in order, with a one-line description of each.
3. Where is database access centralized? Is there a repository pattern?
4. What test command should I run to verify any change I make?
5. What are the three files I should read first to understand the
 project's conventions?

Output as a structured markdown report. What you get back: a markdown report you can paste into your notes. Read the recommended files, then start working with Codex on actual changes. The 10 minutes spent on this orientation typically saves an hour of confused refactoring later. 
 This workflow is particularly useful for new hires. A senior engineer can also use it the first time they touch an unfamiliar service to avoid breaking conventions they cannot see. 
 Workflow 4: Generate a Feature in Parallel 
 Use when: A feature naturally splits into independent pieces (API + tests + docs, or UI + backend + migration) that do not block each other. 
 Steps: 
 Break the work into subtasks. 
 Run separate Codex tasks for UI, API, tests, or docs. 
 Merge the outputs after review. 
 Worked example: 
 Add a new "loyalty discount" capability to codex-demo . The work splits into three pieces that do not depend on each other: 
 Subtask Surface Prompt 
 A. Implementation CLI in terminal 1 "Add a loyalty_discount(price, customer_tier) function to pricing.py . Tiers are 'bronze' (0%), 'silver' (5%), 'gold' (10%). Reject unknown tiers with ValueError. Do not change any other function." 
 B. Tests Codex Cloud "Generate exhaustive tests in test_pricing.py for a function loyalty_discount(price, customer_tier) with tiers bronze/silver/gold. Cover: each tier, unknown tier, negative price, zero price, decimal prices. Do not modify pricing.py — assume the function will exist." 
 C. Docs VS Code extension "Add a section to README.md documenting the new loyalty_discount function: signature, tier table, and one usage example." 
 Each runs in parallel. When all three finish, merge the diffs (typically the implementation goes first, then tests verify against it, then docs reference what shipped). Review each independently. 
 The Codex app and cloud surfaces are especially good for this because they let you launch and monitor multiple tasks without juggling terminal windows. The CLI also supports parallel work, but it benefits from git worktree so each run operates on its own branch checkout. 
 Workflow 5: Use Subagents for Decomposition 
 Use when: A single task is too large for one Codex run but can be naturally split into investigate / plan / implement phases. 
 The CLI explicitly supports subagents — one Codex task that spawns child tasks, each with a narrower scope and its own context window. 
 Worked example: 
 A bug report says: "Cart totals are sometimes off by a penny for European currencies." You do not yet know if this is a rounding bug, a currency-conversion bug, or a data bug. Run a parent task that decomposes: 
 A bug report says cart totals are occasionally off by a penny for
European currencies.

Decompose this into three subagent tasks:

1. INVESTIGATE: Read pricing.py and any currency-related code. Identify
 every place where floating-point arithmetic touches a money value.
 Report findings without proposing fixes.

2. REPRODUCE: Write a failing test in test_pricing.py that demonstrates
 a one-cent discrepancy with EUR amounts. Use the smallest possible
 reproduction.

3. PROPOSE: Based on (1) and (2), propose two possible fixes (e.g.,
 switching to Decimal vs. rounding at the boundary) with the trade-offs
 of each. Do not implement either yet.

Wait for me to pick a fix before writing any production code. Why subagents help: each child task has a clean context, so the investigation findings do not pollute the test-writing context, and the proposal task gets a clean view of both. You also get a natural human checkpoint between investigation and implementation. 
 That division is often faster than one giant all-purpose run, and dramatically more reviewable. 
 Prompt Cookbook 
 New users often ask for examples because they know what they want outcome-wise but not how to phrase it. These templates are a good starting point. 
 Bug Fix Template 
 Inspect the failing behavior in [file or module].
Identify the root cause.
Patch the smallest safe fix.
Add or update tests.
Summarize what changed and any edge cases I should watch. Use this when the bug is narrow and you want a disciplined fix, not a redesign. 
 Refactor Template 
 Refactor [module] to improve readability and maintain the current behavior.
Keep external APIs stable.
Explain the refactor plan before editing.
Make the smallest set of changes that achieves the goal. Use this when the code works but is hard to maintain. 
 Review Template 
 Review this change for correctness, missing tests, security issues, and maintainability risks.
Prioritize findings by severity.
Call out any behavior changes or ambiguous logic. Use this when you want Codex to act like a pre-merge reviewer. 
 Feature Template 
 Implement [feature] in [file or subsystem].
List the files you expect to touch before changing anything.
Add tests.
Keep the implementation aligned with the current architecture. Use this when the task spans multiple files and you want visibility into the plan. 
 Signs You Are Using Codex Well 
 You usually know the workflow is healthy when: 
 Codex makes small, reviewable diffs instead of broad rewrites. 
 The model asks for clarification only when the missing detail matters. 
 Test coverage improves along with functionality. 
 New developers can use the tool without needing a custom training session. 
 The time from prompt to merged change is lower, but review quality does not drop. 
 You usually know the workflow is unhealthy when: 
 Prompts are vague and every result needs heavy rework. 
 The team treats the first output as final. 
 Nobody is checking diffs or running tests. 
 Users keep asking for "make it better" instead of defining a clear target. 
 Those signals matter more than raw usage counts. 
 Section 11: Model Specs and Benchmarks (GPT-5.5 Deep Dive) 
 Section 2 introduced GPT-5.5 as the new general flagship and gave the three-bullet practical takeaway. This section is the deep dive: the published benchmark numbers, what each one actually measures, why it matters for Codex workloads specifically, and how to use those numbers to pick the right model per task. 
 If you are setting budgets or choosing default models for a team, read this section in full. If you just want to use Codex, you can skim it. 
 Why Benchmarks Matter for Model Selection 
 Codex lets you pick the model behind each surface. Picking well is mostly about matching the model's strengths to the task shape: 
 A bounded local edit (one file, one function) does not benefit much from a frontier model. Codex-specific or Codex-mini variants are usually the right call. 
 A repository-wide refactor that needs the model to keep many files in working memory benefits enormously from long-context performance. 
 An agentic cloud task that runs unattended for ten minutes benefits from low hallucination rates and strong tool-use behavior. 
 A PR review benefits from low hallucination rates above almost everything else — a confident-but-wrong review comment costs more than a missed real issue. 
 The benchmarks below tell you which model best matches each shape. 
 GPT-5.5 Performance Highlights 
 The published benchmarks position GPT-5.5 as a meaningful jump over GPT-5.4, particularly on agentic and long-context work — the workloads most relevant to Codex users. 
 Knowledge work (GDPval) — 84.9% . GDPval evaluates whether a model can produce well-specified knowledge-work output across 44 occupations. This is the headline general-capability number. 
 Computer use (OSWorld-Verified) — 78.7% . Measures whether the model can drive a real computer environment end-to-end. Directly relevant to Codex Cloud sandboxes and agentic CLI runs. 
 Coding (Terminal-Bench 2.0) — 82.7% . A terminal-centric coding benchmark with long-context retrieval and computer-use components. The closest public proxy for Codex CLI workloads. 
 Customer-service workflows (Tau2-bench Telecom) — 98.0% without prompt tuning. Indicates strong tool-use and policy-adherence behavior straight out of the box. 
 Long-context retrieval (MRCR v2 at 1M tokens) — 74.0% , up from 36.6% on GPT-5.4. This is the largest single jump in the report and the most important one for repository-scale Codex tasks where the model must keep many files in working memory. 
 Hallucination rate — independent coverage reports a roughly 60% reduction in hallucinations versus prior generations, which materially changes the trust calculus for review and PR-feedback workflows. 
 What Each Benchmark Actually Measures 
 Benchmarks are easy to misread. Quick definitions of the ones cited above: 
 GDPval — Asks the model to produce specified knowledge-work output across 44 occupations (legal memos, financial summaries, technical documentation, etc.). A high score means the model can produce structured, well-specified output reliably. Use as a general-capability signal, not a coding-specific one. 
 OSWorld-Verified — Tasks the model with operating a real desktop environment to complete real workflows (open files, navigate UIs, run commands). High scores predict the model will behave well in agentic sandboxes that mimic a developer's desktop. 
 Terminal-Bench 2.0 — A terminal-driven coding benchmark with long-context retrieval and computer-use components. The closest public proxy for what Codex CLI actually does day to day. 
 Tau2-bench Telecom — Evaluates complex customer-service-style workflows that require following policies and using tools correctly. A proxy for "does the model do what you told it without going off-script." 
 MRCR v2 at 1M tokens — A long-context retrieval benchmark. Tests whether the model can find and use information across a full 1M-token context window. The single best predictor of behavior on repository-scale Codex tasks where many files must be kept in working memory. 
 Practical Guidance for Codex Users 
 Translate the benchmarks into model choice: 
 Repository-wide tasks (cross-file refactors, multi-module migrations): GPT-5.5. The MRCR v2 jump is the single best signal that it will behave better on large codebases than GPT-5.4 did. 
 Cheap, bounded local edits (single function, single test, doc tweak): GPT-5.4 or a Codex-specific model. The cost/latency tradeoff is much better and the capability headroom is wasted on small tasks. Do not default everything to GPT-5.5 just because it is newest. 
 Agentic cloud tasks (background sandbox runs, multi-step workflows): GPT-5.5. The OSWorld-Verified score and lower hallucination rate are the relevant signals — fewer broken sandbox runs and fewer confidently-wrong outputs. 
 PR review and code review workflows : GPT-5.5. The 60% hallucination drop is the single most important number for review work; a noisy reviewer trains the team to ignore the reviewer. 
 Most expensive workloads (anything that approaches GPT-5.5 Pro pricing): keep GPT-5.5 Pro reserved for the small set of tasks where its extra capability is justified — typically deeply novel reasoning or extreme long-context work. 
 For Procurement: Treat GPT-5.5 as a Separate Budget Line 
 Token consumption on agentic tasks is dominated by output. GPT-5.5 outputs are substantially more expensive than GPT-5.4 outputs. Concretely: 
 Mixed-model strategies are now the rule, not the exception. Most mature teams route routine work to a Codex-mini model and reserve GPT-5.5 for repository-wide and review-heavy work. 
 The worked cost example in Section 7 shows the 30-engineer PR-review case across all five model tiers. Read it before approving a budget. 
 Re-check pricing every quarter. The rate card has changed in the past and will change again. 
 Verify Before Quoting 
 The numbers in this section come from OpenAI's launch documentation and contemporaneous press coverage. Before they go into a procurement deck or a public document, verify against the official OpenAI announcement and the model page — see Section 16: Source References . Benchmarks get re-run; numbers shift with eval methodology changes. 
 Section 12: Troubleshooting 
 Even good tools fail if the setup is wrong. Here are the most common issues. 
 "Codex is not installed" 
 Check: 
 You ran npm i -g @openai/codex . 
 You are using a supported shell and runtime. 
 The binary is on your path. 
 "I cannot sign in" 
 Check: 
 Your ChatGPT account has the right plan. 
 Your workspace allows Codex local or cloud use. 
 You are signing in with the correct account. 
 "Windows is behaving badly" 
 The CLI docs say Windows support is experimental. If you are on Windows, the best supported path is to use WSL for the CLI or use the Codex app where appropriate. 
 "Cloud task cannot see my repo" 
 Check: 
 The GitHub connector is installed. 
 The repository is allowed in the connector. 
 Your organization admin has enabled Codex cloud. 
 You are using a GitHub-hosted repository. 
 "Codex will not browse the internet" 
 That is expected by default in cloud mode. Ask your admin whether internet access has been intentionally restricted. 
 "The result is technically correct but not what I wanted" 
 Usually this means the prompt was under-specified. Tighten: 
 The target file or feature. 
 The acceptance criteria. 
 The constraints. 
 The expected output format. 
 Section 13: FAQ 
 Is Codex a chat model? 
 Not exactly. It is a coding agent and product surface built to work on repositories, tests, code review, and multi-step software tasks. 
 Can I use Codex without switching tools all the time? 
 Yes. That is one of its strengths. You can use the CLI, IDE extension, or Codex app depending on your workflow. 
 Do I need the cloud features? 
 No. Many individual users will get value from the local CLI or IDE extension alone. Cloud tasks become more valuable as soon as you want background execution, parallelism, or automated review. 
 Is Codex only for professional engineers? 
 No, but it is most useful when the user can evaluate code changes and understand a repository. It is a developer tool first. 
 Is Codex the same as GPT-5.4? 
 No. GPT-5.4 is a model. Codex is the coding product/workflow. Codex may use different models depending on the surface and configuration. 
 What is the safest way to start? 
 Use the CLI or IDE extension in a small repo change, keep the approval mode conservative, and review every diff before merging. 
 Section 14: When NOT to Use Codex 
 Most of this handbook is affirmative — Codex is good at this, Codex fits here, here is how to set it up. That framing risks creating the impression that Codex is the right tool for any coding-adjacent task. It is not. The fastest way to lose team trust in an AI coding tool is to push it into work it is bad at. The following is an honest list of where Codex is a poor fit today. 
 Tasks With No Reviewable Output 
 Codex's value depends on a human reviewing the diff, the test result, or the explanation. If the task produces something nobody will check — a one-off script that touches production data, an exploratory query whose result drives a decision before anyone reads the SQL — the AI's confidence becomes the only quality gate. That is a bad position to be in regardless of model quality. Either add a review step or do the task yourself. 
 Highly Novel Architecture Decisions 
 Codex is good at applying patterns. It is much weaker at choosing which pattern fits a problem the team has not solved before. Expect it to confidently generate plausible-but-wrong architecture for genuinely new domains: a new pricing model, a new auth boundary, a new event-sourcing scheme. Use it to prototype options, not to decide between them. 
 Work That Crosses Org Boundaries 
 Codex sees the repository it has access to. It does not see the cross-team contracts, the deprecation calendar in the platform team's roadmap, the half-finished migration in another repo, or the political reasons one approach is off-limits. For changes that span multiple teams or services, Codex can implement individual pieces, but a human still needs to own the cross-cutting plan. 
 Anything Touching Live Production State 
 Codex Cloud sandboxes are good. They are not a substitute for human approval before a production change. Database migrations, infrastructure-as-code that mutates real resources, secret rotation, customer-data scripts — these need a human in the approval path even if Codex wrote the diff. The fact that Codex can run commands does not mean it should run those commands. 
 Compliance- and Safety-Critical Code 
 Code that lives inside a regulated boundary (payments, medical, security primitives, model-evaluation harnesses for safety) has higher review and provenance requirements than typical product code. Codex output is fine as a starting draft, but the review burden is the same as for any third-party-authored code, which usually means the speed advantage shrinks substantially. Plan for that or keep these areas Codex-free. 
 Tasks Where the Real Bottleneck Is Knowledge, Not Typing 
 If the team is stuck because nobody understands the legacy system, the failing test, or the weird customer report, generating more code rarely helps. Codex can accelerate the implementation once you know what to do. It cannot replace the discovery and design conversation that should happen first. Teams that skip the discovery step and go straight to "ask Codex" tend to ship the wrong thing fast. 
 Anything Where Hallucinations Have High Cost 
 GPT-5.5 dropped hallucination rates by roughly 60% versus prior generations, which is a real improvement. It is not zero. Tasks where a confident-but-wrong output causes real damage — generating regulatory citations, copying API contract details from a doc the model hasn't actually read, asserting facts about an unfamiliar third-party library — still need the same skepticism you would apply to any AI output. Use search-grounded workflows or human verification for these. 
 Quick Heuristic 
 If you can answer all four of these with "yes," Codex is likely a good fit: 
 Can the output be reviewed by someone who would catch a mistake? 
 Is the task a known pattern, not a novel architecture decision? 
 Is the blast radius local to one repository or service? 
 Is the cost of a bad output bounded (e.g., a failed test, a reverted commit) rather than unbounded (e.g., production data loss, regulatory exposure)? 
 If any of those are "no," either restructure the task to make them "yes" or keep the work outside Codex. 
 Section 15: Final Recommendations 
 If you are rolling Codex out to new users, I would keep the guidance very simple: 
 Start with the CLI or IDE extension. 
 Use one small task to learn the tool. 
 Review every change before merging. 
 Move to cloud tasks only after users trust the local workflow. 
 For teams, separate user access from admin access. 
 Re-check pricing whenever your plan or workspace changes. 
 Codex is most valuable when it is treated as a disciplined engineering tool rather than a novelty. If you give it real code, clear constraints, and a review culture, it can accelerate the boring parts of software development and make bigger tasks easier to break down. 
 The LUNARTECH Fellowship: Bridging Academia and Industry 
 Addressing the growing disconnect between academic theory and the practical demands of the tech industry, the LUNARTECH Fellowship was created to bridge this talent gap. 
 Far too often, aspiring engineers are caught in the “no experience, no job” loop, graduating with theoretical knowledge but unprepared for the messy reality of production systems. 
 To combat this systemic issue and halt the resulting brain drain, the Fellowship invests heavily in promising individuals, offering a transformative environment that prioritizes hands-on experience, mentorship, and real-world engineering over traditional degrees. 
 This 6-month, remote-first apprenticeship serves as an immersive odyssey from aspiring talent to AI trailblazer. Rather than paying to learn in isolation, Fellows work on live, high-stakes AI and data products alongside experienced senior engineers and founders. By tackling actual engineering challenges and building a concrete portfolio of production-ready work, participants acquire the job-ready skills needed to thrive in today’s competitive landscape. 
 If you are ready to break the loop and accelerate your career, you can explore these opportunities and start your journey here: https://www.lunartech.ai/our-careers . 
 Master Your Career: The AI Engineering Handbook 
 For those ready to transition from theory to practice, we have developed The AI Engineering Handbook: How to Start a Career and Excel as an AI Engineer . This comprehensive guide provides a step-by-step roadmap for mastering the skills necessary to thrive in the transformative world of AI in 2026. 
 Whether you are a developer looking to break into a competitive field or a professional seeking to future-proof your career, this handbook offers proven strategies and actionable insights that have already empowered countless individuals to secure high-impact roles. 
 Inside, you will explore real-world industry workflows, advanced architecting methods, and expert perspectives from leaders at companies like NVIDIA, Microsoft, and OpenAI. From discovering the technology behind ChatGPT to learning how to architect systems that transform research into world-changing products, this eBook is your ultimate companion for career acceleration. You can download your free copy and start mastering the future of AI. 
 Section 16: Source References 
 Official OpenAI sources used for this handbook: 
 Introducing GPT-5.5 (OpenAI) 
 Using Codex with your ChatGPT plan 
 Flexible pricing for the Enterprise, Edu, and Business plans 
 All models 
 OpenAI API models overview 
 GPT-5-Codex model 
 GPT-5.2-Codex model 
 codex-mini-latest model 
 Codex use cases 
 Claude overview 
 GitHub Copilot documentation 
 Codex enterprise admin setup 
 Codex IDE extension docs 
 Codex – OpenAI's coding agent (VS Code Marketplace listing) 
 Codex web (cloud) docs 
 Codex CLI docs 
 Codex CLI command-line reference 
 Codex CLI features 
 Codex quickstart 
 Using Codex with your ChatGPT plan (Help Center) 
 Press coverage of the GPT-5.5 release referenced in Section 2 and Section 11 : 
 OpenAI releases GPT-5.5, bringing company one step closer to an AI 'super app' (TechCrunch) 
 OpenAI launches GPT-5.5, calling it "a new class of intelligence" (The New Stack) 
 OpenAI's GPT-5.5 benchmarks show a 60% hallucination drop and coding skills that rival senior engineers (Startup Fortune) 
 Appendix A: 30-60-90 Day Adoption Plan 
 If you are introducing Codex to a team, the fastest way to create trust is to phase adoption instead of rolling it out as a big-bang change. A staged plan also helps you discover where the real friction lives: authentication, permissions, prompt quality, review habits, or budget assumptions. 
 First 30 Days: Prove Value 
 In the first month, the goal is not maximum usage. The goal is repeatable wins. 
 Recommended actions: 
 Pick one or two engineers who are comfortable trying new tools. 
 Restrict usage to small, low-risk tasks such as bug fixes, test generation, and documentation updates. 
 Standardize a short prompt template so every request includes task, context, constraints, and expected output. 
 Require human review for every change. 
 Track the time it takes to go from prompt to merged diff. 
 What you should learn in this phase: 
 Does Codex understand your codebase structure? 
 Are the diffs reviewable? 
 Does the approval flow slow people down in a useful way, or in a frustrating way? 
 Which classes of tasks work well, and which ones need more guidance? 
 If the first month is noisy, do not blame the model first. Usually the issue is task scope, missing context, or unclear acceptance criteria. 
 Days 31-60: Expand Carefully 
 Once the tool has proven itself on a handful of tasks, expand to a broader pilot group. 
 Recommended actions: 
 Add more developers from different parts of the stack. 
 Include at least one person who is skeptical, because their feedback will reveal weak spots. 
 Try the app, CLI, and IDE extension in parallel so people can choose the workflow that matches their habits. 
 Introduce Codex cloud for one or two background tasks or pull request reviews. 
 Start documenting prompts that worked well, including examples of high-quality follow-up instructions. 
 What you should learn in this phase: 
 Which surfaces are actually sticky for the team? 
 Where does Codex save the most time? 
 Do people trust the output enough to delegate real work? 
 Are you seeing the same mistakes repeatedly? 
 At this stage, your internal documentation matters. A short "how we use Codex here" page is often more useful than another technical deep dive. 
 Days 61-90: Operationalize 
 After about three months, your objective should shift from experimentation to operating practice. 
 Recommended actions: 
 Assign ownership for workspace settings, GitHub connector setup, and model access. 
 Define which tasks should stay local and which can go to cloud sandboxes. 
 Document your review standards for Codex-generated diffs. 
 Set budget expectations with the team so no one is surprised by token-heavy tasks. 
 Add Codex to onboarding for new engineers, starting with one simple flow. 
 What good looks like at this stage: 
 New hires can use Codex on day one. 
 Team members know when to reach for Codex and when to use a different workflow. 
 Admins can answer access and pricing questions quickly. 
 The organization has a realistic picture of the tool's strengths and limits. 
 A Practical Onboarding Script 
 If you need a ready-made orientation for a new user, use this: 
 "Install the CLI or extension." 
 "Open a repository you know well." 
 "Ask Codex to make one small, safe change." 
 "Review the diff line by line." 
 "Run the tests." 
 "Ask Codex to explain what it changed and why." 
 "Repeat with a slightly larger task." 
 That sequence teaches the core loop: context, task, change, review, verify. Once a user understands that loop, the rest of the product family becomes much easier to adopt. 
 Appendix B: Glossary 
 Terms used in this handbook, in alphabetical order. The list is intentionally narrow — only terms that appear in the body and are likely to be unfamiliar to a non-engineering reader (procurement, security, leadership) are defined here. 
 Agent / agentic workflow. Software that can take a goal, plan steps, take actions (read files, run commands, call APIs), observe the result, and iterate. Codex is an agentic coding workflow; a chatbot is not. 
 Approval mode. A Codex setting that controls how much the agent can do without asking. Stricter modes prompt the human before running shell commands or modifying files; permissive modes let the agent work uninterrupted. 
 CLI. Command-line interface. The Codex CLI is the terminal-based version of Codex, installed via npm i -g @openai/codex . 
 Codex Cloud. The hosted, sandboxed execution mode for Codex. Tasks run in isolated environments with the repo and finish with a reviewable diff. 
 GDPval. A benchmark that scores models on their ability to produce well-specified knowledge-work output across 44 occupations. Used in Section 11 as a general-capability signal. 
 GitHub Connector. The integration that lets Codex Cloud access GitHub repositories. Required for cloud tasks; uses short-lived, least-privilege tokens. 
 MCP (Model Context Protocol). An open protocol for connecting models to external data sources and tools. Codex CLI supports MCP, which lets it pull in data from systems beyond the repo. 
 MRCR v2. A long-context retrieval benchmark that measures whether the model can find and use information across very large input windows. The 1M-token version is cited in the GPT-5.5 section because it predicts behavior on repository-scale tasks. 
 OSWorld-Verified. A benchmark that measures whether a model can operate a real desktop computer environment to complete tasks. A direct proxy for agentic and computer-use workloads. 
 PR (pull request). A proposed change to a code repository, hosted on GitHub or similar platforms, where reviewers approve before the change merges. 
 RBAC (role-based access control). A permission model where users are assigned to roles, and roles have specific permissions. Used by Codex workspace admins to control who can do what. 
 SCIM (System for Cross-domain Identity Management). A standard for syncing users and groups from an identity provider (Okta, Entra ID, etc.) into another system. Codex supports SCIM-based group sync for enterprise. 
 Subagent. A Codex CLI feature that splits a task across multiple parallel agent runs, each handling a piece of the work. 
 Tau2-bench Telecom. A benchmark for complex customer-service workflows with tool use. Cited as a signal for tool-use reliability and policy adherence. 
 Terminal-Bench 2.0. A coding benchmark focused on terminal-driven workflows, including long-context retrieval and computer use. The closest public proxy for Codex CLI workloads. 
 Worktree. A git feature that lets multiple branches be checked out simultaneously in different directories. The Codex app uses worktrees so multiple agents can work in parallel without stepping on each other. 
 WSL (Windows Subsystem for Linux). A compatibility layer that runs Linux binaries natively on Windows. The recommended environment for Codex CLI on Windows, since direct Windows support is experimental. 
 Appendix C: Admin Security Checklist 
 For workspace admins setting up Codex for an enterprise. This checklist condenses Section 8 into actionable items. Run through it before broad rollout, then revisit quarterly. 
 Access 
 [ ] Decide whether Codex Local, Codex Cloud, or both are enabled at the workspace level. 
 [ ] Create separate RBAC groups for Codex Admins (policy and governance) and Codex Users (day-to-day developers). Avoid mixing the two. 
 [ ] Sync user and group membership from your identity provider via SCIM rather than managing users by hand. 
 [ ] Set a sensible default role for new workspace members. Do not default to admin. 
 GitHub integration 
 [ ] Install the ChatGPT GitHub Connector against the correct GitHub organization. 
 [ ] Allowlist only the repositories Codex Cloud needs. Do not grant org-wide access by default. 
 [ ] Verify Codex respects existing branch protection rules on protected branches before enabling cloud tasks against them. 
 [ ] Confirm the GitHub App tokens Codex uses are short-lived and least-privilege. 
 Network and runtime 
 [ ] Confirm Codex Cloud runs with no internet access by default. This is the secure default; verify it is on. 
 [ ] If a workflow requires internet access, define an explicit allowlist (dependency registries, trusted sites) and limit allowed HTTP methods. 
 [ ] Document which model surfaces are approved for sensitive code (often: local CLI yes, cloud no for the most sensitive repositories). 
 Data and review 
 [ ] Document the team's review standard for Codex-generated diffs. At minimum: a human approves every merge. 
 [ ] Confirm logging and audit trails are configured for Codex actions (model used, prompts, files changed) per your compliance requirements. 
 [ ] Define which classes of data are off-limits to Codex (PII, customer data, secrets) and how those boundaries are enforced. 
 [ ] Establish an incident playbook for the case where Codex generates or commits something it should not have. 
 Budget and ongoing operations 
 [ ] Set a per-workspace token budget or alert threshold so unexpected spend is caught early. 
 [ ] Pick a default model per task type (e.g., Codex-mini for routine review, GPT-5.5 for repository-wide refactors) and document the choice. 
 [ ] Review the Codex pricing page quarterly. The rate card has changed in the past and will change again. 
 [ ] Re-run this checklist when (a) a major model release lands, (b) the workspace expands to a new team, or (c) Codex adds a new surface or capability. 
 Appendix D: Changelog 
 A short, append-only log of substantive revisions to this handbook. Each entry lists the version, date, and a one-line summary of what changed. 
 v1.3 — 2026-04-30. Made the Table of Contents clickable. Added a new Prerequisites section after the TOC. Restructured the early sections: merged the old "Quick Start" and "How to Set Up Codex" into a single Section 4 walkthrough using a self-contained codex-demo repo readers build themselves. Slimmed Section 2 by moving the GPT-5.5 benchmark deep dive to a new Section 11 (Model Specs and Benchmarks). Added per-surface hyperlinks to Section 3 . Rewrote Section 5 (How to Use Codex Effectively) with bad/good examples for every tip and a definition of "bounded change." Rewrote the "Measure What Matters" subsection with concrete computation methods for each metric. Added worked, runnable examples to every workflow in Section 10 . Renumbered downstream sections accordingly. 
 v1.2 — 2026-04-25. Added Appendix E (Working with Codex in VS Code), a detailed step-by-step guide covering the three VS Code entry points — the extension, the CLI in the integrated terminal, and browser Codex at chatgpt.com/codex — with setup instructions, a decision matrix, a combined-workflow pattern, and VS Code-specific troubleshooting. Added a forward-pointer in the setup section. 
 v1.1 — 2026-04-25. Added GPT-5.5 / GPT-5.5 Pro coverage in Section 2 and Section 7 . Added executive summary, comparison matrix in the model-comparison section, worked cost example, "When NOT to use Codex" in Section 14 . Added Appendix B (Glossary), Appendix C (Admin Security Checklist), Appendix D (Changelog). Added version stamp and author line. Press coverage sources for GPT-5.5 added in Section 16 . 
 v1.0 — Initial release. Original Codex onboarding handbook covering surfaces, setup, usage, model comparison, pricing, security, team practices, workflows, troubleshooting, FAQ, and the 30-60-90 day adoption plan. 
 Appendix E: Working with Codex in VS Code 
 This appendix is a focused, step-by-step guide to using Codex inside Visual Studio Code (and its forks, Cursor and Windsurf). 
 VS Code is the most common starting surface for new Codex users, and the workflow has three distinct entry points that can be used independently or together. This guide covers each one, when to pick it, and how the three combine into a single fluid workflow. 
 E.1 Why VS Code Is the Recommended Starting Surface 
 Most teams start with VS Code rather than the standalone Codex app or pure CLI for a few practical reasons: 
 The editor is already where engineers spend their day. Adding Codex does not require a context switch. 
 The extension surface area is small and reviewable. Engineers can try it on a single file before adopting it more broadly. 
 VS Code's integrated terminal makes the CLI a one-keystroke experience, so the extension and CLI can be combined without leaving the editor. 
 Cursor and Windsurf, the most popular VS Code forks, both run the same Codex extension. A team that standardizes on the VS Code workflow does not have to retrain people if some engineers prefer a fork. 
 The downside of starting in VS Code is that you do not get parallel-task management or worktree support out of the box — those are stronger in the Codex app. For most individual contributors, that is not a meaningful loss in the first month. 
 E.2 The Three Entry Points 
 Codex shows up in VS Code in three distinct ways, and they are easy to confuse. Each is a separate piece of software with its own install and its own auth handshake, even though they all sign in with the same ChatGPT account. 
 The Codex VS Code extension — a sidebar UI inside VS Code itself. Installed from the VS Code Marketplace. Best for in-flow editing, quick questions about the open file, and short bounded tasks. 
 The Codex CLI, run inside VS Code's integrated terminal — the command-line agent ( codex ) running in the terminal pane that is already attached to your VS Code workspace. Best for multi-step agentic tasks, scripted runs, and anything where you want explicit approval gates. 
 Browser Codex at chatgpt.com/codex — the web interface to Codex Cloud, where tasks run in isolated sandboxes against your GitHub repository. Best for background work, parallel tasks, and PR-style review. 
 These are not alternatives to each other in the sense that you must pick one. They are three workflows that target different kinds of work, and most experienced Codex users have all three set up. 
 E.3 Setting Up the Codex VS Code Extension 
 This is the entry point most new users meet first. 
 Install 
 There are two install paths: 
 Open the VS Code Marketplace, search for "Codex" or "ChatGPT", and install the extension published by openai . The marketplace identifier is openai.chatgpt . 
 From a terminal, run: 
 code --install-extension openai.chatgpt The CLI install path is useful for scripted dev-environment provisioning, dotfiles repos, and onboarding scripts that bring a new machine up to a known baseline. 
 Sign in 
 After install, the Codex panel appears in the right sidebar. The first time you open it, you will be prompted to sign in. You have two options: 
 Sign in with ChatGPT. Recommended for individuals on Plus, Pro, Business, or Enterprise/Edu plans. Usage is charged against your plan's included Codex credits. 
 Sign in with an API key. Used when you want metered API billing instead of plan-based usage, or when your workspace policy requires it. Get the key from the OpenAI developer console, then paste it into the extension's auth prompt. 
 If both options are visible and you are unsure which to pick, default to ChatGPT sign-in. It is the path that exercises the same plan-included usage that the rest of your team is on, which makes cost behavior predictable. 
 First-run sanity check 
 Once signed in, do a five-minute sanity check before relying on the extension for real work: 
 Open a small repository you know well. 
 Open the Codex panel in the right sidebar. 
 Ask a question about the open file (e.g., "What does this function do?") and confirm the answer matches what you already know. 
 Ask for a small change (e.g., "Add a docstring to this function") and confirm a reviewable diff appears. 
 Apply the change, run your tests, and revert if needed. 
 If any of those steps fails, fix the auth or install before going further. Trying to debug the extension on a real task is much harder than debugging it on a known-good toy task. 
 Platform notes 
 macOS and Linux are first-class. The extension and the underlying CLI both work natively. 
 Windows is experimental for the CLI. The extension itself works, but if you also want to run the CLI inside VS Code's integrated terminal, OpenAI recommends using a WSL workspace. Open the folder via "Reopen in WSL" before installing the CLI. 
 Cursor and Windsurf run the same extension. Watch for visual or shortcut conflicts with the fork's built-in AI features — see E.9 for specifics. 
 E.4 Setting Up the Codex CLI Inside VS Code's Integrated Terminal 
 The CLI is the second entry point. It runs as a normal command-line tool, but inside VS Code's integrated terminal it picks up the active workspace folder automatically, which makes it feel like a native part of the editor. 
 Install the CLI 
 From any terminal, including VS Code's integrated terminal: 
 npm i -g @openai/codex This installs the codex binary globally. Confirm by running: 
 codex --version If the command is not found, the most common cause is that npm's global bin directory is not on your PATH. Either fix the PATH or use a Node version manager (nvm, fnm, volta) that handles it for you. 
 Open the integrated terminal in VS Code 
 Three ways to open it, pick whichever matches your habits: 
 The View menu → Terminal. 
 The keyboard shortcut Ctrl+ ** (backtick) on Windows/Linux, **⌃ on macOS. 
 The Command Palette: Terminal: Create New Terminal . 
 The integrated terminal inherits the active workspace folder as its working directory, which means codex launched from there immediately sees the right repo. 
 Run Codex 
 In the terminal, navigate to the repo (if you are not already there) and run: 
 codex The first time you run it, you will go through the same auth flow as the extension — sign in with ChatGPT or paste an API key. 
 Pick an approval mode 
 The CLI supports several approval modes that govern how much Codex can do without explicit confirmation. For new users, start with the strictest mode (asks before every shell command and every file change), then loosen it once you trust the workflow on your repo. The relevant modes and how to toggle them are described in the CLI docs linked in Section 16 . 
 Where the CLI beats the extension 
 Multi-step agentic runs that need to read several files, run tests, iterate, and report. 
 Anything you want to script or invoke from a package.json script, a Makefile, or a CI step. 
 Subagent decomposition (the CLI explicitly supports splitting a task across multiple parallel agent runs). 
 MCP-connected tools and custom data sources. 
 Cloud task launching from the terminal, when you do not want to leave the keyboard. 
 E.5 Setting Up Browser Codex (chatgpt.com/codex) 
 The third entry point lives outside VS Code but is essential for the full workflow because it is how you launch and monitor cloud tasks. 
 Open browser Codex 
 Navigate to chatgpt.com/codex . You will need to be signed into the same ChatGPT account you used for the extension and CLI. If you are part of an enterprise workspace, your admin must have enabled Codex Cloud at the workspace level — see Section 8 . 
 You can also reach Codex through the sidebar in regular ChatGPT. The browser surface exposes two main verbs: 
 Code — assign a coding task. Codex spins up a sandbox preloaded with your repository and produces a reviewable diff. 
 Ask — ask a question about your codebase without changing any code. 
 Connect a GitHub repository 
 Cloud tasks need a GitHub-hosted repository. Connect it once: 
 Open environment settings at chatgpt.com/codex. 
 Connect your GitHub account through the ChatGPT GitHub Connector. 
 Grant access to the specific repositories you want Codex to be able to use. Do not grant org-wide access by default — see Appendix C for the security checklist. 
 Confirm the connector shows the repo as available. 
 Launch a task 
 From the Codex web interface: 
 Pick the repository and (optionally) the branch. 
 Type a prompt describing the task. Be specific — "Add input validation to the /users POST endpoint and update the matching tests" beats "Improve the API." 
 Click Code (or Ask for a non-mutating question). 
 Watch the live logs as Codex works, or close the tab and let it run in the background. 
 When it finishes, review the diff. From there you can request changes, accept the result, or open a pull request. 
 Delegate from a GitHub PR comment 
 A useful shortcut: in any PR on a connected repo, you can post a comment that tags @codex with an instruction (for example, "@codex review this PR for security issues and missing tests"). Codex will pick up the request and respond on the PR. This requires being signed into ChatGPT in the same browser. 
 Why the browser surface matters even if you live in VS Code 
 Cloud tasks decouple Codex from your local machine. You can launch a long-running task from the browser, close the laptop, and come back to the diff later. The extension and CLI cannot do this — they need an open VS Code instance to run. 
 E.6 When to Pick Which Entry Point 
 The three entry points overlap, which causes confusion. This table makes the choice mechanical. 
 Situation Best entry point Why 
 Quick edit on the file you have open Extension Lowest friction, no context switch 
 "What does this function do?" Extension Right-sidebar Q&A is faster than typing it into a terminal 
 Multi-file refactor with tests CLI in integrated terminal Better at multi-step agentic work and approvals 
 Anything you want to script or wire into a Makefile CLI Only the CLI is invokable from other scripts 
 Long-running task you want to leave running Browser (cloud) Decoupled from your laptop 
 Parallel tasks (e.g., three independent fixes at once) Browser (cloud) Cloud sandboxes run in parallel without local resource contention 
 PR review on a teammate's pull request Browser, via @codex mention in PR Lives where the review actually happens 
 Anything touching production credentials or live infra None of the above without explicit human approval See Section 14 
 The pattern that emerges: extension for in-flow editing, CLI for serious local agentic work, browser for anything you want offloaded or shared with the team. 
 E.7 The Combined VS Code Workflow 
 The three entry points are most powerful when used together. A representative day looks like this. 
 Morning, in VS Code: 
 Open the repo. The Codex extension panel is in the right sidebar. 
 Use the extension to ask questions about an unfamiliar module before you touch it. 
 Make small in-line edits — single-function changes, docstrings, type fixes — using the extension's diff-apply flow. 
 Mid-morning, in the integrated terminal: 
 Open the integrated terminal (Ctrl+`). 
 Run codex and start a multi-file task with explicit approval mode: "Refactor the auth middleware to use the new session interface. List the files you intend to touch first, then make the changes in the smallest commits possible." 
 Approve each shell command and each diff as Codex requests them. 
 Run the test suite when Codex finishes. 
 Afternoon, in the browser: 
 While you are reviewing the morning's CLI changes, open chatgpt.com/codex in another tab. 
 Launch a cloud task: "Add OpenAPI annotations to every public endpoint in the /api/v2 directory." This will take a while. 
 Switch back to VS Code and keep working. The cloud task runs in its own sandbox. 
 When the cloud task finishes, review the diff in the browser, request any tweaks, and open a PR. 
 End of day, on GitHub: 
 Tag @codex on a teammate's open PR with "review for correctness and missing tests." The result lands as a comment overnight. 
 The point of the combined workflow is that each entry point is doing what it is best at simultaneously. The extension keeps in-flow editing fast, the CLI handles local agentic work where you want approval control, and the cloud handles long-running and parallel tasks without consuming your local machine. 
 E.8 VS Code-Specific Tips 
 These are small tips that compound over time once you use Codex daily inside VS Code. 
 Sidebar position. The Codex panel defaults to the right sidebar. If you also have GitHub PR review or another panel there, drag Codex to the secondary side or to a panel-bottom dock — whichever keeps it visible without stealing space from the editor. 
 Keybindings. Bind the most-used Codex commands (open panel, new task, accept diff) to keyboard shortcuts via VS Code's Preferences: Open Keyboard Shortcuts . Reach for the keyboard, not the mouse. 
 Settings sync. If you use VS Code's Settings Sync, the Codex extension's settings travel with you to other machines. Auth state does not — you sign in again on each machine. This is the right behavior; do not work around it. 
 Multi-root workspaces. The extension scopes to the active workspace folder. If you open a multi-root workspace, switch the active folder explicitly before asking Codex to make changes, otherwise it may operate against the wrong root. 
 Integrated terminal profiles. If you use multiple terminal profiles (PowerShell, bash, WSL), set the WSL profile as default on Windows so codex from the integrated terminal always lands in the supported environment. 
 Source control panel. After Codex applies a change, the VS Code Source Control panel shows the diff. Review there before committing — it gives you the same context as a git diff without leaving the editor. 
 Don't fight the approval mode. New users often loosen approvals to "auto" too quickly because the prompts feel slow. Resist that for the first week. The approvals are how you build a mental model of what Codex actually does in your repo. 
 One Codex panel per VS Code window. Avoid running the extension and the CLI in the same workspace simultaneously on the same task — they can both touch files and you will get confused about which one made which change. 
 E.9 Cursor and Windsurf 
 The Codex extension explicitly supports Cursor and Windsurf, the two most popular VS Code forks. The install and sign-in flow is identical. The notes worth knowing: 
 Avoid double-AI confusion. Cursor and Windsurf both ship their own AI features. Engineers using them with Codex sometimes accidentally invoke the fork's built-in AI when they meant to invoke Codex, or vice versa. Pick a primary tool for editing and use the other only when its specific strengths matter. 
 Auth is independent. The Codex extension's ChatGPT sign-in is separate from Cursor's or Windsurf's own model accounts. Your Codex usage is billed against your ChatGPT plan; Cursor/Windsurf usage against theirs. 
 Keybinding conflicts. Cursor in particular has heavily customized AI-related keybindings. Audit your bindings after installing the Codex extension to make sure both surfaces are reachable. 
 Settings sync caveat. Cursor and Windsurf have their own settings sync that diverges from upstream VS Code. Codex extension settings may sync within Cursor or Windsurf separately from your VS Code installs. 
 For pure Codex-first teams, vanilla VS Code is the simplest baseline. For teams that already standardized on Cursor or Windsurf for other reasons, the Codex extension is a clean addition rather than a replacement. 
 E.10 Troubleshooting VS Code Specifically 
 The general troubleshooting list is in Section 12 . The issues below are specific to running Codex inside VS Code. 
 Extension installs but sidebar panel never appears 
 Reload the window (Command Palette → "Developer: Reload Window"). If that does not fix it, check the Output panel, switch the dropdown to "Codex", and look for the actual error. The most common causes are a corporate proxy blocking the extension's auth handshake, or a conflicting older version of the extension still installed. 
 "Sign in" keeps looping back to the sign-in prompt 
 This usually means the redirect from the browser auth flow did not reach the extension. Try signing out completely, closing all VS Code windows, then reopening and signing in fresh. On Windows, verify your default browser is one VS Code can open via the OS handler. 
 codex command not found in the integrated terminal 
 The CLI's npm global bin directory is not on PATH. The fastest fix on macOS/Linux is to add $(npm bin -g) to your shell profile ( .zshrc , .bashrc ). On Windows, restart VS Code after the npm install so the integrated terminal picks up the updated PATH, or switch to a WSL terminal where the install is already on PATH. 
 Cloud task says "no repository connected" even though you connected one 
 Verify in chatgpt.com/codex environment settings that the specific repository is in the allowlist. The GitHub Connector grants per-repository access; granting access to the org alone is not enough. Also confirm your workspace admin has enabled Codex Cloud — individual users cannot enable it themselves. 
 Extension and CLI both editing the same file at the same time 
 Stop one of them. They do not coordinate, and you will get conflicting edits. The simplest discipline: pick one entry point per task, switch between tasks rather than trying to combine within a task. 
 Extension feels slower than the CLI for the same prompt 
 Often this is because the extension is using a different default model than your CLI configuration. Check both for the active model — the model picker in the extension panel, and codex --help or the relevant config file for the CLI. 
 Windows behavior is generally bad 
 Switch to a WSL workspace. OpenAI's own docs call out Windows as experimental for the CLI; the WSL path is the supported one and clears most issues at once. 
 Ready to Excel as an AI Engineer? 
 As we conclude this exploration of intelligent healthcare, it’s clear that the future belongs to those who can bridge the gap between groundbreaking research and real-world utility. If you are inspired to lead this transformation, we invite you to download our flagship resource, The AI Engineering Handbook . Authored by Tatev Aslanyan, a pioneering AI engineer and co-founder of LUNARTECH, this guide is designed to help you navigate the highly competitive landscape of AI engineering, providing you with the step-by-step roadmap and industry workflows needed to build world-changing products. 
 Empower yourself with the same strategies used by AI trailblazers at the world's most innovative tech companies. By mastering these production-ready skills, you won't just keep pace with the hyper-connected world — you will help define it. Get started today by downloading your eBook here: https://www.lunartech.ai/download/the-ai-engineering-handbook . 
 About LunarTech Lab 
 “Real AI. Real ROI. Delivered by Engineers — Not Slide Decks.” 
 LunarTech Lab is a deep-tech innovation partner specializing in AI, data science, and digital transformation – from healthcare to energy, telecom, and beyond. 
 We build real systems, not PowerPoint strategies. Our teams combine clinical, data, and engineering expertise to design AI that’s measurable, compliant, and production-ready. We’re vendor-neutral, globally distributed, and grounded in real AI and engineering, not hype. Our model blends Western European and North American leadership with high-performance technical teams offering world-class delivery at 70% of the Big Four’s cost. 
 How We Work — From Scratch, in Four Phases 
 1. Discovery Sprint (2–4 Weeks): We start with data and ROI – not assumptions to define what’s worth building and what’s not and how much it will cost you. 
 2. Pilot / Proof of Concept (8–12 Weeks): We prototype the core idea – fast, focused, and measurable. 
 This phase tests models, integrations, and real-world ROI before scaling. 
 3. Full Implementation (6–12 Months): We industrialize the solution – secure data pipelines, production-grade models, full compliance (HIPAA, MDR, GDPR), and knowledge transfer. 
 4. Managed Services (Ongoing): We maintain, retrain, and evolve the AI models for lasting ROI. Quarterly reviews ensure that performance improves with time, not decays. As we own LunarTech Academy , we also build customised training to ensure clients tech team can continue working without us. 
 Every project is designed from scratch , integrating clinical knowledge, data engineering, and applied AI research. 
 Why LunarTech Lab? 
 LunarTech Lab bridges the gap between strategy and real engineering, where most competitors fall short. Traditional consultancies, including the Big Four, sell frameworks, not systems – expensive slide decks with little execution. 
 We offer the same strategic clarity, but it’s delivered by engineers and data scientists who build what they design, at about 70% of the cost. Cloud vendors push their own stacks and lock clients in. LunarTech is vendor-neutral: we choose what’s best for your goals, ensuring freedom and long-term flexibility. 
 Outsourcing firms execute without innovation. LunarTech works like an R&D partner, building from first principles, co-creating IP, and delivering measurable ROI. 
 From discovery to deployment, we combine strategy, science, and engineering, with one promise: We don’t sell slides. We deliver intelligence that works. 
 Stay Connected with LunarTech 
 Follow LunarTech Lab on LunarTech NewsLetter and LinkedIn , where innovation meets real engineering. You’ll get insights, project stories, and industry breakthroughs from the front lines of applied AI and data science.
```

---

## 2. Learn Command Line Interface (CLI) Development with Dart: From Zero to a Fully Published Developer Tool

- 日期: 2026-05-08 18:54
- 链接: https://www.freecodecamp.org/news/learn-command-line-interface-cli-development-with-dart-from-zero-to-a-fully-published-developer-tool/

```
Most developers spend a significant portion of their day in the terminal. They run flutter build , push with git , manage packages with dart pub , and orchestrate pipelines from the command line. Every one of those tools is a CLI, or command line interface: a program that lives in the terminal and responds to text commands. 
 Yet most developers have never built one. 
 That's a missed opportunity. CLI tools are one of the most practical things a developer can ship. They automate repetitive workflows, standardise processes across teams, and, when published, become tangible artifacts that the developer community can discover, install, and use. 
 In this handbook, you'll go from zero to building a fully distributed Dart CLI tool. We'll start with the fundamentals – how CLIs work, how Dart receives and processes terminal input, and the core syntax you need to know. Then we'll build three progressively complex CLIs, starting with the basics and finishing with a real-world API request runner. Finally, we will cover every distribution path available, from pub.dev to compiled binaries, Homebrew taps, Docker, and local team activation. 
 By the end of the guide, you'll understand both how to build a CLI tool in Dart as well as how to ship it so other developers can actually use it. 
 Table of Contents 
 Prerequisites 
 What is a CLI and Why Should You Build One? 
 CLI Syntax Anatomy 
 How Dart Receives Terminal Input 
 Core CLI Concepts in Dart 
 stdout, stderr, and stdin 
 Exit Codes 
 Environment Variables 
 File and Directory Operations 
 Running External Processes 
 Platform Detection 
 Async in CLI 
 Setting Up Your Dart CLI Project 
 CLI 1 — Hello CLI: The Fundamentals 
 CLI 2 — dart_todo: A Terminal Task Manager 
 Introducing the args Package 
 Building dart_todo 
 CLI 3 — dart_http: A Lightweight API Request Runner 
 Building dart_http 
 Adding Color and Polish to Your CLI 
 Testing Your CLI Tool 
 Deploying and Distributing Your CLI 
 Mode 1: pub.dev — Public Package Distribution 
 Mode 2: Local Path Activation 
 Mode 3: Compiled Binary via GitHub Releases 
 Mode 4: Homebrew Tap 
 Mode 5: Docker 
 Choosing the Right Distribution Mode 
 Conclusion 
 Prerequisites 
 Before starting, you should have: 
 Dart SDK installed ( dart --version should work in your terminal) 
 Basic familiarity with Dart syntax 
 Comfort with the terminal and running commands 
 A pub.dev account (for the publishing section) 
 A GitHub account (for the binary distribution section) 
 What is a CLI and Why Should You Build One? 
 A CLI (or Command Line Interface ) is a program you interact with entirely through text commands in a terminal, rather than through buttons and screens in a graphical interface. 
 Many of the tools you likely already rely on as a developer are CLI tools: 
 flutter build apk
git commit -m "fix: auth flow"
dart pub get
npm install Flutter, Git, Dart, npm – all CLIs. You are already a CLI user every single day. This article is about becoming a CLI builder. 
 There are three strong reasons to build CLI tools as a developer: 
 Automating repetitive work: Anything you type more than twice a week is a candidate for automation. Generating boilerplate folder structures, running sequences of commands, scaffolding files, checking environments before a build a CLI turns a seven-step manual process into a single command. 
 Standardising team workflows: Instead of a README that says "run these commands in this order," you ship one command that does all of it – consistently, every time, with no room for human error or a missed step. 
 Building and publishing tooling. A published Dart CLI package is a tangible artifact. It shows up on pub.dev, gets installed and used by other developers, and communicates real engineering depth in a way that a portfolio or resume cannot. 
 CLI Syntax Anatomy 
 Before writing a single line of code, it helps to understand the structure of a CLI command. Every command follows a consistent pattern: 
 tool [subcommand] [arguments] [options/flags] Breaking down a real example: 
 flutter build apk --release --obfuscate
│ │ │ │
tool sub arg flags Tool — the program itself ( flutter , dart , git ) 
 Subcommand — the action being performed ( build , run , pub ) 
 Arguments — what the action operates on ( apk , main.dart , a filename) 
 Flags and Options — modifiers that change behaviour 
 There are two types of options: 
 --release # Boolean flag — either present or absent

--output=build/app # Key-value option — name and a value
-v # Short flag — single hyphen, single character This is the anatomy your CLIs will follow. Understanding it before writing any code means you will design your commands intentionally rather than stumbling into structure by accident. 
 How Dart Receives Terminal Input 
 In Dart, everything the user types after your tool name is passed into your program through the main function: 
 void main(List<String> args) {
 print(args);
} Run it: 
 dart run bin/mytool.dart hello world --name=Seyi
# [hello, world, --name=Seyi] That List<String> args is just a list of strings. Each word or flag the user typed becomes an element in that list. Everything else you build on top of a CLI subcommands, flags, validation — is ultimately just processing this list. 
 Core CLI Concepts in Dart 
 Before building anything, there's a set of foundational concepts that every CLI developer needs to understand. These are the building blocks that everything else sits on top of. 
 stdout, stderr, and stdin 
 Most developers use print() for all output when they start building CLIs. That works for learning but it's incorrect in production. 
 There are two separate output streams in a terminal program: 
 stdout — regular output, meant for the user 
 stderr — error output, meant for diagnostic messages and failures 
 import 'dart:io';

void main(List<String> args) {
 if (args.isEmpty) {
 stderr.writeln('Error: no arguments provided');
 exit(1);
 }

 stdout.writeln('Processing: ${args[0]}');
} Keeping these separate matters because users can redirect stdout to a file without errors polluting it: 
 dart run bin/tool.dart > output.txt
# Errors still appear in the terminal
# Normal output goes cleanly to the file Tools like git , flutter , and curl all do this correctly. Your CLI should too. 
 stdin is the third stream — reading input from the user interactively at runtime: 
 import 'dart:io';

void main() {
 stdout.write('Enter your name: ');
 final name = stdin.readLineSync();

 if (name == null || name.trim().isEmpty) {
 stderr.writeln('Error: no name provided');
 exit(1);
 }

 stdout.writeln('Hello, $name!');
} stdout.write (without ln ) keeps the cursor on the same line so the user types right after the prompt. stdin.readLineSync() blocks until the user presses Enter and returns the typed string, or null if the stream closes unexpectedly. Always handle the null case. 
 Exit Codes 
 Every program returns an exit code when it finishes. This is how the shell – and any script or CI system calling your tool – knows whether it succeeded or failed. 
 import 'dart:io';

void main(List<String> args) {
 if (args.isEmpty) {
 stderr.writeln('Error: please provide an argument');
 exit(1); // failure
 }

 stdout.writeln('Done');
 exit(0); // success — also the default if you don't call exit()
} The conventions are: 
 0 — success 
 1 — general failure 
 2 — incorrect usage (wrong arguments, missing flags) 
 Exit codes are critical when your CLI is called inside shell scripts or GitHub Actions workflows. A non-zero exit code stops a pipeline immediately. That's exactly the behaviour you want from a quality gate or a validation step. 
 Environment Variables 
 Your CLI can read environment variables set in the user's shell: 
 import 'dart:io';

void main() {
 final token = Platform.environment['API_TOKEN'];

 if (token == null) {
 stderr.writeln('Error: API_TOKEN environment variable is not set');
 exit(1);
 }

 stdout.writeln('Token found — proceeding...');
} Set it in the terminal and run: 
 export API_TOKEN=mytoken123
dart run bin/tool.dart
# Token found — proceeding... This pattern is essential for CLI tools that interact with APIs, cloud services, or CI environments where credentials should never be hardcoded. 
 File and Directory Operations 
 Many CLI tools read from or write to the file system. Dart's dart:io library covers everything you need: 
 import 'dart:io';

void main(List<String> args) {
 if (args.isEmpty) {
 stderr.writeln('Usage: tool <filename>');
 exit(2);
 }

 final file = File(args[0]);

 if (!file.existsSync()) {
 stderr.writeln('Error: "${args[0]}" not found');
 exit(1);
 }

 final contents = file.readAsStringSync();
 stdout.writeln(contents);

 final output = File('output.txt');
 output.writeAsStringSync('Processed:\n$contents');
 stdout.writeln('Written to output.txt');
} Working with directories: 
 import 'dart:io';

void main() {
 // Where the command was run from
 final cwd = Directory.current.path;
 stdout.writeln('Working directory: $cwd');

 // Create a directory relative to current location
 final dir = Directory('$cwd/generated');

 if (!dir.existsSync()) {
 dir.createSync(recursive: true);
 stdout.writeln('Created: ${dir.path}');
 } else {
 stdout.writeln('Already exists: ${dir.path}');
 }
} The recursive: true flag on createSync means it creates all intermediate directories — equivalent to mkdir -p in bash. 
 Running External Processes 
 One of the most powerful things a CLI can do is call other programs. Your Dart CLI can run git , flutter , dart , or any shell command programmatically: 
 import 'dart:io';

void main() async {
 // Run a command and wait for it to finish
 final result = await Process.run('dart', ['pub', 'get']);

 stdout.write(result.stdout);

 if (result.exitCode != 0) {
 stderr.write(result.stderr);
 exit(result.exitCode);
 }

 stdout.writeln('Dependencies installed successfully');
} For long-running commands where you want output to stream live as it happens: 
 import 'dart:io';

void main() async {
 final process = await Process.start('flutter', ['build', 'apk']);

 // Pipe output directly to the terminal in real time
 process.stdout.pipe(stdout);
 process.stderr.pipe(stderr);

 final exitCode = await process.exitCode;
 exit(exitCode);
} Process.run — waits for completion, returns all output at once. Use for short commands. 
 Process.start — streams output live as it arrives. Use for long-running commands where the user needs to see progress. 
 Platform Detection 
 Sometimes your CLI needs to behave differently depending on the operating system it is running on: 
 import 'dart:io';

void main() {
 if (Platform.isWindows) {
 stdout.writeln('Running on Windows');
 } else if (Platform.isMacOS) {
 stdout.writeln('Running on macOS');
 } else if (Platform.isLinux) {
 stdout.writeln('Running on Linux');
 }

 // Useful for path handling across operating systems
 stdout.writeln(Platform.pathSeparator); // \ on Windows, / elsewhere
 stdout.writeln(Platform.operatingSystem); // 'macos', 'linux', 'windows'
} This matters when your CLI creates files, resolves paths, or calls shell commands that differ between operating systems. 
 Async in CLI 
 Dart CLIs support async/await natively. Any main function can be made async: 
 import 'dart:io';

void main() async {
 stdout.writeln('Starting...');

 await Future.delayed(const Duration(seconds: 1)); // simulating async work

 stdout.writeln('Done');
} Any operation involving file I/O, HTTP requests, or spawning processes will be asynchronous. Get comfortable with async main functions early — you'll use them constantly. 
 Setting Up Your Dart CLI Project 
 Create a new Dart console project: 
 dart create -t console my_cli_tool
cd my_cli_tool This generates a clean structure: 
 my_cli_tool/
 bin/
 my_cli_tool.dart ← entry point
 lib/ ← shared library code
 test/ ← tests
 pubspec.yaml
 README.md The bin/ directory is where your executable entry point lives. The lib/ directory is where you put everything else — commands, utilities, models — that bin/ imports and uses. 
 Open pubspec.yaml . You'll need to add an executables block before publishing: 
 name: my_cli_tool
description: A sample CLI tool built with Dart
version: 1.0.0

environment:
 sdk: '>=3.0.0 <4.0.0'

executables:
 my_cli_tool: my_cli_tool # executable name: bin file name

dependencies:
 args: ^2.4.2

dev_dependencies:
 lints: ^3.0.0
 test: ^1.24.0 The executables block is what makes dart pub global activate my_cli_tool work. It tells Dart which script in bin/ to expose as a runnable command after installation. 
 CLI 1 — Hello CLI: The Fundamentals 
 This first CLI uses pure Dart — no packages. The goal is to get comfortable with args, subcommands, input validation, and exit codes before introducing any external dependencies. 
 Replace the contents of bin/my_cli_tool.dart : 
 import 'dart:io';

void main(List<String> args) {
 if (args.isEmpty) {
 printHelp();
 exit(0);
 }

 final command = args[0];

 switch (command) {
 case 'greet':
 handleGreet(args.sublist(1));
 case 'time':
 handleTime();
 case 'echo':
 handleEcho(args.sublist(1));
 case 'help':
 printHelp();
 default:
 stderr.writeln('Unknown command: "$command"');
 stderr.writeln('Run "mytool help" to see available commands.');
 exit(1);
 }
}

void handleGreet(List<String> args) {
 if (args.isEmpty) {
 stderr.writeln('Usage: mytool greet <name>');
 exit(2);
 }

 final name = args[0];
 stdout.writeln('Hello, $name! Welcome to your first Dart CLI.');
}

void handleTime() {
 final now = DateTime.now();
 stdout.writeln(
 'Current time: ${now.hour.toString().padLeft(2, '0')}:'
 '${now.minute.toString().padLeft(2, '0')}:'
 '${now.second.toString().padLeft(2, '0')}',
 );
}

void handleEcho(List<String> args) {
 if (args.isEmpty) {
 stderr.writeln('Usage: mytool echo <message>');
 exit(2);
 }

 stdout.writeln(args.join(' '));
}

void printHelp() {
 stdout.writeln('''
mytool — a simple Dart CLI

Usage:
 mytool <command> [arguments]

Commands:
 greet <name> Greet someone by name
 time Show the current time
 echo <message> Echo a message back to the terminal
 help Show this help message

Examples:
 mytool greet Seyi
 mytool echo "Hello from the terminal"
 mytool time
 ''');
} Run it: 
 dart run bin/my_cli_tool.dart help

dart run bin/my_cli_tool.dart greet Seyi
# Hello, Seyi! Welcome to your first Dart CLI.

dart run bin/my_cli_tool.dart time
# Current time: 14:32:10

dart run bin/my_cli_tool.dart echo "Dart CLIs are powerful"
# Dart CLIs are powerful

dart run bin/my_cli_tool.dart unknown
# Unknown command: "unknown"
# Run "mytool help" to see available commands. Three things this CLI demonstrates that are worth internalising: 
 Subcommands are just a switch on args[0] . The pattern is simple and scalable — add a new case to add a new command. 
 args.sublist(1) passes remaining args to the handler. When greet receives ['greet', 'Seyi'] , it calls handleGreet(['Seyi']) — clean and isolated. 
 Every error path has a message and a non-zero exit code. The user always knows what went wrong and what to do next. 
 CLI 2 — dart_todo: A Terminal Task Manager 
 This CLI introduces the args package, JSON file persistence, and structured terminal output. It's meaningfully more complex than CLI 1 and reflects real patterns you will use in production tools. 
 Introducing the args Package 
 Manually parsing List<String> args works for simple cases, but breaks down quickly when you add flags like --priority=high , boolean options like --done , or commands with multiple optional arguments. 
 The args package handles all of that cleanly. 
 Add it to your pubspec.yaml : 
 dependencies:
 args: ^2.4.2 Run: 
 dart pub get The core concept in args is the ArgParser . You define what your CLI accepts, and args handles parsing, validation, and generating help text automatically: 
 import 'package:args/args.dart';

void main(List<String> arguments) {
 final parser = ArgParser()
 ..addCommand('add')
 ..addCommand('list')
 ..addFlag('help', abbr: 'h', negatable: false);

 final results = parser.parse(arguments);

 if (results['help'] as bool) {
 print(parser.usage);
 return;
 }
} For more complex CLIs with subcommands that each have their own flags, use ArgParser per command: 
 final parser = ArgParser();

final addCommand = ArgParser()
 ..addOption('priority', abbr: 'p', defaultsTo: 'normal');

parser.addCommand('add', addCommand); Building dart_todo 
 Create a fresh project: 
 dart create -t console dart_todo
cd dart_todo Update pubspec.yaml : 
 name: dart_todo
description: A terminal task manager built with Dart
version: 1.0.0

environment:
 sdk: '>=3.0.0 <4.0.0'

executables:
 dart_todo: dart_todo

dependencies:
 args: ^2.4.2

dev_dependencies:
 lints: ^3.0.0
 test: ^1.24.0 Run dart pub get . 
 Create the folder structure: 
 dart_todo/
 bin/
 dart_todo.dart
 lib/
 models/
 task.dart
 storage/
 task_storage.dart
 commands/
 add_command.dart
 list_command.dart
 complete_command.dart
 delete_command.dart
 clear_command.dart
 pubspec.yaml Step 1 — The Task Model ( lib/models/task.dart ) 
 class Task {
 final int id;
 final String title;
 final String priority;
 final bool isComplete;
 final DateTime createdAt;

 Task({
 required this.id,
 required this.title,
 required this.priority,
 this.isComplete = false,
 required this.createdAt,
 });

 Task copyWith({bool? isComplete}) {
 return Task(
 id: id,
 title: title,
 priority: priority,
 isComplete: isComplete ?? this.isComplete,
 createdAt: createdAt,
 );
 }

 Map<String, dynamic> toJson() => {
 'id': id,
 'title': title,
 'priority': priority,
 'isComplete': isComplete,
 'createdAt': createdAt.toIso8601String(),
 };

 factory Task.fromJson(Map<String, dynamic> json) => Task(
 id: json['id'] as int,
 title: json['title'] as String,
 priority: json['priority'] as String,
 isComplete: json['isComplete'] as bool,
 createdAt: DateTime.parse(json['createdAt'] as String),
 );
} Step 2 — Storage ( lib/storage/task_storage.dart ) 
 This class handles reading and writing tasks to a local JSON file so they persist between CLI runs: 
 import 'dart:convert';
import 'dart:io';

import '../models/task.dart';

class TaskStorage {
 static final _file = File(
 '${Platform.environment['HOME'] ?? Directory.current.path}/.dart_todo.json',
 );

 static List<Task> loadAll() {
 if (!_file.existsSync()) return [];

 try {
 final content = _file.readAsStringSync();
 final List<dynamic> json = jsonDecode(content) as List<dynamic>;
 return json
 .map((e) => Task.fromJson(e as Map<String, dynamic>))
 .toList();
 } catch (_) {
 return [];
 }
 }

 static void saveAll(List<Task> tasks) {
 final json = jsonEncode(tasks.map((t) => t.toJson()).toList());
 _file.writeAsStringSync(json);
 }
} Tasks are stored in a hidden JSON file in the user's home directory — a common pattern for CLI tools that need lightweight local persistence. 
 Step 3 — Commands 
 lib/commands/add_command.dart : 
 import 'dart:io';

import '../models/task.dart';
import '../storage/task_storage.dart';

void runAdd(List<String> args, String priority) {
 if (args.isEmpty) {
 stderr.writeln('Usage: dart_todo add <title> [--priority=high|normal|low]');
 exit(2);
 }

 final title = args.join(' ');
 final tasks = TaskStorage.loadAll();

 final newTask = Task(
 id: tasks.isEmpty ? 1 : tasks.last.id + 1,
 title: title,
 priority: priority,
 createdAt: DateTime.now(),
 );

 tasks.add(newTask);
 TaskStorage.saveAll(tasks);

 stdout.writeln('Added task #\({newTask.id}: "\)title" [$priority]');
} lib/commands/list_command.dart : 
 import 'dart:io';

import '../storage/task_storage.dart';

void runList() {
 final tasks = TaskStorage.loadAll();

 if (tasks.isEmpty) {
 stdout.writeln('No tasks yet. Add one with: dart_todo add <title>');
 return;
 }

 stdout.writeln('');
 stdout.writeln(' ID Status Priority Title');
 stdout.writeln(' ─── ────────── ───────── ────────────────────────');

 for (final task in tasks) {
 final status = task.isComplete ? 'done ' : 'pending';
 final id = task.id.toString().padRight(4);
 final priority = task.priority.padRight(9);
 stdout.writeln(' \(id \)status \(priority \){task.title}');
 }

 stdout.writeln('');
} lib/commands/complete_command.dart : 
 import 'dart:io';

import '../storage/task_storage.dart';

void runComplete(List<String> args) {
 if (args.isEmpty) {
 stderr.writeln('Usage: dart_todo complete <id>');
 exit(2);
 }

 final id = int.tryParse(args[0]);
 if (id == null) {
 stderr.writeln('Error: "${args[0]}" is not a valid task ID');
 exit(1);
 }

 final tasks = TaskStorage.loadAll();
 final index = tasks.indexWhere((t) => t.id == id);

 if (index == -1) {
 stderr.writeln('Error: No task found with ID $id');
 exit(1);
 }

 if (tasks[index].isComplete) {
 stdout.writeln('Task #$id is already complete.');
 return;
 }

 tasks[index] = tasks[index].copyWith(isComplete: true);
 TaskStorage.saveAll(tasks);

 stdout.writeln('Task #\(id marked as complete: "\){tasks[index].title}"');
} lib/commands/delete_command.dart : 
 import 'dart:io';

import '../storage/task_storage.dart';

void runDelete(List<String> args) {
 if (args.isEmpty) {
 stderr.writeln('Usage: dart_todo delete <id>');
 exit(2);
 }

 final id = int.tryParse(args[0]);
 if (id == null) {
 stderr.writeln('Error: "${args[0]}" is not a valid task ID');
 exit(1);
 }

 final tasks = TaskStorage.loadAll();
 final index = tasks.indexWhere((t) => t.id == id);

 if (index == -1) {
 stderr.writeln('Error: No task found with ID $id');
 exit(1);
 }

 final title = tasks[index].title;
 tasks.removeAt(index);
 TaskStorage.saveAll(tasks);

 stdout.writeln('Deleted task #\(id: "\)title"');
} lib/commands/clear_command.dart : 
 import 'dart:io';

import '../storage/task_storage.dart';

void runClear() {
 stdout.write('Are you sure you want to delete all tasks? (y/N): ');
 final input = stdin.readLineSync()?.trim().toLowerCase();

 if (input != 'y') {
 stdout.writeln('Cancelled.');
 return;
 }

 TaskStorage.saveAll([]);
 stdout.writeln('All tasks cleared.');
} Step 4 — Entry Point ( bin/dart_todo.dart ) 
 import 'dart:io';

import 'package:args/args.dart';

import '../lib/commands/add_command.dart';
import '../lib/commands/clear_command.dart';
import '../lib/commands/complete_command.dart';
import '../lib/commands/delete_command.dart';
import '../lib/commands/list_command.dart';

void main(List<String> arguments) {
 final parser = ArgParser();

 // Add subcommand parsers
 final addParser = ArgParser()
 ..addOption(
 'priority',
 abbr: 'p',
 defaultsTo: 'normal',
 allowed: ['high', 'normal', 'low'],
 help: 'Task priority level',
 );

 parser
 ..addCommand('add', addParser)
 ..addCommand('list')
 ..addCommand('complete')
 ..addCommand('delete')
 ..addCommand('clear')
 ..addFlag('help', abbr: 'h', negatable: false, help: 'Show help');

 ArgResults results;

 try {
 results = parser.parse(arguments);
 } catch (e) {
 stderr.writeln('Error: $e');
 stderr.writeln(parser.usage);
 exit(2);
 }

 if (results['help'] as bool || results.command == null) {
 printHelp(parser);
 exit(0);
 }

 final command = results.command!;

 switch (command.name) {
 case 'add':
 runAdd(command.rest, command['priority'] as String);
 case 'list':
 runList();
 case 'complete':
 runComplete(command.rest);
 case 'delete':
 runDelete(command.rest);
 case 'clear':
 runClear();
 default:
 stderr.writeln('Unknown command: "${command.name}"');
 exit(1);
 }
}

void printHelp(ArgParser parser) {
 stdout.writeln('''
dart_todo — a terminal task manager

Usage:
 dart_todo <command> [arguments]

Commands:
 add <title> Add a new task
 -p, --priority Priority: high, normal, low (default: normal)
 list List all tasks
 complete <id> Mark a task as complete
 delete <id> Delete a task
 clear Delete all tasks

Examples:
 dart_todo add "Write the CLI article" --priority=high
 dart_todo list
 dart_todo complete 1
 dart_todo delete 2
 dart_todo clear
 ''');
} Run it: 
 dart run bin/dart_todo.dart add "Write the CLI article" --priority=high
# Added task #1: "Write the CLI article" [high]

dart run bin/dart_todo.dart add "Review PR comments"
# Added task #2: "Review PR comments" [normal]

dart run bin/dart_todo.dart list
# ID Status Priority Title
# ─── ────────── ───────── ────────────────────────
# 1 ⬜ pending high Write the CLI article
# 2 ⬜ pending normal Review PR comments

dart run bin/dart_todo.dart complete 1
# Task #1 marked as complete: "Write the CLI article"

dart run bin/dart_todo.dart delete 2
# Deleted task #2: "Review PR comments" dart_todo demonstrates the patterns that form the backbone of almost every real CLI tool — argument parsing with args , JSON persistence, interactive prompts, structured output, and clean error handling across every command. 
 CLI 3 — dart_http: A Lightweight API Request Runner 
 This is the most complex CLI in this article – and the most immediately useful. dart_http lets developers make HTTP requests directly from the terminal, with pretty-printed JSON responses, response metadata, header support, and the ability to save responses to a file. 
 dart_http get https://jsonplaceholder.typicode.com/users/1
dart_http post https://jsonplaceholder.typicode.com/posts --body='{"title":"Hello"}'
dart_http get https://jsonplaceholder.typicode.com/users --save=users.json
dart_http get https://api.example.com/me --header="Authorization: Bearer mytoken" Building dart_http 
 Create the project: 
 dart create -t console dart_http
cd dart_http Update pubspec.yaml : 
 name: dart_http
description: A lightweight API request runner for the terminal
version: 1.0.0

environment:
 sdk: '>=3.0.0 <4.0.0'

executables:
 dart_http: dart_http

dependencies:
 args: ^2.4.2
 http: ^1.2.1

dev_dependencies:
 lints: ^3.0.0
 test: ^1.24.0 Run dart pub get . 
 Project structure: 
 dart_http/
 bin/
 dart_http.dart
 lib/
 runner/
 request_runner.dart
 printer/
 response_printer.dart
 utils/
 headers_parser.dart
 pubspec.yaml Step 1 — Headers Parser ( lib/utils/headers_parser.dart ) 
 Map<String, String> parseHeaders(List<String> rawHeaders) {
 final headers = <String, String>{};

 for (final header in rawHeaders) {
 final index = header.indexOf(':');
 if (index == -1) continue;

 final key = header.substring(0, index).trim();
 final value = header.substring(index + 1).trim();
 headers[key] = value;
 }

 return headers;
} Step 2 — Response Printer ( lib/printer/response_printer.dart ) 
 import 'dart:convert';
import 'dart:io';

void printResponse({
 required int statusCode,
 required String body,
 required int durationMs,
 required int bodyBytes,
}) {
 final statusLabel = _statusLabel(statusCode);
 final size = _formatSize(bodyBytes);

 stdout.writeln('');
 stdout.writeln('\(statusLabel | \){durationMs}ms | $size');
 stdout.writeln('─' * 50);

 try {
 final decoded = jsonDecode(body);
 const encoder = JsonEncoder.withIndent(' ');
 stdout.writeln(encoder.convert(decoded));
 } catch (_) {
 // Not JSON — print as plain text
 stdout.writeln(body);
 }

 stdout.writeln('');
}

String _statusLabel(int code) {
 if (code >= 200 && code < 300) return '✅ $code';
 if (code >= 300 && code < 400) return '↪️ $code';
 if (code >= 400 && code < 500) return '❌ $code';
 return '$code';
}

String _formatSize(int bytes) {
 if (bytes < 1024) return '${bytes}b';
 if (bytes < 1024 * 1024) return '${(bytes / 1024).toStringAsFixed(1)}kb';
 return '${(bytes / (1024 * 1024)).toStringAsFixed(1)}mb';
} Step 3 — Request Runner ( lib/runner/request_runner.dart ) 
 import 'dart:io';

import 'package:http/http.dart' as http;

import '../printer/response_printer.dart';

Future<void> runRequest({
 required String method,
 required String url,
 required Map<String, String> headers,
 String? body,
 String? saveToFile,
}) async {
 final uri = Uri.tryParse(url);

 if (uri == null) {
 stderr.writeln('Error: "$url" is not a valid URL');
 exit(1);
 }

 stdout.writeln('→ \({method.toUpperCase()} \)url');

 http.Response response;
 final stopwatch = Stopwatch()..start();

 try {
 switch (method.toLowerCase()) {
 case 'get':
 response = await http.get(uri, headers: headers);
 case 'post':
 response = await http.post(uri, headers: headers, body: body);
 case 'put':
 response = await http.put(uri, headers: headers, body: body);
 case 'patch':
 response = await http.patch(uri, headers: headers, body: body);
 case 'delete':
 response = await http.delete(uri, headers: headers);
 default:
 stderr.writeln('Error: unsupported method "$method"');
 exit(2);
 }
 } catch (e) {
 stderr.writeln('Error: request failed — $e');
 exit(1);
 }

 stopwatch.stop();

 printResponse(
 statusCode: response.statusCode,
 body: response.body,
 durationMs: stopwatch.elapsedMilliseconds,
 bodyBytes: response.bodyBytes.length,
 );

 if (saveToFile != null) {
 final file = File(saveToFile);
 file.writeAsStringSync(response.body);
 stdout.writeln('Response saved to $saveToFile');
 }
} Step 4 — Entry Point ( bin/dart_http.dart ) 
 import 'dart:io';

import 'package:args/args.dart';

import '../lib/runner/request_runner.dart';
import '../lib/utils/headers_parser.dart';

void main(List<String> arguments) async {
 final parser = ArgParser();

 for (final method in ['get', 'post', 'put', 'patch', 'delete']) {
 final commandParser = ArgParser()
 ..addMultiOption('header', abbr: 'H', help: 'Request header (repeatable)')
 ..addOption('body', abbr: 'b', help: 'Request body (for POST/PUT/PATCH)')
 ..addOption('save', abbr: 's', help: 'Save response body to a file');

 parser.addCommand(method, commandParser);
 }

 parser.addFlag('help', abbr: 'h', negatable: false, help: 'Show help');

 ArgResults results;

 try {
 results = parser.parse(arguments);
 } catch (e) {
 stderr.writeln('Error: $e');
 printHelp();
 exit(2);
 }

 if (results['help'] as bool || results.command == null) {
 printHelp();
 exit(0);
 }

 final command = results.command!;
 final method = command.name!;
 final rest = command.rest;

 if (rest.isEmpty) {
 stderr.writeln('Error: please provide a URL');
 stderr.writeln('Usage: dart_http $method <url>');
 exit(2);
 }

 final url = rest[0];
 final rawHeaders = command['header'] as List<String>;
 final body = command['body'] as String?;
 final saveToFile = command['save'] as String?;

 final headers = parseHeaders(rawHeaders);

 // Default Content-Type for requests with a body
 if (body != null && !headers.containsKey('Content-Type')) {
 headers['Content-Type'] = 'application/json';
 }

 await runRequest(
 method: method,
 url: url,
 headers: headers,
 body: body,
 saveToFile: saveToFile,
 );
}

void printHelp() {
 stdout.writeln('''
dart_http — a lightweight API request runner

Usage:
 dart_http <method> <url> [options]

Methods:
 get Send a GET request
 post Send a POST request
 put Send a PUT request
 patch Send a PATCH request
 delete Send a DELETE request

Options:
 -H, --header Add a request header (repeatable)
 -b, --body Request body (JSON string)
 -s, --save Save response body to a file
 -h, --help Show this help message

Examples:
 dart_http get https://jsonplaceholder.typicode.com/users
 dart_http get https://api.example.com/me --header="Authorization: Bearer token"
 dart_http post https://api.example.com/posts --body=\'{"title":"Hello"}\'
 dart_http get https://api.example.com/users --save=users.json
 ''');
} Run it: 
 dart run bin/dart_http.dart get https://jsonplaceholder.typicode.com/users/1

# → GET https://jsonplaceholder.typicode.com/users/1
# 200 | 87ms | 510b
# ──────────────────────────────────────────────────
# {
# "id": 1,
# "name": "Leanne Graham",
# "username": "Bret",
# "email": "Sincere@april.biz"
# }

dart run bin/dart_http.dart get https://jsonplaceholder.typicode.com/users --save=users.json
# → GET https://jsonplaceholder.typicode.com/users
# 200 | 143ms | 5.3kb
# ──────────────────────────────────────────────────
# [ ... ]
# Response saved to users.json

dart run bin/dart_http.dart post https://jsonplaceholder.typicode.com/posts \
 --body='{"title":"Hello from dart_http","userId":1}'
# → POST https://jsonplaceholder.typicode.com/posts
# 201 | 312ms | 72b Adding Color and Polish to Your CLI 
 The CLIs above are functional, but terminal output can be made significantly more readable with color. The ansi_styles package provides ANSI escape code support for coloring text in the terminal. 
 Add it to pubspec.yaml : 
 dependencies:
 ansi_styles: ^0.3.0 Using it: 
 import 'package:ansi_styles/ansi_styles.dart';

stdout.writeln(AnsiStyles.green('✅ Success'));
stdout.writeln(AnsiStyles.red('❌ Error: something went wrong'));
stdout.writeln(AnsiStyles.yellow('⚠️ Warning: check your config'));
stdout.writeln(AnsiStyles.bold('dart_http — API request runner'));
stdout.writeln(AnsiStyles.cyan('→ GET https://api.example.com/users')); Apply color intentionally and consistently: 
 Green — success states, completed operations 
 Red — errors and failures 
 Yellow — warnings and non-blocking issues 
 Cyan — informational output, URLs, paths 
 Bold — headers, tool names, important values 
 Avoid coloring everything. Color loses meaning when it is everywhere. Use it to draw the user's eye to what actually matters. 
 Testing Your CLI Tool 
 CLI tools are testable, and they should be tested. The most reliable approach is to test the logic inside your commands directly — not the terminal output formatting, but the behaviour. 
 Add test to your dev dependencies if it's not already there: 
 dev_dependencies:
 test: ^1.24.0 Testing command logic: 
 import 'package:test/test.dart';

import '../lib/models/task.dart';

void main() {
 group('Task model', () {
 test('copyWith updates isComplete correctly', () {
 final task = Task(
 id: 1,
 title: 'Write tests',
 priority: 'high',
 createdAt: DateTime.now(),
 );

 final completed = task.copyWith(isComplete: true);

 expect(completed.isComplete, isTrue);
 expect(completed.title, equals('Write tests'));
 expect(completed.id, equals(1));
 });

 test('toJson and fromJson round-trips correctly', () {
 final task = Task(
 id: 2,
 title: 'Ship the tool',
 priority: 'normal',
 createdAt: DateTime.parse('2025-01-01T00:00:00.000'),
 );

 final json = task.toJson();
 final restored = Task.fromJson(json);

 expect(restored.id, equals(task.id));
 expect(restored.title, equals(task.title));
 expect(restored.priority, equals(task.priority));
 });
 });
} Testing the headers parser: 
 import 'package:test/test.dart';

import '../lib/utils/headers_parser.dart';

void main() {
 group('parseHeaders', () {
 test('parses a single header correctly', () {
 final result = parseHeaders(['Authorization: Bearer mytoken']);
 expect(result['Authorization'], equals('Bearer mytoken'));
 });

 test('parses multiple headers', () {
 final result = parseHeaders([
 'Authorization: Bearer token',
 'Accept: application/json',
 ]);
 expect(result.length, equals(2));
 expect(result['Accept'], equals('application/json'));
 });

 test('ignores malformed headers without a colon', () {
 final result = parseHeaders(['malformed-header']);
 expect(result.isEmpty, isTrue);
 });
 });
} Run your tests: 
 dart test Deploying and Distributing Your CLI 
 Building a CLI tool is half the work. Getting it into the hands of developers is the other half. There are five distribution paths available, each suited to a different use case. 
 Mode 1: pub.dev — Public Package Distribution 
 Publishing to pub.dev makes your tool installable by anyone in the Dart and Flutter community with a single command. 
 Prepare your package: 
 Your pubspec.yaml needs to be complete: 
 name: dart_http
description: A lightweight API request runner for Dart developers.
version: 1.0.0
homepage: https://github.com/yourname/dart_http

environment:
 sdk: '>=3.0.0 <4.0.0'

executables:
 dart_http: dart_http The executables block is critical. It tells pub.dev which script in bin/ to expose as a runnable command. 
 You also need: 
 README.md — what the tool does, how to install it, usage examples 
 CHANGELOG.md — version history 
 LICENSE — an open source license (MIT is standard) 
 Validate before publishing: 
 dart pub publish --dry-run This runs all validation checks without actually publishing. Fix any warnings before proceeding. 
 Publish: 
 dart pub publish You will be prompted to authenticate with your pub.dev account. Once published, your tool is available globally: 
 dart pub global activate dart_http
dart_http get https://api.example.com/users Mode 2: Local Path Activation 
 For internal team tools that you don't want to publish publicly, activate directly from a local or cloned repository: 
 dart pub global activate --source path /path/to/dart_http Any developer on the team clones the repo and runs this command once. The tool is then available globally in their terminal without needing a pub.dev publish. 
 This is the right distribution mode for: 
 Internal company tooling 
 Tools that depend on private packages 
 Work-in-progress tools shared within a team before a public release 
 Mode 3: Compiled Binary via GitHub Releases 
 Dart can compile to a self-contained native executable — no Dart SDK required on the target machine. This makes your tool accessible to developers outside the Dart ecosystem. 
 Compile: 
 # macOS
dart compile exe bin/dart_http.dart -o dist/dart_http-macos

# Linux
dart compile exe bin/dart_http.dart -o dist/dart_http-linux

# Windows
dart compile exe bin/dart_http.dart -o dist/dart_http-windows.exe The compiled binary is fully self-contained. Copy it to any machine and run it — no Dart installation needed. 
 Automate with GitHub Actions: 
 Create .github/workflows/release.yml : 
 name: Release

on:
 push:
 tags:
 - 'v*'

jobs:
 build:
 strategy:
 matrix:
 os: [ubuntu-latest, macos-latest, windows-latest]
 runs-on: ${{ matrix.os }}

 steps:
 - uses: actions/checkout@v3

 - uses: dart-lang/setup-dart@v1
 with:
 sdk: stable

 - name: Install dependencies
 run: dart pub get

 - name: Compile binary
 run: |
 mkdir -p dist
 dart compile exe bin/dart_http.dart -o dist/dart_http-${{ runner.os }}

 - name: Upload binary to release
 uses: softprops/action-gh-release@v1
 with:
 files: dist/dart_http-${{ runner.os }}
 env:
 GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} Every time you push a version tag ( v1.0.0 ), GitHub Actions compiles binaries for all three platforms and attaches them to the GitHub Release automatically. 
 Write an install script: 
 #!/usr/bin/env bash
set -euo pipefail

VERSION="1.0.0"
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
BINARY="dart_http-$OS"
INSTALL_DIR="/usr/local/bin"

curl -L "https://github.com/yourname/dart_http/releases/download/v\(VERSION/\)BINARY" \
 -o "$INSTALL_DIR/dart_http"

chmod +x "$INSTALL_DIR/dart_http"
echo "dart_http installed successfully" Developers install it with: 
 curl -fsSL https://raw.githubusercontent.com/yourname/dart_http/main/install.sh | bash Mode 4: Homebrew Tap 
 Homebrew is the standard package manager for macOS and is widely used on Linux. A Homebrew tap makes your tool installable with brew install — the most familiar installation pattern for macOS developers. 
 Create your tap repository: 
 Create a new GitHub repository named homebrew-tools (the homebrew- prefix is required by Homebrew's naming convention). 
 Write the formula: 
 Create Formula/dart_http.rb in that repository: 
 class DartHttp < Formula
 desc "A lightweight API request runner for the terminal"
 homepage "https://github.com/yourname/dart_http"
 version "1.0.0"

 on_macos do
 url "https://github.com/yourname/dart_http/releases/download/v1.0.0/dart_http-macOS"
 sha256 "YOUR_SHA256_HASH_HERE"
 end

 on_linux do
 url "https://github.com/yourname/dart_http/releases/download/v1.0.0/dart_http-Linux"
 sha256 "YOUR_SHA256_HASH_HERE"
 end

 def install
 bin.install "dart_http-#{OS.mac? ? 'macOS' : 'Linux'}" => "dart_http"
 end

 test do
 system "#{bin}/dart_http", "--help"
 end
end Generate the SHA256 hash for each binary: 
 shasum -a 256 dist/dart_http-macOS Install from the tap: 
 brew tap yourname/tools
brew install dart_http When you release a new version, update the url and sha256 values in the formula and push the change. Users run brew upgrade dart_http to update. 
 Mode 5: Docker 
 Docker distribution is best suited for CI environments, teams that standardise on containers, or tools with complex dependencies. 
 Write a Dockerfile: 
 FROM dart:stable AS build

WORKDIR /app
COPY pubspec.* ./
RUN dart pub get

COPY . .
RUN dart compile exe bin/dart_http.dart -o /app/dart_http

FROM debian:stable-slim
COPY --from=build /app/dart_http /usr/local/bin/dart_http

ENTRYPOINT ["dart_http"] This uses a multi-stage build: the first stage compiles the binary using the Dart SDK image, and the second stage copies only the binary into a minimal Debian image. The final image has no Dart SDK — just the compiled binary. 
 Build and run: 
 docker build -t dart_http .
docker run dart_http get https://jsonplaceholder.typicode.com/users/1 Publish to Docker Hub: 
 docker tag dart_http yourname/dart_http:1.0.0
docker push yourname/dart_http:1.0.0 Users can then run your tool without installing anything locally: 
 docker run yourname/dart_http get https://api.example.com/users Choosing the Right Distribution Mode 
 Mode Best for Dart SDK required 
 pub.dev Public Dart/Flutter developer tools Yes 
 Local path activation Internal team tools, pre-release builds Yes 
 Compiled binary Language-agnostic tools, broad adoption No 
 Homebrew tap macOS/Linux developer tools No 
 Docker CI environments, complex dependencies No 
 For most tools, the practical recommendation is: 
 Start with pub.dev if your audience is Dart developers 
 Add compiled binary + GitHub Releases once you want broader adoption 
 Add a Homebrew tap when macOS developers start asking for it 
 Use Docker only when it is already part of your team's workflow 
 Conclusion 
 You've gone from understanding what a CLI is to building three progressively complex tools and distributing them across five different channels. 
 The foundational skills – args , stdin , stdout , stderr , exit codes, file I/O, and process spawning – are the same building blocks that tools like flutter , git , and dart themselves are built on. Everything else is composition. 
 The three CLIs we built (Hello CLI, dart_todo , and dart_http ) each introduced a new layer: raw Dart fundamentals, the args package with JSON persistence, and real-world HTTP interaction. The distribution section ensures that whatever you build next, you have a clear path to getting it in front of the developers who will use it. 
 Dart is a powerful language for CLI development. Its strong typing, async support, native compilation, and pub.dev ecosystem make it a serious choice for building developer tooling, not just mobile apps. 
 The next step is building something that solves a real problem for you or your team, and shipping it. 
 Happy coding!!
```

---

## 3. How to Bypass Cloud SMTP Restrictions Using Brevo and HTTP APIs

- 日期: 2026-05-08 18:23
- 链接: https://www.freecodecamp.org/news/how-to-bypass-cloud-smtp-restrictions-using-brevo-and-http-apis/

```
Being able to communicate by sending emails through web applications is important these days. It helps businesses stay connected with their potential customers, securely verify user identities, and deliver crucial notifications like password resets. 
 But sometimes, deploying your perfectly working email function to the cloud leads to unexpected and frustrating errors. You build your backend, test it locally, and it works flawlessly. Then you deploy to the cloud, and suddenly your app stops sending emails completely. 
 In this article, you’ll learn exactly why your email setup fails on cloud platforms like Render or Heroku, the underlying networking rules causing the issue, and how to elegantly bypass these restrictions using Brevo's HTTP API. 
 Let’s dive right in. 
 Outline 
 Prerequisites 
 Tools We'll Be Using 
 The Problem: Nodemailer and SMTP Blocking 
 The "Modern" Trap: Domain Verification 
 The Ultimate Solution: Brevo and HTTP APIs 
 Backend Setup 
 Brevo Configuration Setup 
 Creating the Email Function 
 Integrating the Function into an Express Route 
 Conclusion 
 Prerequisites 
 To get the absolute most out of this tutorial, it’s important to have some basic knowledge of the following: 
 JavaScript and Node.js: Having a good fundamental understanding of how JS works on the server side will make it easier to follow along with the project. 
 REST APIs: You should have a basic understanding of how HTTP requests (like POST and GET) work using native fetch() in Node.js. 
 Express.js: A little background on creating basic server routes will be helpful, as we'll build a real-world controller. 
 A basic understanding of what Nodemailer is and how cloud hosting platforms (like Render or Heroku) operate. 
 Tools We’ll Be Using 
 In one of my recent projects, I created a complex authentication flow where users needed an OTP (One Time Password) sent to their email to complete registration. I set up Nodemailer, linked my Gmail, and tested it on localhost . Within seconds, the emails arrived perfectly. 
 But when I deployed my backend to Render, the entire signup flow broke. After doing some deep digging, I found out why it broke and how to fix it permanently. And now that I know how it works, I wanted to share it with you all. 
 The Problem: Nodemailer and SMTP Blocking 
 So what exactly is the issue? 
 Nodemailer is a very popular Node.js module that lets you send emails efficiently. Usually, developers use it to connect to services like Gmail or Mailtrap using SMTP (Simple Mail Transfer Protocol). When your code tries to send an email, Nodemailer opens a connection to the mail server using Port 587 (for STARTTLS) or Port 465 (for SSL). 
 But cloud providers like Render, Heroku, DigitalOcean, and AWS face a massive daily battle against automated spammers. Malicious users often spin up thousands of free-tier servers specifically to blast out millions of spam emails. If a cloud provider allows this, their entire network IP address block will get blacklisted by Gmail, Outlook, and Yahoo. 
 To protect their network reputation, cloud providers enacted a heavy-handed, silent rule: All outbound traffic on Ports 25, 465, and 587 is strictly blocked on free and entry-level tiers. 
 This means your server is literally trapped behind a firewall. If you check your server logs, you won't see an "Invalid Password" error. Instead, you'll see a timeout error that looks like this: 
 Error: connect ETIMEDOUT 142.250.102.108:587
 at TCPConnectWrap.afterConnect [as oncomplete] (node:net:1494:16) Your code isn't broken – it's just being blocked at the network level! 
 The "Modern" Trap: Domain Verification 
 When developers hit this wall, they often try modern API-based email services like Resend or SendGrid. These are amazing tools, but they introduce a new problem for beginners: Strict Domain Authentication. 
 To use Resend in production, you must own a custom domain (like yourname.com ) and configure DNS records (SPF, DKIM, and DMARC). If you don't own a domain, Resend's sandbox mode strictly restricts you to sending emails only to yourself. You can't send emails to your live users. 
 For a developer just trying to launch a portfolio project, buying a domain just to send test emails is a huge bottleneck. 
 The Ultimate Solution: Brevo and HTTP APIs 
 We need a solution that meets two criteria: 
 It must bypass the Port 587 firewall. 
 It must let us send emails to anyone without forcing us to buy a custom domain. 
 This is where the architectural difference between SMTP and REST APIs comes to the rescue. While SMTP is a dedicated protocol for routing mail, a REST API operates over standard web traffic using HTTPS (Port 443) . Cloud providers can't block Port 443, because doing so would prevent your server from fetching data from databases or functioning as a web server entirely. 
 Enter Brevo (formerly Sendinblue). Brevo is a powerful email platform that allows you to send emails via a standard REST API. Best of all, their free tier (300 emails/day) allows Single Sender Verification. You just verify your standard Gmail address, and they let you send to anyone! 
 By sending a JSON payload via HTTPS to Brevo's API, your server routes the traffic out of the unrestricted Port 443 , bypassing the Render firewall completely. 
 Now that you know the theory behind the tools we’ll be using, let’s move on to writing the code. 
 Backend Setup 
 First things first, you have to set up your environment. If you don't already have Node.js installed on your computer, head to their website to download and install it. 
 Start by running npm init -y in your terminal. This creates the package.json file which manages your project and stores all the dependencies. 
 Next, run npm install express dotenv . 
 You might be used to installing nodemailer for your email tasks. But because we are going to use the native Node.js fetch() API to talk to the Brevo API, you actually don't need to install any heavy email libraries at all! We want to keep our backend as lightweight as possible. 
 Brevo Configuration Setup 
 Before you write the email function, you first need to configure Brevo to get access to your API key. 
 Go to Brevo.com and create a free account. 
 During setup, they will ask you to add a Sender Email . Make sure you input your standard Gmail address. They will send you an email with a link to verify you own this address. 
 Once verified and inside the dashboard, click on your profile name in the top right corner, and select SMTP & API from the dropdown menu. 
 Go to the API Keys tab and click Generate a new API key . Give it a name like "MyWebApp". 
 Copy this generated key and store it safely in a .env file at the root of your project: 
 # .env file
EMAIL_USER = yourverifiedemail@gmail.com
BREVO_API_KEY = xkeysib-your-generated-api-key-goes-here Creating the Email Function 
 Now that you’ve gotten your API key and set up your environment variables, all that remains is to start putting your backend code together. 
 Create a file named utils/email.js . 
 First, start by ensuring you can load your .env file so you can easily access the credentials you generated: 
 require("dotenv").config();

// We'll define the function to accept dynamic options
const sendEmail = async (options) => {
 const brevoApiKey = process.env.BREVO_API_KEY;
 const senderEmail = process.env.EMAIL_USER;

 // Validate that the keys actually exist
 if (!brevoApiKey || !senderEmail) {
 throw new Error("Missing Brevo credentials in environment variables.");
 } Next on the line, you’ll need to structure your payload. This is the JSON object that tells Brevo exactly who is sending the email, who is receiving it, and what the content is. Here’s how you can do that: 
 const payload = {
 sender: {
 name: "My Awesome Web App",
 email: senderEmail, // Must match your verified Brevo email
 },
 to: [
 {
 email: options.email, // The dynamic email address of the user receiving the email
 },
 ],
 subject: options.subject,
 htmlContent: options.html,
 }; In the code above, the payload object securely packages up your information. We pass in options.email , options.subject , and options.html so that we can reuse this single function for welcome emails, password resets, and notifications. 
 Now, create the actual network request that sends your data to the Brevo backend. We'll use the POST method. When the data is sent, it must be stringified into a JSON format. 
 try {
 const response = await fetch("https://api.brevo.com/v3/smtp/email", {
 method: "POST",
 headers: {
 "Content-Type": "application/json",
 "api-key": brevoApiKey,
 },
 body: JSON.stringify(payload),
 });

 const result = await response.json();

 if (!response.ok) {
 throw new Error(`Brevo API Error: ${JSON.stringify(result)}`);
 }

 console.log(`Email successfully sent to ${options.email} via Brevo HTTP API!`);
 } catch (error) {
 console.error("Error details:", error.message);
 }
};

module.exports = sendEmail; In the code above, after the payload is submitted, if the message is sent successfully, a success log will be displayed in your terminal. But if the message wasn’t successful – maybe due to a typo in your API key – an error message will be thrown to help you debug exactly what went wrong. 
 Integrating the Function into an Express Route 
 At this point, you've successfully built a robust email function. Let's see how you would actually use this in a real Express application. 
 Create an index.js file and set up a simple Express server route: 
 const express = require("express");
const sendEmail = require("./utils/email");
const app = express();

app.use(express.json()); // Middleware to parse JSON request bodies

app.post("/api/signup", async (req, res) => {
 const { username, email } = req.body;

 // 1. Save user to database (skipped for brevity)
 
 // 2. Generate a random OTP
 const otp = Math.floor(100000 + Math.random() * 900000);

 // 3. Send the email using our new Brevo function
 try {
 await sendEmail({
 email: email,
 subject: "Welcome! Here is your Verification Code",
 html: `
 <div style="font-family: sans-serif; text-align: center;">
 <h2>Welcome to My Awesome Web App, ${username}!</h2>
 <p>Please use the verification code below to complete your registration:</p>
 <h1 style="color: #2563eb; letter-spacing: 5px;">${otp}</h1>
 <p>This code will expire in 10 minutes.</p>
 </div>
 `,
 });

 res.status(201).json({ message: "User created and email sent!" });
 } catch (error) {
 res.status(500).json({ error: "Failed to send email." });
 }
});

app.listen(8000, () => {
 console.log("Server running on port 8000");
}); And that is it! You can now hit this /api/signup endpoint from your React or Vue frontend, and it will instantly fire off a beautifully formatted email via Brevo's REST API. 
 Conclusion 
 As developers, encountering a bug that works locally but fails in production is a rite of passage. But the "Email Delivery Failed" timeout error is special. It teaches you that software engineering isn't just about writing clean syntax – it's about understanding the underlying infrastructure, network layers, and the security context of the environment your code runs in. 
 By swapping a protocol (SMTP) for an architectural pattern (REST API over HTTPS), you didn't just fix a bug. You successfully engineered a secure, free, and robust bypass around a cloud-level firewall without relying on heavy third-party NPM modules like Nodemailer. 
 If you've made it this far, I hope I've successfully shown you the importance of understanding network layers and how you can use HTTP APIs to send email messages directly from your web applications safely. 
 Thank you for reading!
```

---

## 4. How to Apply Academic Theories to Human-Centered Web Design [Full Handbook

- 日期: 2026-05-08 18:22
- 链接: https://www.freecodecamp.org/news/how-to-apply-academic-theories-to-human-centered-web-design-handbook/

```
Have you ever abandoned an app right at the sign‑up page? Or felt uneasy navigating a website because the buttons were scattered randomly, the colors clashed, and the layout felt confusing and unnecessarily complex? 
 Maybe you were asked to complete twenty fields in one go. You carefully filled everything out, hit Submit — and only then were you told that your password didn't meet some hidden, unspoken requirement. A requirement that was never communicated upfront. 
 Instead of helpful guidance, you were met with a vague message: “Invalid input." Invalid how, you wonder? 
 Required fields weren’t marked. There was no real‑time validation. No helpful red outline showing which field was wrong. Just a generic prompt telling you to “go back and correct missing information,” as if you’re supposed to magically know what the system wants. 
 So you scroll. 
 You search. 
 You guess. 
 And you're now getting frustrated. 
 The reason you're frustrated is simple: no one enjoys repeating a task they thought they had already completed — especially when the mistakes could've been prevented with clear guidance along the way. 
 You manage to fill in the form and you tap the Submit button. 
 Nothing happens. 
 No loading spinner. 
 No subtle animation. 
 No confirmation message. 
 No success screen. 
 Just silence. For a brief moment, you’re left wondering: Did it go through? So you tap again. And maybe… one more time. 
 At this point, you become fed up and you either postpone the signup process to when you have the time, or you may not ever return. 
 Even if you haven’t experienced this exact scenario, you’ve almost certainly felt the same kind of friction: that moment when a digital interface makes you pause, hesitate, or wonder what you’re supposed to do next. 
 These frustrations often arise because frontend developers either overlook or are unaware of the essential design principles and theories that underpin a smooth, intuitive user experience. 
 As a frontend developer, your interface should minimise cognitive load, provide immediate clarity, and guide users effortlessly through every task. 
 In this handbook, I'll introduce the academic theories that should inform and elevate your frontend decisions. 
 Table of Contents 
 1.0 Fitts’s Law: 
 1.1 Use padding wisely 
 1.2 Use infinite targets 
 Design Takeaway from Fitts Law: 
 2.0 Hick's Law: 
 Design Takeaway from Hick's Law 
 3.0 Gestalt Principles: 
 Key Gestalt Principles: 
 3.1 Proximity 
 3.2 Similarity 
 3.3 Continuity 
 3.4 Closure 
 3.5 Figure/Ground 
 3.6 Common Fate 
 3.7 Focal Point 
 Design Takeaways from the Gestalt Principles 
 4.0 Von Restorff Effect (The Isolation Effect): 
 Design takeway from Von Restorff 
 5.0 Jakob’s Law 
 Design Takeaway from Jakob's Law 
 6.0 Miller’s Law 
 Design Takeaway from Miller's Law 
 7.0 The Goal-Gradient Hypothesis 
 Design Takeaway from Goal-Gradient Hypothesis 
 8.0 Zeigarnik Effect 
 Design Takeaway from Zeigarnik Effect 
 9.0 Tesla’s Law: 
 Design Takeaway from Tesla's Law 
 10.0 Peak End Rule: 
 Design takeaway from Peak End Rule 
 11.0 Postel’s Law: 
 Design Takeaway from Postel's Law 
 12.0 Doherty Threshold: 
 Design Takeaways from Doherty Threshold 
 13.0 Serial Position Effect (Primacy and Recency): 
 Design Takeaways Serial Position Effect 
 14.0 Occam’s Razor: 
 Design Takeaway from Occam's Razor 
 15.0 Parkinson's Law 
 Design Takeaway for Parkinson's law 
 Conclusion 
 References 
 You might wonder what academic theories have to do with frontend development. 
 The answer is simple. Academic theories aren't abstract ideas. There are the result of rigorous scientific investigation — controlled experiments, validated models, and decades of research into how humans think, learn, perceive, and interact with information. 
 Because these theories are grounded in evidence rather than opinion, they offer reliable guidance for building interfaces that align with how the human brain actually processes information. 
 Applying them to frontend development means you're not designing by guesswork or personal preference. Instead, you're applying tested, scientific insights to create clearer, faster, more humane user experiences. 
 In other words, when you build with academic theory in mind, your frontend becomes more than just visually appealing — it becomes cognitively efficient, behaviourally aligned, and measurably easier for users to navigate. 
 You can use the following laws and principles to guide your development work. Let’s start by looking at Fitt’s law. 
 1.0 Fitts’s Law: 
 Fitts’s law is the brainchild of Paul Fitts. He was among the early psychologists who recognised that many human errors result from flawed design rather than simple human weakness. 
 During World War II, he studied airplane cockpit layouts and concluded that numerous incidents attributed to pilot error were actually caused by poor design decisions (Hall, 2023; Budiu, 2022). 
 Here's the formula: 
 $$T = a + b \cdot \log_2\left(1 + \frac{D}{W}\right)$$ 
 T = Movement Time 
 D = Distance to the target 
 W = Width (size) of the target 
 a, b = Empirically determined constants 
 Based on his findings, Fitts postulated that the time required to acquire/reach a target is determined by the distance to the target and the size of the target. 
 Fig 1.0: Illustration of Fitts Law. 
 From the above, between Target B and Target C, it will be faster to interact with Target C than Target B simply because of the distance (Target B is farther away). Interestingly, though Target A and Target C are at the same distance, Target C will still be faster to interact with and less error-prone because of its larger size. 
 In simple terms, Fitt’s Law tells us that the time required to move to a target depends on two main factors: the distance to the target and the size of the target. The farther away an element is, the longer it takes to reach. The smaller it is, the more precision it demands, which increases the interaction time and the likelihood of errors. 
 Conversely, closer and larger targets reduce cognitive load, motor effort, and frustration. 
 In a nutshell, Fitts’s main message to developers is to reduce the distance users must travel on the screen and to make important buttons large and visually dominant. 
 Fig 1.1: Showing Call-to-Action buttons are the largest and most visually prominent elements on each screen. 
 From the image above, you can see that the Call-to-Action buttons on each of the screens are the most visually dominant button and largest in size. They're also placed within the natural region. This makes them faster/easier to interact with. 
 You should also place your Call-to-Action button within the natural zone. This is a zone on a mobile phone where it's easy to reach with the thumb (as most people use their thumbs to select things on a phone screen). Here's a diagram showing the "natural zone" on a typical smartphone. It's much faster for a user to interact within the "natural zone" than the "hard zone" (see figure). 
 Fig 1.2: Showing three different zones for buttons placement (natural, stretching and hard region) 
 1.1 Use Padding Wisely 
 Fitts' law can be applied to your development by increasing padding wisely. You can also use padding to increase the interactive area. By doing this, you're increasing the size of the targets. 
 This is important, because imagine a menu that disappears the moment your cursor drifts a few inches away. You’re weren't trying to close it — you simply moved slightly, and suddenly the entire menu collapses. That tiny slip forces you to start the interaction all over again. It’s a small mistake, but it creates a disproportionately frustrating experience. 
 This happens because the interactive area is too narrow. 
 That’s why effective padding — or more broadly, generous interactive zones — is essential. By increasing the clickable or hoverable area around a menu, you are increasing the size of the targets, which makes the interaction more stable, more forgiving, and far less cognitively demanding. 
 This ensures users can move naturally without fear of accidentally “falling off” the target. 
 1.2 Use Infinite Targets 
 Another fundamental principle that emerges from Fitt’s Law is the idea of infinite targets. When an interface element is placed at the very edge or corner of a screen, it becomes effectively “infinite” because the cursor can't move beyond the screen boundary. The edge acts as a physical barrier, allowing the user to fling the mouse in that direction without precision or careful aiming. 
 As a result, corners and edges become the fastest, easiest, and most reliable places for users to access important controls. 
 This is why operating systems such as Apple’s macOS and Microsoft Windows position their most essential menus and buttons at these locations. The macOS Apple Menu sits in the top‑left corner, Windows historically placed the Start button in the bottom‑left corner, and both systems anchor taskbars, docks, and notification areas along screen edges. 
 These placements reduce cognitive load, minimise motor effort, and increase interaction speed because users do not need to slow down or correct their cursor movement. The screen itself “catches” the pointer. 
 In essence, infinite targets transform small interface elements into large, easy‑to‑hit zones simply by leveraging the geometry of the screen. 
 What this means for you: place your most important and frequently used actions where users can reach them with the least effort. Screen edges and corners act as natural stopping points, meaning users can't overshoot them. 
 Design Takeaways from Fitts Law: 
 Place Primary Actions Where the Task Ends: 
 Placing a submit button at the top‑right forces users to travel all the way back after completing a long form. This increases interaction cost and breaks flow. The best place for a submit button is at the bottom of the form — exactly where the user finishes the task. This aligns with natural reading and interaction patterns. 
 Keep Related Actions Physically Close: 
 Separating “Add to Cart” and “Check Out” across opposite sides of the screen forces unnecessary thumb movement. Group related actions to reduce effort and speed up decisions. 
 Make Primary Targets Large and Visually Dominant: 
 Your main CTAs (“Subscribe Now,” “Pay Now,” “Create Account,” “Sign Up”) should be the most recognisable elements on the screen. Large, high‑contrast targets reduce errors and improve speed. 
 Place High‑Value Actions at Screen Edges and Corners: 
 Edges and corners act as “infinite targets” because the cursor can’t overshoot them. This makes them the fastest, easiest, and most reliable places for critical controls. 
 A tiny icon in the middle of the screen is hard to hit. The same icon placed at an edge becomes effectively huge because the boundary “catches” the pointer. Also, actions like navigation, primary CTAs, or global controls should live where users can reach them with minimal effort. Avoid burying important actions in the centre of the screen. 
 Increase Target Size With Generous Padding: 
 Small interactive zones force users to aim with pixel‑level precision. Adding padding expands the clickable or hoverable area, making interactions easier, faster, and more forgiving. 
 Prevent Accidental “Fall‑Off” With Larger Hit Areas: 
 Menus that collapse the moment the cursor drifts slightly create frustration. A wider interactive zone keeps the menu open during natural mouse movement, reducing accidental resets. 
 Users don’t move perfectly. Interfaces should accommodate slight slips without punishing them. Larger targets reduce cognitive load and eliminate unnecessary frustration. so by increasing the effective size of buttons, menus, and controls, you create interactions that feel stable and predictable, and users can move confidently without fear of losing their place. 
 To Sum Up: The farther away an element is, the longer it takes to reach. The smaller it is, the more precision it demands, which increases the interaction time and the likelihood of errors. Conversely, closer and larger targets reduce cognitive load, motor effort, and frustration. 
 2.0 Hick's Law : 
 Hick’s Law is a psychological principle that describes the relationship between the number of choices presented to a user and the time it takes them to make a decision. It was formulated by William Edmund Hick in 1952 (Yablonski, 2022; Proctor & Scheider, 2018). 
 The law states that as the number of options increases, the decision time increases logarithmically. In simple terms, more choices slow users down, while fewer choices speed up decision-making. 
 $$T = a + b \cdot \log_2(n + 1)$$ 
 Where: 
 T = time to make a decision, 
 n = number of choices, 
 b= a constant that depends on the task and the individual 
 Figure 2.0 illustrates the relationship between user experience, reaction time, and the number of actions. 
 This is how users feel, for example, when they encounter a form that asks for too much information upfront. The longer the form gets, the more frustrated they become. 
 Examples of this are overloading menus with too many items, presenting long, unorganised forms, giving too many calls-to-action on one screen, and building nested menus with excessive depth. 
 All of these create friction and can lead to cognitive overload. 
 Design Takeaway from Hick's Law 
 Avoid Overloading Users With Too Many Actions: 
 Too many buttons, menu items, or choices at once increases cognitive load and slows decision‑making. Users freeze when everything competes for attention. 
 Keep Navigation Clean and Focused: 
 Cluttered menus hurt both usability and SEO. Search engines struggle to track overly complex navigation structures, and users struggle to find what matters. 
 Use Progressive Disclosure to Reduce Complexity: 
 Hide advanced or rarely used options under “More” or expandable sections. Reveal complexity only when the user needs it. 
 Break Complex Tasks Into Smaller, Manageable Steps: 
 Progressive disclosure works beautifully for multi‑step forms and decision flows. Smaller steps reduce overwhelm and improve completion rates. 
 Group Related Options Into Logical Categories: 
 Organising actions into meaningful clusters helps users process information faster. For example, placing “Edit” and “Delete” together leverages natural mental grouping. 
 Video 2.0: Video description of Progressive Disclosure. 
 From the video above, instead of showing all the menu details at once, it is better to hide them initially. As you can see, the additional information only appears when the arrow down button is pressed. This approach prevents overwhelming the user and keeps the interface clean and focused. 
 You should also reduce decision anxiety, as too many choices create doubt and friction (as they say, the more you ask from a user, the less you get). 
 Beyond this, try to use recommended labels, show brief descriptions, provide visual previews, and use comparison tables wisely to show comparison between products especially when they have many characteristics. An example of a comparison table is shown below: 
 Figure 2.1: A comparison table being used to simplify complex information. 
 Also, rather than showing advanced configuration options by default, display only the most commonly used settings. Advanced options can be hidden under an expandable section like “Advanced” or “More Settings. This makes your interface less cluttered and more visually organized. 
 And speaking of visual organization, this is the perfect moment to introduce Gestalt principles — the psychological rules that explain how users naturally group and interpret what they see. 
 To Sum Up : As the number of options increases, the decision time increases logarithmically. 
 3.0 Gestalt Principles : 
 In the 1920s, a group of German psychologists – Max Wertheimer, Kurt Koffka, and Wolfgang Köhlern – introduced what are now known as the Gestalt Principles. Their work sought to understand how humans perceive and interpret visual information (Bustamante, 2023). 
 The word “Gestalt” is German for “unified whole,” reflecting the core idea behind the theory: people naturally perceive objects as organised patterns and complete forms rather than as separate, disconnected parts. 
 These principles explain how the human mind structures visual elements to make sense of the world. Over time, they have become highly influential in fields such as design, user experience (UX), psychology, and data visualization, where understanding perception is critical. 
 Key Gestalt Principles: 
 3.1 Proximity 
 Elements that are placed close to each other are perceived as a group, while those spaced far apart are seen as separate. This is why labels are placed directly next to their corresponding input fields. 
 For example: In a blog feed, the "Title," "Author," and "Date" should have small margins between them (8px), while the space between one blog post card and the next should be much larger (40px). This tells the user's brain: "These three text strings belong to this specific post." 
 Fig 3:0 Illustration of proximity (Gestalt Principle) 
 From the fig above, the spacing within the blog feed plays a powerful role in how effortlessly users interpret what they see. When elements sit close together, the brain instinctively treats them as belonging to the same unit. This is why placing the author credit just 8px beneath the title creates an immediate mental link. The viewer doesn’t need to pause or decode who wrote which article; proximity does the cognitive work automatically, forming a tight, intuitive grouping. 
 Equally important is the generous 40px gap between individual cards. This larger spacing introduces “visual breathing room.” Without it, a feed can quickly collapse into a dense wall of text, overwhelming the user and discouraging exploration. The wider margin establishes a clear boundary—a natural stop-and-start rhythm—that makes each card feel distinct and the entire layout more scannable. 
 Finally, subtle spacing differences can guide behaviour, not just perception. The slightly larger 12px margin above the read‑more link separates it from the passive information above it. This spacing cues the user that the link represents an action rather than another piece of descriptive text. It’s a small adjustment, but it shifts the element’s role from informational to interactive, helping users understand what they can do next. 
 Together, these spacing decisions transform a simple list of posts into a structured, intuitive, and behaviourally clear interface—one where the user never has to think about the layout, because the layout is already thinking for them. 
 Proximity controls meaning: move elements closer to show connection, separate them to show difference. 
 3.2 Similarity 
 We naturally group elements that share similar visual characteristics, such as color, shape, size, or orientation. 
 For example, even if buttons are spread across a page, if they're all the same shade of blue, the user understands they perform similar functions. 
 If your primary "Submit" button is blue with rounded corners, every other primary action on your site should look exactly the same. If you suddenly use a square red button for a primary action, the user will be confused because the "similarity" is broken. 
 Fig 3:1 : illustration of similarity (Gestalt principle) 
 As you can see from above, the layout clearly demonstrates how the Gestalt Principle of Similarity works by showing two different visual situations: one where everything matches, and one where a single element breaks the pattern. 
 All three product cards share the same visual characteristics: 
 Same card shape 
 Same border and shadow 
 Same image size and placement 
 Same blue “Add to Cart” button 
 Same font style and spacing 
 Because these elements look alike, your brain automatically groups them as one category — “products that belong together.” 
 You don’t have to think about it; the similarity creates instant visual unity. 
 This is the Gestalt Principle of Similarity in action. 
 In the second row, everything is still similar except one button: 
 The middle product’s button is orange, not blue 
 It has square corners, not rounded 
 The text is italic, not regular 
 The label changes to “Quick Buy” 
 Because this button breaks the shared pattern, your brain immediately notices it and treats it as different or special. 
 Developers can use broken similarity to intentionally highlight featured items, promotions, or urgent actions. 
 When similarity is broken, the different element stands out and draws attention. 
 3.3 Continuity 
 The human eye prefers to follow a continuous path or curve rather than jagged or broken lines. We perceive items aligned on a line or curve as being related. This is often used in navigation menus or horizontal carousels to guide the user's gaze. 
 For example, you might have a horizontal carousel where the last visible card is slightly "cut off" at the edge of the screen. This visual break creates a path that encourages the user to keep scrolling as their eyes follow the line of cards. 
 Fig 3:2: illustration of continuity (Gestalt principle) 
 As you can see, all four form fields — First Name , Last Name , Email Address , and Phone Number — are perfectly aligned along one continuous horizontal path. Because the human eye naturally prefers to follow an unbroken line, your gaze moves smoothly from left to right across the fields without effort. 
 The final field is slightly cut off at the edge, which creates a subtle visual cue that the line continues beyond the visible area. This encourages the user to keep scrolling or swiping, because their eyes are already following the direction of the form. 
 when elements are arranged along a straight path, curve, or flow, the brain automatically treats them as connected and expects the pattern to continue. 
 Another example is Instagram Stories, which are arranged in a smooth horizontal line at the top of the app. Instagram reinforces this by slightly revealing the next story circle at the edge of the screen. That tiny “peek” acts as a continuation cue — your eyes expect the line to keep going, so your finger follows. 
 Fig 3:3: illustration of continuity (Gestalt principle) 
 As you can see from above, all the circular story icons are arranged in a straight horizontal line, and your visual system instinctively follows that line from left to right without effort. 
 The slight visibility of the next story at the edge of the screen strengthens this effect, signaling that the sequence continues beyond what's currently shown. Also, because the icons share the same size, spacing, and shape, there are no visual interruptions, allowing your eyes to glide across them in one continuous motion. 
 This seamless flow is exactly what continuity describes: the tendency of the human eye to follow the direction of a line or pattern, assuming it continues even when part of it is out of view. 
 Continuity is the tendency of the human eye to follow the direction of a line or pattern, assuming it continues even when part of it is out of view. 
 3.4 Closure 
 Closure refers to the mind’s ability to perceive a complete, unified form even when parts of that form are missing. Rather than requiring every boundary, line, or shape to be explicitly drawn, the brain instinctively fills in the gaps. When used intentionally, closure allows interfaces to feel cleaner, more elegant, and more cognitively efficient. 
 When we look at a complex arrangement of visual elements, we tend to look for a single, recognisable pattern. If an image is missing parts, our brains fill in the gaps to "close" the shape. 
 One of the most celebrated examples of closure in visual identity design is the panda symbol used by the World Wide Fund for Nature (WWF). This logo demonstrates how strategic omission can produce a memorable, emotionally resonant, and universally recognisable mark. 
 At first glance, the panda illustration appears simple, composed of a few bold black shapes arranged against a white background. 
 Yet a closer look reveals that the panda is not fully drawn. There are no outlines defining the body, no complete contours around the head, and no explicit boundaries separating limbs from background. Instead, the designer uses a series of carefully placed shapes (ears, eye patches, nose, and partial limbs) to imply the rest of the animal. The viewer’s mind fills in the missing information, completing the silhouette effortlessly. 
 This is closure at its most effective: the brain constructs a whole from fragments, creating a sense of completeness without visual overload. 
 Fig 3:4: illustration of closure (Gestalt principle) 
 For example, a "hamburger menu" (three lines) isn't a literal drawer, but our brains "close" the shape to understand it represents a menu. 
 Fig 3:5: illustration of closure (Gestalt principle) 
 An example of closure in practice can be seen in step indicators commonly used in checkout flows. These components often rely on partial shapes, implied boundaries, and incomplete outlines to guide the user through a sequence of actions. 
 For instance, upcoming steps may be represented by dashed circles. Although the circles aren't fully drawn, the viewer immediately recognises them as complete shapes. The brain resolves the missing segments, allowing the interface to communicate progression without heavy borders or fully rendered icons. This subtle use of closure reduces visual clutter while preserving clarity. 
 Closure refers to the mind’s ability to perceive a complete, unified form even when parts of that form are missing. 
 3.5 Figure/Ground 
 This principle describes the mind's tendency to separate an object (the figure) from its surrounding area (the ground or background). In web design, using a "modal" or "pop-up" relies on this: by blurring the background, you force the user to see the pop-up as the focal figure. 
 When a user clicks "Login" on a modal/lightbox, the background site often dims (the "Ground") while the login box stays bright and centered (the "Figure"). This immediate depth change tells the user exactly where their attention belongs. 
 Video 3.5.0 Video description of Figure/Ground (Gestalt Principle) 
 From the video above, you can see that when the Quick View button is clicked, the selected figure stands out while the background darkens. This contrast guides the user’s attention and helps them focus on the figure. Developers can use this technique to direct users’ attention to what matters most or to what they want users to notice. 
 This principle describes the mind's tendency to separate an object (the figure) from its surrounding area (the ground or background). 
 3.6 Common Fate 
 Elements that move in the same direction are perceived as more related than elements that are stationary or move in different directions. Think of a dropdown menu: when all sub-items slide down together, they are clearly part of the same "unit." 
 For example, when you click a FAQ header and five sub-items slide down at the exact same speed and direction, the "Common Fate" tells the user that all those items belong to that specific category. If they flew in from different directions, the relationship would be lost. 
 Video 3.6.1 Video description of common fate (Gestalt Principle) 
 Video 3.6.2 Video description of common fate (Gestalt Principle) 
 From the video shown above, the e‑commerce animation example demonstrates these principles clearly by using two distinct motion patterns: a group of regular products that move upward together, and a pair of special‑category items that enter dramatically from the left. Through these contrasting movements, the interface communicates category differences without relying on text labels or explicit instructions. 
 Therefore, developers can use this motion‑based differentiation as a design strategy to guide users’ perception—allowing the interface to signal hierarchy, category structure, and product importance purely through animated behaviour rather than through static visual labels. 
 Elements that move in the same direction are perceived as more related than elements that are stationary or move in different directions. 
 3.7 Focal Point 
 Whatever stands out visually will capture and hold the viewer’s attention first. This is essentially the principle of emphasis. A bright "Sign Up" button in a sea of gray text acts as the focal point, directing the user's primary action. 
 For example, an alert banner or a pricing table should stand out from its surroundings. Beyond this, in a three-tier pricing table (Basic, Pro, Enterprise), the "Pro" column is often slightly larger or a different color. This creates a focal point that draws the eye to the "recommended" option immediately. 
 Fig 3:7: illustration of closure (Gestalt principle) 
 In visual interface design, the Gestalt principle of Focal Point plays a crucial role in directing user attention toward the most important element on a screen. 
 A focal point is created when one element breaks the established pattern of surrounding elements, making it stand out immediately. 
 In e‑commerce interfaces, this principle is often applied to highlight primary actions such as purchasing, subscribing, or upgrading. The “Buy Now” button provides a clear and practical example of how focal points function within a layout. 
 From the example above, the first two buttons share the same visual characteristics: neutral colours, and regular weight text. This repetition establishes a visual pattern that the user quickly becomes familiar with. 
 But the “Buy Now” button intentionally disrupts this pattern. It uses a bright colour, which contrasts sharply with the muted tones of the other buttons. This colour difference alone is enough to draw the eye, as humans are naturally sensitive to changes in hue and saturation within a uniform environment. 
 The Focal Point may sound like it's similar to the principle of Similarity, but the two operate in completely opposite ways within perceptual psychology. 
 Similarity explains how the mind naturally groups elements that share visual characteristics – such as colour, shape, or size – into coherent units. Once this grouping is established, the interface gains structure and predictability. 
 Focal Point, on the other hand, works by intentionally breaking that structure. Instead of reinforcing uniformity, it introduces a deliberate contrast – through colour, scale, brightness, or motion – to draw the viewer’s attention to one specific element. 
 In other words, Similarity creates the background pattern, while Focal Point identifies the one element that must stand out against that pattern. 
 Whatever stands out visually will capture and hold the viewer’s attention first. 
 Design Takeaways from the Gestalt Principles 
 Use Spacing as Your Primary Grouping Tool: 
 Elements that belong together should sit closer to each other than to anything else. Spacing communicates structure faster than borders or boxes. Use tight internal spacing (6–12px) for related items and wide external spacing (24–48px) to separate groups. 
 Build a Strict, Consistent Visual System — and Stick to It: 
 Define clear rules for button types, text styles, icon sizes, and alignment patterns. Consistent left‑aligned text blocks, predictable carousel lines, and stable flow patterns reduce cognitive load and make interfaces feel trustworthy. 
 Guide the Brain With Spacing, Alignment, Consistency, Contrast, and Motion: 
 The human brain is always trying to group, follow, and prioritise what it sees. Your job is to guide that instinct through intentional layout decisions, not fight against it. 
 4.0 Von Restorff Effect (The Isolation Effect) : 
 This is the brainchild of Hedwig von Restorff, posited in 1933. In principle it states: An item that stands out is more noticable and more likely to be remembered than other items (Hunt, 1995). 
 So unique or visually distinct elements grab attention and are more memorable – in other words, distinctiveness dictates memory. When a user interacts with an interface, their brain naturally seeks patterns to minimize cognitive effort. 
 While consistency is generally a virtue in design, a perfectly uniform layout can lead to "banner blindness" or habituation, where the user stops noticing details. 
 By strategically breaking a pattern through changes in color, size, shape, or spacing, the developer can "isolate" an element, triggering a biological response that flags the item as high-priority. 
 Note that although the Focal Point principle may initially seem similar to the Von Restorff Effect, they describe two different psychological processes. 
 Focal Point is a Gestalt visual principle that explains how one element becomes the centre of attention within a composition because it carries the strongest visual contrast – through size, colour, brightness, position, or motion. Its purpose is to guide the viewer’s eye toward the most important element in the layout. 
 The Von Restorff Effect comes from cognitive psychology, not Gestalt theory. It states that an item that is noticeably different from a group of similar items is not only more attention‑grabbing but also more memorable. 
 So Focal Point is about where the eye goes first, while the Von Restorff Effect is about what the brain remembers later. 
 Design takeaways from Von Restorff 
 Use Isolation to Make CTAs Impossible to Miss: 
 On a page filled with neutral text and standard links, a single high‑contrast button (like a bold “Primary Blue” or “Emergency Red”) instantly becomes the standout element. This leverages the Von Restorff Effect to pull the user’s eye toward the most important action. 
 Create a Visual “Hitch” in the Scan Path: 
 A distinct CTA interrupts the user’s natural left‑to‑right, top‑to‑bottom scanning rhythm. This makes actions like “Buy Now” or “Sign Up” the first thing they notice and the last thing they forget. 
 Make Critical Actions Visually Distinct: 
 Because users naturally notice the one element that breaks a pattern, your most important actions should use deliberate contrast — color, size, shape, weight, or motion. Isolate key information instead of letting it blend into surrounding UI noise. 
 Avoid Over‑Differentiation — or Nothing Stands Out: If every button is loud, animated, or uniquely styled, the interface becomes chaotic. The Von Restorff Effect only works when there is a clear, stable pattern — and you break it once, intentionally. 
 To Sum Up: An item that stands out is more noticable and more likely to be remembered than other items. 
 5.0 Jakob’s Law 
 Jakob’s Law states that users spend most of their time on other sites, so they expect your interface to behave like the ones they already know. 
 Familiar patterns — hamburger menus, top navigation, search icons, and clickable top‑left logos — reduce cognitive load because users don’t have to interpret anything new. 
 But while Jakob’s Law is foundational to UX, I think it can also unintentionally suppress innovation. 
 When developers over‑prioritise familiarity, they fall into a standardisation trap: endlessly optimising conventional patterns instead of exploring fundamentally better ones. 
 The Pie Menu is a perfect illustration of this. According to Fitts’s Law, the time required to reach a target depends on its distance and size. Linear menus place the last item much farther from the cursor than the first, creating uneven interaction costs. 
 Radial menus position every option at an equal distance from the centre, and their wedge‑shaped targets effectively grow larger as the pointer moves outward. 
 Mathematically, pie/radial menu are faster to interact with and more efficient — yet they remain rare in mainstream web design because they violate users’ expectations. In other words, Jakob’s Law keeps us locked into a familiar but suboptimal pattern simply because “that’s how it’s always been done.” 
 But the challenge is not choosing between familiarity and innovation, but balancing them. 
 This is where the Aesthetic–Usability Effect becomes powerful. Research shows that users perceive attractive interfaces as easier to use, and they are more forgiving of minor usability friction when the design is visually pleasing. 
 A beautifully crafted Pie Menu, for example, can encourage users to invest the small amount of learning required to use it. By applying aesthetic delight strategically, developers can introduce innovative patterns without overwhelming users. 
 The principle that emerges is simple: Be conventional where it matters, and innovative where it delights. 
 Design Takeaway from Jakob's Law 
 Keep Trust‑Critical Elements Predictable: 
 Navigation, search, authentication, and other high‑stakes interactions must follow established conventions. Users rely on these patterns for speed, confidence, and safety — this is where Jakob’s Law should be respected without exception. 
 Experiment Only in Low‑Risk, High‑Creativity Areas: 
 In creative or productivity‑focused zones — like editing tools in a photo app — you can safely introduce new interaction models such as radial menus, gesture wheels, or context‑aware tool selectors. These areas invite exploration and benefit from efficiency‑driven innovation. 
 To Sum Up: Be conventional where it matters, and innovative where it delights. 
 6.0 Miller’s Law 
 Miller’s Law originates from George A. Miller’s classic paper “The Magical Number Seven, Plus or Minus Two.” It states that the average person can hold only about 7 (±2) chunks of information in working memory at any given moment (Miller, 1956). 
 Crucially, Miller emphasised that the brain doesn’t store isolated items — it groups them into meaningful units called chunks. Because working memory is so limited, developers must structure information in ways that respect this cognitive boundary. 
 This principle has direct implications for interface design. Long, unbroken strings of information overwhelm users, whereas chunked formats are far easier to process. 
 For example, instead of displaying a phone number as 1234567890, formatting it as 123‑456‑7890 transforms ten digits into three manageable chunks. The same logic applies to navigation: aim for five to nine primary menu items, and if you need more, group them into categories. Users remember the category as a single chunk rather than each individual link. 
 Miller’s Law also explains why long forms are so intimidating. When a user sees 30 fields on one page, their brain interprets it as a single, massive task — far beyond the 7±2 limit. 
 A progressive stepper solves this by breaking the form into smaller stages of 5–7 fields each. This reduces cognitive load, creates a sense of progress, and significantly lowers abandonment rates. 
 The same principle applies to product listings or search results. Expecting users to compare 50 items at once is unrealistic. Instead, provide strong filtering tools so users can narrow the set to a manageable size — ideally within the range their working memory can meaningfully evaluate. 
 In essence, Miller’s Law reminds developers that humans don’t process information in bulk. They process it in structured, meaningful chunks. 
 Fig 6.0: Illustrating progressive stepper 
 In the example above, the interface uses both a progress bar and a stepper to guide the user through multiple stages of a task. After completing the first page and selecting “Continue,” the user moves to the next step, and the progress bar updates accordingly. This creates a clear sense of forward movement and accomplishment. 
 By breaking the process into smaller segments, the interface prevents cognitive overload. If all the information were presented on a single page, users might feel overwhelmed, unsure where to begin, or discouraged by the sheer volume of work. 
 A step‑by‑step flow transforms a large task into a sequence of manageable actions, increasing the likelihood of completion. 
 Design Takeaway from Miller's Law 
 Respect the 7±2 Working‑Memory Limit: 
 Users can only hold about seven chunks of information at once. Long, unbroken content overwhelms them, while chunked information is instantly easier to process. 
 Chunk Information Into Meaningful Units: 
 The brain doesn’t store isolated items — it groups them. Format data (like phone numbers), menus, and settings into clear, memorable chunks instead of long, flat lists. 
 Keep Navigation Within 5–9 Primary Items: 
 If you need more than nine options, group them into categories. Users remember the category as a single chunk, not each individual link. 
 Break Long Forms Into Smaller Steps: 
 A 30‑field form feels like one giant task. A progressive stepper with 5–7 fields per step keeps users below the cognitive overload threshold and dramatically reduces abandonment. 
 Reduce Comparison Load With Strong Filters: 
 Expecting users to compare 50 products at once is unrealistic. Provide filtering tools that shrink the decision set to something the working memory can actually handle. 
 Design for Chunked Thinking, Not Bulk Processing: 
 Humans don’t process information in bulk — they process structured, meaningful groups. Interfaces that respect this limitation feel lighter, faster, and more intuitive. 
 To Sum Up: A step‑by‑step flow transforms a large task into a sequence of manageable actions, increasing the likelihood of completion. 
 7.0 The Goal-Gradient Hypothesis 
 This is the perfect moment to introduce the Goal‑Gradient Hypothesis, originally proposed by behaviorist Clark Hull in 1932 (Yablonski, 2022). The hypothesis states that people become more motivated as they get closer to achieving a goal. In other words, users naturally accelerate their engagement when they sense they are nearing completion. 
 This principle is incredibly powerful in UX design, especially for progress tracking, gamification, and reward systems. 
 The takeaway is straightforward: Because users are more motivated near the finish line, progress indicators should be prominent and meaningful. 
 Percentages, progress bars, and step counters reinforce momentum. Micro‑achievements — such as badges, checkmarks, or subtle confetti — amplify motivation by celebrating small wins. 
 Tasks should be broken into measurable milestones so users can see themselves advancing. 
 This is why e‑learning platforms display messages like “You’ve completed 8 of 10 lessons — almost there!” and why fitness apps highlight progress with prompts such as “3 km done, 2 km to go.” These cues leverage the goal‑gradient effect to keep users engaged, energized, and eager to finish. 
 By combining progressive steppers with clear progress feedback, developers create interfaces that feel lighter, more encouraging, and far more motivating — ultimately improving completion rates and overall user satisfaction. 
 But what happens when a goal isn't completed? Why do we sometimes feel uncomfortable leaving things unfinished? That discomfort is explained by another psychological principle called the Zeigarnik Effect — the tendency for people to remember and feel tension about incomplete tasks. We will look at this next. 
 Design Takeaway from Goal-Gradient Hypothesis 
 Make Progress Visible to Boost Motivation: 
 According to the Goal‑Gradient Hypothesis, users naturally speed up as they sense they’re nearing completion. Prominent progress bars, percentages, and step counters tap into this instinct and keep momentum high. 
 Celebrate Micro‑Achievements to Reinforce Engagement: 
 Badges, checkmarks, subtle confetti, and “step completed” cues reward small wins. These micro‑rewards amplify motivation and make long tasks feel lighter and more achievable. 
 Break Tasks Into Measurable Milestones: 
 Users stay motivated when they can see themselves advancing. Divide complex flows into clear steps so progress feels tangible rather than overwhelming. 
 Use Progress Feedback to Drive Completion: 
 Messages like “8 of 10 lessons completed — almost there” or “3 km done, 2 km to go” leverage the goal‑gradient effect to energise users and pull them toward the finish line. 
 Combine Steppers With Clear Feedback for Maximum Impact: 
 Progressive steppers paired with strong visual feedback create interfaces that feel encouraging, structured, and motivating — dramatically improving completion rates. 
 Video 8.0 : Video illustrating goal gradient 
 To Sum Up: People become more motivated as they get closer to achieving a goal. 
 8.0 Zeigarnik Effect 
 The Zeigarnik Effect is a psychological principle stating that people remember unfinished or interrupted tasks better than completed ones (Cherry, 2024). 
 Memory begins with sensory input, which is processed into short-term memory. Unfinished tasks persist in our thoughts, leading to active recall. This ongoing engagement can turn them into long-term memories, enhancing recall until resolved. This increases engagement, encourages task completion, improves retention, and drives conversions. 
 So because people remember unfinished tasks better than completed ones (Zeigarnik Effect), developers use progress indicators to make users aware that something is incomplete and motivate them to finish it. 
 In your designs, you can break long forms into multi-step processes to encourage completion and display profile completion percentages (for example, 70% complete) to push users toward 100%. 
 This is the main reason why e-commerce platforms send abandoned cart reminders to bring users back to complete their purchases. It's also why apps use streak systems to encourage daily engagement and habit formation and learning platforms show course completion bars to motivate users to finish modules. 
 Design Takeaway from Zeigarnik Effect 
 Unfinished Tasks Stay Active in Memory — Use That to Drive Completion: 
 Because incomplete tasks linger in working memory (Zeigarnik Effect), users naturally keep thinking about what they haven’t finished. This tension boosts recall, engagement, and the likelihood of returning to complete the task. 
 Make Incompleteness Visible With Progress Indicators: 
 Progress bars, percentages, and step counters remind users that something is still unfinished. This gentle psychological pressure motivates them to continue until the task is complete. 
 Break Long Flows Into Multi‑Step Processes: 
 A massive form feels overwhelming, but a stepper with smaller chunks keeps users moving. Showing “70% complete” nudges them toward finishing the last stretch. 
 Use Reminders to Re‑activate Unfinished Intent: 
 Abandoned cart emails, streak reminders, and “continue your lesson” prompts work because the unfinished task is already active in the user’s mind. The reminder simply pulls them back into the loop. 
 Celebrate Completion to Close the Cognitive Loop: 
 Checkmarks, confirmations, and completion badges give users closure. This resolves the mental tension created by the unfinished task and reinforces positive behaviour. 
 To Sum Up: Unfinished tasks persist in our thoughts, leading to active recall. 
 9.0 Tesler’s Law : 
 This law was proposed by Lawrence Tesler. He was a computer scientist known for his work on human-computer interaction, and he contributed significantly to making software more user-friendly, including work on cut, copy, and paste functionality. 
 This law is otherwise known as the Law of Conservation of Complexity. The core Idea here is every process has a certain amount of “inherent complexity" that can't be removed. You can only decide who handles it: the user or the system. 
 Some examples of these inherent complexities might be: 
 translating user actions into correct operations behind the scenes, 
 handling unreliable or slow network connections, 
 connecting with third-party APIs, services, or legacy systems, 
 sorting large datasets quickly, 
 performing complex search operations 
 managing version changes and compatibility issues, 
 managing state, interactions, and animations without confusing the user. 
 All of these can be inherently complex, but it's the job of the developer to deal with the complexity. 
 As a developer, you should always try as much as possible to push complexity to the system. For example, instead of making a user type their full address manually, use an Auto-complete API (Google’s Places and Map is best for this). The complexity of finding and validating the address still exists, but the software handles the work for them. 
 Here's a practical example: let’s say you're designing a student platform that requires users to enter their university name. A practical approach would be to store an array of all universities in the UK in your codebase (This is the hard part Tesla hinted at). 
 As the user types, they don't need to enter the full name, and their full university name is shown (relating to what they have typed). For instance, if they intend to type “University of Sheffield,” simply typing “Sheff” should prompt the system to display the full university name, which they can then select. 
 In Dart, you can use a package like fuzzysearch to implement this kind of intelligent matching. 
 The advantage of this approach is greater than it first appears. It improves data consistency because users often enter the same information in different ways. For example, some users might type “Uni of Sheff,” others “Sheffield University,” and others “Uni of Sheffield,” while all are referring to “University of Sheffield.” 
 This is how messy data is created, and it creates more work for data analysts. Little wonder that data analysts spend up to 70% of their time cleaning data. 
 If developers invested more time in structuring how data is collected to ensure consistency, there would be far less work downstream for analysts. This same logic should be applied in how we collect date, time, and other information. 
 So apart from people's names and email addresses, you should try to standardize the data your app collects as much as possible. Use date and time pickers, stepper controls, input masks, checkboxes, dropdown menu and radio buttons, toggle switches. and so on. 
 The essence of removing complexity from the user is not only about improving usability, but also about ensuring that the data collected is standardised, structured, and consistent. 
 Design Takeaway from Tesler's Law 
 Push Complexity to the System, Not the User: 
 Every process contains unavoidable complexity. Your job is to handle it behind the scenes so the user experiences the simplest possible interaction. 
 Automate Tasks Users Shouldn’t Have to Think About: 
 Use tools like autocomplete, fuzzy search, intelligent defaults, and validation APIs to remove manual effort. The complexity still exists — but the system absorbs it instead of the user. 
 Standardise Inputs to Prevent Messy Data: 
 Users enter the same information in wildly different ways. Use pickers, dropdowns, input masks, radio buttons, and toggles to enforce consistent, structured data collection. 
 Handle Inherent Technical Complexity Internally: 
 Network issues, API quirks, large dataset sorting, search optimisation, state management, and animation logic are all developer responsibilities. Users should never feel this complexity. 
 To Sum Up: Every process contains unavoidable complexity. Your job as a developer is to handle it behind the scenes so the user experiences the simplest possible interaction. 
 10.0 Peak End Rule : 
 In 1993, Daniel Kahneman, Barbara Fredrickson, Charles Schreiber, and Donald Redelmeier invited volunteers into a lab for what sounded like a simple experiment. The task was straightforward: place a hand into a container of painfully cold water (Kahneman et al., 1993) 
 In the first round, participants kept their hand in 14°C water for 60 seconds. It was uncomfortable, sharp, and unpleasant but after one minute, it was over. 
 In the second round, they again endured 60 seconds in 14°C water. But this time, they were asked to keep their hand in for an extra 30 seconds. The temperature was raised slightly to 15°C. Still cold. Still unpleasant. Just slightly less intense. 
 Objectively, the second experience was worse. It lasted 90 seconds instead of 60. More total pain. More suffering. 
 Later, the researchers asked a simple question: 
 If you had to repeat one of the trials, which would you choose?” Surprisingly, most participants chose the longer one. 
 Why would anyone choose more pain? 
 The researchers realised something profound: people don’t remember experiences by calculating total discomfort. Instead, the mind summarizes the experience using just two key moments — the most intense point (the peak) and the final moment (the end). 
 In both trials, the peak pain was the same: 14°C. But the longer trial ended slightly better, at 15°C. That small improvement at the end reshaped how the entire episode was remembered. The participants’ “experiencing self” suffered more during the longer trial. But their “remembering self” preferred it because it ended on a less painful note. 
 From this, the researchers introduced what became known as the Peak–End Rule: we judge experiences largely by their most intense moment and how they finish, not by how long they last. 
 Since people largely judge an experience by how it ends, developers should focus on designing satisfying confirmation screens and smooth exit interactions. You should concentrate less on making every single moment perfect and instead prioritise optimising the peak and final moments. 
 A negative ending can overshadow an otherwise good experience, so carefully avoid frustrating final steps such as unexpected fees or confusing confirmations. 
 Emotional intensity strongly shapes memory, which is why many apps incorporate celebration animations, rewards, or success messages at key moments to leave a lasting positive impression. 
 Design takeaway from Peak End Rule 
 People Judge Experiences by the Peak and the Ending — Not the Total Duration: 
 Users don’t remember every moment. They remember the most intense point and how the experience ends. A slightly better ending can completely reshape how the entire interaction is remembered. 
 Prioritise Strong, Positive Endings in Your UX Flows: 
 A smooth final step, a clear confirmation, or a satisfying success screen leaves a disproportionately strong impression. A bad ending can overshadow an otherwise great experience. 
 Design for Emotional Peaks at Key Moments: 
 Celebration animations, rewards, checkmarks, and success messages create memorable emotional spikes. These peaks anchor the experience in the user’s memory. 
 Don’t Try to Perfect Every Moment — Perfect the Right Moments: 
 Optimise the peak and the end of the journey. These two moments define how users recall the entire interaction. 
 Avoid Negative Surprises at the Finish Line: 
 Unexpected fees, confusing confirmations, or friction at the last step can ruin the memory of the whole process. Protect the ending carefully. 
 To Sum Up: We judge experiences largely by their most intense moment and how they finish, not by how long they last. 
 11.0 Postel’s Law : 
 Jon Postel’s famous principle – “Be conservative in what you send, be liberal in what you accept” –  is a philosophy of kindness in software design. At its core, the principle argues that systems should be generous with what they accept from users, yet disciplined and predictable in what they output. 
 When developers follow this approach, users feel supported and understood. When they don’t, users feel punished for being human. 
 A user’s input is rarely perfect. People type quickly, make mistakes, follow their own habits, or rely on formats familiar to them. A robust system embraces this reality. It accepts messy, human input and quietly transforms it into clean, standardized data. 
 Real people don't think in strict formats. They write dates the way they learned in school, type phone numbers the way they say them aloud, and enter names and addresses in whatever structure feels natural to them. 
 A rigid system will reject anything that doesn’t match its narrow expectations, but a robust system, by contrast, adapts to the user. 
 Consider dates. A brittle interface might demand MM/DD/YYYY and reject everything else. A more humane system accepts a wide range of formats — “1 May 2024,” “2024‑05‑01,” “05/01/24,” or “May 1st, 2024” — and quietly converts them into a standard internal representation. This is where the complex handling described by Tesla's Law comes into play (Shifting complexity to the system, rather than the user). 
 Phone numbers follow the same pattern. People might enter (555) 123 4567, 555‑123‑4567, 5551234567, or +1 555 123 4567. A fragile system throws errors. A robust one parses all of them using libraries like libphonenumber and moves on. 
 Addresses are equally varied. “221B Baker St,” “221‑B Baker Street,” and “221 Baker St., Apt B” all refer to the same place. A forgiving system normalizes these instead of rejecting them. 
 Even names can be surprisingly complex. Hyphens, apostrophes, multiple words, and titles are all part of real human identity. Rejecting “O’Connor,” “Jean‑Luc,” or “Dr. Sarah Lee” is not just technically incorrect — it's disrespectful to the user. 
 Search bars offer another clear example. A strict search bar demands perfect spelling and exact phrasing. A robust one handles typos (“restuarant”), partial words (“resta”), synonyms (“food places”), and natural language (“where can I eat nearby”). It meets the user where they are instead of forcing them to think like a machine. 
 Currency should be normalized to a clear format such as GBP 5.00, no matter whether the user typed “£5,” “5 pounds,” or “5 GBP.” 
 Even file uploads benefit from standardization: whether the user uploads .jpeg, .jpg, .JPG, or .JPEG, the system should store everything as .jpg. 
 Error messages follow the same principle. Vague feedback like “Invalid password” leaves users confused and frustrated. 
 A clear, conservative message — “Incorrect password. Please try again.” — respects the user’s time. And instead of hiding password requirements, the system should state them upfront: minimum eight characters, at least one uppercase letter, at least one number. 
 Predictability reduces friction. 
 Because users inevitably make mistakes or enter data in unexpected ways, developers should design input fields that are tolerant rather than brittle. This means accepting flexible formats, offering autocorrect or intelligent parsing, and using forgiving validation rules that interpret the user’s intent instead of rejecting their effort. 
 Clear instructions, tooltips, and visible requirements should appear before submission so users understand what the system expects without trial and error. 
 When errors do occur, the interface should handle them gently—never crashing, and never forcing the user to start over. 
 Even simple variations, such as phone numbers typed with spaces, dashes, or parentheses, should be accepted and normalized behind the scenes. 
 By embracing flexibility on the input side and clarity on the output side, developers create systems that feel humane, resilient, and respectful of the way real people actually behave. 
 Design Takeaway from Postel's Law 
 Accept Messy Human Input, Output Clean Structured Data: 
 Users type dates, names, phone numbers, and addresses in unpredictable ways. A humane system accepts this variability and quietly normalises it into a consistent internal format. 
 Rigid interfaces punish users for being human. Robust interfaces interpret intent — handling typos, partial matches, synonyms, and natural language without complaint. 
 Also accept variations in spacing, punctuation, casing, and structure. Let users type naturally — the system should handle the complexity, not them. 
 Be Flexible With Input, Be Strict With Output: 
 This is the heart of Postel’s Law. Let users express information naturally, but ensure your system stores and displays it in a predictable, standardised way. 
 Use Intelligent Parsing and Autocorrection to Reduce Errors: 
 Libraries like libphonenumber, fuzzy search, and natural‑language parsers allow systems to accept a wide range of formats while still producing clean, reliable data. 
 Normalise Everything Behind the Scenes: 
 Dates, phone numbers, currency, file extensions, and addresses should all be standardised internally. This prevents messy data and reduces downstream cleanup work. 
 Provide Clear, Predictable Feedback: 
 Error messages should be specific and helpful. Requirements should be visible upfront. Users should never be surprised, confused, or forced to start over. 
 Combine Postel’s Law With Tesler’s Law: 
 Shift complexity to the system. Intelligent handling of messy input reduces cognitive load, improves usability, and ensures consistent, high‑quality data. 
 To Sum Up: A rigid system will reject anything that doesn’t match its narrow expectations, but a robust system, by contrast, adapts to the user. 
 12.0 Doherty Threshold : 
 The Doherty Threshold is a principle in human–computer interaction which proposes that systems should respond quickly enough to keep users actively engaged (Mod 2024). 
 When response times stay below a certain limit, users remain focused and productive. But once performance already meets this optimal responsiveness level, making the system even faster or adding extra capability doesn't significantly enhance satisfaction or efficiency. 
 The idea was introduced by Walter J. Doherty in 1976 in his paper “A Comparison of Programming Systems and Doherty Threshold.” His research showed that maintaining rapid system feedback fast enough to sustain continuous interaction has a stronger impact on productivity than simply increasing system power or features beyond that point. 
 Doherty proposes that this shouldn't be greater than 400ms Rule: If the system responds within this window, the user feels in total control. If the response takes longer, the user's attention begins to wander, and their "train of thought" is broken. 
 The challenge, of course, is that not every operation can realistically complete within 400ms. Some tasks require heavy computation, large network calls, or complex rendering. This is where the concept of perceived performance becomes essential. 
 Even when the system can't finish the work quickly, it can feel fast by responding instantly at the UI level. Developers can achieve this illusion of speed through a combination of thoughtful design patterns and disciplined engineering practices. 
 On the technical side, performance begins with reducing unnecessary work. Keeping the number of HTML elements low helps the browser render faster. Rendering only the visible portion of long lists prevents the Document Oject Model (DOM) from becoming bloated. Splitting scripts and deferring non‑critical code ensures that essential interactions load first. 
 Using CSS transforms and opacity changes avoids expensive layout recalculations. Lazy‑loading images, videos, and scripts ensures that the interface becomes interactive long before all assets are downloaded. 
 These optimizations don’t just improve raw speed — they create the foundation for interfaces that feel responsive. 
 Design Takeaways from Doherty Threshold 
 Instant Feedback : When a user clicks a button, provide a visual change (like a button press animation or a spinner) immediately, even if the background task takes longer. 
 Skeleton Screens : Use placeholder blocks that mimic the layout of the page while data loads. This makes the app feel like it is responding instantly. 
 Progressive Loading : Load text and basic structures first, then "pop in" high-resolution images later. 
 Optimistic UI : When a user hits "Save," don't wait for the server. Update the UI instantly (Doherty) and handle the "messy" data formatting on the backend (Postel). 
 Live Inline Validation : Show a green checkmark or a helpful error message as the user types. This keeps them below the 400ms "thought-break" limit. 
 Debouncing : In search bars, start showing results after a few keystrokes so the user feels the app is "predicting" their needs. 
 To Sum Up: When response times stay below a certain limit, users remain focused and productive. But once performance already meets this optimal responsiveness level, making the system even faster or adding extra capability doesn't significantly enhance satisfaction or efficiency. 
 13.0 Serial Position Effect (Primacy and Recency) : 
 Murdock’s study investigated how the position of a word in a list affects recall, known as the serial position effect. He presented 103 psychology students with lists of 10 to 40 words, one at a time, at either 1 or 2 seconds per word (McLeod, 2025). 
 Participants were divided into six groups, each experiencing a different combination of list length and presentation rate, and were asked to recall as many words as possible in any order. 
 The results showed that participants were most likely to remember words at the beginning of the list (primacy effect) and at the end of the list (recency effect), while words in the middle were recalled less often. The recency effect persisted even in longer lists, and the middle section of the recall curve formed a flat asymptote. 
 Murdock explained this using the multi-store model of memory: early words were rehearsed and transferred to long-term memory, last words remained in short-term memory, and middle words were neither sufficiently rehearsed nor retained, leading to poorer recall. 
 The experiment demonstrated that memory performance varies systematically with the position of information in a sequence. 
 This is the reason why the most important information or actions should never be buried in the middle. 
 As a developer, you should put your most critical navigation links (like "Home" or "Dashboard") at the far left or the top of a list. In a pricing table, put the most popular or recommended plan on the Place "Final Actions" (like "Log Out," "Cart," or "Support") at the end of a menu or the far right of a navigation bar. 
 In a long onboarding flow, put the most exciting benefit of the app on the very last slide so the user enters the app feeling motivated. 
 Avoid placing highly important buttons in the middle of a row. If you have a row of 7 buttons, the user is statistically likely to overlook the 4th one. 
 Design Takeaways Serial Position Effect 
 Place Critical Items at the Beginning or End — Never the Middle: 
 Users reliably remember the first and last items in any sequence (primacy and recency). Anything placed in the middle is statistically more likely to be forgotten or ignored. Also, actions such as “Log Out,” “Cart,” “Support,” or “Checkout” should sit at the far right or bottom — the natural recency position. 
 Put Essential Navigation Links at the Far Left or Top: 
 Links like “Home,” “Dashboard,” or “Overview” should appear at the start of a menu, where recall and recognition are strongest. 
 To Sum Up: The results showed that participants were most likely to remember words at the beginning of the list (primacy effect) and at the end of the list (recency effect), while words in the middle were recalled less often. 
 14.0 Occam’s Razor : 
 Although first articulated in the 14th century by the Franciscan friar William of Ockham, Occam’s Razor remains one of the most indispensable principles in a developer’s toolkit. In fact, skipping this law while discussing other theories and principles would be like skipping the glue that holds the entire framework together. 
 At its core, Occam’s Razor states that “among competing explanations, the simplest one is usually the best.” 
 For example, if two user interfaces achieve the same goal, the one with fewer visual elements is typically superior because it requires less processing power. 
 The fundamental takeaway for modern developers regarding Occam’s Razor is that complexity is a tax on the user’s cognitive resources. 
 In an era of information density, the developer's primary role is no longer to provide "more" features – rather, it's to curate the most direct path to a solution. 
 In practice, Occam’s Razor becomes a reminder to keep things as simple as possible. This “less is more” mindset shapes everything from navigation to forms. 
 A good rule for navigation is the Rule of Five: aim for three to five main menu items instead of a long, overwhelming list. This keeps choices clear and prevents users from freezing up when they see too many options. 
 The same idea applies to data entry. When you ask only for the information that truly matters, you respect the user’s time and reduce the chance of “form fatigue,” which is one of the biggest reasons people abandon sign‑ups or checkout flows. 
 Simplicity isn’t just elegant — it’s practical, humane, and far more effective. 
 Design Takeaway from Occam's Razor 
 Choose the Simplest Effective Solution: 
 When two designs achieve the same goal, the one with fewer elements is almost always better. Simplicity reduces cognitive load and speeds up user decision‑making. 
 Simplicity Is Not Just Aesthetic — It’s Humane: 
 Clear, minimal interfaces respect the user’s time, reduce friction, and make the product feel effortless. Simplicity is both a design strategy and an act of empathy. 
 To Sum Up: Simplicity isn’t just elegant — it’s practical, humane, and far more effective. 
 15.0 Parkinson's Law 
 Occam’s Razor teaches us to prefer the simplest solution that works. But why do we so often end up with complex systems in the first place? That tendency is explained by another principle: Parkinson’s Law. 
 Parkinson’s Law states that "work expands to fill the time available for its completion". In design, this means projects often become overly complex or take longer than necessary if given too much time, resulting in inefficient, over-designed, or cluttered interfaces. 
 In design, this manifests as Feature Creep. If you give yourself three months to build an app, you will spend three months adding "nice-to-have" animations, extra settings toggles, and niche edge cases that nobody asked for and in reality, what you have added isn’t that important. 
 You just succeeded in adding layers of complexity that might ends up violating some of the laws we spoke about. Occam’s Razor reminds us that the simplest solution is often the most effective. 
 By being aware of Parkinson’s Law and the tendency for work to expand, developers can manage their time intentionally and focus only on what truly matters. 
 Design Takeaway for Parkinson's law 
 Set Clear Constraints to Keep Designs Focused: 
 Intentional time limits and scope boundaries prevent over‑designing. Constraints force clarity, prioritisation, and simplicity. 
 Build Only What Truly Matters for the User: 
 Parkinson’s Law reminds you to resist the urge to fill time with unnecessary features. Focus on the core experience, not the edge cases nobody asked for. 
 Use Occam’s Razor to Counterbalance Parkinson’s Law: 
 As work expands, complexity grows. Occam’s Razor pulls you back to the simplest effective solution. Together, the two principles prevent bloated, over‑engineered products. 
 To Sum Up: Work expands to fill the time available for its completion 
 Conclusion 
 Human-centered design is deeply influenced by a set of psychological principles that explain how users perceive, process, and interact with digital systems. 
 Among these, Fitts’s Law establishes that the time required to acquire a target depends on its size and distance. In practice, this means that larger and closer elements are easier and faster to interact with. 
 To apply this in practice, developers should make primary call-to-action elements prominent, large, and easily reachable – especially in mobile interfaces where thumb accessibility is critical. 
 Closely related to decision-making is Hick’s Law, which states that the more choices a user is presented with, the longer it takes to make a decision. Excessive options can overwhelm users and lead to decision fatigue. 
 To address this, developers should simplify interfaces, minimise unnecessary options, and guide users through processes step-by-step rather than presenting everything at once. 
 Another important cognitive principle discussed is Miller’s Law, which suggests that the average person can hold approximately seven (plus or minus two) items in working memory at a time. This limitation highlights the need to present information in manageable chunks. 
 By breaking content into smaller groups and avoiding information overload, developers can improve comprehension and usability. 
 User expectations are strongly shaped by Jakob’s Law, which says that people spend most of their time on other websites and therefore expect similar patterns across digital products. 
 Instead of reinventing basic interactions, developers should follow familiar conventions such as placing the logo in the top‑left, the shopping cart in the top‑right, and keeping scrolling behaviour predictable. 
 But innovation is still possible where it truly adds value. As we discussed with the Aesthetic‑Usability Effect, users are far more tolerant of new or unusual design patterns when the interface is visually appealing and thoughtfully crafted. 
 The Gestalt Principles provided additional insight into how users visually organise information. The principle of proximity suggests that objects placed close together are perceived as related, so grouping related elements improves clarity. Similarity indicates that elements with consistent colours, shapes, or styles are seen as belonging together, reinforcing visual hierarchy and function. Closure explains that users can perceive incomplete shapes as complete, allowing for minimalistic designs where the brain fills in missing details. Continuity highlights that users naturally follow smooth visual paths, meaning layouts should guide the eye logically through alignment and structure. 
 We also looked at The Von Restorff Effect which emphasizes that elements which stand out are more likely to be remembered. By using contrast in colour, size, or design, important features such as buttons or alerts can capture user attention. 
 Managing complexity was addressed by Tesler’s Law, which asserts that every system has inherent complexity that cannot be eliminated but only managed. 
 Developers must therefore shift complexity away from the user by simplifying interfaces while handling intricate processes behind the scenes. 
 The Zeigarnik Effect reveals that people remember unfinished tasks better than completed ones, creating a sense of mental tension. This can be leveraged by incorporating progress indicators, checklists, and reminders that encourage users to complete tasks. 
 Similarly, the Peak-End Rule suggests that users judge an experience based on its most intense moment and its conclusion. Developers should create memorable highlights and ensure a smooth, satisfying ending to user journeys. 
 We also discussed the Goal-Gradient Effect, which explains that users become more motivated as they approach the completion of a task. By showing progress –such as indicating that a process is “80% complete” – and breaking tasks into stages, developers can encourage users to finish what they have started. 
 In terms of system interaction, Postel’s Law advises developers to be flexible in accepting user input while maintaining strict standards for output. This means allowing different input formats while ensuring consistent and reliable system responses. 
 Performance is equally important, as highlighted by the Doherty Threshold, which shows that productivity increases when system response times stay under 400 milliseconds. Fast systems keep users engaged and create a sense of ease. 
 This means that developers should focus on building interfaces that feel instant, even when real processing takes longer, by combining smart engineering practices with thoughtful design patterns that maintain the illusion of speed. 
 Memory and attention are further explained by the Serial Position Effect, where users tend to remember the first and last items in a sequence more than those in the middle. Developers should position key information or actions at the beginning or end of lists. 
 Simplicity is reinforced by Occam’s Razor, which argues that the simplest solution is often the most effective. Eliminating unnecessary features reduces friction and enhances usability, and we further discussed about Parkinson’s Law, which suggests that tasks expand to fill the time available, indicating the importance of setting constraints such as deadlines or timers to encourage timely action. 
 These principles collectively highlight the importance of simplicity, clarity, performance, and user psychology in design. By applying them thoughtfully, developers can create intuitive, efficient, and engaging user experiences that align with both human behaviour and user expectations. 
 References 
 Budiu, R. (2022). Fitts’s Law and Its Applications in UX . [online] Nielsen Norman Group. Available at: https://www.nngroup.com/articles/fitts-law/ . 
 Bustamante, N. (2023). Gestalt Psychology? Definition, Principles, & Examples - Simply Psychology . [online] www.simplypsychology.org . Available at: https://www.simplypsychology.org/what-is-gestalt-psychology.html . 
 Cherry, K. (2024). The Zeigarnik Effect Is Why You Keep Thinking of Unfinished Work . [online] Verywell Mind. Available at: https://www.verywellmind.com/zeigarnik-effect-memory-overview-4175150 . 
 DO, A.M., RUPERT, A.V. and WOLFORD, G. (2008). Evaluations of pleasurable experiences: The peak-end rule. Psychonomic Bulletin & Review , 15(1), pp.96–98. doi: https://doi.org/10.3758/pbr.15.1.96 . 
 GUPTA, S., GUPTA, S., MAHENDRA, A. and GUPTA, S. (2006). Inverse Halo Nevus. Dermatologic Surgery , 32(6), pp.871–872. doi: https://doi.org/10.1097/00042728-200606000-00025 . 
 ‌Hall, D. (2023). Pilot Error, Chapanis and The Shape of Things to Come . [online] UX Magazine. Available at: https://uxmag.com/articles/pilot-error-chapanis-and-the-shape-of-things-to-come . 
 Hunt, R.R. (1995). The subtlety of distinctiveness: What von Restorff really did. Psychonomic Bulletin & Review , 2(1), pp.105–112. doi: https://doi.org/10.3758/bf03214414 . 
 Kahneman, D., Fredrickson, B.L., Schreiber, C.A. and Redelmeier, D.A. (1993). When More Pain Is Preferred to Less: Adding a Better End. Psychological Science , 4(6), pp.401–405. doi: https://doi.org/10.1111/j.1467-9280.1993.tb00589.x . 
 Mod, D. (2024). Doherty Threshold: UX Law of Swift Interactions . [online] Articles on everything UX: Research, Testing & Design. Available at: https://blog.uxtweak.com/doherty-threshold/ . 
 Miller, G.A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review , [online] 101(2), pp.343–352. doi: https://doi.org/10.1037/0033-295x.101.2.343 . 
 Proctor, R.W. and Schneider, D.W. (2018). Hick’s law for choice reaction time: A review. Quarterly Journal of Experimental Psychology , [online] 71(6), pp.1281–1299. doi: https://doi.org/10.1080/17470218.2017.1322622 . 
 Yablonski, J. (2022). Hick’s Law . [online] Laws of UX. Available at: https://lawsofux.com/hicks-law/ . 
 Yablonski, J. (2022). Goal-Gradient Effect . [online] Laws of UX. Available at: https://lawsofux.com/goal-gradient-effect/ . 
 ‌ 
 ‌ 
 ‌
```

---

## 5. How to Convert Images to PDF in the Browser Using JavaScript – A Step-by-Step Guide

- 日期: 2026-05-08 17:18
- 链接: https://www.freecodecamp.org/news/how-to-convert-images-to-pdf-using-javascript/

```
Whether it’s scanned documents, screenshots, receipts, notes, certificates, or multiple photos, users often need a quick way to combine images into a downloadable PDF. 
 Modern browsers make this much easier than before. 
 Instead of uploading files to a server, we can now process images directly in the browser using JavaScript. This keeps the tool fast, private, and easy to use. 
 In this tutorial, you’ll build a browser-based Image to PDF converter using JavaScript. 
 The tool will support uploading multiple images, sorting files, choosing orientation and page size, configuring margins, and merging images into either a single PDF or separate PDF files. Users will also be able to preview and download the generated document directly in the browser. 
 Everything runs entirely client-side without any backend. 
 Table of Contents 
 How Image to PDF Conversion Works 
 Project Setup 
 What Library Are We Using? 
 Creating the Upload Interface 
 Reading Uploaded Images 
 Generating the PDF 
 Handling Multiple Images 
 Configuring PDF Settings 
 Renaming and Downloading the PDF 
 Demo: How the Image to PDF Tool Works 
 Important Notes from Real-World Use 
 Common Mistakes to Avoid 
 Conclusion 
 How Image to PDF Conversion Works 
 The browser can't directly combine images into a PDF by itself. 
 Instead, we'll use a JavaScript PDF library that creates pages, inserts images, and exports everything as a downloadable PDF document. 
 The process starts when users upload one or multiple images into the browser. JavaScript then reads the image data and prepares it for PDF generation. After that, the tool creates PDF pages, inserts the uploaded images into those pages, and finally exports everything as a downloadable PDF document. 
 Everything happens locally inside the browser. 
 This means users don’t need to upload private files to a server, which makes the process faster and more privacy-friendly. 
 Project Setup 
 This project is intentionally simple. 
 You only need: 
 an HTML file 
 a JavaScript file 
 a PDF library 
 No backend or database is required. 
 What Library Are We Using? 
 We’ll use the jsPDF library. It allows us to generate PDF files directly in JavaScript. 
 Add it using a CDN: 
 <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script> Once loaded, we can create and export PDF files directly from the browser. 
 Creating the Upload Interface 
 Start with a basic upload area: 
 <input type="file" id="upload" multiple accept="image/*">

<button onclick="convertToPDF()">
 Convert to PDF
</button> This allows users to upload multiple image files and generate the PDF. 
 Here’s what the upload section looks like inside the tool: 
 You can also expand the interface with additional controls for sorting, page settings, margins, and merge modes. 
 Reading Uploaded Images 
 After users select files, we need to read them in JavaScript. 
 We can use FileReader for this: 
 const fileInput = document.getElementById("upload");

const files = fileInput.files;

for (const file of files) {
 const reader = new FileReader();

 reader.onload = function (e) {
 const imageData = e.target.result;

 console.log(imageData);
 };

 reader.readAsDataURL(file);
} This converts uploaded images into readable Base64 data that can later be inserted into the PDF. 
 Generating the PDF 
 Now we can create the PDF document. 
 const { jsPDF } = window.jspdf;

const pdf = new jsPDF(); Once the PDF is created, images can be inserted into pages: 
 pdf.addImage(imageData, "JPEG", 10, 10, 180, 120); This inserts the uploaded image into the PDF page at a specific position and size. 
 Finally, export the document: 
 pdf.save("images.pdf"); This downloads the generated PDF instantly. 
 Handling Multiple Images 
 If users upload multiple files, each image can be added to its own PDF page automatically. 
 For example: 
 files.forEach((file, index) => {

 if (index !== 0) {
 pdf.addPage();
 }

}); This creates a new page before inserting the next image into the document. 
 In some situations, users may also want multiple images on the same page instead of one image per page. 
 For example: 
 pdf.addImage(img1, "JPEG", 10, 20, 80, 80);

pdf.addImage(img2, "JPEG", 110, 20, 80, 80); This allows more flexible layouts for galleries, reports, or grouped documents. 
 Configuring PDF Settings 
 Before generating the final PDF, users can customize several layout and output settings. 
 These settings improve document quality and give users more control over the generated file. 
 Here’s what the configuration panel looks like inside the tool: 
 Sorting Images 
 When multiple images are uploaded, organizing them properly becomes important before generating the PDF. 
 Users may want to sort images alphabetically, reverse the order, or arrange them based on file size. 
 For example, images can be sorted alphabetically like this: 
 files.sort((a, b) => a.name.localeCompare(b.name)); You can also sort files by size: 
 files.sort((a, b) => a.size - b.size); Here’s an example of sorting options inside the tool: 
 This helps users organize documents more efficiently before converting them into a PDF. 
 Choosing Orientation 
 Different images work better in different page orientations. 
 Portrait orientation works well for vertical images, while landscape orientation is better for wider images. 
 For example: 
 const pdf = new jsPDF({
 orientation: "portrait"
}); You can also switch to "landscape" when needed. 
 Here’s an example of orientation options inside the tool: 
 Selecting Page Size 
 PDF page size controls the dimensions of the generated document. 
 For example: 
 const pdf = new jsPDF({
 unit: "mm",
 format: "a4"
}); This creates an A4-sized PDF document using millimeter units. 
 Other formats like letter, legal, or custom page sizes can also be supported. 
 Here’s an example of selecting page size options inside the tool: 
 Adding Margins 
 Margins create spacing between the image and the edges of the page. 
 Without margins, images may touch the borders and appear cramped. 
 For example: 
 const margin = 10;

pdf.addImage(imageData, "JPEG", margin, margin, 180, 120); Here’s an example of margins options inside the tool: 
 This creates cleaner spacing around the inserted image. 
 Automatic Image Fitting 
 One common issue when generating PDFs from images is incorrect sizing. 
 If images are inserted with fixed dimensions, they may stretch, overflow outside the page, or appear distorted. 
 Instead, it’s better to calculate image dimensions dynamically. 
 For example: 
 const pageWidth = pdf.internal.pageSize.getWidth();

const imgWidth = pageWidth - 20;

const imgHeight = (image.height * imgWidth) / image.width;

pdf.addImage(imageData, "JPEG", 10, 10, imgWidth, imgHeight); This automatically scales images proportionally while maintaining margins and layout consistency. 
 Merge Options 
 One useful feature is allowing different output modes. 
 For example, users may want to merge all uploaded images into a single PDF document when creating reports, notes, or combined files. 
 In some cases, users may prefer generating separate PDFs for each image instead of combining everything together. This can be useful when exporting individual documents or scanned pages. 
 Custom grouping is another helpful option because it allows users to combine selected images into multiple PDFs based on their own arrangement or categories. 
 These different output modes make the tool much more flexible for different real-world use cases. 
 A simple selection dropdown works well: 
 <select id="mergeMode">
 <option>Merge all into Single PDF</option>
 <option>Create Separate PDFs</option>
 <option>Custom Grouping</option>
</select> Once selected, JavaScript can apply different generation logic based on the chosen mode. 
 Here’s an example of merge mode options inside the tool: 
 This makes the tool more flexible for handling different document workflows. 
 Renaming and Downloading the PDF 
 After generating the document, users may want to rename the file before downloading. 
 You can prompt for a filename like this: 
 const fileName = prompt("Enter PDF name:", "images");

pdf.save(`${fileName}.pdf`); This gives users more control over the exported file. 
 Here’s an example of the rename popup inside the tool: 
 Demo: How the Image to PDF Tool Works 
 Step 1: Upload Images 
 Users upload one or multiple image files into the browser-based tool. 
 The tool supports common formats like JPG, PNG, and WEBP. 
 Step 2: Configure PDF Settings 
 Users can customize layout settings before generating the PDF. 
 This includes: 
 sorting images 
 orientation 
 page size 
 margins 
 merge mode 
 These settings help create cleaner PDF output. 
 Step 3: Generate the PDF 
 Once settings are configured, users click the convert button. 
 The browser processes all uploaded images locally and generates the PDF instantly. 
 Step 4: Rename the Generated File 
 Before downloading, users can rename the generated PDF. 
 This improves organization when exporting multiple documents. 
 Step 5: Download the PDF 
 Finally, the generated PDF becomes available for download directly in the browser. 
 The entire process works without uploading files to any server. 
 Important Notes from Real-World Use 
 When working with large images, performance and memory usage become important. 
 Large images can slow down PDF generation and create unnecessarily large output files. 
 For example, you can limit upload size before processing: 
 const MAX_SIZE = 10 * 1024 * 1024;

if (file.size > MAX_SIZE) {
 alert("Image is too large.");
 return;
} Another useful optimization is resizing images before inserting them into the PDF. 
 For example: 
 const canvas = document.createElement("canvas");

const ctx = canvas.getContext("2d");

canvas.width = image.width * 0.5;
canvas.height = image.height * 0.5;

ctx.drawImage(image, 0, 0, canvas.width, canvas.height);

const resizedImage = canvas.toDataURL("image/jpeg", 0.7); This reduces image dimensions and compression quality before generating the PDF. 
 It also helps reduce memory usage and improves PDF generation speed for large files. 
 Since everything runs directly inside the browser, uploaded images never leave the user’s device, which improves privacy. 
 Common Mistakes to Avoid 
 One common mistake is not validating uploaded files before processing them. 
 For example, users may upload unsupported formats or attempt to generate a PDF without selecting images. 
 Always validate input before processing: 
 if (!fileInput.files.length) {
 alert("Please upload images first.");
 return;
} Another issue is inserting very large images without resizing them first. 
 Large images can create oversized PDFs and reduce performance significantly. 
 Incorrect image positioning is also common. 
 If dimensions are hardcoded incorrectly, images may overflow outside the page or become distorted. 
 Using dynamic image sizing and margins helps prevent these layout issues. 
 Conclusion 
 In this tutorial, you built a browser-based image to PDF converter using JavaScript. 
 You learned how to upload images, generate PDF documents, configure layout settings, and export files directly inside the browser. 
 More importantly, you saw how modern browsers can handle document generation locally without relying on a backend server. 
 This approach keeps the tool fast, private, and easy to use. 
 Once you understand this workflow, you can extend it further with features like compression, drag-and-drop sorting, watermarking, batch exports, or advanced PDF editing tools. 
 You can also try a full working version here: 
 https://allinonetools.net/image-to-pdf-converter/ 
 And that’s where things start getting really interesting.
```

---

## 6. The Rise of AI Agents: How Software Is Learning to Act

- 日期: 2026-05-08 17:07
- 链接: https://www.freecodecamp.org/news/the-rise-of-ai-agents-how-software-is-learning-to-act/

```
Software has always been reactive. 
 You click a button, it responds. You call an API, it returns data. 
 Even the most sophisticated systems have historically depended on explicit instructions and tightly defined workflows. That model is starting to break. 
 A new class of software is emerging that doesn't just respond, but act. 
 This shift isn't cosmetic. It changes how software is designed, how systems are operated, and how work itself is executed. 
 Instead of encoding every step of a workflow, developers are now defining goals, constraints, and tools, then letting software figure out the execution path. The result is software that behaves less like a function and more like an operator. 
 In this article, you'll learn what AI agents actually are, how they differ from traditional software systems, and why they're starting to represent a major shift in modern software design. 
 This article is written for developers, technical founders, engineering managers, and anyone building software systems with AI components. 
 You don't need prior experience building AI agents, but it helps to be familiar with Basic Python syntax and Large language models (LLMs) 
 What We'll Cover: 
 From Deterministic Systems to Goal-Driven Execution 
 The Core Components of an AI Agent 
 Why AI Agents Are Emerging Now 
 The Illusion and Reality of Autonomy 
 Designing Agents That Work in Practice 
 Multi-Agent Systems and Coordination 
 Where AI Agents Are Already Delivering Value 
 The Shift in Software Design 
 What Comes Next 
 From Deterministic Systems to Goal-Driven Execution 
 Traditional software systems are deterministic. Given the same input, they produce the same output. 
 This predictability is what makes them reliable, but it's also what limits them. Any variation in workflow requires new code, new conditions, and new branches. 
 AI agents introduce a different model. They're goal-driven rather than instruction-driven. Instead of specifying every step, you define an objective and provide access to tools. The agent decides how to achieve the objective, often adapting in real time. 
 Consider a simple task like summarizing a set of documents and emailing the result. In a traditional system, you would write a pipeline that loads documents, processes them, formats the output, and sends an email. Each step is explicitly coded. 
 With an agent, the system might look more like this: 
 from openai import OpenAI

client = OpenAI()
goal = "Summarize all documents in /reports and email a concise briefing to the leadership team"
tools = [
 "read_files",
 "summarize_text",
 "send_email"
]
response = client.responses.create(
 model="gpt-4.1",
 input=f"Goal: {goal}. Available tools: {tools}"
)
print(response.output_text) This example is simplified, but it captures the shift. The developer defines intent and capability. The agent determines execution. 
 The Core Components of an AI Agent 
 To understand how agents work, it helps to break them into components. At a high level, most agents consist of reasoning, memory, and tools. 
 Reasoning is handled by a large language model. This is what allows the agent to interpret goals, plan actions, and adapt when something fails. It's not just generating text, it's generating decisions. 
 Memory allows the agent to maintain context across steps. Without memory, the agent behaves like a stateless function. With memory, it can track progress, recall past actions, and refine its approach. 
 Tools are what make the agent useful . A tool can be anything from an API to a database query to a shell command. The agent doesn't need to know how the tool works internally. It only needs to know when and how to use it. 
 Here is a minimal example of tool usage in an agent loop: 
 def agent_loop(goal, tools):
 context = []
 
 while True:
 prompt = f"Goal: {goal}\nContext: {context}\nWhat should be done next?"
 
 decision = model.generate(prompt)
 
 if decision == "DONE":
 break
 
 if decision.startswith("USE_TOOL"):
 tool_name, tool_input = parse_tool_call(decision)
 result = tools[tool_name](tool_input)
 context.append(result)
 else:
 context.append(decision)
 
 return context This loop is where the agent “acts.” It observes, decides, executes, and updates its understanding. 
 Why AI Agents Are Emerging Now 
 The idea of autonomous software isn't new. What has changed is the capability of the underlying models. 
 Large language models can now reason across multiple steps, interpret unstructured inputs, and generate structured outputs that can drive real systems. 
 Equally important is the ecosystem around them. APIs are more standardized, infrastructure is more programmable, and data is more accessible. This makes it easier to expose tools and let them interact with real systems helping build some of the best AI agents in use today. 
 There's also an economic driver. Many workflows today are still manual, even in highly digitized organizations. These workflows often involve coordination across systems, interpretation of data, and decision-making under uncertainty. This is exactly the kind of work agents are suited for. 
 The Illusion and Reality of Autonomy 
 It's tempting to describe AI agents as fully autonomous. In practice, most are not. They operate within constraints defined by developers. They rely on tools that expose only certain actions. They're often monitored, rate-limited, and evaluated at each step. 
 What makes them different isn't complete autonomy, but partial autonomy. They can decide how to execute within a bounded environment. 
 This distinction matters because it affects how systems are designed. You're not building a system that always behaves predictably. You're building a system that explores a solution space and converges on an outcome. 
 That introduces new challenges. Agents can take inefficient paths. They can misinterpret goals. They can fail in ways that are hard to debug because the failure isn't a single error, but a chain of decisions. 
 Designing Agents That Work in Practice 
 Building an agent is easy. Building one that works reliably is harder. The difference comes down to control. 
 One approach is to constrain the agent’s action space . Instead of giving it open-ended access, you define a limited set of tools with clear interfaces. This reduces ambiguity and makes behavior more predictable. 
 Another approach is to introduce intermediate checkpoints. Instead of letting the agent run freely, you validate its decisions at key steps. You can do this through rules, secondary models, or even human review. 
 Here's an example of adding a validation layer: 
 def safe_execute(tool, input_data):
 if not validate_input(tool, input_data):
 return "Invalid input"
 
 result = tool(input_data)
 
 if not validate_output(tool, result):
 return "Invalid output"
 
 return result This pattern is critical in production systems. It turns an unconstrained agent into a controlled system that can still adapt, but within safe boundaries. 
 Multi-Agent Systems and Coordination 
 As agents become more capable, a single agent is often not enough. Complex tasks can be decomposed into multiple agents, each responsible for a specific function. 
 For example, one agent might handle data retrieval, another might handle analysis, and a third might handle communication. These agents can coordinate by passing structured messages. 
 class Message:
 def __init__(self, sender, receiver, content):
 self.sender = sender
 self.receiver = receiver
 self.content = content

def send_message(agent, message):
 return agent.process(message)
message = Message("retriever", "analyst", "Data collected from API")
response = send_message(analyst_agent, message) This model starts to resemble a distributed system, but with agents instead of services. Coordination becomes a first-class concern. You need to define protocols, handle failures, and ensure consistency across agents. 
 Where AI Agents Are Already Delivering Value 
 Despite the hype, there are concrete areas where agents are already useful. Internal tooling is one of them. Automating repetitive workflows, generating reports, and orchestrating tasks across systems are all well-suited for agents. 
 Customer support is another area. Agents can handle complex queries that require accessing multiple systems, not just retrieving canned responses. 
 Security and compliance workflows are also a strong fit. These often involve monitoring signals, correlating data, and taking action based on rules that aren't always deterministic. 
 What these use cases have in common is that they involve structured environments with clear objectives and measurable outcomes. Agents perform best when the problem space is bounded, even if the execution path is not. 
 The Shift in Software Design 
 The rise of AI agents isn't just about adding a new feature. It's about changing the abstraction layer of software. 
 Instead of writing code that directly implements behavior, you're designing systems that enable behavior. You define goals, expose capabilities, and enforce constraints. The actual execution becomes dynamic. 
 This requires a different mindset. Debugging is no longer just about tracing code. It's about understanding decision paths. Testing is no longer just about input-output pairs. It's about evaluating behavior across scenarios. 
 Observability becomes critical. You need to log not just what the system did, but why it did it. This includes prompts, intermediate decisions, and tool interactions. 
 What Comes Next 
 AI agents are still in the relatively early stages. The current generation is powerful but imperfect. Reliability is a major challenge. So is cost, especially when agents require multiple model calls per task. 
 But the direction is clear: software is moving from static execution to dynamic action. The boundary between user and system is becoming less rigid. Instead of telling software what to do step by step, users will increasingly define outcomes and let systems figure out the rest. 
 This doesn't eliminate the need for engineers. It changes what engineers do. The focus shifts from implementing logic to designing systems that can reason, act, and adapt. 
 The rise of AI agents marks a transition. Software is no longer just a tool. It's becoming an actor. 
 Join my Applied AI newsletter to learn how to build and ship real AI systems. Practical projects, production-ready code, and direct Q&A. You can also connect with me on LinkedIn .
```

---

## 7. How to Build a Complete SaaS Payment Flow with Stripe, Webhooks, and Email Notifications

- 日期: 2026-05-08 15:58
- 链接: https://www.freecodecamp.org/news/saas-payment-flow-stripe-webhooks-email/

```
Most Stripe tutorials end at the checkout page. The customer clicks "Pay," Stripe processes the charge, and the tutorial congratulates you on integrating payments. 
 But that's only the first 10% of a real payment system. 
 What happens after the customer pays? You need to record the purchase in your database, send a confirmation email, and grant product access (a GitHub repo invitation, an API key, a license file). You need to notify yourself as the admin. You need to handle refunds two weeks later and send recovery emails when someone abandons checkout. 
 This is the complete payment lifecycle, and it's where most SaaS applications break. 
 This article walks you through building the entire flow, from the "Buy" button to the "Welcome" email and everything in between. Every code example comes from a production application processing real payments. You'll see how to design the database schema, create Stripe products, build the checkout flow, process purchases reliably, handle refunds, recover abandoned carts, and send transactional emails. 
 Here is what you'll learn: 
 How to design a database schema that tracks every stage of a purchase 
 How to create Stripe products and prices programmatically 
 How to build a checkout flow with success/cancel handling 
 How to process webhooks securely with signature verification 
 How to split post-payment processing into durable, independently retried steps 
 How to handle full and partial refunds with automatic access revocation 
 How to recover revenue from abandoned checkouts 
 How to build transactional email templates with React Email and Resend 
 How to test the entire flow locally with Stripe CLI and Inngest 
 Table of Contents 
 Prerequisites 
 How to Design the Payment Database Schema 
 How to Create Stripe Products and Prices 
 How to Build the Checkout Flow 
 How to Handle Webhooks Securely 
 How to Process Purchases with Durable Background Jobs 
 How to Handle Refunds 
 How to Recover Abandoned Checkouts 
 How to Send Transactional Emails with React Email 
 How to Test the Complete Flow Locally 
 Conclusion 
 Prerequisites 
 To follow along, you should be familiar with: 
 TypeScript and Node.js 
 SQL databases (the examples use PostgreSQL) 
 React (for email templates) 
 Basic understanding of webhooks 
 You don't need prior experience with any of the specific libraries. This handbook explains each one as it appears. 
 What You Need Installed 
 Install these packages to run the code examples: 
 bun add stripe drizzle-orm @neondatabase/serverless inngest resend @react-email/components You'll also need: 
 A Stripe account (test mode is fine) 
 A Neon PostgreSQL database (or any PostgreSQL instance) 
 A Resend account for sending emails 
 The Stripe CLI for local webhook testing 
 Environment Variables 
 Set up these environment variables in your .env file: 
 # Database
DATABASE_URL=postgresql://...

# Stripe
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
STRIPE_PRO_PRICE_ID=price_...

# Email
RESEND_API_KEY=re_...
EMAIL_FROM="Your App <noreply@mail.yourapp.com>"
ADMIN_EMAIL=you@yourapp.com

# App
BETTER_AUTH_URL=http://localhost:3000 How to Design the Payment Database Schema 
 Before writing any Stripe code, you need a database schema that can track a purchase through every stage of its lifecycle: creation, completion, partial refund, and full refund. 
 A purchase starts as pending when the user clicks "Buy." After Stripe confirms payment, it transitions to completed . From there, it can move to refunded or partially_refunded . Pending purchases that are never completed expire after 24 hours (abandoned carts). 
 Here is the schema I use in production, defined with Drizzle ORM . The examples throughout this article grant access to a private GitHub repository because that's what this particular product sells. 
 Your "grant access" step will be different: upgrading a user to a Pro plan, provisioning API credits, unlocking course content, or activating a subscription. The schema fields and step logic change, but the durable execution pattern is the same. 
 // src/lib/db/schema.ts
import {
 boolean,
 integer,
 pgEnum,
 pgTable,
 text,
 timestamp,
 varchar,
} from "drizzle-orm/pg-core";

export const purchaseTierEnum = pgEnum("purchase_tier", ["pro"]);
export const purchaseStatusEnum = pgEnum("purchase_status", [
 "completed",
 "partially_refunded",
 "refunded",
]);

export const users = pgTable("users", {
 id: text("id").primaryKey(),
 email: varchar("email", { length: 255 }).notNull().unique(),
 emailVerified: boolean("email_verified").notNull().default(false),
 name: text("name"),
 image: text("image"),
 githubUsername: text("github_username"),
 createdAt: timestamp("created_at").notNull().defaultNow(),
 updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

export const purchases = pgTable("purchases", {
 id: text("id")
 .primaryKey()
 .$defaultFn(() => crypto.randomUUID()),
 userId: text("user_id")
 .notNull()
 .references(() => users.id, { onDelete: "cascade" }),
 stripeCheckoutSessionId: text("stripe_checkout_session_id")
 .notNull()
 .unique(),
 stripeCustomerId: text("stripe_customer_id"),
 stripePaymentIntentId: text("stripe_payment_intent_id"),
 tier: purchaseTierEnum("tier").notNull(),
 status: purchaseStatusEnum("status").notNull().default("completed"),
 githubAccessGranted: boolean("github_access_granted")
 .notNull()
 .default(false),
 githubInvitationId: text("github_invitation_id"),
 amount: integer("amount").notNull(),
 currency: text("currency").notNull().default("usd"),
 purchasedAt: timestamp("purchased_at").notNull().defaultNow(),
 createdAt: timestamp("created_at").notNull().defaultNow(),
 updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

export type Purchase = typeof purchases.$inferSelect;
export type NewPurchase = typeof purchases.$inferInsert; Let me walk through the design decisions behind this schema. 
 Why Three Stripe ID Columns? 
 The purchases table stores three separate Stripe identifiers: stripeCheckoutSessionId , stripeCustomerId , and stripePaymentIntentId . 
 Each one serves a different purpose. 
 The checkout session ID is what you receive first. When a customer starts checkout, Stripe creates a session and gives you this ID. You use it to claim the purchase after the customer returns from Stripe's hosted checkout page. 
 The unique() constraint on this column is your idempotency guard. If someone tries to claim the same session twice, the database rejects the second insert. 
 The customer ID is Stripe's internal identifier for the buyer. You need this to look up the customer's payment history in Stripe's dashboard and to create future checkout sessions pre-filled with their billing info. 
 The payment intent ID is what Stripe sends in refund webhook events. When a charge.refunded event fires, it includes the payment intent ID but not the checkout session ID. Without storing this field, you would have no way to match a refund back to a purchase in your database. 
 Why Track Access State in Your Database 
 The githubAccessGranted and githubInvitationId fields might look unnecessary. You could check GitHub's API to see if a user has access. But querying an external API every time you need to check a user's access state is slow, rate-limited, and unreliable. 
 By tracking access state in your own database, you can answer "does this user have access?" with a single indexed query. You also know whether access was ever granted, which is critical for refund processing. If githubAccessGranted is false , you don't need to revoke anything on refund. 
 Why a Status Enum with Three Values? 
 The purchaseStatusEnum has three values: completed , partially_refunded , and refunded . 
 This matters for downstream logic. Your dashboard, analytics, support tools, and email sequences all need to know the exact state of a purchase. A partially refunded customer still has access, but a fully refunded customer doesn't. 
 If you only tracked "refunded" as a boolean, you would lose the distinction between partial and full refunds. That distinction affects whether you revoke product access. 
 How to Generate and Run Migrations 
 After defining your schema, generate a migration file and apply it to your database: 
 # Generate migration SQL from schema changes
bun run drizzle-kit generate

# Push schema directly (development only)
bun run drizzle-kit push

# Run migrations (production)
bun run drizzle-kit migrate Drizzle Kit compares your TypeScript schema to the database and generates the SQL needed to bring them in sync. Review the generated migration file before running it in production. Schema changes are one of the few things you can't easily undo. 
 For development, drizzle-kit push is faster because it applies changes directly without creating migration files. For production, always use drizzle-kit generate followed by drizzle-kit migrate so you have a versioned record of every schema change. 
 How to Create Stripe Products and Prices 
 You can create products and prices through the Stripe dashboard, but managing them programmatically is better for reproducibility. Here's a seed script that creates everything you need: 
 // src/lib/payments/seed.ts
import { stripe } from "./index";

const PRODUCTS = [
 {
 name: "My SaaS Product",
 description: "Full access, one-time purchase",
 features: [
 "Full source code access",
 "Production-ready infrastructure",
 "Lifetime updates",
 ],
 metadata: { tier: "pro" },
 prices: [
 {
 lookupKey: "pro_one_time",
 unitAmount: 19900, // $199.00 in cents
 currency: "usd",
 nickname: "Pro One-Time",
 },
 ],
 },
];

async function main() {
 console.log("Seeding Stripe products and prices...\n");

 for (const config of PRODUCTS) {
 // Create or find product
 const products = await stripe.products.list({ active: true, limit: 100 });
 let product = products.data.find((p) => p.name === config.name);

 if (!product) {
 product = await stripe.products.create({
 name: config.name,
 description: config.description,
 marketing_features: config.features.map((f) => ({ name: f })),
 metadata: config.metadata,
 });
 console.log(`Created product "\({config.name}" (\){product.id})`);
 }

 // Create prices
 for (const priceConfig of config.prices) {
 const existing = await stripe.prices.list({
 lookup_keys: [priceConfig.lookupKey],
 active: true,
 limit: 1,
 });

 if (existing.data[0]) {
 console.log(`Price "${priceConfig.lookupKey}" already exists`);
 continue;
 }

 const price = await stripe.prices.create({
 product: product.id,
 unit_amount: priceConfig.unitAmount,
 currency: priceConfig.currency,
 nickname: priceConfig.nickname,
 lookup_key: priceConfig.lookupKey,
 transfer_lookup_key: true,
 });

 console.log(`Created price "\({priceConfig.lookupKey}" (\){price.id})`);
 }
 }

 console.log("\nDone! Add the price ID to your .env as STRIPE_PRO_PRICE_ID");
}

main().catch(console.error); Run this with bun run src/lib/payments/seed.ts . 
 A few things worth noting. 
 Use lookup_key instead of hardcoding price IDs: Price IDs are different between test and live mode. Lookup keys let you reference prices by name ( pro_one_time ) rather than by Stripe's generated ID ( price_1P... ). 
 The transfer_lookup_key: true option ensures that if you create a new price with the same lookup key, it replaces the old one automatically. 
 Prices are in cents: Stripe's API expects amounts in the smallest currency unit. For USD, that means 19900 represents $199.00. 
 This is a common source of bugs. Always store amounts in cents in your database and convert to dollars only at the display layer. 
 The seed script is idempotent: You can run it multiple times safely. It checks for existing products and prices before creating new ones. 
 How to Set Up the Stripe Client 
 The Stripe client uses lazy initialization so that importing it doesn't throw if the API key is missing at module load time. This matters in build environments where environment variables aren't set. 
 // src/lib/payments/index.ts
import Stripe from "stripe";

let stripeClient: Stripe | null = null;

function getStripe(): Stripe {
 if (!stripeClient) {
 const secretKey = process.env.STRIPE_SECRET_KEY;
 if (!secretKey) {
 throw new Error("STRIPE_SECRET_KEY is not set");
 }
 stripeClient = new Stripe(secretKey);
 }
 return stripeClient;
}

export const stripe = new Proxy({} as Stripe, {
 get(_, prop) {
 return Reflect.get(getStripe(), prop);
 },
}); The Proxy wrapper is the key pattern here. Code across your application imports stripe and calls methods like stripe.checkout.sessions.create(...) . The proxy intercepts every property access and forwards it to the lazily initialized client. 
 This means the Stripe SDK only initializes when you actually use it, not when the module is imported. 
 How to Build the Checkout Flow 
 The checkout flow has three parts: creating the session, redirecting the customer, and handling the return. 
 How to Create a Checkout Session 
 Here's the function that creates a Stripe Checkout session for a one-time payment: 
 // src/lib/payments/index.ts
export async function createOneTimeCheckoutSession(params: {
 priceId: string;
 successUrl: string;
 cancelUrl: string;
 metadata: Record<string, string>;
 customerEmail?: string;
 couponId?: string;
}) {
 const client = getStripe();

 const session = await client.checkout.sessions.create({
 mode: "payment",
 line_items: [{ price: params.priceId, quantity: 1 }],
 success_url: params.successUrl,
 cancel_url: params.cancelUrl,
 metadata: params.metadata,
 ...(params.customerEmail && {
 customer_email: params.customerEmail,
 }),
 ...(params.couponId
 ? { discounts: [{ coupon: params.couponId }] }
 : { allow_promotion_codes: true }),
 });

 return session;
} Three details matter here. 
 The mode: "payment" setting tells Stripe this is a one-time charge , not a subscription. For subscriptions, you would use mode: "subscription" . The mode affects which webhook events Stripe sends after payment. 
 The metadata field is how you link the Stripe session back to your application. Pass your internal product tier, user ID, or any other data you need after payment. Stripe stores this metadata and includes it in webhook events and API responses. 
 The allow_promotion_codes: true option shows a promo code field on the checkout page. If you have a specific coupon to apply (from a landing page URL parameter, for example), pass it via discounts instead. You can't use both at the same time. 
 How to Create the Checkout API Endpoint 
 Here's the API endpoint that creates a checkout session and returns the URL: 
 // src/server/api.ts
app.post("/api/payments/checkout", async ({ set }) => {
 const priceId = process.env.STRIPE_PRO_PRICE_ID;

 if (!priceId) {
 set.status = 500;
 return { error: "Price not configured" };
 }

 const baseUrl = process.env.BETTER_AUTH_URL ?? "http://localhost:3000";
 const tier = "pro";

 const checkoutSession = await createOneTimeCheckoutSession({
 priceId,
 successUrl: `${baseUrl}/dashboard?purchase=success&session_id={CHECKOUT_SESSION_ID}`,
 cancelUrl: `${baseUrl}/pricing`,
 metadata: { tier },
 });

 return { url: checkoutSession.url };
}); The {CHECKOUT_SESSION_ID} placeholder in the success URL is a Stripe template variable. Stripe replaces it with the actual session ID when redirecting the customer. This lets your frontend know which session just completed. 
 How to Claim the Purchase After Checkout 
 When the customer returns to your success URL, your frontend reads the session_id from the URL and sends it to a "claim" endpoint. This endpoint verifies the payment and creates the purchase record. 
 // src/server/api.ts
app.post(
 "/api/purchases/claim",
 async ({ body, request, set }) => {
 const session = await auth.api.getSession({
 headers: request.headers,
 });

 if (!session) {
 set.status = 401;
 return { error: "Unauthorized" };
 }

 const { sessionId } = body;

 // Check if this session was already claimed
 const existing = await db
 .select()
 .from(purchases)
 .where(eq(purchases.stripeCheckoutSessionId, sessionId))
 .limit(1);

 if (existing[0]) {
 return { success: true, alreadyClaimed: true, tier: existing[0].tier };
 }

 // Retrieve the Stripe checkout session to verify payment
 const stripeSession = await retrieveCheckoutSession(sessionId);

 if (stripeSession.payment_status !== "paid") {
 set.status = 400;
 return { error: "Payment not completed" };
 }

 const tier = (stripeSession.metadata?.tier ?? "pro") as PaymentTier;

 // Create purchase record
 await db.insert(purchases).values({
 userId: session.user.id,
 stripeCheckoutSessionId: sessionId,
 stripeCustomerId:
 typeof stripeSession.customer === "string"
 ? stripeSession.customer
 : stripeSession.customer?.id ?? null,
 stripePaymentIntentId:
 typeof stripeSession.payment_intent === "string"
 ? stripeSession.payment_intent
 : stripeSession.payment_intent?.id ?? null,
 tier,
 status: "completed",
 amount: stripeSession.amount_total ?? 0,
 currency: stripeSession.currency ?? "usd",
 });

 // Trigger background processing
 await inngest.send({
 name: "purchase/completed",
 data: {
 userId: session.user.id,
 tier,
 sessionId,
 },
 });

 return { success: true, tier };
 },
 {
 body: t.Object({
 sessionId: t.String(),
 }),
 }
); This endpoint does four things, in order. 
 First, it checks if the session was already claimed. The unique() constraint on stripeCheckoutSessionId in the schema prevents duplicate records, but checking first lets you return a clean response without catching a database error. 
 Second, it verifies payment with Stripe. Never trust data from the client. The frontend passes the session ID, but you must call Stripe's API to confirm that payment_status is "paid" . 
 Third, it creates the purchase record. Notice how it extracts the customer and payment_intent from the Stripe session. Both fields are returned as either strings or expanded objects depending on your Stripe API settings, so the ternary handles both cases. 
 Fourth, it sends a purchase/completed event to Inngest. This triggers the background processing flow that handles emails, access grants, analytics, and follow-up scheduling. The API endpoint doesn't do any of that work and returns { success: true } immediately. 
 This separation between recording the purchase and processing it is fundamental. The database insert is fast and reliable. The downstream processing (emails, API calls, analytics) is slow and unreliable. 
 By splitting them, you ensure the customer sees a success response instantly while the background work happens durably. 
 How to Handle Webhooks Securely 
 Your webhook endpoint is the entry point for Stripe events that happen outside your checkout flow: refunds, expired sessions, and disputes. 
 How to Verify Webhook Signatures 
 Every webhook from Stripe includes a signature header. You must verify this signature before processing the event. Without verification, anyone could send fake events to your webhook URL. 
 // src/lib/payments/index.ts
export async function constructWebhookEvent(
 payload: string | Buffer,
 signature: string
) {
 const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;
 if (!webhookSecret) {
 throw new Error("STRIPE_WEBHOOK_SECRET is not set");
 }
 const client = getStripe();
 return client.webhooks.constructEventAsync(payload, signature, webhookSecret);
} One critical detail: use constructEventAsync instead of constructEvent . The async version uses the Web Crypto API, which is compatible with modern runtimes like Bun and Cloudflare Workers. The synchronous version depends on Node.js's crypto module, which isn't available everywhere. 
 Another critical detail: pass the raw request body to signature verification. If your framework parses the body as JSON before you access it, the signature check fails. The signature is computed over the raw bytes of the request, not the parsed JSON. 
 How to Build the Webhook Endpoint 
 Here is the production webhook handler. Its only job is to validate the event and route it to the background job system. 
 // src/server/api.ts
app.post("/api/payments/webhook", async ({ request, set }) => {
 const body = await request.text();
 const sig = request.headers.get("stripe-signature");

 if (!sig) {
 set.status = 400;
 return { error: "Missing signature" };
 }

 try {
 const event = await constructWebhookEvent(body, sig);
 console.log(`[Webhook] Received ${event.type}`);

 if (event.type === "charge.refunded") {
 const charge = event.data.object as {
 id: string;
 payment_intent: string;
 amount: number;
 amount_refunded: number;
 currency: string;
 };
 await inngest.send({
 name: "stripe/charge.refunded",
 data: {
 chargeId: charge.id,
 paymentIntentId: charge.payment_intent,
 amountRefunded: charge.amount_refunded,
 originalAmount: charge.amount,
 currency: charge.currency,
 },
 });
 }

 if (event.type === "checkout.session.expired") {
 const session = event.data.object as {
 id: string;
 customer_email: string | null;
 };
 await inngest.send({
 name: "stripe/checkout.session.expired",
 data: {
 sessionId: session.id,
 customerEmail: session.customer_email,
 },
 });
 }

 return { received: true };
 } catch (error) {
 console.error("[Webhook] Stripe verification failed:", error);
 set.status = 400;
 return { error: "Webhook verification failed" };
 }
}); This is the "thin webhook handler" pattern. Notice what it does not do: it does not query the database, send emails, grant access, or call any external service. It validates the signature, extracts the fields it needs, and sends a typed event to Inngest. 
 The entire handler completes in milliseconds. 
 Why does this matter? Stripe expects your webhook to return a 2xx response within about 20 seconds. If your handler tries to do too much work (database queries, email sends, API calls), it risks timing out. 
 Stripe marks it as failed and retries the entire event. Now you have partial completion and duplicate processing. 
 The thin handler avoids this entirely. Validate, enqueue, return. All the real work happens asynchronously in durable background functions. 
 Why Extract Fields Before Enqueueing? 
 You might notice that the webhook handler extracts specific fields from the Stripe event before sending them to Inngest: 
 await inngest.send({
 name: "stripe/charge.refunded",
 data: {
 chargeId: charge.id,
 paymentIntentId: charge.payment_intent,
 amountRefunded: charge.amount_refunded,
 originalAmount: charge.amount,
 currency: charge.currency,
 },
}); Why not forward the entire Stripe event? Two reasons. 
 First, Stripe event objects are large and deeply nested. Your background function only needs five fields. Sending the entire object means your durable function stores a large payload at every checkpoint, and over thousands of runs, this adds up. 
 Second, extracting fields at the boundary creates a clean contract between your webhook handler and your background functions. If Stripe changes the shape of their event objects in a future API version, you only need to update the extraction logic in the webhook handler. Your background functions keep working because they depend on your own typed data shape, not Stripe's. 
 How to Set Up Webhooks in Production 
 For production, you configure webhooks in the Stripe Dashboard: 
 Go to Stripe Dashboard, then Developers, then Webhooks. 
 Add an endpoint pointing to your production URL: https://yourapp.com/api/payments/webhook . 
 Select the events you want to receive: charge.refunded and checkout.session.expired . 
 Copy the signing secret and add it to your production environment variables as STRIPE_WEBHOOK_SECRET . 
 The production signing secret is different from the one the Stripe CLI generates for local testing. Make sure your environment variables are set correctly for each environment. 
 Which Webhook Events to Listen For 
 For a complete payment flow, you need these webhook events configured in Stripe: 
 Event When It Fires What You Do 
 charge.refunded Customer receives a refund Revoke access (full refund) or update status (partial) 
 checkout.session.expired Checkout session times out (24 hours) Send abandoned cart recovery email 
 For subscription-based billing, you would also listen for customer.subscription.updated , customer.subscription.deleted , and invoice.payment_failed . This article covers one-time payments, so the examples focus on the two events above. 
 The checkout.session.completed event is notably absent. For one-time payments, you typically process the purchase in the "claim" endpoint (shown in the previous section) rather than in a webhook, because you need the authenticated user's session to link the purchase to their account. 
 How to Process Purchases with Durable Background Jobs 
 This is the heart of the payment flow. After the purchase record is created and the purchase/completed event is sent, a durable function takes over and runs the entire post-payment workflow. 
 Each step in this function is individually checkpointed. If step 5 fails, steps 1 through 4 don't re-run. Step 5 retries on its own, and once it succeeds, steps 6 through 9 continue. 
 This is what "durable execution" means. It's the difference between a payment system that works in development and one that works in production. 
 I use Inngest for this. It is an event-driven durable execution platform that provides step-level checkpointing out of the box. You define functions with step.run() blocks, and Inngest handles retry logic, state persistence, and observability. 
 The Inngest client setup is minimal: 
 // src/lib/jobs/client.ts
import { Inngest } from "inngest";

export const inngest = new Inngest({
 id: "my-app",
}); Register your functions with the Inngest serve handler so the dev server (and production) can discover them: 
 import { serve } from "inngest/bun";
import { inngest } from "@/lib/jobs/client";
import { stripeFunctions } from "@/lib/jobs/functions/stripe";

const inngestHandler = serve({
 client: inngest,
 functions: [...stripeFunctions],
});

// Mount on your API
app.all("/api/inngest", async (ctx) => {
 return inngestHandler(ctx.request);
}); Here's the complete purchase function: 
 // src/lib/jobs/functions/stripe.ts
import { eq } from "drizzle-orm";
import { createElement } from "react";

import { inngest } from "../client";
import { trackServerEvent } from "@/lib/analytics/server";
import { brand } from "@/lib/brand";
import { db, purchases, users } from "@/lib/db";
import {
 sendEmail,
 PurchaseConfirmationEmail,
 AdminPurchaseNotificationEmail,
 RepoAccessGrantedEmail,
} from "@/lib/email";
import { addCollaborator } from "@/lib/github";

export const handlePurchaseCompleted = inngest.createFunction(
 { id: "purchase-completed", triggers: [{ event: "purchase/completed" }] },
 async ({ event, step }) => {
 const { userId, tier, sessionId } = event.data as {
 userId: string;
 tier: string;
 sessionId: string;
 };

 // Step 1: Look up user and purchase details
 const { user, purchase } = await step.run(
 "lookup-user-and-purchase",
 async () => {
 const userResult = await db
 .select({
 id: users.id,
 email: users.email,
 name: users.name,
 githubUsername: users.githubUsername,
 })
 .from(users)
 .where(eq(users.id, userId))
 .limit(1);

 const foundUser = userResult[0];
 if (!foundUser) {
 throw new Error(`User not found: ${userId}`);
 }

 const purchaseResult = await db
 .select({
 amount: purchases.amount,
 currency: purchases.currency,
 stripePaymentIntentId: purchases.stripePaymentIntentId,
 })
 .from(purchases)
 .where(eq(purchases.stripeCheckoutSessionId, sessionId))
 .limit(1);

 const foundPurchase = purchaseResult[0];

 return {
 user: foundUser,
 purchase: foundPurchase ?? {
 amount: 0,
 currency: "usd",
 stripePaymentIntentId: null,
 },
 };
 }
 );

 // Step 2: Track purchase in analytics
 await step.run("track-purchase-to-posthog", async () => {
 try {
 await trackServerEvent(userId, "purchase_completed_server", {
 tier,
 amount_cents: purchase.amount,
 currency: purchase.currency,
 stripe_session_id: sessionId,
 stripe_payment_intent_id: purchase.stripePaymentIntentId,
 });
 } catch (error) {
 console.error(`Failed to track to PostHog:`, error);
 }
 });

 // Step 3: Send purchase confirmation to customer
 await step.run("send-purchase-confirmation", async () => {
 await sendEmail({
 to: user.email,
 subject: `Your ${brand.name} purchase is confirmed!`,
 template: createElement(PurchaseConfirmationEmail, {
 amount: purchase.amount,
 currency: purchase.currency,
 customerEmail: user.email,
 }),
 });
 });

 // Step 4: Send admin notification
 await step.run("send-admin-notification", async () => {
 const adminEmail = process.env.ADMIN_EMAIL;
 if (!adminEmail) return;

 await sendEmail({
 to: adminEmail,
 subject: `New template sale: ${user.email}`,
 template: createElement(AdminPurchaseNotificationEmail, {
 amount: purchase.amount,
 currency: purchase.currency,
 customerEmail: user.email,
 customerName: user.name,
 stripeSessionId: purchase.stripePaymentIntentId ?? sessionId,
 }),
 });
 });

 // Early return if user has no GitHub username
 if (!user.githubUsername) {
 return { success: true, userId, tier, githubAccessGranted: false };
 }

 // Step 5: Grant GitHub repository access
 const collaboratorResult = await step.run(
 "add-github-collaborator",
 async () => {
 return addCollaborator(user.githubUsername!);
 }
 );

 // Step 6: Track GitHub access granted
 await step.run("track-github-access", async () => {
 await trackServerEvent(userId, "github_access_granted", {
 tier,
 github_username: user.githubUsername,
 invitation_status: collaboratorResult.status,
 });
 });

 // Step 7: Update purchase record
 await step.run("update-purchase-record", async () => {
 await db
 .update(purchases)
 .set({
 githubAccessGranted: true,
 githubInvitationId: collaboratorResult.status,
 updatedAt: new Date(),
 })
 .where(eq(purchases.stripeCheckoutSessionId, sessionId));
 });

 // Step 8: Send repo access email
 await step.run("send-repo-access-email", async () => {
 const repoUrl = brand.social.github;
 await sendEmail({
 to: user.email,
 subject: `Your ${brand.name} repository access is ready!`,
 template: createElement(RepoAccessGrantedEmail, { repoUrl }),
 });
 });

 // Step 9: Schedule follow-up email sequence
 await step.run("schedule-follow-up", async () => {
 const purchaseRecord = await db
 .select({ id: purchases.id })
 .from(purchases)
 .where(eq(purchases.stripeCheckoutSessionId, sessionId))
 .limit(1);

 if (purchaseRecord[0]) {
 await inngest.send({
 name: "purchase/follow-up.scheduled",
 data: {
 userId,
 purchaseId: purchaseRecord[0].id,
 tier,
 },
 });
 }
 });

 return { success: true, userId, tier, githubAccessGranted: true };
 }
); That's a lot of code. Let me break down why each step exists and why it must be separate. 
 Step 1: Look Up User and Purchase 
 const { user, purchase } = await step.run(
 "lookup-user-and-purchase",
 async () => {
 // Database queries for user and purchase records
 return { user: foundUser, purchase: foundPurchase };
 }
); This step queries the database for the user and purchase details. Every subsequent step depends on these values (the user's email, the purchase amount, the user's GitHub username). 
 Because this is wrapped in step.run() , the return value is cached by Inngest. If a later step fails and the function retries, this step doesn't re-run. The cached values are replayed instead. 
 If the user doesn't exist in the database, this step throws an error that halts the entire function. There's no point continuing if the user can't be found. 
 Step 2: Track Analytics 
 await step.run("track-purchase-to-posthog", async () => {
 try {
 await trackServerEvent(userId, "purchase_completed_server", {
 tier,
 amount_cents: purchase.amount,
 currency: purchase.currency,
 });
 } catch (error) {
 console.error(`Failed to track to PostHog:`, error);
 }
}); Analytics tracking gets its own step because analytics services have their own failure modes. PostHog could be rate-limited or temporarily unreachable. If that happens, you don't want it to block the confirmation email. 
 Notice the try-catch. A tracking failure logs the error but doesn't halt the function. Analytics data is valuable but not critical to the purchase flow. 
 Steps 3 and 4: Email Notifications 
 The customer confirmation and admin notification are separate steps because they are independent operations. If Resend returns a 500 when sending the admin email, the customer should still get their confirmation. 
 // Step 3: Customer confirmation
await step.run("send-purchase-confirmation", async () => {
 await sendEmail({
 to: user.email,
 subject: `Your ${brand.name} purchase is confirmed!`,
 template: createElement(PurchaseConfirmationEmail, {
 amount: purchase.amount,
 currency: purchase.currency,
 customerEmail: user.email,
 }),
 });
});

// Step 4: Admin notification
await step.run("send-admin-notification", async () => {
 const adminEmail = process.env.ADMIN_EMAIL;
 if (!adminEmail) return;

 await sendEmail({
 to: adminEmail,
 subject: `New template sale: ${user.email}`,
 template: createElement(AdminPurchaseNotificationEmail, {
 // ... admin-specific fields
 }),
 });
}); The admin notification step includes a guard: if ADMIN_EMAIL isn't set, it returns early. This makes the function work in development environments where you haven't configured all environment variables. 
 Step 5: Grant Product Access 
 if (!user.githubUsername) {
 return { success: true, userId, tier, githubAccessGranted: false };
}

const collaboratorResult = await step.run(
 "add-github-collaborator",
 async () => {
 return addCollaborator(user.githubUsername!);
 }
); This is the step most likely to fail. GitHub's API has rate limits, can time out, and the user's GitHub username might be invalid. 
 By making it its own step, a GitHub API failure doesn't re-trigger the confirmation email (step 3) or the admin notification (step 4). Those are already checkpointed. 
 Notice the early return before step 5. If the user has no GitHub username linked, the function returns after step 4. The remaining steps only run when there's a GitHub account to grant access to. 
 Steps 6-7: Track and Update 
 After granting GitHub access, the function tracks the event in analytics (step 6) and updates the purchase record in the database (step 7). 
 The database update is intentionally ordered after the GitHub API call. You only set githubAccessGranted: true after the invitation actually succeeded. If you updated the record first and the GitHub step failed, your database would say access was granted when it was not. 
 Step 8: Send Access Email 
 await step.run("send-repo-access-email", async () => {
 const repoUrl = brand.social.github;
 await sendEmail({
 to: user.email,
 subject: `Your ${brand.name} repository access is ready!`,
 template: createElement(RepoAccessGrantedEmail, { repoUrl }),
 });
}); This email only sends after the GitHub invitation is confirmed. The ordering is deliberate. You don't tell the customer "your access is ready" if the invitation hasn't been sent. 
 Step 9: Schedule Follow-Up Sequence 
 await step.run("schedule-follow-up", async () => {
 const purchaseRecord = await db
 .select({ id: purchases.id })
 .from(purchases)
 .where(eq(purchases.stripeCheckoutSessionId, sessionId))
 .limit(1);

 if (purchaseRecord[0]) {
 await inngest.send({
 name: "purchase/follow-up.scheduled",
 data: {
 userId,
 purchaseId: purchaseRecord[0].id,
 tier,
 },
 });
 }
}); The final step triggers a separate function that handles the follow-up email sequence: day 7 onboarding tips, day 14 feedback request, day 30 testimonial request. This is an event-driven chain: one function completes and triggers another. 
 The follow-up function uses step.sleep() to wait between emails without consuming compute resources: 
 export const handlePurchaseFollowUp = inngest.createFunction(
 {
 id: "purchase-follow-up",
 triggers: [{ event: "purchase/follow-up.scheduled" }],
 cancelOn: [
 {
 event: "purchase/follow-up.cancelled",
 match: "data.purchaseId",
 },
 ],
 },
 async ({ event, step }) => {
 await step.sleep("wait-7-days", "7d");
 await step.run("send-day-7-email", async () => {
 // Send onboarding tips
 });

 await step.sleep("wait-14-days", "7d");
 await step.run("send-day-14-email", async () => {
 // Send feedback request
 });
 }
); The cancelOn option is worth noting. If the purchase is refunded, you send a purchase/follow-up.cancelled event, and the entire follow-up sequence stops. No stale emails to customers who refunded. 
 The Rule for Step Separation 
 Any operation that calls an external service or could fail independently should be its own step. A database query is a step because the database can be temporarily unreachable. An email send or API call is a step because those services can return errors or hit rate limits. 
 If two operations always succeed or fail together, they can share a step. But when in doubt, make it separate. The overhead is negligible, and the reliability gain is significant. 
 How to Handle Refunds 
 Refund processing is the most commonly overlooked part of a payment system. You need to handle two cases: full refunds (revoke access) and partial refunds (keep access, update status). 
 Here's the complete refund handler: 
 // src/lib/jobs/functions/stripe.ts
export const handleRefund = inngest.createFunction(
 { id: "refund-processed", triggers: [{ event: "stripe/charge.refunded" }] },
 async ({ event, step }) => {
 const data = event.data as {
 chargeId: string;
 paymentIntentId: string;
 amountRefunded: number;
 originalAmount: number;
 currency: string;
 };

 const chargeId = data.chargeId;
 const paymentIntentId = data.paymentIntentId;
 const currency = data.currency;
 const amountRefunded = data.amountRefunded;
 const originalAmount = data.originalAmount;
 const isFullRefund = amountRefunded >= originalAmount;

 // Step 1: Look up the purchase and user
 const { user, purchase } = await step.run(
 "lookup-purchase-by-payment-intent",
 async () => {
 const purchaseResult = await db
 .select({
 id: purchases.id,
 userId: purchases.userId,
 stripePaymentIntentId: purchases.stripePaymentIntentId,
 githubAccessGranted: purchases.githubAccessGranted,
 })
 .from(purchases)
 .where(eq(purchases.stripePaymentIntentId, paymentIntentId))
 .limit(1);

 const foundPurchase = purchaseResult[0];
 if (!foundPurchase) {
 return { user: null, purchase: null };
 }

 const userResult = await db
 .select({
 id: users.id,
 email: users.email,
 name: users.name,
 githubUsername: users.githubUsername,
 })
 .from(users)
 .where(eq(users.id, foundPurchase.userId))
 .limit(1);

 return { user: userResult[0] ?? null, purchase: foundPurchase };
 }
 );

 if (!purchase || !user) {
 return { success: false, reason: "no_matching_purchase" };
 }

 let accessRevoked = false;

 // Step 2: Revoke GitHub access (only for full refunds)
 if (isFullRefund && user.githubUsername && purchase.githubAccessGranted) {
 const revokeResult = await step.run(
 "revoke-github-access",
 async () => {
 return removeCollaborator(user.githubUsername!);
 }
 );
 accessRevoked = revokeResult.success;
 }

 // Step 3: Update purchase status
 await step.run("update-purchase-status", async () => {
 if (isFullRefund) {
 await db
 .update(purchases)
 .set({
 status: "refunded",
 githubAccessGranted: false,
 updatedAt: new Date(),
 })
 .where(eq(purchases.id, purchase.id));
 } else {
 await db
 .update(purchases)
 .set({
 status: "partially_refunded",
 updatedAt: new Date(),
 })
 .where(eq(purchases.id, purchase.id));
 }
 });

 // Step 4: Track refund in analytics
 await step.run("track-refund-event", async () => {
 try {
 await trackServerEvent(user.id, "refund_processed", {
 charge_id: chargeId,
 payment_intent_id: paymentIntentId,
 amount_cents: amountRefunded,
 original_amount_cents: originalAmount,
 currency,
 is_full_refund: isFullRefund,
 github_access_revoked: accessRevoked,
 });
 } catch (error) {
 console.error(`Failed to track to PostHog:`, error);
 }
 });

 // Step 5: Notify customer
 await step.run("send-customer-notification", async () => {
 if (isFullRefund) {
 await sendEmail({
 to: user.email,
 subject: `Your ${brand.name} refund has been processed`,
 template: createElement(AccessRevokedEmail, {
 customerEmail: user.email,
 refundAmount: amountRefunded,
 currency,
 }),
 });
 } else {
 await sendEmail({
 to: user.email,
 subject: `Your ${brand.name} partial refund has been processed`,
 template: createElement(PartialRefundEmail, {
 customerEmail: user.email,
 refundAmount: amountRefunded,
 originalAmount,
 currency,
 }),
 });
 }
 });

 // Step 6: Notify admin
 await step.run("send-admin-notification", async () => {
 const adminEmail = process.env.ADMIN_EMAIL;
 if (!adminEmail) return;

 await sendEmail({
 to: adminEmail,
 subject: `\({isFullRefund ? "Full" : "Partial"} refund processed: \){user.email}`,
 template: createElement(AdminRefundNotificationEmail, {
 customerEmail: user.email,
 customerName: user.name,
 githubUsername: user.githubUsername,
 refundAmount: amountRefunded,
 originalAmount,
 currency,
 stripeChargeId: chargeId,
 accessRevoked,
 isPartialRefund: !isFullRefund,
 }),
 });
 });

 return { success: true, accessRevoked, isFullRefund, userId: user.id };
 }
); How Full Refunds Differ from Partial Refunds 
 The function distinguishes between the two with a simple comparison: 
 const isFullRefund = amountRefunded >= originalAmount; For a full refund , three things happen: 
 GitHub access is revoked (the removeCollaborator call). 
 The purchase status is set to "refunded" . 
 The customer receives an AccessRevokedEmail explaining that their access has been removed. 
 For a partial refund , the customer keeps access: 
 GitHub access is not revoked. 
 The purchase status is set to "partially_refunded" . 
 The customer receives a PartialRefundEmail showing the refunded amount and the original amount. 
 This distinction matters for your database integrity. Downstream systems (your dashboard, analytics, support tools) need accurate status values. A partially_refunded purchase still represents an active customer. 
 How Conditional Steps Work 
 The "revoke GitHub access" step only runs when three conditions are all true: it's a full refund, the user has a GitHub username, and access was previously granted. 
 if (isFullRefund && user.githubUsername && purchase.githubAccessGranted) {
 const revokeResult = await step.run("revoke-github-access", async () => {
 return removeCollaborator(user.githubUsername!);
 });
 accessRevoked = revokeResult.success;
} If any of those conditions is false, the step is skipped entirely. Inngest handles this cleanly. The function continues to step 3 (update purchase status) with accessRevoked still set to false . 
 How to Recover Abandoned Checkouts 
 When a customer starts checkout but doesn't complete it, Stripe eventually expires the session (after 24 hours by default). You can listen for this event and send a recovery email. 
 The key insight is that you don't want to send the email immediately. Give the customer an hour to come back on their own. 
 // src/lib/jobs/functions/stripe.ts
export const handleCheckoutExpired = inngest.createFunction(
 {
 id: "checkout-expired",
 triggers: [{ event: "stripe/checkout.session.expired" }],
 },
 async ({ event, step }) => {
 const { customerEmail, sessionId } = event.data as {
 customerEmail: string | null;
 sessionId: string;
 };

 if (!customerEmail) {
 return { success: false, reason: "no_email" };
 }

 // Wait 1 hour before sending recovery email
 await step.sleep("wait-before-recovery-email", "1h");

 // Send abandoned cart email
 await step.run("send-abandoned-cart-email", async () => {
 const baseUrl =
 process.env.BETTER_AUTH_URL ?? "https://your-app.com";
 const checkoutUrl = `${baseUrl}/pricing`;

 await sendEmail({
 to: customerEmail,
 subject: `Your ${brand.name} checkout is waiting`,
 template: createElement(AbandonedCartEmail, {
 customerEmail,
 checkoutUrl,
 }),
 });
 });

 // Track the recovery attempt
 await step.run("track-abandoned-cart", async () => {
 try {
 await trackServerEvent("anonymous", "abandoned_cart_email_sent", {
 customer_email: customerEmail,
 session_id: sessionId,
 });
 } catch (error) {
 console.error(`Failed to track to PostHog:`, error);
 }
 });

 return { success: true, customerEmail };
 }
); The step.sleep("wait-before-recovery-email", "1h") line pauses the function for one hour without consuming compute resources. Inngest schedules the function to resume after the delay. No cron jobs, no Redis queues, no setTimeout that gets lost when your server restarts. 
 There is a guard at the top of the function. If the checkout session has no customer email (the customer closed the page before entering their email), the function returns early. You can't send a recovery email without an address. 
 You could extend this pattern with a second sleep and follow-up email three days later. You could also check if the customer has since completed a purchase (by querying the database in a step.run() ) and skip the email if they have. 
 Why One Hour Is the Right Delay 
 Sending the recovery email immediately after checkout expiration feels aggressive. The customer might still be comparing options, waiting for payday, or just distracted. An immediate email says "we noticed you left," which feels surveillance-like. 
 Waiting 24 hours is too long. The customer has moved on. They have forgotten your product or found an alternative. 
 One hour is the sweet spot I found through testing. The customer's intent is still fresh, and the email feels helpful rather than pushy. 
 Your mileage may vary. The delay is configurable: change "1h" to "30m" or "3h" and redeploy. 
 Why This Is Better Than a Cron Job 
 Without durable execution, abandoned cart recovery typically works like this: a cron job runs every hour, queries the database for expired sessions that haven't been recovered yet, sends emails to each one, and marks them as recovered. 
 This approach has several problems. You need a recovered_at column to avoid sending duplicate emails. You need to handle the case where the cron job crashes halfway through the batch, and you need to tune the cron interval carefully. 
 The step.sleep() approach eliminates all of this. Each expired session gets its own function instance with its own timer. There's no batch processing, no database flag, and no duplicate risk. 
 How to Send Transactional Emails with React Email 
 Every email in the payment flow is a React component rendered to HTML and sent via Resend. This gives you type-safe templates with props, component reuse, and the ability to preview emails in your browser during development. 
 How to Set Up the Email Client 
 The email client wraps Resend with a simple sendEmail function: 
 // src/lib/email/index.ts
import { render } from "@react-email/components";
import type { ReactElement } from "react";
import { Resend } from "resend";

import { brand } from "@/lib/brand";

let resendClient: Resend | null = null;

function getResend(): Resend {
 if (!resendClient) {
 const apiKey = process.env.RESEND_API_KEY;
 if (!apiKey) {
 throw new Error("RESEND_API_KEY is not set");
 }
 resendClient = new Resend(apiKey);
 }
 return resendClient;
}

interface SendEmailOptions {
 to: string | string[];
 subject: string;
 template: ReactElement;
 from?: string;
 replyTo?: string;
}

export async function sendEmail({
 to,
 subject,
 template,
 from = process.env.EMAIL_FROM ?? brand.emails.from,
 replyTo,
}: SendEmailOptions) {
 const resend = getResend();
 const html = await render(template);

 return resend.emails.send({
 from,
 to,
 subject,
 html,
 replyTo,
 });
} The render() function from @react-email/components converts a React element into an HTML string. This HTML is what Resend delivers to the customer's inbox. 
 The from address defaults to your brand's email configuration. You need a verified domain in Resend for this to work. During development, Resend's free tier lets you send to your own email address without domain verification. 
 How to Build a Purchase Confirmation Template 
 Here's the real purchase confirmation email template: 
 // src/lib/email/emails/purchase-confirmation.tsx
import {
 Body,
 Container,
 Head,
 Heading,
 Hr,
 Html,
 Link,
 Preview,
 Section,
 Text,
} from "@react-email/components";

import { brand } from "@/lib/brand";

interface PurchaseConfirmationEmailProps {
 amount: number;
 currency: string;
 customerEmail: string;
}

const colors = {
 primary: "#d97757",
 background: "#faf9f5",
 foreground: "#30302e",
 muted: "#6b6860",
 border: "#e5e4df",
 card: "#ffffff",
 success: "#16a34a",
 successLight: "#f0fdf4",
};

export default function PurchaseConfirmationEmail({
 amount,
 currency,
 customerEmail,
}: PurchaseConfirmationEmailProps) {
 const formattedAmount = new Intl.NumberFormat("en-US", {
 style: "currency",
 currency: currency.toUpperCase(),
 }).format(amount / 100);

 return (
 <Html>
 <Head />
 <Preview>Your {brand.name} purchase is confirmed!</Preview>
 <Body style={main}>
 <Container style={container}>
 <Section style={header}>
 <Text style={logoText}>{brand.name}</Text>
 </Section>

 <Hr style={divider} />

 <Section style={successBadge}>
 <Text style={successText}>Payment Successful</Text>
 </Section>

 <Heading style={h1}>Thank you for your purchase!</Heading>

 <Text style={text}>
 Your payment has been processed successfully. We are now setting
 up your GitHub repository access. You will receive another email
 shortly with your access link.
 </Text>

 <Section style={detailsBox}>
 <Text style={detailsTitle}>Order Details</Text>

 <Section style={detailRow}>
 <Text style={detailLabel}>Product</Text>
 <Text style={detailValue}>{brand.name}</Text>
 </Section>

 <Section style={detailRow}>
 <Text style={detailLabel}>Amount</Text>
 <Text style={detailValue}>{formattedAmount}</Text>
 </Section>

 <Section style={detailRow}>
 <Text style={detailLabel}>Email</Text>
 <Text style={detailValue}>{customerEmail}</Text>
 </Section>
 </Section>

 <Text style={text}>
 This is a one-time purchase. No recurring charges will be made.
 </Text>

 <Hr style={divider} />

 <Text style={footer}>
 Questions about your purchase? Reply to this email or reach
 out at{" "}
 <Link
 href={`mailto:${brand.emails.support}`}
 style={link}
 >
 {brand.emails.support}
 </Link>
 </Text>
 </Container>
 </Body>
 </Html>
 );
}

PurchaseConfirmationEmail.PreviewProps = {
 amount: 9900,
 currency: "usd",
 customerEmail: "customer@example.com",
} satisfies PurchaseConfirmationEmailProps; A few things to note about this template. 
 Currency formatting happens in the template: The amount prop is in cents (the same format stored in your database and returned by Stripe). The Intl.NumberFormat call converts it to a human-readable string like "$99.00" and keeps currency formatting logic in one place. 
 The PreviewProps object is for development. React Email uses these props to render a preview in the browser. The satisfies keyword ensures the preview props match the component's interface. 
 All styles are inline objects. Email clients strip <style> tags and ignore most CSS. Inline styles are the only reliable way to style emails across Gmail, Outlook, Apple Mail, and every other client. 
 How to Build a Repo Access Template 
 The repo access email is sent after the GitHub invitation succeeds: 
 // src/lib/email/emails/repo-access-granted.tsx
import {
 Body,
 Button,
 Container,
 Head,
 Heading,
 Hr,
 Html,
 Link,
 Preview,
 Section,
 Text,
} from "@react-email/components";

import { brand } from "@/lib/brand";

interface RepoAccessGrantedEmailProps {
 repoUrl: string;
}

export default function RepoAccessGrantedEmail({
 repoUrl,
}: RepoAccessGrantedEmailProps) {
 return (
 <Html>
 <Head />
 <Preview>Your {brand.name} repository access is ready!</Preview>
 <Body style={main}>
 <Container style={container}>
 <Section style={header}>
 <Text style={logoText}>{brand.name}</Text>
 </Section>

 <Hr style={divider} />

 <Heading style={h1}>You are in!</Heading>

 <Text style={text}>
 Your GitHub repository access has been granted. You now have
 full access to the {brand.name} codebase.
 </Text>

 <Section style={buttonContainer}>
 <Button style={button} href={repoUrl}>
 Open Repository
 </Button>
 </Section>

 <Section style={infoBox}>
 <Text style={infoTitle}>Quick Start</Text>
 <Text style={infoText}>
 <strong>1.</strong> Clone the repository to your machine
 </Text>
 <Text style={infoText}>
 <strong>2.</strong> Run{" "}
 <code style={codeStyle}>bun install</code> to install
 dependencies
 </Text>
 <Text style={infoText}>
 <strong>3.</strong> Follow the README for environment setup
 </Text>
 <Text style={infoText}>
 <strong>4.</strong> Run{" "}
 <code style={codeStyle}>bun dev</code> to start building
 </Text>
 </Section>

 <Hr style={divider} />

 <Text style={footer}>
 Need help? Reply to this email or reach out at{" "}
 <Link
 href={`mailto:${brand.emails.support}`}
 style={link}
 >
 {brand.emails.support}
 </Link>
 </Text>
 </Container>
 </Body>
 </Html>
 );
} This template includes a <Button> component that links directly to the GitHub repository. The quick start section gives the customer immediate next steps so they aren't left wondering what to do after gaining access. 
 How to Build an Abandoned Cart Template 
 The abandoned cart email brings the customer back to your pricing page: 
 // src/lib/email/emails/abandoned-cart.tsx
import {
 Body,
 Button,
 Container,
 Head,
 Heading,
 Hr,
 Html,
 Preview,
 Section,
 Text,
} from "@react-email/components";

import { brand } from "@/lib/brand";

interface AbandonedCartEmailProps {
 customerEmail: string;
 checkoutUrl: string;
}

export default function AbandonedCartEmail({
 customerEmail,
 checkoutUrl,
}: AbandonedCartEmailProps) {
 return (
 <Html>
 <Head />
 <Preview>Your {brand.name} checkout is waiting for you</Preview>
 <Body style={main}>
 <Container style={container}>
 <Section style={header}>
 <Text style={logoText}>{brand.name}</Text>
 </Section>

 <Hr style={divider} />

 <Heading style={h1}>You left something behind</Heading>

 <Text style={text}>
 We noticed you started a checkout but did not complete your
 purchase. No worries. Your cart is still waiting for you.
 </Text>

 <Text style={text}>
 {brand.name} gives you everything you need to ship your
 startup this weekend: authentication, payments, email,
 background jobs, and more. All wired together and ready
 to go.
 </Text>

 <Section style={buttonContainer}>
 <Button style={button} href={checkoutUrl}>
 Complete Your Purchase
 </Button>
 </Section>

 <Text style={textSmall}>
 If you ran into any issues during checkout or have questions
 about {brand.name}, just reply to this email. I read every
 message personally.
 </Text>

 <Hr style={divider} />

 <Text style={footer}>
 This email was sent to {customerEmail} because you started
 a checkout on {brand.name}. If this was not you, you can
 safely ignore this email.
 </Text>
 </Container>
 </Body>
 </Html>
 );
} The tone matters here. "You left something behind" is friendly, not pushy. The email explains the product's value briefly, includes a single clear call to action, and the footer explains why they received the email. 
 How Templates Integrate with Durable Steps 
 Every email template is invoked via createElement inside a step.run() block: 
 await step.run("send-purchase-confirmation", async () => {
 await sendEmail({
 to: user.email,
 subject: `Your ${brand.name} purchase is confirmed!`,
 template: createElement(PurchaseConfirmationEmail, {
 amount: purchase.amount,
 currency: purchase.currency,
 customerEmail: user.email,
 }),
 });
}); The createElement call creates a React element from the template component with the given props. The sendEmail function renders it to HTML via React Email's render() and sends it through Resend. 
 Because this is inside a step.run() , the email send is checkpointed. If Resend is down and the step fails, it retries on its own without re-running previous steps. The customer never gets a duplicate email. 
 How to Test the Complete Flow Locally 
 Testing the complete payment lifecycle locally requires three things running simultaneously: your application, the Stripe CLI forwarding webhook events, and the Inngest dev server processing background jobs. 
 Step 1: Start the Stripe CLI 
 Install the Stripe CLI and log in: 
 # macOS
brew install stripe/stripe-cli/stripe

# Authenticate
stripe login Forward webhook events to your local server: 
 stripe listen --forward-to localhost:3000/api/payments/webhook The CLI prints a webhook signing secret starting with whsec_ . Copy this to your .env as STRIPE_WEBHOOK_SECRET . 
 Step 2: Start the Inngest Dev Server 
 The Inngest dev server gives you real-time visibility into every function execution, every step, and every retry: 
 npx inngest-cli@latest dev -u http://localhost:3000/api/inngest Open http://localhost:8288 in your browser. This is the Inngest dashboard where you'll watch your durable functions execute step by step. 
 Step 3: Start Your Application 
 bun run dev Your application should now be running on http://localhost:3000 . 
 Step 4: Test the Purchase Flow 
 Go to your pricing page and click the checkout button. 
 Use Stripe's test card number 4242 4242 4242 4242 with any future expiration date and any CVC. 
 Complete the checkout. Stripe redirects you to your success URL. 
 Your frontend calls the /api/purchases/claim endpoint with the session ID. 
 Watch the Inngest dashboard. You should see the purchase-completed function trigger and each step execute in sequence. 
 In the Inngest dashboard, you will see: 
 Step 1: "lookup-user-and-purchase" completes with the user and purchase data. 
 Step 2: "track-purchase-to-posthog" completes (or logs a warning if PostHog isn't configured). 
 Step 3: "send-purchase-confirmation" completes. Check your email. 
 Step 4: "send-admin-notification" completes (if ADMIN_EMAIL is set). 
 Steps 5-9: Run if the user has a GitHub username linked. 
 Step 5: Test a Refund 
 Trigger a refund through the Stripe CLI: 
 stripe trigger charge.refunded Or go to the Stripe dashboard, find the test payment, and issue a refund manually. The Stripe CLI will forward the charge.refunded webhook to your local server. 
 In the Inngest dashboard, you'll see the refund-processed function trigger with its own set of steps: lookup, conditional access revocation, status update, analytics tracking, and email notifications. 
 Step 6: Test Abandoned Cart Recovery 
 Trigger a checkout expiration: 
 stripe trigger checkout.session.expired The checkout-expired function will appear in the Inngest dashboard. You'll see the 1-hour sleep step. In the dev server, you can fast-forward through sleeps by clicking the "Skip" button in the dashboard. This lets you test the delayed email without actually waiting an hour. 
 How to Simulate Step Failures 
 To test the retry behavior, temporarily throw an error in one of your steps: 
 const collaboratorResult = await step.run(
 "add-github-collaborator",
 async () => {
 throw new Error("Simulated GitHub API failure");
 }
); In the Inngest dashboard, you'll see: 
 Steps 1 through 4 succeed and their results are cached. 
 Step 5 fails and is retried with exponential backoff. 
 Steps 6 through 9 remain pending. 
 Remove the thrown error, and on the next retry, step 5 succeeds. Steps 6 through 9 execute, while steps 1 through 4 aren't re-executed. This is the checkpointing behavior that makes durable execution reliable. 
 Conclusion 
 Building a complete SaaS payment flow is more than integrating Stripe Checkout. It's the entire lifecycle from "Buy" button to "Welcome" email, including the parts that happen when things go wrong. 
 Here's what you built in this tutorial: 
 A database schema that tracks purchases through every state: completed, partially refunded, and fully refunded. 
 A Stripe product and price seed script that creates your catalog programmatically. 
 A checkout flow with session creation, payment verification, and idempotent purchase claiming. 
 A thin webhook handler that validates signatures and routes events to background jobs. 
 A 9-step durable purchase function where each step is independently checkpointed and retried. 
 A refund handler that distinguishes between full and partial refunds, revoking access only when appropriate. 
 An abandoned cart recovery flow that waits an hour before sending a friendly recovery email. 
 Three transactional email templates built with React Email: purchase confirmation, repo access granted, and abandoned cart. 
 A local testing setup with Stripe CLI, Inngest dev server, and step-by-step observability. 
 The most important pattern is the separation between receiving and processing. Your API endpoints and webhook handlers should be thin: validate, record, enqueue, return. All the complex multi-step work happens in durable background functions where failures are isolated and retried at the step level. 
 This pattern scales. Add a new step to the purchase flow, and it gets the same checkpointing and retry behavior. Add a new webhook event, and you route it to a new durable function. 
 Your requirements may differ. You might sell subscriptions instead of one-time purchases, or provision API keys instead of GitHub access. The specific steps change, but the architecture stays the same. 
 If you want to start with all of these patterns already wired together in a production-ready codebase, Eden Stack includes the complete payment flow described in this article, along with 30+ additional production-tested patterns for authentication, email, analytics, background jobs, and more. 
 Magnus Rødseth builds AI-native applications and is the creator of Eden Stack , a production-ready starter kit with 30+ Claude skills encoding production patterns for AI-native SaaS development.
```

---

## 8. Product Experimentation with Regression Discontinuity: How an LLM Confidence Threshold Creates a Natural Experiment in Python

- 日期: 2026-05-08 15:33
- 链接: https://www.freecodecamp.org/news/gen-ai-product-experimentation-with-regression-discontinuity-design/

```
Causal inference for LLM-based features starts with one question editors ask before they ship anything: Did the change actually move the metric, or did the metric just move? 
 Let's say that your team built a routing layer that splits incoming queries between two models: queries with a confidence score below 0.85 go to a premium model, and those above 0.85 go to a cheaper distilled model. The premium model costs 5x as much as the cheaper one. 
 Your boss wants the answer that ends the debate: Is the premium model worth it for the queries it sees? 
 You can't run a clean A/B test, because routing is deterministic: a query at confidence 0.84 always gets premium, a query at 0.86 always gets cheap, and you can't randomize the assignment. 
 You also can't trust a naïve comparison of premium-routed users against cheap-routed users. Premium handles the harder queries by design (that's the reason you built the gate), so the two groups differ in query difficulty before either model touches them. 
 The threshold itself is your free experiment. Right at 0.85, the assignment flips, but the queries on either side of that boundary are essentially identical. A query at confidence 0.849 isn't meaningfully different from a query at 0.851. Any differences in outcomes between the two narrow groups stem solely from the routing decision. That's what regression discontinuity design (RDD) reads. 
 In this tutorial, you'll use Python to estimate the causal effect of premium routing on task completion using sharp RDD with local linear regression. You'll sweep bandwidths to test estimate stability, run a manipulation diagnostic, check robustness with a quadratic specification, and bootstrap 95% confidence intervals around every point estimate. 
 The LLM telemetry is a 50,000-user synthetic dataset with the ground-truth premium-routing effect baked in at +6 percentage points, so you can verify that RDD recovers it. 
 Companion code: every code block runs end-to-end in the companion notebook . 
 Table of Contents 
 Why Threshold Routing is a Natural Experiment 
 What Regression Discontinuity Actually Does 
 Prerequisites 
 Setting Up the Working Example 
 Step 1: A Sharp RDD with Local Linear Regression 
 Step 2: Try Different Bandwidths 
 Step 3: Checking for Manipulation at the Threshold 
 Step 4: Quadratic Specification as a Robustness Check 
 Step 5: Bootstrap Confidence Intervals 
 When Regression Discontinuity Fails 
 What to Do Next 
 Why Threshold Routing is a Natural Experiment 
 The product reason this routing rule exists is to help your team spend the premium model budget where it earns its keep. Low-confidence queries are the harder ones, which is where a stronger model has the most upside. High-confidence queries already look easy enough for the cheap model to handle. 
 You'll see this routing direction across confidence-score gates for Q&A assistants, query-complexity gates in multi-model gateways like OpenRouter, safety-score gates in content moderation, and latency-budget gates that re-route when the cheap model would exceed a p99 latency budget. 
 The mechanism is the same in every case: a continuous score, a threshold, and a deterministic routing rule. 
 What makes this setup useful for causal inference is that users don't pick which model they get. A query lands, the system computes confidence, and the routing layer decides. Right at the threshold, the user's experience flips from premium to cheap based on a difference too small to be meaningful. 
 Again, a query at 0.849 confidence isn't shipping a different problem to the model than a query at 0.851. Anything that differs in outcomes between those two groups is the routing decision speaking. The underlying query is the same. 
 That local randomness is the experiment RDD reads from. You don't need a randomized control group, you don't need a propensity score. And you don't need an instrument, you need a sharp threshold that nobody can game. 
 What Regression Discontinuity Actually Does 
 The jump at the threshold is the causal effect, which is the number a product team can act on. RDD reads it by fitting two separate regression lines to the outcome: one for users just below the threshold and one for users just above. The vertical difference between those two fitted lines at the cutoff is the local average treatment effect at that point. 
 Graphically, picture task completion on the y-axis and query confidence on the x-axis. Completion generally trends with confidence (easier queries complete more often). At exactly 0.85, though, users below the cutoff get premium routing, and users above get cheap. 
 If premium routing helps, you'd see a sharp upward jump in task completion just below 0.85, then disappear just above. Approached from left to right with confidence rising, the visual reads as a downward step at 0.85, because you're moving from the premium-treated zone into the cheap-treated zone. 
 Figure 1. Conceptual schematic. Two outcome trajectories, one for premium-routed queries (confidence below 0.85) and one for cheap-routed queries (confidence above 0.85), meet at the threshold but don't match. The vertical gap between their endpoints at 0.85 is the local causal effect of premium routing. 
 That gap is identified under two named assumptions: 
 No manipulation of the running variable: Users (or your system) can't precisely nudge a query's confidence score across the cutoff. If anyone can game their score to land just below 0.85 and grab premium routing, the cutoff is no longer drawn at random, and RDD breaks. 
 Continuity of potential outcomes at the cutoff: Every other factor that affects task completion (query type, user expertise, workspace tenure, time of day) varies smoothly across 0.85. Only the routing assignment changes discontinuously at exactly the threshold. If a second product rule fires at 0.85 (a different logging level, a separate UI treatment, a retry policy), RDD will attribute that rule's effect to the routing decision. 
 These are the two assumptions you check before you trust the estimate. Step 3 below tests the first one. The second is a structural property of your system that you have to know cold. 
 Two practical choices shape every RDD: the bandwidth (how close to the cutoff to restrict the analysis) and the functional form (linear, quadratic, or local polynomial). 
 Narrow bandwidths cut potential bias by staying close to the local-randomization zone, but they shrink the sample. Linear specifications are stable, though they assume the underlying relationship can be approximated by a straight line on each side. 
 You'll try both linear and quadratic specifications at multiple bandwidths to see whether the answer holds. 
 The article uses sharp RDD throughout, since assignment is a deterministic function of confidence (below 0.85 always premium, above 0.85 always cheap). When the threshold is probabilistic and compliance is partial, the design is a fuzzy RDD, which requires an instrumental variables framework that you can implement using the rdrobust Python package. 
 Prerequisites 
 You need Python 3.11 or newer, comfort with pandas and statsmodels, and rough familiarity with linear regression and interaction terms. 
 Install the packages used in this tutorial: 
 pip install numpy pandas statsmodels matplotlib scipy Here's what's happening: four standard scientific Python libraries plus matplotlib for the diagnostic visualization. Nothing exotic. 
 Clone the companion repo and generate the synthetic dataset: 
 git clone https://github.com/RudrenduPaul/product-experimentation-causal-inference-genai-llm.git
cd product-experimentation-causal-inference-genai-llm
python data/generate_data.py --seed 42 --n-users 50000 --out data/synthetic_llm_logs.csv Here's what's happening: the data generator draws 50,000 users with a query_confidence score from a Beta(5,2) distribution, applies the routing rule ( routed_to_premium = query_confidence < 0.85 ), and bakes a +6-percentage-point premium routing effect into task_completed . Same seed, same dataset, every time. 
 Setting Up the Working Example 
 The dataset simulates a SaaS product that routes queries between a premium and a cheap model based on confidence score. The threshold is 0.85, and the ground-truth causal effect of premium routing is +6 percentage points on task completion. You know the truth, so you can check whether RDD recovers it. 
 Load the data and look at the routing breakdown: 
 import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("data/synthetic_llm_logs.csv")
print(f"Loaded {len(df):,} rows, {df.shape[1]} columns")

print("\nRouting breakdown:")
counts = df.routed_to_premium.value_counts().to_dict()
print(f" Premium-routed (confidence < 0.85): {counts.get(1, 0):,}")
print(f" Cheap-routed (confidence >= 0.85): {counts.get(0, 0):,}")

print("\nQuery confidence distribution:")
print(df.query_confidence.describe().round(3)) Expected output: 
 Loaded 50,000 rows, 16 columns

Routing breakdown:
 Premium-routed (confidence < 0.85): 38,874
 Cheap-routed (confidence >= 0.85): 11,126

Query confidence distribution:
count 50000.000
mean 0.715
std 0.159
min 0.078
25% 0.611
50% 0.736
75% 0.838
max 0.998 Here's what's happening: about 78% of queries land below the 0.85 cutoff and get premium routing. The Beta(5,2) distribution is skewed toward the upper end, with a median of 0.736, and most of its mass still sits below 0.85. The remaining 22% are queries that the model already feels confident about, and they go to the cheap model. 
 Before any regression, look at the naïve comparison every product team is tempted to run: 
 naive = (
 df[df.routed_to_premium == 1].task_completed.mean()
 - df[df.routed_to_premium == 0].task_completed.mean()
)
print(f"Naive premium-vs-cheap effect: {naive:+.4f} (ground truth = +0.06)") Expected output: 
 Naive premium-vs-cheap effect: +0.0632 (ground truth = +0.06) Here's what's happening: the naive estimate sits at +0.0632, which is suspiciously close to the truth. That's a coincidence of this specific synthetic dataset, where the only confounder of premium vs. cheap is query_confidence itself, and the outcome doesn't depend on confidence except through routing. 
 In production, you almost never get this lucky. User expertise, prompt phrasing, time of day, and a dozen unobserved query traits all correlate with confidence and with completion. 
 A naïve comparison in a real system can be off by 50% or more in either direction. RDD gives you identification that doesn't depend on the absence of hidden confounders. 
 Step 1: A Sharp RDD with Local Linear Regression 
 The basic sharp RDD estimator is a local linear regression. Restrict to users whose confidence sits within a bandwidth of the cutoff, fit separate linear slopes on each side, and read off the jump at 0.85. 
 cutoff = 0.85
bw = 0.10

near = df[(df.query_confidence > cutoff - bw)
 & (df.query_confidence < cutoff + bw)].copy()
near["below_cutoff"] = (near.query_confidence < cutoff).astype(int)
near["rc"] = near.query_confidence - cutoff

rdd_model = smf.ols(
 "task_completed ~ below_cutoff + rc + below_cutoff:rc",
 data=near,
).fit(cov_type="HC3")

effect = rdd_model.params["below_cutoff"]
print(f"RDD effect at cutoff (LATE): {effect:+.4f}")
print(f"Std error (HC3): {rdd_model.bse['below_cutoff']:.4f}")
print(f"p-value: {rdd_model.pvalues['below_cutoff']:.4f}")
print(f"N users in [0.75, 0.95): {len(near):,}") Expected output: 
 RDD effect at cutoff (LATE): +0.0548
Std error (HC3): 0.0131
p-value: 0.0000
N users in [0.75, 0.95): 21,689 Here's what's happening: the model fits separate intercepts and slopes on each side of 0.85 ( below_cutoff is the side indicator, rc is confidence centered at the cutoff). The coefficient on below_cutoff reads off the vertical jump at the threshold, which is the local average treatment effect (LATE) for queries with confidence near 0.85. You get +0.0548, within sampling noise of the +0.06 ground truth. 
 Three notes on the specification. First, task_completed is binary, so this is a linear probability model. For RDD with a binary outcome at the cutoff, the linear probability model is standard practice because local linearity is the identifying assumption either way. Logit at the cutoff is an alternative if you need bounded predictions globally. 
 Second, the standard errors are used cov_type="HC3" to relax the homoskedasticity assumption, which is almost always wrong for binary outcomes. 
 Third, the dataset has one query per user with no within-user clustering, so cluster-robust standard errors aren't needed here. In a setting with multiple queries per user, you'd cluster on user_id . 
 The next diagnostic to look at is the confidence distribution near the cutoff. Figure 2 shows what 50,000 queries look like in the bandwidth window: 
 Figure 2. Real distribution from the 50,000-user synthetic dataset. Unlike the schematic in Figure 1, this shows the actual query density by confidence score, with the routing threshold annotated. The bottom panel counts how many queries land in each 2-percentage-point bin near the cutoff (2,461 / 2,481 / 2,335 / 2,229 / 2,048 across the 0.80–0.90 range). The roughly uniform spread is the visual signal that no manipulation is concentrating users on one side of the threshold. 
 Step 2: Try Different Bandwidths 
 Bandwidth choice matters. Too narrow and you have too few observations, so the confidence interval blows up. Too wide and you're extrapolating into regions where the linear specification is no longer a reasonable local approximation. 
 The honest move is to try multiple bandwidths and report whether the estimate holds. 
 results = []
for bw in [0.05, 0.10, 0.15, 0.20]:
 sub = df[(df.query_confidence > cutoff - bw)
 & (df.query_confidence < cutoff + bw)].copy()
 sub["below_cutoff"] = (sub.query_confidence < cutoff).astype(int)
 sub["rc"] = sub.query_confidence - cutoff

 m = smf.ols(
 "task_completed ~ below_cutoff + rc + below_cutoff:rc",
 data=sub,
 ).fit(cov_type="HC3")

 results.append({
 "bandwidth": bw,
 "n": len(sub),
 "effect": m.params["below_cutoff"],
 "se": m.bse["below_cutoff"],
 "p": m.pvalues["below_cutoff"],
 })

print(pd.DataFrame(results).round(4).to_string(index=False)) Expected output: 
 bandwidth n effect se p
 0.05 11554 0.0635 0.0183 0.0005
 0.10 21689 0.0548 0.0131 0.0000
 0.15 29137 0.0618 0.0112 0.0000
 0.20 34074 0.0614 0.0107 0.0000 Here's what's happening: four bandwidths from ±0.05 to ±0.20 around the cutoff, refitting the same RDD specification at each. The estimates range from +0.0548 to +0.0635, all in the same neighborhood as the +0.06 ground truth, with standard errors that shrink as the bandwidth widens and grow as it narrows. Every p-value is well below 0.05. Whether the estimates are "stable" depends on the confidence intervals around them, which Step 5 produces with the bootstrap. 
 Step 3: Checking for Manipulation at the Threshold 
 RDD is valid only if users can't precisely manipulate the running variable around the cutoff. If your users (or your system) can nudge confidence scores just below 0.85 to force premium routing, you get a density spike at the cutoff, and the RDD estimate is contaminated. 
 The standard diagnostic is the McCrary density test, which checks whether the distribution of the running variable has a sharp jump at the cutoff. The simple version: bin the data tightly around 0.85 and check whether the counts on the two sides are similar. 
 print("User counts in 2-percentage-point bins around 0.85:")
for lo in [0.80, 0.82, 0.84, 0.86, 0.88]:
 hi = lo + 0.02
 cnt = ((df.query_confidence >= lo) & (df.query_confidence < hi)).sum()
 print(f" [{lo:.2f}, {hi:.2f}): n = {cnt:,}") Expected output: 
 User counts in 2-percentage-point bins around 0.85:
 [0.80, 0.82): n = 2,461
 [0.82, 0.84): n = 2,481
 [0.84, 0.86): n = 2,335
 [0.86, 0.88): n = 2,229
 [0.88, 0.90): n = 2,048 Here's what's happening: counts trend gently downward across the bandwidth because Beta(5,2) places more mass at higher confidence levels, and the density tapers as it approaches 1.0. There's no spike or dip at the 0.84–0.86 bin that straddles the cutoff. The 433-user spread across all five bins is consistent with smooth tapering of the underlying density. 
 That's the pattern you want when manipulation is absent. For a more rigorous test, the rddensity Python package implements the formal McCrary procedure with bias-corrected standard errors. 
 What manipulation looks like when it's real: a spike in users at confidences just barely below 0.85 (they're being nudged into premium routing) and a dip just above. If you see that pattern, the RDD estimate overstates the causal effect because the users right below 0.85 differ in motivation from those right above. They cared enough to manipulate the score, and they'd have shown different outcomes even under random routing. 
 Step 4: Quadratic Specification as a Robustness Check 
 If the true relationship between confidence and task completion isn't exactly linear, a local linear RDD can mistake the curvature for a jump. The standard robustness check allows quadratic terms on both sides of the cutoff and tests whether the estimate holds. 
 near = df[(df.query_confidence > cutoff - 0.10)
 & (df.query_confidence < cutoff + 0.10)].copy()
near["below_cutoff"] = (near.query_confidence < cutoff).astype(int)
near["rc"] = near.query_confidence - cutoff
near["rc2"] = near.rc ** 2

rdd_quad = smf.ols(
 "task_completed ~ below_cutoff + rc + below_cutoff:rc"
 " + rc2 + below_cutoff:rc2",
 data=near,
).fit(cov_type="HC3")

print(f"Linear RDD (bw=0.10): effect = +0.0548, p < 0.0001")
print(f"Quadratic RDD (bw=0.10): effect = "
 f"{rdd_quad.params['below_cutoff']:+.4f}, "
 f"p = {rdd_quad.pvalues['below_cutoff']:.4f}") Expected output: 
 Linear RDD (bw=0.10): effect = +0.0548, p < 0.0001
Quadratic RDD (bw=0.10): effect = +0.0569, p = 0.0036 Here's what's happening: the quadratic specification adds squared terms and interactions with the cutoff indicator, allowing the relationship to curve differently on each side. The below_cutoff coefficient still captures the jump at the threshold, now under a more flexible specification. 
 The two estimates differ by 0.0022, both close to the +0.06 ground truth, and both are significant at p < 0.01. The answer doesn't change when you let the model bend. 
 When linear and quadratic specifications disagree noticeably, you have a real signal. With small samples (a few thousand at narrow bandwidths), the quadratic version can lose power because four extra parameters need data to be identified. 
 The standard move is to widen the bandwidth and re-run both specifications. If they still disagree at wider bandwidths, the linear approximation is wrong, and you should report both numbers. 
 Step 5: Bootstrap Confidence Intervals 
 Every point estimate in this article is a single number from a finite sample. The bootstrap quantifies how much that number would move under resampling, which is what a confidence interval describes. 
 def bootstrap_ci(df, cutoff, bw, quadratic=False, n_reps=500, seed=7):
 rng = np.random.default_rng(seed)
 near = df[(df.query_confidence > cutoff - bw)
 & (df.query_confidence < cutoff + bw)].copy()
 near["below_cutoff"] = (near.query_confidence < cutoff).astype(int)
 near["rc"] = near.query_confidence - cutoff
 if quadratic:
 near["rc2"] = near.rc ** 2
 formula = ("task_completed ~ below_cutoff + rc + below_cutoff:rc"
 " + rc2 + below_cutoff:rc2")
 else:
 formula = "task_completed ~ below_cutoff + rc + below_cutoff:rc"

 n = len(near)
 estimates = np.empty(n_reps)
 for i in range(n_reps):
 sample = near.iloc[rng.integers(0, n, size=n)]
 m = smf.ols(formula, data=sample).fit()
 estimates[i] = m.params["below_cutoff"]
 return (np.percentile(estimates, 2.5), np.percentile(estimates, 97.5))

print("Linear RDD (bw=0.10):")
lo, hi = bootstrap_ci(df, cutoff, bw=0.10)
print(f" effect = +0.0548 95% CI: [{lo:+.4f}, {hi:+.4f}]")

print("\nBandwidth sensitivity:")
for bw, eff in [(0.05, 0.0635), (0.10, 0.0548), (0.15, 0.0618), (0.20, 0.0614)]:
 lo, hi = bootstrap_ci(df, cutoff, bw=bw)
 print(f" bw = {bw:.2f} effect = {eff:+.4f} "
 f"95% CI: [{lo:+.4f}, {hi:+.4f}]")

print("\nQuadratic RDD (bw=0.10):")
lo, hi = bootstrap_ci(df, cutoff, bw=0.10, quadratic=True)
print(f" effect = +0.0569 95% CI: [{lo:+.4f}, {hi:+.4f}]") Expected output: 
 Linear RDD (bw=0.10):
 effect = +0.0548 95% CI: [+0.0278, +0.0817]

Bandwidth sensitivity:
 bw = 0.05 effect = +0.0635 95% CI: [+0.0244, +0.0986]
 bw = 0.10 effect = +0.0548 95% CI: [+0.0278, +0.0817]
 bw = 0.15 effect = +0.0618 95% CI: [+0.0381, +0.0823]
 bw = 0.20 effect = +0.0614 95% CI: [+0.0420, +0.0808]

Quadratic RDD (bw=0.10):
 effect = +0.0569 95% CI: [+0.0205, +0.0959] Here's what's happening: the bootstrap resamples the bandwidth-restricted data with replacement 500 times, refits the RDD on each replicate, and collects the below_cutoff coefficient. The 2.5th and 97.5th percentiles of those 500 estimates form the 95% interval. Every interval covers the +0.06 ground truth, every interval excludes zero, and the bandwidth sweep produces overlapping intervals. 
 That's quantitative stability, verified by resampling across the full bandwidth range. Intervals widen as the bandwidth shrinks and narrow as it grows. The quadratic interval is wider than the linear one because the four extra parameters absorb degrees of freedom. 
 One thing the intervals do NOT do on this dataset: exclude the naive +0.0632 estimate. That's because the data generator doesn't bake in confounding by query confidence. The only difference between the premium and cheap groups in expectations is the +6pp routing effect itself, so the naïve comparison is close to the truth. 
 Real systems are messier. In a production setting where unobserved query traits affect both the routing assignment and task completion, the naïve estimate would diverge from the RDD estimate, and the bootstrap intervals would tell you which one to trust. 
 When Regression Discontinuity Fails 
 RDD looks clean, but several specific failure modes can destroy the identification. Each one maps to a violation of one of the two named assumptions. 
 Users manipulate the running variable (violates assumption 1). The whole setup depends on users (or any upstream service) being unable to precisely control which side of the cutoff they land on. Any system that reveals the cutoff and gives users a way to influence their score (a retry mechanism, a prompt engineering workaround, a confidence-inflating trick) breaks RDD. 
 Run the density check in Step 3 every time. If you find manipulation, switch to a fuzzy RDD that treats the threshold as probabilistic, or abandon the approach. 
 Other policies fire at the same cutoff (violates assumption 2). If your product has additional rules that activate at 0.85 (a separate UI treatment, a different logging level, a different retry policy), RDD can't separate the routing effect from those other policy effects. Audit the full rule book for anything that shares the threshold. 
 The threshold has noise or overrides (violates assumption 1, in the structural sense). Maybe routing isn't strictly deterministic at 0.85 – it may have random jitter, or a second rule may override the main rule in some cases. 
 If assignment to the premium model isn't a deterministic function of query_confidence , you have a fuzzy RDD, which requires an instrumental variables framework. The rdrobust package handles both sharp and fuzzy designs. 
 Curvature masquerading as a jump (breaks the linear approximation that supports identification at the cutoff). Sharp RDD assumes linearity is a reasonable local approximation. When the underlying outcome-confidence relationship is strongly curved, the linear specification can mistake the bend for a jump. 
 Step 4's quadratic robustness check is the standard diagnostic. If linear and quadratic disagree, widen the bandwidth and re-run both. 
 Extrapolation bias (a continuity issue, reframed). RDD estimates are strictly local to the cutoff. The +0.06 effect at 0.85 tells you nothing about what premium routing would do for queries with confidence 0.30 or 0.99. 
 If you want a global average effect, you need a different technique: propensity methods, regression with confounder adjustment, or an actual experiment. 
 What to Do Next 
 RDD is the right tool when your AI feature is gated by a continuous score and a sharp threshold. 
 If your feature is gated by a user-controlled toggle, propensity score methods are a better fit. If it's gated by a staged rollout across workspaces, difference-in-differences handles it. If it's gated by rules you can't observe directly but that have a random component, instrumental variables is the right choice. 
 For production RDD analyses, use the rdrobust Python package. It gives you optimal bandwidth selection (Calonico, Cattaneo, and Titiunik 2014), bias-corrected standard errors, and a built-in plotting utility. The companion rddensity package implements the McCrary density test you saw informally in Step 3. 
 The from-scratch version in this tutorial shows the mechanics. The rd-packages stack is what you ship to a reviewer. 
 One thing the LATE doesn't do: tell you the effect for users far from the cutoff. If a +0.06 LATE at 0.85 is enough to keep premium routing in the pipeline, you're done. If you need to know what premium would do for the easy queries you're currently sending to cheap (or the hardest queries near the floor), the next step is a small randomized rollout in those zones, scored against the RDD estimate as a calibration check. Don't generalize the LATE without evidence. 
 The companion notebook for this tutorial lives here on GitHub . Clone the repo, generate the synthetic dataset, and run rdd_demo.ipynb to reproduce every code block from this tutorial. 
 Threshold routing is one of the most common patterns in production LLM systems, and every confidence-gated routing decision in your stack is a potential RDD. Run the analysis.
```

---

## 9. How to Build a Live Options Database in Python – A Complete Guide

- 日期: 2026-05-07 23:00
- 链接: https://www.freecodecamp.org/news/how-to-build-a-live-options-database-in-python-a-complete-guide/

```
Live options analytics change constantly. Implied volatility shifts, Greeks drift, and the shape of the surface can look different even a few minutes later. 
 But a lot of teams still treat these numbers like something you glance at once. A screenshot in a deck. A one-off notebook cell. A quick check in a UI before a meeting. 
 That works until you need to answer basic questions that show up in real workflows: 
 What did TSLA's surface look like at 10:32? When did skew start steepening? Did the change come from the wings moving or the ATM shifting? 
 If you don't store the data as it arrives, you can't replay it, compare it, or audit it. You're stuck with whatever you happened to look at in the moment. 
 In this walkthrough, we'll build something small but practical: an internal database that continuously captures SpiderRock MLink's LiveImpliedQuote analytics for TSLA, stores each snapshot as queryable history, and also maintains a "latest view" table so you can pull the current surface state without scanning the full history. 
 The goal is not to build a trading system. It's to build a reliable internal dataset that you can monitor and query. 
 Note: SpiderRock MLink's LiveImpliedQuote analytics is a product offered for a fee, which includes exchange charges for the underlying market data used in its creation. 
 Table of Contents 
 Prerequisites 
 What Data We're Using 
 Setup: Importing Packages 
 Database Design 
 Pulling LiveImpliedQuote 
 Normalizing the Response Into Rows 
 Writing To The Database 
 Running a Short Polling Capture 
 Analysis: Smile Reconstruction From the Database 
 Pick an Expiry with Good Coverage 
 Rebuild the Smile Across Snapshots 
 Zoom-In Around Spot 
 Analysis: ATM IV and Skew Over Time 
 Alert-Style Thresholds 
 Wrapping Up 
 Prerequisites 
 Before running any of the code in this walkthrough, there are a few things you need to have in place. 
 On the API side, you need a SpiderRock MLink account with access to the LiveImpliedQuote feed. The examples use the REST interface, so no websocket setup is required, but you do need a valid API key. If you don't have one yet, you can reach out to SpiderRock directly to get access. 
 On the Python side, the environment is minimal. You need Python 3.10 or later for the tuple type hint syntax used in one of the function signatures. The external packages are requests, pandas, numpy, and matplotlib. Everything else – sqlite3, time, datetime – is part of the standard library. You can install the external dependencies with: 
 pip install requests pandas numpy matplotlib No database setup is required beyond a writable local path. SQLite creates the file automatically on first run, so there's nothing to install or configure separately. 
 Finally, the walkthrough uses TSLA as the target symbol because it has a liquid and active options chain. If you want to swap in a different underlying, the only thing you need to change is the symbol variable in the config block. 
 What Data We're Using 
 This build is driven by one OptAnalytics message type from SpiderRock MLink: LiveImpliedQuote . 
 Each message represents an option contract and comes with the analytics you actually need for monitoring: 
 the option identifier (symbol, expiry, strike, call or put) 
 surface IV (sVol) and related surface fields 
 Greeks (delta, gamma, theta, vega) 
 context fields like underlying price (uPrc), time to expiry (years), and rate (rate) 
 timestamps and calc source markers, which matter when you're turning a live feed into a database 
 We'll treat sVol as the main volatility field for the article and refer to it as surface IV. That keeps the workflow consistent when we rebuild smiles or compute skew proxies from stored history. 
 The demo uses TSLA because it has a rich and active options chain, which makes the database and queries more interesting even in a short capture window. The same pipeline works for any other underlying – the only thing you change is the symbol filter. 
 Setup: Importing Packages 
 Before touching the database or the API, we set up a small, repeatable environment. This section is intentionally minimal. We only import what we need for three things: making REST calls, storing data in SQLite, and doing basic analysis and plots. 
 import requests
import sqlite3
import pandas as pd
import numpy as np
import time
from datetime import datetime, timezone
import matplotlib.pyplot as plt
plt.style.use('ggplot') requests is used for calling MLink REST endpoints. 
 sqlite3 gives us a lightweight database we can write to locally without extra setup. 
 pandas and numpy are only for shaping and filtering the data once it comes back. 
 time and datetime help us run a polling loop and timestamp each snapshot so the database becomes a real-time series. 
 Database Design 
 If the goal is to make live analytics queryable, the database design has to support two different needs. 
 First, you want an audit trail. Every snapshot should be preserved so you can reconstruct what the surface looked like at a specific time. 
 Second, you also want a fast way to answer "what does it look like right now" without scanning everything you've ever stored. 
 So we use two tables: 
 implied_quote_history : Append-only. Every poll inserts a full snapshot. 
 implied_quote_latest : One row per option contract. Each poll upserts into this table so it always reflects the most recent snapshot. 
 The core of both tables is a stable option identifier. In the feed, the option key is nested, so we normalize it into a single option_key string that includes symbol, expiry, strike, call or put, and venue fields. This becomes the primary key for the latest table and the main join key for queries. 
 #config
api_key = "YOUR SPIDERROCK API KEY"
mlink_url = "https://mlink-live.nms.saturn.spiderrockconnect.com/rest/json"

msg_type = "LiveImpliedQuote"

symbol = "TSLA"
poll_interval_s = 10
poll_duration_s = 120
limit = 2000

#create db connection
db_path = "/mnt/data/optanalytics_iv_greeks.db"

def get_conn(path: str = db_path):
 conn = sqlite3.connect(path)
 conn.execute("PRAGMA journal_mode=WAL;")
 conn.execute("PRAGMA synchronous=NORMAL;")
 return conn

#create db schema
def setup_db(path: str = db_path):
 conn = get_conn(path)
 cur = conn.cursor()

 cur.execute("""
 create table if not exists implied_quote_history (
 id integer primary key autoincrement,
 asof_ts text not null,

 option_key text not null,
 symbol text not null,
 expiry text not null,
 strike real not null,
 cp text not null,

 calc_source text,
 u_prc real,
 years real,
 rate real,

 s_vol real,
 atm_vol real,
 s_mark real,

 o_bid real,
 o_ask real,
 o_bid_iv real,
 o_ask_iv real,

 delta real,
 gamma real,
 theta real,
 vega real,

 src_ts text
 );
 """)

 cur.execute("""
 create index if not exists idx_hist_symbol_expiry_asof
 on implied_quote_history(symbol, expiry, asof_ts);
 """)

 cur.execute("""
 create index if not exists idx_hist_option_asof
 on implied_quote_history(option_key, asof_ts);
 """)

 cur.execute("""
 create table if not exists implied_quote_latest (
 option_key text primary key,

 last_asof_ts text not null,
 symbol text not null,
 expiry text not null,
 strike real not null,
 cp text not null,

 calc_source text,
 u_prc real,
 years real,
 rate real,

 s_vol real,
 atm_vol real,
 s_mark real,

 o_bid real,
 o_ask real,
 o_bid_iv real,
 o_ask_iv real,

 delta real,
 gamma real,
 theta real,
 vega real,

 src_ts text
 );
 """)

 cur.execute("""
 create index if not exists idx_latest_symbol_expiry
 on implied_quote_latest(symbol, expiry);
 """)

 conn.commit()
 conn.close()

setup_db() This creates the SQLite database file and both tables. The history table is append-only and indexed for the two queries we'll run later: pulling snapshots by expiry and time, and pulling a specific option's timeline by option_key . The latest table is keyed by option_key , which lets us upsert and maintain a consistent "current view." 
 The columns we store are intentionally opinionated. We keep surface IV (s_vol), surface mark (s_mark), Greeks, and a few context fields. We also store timestamps so later we can reason about when a value was produced. 
 Pulling LiveImpliedQuote 
 Now we do the first live pull. The goal here is not to build a perfect filter. It's to confirm that we can retrieve a meaningful slice of TSLA option analytics and that the response structure is what we expect. 
 We request LiveImpliedQuote and filter by symbol using the where clause. The response is a list where most rows are actual LiveImpliedQuote messages, and one row at the end is a QueryResult summary. 
 def fetch_live_implied_quote(symbol: str, limit: int = 2000):
 where = f"okey.tk:eq:{symbol}"

 params = {
 "apiKey": api_key,
 "cmd": "getmsgs",
 "msgType": msg_type,
 "where": where,
 "limit": limit
 }

 r = requests.get(mlink_url, params=params)
 r.raise_for_status()
 return r.json()

raw = fetch_live_implied_quote(symbol, limit=limit)
print("raw messages:", len(raw))
print("first type:", raw[0].get("header", {}).get("mTyp") if raw else None) This is a straight REST getmsgs call. We pass the API key, message type, and a simple symbol filter. The limit is important. It caps how many messages we get back in one poll, so for active underlyings, the returned set of strikes and expiries can vary between polls. That's fine for this tutorial, because the goal is to show the database pattern and the types of monitoring queries it enables. 
 This is the output you should see: 
 Normalizing the Response Into Rows 
 Right now, raw is a list of nested message objects. That format is fine for transport, but it's not something you can store or query directly. So now, we turn each LiveImpliedQuote message into one flat row with a consistent schema. 
 def make_option_key(okey: dict) -> str:
 return "|".join([
 str(okey.get("tk")),
 str(okey.get("dt")),
 str(okey.get("xx")),
 str(okey.get("cp")),
 str(okey.get("at")),
 str(okey.get("ts")),
 ])

def normalize_liq(raw: list, asof_ts: str, keep_calc_source: str = "Loop") -> pd.DataFrame:
 rows = []

 for row in raw:
 if row.get("header", {}).get("mTyp") != "LiveImpliedQuote":
 continue

 m = row.get("message", {})
 if keep_calc_source and m.get("calcSource") != keep_calc_source:
 continue

 pkey = m.get("pkey", {})
 okey = pkey.get("okey", {})
 if not okey:
 continue

 s_vol = m.get("sVol")
 if s_vol is None or s_vol == 0:
 continue

 o_bid = m.get("oBid", 0) or 0
 o_ask = m.get("oAsk", 0) or 0

 quote_ok = int(not (o_bid == 0 and o_ask == 0))

 rows.append({
 "asof_ts": asof_ts,
 "option_key": make_option_key(okey),

 "symbol": okey.get("tk"),
 "expiry": okey.get("dt"),
 "strike": okey.get("xx"),
 "cp": okey.get("cp"),

 "calc_source": m.get("calcSource"),
 "u_prc": m.get("uPrc"),
 "years": m.get("years"),
 "rate": m.get("rate"),

 "s_vol": s_vol,
 "atm_vol": m.get("atmVol"),
 "s_mark": m.get("sMark"),

 "o_bid": o_bid,
 "o_ask": o_ask,
 "o_bid_iv": m.get("oBidIv"),
 "o_ask_iv": m.get("oAskIv"),
 "quote_ok": quote_ok,

 "delta": m.get("de"),
 "gamma": m.get("ga"),
 "theta": m.get("th"),
 "vega": m.get("ve"),

 "src_ts": m.get("timestamp"),
 })

 df = pd.DataFrame(rows)
 if df.empty:
 return df

 df = (
 df.sort_values("src_ts")
 .drop_duplicates(subset=["option_key"], keep="last")
 .reset_index(drop=True)
 )
 return df

asof_ts = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
snapshot_df = normalize_liq(raw, asof_ts)

print("snapshot rows:", len(snapshot_df))
print("quote_ok distribution:", snapshot_df["quote_ok"].value_counts().to_dict() if not snapshot_df.empty else {})
snapshot_df.head() There are three practical decisions baked into this normalization step: 
 First, we build a stable option_key from the option identifier so we have a consistent primary key for the latest table. 
 Second, we keep only calcSource="Loop" . LiveImpliedQuote can include both Tick and Loop records. Loop records tend to be more consistent for snapshot-style analysis because the underlying reference price is stable across the surface. 
 Third, we avoid aggressive filtering. In this dataset, the top-of-book bid and ask fields can be zero even when the analytics fields are populated. So instead of dropping those rows, we store a quote_ok flag and keep the record. That keeps the pipeline usable while still making it obvious later which rows had live quotes. 
 This is the output: 
 At this point, one row represents one option contract snapshot. The fact that quote_ok is 0 across the board simply means bid and ask are not populated in this slice, even though surface IV, Greeks, and other analytics fields are present. That's still useful for building a monitoring database, because the core idea here is tracking the evolution of analytics over time, not reconstructing executable markets. 
 Writing to the Database 
 Now that we have a clean snapshot DataFrame, the job is to persist it in two places. 
 History table: Append everything. This is the audit log. Latest table: Upsert by option_key . This is the fast "current view." 
 This separation is what makes the database useful. History lets you reconstruct any past snapshot. Latest lets you answer "what does the surface look like right now" without scanning time series. 
 def safe_add_column(table: str, col: str, col_type: str, path: str = db_path):
 conn = get_conn(path)
 cur = conn.cursor()
 existing = [r[1] for r in cur.execute(f"PRAGMA table_info({table});").fetchall()]
 if col not in existing:
 cur.execute(f"ALTER TABLE {table} ADD COLUMN {col} {col_type};")
 conn.commit()
 conn.close()

safe_add_column("implied_quote_history", "quote_ok", "INTEGER")
safe_add_column("implied_quote_latest", "quote_ok", "INTEGER")

def write_snapshot_to_db(df: pd.DataFrame, path: str = db_path) -> tuple[int, int]:
 if df.empty:
 return 0, 0

 conn = get_conn(path)
 cur = conn.cursor()

 cols = [
 "asof_ts",
 "option_key","symbol","expiry","strike","cp",
 "calc_source","u_prc","years","rate",
 "s_vol","atm_vol","s_mark",
 "o_bid","o_ask","o_bid_iv","o_ask_iv",
 "delta","gamma","theta","vega",
 "quote_ok","src_ts"
 ]

 for c in cols:
 if c not in df.columns:
 df[c] = None

 insert_df = df[cols].copy()

 cur.executemany(
 """
 insert into implied_quote_history (
 asof_ts,
 option_key, symbol, expiry, strike, cp,
 calc_source, u_prc, years, rate,
 s_vol, atm_vol, s_mark,
 o_bid, o_ask, o_bid_iv, o_ask_iv,
 delta, gamma, theta, vega,
 quote_ok, src_ts
 ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
 """,
 insert_df.itertuples(index=False, name=None)
 )
 history_inserted = cur.rowcount

 cur.executemany(
 """
 insert into implied_quote_latest (
 option_key,
 last_asof_ts, symbol, expiry, strike, cp,
 calc_source, u_prc, years, rate,
 s_vol, atm_vol, s_mark,
 o_bid, o_ask, o_bid_iv, o_ask_iv,
 delta, gamma, theta, vega,
 quote_ok, src_ts
 ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
 on conflict(option_key) do update set
 last_asof_ts=excluded.last_asof_ts,
 symbol=excluded.symbol,
 expiry=excluded.expiry,
 strike=excluded.strike,
 cp=excluded.cp,
 calc_source=excluded.calc_source,
 u_prc=excluded.u_prc,
 years=excluded.years,
 rate=excluded.rate,
 s_vol=excluded.s_vol,
 atm_vol=excluded.atm_vol,
 s_mark=excluded.s_mark,
 o_bid=excluded.o_bid,
 o_ask=excluded.o_ask,
 o_bid_iv=excluded.o_bid_iv,
 o_ask_iv=excluded.o_ask_iv,
 delta=excluded.delta,
 gamma=excluded.gamma,
 theta=excluded.theta,
 vega=excluded.vega,
 quote_ok=excluded.quote_ok,
 src_ts=excluded.src_ts
 """,
 insert_df[[
 "option_key","asof_ts","symbol","expiry","strike","cp",
 "calc_source","u_prc","years","rate",
 "s_vol","atm_vol","s_mark",
 "o_bid","o_ask","o_bid_iv","o_ask_iv",
 "delta","gamma","theta","vega",
 "quote_ok","src_ts"
 ]].itertuples(index=False, name=None)
 )
 latest_upserted = cur.rowcount

 conn.commit()
 conn.close()
 return history_inserted, latest_upserted

hist_n, latest_n = write_snapshot_to_db(snapshot_df)
print("history inserted:", hist_n)
print("latest upserted:", latest_n) We batch write using executemany so inserts are fast even with thousands of option rows. The history insert is straightforward. The latest write uses a SQLite upsert keyed on option_key , which means if the contract already exists in the latest table, its fields are overwritten with the newest snapshot. 
 You should see: 
 After the first write, both tables have the same number of rows. That's expected, because there is only one snapshot in history so far. Once we start polling multiple snapshots, the history table will grow every cycle, while the latest table will stay roughly flat and continue updating in place. 
 Running a Short Polling Capture 
 At this point, the pipeline works end-to-end for a single snapshot. The whole point of the database, though, is to turn live analytics into a time series. So we run a short capture window and store multiple snapshots back-to-back. 
 This isn't meant to be a production scheduler. It's just a simple loop that runs for a couple of minutes, polls every few seconds, timestamps the snapshot, and writes it to both tables. 
 def poll_and_write(symbol: str, duration_s: int = poll_duration_s, interval_s: int = poll_interval_s):
 start = time.time()
 polls = 0
 total_hist = 0

 while time.time() - start < duration_s:
 asof_ts = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

 raw = fetch_live_implied_quote(symbol, limit=limit)
 df = normalize_liq(raw, asof_ts)

 hist_n, latest_n = write_snapshot_to_db(df)
 polls += 1
 total_hist += hist_n

 print(f"[{polls}] {asof_ts} snapshot_rows={len(df)} history+={hist_n} latest_upsert={latest_n}")
 time.sleep(interval_s)

 print(f"done. polls={polls}, total_history_added={total_hist}")

poll_and_write(symbol, duration_s=120, interval_s=10) Each loop iteration represents one snapshot. We generate a UTC timestamp (asof_ts), pull the latest batch from LiveImpliedQuote, normalize it into rows, then write it into the database. The history table accumulates every snapshot. The latest table overwrites by option_key , so it always represents the most recent view. 
 One practical detail is worth calling out. The API call is capped by limit, so you're not guaranteed to receive an identical set of strikes and expiries every poll. That's why snapshot_rows can vary between iterations. 
 In production, you usually stabilize the slice by pinning specific expiries and a strike band or by interpolating IV to fixed moneyness points. For this tutorial, we're keeping ingestion simple and focusing on the database pattern and the monitoring queries it enables. 
 You should see per-poll telemetry like this: 
 [1] 2026-04-14T18:09:29Z snapshot_rows=1454 history+=1454 latest_upsert=1454
...
done. polls=9, total_history_added=12806 This confirms the database is building a time series. Over nine polls, you stored 12,806 option rows in history. The latest table is updated each time, but it doesn't grow in the same way as history because it overwrites per contract key. 
 From the next section, we'll stop writing and start querying. 
 Analysis: Smile Reconstruction From the Database 
 Once the data is in implied_quote_history , the workflow flips. We stop thinking in terms of "API responses" and start thinking in terms of "queries." This section does two things. First, it picks an expiry that has enough rows to be representative. Then it reconstructs the call-side volatility smile for that expiry across a few timestamps. 
 Pick an Expiry with Good Coverage 
 If you pick an expiry that only appears sporadically in the captured snapshots, the smile plot will be misleading. So we start by looking at which expiries have the most rows in the history table. 
 conn = get_conn()

expiry_counts = pd.read_sql_query(
 """
 select expiry, count(*) as n
 from implied_quote_history
 where symbol = ?
 group by expiry
 order by n desc
 limit 10
 """,
 conn,
 params=(symbol,)
)

conn.close()
expiry_counts This query scans only the history table, filters to TSLA, and counts how many option rows exist per expiry across the capture window. We keep the top 10 and pick the first one as the expiry we'll reconstruct. 
 The expiry date 2026-11-20 has the highest count. 
 Here, the count doesn't mean this expiry is "best" in any trading sense. It just means it showed up most consistently in the captured data. That makes it a practical choice for a clean smile comparison. 
 Rebuild the Smile Across Snapshots 
 Now we query the stored history for one expiry, keep only calls, and plot surface IV (s_vol) against strike for multiple snapshot timestamps. 
 chosen_expiry = "2026-11-20" 

conn = get_conn()
smile = pd.read_sql_query(
 """
 select asof_ts, strike, cp, s_vol, u_prc
 from implied_quote_history
 where symbol = ? and expiry = ?
 """,
 conn,
 params=(symbol, chosen_expiry)
)
conn.close()

smile_calls = smile[smile["cp"] == "Call"].copy()

ts_list = sorted(smile_calls["asof_ts"].unique())
pick = [ts_list[0], ts_list[len(ts_list)//2], ts_list[-1]]

plt.figure(figsize=(9,5))
for ts in pick:
 g = smile_calls[smile_calls["asof_ts"] == ts].sort_values("strike")
 plt.plot(g["strike"], g["s_vol"], label=ts)

plt.title(f"{symbol} Vol Smile (Calls) | Expiry {chosen_expiry} | 3 snapshots")
plt.xlabel("Strike")
plt.ylabel("Implied Vol (s_vol)")
plt.grid(True)
plt.legend()
plt.show() We pull all rows for the chosen expiry from history, then filter to calls so we don't mix put and call shapes. To keep the plot readable, we only plot three snapshots. First, middle, and last. 
 Over a short capture window, the smiles often overlap heavily. That doesn't mean the system isn't working. It usually means the surface didn't move much in those two minutes. The important part is that we can reconstruct and compare it purely from stored history. 
 Zoom-In Around Spot 
 The full-range plot is useful for shape, but it can hide small shifts near the region people actually care about. So we zoom to a band around the underlying price. 
 s0 = float(smile_calls["u_prc"].dropna().median())
low, high = s0 * 0.6, s0 * 1.4

for ts in pick:
 g = smile_calls[smile_calls["asof_ts"] == ts].sort_values("strike")
 g = g[(g["strike"] >= low) & (g["strike"] <= high)]
 plt.plot(g["strike"], g["s_vol"], label=ts)

plt.title(f"{symbol} Vol Smile (Calls) | Expiry {chosen_expiry} | zoomed")
plt.xlabel("Strike")
plt.ylabel("Implied Vol (s_vol)")
plt.grid(True)
plt.legend(fontsize=8)
plt.show() We take a robust spot proxy from the stored u_prc values and then keep strikes within a range around it. The goal is not precision. It's to make the chart readable and show whether the near-ATM region is drifting. 
 Here, even small changes become visible. This is also why storing history matters. If you only looked at one snapshot in isolation, these shifts would be easy to miss or dismiss. 
 Analysis: ATM IV and Skew Over Time 
 A full smile plot is useful, but it's not always the fastest way to monitor a surface. In practice, teams usually track a few summary numbers per expiry so they can spot changes quickly, then drill down only when something looks off. 
 Here we reduce each stored snapshot into two metrics for a single expiry. 
 ATM IV: Surface IV at the strike closest to spot. 
 Skew proxy: Surface IV at 0.9 times spot minus surface IV at 1.1 times spot, using the closest available strikes. 
 chosen_expiry = "2026-11-20"

conn = get_conn()
df = pd.read_sql_query(
 """
 select asof_ts, strike, s_vol, u_prc
 from implied_quote_history
 where symbol = ? and expiry = ? and cp = 'Call'
 """,
 conn,
 params=(symbol, chosen_expiry)
)
conn.close()

df["strike"] = df["strike"].astype(float)
df["s_vol"] = df["s_vol"].astype(float)

def closest_iv(grp: pd.DataFrame, target_strike: float):
 g = grp.iloc[(grp["strike"] - target_strike).abs().argsort()[:1]]
 return float(g["s_vol"].iloc[0]), float(g["strike"].iloc[0])

rows = []
for ts, grp in df.groupby("asof_ts"):
 spot = float(grp["u_prc"].dropna().median())
 atm_target = spot
 down_target = spot * 0.9
 up_target = spot * 1.1

 atm_iv, atm_k = closest_iv(grp, atm_target)
 down_iv, down_k = closest_iv(grp, down_target)
 up_iv, up_k = closest_iv(grp, up_target)

 rows.append({
 "asof_ts": ts,
 "spot": spot,
 "atm_strike": atm_k,
 "atm_iv": atm_iv,
 "k90": down_k,
 "iv_90": down_iv,
 "k110": up_k,
 "iv_110": up_iv,
 "skew_90_110": down_iv - up_iv
 })

metrics = pd.DataFrame(rows).sort_values("asof_ts").reset_index(drop=True)
metrics We query the history table for one expiry and keep only calls, then group by snapshot timestamp. For each snapshot, we use the median u_prc as a spot proxy and pick the closest available strike to spot. That gives ATM IV. We repeat the same approach for 0.9 times spot and 1.1 times spot and compute a skew proxy as the difference. 
 The table also stores the actual strikes used (atm_strike, k90, k110). Options strikes are discrete, so the nearest strike can change between snapshots. Keeping the chosen strikes visible makes the metric explainable when it moves. 
 The output is a table with one row per snapshot timestamp and the computed metrics. 
 Now that we have a clean time series table, we can visualize the two metrics. First, ATM IV. Then, the skew proxy. 
 plt.plot(metrics["asof_ts"], metrics["atm_iv"])
plt.title(f"{symbol} ATM IV over time | Expiry {chosen_expiry}")
plt.xticks(rotation=30, ha="right")
plt.ylabel("ATM IV (s_vol)")
plt.grid(True)
plt.show()

plt.plot(metrics["asof_ts"], metrics["skew_90_110"])
plt.title(f"{symbol} Skew proxy (IV@0.9S - IV@1.1S) | Expiry {chosen_expiry}")
plt.xticks(rotation=30, ha="right")
plt.ylabel("Skew proxy")
plt.grid(True)
plt.show() Here is the first chart, ATM IV over time. 
 ATM IV tends to move slowly over short windows unless there is a sharp repricing event. In this run, it stays fairly stable, which is a realistic outcome for a short capture. The value here is that the database turns "fairly stable" into something you can quantify and compare later, rather than a vague impression. 
 Here is the second chart, Skew proxy over time. 
 The skew proxy is more sensitive because it's based on wing points. If it changes, it usually means the downside is being repriced differently from the upside for that expiry. One nuance is that the nearest available strike can change between snapshots, which can create step-like moves even when the surface isn't moving dramatically. That's why we keep k90 and k110 in the metrics table. It keeps the skew plot explainable. 
 Alert-Style Thresholds 
 Once you have a metrics table per snapshot, adding a monitoring layer is straightforward. The idea isn't to generate trades. It's to flag when the surface moves enough that someone should look closer. 
 Here we do two checks: 
 ATM IV change alert: Flag if ATM IV changes more than a small threshold between snapshots. 
 Skew change alert: Flag if the skew proxy changes more than a threshold between snapshots. 
 alerts = metrics.copy()

alerts["atm_iv_change"] = alerts["atm_iv"].diff()
alerts["skew_change"] = alerts["skew_90_110"].diff()

atm_thresh = 0.002 
skew_thresh = 0.003 

alerts["atm_alert"] = alerts["atm_iv_change"].abs() >= atm_thresh
alerts["skew_alert"] = alerts["skew_change"].abs() >= skew_thresh

alerts[[
 "asof_ts",
 "atm_iv", "atm_iv_change", "atm_alert",
 "skew_90_110", "skew_change", "skew_alert",
 "atm_strike", "k90", "k110"
]] We take the per-snapshot metrics table and compute first differences. Then we compare those changes to thresholds and store boolean flags. The output table keeps both the metrics and the strikes used for the calculations, so any alert is explainable rather than a black box. 
 In this run, the ATM IV alerts are all false, while the skew alert triggers once. 
 The skew alert fires because the skew proxy jumps by more than the threshold between two snapshots. This is explainable. If you see the table, you can see the strikes used for the proxy changed around the same time (k90 shifts from 340 to 315). Because strikes are discrete, nearest-strike metrics can step even when the surface is not moving dramatically. 
 To make this easier to read, we also plot the two series and mark alert points. 
 plt.plot(alerts["asof_ts"], alerts["atm_iv"])
for i, r in alerts[alerts["atm_alert"]].iterrows():
 plt.scatter(r["asof_ts"], r["atm_iv"], s=30, edgecolors="r", alpha=0.6, linewidth=2)
plt.title(f"{symbol} ATM IV with alerts | Expiry {chosen_expiry}")
plt.xticks(rotation=30, ha="right")
plt.grid(True)
plt.show()

plt.plot(alerts["asof_ts"], alerts["skew_90_110"])
for i, r in alerts[alerts["skew_alert"]].iterrows():
 plt.scatter(r["asof_ts"], r["skew_90_110"], s=30, edgecolors="r", alpha=0.6, linewidth=2)
plt.title(f"{symbol} Skew proxy with alerts | Expiry {chosen_expiry}")
plt.xticks(rotation=30, ha="right")
plt.grid(True)
plt.show() Both plots use the same pattern. Plot the metric as a line, then overlay a marker on any timestamp where the corresponding alert flag is true. This makes it obvious when something crossed the threshold. 
 This chart represents skew proxy with alerts. 
 This chart shows one alert marker, which matches what we saw in the table. 
 The ATM IV plot isn't featured since there are no alert points. 
 Wrapping Up 
 In this walkthrough, we used SpiderRock MLink's LiveImpliedQuote feed for TSLA and turned it into a small internal database you can query. We stored every snapshot in an append-only history table, maintained a latest view keyed by a stable option identifier, then used that stored data to rebuild a smile, track ATM surface IV and a simple skew proxy, and add a basic alert rule on top. 
 This fits well in B2B workflows because it turns live analytics into something operational: a dataset you can audit, replay, and monitor. The same pattern works whether you're building an internal dashboard, running routine surface checks for a desk, or doing a quick post-event review without relying on screenshots and one-off notebook runs. 
 If you want to extend it, the most practical next steps are longer capture windows, tracking multiple symbols, and moving from SQLite to Postgres once the data volume grows. If metric stability becomes important, you can also standardize the slice you track per poll or interpolate IV to fixed moneyness points so skew measures don't step when nearest strikes change. 
 With that being said, you've reached the end of the article. Hope you learned something new and useful.
```

---

## 10. How to Migrate to S3 Native State Locking in Terraform

- 日期: 2026-05-07 22:58
- 链接: https://www.freecodecamp.org/news/how-to-migrate-to-s3-native-state-locking-in-terraform/

```
If you've been running Terraform on AWS for any length of time, you know the setup: an S3 bucket for state storage, a DynamoDB table for state locking, and a handful of IAM policies tying them together. It works. It has worked for years. 
 But it has always carried a cost that rarely gets discussed openly. That cost isn't just money, though a DynamoDB table with on-demand billing adds up across multiple teams and environments. 
 The real cost is complexity. Every new AWS environment needs both resources provisioned before Terraform can manage anything else. Every engineer who sets up their first Terraform backend has to understand why two completely different AWS services are responsible for what is logically one thing: storing and protecting state. And every incident involving a stuck lock has required someone to manually delete a record from DynamoDB to unblock the team. 
 In November 2024, AWS announced that S3 now supports native object locking for Terraform state files, meaning DynamoDB is no longer required for state locking . Terraform 1.10 added support for this feature, and it's now generally available. 
 In this tutorial, you'll learn: 
 What S3 native locking is and how it works 
 How to set it up from scratch if you're starting a new project 
 How to migrate an existing S3 + DynamoDB setup to S3 native locking safely 
 How to verify locking is working and handle edge cases 
 By the end, you'll have a simpler, cleaner Terraform backend with one fewer AWS resource to manage. 
 Table of Contents 
 What Is Terraform State Locking? 
 What Is S3 Native State Locking? 
 How S3 Native Locking Compares to the S3 + DynamoDB Approach 
 Prerequisites 
 Part 1: Fresh Setup – How to Configure S3 Native Locking from Scratch 
 Step 1: Create the S3 Bucket with Versioning and Encryption 
 Step 2: Configure the Terraform Backend with Native Locking 
 Step 3: Initialize and Verify 
 Part 2: Migration – How to Move from S3 + DynamoDB to S3 Native Locking 
 Step 1: Verify Your Current Setup 
 Step 2: Enable Object Lock on the Existing S3 Bucket 
 Step 3: Update the Terraform Backend Configuration 
 Step 4: Reinitialize Terraform 
 Step 5: Verify the Migration 
 Step 6: Clean Up the DynamoDB Table 
 How to Verify That Locking Is Working 
 How to Handle a Stuck Lock 
 Rollback Plan: If Something Goes Wrong 
 Security Best Practices for Your State Bucket 
 Conclusion 
 References 
 What is Terraform State Locking? 
 Before looking at the new approach, it helps to understand what state locking is solving. 
 Terraform stores everything it knows about your infrastructure in a state file – a JSON document that maps your configuration to real AWS resources. When you run terraform apply , Terraform reads this file, calculates the difference between the current state and your configuration, and makes the necessary changes. 
 The problem arises when two engineers or two CI/CD pipelines run and try to apply changes at the same time. If both read the state file simultaneously, calculate changes independently, and both try to write back, you get a race condition . The second write overwrites changes from the first, and your state is now out of sync with reality. This is a serious problem that can cause resources to be untracked, doubled, or destroyed unexpectedly. 
 State locking solves this by creating a lock when any operation starts that could modify state. If a lock already exists, Terraform refuses to proceed and reports who holds the lock and when it was acquired. Only one operation can hold the lock at a time. When the operation completes, the lock is released. 
 Terraform Run A State File / Lock Terraform Run B
(User 1) (S3/DynamoDB) (User 2)

 | | |
 |------- 1. Acquire Lock ---------->| |
 | | |
 |<------ 2. Lock Granted -----------| |
 | | |
 | |------- 3. Acquire Lock --->|
 | [PROCESSING] | |
 | (Modifying Infrastructure) |<------ 4. Lock Denied -----|
 | | (Wait / Retry) |
 | | |
 |------- 5. Release Lock ---------->| |
 | | |
 | [COMPLETED] |<------ 6. Lock Granted ----|
 | | |
 | | [PROCESSING] |
 | | (Modifying Infrastructure) | 
 | | | What Is S3 Native State Locking? 
 Previously, Terraform's S3 backend used a DynamoDB table as the locking mechanism. When a lock was needed, Terraform wrote a record to DynamoDB with a LockID primary key. DynamoDB's conditional writes guaranteed that only one process could create that record, which is what made the locking atomic. 
 S3 native locking uses S3 Object Lock instead. S3 Object Lock is an S3 feature originally designed to enforce WORM (Write Once, Read Many) compliance for regulatory requirements. AWS extended this capability to support Terraform's state locking workflow. 
 When S3 native locking is enabled in your Terraform backend: 
 Terraform writes your state to an .tfstate object in S3 (as before) 
 To acquire a lock, Terraform uses S3's conditional write operations – specifically the if-none-match conditional header to create a lock file atomically 
 If the lock file already exists, S3 rejects the write, and Terraform reports that a lock is held 
 When the operation completes, Terraform deletes the lock file to release the lock. 
 The key difference from DynamoDB: the entire locking mechanism lives inside S3. No second service. No second set of IAM permissions. No second resource to provision. 
 Note: This feature requires Terraform version 1.10.0 or later and an S3 bucket with Object Lock enabled . Object Lock must be enabled at bucket creation time. You can't enable it on an existing bucket through the console or CLI. But there is a supported workaround for existing buckets, which we'll cover in Part 2. 
 How S3 Native Locking Compares to the S3 + DynamoDB Approach 
 Aspect S3 + DynamoDB (Old) S3 Native Locking (New) 
 AWS services required S3 + DynamoDB S3 only 
 IAM permissions needed S3 + DynamoDB permissions S3 permissions only 
 Terraform version Any 1.10.0 or later 
 Setup complexity Two resources, two IAM scopes One resource 
 Stuck lock resolution Delete DynamoDB record Delete S3 lock file 
 Cost S3 storage + DynamoDB on-demand S3 storage only 
 Object Lock requirement Not required Required on S3 bucket 
 Locking mechanism DynamoDB conditional writes S3 conditional writes ( if-none-match ) 
 State versioning S3 Versioning (recommended) S3 Versioning (required for full safety) 
 The functional behavior from Terraform's perspective is identical. Locking works the same way. The lock information displayed when a lock is held has the same structure. The only difference is what happens under the hood. 
 Prerequisites 
 Before you start, make sure you have the following in place: 
 Terraform 1.10.0 or later installed. Check your version: 
 terraform version If you need to upgrade, follow the official upgrade guide . 
 AWS CLI installed and configured with credentials that have permission to create and manage S3 buckets. 
 aws --version
aws sts get-caller-identity # confirm you're authenticated IAM permissions to perform the following S3 actions: 
 s3:CreateBucket 
 s3:PutBucketVersioning 
 s3:PutBucketEncryption 
 s3:PutObjectLegalHold 
 s3:PutObjectRetention 
 s3:GetObject 
 s3:PutObject 
 s3:DeleteObject 
 s3:ListBucket 
 For the migration path : access to your existing Terraform project and the S3 bucket and DynamoDB table currently in use. 
 Part 1: Fresh Setup – How to Configure S3 Native Locking from Scratch 
 Follow this section if you're starting a new Terraform project and want to use S3 native locking from the beginning. 
 Step 1: Create the S3 Bucket with Versioning and Encryption 
 Object Lock must be enabled at bucket creation time . You can't add it afterward through the standard console flow. Create the bucket using the AWS CLI with Object Lock enabled: 
 aws s3api create-bucket \
 --bucket your-project-terraform-state \
 --region us-east-1 \
 --object-lock-enabled-for-bucket Note: For regions other than us-east-1 , add the --create-bucket-configuration flag. 
 aws s3api create-bucket \
 --bucket your-project-terraform-state \
 --region eu-west-1 \
 --create-bucket-configuration LocationConstraint=eu-west-1 \
 --object-lock-enabled-for-bucket Now enable versioning on the bucket. Versioning is required alongside Object Lock and allows Terraform to recover previous state versions if something goes wrong: 
 aws s3api put-bucket-versioning \
 --bucket your-project-terraform-state \
 --versioning-configuration Status=Enabled Enable server-side encryption so your state files are encrypted at rest: 
 aws s3api put-bucket-encryption \
 --bucket your-project-terraform-state \
 --server-side-encryption-configuration '{
 "Rules": [
 {
 "ApplyServerSideEncryptionByDefault": {
 "SSEAlgorithm": "AES256"
 },
 "BucketKeyEnabled": true
 }
 ]
 }' Block all public access to the bucket. A Terraform state file contains resource IDs, IP addresses, and potentially sensitive values. It should never be publicly accessible: 
 aws s3api put-public-access-block \
 --bucket your-project-terraform-state \
 --public-access-block-configuration \
 "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true" Verify the bucket configuration: 
 # Confirm Object Lock is enabled
aws s3api get-object-lock-configuration \
 --bucket your-project-terraform-state
 
# Confirm versioning is enabled
aws s3api get-bucket-versioning \
 --bucket your-project-terraform-state
 
# Confirm encryption is configured
aws s3api get-bucket-encryption \
 --bucket your-project-terraform-state Expected output for the Object Lock check: 
 {
 "ObjectLockConfiguration": {
 "ObjectLockEnabled": "Enabled"
 }
} Step 2: Configure the Terraform Backend with Native Locking 
 In your Terraform project, create or update your backend.tf file: 
 terraform {
 backend "s3" {
 bucket = "your-project-terraform-state"
 key = "production/terraform.tfstate"
 region = "us-east-1"
 
 # Enable S3 native state locking
 # Requires Terraform 1.10.0+ and a bucket with Object Lock enabled
 use_lockfile = true
 
 # Encryption at rest
 encrypt = true
 }
} The critical difference from the old configuration is the use_lockfile = true parameter. Notice what is absent : there's no dynamodb_table argument. No DynamoDB table. No second service. 
 Here's a direct comparison of the old and new configurations: 
 Old configuration (S3 + DynamoDB): 
 terraform {
 backend "s3" {
 bucket = "your-project-terraform-state"
 key = "production/terraform.tfstate"
 region = "us-east-1"
 encrypt = true
 dynamodb_table = "terraform-state-lock" # this goes away
 }
} New configuration (S3 native locking): 
 terraform {
 backend "s3" {
 bucket = "your-project-terraform-state"
 key = "production/terraform.tfstate"
 region = "us-east-1"
 encrypt = true
 use_lockfile = true # this replaces dynamodb_table
 }
} Step 3: Initialize and Verify 
 Run terraform init to initialize the backend: 
 terraform init Expected output: 
 Initializing the backend...
 
Successfully configured the backend "s3"! Terraform will automatically
use this backend unless the backend configuration changes.
 
Initializing provider plugins...
 
Terraform has been successfully initialized! Run a plan to confirm everything is working end-to-end: 
 terraform plan If locking is working, you'll see a brief pause while Terraform acquires the lock before the plan output appears. You'll also see the lock information if you look at the S3 bucket – a .tflock file will appear temporarily alongside your state file during the operation and disappear when it completes. 
 Part 2: Migration – How to Move from S3 + DynamoDB to S3 Native Locking 
 Follow this section if you have an existing Terraform setup using an S3 bucket and DynamoDB table for state locking, and you want to migrate to S3 native locking. 
 Important: Migration requires a maintenance window or at minimum a period where no Terraform operations are running. You're changing the backend configuration, which means all team members and CI/CD pipelines must stop running terraform plan or terraform apply during the migration . The migration itself takes under 10 minutes. 
 Step 1: Verify Your Current Setup 
 Before making any changes, document your existing backend configuration and confirm the state file is accessible: 
 # Confirm your state file is in S3
aws s3 ls s3://your-existing-bucket/path/to/terraform.tfstate
 
# Confirm the DynamoDB table exists
aws dynamodb describe-table \
 --table-name your-dynamodb-lock-table \
 --query 'Table.TableStatus' Check your current backend.tf and note the exact values: 
 # Your current backend.tf - note these values before changing anything
terraform {
 backend "s3" {
 bucket = "your-existing-bucket" # note this
 key = "path/to/terraform.tfstate" # note this
 region = "us-east-1" # note this
 encrypt = true
 dynamodb_table = "your-dynamodb-lock-table" # this will be removed
 }
} Run one final plan to confirm the current state is clean and there are no unexpected changes pending: 
 terraform plan If the plan shows no changes, you're in a safe state to proceed. 
 Step 2: Enable Object Lock on the Existing S3 Bucket 
 This is the most important step in the migration. Object Lock can't normally be enabled on an existing bucket. It's a setting that must be configured at creation time. 
 But AWS provides a way to enable Object Lock on an existing bucket through a support request or through a direct API call that's not exposed in the standard console UI. AWS has officially documented this path for the Terraform migration use case. 
 Run the following AWS CLI command to enable Object Lock on your existing bucket: 
 aws s3api put-object-lock-configuration \
 --bucket your-existing-bucket \
 --object-lock-configuration '{"ObjectLockEnabled": "Enabled"}' Note: This command enables Object Lock in governance mode with no default retention , meaning it enables the locking capability without setting a default retention period on all objects. This is exactly what Terraform's native locking needs: the ability to create and delete lock files, not permanent object retention. 
 Verify Object Lock is now enabled: 
 aws s3api get-object-lock-configuration \
 --bucket your-existing-bucket Expected output: 
 {
 "ObjectLockConfiguration": {
 "ObjectLockEnabled": "Enabled"
 }
} Also verify that versioning is already enabled (it should be if you are running a production Terraform setup): 
 aws s3api get-bucket-versioning \
 --bucket your-existing-bucket Expected output: 
 {
 "Status": "Enabled"
} If versioning isn't enabled, enable it before proceeding: 
 aws s3api put-bucket-versioning \
 --bucket your-existing-bucket \
 --versioning-configuration Status=Enabled Step 3: Update the Terraform Backend Configuration 
 Update your backend.tf to remove the dynamodb_table argument and add use_lockfile = true : 
 terraform {
 backend "s3" {
 bucket = "your-existing-bucket"
 key = "path/to/terraform.tfstate"
 region = "us-east-1"
 encrypt = true
 
 # Add this:
 use_lockfile = true
 
 # Remove this line entirely:
 # dynamodb_table = "your-dynamodb-lock-table"
 }
} Your updated backend.tf should look like this: 
 terraform {
 backend "s3" {
 bucket = "your-existing-bucket"
 key = "path/to/terraform.tfstate"
 region = "us-east-1"
 encrypt = true
 use_lockfile = true
 }
} Step 4: Reinitialize Terraform 
 Run terraform init with the -reconfigure flag. This flag tells Terraform that the backend configuration has changed intentionally and to reinitialize without prompting you to copy state (the state is already in the same bucket): 
 terraform init -reconfigure Expected output: 
 Initializing the backend...
 
Successfully configured the backend "s3"! Terraform will automatically
use this backend unless the backend configuration changes.
 
Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
 
Terraform has been successfully initialized! If you see an error here: The most common cause is that Object Lock wasn't successfully enabled on the bucket. Re-run the verification from Step 2 before proceeding. 
 Step 5: Verify the Migration 
 Run a plan to confirm Terraform is working correctly with the new backend configuration: 
 terraform plan The plan should: 
 Complete successfully 
 Show the same result as the plan you ran in Step 1 (no changes, or the same changes as before) 
 NOT mention DynamoDB anywhere in its output 
 To confirm that locking is actually using S3 instead of DynamoDB, open a second terminal and run a plan while the first one is running. You should see the second terminal output a lock error that mentions S3, not DynamoDB: 
 ╷
│ Error: Error acquiring the state lock
│
│Error message: operation error S3: PutObject, https response error StatusCode: 409,
│ RequestID: ..., api error Conflict: Object lock already exists for this key.
│
│ Lock Info:
│ ID: a1b2c3d4-e5f6-7890-abcd-ef1234567890
│ Path: your-existing-bucket/path/to/terraform.tfstate.tflock
│ Operation: OperationTypePlan
│ Who: user@hostname
│ Version: 1.10.0
│ Created: 2026-05-06 14:22:01 UTC
│ Info:
╵ The Path field shows .tfstate.tflock , a file in your S3 bucket, not a DynamoDB record. This confirms that locking is now handled entirely by S3. 
 Step 6: Clean Up the DynamoDB Table 
 Once you've confirmed the migration is working correctly and your team has run at least one successful plan and apply cycle using the new backend, you can remove the DynamoDB table. 
 Wait at least 24-48 hours before deleting the DynamoDB table if you have CI/CD pipelines or multiple team members. This gives time to catch any pipeline that wasn't updated with the new backend configuration. 
 When you're ready, delete the DynamoDB table: 
 aws dynamodb delete-table \
 --table-name your-dynamodb-lock-table Confirm the deletion: 
 aws dynamodb describe-table \
 --table-name your-dynamodb-lock-table Expected output: 
 An error occurred (ResourceNotFoundException) when calling the DescribeTable operation:
Requested resource not found This error confirms that the table is gone. The migration is complete. 
 If you provisioned the DynamoDB table using Terraform (which is the recommended pattern), remove the resource from your Terraform configuration and run terraform apply to destroy it via Terraform rather than the CLI directly. This keeps your state clean: 
 # Remove this entire block from your Terraform configuration:
resource "aws_dynamodb_table" "terraform_state_lock" {
 name = "terraform-state-lock"
 billing_mode = "PAY_PER_REQUEST"
 hash_key = "LockID"
 
 attribute {
 name = "LockID"
 type = "S"
 }
} After removing the block, run: 
 terraform apply Terraform will detect that the DynamoDB table resource has been removed from configuration and will destroy the table. 
 How to Verify That Locking Is Working 
 After completing either the fresh setup or the migration, use this procedure to independently verify that locking is functioning correctly. 
 Method 1: Observe the lock file during an operation 
 In one terminal, start a long-running plan against a configuration with many resources: 
 terraform plan While it's running, in a second terminal, check for the lock file in S3: 
 aws s3 ls s3://your-bucket/path/to/ | grep tflock You should see a file like: 
 2026-05-06 14:22:01 512 terraform.tfstate.tflock After the plan completes, run the same command again. The .tflock file should be gone. 
 Method 2: Read the lock file contents 
 While a plan is running, download and read the lock file to see its contents: 
 aws s3 cp \
 s3://your-bucket/path/to/terraform.tfstate.tflock \
 /tmp/current.lock && cat /tmp/current.lock Expected output (formatted for readability): 
 {
 "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
 "Operation": "OperationTypePlan",
 "Info": "",
 "Who": "tolani@dev-machine",
 "Version": "1.10.0",
 "Created": "2026-05-06T14:22:01.123456789Z",
 "Path": "your-bucket/path/to/terraform.tfstate"
} This is the same lock information that Terraform displays when a lock is held. It's now a JSON file in S3 rather than a record in DynamoDB. 
 How to Handle a Stuck Lock 
 With the DynamoDB backend, resolving a stuck lock meant deleting a record from the DynamoDB table. With S3 native locking, it means deleting the .tflock file from S3. 
 A lock can get stuck if: 
 A terraform apply or plan process was killed mid-execution 
 A CI/CD pipeline runner crashed during a Terraform operation 
 A network interruption prevented the lock release from completing 
 Here's how you can check for a stuck lock: 
 aws s3 ls s3://your-bucket/path/to/ | grep tflock If a .tflock file exists and no Terraform operation is currently running, it is a stuck lock. 
 You can also read the lock to understand who held it: 
 aws s3 cp \
 s3://your-bucket/path/to/terraform.tfstate.tflock \
 /tmp/stuck.lock && cat /tmp/stuck.lock This tells you who ( Who field) was running the operation, what operation it was ( Operation field), and when it was acquired ( Created field). 
 And you can force-unlock using Terraform like this: 
 terraform force-unlock LOCK-ID Replace LOCK-ID with the ID value from the lock file contents. For example: 
 terraform force-unlock a1b2c3d4-e5f6-7890-abcd-ef1234567890 Terraform will confirm: 
 Do you really want to force-unlock?
 Terraform will remove the lock on the remote state.
 This will allow local Terraform commands to modify this state, even though it
 may be still be in use. Only 'yes' will be accepted to confirm.
 
 Enter a value: yes
 
Terraform state has been successfully unlocked! An alternative is to delete the lock file directly via CLI. If terraform force-unlock doesn't work (for example, because you are running in a CI environment without Terraform available), delete the lock file directly: 
 aws s3 rm s3://your-bucket/path/to/terraform.tfstate.tflock Only delete the lock file if you are certain no Terraform operation is currently running. Deleting a lock that is actively held by a running operation will allow a second concurrent operation to start, which is exactly the race condition locking is designed to prevent. 
 Rollback Plan: If Something Goes Wrong 
 If you encounter problems after migrating, you can roll back to the S3 + DynamoDB setup with these steps. 
 Step 1: Stop all Terraform operations in your team and CI/CD pipelines. 
 Step 2: Recreate the DynamoDB table if you already deleted it: 
 aws dynamodb create-table \
 --table-name terraform-state-lock \
 --attribute-definitions AttributeName=LockID,AttributeType=S \
 --key-schema AttributeName=LockID,KeyType=HASH \
 --billing-mode PAY_PER_REQUEST Step 3: Revert backend.tf to the previous configuration: 
 terraform {
 backend "s3" {
 bucket = "your-existing-bucket"
 key = "path/to/terraform.tfstate"
 region = "us-east-1"
 encrypt = true
 dynamodb_table = "terraform-state-lock" # restored
 # Remove: use_lockfile = true
 }
} Step 4: Reinitialize: 
 terraform init -reconfigure Step 5: Verify: 
 terraform plan The state file hasn't moved, so there's no data loss during a rollback. The only change is which locking mechanism Terraform uses. 
 Note: Object Lock being enabled on the S3 bucket doesn't prevent the rollback. Object Lock and DynamoDB locking can coexist, Object Lock simply adds a capability to the bucket. Using dynamodb_table in your backend config tells Terraform to use DynamoDB regardless of whether Object Lock is enabled on the bucket. 
 Security Best Practices for Your State Bucket 
 Migrating to S3 native locking is a good opportunity to review the overall security configuration of your state bucket. Here are the practices every production Terraform state bucket should implement: 
 Enable Versioning (Required) 
 Versioning is a hard requirement for S3 native locking to work safely. It ensures that if a state file is accidentally overwritten or corrupted, you can restore a previous version. 
 aws s3api put-bucket-versioning \
 --bucket your-state-bucket \
 --versioning-configuration Status=Enabled Block All Public Access (Non-Negotiable) 
 Your state file contains resource ARNs, IP addresses, and may contain sensitive values passed through Terraform variables. It must never be publicly accessible. 
 aws s3api put-public-access-block \
 --bucket your-state-bucket \
 --public-access-block-configuration \
 "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true" Enable Server-Side Encryption 
 Always encrypt state files at rest. AES256 is the minimum. If your organization requires KMS key management: 
 aws s3api put-bucket-encryption \
 --bucket your-state-bucket \
 --server-side-encryption-configuration '{
 "Rules": [
 {
 "ApplyServerSideEncryptionByDefault": {
 "SSEAlgorithm": "aws:kms",
 "KMSMasterKeyID": "arn:aws:kms:us-east-1:123456789012:key/your-kms-key-id"
 },
 "BucketKeyEnabled": true
 }
 ]
 }' Apply Least-Privilege IAM Permissions 
 The role or user that Terraform uses to access the state bucket should have only the permissions it needs. Here's a minimal IAM policy for S3 native locking: 
 {
 "Version": "2012-10-17",
 "Statement": [
 {
 "Sid": "TerraformStateAccess",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::your-state-bucket",
 "arn:aws:s3:::your-state-bucket/*"
 ]
 },
 {
 "Sid": "TerraformStateLocking",
 "Effect": "Allow",
 "Action": [
 "s3:GetObjectLegalHold",
 "s3:PutObjectLegalHold",
 "s3:GetObjectRetention",
 "s3:PutObjectRetention"
 ],
 "Resource": "arn:aws:s3:::your-state-bucket/*.tflock"
 }
 ]
} Notice what is absent: there are no DynamoDB permissions. This is a cleaner, smaller permission set than the old approach required. 
 Enable Access Logging 
 Log all access to your state bucket in CloudTrail or S3 server access logs. This gives you an audit trail of every time state was read, written, or locked: 
 aws s3api put-bucket-logging \
 --bucket your-state-bucket \
 --bucket-logging-status '{
 "LoggingEnabled": {
 "TargetBucket": "your-logging-bucket",
 "TargetPrefix": "terraform-state-access/"
 }
 }' Conclusion 
 AWS S3 native state locking removes the need for a DynamoDB table from your Terraform backend setup. The result is simpler infrastructure, a smaller IAM permission surface, and one fewer service to provision, monitor, and pay for across every environment your team manages. 
 Here's a summary of what you accomplished: 
 Understood what state locking is and why it's required for safe Terraform operations 
 Compared S3 native locking to the existing S3 + DynamoDB approach 
 Set up a fresh Terraform backend using S3 native locking with correct bucket configuration 
 Migrated an existing backend from S3 + DynamoDB to S3 native locking safely 
 Learned how to verify locking, handle stuck locks, and roll back if needed 
 Applied security best practices to the state bucket 
 This pattern – using S3 native locking – is the recommended approach for all new Terraform projects on AWS going forward. If you're managing a large estate with multiple Terraform backends, consider automating the migration using a script or Terraform module that applies the pattern across all your state buckets. 
 If you are building or optimizing cloud infrastructure for a startup and want a complete reference for production-ready Terraform modules, CI/CD pipeline patterns, and infrastructure runbooks, check out The Startup DevOps Field Guide . It covers the full lifecycle of AWS infrastructure from initial setup to production reliability. 
 References 
 HashiCorp - S3 Backend Configuration: use_lockfile 
 HashiCorp: Terraform 1.10 Release Notes 
 AWS Docs: S3 Object Lock Overview 
 AWS Docs: PutObjectLockConfiguration API 
 AWS Docs: S3 Conditional Writes 
 HashiCorp: Backend State Locking 
 HashiCorp: terraform force-unlock Command 
 AWS Docs: Enabling S3 Versioning 
 AWS Docs: S3 Server-Side Encryption
```

---
