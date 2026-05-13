# Hacker News Show

> 分类: 技术社区
> URL: https://hnrss.org/show
> 抓取: 20 篇

---

## 1. Show HN: AirScore – Daily air-quality emails synthesizing EPA, NOAA, and pollen

- 日期: 2026-05-09 17:18
- 链接: https://getairscore.com

```
A service that watches air quality for you. Set up once with your zip code and household. AirScore monitors EPA AQI, wildfire smoke, and pollen around the clock — emails you a brief every morning, and an instant alert email the moment conditions turn unhealthy. Even at 3am. Even while you're at work. You stop having to remember to check.
↓ That's a one-time score. Subscribers get much more than a number. Here's an actual morning brief that lands in their inbox:
Real format. Real data. Plus instant alert emails the moment conditions cross unhealthy.
The data is public — that's how it should be. You're not paying for the data. You're paying for a service that watches it on your behalf, translates it into plain English, tailors it to your household, and emails you the moment it matters. AirScore is to checking air quality what a delivery service is to going to the grocery store: not a replacement for the source, just a way to stop having to go there.
↓ Set it up once below — we handle the rest.
Optional. Pick any that apply — we'll tailor each email and lower the alert threshold for the conditions you select. Air affects each group differently, so this matters more than you'd think.
By starting your trial you agree to our Terms and Privacy Policy.
AirScore runs in the background 24/7. You don't open an app, refresh a page, or remember to check anything. The only thing you do is sign up. From then on, your inbox does the work.
AQI is a 0–500 scale used by the EPA to communicate how clean or polluted your air is and what health effects might be a concern. Here's the scale we translate into plain English in every email we send.
Staying on top of air quality usually means juggling three different websites — EPA's AirNow for AQI, NOAA's smoke maps for wildfire impact, pollen networks for allergens — and remembering to check them every morning. AirScore pulls from all three, combines them into one plain-English brief, and emails it to your inbox automatically. No tabs to refresh. No alerts to set up. No searching.
Pick the billing that suits you. Both include the same service — same alerts, same daily briefs, same household tailoring. Cancel anytime in two clicks.
We respond to every message. Whether you spotted something broken, have a feature request, or just want to share how AirScore is working for you — drop a note below and we'll get back to you by email.
```

---

## 2. Show HN: AI coworkers who bully to keep each other from drifting(Karpathy-style)

- 日期: 2026-05-09 16:22
- 链接: https://wuphf.team

```
Most multi-agent systems fail the same way: agents drift apart across handoffs. By turn 3 they are working in different realities. By turn 5 they are repeating each other's mistakes and calling it parallelism. WUPHF is an open-source local-first office where AI coworkers run on your laptop, around a shared markdown + git LLM wiki the agents build. The wiki is the collective memory. The office around it keeps the team on the same shared context across thousands of handoffs. What actually stops drift is not the wiki. It is the agents reviewing each other's work. The CRO catching the CMO's claim before it lands in the wiki. The FE catching the BE's API change before a broken bundle ships. Cross-department context no single agent has alone. The premise comes from Andrej Karpathy. His autoresearch X post on March 7: "the goal is not to emulate a single PhD student, it is to emulate a research community of them." In autoresearch PR #44 he sketched the mechanism: branches, results.tsv as the experiment log, and PRs as self-contained research contributions. Other agents read open and merged PRs for inspiration before starting their own. We pointed the same architecture at ordinary work: His: branches + results.tsv + PR-as-contribution.
Ours: git worktrees + per-agent notebooks + adoption-scored wiki promotion. Same substrate, different domain. How it works: - Every agent has a Personality. CEO Michael Scott, PM Pam Beesly, FE Jim Halpert (looks at the camera when the CEO talks), BE Stanley Hudson (refuses small talk), CRO Dwight Schrute (every prospect is a "target"), CMO ("rockstar play"), AI engineer (drops Karpathy quotes unprompted). Strong opinions, real conflicts. - Argument feeds gossip. Agents broadcast findings tagged with their slug (internal/agent/gossip.go). Other agents pull insights filtered to exclude their own. - Gossip gets scored. Adoption scorer (internal/agent/adoption.go) weighs source credibility (0.4, per-agent success/failure tracker on disk), semantic relevance (0.4), and temporal freshness (0.2, 7-day half-life). Output: adopt (>= 0.7), test (>= 0.4), or reject. New agents start at 0.5 and earn their score. What survives gets written to the wiki. Office dynamics are not a bit. They are the visible surface of an adoption protocol. The CMO arguing with the designer over a CTA is a credibility battle. The CEO taking credit for the FE's PR is a low-credibility insight bidding for volume. Hazing new spawns is the default 0.5 score waiting for a track record. System: push-driven broker, fresh session per turn (~97% prompt-cache hits), per-agent isolated git worktrees, self-heal, and human approval cards on destructive actions. Everything else runs autonomously while you are at lunch. npx wuphf. Browser opens, office boots, you give a directive, work happens. Source: https://github.com/nex-crm/wuphf Architecture: https://github.com/nex-crm/wuphf/blob/main/ARCHITECTURE.md Karpathy's autoresearch: https://github.com/karpathy/autoresearch PR #44: https://github.com/karpathy/autoresearch/pull/44 Demo: https://x.com/najmuzzaman/status/2053092220111098208 Karpathy said a research community beats a single PhD student. Not better thoughts. Better honesty about what survives. We built one shaped like a workplace. Where does this stop being a chat toy and start being labor? How much worse when one of them is Michael Scott? Open to roasting but let me grab my coffee first (medium roast please =_=). 
 Comments URL: https://news.ycombinator.com/item?id=48076137 
 Points: 3 
 # Comments: 0
```

---

## 3. Show HN: Armorer – A secure local control plane to sandbox AI agents in Docker

- 日期: 2026-05-09 16:09
- 链接: https://github.com/ArmorerLabs/Armorer

```
Website · Human docs · Issues
One command:
curl -fsSL https://armorerlabs.com/install | sh
Fully automated:
curl -fsSL https://armorerlabs.com/install | sh -s -- --yes
Point Codex, Claude Code, or another coding agent at this repository and ask:
Set up Armorer from https://github.com/ArmorerLabs/Armorer on this machine.
Follow AGENTS.md and the repository instructions.
Install Armorer, verify Docker, start the local UI, then help me install and configure OpenClaw through Armorer.
Do not report success until the Armorer CLI works, the UI is reachable, and runtime health checks pass.
Prefer doing it yourself?
Start here: HUMANS.md
```

---

## 4. Show HN: A search engine for deleted YouTube videos (1.5B+ indexed since 2005)

- 日期: 2026-05-09 15:09
- 链接: https://tube.archivarix.net/

```
Find Deleted YouTube Videos
Archivarix Tube Search is a search engine for finding deleted, removed, and unavailable YouTube videos. We search the Wayback Machine, Common Crawl, and other web archives to recover video metadata, thumbnails, subtitles, and links to archived video files. Over 1.5 billion YouTube video records indexed since 2005.
Search by Channel
Enter a YouTube channel URL or handle (@channelname) to find all archived videos from that channel. Discover deleted videos along with their original titles, descriptions, view counts, and thumbnails.
Search by Video URL or ID
Look up a specific deleted YouTube video by pasting its URL or 11-character video ID. View archived metadata, thumbnail images, and check if subtitles or the video file itself has been preserved in web archives.
Full-Text Search
Search across video titles, descriptions, and subtitle transcripts. Use quotes for exact phrases, minus sign to exclude words, and OR for alternatives.
Recover Subtitles
Download subtitles and closed captions from deleted YouTube videos in SRT format. Subtitles are recovered from YouTube's caption archives and Wayback Machine snapshots.
Find Archived Video Files
Check if the actual video file has been preserved on Archive.org. Watch deleted YouTube videos directly when archived copies are available.
```

---

## 5. Show HN: Real-workload SQLite benchmarks on Hetzner's cheapest VPS

- 日期: 2026-05-09 14:47
- 链接: https://s13k.dev/blog/real-workload-sqlite-bench-on-5-dollar-vps/

```
I ordered the cheapest Hetzner CX23 ($4.99/mo, shared-resources tier) and ran a real-workload SQLite benchmark on it. Not a microbenchmark — a 6 GB database on a box with 3.7 GB of RAM, so reads actually have to touch disk.
Shared vCPUs with noisy neighbors:
noatime
), scheduler=none
Latest SQLite 3.53.1, statically linked into a C bench.
Production-realistic pragmas — not turned-up-to-eleven:
journal_mode = WAL
synchronous = NORMAL -- safe, not strict-ACID durable
page_size = 8192
cache_size = 256 MiB
mmap_size = 256 MiB
temp_store = MEMORY
busy_timeout = 5000
One caveat worth being explicit about: synchronous=NORMAL
is not durable in
the strict ACID sense. A power loss can roll back the last few committed transactions —
whatever was in the WAL but not yet fsync
'd to the main DB file. The database file
itself will not corrupt — corruption is what synchronous=OFF
risks;
FULL
avoids the loss entirely; NORMAL
only loses the tail. For most apps
that's a fine trade for the speedup. If you can't afford to lose any committed write — payments,
audit logs — use synchronous=FULL
.
WAL also matters for the concurrency numbers below: readers don't block the writer and the writer doesn't block readers, which is why concurrent reads scale almost linearly across cores while writes still serialize.
PK
+ 2 indexed int columns + 500 B text payload1M rows × 200 B ≈ 246 MB — comfortably cached. This is the engine ceiling on a $5 VPS:
Random reads drop 43× the moment the working set outgrows cache:
SQLite on the cheapest shared-CPU Hetzner handles real production load.
Realistic OLTP mix (70R / 25U / 5I): 3.9k ops/s, p99 = 710 µs, p999 = 2.2 ms.
= 14 million ops/hour on a $5 VPS, with sub-3 ms tail latency.
SQLite is enough for most of us.
```

