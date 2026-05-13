# Hacker News 首页

> 分类: 技术社区
> URL: https://hnrss.org/frontpage
> 抓取: 20 篇

---

## 1. Zed Editor Theme-Builder

- 日期: 2026-05-09 17:30
- 链接: https://zed.dev/theme-builder

```
Theme Builder is Desktop-only
To fully utilize Zed's theme builder, access it from the desktop. In the meantime, browse available theme extensions.
View Theme ExtensionsBackground
Surface Background
Elevated Surface Background
Linked to
Panel Background
Linked to
Panel Focused Border
Linked to
Panel Indent Guide
Panel Indent Guide Hover
Panel Indent Guide Active
Panel Overlay Background
Linked to
Panel Overlay Hover
Linked to
Pane Focused Border
Linked to
/
scheduler.tsx
catware.rs
Uncommitted Changes
panic
src/components/scheduler.tsx
1"use client"23import * as React from "react"4import { format, addMinutes, isAfter } from "date-fns"56// Types for our "essential" meeting system7interface Meeting {8 id: string9 title: string10 : boolean'couldHaveBeenAnEmail' is declared but its value is never read.11 attendees: string[]12 snacksProvided: boolean13 : numberType 'string' is not assignable to type 'number'.14}1516type MeetingStatus = "scheduled" | "running-late" | "cancelled" | "eternal"1718function validateMeeting(: string[]): boolean {Consider using 'attendees' instead of 'atendees' for clarity.19 return atendees.length > 0 && atendees.length < 5020}2122let = "Discuss why we need more meetings"'agendaItem' can be declared as 'const' since it is never reassigned.2324const MEETING_EXCUSES = [25 "Sorry, I was on mute",26 "Can everyone see my screen?",27 "Let's take this offline",28 "Per my last email...",29 "I have a hard stop in 5 minutes",30] as const3132/** Props for the world's most essential component */33interface MeetingSchedulerProps {34 defaultDuration?: number35 maxAttendees?: number36 requiresSnacks?: boolean37 onMeetingCreate?: (meeting: Meeting) => void38 onEscapeAttempt?: () => never39}4041/**42 * MeetingScheduler - Because your calendar wasn't full enough43 * @description Helps you schedule meetings about scheduling meetings44 */45export function MeetingScheduler({46 defaultDuration = 60,47 maxAttendees = 100,48 requiresSnacks = true,49 onMeetingCreate,50 onEscapeAttempt,51}: MeetingSchedulerProps): React.ReactElement {52 const [meetings, setMeetings] = React.useState<Meeting[]>([])53 const [excuseIndex, setExcuseIndex] = React.useState(0)54 const [isLoading, setIsLoading] = React.useState<boolean>(false)5556 const formRef = React.useRef<HTMLFormElement>(null)57 const sanityRef = React.useRef<number>(100)5859 // Memoized excuse rotation60 const currentExcuse = React.useMemo(() => {61 return MEETING_EXCUSES[excuseIndex % MEETING_EXCUSES.length]62 }, [excuseIndex])6364 // Effect: Gradually decrease sanity65 React.useEffect(() => {66 const interval = setInterval(() => {67 sanityRef.current = Math.max(0, sanityRef.current - 1)68 if (sanityRef.current === 0) {69 console.warn("Developer sanity depleted")70 }71 }, 60000)7273 return () => clearInterval(interval)74 }, [])7576 // Callback for creating meetings77 const handleCreateMeeting = React.useCallback(78 async (title: string, attendees: string[]) => {79 if (!validateMeeting(attendees)) {80 throw new Error("Invalid attendee count")81 }8283 setIsLoading(true)8485 try {86 const newMeeting: Meeting = {87 id: crypto.randomUUID(),88 title: title || "Meeting about meetings",89 couldHaveBeenAnEmail: true,90 attendees,91 snacksProvided: requiresSnacks,92 actuallyStartsOnTime: "never", // This causes the error93 }9495 setMeetings((prev) => [...prev, newMeeting])96 onMeetingCreate?.(newMeeting)97 setExcuseIndex((i) => i + 1)98 } catch (error) {99 console.error("Failed to create meeting:", error)100 } finally {101 setIsLoading(false)102 }103 },104 [requiresSnacks, onMeetingCreate]105 )106107 // Render the meeting madness108 return (109 <div className="meeting-scheduler p-6 bg-white rounded-lg shadow-xl">110 <header className="mb-4 border-b pb-2">111 <h1 className="text-2xl font-bold text-gray-900">112 📅 Meeting Scheduler Pro™113 </h1>114 <p className="text-sm text-gray-500 italic">115 "{currentExcuse}"116 </p>117 </header>118119 <form120 ref={formRef}121 onSubmit={(e) => {122 e.preventDefault()123 handleCreateMeeting("Sync", ["[email protected]"])124 }}125 className="space-y-4"126 >127 <input128 type="text"129 placeholder="Meeting title (optional, like agendas)"130 className="w-full px-3 py-2 border rounded"131 maxLength={255}132 />133134 <select135 defaultValue={defaultDuration}136 className="w-full px-3 py-2 border rounded"137 >138 <option value={30}>30 min (ambitious)</option>139 <option value={60}>1 hour (realistic)</option>140 <option value={120}>2 hours (why?)</option>141 <option value={480}>All day (send help)</option>142 </select>143144 <button145 type="submit"146 disabled={isLoading}147 className="w-full py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50"148 >149 {isLoading ? "Syncing calendars..." : "Schedule Meeting"}150 </button>151 </form>152153 {meetings.length > 0 && (154 <ul className="mt-6 divide-y">155 {meetings.map((meeting) => (156 <li key={meeting.id} className="py-3">157 <span className="font-medium">{meeting.title}</span>158 <span className="text-gray-400 ml-2">159 ({meeting.attendees.length} victims)160 </span>161 </li>162 ))}163 </ul>164 )}165 </div>166 )167}168169export default MeetingScheduler
zed.dev — zsh
███████╗███████╗██████╗
╚══███╔╝██╔════╝██╔══██╗
███╔╝ █████╗ ██║ ██║
███╔╝ ██╔══╝ ██║ ██║
███████╗███████╗██████╔╝
╚══════╝╚══════╝╚═════╝
Editor: Zed
Version: 1.1.7
Platform: macOS
9 Changes
Tracked
src
services
coffee.ts
utils
monday.ts
sleep.ts
Untracked
src/utils
excuses.ts
meeting-survival.ts
Fixed the thing that broke the thing
Theme Builder
Setting up the workbench…
```

---

## 2. CPanel's Black Week: 3 New Vulnerabilities Patched After Attack on 44k Servers

- 日期: 2026-05-09 17:06
- 链接: https://www.copahost.com/blog/cpanels-black-week-three-new-vulnerabilities-patched-after-ransomware-attack-on-44000-servers/

```
If you run a server with cPanel or WHM, you need to read this carefully.
On May 8, 2026 — just ten days after the cPanel CVE-2026-41940 authentication bypass was used to compromise 44,000 web hosting servers and deploy ransomware — cPanel quietly released a second emergency security patch. This one covers three new vulnerabilities: CVE-2026-29201, CVE-2026-29202, and CVE-2026-29203.
Two of the three carry a CVSS score of 8.8. That puts them firmly in the High severity tier, one step below Critical.
This is the second Technical Security Release (TSR) in 10 days from cPanel. Two emergency patches in less than two weeks is not normal, and the timing — immediately following the worst cPanel attack in years — tells a clear story: the ransomware incident triggered a deeper code audit, and that audit found more problems.
Table of Contents
What Is a cPanel TSR?
Before diving into the vulnerabilities, a quick note for context: cPanel uses a standardized process called a Technical Security Release (TSR) when a security patch is ready. cPanel notifies registered customers in advance so they can prepare update windows and maintenance schedules. CVE numbers are reserved through MITRE, but full technical details are embargoed until the moment the patch goes live — to prevent exploitation before a fix is available.
On May 7, 2026, WebPros sent a second TSR pre-disclosure email to registered customers — the second such emergency notice in ten days. The patches were released on May 8 at 12:00 EST.
The Three New Vulnerabilities
CVE-2026-29201 — Arbitrary File Read (CVSS 4.3)
What it is: An insufficient input validation of the feature file name in the feature::LOADFEATUREFILE
adminbin call that could result in an arbitrary file read.
What it means in practice: An authenticated attacker can manipulate the feature file name parameter to read files on the hosting server they should not have access to. While this does not directly grant root access, the information gathered — configuration files, credentials, internal paths — can be used to stage more damaging follow-up attacks.
Severity: Moderate (CVSS 4.3). Lower urgency than the others, but still worth patching immediately given the current threat environment.
CVE-2026-29202 — Arbitrary Perl Code Execution (CVSS 8.8)
What it is: An insufficient input validation of the plugin
parameter in the create_user
API call that could result in arbitrary Perl code execution on behalf of the already authenticated account’s system user.
What it means in practice: This is the most dangerous of the three. An authenticated user — which could be any account holder on a shared server — can inject arbitrary Perl code through the create_user
API. Perl code running in the context of cPanel has significant system-level access. On a shared hosting server, this could allow one tenant to run code that affects the entire machine.
Severity: High (CVSS 8.8). Requires authentication, but on shared hosting, that bar is low — any account is enough.
CVE-2026-29203 — Privilege Escalation via Unsafe Symlink (CVSS 8.8)
What it is: An unsafe symlink handling vulnerability that allows a user to modify access permissions of an arbitrary file using chmod, resulting in denial-of-service or possible privilege escalation.
What it means in practice: By creating a symlink that points to a sensitive system file and triggering a chmod operation through cPanel, an attacker can change permissions on files they should not be able to touch. This can lead to privilege escalation or denial of service if system files are rendered inaccessible.
Severity: High (CVSS 8.8). In combination with CVE-2026-29202, these two flaws could be chained: execute code to create the symlink, then use the chmod escalation to gain deeper access.
Context: What Just Happened to cPanel
To understand why these three patches matter more than their individual CVSS scores suggest, it is necessary to look at what happened in the ten days before them.
On April 28, 2026, cPanel released an emergency patch for CVE-2026-41940 — a CVSS 9.8 authentication bypass that allowed unauthenticated remote attackers to gain administrative access to cPanel and WHM. The flaw was actively exploited as a zero-day with exploitation attempts dating back to late February 2026 — meaning attackers had a roughly two-month head start before a fix was available.
The consequences were immediate and severe. At least 44,000 IP addresses running cPanel were compromised in ongoing attacks. Hackers exploited the flaw to breach servers and deploy a Go-based Linux encryptor for a ransomware strain called “Sorry.”
Two emergency Technical Support Releases in a 10-day window reflects what security teams recognize as a concentrated remediation cycle: an initial critical patch triggers a deeper audit of adjacent code paths, and that audit surfaces additional issues that were previously undiscovered or deprioritized. This is not unusual following a high-profile incident — it is actually the expected outcome of an accelerated re-examination of authentication and session handling code.
In other words: finding CVE-2026-29201, 29202, and 29203 right after CVE-2026-41940 is not bad luck. It is the result of cPanel auditing their code under pressure — and finding more problems. There may be further disclosures to come.
How to Patch — Step by Step
Standard update:
/scripts/upcp
Run this from the command line as root after 12:00 EST on May 8. This pulls the latest TSR through cPanel’s standard tier mechanism.
If automatic updates are disabled or you are on a pinned tier:
/scripts/upcp --force
For CloudLinux 6 servers:
sed -i "s/CPANEL=.*/CPANEL=cl6110/g" /etc/cpupdate.conf
/scripts/upcp
After patching, restart cpsrvd:
/scripts/restartsrv_cpsrvd
Verify the patched version is running:
/usr/local/cpanel/cpanel -V
Confirm the version matches the patched release listed in cPanel’s official security advisory before considering the server protected.
Should You Also Check for the Previous Compromise?
If your server was running an unpatched version of cPanel during the period between late February and April 28, you should treat it as potentially compromised and investigate, not just patch.
The recommended forensic steps include: auditing access logs retroactively from February 23, 2026 — reviewing /usr/local/cpanel/logs/access_log
and /usr/local/cpanel/logs/login_log
for anomalous session authentication patterns originating from unexpected IP addresses. Also run a recursive scan of user home directories for files with the .sorry
extension. Presence of .sorry
files confirms ransomware deployment and requires full incident response, not just patching.
The Broader Pattern
What is happening to cPanel right now is part of a wider trend affecting the entire web hosting security landscape.
Three of the highest-profile Linux kernel vulnerabilities in years — Copy Fail (CVE-2026-31431) and Dirty Frag (CVE-2026-43284/43500) — were disclosed within eight days of each other in late April and early May. The cPanel ransomware attack exposed over 44,000 servers. And now three more cPanel CVEs land within days of the first emergency patch.
This concentration of disclosures is not coincidental. AI-assisted security research is finding vulnerabilities faster than coordinated disclosure processes can handle them. The window between a vulnerability becoming known to attackers and being exploited in production is shrinking from weeks to days. In the case of CVE-2026-41940, exploitation started months before a patch existed.
For anyone operating cPanel servers, the operational implication is direct: automated updates must be on, patch verification must be part of your maintenance checklist, and log review after every major incident is no longer optional.
Summary Checklist
Sources
- The Hacker News — cPanel, WHM Release Fixes for Three New Vulnerabilities: https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html
- Panelica — cPanel Pre-Discloses Three New CVEs, Second Emergency TSR in 10 Days: https://panelica.com/blog/cpanel-cve-2026-29201-29202-29203-may-2026-tsr-advisory
- Panelica — cPanel’s 30-Day Security Storm: https://panelica.com/blog/cpanel-30-day-security-storm-2026
- BleepingComputer — Critical cPanel flaw mass-exploited in “Sorry” ransomware attacks: https://www.bleepingcomputer.com/news/security/critrical-cpanel-flaw-mass-exploited-in-sorry-ransomware-attacks/
- BleepingComputer — cPanel, WHM emergency update fixes critical auth bypass bug: https://www.bleepingcomputer.com/news/security/cpanel-whm-emergency-update-fixes-critical-auth-bypass-bug/
- Help Net Security — cPanel zero-day exploited for months before patch release: https://www.helpnetsecurity.com/2026/04/30/cpanel-zero-day-vulnerability-cve-2026-41940-exploited/
- KnownHost Community Forum — CVE-2026-29201, 29202, 29203 patch thread: https://www.knownhost.com/forums/threads/cpanel-cve-2026-29201-cve-2026-29202-and-cve-2026-29203-patch-released-5-8-26-noon-est.6603/
```

---

## 3. I Will Not Add Query Strings to Your URLs

- 日期: 2026-05-09 16:28
- 链接: https://susam.net/no-query-strings.html

```
I Will Not Add Query Strings to Your URLs
Last evening, a short blog post appeared in my feed reader that felt as if it spoke directly to me. It is Chris Morgan's excellent post I've banned query strings.
Contents
Wisdom on the Web
Chris is someone whose Internet comments I have been reading for about half a decade now. I first stumbled upon his comments when he left very detailed feedback on one of my collections of CSS rules on Hacker News. I am by no means a web developer. I have spent most of my professional life doing systems programming in C and C++. However, developing websites and writing small HTML tools has been a long-time hobby for me. I have learnt most of my web development skills as a hobbyist by studying what other people do: first by viewing the source of websites I liked in the early 2000s, and later by occasionally getting possessed by the urge to implement a new game or tool and searching MDN Web Docs to learn whatever I needed to make it work. One problem with learning a skill this way is that you sometimes pick up habits and practices that are fashionable but not necessarily optimal or correct. So it was really valuable to me when Chris commented on my collection of boilerplate CSS rules. It helped me improve my CSS a lot. In fact, a few of the lessons from his comment have really stuck with me; I keep them in mind whenever I make a hobby HTML project: always retain underlines in links and retain purple for visited links.
I have been following Chris's posts and comments on web-related topics since then. He often posts great feedback on web-related projects. Whenever I come across one, I make sure to read them carefully, even when the project isn't mine. I always end up learning something nice and useful from his comments. Here is one such recent example from the Lobsters story Adding author context to RSS.
Wander on the Web
A couple of months ago, I created a new project called Wander Console. It is a small, decentralised, self-hosted web console that lets visitors to your website explore interesting websites and pages recommended by a community of independent personal website owners. For example, my console is here: susam.net/wander/. If you click the 'Wander' button there, the tool loads a random personal web page recommended by the Wander community.
The tool consists of one HTML file that implements the console and one JavaScript file where the website owner defines a list of neighbouring consoles along with a list of web pages they recommend. If you copy these two files to your web server, you instantly have a Wander console live on the Web. You don't need any server-side logic or server-side software beyond a basic web server to run Wander Console. You can even host it in constrained environments like Codeberg Pages or GitHub Pages. When you click the 'Wander' button, the console connects to other remote consoles, fetches web page recommendations, picks one randomly and loads it in your web browser. It is a bit like the now defunct StumbleUpon but it is completely decentralised. It is also a bit like web rings except that the community network is not restricted to being a cycle; it is a graph and it is flexible.
There are currently over 50 websites hosting this tool. Together, they recommend over 1500 web pages. You can find a recent snapshot of the list of known consoles and the pages they recommend at susam.codeberg.page/wcn/. To learn more about this tool or to set it up on your website, please see codeberg.org/susam/wander.
Misfeature
In case you were wondering why I suddenly plugged my project into this post in the previous section, it is because I recently added a dubious feature to that project that I myself was not entirely convinced about. That misfeature is relevant to this post.
In version 0.4.0 of Wander Console, I added support for
a via=
query parameter while loading web pages. For
example, if you encountered midnight.pub
while using the console at susam.net/wander/,
the console loaded the page using the following URL:
https://midnight.pub/?via=https://susam.net/wander/
This allowed the owner of the recommended website to see, via their access logs, that the visit originated from a Wander Console. Chris's recent blog post is critical of features like this. He writes:
I don't like people adding tracking stuff to URLs. Still less do I like people adding tracking stuff to my URLs.
https://chrismorgan.info/no-query-strings?ref=example.com
? Did I ask? If I wanted to know I'd look at theReferer
header; and if it isn't there, it's probably for a good reason. You abuse your users by adding that to the link.
I mentioned earlier that I was not entirely convinced that adding a referral query string was a good thing to do. Why did I add it anyway? I succumbed to popular demand. Let me briefly describe my frame of mind when I considered and implemented that feature. When I first saw the feature request on Codeberg, my initial reaction was reluctance. I wasn't convinced it was a good feature. But I was too busy with some ongoing algebraic graph theory research, another recent hobby, with a looming deadline, so I didn't have a lot of time to think about it clearly. In fact, everything about Wander Console has been made in very little time during the short breaks I used to take from my research. I made the first version of the console in about one and a half hours one early morning when my brain was too tired to read more algebraic graph theory literature and I really needed a break. During another such break, I revisited that feature request and, despite my reservations, decided to implement it anyway. During yet another such break, I am writing this post.
Normally, I don't like adding too many new features to my little projects. I want them to have a limited scope. I also want them to become stable over time. After a project has fulfilled some essential requirements I had, I just want to call it feature complete and never add another feature to it again. I'll fix bugs, of course. But I don't like to keep adding new features endlessly. That's my style of maintaining my hobby projects. So it should have been very easy for me to ignore the feature request for adding a referral query string to URLs loaded by the console tool. But I think a tired body and mind, worn down by long and intense research work, took a toll on me.
Although my gut feeling was telling me that it was not a good feature, I couldn't articulate to myself exactly why. So I implemented the referral query string feature anyway. While doing so, I added an opt-out mechanism to the configuration, so that if someone else didn't like the feature, they could disable it for themselves. This was another mistake. A questionable feature like this should be implemented as an opt-in feature, not an opt-out feature, if implemented at all. The fact that I didn't have a lot of time to reason through the implications of this feature meant that I just went ahead and implemented it without thinking about it critically. As the famous quote from Jurassic Park goes:
Your scientists were so preoccupied with whether or not they could that they didn't stop to think if they should.
Broken URLs
It soon turned out that my gut feeling was correct. After I implemented that feature, a page from one of my favourite websites refused to load in the console. To illustrate the problem, here are a few similar but slightly different URLs for that page:
- https://int10h.org/oldschool-pc-fonts/fontlist/
- https://int10h.org/oldschool-pc-fonts/fontlist/?2
- https://int10h.org/oldschool-pc-fonts/fontlist/?foo
The first and second URLs load fine, but the third URL returns an
HTTP 404 error page. The website uses the query string to determine
which one of its several font collections to show. So when we add
an arbitrary query string to the URL, the website tries to interpret
it as a font collection identifier and the page fails to load. That
is why, when my tool added the via=
query parameter to
the first URL, the page failed to load.
Later, with a little time to breathe and some hindsight, I could articulate why adding referral query strings to a working URL was such a bad idea. Altering a URL gives you a new URL. The new URL could point to a completely different resource, or to no resource at all, even if the alteration is as small as adding a seemingly harmless query string. By adding the referral query string, I had effectively broken a working URL from a website I am very fond of.
Qualms
It is also worth asking whether an HTML tool should concern itself with referral query strings at all when web browsers already have a mechanism for this: the HTTP Referer header, governed by Referrer-Policy. That policy can be set at the server level, the document level or even on individual links. The Web standards already provide deliberate controls to decide how much referrer information should be sent. Appending referral query strings to URLs bypasses those controls. It moves a privacy and attribution concern out of the referrer mechanism and embeds it into the destination URL instead. I don't think an HTML tool should do that.
There is also a moral question here about whether it is okay to modify a given URL on behalf of the user in order to insert a referral query string into it. I think it isn't.
Conclusion
In the end, I decided to remove the referral query string feature from Wander Console. One might wonder why I couldn't simply leave the feature in as an opt-in. Well, the answer is that once I had deemed the feature misguided, I no longer wanted it to be part of my software in any form. The project is still new and we are still in the days of 0.x releases, so if there is a good time to remove features, this is it. But my ongoing research work left me with no time to do it. Finally, when the post I've banned query strings appeared in my feed reader last evening, it pushed me enough to take a little time away from my academic hobby and devote it to removing that ill-considered feature. The feature is now gone. See commit b26d77c for details. The latest release, version 0.6.0, does not have it anymore.
This is a lesson I'll remember for any new hobby projects I happen to make in the future. If I ever load URLs again, I'll load them exactly as the website's author intended. I will never add query strings to your URLs.
```

