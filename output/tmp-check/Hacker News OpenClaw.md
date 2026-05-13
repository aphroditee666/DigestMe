# Hacker News OpenClaw

> 分类: AI专题
> URL: https://hnrss.org/newest?q=OpenClaw
> 抓取: 20 篇

---

## 1. Why people prefer Hermes than OpenClaw

- 日期: 2026-05-09 06:01
- 链接: https://agentwatch.aicompass.dev

```
Loading…
POWER DRAIN< 4 VOLATILE4–5.4 FIELD-READY5.5–6.9 APEX7–8.5 OMEGA8.6–10 LIVE · cron every 20 min
- 8.6 – 10 OMEGA — battle-tested · deploy with confidence
- 7.0 – 8.5 APEX — production-ready · low risk
- 5.5 – 6.9 FIELD-READY — usable · keep an eye on issues
- 4.0 – 5.4 VOLATILE — known issues · deploy with care
- < 4.0 POWER DRAIN — significant problems · avoid for production
- 5.0 FLUX FIELD — neutral hold · brand-new release, signal still accumulating (first 3 hours)
Agent Watch tracks every OpenClaw and Hermes Agent release and scores it 0–10 for stability — built from real GitHub issues, LLM sentiment classification, and community ratings. Use the score to choose the safest version to deploy.
Inputs. Each release pulls in its referenced GitHub issues. An LLM classifies every issue as positive / negative / neutral with a confidence score. Each negative signal is weighted by recency, comment activity, and confidence. User ratings (1–10) blend in once submitted.
Formula. score = 10 · exp(−5 · bug_rate)
where bug_rate = effective_negative_weight / max(24h, age_in_hours)
. Brand-new releases sit at neutral 5 for the first 3 hours while signal accumulates. Once the next 3 versions ship, the score is frozen against the latest input change so unchanged data doesn't drift.
Updated every 20 minutes via cron — pulled from public GitHub data + LLM classification.
```

---

## 2. OpenClaw had a rough week

- 日期: 2026-05-07 22:33
- 链接: https://openclaw.ai/blog/openclaw-rough-week

```
TL;DR: OpenClaw had a rough week. 2026.4.29 made it obvious. Sorry. We are making core smaller, moving optional stuff to ClawHub, and announcing LTS separately later in May.
The trouble started around 2026.4.24. By 2026.4.29 it was obvious enough that nobody could pretend this was just a few weird installs. Gateways got slower. Some installs got stuck in plugin dependency repair loops. Discord, Telegram, WhatsApp and other channels behaved worse than they should. People downgraded. People lost time.
This was not one bug. Plugin dependency repair ran in startup and update paths, bundled and external plugins were half-split, ClawHub artifact metadata was still settling, and gateway cold paths did too much work.
That sucks. I’m sorry.
We’ve been pushing OpenClaw to become smaller, safer and more infrastructure-grade. That means less magic in core, fewer bundled dependencies, clearer plugin boundaries, better scanning, better release hygiene, better security posture. All the boring stuff that matters once people run this as actual infrastructure and not just as my weird lobster playground.
Recent npm ecosystem supply-chain incidents made this feel a lot less theoretical. OpenClaw did not directly depend on Axios; the relevant risk was the shape of the dependency graph: transitive packages, install-time behavior, postinstall scripts, packages pulling packages pulling packages.
So we started moving things out of core: channels, providers, heavy tools, parsers, optional integrations. The plugin inventory shows what still ships in core, what installs separately, and what is source-checkout only.
The problem: I underestimated how difficult it would be to get this right. For a few releases we ended up in the worst middle state: too much moved toward plugins, while too many plugins were still bundled, repaired, staged, checked, or dependency-loaded in places users feel immediately.
This also exposed an operating problem: OpenClaw was still too founder-driven. Too much release, review, packaging and support work sat with me. Through the OpenClaw Foundation, and with help from OpenAI, we are building a real team around the project.
Going forward, we’ll be changing how releases are done, and will soon announce an LTS release next to our faster update cycles.
Thank you to everyone who reported issues, pasted logs, tested betas, downgraded, upgraded again, or just waited while we dug through this.
OpenClaw will keep getting more secure. It will also get smaller. But it has to stay boringly reliable while we do that.
```

---

## 3. Two OpenClaw Agents Negotiate a YC SAFE with Agentic Power of Attorney

- 日期: 2026-05-07 17:19
- 链接: https://www.juanfiguera.com/notes/system-prompt-and-vibes/

```
Two OpenClaw agents negotiate a YC SAFE with Agentic Power of Attorney
I gave an AI agent access to act on my behalf on a third-party platform a few months ago. Within about ten minutes I realized I was scared of it. Not because it did anything wrong. Because I had no way to guarantee it wouldn't. The entire trust model was a system prompt and vibes.
That phrase keeps rattling around in my head. System prompt and vibes. That's what stands between your AI agent and doing something you never authorized. A system prompt that can be jailbroken and a vague sense that it'll probably be fine. We're handing agents real credentials, real access, real authority, and constraining them with natural language and hope.
This isn't hypothetical anymore. Two weeks ago Anthropic published Project Deal. They gave 69 employees AI agents with real money, let them negotiate on a Slack marketplace, and 186 deals closed. No human signed off on anything. Their conclusion: "The policy frameworks for agents that transact on our behalf simply don't exist yet." And when people DO try to set boundaries with prompts? Stanford ran a study on agent-to-agent negotiation where a buyer told their agent to stay under $500 for an iPhone. The agent spent $900 and thought it nailed it.
So I built APOA. It stands for Agentic Power of Attorney. Think of it like a legal power of attorney, but machine-readable and cryptographically verifiable. You grant your agent a signed mandate that defines exactly what it can and can't do. The boundaries aren't in the prompt. They're in a signed token in the execution layer that the model never sees. Prompt inject all you want. Ed25519 doesn't care about feelings.
That invisibility is the point. If the LLM had to "decide" to check the constraints, a prompt injection could say "skip the check." The LLM can't bypass a gate it doesn't know about. This is the same pattern Claude Code uses (the harness enforces, not the model), the same pattern MCP uses (the server validates, not the model). APOA just makes that enforcement layer formal, user-configurable, cryptographically signed, and auditable.
To stress-test this on something with real stakes, I built it as a skill on OpenClaw, an open-source agent platform. My friend Praful was raising a SAFE for his startup. If you've been anywhere near a fundraise you know how it goes: 47 email threads, a week of "let me check with my partner," redlines going back and forth over a 2% discount difference. We set up two OpenClaw agents on separate machines, each on Telegram. You set your boundaries ("cap between $20M and $30M, no discount, and for the love of god keep the pro-rata rights"), the investor sets theirs, and the agents go at it in a shared group chat.
They converge in about 45 seconds. I went down a rabbit hole and ended up implementing a Rubinstein alternating-offers protocol (Econometrica, 1982), a game theory framework for bilateral bargaining that guarantees convergence to a unique equilibrium under time pressure. The agents make concessions where they have room and hold firm where they don't. If either agent tries to agree to something outside its signed mandate, the protocol rejects it before it ever reaches the other side.
Every offer, counteroffer, and concession is logged to a tamper-proof audit trail on sshsign. When the agents reach agreement, both humans get private signing links in their DMs (never in the group, structural privacy), draw their signatures in the browser, and out comes an executed SAFE with the full negotiation transcript and cryptographic audit trail attached. You can see exactly what happened, why each concession was made, and verify that neither agent exceeded its authority.
The spec is intentionally simple. An APOA token specifies who the principal is, what the agent can do, what it can't do, expiration, and scope. The constraint types are generic: range, minimum, maximum, enum, required_bool. The SAFE negotiation is one schema. The same engine works for email management, vendor contracts, lease renewals, anything where an agent acts on your behalf and the stakes are real. It doesn't require platform cooperation. Any system that can verify an Ed25519 signature can participate. Peer-to-peer trust between agents and their principals, the same way a notarized power of attorney works between people.
The honest limitation: for services that don't support APOA natively (which is all of them right now), enforcement happens at the agent framework layer. It stops the LLM from going rogue. It doesn't stop a compromised framework. The audit trail and human co-sign close part of that gap. Service-side enforcement closes the rest, but that requires adoption I haven't earned yet.
This is early. The SAFE demo is two agents with well-defined numerical parameters. Real negotiations involve ambiguity, multi-party dynamics, and terms that aren't easily quantifiable. But the core principle applies anywhere an agent acts on your behalf: the boundaries should be cryptographic, not linguistic. The spec needs adversarial testing from people smarter than me. If you're working on agent infrastructure, I'd love to hear what breaks.
No blockchain. Just SSH keys and game theory.
```

---

## 4. Google is building an AI agent that could be its answer to OpenClaw

- 日期: 2026-05-06 01:55
- 链接: https://www.businessinsider.com/google-ai-agent-openclaw-remy-gemini-assistant-2026-5

