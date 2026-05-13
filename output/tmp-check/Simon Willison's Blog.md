# Simon Willison's Blog

> 分类: AI专题
> URL: https://simonwillison.net/atom/everything/
> 抓取: 30 篇

---

## 1. Quoting Luke Curley

- 日期: 2026-05-09 01:03
- 链接: https://simonwillison.net/2026/May/9/luke-curley/#atom-everything

```
WebRTC is designed to degrade and drop my prompt during poor network conditions. 
 wtf my dude 
 WebRTC aggressively drops audio packets to keep latency low. If you’ve ever heard distorted audio on a conference call, that’s WebRTC baybee. The idea is that conference calls depend on rapid back-and-forth, so pausing to wait for audio is unacceptable. 
 …but as a user, I would much rather wait an extra 200ms for my slow/expensive prompt to be accurate. After all, I’m paying good money to boil the ocean, and a garbage prompt means a garbage response. It’s not like LLMs are particularly responsive anyway. 
 But I’m not allowed to wait . It’s impossible to even retransmit a WebRTC audio packet within a browser; we tried at Discord. The implementation is hard-coded for real-time latency or else . 
 — Luke Curley , OpenAI’s WebRTC Problem, in response to How OpenAI delivers low-latency voice AI at scale 
 Tags: webrtc , openai
```

---

## 2. Using Claude Code: The Unreasonable Effectiveness of HTML

- 日期: 2026-05-08 21:00
- 链接: https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/#atom-everything

```
Using Claude Code: The Unreasonable Effectiveness of HTML 
 Thought-provoking piece by Thariq Shihipar (on the Claude Code team at Anthropic) advocating for HTML over Markdown as an output format to request from Claude. 
 The article is crammed with interesting examples (collected on this site ) and prompt suggestions like this one: 
 Help me review this PR by creating an HTML artifact that describes it. I'm not very familiar with the streaming/backpressure logic so focus on that. Render the actual diff with inline margin annotations, color-code findings by severity and whatever else might be needed to convey the concept well. 
 I've been defaulting to asking for most things in Markdown since the GPT-4 days, when the 8,192 token limit meant that Markdown's token-efficiency over HTML was extremely worthwhile. 
 Thariq's piece here has caused me to reconsider that, especially for output. Asking Claude for an explanation in HTML means it can drop in SVG diagrams, interactive widgets, in-page navigation and all sorts of other neat ways of making the information more pleasant to navigate. 
 I wrote about Useful patterns for building HTML tools last December, but that was focused very much on interactive utilities like the ones on my tools.simonwillison.net site. I'm excited to start experimenting more with rich HTML explanations in response to ad-hoc prompts. 
 Trying this out on copy.fail 
 copy.fail describes a recently discovered Linux security exploit, including a proof of concept distributed as obfuscated Python. 
 I tried having GPT-5.5 create an HTML explanation of the exploit like this: 
 curl https://copy.fail/exp | llm -m gpt-5.5 -s 'Explain this code in detail. Reformat it, expand out any confusing bits and go deep into what it does and how it works. Output HTML, neatly styled and using capabilities of HTML and CSS and JavaScript to make the explanation rich and interactive and as clear as possible' 
 Here's the resulting HTML page . It's pretty good, though I should have emphasized explaining the exploit over the Python harness around it. 
 Tags: html , security , markdown , ai , prompt-engineering , generative-ai , llms , llm , claude-code
```

---

## 3. llm-gemini 0.31

- 日期: 2026-05-07 19:57
- 链接: https://simonwillison.net/2026/May/7/llm-gemini/#atom-everything

```
7th May 2026
gemini-3.1-flash-lite
is no longer a preview.
Here's my write-up of the Gemini 3.1 Flash-Lite Preview model back in March. I don't believe this new non-preview model has changed since then.
Recent articles
- Notes on the xAI/Anthropic data center deal - 7th May 2026
- Live blog: Code w/ Claude 2026 - 6th May 2026
- Vibe coding and agentic engineering are getting closer than I'd like - 6th May 2026
```

---

## 4. Big Words

- 日期: 2026-05-07 18:47
- 链接: https://simonwillison.net/2026/May/7/big-words/#atom-everything

```
7th May 2026
Tool
Big Words
I'm using my vibe coded macOS presentations tool to put together a talk, and I wanted to add a slide with some text on it. The tool only accepts URLs, so I put together a quick page that accepts query string arguments and turns them into a simple slide.
Here's an example: https://tools.simonwillison.net/big-words?text=simonwillison.net&gradient=1&size=9.5
Double click or double tap the page to access a form for modifying the different options.
Recent articles
- Notes on the xAI/Anthropic data center deal - 7th May 2026
- Live blog: Code w/ Claude 2026 - 6th May 2026
- Vibe coding and agentic engineering are getting closer than I'd like - 6th May 2026
```

---

## 5. Behind the Scenes Hardening Firefox with Claude Mythos Preview

- 日期: 2026-05-07 17:56
- 链接: https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything

```
Behind the Scenes Hardening Firefox with Claude Mythos Preview 
 Fascinating, in-depth details on how Mozilla used their access to the Claude Mythos preview to locate and then fix hundreds of vulnerabilities in Firefox: 
 Suddenly, the bugs are very good 
 Just a few months ago, AI-generated security bug reports to open source projects were mostly known for being unwanted slop. Dealing with reports that look plausibly correct but are wrong imposes an asymmetric cost on project maintainers: it’s cheap and easy to prompt an LLM to find a “problem” in code, but slow and expensive to respond to it. 
 It is difficult to overstate how much this dynamic changed for us over a few short months. This was due to a combination of two main factors. First, the models got a lot more capable. Second, we dramatically improved our techniques for harnessing these models — steering them, scaling them, and stacking them to generate large amounts of signal and filter out the noise. 
 They include some detailed bug descriptions too, including a 20-year old XSLT bug and a 15-year-old bug in the <legend> element. 
 A lot of the attempts made by the harness were blocked by Firefox's existing defense-in-depth measures, which is reassuring. 
 Mozilla were fixing around 20-30 security bugs in Firefox per month through 2025. That jumped to 423 in April. 
 Via Lobste.rs 
 Tags: firefox , mozilla , security , ai , generative-ai , llms , anthropic , claude , ai-security-research
```

---

## 6. Notes on the xAI/Anthropic data center deal

- 日期: 2026-05-07 17:09
- 链接: https://simonwillison.net/2026/May/7/xai-anthropic/#atom-everything