---

## 4. Introduction to Beaver Triples

- 日期: 2026-05-09 16:02
- 链接: https://stoffelmpc.com/stoffel-blog/beaver-triples-tuples

```
You and your friends are planning to go out to dinner. Typically, you are the friend in the friend group that pays for everyone else's meals. But recently, the market isn't doing to well recently. So, everyone needs to start paying up.
However, not all of the homies are ballin' because well, the market isn't doing too well and one of them is still a student. But, just because external forces are kicking everyone's butt doesn't prevent the friend group from hanging out and enjoying a nice meal together. In order to have an enjoyable meal together, a restaurant needs to be decided upon. But, not everyone likes the same cuisine and some restaurants are more expensive than others. Considering that everyone's financial situation and food preferences are different, you attempt to devise a privacy-respecting way to allow the group to come to consensus on which restaurant to go to.
As you are a cryptographer, you know that you can leverage secret sharing to solve this problem. You figure out a simple scoring rule to determine which restaurant everyone will go to: For a restaurant j, person i will submit
aᵢⱼ = how much can I afford to eat at this restaurant
fᵢⱼ = how much do I want to eat at this restaurant
Each aᵢⱼ and fᵢⱼ are graded on a 0-10 scale. The friend level score will be sᵢⱼ = aᵢⱼ * fᵢⱼ. The group level score for a restaurant j will be Sⱼ = Σsᵢⱼ.
At the end, at least 2 friends will unveil the scores for the restaurant and then decide which restaurant the dinner will happen at.
We want to keep each person's aᵢⱼ and fᵢⱼ scores private in order to keep the peace among everyone in the group chat.
There are 4 friends in the friend group and you all are trying to decide among 3 restaurants to have the dinner at. You need at least 2 of them together to unveil the group level restaurant scores.
To make this concrete, let's say the 4 friends are Alice, Ben, Chloe, and Stoffel. The group is deciding between 3 restaurants: Restaurant A, Restaurant B, and Restaurant C.
Each friend submits a pair (a,f), where a is affordability and f is food preference.
The private inputs are:
Restaurant A: Alice (8,5), Ben (7,6), Chloe (9,4), Stoffel (6,5).
Restaurant B: Alice (6,9), Ben (8,8), Chloe (7,7), Stoffel (5,9).
Restaurant C: Alice (9,3), Ben (4,7), Chloe (6,6), Stoffel (8,4).
The goal is not to reveal these numbers to everyone in the group chat. The goal is to use them to privately compute the restaurant scores and only reveal the final group level scores at the end.
Using secret sharing notation, every private input gets turned into shares. So instead of Alice revealing her affordability score for Restaurant A, the group gets a share of that value. In notation, this is one instance of [aᵢⱼ].
Instead of Alice revealing her food preference score for Restaurant A, the group gets a share of that value. In notation, this is one instance of [fᵢⱼ].
The same thing happens for every friend and every restaurant. More generally, every private affordability score becomes [aᵢⱼ] and every private food preference score becomes [fᵢⱼ].
What we want is to compute shares of the friend level scores [sᵢⱼ] = [aᵢⱼfᵢⱼ], and then shares of the group level restaurant scores [Sⱼ] = Σ[sᵢⱼ].
At the end, the group opens the final restaurant scores for Restaurant A, Restaurant B, and Restaurant C, but not the individual affordability or food preference scores.
But you realize that there is one issue.
How can you actually compute [aᵢⱼ] [fᵢⱼ]?
We know that for each restaurant j and friend i, that we get the following shares:
pᵢⱼ(x) = aᵢⱼ + px, qᵢⱼ(x) = fᵢⱼ + qx
where pᵢⱼ(0) = aᵢⱼ and qᵢⱼ(0) = fᵢⱼ.
If we were to directly compute pᵢⱼ(x)qᵢⱼ(x), we get pqx² + (fᵢⱼp + aᵢⱼq)x + aᵢⱼfᵢⱼ where pᵢⱼqᵢⱼ(0) = aᵢⱼfᵢⱼ. So, this would indeed give us the right per restaurant per friend score privately.
The issue is that now, before we required at least 2 friends to unveil the final scores. But now, we require at least 3 friends to unveil the final scores; which is nearly everyone in the group chat.
Is there a way to still get a polynomial of degree t where the intercept of this polynomial is still aᵢⱼfᵢⱼ?
Well, it turns out, the answer is yes.
Computing with secret shares
Remember from the secret sharing article that secret sharing itself is a linear function with the following properties:
For secret shares [x] and [y], we have
For a known number a, we have
Additionally, we have the open operation which is reconstruction of the secret using Lagrange Interpolation:
How can we go about computing [x][y] without increasing the threshold needed for reconstruction?
For arbitrary x and y, let's consider the following plot:
Notice that the distance between 0 and x on the x-axis is x and similarly, the distance between 0 and y on the y-axis is y. We can draw a rectangle and get a rectangle with dimensions x x y with areas xy.
Is there a way to leverage this geometric interpretation of xy to come up with a way to compute [x][y] ?
In the plot, let's look closer at the interior of the rectangle. For an arbitrary point (a,b), we can similarly form another rectangle of area ab.
Notice that to we can write x and y in terms of a and b like so x = a + (x-a), y = b + (y-b).
Then we can recompute the area of xy in terms of a and b. We get
Each term forms a smaller rectangle within the larger xy rectangle.
Now, let d = x-a, e = y-b and c = ab. Then
We now have a relation that we can use towards enabling multiplication of shared secrets without increasing the degree of the underlying polynomial!
But hold on.
We are almost there but not quite.
If we have shares [x][y] then we'd like to reuse our rectangle identity to compute [xy] = [c] + [bd] + [ae] + [de], where d, e, and c are defined as above. But how do we handle d and e if they are also secret shared? The key is actually to reveal d and e and use them as publicly known numbers.
But doesn't that reveal x and y?
No, because as we will show, a and b act as randomly generated masks for x and y. Thus, revealing d and e reveals nothing about x and y.
First, suppose that a is not randomly generated. Then a is the result of some known process and can be discerned by an external observer. Which means that using the known relation d=x-a, an external observer can infer information about x. If an external observer can calculate a directly, then they can get x directly via x = d + a. So, opening d reveals information about x. Thus, a needs to be randomly generated. A similar argument follows for b.
Second, suppose that [a] and [b] are being reused across two different multiplications, (x, y) and (x', y'). Then, we have that d = x-a, d' = x'-a, e = y-b, e' = y'-b. Then, we can see that d'-d = x'-x and e'-e = y'-y, revealing relationships between secret values x, x', y, y'. These relationships contradict the fact that opening d, d', e, and e' shouldn't reveal anything meaningful about x, x', y, and y'. Thus, [a], [b] and [c] need to be used exactly once.
For example, if anyone in the group chat can discern that Ben has scored a restaurant 5 points higher than Chloe, then they know that have enough information to infer what Ben's private scores were. Maybe he likes the restaurant more. Maybe he can afford it more. Who knows? Well, no one should. We don't want anyone in the group chat to be able to determine such information.
We now have shown that a and b need to be randomly generated and used exactly once in order to be masks of x and y. Which means that d and e can be safely revealed without giving an external observer information about x and y.
To bring it all together, we can now compute
since d and e can be safely revealed.
The triples [a], [b], [c], where c=ab are what are known as Beaver Triples named after the original author, Don Beaver.
How do we use them though?
You know that there's a service that gives you beaver triples generated using entropy from satellites. Using this service, everyone in the group chat gets their shares of the same beaver triples [a], [b], [c].
Wait? Everyone gets the same beaver triples?
Yes and no. Everyone gets shares of the same underlying beaver triples. They do not get the raw values a, b, and c.
Alice gets one share of a, one share of b, and one share of c. Ben, Chloe, and Stoffel get their own shares too. Together, their shares represent the same underlying beaver triple [a], [b], [c]. But no individual person knows the raw a, b, and c values.
Since there are 4 friends and 3 restaurants, we need 12 friend level scores. Each friend level score requires one multiplication. So, the group needs 12 fresh beaver triples. Each triple is used exactly once.
Now, let's walk through one score. Take Ben's score for Restaurant B. Ben submits a=8 and f=8. Here, a is affordability and f is food preference. So Ben's friend level score for Restaurant B should be 8 * 8 = 64.
But Ben does not reveal either of these values directly. The group chat does not need to know how much Ben can afford Restaurant B. The group chat also does not need to know how badly Ben wants to eat at Restaurant B.
So, Ben secret shares both values. The group has [8] and [8], and now needs to compute [8 * 8].
For this multiplication, suppose the beaver triple has the underlying values a=5, b=6, and c=ab=30. The notation is a little overloaded here. This a is the beaver triple mask. It is not Ben's affordability score.
Again, nobody sees the raw values 5, 6, and 30. Everyone only has shares [5], [6], and [30].
The group computes [d] = [8] - [5] and [e] = [8] - [6]. Then the group opens d=3 and e=2. This is safe because 5 and 6 are random masks that remain hidden.
Now everyone can compute [xy] = [c] + d[b] + e[a] + de.
Substituting in the numbers, [64] = [30] + 3[6] + 2[5] + 3 * 2 = [30] + [18] + [10] + 6 = [64].
So the group now has shares of Ben's score for Restaurant B: [64], without Ben revealing his affordability score or his food preference score.
This same process happens for every friend and every restaurant. Inside the protocol, the individual friend level scores are not public values. The group only has shares [sᵢⱼ] for every friend i and restaurant j.
Now, because secret sharing is linear, the group can compute the restaurant level scores by adding shares.
For Restaurant A, the group computes [40] + [42] + [36] + [30] = [148].
For Restaurant B, the group computes [54] + [64] + [49] + [45] = [212].
For Restaurant C, the group computes [27] + [28] + [36] + [32] = [123].
At this point, the group has shares of the final restaurant scores.
No one has learned everyone else's affordability scores. No one has learned everyone else's food preference scores. No one even needs to learn the individual friend level scores.
All that needs to be opened are the final restaurant scores. Since this is a 2-of-4 secret sharing scheme, at least 2 friends need to open the scores.
Suppose Alice and Chloe are designated to open the final scores. They reveal their shares of the final restaurant scores. Using Lagrange interpolation, the group reconstructs Restaurant A's score as 148, Restaurant B's score as 212, and Restaurant C's score as 123.
Now the group compares the scores: 212 > 148 > 123. So the restaurant with the highest score is Restaurant B.
The dinner has been decided. Nobody had to reveal how much they could afford. Nobody had to reveal how badly they wanted a particular restaurant. The group chat remains peaceful. And a restaurant for the group dinner has been chosen.
To Recap
Ahead of time, everyone gets precomputed secret shared triples, [a], [b], [c], where c=ab
Everyone secret shares their preference and affordability scores into 4
Everyone passes their shares to each other
Upon your signal, everyone goes through the algorithm and uses the triples [a], [b], [c] to compute the multiplications involved using the identity xy = c + bd + ae + de
Once completed, 2 members of the group open the group-level restaurant scores using lagrange interpolation and reveal the results to the group
A restaurant for the group dinner has been chosen!
```

---

## 5. PipeDream on the Acorn Archimedes

- 日期: 2026-05-09 15:01
- 链接: https://stonetools.ghost.io/pipedream-archimedes/