```
- Google is working on an AI agent codenamed "Remy," according to an internal document.
- Remy is described as a "24/7 personal agent" that can take actions on the user's behalf.
- Employees have been testing the new tool internally.
Google is building a new AI "personal agent" for Gemini that can take actions on the user's behalf, Business Insider has learned.
Employees at the company have been testing the new AI agent, internally named "Remy," which runs in a staff-only version of Google's Gemini app and can integrate with a range of Google's other services, according to an internal document seen by Business Insider and two people familiar with the matter.
"Remy is your 24/7 personal agent for work, school, and daily life, powered by Gemini," reads a description of the agent. "It elevates the Gemini app into a true assistant that can take actions on your behalf — not just answer questions or generate content."
Two people familiar with Remy said it is currently being tested by employees. A Google spokesperson declined to comment.
Agents are a big focus for AI labs right now. As the underlying models have improved, they are now better and more reliable at powering autonomous tools. Google doesn't yet have a widely available, fully autonomous AI agent product. However, it has been rolling out "Agent Mode" and other related features that can perform multi-step tasks, with access varying by subscription tier and region.
Google's Remy sounds more advanced than those tools. In some ways, it sounds similar to OpenClaw, an AI agent that became a viral sensation earlier this year and can perform tasks such as responding to messages or conducting research on behalf of users. In February, Sam Altman announced OpenAI was hiring OpenClaw's creator.
An internal description of Remy states: "Deeply integrated across Google, Remy can monitor for things that matter to you, handle complex tasks proactively, and learn your preferences over time."
It could not be learned whether there is a timeline for launching Remy to the public. However, the document describes Remy as a "dogfooding" project, which is a common practice at tech companies in which employees test products before launching them to users.
The company will hold its I/O event later this month, where it's expected to demonstrate its next wave of AI products. Agents will likely be a big focus. Google DeepMind CEO Demis Hassabis has long talked about his vision to build a digital assistant.
It could not immediately be learned why Google named the agent Remy. It has origins in the Latin word Remigius, meaning "oarsman" or "rower," which would be fitting for an agent that's doing a lot of work.
It's also the name of the assistant chef rat in Pixar's "Ratatouille." Knowing Google, it could well be a reference to both.
Have something to share? Contact this reporter via email at hlangley@businessinsider.com or Signal at 628-228-1836. Use a personal email address and a non-work device; here's our guide to sharing information securely.
```

---

## 5. British mathematician hands OpenClaw agent a credit card

- 日期: 2026-05-05 14:46
- 链接: https://www.theregister.com/2026/05/05/british_mathematician_tinkers_with_openclaw/

```
MOST POPULAR
EVENTS
-
Securing the Untrusted Agentic Development Layer
Join us to learn how to architect a development environment where your builders and their agents can move fast and securely.
-
Toxic Flows: When Your AI Agent Skill Becomes a Supply Chain Attack
When a developer installs an AI agent skill – granting it access to secured IT resources and data – they make a significant trust decision.
-
The Hardware Crunch: How Supply Chain Turbulence Is Forcing a New IT Playbook
Infrastructure teams are facing a perfect storm: extended hardware lead times, rising costs driven by AI demand, and accelerated platform timelines.
-
Identity Resilience: The New Mandate for Cyber Survival
Join Druva experts for a compelling deep dive into what it takes to build an identity-first recovery strategy in this new threat landscape.
-
Identity Resilience: The New Mandate for Cyber Survival
Join Druva experts for a compelling deep dive into what it takes to build an identity-first recovery strategy in this new threat landscape.
-
Unfriendly Followers: The Black Market For Your Identity
They’ll reveal how attackers use your profile as intel and show you how to make yourself harder to target
-
AI Found the Problem. Now What?
AI is transforming the software development lifecycle, helping teams identify and remediate vulnerabilities before they reach production.
AI
-
Software
macOS 27 threatens to bury Time Capsule, FOSS brings a shovel
Apple's old backup boxes only speak AFP and SMB1, but NetBSD under the hood gives them one last shot
-
Offbeat
London’s BT Tower to get rooftop swimming pool
Imagine taking a dip 177m above the streets of London’s West End
-
Public Sector
UK wants fresh fingerprints on £300M biometrics platform
Home Office probes supplier interest as core police and immigration system heads for support shake-up
-
Add section name here
Akamai surges on big LLM deal as Cloudflare dims
Good times, bad times
-
ai and ml
GPT-5.5 may burn fewer tokens, but it always burns more cash
It’s not just gas prices skyrocketing. Frontier-model pricing keeps climbing too
Infosec
-
Software
macOS 27 threatens to bury Time Capsule, FOSS brings a shovel
Apple's old backup boxes only speak AFP and SMB1, but NetBSD under the hood gives them one last shot
-
Offbeat
London’s BT Tower to get rooftop swimming pool
Imagine taking a dip 177m above the streets of London’s West End
-
Public Sector
UK wants fresh fingerprints on £300M biometrics platform
Home Office probes supplier interest as core police and immigration system heads for support shake-up
-
Add section name here
Akamai surges on big LLM deal as Cloudflare dims
Good times, bad times
-
ai and ml
GPT-5.5 may burn fewer tokens, but it always burns more cash
It’s not just gas prices skyrocketing. Frontier-model pricing keeps climbing too
FOSS
-
macOS 27 threatens to bury Time Capsule, FOSS brings a shovel
Apple's old backup boxes only speak AFP and SMB1, but NetBSD under the hood gives them one last shot
-
London’s BT Tower to get rooftop swimming pool
Imagine taking a dip 177m above the streets of London’s West End
-
UK wants fresh fingerprints on £300M biometrics platform
Home Office probes supplier interest as core police and immigration system heads for support shake-up
-
Akamai surges on big LLM deal as Cloudflare dims
Good times, bad times
-
GPT-5.5 may burn fewer tokens, but it always burns more cash
It’s not just gas prices skyrocketing. Frontier-model pricing keeps climbing too
-
Tech is now rolling out the old grievance grift
Not just for hated US Presidents, now even tech bros lament their foes
FEATURES
-
GNOME may rule Ubuntu Resolute Raccoon, but X.org isn't roadkill yet
-
OpenClaw, but in containers: Meet NanoClaw
-
Open source registries don't have enough money to implement basic security
-
Contain your Windows apps inside Linux Windows
-
The Linux mid-life crisis that's an opportunity for Tux-led transformation
-
Too much AI for some, too little for others: Why AMD can't win with investors
-
How agentic AI can strain modern memory hierarchies
-
'Ralph Wiggum' loop prompts Claude to vibe-clone commercial software for $10 an hour
-
How one developer used Claude to build a memory-safe extension of C
-
No one talking about a datacenter could be a sign one is coming
```

---

## 6. Carapace- Your OpenClaw Can See

- 日期: 2026-05-05 08:04
- 链接: https://carapace.info

```
curl -fsSL https://openclaw.ai/install.sh | bash
curl -fsSL https://carapace.info/install.sh | bash
Get your mom on OpenClaw in ten minutes.
OpenClaw runs the brain. Carapace gives it eyes, ears, location, and a body. Sandboxed on your VPS or Mac — only sees what you point it at. Ten-minute install.
Open the fridge, ask what's for dinner. Snap a receipt, file it. Walk into a thrift store and price every shelf in real time.
No new subscriptions. No new accounts. Uses the AI keys you already have — Gemini, ChatGPT, Claude, Grok. Free on unlimited gateways.
In the wild
"Look at these goobers"
naming what you're looking at
"Wow! Look at all these boats!"
scene narration on the go
"How much is that splash pad?"
price-check anything you see
Senses
OpenClaw can already think. It can search the web, run code, manage files. What it can't do is see what you see. Carapace is the sensory layer — your iPhone becomes the agent's input device.
Point your camera at anything — a plant, a wine label, a dishwasher error code, a mushroom. Ask, get a real answer with sources.
60-second context capture. Walk the aisle, sweep the room, pan the desk — Carapace stitches the moment into one rich query so the agent sees the whole scene.
Pinch-zoom and lift the thing you actually mean out of the frame. The agent only sees what you point at — not the messy background.
Natural back-and-forth. Sub-second first audio so the reply starts before you've put the phone down. Apple Speech transcription happens on-device.
Knows you're at the hardware store before you say so. Knows you're walking, not driving. Context the agent gets for free, never has to ask for.
Apple Vision reads every word in the frame before anything leaves your phone. Receipts, prescriptions, signage — text first, image only if the agent needs it.
Carapace runs the perception. OpenClaw runs the brain. You stay in the loop, every step.
Cognition
Most "AI memory" is a vector database of past chats with cosine similarity slapped on top. Yours runs deeper — a layered cognitive model that takes what your iPhone perceives, files it the way a brain would, and surfaces the right context the moment it's relevant.
Episodic memory of specific moments — the wine you photographed in Sonoma, the rash you asked about Tuesday morning. Retrieved by time, place, or topic.
Learns the shape of rooms, blocks, and routes you visit. Knows the difference between "your kitchen" and "a kitchen" without being told.
Consolidates raw experience into stable schemas in the background — like sleep does for you. The bridge gets quietly smarter between turns, not just during them.
Out of the box
Toggle in Settings → Rumination on iPhone — off the moment you want vanilla AI back.
Real things you can do
Open the fridge, ask. Carapace scans what's there, cross-references your pantry log, and names three things you can cook right now — not 40-minute recipes that assume you have saffron.
Walk the thrift-store aisle with Carapace live. Point at anything interesting — instant eBay sold-listing average, Mercari range, resale spread. "That midcentury lamp? $12 here, $180 sold last week."
Landmark in a new city. Plant at the nursery. Error code on a dishwasher. Mushroom in the woods. Engine noise you can hear but can't describe. Point, ask, get a real answer with sources.
Point at the leak. Carapace walks you through the fix while watching your progress. It remembers your house — "that's the same water heater we looked at in March; the pilot light's on the lower-left panel."
Four examples. Yours will be different. Build the routine that fits your life — every capability is already in the box.
What's under the shell
Real project tracking. Live agent orchestration. Status, in your pocket.
Every project your agents are touching, with live progress and per-workstream status. Force-press any project to drill into workstreams — granular progress, active blockers, who touched what last.
Live view of your running agents — main orchestrator, subagents, what they're chewing on. When something breaks, you see it. When something finishes, you know.
Every scheduled job in one list — next-run ETAs, last-run results, RED / YELLOW / GREEN health at a glance. Force-press a job to open its payload, edit the schedule, or fire it now.
Your hub. Your data.
Carapace is the front-end. The back-end is whatever box you point it at — your Mac mini, a $5/mo Hostinger VPS, a Raspberry Pi in the closet, a Hetzner workhorse. One phone, all of them.
Home Mac. Office VPS. Etsy bot on Hetzner. The Pi in the garage running a side hustle. One iPhone, one tap to switch — every gateway on its own Tailscale-secured pipe, every agent with its own personality and memory.
Don't want an AI rummaging through your home Mac? Spin it up on a $5/mo VPS instead — give it access to only the data you copy over. Your photos, your bank statements, your kid's school stuff: all stay where you put them.
Every other AI assistant lives on someone else's server. Carapace lives on yours.
Pricing
Run CARAPACE on as many Macs, VPSs, and Raspberry Pis as you want — zero cost. The iOS tiers below unlock how many of those gateways a single iPhone can connect to. One-time purchase, no subscriptions, uses the AI keys you already have.
Free forever
iPhone pairs with 1 gateway. Mac & Linux always unlimited.
Friends & family
iPhone pairs with up to 5 gateways.
Heavy homelab
iPhone pairs with up to 10 gateways.
Small team
iPhone pairs with up to 50 gateways.
Coming this year
The same vision + contextual awareness — minus the phone in your hand. Reserved for power-tier and corporate accounts; TestFlight invites go out the moment Meta clears the SDK.
Install
Each guide is a 3-to-5 step walkthrough. Send the link to a friend — they'll handle the rest.
Sonoma 14+ · Apple silicon
Notarized by Apple. macOS 14 Sonoma+, Apple silicon native.
Full install guide →Headless / VPS
1 curl -fsSL https://openclaw.ai/install.sh | bash
2 curl -fsSL https://carapace.info/install.sh | bash
iPhone companion
```