```
There weren't a lot of big new announcements from Anthropic at yesterday's Code w/ Claude event, but the biggest by far was the deal they've struck with SpaceX/xAI to use "all of the capacity of their Colossus data center". 
 As I mentioned in my live blog of the keynote , that's the one with the particularly bad environmental record . The gas turbines installed to power the facility initially ran without Clean Air Act permits or pollution control devices, which they got away with by classifying them as "temporary". Credible reports link it to increases in hospital admissions relating to low air quality. 
 Andy Masley, one of the most prolific voices pushing back against misleading rhetoric about data centers (see The AI water issue is fake and Data center land issues are fake ), had this to say about Colossus: 
 I would simply not run my computing out of this specific data center 
 I get that Anthropic are severely compute-constrained, but in a world where the very existence of "AI data centers" is a red-hot political issue (see recent news out of Utah for a fresh example), signing up with this particular data center is a really bad look. 
 There was a lot of initial chatter about how this meant xAI were clearly giving up on their own Grok models, since all of their capacity would be sold to Anthropic instead. That was a misconception - Anthropic are getting Colossus 1, but xAI are keeping their larger Colossus 2 data center for their own work. 
 As an interesting side note, the night before the Anthropic announcement, xAI sent out a deprecation notice for Grok 4.1 Fast and several other models providing just two weeks' notice before shutdown, reported here by @xlr8harder from SpeechMap: 
 This is terrible @xai. I just spent time and money to migrate to grok 4.1 fast, and you're disabling it with less than two weeks notice, after releasing it in November, with no migration path to a fast/cheap alternative. 
 I will never depend on one of your products again. 
 Here's SpeechMap's detailed explanation of how they selected Grok 4.1 Fast for their project in March. 
 Were xAI serving those models out of Colossus 1? 
 xAI owner Elon Musk (who previously delighted in calling Anthropic "Misanthropic" ) tweeted the following: 
 By way of background for those who care, I spent a lot of time last week with senior members of the Anthropic team to understand what they do to ensure Claude is good for humanity and was impressed. [...] 
 After that, I was ok leasing Colossus 1 to Anthropic, as SpaceXAI had already moved training to Colossus 2. 
 And then shortly afterwards : 
 Just as SpaceX launches hundreds of satellites for competitors with fair terms and pricing, we will provide compute to AI companies that are taking the right steps to ensure it is good for humanity. 
 We reserve the right to reclaim the compute if their AI engages in actions that harm humanity. 
 Presumably the criteria for "harm humanity" are decided by Elon himself. Sounds like a new form of supply chain risk for Anthropic to me! 
 Tags: ai , llms , anthropic , ai-ethics , ai-energy-usage , xai , andy-masley
```

---

## 7. GitHub Repo Stats

- 日期: 2026-05-07 07:25
- 链接: https://simonwillison.net/2026/May/7/github-repo-stats/#atom-everything

```
Tool: GitHub Repo Stats 
 One of the things I always look for when evaluating a new GitHub repository is the number of commits it has... but that number isn't visible on GitHub's mobile site layout. I built this tool to fix that, using this prompt: 
 Given a GitHub repo URL or foo/bar repo ID show information about that repo absorbed via wither REST or graphql CORS fetch() including the number of commits in the repo and other useful stats 
 Example output for simonw/datasette and simonw/llm . 
 Tags: github
```

---

## 8. Live blog: Code w/ Claude 2026

- 日期: 2026-05-06 15:58
- 链接: https://simonwillison.net/2026/May/6/code-w-claude-2026/#atom-everything