```
PipeDream on the Acorn Archimedes
A productivity suite that willfully rejects common notions on how such software should behave, on an operating system most haven't heard of, running on a processor 30 years ahead of its time.
During the "throw everything at the wall and see what sticks" years of home computing, up to around 1995, a lot was thrown and a lot failed to stick. Sometimes clumps would form that appeared to have the combined friction necessary to maintain wall grip, each holding the other up. But, like Mitch Hedberg's observation of belts and belt loops, it was difficult to discern who was helping who stick to what.
Take for example, our focus today. We have a completely novel CPU, built by a tiny team of engineers who had never designed a processor before, running a bespoke operating system squeezed out in a rush to meet the shipping deadline of a computer that wanted to carry on the legacy of a system beloved by British schoolchildren, hosting a productivity suite that completely rethought what the term "productivity suite" even meant.
Together, they formed a complete computing dead-end. Yet separately, they each achieved life beyond expectations, given their shaky beginnings.
Let's start with the hardware, Acorn Computer Ltd.'s follow-up to the famous 8-bit BBC Micro, the Archimedes. Feeling the 16-bit processors of the day didn't deliver enough bang-for-the-quid, they began an investigation into 32-bit processor options. After reading a U.C. Berkeley paper extolling the virtues of the RISC architecture, and seeing firsthand the ease with which chips could be designed, in 1983 Acorn launched the Acorn RISC Machine project to develop the 32-bit brain of their next system.
The fruit of that labor, the ARM processor, defined the Archimedes line. Try as they might, Acorn could never crack the home market the way they did education. Still, those ARM CPUs had longevity well beyond the life of the company that commissioned it. Your smartphone likely has ARM in it right now, and Apple's entire current hardware ecosystem is built on its spec.
That powerful hardware needed a preemptive multitasking operating system that befit its computing prowess. That was to be ARX, whose troubled development missed the product launch window. In the meantime, so the computer could have something driving it at launch, a stop-gap operating system called Arthur was shipped. It was similar to Acorn's previous BBC Micro MOS (Machine Operating System), with a graphical layer grafted on top; hit F12 and that text interface will peek out from behind the curtain. Over time it was decided that Arthur was doing a bang-up job and ARX was cancelled.
Thus was born RISC OS, a cooperative multitasking WIMP (windows, icons, menu, pointer) with possibly the first application "dock" on a home computer. Its mandatory three-button mouse summons an application's current context menu at the pointer location; there are no menu bars whatsoever. Drag-and-drop is embraced as a central file management metaphor, even to save documents. On top of all that, it was the first to offer scalable, anti-aliased font rendering, even if its fonts were a little "off brand."
On top of this unique foundation, we have PipeDream. Developer Mark Colton was convinced that the boundaries between word processor, spreadsheet, and database were artificial and could be eliminated. A document should be able to do any of those functions at any time, anywhere on the page, he posited. One might think, "Oh, like Google Sheets." but PipeDream handles word processing more elegantly. Another might think, "Oh, like Apple Pages" but the spreadsheet and database functions are more robust in PipeDream. This particular balance of the three productivity functions feels unique amongst even its modern peers.
Does a productivity suite work better when it's just a single app? Did Colton successfully execute his vision? And where is the Homerton documentary we deserve?
Historical Context
(I didn't know Ghost blogging platform forces images to 2000px max; I've revised my design workflow to mitigate this in the future. To make amends for this timeline's illegibility at 2000px, please accept this PDF version)
Testing Rig
- RPCEmu v371 on Windows 11
- RISC OS v3.7
- 1024 x 768 15-bit color
- 64MB RAM
- PipeDream v4.13
Let's Get to Work
My process when first examining unfamiliar systems is as follows:
- boot the system
- launch my application of interest
- make a dummy document
- save it
- quit the emulator entirely and reboot
- load my saved document
I do that across a variety of emulators to see which gives me the least grief; I need to be sure I can trust a basic productivity loop. I usually try to give it a go without research, to see how far I can get on pure skillz (with a Z).
It's unusual to sit down at what appears to be a computer I understand and be baffled every step of the way. I've heard this system described as "elegant" and "easy to learn." This has me questioning if maybe I'm actually a very dumb person because my impression is "uncomfortable."
You know that modern horror story, aka "creepypasta", The Backrooms? It's a hidden world that co-exists with our own, which can be entered only by clipping through a seam of reality which separates the two. In there, buzzing fluorescents light an infinite maze of featureless, yellow-wallpapered office-style floor layouts.
If one were to find a running computer there, I suspect RISC OS would drive it.
It's just common enough in its GUI metaphors to feel familiar, and just off-kilter enough to turn that familiarity against you. Liam Proven wrote in The Register, "You will find it very disorienting, especially if all you know is post-1990s OSes." My dude, I've been computing since the 1970s and I find it disorienting.
Nothing is unlearnable (I'm dumb, not incompetent), but I genuinely had to work through its manual to acclimate myself. To be clear, I enjoyed the thrill of venturing into the unknown. After all, one of the goals of this blog is to investigate the less-trodden paths in software history. Still, there are times when I feel RISC OS is "having me on." (trying to ingratiate myself with British readers in today's post)
I'll start with the three-button mouse. From left to right the buttons are "Select", "Menu", and "Adjust." After weeks working with the system, I still can't figure out what problem the "Adjust" button solves. It's semi-analogous to CTRL + Left-click
on modern systems, as when clicking to add/remove elements to/from a set of selected items. Then, sometimes it does something unexpected like, "drag a window by its title bar without bringing that window to the front."
Other times it is baffling. Select-dragging
a file icon to a new folder location doesn't move the file to the new location. It copies the file. If you want to move the file, you must SHIFT + Select-drag
. Why are we "SHIFT" dragging anything when we have a perfectly good "Adjust" button?
Sometimes the "Adjust" button does "opposite" actions. Click a "down" scroll arrow with "Adjust" and it will to scroll up instead. Is that an "adjustment?" What does it even mean, to "Adjust" a mouse click? It seems like it could mean anything, and that's kind of my point. It's unguessable and unintuitive.
An interesting UI element (which predates NeXT and Windows 95) is the Icon Tray, an important tool inexplicably not described at all in the RISC OS 3 manual. Situated along the bottom of the screen, currently running applications and directory icons sit on a little shelf. Double-click "Select" on an application icon to launch it and... nothing.
Its icon displays in the Icon Tray, and that's it. We must now Single-click "Select" on that icon to actually bring the application to the forefront and activate it. I don't know what that's all about, but that's how it works.
Menus are fascinating in both the positive and negative meanings of the word. There are no menus on screen whatsoever, they are only made visible by the middle "Menu" mouse button. "Menu" clicking opens a given menu at the current mouse pointer location. Icons in the Icon Tray can be "Menu" clicked to get application-level menus, like "Make a new document." Within a document, "Menu" click will give us document-level options. Conceptually, I like the "Menu" button a lot.
Within a menu, any choices which open dialog boxes or control panels tend to open in-menu. It's kind of cool, being able to type, or flip switches and radio buttons, directly inside the menu itself, rather than popping up a modal window. However, it is jarring to have large panels suddenly lunge out like a xenomorph's inner jaws when scrolling through menus. These can obscure the root menu, depending on screen position.
The last point to get our collective heads around is file saving. When saving a new document, simply typing in a file name is not sufficient. Save dialog boxes expect and require the full path to your save destination; no assumptions or default folder locations are provided.
You can manually type in the full path to your desired save location like this:HostFS::HostFS.$.Apps.Documents.Examples.Tutorial.StoneDoc
While you type, the system will not assist you in navigating the directory structure; no autocompletion here. You must know the path by heart.
The other option, as described in manuals, is to drag-and-drop your document to its save location. Drag-and-drop really seems to be the RISC OS idiomatic way to manipulate files. In a Save dialog box there is a little icon for the application. It looks like decoration, but it physically represents your document. Type a name into the text field, then drag that icon to your desired save folder.
I don't want to get bogged down enumerating RISC OS's idiosyncrasies, but a few more things need mentioning. There is a kind of "programmer's art" ugliness to the user interface; those folder icons are terrible. There are graphical glitches, as when scrolling a window too quickly (though moving windows around shows full contents, which wasn't typical during that period). Everything you set up to customize the system, like desktop icons, window positions, desktop resolution, and other settings is reset every boot unless you manually tell the system to save the current state as the "boot file." The list goes on like that.
OK, now let's get to work
Sheesh, what a journey just to understand the basics. I expect that kind of learning curve for the text-based systems, as those DOS-like commands are unknown to me. For a GUI system to throw this "spanner in the works" (continuing my pandering) is unexpected, but a fun challenge. I can't feel myself growing to love it, but the initial feeling of discombobulation is receding.
Colton's grand unified theory of spreadsheets
A spreadsheet is an ordered matrix of cells, each of which can hold text or math. Cells with text are typically used as labels for columns and rows of numbers, and the math cells do the work of calculating relationships between those numbers. It's all very simple. No, wait, I mean it's "easy-peasy." (commitment to the bit)
Lotus 1-2-3 felt "columns and rows" could also be useful for textual data. They said the line between spreadsheets and databases is pretty fuzzy, and even today spreadsheets are used to hold and manipulate simple databases.
Then racecar driver Mark Colton pierced the veil entirely. It wasn't just spreadsheets and databases that had a fuzzy separation. If we can type arbitrary text into a cell in a spreadsheet, why couldn't we type an entire book? What if all applications were really just one application, in the end? He fired his first shot at uniting everything in View Professional.
This was released as PipeDream on the Cambridge Z88, a portable Z80 machine by Sir Clive Sinclair's Cambridge Computer. Built into the ROM itself, it was insta-boot, insta-launch right into a multi-purpose integrated document suite. Jerry Pournelle, in BYTE Magazine's February 1989 issue, was moderately enamored with the hardware, but PipeDream was, "disappointingly hard to use."
With Acorn evolving their BBC Micro via the Archimedes, Colton continued to support their hardware line. In interviews, he seemed to really be leaning toward Windows for the future of his company. However, since he switched development to C and there was a C compiler for the Archimedes, he said it wasn't hard to provide his product to the Acorn crowd. Running on Arthur, the precursor to RISC OS, he embraced and extended the "one document, many forms" approach.
Much like today's Google Sheets, we can add arbitrarily long sections of text, insert images, set up database information, perform spreadsheet calculations, run spellcheck, and generate inline graphs. However, try typing a chapter of a book into Google Sheets if you want to drive yourself "mental." (there's no stopping me) In PipeDream, that's frictionless (within a certain definition of "friction").
Like RISC OS itself, PipeDream also requires certain shifts in thinking to not lose a finger to its sharp edges. I suppose that when a developer offers a truly new paradigm, it is fair to ask users to meet it halfway. I'm not convinced the advertising (see "Historical Record" at the end) gave customers a full understanding of how drastic that shift was.
Rank and file
"Menu" click the Icon Tray icon (i.e. the application-level menu) for PipeDream to start up a new "Text" file and begin typing into cell A1. You'll find that text overflows, across cell boundaries, until it hits the "row wrap marker" seen in the rightmost column header (shown as a "down arrow" icon).
Every line of text is its own row, in spreadsheet terms. As you type, PipeDream fills the current row, then silently inserts a new row to catch overflow. Until a paragraph break, these rows are internally associated as a logical unit. Edits which alter or disrupt text flow across rows within a paragraph are not reflected immediately in the UI. Or maybe they are? It's hard to tell with the graphic glitches in the screen redraw, a constant source of frustration while working on this article.
PipeDream concedes the reflow point itself. When in doubt about the current visual structure of your text, CTRL + R
, a manual action, will force PipeDream to recalculate text wrapping and line spacing. This can be mitigated a bit through a hidden toggle in the "Options" screen, the confusingly named "Insert on Return." This reduces the need to force a manual reflow, but can still leave visual chaos.
Interestingly, I saw similar redraw issues in View Professional on the BBC Micro. It would appear this is, to some extent, part of the software's DNA. Honestly, this is all "a bit of a shambles." (the hits keep coming)
Cell culture
Have you ever wanted a word processor that won't indent paragraphs? PipeDream being a chimera, navigation idioms are forced to choose which parent they love most. An examination of the TAB
key demonstrates this.
In a word processor, we usually have a horizontal page ruler with tab stops. Tab over to a tab stop and type to align text at that indentation point on the page. In a spreadsheet, TAB
navigates us to the next cell to the right. In PipeDream, the spreadsheet idiom wins TAB's love.
In a text cell, TAB
sets an invisible indicator at paragraph start which forces every subsequent line of that paragraph to begin at that same column. For example, by default every line of text is added to column A, the leftmost. If we TAB
to column B, the text will start there but when it wraps to the next line, that will also begin in column B. "Indentation" is at the paragraph level, not the line level.
How do we indent the first line of a paragraph? The manual has a solution.
In looking back through the history of Colton's software on the Acorn line, I found this note in a review of View 2.1, his standalone word processor for the BBC Micro. "Why is there no numerical information on the rulers or cursors to assist formatting?" asked Acorn User, January 1985. It seems Colton had it in for rulers for a decade, and to my thinking this points to a disconnect between what a programmer thinks users need, versus what users actually need. A stubborn rejection of norms doesn't always mean we're on the right track.
Cell division
We can use the cell-based layout engine of the program to pull off a fun party trick. Under "Options" there is a toggle between Row and Column text wrap. "Row" behaves like a typical word processor. "Column" lets us divide the page into columns, like a newspaper. Tab between columns and the column width will be respected by the word wrap. Kind of cool, and could be useful in a "I need to make a newsletter, stat!" pinch.
Like a spreadsheet, column widths are document-wide, so no mix-and-match. Someone very clever with the tools could probably coax complex layouts out of it, but that would require an ungodly amount of pre-planning, design, and patience before starting a document. You really have to try to get it right the first time, because I don't find PipeDream particularly adept at handling large structural changes after the fact.
Grab bag
The column-based formatting gets frustrating, but in other ways the word processing is "bog-standard." (How many will I squeeze in? Place your bets!) We have a built-in spell check, user-definable dictionary, word count, text alignment, font choices, and an anagram/subgram maker. Bank Street Writer Plus had an anagram maker as well. Why was that such a thing back then? Have I forgotten some fad of the 80s and 90s?
That's all fine and dandy, but I'll tell you what isn't: there's no simple cut/copy/paste, at least not as a modern audience may understand those tools. In the document, we are restricted to cell-level selection, meaning I can't select individual words inside cell A1. I can only select the entire cell A1, which in PipeDream means an entire line of text.
We can ask PipeDream to edit a cell in its own window, where it pops out for surgical editing. "Edit Formula in Window" highjacks the spreadsheet formula editor in order to get character-level selection control. In this pop-out window, we can highlight individual words and do typical cut/copy/paste actions. Notice, though, we're still restricted to only the text within the cell, which means only that line (row) of text. It's highly likely any given row will contain the tail-end of the previous sentence and the first part of the next sentence. If we want to cut out a specific sentence which doesn't align neatly to the row structure, there is no way to do so.
I will repeat that.
There is no way to cut/copy/paste an arbitrary string of characters.
Now I feel PipeDream's vision working against itself for anything but simple correspondence. Remember, this is version 4 of PipeDream, Colson's fifth software release to pursue this unified application dream, and this is where we're at. I can't imagine writing anything substantial within these frustrating limitations.
Lotus position
As a spreadsheet, PipeDream performs far more admirably, even if certain conventions have been eschewed in favor of its new vision. Hey, if you're gonna quirk it up, might as well go for broke.
Unlike its spreadsheet ancestors, there is no /
menu, nor is there a simple way to tell PipeDream that we want to enter a formula into a cell, as with @
to denote a function call, or =
to indicate we want to do math. Many of Lotus 1-2-3's innovations have been utterly ignored.
The global "Options" allows us to set default behavior for cell entry. Setting it to "numbers" will put us into the right context for easy formula entry, or we can click into the ever-present formula entry line at the top of the window. Turn on the "Grid" overlay to draw cell boundaries and before you know it what was a word processing document is now a spreadsheet with "the full Monty." (TIL it doesn't mean "full-frontal nudity")
The functions available to number crunchers are plentiful and robust. Trigonometric functions are a given, but its inclusion of matrix math may come as a surprise. Even complex functions like acosech
, which computes "the complex hyperbolic arc cosecant of complex_number
as a complex number," are present and accounted for, so hardcore math nerds can breathe a sigh of relief.
A wide number of financial functions, statistical functions, lookup tables, string manipulations, and date handling are all here. So too are flow control tools, like if
, repeat
, while
and more. There are even GUI controls available for showing error dialog boxes and prompts for user input, though those are only available from within custom functions.
DIY
Yes, if you're missing a function, you can make your own. In a new worksheet, start a formula with function()
(which can accept typed parameters) and end it with result()
. In between, do the work. PipeDream will check syntax and accept or reject each line of your function. If accepted, it will prefix a line with ...
In your real working worksheet, access the formula by [file that contains your function definition]function(parameters)
. That file reference implies PipeDream can access data from other worksheets, and that is true. Even a cell reference in a formula can be pulled from a completely different worksheet.
I find the syntax for custom functions opaque, and the manual does a poor job of explaining what is possible and how to use the tool. There are a handful of examples provided with the software installation, with bugs, that reveal secrets only upon very close inspection. For example, notice in the screenshot above that the parameters to the function are later referenced by @
prefix, but local variables, as set by the set_name
function are not prefixed when used in calculations.
It's those subtle little things that tripped me up. The same with having the return value called result
. Or how the program has a selection of "Strings" functions, but when passing a string as a parameter its type is "Text." I stared at that syntax for a LONG TIME before finally realizing my various little misunderstandings.
Customization doesn't stop there. Individual keys can be defined as shortcuts to longer string sequences, F-Keys (plain and modified) can be defined to trigger commands, and command sequences (triggered by the CTRL key) can be redefined to your liking (which risks overwriting built-in command shortcuts).
You really can make PipeDream your own, though you're in for a struggle compared to Lotus 1-2-3 and the thousands of books available to help learn its principles. I found no actual books for PipeDream, just publishing announcements in old magazines. Something must exist, but the internet at large appears bereft.
Based data
On the scorecard of "this amalgamation approach to productivity software is working," I'd say we're 1 and 1. The spreadsheet tools are fiddly, but robust. The word processing has me very underwhelmed. Time for the tie-breaker: databases.
Using the supplied Lotus 1-2-3 conversion tool, I was able to bring in the data I originally created in CP/M dBASE II and had subsequently converted to DOS Lotus 1-2-3. Now it lives on in RISC OS PipeDream. This data has more passport stamps than Indiana Jones.
Let's consider some of the basic things one might want to do with data. PipeDream beats out Lotus in sorting, giving us a five-stage, multi-row, sort with ascension. Not too shabby for the time, all things considered.
Search and replace does what it "says on the tin" (in for a penny, in for a pound), and can also accept regex-like tokens and patterns.
More interestingly, cells can be set up to directly perform queries on table data. There are a small handful of d
prefixed database functions to calculate averages, min/max, counts of things, and more.
One last feature of note is how to use the query tools to extract a result into a new database. This is interesting as it utilizes RISC OS's drag-and-drop Save functionality in a clever way.
I was initially ready to write off the database functionality as being underwhelming, until I reminded myself of the stated goal for PipeDream. Its core proposition is that there is no difference between the various aspects of the software. The word processor is the spreadsheet is the database. We're not limited to the "database" functions when manipulating our database data. We have access to everything the program has to offer, at all times.
Let's clip through the inverted UV plane separating database and spreadsheet, and see what kind of trouble we can get into.
Beyond the veil
I'm thinking back to the Lotus 1-2-3 article and how database information was queried there. With a table of data, we had to use the built-in query forms, define areas on the sheet to hold query parameters, and designate another section of the sheet into which query results would display. It was an obtuse Rube Goldberg machine that I couldn't understand until I drew a diagram of the process.
In PipeDream, we just write a formula, the same as if it were a spreadsheet. Let's get the average rating of all adventure games in the database published before 1985.
davg(e2e31, c2c31="Adventure" & b2b31<1985)
"Bob's your uncle!" (I was hoping to work that one in) Let's mix it up a little and get the same average, but only for titles which begin with "Zork." We can use wildcards, but let's leverage PipeDream's word processing string tools.
davg(e2e31, left(a2a31,4)="Zork" & c2c31="Adventure" & b2b31<1985)
The most awesome part about this is that, like any spreadsheet formula, it updates in real time. Change the ratings, or add a new Zork game to the mix, and get the new average instantly. The database is the spreadsheet is the database, so that calculation can then be referenced as a value for another cell's formula, perhaps adding sales tax to the average unit price. While we're at it, might as well throw in some fancier text formatting to make it look pretty.
In the Lotus 1-2-3 investigation, I wanted a pie chart showing a breakdown by game categories. Lotus had a handy UNIQUE
function which removed duplicates from lists, making it possible to extract the full list of unique game categories, which could then be used as the query parameters for generating a chart.
PipeDream can't do that, but it does have other string parsing routines, variables, cross-file data referencing, and the ability to write custom functions and macros. I don't doubt it would be possible to homebrew a workaround to this missing function. In fact, let's "have a bash at it." (swish!)
Ultimately, I couldn't achieve an elegant solution, but I could achieve my goal. I sorted the original data by genre, then created a UNIQUE
column that checks if the genre for each row matches the one above it. If so, it's a 1
otherwise a 0
. Then, I extracted all rows with 0
in the UNIQUE
column. Last, I did dcounta
(count any items in a list), where the source list is contained in the original database document. With the documents thus linked, I get real-time graph updates when I alter the core database, thanks to external reference handling. Everything's "tickety-boo!" (I'm trusting The Independent on this one)
OK, PipeDream, you're winning me over a little more now.
By your powers combined
Time to take this to its logical conclusion. We haven't yet pushed it as the multi-purpose document creation tool it promises to be. We've done a little dabbling, with text formatting and data extraction, but I want to see everything come together. I want the borders to crumble.
The approach I'm finding to be least troublesome is to begin with a "text" document, then decorate that with spreadsheet/database elements.
In building that document, here's what I learned.
- Because rows and columns are shared throughout the document, insertions and deletions, or moving things around, creates difficult-to-resolve layout issues. If a spreadsheet sits to the right of a block of text, and we want to insert a row into only the spreadsheet part, that's not possible. Doing so will also insert an empty row into the paragraph, leaving a gap.
- PipeDream has a strange concept of "global font" vs. "local font". Local fonts can't be changed until the global font is set to something other than the system font. The global font controls value cells, which cannot be styled individually. Local fonts will style a cell from wherever the cursor is currently located, and it is very easy to target a cell and style its font, but miss the first character or two, even though the entire cell is highlighted as a selection. "What will be the result of my action?" is not always crystal clear.
- The controls for styling charts are difficult to understand, and messing up is hard to reverse out. I accidentally added "New Text" to the chart and it took a long time to figure out how to delete it; selecting it and hitting "delete" doesn't work. There is no way to modify the legend.
- There's no facility for selecting elements for inclusion/exclusion from the graph. In my case, formatting to look good on the printed page meant adding empty columns which wound up in the pie chart. This is very representative of the struggles the layout engine introduces. Making data look good in one context risks "making a shambles of it" (are these working? have I won you over?) in another.
- Page layout settings are cryptic. Margins can only be set to the top and left (?!?!) and only in unspecified numeric units. I used the template default values, and the page wound up shifted down and to the left. Getting beautiful output is a challenge.
- How could I forget? There's no UNDO! Some programs, like !Draw (vector illustration) and !Edit (text editor) have undo, and others like !Paint and !PipeDream do not.
Where are they now?
We have a unique confluence of interesting technologies coming together to form a strangely flawed jewel. It sparkles and shines when the light hits it just right, and in those sparkles we may catch a fleeting glimpse of a world that might have been. Might have been, but wasn't. Let's see where each of the underlying technologies wound up and those in the know can feign shock with the rest of us when we learn that ARM isn't the only thing that survives to this day.
ARM I'm gettin'
We'll start with the obvious truth: ARM won. It's in everything, everywhere, all at once. If it isn't in your computer, it's in your phone, or your Newton, or your Palm Pilot, or your Canon camera, or your Nintendo DS, or your Nintendo 3DS, or your Nintendo Wii, or your Nintendo Switch, or your Nintendo Switch 2, or your Raspberry Pi, or maybe you're sidetalking on your N-Gage. Its combination of low power consumption with high performance makes it ideal for mobile devices, of which we are in abundance.
But why ARM specifically? Others have swung for the RISC fences and stumbled, yet Acorn set two engineers to the task of designing their first ever microprocessor and somehow achieved a ubiquity that has remained (mostly) unchallenged.
Apple/IBM/Motorola gathered their forces and developed their own RISC architecture, which debuted in Apple's Power Macintosh 6100. PowerPC doesn't mean much to a Windows/Intel crowd, but the Mac faithful remember all too well Apple's investment in that as the successor to the x68000.
Frustrated by delays in the evolution of the chip line, Apple wound up ditching it for Intel x86, even if they eventually rediscovered the joys of RISC. PowerPC went on to be adopted by a number of game consoles, notably the Nintendo Wii, XBox 360, and PS3 simultaneously. The line continues today, and heck, Mars rovers Curiosity and Perseverance both have PPC inside. Hard to call such a history a "failure," but who outside hardcore Amiga faithful today is clamoring for a PowerPC chip?
The SPARC RISC architecture, of "Sun SPARC Workstation" fame, chugged along until as late as 2017, when Oracle purchased Sun. A notable achievement, in pop culture circles, is this is the hardware Pixar's first Toy Story was rendered on. Though Oracle disbanded the design team keeping the architecture alive, the architecture itself is free and open source. There's nothing stopping an intrepid reader from carrying on the lineage, I suppose. Fujitsu, the last of the production line for the series, has abandoned SPARC for ARM.
I'll be honest, I can't figure out what ARM does so much better than other attempts, like SPARC, at making a great RISC processor. Reading through the Ars Technica story, it seems to be less about the underlying tech and more about the savvy promotional work of Robin Saxby and his absolute unwillingness to lose the RISC wars. Where others were building RISC for the server-side, ARM committed themselves to the mobile side, skating to where the puck would be.
Whatever the case, whatever the magic, ARM makes it available to anyone who wants it, through their licensing partnerships. Ultimately, this really seems to be what has given ARM its staying power; a low barrier to entry to quickly join in on high-performance, low-power draw, ARM fun.
It's important to note that ARM doesn't make processors; they only license their IP. <<record_scratch.mp3>>
Breaking News, as of literally just like a week or so ago:
ARM is set to launch its own silicon for the first time in 35 years.
https://techcrunch.com/2026/03/24/arm-is-releasing-its-first-in-house-chip-in-its-35-year-history/
OK, be that as it may, it is still substantially correct to say that IP licenses are their bread and butter. A "core license" allows a company to manufacture a specific ARM-designed CPU, a popular choice for system-on-a-chip designs. Alternatively, an "architectural license" permits a company to design and build its own custom CPU around the ARM instruction set. That's what Apple does with their A- and M-series chips.
In recent years, ARM is feeling light competitive pressure from the RISC-V architecture. Born in the same UC Berkeley labs that birthed the original RISC design reports that inspired Acorn to take a chance on RISC, its architecture, unlike ARM, is free and open source. Consumer-level devices running on RISC-V have already started shipping. A new race has begun.
Archimedes screwed
Acorn's Archimedes line ultimately never sold particularly well. It's hard to nail down specific sales figures, but a 1991 Acorn shareholder report said, "Acorn is now the UK number one supplier of 32-bit RISC machines with an installed base of over 150,000 units." For context, the Amiga line had sold some 2 million units by 1991.
We can't say Acorn didn't put in the effort, releasing some 13 model variations in under a decade. The general consensus seems to be that they "cost a bomb." (that's a new one on me) Schools adopted them, as a natural evolution of Acorn's prior BBC Micro installations, but at US$3,000 to $9,000 (in 2026 money) families just couldn't afford to put one in the home.
In the mid-90s, Acorn dropped the Archimedes line, switching tracks to the more business-like Risc PC line, and produced a handful of systems around the StrongARM CPU. However, while the CPU spirit was willing, the motherboard flesh was weak, leaving the CPU underutilized. The lineup ended concurrently with the end of Acorn around 1998. Castle Technology tried to keep the Risc PC line going, post Acorn, but called it quits shortly thereafter, in 2003.
RISC-OS
Open-sourced in 2018, RISC OS Open keeps it running and up to date for modern RISC-based hardware platforms, especially the Raspberry Pi. Currently at v5.30 at the time of this writing, it is still a 32-bit operating system with "moonshot" aspirations of 64-bit someday. *checks watch* Time is ticking to pull that together before fading into 32-bit irrelevance.
Did I mention how tiny this thing is? The latest version for Raspberry Pi is a 155MB download. Version 3.7, which I used for this article, downloaded as a pre-configured emulator with OS and apps pre-installed, was a mere 129MB. Even the most up-to-date pre-configured package tops out at a "massive" 1GB, apps and emulator inclusive. How big is macOS on ARM?
The death of Mark Colton
Leading in with his View lineup of productivity apps on the BBC Micro, Mark Colton was the man with the all-in-one vision. With View Professional, he took his first stab at providing an uber-app for that 8-bit workhorse. It's primitive and clunky to use, but the spark is present.
He would then expand on his ideas through the PipeDream lineup, taking it all the way to version 4.5. Every version refined the vision, but ultimately its character-based layout engine roots became a limiting factor to its growth.
One rewrite later, he had a true GUI-based implementation, for both the Archimedes and Windows, in Fireworkz released in 1993. Having created standalone products Wordz and Resultz, Fireworkz combined those back into one. By mid 1995, Fireworkz Pro added in the database functionality, merging the new Recordz into the product, and that's where Colton's involvement ended.
Besides asking "What even is a spreadsheet anyway?" Colton's other passion was race car driving. In August 1995, an engineering defect in the front wing of his Pilbeam M72 caused it to fold under his car while he was at top speed. He lost control, crashing headlong into a telegraph pole, and was killed.
Long live Mark Colton
Most shockingly, both PipeDream and Fireworkz continue to be maintained to this day. Mark's father, Richard, generously open-sourced both PipeDream and Fireworkz just before his own untimely death in 2015. Fireworkz Pro, the version that includes database functionality, is not open-sourced and is still for sale.
The PipeDream package available for installation in RISC OS package manager is not the version I'm using for this article. That is the modern update, which adds a bunch of niceties, including a GUI toolbar for formatting text, expanded spreadsheet functions, and a mind-boggling number of bug fixes.
This is all maintained by lone developer Stewart Swales, someone intimately involved in the RISC OS and PipeDream history. He worked at Acorn and helped develop Arthur, the OS that became RISC OS. Later, he joined Colton Software as lead developer, working on PipeDream and Fireworkz. There's really nobody better to carry on the legacy.
Where, precisely, Colton's continuation of that legacy would have gone, we can't say with certainty. However, we do have a little insight into his thinking. In an interview with Acorn User, December 1994, he said, "Over the next few years...we won’t be writing spreadsheets either; we'll be writing a totally different style of program. I expect spreadsheets, word processors and so on to be provided as part of the operating system in the future."
Reach vs. grasp
Let me start by making it clear that I appreciate the effort. I say that with all sincerity and for everyone involved. From the machine, to the OS, to the productivity suite, all katamari'd up into a unique star. It was a lot of fun feeling like a beginner again. I had moments of true learning, shedding expectations of "how things should be" and experiencing fresh, alternate ways to approach work.
I said at the beginning, the question that needs answering is, "Did Colton successfully execute his vision?" and here I must waffle. From View Professional, through five major releases of PipeDream, and two Fireworkz releases, he held fast to a very particular line of exploration. That he never wavered in his pursuit of that vision, says to me that he must have felt he had achieved his goal to some degree. In that regard, we can say he successfully executed his vision.
As an end-user, it is hard to align myself to that vision. I get what he's after, especially when trying to make sure documents always reflect the latest data. After using PipeDream for a number of weeks, I remain unconvinced that the solution is to graft all software into one uber-application. If we follow that thinking to its logical conclusion, then why not include paint features? Why not include robust desktop publishing features? Where would it stop?
Had the amalgamation of these productivity apps birthed something uniquely unachievable by other means, or unlocked some latent potential in the individual apps, I'd be very willing to adapt to this "skew-whiff" (last one, I promise!) approach to application design. As it stands, I ultimately don't see what it does that wouldn't be equally well-served, perhaps better-served, by intelligent file link management with robust publish/subscribe functionality. In fairness, a deep implementation of that would work best as an OS-level feature, and Colton could only control his own works.
Paradoxically, the most frustrating aspect in removing the barriers between applications is how we wind up with a slate of new barriers forged in that alliance. Colton said of View Professional that even when the apps are combined, none should feel like a compromised version of that app. Yet, compromises are what I feel with every document I build. Is it worth giving up easy text formatting and basic cut/copy/paste for the off-chance I might need to insert a little spreadsheet table? There's an 80/20 rule being almost willfully ignored here.
I love that Colton had a unique vision and stuck to it.
I love that someone tried to forge a new path in productivity application design.
I love that PipeDream exists, but I don't love it.
Sharpening the Stone
Ways to improve the experience, notable deficiencies, workarounds, and notes about incorporating the software into modern workflows (if possible).
Emulator improvements
- Getting started with RPCEmu, using a pre-built package, was as dead simple to use as you'd imagine. I experienced no crashes of the emulator, operating system, or PipeDream. It was a very solid experience in that regard.
PipeDream itself, at least the version I used, had a ton of annoying bugs and the graphical glitches were even noted in a review by Micro User, February 1992. But emulator-wise, everything was smooth. - I recommend first-time users grab a pre-built image for quickly jumping in and seeing what the fuss is all about. I also do recommend going through the RISC OS Manual. The operating system is almost unusable until you learn its little tricks and nuances of operation.
Pre-built images: https://www.marutan.net/rpcemu/easystart.html
v3 Manual: https://archive.org/details/ro-3-user-guide
v5 Manual: https://archive.org/details/risc-os-5.28-user-guide - Technically, I am cheating a bit in this review. RPCEmu doesn't emulate an Archimedes but rather Acorn's later Risc PC. I ran PipeDream from floppy in Arculator, which explicitly emulates Archimedes systems, to compare the experiences. Except for RPCEmu's snappier performance (which I want anyway), RISC OS itself abstracts away the hardware layer so much it didn't seem to matter one emulator over the other.
Troubleshooting
- The emulator itself expects some specific keyboard, with the
\ |
key situated betweenLEFT SHIFT
andZ
. I don't have that, and nothing on my extended keyboard would send the right code to the emulator.|
is used for logicalOR
in PipeDream data queries; I had to use Windows ALT keycodes. - I mentioned earlier, but I'll make it explicit here: there is no undo.
Interfacing with the Real World
- Fireworkz is available as a native Win32 app. It launches without issue on Windows 11 64-bit, and even in Wine on macOS. It looks and feels exactly like Fireworkz on RISC OS, which looks and feels a lot like the latest version of PipeDream (minus the database parts). The list of bug fixes and quality of life enhancements is vast. Scrolling through all changes since Colton passed is kind of pointless due to its scope. I'll say, "a lot has improved" and leave it at that.
As a local-only alternative to the Google/Apple/Microsoft hegemony, it's worth checking out. It's free, open source, actively maintained, a mere 2.5MB download, and for God's sake at least it's trying to do something different. - Getting documents out of RISC OS into a modern system is easy, but has its caveats. RPCEmu can directly save to the host operating system, so getting files out is a non-issue. PipeDream's options for saving documents will strip the document's uniqueness, however.
- Saving as ASCII will try to keep text precisely as shown in PipeDream, inserting line breaks at the end of every line of text. Tables are just tab-indented. Any text formatting, fonts, graphs, etc. are stripped, of course.
- Saving as "Paragraph" is like ASCII, but will keep text together as logical paragraphs. This is much better for pasting the text into new documents. We still lose anything done to make the document look pretty.
- PDF printing is an option in RISC OS, and proved to be the best way I could find to get PipeDream documents into the real world. This required two parts: activating the PDF printer and running a separate !PrintPDF application. With both active, PipeDream generated PDFs without issue.
```