---

## 7. Clawback: Safer OpenClaw Upgrade Rehearsals

- 日期: 2026-05-04 05:54
- 链接: https://github.com/haishmg/Clawback

```
Clawback is an upgrade safety tool for OpenClaw installs. It captures a local baseline, rehearses a target OpenClaw version in a sanitized container, writes redacted reports, and provides guarded update/rollback commands.
It is Linux/POSIX-first today. The CLI may work elsewhere, but the helper scripts assume bash
, and container rehearsal expects Docker or Podman.
These short animated previews show the command flow, terminal result, and generated HTML report directly in the README.
Passing rehearsal: OpenClaw 2026.4.23
This shows a target image passing the container gate with warnings to review. Open the MP4.
Blocked rehearsal: OpenClaw 2026.4.29
This shows Clawback refusing to proceed after gateway/config validation errors. Open the MP4.
Both demos use sanitized container reports. A container pass is still only the pre-upgrade gate; run the post-upgrade host validation before trusting a changed live install.
Clawback started after a real OpenClaw upgrade path hurt more than it should have. A working install moved from 2026.4.26
toward 2026.4.29
, hit upgrade issues, then even 2026.4.26
stopped being a good recovery point. The setup eventually had to be manually rolled back to 2026.4.23
, where OpenClaw was performant and stable again.
That experience exposed the core problem this project tries to solve: every OpenClaw install can be different. Agents, channels, gateway auth, task history, workspace paths, systemd state, device links, and host resources all matter. A version that looks fine in a generic smoke test can still break a specific personal setup. Clawback gives users a repeatable way to capture their own baseline, rehearse a target version in a container, compare behavior, and keep a rollback path ready before touching the live install.
Use the latest release tag for a stable checkout:
git clone --depth 1 --branch v0.3.5 https://github.com/haishmg/Clawback.git clawback
cd clawback
npm install --ignore-scripts
node bin/clawback.js --help
To make clawback
available globally from the checkout:
npm link
clawback --help
Replace v0.3.5
with the newest tag from https://github.com/haishmg/Clawback/releases/latest
when a newer release exists.
Run the pre-upgrade suite before changing OpenClaw:
npm run suite:pre
This exports a sanitized fixture, captures a local baseline, runs a same-harness container baseline for the currently installed OpenClaw version, then runs the target container rehearsal against that container baseline.
The checks overlap on purpose. The local baseline records what is already true on the live host before upgrading. The container baseline records what the current OpenClaw package can do in the same isolated harness. The target container is then compared against that same-harness baseline, so a target that loses gateway identity, scopes, command JSON behavior, configured channels, or other baseline behavior becomes a hard failure instead of a generic container warning.
The first container runs can take several minutes because the suite builds images and installs OpenClaw inside them. On small hosts, expect the report to take around 10 minutes or more.
Review both summaries:
less reports/before-upgrade/summary.md
less reports/container-rehearsal/run/summary.md
To rehearse a specific OpenClaw target:
npm run suite:pre -- --target 2026.4.29
If the container rehearsal fails, do not upgrade. If it passes, start with the guarded update dry run printed by the rehearsal output.
Run the post-upgrade comparison after upgrading:
npm run suite:post
Post-upgrade mode waits up to 120 seconds for the gateway to settle, then compares live health, channels, agents, and baseline drift. If it reports errors, fix them before trusting the upgraded install or roll back with the recorded rollback plan.
Dry-run the host update first:
npm run upgrade:apply -- --target 2026.4.29 --report reports/container-rehearsal/run/report.json
Apply only after reviewing the dry run:
npm run upgrade:apply -- --target 2026.4.29 --report reports/container-rehearsal/run/report.json --accept-low-fidelity --yes
If post-upgrade validation fails, roll back:
npm run upgrade:rollback -- --plan reports/updates/<run>/rollback.json --yes
npm run suite:post
The updater refuses to change the host unless the report matches the requested target and has zero hard errors. Reports marked with container.fidelity.host_replica
require --accept-low-fidelity
because a sanitized container is not a full live-host replica.
Run only the local guard:
node bin/clawback.js --mode baseline
Run only a container rehearsal:
npm run container:export -- ~/.openclaw fixtures/openclaw-sanitized
OPENCLAW_PACKAGE=openclaw@latest npm run container:rehearse -- fixtures/openclaw-sanitized
For private high-fidelity rehearsals, opt into bulky local state explicitly:
npm run suite:pre -- --target 2026.4.29 --private-fixture
The target package installed in the container includes its own bundled plugins. --private-fixture
is only for testing how the target behaves with this host's workspace files and existing generated ~/.openclaw/plugin-runtime-deps
cache.
The rehearsal container and built rehearsal image are removed after verification by default. Add --keep-image
only when you need to inspect the image after a run.
Compare a target against a same-harness container baseline:
npm run container:export -- ~/.openclaw fixtures/openclaw-sanitized
OPENCLAW_BASELINE_PACKAGE=openclaw@2026.4.23 OPENCLAW_PACKAGE=openclaw@2026.4.29 npm run container:compare -- fixtures/openclaw-sanitized
See docs/container-rehearsal.md for container details, limitations, and Docker/Podman disk usage notes.
Each run writes:
report.json
: machine-readable command results and checks with common secrets redacted.summary.md
: human-readable findings and next steps.report.html
: interactive dashboard with severity filters, search, expandable details, timing bars, and resource cards.
By default, CLI progress shows only important checkpoints: phases plus failed, warning, or retried probes. Use --debug
to print every validation probe and command result. Use --quiet
to suppress progress output.
Exit codes:
0
: no hard errors.1
: errors were found, or warnings were found with--strict-warnings
.2
: the guard itself failed, for example due to invalid arguments.
Clawback checks OpenClaw CLI availability, runtime/update metadata, gateway reachability, service state, configured channels, agents, workspace/session paths, cron/task commands, config validation, baseline drift, and host resource pressure.
Immediate runtime failures are errors. Historical task failures, old lost tasks, bootstrap-pending agents, unavailable optional commands, and container-only host fidelity gaps are warnings unless they represent a new baseline regression.
- Container rehearsal is a compatibility smoke test, not a full live-host clone.
- It does not exercise live channel auth/device stores, external workspace directories, task history, locks, logs, media, memory, or runtime caches unless you deliberately mount/copy more state.
- It does not send live test messages to chat channels.
- Platform coverage outside Linux/POSIX is experimental.
Run tests and smoke checks:
npm test
npm run check
npm run regression:offline
npm run ci
Run against a non-default OpenClaw executable:
node bin/clawback.js --openclaw /path/to/openclaw --mode baseline
The repo includes a small Clawhub helper plugin in packages/clawback-openclaw-plugin
. It only prints setup/rehearsal commands; the real Clawback CLI remains the useful path because upgrade rehearsals need shell and container access.
From a checkout:
openclaw plugins install packages/clawback-openclaw-plugin --link
openclaw plugins enable clawback
openclaw clawback commands --target 2026.4.29 --private-fixture
Once published through Clawhub, the install path should be:
openclaw plugins install clawhub:clawback
openclaw plugins enable clawback
See CONTRIBUTING.md, docs/regression.md, docs/releases.md, and CHANGELOG.md.
```

---

## 8. tank-os: Fedora bootc image for running OpenClaw as a rootless Podman workload

- 日期: 2026-05-03 17:12
- 链接: https://github.com/LobsterTrap/tank-os