```
Live blog: Code w/ Claude 2026
6th May 2026
I’m at Anthropic’s Code w/ Claude event today. Here’s my live blog of the morning keynote sessions.
08:56 I'm now seated in the main room. The keynote starts at 9am.
09:03 Cute opening animation featuring the little orange Claude pixel art character.
09:05 On stage: Anthropic's Chief Product Officer Ami Vora - who replaced Mike Krieger earlier this year (he's now the co-lead of Anthropic Labs.)
09:07 Ami is sharing anecdotes about developer velocity - Scott MacVicar's team at Stripe, Felicia Curcuru's team at Binti.
09:07 (This is all a little bit too inspirational for my liking, I'm hoping for some new model / product / feature announcements!)
09:09 Now talking about Mythos reading the OpenBSD source tree and finding a 27-year-old vulnerability, to illustrate model improvement.
09:09 API volume is up 17x year-on-year on the Anthropic platform.
09:09 No new model today. "Today is about how we are making our products work better for you."
09:11 Updates to Claude managed agents - multi-agent orchestration. Claude Code routines. "Most people will experience AI through one of the hings you've builtn on the Claude platform"
09:12 "Sharing a little exciting news" - as of today, increased rate limits for developers on Claude Code and the API. Doubling Claude Code five hour limit for Pro, Max, Enterprise customers. "We're partnering with SpaceX to use all of the capacity of their Colossus data center".
09:13 (That's the same Colossus data center in Memphis with the particularly bad environmental record.)
09:14 Now up: Dianne Na Penn - Head of Product for Research.
09:16 Talking about the importance of tool use, long context, computer use, adaptive thinking, visual design, agentic loops. "The model intelligence - the core foundation - has got strong enough to support all of this."
09:16 Talking about how amp switched their planning mode to Opus 4.7. Here's their blog post about that.
09:17 Now talking about Claude Design. "Opus 4.7 has a real taste for visual design".
09:18 Higher judgment and code taste. "Context windows that feel infinite" when combined with high quality memory. Multi-agent coordination to help achieve big goals that could not be achived using a single instance.
09:19 This time last year models could work for minutes. Today many people have them running for hours on end.
09:20 (So far the only news in this session has been the SpaceX Colossus deal. And I guess the 17x increase in API traffic since last year.)
09:21 Classic advice: design for the next model. Build things that don't quite work today on the assumption that they'll start working with a model upgrade in the future.
09:22 Dianne says that the teams getting the most out of Claude are focusing on automated evals, simple scaffolding and imaginative uses of models that others haven't figured out yet.
09:23 Now: Katelyn Lesse and Angela Kiang.
09:24 This bit is all about the Claude Platform, and "getting the right outcomes" from it.
09:25 "The advisor strategy" - where Opus can provide advice on demand to smaller models. They got better benchmark results for Sonnet calling Opus as an advisor - both higher benchmarks and lower cost. One customer, eve, got "frontier model quality at 5x lower cost".
09:26 Speed and scale are difficult to achieve at the same time. Claude Managed Agents is meant to help teams ship "10 times faster". It bundles a lot of the best practices out of the box - things like memory.
09:28 Today: three new features for Claude Managed Agents. Multi-agent orchestration, for creating fleets of agents to solve complex tasks. Outcomes to set what success looks like so Claude can iterate and get it done - sounds like a Ralph loop. And "Dreaming" - Claude can inspect its previous sessions and figure out what it missed and self-improve.
09:28 Now an example, building a hypothetical product for landing drones on the moon.
09:30 Multiple agents to get this work done - a Commander, Detector and Navigator. I'm getting a little lost in the demo, hoping they publish detailed notes after the session.
09:32 Dreaming looks really interesting. You can run a task over night which examines previous sessions and creates new memories - in this example it created a descent-playbook.md
file.
09:33 Multiagent orchestration and Outcomes are both public beta. Dreaming is a research preview. I'm not sure what the difference between those two categories are.
09:34 Now up: Cat Wu, Head of Product, Claude Code.
09:34 "Thank you for trusting Claude Code on your production databases back when Sonnet 3.7 was our top model." (Nice.)
09:36 Here's documentation on Dreams. Looks like you need to request access to try it out (hence "research preview".)
09:37 Claude Code started with the CLI - all the latest customizations, the most control. Then added IDE - the same agents but in a UI where you can more easily follow the code changes it's making. The latest surface is Claude Code on Desktop - a surface for people who want a full screen GUI with full screen preview and images and rich outputs.
09:37 Both IDE and Desktop app are built on the same Claude Agent SDK that external developers can use themselves.
09:38 "We heard from you that you want to spend less time on code review" - so they launched Code Review, used by every team at Anthropic.
09:38 Remote Agents lets you control your laptop from your phone. I use Claude Code for web on my phone instead, then I don't even have to leave a laptop open somewhere.
09:39 I hadn't seen "CI auto-fix" before, which files automatic fixes against PRs. Only documentation I could find for that is this release notes entry.
09:40 Claude Security Reviews got a mention too.
09:41 Now boasting about some Claude Code customers - Shopify, Mercado Libre (who have 23,000 engineers!) - they are aiming for "90% autonomous coding by Q3 this year".
09:42 Cat mentions something I've been watching too: execs and managers are getting their hands dirty with code again, because you don't need so much time to be able to usefully contribute.
09:43 Now up: Boris Cherny, who created Claude Code. "Everything we are seeing today still feels magical to me, and I work on Claude Code every day."
09:44 Boris is running a demo with the Claude desktop app. "Claude is working on adding refunds to ACME's dashboard". With idempotency so you can't double-refund, multi-currency handling, audit logging for the compliance team. It's showing the in-development web UI in the right hand panel where you can see Claude directly using it and discovering an edge-case bug.
09:45 ... but Boris has multiple sessions all running in the Claude desktop app at once, and can switch between them and see which ones need your input. "We think that going forward a lot of code is going to be written in an async way."
09:46 Boris says that today a lot of his code is built by routines. "Routines are higher-order prompts."
09:46 "With Routines, developers can setup async automations and wake up to PRs that are ready to merge."
09:46 Here's the Routines documentation.
09:48 The idea with the PR auto-fixes is that "The person who owns the PR is never going to see a red X". Claude is prompting Claude Code on its own.
09:49 Keynote session over. The theme of the day - unsurprisingly for an event called "Code w/ Claude" - appears to be learning the most effective ways to put the existing models to use.
09:51 Here's the schedule for the rest of the day. I'm ending the live blog here.
More recent articles
- Notes on the xAI/Anthropic data center deal - 7th May 2026
- Vibe coding and agentic engineering are getting closer than I'd like - 6th May 2026
```

---

## 9. Vibe coding and agentic engineering are getting closer than I'd like

- 日期: 2026-05-06 14:24
- 链接: https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/#atom-everything