---

## 6. Apple is increasing my cortisol levels

- 日期: 2026-05-09 14:40
- 链接: https://blog.kronis.dev/blog/apple-is-increasing-my-cortisol-levels

```
Apple is increasing my cortisol levels
Date:
I'm creating a simple developer utility to make managing Claude Code profiles (e.g. running it with DeepSeek, or some OpenRouter models) a little bit easier. The utility itself is written in the Go language, and the tooling there makes it really easy to compile for various platforms - I get a static executable I can put anywhere I want. I intend to release it soon, but for now wanted to check how easily I can get it running everywhere.
It works just fine for distributing Windows software (I get an .exe).
It works just fine for distributing Linux software (same deal, after chmod +x
).
Distributing Mac software
It does not just work for macOS and my MacBook instead shows me this:
What you see is their quarantine kicking in for downloaded software, even if I share it with myself over Nextcloud.
Technically, you can ask your users to override it manually, in the terminal:
Most developers might be willing to do that. It is not, however, good user experience and might raise some eyebrows.
Doesn't seem like such a big deal, right? I'll just enroll in their Apple Developer Program, sign the executable and be on my way, right?
Giving Apple money, and failing
Wait, they want how much money for the account?
And it's a yearly subscription? My brother in Christ, I intend to release a utility maybe a dozen or two dozen people are going to download, tops, for like 7 USD on Itch.io with a pay-what-you-want model, meaning that most of those people will probably choose the price of 0 USD instead (since I don't intend to be like Apple, people have various circumstances).
That means that even if it works out that much, there's going to be VAT and Itch.io will also take a cut so out of those maybe 50 USD I'll get about 25 USD, which funds me about 3 months of that Apple Developer Program price. I guess the reason for it being priced like that lies somewhere between greed and wanting to gatekeep hobbyists out and only support Serious Users™, but it seems a bit stupid. Oh well, I already had to get the overpriced MacBook for another freelance thing, because they also won't let me compile macOS/iOS apps on Windows or Linux, so I guess this is just them spitting on me after slapping me in the face.
What I get from that is that articles like An app can be a home-cooked meal are cool but don't take the economics of wanting to release something publicly into account - unless you're developing something that you'll add a bunch of monetization to, you'll be losing money. For desktop software there is Homebrew but that also means that you couldn't charge a few bucks for it even if you wanted to (or that you'd need to add mac-homebrew-install-instructions.txt
to the Itch.io downloads page when doing the pay-what-you-want approach, which would feel awkward).
I don't like that the economics are pushing software and app development in a direction where releasing a package (that might be non-open-source or just source-available, but you want to release binaries) costs money, though I also acknowledge that there would be other issues, like insane amounts of spam, with not doing that.
Then, we get to the actual verification process - it's understandable that they'd want to verify my ID. The problem is that on the MacBook they also expect me to use its webcam to take a picture. I will admit that my M1 MacBook Air is getting dated at this point, but regardless of what lighting I tried, I could just not get a good picture of the document. It's not like they were like "Oh hey, we've detected that your own iPhone is connected to the same local network as this MacBook, would you like to use it as a camera?", so for about 10 attempts, this is what I saw:
Eventually, I moved over to trying to use my main webcam for that, since their built in one just doesn't work:
Why they can't just let me upload a scan of the document eludes me. I mean, I guess I can imagine a few reasons why, but it'd probably be easier to forge my own ID so it's not as glossy rather than having to turn my small kitchen table into this. Pictured for maximum frustration, a dongle that I needed:
Even that wasn't good enough, because understandably it doesn't have autofocus for something that you hold close. Not only that, but every 2nd failure seemed to just give me a generic error and I'd have to start the whole enrollment process from the beginning again:
Luckily I realized that I can install the app on my iPhone directly. There, it worked on the first try. I guess it must really suck if you don't have an iPhone or a fancy webcam, better spend some more money so you can give them money! The payment went through okay, soon after I had an activated developer account.
Except of course I didn't, look, the app tells me to await an e-mail (which I seemingly already received?):
And the desktop app doesn't care at all either, it doesn't even know that I've tried the enrollment, and offers me to start the whole thing over again, despite me being signed into the exact same account:
It's probably a case of eventual consistency and some background processes or whatever, but it's also quite frustrating and, in a word, stupid.
Apple is kind of frustrating
Apple, I think you make hardware with pretty good build quality and the M-series chips made for pretty much the perfect notebook for me - and I'm sure they're great main dev machines for those that can afford the higher spec versions.
I think that's nice and I genuinely enjoy having the iPhone SE 2022, at least before learning that you killed off the budget series altogether (your new e-series are more expensive) and removed the nice silent mode toggle on the side and removed TouchID. That's before we even start talking about the 3.5mm jack and frankly all of that makes me question whether my next phone shouldn't just be an Android again.
I can deal with needing software like AutoRaise and Rectangle and DiscreteScroll alongside others to customize your OS to my liking because you won't let me do that myself like most Linux distros do. I can even deal with your window focus needing an extra click across multiple monitors and AutoRaise being nice but perhaps too aggressive, since the developers are at least trying to make the experience nicer!
I can deal with your keyboard shortcuts being odd and not even having a "Cut" option in your Finder program.
I can deal with your weird Control/Command button setup which even breaks remote desktop software.
I can deal with your weird "programs you close aren't actually closed" approach even though you sold me a MacBook with 8 GB of RAM just so I could develop software in your walled garden ecosystem.
But to first vendor lock me to your ecosystem for developing apps, then demanding a whole bunch of money so I can sign my software and it not get quarantined all while I'm not too well off financially, then refuse to let me submit my documents to you because your hardware produces pictures that are not good enough and make me have to install the app on a phone that's also expensive and that not even everyone has, then to still make me wait and have your apps not even show that I've submitted my application?
You know what? Apple, fuck you and your forsaken ecosystem. This sucks.
A more sane world
I can use SmartID to verify my ID (and age) in about 20 seconds when buying an energy drink at the local grocery store.
I can use eParaksts to digitally sign documents in about a minute, from either my PC with a card reader (using my government issued ID card), or my phone with their app, ending up with a proper cryptographic signature either attached to the EDOC container (ASIC-E) or a PDF file directly.
I'm sure that other countries also have plenty of similar services for ID and age verification, signing documents, and other digital services. I acknowledge that that's not all of them, and that things are all over the place in this regard (alongside the credit card mafia holding a lot of the world's payment infrastructure hostage), but come on, surely it's possible to create something that works better than my experience did.
Having a bunch of scrappy Baltic software packages working better than those by a multi-billion dollar company feels silly.
Other posts: Previous »
```

---

## 7. GrapheneOS fixes Android VPN leak Google refused to patch

- 日期: 2026-05-09 14:11
- 链接: https://cyberinsider.com/grapheneos-fixes-android-vpn-leak-google-refused-to-patch/

```
GrapheneOS has released a new update that fixes a recently disclosed Android VPN bypass vulnerability capable of leaking a user’s real IP address.
The leak happens even when Android’s “Always-On VPN” and “Block connections without VPN” protections were enabled.
The issue, disclosed last week by security researcher “lowlevel/Yusuf,” affected Android 16 and stemmed from a newly introduced QUIC connection teardown feature in Android’s networking stack. In its latest release, GrapheneOS says it has “disable[d] registerQuicConnectionClosePayload optimization to fix VPN leak,” effectively neutralizing the attack vector on supported Pixel devices.
GrapheneOS is a privacy- and security-focused Android-based operating system primarily developed for Google Pixel devices. The project is widely used by privacy-conscious consumers, journalists, activists, and enterprise users seeking stronger application sandboxing, exploit mitigations, and reduced reliance on Google services.
According to Yusuf’s technical write-up, the vulnerable API allowed ordinary applications with only the automatically granted INTERNET and ACCESS_NETWORK_STATE permissions to register arbitrary UDP payloads with system_server.
When the app’s UDP socket was later destroyed, Android’s privileged system_server process would transmit the stored payload directly over the device’s physical network interface rather than through the VPN tunnel. Because system_server operates with elevated networking privileges and is exempt from VPN routing restrictions, the packet bypassed Android’s VPN lockdown protections entirely.
The researcher demonstrated the flaw on a Pixel 8 running Android 16 with Proton VPN enabled alongside Android’s lockdown mode. The app reportedly leaked the device’s actual public IP address to a remote server despite VPN protection being fully enabled.
Google introduced a feature that allows applications to gracefully terminate QUIC sessions when sockets are unexpectedly destroyed. However, the implementation accepted arbitrary payloads without validating whether they were legitimate QUIC CONNECTION_CLOSE frames and did not verify whether the originating application was restricted to VPN-only traffic.
The researcher reported the issue to Android’s security team, which classified it as “Won’t Fix (Infeasible)” and “NSBC” (Not Security Bulletin Class), stating that it did not meet the threshold for inclusion in Android security advisories. The researcher appealed the decision, arguing that any application could leak identifying network information using only standard permissions, but Google maintained its position, authorizing public disclosure on April 29.
GrapheneOS responded by disabling the underlying optimization entirely in release 2026050400.
Beyond the VPN leak fix, the latest release also includes the full May 2026 Android security patch level, multiple hardened_malloc improvements, Linux kernel updates across Android’s 6.1, 6.6, and 6.12 branches, and a backported fix for CVE-2026-33636 in libpng. The update additionally ships newer Vanadium browser builds and expanded Dynamic Code Loading restrictions.
The researcher noted that stock Android users could temporarily mitigate the issue manually through ADB by disabling the close_quic_connection DeviceConfig flag. However, that workaround requires developer access and may not persist indefinitely if Google removes the feature flag in future updates.
Leave a Reply
```