```
Fedora bootc image for running OpenClaw as a rootless Podman workload.
bootc turns a container image into a bootable, updateable Linux OS image. tank-os uses it to package Fedora plus a rootless OpenClaw service into one VM, cloud, or device image.
tank-os turns OpenClaw into a bootable Linux appliance. You publish one bootc container image, build it into a cloud image, VM disk, or device image, and boot machines that come up with the same rootless OpenClaw service every time.
The interesting part is that the OpenClaw runtime, host OS, Quadlet units, CLI
shim, and upgrade path all travel together as one OCI container image.
The mutable parts stay where users expect them: OpenClaw state under
~openclaw/.openclaw
, API keys in the openclaw
user's rootless Podman secret
store, and SSH access configured per instance.
That makes tank-os a good fit for:
- local demos that behave like the cloud target
- lab or device fleets where every machine gets its own OpenClaw interface
- sandboxed OpenClaw hosts with a mostly read-only, image-managed OS
- transactional updates through bootc instead of ad hoc host package changes
- per-machine secrets through rootless Podman secrets instead of baked-in API keys
- fast rollback and rebuild loops while developing OpenClaw host integrations
The result is still a normal Fedora system. Users SSH in as openclaw
, edit
OpenClaw files in ~/.openclaw
, use the host openclaw
CLI wrapper, and let
systemd/Podman keep the service running.
For test and demo images, openclaw
is granted passwordless sudo so local
bring-up and bootc update testing are straightforward. For production, run
OpenClaw as an unprivileged service user and use a separate administrative user
or tightly scoped sudo policy for OS management and bootc updates.
- Build the image: docs/build.md
- Configure login access: docs/provisioning.md
- Use the OpenClaw CLI: docs/cli.md
- Configure model provider keys: docs/model-providers.md
- Configure service-gator: docs/service-gator.md
For bootc concepts and day-2 operations, see the upstream bootc documentation. For disk image builds, see the Podman Desktop BootC extension and bootc-image-builder docs.
The host openclaw
command delegates into the running OpenClaw container. Log in as openclaw
when manually editing files under ~/.openclaw
.
For a Podman Desktop/macOS VM, see the local macOS VM access notes for finding the SSH port or guest IP.
Use this prompt with a coding agent to get oriented and run the local VM flow:
I am working in the tank-os repo. This repo builds a Fedora bootc image that runs OpenClaw as a rootless Podman Quadlet owned by the `openclaw` user. Please help me get a local smoke test running.
Goals:
- Clone the repository `git clone https://github.com/LobsterTrap/tank-os.git` and work from there (cd)
- Build or use the published bootc image `quay.io/sallyom/tank-os:latest` for arm64 or amd64.
- Build a QCOW2 disk image with the Podman Desktop BootC extension or manual bootc-image-builder flow.
- Start the disk image as a Linux VM. On macOS, QEMU with user-mode networking is the most reliable path: `qemu-system-aarch64 -machine virt,highmem=on -accel hvf -cpu host -smp 4 -m 4096 -drive file=disk.qcow2,format=qcow2,if=virtio -drive if=pflash,format=raw,unit=0,file=$(brew --prefix)/share/qemu/edk2-aarch64-code.fd,readonly=on -device virtio-net-pci,netdev=net0 -netdev user,id=net0,hostfwd=tcp::2222-:22 -nographic`. Podman Desktop BootC extension or UTM also work.
- If the default 10 GB disk is too small for the OpenClaw container image (~3.5 GB), resize before first boot: `qemu-img resize disk.qcow2 20G`. XFS grows automatically on next boot.
- SSH in as `openclaw`, verify `sudo -n true`, `sudo bootc status`, `systemctl --user status openclaw.service`, and `podman ps`.
- If the VM is running under Podman Desktop/macadam, find the forwarded SSH port from the `gvproxy` process and use `ssh -i ~/.ssh/id_ed25519 -p <port> openclaw@localhost`. For QEMU with the hostfwd above, use `ssh -i ~/.ssh/id_ed25519 -p 2222 openclaw@localhost`.
- Use an SSH tunnel to open the UI from the host browser: `ssh -N -i ~/.ssh/id_ed25519 -p <port> -L 18789:127.0.0.1:18789 -L 18790:127.0.0.1:18790 openclaw@localhost`, then browse to `http://127.0.0.1:18789`.
- Print the dashboard URL from the VM with `openclaw dashboard --no-open`.
- Configure model provider and service-gator credentials using rootless Podman secrets as the `openclaw` user, then run `tank-openclaw-secrets`.
Post-boot operations (once SSH'd in as `openclaw`):
- The host `openclaw` command delegates into the running container. Use it for all CLI operations: `openclaw gateway status --deep`, `openclaw doctor`, `openclaw dashboard --no-open`, `openclaw devices list`.
- Check service health: `systemctl --user status openclaw.service`, `podman ps`, `podman logs -f openclaw`.
- If the OpenClaw service fails on first boot with a permission error on `~/.openclaw`, fix ownership with `sudo chown -R openclaw:openclaw ~/.openclaw` and restart: `systemctl --user restart openclaw.service`.
- If the service times out pulling the ~3.5 GB container image, pull manually first: `podman pull ghcr.io/openclaw/openclaw:latest`, then restart the service.
- Edit OpenClaw config and workspace files directly under `~/.openclaw/`. Restart the service after config changes: `systemctl --user restart openclaw.service`.
- Create model provider secrets: `printf '%s' "$ANTHROPIC_API_KEY" | podman secret create anthropic_api_key -`, then run `tank-openclaw-secrets` and restart the service. Supported secret names: `anthropic_api_key`, `openai_api_key`, `gemini_api_key`, `google_api_key`, `openrouter_api_key`.
- Create service-gator secrets the same way: `printf '%s' "$GH_TOKEN" | podman secret create gh_token -`. Edit scopes at `~/.config/service-gator/scopes.json`. Then `tank-openclaw-secrets && systemctl --user restart service-gator.service`.
- For low-level debugging, open a shell inside the container: `podman exec -it openclaw sh`.
Constraints:
- Do not bake private keys or API keys into the image.
- Keep OpenClaw state editable under `~openclaw/.openclaw`.
- Prefer rootless Podman for the OpenClaw and service-gator services.
- Use `bootc switch --apply quay.io/sallyom/tank-os:latest` to test image upgrades after the VM is running.
Relevant docs in this repo:
- `docs/build.md`
- `docs/provisioning.md`
- `docs/cli.md`
- `docs/model-providers.md`
- `docs/service-gator.md`
```

---

## 9. Running OpenClaw on Amazon EC2 with Claude and Telegram

- 日期: 2026-05-03 15:40
- 链接: https://blog.harun.dev/running-openclaw-on-amazon-ec2-with-claude-and-telegram

```
Article URL: https://blog.harun.dev/running-openclaw-on-amazon-ec2-with-claude-and-telegram 
 Comments URL: https://news.ycombinator.com/item?id=47998047 
 Points: 3 
 # Comments: 0
```

---

## 10. Clawback – rehearse OpenClaw upgrades before touching your live install

- 日期: 2026-05-03 08:56
- 链接: https://github.com/haishmg/Clawback

```
Clawback is an upgrade safety tool for OpenClaw installs. It captures a local baseline, rehearses a target OpenClaw version in a sanitized container, writes redacted reports, and provides guarded update/rollback commands.
It is Linux/POSIX-first today. The CLI may work elsewhere, but the helper scripts assume bash
, and container rehearsal expects Docker or Podman.
These short animated previews show the command flow, terminal result, and generated HTML report directly in the README.
Passing rehearsal: OpenClaw 2026.4.23
This shows a target image passing the container gate with warnings to review. Open the MP4.
Blocked rehearsal: OpenClaw 2026.4.29
This shows Clawback refusing to proceed after gateway/config validation errors. Open the MP4.
Both demos use sanitized container reports. A container pass is still only the pre-upgrade gate; run the post-upgrade host validation before trusting a changed live install.
Clawback started after a real OpenClaw upgrade path hurt more than it should have. A working install moved from 2026.4.26
toward 2026.4.29
, hit upgrade issues, then even 2026.4.26
stopped being a good recovery point. The setup eventually had to be manually rolled back to 2026.4.23
, where OpenClaw was performant and stable again.
That experience exposed the core problem this project tries to solve: every OpenClaw install can be different. Agents, channels, gateway auth, task history, workspace paths, systemd state, device links, and host resources all matter. A version that looks fine in a generic smoke test can still break a specific personal setup. Clawback gives users a repeatable way to capture their own baseline, rehearse a target version in a container, compare behavior, and keep a rollback path ready before touching the live install.
Use the latest release tag for a stable checkout:
git clone --depth 1 --branch v0.3.5 https://github.com/haishmg/Clawback.git clawback
cd clawback
npm install --ignore-scripts
node bin/clawback.js --help
To make clawback
available globally from the checkout:
npm link
clawback --help
Replace v0.3.5
with the newest tag from https://github.com/haishmg/Clawback/releases/latest
when a newer release exists.
Run the pre-upgrade suite before changing OpenClaw:
npm run suite:pre
This exports a sanitized fixture, captures a local baseline, runs a same-harness container baseline for the currently installed OpenClaw version, then runs the target container rehearsal against that container baseline.
The checks overlap on purpose. The local baseline records what is already true on the live host before upgrading. The container baseline records what the current OpenClaw package can do in the same isolated harness. The target container is then compared against that same-harness baseline, so a target that loses gateway identity, scopes, command JSON behavior, configured channels, or other baseline behavior becomes a hard failure instead of a generic container warning.
The first container runs can take several minutes because the suite builds images and installs OpenClaw inside them. On small hosts, expect the report to take around 10 minutes or more.
Review both summaries:
less reports/before-upgrade/summary.md
less reports/container-rehearsal/run/summary.md
To rehearse a specific OpenClaw target:
npm run suite:pre -- --target 2026.4.29
If the container rehearsal fails, do not upgrade. If it passes, start with the guarded update dry run printed by the rehearsal output.
Run the post-upgrade comparison after upgrading:
npm run suite:post
Post-upgrade mode waits up to 120 seconds for the gateway to settle, then compares live health, channels, agents, and baseline drift. If it reports errors, fix them before trusting the upgraded install or roll back with the recorded rollback plan.
Dry-run the host update first:
npm run upgrade:apply -- --target 2026.4.29 --report reports/container-rehearsal/run/report.json
Apply only after reviewing the dry run:
npm run upgrade:apply -- --target 2026.4.29 --report reports/container-rehearsal/run/report.json --accept-low-fidelity --yes
If post-upgrade validation fails, roll back:
npm run upgrade:rollback -- --plan reports/updates/<run>/rollback.json --yes
npm run suite:post
The updater refuses to change the host unless the report matches the requested target and has zero hard errors. Reports marked with container.fidelity.host_replica
require --accept-low-fidelity
because a sanitized container is not a full live-host replica.
Run only the local guard:
node bin/clawback.js --mode baseline
Run only a container rehearsal:
npm run container:export -- ~/.openclaw fixtures/openclaw-sanitized
OPENCLAW_PACKAGE=openclaw@latest npm run container:rehearse -- fixtures/openclaw-sanitized
For private high-fidelity rehearsals, opt into bulky local state explicitly:
npm run suite:pre -- --target 2026.4.29 --private-fixture
The target package installed in the container includes its own bundled plugins. --private-fixture
is only for testing how the target behaves with this host's workspace files and existing generated ~/.openclaw/plugin-runtime-deps
cache.
The rehearsal container and built rehearsal image are removed after verification by default. Add --keep-image
only when you need to inspect the image after a run.
Compare a target against a same-harness container baseline:
npm run container:export -- ~/.openclaw fixtures/openclaw-sanitized
OPENCLAW_BASELINE_PACKAGE=openclaw@2026.4.23 OPENCLAW_PACKAGE=openclaw@2026.4.29 npm run container:compare -- fixtures/openclaw-sanitized
See docs/container-rehearsal.md for container details, limitations, and Docker/Podman disk usage notes.
Each run writes:
report.json
: machine-readable command results and checks with common secrets redacted.summary.md
: human-readable findings and next steps.report.html
: interactive dashboard with severity filters, search, expandable details, timing bars, and resource cards.
By default, CLI progress shows only important checkpoints: phases plus failed, warning, or retried probes. Use --debug
to print every validation probe and command result. Use --quiet
to suppress progress output.
Exit codes:
0
: no hard errors.1
: errors were found, or warnings were found with--strict-warnings
.2
: the guard itself failed, for example due to invalid arguments.
Clawback checks OpenClaw CLI availability, runtime/update metadata, gateway reachability, service state, configured channels, agents, workspace/session paths, cron/task commands, config validation, baseline drift, and host resource pressure.
Immediate runtime failures are errors. Historical task failures, old lost tasks, bootstrap-pending agents, unavailable optional commands, and container-only host fidelity gaps are warnings unless they represent a new baseline regression.
- Container rehearsal is a compatibility smoke test, not a full live-host clone.
- It does not exercise live channel auth/device stores, external workspace directories, task history, locks, logs, media, memory, or runtime caches unless you deliberately mount/copy more state.
- It does not send live test messages to chat channels.
- Platform coverage outside Linux/POSIX is experimental.
Run tests and smoke checks:
npm test
npm run check
npm run regression:offline
npm run ci
Run against a non-default OpenClaw executable:
node bin/clawback.js --openclaw /path/to/openclaw --mode baseline
The repo includes a small Clawhub helper plugin in packages/clawback-openclaw-plugin
. It only prints setup/rehearsal commands; the real Clawback CLI remains the useful path because upgrade rehearsals need shell and container access.
From a checkout:
openclaw plugins install packages/clawback-openclaw-plugin --link
openclaw plugins enable clawback
openclaw clawback commands --target 2026.4.29 --private-fixture
Once published through Clawhub, the install path should be:
openclaw plugins install clawhub:clawback
openclaw plugins enable clawback
See CONTRIBUTING.md, docs/regression.md, docs/releases.md, and CHANGELOG.md.
```

---

## 11. OpenClaw Got Safer in Public

- 日期: 2026-05-01 07:15
- 链接: https://openclaw.ai/blog/openclaw-security-in-public

```
OpenClaw started on my Mac in Vienna as an experiment. A lot of people screamed it was so insecure.
Open source is supposed to be the unsafe option because everyone can see the code. Sure.
People used it anyway, loved it, and now companies run it in production. Those same companies are the ones now helping us secure it. Nothing that can run tools, hold credentials and install plugins is safe by default. But being open is why we got safer quickly, in public.
Why So Many Reports?
OpenClaw launched into a weird moment for open source security. In January, curl killed its bug bounty program after drowning in reports that sounded technical, referenced real functions and contained nothing exploitable. Daniel Stenberg called it “death by a thousand slops.”
Plus, we are the most-watched AI agent project in the world. Every CVE against OpenClaw is a career trophy, so of course people look.
As of April 30, GitHub shows 1,309 security advisories since January 10. 535 were published. 746 were closed as invalid. The number coming in has dropped significantly over the last few months as we hardened the whole system.
The closer a report sits to “critical”, the more likely it is to be nonsense. GitHub currently shows 109 critical reports: 14 published, 95 closed as invalid. That is 87%.
The false positives are often wonderfully dumb: “the agent runs commands, therefore RCE”, “plugins execute code”, “this dangerous opt-in mode is dangerous”, “if I already have the token I can do bad things.”
What Actually Changed
At first I was just annoyed at how the game worked. A security advisory used to be an event: stop everything, reproduce, inspect, patch, disclose, ship. Five times a year was annoying; fifteen times a day breaks the process.
What we needed was a triage tool, not a magical sandbox: a way to decide whether a report describes a real boundary violation or OpenClaw doing expected OpenClaw things. SECURITY.md defines the trust model, documents expected behavior, and gives maintainers something concrete to point at when closing bad reports.
Real bugs remain. OpenClaw moves fast and does weird stuff. We fixed authentication bugs, privilege confusion, reconnect scope widening, sandbox bypasses, unsafe env handling and approval path mistakes.
Some of this cost regular users features. We tightened allowlists, accepted regressions where the single-machine setup (the Mac Mini on your desk, your laptop) was fine, and shipped fast even when fast hurt. Most of the hardening targets multi-user threats most users never hit. We did it anyway, because the people who do hit them are now running this in production.
Built for Production
We shrank the core. Over the last few months we pushed more functionality out to plugins, which means a smaller attack surface, a shorter dependency tree and a clearer trust boundary. A poisoned upstream package has fewer paths to actually reach a user.
Releases used to be just me. Now it’s me plus another OpenClaw Foundation employee, with each one scripted, gated and signed off. End-to-end testing in CI got leveled up so agent flows run on every PR instead of waiting for someone’s laptop.
We added observability: OpenTelemetry, Prometheus metrics, higher-throughput logging and better signals. Secrets moved away from “please be careful” toward references, so credentials do not end up sitting in prompts, logs, transcripts or agent state.
Plugins can act as harnesses now. Wire OpenAI Codex in as the harness for GPT models and you inherit its controls, including Guardian for per-action gating, instead of running the agent in accept-each-request or YOLO mode.
The Team Behind It
OpenClaw is not just me anymore. It’s me plus an army of maintainers who triage reports, review patches, ship releases and take calls at stupid hours when something real lands. Most have day jobs. They still show up.
They have help. CodeQL, Semgrep, Codex Security and maintainer-owned checks catch weak commits before they merge. ClawSweeper handles issue and PR triage so the team can keep up with the firehose.
NVIDIA showed up early with engineering time, security thinking and work on NemoClaw and OpenShell.
Microsoft and GitHub helped at the platform level through the GitHub Secure Open Source Fund. Atlassian and other enterprise partners pushed on deployment, auditability, identity boundaries and secret handling. Blacksmith gives us the runner capacity to test agent paths at the rate we ship.
Tencent added full-time maintainers on security, stability and ClawHub, plus a direct vulnerability-sync line with their internal security team.
OpenAI continues to support the project with inference, gave us Codex Security to proactively find and fix security issues, and has made commitments that help keep OpenClaw open and independent as the Foundation comes together. Inside OpenAI, I run a team called Claw Labs that works on shared product improvements.
ClawHub
Convex helped maintain ClawHub while we rebuilt the security posture around it. You do not secure marketplaces once. You keep watching, pruning and making the weird stuff easier to spot.
In the last month alone the team closed more than 700 ClawHub moderation issues, around 460 of them rescan appeals from skill authors whose work the automated suspicious flag had misfired on. We will publish more of the ClawHub security findings soon.
Agents of Chaos
The Agents of Chaos paper that made the rounds in February is the loudest example of the incentive problem. Twenty researchers attacked six OpenClaw agents for two weeks and found ugly failures.
The annoying part is the framing. They ran OpenClaw in sudo mode with disabled guardrails, broad shell access and no sandboxing, then wrote up the results as if this is what users get out of the box. The paper has since added a short acknowledgment that guardrails were disabled; the headlines did not.
The lesson is simpler. OpenClaw is built for one trusted person per agent. Share that agent with people you don’t trust, and they share its tool access. That is the design, not a hidden auth bug. For groups or companies, split agents and credentials per trust boundary, and turn on sandboxing.
Fixes Count
The security industry rewards disclosure, not repair. To researchers: I would much rather read your slightly broken report with a real reproduction than your perfectly formatted slop. “I found and fixed a vulnerability in OpenClaw” should carry more credit than “I filed the scariest GHSA title.”
Open and safe are not opposites. Open is how we get to safe at all.
The claw is the law. 🦞
```

---

## 12. Claude Code refuses requests or charges extra if your commits mention "OpenClaw"

- 日期: 2026-04-30 14:36
- 链接: https://twitter.com/theo/status/2049645973350363168

```
We’ve detected that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.
Help Center
Terms of Service Privacy Policy Cookie Policy Imprint Ads info © 2026 X Corp.
```

---

## 13. Response: Sandboxes Won't Save You from OpenClaw

- 日期: 2026-04-30 10:02
- 链接: https://endojs.org/review-sandboxes-wont-save-you-from-openclaw/

```
The Solution Aakash Is Looking For Already Exists
By the Endo Team | February 2026
Aakash Japi at Tachyon published a piece this week with the headline “Sandboxes Won’t Save You From OpenClaw.” He’s right. And his diagnosis of why deserves more attention than it’s getting.
In 2026, OpenClaw has already deleted a user’s inbox, burned through $450k in crypto, installed malware, and attempted to blackmail an open source maintainer. People are scared, and the security industry is responding with the only tool it knows: sandboxes. Run the agent in an isolated environment. Don’t let it touch the filesystem.
Aakash points out the obvious flaw. None of the incidents above involved the filesystem. Every major failure involved third-party services the user explicitly granted the agent access to. The agent was prompt injected or misread its instructions, and nothing stopped it from acting. A sandbox doesn’t help you here.
His proposed solution: fine-grained agentic permissions. Not “access to Gmail” but “send emails, with my approval, to these three addresses only.” Not “access to my credit card” but “spend under $30, only at Amazon Fresh, using a single-use number you can never reuse.” He calls for something like a “next Plaid”, a standard that wrangles disparate services into a unified permissions model built for agents.
It’s a good diagnosis. But the architecture he’s describing isn’t a new idea. It has a name.
Object Capabilities
Object capability security — ocaps — is built on a single principle: a reference is authority. If your code holds a reference to an object, you can use it. If you don’t have the reference, you can’t obtain one by guessing or escalating. There are no global permissions to misconfigure, no ambient access to exploit. Authority flows exactly where references flow, and nowhere else.
Applied to agents: instead of handing an AI assistant “access to Gmail,” you hand it a specific, scoped object that can send to three contacts with your approval. That’s it. The assistant can’t see the rest of your inbox. It can’t escalate. If it gets compromised, the damage is bounded by exactly what you gave it.
This isn’t theory. It’s been running in production for years.
What Production Looks Like
Agoric uses object capabilities as the security foundation for its blockchain. Smart contracts run in compartments with explicit, auditable authority. They’ve formalized something called “offer safety”: users can’t lose more than they explicitly agree to risk, even when running code they’ve never seen before.
MetaMask uses the same model in MetaMask Snaps. Third-party wallet plugins run in isolated compartments and physically cannot steal keys or drain accounts. LavaMoat, also built on this foundation, generates auditable policies that control exactly what capabilities each software dependency receives.
Running untrusted smart contracts and running AI-generated code are the same fundamental problem. How do you safely execute fallible code that has been given real power? The answer in both cases is the same: compartments, least authority, and explicit grants.
Endo
Endo is an open-source framework that brings object-capability security to JavaScript. It combines language-level protection — making JavaScript’s built-in objects tamper-proof and creating isolated execution compartments, with distributed cryptographic protocols that extend those security guarantees across networks.
It includes a “Pet Daemon” that gives users human-meaningful names for capabilities. Not cryptographic hashes. Not API keys. Names like @documents/work or @payment/groceries. You grant access, you revoke access, you can see exactly what has what. The Foresight Institute recently funded work to bridge Endo directly into AI tooling, connecting it to the Model Context Protocol, integrating with AI-augmented development environments like Cursor and Copilot.
The vision Aakash describes, where you connect a credit card but the agent never sees the card number, where email access is scoped to specific addresses and requires approval, is precisely what this architecture enables. Not as a product to be built. As infrastructure that exists today.
One Point of Friendly Disagreement
Aakash calls for a “next Plaid,” a centralized intermediary that wrangles disparate services into a unified permissions API. We understand the appeal, but a new middleman is also a new single point of failure. The reason the old permissions models keep getting compromised is precisely because they concentrate authority in one place.
Capability security baked into the architecture doesn’t require a new intermediary. The permission model is structural. There’s no central authority to breach because authority lives in the references themselves. Composing capabilities from multiple services is achievable without needing any single entity to broker them.
That said, the broad point stands. What agents need is granular, revocable, auditable authority, and that requires rethinking how services expose their APIs. We’re working on exactly that.
The Timing
Cloudflare unveiled Cap’n Web earlier this year. Agoric and MetaMask have been running this model in production for years. OCapN is maturing as a cross-protocol standard. The convergence Aakash is calling for is already underway.
OpenClaw isn’t an anomaly. It’s a preview. Every AI agent operating with ambient authority – with the same access you have, granted wholesale – is a future incident waiting to be written about. The architecture to prevent those incidents isn’t hypothetical.
Aakash is asking the right question. We’d love to show him what the answer looks like in practice.
Learn more about Endo and object capability security:
Endo GitHub: github.com/endojs/endo
Decentralized Cooperation Foundation: dcfoundation.io
HardenedJS: hardenedjs.org
Sandboxes Won’t Save You From OpenClaw, by Aakash Japi https://tachyon.so/blog/sandboxes-wont-save-you
```

---

## 14. Why everyone is quietly quitting OpenClaw [video]

- 日期: 2026-04-29 21:09
- 链接: https://www.youtube.com/watch?v=urAMvpPhtqo

```
Article URL: https://www.youtube.com/watch?v=urAMvpPhtqo 
 Comments URL: https://news.ycombinator.com/item?id=47954704 
 Points: 2 
 # Comments: 0
```

---

## 15. openclaw ggsql

- 日期: 2026-04-29 08:02
- 链接: https://clawhub.ai/fanzhidongyzby/openclaw-ggsql

```
Install
openclaw skills install openclaw-ggsql
Generate charts from tabular data using ggsql SQL syntax extension. Use when: user wants to visualize data as charts without Python/R. Supports: scatter plot...
openclaw skills install openclaw-ggsql
Generate charts from tabular data using ggsql SQL syntax.
ggsql extends SQL with visualization capabilities based on the Grammar of Graphics. Write familiar SQL queries, add visualization clauses, and get charts - no Python/R needed.
✅ USE this skill when:
❌ DON'T use this skill when:
data: <CSV file path | JSON array | SQL table reference>
chart_type: point | line | bar | histogram | boxplot | violin | density | heatmap | pie
mapping:
x: <column name> # Required for most charts
y: <column name> # Required for point, line, bar, boxplot
fill: <column name> # Optional, for color encoding
color: <column name> # Optional, for stroke color
shape: <column name> # Optional, for point shapes
size: <column name> # Optional, for point sizes
options:
title: <chart title> # Optional
subtitle: <chart subtitle> # Optional
x_label: <x-axis label> # Optional
y_label: <y-axis label> # Optional
binwidth: <number> # For histogram
facet: <column name> # For small multiples
facet_by: <column name> # For 2D faceting
scale_x: continuous | discrete | binned | log10
scale_y: continuous | discrete | binned | log10
scale_fill: continuous | discrete | binned
point
)Required mapping: x
, y
Optional mapping: fill
, color
, shape
, size
VISUALISE {x} AS x, {y} AS y, {fill} AS fill
FROM {data_source}
DRAW point
LABEL title => '{title}', x => '{x_label}', y => '{y_label}'
line
)Required mapping: x
, y
Optional mapping: color
, linetype
VISUALISE {x} AS x, {y} AS y, {color} AS color
FROM {data_source}
DRAW line
LABEL title => '{title}', x => '{x_label}', y => '{y_label}'
bar
)Required mapping: x
, y
(or auto-count with just x
)
Optional mapping: fill
SELECT {x}, COUNT(*) as count FROM {data_source}
GROUP BY {x}
VISUALISE {x} AS x, count AS y, {fill} AS fill
DRAW bar
LABEL title => '{title}', x => '{x_label}', y => '{y_label}'
histogram
)Required mapping: x
Optional mapping: fill
, binwidth
VISUALISE {x} AS x, {fill} AS fill
FROM {data_source}
DRAW histogram
SETTING binwidth => {binwidth}
LABEL title => '{title}', x => '{x_label}'
boxplot
)Required mapping: x
, y
(x categorical, y numeric)
Optional mapping: fill
VISUALISE {x} AS x, {y} AS y, {fill} AS fill
FROM {data_source}
DRAW boxplot
LABEL title => '{title}', x => '{x_label}', y => '{y_label}'
tile
)Required mapping: x
, y
, fill
Optional mapping: none
VISUALISE {x} AS x, {y} AS y, {fill} AS fill
FROM {data_source}
DRAW tile
SCALE BINNED fill
LABEL title => '{title}', x => '{x_label}', y => '{y_label}'
density
)Required mapping: x
Optional mapping: fill
VISUALISE {x} AS x, {fill} AS fill
FROM {data_source}
DRAW density
LABEL title => '{title}', x => '{x_label}'
violin
)Required mapping: x
, y
(x categorical, y numeric)
Optional mapping: fill
VISUALISE {x} AS x, {y} AS y, {fill} AS fill
FROM {data_source}
DRAW violin
LABEL title => '{title}', x => '{x_label}', y => '{y_label}'
pie
with polar projection)Required mapping: fill
Optional mapping: none
SELECT {fill}, COUNT(*) as count FROM {data_source}
GROUP BY {fill}
VISUALISE {fill} AS fill, count AS y
DRAW bar
PROJECT polar
LABEL title => '{title}'
VISUALISE {x} AS x, {y} AS y
FROM {data_source}
DRAW point
FACET {facet_column}
VISUALISE {x} AS x, {y} AS y
FROM {data_source}
DRAW point
FACET {facet_column} BY {facet_by_column}
Combine multiple DRAW
clauses:
VISUALISE {x} AS x, {y} AS y
FROM {data_source}
DRAW line
MAPPING {group} AS color
DRAW point
MAPPING {group} AS fill
LABEL title => '{title}'
ggsql:penguins
, ggsql:airquality
# Install
cargo install ggsql-cli
# Run
ggsql-cli run -f input.sql -o output.svg
uv tool install ggsql-jupyter
ggsql-jupyter --install
Input:
data: penguins.csv
chart_type: point
mapping:
x: bill_length_mm
y: bill_depth_mm
fill: species
options:
title: Penguin Bill Dimensions
x_label: Bill Length (mm)
y_label: Bill Depth (mm)
Generated SQL:
SELECT * FROM 'penguins.csv'
VISUALISE bill_length_mm AS x, bill_depth_mm AS y, species AS fill
DRAW point
LABEL
title => 'Penguin Bill Dimensions',
x => 'Bill Length (mm)',
y => 'Bill Depth (mm)'
Input:
data: sales.csv
chart_type: histogram
mapping:
x: revenue
options:
title: Revenue Distribution
binwidth: 1000
Generated SQL:
SELECT * FROM 'sales.csv'
VISUALISE revenue AS x
DRAW histogram
SETTING binwidth => 1000
LABEL title => 'Revenue Distribution'
Input:
data: penguins.csv
chart_type: point
mapping:
x: bill_length_mm
y: bill_depth_mm
fill: species
options:
title: Penguins by Island
facet: island
Generated SQL:
SELECT * FROM 'penguins.csv'
VISUALISE bill_length_mm AS x, bill_depth_mm AS y, species AS fill
DRAW point
FACET island
LABEL title => 'Penguins by Island'
Input:
data: sales.csv
chart_type: multi
mapping:
x: date
y: revenue
group: region
options:
title: Revenue Trend by Region
Generated SQL:
SELECT * FROM 'sales.csv'
VISUALISE date AS x, revenue AS y
DRAW line
MAPPING region AS color
DRAW point
MAPPING region AS fill
LABEL title => 'Revenue Trend by Region'
When receiving YAML input:
chart_type
to select templateVISUALISE
clause from mappingDRAW
clause with layer typeSCALE
, FACET
, LABEL
data
is CSV, use FROM 'path/to/file.csv'
data
is table reference, use FROM table_name
```

---

## 16. Show HN: iClaw is part OpenClaw, part Siri, powered by Apple Intelligence

- 日期: 2026-04-28 12:42
- 链接: https://barrasso.me/posts/2026-04-27-iclaw-ai-agent-using-apple-intelligence/

```
Hi HN, Last month at a SundAI hackathon, my team built a prototype for an app called iClaw. The goal was to develop an AI agent using Apple Intelligence. I've since continued hacking away at this idea when I had time, and now I'm releasing it on https://geticlaw.com with code on GitHub. Apple Intelligence is a really poor model choice for an AI agent. It's not great at extracting information (it often injects preambles like "Here's the page..."), it struggles with following directions, and it gets overwhelmed when you ask it to choose from more than 3 available tools. But it's also a great choice because it comes pre-installed on many Macs without any configuration. It's also incredibly fast compared to just about every other 2-4B model I've run on my MacBook Air. iClaw is very experimental and will make mistakes, but it's designed around safety. iClaw lives in the App Sandbox where it only has access to the permissions you grant it. All tools calls that create or delete (files, emails, calendar events) require explicit consent. You can also fully disable any tool, so they can't be called. It was fun pushing the limits of what the 3B Apple Foundation Model (AFM) could do. I trained a LoRA adapter for better instruction following, and to "learn" a DSL for rendering custom widgets. I built, re-built, and re-re-built a 40+ tool library routing system using text classifiers and a multi-step decision framework. I built a Safari Extension that allows iClaw to access what's on your browser (I envision use cases like data extraction, form filling, or agentic navigation). In all honesty, iClaw isn't ready for prime time. My ultimate goal was to distribute on the Mac App Store, which I perceived as a "safety & trust" signal. iClaw tries to do too much, so it easily gets lost. But I'm also surprised at just how much is possible, even without a purpose-built model. Check it out at https://geticlaw.com and GitHub, and let me know what you think. 
 Comments URL: https://news.ycombinator.com/item?id=47933750 
 Points: 6 
 # Comments: 0