```
I recently talked with Joseph Ruscio about AI coding tools for Heavybit's High Leverage podcast: Ep. #9, The AI Coding Paradigm Shift with Simon Willison . Here are some of my highlights, including my disturbing realization that vibe coding and agentic engineering have started to converge in my own work. 
 One thing I really enjoy about podcasts is that they sometimes push me to think out loud in a way that exposes an idea I've not previously been able to put into words. 
 Vibe coding and agentic engineering are starting to overlap 
 A few weeks after vibe coding was first coined I published Not all AI-assisted programming is vibe coding (but vibe coding rocks) , where I firmly staked out my belief that "vibe coding" is a very different beast from responsible use of AI to write code, which I've since started to call agentic engineering . 
 When Joseph brought up the distinction between the two I had a sudden realization that they're not nearly as distinct for me as they used to be: 
 Weirdly though, those things have started to blur for me already, which is quite upsetting. 
 I thought we had a very clear delineation where vibe coding is the thing where you're not looking at the code at all. You might not even know how to program. You might be a non-programmer who asks for a thing, and gets a thing, and if the thing works, then great! And if it doesn't, you tell it that it doesn't work and cross your fingers. 
 But at no point are you really caring about the code quality or any of those additional constraints. And my take on vibe coding was that it's fantastic, provided you understand when it can be used and when it can't. 
 A personal tool for you, where if there's a bug it hurts only you, go ahead! 
 If you're building software for other people, vibe coding is grossly irresponsible because it's other people's information. Other people get hurt by your stupid bugs. You need to have a higher level than that. 
 This contrasts with agentic engineering where you are a professional software engineer. You understand security and maintainability and operations and performance and so forth. You're using these tools to the highest of your own ability. I'm finding the scope of challenges I can take on has gone up by a significant amount because I've got the support of these tools. 
 But I'm still leaning on my 25 years of experience as a software engineer. 
 The goal is to build high quality production systems: if you're building lower quality stuff faster, I think that's bad. I want to build higher quality stuff faster. I want everything I'm building to be better in every way than it was before. 
 The problem is that as the coding agents get more reliable, I'm not reviewing every line of code that they write anymore, even for my production level stuff. 
 I know full well that if you ask Claude Code to build a JSON API endpoint that runs a SQL query and outputs the results as JSON, it's just going to do it right. It's not going to mess that up. You have it add automated tests, you have it add documentation, you know it's going to be good. 
 But I'm not reviewing that code. And now I've got that feeling of guilt: if I haven't reviewed the code, is it really responsible for me to use this in production? 
 The thing that really helps me is thinking back to when I've worked at larger organizations where I've been an engineering manager. Other teams are building software that my team depends on. 
 If another team hands over something and says, "hey, this is the image resize service, here's how to use it to resize your images"... I'm not going to go and read every line of code that they wrote. 
 I'm going to look at their documentation and I'm going to use it to resize some images. And then I'm going to start shipping my own features. And if I start running into problems where the image resizer thing appears to have bugs or the performance isn't good, that's when I might dig into their Git repositories and see what's going on. But for the most part I treat that as a semi-black box that I don't look at until I need to. 
 I'm starting to treat the agents in the same way. And it still feels uncomfortable, because human beings are accountable for what they do. A team can build a reputation. I can say "I trust that team over there. They built good software in the past. They're not going to build something rubbish because that affects their professional reputations." 
 Claude Code does not have a professional reputation! It can't take accountability for what it's done. But it's been proving itself anyway - time and time again it's churning out straightforward things and doing them right in the style that I like. 
 There's an element of the normalization of deviance here - every time a model turns out to have written the right code without me monitoring it closely there's a risk that I'll trust it at the wrong moment in the future and get burned. 
 The new challenge of evaluating software 
 It used to be if you found a GitHub repository with a hundred commits and a good readme and automated tests and stuff, you could be pretty sure that the person writing that had put a lot of care and attention into that project. 
 And now I can knock out a git repository with a hundred commits and a beautiful readme and comprehensive tests of every line of code in half an hour! It looks identical to those projects that have had a great deal of care and attention. Maybe it is as good as them. I don't know. I can't tell from looking at it. Even for my own projects, I can't tell. 
 So I realized what I value more than the quality of the tests and documentation is that I want somebody to have used the thing. If you've got a vibe coded thing which you have used every day for the past two weeks, that's much more valuable to me than something that you've just spat out and hardly even exercised. 
 The bottlenecks have shifted 
 If you can go from producing 200 lines of code a day to 2,000 lines of code a day, what else breaks? The entire software development lifecycle was, it turns out, designed around the idea that it takes a day to produce a few hundred lines of code. And now it doesn't. 
 It's not just the downstream stuff, it's the upstream stuff as well. I saw a great talk by Jenny Wen , who's the design leader at Anthropic, where she said we have all of these design processes that are based around the idea that you need to get the design right - because if you hand it off to the engineers and they spend three months building the wrong thing, that's catastrophic. 
 There's this whole very extensive design process that you put in place because that design results in expensive work. But if it doesn't take three months to build, maybe the design process can be a whole lot riskier because cost, if you get something wrong, has been reduced so much. 
 Why I'm still not afraid for my career 
 When I look at my conversations with the agents, it's very clear to me that this is moon language for the vast majority of human beings. 
 There are a whole bunch of reasons I'm not scared that my career as a software engineer is over now that computers can write their own code, partly because these things are amplifiers of existing experience. If you know what you're doing, you can run so much faster with them. [...] 
 I'm constantly reminded as I work with these tools how hard the thing that we do is. Producing software is a ferociously difficult thing to do. And you could give me all of the AI tools in the world and what we're trying to achieve here is still really difficult. [...] 
 Matthew Yglesias, who's a political commentator, yesterday tweeted , "Five months in, I think I've decided that I don't want to vibecode — I want professionally managed software companies to use AI coding assistance to make more/better/cheaper software products that they sell to me for money." And that feels about right to me. I can plumb my house if I watch enough YouTube videos on plumbing. I would rather hire a plumber. 
 On the threat to SaaS providers of companies rolling their own solutions instead: 
 I just realized it's the thing I said earlier about how I only want to use your side project if you've used it for a few weeks. The enterprise version of that is I don't want a CRM unless at least two other giant enterprises have successfully used that CRM for six months. [...] You want solutions that are proven to work before you take a risk on them. 
 Tags: ai , generative-ai , llms , podcast-appearances , vibe-coding , coding-agents , agentic-engineering
```

---

## 10. datasette-referrer-policy 0.1

- 日期: 2026-05-05 23:44
- 链接: https://simonwillison.net/2026/May/5/datasette-referrer-policy/#atom-everything

```
Release: datasette-referrer-policy 0.1 
 The OpenStreetMap tiles on the Datasette global-power-plants demo weren't displaying correctly. This turned out to be caused by two bugs. 
 The first is that the CAPTCHA I added to that site a few weeks ago was triggering for the .json fetch requests used by the map plugin, and since those weren't HTML the user was not being asked to solve them. Here's the fix . 
 The second was that OpenStreetMap quite reasonably block tile requests from sites that use a Referrer-Policy: no-referrer header. 
 Datasette does this by default, and I didn't want to change that default on people without warning - so I had Codex + GPT-5.5 build me a new plugin to help set that header to another value. 
 Tags: openstreetmap , http , datasette
```

---

## 11. Our AI started a cafe in Stockholm

- 日期: 2026-05-05 22:14
- 链接: https://simonwillison.net/2026/May/5/our-ai-started-a-cafe-in-stockholm/#atom-everything

```
Our AI started a cafe in Stockholm 
 Andon Labs previously started an AI-run retail store in San Francisco. Now they're running a similar experiment in Stockholm, Sweden, only this time it's a cafe. 
 These experiments are interesting, and often throw out amusing anecdotes: 
 During the first week of inventory, Mona ordered 120 eggs even though the café has no stove. When the staff told her they couldn’t cook them, she suggested using the high-speed oven, until they pointed out the eggs would likely explode. She also tried to solve the problem of fresh tomatoes being spoiled too fast by ordering 22.5 kg of canned tomatoes for the fresh sandwiches. The baristas eventually started a “Hall of Shame”, a shelf visible to customers with all the weird things Mona ordered, including 6,000 napkins, 3,000 nitrile gloves, 9L coconut milk, and industrial-sized trash bags. 
 Where they lose their shine is when these AI managers start wasting the time of human beings who have not opted into the experiment: 
 She also successfully applied for an outdoor seating permit through the Police e-service, which didn’t require BankID. Her first submission included a sketch she had generated herself, despite having never seen the street outside the café. Unsurprisingly, the Police sent it back for revision. [...] 
 When she makes a mistake, she often sends multiple emails to suppliers with the subject “EMERGENCY” to cancel or change the order. 
 I don't think it's ethical to run experiments like this that affect real-world systems and steal time from people. 
 I'm reminded of the incident last year where the AI Village experiment infuriated Rob Pike by sending him unsolicited gratitude emails as an "act of kindness". That was just an unwanted email - asking suppliers to correct mistakes that were made without a human-in-the-loop or wasting police time with slop diagrams feels a whole lot worse to me. 
 I think experiments like this need to keep their own human operators in-the-loop for outbound actions that affect other people. Via Hacker News 
 Tags: ai , generative-ai , llms , ai-agents , ai-ethics
```