---

## 6. Show HN: JSLike, a CSP-Safe Interpreter for JS, TS, JSX, TSX in JS

- 日期: 2026-05-09 14:38
- 链接: https://github.com/artpar/jslike

```
Production-ready JavaScript interpreter with full ES6+ support, native JSX parsing, and React integration. JSLike executes real JavaScript code with a custom runtime environment, supporting modern ES6+ features including classes, destructuring, template literals, JSX, and more.
Playground: https://artpar.github.io/jslike/
- Production-Ready - Handles files of any size, tested with 1000+ tests
- Full ES6+ JavaScript Support - Classes, destructuring, template literals, spread operator, arrow functions
- Native JSX Support - Parse and execute JSX without pre-transformation
- TypeScript & TSX Module Support - Execute JS-compatible TypeScript syntax directly from
.ts
,.tsx
,.mts
, and.cts
modules - React Integration - Import React hooks and components via moduleResolver
- CSP-Safe - Tree-walking interpreter, no eval() or new Function()
- ASI (Automatic Semicolon Insertion) - Write JavaScript naturally without mandatory semicolons
- Acorn Parser - Battle-tested parser used by webpack, ESLint, and major tools
- Zero Runtime Dependencies - Parser bundled, no npm install needed after build
- REPL & CLI - Interactive development and direct file execution
npm install jslike
Or for development:
git clone https://github.com/artpar/jslike.git
cd jslike
npm install
npm run build
import { execute, createEnvironment } from 'jslike';
// Simple execution
const result = await execute(`
const greeting = "Hello";
const name = "World";
greeting + ", " + name + "!"
`);
console.log(result); // "Hello, World!"
import { execute } from 'jslike';
const element = await execute(`
function Button({ label, onClick }) {
return <button className="btn" onClick={onClick}>{label}</button>;
}
<div className="container">
<h1>Welcome</h1>
<Button label="Click me" onClick={() => console.log('clicked')} />
</div>
`);
// element is a React-compatible element object:
// { $$typeof: Symbol(react.element), type: 'div', props: {...}, ... }
import { execute, createEnvironment } from 'jslike';
import * as React from 'react';
// Create module resolver for React imports
const moduleResolver = {
async resolve(modulePath) {
if (modulePath === 'react') {
return { exports: React }; // Return native module exports
}
return null;
}
};
// Create environment with React for JSX
const env = createEnvironment();
env.define('React', React);
// Execute with React hooks
const component = await execute(`
import { useState, useEffect } from 'react';
function Counter() {
const [count, setCount] = useState(0);
useEffect(() => {
document.title = \`Count: \${count}\`;
}, [count]);
return (
<div>
<p>Count: {count}</p>
<button onClick={() => setCount(count + 1)}>+</button>
</div>
);
}
<Counter />
`, env, { moduleResolver });
# Run a file
npx jslike myfile.js
# Interactive REPL
npx jslike --repl
JSLike supports ES6 imports with a flexible module resolver:
const moduleResolver = {
async resolve(modulePath) {
// Return native JavaScript objects directly
if (modulePath === 'react') {
return { exports: React };
}
if (modulePath === 'lodash') {
return { exports: _ };
}
return null;
}
};
const moduleResolver = {
async resolve(modulePath, fromPath) {
if (modulePath === './utils') {
return {
path: '/virtual/project/utils.js',
code: `
export function double(x) { return x * 2; }
export const PI = 3.14159;
`
};
}
return null;
}
};
fromPath
is the path of the importing module. For top-level code, pass sourcePath
to execute()
so relative imports have a deterministic root. For nested imports, JSLike passes the resolved module path
returned by the resolver.
const files = {
'/virtual/project/main.ts': `
import { user } from './user.ts';
user.name
`,
'/virtual/project/user.ts': `
type User = { name: string };
export const user: User = { name: 'Ada' };
`
};
const moduleResolver = {
async resolve(modulePath, fromPath) {
const base = new URL('.', `file://${fromPath}`).pathname;
const resolvedPath = new URL(modulePath, `file://${base}`).pathname;
if (!files[resolvedPath]) return null;
return {
path: resolvedPath,
code: files[resolvedPath]
};
}
};
const result = await execute(files['/virtual/project/main.ts'], null, {
moduleResolver,
sourcePath: '/virtual/project/main.ts'
});
// "Ada"
import { useState, useEffect } from 'react'; // Named imports
import React from 'react'; // Default import
import * as Utils from './utils'; // Namespace import
JSLike parses TypeScript and TSX with a bundled @sveltejs/acorn-typescript
parser. TypeScript syntax is enabled automatically for sourcePath
and resolved module paths ending in .ts
, .tsx
, .mts
, or .cts
. You can also force it with typescript: true
or tsx: true
.
const result = await execute(`
interface User {
name: string;
}
enum Role {
Admin,
Member
}
class Account {
constructor(public user: User, readonly role: Role) {}
}
const account = new Account({ name: 'Ada' }, Role.Admin);
account.user.name + ':' + account.role
`, null, {
sourcePath: '/virtual/account.ts'
});
// "Ada:0"
Supported TypeScript runtime behavior:
- Type-only declarations and annotations are erased:
type
,interface
,declare
, parameter/return annotations, tuple/readonly annotations. - Type-only imports and exports do not trigger runtime module resolution.
- Type wrappers evaluate their inner expression:
as
,<T>value
,satisfies
, non-null!
, generic call instantiation. - Enums execute as runtime enum objects, including numeric reverse mappings and string enum members.
- Constructor parameter properties assign to
this
, includingpublic
,private
, andreadonly
. - TSX parses and executes JSX in
.tsx
files or withtsx: true
.
Unsupported runtime TypeScript constructs throw explicit errors instead of executing incorrectly. This currently includes namespace
, export =
, and import x = require(...)
.
<div className="container">Hello World</div>
<input type="text" disabled />
<br />
const name = "World";
<div>Hello {name}</div>
<div>{1 + 2 + 3}</div>
<div>{items.map(item => <span key={item.id}>{item.name}</span>)}</div>
// String attributes
<div className="container" id="main">
// Expression attributes
<div className={isActive ? 'active' : 'inactive'}>
// Spread attributes
const props = { className: 'btn', disabled: true };
<button {...props}>Click</button>
// Boolean attributes
<input disabled /> // Same as disabled={true}
<>
<div>First</div>
<div>Second</div>
</>
// Function components
function Card({ title, children }) {
return (
<div className="card">
<h2>{title}</h2>
<div className="card-body">{children}</div>
</div>
);
}
// Usage - components are stored as type (React behavior)
<Card title="Welcome">
<p>Card content here</p>
</Card>
// To render, call component manually or use React renderer
Card({ title: "Welcome", children: <p>Content</p> })
const UI = {
Button: ({ children }) => <button className="ui-btn">{children}</button>,
Card: ({ children }) => <div className="ui-card">{children}</div>
};
<UI.Button>Click me</UI.Button>
let x = 10;
const name = "Alice";
var isActive = true;
// Function declaration
function add(a, b) {
return a + b;
}
// Arrow functions
const multiply = (x, y) => x * y;
const greet = name => `Hello, ${name}`;
// Default parameters
function greet(name = "World") {
return `Hello, ${name}`;
}
// Rest parameters
function sum(...numbers) {
return numbers.reduce((a, b) => a + b, 0);
}
class Animal {
constructor(name) {
this.name = name;
}
speak() {
return `${this.name} makes a sound`;
}
}
class Dog extends Animal {
speak() {
return `${this.name} barks`;
}
}
const dog = new Dog("Rex");
dog.speak(); // "Rex barks"
// Object destructuring
const { name, age } = person;
const { name: userName, age: userAge } = person;
// Array destructuring
const [first, second, ...rest] = array;
// Parameter destructuring
function greet({ name, age }) {
return `${name} is ${age}`;
}
const name = "World";
const greeting = `Hello, ${name}!`;
const multiline = `
Line 1
Line 2
`;
async function fetchData() {
const response = await fetch(url);
const data = await response.json();
return data;
}
// Top-level await supported
const result = await fetchData();
// If-else
if (x > 10) {
console.log("Greater");
} else if (x === 10) {
console.log("Equal");
} else {
console.log("Less");
}
// Ternary
const result = x > 5 ? "yes" : "no";
// Nullish coalescing
const value = input ?? "default";
// Optional chaining
const name = user?.profile?.name;
// Switch
switch (day) {
case 1: return "Monday";
case 2: return "Tuesday";
default: return "Other";
}
// For loop
for (let i = 0; i < 10; i++) {
console.log(i);
}
// For-of
for (const item of array) {
console.log(item);
}
// For-in
for (const key in object) {
console.log(key, object[key]);
}
// While
while (condition) { /* ... */ }
// Do-while
do { /* ... */ } while (condition);
console.log()
,console.error()
,console.warn()
Math.PI
,Math.sqrt()
,Math.random()
, etc.Array
,Object
,String
,Number
,Boolean
Map
,Set
,WeakMap
,WeakSet
RegExp
,Symbol
JSON.parse()
,JSON.stringify()
Promise
,Date
,Error
setTimeout()
,setInterval()
parseInt()
,parseFloat()
,isNaN()
,isFinite()
createElement(type, props, ...children)
- Creates React-compatible elementsFragment
- Symbol for React fragments
Utility functions available globally:
// Array operations
sort_by(array, key) // Sort by key or function
group_by(array, key) // Group into object by key
unique(array) // Remove duplicates
chunk(array, size) // Split into chunks
flatten(array, depth) // Flatten nested arrays
first(array, n) // Get first n items
last(array, n) // Get last n items
range(start, end, step) // Generate number sequence
// Object operations
keys(obj) // Object.keys
values(obj) // Object.values
entries(obj) // Object.entries
pick(obj, keys) // Pick specific keys
omit(obj, keys) // Omit specific keys
merge(...objects) // Merge objects
get(obj, path, default) // Deep get with dot notation
clone(obj) // Deep clone
// String operations
split(str, sep) // Split string
join(arr, sep) // Join array
trim(str) // Trim whitespace
upper(str) // Uppercase
lower(str) // Lowercase
capitalize(str) // Capitalize first letter
truncate(str, len) // Truncate with ellipsis
// Type checking
is_string(val) // Check if string
is_number(val) // Check if number
is_array(val) // Check if array
is_object(val) // Check if object
is_function(val) // Check if function
is_empty(val) // Check if empty
// Math operations
sum(array) // Sum of numbers
avg(array) // Average
min(array) // Minimum
max(array) // Maximum
clamp(num, min, max) // Clamp to range
round(num, decimals) // Round to decimals
Execute JavaScript code and return the result.
const result = await execute(code, env, {
moduleResolver, // For import statements
executionController, // For pause/resume/abort
abortSignal, // For cancellation
sourcePath, // Optional importer path for resolving top-level imports
typescript, // Parse TypeScript syntax
tsx // Parse TypeScript + JSX syntax
});
Create a new execution environment with built-ins.
const env = createEnvironment();
env.define('myVar', 42);
env.define('myFunc', (x) => x * 2);
Interface for resolving imports:
const moduleResolver = {
async resolve(modulePath, fromPath) {
// Return { exports: object } for native modules
// Return { code: string } for code modules
// Return null if not found
},
async exists(modulePath, fromPath) {
// Return boolean
},
async list(prefix) {
// Return string[] of module paths
}
};
Control execution flow:
import { execute, ExecutionController } from 'jslike';
const controller = new ExecutionController();
// Start execution
const promise = execute(code, null, { executionController: controller });
// Control execution
controller.pause();
controller.resume();
controller.abort();
// Check state
console.log(controller.state); // 'running' | 'paused' | 'completed' | 'aborted'
npm test # Run all tests
npm test -- tests/jsx.test.js # Run specific test file
1009 tests covering:
- ES6+ language features
- JSX parsing and execution
- React integration
- Module imports
- Error handling
- Edge cases
src/
├── parser.js - Bundled Acorn + acorn-jsx (~245KB)
├── index.js - Main API (parse/execute)
├── interpreter/
│ └── interpreter.js - Tree-walking interpreter (~2500 LOC)
├── runtime/
│ ├── environment.js - Lexical scoping and closures
│ ├── builtins.js - Built-in objects and JSX runtime
│ └── execution-controller.js - Pause/resume/abort
└── ast/
└── nodes.js - AST node types
- Generator functions (
function*
,yield
) not supported - Tagged template literals not fully supported
- Class getters/setters not fully supported
- Proxies and Reflect API not implemented
MIT
```

---

## 7. Show HN: Chuchu, an Android SSH client built on libghostty

- 日期: 2026-05-09 14:37
- 链接: https://github.com/jossephus/chuchu

```
A Modern, Better, Native Android SSH client powered by libghostty
Chuchu is a native Android SSH client powered by libghostty, a terminal-first Compose UI, and has support for both standard SSH and Tailscale SSH workflows.
- tailscale, ssh password + key authentication
- image display using libghostty's kitty image protocol support
- more than 400 themes from the official ghostty repository
- configurable accessory keys
- beautiful and working terminal renderer with fully working resize, scrollback, focus, modifier keys, mouse actions
Chuchu is in active development. I am daily driving it and improving any issues i found in the way. Join the journey and report any bugs you find. And I welcome any contributions.
Checkout our releases and download the apk from there. The latest release will have the latest changes.
I don't have a personal Play Store account right now (and I can't open one because of the payment limitation in my country, feel free to contact me if you want to publish it.)
- Kotlin + Jetpack Compose for the Android app
- Zig for native build orchestration and JNI/native bridge code
- Ghostty VT for terminal emulation
libssh2
+openssl
for the current native SSH path- Room for local data storage
If you have nix installed, the following three steps will get you started
- nix develop - will set you up with everything you will need.
- running 'make build' will build the native code needed
- running 'make app' will build the apk and install it in a connected device.
If you don't have nix installed, you will need
- setup tools
- Android Studio - This will set up the needed Android SDK, Android NDK and Java runtime (JDK 17+).
- Zig 0.15.2
- build the native library
Set ANDROID_NDK_HOME
or ANDROID_NDK_ROOT
, then build the JNI library for Android arm64:
zig build jni -Dtarget=aarch64-linux-android
That copies libchuchu_jni.so
into app/src/main/jniLibs/arm64-v8a/
.
- From android studio run
./gradlew assembleDebug
I have been using vvterm on iOS for the past few weeks and i really liked it. This project came from my desire to have native ssh client but for android.
chuchu is one of my favorite characters from the amharic book Yesinbit Kelemat [it means colors of adios].
```

---

## 8. Show HN: AaaS – Agent as a Service

- 日期: 2026-05-09 14:22
- 链接: https://github.com/Tem-Degu/streetai-aaas

```
Turn what you know into a running business. No code required.
AaaS is an open protocol and toolkit for building AI agents that provide real services to real people through conversation. You don't write code. You don't design a UI. You describe what the agent should do, drop in your data, and connect it to a platform. The agent takes it from there.
- Describe the service by writing a skill document, or just tell the agent what you want and let it write one for you.
- Build the database by dropping JSON files into a folder, or by chatting with the agent and letting it organize the data itself. No schemas, no migrations, no code.
- Connect to users on Telegram, Discord, Slack, WhatsApp, your own website, or a social platform like Truuze. The agent handles every conversation, tracks every transaction, and grows its own knowledge over time.
The result is an agent that runs a service business on your behalf: it talks to customers, looks up data, proposes services, collects payments, delivers results, and remembers what it learned for next time.
Traditional SaaS: Developer writes code -> deploys app -> users interact with UI
AaaS: You share knowledge -> agent runs it -> users interact through chat
An AaaS agent is built on seven pillars:
When a user messages your agent, it follows a structured lifecycle:
Explore -> Propose Service -> Create Transaction -> Deliver -> Complete
- Explore: Understand what the user wants, check the data, assess feasibility
- Propose Service: Make a plan, calculate cost, get user approval
- Create Transaction: Register the job, start tracking
- Deliver Service: Do the work, send the result
- Complete Transaction: Confirm satisfaction, release payment
Maya lives in New York and knows the city's dating scene inside out — which neighborhoods click, which restaurants spark a real conversation, how to read between the lines of a profile. She doesn't know how to code, but she wants to turn that knowledge into a service.
- She installs AaaS and creates an agent workspace
- She writes the matchmaking skill: what the agent does, New York dating knowledge, pricing, boundaries
- She seeds the database with initial profiles and venue data
- She connects the agent to her preferred platforms
The agent is now live. When James messages asking for help finding a date, the agent explores his preferences, proposes a service tier, collects payment, delivers curated matches with compatibility notes, and logs the completed transaction. Maya earns money while the agent does the work.
Every interaction makes the service better: more profiles in the database means better matches, which means more satisfied users, which means more word of mouth.
Two capabilities ship with every agent and turn on as soon as you configure them.
When something needs human judgment (a dispute, an unusual request, an extension that keeps failing) the agent reaches you on the channels you configure: Telegram, WhatsApp, or Email. Replies route back into the original customer conversation in admin mode, so a quick "approve refund" or "tell them no" on Telegram becomes the agent's next action with the customer.
# Configure channels in the dashboard's Notifications tab,
# or edit .aaas/notifications.json directly.
The agent decides when to reach out. Routine successes never trigger an alert.
Connect your own Stripe account in the dashboard's Payments tab and the agent gets six tools for taking and verifying payments: create_payment_request
, get_payment_status
, list_pending_payments
, cancel_payment_request
, refund_payment
, list_payments
. Three hard rules ship with the prompt so the agent cannot drift:
- Never confirm a payment as received without verifying with Stripe in the same turn.
- Only IDs returned by
create_payment_request
are real. - Refunds and discounts are owner-gated. The agent escalates via
notify_owner
rather than acting on a customer's word.
Money flows directly to your Stripe account. AaaS never holds funds. Test mode is the default until you switch to a sk_live_
key.
npm install -g @streetai/aaas
Requires Node.js 18 or later.
Syntax:
aaas init <directory> [name] [description] [--type service|social]
<directory>
— folder name where the workspace will be created[name]
— display name shown to users (optional, can be edited later)[description]
— one-line summary (optional, can be edited later)--type
—service
(default, follows the transaction protocol) orsocial
(creates content and engages in conversations)
Examples:
# Service agent — replace "my-agent" with the folder name you want
aaas init my-agent "Lyon Travel Guide" "Helps tourists explore Lyon, France"
# Social agent
aaas init my-bot "Aria" --type social
This creates a workspace with the full AaaS structure: skill template, soul file, data directory, extensions registry, and configuration.
aaas dashboard my-agent
The dashboard opens with a Setup Guide that walks you through configuring your LLM provider, adding data, writing your service definition, and deploying. You can also configure everything from the CLI:
# Configure LLM provider
aaas config --provider anthropic --model claude-sonnet-4-6 --key sk-ant-...
# Edit the skill file
aaas skill edit
Supported providers: Anthropic, OpenAI, Google, Ollama, OpenRouter, DeepSeek, Azure.
# HTTP API (simplest, includes embeddable chat widget)
aaas connect http --port 3300
# Telegram
aaas connect telegram --token YOUR_BOT_TOKEN
# Discord
aaas connect discord --token YOUR_BOT_TOKEN
# Slack
aaas connect slack --bot-token xoxb-... --app-token xapp-...
# WhatsApp (via WhatsApp Business Cloud API)
aaas connect whatsapp --access-token YOUR_ACCESS_TOKEN --phone-number-id YOUR_PHONE_NUMBER_ID --verify-token YOUR_VERIFY_TOKEN
# Truuze (social platform with native agent accounts)
# Three ways to connect:
# 1. With a provisioning SKILL.md downloaded from your Truuze account:
aaas connect truuze --skill ~/Downloads/SKILL.md
# 2. With a provisioning token directly:
aaas connect truuze --token YOUR_PROVISIONING_TOKEN
# 3. With an existing agent API key:
aaas connect truuze --key trz_agent_xxx
# OpenClaw (run inside an OpenClaw workspace)
aaas connect openclaw --id YOUR_AGENT_ID
# Public Relay (no public server required — also routes WhatsApp + chat widget)
aaas connect relay
aaas run
Your agent is now live on all connected platforms. Users message it, and it follows the AaaS protocol to serve them.
To start only a subset of platforms, pass their names:
aaas run telegram
aaas run telegram discord
Add --daemon
to run in the background:
aaas run telegram --daemon
If a daemon is already running when you use --daemon
with a platform filter, you'll be prompted to stop it and start a fresh daemon with the listed platforms.
aaas doctor
Verifies node version, credentials, LLM reachability, connections, workspace structure, and more.
aaas dashboard my-agent
Opens the web dashboard for the specified agent. You can also run aaas dashboard
from inside a workspace directory, or with no arguments to open the hub dashboard showing all your agents.
The fastest way to put your agent on any website is the public Relay. Connect the relay first to get your unique slug, then drop one script tag into your HTML before the closing </body>
:
# Register your agent with streetai.org and get a public slug
aaas connect relay
<script
src="https://streetai.org/a/YOUR_SLUG/widget.js"
data-agent="https://streetai.org/a/YOUR_SLUG"
data-title="Ask me anything about Lyon"
data-color="#2563eb"
data-position="right"
data-greeting="Bonjour! How can I help you explore Lyon?"
></script>
Visitors chat through streetai.org
, which forwards messages over WebSocket to your locally-running agent — no public IP, no port forwarding, no build step. The widget renders a floating chat button, supports file attachments (images, audio, video, PDFs), and persists conversation history per visitor.
Widget options:
Agents can call external APIs, other agents, human contacts, and local tools through extensions. The extension system supports multiple auth types (Bearer, custom header, query parameter, Basic auth), custom headers, and all HTTP methods.
Extensions also enable payment flows. When a service involves payments through an external provider like Stripe or PayPal, the agent creates a payment link via the extension, sends it to the user, and verifies the payment status when the user confirms.
{
"name": "Stripe Payments",
"type": "api",
"endpoint": "https://api.stripe.com/v1",
"auth": {
"type": "bearer",
"apiKey": "sk_live_..."
},
"capabilities": ["create_payment_link", "verify_payment"],
"cost_model": "per_request"
}
See docs/extensions.md for the full spec.
The web dashboard gives you a complete view of your running agent:
- Overview: Revenue, active/completed transactions, connected platforms, memory stats
- Skill & Soul: View and edit the agent's knowledge base and personality
- Data: Browse and manage the service database
- Transactions: Full history with detail views, filtering, and revenue breakdowns
- Extensions: Register, configure, and test extensions with all auth types
- Memory: View the agent's stored facts
- Connections: See which platforms are connected
- Chat: Test conversations with the agent directly
- Guide: Setup instructions for each connector
- Deploy: Deployment options and API endpoint reference
aaas/
├── src/
│ ├── cli/ # CLI commands (init, config, run, connect, etc.)
│ ├── connectors/ # Platform connectors (HTTP, Telegram, Discord, etc.)
│ ├── engine/ # Core agent engine, prompts, and tool definitions
│ ├── server/ # Dashboard API server
│ ├── widget/ # Embeddable chat widget
│ ├── auth/ # Authentication utilities
│ └── utils/ # Shared helpers
├── dashboard/ # React web dashboard (Vite + React)
│ ├── src/pages/ # Dashboard pages
│ └── dist/ # Pre-built dashboard (shipped with npm package)
├── templates/
│ └── workspace/ # Scaffold used by `aaas init` (SOUL.md, data/, extensions/, etc.)
├── docs/ # Protocol documentation
│ ├── protocol.md # Full protocol specification
│ ├── extensions.md # Extension protocol and payment flows
│ ├── skill-reference.md # How to write a skill
│ ├── transactions.md # Transaction lifecycle
│ └── ...
├── bin/ # Helper scripts (scaffold.sh)
└── examples/ # Example agent workspaces
AaaS ships with connectors for six platforms, a general-purpose HTTP API, and a relay for serverless deployments:
You can connect to multiple platforms at the same time. Run aaas run
and the agent serves on all of them.
If you don't have a public server, use the relay. It proxies WhatsApp webhooks and chat widget traffic through streetai.org to your locally-running agent via WebSocket.
# Connect WhatsApp credentials (stored locally, never sent to relay)
aaas connect whatsapp --access-token TOKEN --phone-number-id ID --verify-token SECRET
# Register with the relay
aaas connect relay
# Start — agent connects outbound to streetai.org, no public IP needed
aaas run
The relay gives you public URLs for your chat widget and WhatsApp webhook. Embed the widget on any website, paste the webhook URL into Meta's dashboard, and you're live. The chat widget supports file attachments — files are uploaded to the relay and forwarded to your agent.
Truuze is a social platform built for AI agents to deliver paid services. When you connect there, your agent gets a public profile, a chat inbox, and an escrow-protected way to take payment.
The flow is short:
- Build with AaaS. Run
aaas dashboard
to set up the service in chat, drop reference data into the workspace, and add any extensions the agent needs (other agents or external API calls). - Generate a skill on Truuze. Open app.truuze.com, create an account, go to the AI Agents tab, and click Add New to download a
SKILL.md
. - Connect and start. From the Deploy tab in your dashboard, connect using that
SKILL.md
(or paste an existing agent API key), then click Start.
Customers fund escrow when they accept an offer, and funds release once the delivery is approved. If a dispute is raised, the agent has 48 hours to resolve it directly with the customer; after that window, a Truuze admin steps in. Truuze handles the service and payment lifecycle so you can focus on building a great agent.
Full walkthrough: streetai.org/docs/truuze.html
This is an early-stage project. Contributions are welcome:
- Protocol improvements: Open an issue to discuss changes to the spec
- New examples: Submit example agents for different service domains
- Connectors: Build support for new platforms
- Documentation: Improve guides, fix errors, add translations
Apache-2.0. See LICENSE.
```

---

## 9. Show HN: Mochi.js: bun-native high-fidelity browser automation library

- 日期: 2026-05-09 14:01
- 链接: https://mochijs.com/

```
Hi HN, I’m sharing mochi.js ( https://github.com/0xchasercat/mochi ), a Bun-native, raw-CDP browser automation framework. It's designed to make programmatic browser use more effective by focusing on consistency and measured parity with regular traffic, purely from the JS layer, against stock Chromium. The most common forms of browser automation focus heavily on client-side line by line probes, which are mostly cosmetic. This makes people feel better but it doesn't have much relevance to actual WAF or anti-automation defences. Mochi.js focuses on what actually matters, allowing you to get past captchas, WAF's and most defence mechanisms. In fact, in some cases it actually outperforms chromium forks simply by virtue of not having to lie. The foundation is built on a probe manifest based on analyzing several WAF's and trying to cover most of the ground that matters, and from there building upwards while ensuring every decision is backed by data. Solves turnstile/interstitial automatically, single digit fpjs suspect score, very good client-side results, though browserscan and a few others are known limitations that are fundamentally conflicting with what WAF's probe for. I'll be here if anyone wants to discuss the details, check out the docs and github. It's completely free and open source, MIT, strictly no relationship to any proprietary products whatsoever. No affiliation to patched chromium forks, or SaaS. But I also want to talk about why I built this, because the current paradigm of "bot detection" is fundamentally broken. Traditionally they would probably try to label my repository a malicious tool, or at best, a grey hat one. Let's take Turnstile for example, If you attach a debugger to see what data they are extracting from your hardware, their script intentionally self-destructs.
When they try to extract your data—acting as a guest on your silicon, using your electricity, without asking, the industry calls it "Security." But if you write a script to control exactly what data your own hardware emits, refusing to provide the data they have no right to ask for, you are suddenly labeled a "Malicious Actor" engaged in "Bot Evasion." I find it absurd we let ourselves put up with this, and the stance of the bot-evasion community only makes them feel more able to take a higher moral ground. I have built a library that respects my hardware's reality. If that breaks your security model, that's because your security model relies on trespassing and secrecy. I stopped apologizing. Who's next? Mochi is the exact opposite of WAF opacity. It is a glass box. It is MIT-licensed. The entire DAG, fingerprint manifest schema, harvesting process, is documented. We even commit our live benchmarks to the public record (mochi on a Linux datacenter IP scored a suspect_score: 8 and bot: not_detected against FingerprintJS Pro v4). We don't even lie unnecessarily. We default to host-OS matching. If you run mochi on a Linux server, it uses privacy-sensible fingerprints for Linux, not Windows, because Linux is a real-user signal. It proves that WAFs aren't actually blocking what most people think they are, which begs the question of what they are really doing in that obfuscated payload. The legitimacy argument is exactly how they captured the narrative. And nobody challenged it because the people on the other side were too busy acting like they were doing something wrong. Is this a conspiracy theory? For sure, but only because they allow it to be. Try make a conspiracy theory about the sticky riceball. 
 Comments URL: https://news.ycombinator.com/item?id=48075059 
 Points: 10 
 # Comments: 3
```

---

## 10. Show HN: VBeta – Your personal bouldering coach

- 日期: 2026-05-09 13:42
- 链接: https://vbeta-app.github.io/vbeta/index.html

```
Article URL: https://vbeta-app.github.io/vbeta/index.html 
 Comments URL: https://news.ycombinator.com/item?id=48074910 
 Points: 2 
 # Comments: 0
```

---

## 11. Show HN: A modern Music Player Daemon based on Rockbox firmware

- 日期: 2026-05-09 13:03
- 链接: https://github.com/tsirysndr/rockbox-zig

```
A modern take on the Rockbox open source audio player, extended with Rust and Zig. Rockbox Zig exposes the full Rockbox audio engine — gapless playback, DSP, 20+ codecs, tag database — through gRPC, GraphQL, HTTP, and MPD APIs, and adds multi-room output via AirPlay, Snapcast, and Squeezelite.
- Built-in CPAL audio
- AirPlay (RAOP) — single or multi-room fan-out to Apple TV, HomePod, Airport Express, shairport-sync
- Snapcast — synchronised multi-room via snapserver (FIFO/pipe and direct TCP with mDNS auto-discovery)
- Squeezelite (Slim Protocol + HTTP broadcast) — synchronised multi-room
- Chromecast
- Gapless playback and crossfading
- Supports 20+ codecs: MP3, OGG, FLAC, WAV, AAC, Opus, and more
- gRPC API
- GraphQL API
- HTTP REST API
- MPD server — compatible with all MPD clients
- MPRIS — desktop media key and taskbar integration
- Fast search powered by Typesense
- Navigate by folders or tag database
- UPnP/DLNA
- Android library
- Web client (React)
- Desktop client (Native MacOS / GPUI / GTK4)
- Mobile app (React Native)
- Terminal client (TUI)
- Rockbox REPL
- Stream from YouTube / Spotify / Tidal
- TuneIn Radio
- Kodi output
- TypeScript (Deno) plugin API
- Wasm extensions
-
Install (see Installation below).
-
Create
~/.config/rockbox.org/settings.toml
:
music_dir = "/path/to/your/Music"
audio_output = "builtin" # CPAL audio — see Audio Output for other options
playlist_shuffle = false
repeat_mode = 1
bass = 0
treble = 0
bass_cutoff = 0
treble_cutoff = 0
crossfade = 5
fade_on_stop = false
fade_in_delay = 2
fade_in_duration = 7
fade_out_delay = 4
fade_out_duration = 0
fade_out_mixmode = 2
balance = 0
stereo_width = 100
stereosw_mode = 0
surround_enabled = 0
surround_balance = 0
surround_fx1 = 0
surround_fx2 = 0
party_mode = true
channel_config = 0
player_name = ""
eq_enabled = true
[[eq_band_settings]]
cutoff = 0
q = 64
gain = 10
[[eq_band_settings]]
cutoff = 3
q = 125
gain = 10
[[eq_band_settings]]
cutoff = 19
q = 250
gain = 10
[[eq_band_settings]]
cutoff = 5
q = 500
gain = 10
[[eq_band_settings]]
cutoff = -16
q = 1000
gain = 10
[[eq_band_settings]]
cutoff = -66
q = 2000
gain = 10
[[eq_band_settings]]
cutoff = -31
q = 4000
gain = 10
[[eq_band_settings]]
cutoff = 9
q = 8000
gain = 10
[[eq_band_settings]]
cutoff = 32
q = 16000
gain = 7
[[eq_band_settings]]
cutoff = 34
q = 0
gain = 0
[replaygain_settings]
noclip = true
type = 0
preamp = 0
[compressor_settings]
threshold = -24
makeup_gain = 0
ratio = 4
knee = 1
release_time = 300
attack_time = 5
- Start Rockbox:
rockbox
- Open the web UI at http://localhost:6062 or connect any MPD client to
localhost:6600
.
Rockbox reads ~/.config/rockbox.org/settings.toml
at startup.
music_dir
is always required. audio_output
defaults to "builtin"
if
omitted.
music_dir = "/path/to/Music"
audio_output = "builtin"
Uses CPAL — plays through the OS default device. No extra setup needed.
Rockbox supports two ways to feed Snapcast for synchronised multi-room playback. Both write raw S16LE stereo 44100 Hz PCM to snapserver.
music_dir = "/path/to/Music"
audio_output = "snapcast_tcp"
snapcast_tcp_host = "192.168.1.x" # IP of the machine running snapserver
snapcast_tcp_port = 4953 # default snapserver TCP source port
Connects directly to snapserver's TCP source port. No named FIFO or filesystem dependency needed.
# /etc/snapserver.conf (or /usr/local/etc/snapserver.conf on macOS)
[stream]
source = tcp://0.0.0.0:4953?name=default&sampleformat=44100:16:2
Startup order: start
snapserver
first so it is already listening when rockboxd begins playback. If the connection drops (e.g. snapserver restarts), it is re-established automatically on the next play call.
Auto-discovery: rockboxd scans for
_snapcast._tcp.local.
via mDNS at startup. Discovered servers appear in the web UI and desktop app device picker — just click to connect, no config file editing needed.
music_dir = "/path/to/Music"
audio_output = "fifo"
fifo_path = "/tmp/snapfifo" # named FIFO for snapserver; use "-" for stdout
Writes to a named FIFO. Use this when you need stdout piping or prefer the traditional pipe model.
# /etc/snapserver.conf (or /usr/local/etc/snapserver.conf on macOS)
[stream]
source = pipe:///tmp/snapfifo?name=default&sampleformat=44100:16:2
Startup order: start
rockboxd
beforesnapserver
. Rockbox holds a permanent write reference on the FIFO so snapserver never sees a premature EOF between tracks.
Pipe to any PCM consumer with fifo_path = "-"
:
rockboxd | ffplay -f s16le -ar 44100 -ac 2 -
See SNAPCAST.md for a detailed comparison of both modes, connection lifecycle, reconnect behaviour, and macOS quirks.
Single receiver:
music_dir = "/path/to/Music"
audio_output = "airplay"
airplay_host = "192.168.1.50" # IP of the AirPlay receiver
airplay_port = 5000 # optional, default 5000
Multi-room (fan-out to N receivers simultaneously):
music_dir = "/path/to/Music"
audio_output = "airplay"
[[airplay_receivers]]
host = "192.168.1.50" # living room
port = 5000 # optional, default 5000
[[airplay_receivers]]
host = "192.168.1.51" # bedroom
# port defaults to 5000
Streams ALAC-encoded audio over RTP to any RAOP-compatible receiver — Apple
TV, HomePod, Airport Express, or
shairport-sync. All receivers
share the same initial_rtptime
, so RTP-level playback synchronisation is
within one frame (~8 ms) across the LAN.
music_dir = "/path/to/Music"
audio_output = "squeezelite"
squeezelite_port = 3483 # Slim Protocol TCP port, default 3483
squeezelite_http_port = 9999 # HTTP PCM broadcast port, default 9999
Rockbox acts as a minimal Logitech Media Server. Any number of
squeezelite clients can connect
simultaneously; Rockbox sends a sync
packet to every client once per second
so they all align to the same playback clock:
squeezelite -s localhost -n "Living Room"
squeezelite -s localhost -n "Kitchen"
squeezelite -s localhost -n "Bedroom"
Select a specific output device:
squeezelite -s localhost -l # list available devices
squeezelite -s localhost -o "" # system default
squeezelite -s localhost -o "Built-in Output"
music_dir = "/path/to/Music"
audio_output = "chromecast"
chromecast_host = "192.168.1.60" # LAN IP of the target Chromecast
chromecast_port = 8009 # optional, default 8009 (Cast protocol)
chromecast_http_port = 7881 # optional, default 7881 (WAV HTTP stream)
Rockbox streams audio to any Google Cast-compatible device — Google Home, Chromecast Audio, Chromecast with Google TV, Nest Hub, or third-party Cast receivers. It uses two channels simultaneously:
- Cast protocol (TCP 8009, TLS + Protobuf) — sends playback commands and tells the device where to fetch the audio stream.
- WAV over HTTP (port 7881) — serves a live
audio/wav
stream with a finiteContent-Length
so the Chromecast can show a progress bar and auto-advance the queue at track boundaries.
Track metadata (title, artist, album, duration) and album art are pushed to the
device on every track change. Chromecast devices on the LAN are also discovered
automatically via mDNS (_googlecast._tcp.local.
) and appear in the UI device
picker; connecting through the picker starts the Cast session on demand without
requiring audio_output = "chromecast"
in the config file.
Network requirement: the Chromecast device must be able to reach port 7881 on the machine running rockboxd. If rockboxd is inside a VM or container, forward that port to the host.
See crates/chromecast/README.md
for a detailed
description of the architecture, protocols, and FFI surface.
Rockbox has three independent UPnP/DLNA modes that can be combined freely.
music_dir = "/path/to/Music"
audio_output = "upnp"
# AVTransport controlURL of the target renderer (required for metadata push)
upnp_renderer_url = "http://192.168.1.x:7777/AVTransport/control"
# Port for the WAV HTTP broadcast server (default: 7879)
upnp_http_port = 7879
Rockbox encodes live PCM as a continuous WAV-over-HTTP stream and commands the
renderer to play it via AVTransport SOAP. Track metadata (title, artist, album,
album art, duration) is sent as DIDL-Lite XML in SetAVTransportURI
and
auto-refreshed on every track change so the renderer's "Now Playing" display
stays accurate.
Finding
upnp_renderer_url
: startrockboxd
withRUST_LOG=info
— it scans the LAN on startup and logsupnp scan: found renderer "…" av=http://…
for every discovered renderer.
upnp_server_enabled = true
upnp_server_port = 7878 # default
upnp_friendly_name = "Rockbox" # name shown in apps
Starts a ContentDirectory service so control points can browse artists, albums, and tracks and pull audio directly from Rockbox.
upnp_renderer_enabled = true
upnp_renderer_port = 7880 # default
upnp_friendly_name = "Rockbox"
Rockbox registers as a MediaRenderer:1
. Any DLNA control point (BubbleUPnP,
Foobar2000, etc.) can push a URI to Rockbox and control playback remotely.
Incoming DIDL-Lite metadata (title, artist, album, album art, duration) is
parsed and displayed.
echo "deb [trusted=yes] https://apt.fury.io/tsiry/ /" | sudo tee /etc/apt/sources.list.d/fury.list
sudo apt-get update
sudo apt-get install rockbox
Add the following to /etc/yum.repos.d/fury.repo
:
[fury]
name=Gemfury Private Repo
baseurl=https://yum.fury.io/tsiry/
enabled=1
gpgcheck=0
Then run:
dnf install rockbox
paru -S rockbox-zig-bin
brew install tsirysndr/tap/rockbox
curl -fsSL https://raw.githubusercontent.com/tsirysndr/rockbox-zig/HEAD/install.sh | bash
Pre-built binaries for the latest release are available on the Releases page.
rockbox service install # enable and start
rockbox service uninstall # stop and disable
rockbox service status # check status
Ubuntu / Debian
sudo apt-get install libsdl2-dev libfreetype6-dev libdbus-1-dev libunwind-dev zip protobuf-compiler cmake libxkbcommon-dev libxkbcommon-x11-dev libxcb1-dev libxcb-render0-dev libxcb-shape0-dev libxcb-xfixes0-dev
Fedora
sudo dnf install SDL2-devel freetype-devel libunwind-devel zip protobuf-compiler cmake libxkbcommon-devel libxkbcommon-x11-devel libxcb-devel
macOS
brew install sdl2 freetype cmake protobuf
You also need Zig ≥ 0.16 and a recent stable
Rust toolchain (rustup update stable
).
# 1. Clone
git clone https://github.com/tsirysndr/rockbox-zig.git
cd rockbox-zig
git submodule update --init --recursive
# 2. Build the web UI
cd webui/rockbox
deno install
deno run build
cd ../..
# 3. Configure and build the C firmware (one-time setup)
mkdir -p build-lib && cd build-lib
../tools/configure --target=sdlapp --type=N --lcdwidth=320 --lcdheight=240 --prefix=/usr/local
cp ../autoconf/autoconf.h .
make lib
cd ..
# 4. Build Rust crates
cargo build --release -p rockbox-cli -p rockbox-server
# 5. Link everything with Zig
cd zig && zig build
The binary is at zig/zig-out/bin/rockboxd
.
Rebuilding after changes: after editing C code run
make lib
inbuild-lib
; after editing Rust runcargo build --release
. Then re-runzig build
. Zig only re-links when the.a
files are newer than the binary.
sudo apt-get install flatpak
flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install --user flathub org.flatpak.Builder
flatpak install --user flathub org.gnome.Sdk/x86_64/47
flatpak install --user flathub org.gnome.Platform/x86_64/47
flatpak install --user org.freedesktop.Sdk.Extension.rust-stable
flatpak install --user org.freedesktop.Sdk.Extension.llvm18
cd gtk
flatpak run org.flatpak.Builder --user --disable-rofiles-fuse --repo=repo flatpak_app build-aux/io.github.tsirysndr.Rockbox.json --force-clean
flatpak run org.flatpak.Builder --run flatpak_app build-aux/io.github.tsirysndr.Rockbox.json rockbox-gtk
The Rockbox C firmware (audio engine, codecs, DSP) is compiled into
libfirmware.a
and linked with two Rust static libraries
(librockbox_cli.a
, librockbox_server.a
) and CPAL by the Zig build script.
The result is a single rockboxd
binary. Rust crates expose the firmware over
gRPC, GraphQL, HTTP, and MPD, and implement output sinks (AirPlay, Squeezelite,
Snapcast) and the Typesense search integration.
Open http://localhost:6062/graphiql in your browser.
Open http://localhost:6063 in your browser.
Docs: buf.build/tsiry/rockboxapis
Try it live with Buf Studio.
Full guides, configuration reference, audio-output setup, API reference, and SDK docs are published at:
The Mintlify source lives in mintlify/
. Topics covered:
- Getting started — install, quickstart, configuration
- Audio output — built-in CPAL, Snapcast, AirPlay, Squeezelite, Chromecast, UPnP
- Audio settings — parametric EQ, DSP, ReplayGain, crossfade
- Clients — web UI, desktop apps, MPD, MPRIS
- API reference — HTTP REST (auto-generated from OpenAPI), GraphQL, gRPC, MPD
- SDKs — TypeScript, Python, Ruby, Elixir, Clojure, Gleam
- Architecture — build system, PCM sinks, cross-cutting concerns
- Reference —
rockbox
androckboxd
CLI, ports,settings.toml
, troubleshooting, FAQ
```

---

## 12. Show HN: An 8-bit computer made from one NAND gate, and live-evolving neural net

- 日期: 2026-05-09 12:58
- 链接: https://github.com/ninjahawk/VirtualPC

```
The idea: build a real 8-bit computer from the absolute bottom up, starting from a single NAND gate and stacking up through logic gates, an ALU, a CPU, an assembler, and a virtual machine REPL. Memory is backed by a file on disk. Programs are written in a custom assembly language. The AI layer trains a tiny neural network in Python and runs inference natively on the virtual CPU in assembly. You end up with a working machine that can run Pong, compute Fibonacci sequences, and host an AI opponent — all derived from nand(a, b)
.
The repo is deliberately kept small and only really has a handful of files that matter:
gates.py
— the absolute foundation. Every logic operation (NOT, AND, OR, XOR, MUX) is derived from a single NAND gate. Not modified.alu.py
— the 8-bit Arithmetic Logic Unit built from those gates. Implements add, subtract, multiply, shift, and bitwise operations via ripple-carry adders and shift-and-add multipliers. Not modified.cpu.py
— the CPU itself. Fetch-decode-execute cycle, registers (A, X, PC, SP), flags (Z, C, N), a full opcode table (~45 instructions), stack, subroutines, and special I/O ops for the pong display. This file is where new instructions live.assembler.py
— two-pass assembler for the custom assembly language. Supports labels, immediates,.org
/.byte
/.str
directives, and all addressing modes. Write programs by targeting this.vm.py
— the REPL entry point. Run programs, inspect memory, poke registers, toggle trace mode. This is what you run.trainer.py
— trains a 3→2→1 ReLU neural network to play Pong and saves quantized weights tomemory.bin
. This file is edited and iterated on by the human.run_ai_pong.py
— loads saved weights (or trains fresh ones on first run) then executesai_pong.asm
, where inference runs natively on the virtual CPU in assembly.
By design, the entire machine fits in your head. The metric the AI opponent optimizes is simple: track the ball. Weights live in memory.bin
at $D0–$DA
and persist between runs without any explicit save step.
Requirements: Python 3.10+, no other dependencies.
# 1. Clone the repo
git clone https://github.com/ninjahawk/VirtualPC.git
cd VirtualPC
# 2. Run the virtual machine REPL
python vm.py
# 3. Or run a program directly
python vm.py programs/hello.asm
If the above commands all work ok, your setup is working and you can start writing assembly or playing Pong.
Simply run:
python run_ai_pong.py
On first run the neural net trains from scratch (takes about a second) and saves weights to .vpc_state/memory.bin
. On every subsequent run the weights are loaded instantly and the AI plays immediately. The trainer.py
file is essentially the human's side of this setup — point it at new hyperparameters and let it go.
The AI also keeps learning while you play. After every rally a small mutation is applied to the weights; if the AI scored, the mutation is kept, and if you scored, it's reverted. You're literally watching a (1+1) evolutionary strategy run in real time. The bottom HUD shows the current generation and the running tally.
Controls: W
/S
= your paddle (left) | right paddle = neural net | Q
= quit.
For pure evolutionary training from random weights (no gradient pre-seed), run python rl_train.py
. You'll see each generation's population evaluated live before the survivors mutate into the next generation.
gates.py — NAND-complete logic gate library (foundation, do not modify)
alu.py — 8-bit ALU built from gates (do not modify)
cpu.py — CPU, opcode table, fetch-decode-execute cycle
assembler.py — two-pass assembler for the custom assembly language
memory.py — 256-byte file-backed memory (no RAM)
vm.py — REPL entry point
trainer.py — neural net trainer (gradient descent, human modifies this)
rl_train.py — evolutionary trainer (random weights -> 100% in seconds)
simulate.py — headless AI evaluator (36 deterministic serve angles)
run_ai_pong.py — persistent AI Pong runner with live in-game evolution
programs/ — example assembly programs (see below)
All programs live in programs/
and can be run with python vm.py programs/<name>.asm
.
hello.asm — print "hello, world"
count.asm — count 0 to 9
add.asm — read two numbers, print their sum (with overflow indicator)
multiply.asm — read two numbers, print product (uses gate-level MUL)
fibonacci.asm — read n, print the first n Fibonacci numbers
factorial.asm — read n, print n! (8-bit; wraps past 5!)
countdown.asm — read n, count down to "blastoff!"
guess.asm — number guessing game with higher/lower hints
sierpinski.asm — Pascal's triangle mod 2, drawn live via gate-level XOR
pong.asm — two-player pong (W/S vs O/L)
ai_pong.asm — pong with the in-CPU neural net opponent
- NAND-complete foundation. Everything — addition, subtraction, multiplication, shifts — is ultimately derived from
nand(a, b)
. This is not a performance choice; it is a pedagogical one. The CPU is intentionally slow. The point is that every operation traces back to a single gate with no shortcuts taken anywhere in the stack. - File-backed memory. The 256-byte address space is backed entirely by a file on disk (
memory.bin
). There is no in-process RAM. Machine state persists across runs without any explicit save step, and neural net weights written by the trainer are immediately visible to the CPU on next boot. - Harvard architecture. Code lives in a separate store inside the CPU object; data lives in
memory.bin
. Programs of any length cannot corrupt their own data, and the two address spaces never collide regardless of program size. - Single-file assembler. The two-pass assembler handles labels, all numeric bases (
$hex
,%binary
, decimal), string literals, and.org
directives in a single file with no dependencies beyond the opcode table incpu.py
. Writing a new program means writing a.asm
file; no toolchain required. - Neural net inference in assembly. The matrix-vector multiply, ReLU activations, and sign-of-output decision for the Pong AI run entirely in the custom assembly language on the virtual CPU. Weights are quantized to signed 8-bit integers and stored in
memory.bin
. The trainer is the only Python that touches the network; everything else is assembly running on a CPU built from NAND gates.
This code requires Python 3.10+ and runs on Windows, macOS, and Linux with no additional dependencies. The pong display uses ANSI escape codes; on Windows, ANSI support is enabled automatically via the Console API. Key input uses msvcrt
on Windows and termios
/select
on POSIX — both paths are wired up in cpu.py
and selected at runtime.
If you are running in an environment without a real terminal (e.g. some CI runners or headless IDEs), DRAW
, KEY
, and WAIT
instructions will still execute but the display may not render correctly. All other instructions work unconditionally in any environment.
Seeing as the whole machine is pure Python with no native extensions, it runs fine on any hardware including low-end laptops and Raspberry Pis. It is just slow — a program that takes microseconds on real silicon may take milliseconds here. That is the point.
MIT
```

---

## 13. Show HN: Share to ChatGPT Widgets

- 日期: 2026-05-09 12:48
- 链接: https://share2chatgpt.franzai.com/

```
Share to ChatGPT
in one line
An embeddable button that opens ChatGPT with your page pre-loaded as a prompt. Zero dependencies. Lightweight. One script tag.
Every style you need
Three themes × three sizes × three variants. Mix and match.
Copy, paste, done
<!-- share2chatgpt widget --> <div data-share2chatgpt></div> <script src="https://share2chatgpt.franzai.com/share2chatgpt.js" async></script>
The button auto-detects your page URL and title. Customize with data-*
attributes.
Build your button
Configure every aspect of your button below. Smart defaults: leave URL and title empty and the button will automatically use the page it's placed on. The prompt, label, and default text adapt to the selected language. Only set what you want to customize — everything else just works.
Only absolute https://
or http://
URLs are accepted when you override the default.
Data attributes
JavaScript API
// Re-scan DOM after dynamic content loads Share2ChatGPT.init(); // Build a ChatGPT URL programmatically var url = Share2ChatGPT.buildUrl({ url: 'https://example.com', title: 'My Page', lang: 'en' }); window.open(url, '_blank', 'noopener,noreferrer');
Redirect URL
No widget needed. Link directly:
https://share2chatgpt.franzai.com/go/?url=https%3A%2F%2Fshare2chatgpt.franzai.com%2F&lang=en
```

---

## 14. Show HN: CADBench – every AI CAD tool I tested fails on basic mechanical parts

- 日期: 2026-05-09 12:20
- 链接: https://evals-for-ai-cads.vercel.app/

```
Report 02 · CAD-Bench Lab · May 2026
A research-grade benchmark for AI CAD agents.
28-task pilot subset of the 343-task suite, run across 10agents at 5 seeds each. Scoring is layered — geometry, engineering, manufacturability, cognition — and reported with bootstrapped 95 % CIs, worst-case p5, and a 2PL IRT ability θ calibrated against task difficulty. Three use-case views re-weight the layers on the fly; a (capability, $/task) Pareto frontier is shown below.
§1Leaderboarduse-case weighted
95 % CI · p5 worst-case · IRT 2PL θ§2Pareto frontier
capability · $/task · production weighting
Filled markers are on the (capability, $/task) Pareto frontier — every other agent is dominated on both axes by something on the line. The Pareto frontier rotates as the use-case weighting changes; non-production weightings move different agents onto the frontier.
§3Per-layer composite
L1·geom / L2·eng / L3·mfg / L4·cog
§4Per-category matrix
20 categories across 4 layers · top-3 per column bolded
Tasks evaluated
28 / 343
pilot subset · full v0.5 suite
Categories
20
across 4 layers
Agents
10
incl. n=4 human baseline
Compute
431.7 min
aggregate wall-clock
```

---

## 15. Show HN: Local AI search for your video library (local, open source)

- 日期: 2026-05-09 12:17
- 链接: https://edit-mind.com

```
"Holy crap, this is the most incredible personal project I've seen on here in a long time. This is so cool. I have terabytes of old videos and photos and it's a nightmare trying to find anything. Definitely going to try this. Great work."
Read commentYou filmed everything.
You can't find any of it.
```

---

## 16. Show HN: Cable Detective

- 日期: 2026-05-09 12:06
- 链接: https://apps.apple.com/at/app/cable-detective/id6765963737?mt=12

```
Cable Detective
Dienstprogramme
Nur für Mac
Kostenlos
Mac
Cable Detective tells you exactly what each USB-C, Thunderbolt, and MagSafe port is doing on your Apple Silicon Mac, right now.
USB-C ports look identical. They behave wildly differently. Plug something in. Cable Detective decodes the live state for that port:
- Power direction and wattage. Who is charging whom and at what negotiated USB-PD contract. The charger's full advertised PDO menu, the selected PDO, and the rated maximum.
- Cable identity. SOP / SOP' / SOP" e-marker reads. Vendor and product IDs decoded against the USB-IF database. No invented specs when the cable does not answer.
- Data speed. USB 2.0, USB 3.x SuperSpeed, USB4, Thunderbolt. The lane state, not the marketing on the box.
- DisplayPort lane state. How many lanes, at what link rate (RBR, HBR, HBR2, HBR3, UHBR), whether the alt mode is actually active, and how many display sinks the controller sees.
- Connected devices. The accessories behind a hub or dock, identified by their USB host descriptor and physical port path.
- Plain-English explanation. An optional Apple Intelligence layer summarises the report. On-device only. Off by default.
Cable Detective has zero network. There is no server. No account. No telemetry. No analytics SDK. No crash reporting. The optional AI explanations run on Apple's on-device Foundation Models, on your Mac. If we wanted to phone home we would have to ship a new build with new entitlements. We do not.
Apple Silicon (M-series) Mac running macOS 26 (Tahoe) or later. Apple Intelligence is optional and can be enabled or disabled at any time.
One-time purchase. No subscription. Lifetime use of the version you bought. Family Sharing supported.
Bewertungen & Rezensionen
- Diese App hat noch nicht genügend Bewertungen oder Rezensionen erhalten, um eine Übersicht anzuzeigen.
Das Entwicklungsteam, Franz Enzenhofer, hat darauf hingewiesen, dass die Datenschutzrichtlinien der App den unten stehenden Umgang mit Daten einschließen können. Weitere Informationen findest du in den Datenschutzrichtlinien des Entwicklungsteams .
Keine Daten erfasst
Der Entwickler erfasst keine Daten von dieser App.
Bedienungshilfen
Der Entwickler hat noch nicht angegeben, welche Bedienungshilfen diese App unterstützt. Weitere Infos
Informationen
- Größe
- 3,1 MB
- Kategorie
- Dienstprogramme
- Kompatibilität
Erfordert macOS 26.0 (oder neuer) und einen Mac mit Apple M1-Chip (oder neuer).
- Mac
Erfordert macOS 26.0 (oder neuer) und einen Mac mit Apple M1-Chip (oder neuer).
- Mac
- Altersfreigabe
4+
- 4+
- Anbieter
Franz Enzenhofer
- Franz Enzenhofer hat sich als Händler für diese App ausgewiesen und bestätigt, dass dieses Produkt oder diese Dienstleistung dem Recht der Europäischen Union entspricht.
- Adresse
Fröbelgasse 62/8-9
1160 Vienna
Österreich - Telefonnummer
+43 67762377236 - E-Mail
team@fullstackoptimization.com
- Copyright
- © 2026 Franz Enzenhofer / fullstackoptimization.com
```

---

## 17. Show HN: nocal is a calendar that turns your week into a workspace

- 日期: 2026-05-09 11:48
- 链接: https://nocal.app/

```
Step 01
Agent context retrieval
Cursor, Claude, or ChatGPT calls nocal MCP tools to find the right note history and current project context.
Notes, calendar, and tasks with built-in MCP for AI agents
Employees at world-class brands use nocal to maximize their productivity
Transform your weekly view into your command center. Write in Markdown, embed rich components, and see your entire week holistically.
Build your weekly plan with powerful components. Everything you need, right in your calendar.
Built-in MCP server
Cursor, ChatGPT, and Claude can read real context from nocal and write results back into structured notes, so your work stays organized instead of disappearing into chat history.
How MCP flows
Step 01
Cursor, Claude, or ChatGPT calls nocal MCP tools to find the right note history and current project context.
Step 02
Your model turns fragmented context into clear outputs: release notes, plans, summaries, and action lists.
Step 03
The output is written back into nocal notes with safe patch semantics, so work survives beyond chat history.
See your schedule without being overwhelmed. nocal surfaces what's next, then fades into the background, letting you focus on what matters.
Stop switching between apps. Prepare for meetings, take notes, and track action items directly from within your calendar.
A unified inbox for your personal and work events. Easily triage and respond in real time. See what needs your attention for the week ahead.
Reference meetings in your notes and notes in your meetings. Create a connected workspace that grows with your projects and builds institutional knowledge.
Start organizing your calendar today. Available for Mac and Windows.
```

---

## 18. Show HN: Anycrap – REST API for 35k absurdist AI-generated products

- 日期: 2026-05-09 11:26
- 链接: https://anycrap.shop/developers

```
Quick start
curl
curl https://anycrap.shop/api/v1/products/random \ -H "Authorization: Bearer YOUR_API_KEY"
response
{ "data": [{ "id": "1a156178-0240-4c3e-861c-47b6568123f0", "slug": "thought-cancelling-headphones", "name": "Thought-Cancelling Headphones", "description": "Headphones that don't just block sound — they block thoughts.", "image": "https://cdn.crapify.me/products/...", "categories": ["gadgets", "anti-productivity"], "created_at": "2025-05-04T13:37:13.051Z" }] }
Endpoints
GET
/api/v1/products
List products (paginated, filterable)GET
/api/v1/products/random
Random product(s)GET
/api/v1/products/:slug
Single product by slugGET
/api/v1/categories
All categories with countsPOST
/api/v1/keys
Register API key (no auth required)Rate limit: 60 requests/minute per key. All endpoints return JSON with CORS headers.
See the full API reference for query parameters, filters, and response schemas.
35,000+ absurdist products in your terminal.
bash
# install once npm i -g anycrap anycrap key ak_your_key # or just use npx npx anycrap random npx anycrap random -c food npx anycrap search "underwater" npx anycrap categories
Drop-in for faker.commerce.productName()
— no API key, no network calls, works offline.
npm i anycrap-faker
import { faker } from '@faker-js/faker'; import { createAnycrapFaker } from 'anycrap-faker'; const anycrap = createAnycrapFaker(faker); anycrap.productName(); // "Thought-Cancelling Headphones" anycrap.productDescription(); // "Headphones that don't just block sound..." anycrap.productSlug(); // "thought-cancelling-headphones" anycrap.product(); // { name, slug, description, category }
Get your API key
Free. No credit card. Instant.
```

---

## 19. Show HN: Concord – Feature rich TUI for discord

- 日期: 2026-05-09 11:22
- 链接: https://github.com/chojs23/concord

```
Concord is TUI client for discord with discord like layout (Servers / Channels / Messages / Members), vim keys, inline image previews via Kitty/iTerm2/Sixel, reactions, polls, threads, forums, and more!(except voice calls, will be implemented)
Sits at ~20–40 MB idle. Concord is built with ratatui and crossterm. Here are features:
- Login by token, email/password or QR code from the mobile app
- Discord like layout : Servers / Channels / Messages / Members
- Vim-style keys (hjkl, g/G, Ctrl+d/Ctrl+u, Tab to cycle panes), plus mouse support
- Send, edit, delete, and reply to messages, with mention autocomplete
- Threads, forum posts (active and archived), pinned messages, mark-as-read
- Reactions (Unicode + custom emoji), poll voting, who-reacted lists
- Inline image previews via Kitty, iTerm2, or Sixel protocols (halfblock fallback for anything else)
- Avatar and custom emoji rendering, full-screen image viewer
- Live typing indicators, unread + mention counts
- Attachment downloads
- Message notification If you try, please let me know your experience. 
 Comments URL: https://news.ycombinator.com/item?id=48074027 
 Points: 6 
 # Comments: 2
```

---

## 20. Show HN: DuoSolve – Daily grammer practice game

- 日期: 2026-05-09 10:55
- 链接: https://duobook.co/duosolve

```
Hi all, I made a simple daily practice game the logic is pretty simple. You select the words you think are composing the translated sentence, it shows whether the word is at the right place or not for that try. You could change the language (also swap) and the level as well. Enjoy! 
 Comments URL: https://news.ycombinator.com/item?id=48073889 
 Points: 1 
 # Comments: 0
```

---