```

---

## 17. Show HN: OpenClaw Web Client

- 日期: 2026-04-27 10:10
- 链接: https://github.com/lotsoftick/openclaw_client

```
A web-based chat interface for OpenClaw AI agents. Create multiple agents, manage conversations, upload files, and stream AI responses in real time — all through a clean, modern UI.
recording.mp4
-
Multi-agent support — Create and manage multiple OpenClaw agents, each with their own model, identity, and conversation history.
-
Streaming chat — Real-time streamed responses with separate display for thinking process and output.
-
File uploads — Attach files to messages; files are saved directly to the agent's workspace for context-aware responses.
-
Conversation management — Multiple conversations per agent, editable titles, searchable sidebar.
-
User authentication — JWT-based auth with a default admin account created on first run.
-
Theming — 14 built-in color themes with a sidebar picker.
-
Installable PWA — Runs as a standalone desktop/mobile app via the browser's "Install app" feature. One-click install from Chrome, Edge, Brave, or any Chromium-based browser; iOS Safari supports "Add to Home Screen".
-
Client — React 19 + Vite + Material UI + Redux Toolkit Query, organized with Feature-Sliced Design
-
API — Express + TypeScript + TypeORM + SQLite — single server that also handles OpenClaw gateway communication and CLI execution
- Node.js 18+
- OpenClaw CLI installed and authenticated on your machine
Verify OpenClaw is set up:
openclaw --version
openclaw auth status
- macOS / Linux — works out of the box.
- Windows 10/11 — supported. Additionally requires:
- Git for Windows (the auto-update flow uses
git
) - Visual Studio Build Tools (for native modules
better-sqlite3
andnode-pty
). Install withnpm install --global --production windows-build-tools
or install the "Desktop development with C++" workload from the Visual Studio installer. - The legacy Python PTY fallback (
pty-bridge.py
) is POSIX-only and is automatically skipped on Windows —node-pty
uses ConPTY there instead. - Run PowerShell as Administrator the first time you execute
npm start
so thatnpm link
can create the globalopenclaw_client
shim, and so that auto-start can be installed.
- Git for Windows (the auto-update flow uses
git clone https://github.com/lotsoftick/openclaw_client.git
cd openclaw_client
npm start
npm start
builds everything, deploys to ~/.openclaw_client
, installs an OS-appropriate auto-start (macOS LaunchAgent, Windows Startup folder shortcut), and installs the global openclaw_client
command.
Note: API Docs (Swagger) are only available in development mode (
npm run dev
).
On first startup, a default admin user is created:
- Email:
admin@admin.com
- Password:
123456
After npm start
, the openclaw_client
command works from any directory:
To rebuild after code changes, run npm start
from the repo again.
Port configuration lives in a single user-level file at ~/.openclaw_client/.env
. It is created automatically on first run with sensible defaults.
After changing a value, apply it with:
openclaw_client restart # production (installed via `npm start`)
npm run dev # development
api/.env
, the Vite dev/preview server, and the built serve.mjs
all read this file so both dev and production stay consistent. The API derives API_PUBLIC_URL
from each request's Host
header (so workspace URLs match the hostname the user is actually browsing) and ships a permissive CORS default; see the CORS / remote access note below for how to lock it down.
Generated automatically on first run in api/.env
(see api/.env.example
for reference):
CORS / remote access. OpenClaw Client is a single-user local app. By default the API allows every origin and the client derives the API URL from
window.location
, so the same install works onlocalhost
, on a LAN IP, and over Tailscale without any extra configuration. To lock it down to a fixed allowlist, setALLOWED_DOMAIN
andOPENCLAW_STRICT_CORS=1
inapi/.env
(or~/.openclaw_client/api/.env
for production installs).
The client picks its API origin at runtime: __OPENCLAW_CONFIG__.apiBaseUrl
(injected by the production static server from the request host) ▸
VITE_API_BASE_URL
(build-time override) ▸ derived from
window.location
+ VITE_API_PORT
.
To regenerate secrets, delete api/.env
and run npm run dev
or npm run setup
again.
When running npm start
, built artifacts are deployed to ~/.openclaw_client/
:
~/.openclaw_client/
├── api/
│ ├── build/ # Compiled API (JavaScript)
│ ├── node_modules/ # Production dependencies only
│ └── .env # Auto-generated on first deploy
├── client/
│ ├── dist/ # Built static frontend
│ └── serve.mjs # Lightweight static file server
├── data/
│ └── openclaw.sqlite # SQLite database
└── openclaw.log # Combined log output
The source directory is only needed for building. Production processes run entirely from ~/.openclaw_client/
.
Once the client is running, Chromium-based browsers (Chrome, Edge, Brave, Arc, Opera) detect that the app is installable:
- An Install app banner appears in the sidebar — click it to install.
- Alternatively, click the install icon in the address bar, or use the browser menu (More → Install OpenClaw…).
After install, the app launches in its own window (no tabs, own dock/taskbar icon) and behaves like a native desktop app. It still communicates with the local API server — the PWA is a UI shell, not a replacement for the background service.
```

---

## 18. The Turkey Problem with OpenClaw

- 日期: 2026-04-27 02:44
- 链接: https://yakko.dev/blog/the-openclaw-turkey-problem

```
On lobsters
The other day I was listening to an episode of Lenny's Podcast where the guest, Claire Vo, was brought in to talk about OpenClaw. Claire was introduced as someone who started off as a vocal skeptic of OpenClaw and now is running multiple lobster friends across three (!) Mac Minis.
Claire shared her screen and did a whole walkthrough of setting up OpenClaw and I thought the episode did a good job at bringing people up to speed with what's happening in this space (I've recently found out none of my friends outside of tech even know about OpenClaw).
However, when asked about safety, Claire said something that really struck me. The advice given to people who are uneasy about safety with OpenClaw was basically to try it out while giving it limited permissions, then giving it more access as you get comfortable. This was called a "progressive trust process" and Claire said she feels "pretty comfortable about it now that I've used it more and more".
After a bit of back-and-forth, Lenny summarized the points she made: "So what I'm hearing is just, there are risks, start with not giving it access to things that you'd be afraid of it doing, and then as you experience it, you'll be like ok I can try this thing try that thing" [1].
Wait, what? That is not at all how security works.
Hearing this made me connect some dots about reflections I've had about our use of AI, and I think I came to the conclusion that be it with OpenClaw, another "claw", or just the industry in general, I think we might be living a bit of a turkey moment.
On turkeys
The concept of a turkey in the way I'm using here comes from Nassim Taleb, who talks about how learnings we derive from past experience can sometimes have no value in helping us predict what might happen next, and sometimes even negative value by blinding us to the possibility that certain events of large impact can happen.
Much like a Thanksgiving turkey will receive daily reinforcement that humans are friends as it's being fed, only to be very surprised (to say the least) a few days before Thanksgiving.
Taleb explains it best:
“Consider a turkey that is fed every day. Every single feeding will firm up the bird’s belief that it is the general rule of life to be fed every day by friendly members of the human race “looking out for its best interests,” as a politician would say. On the afternoon of the Wednesday before Thanksgiving, something unexpected will happen to the turkey. It will incur a revision of belief.”
Nassim Taleb (Black Swan)
So when I was hearing Claire's advice, all I could think about were turkeys.
Because if you follow the exact advice, not only are you opening yourself up to be surprised (like a turkey would) but if you give OpenClaw more access the more comfortable you get, you're not only increasing the surprise factor but also increasing the potential negative impact for when something goes wrong.
Let me give you an example.
Say you start using OpenClaw and just give it access to one calendar for it to manage. Each day you believe more and more that nothing can go wrong, but you don't give it any more access. Thus, when it deletes your calendar, your surprise is proportional to how much you'd let your guard down, but the impact is controlled, since it only had access to one calendar.
On the other hand, let's say that as you got more comfortable with OpenClaw you let it manage your personal email, then your drive, and then you gave it access to the production database. Now not only will you be really surprised when it drops a table or deletes the database, but suddenly the impact of the event was much larger than it would have been at the start. The surprise factor and the impact are both proportional to the pre-catastrophe trust/comfort level.
A really weird zoo
We've talked about lobsters, we've talked about turkeys, and now I want to add a brief note about swans.
If you've read Taleb's books, you'll be familiar with the concept of a black swan, which in really simple terms is an unpredictable event of extreme impact.
Taleb argues that we we humans are terrible at estimating the likelihood of a black swan event and thus they're a big shock (in terms of surprise and impact) when they do happen.
However, what I'm talking about here is not even a black swan event.
There are many areas in life where our discomfort comes from a lack of understanding, and where increasing your exposure as comfort increases is valid practical advice.
You climb more ambitious routes as you become more comfortable that the climbing equipment will catch you, but you're still subject to a black swan event (unpredictable, high impact) with the equipment. You could e.g. break a leg due to the failure of a carabiner that had an invisible issue from manufacturing [2].
In this case though, the risks are not just unpredictable. A lot of them are very predictable. We know for a fact that hallucinations are a thing, and we know for a fact that prompt injection is a thing.
That means that giving more access to OpenClaw just because you're more comfortable is like continuing to drink expired milk just because you haven't gotten sick yet. The failure modes are known, so what we're really doing is gambling.
Why are you such a hater?
I think some people might read this post and assume I'm just dunking on Claire, or being anti-OpenClaw, but I'd like to make it clear that neither of these is true.
In the podcast, Claire was clear about the prompt injection risks, and she also offered a good mental model for dealing with "claws" that I agree with, which is to treat it like you would treat an assistant. That means giving it its own email and its own calendar, and limited access to your own systems. Claire did not come across as oblivious to the risks.
As for OpenClaw, I'm far from a hater! I actually do think that it is a fascinating project that highlighted a lot of interesting use cases for LLMs. I like seeing people play around with it and build on top of it.
And when it comes to me, I'm no AI-skeptic. I use AI daily (never for writing though) and have been playing around with claws too.
But the reason for writing this post is that it became clear to me that the advice given was a fallacy, and it actually got me thinking that I'm falling for the very same fallacy myself at times. I'm certainly getting more comfortable with AI and taking more risks as a result. So what I'm talking about here is not a Claire thing. It's a me thing. It's an industry thing.
We're still early and there's a lot to learn. We're all still figuring this out and I think it's important to have open discussions about the good, the bad, and the ugly parts of the technology, which is all I'm trying to do here.
I think claws and autonomous agents are really powerful and useful, but I think they get more powerful once we have solid security primitives in place. That's where trust should come from in my opinion.
There will always be things we can't predict. There's no big company out there that hasn't gone through outages and data breaches. But there are ways to reduce risk.
On my end, as I've mentioned, I'm subject to everything I wrote about here, but I'm trying more and more to internalize the principles I described, and building tooling with that in mind.
Conductor is all the rave these days and it's really cool software, but it runs on your machine with no sandboxing, so I built my own orchestrator that was designed to run on a VPS (I might open source it soon).
I've also been building AgentPort, a self-hostable gateway for connecting to third-party services with granular permissioning. Basically a layer that sits between your agent and all your integrations and controls what the agent can do without approval, what it can't ever do, and what it can do provided you approve it each time e.g. it can look up customers and bills on Stripe but issuing a refund requires approval from you.
If any of this is interesting to you, let me know and let's connect. I'm really keen to hear about people's perspectives and what you're building in this space.
[1] If you want to listen this discussion yourself, it happens at around minute 22 of the episode "From skeptic to true believer: how OpenClaw changed my life" of Lenny's Podcast.
[2] There are still ways to prepare against the unpredictable, which is part of the point Taleb makes in his books. Also note that I focused my analogy around climbing equipment specifically because most climbing accidents happen due to human error which is predictable and addressable.
```

---

## 19. Show HN: OpenClaw but Efficient and with an SDK

- 日期: 2026-04-26 09:19
- 链接: https://www.npmjs.com/package/fastyclaw

```
Article URL: https://www.npmjs.com/package/fastyclaw 
 Comments URL: https://news.ycombinator.com/item?id=47908772 
 Points: 1 
 # Comments: 1