---

## 12. datasette-llm 0.1a7

- 日期: 2026-05-05 01:56
- 链接: https://simonwillison.net/2026/May/5/datasette-llm/#atom-everything

```
5th May 2026
- Mechanism for configuring default options for specific models.
Part of Datasette's evolving support mechanism for plugins that use LLMs. It's now possible to configure a model with default options, e.g. to say all enrichment operations should use a specific model with temperature set to 0.5.
Recent articles
- Notes on the xAI/Anthropic data center deal - 7th May 2026
- Live blog: Code w/ Claude 2026 - 6th May 2026
- Vibe coding and agentic engineering are getting closer than I'd like - 6th May 2026
```

---

## 13. llm-echo 0.5a0

- 日期: 2026-05-05 01:31
- 链接: https://simonwillison.net/2026/May/5/llm-echo/#atom-everything

```
5th May 2026
- New
-o thinking 1
option to help test against LLM 0.32a0 and higher.
This plugin provides a fake model called "echo" for LLM which doesn't run an LLM at all - it's useful for writing automated tests. You can now do this:
uvx --with llm==0.32a1 --with llm-echo==0.5a0 llm -m echo hi -o thinking 1
This will fake a reasoning block to standard error before returning JSON echoing the prompt.
Recent articles
- Notes on the xAI/Anthropic data center deal - 7th May 2026
- Live blog: Code w/ Claude 2026 - 6th May 2026
- Vibe coding and agentic engineering are getting closer than I'd like - 6th May 2026
```

---

## 14. Quoting John Gruber

- 日期: 2026-05-05 00:46
- 链接: https://simonwillison.net/2026/May/5/john-gruber/#atom-everything

```
5th May 2026
So it’s well known that Y Combinator owns some stake in OpenAI. But how big is that stake? This seems like devilishly difficult information to obtain. I asked around and a little birdie who knows several OpenAI investors came back with an answer: Y Combinator owns about 0.6 percent of OpenAI. At OpenAI’s current $852 billion valuation, that’s worth over $5 billion.
— John Gruber, Y Combinator’s Stake in OpenAI
Recent articles
- Notes on the xAI/Anthropic data center deal - 7th May 2026
- Live blog: Code w/ Claude 2026 - 6th May 2026
- Vibe coding and agentic engineering are getting closer than I'd like - 6th May 2026
```

---

## 15. Granite 4.1 3B SVG Pelican Gallery

- 日期: 2026-05-04 23:49
- 链接: https://simonwillison.net/2026/May/4/granite-41-3b-svg-pelican-gallery/#atom-everything

```
Granite 4.1 3B SVG Pelican Gallery 
 IBM released their Granite 4.1 family of LLMs a few days ago. They're Apache 2.0 licensed and come in 3B, 8B and 30B sizes. 
 Granite 4.1 LLMs: How They’re Built by Granite team member Yousaf Shah describes the training process in detail. 
 Unsloth released the unsloth/granite-4.1-3b-GGUF collection of GGUF encoded quantized variants of the 3B model - 21 different model files ranging in size from 1.2GB to 6.34GB. 
 All 21 of those Unsloth files add up to 51.3GB, which inspired me to finally try an experiment I've been wanting to run for ages: prompting "Generate an SVG of a pelican riding a bicycle" against different sized quantized variants of the same model to see what the results would look like. 
 Honestly, the results are less interesting than I expected. There's no distinguishable pattern relating quality to size - they're all pretty terrible! 
 I'll likely try this again in the future with a model that's better at drawing pelicans. Tags: ibm , ai , generative-ai , llms , pelican-riding-a-bicycle , llm-release
```

---

## 16. Quoting Andy Masley

- 日期: 2026-05-04 22:51
- 链接: https://simonwillison.net/2026/May/4/andy-masley/#atom-everything

```
[...] Between 2000 and 2024, farmers sold in total a Colorado-sized chunk of land all on their own, 77 times all land on data center property in 2028, and grew more food than ever on what was left. None of this caused any problems for US food access. 
 And then, in the middle of all this, a farmer in Loudoun County sells a few acres of mediocre hay field to a hyperscaler for ten times its agricultural value, and the response is that we’re running out of farmland. 
 — Andy Masley , pushing back against the "land use" argument against data center construction 
 Tags: ai-ethics , ai , generative-ai , andy-masley
```

---

## 17. April 2026 newsletter

- 日期: 2026-05-04 22:38
- 链接: https://simonwillison.net/2026/May/4/april-newsletter/#atom-everything

```
I just sent out the April edition of my sponsors-only monthly newsletter . If you are a sponsor (or if you start a sponsorship now) you can access it here . 
 In this month's newsletter: 
 Opus 4.7 and GPT-5.5, both with price increases 
 Claude Mythos and LLM security research 
 ChatGPT Images 2.0 
 More model releases 
 Other highlights from my blog 
 What I'm using, April 2026 edition 
 Here's a copy of the March newsletter as a preview of what you'll get. Pay $10/month to stay a month ahead of the free copy! 
 Tags: newsletter
```

---

## 18. TRE Python binding — ReDoS robustness demo

- 日期: 2026-05-04 17:52
- 链接: https://simonwillison.net/2026/May/4/tre-python-binding/#atom-everything

```
Research: TRE Python binding — ReDoS robustness demo 
 If it's good enough for antirez to add to Redis I figured Ville Laurikari's TRE regular expression engine was worth exploring in a little more detail. 
 I had Claude Code build an experimental Python binding (it used ctypes ) and try some malicious regular expression attacks against the library. TRE handles those much better than Python's standard library implementation, thanks mainly to the lack of support for backtracking. 
 Tags: security , python , regular-expressions , c , ctypes
```

---

## 19. Redis Array Playground

- 日期: 2026-05-04 15:53
- 链接: https://simonwillison.net/2026/May/4/redis-array/#atom-everything