---

## 8. Show HN: Mochi.js: bun-native high-fidelity browser automation library

- 日期: 2026-05-09 14:01
- 链接: https://mochijs.com/

```
Hi HN, I’m sharing mochi.js ( https://github.com/0xchasercat/mochi ), a Bun-native, raw-CDP browser automation framework. It's designed to make programmatic browser use more effective by focusing on consistency and measured parity with regular traffic, purely from the JS layer, against stock Chromium. The most common forms of browser automation focus heavily on client-side line by line probes, which are mostly cosmetic. This makes people feel better but it doesn't have much relevance to actual WAF or anti-automation defences. Mochi.js focuses on what actually matters, allowing you to get past captchas, WAF's and most defence mechanisms. In fact, in some cases it actually outperforms chromium forks simply by virtue of not having to lie. The foundation is built on a probe manifest based on analyzing several WAF's and trying to cover most of the ground that matters, and from there building upwards while ensuring every decision is backed by data. Solves turnstile/interstitial automatically, single digit fpjs suspect score, very good client-side results, though browserscan and a few others are known limitations that are fundamentally conflicting with what WAF's probe for. I'll be here if anyone wants to discuss the details, check out the docs and github. It's completely free and open source, MIT, strictly no relationship to any proprietary products whatsoever. No affiliation to patched chromium forks, or SaaS. But I also want to talk about why I built this, because the current paradigm of "bot detection" is fundamentally broken. Traditionally they would probably try to label my repository a malicious tool, or at best, a grey hat one. Let's take Turnstile for example, If you attach a debugger to see what data they are extracting from your hardware, their script intentionally self-destructs.
When they try to extract your data—acting as a guest on your silicon, using your electricity, without asking, the industry calls it "Security." But if you write a script to control exactly what data your own hardware emits, refusing to provide the data they have no right to ask for, you are suddenly labeled a "Malicious Actor" engaged in "Bot Evasion." I find it absurd we let ourselves put up with this, and the stance of the bot-evasion community only makes them feel more able to take a higher moral ground. I have built a library that respects my hardware's reality. If that breaks your security model, that's because your security model relies on trespassing and secrecy. I stopped apologizing. Who's next? Mochi is the exact opposite of WAF opacity. It is a glass box. It is MIT-licensed. The entire DAG, fingerprint manifest schema, harvesting process, is documented. We even commit our live benchmarks to the public record (mochi on a Linux datacenter IP scored a suspect_score: 8 and bot: not_detected against FingerprintJS Pro v4). We don't even lie unnecessarily. We default to host-OS matching. If you run mochi on a Linux server, it uses privacy-sensible fingerprints for Linux, not Windows, because Linux is a real-user signal. It proves that WAFs aren't actually blocking what most people think they are, which begs the question of what they are really doing in that obfuscated payload. The legitimacy argument is exactly how they captured the narrative. And nobody challenged it because the people on the other side were too busy acting like they were doing something wrong. Is this a conspiracy theory? For sure, but only because they allow it to be. Try make a conspiracy theory about the sticky riceball. 
 Comments URL: https://news.ycombinator.com/item?id=48075059 
 Points: 12 
 # Comments: 4
```

---

## 9. The Intolerable Hypocrisy of Cyberlibertarianism

- 日期: 2026-05-09 13:48
- 链接: https://matduggan.com/the-intolerable-hypocrisy-of-cyberlibertarianism/

```
I like the Internet. I am old enough to remember the pre-Internet era and despite the younger generations pining for those simpler days, I was there. Paper maps were absolutely horrible, just you and a compass in your car on the side of the road in the middle of the night trying to figure out where you are and where you are going. Once when driving from Michigan to Florida I got so lost in the middle of the night in Kentucky that I had to pull over to sleep and wait for the sun so I could figure out where I was. I awoke to an old man staring unblinkingly into my car, shirtless, breathing heavy enough to fog the windows. To say I floored that 1991 Honda Civic is an understatement.
You would leave your house and then just disappear. This is presented as kind of romantic now, as if we were just free spirits on the wind and could stop and really watch a sunset. In practice it was mostly an annoying game of attempting to guess where people were. You'd call their job, they had left. You'd call their house, they weren't home yet. Presumably they were in transit but you actually had no idea. As a child my response to people asking me where my parents were was often a shrug as I resumed attempting to eat my weight in shoplifted candy or make homemade napalm with gasoline and styrofoam. Sometimes I shudder as a parent remembering how young I was putting pennies on train tracks and hiding dangerously close so that we could get the cool squished penny afterwards.
Cassettes are the worst way to listen to music ever invented. Tapes squealed. Tapes slowed down for no reason, like they were depressed. Multiple times in my life I would set off on a long road trip, pop in a tape, and within fifteen minutes watch as it shot from the deck unspooled like the guts from the tauntaun in Star Wars. You'd then spend forty-five minutes at a Sunoco trying to wind it back in with a Bic pen knowing in your heart you were performing CPR on a corpse. Then you'd put it back in the player out of pure stubbornness, and it would chew itself again immediately, and you'd drive the next six hours in silence with your own thoughts, which were not as good as Pearl Jam.
So I am, mostly, grateful for the bounty the internet has provided. But there is something wrong, deeply wrong, with what we built. The wrongness was there at the start. It was baked into the foundation by people who told themselves a story about freedom, and that story was a lie, and we are all, every one of us, paying their tab.
To understand what happened we need to go back to the 90s.
A Declaration of the Independence of Cyberspace
One of the first and most classic examples of the ideology that powered and continues to power tech is the classic "A Declaration of the Independence of Cyberspace" by John Perry Barlow written in 1996. You can find the full text here. I remember thinking it was genius when I first read it. I was young enough that I also thought "Snow Crash" was a serious political document. Today the Declaration reads like one of those sovereign citizen TikToks where someone in traffic court is claiming diplomatic immunity under maritime law.
It helps to know who Barlow was. Barlow was a Grateful Dead lyricist. He was also a Wyoming cattle rancher. He was also, briefly, the campaign manager for Dick Cheney's first run for Congress. (You did not misread that.) He spent his later years as a fixture at Davos, the World Economic Forum, where the very wealthy gather each January to remind each other that they are interesting. It was at Davos, in February 1996, fueled by champagne and grievance over the Telecommunications Act, that Barlow banged out the Declaration on a laptop and emailed it to a few hundred friends. From there it became, somehow, one of the founding documents of the modern internet.
These increasingly hostile and colonial measures place us in the same position as those previous lovers of freedom and self-determination who had to reject the authorities of distant, uninformed powers. We must declare our virtual selves immune to your sovereignty, even as we continue to consent to your rule over our bodies. We will spread ourselves across the Planet so that no one can arrest our thoughts.
Many of the pillars of "modern Internet" are here. Identity isn't a fixed concept based on government ID but is a more fluid concept. We don't need centralized control or really any form of control because those things are unnecessary. It was this and the famous earlier "Cyberspace and the American Dream: A Magna
Carta for the Knowledge Age" that laid a familiar foundation for a lot of the culture we now have. [link]
The Magna Carta is also our introduction to the (now familiar) creed of "catch up or get left behind". The adoption of new technology must be done at the absolute fastest speed possible with no regulations or checks. You don't need to worry about the consequences of technology because these problems correct themselves. If you told me the following was written two weeks ago by OpenAI I would have believed you.
If this analysis is correct, copyright and patent protection of knowledge (or at least many forms of it) may no longer be unnecessary. In fact, the marketplace may already be creating vehicles to compensate creators of customized knowledge outside the cumbersome copyright/patent process
The cumbersome copyright/patent process. Cumbersome to whom, exactly? This is always the move. The thing your industry would prefer not to deal with is reframed as an obsolete burden. Your refusal to do it is rebranded as innovation. Your inability to imagine a world where you don't get exactly what you want becomes a manifesto.
Winner Saw It Coming
So there are dozens of these pieces and they all read the same. If you don't regulate these technologies humanity will only benefit. Education, healthcare, industry, etc. We don't need regulations because the transformation from the medium of paper to digital has transformed the human spirit. But one was extremely surprising to me. Langdon Winner wrote something almost prophetic back in 1997. You can read it here.
He coins the term cyberlibertarianism (or at least is the first mention of it I could find) and then goes on to describe an almost eerily accurate set of events.
In this perspective, the dynamism of digital technology is our true destiny. There is no time to pause, reflect or ask for more influence in shaping these developments. Enormous feats of quick adaptation are required of all of us just to respond to the
requirements the new technology casts upon us each day. In the writings of cyberlibertarians those able to rise to the challenge are the champions of the coming millennium. The rest are fated to languish in the dust.
Characteristic of this way of thinking is a tendency to conflate
the activities of freedom seeking individuals with the operations
of enormous, profit seeking business firms. In the Magna Carta
for the Knowledge Age, concepts of rights, freedoms, access, and
ownership justified as appropriate to individuals are marshaled
to support the machinations of enormous transnational firms.
We must recognize, the manifesto argues, that "Government does
not own cyberspace, the people do." One might read this as a
suggestion that cyberspace is a commons in which people have
shared rights and responsibilities. But that is definitely not where
the writers carry their reasoning.
What "ownership by the people" means, the Magna Carta
insists, is simply "private ownership." And it eventually becomes
clear that the private entities they have in mind are actually large,
transnational business firms, especially those in communications.
Thus, after praising the market competition as the pathway to a
better society, the authors announce that some forms of compe-
tition are distinctly unwelcome. In fact, the writers fear that the
government will regulate in a way that requires cable companies
and phone companies to compete. Needed instead, they argue,
is the reduction of barriers to collaboration of already large firms,
a step that will encourage the creation of a huge, commercial,
interactive multimedia network as the formerly separate kinds of
communication merge.
In all he lays out 4 pillars of this ideology.
Technological determinism. The new technology is going to transform everything, it cannot be stopped, and your only job is to keep up. Stewart Brand's actual quote, which Winner pulls out and lets sit there like a body on display, is "Technology is rapidly accelerating and you have to keep up." There's no room to ask whether we want any of this. The wave is coming. Surf or drown.
It does not occur to anyone in this discourse that 'drown' is a choice the wave is making, not a natural law. Waves do not have intentions. Destroying your livelihood and leaving you to rot isn't a requirement of the natural order as much as that would convenient.
Radical individualism. The point of all this technology is personal liberation. Anything that gets in the way of the individual maximizing themselves be it government, regulation, social obligation, your annoying neighbors, is an obstacle to be removed. Winner notes, with what I imagine was a very dry expression, that the writers of the "Magna Carta for the Knowledge Age" cited Ayn Rand approvingly. In 1994. As intellectual grounding. For a document about computers.
There is something deeply funny about a movement claiming to invent the future and grounding its case in a Russian émigré's airport novels about steel barons in love with their own reflections.
Free-market absolutism. Specifically the Milton Friedman, Chicago School, supply-side flavor. The market will sort it out. Regulation is theft. Wealth is virtue. George Gilder, who co-wrote the Magna Carta, had previously written a book called Wealth and Poverty that helped sell Reaganomics to the masses. He then wrote Microcosm, which argued that microprocessors plus deregulated capitalism would liberate humanity. He was very serious about this.
Don't worry, Gilder is still out there. He loves the blockchain and crypto now. He now writes about how Bitcoin will save the soul of capitalism, which it is somehow doing while also destroying the planet. Both can be true in his cosmology. The ideology is flexible like that.
A fantasy of communitarian outcomes. This is the part that should make you laugh out loud. After establishing that government is bad, regulation is theft, and the individual is sovereign, the cyberlibertarians then promise that the result of all this will be... rich, decentralized, harmonious community life. Negroponte: "It can flatten organizations, globalize society, decentralize control, and help harmonize people." Democracy will flourish. The gap between rich and poor will close. The lion will lie down with the lamb, and the lamb will have a Pentium II.
We also have the advantage of hindsight and know, without question, that all of these predicted outcomes were wrong. Not 'directionally wrong' or 'wrong in the details.' Wrong the way it would be wrong to predict that if you set your kitchen on fire, the result will be a renovation.
You have to hold these four ideas in your head at the same time to see the trick. The cyberlibertarians wanted you to believe that radical individualism plus deregulated capitalism plus inevitable technology would produce communitarian utopia. This is, on its face, insane. It is the economic equivalent of claiming that if everyone punches each other really hard, eventually we'll all be hugging.
But Winner's sharpest observation, the one I keep coming back to, isn't about any of the four pillars individually. It's about the move underneath them. He writes:
"Characteristic of this way of thinking is a tendency to conflate the activities of freedom seeking individuals with the operations of enormous, profit seeking business firms."
This is the entire game. This is how "don't tread on me" becomes "Meta should be allowed to do whatever it wants." This is how the rights of the lone hacker working in their garage become indistinguishable from the rights of a multinational with a market cap larger than most countries' GDP. The Magna Carta literally argues that the government should reduce barriers to collaboration between cable companies and phone companies in the name of individual freedom and social equality. Winner caught this in 1997.
That is why obstructing such collaboration – in the cause of forcing a competition
between the cable and phone industries – is socially elitist. To the extent it prevents collaboration between the cable industry and the phone companies, present federal policy actually thwarts the Administration's own goals of access and empowerment.
What makes the essay uncomfortable to read now is that Winner wasn't even predicting the future. He was just describing what was already happening and noting where it would obviously lead. He saw the media mergers and asked the question nobody in the industry wanted to answer: what happened to the predicted collapse of large centralized structures in the age of electronic media? Where, exactly, did the decentralization go? He saw that the cyberlibertarians were going to deliver the opposite of everything they promised, and that they were going to keep getting paid to promise it anyway.
He was writing before Google. Before Facebook. Before the iPhone. Before YouTube. Before Twitter, Bitcoin, Uber, AirBnB, OpenAI, and the entire app economy. Before any of the actual examples that would eventually prove him right existed. He just looked at the people doing the talking, listened to what they were saying, and wrote down where it ended. It is not a long essay. He didn't need a long essay. The future was right there on the page, in their own words. He just had to read it back to them.
The essay closes with a question that has, to my knowledge, never been seriously answered by the industry it was aimed at:
"Are the practices, relationships and institutions affected by people's involvement with networked computing ones we wish to foster? Or are they ones we must try to modify or even oppose?"
Twenty-eight years later, the industry still treats this question as somewhere between naive and seditious. It's the question Barlow's declaration was specifically designed to make unaskable. And it remains, to this day, the only question that actually matters.
Caveat emptor
When you look at these early formative writings, so much of what we see now becomes clear. The cyberlibertarian deal was always the same: you're on your own. The industry would build the infrastructure, take the profits, and shove every consequence, every harm, every cost, every responsibility, onto somebody else.
There is no greater example to me than the moderator. Anyone who has ever moderated a forum or a subreddit knows that adding the word "cyber" to a space doesn't suddenly turn people into better humans. People are still people. They flame each other, they post slurs, they doxx, they harass, they spam, they post CSAM, they radicalize each other, they grief, they coordinate, they lie. A space with humans in it requires governance.
They produce, with frightening regularity, the exact behavior any kindergarten teacher could have predicted. Then they act surprised.
But the cyberlibertarian model required pretending it was unforeseeable. The platforms couldn't acknowledge that they needed governance because acknowledging it would mean acknowledging responsibility, and acknowledging responsibility would mean acknowledging liability, and acknowledging liability would mean the entire economic model collapses. So instead the industry invented a beautiful fiction: governance happens, but it happens by magic, performed by volunteers, for free, who we will simultaneously rely on and mock.
Reddit is run by unpaid moderators. Wikipedia is run by unpaid editors. Stack Overflow was run by unpaid experts and is now a ghost town. On TikTok and Twitter it is the unknowable "algorithm" that is the cause of and solution to every problem backed by capricious moderators who delight in stopping free speech. Unless you don't like it, then it's negligence moderation in defense of your enemies.
Open source is run by unpaid maintainers having nervous breakdowns. The platforms collect the rent. The people doing the actual work of making the platforms livable get nothing, and when they ask for anything like recognition, tools, basic protection from harassment, they're told they're power-tripping nerds who should touch grass.
This is also the crypto story, just with the masks off. What if we made worse money on purpose, money that bypassed every protection consumers had won over the previous century, money that couldn't be reversed when stolen, money that funded ransomware attacks on hospitals and pump-and-dumps targeting people's retirement accounts? The cyberlibertarian answer was: that's freedom. The losses were real. People killed themselves. Hospitals had to turn away patients. The architects became billionaires and bought yachts and now sit on the boards of AI companies, where they are reinventing the same con with a new vocabulary.
Now Winner got one thing wrong, and it's worth pausing on, because it's the most interesting wrinkle in all of this. What actually happened was weirder and worse. The cyberlibertarians became the corporations. They didn't sell out. They didn't betray their principles for the first offer of money. They simply scaled until their principles became inconvenient, and then they stopped mentioning them.
Once the platforms got large enough to be unstoppable, once they captured enough of the regulatory apparatus to write their own rules, the libertarian rhetoric got quietly shelved like a college poster you took down before your in-laws came over. Meta no longer pretends it stands for free speech and seemingly takes delight in putting its thumb on the scale. TikTok users have invented an entire euphemistic shadow language to evade automated censorship like "unalive," "le dollar bean," "graped" that would have made 1996 Barlow weep into his bolo tie.
Copyright and patents matter when they're Apple's copyright and patents. Or Googles. Or OpenAIs. Go try to make a Facebook+ website and see how quickly Meta is capable of responding to content it finds objectionable.
Cyberlibertarianism was the ladder. Once they were on the roof, they kicked it away and started charging admission to look at the view.
So the Internet is Doomed?
Remember I like the Internet. I said it in the beginning and it is still true. I love the Fediverse, I love weird Discords about small tabletop RPGs I'm in. I spend hours in the Mister FPGA forums. There are corners that are good. But they're mostly good because they're not big enough to be worth breaking up.
It feels increasingly like I'm hanging out in the old neighborhood dive bar after most of the regulars have moved away. The lighting is the same. The bartender remembers your order. But you can hear yourself think now, and that's mostly because the room is half empty and the jukebox finally died. The new clientele is from out of town. They are taking pictures of the menu.
If we want to have a serious conversation about why we are in the situation we're in, it is no longer possible to pretend that the broken ideology that put us on this trajectory is still somehow compatible with the harsh realities that surround us. It is not clear to me if democracy can survive a deregulated Internet. A deregulated Internet filled with LLMs that can perfectly impersonate human beings powered by unregulated corporations with zero ethical guidelines seems like a somewhat obvious problem. Like an episode of Star Trek where you the viewer are like "well clearly the Zorkians can't keep the Killbots as pets." It doesn't take some giant intellect to see the pretty fucking obvious problem.
If we want to save the parts of the internet worth saving, we have to evolve. We have to find some sort of ethical code that says: just because I can do something and it makes money, that is not sufficient justification to unleash it on the world. Or, more simply: just because I want to do something and you cannot actively stop me, that does not make doing it a good idea. We have waited thirty years for the cyberlibertarian future to arrive and produce the promised harmonious community. It's time to face the facts. It's never coming. The bus left in 1996. The bus was never real.
People did not get better because they went online. Giving everyone access to a raw, unfiltered pipeline of every fact and lie ever produced did not turn them into better-educated people. It broke them. It allowed them to choose the reality they now inhabit, like ordering off a menu. If I want to believe the world is flat, TikTok will gladly serve me that content all day. Meta will recommend supportive groups. There will be hashtags. There will be Discords. There will be a guy named Trent who runs a podcast. I will never have to face the deeply uncomfortable possibility that I might be wrong about anything, ever, until the day I die, surrounded by people who agree with me about everything, including which of the other mourners are secretly lizards.
That is the internet we built. It was not an accident. It was the product of a specific ideology, written down by specific people, at a specific cocktail party in Davos, in 1996. Winner watched it happen and told us where it was going. We did not listen. There is still time, maybe, to start.
```