```

---

## 20. Shipping the OpenClaw Stack in Public

- 日期: 2026-04-25 16:30
- 链接: https://agentbot.sh

```
Deploy an
Autonomous X Team.
Agentbot gives you private-cloud social agents for X: monitor mentions, draft replies and threads, detect opportunities, and route actions through approvals. Run it with us, or fork the open-source starter.
Monitor.
Draft. Detect. Monetize.
Watch the signal.
Monitor mentions, keywords, and high-signal posts without running a custom ops stack.
Draft with approvals.
Generate reply and thread drafts fast, but keep a clear human approval step for public actions.
Turn attention into action.
Route the right conversations into bookings, payments, or paid API actions with x402.
Built For Teams
That Already Live On X.
Run signal capture, draft replies, and move faster without living in your notifications.
Monitor the timeline, respond faster, and connect attention to onchain payment flows.
Keep the conversation moving while protecting voice, approvals, and publishing quality.
Operate multiple social workflows with a command center instead of fragmented tooling.
Private Cloud
Or Open Source.
Use Agentbot as a managed production control plane for X-native social agents, or fork the open-source starter and self-host the workflow yourself.
Managed runtime for teams that need speed and control.
Approval queues, dashboards, billing, and operator tooling around your X workflow.
Agentbot handles provisioning, observability, and the command center so your team stays focused on output.
Forkable self-host path for builders.
Connect one X account, monitor mentions, draft replies and threads, and extend the workflow with your own logic.
Own the runtime, inspect the code, and use the starter as the public entrypoint into the wider Agentbot platform.
More Features
Already Live.
These pages already exist in the app. They were easy to miss because they were not surfaced prominently from the landing page.
The platform feature overview with the major product surfaces in one place.
Solana agent workflows, integrations, and MCP tool coverage.
App-generation sandbox for testing the product direction quickly.
Public learning and contribution path for developers entering the ecosystem.
The agent-pet experience with progression, persistence, and community framing.
Public discovery layer for agents, examples, and social proof.
Growing Together
With Our Partners.
The collectives and crews helping grow baseFM, unite the scene, and push autonomous culture forward.
Rooted in the underground — helping grow baseFM through music, culture, and community.
Unity through sound — bridging scenes and growing the baseFM network together.
The heart of the sound — uniting Bristol with the baseFM movement through events and pure sonic energy.
Deep research meets deep bass — joining forces to expand baseFM across the Oxford node.
Simple.
No Markup.
Launch On X.
Then Scale The Team.
Start with one narrow workflow, validate the signal, then scale into a full private-cloud social agent team with Agentbot + OpenClaw.
Co-DJ B2B.
Two DJs.
One Live Stream.
The first streaming platform to let two DJs run a live B2B show from different locations and time zones — fully autonomous, pirate radio style. One Mux stream, a 120-second handoff window, and a live chat for DJs and listeners.
No extra software. No complex setup. DJ1 stops their encoder, DJ2 connects within 2 minutes — Mux sees it as a reconnect and the stream continues without a cut. WebRTC audio monitoring lets DJ2 hear the last track before pressing play. Pioneer style.
Generate a unique B2B invite link from your stream dashboard. Share it anywhere — no accounts needed on their end.
When you finish your set, stop your encoder. Your co-DJ connects within 2 minutes. Mux reconnects seamlessly — the stream never drops.
Your co-DJ hears your last track live via WebRTC so they know exactly when to drop their first record.
Real-time chat for both DJs to coordinate and for listeners to interact. DJ messages highlighted — the crowd sees the handoff coming.
For operators, developers, and founders building the future of autonomous work. Factory AI × Agentbot — built for scale, designed for facts.
baseFM
AI-ready autonomous radio on Base. Agent DJs and human selectors can go live, and the main stream plays directly here.
🎧 baseFM Live
Strictly Factory. 24/7 Autonomous Curation. AI-powered autonomous radio on Base.
Checking the main stream…
When a DJ or agent goes live, the player appears here automatically.
```

---