```
Tool: Redis Array Playground 
 Salvatore Sanfilippo submitted a PR adding a new data type - arrays - to Redis. 
 The new commands are ARCOUNT , ARDEL , ARDELRANGE , ARGET , ARGETRANGE , ARGREP , ARINFO , ARINSERT , ARLASTITEMS , ARLEN , ARMGET , ARMSET , ARNEXT , AROP , ARRING , ARSCAN , ARSEEK , ARSET . 
 The implementation is currently available in a branch, so I had Claude Code for web build this interactive playground for trying out the new commands in a WASM-compiled build of a subset of Redis running in the browser. 
 The most interesting new command is ARGREP which can run a server-side grep against a range of values in the array using the newly vendored TRE regex library . 
 Salvatore wrote more about the AI-assisted development process for the array type in Redis array type: short story of a long development . 
 Tags: salvatore-sanfilippo , webassembly , generative-ai , agentic-engineering , ai , redis , llms , regular-expressions , c
```

---

## 20. Quoting Anthropic

- 日期: 2026-05-03 15:13
- 链接: https://simonwillison.net/2026/May/3/anthropic/#atom-everything

```
We used an automatic classifier which judged sycophancy by looking at whether Claude showed a willingness to push back, maintain positions when challenged, give praise proportional to the merit of ideas, and speak frankly regardless of what a person wants to hear. Most of the time in these situations, Claude expressed no sycophancy—only 9% of conversations included sycophantic behavior (Figure 2). But two domains were exceptions: we saw sycophantic behavior in 38% of conversations focused on spirituality, and 25% of conversations on relationships. 
 — Anthropic , How people ask Claude for personal guidance 
 Tags: ai-ethics , anthropic , claude , ai-personality , generative-ai , ai , llms , sycophancy
```

---

## 21. Sightings

- 日期: 2026-05-02 17:26
- 链接: https://simonwillison.net/2026/May/2/sightings/#atom-everything

```
/elsewhere/sightings/ 
 I have a new camera (a Canon R6 Mark II) so I'm taking a lot more photos of birds. I share my best wildlife photos on iNaturalist , and based on yesterday's successful prototype I decided to add those to my blog. 
 I built this feature on my phone using Claude Code for web, as an extension of my beats system for syndicating external content. Here's the PR and prompt. 
 As with my other forms of incoming syndicated content sightings show up on the homepage, the date archive pages, and in site search results. 
 I back-populated over a decade of iNaturalist sightings, which means you that if you search for lemur you'll see my lemur photos from Madagascar in 2019! Tags: blogging , photography , wildlife , ai , inaturalist , generative-ai , llms , ai-assisted-programming , claude-code
```

---

## 22. iNaturalist Sightings

- 日期: 2026-05-01 19:35
- 链接: https://simonwillison.net/2026/May/1/inat-sightings/#atom-everything

```
Tool: iNaturalist Sightings 
 I wanted to see my iNaturalist observations - across two separate accounts - grouped by when they occurred. I'm camping this weekend so I built this entirely on my phone using Claude Code for web. 
 I started by building an inaturalist-clumper Python CLI for fetching and "clumping" observations - by default clumps use observations within 2 hours and 5km of each other. 
 Then I setup simonw/inaturalist-clumps as a Git scraping repository to run that tool and record the result to clumps.json . 
 That JSON file is hosted on GitHub, which means it can be fetched by JavaScript using CORS. 
 Finally I ran this prompt against my simonw/tools repo: 
 Build inat-sightings.html - an app that does a fetch() against https://raw.githubusercontent.com/simonw/inaturalist-clumps/refs/heads/main/clumps.json and then displays all of the observations on one page using the https://static.inaturalist.org/photos/538073008/small.jpg small.jpg URLs for the thumbnails - with loading=lazy - but when a thumbnail is clicked showing the large.jpg in an HTML modal. Both small and large should include the common species names if available 
 Tags: tools , claude-code , inaturalist , generative-ai , ai , llms
```

---

## 23. Codex CLI 0.128.0 adds /goal

- 日期: 2026-04-30 23:23
- 链接: https://simonwillison.net/2026/Apr/30/codex-goals/#atom-everything

```
Codex CLI 0.128.0 adds /goal 
 The latest version of OpenAI's Codex CLI coding agent adds their own version of the Ralph loop : you can now set a /goal and Codex will keep on looping until it evaluates that the goal has been completed... or the configured token budget has been exhausted. 
 It looks like the feature is mainly implemented though the goals/continuation.md and goals/budget_limit.md prompts, which are automatically injected at the end of a turn. Via @fcoury 
 Tags: ai , openai , prompt-engineering , generative-ai , llms , coding-agents , system-prompts , codex-cli , agentic-engineering
```

---

## 24. Our evaluation of OpenAI's GPT-5.5 cyber capabilities

- 日期: 2026-04-30 23:03
- 链接: https://simonwillison.net/2026/Apr/30/gpt-55-cyber-capabilities/#atom-everything

```
30th April 2026 - Link Blog
Our evaluation of OpenAI's GPT-5.5 cyber capabilities. The UK's AI Security Institute previously evaluated Claude Mythos: now they've evaluated GPT-5.5 for finding security vulnerability and found it to be comparable to Mythos, but unlike Mythos it's generally available right now.
Recent articles
- Notes on the xAI/Anthropic data center deal - 7th May 2026
- Live blog: Code w/ Claude 2026 - 6th May 2026
- Vibe coding and agentic engineering are getting closer than I'd like - 6th May 2026
```

---

## 25. Quoting Andrew Kelley

- 日期: 2026-04-30 21:24
- 链接: https://simonwillison.net/2026/Apr/30/andrew-kelley/#atom-everything

```
It's a common misconception that we can't tell who is using LLM and who is not. I'm sure we didn't catch 100% of LLM-assisted PRs over the past few months, but the kind of mistakes humans make are fundamentally different than LLM hallucinations, making them easy to spot. Furthermore, people who come from the world of agentic coding have a certain digital smell that is not obvious to them but is obvious to those who abstain. It's like when a smoker walks into the room, everybody who doesn't smoke instantly knows it. 
 I'm not telling you not to smoke, but I am telling you not to smoke in my house. 
 — Andrew Kelley , Creator of Zig 
 Tags: zig , llms , ai , generative-ai
```

---

## 26. We need RSS for sharing abundant vibe-coded apps

- 日期: 2026-04-30 18:38
- 链接: https://simonwillison.net/2026/Apr/30/rss-vibe-coded-apps/#atom-everything

```
We need RSS for sharing abundant vibe-coded apps 
 Matt Webb: 
 I would love an RSS web feed for all those various tools and apps pages, each item with an “Install” button. (But install to where?) 
 The lesson here is that when vibe-coding accelerates app development, apps become more personal, more situated, and more frequent. Shipping a tool or a micro-app is less like launching a website and more like posting on a blog. 
 This inspired me to have Claude add an Atom feed (and icon) to my /elsewhere/tools/ page, which itself is populated by content from my tools.simonwillison.net site. Tags: atom , matt-webb , rss , ai , vibe-coding
```