---

## 10. Read Programming as Theory Building

- 日期: 2026-05-09 13:31
- 链接: https://codeutopia.net/blog/2026/05/09/you-should-read-programming-as-theory-building/

```
When I finished reading Peter Naur’s Programming as Theory Building my first thought was “How come nobody ever told me to read this?” I ended up reading it multiple times, as I attempted to collect my thoughts on why it makes so much sense.
Have you ever had a situation where you’re trying to explain something or say something, and you’re looking for a suitable word or term, but no matter how much you look for it, you can’t find it? I think Naur’s “theory” is that term when it comes to writing good code and creating maintainable software. I’ve had many ideas and thoughts on those topics, but they were all disparate concepts, which even when grouped together didn’t really answer the question “why is writing good software hard?” Viewing programming as “theory building”, as Naur puts it, is the missing piece that pulls all of it together and answers the question.
In summary, Programming as Theory Building suggests that the program code, documentation and other products are secondary to what programming really is about: Building an understanding, or a mental model, of the program, its requirements, and how they relate to everything around it. That is, your primary goal as a programmer is to learn, understand, retain, improve and share this “theory” of the program.
If you think of things like “good code” or “maintainable code”, what is it that comes to mind? It’s probably things that make code easier to understand, like following good conventions, writing “clean” code, having a good architecture, and so on. You might also think of documentation and diagrams. Perhaps automated tests.
If you think about it, the goal with everything that relates to writing maintainable code is actually about communicating the design intention of the code. You write clean code because it’s easy to understand what it does, you architect code so it’s easy to understand its structure and purpose of the structure, you add documentation to help explain what the code does, and draw diagrams for similar purposes as well. But at least in my experience, developers treat the different aspects of this as separate activities - eg. writing tests is its own activity with its own goals, writing documentation is its own activity, and so forth.
If you look at programming as theory building in the way Naur suggests, you can see these activities as part of a larger whole: Communicating the theory of the program. When seen as part of a larger whole, you can start using the separate activities to achieve the shared goal better. And communicating the theory of the program is important: If you try to modify a program without having an understanding of the theory, you won’t be able to do it in a way that isn’t hacky. Similarly, if you need to evaluate the feasibility of some change to the code, such as a new feature, you cannot do this unless you have an understanding of the theory.
In this sense, programming is theory building.
If you think of it in this way, suddenly many more things connect together. For example, what do design patterns and Domain-Driven Design have in common? They help you communicate ideas and mental models used in your code - that is, they help communicate the theory of the program. Similarly, others have suggested concepts like Intellectual Control - having a mental model of the program, allowing you to confirm it works correctly, and reason about changes to it and so forth - which could also be seen as a form of “theory building”.
Hopefully I’ve managed to convey at least some of the value of reading Peter Naur’s essay. There’s more to it, so I highly recommend reading the original “Programming as Theory Building” text. It isn’t too long, and you can find it pretty easily on Google - I would link it, but it’s a bit of a gray area copyright-wise, and I’d have to deep link it from someone’s website. If you have read it, I’d love to hear your thoughts on it.
Comments or questions?
If you have any comments or questions about this post, feel free to email me to jani@codeutopia.net, or use any of the other methods on the contact page.
```

---

## 11. Internet Archive Switzerland

- 日期: 2026-05-09 12:00
- 链接: https://internetarchive.ch/

```
Welcome
Welcome to
Internet Archive Switzerland.
Universal Access to ALL Knowledge.
Internet Archive Switzerland is an independent Swiss foundation, which is operating as an non-profit organisation based in Sankt Gallen. Our primary goal is: Universal Access to All Knowledge.
Together with like-minded partners we collect and preserve digital information for learning and research. Our objective is to ensure people can find any kind of helpful digital materials, today and in the future.
Although at first glance one might think that the digital content available on the internet is inexhaustible and endlessly growing, it is also evident that digital information is actually short-lived.
We are facing constant changes in file formats, sudden failure of storage media, rapid deletion processes (accidental or deliberate) and an increasing tendency of hiding knowledge behind paywalls. All of this jeopardises easy access to information, learning and the shaping of opinions on the basis of facts.
All of this has led us to launch two initiatives in the foundation’s early stages: We are partnering with the University of St. Gallen to build the Gen Artificial Intelligence (AI) Archive, preserving today's AI models for future generations. And through our Endangered Archives initiative, we invite global partners to explore ways of rescuing vulnerable collections from conflict, disaster, and suppression before they are lost.
Projects
What we are WORKING on.
Project 01 · Research
Gen AI Archive
Artificial Intelligence, Generative AI, and Large Language Models (LLMs) are fundamentally reshaping how humanity creates and shares knowledge. To document this evolution, the University of St. Gallen and Internet Archive Switzerland partner in preserving today’s most profound models for future generations in the Gen AI Archive.
Project 02 · Preservation
Endangered Archives
Cultural heritage and historical records worldwide face ever growing threats from conflict, instability, and natural disasters. To prevent the loss of this collective memory, Internet Archive Switzerland seeks to establish an initiative called Endangered Archives. In cooperation with UNESCO and other well established organisations we aim to rescue vulnerable materials by providing a secure digital haven.
About
The foundation.
Organization
An independent non profit foundation in St. Gallen, Switzerland. Mission-aligned with the Internet Archive, Internet Archive Canada and Internet Archive Europe, and a common goal: Universal Access to All Knowledge.
Our charter states (excerpt): “The purpose of the Foundation is to advance the preservation and universal accessibility of all knowledge as inspired by the United Nations Universal Declaration of Human Rights (Articles 19, 26, and 27) and the United Nations's Sustainable Development Goal 4, which strives to ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.
Executive Director
Roman Griesfelder
Internet Archive Switzerland is led by Roman Griesfelder as Executive Director. Roman is an Austrian citizen and has been living in Switzerland since 1998. The sociologist and business administrator has been working for many years in senior roles as project manager and management consultant, among other things, before holding leading positions at cultural institutions in Switzerland. His wide-ranging interests converge at the points where social, cultural and technological developments intersect and affect the lives of many people, or even just a few individuals.
Location
St. Gallen.
47.4245° N · 9.3767° E
St. Gallen is no stranger to the idea that preserving the record is a form of civic responsibility. Its archival tradition stretches back over a thousand years — a fitting symbolic home for this new chapter of the Internet Archive.
The existence of the Abbey Archives proves that, with conviction and perseverance, it is possible to preserve the foundations of our knowledge about society. This conviction motivates the Internet Archive Switzerland to embark boldly on its mission and to pursue it unwaveringly.
We are also delighted to be partnering with the University of St. Gallen to establish the world’s first comprehensive AI archive.
Blog
Latest NEWS.
-
• 5 minutes of reading
Internet Archive Switzerland Launches in St. Gallen
A Thousand Years of Memory, and a New Chapter
Read more: Internet Archive Switzerland Launches in St. GallenOn May 5th, 2026, Internet Archive Switzerland celebrates its launch at the exhibition hall of the Abbey Archives of St. Gallen, one of the oldest continuously active archives in the world. We are grateful to Peter Erhart and the Abbey Archives of St. Gallen for hosting us: two institutions, one a millennium old and one…
Partners
Working TOGETHER.
Contact
PLEASE GET IN TOUCH!
Researchers, libraries, developers, curious citizens: write to us in St. Gallen.
We want to hear from you. Whether you know of a collection at risk, want to explore a partnership, or simply believe that open access to knowledge matters, reach out. Every conversation helps us do this work better.
Address
Internet Archive Switzerland
c/o St. Galler Stiftung für internationale Studien
Dufourstrasse 83
9000 St. Gallen
CHE-238.343.099
```

---

## 12. Killswitch: Per-function short-circuit mitigation primitive

- 日期: 2026-05-09 09:14
- 链接: https://lwn.net/ml/all/20260507070547.2268452-1-sashal@kernel.org/

```
Article URL: https://lwn.net/ml/all/20260507070547.2268452-1-sashal@kernel.org/ 
 Comments URL: https://news.ycombinator.com/item?id=48073394 
 Points: 63 
 # Comments: 14
```

---

## 13. LLMs Corrupt Your Documents When You Delegate

- 日期: 2026-05-09 08:44
- 链接: https://arxiv.org/abs/2604.15597

```
Computer Science > Computation and Language
[Submitted on 17 Apr 2026]
Title:LLMs Corrupt Your Documents When You Delegate
View PDF HTML (experimental)Abstract:Large Language Models (LLMs) are poised to disrupt knowledge work, with the emergence of delegated work as a new interaction paradigm (e.g., vibe coding). Delegation requires trust - the expectation that the LLM will faithfully execute the task without introducing errors into documents. We introduce DELEGATE-52 to study the readiness of AI systems in delegated workflows. DELEGATE-52 simulates long delegated workflows that require in-depth document editing across 52 professional domains, such as coding, crystallography, and music notation. Our large-scale experiment with 19 LLMs reveals that current models degrade documents during delegation: even frontier models (Gemini 3.1 Pro, Claude 4.6 Opus, GPT 5.4) corrupt an average of 25% of document content by the end of long workflows, with other models failing more severely. Additional experiments reveal that agentic tool use does not improve performance on DELEGATE-52, and that degradation severity is exacerbated by document size, length of interaction, or presence of distractor files. Our analysis shows that current LLMs are unreliable delegates: they introduce sparse but severe errors that silently corrupt documents, compounding over long interaction.
References & Citations
Loading...
Bibliographic and Citation Tools
Bibliographic Explorer (What is the Explorer?)
Connected Papers (What is Connected Papers?)
Litmaps (What is Litmaps?)
scite Smart Citations (What are Smart Citations?)
Code, Data and Media Associated with this Article
alphaXiv (What is alphaXiv?)
CatalyzeX Code Finder for Papers (What is CatalyzeX?)
DagsHub (What is DagsHub?)
Gotit.pub (What is GotitPub?)
Hugging Face (What is Huggingface?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
```

---

## 14. Using Claude Code: The unreasonable effectiveness of HTML

- 日期: 2026-05-09 04:53
- 链接: https://twitter.com/trq212/status/2052809885763747935

```
We’ve detected that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.
Help Center
Terms of Service Privacy Policy Cookie Policy Imprint Ads info © 2026 X Corp.
```

---

## 15. A recent experience with ChatGPT 5.5 Pro

- 日期: 2026-05-09 02:41
- 链接: https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/

```
We are all having to keep revising upwards our assessments of the mathematical capabilities of large language models. I have just made a fairly large revision as a result of ChatGPT 5.5 Pro, to which I am fortunate to have been given access, producing a piece of PhD-level research in an hour or so, with no serious mathematical input from me.
The background is that, as has been widely reported, LLMs are now capable of solving research-level problems, and have managed to solve several of the Erdős problems listed on Thomas Bloom’s wonderful website. Initially it was possible to laugh this off: many of the “solutions” consisted in the LLM noticing that the problem had an answer sitting there in the literature already, or could be very easily deduced from known results. But little by little the laughter has become quieter. The message I am getting from what other mathematicians more involved in this enterprise have been saying is that LLMs have got to the point where if a problem has an easy argument that for one reason or another human mathematicians have missed (that reason sometimes, but not always, being that the problem has not received all that much attention), then there is a good chance that the LLMs will spot it. Conversely, for problems where one’s initial reaction is to be impressed that an LLM has come up with a clever argument, it often turns out on closer inspection that there are precedents for those arguments, so it is still just about possible to comfort oneself that LLMs are merely putting together existing knowledge rather than having truly original ideas. How much of a comfort that is I will not discuss here, other than to note that quite a lot of perfectly good human mathematics consists in putting together existing knowledge and proof techniques.
I decided to try something a little bit different. At least in combinatorics, there are quite a lot of papers that investigate some relatively new combinatorial parameter that leads naturally to several questions. Because of the sheer number of questions one can ask, the authors of such papers will not necessarily have the time to spend a week or two thinking about each one, so there is a decent probability that at least some of them will not be all that hard. This makes such papers very valuable as sources of problems for mathematicians who are doing research for the first time and who will be hugely encouraged by solving a problem that was officially open. Or rather, it used to make them valuable in that way, but it looks as though the bar has just been raised. It is no longer enough that somebody asks a problem: it needs to be hard enough for an LLM not to be able to solve it.
In any case, a little over a week ago I decided to see how ChatGPT 5.5 Pro would fare with a selection of problems asked by Mel Nathanson in a paper entitled Diversity, Equity and Inclusion for Problems in Additive Number Theory. Nathanson has a remarkable record of being interested in problems and theorems that have later become extremely fashionable, which has led him to write a series of extremely well timed and therefore highly influential textbooks. In this paper, he argues for the interest of several other problems, some of which I will now briefly describe.
If is a set of integers, then its sumset is defined to be . For a positive integer , the –fold sumset, denoted , is defined to be . Nathanson is interested in the possible sizes of given the size of . To that end one can define a set to be the set of all such that there exists a set with and .
An obvious first question to ask is simply “What is ?” When , the answer is the set of all integers between and . It is an easy exercise to show that if , then , so this result is saying that all sizes in between can be realized. However, it is not true in general that can take every size between its minimum and maximum possibilities, and we do not currently have a complete description of .
Another natural question one can ask, and this is where ChatGPT came in, is how large a diameter you need if you want a set with and having prescribed sizes. (Of course, the size of must belong to .) Nathanson showed that for every there is a subset of with and , and asked whether the bound could be improved. ChatGPT 5.5 Pro thought for 17 minutes and 5 seconds before providing a construction that yielded a quadratic upper bound, which is clearly best possible. It wrote up its argument in a slightly rambling LLM-ish style, so I asked if it could write the argument up as a LaTeX file in the style of a typical mathematical preprint. After two minutes and 23 seconds it gave me that, after which I spent some time convincing myself that the argument was correct.
The basic idea behind both Nathanson’s argument and ChatGPT’s was that in order to obtain a set of a given size with a sumset of a given size, it is useful to build it out of a Sidon set, which means a set with sumset of maximal size (that is not quite the usual definition but it is the simplest to use in this discussion), and an arithmetic progression. Also, for a bit of fine tuning one can take an additional point near the arithmetic progression. Then if one plays around with the various parameters, one finds that one can obtain sets of all the sizes one wants. Nathanson doesn’t express his argument this way (it is Theorem 5 of this paper), instead giving an inductive argument, but I think, without having checked too carefully, that if one unravels his argument, one finds that effectively that is what he ends up with, and the Sidon set in question consists of powers of 2. ChatGPT obtained its improvement by simply using a more efficient Sidon set — it is well known that one can find Sidon sets of quadratic diameter. (One might ask why Nathanson didn’t do that in the first place: I think it is because the obvious idea of using a more efficient Sidon set becomes obvious only after one has redescribed his inductive construction. Is that what ChatGPT did? It is very hard to say.)
Next, I asked ChatGPT to see whether it could do the same for a closely related question, where instead of looking at the size of the sumset, one looks at the size of the restricted sumset, which is defined to be . Unsurprisingly, it was able to do that with no trouble at all. I got it to write both results up in a single note, to avoid a certain amount of duplication. If you are curious, you can see the note here.
I then asked what it could do for general . I was much less optimistic that it would manage to do anything interesting, because the proof for makes fundamental use of the fact (due to Erdős and Szemerédi) that we know exactly which sizes we need to create. If we don’t know what the set is, then it seems that we are forced to start with a hypothetical set with and and build out of it a set of small diameter with the same property. As it happens, I still don’t know how to get round that difficulty (I’m mentioning that just to demonstrate that my mathematical input was zero, and I didn’t even do anything clever with the prompts), but Nathanson mentioned in his paper a remarkable paper of Isaac Rajagopal, a student at MIT, who must have got round the difficulty somehow, because he had managed to prove an exponential dependence of on for each fixed .
I’ll leave the previous paragraph there, but Isaac has subsequently explained to me that that isn’t really the difficulty. His argument gives a complete description of when is sufficiently large, and if one wants to prove a polynomial dependence for fixed , then assuming that is sufficiently large is clearly permitted. The real difficulty is that constructing the sets with given sumset sizes was significantly more complicated, and necessarily so because the degree of the polynomial grows with , and one therefore needs more and more parameters to define the sets.
In any case, the task faced by ChatGPT was not to solve the problem from scratch, but to see whether it was possible to tighten up Isaac Rajagopal’s argument. Here’s what happened.
- After 16 minutes and 41 seconds, it came back with an argument that claimed to have improved the upper bound from exponential in to exponential in for any .
- I asked it to write that in preprint form too, which took it a further 47 minutes and 39 seconds.
- That preprint would have been hard for me to read, as that would have meant carefully reading Rajagopal’s paper first, but I sent it to Nathanson, who forwarded it to Rajagopal, who said he thought it looked correct.
- Both ChatGPT and Rajagopal speculated a little on what might need to be done to push things further and get a polynomial bound, so I got greedy and asked ChatGPT to give that a go.
- After 13 minutes and 33 seconds it told me it felt optimistic about the existence of such an argument but there were a couple of technical statements that needed checking.
- I asked it to check them.
- After 9 minutes and 12 seconds it got back to me with the check having been done, so I asked for this too to be written in preprint form.
- After 31 minutes and 40 seconds the “preprint” was ready. Here it is.
- Isaac Rajagopal looked at it and declared it to be almost certainly correct. It was clear that he meant this not just at a line-by-line level but at the level of ideas.
Isaac made some very interesting remarks about the nature of what the additional ideas were that ChatGPT contributed. Since, as I have already said, my mathematical input was zero, I invited him to write a guest section to this post. Just before we get to that, I want to raise a question (that will undoubtedly have been raised by others as well), which is simple: what should we do with this kind of content? Had the result been produced by a human mathematician, it would definitely have been publishable, so I think it would be wrong to describe it as AI slop. On the other hand, it seems pointless even to think about putting it in a journal, since it can be made freely available, and nobody needs “credit” for it (except that Isaac deserves plenty of credit for creating the framework on which ChatGPT could build). I understand that arXiv has a policy against accepting AI-written content, which makes good sense to me. So maybe there should be a different repository where AI-produced results can live. But various decisions would need to be made about how it was organized. I myself think that one would probably want to have some kind of moderation process, so that results would be included only if a human mathematician was prepared to certify that they were correct — or, better still, that they had been formalized by a proof assistant — and perhaps also that they answered a question that had been asked in a human-written paper. On the other hand, I wouldn’t want a moderation process that created vast amounts of work (unless the work was itself done by AI, but there are obvious dangers in going down that route). Anyway, until these questions are answered, this result is available from the link above, and perhaps, now that LLMs are so good at literature search, that will be enough to make it findable by anyone who wants to know whether Nathanson’s problem has been solved.
Isaac’s evaluation of what ChatGPT achieved
With just a few prompts, ChatGPT was able to improve the upper bound on (which I will define very soon) from exponential in to polynomial in . While its first improvement of the bound, from exponential in to exponential in , was a routine modification of my work, the improvement to polynomial in is quite impressive. To do this, ChatGPT came up with an idea which is original and clever. It is the sort of idea I would be very proud to come up with after a week or two of pondering, and it took ChatGPT less than an hour to find and prove, using similar methods to those in my own proof. My goal is to explain that idea, in a manner that will be digestible to my friends who are computer science majors as well as my math major friends.
The problem of bounding is closely related to a problem I worked on at the Duluth REU (Research Experience for Undergrads) program, of determining . In particular, is the set of possible -fold sumset sizes , where can be chosen to be any set of integers. is the minimal such that we can achieve all of the values of using -element sets . I spent last summer explicitly characterizing the set for large , by constructing sets such that achieves all sizes which I could not rule out as impossible. So, can be upper-bounded by optimizing my constructions.
I constructed these sets by combining smaller component sets which are simpler to analyze. Some of these components are the geometric series
for various values of and . Unfortunately, the elements of and are exponentially large in terms of . So, I asked ChatGPT (through Tim) whether there exist sets of elements which have similar sumset sizes to these geometric series, but contain only numbers of polynomial size in : I had no idea if this was possible, or how to begin constructing such sets. ChatGPT came back with an answer, constructing sets and which behave like “half a geometric series squeezed into a polynomial interval,” which is counterintuitive. Before I discuss the construction of and , I will explain the important properties of the sumset sizes of and which they recreate.
For , a set is called a set if the only solutions to
with in are the “trivial” solutions, by which I mean that one side of the equation is a reordering of the other side. If is a set of size , then elements of correspond exactly to choices of elements of , with repetition allowed. Using “stars and bars,” one can see that and this is the maximum possible value of among sets of size . So, another definition is that is a set if . Sidon sets, which Tim discussed, are exactly sets.
To make things more concrete, let us assume that in (1). Then, is a set, but it is not a set because of the relations
for any choice of in . In particular, , as these relations are the only ones preventing from being a set. lacks the relations in (2) because is not in . So, is a set, but it is not a set because of the relations
for any choices of in . This gives relations, and one can check that . To summarize, we have seen that
(a) is a set.
(b) is a linear function of .
(c) is a set.
(d) is a quadratic function of .
ChatGPT was able to find sets and of elements which satisfy (a)-(d), but whose elements all have polynomial size in . The construction of and uses -dissociated sets, which are sets where the only solutions to
with and in are the “trivial” solutions, i.e. and one side of the equation is a reordering of the other side. For , it is possible to construct an -dissociated set , where is approximately , and in particular polynomial in . Constructions of such a using finite fields date back to Singer (1938) and Bose–Chowla (1963) and are described in Appendix 1. Define
and
In hindsight, I have good intuition for the construction of and . All of the relations in (2) and (3) are formed by combining one or two relations of the form . There are approximately relations of the form in and , and approximately such relations in and . There are few other low-order relations in and , and similarly in and because is -dissociated. So, and manage to contain half as many -relations as their geometric series counterparts, while also containing few low-order relations.
We now see why (a)-(d) hold with and replaced by and , respectively. For concreteness, we assume that and , so contains no nontrivial relations as in (4) with . Then, is a set, but it is not a set because of the relations
for any choice of in . If we let , we can check that is linear in . In particular, (a) and (b) hold with replaced by , and the linear function replaced by . We can also see that is a set, but it is not a set because of the relations
for any in . If we let , we can check that is quadratic in . In a similar manner, (c) and (d) hold with replaced by , and the quadratic function replaced by .
Even though I can motivate it in retrospect, ChatGPT’s idea to use -dissociated sets to control relations of order at most feels quite ingenious. As far as I can tell, this idea is completely original.
ChatGPT’s proof that its construction produces the desired values of is very similar to my proof that the sets which I construct achieve all possible values of , after replacing and by and , respectively. Properties (a)-(d) capture many of the important properties of and (or and ) which are used in this proof. The final constructions involve combining the sets and (or and in my paper) for each value of between and with another set which is the union of an arithmetic progression and a point. Intuitively, and (or and ) have large sumsets, while arithmetic progressions have small sumsets, so it is plausible that one could get sets which achieve all the medium-sized sumsets by combining them. However, the proof of this is quite involved, and it occupies Section 4 of my paper and the entirety of the ChatGPT preprint. In Appendix 2, I work out the details of the ChatGPT construction to show that for sufficiently large,
For comparison, it is easy to see that is at least on the order of , and it is unknown what the real value is. In Appendix 3, I give details of the correspondence between my paper and the ChatGPT preprint, which will be helpful for those who want to read either.
Finally, I want to express my deep gratitude to Tim for allowing me to contribute to this blog. I am still stunned by the coincidence that the problem he chose to put into ChatGPT 5.5 Pro led him to my paper on the arXiv.
Tim on what this means for mathematical research
I would judge the level of the result that ChatGPT found in under two hours to be that of a perfectly reasonable chapter in a combinatorics PhD. It wouldn’t be considered an amazing result, since it leant very heavily on Isaac’s ideas, but it was definitely a non-trivial extension of those ideas, and for a PhD student to find that extension it would be necessary to invest quite a bit of time digesting Isaac’s paper, looking for places where it might not be optimal, familiarizing oneself with various algebraic techniques that he used, and so on.
It seems to me that training beginning PhD students to do research, which has always been hard (unless one is lucky enough, as I have often been, to have a student who just seems to get it and therefore doesn’t need in any sense to be trained), has just got harder, since one obvious way to help somebody get started is to give them a problem that looks as though it might be a relatively gentle one. If LLMs are at the point where they can solve “gentle problems”, then that is no longer an option. The lower bound for contributing to mathematics will now be to prove something that LLMs can’t prove, rather than simply to prove something that nobody has proved up to now and that at least somebody finds interesting.
I would qualify that statement in two ways though. First, there is the obvious point that a beginning PhD student has the option of using LLMs. So the task is potentially easier than proving something that LLMs can’t prove: it is proving something in collaboration with LLMs that LLMs cannot manage on their own. I have done quite a lot of such collaboration recently and found that LLMs have made useful contributions without (yet) having game-changing ideas.
A second point is that I don’t know how much of what I have said generalizes to other areas of mathematics. Combinatorics tends to be quite focused on problems: you start with a question and you reason back from the question or if you reason forwards you do so very much with the question in mind. In other areas there can be much more of an emphasis on forwards reasoning: you start with a circle of ideas and see where it leads. To do it successfully, you need to have some way of discriminating between interesting observations and uninteresting ones, and it isn’t obvious to me what LLMs would be like at that.
Of course, everything I am saying concerns LLMs as they are right now. But they are developing so fast that it seems almost certain that my comments will go out of date in a matter of months. It is also almost certain that these developments will have a profoundly disruptive effect on how we go about mathematical research, and especially on how we introduce newcomers to it. Somebody starting a PhD next academic year will be finishing it in 2029 at the earliest, and my guess is that by then what it means to undertake research in mathematics will have changed out of all recognition.
I sometimes get emails from people who are interested in doing mathematical research but are not sure whether that makes sense any more as an aspiration. I have a view on that question, but it may very well change in response to further developments. That view is that there is still a great deal of value in struggling with a mathematics problem, but that the era where you could enjoy the thrill of having your name forever associated with a particular theorem or definition may well be close to its end. So if your aim in doing mathematics is to achieve some kind of immortality, so to speak, then you should understand that that won’t necessarily be possible for much longer — not just for you, but for anybody. Here’s a thought experiment: suppose that a mathematician solved a major problem by having a long exchange with an LLM in which the mathematician played a useful guiding role but the LLM did all the technical work and had the main ideas. Would we regard that as a major achievement of the mathematician? I don’t think we would.
So what is the point of struggling with a difficult mathematics problem? One answer is that it can be very satisfying to solve a problem even if the answer is already known, but I don’t think that is a sufficient reason to spend several years of your life on this peculiar activity. A better answer is that by solving hard problems you get an insight into the problem-solving process itself, at least in your area of expertise, in a way that you simply don’t if all you do is read other people’s solutions. One consequence of this is that people who have themselves solved difficult problems are likely to be significantly better at using solving problems with the help of AI, just as very good coders are better at vibe coding than not such good coders, or people who have a solid grasp of how to do basic arithmetic are likely to be more skilled at using calculators (and especially at noticing when an answer feels off). Mathematics is a highly transferable skill, and that applies to research-level mathematics as well. By doing research in mathematics, you may not get the same rewards as your equivalents a generation ago, but there is a good chance that you will be equipping yourself very well for the world we are about to experience.
Appendix 1 (Isaac)
We will construct an -dissociated set , where is approximately . This construction is a very minor modification of Bose–Chowla (1963)’s construction of a set, which I learned about from this paper. For whatever reason, the GPT preprint (Lemma 3.1) uses a different, less efficient construction using moment curves.
Let be a prime, let , let be the finite field with elements and fix a generator of , so that is equal to . Define a set of elements
Then, each element corresponds to a unique value of , by taking . Now an additive relation of the form in (4) with can be reframed by taking powers of as
As is a degree- extension of and is a generator of as an -extension, this means that does not satisfy any nonzero polynomials in of degree . So, both sides of (6) are identical as polynomials in and thus the additive relation in (4) is trivial. So, is -dissociated, and of course one can prune a few elements to reduce to size .
Appendix 2 (Isaac)
Fix constants such that (in my paper I arbitrarily chose ). Let the two sets in (5) be called and . Let denote the set of integers satisfying . Similarly to my paper, the constructions of such that achieves the desired sizes will combine sets of the following four types:
- with choices of and .
- for each value of , with choices of .
- for each value of , with choices of .
- A set of the correct size so that .
One reason that this construction needs to be complicated is that we need to create at least many sets. To do this, we vary parameters and in the domain and parameters and in the domain . We can choose to be slightly bigger than , and then the above construction gives us different sets where can be made arbitrarily small. So, if we were to remove any of the above parameters from the construction, and not change the others, this construction would no longer create many sets. In comparison, Nathanson’s construction when only needs to create sets. He does this by combining a Sidon set, an arithmetic progression, and one extra value, and varying the size of the arithmetic progression and the extra value in ranges of size .
We want to combine sets , which are given by , for the values of , for the values of , and a set. By Appendix 1, for all , there exists a -dissociated set of diameter . By the constructions of and , we can take each , where . Let have basis vectors . To combine , we can define as
Similarly to my Lemma 4.9, this construction ensures that the generating function product holds, which is the identity that both my paper and the GPT preprint use (see either paper for a definition of these generating functions). By (the standard) Lemma 2.3 of the GPT preprint, is Freiman-isomorphic of order to a subset of . Therefore, for sufficiently large (the whole construction relies on this for the same reasons as in my paper),
Appendix 3 (Isaac)
In Section 4.2 of my paper, I use a different, simpler construction to construct sets achieving the values in which have , for some small . These sets are subsets of , meaning that all elements have polynomial size in . This is observed in Section 5 of the GPT preprint.
Section 4.3 of my paper carries out the construction which combines many components including and . This corresponds to Sections 2, 3, 4, and 6 of the GPT preprint. This section has a lot of moving parts; I give an outline in Section 4.3.1.
In Section 4.3.2, I describe how the different components will be combined, using a construction which I call the disjoint union, and introduce generating functions as a bookkeeping tool to keep track of the sumset sizes of a set . This corresponds to Section 2 and Section 4 of the GPT preprint.
In Section 4.3.3, I compute the generating function of each of the component sets, including (Lemma 4.15) and (Lemma 4.17). This corresponds to Section 3 and Section 6.1 of the GPT preprint. In particular, is computed in Lemma 3.3 and is computed in Lemma 3.4. Once these generating functions have been computed, the remainder of the proof is almost identical in my paper and in the GPT preprint.
In Section 4.3.4, I put all the pieces together to show that as we range over the sets which I have constructed, the values of will assume all of the elements of . The key idea is to show that the set of all values of forms an interval, and contains numbers both smaller than and equal to .
Tags: ai, mathematics
May 8, 2026 at 5:14 pm |
Tim, in Terry Tao’s recent talk at the Future of Mathematics symposium at Stanford, he also suggested that perhaps we ought to have different venues for AI generated mathematics versus human mathematics, making an analogy to a highway vs a pedestrian walkway: https://www.youtube.com/live/tN4hsT5t0nw?si=cIQj2Di6sNdZHr7P&t=6330
May 8, 2026 at 5:39 pm |
Very interesting post, it will be fun to look back at it in 2029. To some of your points, there’s a famous Italian quote (but not so famous that chatgpt knows who said it): “Chi meglio combina meglio crea.” The literal translation is “Who better combines better creates.” Personally I don’t think there is anything “special” in human intelligence or insight, and like you suggest I feel that a very vast amount of results in math (but also literature etc.) are “banal” in the sense that they are basically a combination of known idea; they can be obtained by tediously trying one idea after the other in the “obvious way.” Papers (in math) are often written (and talks given) to give the opposite impression of phenomenal and inexplicable deus ex machina insight of the author, but in many (most) cases the ideas can be presented in a much more pednatic way (I think you expressed a similar view that ideas always come from somewhere, with the exception of Razborov’s ;-). LLMs obviously excel at this type of combination. Personally I don’t think anyone has a clear idea of the extent to which they will be able to produce without guidance research or art that we humans are interested in, and I am open to various scenarios. What seems clear is that being able to harness these tools is already a key factor. But so far, at the high level this is not very different than Google, or mathematical software. The ability to do quick searches online or use mathematical software has been a key advantage. I’ll add that I have often wondered how to define “banality.” In some sense Kolmogorov complexity seems relevant, if something has a short description given available data, it is banal. Time-bounded Kolmogorov complexity is a better idea. One issue is how to capture “available data.” Trained LLMs seem to give us just that.
May 8, 2026 at 7:51 pm |
The question of how best to introduce beginning PhD students to research in an LLM-era feels extremely important to think about. I want to highlight that, while it’s true in theory that such students have the option of using LLMs, the top models are currently quite expensive to get access to, and there are internal models at various companies to which only a select few have access. If one goes down the route of ‘PhD students are also allowed to use LLMs’, then it can quickly become a game of ‘which student has access to the best LLMs’, which seems to me extremely unfortunate. Is it an issue that can be gotten round on a global scale?
May 8, 2026 at 7:52 pm
Sorry, I didn’t realise that was anonymous! Best wishes, Olof (Sisask)
May 9, 2026 at 5:32 am
This raises a very important issue that is relevant to all researchers, not just PhD students. Until now, unlike in most other sciences, to do research level math having access to expensive resources gave almost no advantage (except, of course, having prior access to a good education). That is gone now. I don’t know what will happen in the future, but at this moment the age of equality, in the communist sense, is sadly over in research math.
May 8, 2026 at 8:01 pm |
A quick comment to say that I’m having annoying compilation problems with LaTeX subscripts and superscripts, which have affected Isaac’s appendixes. I will try to sort them out soon, but if anyone has any idea what to do then that would be helpful.
May 9, 2026 at 5:54 am
My standard is to ask the AI (in particular ChatGPT): Write your finding/proof in texfile, also output as pdf. It works savely.
May 9, 2026 at 7:02 pm
I always use Luca Trevisan’s script to convert LaTeX files into friendly wordpress.com html files (https://lucatrevisan.wordpress.com/latex-to-wordpress/). This have some limitations though because wordpress.com LaTeX lacks some packages. Anoter option is to install one LaTeX plugin for wordpress.com (I don’t use any) because usually these allow the the use of other LaTeX packages.
May 8, 2026 at 9:13 pm |
I don’t see how this follows. If the student wants to learn, and if you as their advisor suggest it, they will refrain from using the LLM for such an exercise. This won’t produce an “equally original/publishable result” as it would have before, but it should in principle be just as educational as if the LLM didn’t exist. It doesn’t seem too different from how the student in the past would have refrained from asking you for detailed help with the same problem.
I think this depends on whether that guidance was also a significant contribution. This will sometimes be hard to judge. But if the problem had been open and interesting, and the LLMs had been generally available, for awhile, that would be evidence in favor. It seems similar to one coauthor playing an important guiding role in a joint work with another one.
May 8, 2026 at 9:17 pm |
My view on this is really pessimistic. The way things progress, the value of thinking and having deep ideas seems to be lower and lower. Even before AI, institutions questioned if mathematics research was worth it. I wouldn’t recommend anyone to start a PhD now in pure maths.
May 9, 2026 at 12:10 pm
> I wouldn’t recommend anyone to start a PhD now in pure maths.
I see it more positively, but the young candidate would need an open-minded supervisor and the courage to use AI systems full throttle. – Likely, Mathe departments should install new procedures for PhD projects.
Cheers, Ingo.
May 8, 2026 at 9:22 pm |
[…] 详情参考 […]
May 8, 2026 at 10:51 pm |
You wrote “I understand that arXiv has a policy against accepting AI-written content, which makes good sense to me. So maybe there should be a different repository where AI-produced results can live.” You may find https://arxiv.org/abs/2604.16476 a step in this direction.
May 8, 2026 at 10:54 pm |
It’s sad, but really Mathematics is just at the leading edge of a wider phenomenon. We’re going to see similar questions raised for most intellectually fulfilling activities.
May 9, 2026 at 12:25 am |
Dear Professor, Respectfully, it would be remarkable if this Chatgpt model were some evolutionary result of the (free) model I have consulted from time to time; it tells me today, when I submit a very brief source, rudimentary arithmetic, and ask for an evaluation of the conclusion, “The conclusion is unproven since, conditionally, the result of a CRT set may be smaller than one of the set of strictly positive base residues”, and sticks to its guns when challenged; the source a demonstration of an Archimedean obstruction which prevents the addition of some divisor th2 to the singleton CRT set under some divisor th1, a candidate “non Brauer Manin obstruction” (Katherine Stange); I have found a method which corrects in at least 6 cases the (free) LLMs’ mishandling of reductio arguments, but not Chatgpt’s; on the off chance you have the time / interest to put the source to this 5.5 Pro version, my email address is registered; Regards, Davide
May 9, 2026 at 6:01 am
Often, it helps to use different AIs in pingpong mode: AI 1 thinks to have proved something. Ask it to give output in texfile. This becomes input for AI 2 with the prompt: “Check this proof carefully for correctness. List all errors, gaps, and weaknesses. Ouput in tex file.” If this feedback claims to have found errors or gaps, ask AI 2 for a repair, or give ints answer file back to AI 1, asking: “Here is feed back to your proof attempt…” It works really very often in my research.
May 9, 2026 at 11:08 am
You don’t need to ask Gowers if he can put the source to this 5.5 Pro version as you phrase it. You can access it yourself at https://chatgpt.com/, click the “select model” dropdown menu. You do need to pay $200 first.
May 9, 2026 at 6:00 am |
[…] A recent experience with ChatGPT 5.5 Pro 🔥 12 […]
May 9, 2026 at 6:08 am |
[…] https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/ […]
May 9, 2026 at 6:20 am |
I think you must have a typo after “It is an easy exercise to show that”, because it reads “if |A| = k, then 2k-1 <= |A|…” which isn’t even a true statement, let alone an easy exercise…
May 9, 2026 at 12:46 pm
Corrected — thanks.
May 9, 2026 at 6:52 am |
[…] 元記事: https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/ […]
May 9, 2026 at 7:12 am |
I have found interacting with these models to be a rather frustrating experience, though I have only been trying to get it to solve my favorite problems or give me new ideas as to how to solve it. I’ve found myself either trying to filter my way through nonsense or excitedly trying an idea it has, only to be let down for the idea is either trivial or hopeless.
If this is the future of mathematics research-endlessly trying to filter through an LLM’s output looking for something sensible, I’m really not looking forward to this.
May 9, 2026 at 7:27 am |
Why do you get access to ChatGPT 5.5 Pro but not everyone else?
May 9, 2026 at 7:51 am |
[…] A recent experience with ChatGPT 5.5 Pro […]
May 9, 2026 at 8:02 am |
[…] 🔗 閱讀原文 […]
May 9, 2026 at 8:49 am |
hello! I am a numberphobe, my friend sent this article, and I skipped the math-y parts but definitely got the main message of this article so good job you
May 9, 2026 at 9:00 am |
[…] Share on X (Opens in new window) X […]
May 9, 2026 at 9:15 am |
[…] 知名菲爾茲獎得主、數學家 Timothy Gowers 日前在其個人部落格發表了一篇文章《A recent experience with ChatGPT 5.5 Pro》，引起不少關注和討論。他表示，在幾乎沒有人類數學提示的情況下，ChatGPT 5.5 Pro 僅用了短短一小時左右，就產出了一份達到博士生研究水準的數學證明。 […]
May 9, 2026 at 10:03 am |
Anonymous wrote:
“My view on this is really pessimistic. The way things progress, the value of thinking and having deep ideas seems to be lower and lower.”
Where does the value of thinking and having deep ideas come from? We need to think about this now. If it comes primarily from their scarcity – the fact that having certain ideas is hard – then indeed this value may drop precipitously when the manufacture of ideas can be automated. But if the value comes from the utility of the ideas – the benefit that the idea brings – then the story changes: perhaps creating more good ideas is actually better, not worse. Here I’m using “utility” in a broad sense, not just in the sense of what people often call applied mathematics.
In other words, mathematicians may need to adjust to a transformation from a scarcity economy to an abundance economy.
In a society where food is cheap to produce, people still get paid to make nice food.
Maybe mathematicians will need to pay more attention to convincing people that their work is not only difficult, but good. If it’s truly good, it doesn’t get its value mainly from being difficult.
Then, looking ahead another step, maybe we should think about how good AI is at convincing people that the mathematics it creates is actually good. When AI becomes better at this than humans, that’s another thing we don’t need mathematicians for. But at this point we may be wondering what we need humans for at all. (It’s mainly humans who need humans.)
May 9, 2026 at 11:59 am |
“2k-1 <= k” typo?
Thanks — corrected now.
May 9, 2026 at 12:45 pm |
Can LLM not only solve but pose new math problems worthy of attention? It can be an interesting study.
May 9, 2026 at 3:04 pm
From my experience, (GPT 5.5 Pro) yes and no. The main problem is that the model seems to have a fuzzy understanding of where the “solvable” frontier (given the current theory) is located. I have tried to rank problems in the Erdos problems to see if it is able to “predict” which problems are solvable, or eventually close to be solved, with relative success. Then when asking to reevaluate the problems with e.g. Deep Research, this prediction or “difficulty score” can drastically go either up or down. Since it doesn’t have a defined internal criteria/”representation” of this frontier, when creating new problems, often they are solvable in easy or trivial ways, or are too strong, and outside the technology of the theory. Longer prompting and user’s mathematical knowledge (including trends and importance) can help to define a good frontier problem by “collaborating” with the LLM, but I haven’t got a new interesting question solely from the LLM in one-shot.
May 9, 2026 at 1:31 pm |
Interesting. While you’re debating whether LLMs are truly intelligent, I built a deterministic execution framework that forces consistent outputs regardless of the underlying reasoning mechanism.The question isn’t whether it’s ‘real’ intelligence. The question is whether you can engineer reliable outcomes.If you want to move past probabilistic outputs and into structural control, here’s the system:
https://www.skool.com/trans-sentient-intelligence-8186/about?ref=8aeedb072d4b4d7fb98cc2238610f2f4
May 9, 2026 at 2:14 pm |
[…] Source: A recent experience with ChatGPT 5.5 Pro […]
May 9, 2026 at 3:03 pm |
[…] for de-googled Android usersTrust and access are increasingly mediated by platform identity. A recent experience with ChatGPT 5.5 ProPower users are now benchmarking models by workflow reliability, not demo quality. Using Claude […]
May 9, 2026 at 5:11 pm |
[…] Source: Gowers […]
May 9, 2026 at 5:30 pm |
[…] Источник: Гауэрс […]
May 9, 2026 at 5:38 pm |
[…] 网站: gowers.wordpress.com HN评论: […]
May 9, 2026 at 6:13 pm |
lean+paper of infinite twins cocreated with gpt 5.4/5.5 pro
https://github.com/alegator-cs/infinite_twin_primes
May 9, 2026 at 7:00 pm |
Thank you, I enjoyed reading your write-up of your interactions with ChatGPT. I really wish more mathematicians would do this.
Thinking about $R(2,k)$ was interesting for me: I knew that the minimum value of $2k-1$ was attained for cosets of subgroups, but I did not expect the result that every value between the minimum $2k-1$ and the obvious maximum of the number of 2-multisubsets of $\{1,\ldots, k\}$ would be attained. And I think I learned something by asking ‘if that’s true, then how do we get $k^{3/2}$’. The construction I came up with is $\{1,\ldots, r\}, \{2^s ,2^{s+1}, \ldots, 2^{s+t-1} \}$ where $2^s$ is bigger than $2r$; then by thinking about binary representations of the numbers it’s easy to see that $|A + A| = 2r-1 + rt + t^2$, and by taking $t = \sqrt{r}$, we get $|A| \approx r$ and $|A+A| \approx r^{3/2}$. On closer reading, I saw this has some of the flavour of the sets the LLM found.
To prove I’m not an LLM, let me give a completely off-the-wall analogy. The chain decompositions e.g. for $A = \{a < b < c < d < e\}$ that $a+a < a+b < 2b < b+c < 2c < c+d < 2d < d+e < 2e$ and $a+c < a+d < b+d < b + e < c+e$ and $a+e$ (on its own) show that $9 \le |A+A| \le 9 + 5 + 1 = 15 = \binom{5}{2} + \binom{5}{1}$. These numbers are familiar to me from the decomposition of the $\mathrm{SL}_2(\mathbb{C})$-representation $\mathrm{Sym}^2 \mathrm{Sym}^4 \mathbb{C}^2$ as a direct sum of the irreducible representations $\mathrm{Sym}^8 \mathbb{C}^2$, $\mathrm{Sym}^4 \mathbb{C}^2$ and $\mathrm{Sym}^0 \mathbb{C}^2 \cong \mathbb{C}$. I don’t think the analogy goes any further: the algebraic side has just too much structure, but it would be rather wonderful if one could ‘categorify’ some aspect of arithmetic combinatorics.
Finally, a brief response to your thought experiment:
> Here’s a thought experiment: suppose that a mathematician solved a major problem by having a long exchange with an LLM in which the mathematician played a useful guiding role but the LLM did all the technical work and had the main ideas. Would we regard that as a major achievement of the mathematician? I don’t think we would.
I think you are right for ‘we’ as the community stands at the moment, but it is perhaps interesting to reread this quote substituting ‘computer algebra system’ in place of ‘LLM’ … My tentative hope is that the community learns to use LLMs as the tools they are, and that the more adventurous of us start to credit LLMs in the acknowledgements of our papers. Or even as coauthors?! Going back to my analogy with computer algebra, Doron Zeilberger has set a precedent here with his frequent coauthor Shalosh B. Ekhad.
```