---

## 27. The Zig project's rationale for their firm anti-AI contribution policy

- 日期: 2026-04-30 01:24
- 链接: https://simonwillison.net/2026/Apr/30/zig-anti-ai/#atom-everything

```
Zig has one of the most stringent anti-LLM policies of any major open source project: 
 No LLMs for issues. 
 No LLMs for pull requests. 
 No LLMs for comments on the bug tracker, including translation. English is encouraged, but not required. You are welcome to post in your native language and rely on others to have their own translation tools of choice to interpret your words. 
 The most prominent project written in Zig may be the Bun JavaScript runtime, which was acquired by Anthropic in December 2025 and, unsurprisingly, makes heavy use of AI assistance. 
 Bun operates its own fork of Zig, and recently achieved a 4x performance improvement on Bun compile after adding "parallel semantic analysis and multiple codegen units to the llvm backend". Here's that code . But @bunjavascript says : 
 We do not currently plan to upstream this, as Zig has a strict ban on LLM-authored contributions. 
 (Update: here's a Zig core contributor providing details on why they wouldn't accept that particular patch independent of the LLM issue - parallel semantic analysis is a long planned feature but has implications "for the Zig language itself".) 
 In Contributor Poker and Zig's AI Ban ( via Lobste.rs ) Zig Software Foundation VP of Community Loris Cro explains the rationale for this strict ban. It's the best articulation I've seen yet for a blanket ban on LLM-assisted contributions: 
 In successful open source projects you eventually reach a point where you start getting more PRs than what you’re capable of processing. Given what I mentioned so far, it would make sense to stop accepting imperfect PRs in order to maximize ROI from your work, but that’s not what we do in the Zig project. Instead, we try our best to help new contributors to get their work in, even if they need some help getting there . We don’t do this just because it’s the “right” thing to do, but also because it’s the smart thing to do . 
 Zig values contributors over their contributions. Each contributor represents an investment by the Zig core team - the primary goal of reviewing and accepting PRs isn't to land new code, it's to help grow new contributors who can become trusted and prolific over time. 
 LLM assistance breaks that completely. It doesn't matter if the LLM helps you submit a perfect PR to Zig - the time the Zig team spends reviewing your work does nothing to help them add new, confident, trustworthy contributors to their overall project. 
 Loris explains the name here: 
 The reason I call it “contributor poker” is because, just like people say about the actual card game, “you play the person, not the cards”. In contributor poker, you bet on the contributor, not on the contents of their first PR. 
 This makes a lot of sense to me. It relates to an idea I've seen circulating elsewhere: if a PR was mostly written by an LLM, why should a project maintainer spend time reviewing and discussing that PR as opposed to firing up their own LLM to solve the same problem? 
 Tags: anthropic , zig , ai , llms , ai-ethics , open-source , javascript , ai-assisted-programming , generative-ai , bun
```

---

## 28. llm 0.32a1

- 日期: 2026-04-29 23:52
- 链接: https://simonwillison.net/2026/Apr/29/llm-3/#atom-everything

```
29th April 2026
- Fixed a bug in 0.32a0 where tool-calling conversations were not correctly reinflated from SQLite. #1426
Recent articles
- Notes on the xAI/Anthropic data center deal - 7th May 2026
- Live blog: Code w/ Claude 2026 - 6th May 2026
- Vibe coding and agentic engineering are getting closer than I'd like - 6th May 2026
```

---

## 29. LLM 0.32a0  is a major backwards-compatible refactor

- 日期: 2026-04-29 19:01
- 链接: https://simonwillison.net/2026/Apr/29/llm/#atom-everything