---

## 16. Mux (YC W16) Is Hiring

- 日期: 2026-05-08 21:02
- 链接: https://www.mux.com/jobs

```
Mux is video for developers. Our mission is to democratize video by solving the hard problems developers face when building video: video encoding and streaming (Mux Video), video monitoring (Mux Data), and more. Video is a huge part of people’s lives, and we want to help make it better.
We’re committed to building a healthy team that welcomes a diverse range of backgrounds and experiences. We want people who care about our mission, are ready to grow, believe in our values (from Be Human to Turn Customers Into Fans), and want to make the people around them better.
You’ll be joining a tight-knit team with experience at places like Google, YouTube, Twitch, Zencoder, Fastly, and more. Our founders previously started (and sold) Zencoder, an early leader in cloud video technology, and authored Video.js, the biggest HTML5 video player on the web. We organize Demuxed, the premiere conference for video engineers in the world.
We’re backed by top investors like Coatue, Accel, Andreessen Horowitz, and Y Combinator. You’ll get to work with amazing companies: hundreds of startups, plus Reddit, Vimeo, Robinhood, CBSi, Discovery, PBS, and TED. Customers large and small love working with us and love our team.
We are building something big together. We’d love to hear from you!
Every frame matters.
We are humans first and believe there is more to life than work.
Look for ROI on time and money. We are a startup after all.
Good communication leads to good thinking (and vice versa).
Always look for opportunities to delight our users.
Don’t wait for something to be on fire to fix it.
Mux is remote-equal with offices in Downtown San Francisco and London
Flexible vacation & paid company holidays
Competitive health insurance (100% employee and 65% dependents coverage)
Family friendly with paid leave, funded fertility benefits, and a snoo rental
No-meeting Thursdays + focus weeks every quarter
FSA and funded HSA available
Annually renewed professional development stipends
3 day/week lunch for in-office and remote employees
Fully paid premiums for STD, LTD, and group life insurance
Fun perks like equipment, sVOD, and cell phone reimbursement
Mux is an Equal Opportunity employer committed to building a diverse company. We believe diversity makes us better, and we strive to be inclusive and equitable. That’s why we do not discriminate on the basis of race, religion, color, national origin, gender, sexual orientation, age, marital status, veteran status or disability status.
Don’t see the position you’re looking for?
No credit card required to start using Mux.
```

---

## 17. Google broke reCAPTCHA for de-googled Android users

- 日期: 2026-05-08 18:45
- 链接: https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users

```
Google has tied its next-generation reCAPTCHA system to Google Play Services on Android, meaning anyone running a de-Googled phone will automatically fail verification when the system decides to challenge them.
The requirement forces Android users to run Google’s proprietary app framework version 25.41.30 or higher just to prove they’re human.
When reCAPTCHA flags what it considers suspicious activity, it abandons the old image puzzles and demands you scan a QR code. That scan requires Play Services running in the background, communicating with Google’s servers. If you’re using GrapheneOS or any other custom ROM that strips out Google’s software, the verification fails.
Google announced the broader system, Google Cloud Fraud Defense, at Cloud Next on April 23, pitching it as a trust platform designed to handle autonomous AI agents and traditional bots alike. What Google didn’t emphasize was the part where proving you’re human now requires submitting to its proprietary surveillance.
Reclaim Your Digital Freedom.
Get unfiltered coverage of surveillance, censorship, and the technology threatening your civil liberties.
This wasn’t sudden, either. An Internet Archive snapshot from October 2025 shows the same support page already listing a Play Services requirement at version 25.39.30. Google built this dependency quietly for at least seven months before a Reddit user on the degoogle subreddit flagged it, with reporting from PiunikaWeb and Android Authority bringing wider attention.
The iOS comparison is revealing because Apple devices running iOS 16.4 or later complete the same verification without installing any additional apps. Google didn’t demand iPhone users install Google software to pass the test. Only Android users who refuse Play Services get locked out. The asymmetry reveals what this is really about: not security, but ecosystem control.
reCAPTCHA sits in front of millions of websites. When Google ties verification to Play Services, it establishes a precedent where accessing basic web content requires running Google’s software and transmitting data to Google’s servers.
People running de-Googled phones chose those setups because they read the data practices, understood what Play Services phones home about, and decided they didn’t consent. Google’s new system punishes that decision by treating the absence of its proprietary software as suspicious by default.
Web developers adopting this reCAPTCHA should understand what they’re choosing. Every site that implements it tells de-Googled Android users they’re not welcome. That’s a small audience today. It’s also the audience most likely to care about how a website treats their data, and the least likely to capitulate.
```

---

## 18. AI is breaking two vulnerability cultures

- 日期: 2026-05-08 17:55
- 链接: https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures

```
Someone else noticed the change, however, realized the security implications, and shared it publicly. Since it was now out, the embargo was deemed over, and we can now see the full details.
It's interesting to see the tension here between two different approaches to vulnerabilities, and think about how this is likely to change with AI acceleration.
On one side you have "coordinated disclosure" culture. This is probably the most common approach in computer security. When you discover a security bug you tell the maintainers privately and give them some amount of time (often 90d) to fix it. The goal is that a fix is out before anyone learns about the hole.
On the other side you have "bugs are bugs" culture. This is especially common in Linux, where the argument is that if the kernel is doing something it shouldn't then someone somewhere may be able to turn it into an attack. Just fix things as quickly as possible, without drawing attention to them. Often people won't notice, with so many changes going past, and there's still time to get machines patched.
This approach never worked perfectly, but with AI getting good at finding vulnerabilities it's a much bigger problem. So many security fixes are coming out now that examining commits is much more attractive: the signal-to-noise ratio is higher. Additionally, having AI evaluate each commit as it passes is increasingly cheap and effective. [1]
Long embargoes, however, aren't doing well either. The historical pace of detection was slow: if you found something and reported it to the vendor with a 90d disclosure window, there was a very good chance no one else would notice during that time. But now with so many AI-assisted groups scanning software for vulnerabilities, that no longer holds. In this case, just nine hours after Kim reported the ESP vulnerability Kuan-Ting Chen also independently reported it. Embargoes can increase risk: they create a false sense of non-urgency and limit which actors can work to fix a flaw.
I don't know how to resolve this, but personally very short embargoes seem like a good approach, and they'd need to get even shorter over time. Luckily AI can speed up defenders as well as attackers here, allowing embargoes that would previously have been uselessly short.
[1] I tested on Gemini 3.1 Pro, ChatGPT-Thinking 5.5, and Claude Opus
4.7. All three all got it right away when given f4c50a403.
When I gave them just the diff, imagining a hypothetical future where
diffs are still public right away but with less context, Gemini was
sure it was a security fix, GPT thought it probably was, and Claude
thought it probably wasn't. This is just a very quick test to
illustrate what's possible: one run of each with the prompt "Without
searching, does this look like a security patch?" There's no control
group, and don't put much stock in the cross-model comparison!
Comment via: facebook, lesswrong, hacker news, mastodon, bluesky, substack
```

---

## 19. Cartoon Network Flash Games

- 日期: 2026-05-08 16:29
- 链接: https://www.webdesignmuseum.org/flash-game-exhibitions/cartoon-network-flash-games

```
Cartoon Network Flash Games
Explore a collection of Cartoon Network browser games inspired by The Powerpuff Girls, Dexter’s Laboratory, Samurai Jack, and other fan-favorite series.
Explore a collection of Cartoon Network browser games inspired by The Powerpuff Girls, Dexter’s Laboratory, Samurai Jack, and other fan-favorite series.
```

---

## 20. David Attenborough's 100th Birthday

- 日期: 2026-05-08 12:03
- 链接: https://www.bbc.com/news/articles/cp3pww9g0p5o

```
King and Queen lead tributes for David Attenborough's 100th birthday
King Charles III and Queen Camilla are among well-wishers to share a birthday message celebrating Sir David Attenborough turning 100.
The royal couple also shared photographs of Sir David, including one of him with a young Prince Charles and Princess Anne in 1958, in which he is introducing them to Cocky the cockatoo, from his BBC Zoo Quest TV series.
The King and Queen wished him a very happy birthday, adding: "Enjoy your special celebration this evening!"
The veteran broadcaster and environmentalist has said he was "completely overwhelmed" by messages he had received ahead of his big day, which includes a special concert on Friday evening at the Royal Albert Hall in London.
Sir David added: "I simply can't reply to each of you separately, but I'd like to thank you all most sincerely for your kind messages, and wish those of you who have planned your own local events: have a very happy day."
In a video for the Earthshot Prize, which celebrates climate leadership and innovation, the Prince of Wales said: "Happy 100th David, cannot believe it's your 100th birthday."
He went on to thank him for all his support, while noting how "everything you do continues to inspire me".
Prince William's brother, the Duke of Sussex, is also among the well-wishers, describing Sir David as a "secular saint" in an article in Time.com.
"His most significant contribution has been the systematic dismantling of the notion that climate issues are happening 'somewhere else'," he said.
"Young people continue to listen to him not just for the spectacle of nature, but for a sense of continuity in an unstable world."
Former England men's football captain Sir David Beckham simply called the broadcaster "our National Treasure", while actress and activist Joanna Lumley wished the broadcaster a happy birthday with a little help from the people of Stroud, Gloucestershire, in a video message.
TV naturalist and presenter Chris Packham wrote in The Big Issue: "I don't think that any person in the entire history of our species has made such a significant contribution to engaging people and developing a love for all of life on Earth as David Attenborough."
Meanwhile, the World Wide Fund for Nature (WWF) shared a birthday tribute video, voiced by actors Dame Judi Dench, Morgan Freeman, Miranda Richardson, Asa Butterfield, Sam Heughan and Iwan Rheon, along with former Spice Girl Geri Halliwell‑Horner and wildlife presenter Liz Bonnin.
It is a spoken-word version of the Louis Armstrong classic song, What a Wonderful World, featuring footage of various animals.
Oscar-winning composer Hans Zimmer also paid tribute, saying that despite his extensive feature film success, "none of it is as important as working for David Attenborough because that is really about the existence of our planet."
Actor Sir Ian McKellen added that Sir David "sums up what was best about the BBC" with "serious programmes made for a popular audience".
"His ability to communicate his own enthusiasms are very precious and he's brought such joy to so many people," he said. "And I think, along with a lot of people, my favourite television programmes are probably natural history."
Friday evening's show at the Royal Albert Hall is the climax of a week of special events and broadcast programming in honour of Sir David, who was born in 1926 and joined the BBC in 1952.
Presenter Kirsty Young will host the special 90-minute concert celebrating Sir David's life, which will air on BBC One and iPlayer from 20:30 BST.
Special guests including Sir Michael Palin, Steve Backshall, Liz Bonnin and Chris Packham will appear at the event to reflect on Sir David's life and legacy.
Ahead of the concert, Young said: "Sir David's gift to the world has been a life spent exquisitely revealing Earth's wonders to us all.
"The very least he deserves is a big 100th birthday bash at the Royal Albert Hall. I'm very happy indeed, as the host, to be able to invite everyone to the party."
The event will recall some of the most memorable wildlife moments from Sir David's career and the BBC's natural history archive.
Live music from the BBC Concert Orchestra will include pieces associated with his most famous television series, including the snakes and iguanas chase from Planet Earth II, and the wave-washing orcas sequence from Frozen Planet II.
The concert will also feature performances from Bastille frontman Dan Smith, who will join the orchestra for a rendition of the band's hit Pompeii, which featured in Planet Earth III.
Elsewhere, Sigur Rós will perform Hoppípolla, which was used in the promotion of Planet Earth and Planet Earth II, while other musical guests will include singer Sienna Spiro and harpist Francisco Yglesia.
The BBC has been celebrating Sir David's centenary with special programming throughout the week.
Sir David and members of his former production team reflected on the making of their groundbreaking 1979 series Life on Earth for a documentary broadcast last weekend.
Meanwhile, recent BBC One series Secret Garden saw Sir David examine the hidden worlds and wildlife thriving in British gardens. Many of his other programmes have also been made available as part of a dedicated collection on iPlayer.
The BBC's chief content officer Kate Philips said Sir David's 100th birthday marked an "extraordinary" moment, describing him as a "truly remarkable individual".
Sir David was born in west London on 8 May 1926, and has also fronted pioneering natural history series including his Life Collection, The Trials of Life and The Blue Planet.
He has two children with wife Jane, who died in 1997. His brother Richard was an Oscar-winning actor and director, and died in 2014.
On Thursday, the Natural History Museum paid tribute to Sir David by naming a species of parasitic wasp after him.
The Attenboroughnculus tau is native to the Patagonian lakes of Chile, and a specimen was recently found in the museum's collection, four decades after it was collected.
Other species to have been named after the broadcaster in the past include a wildflower, butterfly, grasshopper, dinosaur and ghost shrimp.
Get our flagship newsletter with all the headlines you need to start the day. Sign up here.
```

---