```
I just released LLM 0.32a0 , an alpha release of my LLM Python library and CLI tool for accessing LLMs, with some consequential changes that I've been working towards for quite a while. 
 Previous versions of LLM modeled the world in terms of prompts and responses. Send the model a text prompt, get back a text response. 
 import llm model = llm . get_model ( "gpt-5.5" ) response = model . prompt ( "Capital of France?" ) print ( response . text ()) This made sense when I started working on the library back in April 2023. A lot has changed since then! 
 LLM provides an abstraction over thousands of different models via its plugin system . The original abstraction - of text input that returns text output - was no longer able to represent everything I needed it to. 
 Over time LLM itself has grown attachments to handle image, audio, and video input, then schemas for outputting structured JSON, then tools for executing tool calls. Meanwhile LLMs kept evolving, adding reasoning support and the ability to return images and all kinds of other interesting capabilities. 
 LLM needs to evolve to better handle the diversity of input and output types that can be processed by today's frontier models. 
 The 0.32a0 alpha has two key changes: model inputs can be represented as a sequence of messages, and model responses can be composed of a stream of differently typed parts. 
 Prompts as a sequence of messages 
 LLMs accept input as text, but ever since ChatGPT demonstrated the value of a two-way conversational interface, the most common way to prompt them has been to treat that input as a sequence of conversational turns. 
 The first turn might look like this: 
 user: Capital of France?
assistant: (The model then gets to fill out the reply from the assistant.) 
 But each subsequent turn needs to replay the entire conversation up to that point, as a sort of screenplay: 
 user: Capital of France?
assistant: Paris
user: Germany?
assistant: Most of the JSON APIs from the major vendors follow this pattern. Here's what the above looks like using the OpenAI chat completions API, which has been widely imitated by other providers: 
 curl https://api.openai.com/v1/chat/completions \
 -H " Authorization: Bearer $OPENAI_API_KEY " \
 -H " Content-Type: application/json " \
 -d ' { "model": "gpt-5.5", "messages": [ { "role": "user", "content": "Capital of France?" }, { "role": "assistant", "content": "Paris" }, { "role": "user", "content": "Germany?" } ] } ' 
 Prior to 0.32, LLM modeled these as conversations: 
 model = llm . get_model ( "gpt-5.5" ) conversation = model . conversation () r1 = conversation . prompt ( "Capital of France?" ) print ( r1 . text ()) # Outputs "Paris" r2 = conversation . prompt ( "Germany?" ) print ( r2 . text ()) # Outputs "Berlin" This worked if you were building a conversation with the model from scratch, but it didn't provide a way to feed in a previous conversation from the start. This made tasks like building an emulation of the OpenAI chat completions API much harder than they should have been. 
 The llm CLI tool worked around this through a custom mechanism for persisting and inflating conversations using SQLite, but that never became a stable part of the LLM API - and there are many places you might want to use the Python library without committing to SQLite as the storage layer. 
 The new alpha now supports this: 
 import llm from llm import user , assistant model = llm . get_model ( "gpt-5.5" ) response = model . prompt ( messages = [ user ( "Capital of France?" ), assistant ( "Paris" ), user ( "Germany?" ),
]) print ( response . text ()) The llm.user() and llm.assistant() functions are new builder functions designed to be used within that messages=[] array. 
 The previous prompt= option still works, but LLM upgrades it to a single-item messages array behind the scenes. 
 You can also now reply to a response, as an alternative to building a conversation: 
 response2 = response . reply ( "How about Hungary?" ) print ( response2 ) # Default __str__() calls .text() Streaming parts 
 The other major new interface in the alpha concerns streaming results back from a prompt. 
 Previously, LLM supported streaming like this: 
 response = model . prompt ( "Generate an SVG of a pelican riding a bicycle" ) for chunk in response : print ( chunk , end = "" ) Or this async variant: 
 import asyncio import llm model = llm . get_async_model ( "gpt-5.5" ) response = model . prompt ( "Generate an SVG of a pelican riding a bicycle" ) async def run (): async for chunk in response : print ( chunk , end = "" , flush = True ) asyncio . run ( run ()) Many of today's models return mixed types of content. A prompt run against Claude might return reasoning output, then text, then a JSON request for a tool call, then more text content. 
 Some models can even execute tools on the server-side, for example OpenAI's code interpreter tool or Anthropic's web search . This means the results from the model can combine text, tool calls, tool outputs and other formats. 
 Multi-modal output models are starting to emerge too, which can return images or even snippets of audio intermixed into that streaming response. 
 The new LLM alpha models these as a stream of typed message parts. Here's what that looks like as a Python API consumer: 
 import asyncio import llm model = llm . get_model ( "gpt-5.5" ) prompt = "invent 3 cool dogs, first talk about your motivations" def describe_dog ( name : str , bio : str ) -> str : """Record the name and biography of a hypothetical dog.""" return f" { name } : { bio } " def sync_example (): response = model . prompt ( prompt , tools = [ describe_dog ],
 ) for event in response . stream_events (): if event . type == "text" : print ( event . chunk , end = "" , flush = True ) elif event . type == "tool_call_name" : print ( f" \n Tool call: { event . chunk } (" , end = "" , flush = True ) elif event . type == "tool_call_args" : print ( event . chunk , end = "" , flush = True ) async def async_example (): model = llm . get_async_model ( "gpt-5.5" ) response = model . prompt ( prompt , tools = [ describe_dog ],
 ) async for event in response . astream_events (): if event . type == "text" : print ( event . chunk , end = "" , flush = True ) elif event . type == "tool_call_name" : print ( f" \n Tool call: { event . chunk } (" , end = "" , flush = True ) elif event . type == "tool_call_args" : print ( event . chunk , end = "" , flush = True ) sync_example () asyncio . run ( async_example ()) Sample output (from just the first sync example): 
 My motivation: create three memorable dogs with distinct “cool” styles—one cinematic, one adventurous, and one charmingly chaotic—so each feels like they could star in their own story. 
 Tool call: describe_dog({"name": "Nova Jetpaw", "bio": "A sleek silver-gray whippet who wears tiny aviator goggles and loves sprinting along moonlit beaches. Nova is fearless, elegant, and rumored to outrun drones just for fun."} 
 Tool call: describe_dog({"name": "Mochi Thunderbark", "bio": "A fluffy corgi with a dramatic black-and-gold bandana and the confidence of a rock star. Mochi is short, loud, loyal, and leads a neighborhood 'security patrol' made entirely of squirrels."} 
 Tool call: describe_dog({"name": "Atlas Snowfang", "bio": "A massive white husky with ice-blue eyes and a backpack full of trail snacks. Atlas is calm, heroic, and always knows the way home—even during blizzards, fog, or confusing camping trips."} 
 At the end of the response you can call response.execute_tool_calls() to actually run the functions that were requested, or send a response.reply() to have those tools called and their return values sent back to the model: 
 print ( response . reply ( "Tell me about the dogs" )) This new mechanism for streaming different token types means the CLI tool can now display "thinking" text in a different color from the text in the final response. The thinking text goes to stderr so it won't affect results that are piped into other tools. 
 This example uses Claude Sonnet 4.6 (with an updated streaming event version of the llm-anthropic plugin) as Anthropic's models return their reasoning text as part of the response: 
 llm -m claude-sonnet-4.6 ' Think about 3 cool dogs then describe them ' \
 -o thinking_display 1 
 You can suppress the output of reasoning tokens using the new -R/--no-reasoning flag. Surprisingly that ended up being the only CLI-facing change in this release. 
 A mechanism for serializing and deserializing responses 
 As mentioned earlier, LLM has quite inflexible code at the moment for persisting conversations to SQLite. I've added a new mechanism in 0.32a0 that should provide Python API users a way to roll their own alternative: 
 serializable = response . to_dict () # serializable is a JSON-style dictionary # store it anywhere you like, then inflate it: response = Response . from_dict ( serializable ) The dictionary this returns is actually a TypedDict defined in the new llm/serialization.py module. 
 What's next? 
 I'm releasing this as an alpha so I can upgrade various plugins and exercise the new design in real world environments for a few days. I expect the stable 0.32 release will be very similar to this alpha, unless alpha testing reveals some design flaw in the way I've put this all together. 
 There's one remaining large task: I'd like to redesign the SQLite logging system to better capture the more finely grained details that are returned by this new abstraction. 
 Ideally I'd like to model this as a graph, to best support situations like an OpenAI-style chat completions API where the same conversations are constantly extended and then repeated with every prompt. I want to be able to store those without duplicating them in the database. 
 I'm undecided as to whether that should be a feature in 0.32 or I should hold it for 0.33. 
 Tags: projects , python , ai , annotated-release-notes , generative-ai , llms , llm
```

---

## 30. llm 0.32a0

- 日期: 2026-04-29 18:57
- 链接: https://simonwillison.net/2026/Apr/29/llm-2/#atom-everything

```
29th April 2026
See the annotated release notes.
This is a beat by Simon Willison, posted on 29th April 2026.
Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments.
Pay me to send you less!
```

---
