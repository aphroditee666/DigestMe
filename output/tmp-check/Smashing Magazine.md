# Smashing Magazine

> 分类: 科技媒体
> URL: http://rss1.smashingmagazine.com/feed/
> 抓取: 30 篇

---

## 1. The Architecture Of Local-First Web Development

- 日期: 2026-05-06 10:00
- 链接: https://smashingmagazine.com/2026/05/architecture-local-first-web-development/

```
Last October, I was sitting in a hotel room in Lisbon, the night before I was supposed to demo a project management tool my team had spent four months building. The hotel Wi-Fi was doing that thing where it connects but nothing actually loads. And I watched our app, this thing I was genuinely proud of, render a blank screen with a spinner. Then a timeout error. Then nothing. 
 I pulled out my phone, tethered to cellular, and got a shaky connection. The app loaded, but every click was a two-second wait. Create a task? Spinner. Move a task between columns? Spinner. I sat there thinking: we built a front end in React, a back end in Node, a Postgres database, a Redis cache, a GraphQL API with six resolvers just for the task board. All that infrastructure, and the damn thing can’t show me my own data without a round-trip to a server 3,000 miles away. 
 That was the night I started seriously looking at local-first architecture . Not because I read a blog post or saw a tweet. Because I was embarrassed . 
 I want to be upfront about something: I spent the first year or so dismissing local-first as academic. I read the Ink & Switch “Local-First Software” paper when it came out in 2019 and thought, “Cool research, not practical for real apps.” I was wrong. The tooling in 2019 genuinely wasn’t ready. But I was also being lazy, defaulting to the architecture I already knew. The paper laid out seven ideals for software: fast, multi-device, offline, collaboration, longevity, privacy, user ownership . And I remember thinking those sounded like a wish list, not engineering requirements. 
 Seven years later, I’ve shipped three production apps using local-first patterns. I’ve also ripped local-first out of two projects where it was the wrong call. I have opinions. Some of them are probably wrong. But they’re earned. 
 So here’s what I actually think about building local-first web apps in 2026, written for developers who’ve been doing this long enough to be skeptical of silver bullets. 
 What “Local-First” Actually Means (And The Confusion That Won’t Die) I need to clear something up because I keep having this conversation at meetups. Local-first is not offline-first. It’s not “add a service worker and call it a day.” It’s not a synonym for PWA. I’ve seen all of these conflated in conference talks, and it drives me a little crazy. 
 Offline-first means your app handles network loss gracefully, but the server is still the source of truth . When the network comes back, the server wins. Cache-first (service workers caching responses) is a performance optimization. You’re serving stale data faster, which is great, but you haven’t changed who owns the data. PWAs are a delivery mechanism: installable, cached, push notifications. None of these is a data architecture. 
 Local-first is a data architecture. Your user’s device holds the primary copy of their data. The app reads and writes to a local database. Renders instantly. Syncs with servers or other devices in the background. The server, when it exists, is a sync peer with some special authority (authentication, backup, access control). But it’s not the gatekeeper. 
 The Ink & Switch paper defined seven ideals, and I think they still hold up. But the one that matters most in practice, the one that changes how you build everything, is this: 
 The client is not a thin view requesting permission to show data. The client is a node in a distributed system with its own database. 
 That distinction sounds subtle. It isn’t. It changes your entire stack. 
 Be Honest Early: When You Should Not Do This I’m putting this near the top because I’ve watched too many developers (including myself, once) get excited about a new architecture and shoehorn it into projects where it doesn’t belong. I wasted about six weeks trying to make a local-first approach work for an internal analytics dashboard at a previous job. My colleague Sarah finally pulled me aside and said, “The data is generated on the server. There’s nothing to replicate to the client. What are you doing?” She was right. 
 Local-first is a bad fit when your data is primarily server-generated. Analytics dashboards, social media feeds, search results: the server produces this data, so the client consuming it via API requests is completely fine. 
 It’s wrong for systems that need strong transactional consistency. Banking, payment processing, and inventory management. If two people try to buy the last item in stock, you need a single authoritative database making that decision with ACID guarantees. Eventual consistency will lose you money, or worse. 
 It’s overkill for simple CRUD apps with no offline or collaboration needs. If you’re building an internal admin panel used by five people in an office with good internet, adding a sync engine is over-engineering. And it’s physically impractical for massive datasets that won’t fit on client devices. 
 But here’s where it shines: note-taking, document editing, collaborative design tools, project management, field apps with unreliable connectivity, basically anything where data privacy is a selling point , as well as anything with real-time collaboration . In other words, it’s great for user-generated data that benefits from instant interaction and should survive the server going down. 
 One more thing I wish someone had told me earlier: you don’t have to go all-in. I’ve had the best results using local-first for specific features within otherwise traditional apps. Offline drafts in a blog editor. Real-time collaborative notes inside a project management tool that’s otherwise standard REST. 
 The “spectrum of local-first” is a real thing, and starting with one feature is how I’d recommend anyone begin. 
 Replicas, Not Requests If you’ve used Git, you already understand the mental model. 
 SVN (remember SVN?) was centralized. One server. You check out files, make changes, and commit to the server. Server down? Can’t commit. Can’t even see history. 
 Git gave every developer a full clone. You commit locally, branch locally, and merge locally. Push and pull when you’re ready. The remote repository is important, but it’s not the only copy of the truth. 
 Local-first web development is Git for application data. Every client device holds a replica (full or partial) of the relevant data. Writes happen locally. Sync is push/pull in the background. Conflicts get resolved through defined merge strategies. 
 I remember the first time this clicked for me in practice. I was prototyping a task board, and I wrote a function to add a task. In our old architecture, it would be: 
 POST to API. 
 Wait for the response. 
 If success, update the local state. 
 If failure, show error toast and maybe roll back optimistic update. 
 In the local-first version, it was: write to local SQLite, done. The UI updated instantly because it was reading from the same local database. Sync happened whenever. No loading state, no error handling for the write itself, no optimistic update logic (because there’s nothing to be “optimistic” about; the local write is the state). 
 The implications ripple through everything. You don’t need React Query or SWR for data fetching, because you’re not fetching. You don’t need Redux or Zustand for server-derived state, because the local database is your state. Your routing doesn’t trigger API calls. Authentication works differently because the server isn’t checking permissions on every read. 
 Here’s a visual comparison that might help if you’re the kind of person (like me) who thinks spatially: 
 On the left, every user interaction is a round-trip. Click, wait, render. On the right, reads and writes hit the local database directly. The sync server is still there, but it’s doing its work in the background. The user never waits for it. That’s the fundamental shift. 
 But I’m getting ahead of myself. Before we can talk about sync and conflicts, we need to talk about where the data actually lives on the client. 
 Where Data Lives on the Client Forget localStorage . It’s synchronous (blocks the main thread), caps at 5-10 MB, and only stores strings. It’s fine for a theme preference. It’s not a database. 
 IndexedDB is the workhorse that nobody loves. It’s in every browser, it’s asynchronous, it can handle hundreds of megabytes, and its API is absolutely miserable to work with. I’ve used it directly a grand total of once. Now I use it through abstractions or, more often, I don’t use it at all. 
 Because the real story in 2026 is SQLite running in the browser via WebAssembly. 
 I know that sounds like a party trick, but it’s not. SQLite compiled to WASM, persisted to the Origin Private File System (OPFS), gives you a real relational database in the browser. Full SQL queries. Transactions. Indexes. The works. 
 OPFS is the newer API that makes this practical. It gives web apps a sandboxed file system with high-performance synchronous access (in Web Workers), which is exactly what SQLite needs. Before OPFS, you could run SQLite in memory and manually persist to IndexedDB, which worked but was slow and fragile. 
 Here’s roughly what initialization looks like in a real project (I’m using wa-sqlite here, which is the library I’ve had the best luck with): 
 import { SQLiteAPI } from 'wa-sqlite';
import { OPFSCoopSyncVFS } from 'wa-sqlite/src/examples/OPFSCoopSyncVFS.js';

async function initDatabase() {
 const module = await SQLiteAPI.initialize();
 const vfs = new OPFSCoopSyncVFS('pm-tool-db');
 await vfs.initialize(module);

 const db = await module.open_v2('workspace.db');

 // HACK: wa-sqlite doesn't handle concurrent writes well on Safari,
 // so we serialize through a queue. See vlcn-io/wa-sqlite#247
 await module.exec(db, PRAGMA journal&#95;mode=WAL );

 await module.exec(db, CREATE TABLE IF NOT EXISTS tasks (
 id TEXT PRIMARY KEY,
 title TEXT NOT NULL,
 status TEXT DEFAULT 'backlog',
 assignee&#95;id TEXT,
 project&#95;id TEXT NOT NULL,
 position REAL DEFAULT 0,
 created&#95;at TEXT DEFAULT (datetime('now')),
 updated&#95;at TEXT DEFAULT (datetime('now'))
 ) );

 return db;
} 
 In production, I wrap all database access in a write queue that serializes mutations. I also log every failed write to Sentry with the full SQL statement (scrubbed of PII, obviously) because debugging database issues in a user’s browser is hell without that telemetry. 
 A gotcha I wasted almost two days on: Safari’s OPFS implementation behaves differently from Chrome’s in subtle ways. Specifically, I hit a bug where createSyncAccessHandle() would silently fail in certain iframe contexts on Safari 18. There’s no error, no exception. It just doesn’t work. I ended up falling back to IndexedDB-backed persistence on Safari, which was slower but at least functioned. (I’m told Safari 19/26 fixes this, but I haven’t verified it yet.) 
 Quick comparison of the options I’ve actually used: 
 Storage Good For Watch Out For 
 IndexedDB Broad compatibility, moderate data Terrible DX, no SQL, verbose 
 OPFS + SQLite WASM Relational data, complex queries, serious apps Safari quirks, ~400KB bundle addition 
 PGlite (Postgres in WASM) Full Postgres compatibility on client Newer, larger bundle, still maturing 
 I’ve also tried cr-sqlite , which adds CRDT column support directly to SQLite tables. Clever idea, but I found it too early-stage for production use when I evaluated it in late 2025. The merge semantics were sometimes surprising, and debugging CRDT state inside SQLite was painful. I’d revisit it later this year. 
 The Part That’s Actually Hard Storing data locally is a solved problem. Syncing it reliably across devices and users is where you earn your gray hairs. 
 When multiple replicas can independently read and write, you need a mechanism to reconcile changes. There are basically four approaches, and I’ve used three of them. 
 CRDTs (Conflict-Free Replicated Data Types) are data structures designed so that concurrent edits can always be merged without conflicts, mathematically guaranteed. Yjs is the most popular implementation in JavaScript, and it’s genuinely excellent for real-time collaborative text editing. I used it to build a collaborative document editor at my last company, and the experience was mostly good, though I’ll get into the pain points in the conflict resolution section. 
 Here’s what setting up a shared Yjs document looks like in practice: 
 import * as Y from 'yjs';
import { WebsocketProvider } from 'y-websocket';

const ydoc = new Y.Doc();

const provider = new WebsocketProvider(
 'wss://sync.our-app.dev',
 'workspace-a1b2c3d4',
 ydoc
);

const tasks = ydoc.getMap('tasks');

// Add a task
const task = new Y.Map();
task.set('title', 'Review Q3 roadmap draft');
task.set('completed', false);
task.set('assignee', 'maria');
// TODO: type this properly once; yjs exports better TS types
// for nested maps. For now, this works fine.
tasks.set('f47ac10b-58cc-4372-a567-0e02b2c3d479', task as any);

tasks.observeDeep(() => {
 // Re-render UI. In practice, I debounce this to ~16ms
 // because observeDeep fires a LOT during active collaboration
 renderTaskList(tasks.toJSON());
}); Automerge is the other major CRDT library, backed by Rust and with a document-oriented model. I’ve used it less, but I know teams who swear by it. Loro is newer, Rust-based, and claims better performance. I haven’t shipped anything with Loro yet. 
 Database replication is the other big approach, and honestly, for most apps that don’t need Google Docs-style real-time text editing, I think it’s the better choice. The idea is straightforward: replicate rows between a server database (Postgres) and a client database (SQLite) with a sync engine managing the plumbing. 
 PowerSync does this well. It gives you one-way replication from Postgres to client SQLite with a write-back path for mutations. ElectricSQL is more ambitious, going for full active-active sync between Postgres and SQLite. I’ve used PowerSync in production and ElectricSQL in prototypes. PowerSync felt more stable when I evaluated them both in early 2026, but ElectricSQL’s approach is more powerful if they nail the execution. 
 Triplit takes a different angle entirely: it’s a full-stack database with sync built in, so you don’t think about “client DB” and “server DB” separately. I haven’t tried it beyond a weekend prototype, but the developer experience was surprisingly nice. 
 Event sourcing (syncing a log of mutations rather than the current state) is the approach LiveStore takes. I find it intellectually appealing and occasionally useful, but in practice, I’ve found that reconstructing state from an event log adds complexity that most apps don’t need. My controversial opinion: Event sourcing is over-recommended for application development. It’s great for audit logs and certain domains, but for a task board? Just sync the rows. 
 Not everyone will agree with that. I know event sourcing has passionate advocates, and I’ve been told I’m wrong about this at least twice at conferences. Maybe I just haven’t built the right app for it yet. 
 Conflicts: The Thing Everyone’s Afraid Of I used to think conflict resolution was a terrifying, unsolvable problem. After building three apps that handle it, I’d revise that to: it’s a manageable problem that requires you to think carefully about your specific data model, and most developers overthink it. 
 Conflicts happen when two replicas modify the same data without seeing each other’s changes. User A edits a task title on their phone while offline. User B edits the same title on their laptop. Both come back online. Now what? 
 My first attempt at handling this was embarrassingly naive: 
 // My first try. Don't do this.
function resolveConflict(local: any, remote: any) {
 // just... take the remote one? sure?
 return remote;
} The problem is obvious: local changes get silently dropped. User A edits a title, syncs, and their edit vanishes. They don’t even know it happened. 
 What actually works for most cases is last-write-wins (LWW) at the field level, not the record level. If User A changes the title and User B changes the due date, you keep both changes because they touched different fields. You only have a real conflict when both modified the same field, and then you pick the later timestamp. 
 interface FieldValue {
 value: string | number | boolean;
 // ISO timestamp with enough precision to break most ties
 updatedAt: string;
 // Client ID as tiebreaker when timestamps match.
 // This happens more often than you'd think.
 clientId: string;
}

function pickWinner(a: FieldValue, b: FieldValue): FieldValue {
 const timeA = new Date(a.updatedAt).getTime();
 const timeB = new Date(b.updatedAt).getTime();
 if (timeA !== timeB) return timeA > timeB ? a : b;
 // Deterministic tiebreaker when timestamps match
 return a.clientId > b.clientId ? a : b;
}

// In practice, I apply this per-field across the whole record.
function mergeTask(local: Record<string, FieldValue>, remote: Record<string, FieldValue>) {
 const merged: Record<string, FieldValue> = {};
 const allKeys = new Set([...Object.keys(local), ...Object.keys(remote)]);
 for (const key of allKeys) {
 if (!local[key]) { merged[key] = remote[key]; continue; }
 if (!remote[key]) { merged[key] = local[key]; continue; }
 merged[key] = pickWinner(local[key], remote[key]);
 }
 return merged;
} 
 In our production app, this handles about 95% of conflicts without any user-visible issues. For the remaining cases (two people editing the same text field), LWW means one person’s edit silently wins. For a task title? Honestly, that’s usually fine. For a document body? No. That’s where CRDTs earn their keep. 
 But there’s a subtler problem I didn’t appreciate until I hit it: semantic conflicts . Data merges cleanly at the structural level, but the result is nonsensical. Two users, both offline, book the same 2 PM meeting slot with different meetings. Field-level merge accepts both writes because they’re writing to different records. No structural conflict. But you’ve got a double-booking, and your merge function has no idea that’s a problem. 
 Semantic conflicts require application-level validation, and that has to happen on the server during sync. Your sync engine merges the data structurally, but your server needs to check domain invariants before accepting the result. The approach I’ve landed on (after getting it wrong twice) is: validate on the server during the write-back phase, but flag violations rather than silently rejecting them. 
 Here’s what I mean. When the client pushes mutations to the server during sync, the server runs them through a constraint validation layer before applying them to Postgres: 
 interface SyncViolation {
 type: 'scheduling_conflict' | 'capacity_exceeded' | 'stale_assignment';
 recordId: string;
 description: string;
 // The conflicting records so the client can show context
 conflictingRecords: string[];
 // When was this violation detected
 detectedAt: string;
}

async function validateSyncBatch(
 mutations: SyncMutation[],
 serverDb: Database
): Promise<{ accepted: SyncMutation[]; violations: SyncViolation[] }> {
 const accepted: SyncMutation[] = [];
 const violations: SyncViolation[] = [];

 for (const mutation of mutations) {
 if (mutation.table === 'calendar_events') {
 // Check for double-booking
 const overlapping = await serverDb.query( SELECT id, title FROM calendar&#95;events
 WHERE room&#95;id = ? AND id != ?
 AND start&#95;time &lt; ? AND end&#95;time &gt; ? ,
 [mutation.data.room_id, mutation.data.id,
 mutation.data.end_time, mutation.data.start_time]
 );

 if (overlapping.length > 0) {
 violations.push({
 type: 'scheduling_conflict',
 recordId: mutation.data.id,
 description: Conflicts with "${overlapping[0].title}" ,
 conflictingRecords: overlapping.map(r => r.id),
 detectedAt: new Date().toISOString()
 });
 // Still accept the write, but flag it
 // The alternative is rejecting it, but then the user's
 // local state and server state diverge, and that's worse
 accepted.push(mutation);
 continue;
 }
 }
 accepted.push(mutation);
 }

 return { accepted, violations };
} 
 The key decision here — and I went back and forth on this — is that we accept the conflicting write and flag it, rather than rejecting it outright. If you reject it, the user’s local database has a record that the server refuses to acknowledge, and now you’re in a state divergence situation that’s genuinely hard to recover from. I tried the rejection approach first, and it led to ghost records on the client that users couldn’t delete because they didn’t exist on the server. Nightmare. 
 So instead, the server accepts the write, stores the violation, and syncs the violation back to the client. The client shows a non-blocking notification: “Your meeting ‘Q3 Planning’ conflicts with ‘Design Review’ in Room B at 2 PM. Tap to resolve.” The user taps, sees both meetings, and picks one to reschedule or cancel. The resolution is a normal write that syncs back. 
 Is this perfect? No. There’s a window between when the violation is created and when the user resolves it, where both conflicting records exist. For meeting rooms, that’s tolerable. For something like inventory management where two people “buy” the last item, that window is unacceptable, and that’s exactly why I said earlier that local-first is wrong for systems requiring strong transactional consistency. 
 I’m still iterating on this pattern. The violation table grows if users ignore notifications (we expire them after 72 hours, which feels arbitrary). And deciding which invariants to validate on the server requires you to essentially maintain a parallel set of business rules outside your client-side application logic. It’s not elegant. But it works, and it’s the best approach I’ve found for the class of apps I’m building. If you’ve built something cleaner, I genuinely want to hear about it. 
 For CRDTs like Yjs, conflict resolution at the character level (for text) works remarkably well. Two people typing in the same paragraph will see both sets of characters appear in a sensible order. But CRDT merging of structured data (maps, arrays, nested objects) can produce results that surprise you. I once watched a Yjs-backed task list duplicate items after a merge because two users had reordered the same list offline, and the CRDT’s list merge semantics interleaved their orderings. Technically correct. Practically confusing. We ended up adding a post-merge de-duplication step, which felt like a hack but solved the problem. 
 When should you surface conflicts to the user, Git-style? In my experience, almost never for typical app data. Users don’t want to resolve merge conflicts. They want the app to figure it out. The exception is high-stakes content: legal documents, medical records, anything where silently dropping an edit could cause real harm. 
 The Tools Right Now I’m going to give you my honest read on the tools available as of mid-2026, with the caveat that this space is moving fast enough that some of this might be outdated by the time you read it. 
 Yjs is the most mature CRDT library. Production-ready, huge community, integrates with most collaborative editors (TipTap, BlockNote, Lexical). If you need real-time collaborative editing, start here. 
 Automerge is solid, Rust-backed, and takes a more document-oriented approach than Yjs. I’ve seen it used well in apps where the data model fits a document metaphor. Fewer integrations than Yjs, but the core is well-engineered. 
 PowerSync is what I’d recommend for teams that have an existing Postgres back-end and want to add offline support. It’s production-ready, the docs are good, and the mental model (Postgres syncs to client SQLite, client writes go through a defined upload path) is easy to reason about. In our app, initial sync for a workspace with around 5,000 tasks takes about 1.2 seconds on a decent connection and about 3.5 seconds on a throttled 3G simulation. That was acceptable for us. 
 ElectricSQL is going for something more ambitious: true active-active replication between Postgres and SQLite, with “shapes” defining what data syncs to which client. I want this to succeed because the developer experience in prototypes was excellent. But when I evaluated it for production in February 2026, I hit enough rough edges (particularly around shape management and reconnection behavior) that I went with PowerSync instead. I plan to revisit it. 
 Triplit impressed me in a weekend prototype. Full-stack database with sync built in, nice TypeScript API. I haven’t stress-tested it with real production load, and I’d want to before committing. 
 Zero (from Rocicorp, the Replicache people) is interesting because it takes a query-based approach to sync, which is different from the row-replication model. Replicache was sunset in favor of Zero, which tells you something about how fast approaches are evolving in this space. Worth watching, but I wouldn’t build on it yet for a production app. 
 TinyBase is a lightweight reactive store that’s great for smaller apps or prototyping. I used it for a personal side project (a reading tracker) and liked it a lot. Not sure I’d use it for a team-scale product. 
 PGlite (Postgres compiled to WASM) is wild. Same SQL dialect on client and server. Combined with ElectricSQL, you could theoretically run identical queries everywhere. I think this is where things are heading long-term, but PGlite’s bundle size and memory footprint are still concerns for mobile browsers. 
 One thing the Replicache sunset taught me: don’t bet your architecture on a single tool from a small company without a fallback plan. I keep my sync layer abstracted enough that I could swap engines in a few weeks, not months. I know that sounds like premature abstraction, but in a space this young, I think it’s just prudence. 
 Building A Real App: Architecture, Auth, And Migrations I want to walk through how I actually structure a local-first app in practice, because the layer diagrams you see in blog posts rarely match what the code looks like. 
 My current stack for a collaborative project management tool looks like this: 
 UI: React components that never call fetch() for data reads. 
 Query layer: useLiveQuery hooks that subscribe to the local SQLite database and re-render automatically when data changes. 
 Local database: SQLite via wa-sqlite, persisted to OPFS. 
 Mutation layer: Plain INSERT / UPDATE / DELETE statements against local SQLite. 
 Sync: PowerSync managing replication between local SQLite and our Postgres back-end. 
 Server: Postgres, a Node.js auth service, and a small sync validation layer. 
 The component code ends up looking almost absurdly simple compared to what I used to write: 
 import { useLiveQuery } from '@powersync/react';
import { db } from '../lib/database';

function TaskBoard({ projectId }: { projectId: string }) {
 const tasks = useLiveQuery( SELECT &#42; FROM tasks WHERE project&#95;id = ? AND archived = 0 ORDER BY position ,
 [projectId]
 );

 async function addTask(title: string) {
 await db.execute( INSERT INTO tasks (id, title, project&#95;id, position, created&#95;at)
 VALUES (?, ?, ?, ?, datetime('now')) ,
 [crypto.randomUUID(), title, projectId, tasks.length]
 );
 // That's it. useLiveQuery picks up the change automatically.
 // No invalidation, no refetch, no loading state.
 }

 // No isLoading check. Data is local. It's always there after the first sync.
 return (
 <div>
 {tasks.map(task => <TaskCard key={task.id} task={task} />)}
 <NewTaskInput onSubmit={addTask} />
 </div>
 );
} 
 Compare that to the React Query + REST equivalent, which would be at least twice the code and include loading states, error states, optimistic update logic with rollback, and cache invalidation. I don’t miss it. 
 Auth In A Local-First World 
 Authentication works roughly the same as traditional apps: JWT tokens, OAuth flows, and session management. The token authenticates the sync connection rather than every individual request. Offline access works because the data is already local. The user was authenticated when the data was originally synced. 
 Authorization is trickier, and I think most local-first articles under-explain this. You cannot sync your entire database to every client and rely on client-side code to hide unauthorized data. Someone will open DevTools, find the local SQLite file, and see everything. The client is not a trust boundary. 
 You enforce authorization at the sync layer. PowerSync has “sync rules” that define which rows go to which clients. ElectricSQL has “shapes.” Either way, the server only sends data that the user is authorized to see. When the client sends writes back, the server validates them against authorization rules before applying them to Postgres. If a user tries to modify something they shouldn’t, the server rejects it during sync. 
 I also want to mention end-to-end encryption (E2EE) , because it pairs naturally with local-first. Since data lives on the client, you can encrypt it before sync. The server stores and relays encrypted blobs it can’t read. Apps like Anytype do this. We haven’t implemented E2EE in our current app, but it’s on the roadmap for when we handle more sensitive data. 
 Schema Migrations On A Thousand Devices 
 This one caught me off guard the first time. On the server, you run a migration against one database you control. On the client, every user has their own database that might be running any version of your schema, depending on when they last opened the app. 
 I use a simple migration runner that checks a version number at app startup: 
 const MIGRATIONS = [
 {
 version: 1,
 sql: CREATE TABLE IF NOT EXISTS tasks (
 id TEXT PRIMARY KEY,
 title TEXT NOT NULL,
 status TEXT DEFAULT 'backlog',
 project&#95;id TEXT NOT NULL,
 created&#95;at TEXT DEFAULT (datetime('now'))
 ); },
 {
 version: 2,
 // Added priority and due_date in sprint 4
 sql: ALTER TABLE tasks ADD COLUMN priority INTEGER DEFAULT 0;
 ALTER TABLE tasks ADD COLUMN due&#95;date TEXT; },
 {
 version: 3,
 // Denormalized assignee name for offline display.
 // Yes, I know this is a trade-off. The JOIN was killing
 // performance on low-end Android devices.
 sql: ALTER TABLE tasks ADD COLUMN assignee&#95;name TEXT DEFAULT ''; }
];

async function runMigrations(db: Database) {
 await db.execute( CREATE TABLE IF NOT EXISTS &#95;schema&#95;version (version INTEGER) );

 const rows = await db.execute('SELECT version FROM _schema_version');
 const currentVersion = rows.length > 0 ? rows[0].version : 0;

 for (const migration of MIGRATIONS) {
 if (migration.version > currentVersion) {
 console.log( Migrating local DB to v${migration.version} );
 await db.execute('BEGIN');
 try {
 await db.execute(migration.sql);
 await db.execute(
 'INSERT OR REPLACE INTO _schema_version (rowid, version) VALUES (1, ?)',
 [migration.version]
 );
 await db.execute('COMMIT');
 } catch (err) {
 await db.execute('ROLLBACK');
 // In production, this fires a Sentry alert with the
 // migration version and error details
 throw err;
 }
 }
 }
} 
 Design your migrations to be additive. New columns with defaults. New tables. Don’t rename or drop columns unless you absolutely must, because users running old app versions will still be syncing data, and your server needs to handle the mismatch. I learned this the hard way when I dropped a column that an older client was still writing to, which caused silent sync failures for about 200 users over a weekend. Not fun. 
 If I Were Starting A New Project Today I get asked this a lot, so here’s my current answer. It changes every six months or so. 
 For a collaborative app with real-time features and offline support, I’d start with: React on the front end, PowerSync for sync, SQLite via wa-sqlite on the client (persisted to OPFS with IndexedDB fallback for Safari), and Supabase (which gives me Postgres, auth, and row-level security out of the box). I’d use Yjs only if I needed rich text collaboration, and I’d avoid it if I didn’t, because CRDTs add meaningful complexity to your data model. 
 For a simpler app where I mostly need offline support and instant reads but collaboration is secondary, I might skip the sync engine entirely and just use a local SQLite database with a custom sync layer that pushes/pulls from a REST API. I know that sounds like reinventing the wheel, but for simple cases, a custom sync that you fully understand is better than a general-purpose sync engine that adds concepts you don’t need. 
 I would not currently use ElectricSQL or Zero for production, not because they’re bad, but because I want another 6-12 months of maturity before I’d trust them for something I’m on-call for. I’ve been burned before by building on early-stage infrastructure (I was an early Meteor adopter, if that tells you anything) and I’m more cautious now about where I accept novelty risk. 
 Performance: What’s Actually Fast And What Hurts Reads are instant. That’s not marketing. Querying a local SQLite database for a list of 500 tasks takes under two milliseconds on my M2 MacBook and about eight milliseconds on a mid-range Android phone. No network. No spinner. No loading state. 
 Writes are instant, too. INSERT INTO tasks runs locally, the UI updates reactively, and sync happens whenever. Users perceive writes as instantaneous because they are. 
 Initial sync is where you pay the cost. Bootstrapping the local replica on first load (or on a new device) means downloading potentially megabytes of data. In our app, a workspace with 5,000 tasks, 200 projects, and 50 users takes about 1.2 seconds on broadband and four to five seconds on a slow mobile connection. We mitigate this with partial sync (only sync the user’s active projects) and by showing a one-time “Setting up your workspace” screen during the first sync. After that initial sync, incremental updates are tiny. 
 Bundle size is a real concern. SQLite compiled to WASM adds roughly 400KB gzipped to your JavaScript bundle. That’s not trivial, especially if you care about Time to Interactive on mobile. I lazy-load the database module with dynamic import() so it doesn’t block the initial render. 
 Memory is the other gotcha. SQLite WASM runs in memory, and on mobile browsers with aggressive memory limits, a large database can cause tab crashes. I haven’t found a great solution for this beyond keeping the synced dataset small through partial sync and being aggressive about pruning old data. 
 Note : Speaking of memory issues, I’ve been reading Designing Data-Intensive Applications by Martin Kleppmann for the third time. Every re-read, I catch something new. If you haven’t read it and you’re thinking about distributed data, just stop and read it first. 
 Testing This Stuff I’ll keep this brief because the honest answer is that testing local-first apps is harder than testing traditional apps, and the tooling isn’t great yet. 
 What works for me: unit tests for merge logic (these are pure functions, easy to test), integration tests that spin up two client instances in memory and verify they converge after concurrent edits, and Playwright E2E tests that use context.setOffline(true) to simulate offline/online transitions. 
 What I haven’t figured out well: reproducing bugs that only happen during conflict resolution with specific timing. When a user reports that a task “lost its description,” I often can’t reproduce it because I don’t know exactly what sequence of offline edits and sync events led to the conflict. I’ve started logging sync events in more detail (what was sent, what was received, what conflicts were detected, how they were resolved) and shipping those logs to our observability stack. It helps, but it’s not as clean as I’d like. 
 Property-based testing with something like fast-check is genuinely useful for CRDT logic. Generate random operation sequences, apply them in random orders, and assert convergence. I wish I’d started doing this earlier. 
 What I’m Watching, What Worries Me I’m excited about where this is going. PGlite (full Postgres in the browser) feels like a glimpse of a future where the client/server data layer distinction just dissolves. You write SQL, it runs everywhere, sync is a runtime concern rather than an architectural decision. We’re not there yet, but you can see it from here. 
 I’m also watching the convergence of local-first and AI. Running models locally, keeping data on-device, using cloud AI only with explicit consent, and encrypted data. The privacy implications are compelling, and I think “your data never leaves your device” will become a real product differentiator as AI eats more of the software experience. 
 What worries me is fragmentation . Every sync engine uses its own protocol. There’s no standard. If ElectricSQL shuts down (it won’t, probably, but if ), migrating to PowerSync isn’t trivial. I abstract my sync layer partly for this reason, but it still makes me nervous. 
 The web has standards for nearly everything. We don’t have one for sync, and I don’t see one emerging soon. 
 I’m also worried about the complexity budget . Local-first adds real architectural complexity: sync engines, conflict resolution, client-side migrations, partial replication, and auth at the sync boundary. For a team of experienced developers building the right kind of app, that complexity pays for itself many times over. For a team that just needs a CRUD app, it’s a trap. 
 I keep coming back to something a developer named Kevin said to me at a local-first meetup in Berlin last year: 
 “The best architecture is the one your team can debug at 2 AM.” 
 He’s right. If local-first makes your app faster, more reliable, and better for users, and your team understands how the sync works, go for it. If you’re adding it because it sounds cool and you don’t fully understand the failure modes yet, build a prototype first. Learn where it breaks. Then decide. 
 I’m building my fourth local-first app right now: a collaborative planning tool for small teams, with offline support and optional E2E encryption. It’s the most ambitious thing I’ve attempted with this architecture. I’ll write about how it goes. 
 If you’re starting out, pick one feature in your current app that would benefit from instant local reads and offline writes. Add a local SQLite database. Wire up reactive queries. See how it feels. I think you’ll have the same reaction I did: oh, this is how it should have always worked. 
 Further Reading “ Local-First Software ” (Ink & Switch): This is still the best starting point. 
 “ CRDTs: The hard parts” ” (Martin Kleppmann, video): Martin’s talks on CRDTs are excellent. 
 The localfirstweb.dev community site: A good directory of tools. 
 PowerSync Documentation 
 ElectricSQL Documentation 
 Yjs Documentation 
 Automerge Documentation
```

---

## 2. Rethinking The Experience Of System Tools

- 日期: 2026-05-05 08:00
- 链接: https://smashingmagazine.com/2026/05/rethinking-experience-system-tools/

```
This article is a sponsored by MacPaw 
 Your grandmother’s vacuum was a trusty but ugly workhorse hidden in a dark closet. Dyson turned that practical tool into an aspirational product, one you love leaving out even when guests come over. Dish soap was just dish soap until Method put it in a glass container, and it became an addition to, not a distraction from, the aesthetics of your kitchen. Physical product brands spent the last two decades transforming mundane, practical items like soap and vacuums into must-have experiences. 
 But utility software — especially maintenance tools, a type of system software designed to analyze, configure, optimize, and maintain a computer — hasn’t made that leap from something you open as a chore to an experience you choose with excitement. And that means those brands are missing an interesting design opportunity: these tools are well overdue for a more intelligent, more human, and less emotionally flat approach. 
 “The Most Underexplored Frontier In UX Is The Maintenance Layer.” Utility software still feels like a chore. Using it has all the excitement of pulling out that dusty old vacuum from the back of the closet. These four common software design assumptions illustrate why the category hasn’t yet transcended its chore status. 
 Assuming the user already resents the task : they’re here because something is wrong, not because they chose to open this tool. Designing accordingly means assuming they want the software to be fast, clinical, invisible, and something to get out of the way, not get into. But a design built for resentment produces tools that deserve it. If you expect your users to want to get out of the product as fast as possible, they’ll feel it in the design. 
 Assuming function is enough and feelings are for consumer apps : emotion in interface design is decoration. The maintenance layer is infrastructure, and nobody decorates infrastructure. But nobody decorated dish soap either, until Method. They didn’t change the product, just the user’s relationship to the tool they use to accomplish a task. 
 Assuming your users are not your fans because nobody cares about maintenance tools : utility tools don’t build communities, and nobody posts about running a disk cleanup. But people care deeply about tools that respect their time and make complex things simple for them to use. The MacPaw team listens to our community and implements many of the features they ask for, because we know users can be fans too, and they should shape how our products work. 
 Assuming that designers shouldn’t waste pixels on personality : you need to hide complexity and show minimal UI. Utility software should look neutral, technical, and forgettable. 
 But when software hides the system, people lose trust in it. 
 Design always starts with function — function shapes form. But if that function can’t be made completely invisible and people still have to interact with it, it inevitably becomes part of their experience. In that case, people expect it not just to work, but to match their environment, influence their mood, and contribute to their overall experience. 
 A good example is a watch. Its core function is simple: show the time. But because a watch occupies physical space in a person’s world, you want more from it than just functionality. It needs to play an aesthetic role and complement the environment. 
 “The Maintenance Layer Is A Behavioral Problem, Not Just A UX One.” The user experience in utility software matters more than the industry tends to admit. In utility software, experience is not something added on top of function. It emerges from how the function is structured, explained, and interacted with. If you think you can design the most functional app on the market without considering how users understand and experience the process, you’re missing an opportunity to build a relationship with that user. 
 Part of that ignored UX element is a behavioral problem: users don’t avoid utility software because using it is hard, but instead because it produces no positive emotional signal at any point. The problem is rarely complex. It’s the absence of meaningful interaction during the process of using the app. 
 Another issue is focusing solely on function. The aesthetic-usability effect shows us clearly that if something looks better, it feels better — ATM screens in a 1995 study were judged easier to use if the screen layout was more attractive. Even something as purely functional as an ATM screen display needs attention to how the function is structured, presented, and perceived. 
 And then there’s the memory problem. People remember the emotional peak and the ending of an experience , not the average. A completed process that ends with a clear “done” is remembered more positively than one that just fades out, even if the end task is completed successfully in both cases. System tools rarely intentionally design the ending of an interaction — they just stop running. 
 “Thoughtful System Design Can Transform Maintenance From A Technical Chore Into A Seamless User Experience.” What does emotional design actually mean, then, in utility UX? Here are three principles the MacPaw team follows to design its products against the category norm. 
 Translating system complexity into human language 
 Maintenance tools deal with storage, task management, and background processes. Good design explains what’s happening, avoids system jargon, and communicates outcomes clearly. 
 Linear’s game-changing move that illustrates this principle was agreeing on straightforward units of work, like projects and teams, that any new user can immediately understand. That helps them spend less time ramping up and more time building. 
 Make the process clear and show progress 
 System tools run complex processes. Design should show progress, impact, and system change to create trust and control. 
 Vercel’s deployment infrastructure is an excellent example here. When you trigger a build, the browser tab favicon changes — a spinner while building, a green checkmark when done, a red X if it fails. It’s ruthlessly functional, not visual or warm, but it’s emotionally intelligent: it exists purely to reduce the low-level anxiety of waiting for a build to finish. 
 Design the moment of completion 
 Maintenance tasks often end quietly. But completion is the emotional payoff. Design should emphasize clarity of results, a sense of resolution, and visible improvement so users remember a positive and distinct ending. 
 Take the new CleanMyMac by MacPaw after its 2024 major update . Unlike the maintenance utility category norm, CleanMyMac uses visual language, including color, depth, motion, icons, and 3D illustrations, to shift the focus from diagnosing problems to showing progress: space cleared, threats removed, time saved. Instead of confronting the user with what's wrong, the interface closes with a picture of a machine that's already working better. 
 The task is the same, but the ending tells a different story, giving the user a picture of a machine that's already working better. 
 “Even if you don’t care about emotional design as a principle, the change is coming anyway.” The market is forcing this issue even for those who don’t find the argument I’ve made here compelling. 
 That’s partly generational — designers and users who grew up with Linear, Figma, and Notion have a completely different baseline for the tools they use. Good software is not a happy accident for them, but a given. That generation is now the primary audience for maintenance software, and so the old “it’s fine, it’s just a utility” excuse doesn’t work philosophically or commercially. Just like Dyson and Method changed how entire product categories approached design, the current state of utility software is shifting for good. 
 And digital fatigue is the current cultural state. The resurgence of vinyl records, film cameras, and dumbphones is not merely nostalgia, but a signal that the emotional relationship between people and their tools is changing. 
 The question has shifted from whether your utility software should feel better to use to whether it can afford not to.
```

---

## 3. Designing Stable Interfaces For Streaming Content

- 日期: 2026-05-01 08:00
- 链接: https://smashingmagazine.com/2026/05/designing-stable-interfaces-streaming-content/

```
More interfaces now render while the response is still being generated. The UI begins in one state, then updates as more data comes in. You see this in chat apps, logs, transcription tools, and other real-time systems. 
 The tricky part is that the interface is not in a fixed state ; it keeps changing as new content comes in. It grows where lines become longer and new blocks appear. Something that was just below the screen can suddenly move, and the user’s scroll position becomes harder to manage. Parts of the UI might even be incomplete while the user is already interacting with it. 
 In this article, we’ll take a simple interface and make it handle this properly. We’ll look at how to keep things stable, manage scrolling, and render partial content without breaking the reading experience. 
 What Does A Streaming UI Actually Look Like? I’ve built three demos that stream content in different ways: a chat bubble, a log feed, and a transcription view. They look different on the surface, but they all run into the same three problems. 
 The first is scroll . When content is streaming in, most interfaces keep the viewport pinned to the bottom. That works if you are just watching, but the moment you scroll up to read something, the page snaps back down. You did not ask for that. The interface decided for you, and now you’re fighting it instead of reading. 
 The second is layout shift . Streaming content means containers are constantly growing, and as they do, everything below shifts downward. A button you were about to click is no longer where it was. A line you were reading has moved. The page is not broken; it is just that nothing stays still long enough to interact with comfortably. 
 The third is render frequency . Browsers paint the screen around 60 times per second, but streams can arrive much faster than that. This means the DOM, which is the browser’s internal representation of everything on the page, ends up being updated for frames the user will never actually see. Each update still costs something, and that cost adds up quietly until performance starts to slip. 
 As you go through each demo, pay attention to where things start feeling off. That small moment of friction when the interface starts getting in your way. This is exactly what we are here to fix. 
 Example 1: Streaming AI Chat Responses This is the most familiar case. You click Stream , and the message starts growing token by token, just like a typical AI chat interface. 
 Here’s what I want you to try: 
 Click the Stream button. 
 Try scrolling upwards while the message is streaming. 
 Increase the speed (to something like 10ms). 
 You will notice something subtle but important: the UI keeps trying to pull you back down. Basically, it is making a decision for you about where your attention should be. 
 That’s one example. Let’s look at another. 
 Example 2: Live Processing In A Log Viewer This example looks different on the surface, but the problem is actually very similar to the first example. Rather than a message that gets longer over time, new lines are appended continuously, like a terminal or a log stream. 
 The interesting part here is the tail toggle. It makes the trade-off between interaction and stable interfaces very clear: 
 Again, here is what I want you to try: 
 Click the Start button. 
 Allow the logs to stream past the container’s height. 
 Scroll up to the beginning. 
 Stop the stream and disable the “tail” option. 
 Notice that, when tail is enabled, the UI follows the new content. But you’re unable to scroll up and stay in place. Instead, you need to stop the stream or enable “tail” to explore the content. 
 Example 3: Dashboard Displaying Real-Time Metrics In this case, the UI updates in place: 
 Numbers change, 
 Charts shift, 
 Values refresh continuously. 
 There is no scroll tension this time, but a different issue shows up. That’s what we’ll get into next. 
 Why The UI Feels Unstable And How To Fix It If you tried the chat demo and scrolled upward while the responses were coming in, you may have spotted the first issue right away: the UI keeps pulling you back down to the latest streamed content as it updates. This takes you out of context and never allows you the time to fully digest the content once it has passed. 
 We see that exact same issue in the second example, the log viewer. Without the tail toggle, the streamed content overrides your scroll position. 
 These aren’t bugs in the traditional sense that they produce code errors; rather, they are accessibility issues that affect all users. That said, they can be fixed and prevented with careful UX considerations as you plan and test your work. 
 Ensure Predictable Scroll Behavior 
 This is the goal: 
 Enable auto-scrolling when detecting that the user is at the bottom of the stream. 
 Stop auto-scrolling when the user has scrolled upwards. 
 Resume auto-scrolling if the user scrolls back to the bottom of the stream. 
 To do that, we need to know whether the user has intentionally moved away from the bottom, which we can assume is true when the scroll position is manually changed. We can track that behavior with a flag. 
 let userScrolled = false;

chatEl.addEventListener('scroll', () => {
 const gap = chatEl.scrollHeight
 - chatEl.scrollTop
 - chatEl.clientHeight;

 userScrolled = gap > 60;
}); That 60px threshold matters. Without it, tiny layout changes (like a new line) would briefly create a gap and break auto-scroll, even if the user didn’t actually scroll. 
 Now let’s make sure that we enable auto-scrolling only when the user’s scroll position is equal to the stream’s scroll height, i.e., the user is at the bottom of the stream: 
 function autoScroll() {
 if (!userScrolled) {
 chatEl.scrollTop = chatEl.scrollHeight;
 }
} One small thing that’s easy to miss: we need to reset userScrolled once a new stream begins. Otherwise, one scroll from a previous message can silently disable auto-scroll for the next one. 
 Solidify Layout Stability 
 We saw this in the first example as well. As new content streams in, the layout jumps, or shifts, taking you out of your current context. To be specific about what’s shifting: it’s not the page layout in a broad sense, it’s the content directly below the chat bubble. 
 There’s also a subtler artifact worth calling out before we look at the code: cursor flicker. Because we’re wiping innerHTML and recreating every element on every tick, the cursor is being destroyed and re-added constantly, up to 80 times per second at fast speeds. 
 At normal speed, it’s easy to miss, but slow the slider down to around 30ms, and you’ll see a faint but persistent flicker at the end of the text. Once we fix the rebuild pattern, the flicker disappears entirely. 
 None of these changes is a big effort on its own. But once they are in place, the interface stops reacting blindly to every update. It becomes easier to read, easier to control, and a lot less distracting, even though the content is still coming in continuously. 
 There are even more considerations to take into account for ensuring a stable, predictable, and good user experience. For example, what happens if the stream is canceled mid-flow? And what can we do to ensure that user preferences are respected for things like reduced motion, keyboard navigation, and screen reader accessibility? Let’s get into those next. 
 Handling Interrupted Streams Most streaming interfaces include a way to stop or cancel the stream. We saw that in the demos. But stopping often leaves the UI in an awkward state. The cursor might keep blinking, buttons don’t update, and the message just freezes mid-stream with no clear indication that it didn’t finish. 
 The problem is that the stop is usually wired to do one thing: cancel the timer. That’s not enough. You also need to (1) clear the pending buffer, (2) remove the cursor, (3) mark the response as incomplete, and (4) reset the buttons. Here’s how we accomplish those. 
 1. Stop The Stream Cleanly 
 Here’s what stopStream needs to do, in order: 
 Cancel the timer and flip the isStreaming flag so no more ticks run. 
 Clear the requestAnimationFrame (RAF) buffer so nothing still queued gets written on the next frame. 
 function stopStream() {
 clearTimeout(streamTimer);
 isStreaming = false;
 pending = '';
 rafQueued = false;
} Clearing the pending property matters because there might be characters buffered from the last stream instance that haven’t been flushed yet. If you don’t clear it, the next requestAnimationFrame fires, drains the buffer, and writes those characters to the DOM after the stream has officially stopped. 
 Now we move on to removing the cursor by calling markStopped on the bubble: 
 if (cursorEl && cursorEl.parentNode) cursorEl.remove();
 markStopped(aiBubble);

 stopBtn.style.display = 'none';
 retryBtn.style.display = '';
 playBtn.style.display = '';
 setStatus('Stopped', 'stopped');
 chat.removeEventListener('scroll', onScroll);
} The cursorEl.parentNode check is there because stopStream is also called internally when a new message fires mid-stream, at which point the cursor might already be gone. Calling remove() on a detached node throws, so we check first. 
 markStopped appends a small label to the bottom of the bubble so the user knows the response didn’t finish: 
 function markStopped(bubble) {
 if (!bubble) return;
 bubble.classList.add('stopped');

 const label = document.createElement('span');
 label.className = 'stopped-label';
 label.textContent = 'response stopped';
 bubble.appendChild(label);
} The null check on bubble handles the edge case where stop fires before the AI message element has been initialized, which can happen if the user clicks stop during the 300ms delay before the bubble appears. 
 Provide A Retry Option 
 If the stream simply stops — perhaps due to a network issue or some other unexpected error — we ought to provide the user with a path to re-attempt the stream. What that basically means is preventing the UI from doing the expensive work needed to scroll back up to the top, re-read the prompt, and retype it. With a retry option, the user only needs to click a button, and the stream restarts from the current position. 
 To make that work, we need to hold onto the question when the stream starts: 
 let lastQuestion = '';

function startStream(question, answer) {
 lastQuestion = question;
 // rest of setup...
} Then, when the retry attempt runs, we reset everything and start fresh: 
 function retryStream() {
 if (currentMsgEl && currentMsgEl.parentNode) {
 currentMsgEl.remove();
 }

 charIndex = 0;
 userScrolled = false;
 pending = '';
 rafQueued = false;
 isStreaming = true;

 retryBtn.style.display = 'none';
 stopBtn.style.display = '';
 setStatus('Streaming...', 'streaming');

 chat.addEventListener('scroll', onScroll, { passive: true });

 setTimeout(() => {
 initAIMsg();
 tick(lastAnswer);
 }, 200);
} The reset is critical. Every piece of state needs to go back to its initial value, just like a brand new stream. 
 Note: We remove the entire message row ( currentMsgEl ), not just the bubble. If only the bubble is removed, the layout wrapper and avatar remain persistent and break the structure. 
 Send A New Message Mid-Stream 
 There’s one more edge case that’s easy to miss. If the user sends a new message while a stream is still running, you end up with two loops writing to the DOM at the same time. The result is messy, and characters from different responses get mixed together. 
 Here’s what to do: stop the current stream before starting a new one. 
 function startStream(question, answer) {
 if (isStreaming) {
 clearTimeout(streamTimer);
 isStreaming = false;
 pending = '';
 rafQueued = false;
 if (cursorEl && cursorEl.parentNode) cursorEl.remove();
 chat.removeEventListener('scroll', onScroll);
 }

 // now reset and start fresh
 charIndex = 0;
 userScrolled = false;
 isStreaming = true;
 lastQuestion = question;
 // ...
} Here, we inline the cleanup rather than calling stopStream directly because stopStream also calls markStopped and resets the buttons. The next demo has all three behaviors wired up. You can start a stream, hit “Stop” mid-stream, and the cursor disappears, the “response stopped” label appears, and a “Retry” buttons displayed. 
 Accessibility Streaming interfaces are often built and tested with a mouse, so they may feel just fine in a browser, but break down in other situations that may not have been considered, like whether a screen reader announces new content at all. Or navigating with a keyboard might get stuck or lose focus as things update. And, of course, moving text can be uncomfortable — or even disabling — for those with motion sensitivities . 
 The good part is that you do not need to rebuild everything to accommodate these things; they can be fixed with solutions that sit on top of what is already there. 
 Accommodating Assistive Technology With Live Regions 
 Screen readers don’t automatically announce content that shows up on its own. They usually read things when the user moves to them. So, in a streaming UI, where text builds up over time, nothing gets announced. The content is there, but the user doesn’t hear anything. 
 The fix is aria-live . It tells the browser to watch a container and announce updates as they happen, without the user needing to move focus. 
 <div
 id="chat"
 role="log"
 aria-live="polite"
 aria-atomic="false"
 aria-label="Chat messages"
></div> role="log" tells assistive tech this is a stream of updates, like a running transcript. Some tools handle this automatically, but it’s safer to be explicit so behavior stays consistent. 
 aria-atomic="false" makes sure only the new content is announced. Without it, some screen readers try to read the whole message again on every update, which quickly becomes unusable. 
 aria-live="polite" queues updates instead of interrupting. Use assertive only for things that really need immediate attention, like errors. 
 Handling Incomplete States 
 Earlier, we inserted a “Response Stopped” label to the message when the stream stops mid-stream. Visually, that’s enough. But for a screen reader, that change needs to be announced. 
 Since the message is inside a live region with aria-live="polite" , the label will be automatically announced as new content when it’s added to the DOM. The live region already handles the announcement, so no additional ARIA is needed on the label itself. 
 The Retry button that appears next also needs context. If a screen reader simply says “Retry, button,” it’s not clear what action that refers to. You can fix that by adding an aria-label that includes the original question: 
 retryBtn.setAttribute(
 'aria-label',
 `Retry: ${lastQuestion.slice(0, 60)}`
); What you can do here is to set this label when the button appears, not on page load: 
 retryBtn.style.display = 'inline-block';
retryBtn.setAttribute(
 'aria-label',
 `Retry: ${lastQuestion.slice(0, 60)}`
); We also call retryBtn.focus() after stopping. That way, keyboard users don’t have to Tab around with the keyboard to find the next action. 
 Testing with assistive technology: Don’t rely on assumptions about how screen readers announce this. Test with actual tools like NVDA (Windows), JAWS (Windows), or VoiceOver (Mac/iOS). Browser DevTools can show you what’s exposed in the accessibility tree, but they can’t tell you how the content sounds . A real screen reader will reveal whether the announcement is happening at the right time and in the right way. 
 Account For Keyboard Navigation 
 The controls need to work with the keyboard while the UI is live, so the Stop button has to be reachable. For someone not using a mouse, Tab + Enter is the only way to cancel a running stream. 
 Using display: none is fine for hiding buttons; it removes them from the tab order. The problem is using things like opacity: 0 or visibility: hidden . Those hide elements visually, but they can still receive focus, so users end up tabbing onto something they can’t see. 
 Use :focus-visible so the focus ring shows up for keyboard navigation, but not for mouse clicks: 
 btn:focus-visible {
 outline: 2px solid #1d9e75;
 outline-offset: 2px;
} The cursor inside the message should have aria-hidden="true" . It’s just visual. Without that, some screen readers try to read it as text, which gets distracting. 
 Motion Sensitivity 
 The typewriter effect we see in practically every AI interface produces constant motion. As we’ve already discussed, certain amounts of motion can be disabling. Thankfully, browsers expose prefers-reduced-motion , which detects a user’s motion preferences at the operating system level. 
 For streaming, the best approach is simple: skip the animation and render the full response at once. The content stays the same, only without the motion. 
 const reducedMotion = window.matchMedia(
 '(prefers-reduced-motion: reduce)'
).matches; if (reducedMotion) {
 initAIMsg();
 for (const char of text) appendChar(char);
 if (cursorEl && cursorEl.parentNode) cursorEl.remove();
 done();
 return;
}
tick(text); // normal animation In CSS, the cursor blink also needs to stop. Despite being a minor detail, a blinking cursor element counts as flashing content . 
 @media (prefers-reduced-motion: reduce) {
 .cursor { animation: none; opacity: 1; }
} There we go! The demo below puts everything from this article together, so you can see how these patterns work in practice. It also includes a reduced motion toggle, so you can test the instant render version easily. 
 Conclusion Streaming itself is mostly solved. Getting data from the server to the client is not the hard part anymore. What breaks is the UI on top of it. 
 When content updates continuously, small things start to matter, like scroll behavior, layout stability, render timing, and how the interface responds to user actions. If those aren’t handled well, the UI feels unstable and hard to use. 
 The patterns in this article fix that by: 
 Keeping scroll position under the user’s control, 
 Updating only what has changed, 
 Batching renders per frame, 
 Handling stop and retry actions, and 
 Making the interface accessible. 
 You don’t need all of these every time. But when streaming is involved, these are the places things usually go wrong. 
 Further Reading 
 Using Server-Sent Events 
 How to open a connection, handle events, and reconnect when needed. This is the transport layer, everything here builds on. 
 Streams API 
 Streaming data directly from fetch . Useful when you need more control than SSE. 
 Chrome DevTools Performance panel 
 Helps you see layout recalculations and paint costs, so you can verify performance improvements. 
 “ How Large DOM Sizes Affect Interactivity, And What You Can Do About It ”, Jeremy Wagner 
 Why large DOM trees slow things down, and how to keep them under control in long streaming sessions.
```

---

## 4. A Fresh View In May (2026 Wallpapers Edition)

- 日期: 2026-04-30 11:00
- 链接: https://smashingmagazine.com/2026/04/desktop-wallpaper-calendars-may-2026/

```
May has a way of sneaking in with longer days, softer light, and that first real hint of summer in the air. It’s the season of fresh ideas and just enough energy to start something new , or finally pick up something you’ve been putting off. And sometimes, all it takes to spark that little bit of inspiration is a fresh view… even if it’s just on your desktop. 
 That’s where our monthly wallpapers series comes in. For the past 15 years, artists and designers from around the world have been contributing their designs to celebrate each new month. This May is no exception. Created with care and a unique personal touch , every wallpaper in this collection comes in a variety of screen resolutions and can be downloaded for free. A huge thank-you to everyone who got creative — this post wouldn’t be possible without your wonderful support! 
 If you too would like to get featured in one of our upcoming wallpapers posts, please don’t hesitate to join in . We can’t wait to see what you’ll come up with! Happy May! 
 You can click on every image to see a larger preview . 
 We respect and carefully consider the ideas and motivation behind each and every artist’s work. This is why we give all artists the full freedom to explore their creativity and express emotions and experience through their works. This is also why the themes of the wallpapers weren’t anyhow influenced by us but rather designed from scratch by the artists themselves. 
 Happily Invisible Online Designed by Ricardo Gimenes from Spain. 
 preview 
 with calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Where Every Sip Tells A Secret “A quiet ritual, a shared moment, a pause in the rush — tea invites you to slow down and discover warmth in the smallest details. Let each cup unfold its own little story.” — Designed by PopArt Studio from Novi Sad, Serbia. 
 preview 
 with calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Just A Style Thing Designed by Ricardo Gimenes from Spain. 
 preview 
 with calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Next Bloom “A small bee with a big garden plan checks each flower on her list and looks for the next bloom to visit.” — Designed by Ginger IT Solutions from Serbia. 
 preview 
 with calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 No Play Jack “Summer is getting closer, but we’re reminded of a more wintry and eerie landscape, like that of ‘The Shining.’ A truly great film, proving that you don’t need much, but it needs to be used well to create suspense and terror.” — Designed by Veronica Valenzuela from Spain. 
 preview 
 with calendar: 640x480 , 800x480 , 1024x768 , 1280x720 , 1280x800 , 1440x900 , 1600x1200 , 1920x1080 , 1920x1440 , 2560x1440 
 without calendar: 640x480 , 800x480 , 1024x768 , 1280x720 , 1280x800 , 1440x900 , 1600x1200 , 1920x1080 , 1920x1440 , 2560x1440 
 Buddha Purnima “Buddha Purnima, falling on May 1st, is the most sacred Buddhist festival commemorating the birth, enlightenment, and passing of Gautama Buddha. It is observed on the full moon day of the Vaisakha month, symbolizing spiritual liberation and the triumph of peace. The day serves as a global reminder of his core teachings: non-violence, compassion, and the path to ending suffering.” — Designed by V D Photography from Surat, Gujarat, India. 
 preview 
 with calendar: 1280x720 , 1920x1080 , 2560x1440 , 3840x2160 
 without calendar: 1280x720 , 1920x1080 , 2560x1440 , 3840x2160 
 Hello May “The longing for warmth, flowers in bloom, and new beginnings is finally over as we welcome the month of May. From celebrating nature on the days of turtles and birds to marking the days of our favorite wine and macarons, the historical celebrations of the International Workers’ Day, Cinco de Mayo, and Victory Day, to the unforgettable ‘May the Fourth be with you’, May is a time of celebration — so make every May day count!” — Designed by PopArt Studio from Serbia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1440x900 , 1440x1050 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Add Color To Your Life! “This month is dedicated to flowers, to join us and brighten our days giving a little more color to our daily life.” — Designed by Verónica Valenzuela Jimenez from Spain. 
 preview 
 without calendar: 800x480 , 1024x768 , 1152x864 , 1280x800 , 1280x960 , 1440x900 , 1680x1200 , 1920x1080 , 2560x1440 
 Ladies And Gentlemen Designed by Ricardo Gimenes from Spain. 
 preview 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Poppies Paradise Designed by Nathalie Ouederni from France. 
 preview 
 without calendar: 320x480 , 1024x768 , 1280x1024 , 1440x900 , 1680x1200 , 1920x1200 , 2560x1440 
 Understand Yourself “Sunsets in May are the best way to understand who you are and where you are heading. Let’s think more!” — Designed by Igor Izhik from Canada. 
 preview 
 without calendar: 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Navigating The Amazon “We are in May, the spring month par excellence, and we celebrate it in the Amazon jungle.” — Designed by Veronica Valenzuela Jimenez from Spain. 
 preview 
 without calendar: 640x480 , 800x480 , 1024x768 , 1280x720 , 1280x800 , 1440x900 , 1600x1200 , 1920x1080 , 1920x1440 , 2560x1440 
 ARRR2-D2 Designed by Ricardo Gimenes from Spain. 
 preview 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Lake Deck “I wanted to make a big painterly vista with some mountains and a deck and such.” — Designed by Mike Healy from Australia. 
 preview 
 without calendar: 1280x960 , 1440x900 , 1680x1050 , 1920x1080 , 2560x1440 , 2560x1600 , 2880x1800 
 Today, Yesterday, Or Tomorrow Designed by Alma Hoffmann from the United States. 
 preview 
 without calendar: 1024x768 , 1024x1024 , 1280x800 , 1280x1024 , 1366x768 , 1440x900 , 1680x1050 , 1920x1080 , 1920x1200 , 2560x1440 
 The Monolith Designed by Ricardo Gimenes from Spain. 
 preview 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Tentacles Designed by Julie Lapointe from Canada. 
 preview 
 without calendar: 320x480 , 1024x768 , 1280x800 , 1280x1024 , 1440x900 , 1680x1050 , 1920x1200 
 Geo Designed by Amanda Focht from the United States. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1680x1200 , 1920x1080 , 1920x1440 , 2560x1440 
 Make A Wish Designed by Julia Versinina from Chicago, USA. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Bat Traffic Designed by Ricardo Gimenes from Spain. 
 preview 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Blooming May “In spring, especially in May, we all want bright colors and lightness, which were not there in winter.” — Designed by MasterBundles from Ukraine. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Enjoy May! “Springtime, especially May, is my favorite time of the year. And I like popsicles — so it’s obvious isn’t it?” — Designed by Steffen Weiß from Germany. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Stone Dahlias Designed by Rachel Hines from the United States. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x1024 , 1366x768 , 1400x900 , 1400x1050 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Spring Gracefulness “We don’t usually count the breaths we take, but observing nature in May, we can’t count our breaths being taken away.” — Designed by Ana Masnikosa from Belgrade, Serbia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Sweet Lily Of The Valley “The ‘lily of the valley’ came earlier this year. In France, we celebrate the month of May with this plant.” — Designed by Philippe Brouard from France. 
 preview 
 without calendar: 800x480 , 1024x768 , 1024x1024 , 1280x720 , 1280x1024 , 1440x900 , 1920x1080 , 1920x1440 , 2560x1440 
 April Showers Bring Magnolia Flowers “April and May are usually when everything starts to bloom, especially the magnolia trees. I live in an area where there are many and when the wind blows, the petals make it look like snow is falling.” — Designed by Sarah Masucci from the United States. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Always Seek Knowledge “‘As knowledge increases, wonder deepens.’ (Charles Morgan) So I tried to create an illustration based on this.” — Designed by Bisakha Datta from India. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x900 , 1400x1050 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 May Your May Be Magnificent “May should be as bright and colorful as this calendar! That’s why our designers chose these juicy colors.” — Designed by MasterBundles from Ukraine. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Celestial Longitude Of 45° “Lixia is the 7th solar term according to the traditional East Asian calendars, which divide a year into 24 solar terms. It signifies the beginning of summer in East Asian cultures. Usually begins around May 5 and ends around May 21.” — Designed by Hong, Zi-Cing from Taiwan. 
 preview 
 without calendar: 1024x768 , 1080x1920 , 1280x720 , 1280x800 , 1280x960 , 1366x768 , 1400x1050 , 1680x1050 , 1920x1080 , 1920x1200 , 2560x1440 
 Power Designed by Elise Vanoorbeek from Belgium. 
 preview 
 without calendar: 1024x768 , 1280x800 , 1280x1024 , 1440x900 , 1680x1050 , 1920x1200 , 2560x1440 
 Rainy Days “Winter is nearly here in my part of the world and I think rainy days should be spent at home with a good book!” — Designed by Tazi Design from Australia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x600 , 1024x768 , 1152x864 , 1280x720 , 1280x960 , 1600x1200 , 1920x1080 , 1920x1440 , 2560x1440 
 Birds Of May “Inspired by a little-known ‘holiday’ on May 4th known as ‘Bird Day’. It is the first holiday in the United States celebrating birds. Hurray for birds!” — Designed by Clarity Creative Group from Orlando, FL. 
 preview 
 without calendar: 320x480 , 640x480 , 640x960 , 640x1136 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Magical Sunset “I designed Magical Sunset as a friendly reminder to take a moment and enjoy life around you. Each sunset and sunrise brings a new day for greatness and a little magic.” — Designed by Carolyn Warcup from the United States. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 All Is Possible In May “Edwin Way Teale once said that ‘[t]he world’s favorite season is the spring. All things seem possible in May.’ Now that the entire nature is clothed with grass and branches full of blossoms that will grow into fruit, we cannot help going out and enjoying every scent, every sound, every joyful movement of nature’s creatures. Make this May the best so far!” — Designed by PopArt Studio from Serbia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1440x900 , 1440x1050 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Get Featured Next Month Feeling inspired? We’ll publish the June wallpapers on May 31, so if you’d like to be part of the collection, please don’t hesitate to submit your design . We are already looking forward to it!
```

---

## 5. The “Bug-Free” Workforce: How AI Efficiency Is Subtly Disrupting The Interactions That Build Strong Teams

- 日期: 2026-04-27 10:00
- 链接: https://smashingmagazine.com/2026/04/bug-free-workforce-ai-disrupting-teams/

```
Through many discussions with industry colleagues, we’ve started hearing a phrase more often when swapping stories about AI adoption: 
 “Now I don’t have to bug [someone].” 
 Product designers don’t need to bug researchers anymore — retrieval-augment generation (RAG) tools surface insights instantly. Product Managers don’t need to bug designers for mockups — AI generates acceptable options. Engineers don’t need to bug accessibility teams — automated scanners flag issues in real-time. 
 It’s framed as liberation, and in many ways, it is. There’s genuine relief in being unblocked, in not having to wait, in solving problems independently. 
 With AI, we’re building a “bug-free workforce”. 
 But what if the bugs that AI is automating away, such as the quick questions, the small talk, the organic connections, are actually an important part of the scaffolding that builds and sustains healthy teams? 
 The Vanishing Scaffolding Consider what actually disappears when we turn to AI assistance before engaging with a colleague directly. For instance: 
 The 2-minute Slack exchange that turns into a 20-minute whiteboarding session. 
 The “quick question” that reveals a fundamental misalignment. 
 The accessibility review that becomes mentorship. 
 Although these interactions are primarily intended to exchange information and unblock individuals’ tasks, many are the building blocks for the intangible but crucial sense of belonging and connection in the workplace. 
 The inefficiencies of interpersonal communication and daily interaction build the larger organism known as work culture. When AI disrupts these interactions, what is lost? 
 What The Research Actually Shows There is ample psychological research to support our hypothesis: If the trust built through organic and informal connections is threatened, teams will be negatively impacted. Let’s examine a few: 
 In 2012, MIT’s Human Dynamics Lab (Pentland, 2012) discovered that the best predictor of team productivity wasn’t formal meetings but “energy” from informal communication: the hallway conversations, coffee chats, and quick questions. Teams with the most informal interaction had 35% more successful outcomes . With AI, what energy is not generated, leading to fewer successful outcomes? 
 In 2015, Google’s Project Aristotle studied over 180 teams to find out why some thrived, and others underperformed. They found that psychological safety, the shared belief among team members that the environment is safe for interpersonal risk-taking, built through frequent, low-stakes interactions, was the number one predictor of high performance . Not intelligence. Not resources. Trust built through micro-moments . The exact micro-moments we see vanishing when we overuse AI. 
 In 2025, researchers from Harvard, Columbia, and Yeshiva University published a study focused on the impact of AI on performance and team coordination . The authors concluded that AI-driven automation decreased overall team performance and increased coordination failures. These effects were especially large in the short-term and in low- and medium-skilled teams. Automation also decreased team trust. 
 Why This Matters When AI disrupts the team’s energy and psychological safety, a sense of disconnection sets in, which, in turn, hurts the company’s bottom line. 
 Disconnected Employees Leave 
 People don’t stay at companies because of the work. They stay because of the people. And if connections to colleagues decrease due to AI’s presence, how might that expedite one’s departure? 
 Consider this question in dollar terms. McKinsey’s Great Attrition research found that not feeling a sense of belonging was one of the most frequently cited reasons employees left. When informal micro-interactions disappear, belonging erodes, and people walk. 
 “Employee disengagement and attrition could cost a median-size S&P 500 company between $228 million and $355 million a year in lost productivity.” 
 — McKinsey 
 Leaders must ask themselves if the potential gains from AI rollouts and promised productivity gains outweigh the costs of a disengaged and attrition-prone workforce. The evidence suggests otherwise. 
 Disconnected Teams Are Less Innovative 
 Korean researchers in 2024 analyzed innovation in the private sector and concluded that weak ties — the bridging conversations with people you interact with occasionally — sustained innovative performance in companies characterized by active technological innovation. 
 Simply put, breakthroughs do not necessarily emerge from your core team but from interactions with the people you would have “bugged” in the past. Eliminating these interactions in favor of AI could not only negatively impact team health, but it could also hurt the business through decreased depth and breadth of innovation in design, coding, content, and beyond. 
 AI’s seduction is that it feels like pure gain until the team realizes they’ve become strangers who happen to work on the same project. 
 If a shared sense of purpose and belonging disappears, employers have a workforce less engaged and less innovative, with a higher chance of attrition. 
 If AI helps us need each other less, how can a company hope to nurture a connected, supported, and effective workforce? 
 The answer requires a balanced and multi-pronged approach. Use AI tools for dull, repetitive, and high-volume tasks while reserving the human brain for higher-level problem solving. Design physical workspaces and online team interactions that will maintain or increase human connection. 
 Maintaining The Best Of Both In short, leverage the best of AI tools and human abilities. 
 1. Use AI To Eliminate The Toil 
 In the March 2026 article “ When Using AI Leads to ‘Brain Fry’ ,” the authors outline their study of 1,488 full-time U.S.-based workers to understand the impact of AI use on professionals. The result was a concept they call “AI Brain Fry,” a form of acute mental fatigue and cognitive exhaustion resulting from excessive use, interaction, or oversight of AI tools beyond an individual’s cognitive capacity. 
 Further, the study reveals that the cognitive strain created by intensive AI use carries business costs, including decision fatigue and error-prone work. Perhaps the most troubling finding is that 34% of workers who reported experiencing brain fry intended to quit their jobs. The loss of institutional knowledge caused by turnover is well documented. 
 One conclusion is that AI is not inherently bad or cognitively taxing. Rather, as with any tool, what matters is how it’s used. 
 Focusing our energy on identifying the repetitive, unenjoyable parts of our jobs (or “toil”) and using AI to remove them is a way to improve cognitive and team health. 
 Indeed, the Harvard Business Review authors explain that participants in their study who used AI to eliminate toil only had 15% lower rates of burnout but also reported “a higher degree of social connection with peers…because they had more time to spend ‘off keyboard.’” In this toil-elimination scenario, AI did not disrupt team connections; it removed what we consider busy work that prevented the team from solving problems with colleagues. 
 2. Institutionalize Productive Friction 
 Steve Jobs famously designed the Pixar studios so employees would have to bump into each other. “Steve realized that when people run into each other, when they make eye contact, things happen,” reflected Brad Bird , the director of The Incredibles and Ratatouille movies. John Lasseter, responsible for some of Pixar’s most beloved films, shared that he’d “never seen a building that promoted collaboration and creativity as well as this one.” Jobs understood that serendipitous collision drives creative work, and Pixar’s oeuvre reveals the genius. 
 What is the equivalent of creating this type of organizational design in the age of AI? 
 Build AI tools that connect the team. 
 We’ve found that when building internal agents, it’s best to attach the names of the original creators to the work and to direct seekers to these creators. This way, any seeker not only finds the answer but is connected to others with more institutional knowledge to help. 
 Publicly spotlight successful team uses of AI. 
 By finding examples of how teams have used AI to work more effectively and efficiently together and highlighting them in public forums and townhalls, it helps establish the narrative that AI can be something that brings us together rather than pushes us apart. 
 Establish rotation programs. 
 If AI means product managers can prototype, have them shadow designers anyway. Having a more holistic understanding of each other’s craft through direct dialogues benefits both sides beyond simple AI outputs. 
 Hold panel discussions on the evolution of work. 
 Gather cross-functional partners to regularly discuss and debate how our work is currently changing or could in the near future. It keeps intentional change top of mind and in the open. 
 3. Build Team Cohesion Through AI-inspired Laughter 
 Positive humor in the workplace has been studied extensively as a way for teams to bond. We see how AI can improve team connections through a good, absurd laugh. 
 Bad UX Vibecoding Competitions 
 Give your team a silly prompt (“Design the worst volume control”) and 30 minutes to vibe-code a horrible solution. The process of building these outputs helps the team: learn new AI tools, get the creative juices flowing, and, most importantly, laugh together. 
 Hyper-specific AI Creations 
 Would a certain image make people smile in this workshop? Is there a funny idea at work that would be even weirder as an AI-generated song? Using them for absurd work moments is a fun way to get people laughing. 
 Eliminating toil, institutionalizing productive friction, and building team cohesion through humor show the power of integrating the best of the human brain and AI algorithms. 
 The question isn’t whether to use AI. Contemporary workers have less and less choice. The question is: what kind of team do you want to become when AI is the newest teammate? 
 Conclusion Leaders who introduce artificial intelligence with an equal amount of emotional intelligence will enable their teams to thrive by leveraging the power of AI while also shielding their teams from the inherent risks associated with the disruptive natures of these new tools. 
 When the unexpected hits — the crisis, the pivot, the moment that requires trust you can’t manufacture overnight — it will be the teams with cultures intact that will thrive. 
 References 
 The 4 Stages of Psychological Safety: Defining the Path to Inclusion and Innovation , Clark, T. R. (2020), Berrett-Koehler Publishers 
 What Google Learned From Its Quest to Build the Perfect Team , Duhigg, C. (2016), The New York Times Magazine 
 Psychological Safety and Learning Behavior in Work Teams , Edmondson, A. C. (1999), Administrative Science Quarterly, 44(2) 
 The Strength of a Weak Tie in the Innovative Performance of Firms: A Case of Korean High-tech Manufacturing Small and Medium-sized Enterprises , Hong, Jinki; Lee; Raehyung; Ohm, Jay Y.;, Lee, Duk Hee (2024), Sociology Compass Volume 18, Issue 5 
 How Psychological Safety Impacts R&D Project Teams , Liu, Yuwen; Keller, R.T. (2021), Research-Technology Management Volume 64, Issue 2 
 Creating Psychological Safety in the Workplace , McCausland, Tammy (2023), Research-Technology Management Volume 66, Issue 2 
 Some Employees Are Destroying Value. Others Are Building It. Do You Know the Difference? , De Smet, Aaron; Mugayar-Baldocchi, Marino; Reich, Angelika; Schaninger, Bill (September 11, 2023), McKinsey Quarterly 
 The New Science of Building Great Teams , Pentland, A. (2012), Harvard Business Review 
 Super Mario Meets AI: Experimental Effects of Automation and Skills on Team Performance and Coordination , Dell’Acqua, Fabrizio; Kogut, Bruce; Perkowski, Patryk (2025), The Review of Economics and Statistics 107 (4) 
 Humor Is Serious Business: Why Humor Is A Secret Weapon In Business And Life , Aaker, J; Bagdonas, Naomi (2021)
```

---

## 6. The UX Designer’s Nightmare: When “Production-Ready” Becomes A Design Deliverable

- 日期: 2026-04-22 10:00
- 链接: https://smashingmagazine.com/2026/04/production-ready-becomes-design-deliverable-ux/

```
In early 2026, I noticed that the UX designer’s toolkit seemed to shift overnight. The industry standard “Should designers code?” debate was abruptly settled by the market, not through a consensus of our craft, but through the brute force of job requirements. If you browse LinkedIn today, you’ll notice a stark change: UX roles increasingly demand AI-augmented development , technical orchestration, and production-ready prototyping. 
 For many, including myself, this is the ultimate design job nightmare. We are being asked to deliver both the “vibe” and the “code” simultaneously, using AI agents to bridge a technical gap that previously took years of computer science knowledge and coding experience to cross. But as the industry rushes to meet these new expectations, they are discovering that AI-generated functional code is not always good code. 
 The LinkedIn Pressure Cooker: Role Creep In 2026 The job market is sending a clear signal. While traditional graphic design roles are expected to grow by only 3% through 2034, UX, UI, and Product Design roles .) are projected to grow by 16% over the same period. 
 However, this growth is increasingly tied to the rise of AI product development , where “design skills” have recently become the #1 most in-demand capability, even ahead of coding and cloud infrastructure. Companies building these platforms are no longer just looking for visual designers; they need professionals who can “ translate technical capability into human-centered experiences .” 
 This creates a high-stakes environment for the UX designer. We are no longer just responsible for the interface; we are expected to understand the technical logic well enough to ensure that complex AI capabilities feel intuitive, safe, and useful for the human on the other side of the screen. Designers are being pushed toward a “design engineer” model , where we must bridge the gap between abstract AI logic and user-facing code . 
 A recent survey found that 73% of designers now view AI as a primary collaborator rather than just a tool. However, this “collaboration” often looks like “role creep.” Recruiters are often not just looking for someone who understands user empathy and information architecture — they want someone who can also prompt a React component into existence and push it to a repository! 
 This shift has created a competency gap . 
 As an experienced senior designer who has spent decades mastering the nuances of cognitive load, accessibility standards, and ethnographic research, I am suddenly finding myself being judged on my ability to debug a CSS Flexbox issue or manage a Git branch. 
 The nightmare isn’t the technology itself. It’s the reallocation of value . 
 Businesses are beginning to value the speed of output over the quality of the experience, fundamentally changing what it means to be a “successful” designer in 2026. 
 The Competence Trap: Two Job Skill Sets, One Average Result 
 There is potentially a very dangerous myth circulating in boardrooms that AI makes a designer “equal” to an engineer. This narrative suggests that because an LLM can generate a functional JavaScript event handler, the person prompting it doesn’t need to understand the underlying logic. In reality, attempting to master two disparate, deep fields simultaneously will most likely lead to being averagely competent at both. 
 The “Averagely Competent” Dilemma 
 For a senior UX designer to become a senior-level coder is like asking a master chef to also be a master plumber because “they both work in the kitchen.” You might get the water running, but you won’t know why the pipes are rattling. 
 The “cognitive offloading” risk. 
 Research shows that while AI can speed up task completion, it often leads to a significant decrease in conceptual mastery. In a controlled study, participants using AI assistance scored 17% lower on comprehension tests than those who coded by hand. 
 The debugging gap. 
 The largest performance gap between AI-reliant users and hand-coders is in debugging . When a designer uses AI to write code they don’t fully understand, they don’t have the ability to identify when and why it fails. 
 So, if a designer ships an AI-generated component that breaks during a high-traffic event and cannot manually trace the logic, they are no longer an expert. They are now a liability. 
 The High Cost Of Unoptimised Code 
 Any experienced code engineer will tell you that creating code with AI without the right prompt leads to a lot of rework. Because most designers lack the technical foundation to audit the code the AI gives them, they are inadvertently shipping massive amounts of “Quality Debt” . 
 Common Issues In Designer-Generated AI Code The security flaw 
 Recent reports indicate that up to 92% of AI-generated codebases contain at least one critical vulnerability. A designer might see a functioning login form, unaware that it has an 86% failure rate in XSS defense, which are the security measures aimed at preventing attackers from injecting malicious scripts into trusted websites. 
 The accessibility illusion 
 AI often generates “functional” applications that lack semantic integrity. A designer might prompt a “beautiful and functional toggle switch,” but the AI may provide a non-semantic <div> that lacks keyboard focus and screen-reader compatibility, creating Accessibility Debt that is expensive to fix later. 
 The performance penalty 
 AI-generated code tends to be verbose. AI is linked to 4x more code duplication than human-written code. This verbosity slows down page loads, creates massive CSS files, and negatively impacts SEO. To a business, the task looks “done.” To a user with a slow connection or a screen reader, the site is a nightmare. 
 Creating More Work, Not Less The promise of AI was that designers could ship features without bothering the engineers. The reality has been the birth of a “Rework Tax” that is draining engineering resources across the industry. 
 Cleaning up 
 Organisations are finding that while velocity increases, incidents per Pull Request are also rising by 23.5% . Some engineering teams now spend a significant portion of their week cleaning up “AI slop” delivered by design teams who skipped a rigorous review process. 
 The communication gap 
 Only 69% of designers feel AI improves the quality of their work, compared to 82% of developers . This gap exists because “code that compiles” is not the same as “code that is maintainable.” 
 When a designer hands off AI-generated code that ignores a company’s internal naming conventions or management patterns, they aren’t helping the engineer; they are creating a puzzle that someone else has to solve later. 
 The Solution 
 We need to move away from the nightmare of the “ Solo Full-Stack Designer ” and toward a model of designer/coder collaboration . 
 The ideal reality: 
 The Partnership 
 Instead of designers trying to be mediocre coders, they should work in a human-AI-human loop . A senior UX designer should work with an engineer to use AI; the designer creates prompts for intent, accessibility, and user flow , while the engineer creates prompts for architecture and performance . 
 Design systems as guardrails 
 To prevent accessibility debt from spreading at scale, accessible components must be the default in your design system. AI should be used to feed these tokens into your UI, ensuring that even generated code stays within the “source of truth.” 
 Beyond The Prompt The industry is currently in a state of “AI Infatuation,” but the pendulum will eventually swing back toward quality. 
 The UX designer’s nightmare ends when we stop trying to compete with AI tools at what they do best (generating syntax) and keep our focus on what they cannot do (understanding human complexity). 
 Businesses that prioritise “designer-shipped code” without engineering oversight will eventually face a reckoning of technical debt, security breaches, and accessibility lawsuits. The designers who thrive in 2026 and beyond will be those who refuse to be “prompt operators” and instead position themselves as the guardians of the user experience . This is the perfect outcome for experienced designers and for the industry. 
 Our value has always been our ability to advocate for the human on the other side of the screen. We must use AI to augment our design thinking, allowing us to test more ideas and iterate faster, but we must never let it replace the specialised engineering expertise that ensures our designs technically work for everyone. 
 Summary Checklist for UX Designers 
 Work Together. 
 Use AI-made code as a starting point to talk with your developers. Don’t use it as a shortcut to avoid working with them. Ask them to help you with prompts for code creation for the best outcomes. 
 Understand the “Why”. 
 Never submit code you don’t understand. If you can’t explain how the AI-generated logic works, don’t include it in your work. 
 Build for Everyone. 
 Good design is more than just looks. Use AI to check if your code works for people using screen readers or keyboards, not just to make things look pretty.
```

---

## 7. Session Timeouts: The Overlooked Accessibility Barrier In Authentication Design

- 日期: 2026-04-20 13:00
- 链接: https://smashingmagazine.com/2026/04/session-timeouts-accessibility-barrier-authentication-design/

```
For web professionals, session management is a balancing act between user experience, cybersecurity, and resource usage. For people with disabilities, it is more than that — it is a barrier to buying digital tickets, scrolling on social media, or applying for a loan online. Session timeout accessibility can be the difference between a bad day and a good day for those with disabilities. 
 For many, getting halfway through an important form only to be unceremoniously kicked back to the login screen is a common experience. Such incidents can lead to exasperation and even abandonment of the website entirely. With some backend work, web professionals can ensure no one has to experience this frustration. 
 Why Session Timeouts Disproportionately Affect Users With Disabilities A considerable portion of the global population has cognitive, motor, or vision impairments. Worldwide, around 1.3 billion people have significant disabilities. Whether they possess motor, cognitive, or visual impairments, their disabilities affect their ability to interact with technology easily. They can all be disproportionately affected by session timeouts, making session timeout accessibility a critical issue. 
 Session timeouts are inaccessible for a large percentage of the population. An estimated 20% of people are neurodivergent, meaning timeout barriers don’t just affect a small subset of users — they impact a substantial portion of any website’s audience . As a result, some users may look inactive when they are not. Strict timeouts create undue pressure. 
 Motor Impairments and Slower Input Speeds 
 For instance, someone with cerebral palsy tries to purchase tickets online for an upcoming concert. Due to coordination difficulties and muscle stiffness, they may enter their information more slowly than a non-disabled person would. They select the date, choose their seats, and fill out personal information. Before they can enter their credit card details, a timeout pop-up appears. They have been logged out due to “inactivity” and must restart the entire process. 
 This situation is not entirely hypothetical. Matthew Kayne is a disability rights advocate, broadcaster, and contributor to The European magazine. He describes the effort required to navigate websites as someone with cerebral palsy. He explains how the user interface is often poorly designed for adaptive devices, and he worries his equipment won’t respond correctly. After carefully navigating each page, he is suddenly logged out. In a moment, one timed form can erase hours of work, and it’s not just a matter of inconvenience. A single failed attempt can delay support or cause him to miss appointments. 
 Motor impairments can slow input speed , making it appear the user is not at their computer. As such, people who experience stiffness, hand tremors, coordination challenges, involuntary movements, or muscle weakness are disproportionately affected by session timeouts. According to the DWP Accessibility Manual, it can take multiple attempts for adaptive technology to register input, slowing users down considerably. Even if they receive a warning, they may not be able to act fast enough to prove they are still active. 
 Cognitive Impairments and Processing Time 
 Session timeouts can also create accessibility barriers for those with various types of cognitive differences. Strict timeouts can create undue pressure that assumes everyone processes information at the same speed. Users may appear inactive when they are actually reading, thinking, or processing. 
 Cognitive differences encompass a wide range of experiences, including neurodivergences like autism and ADHD, developmental disabilities like Down syndrome, and learning disabilities like dyslexia. Many people are born with cognitive differences. In fact, an estimated 20% of people are neurodivergent, making up a large portion of any website’s audience. Others acquire cognitive disabilities later in life through traumatic brain injury or conditions like dementia. 
 People with cognitive disabilities often need more time to complete online tasks — not because of any deficit, but because they process information differently. Design choices that work well for neurotypical users can create unnecessary obstacles for people with ADHD, dyslexia, autism, or memory-related conditions. 
 Invisible session timeouts are particularly problematic for people who experience memory loss, language processing differences, or time blindness . For example, neurodivergent technology leader Kate Carruthers says ADHD has affected her perception of time. She has time blindness and can’t reliably track how much time has passed, making estimates unhelpful. 
 When websites depend on users estimating remaining time before a session expires, they quietly exclude people — not just those with formal ADHD diagnoses, but anyone who experiences time differently or processes information at a different pace. 
 Vision Impairments and Screen Reader Navigation Overhead 
 Since blind or low-vision users cannot visually scan a page to find what they need, they must listen to links, headings, and form fields, which is inherently more time-consuming . More than 43 million people worldwide are affected by blindness, while 295 million have moderate to severe vision impairment, which makes this a significant accessibility concern for any global-facing website. 
 As a result, these users’ sessions may expire even if they are active. Live timers and 30-second warnings do little to help , as they are not built with screen readers in mind. 
 Bogdan Cerovac, a web developer passionate about digital accessibility, experienced this firsthand. The countdown timer informed him how long he had left before being logged out due to inactivity. By all accounts, it worked fine. However, he describes the screen reader experience as horrible , as it notified him of the remaining time every single second. He couldn’t navigate the page because he was spammed by constant status messages. 
 Common Timeout Patterns That Fail Accessibility Requirements According to the National Institute of Standards and Technology, session management is preferable to continually preserving credentials, which would incentivize users to create authentication workarounds that could threaten security. However, several common timeout patterns fail to meet modern standards for session timeout accessibility. 
 Silent Timeouts and Insufficient Warnings 
 Many websites either provide no warning before logging users out, or they display a brief, seconds-long pop-up that appears too late to be actionable. For users who navigate via screen reader, these warnings may not be announced in time. For those with motor impairments, a 30-second countdown may not provide enough time to respond. 
 Let’s consider the Consular Electronic Application Center’s DS-260 page, which is used to apply for or renew U.S. nonimmigrant visas. If an application is idle for around 20 minutes , it will log the user off without warning. The FAQ page only provides an approximate time estimate. Someone’s work only saves when they complete the page, so they may lose significant progress. 
 Nonextendable Sessions 
 An abrupt “session expired” message is frustrating even for individuals without disabilities. If there is no option to continue, users are forced to log back in and restart their work, wasting time and energy. 
 Form Data Loss on Expiration 
 Unless the website automatically saves progress, visitors will lose everything when the session expires. For someone with disabilities, this does not simply waste time. It can make their day immeasurably harder. Imagine spending an hour on a service request, job application, or purchase order only for all progress to be completely erased with little to no warning. 
 Design Patterns That Balance Security and Accessibility Inconsistent timeout periods and a lack of warnings lead to the sudden, unexpected loss of all unsaved work. For long, complex forms, like the DS-260, a poor user experience is extremely frustrating. In comparison, the United Kingdom’s application for pension credit is highly accessible. It warns users at least two minutes in advance and allows them to extend the session. It meets level AA of the WCAG 2.2 success criteria, indicating its accessibility. 
 People with disabilities are disproportionately affected by the unintended consequences of poor session management. Thankfully, session timeouts’ inaccessibility is not a matter of fact. With a few small changes, web professionals can significantly improve their website’s accessibility. 
 Advance Warning Systems and Extend Functionality 
 Websites should clearly state the time limit’s existence and duration before the session starts. For instance, if someone is filling out a bank form, the first page should exist solely to inform them that it has a 60-minute time limit. A live counter that updates regularly can help them track how much time remains. Also, users should be told whether they can adjust the session timeout length. 
 Activity-Based vs. Absolute Timeouts 
 An activity-based timeout logs users out due to inactivity, while an absolute timeout logs them out regardless of activity. For an office, a 24-hour absolute timer might make sense, since workers only need to log in when they get to work. As long as users know when their session will expire, the latter is more accessible than the former. 
 Auto-Save and Progress Preservation 
 Cookies, localStorage, and sessionStorage are temporary, client-side storage mechanisms that allow web applications to store data for the duration of a single browser session. They are powerful, lightweight tools. Web developers can use them to automatically save users’ progress at frequent intervals, ensuring data is restored upon reauthentication. 
 This way, even if someone’s session expires by accident, they are not penalized. Once they log back in, they can finish filling out their credit card details or pick up where they left off with an online form. 
 Testing and WCAG Compliance Considerations The Web Content Accessibility Guidelines (WCAG) is a collection of internationally accepted internet accessibility standards published by the W3C. It acts as the arbiter of session timeout accessibility. Web developers should pay special attention to Guideline 2.9.2 , which outlines best practices for adequate time. 
 The timeout adjustable mechanism should extend the time limit before the session expires or allow it to be turned off completely. For the former option, a dialog box should appear asking users if they need more time, allowing them to continue with one click. The WC3 notes that exceptions exist. 
 For example, when a website conducts a live ticket sale, users can only hold tickets in their carts for 10 minutes to give others a chance to purchase limited inventory. Alternatively, session timeouts may be necessary on shared computers. If librarians allowed everyone to stay logged in instead of automatically signing them out overnight, they would risk security issues. 
 Some processes should not have time limits at all. When browsing social media, reading a news article, or searching for items on an e-commerce site, there is no reason a session should expire within an arbitrary time frame. Meanwhile, in a timed exam, it may be necessary. However, in this case, administrators can extend time limits for students with disabilities. 
 When web developers make session management accessible, they are not catering to a small group. Pew Research Center data shows 62% of adults with disabilities own a computer. 72% have high-speed home internet. These figures do not differ statistically from the percentage of non-disabled adults who say the same. 
 Overcoming the Session Timeout Accessibility Barrier The WCAG provides additional resources that web developers can review to understand session management accessibility better: 
 WCAG SC 2.2.1 Timing Adjustable 
 WCAG SC 2.2.5 Re-authenticating 
 WCAG SC 2.2.6 Timeouts 
 In addition to following these guidelines, there is a wealth of information from leading educational institutions, authorities on open web technologies, and government agencies. They provide a great starting place for those with intermediate web development knowledge. 
 Web professionals should consider the following resources to learn more about tools and techniques they can use to make session management more accessible: 
 Harvard University’s Session Extension Technique 
 DWP Accessibility Manual: How to test session timeouts 
 Window: sessionStorage property 
 Session timeout accessibility is not only an industry best practice but an ethical web development standard. 
 Those who prioritize it will appeal to a wider audience, improve usability , and attract more website visitors and longer sessions. 
 The main takeaway is that a website with inaccessible session timeouts sends a clear message that it doesn’t value the user’s time or effort, a problem that creates significant barriers for people with disabilities. However, this is a solvable issue. With a few simple changes, such as providing session extension warnings and auto-saving progress, web developers can build a more considerate, accessible, and respectful internet for everyone. 
 Further Reading On SmashingMag 
 “ What Does It Really Mean For A Site To Be Keyboard Navigable ”, Eleanor Hecks 
 “ Designing For Neurodiversity ”, Vitaly Friedman 
 “ What I Wish Someone Told Me When I Was Getting Into ARIA ”, Eric Bailey 
 “ A Designer’s Accessibility Advocacy Toolkit ”, Yichan Wang
```

---

## 8. How To Improve UX In Legacy Systems

- 日期: 2026-04-10 13:00
- 链接: https://smashingmagazine.com/2026/04/legacy-systems/

```
Imagine that you need to improve the UX of a legacy system . A system that has been silently working in the background for almost a decade. It’s slow, half-broken, unreliable, and severely outdated — a sort of “black box” that everyone relies upon, but nobody really knows what’s happening under the hood. 
 Where would you even start? Legacy stories are often daunting, adventurous, and utterly confusing. They represent a mixture of fast-paced decisions, quick fixes, and accumulating UX debt. 
 There is no one-fits-all solution to tackle them, but there are ways to make progress, albeit slowly, while respecting the needs and concerns of users and stakeholders. Now, let’s see how we can do just that. 
 The Actual Challenges Of Legacy UX It might feel that legacy products are waiting to be deprecated at any moment. But in reality, they are often critical for daily operations . Many legacy systems are heavily customized for the needs of the organization, often built externally by a supplier and often without rigorous usability testing. 
 It’s common for enterprises to spend 40–60% of their time managing, maintaining, and fine-tuning legacy systems. They are essential, critical — but also very expensive to keep alive. 
 1. Legacy Must Co-Exist With Products Built Around Them 
 Running in a broken, decade-old ecosystem , legacy still works, yet nobody knows exactly how and why it still does. People who have set it up originally probably have left the company years ago, leaving a lot of unknowns and poorly documented work behind. 
 With them come fragmented and inconsistent design choices , stuck in old versions of old design tools that have long been discontinued. 
 Still, legacy systems must neatly co-exist within modern digital products built around them. In many ways, the end result resembles a Frankenstein — many bits and pieces glued together, often a mixture of modern UIs and painfully slow and barely usable fragments here and there — especially when it comes to validation, error messages, or processing data. 
 2. Legacy Systems Make or Break UX 
 Once you sprinkle a little bit of quick bugfixing, unresolved business logic issues, and unresponsive layouts, you have a truly frustrating experience , despite the enormous effort put into the rest of the application. 
 If one single step in a complex user flow feels utterly broken and confusing , then the entire product appears to be broken as well, despite the incredible efforts the design teams have put together in the rest of the product. 
 Well, eventually, you’ll have to tackle legacy. And that’s where we need to consider available options for your UX roadmap . 
 UX Roadmap For Tackling Legacy Projects Don’t Dismiss Legacy: Build on Existing Knowledge 
 Because legacy systems are often big unknowns that cause a lot of frustration to everyone, from stakeholders to designers to engineers to users. The initial thought might be to remove it entirely and redesign it from scratch , but in practice, that’s not always feasible. Big-bang-redesign is a remarkably expensive and very time-consuming endeavor. 
 Legacy systems hold valuable knowledge about the business practice, and they do work — and a new system must perfectly match years of knowledge and customization done behind the scenes. That’s why stakeholders and users (in B2B) are typically heavily attached to legacy systems , despite all their well-known drawbacks and pains. 
 To most people, because such systems are at the very heart of the business, operating on them seems to be extremely risky and will require a significant amount of caution and preparation . Corporate users don’t want big risks. So instead of dismissing legacy entirely, we might start by gathering existing knowledge first. 
 Map Existing Workflows and Dependencies 
 The best place to start is to understand how and where exactly legacy systems are in use. You might discover that some bits of the legacy systems are used all over the place — not only in your product, but also in business dashboards, by external agencies, and by other companies that integrate your product into their services. 
 Very often, legacy systems have dependencies on their own, integrating other legacy systems that might be much older and in a much worse state. Chances are high that you might not even consider them in the big-bang redesign — mostly because you don’t know just how many black boxes are in there. 
 Set up a board to document current workflows and dependencies to get a better idea of how everything works together. Include stakeholders, and involve heavy users in the conversation . You won’t be able to open the black box, but you can still shed some light on it from the perspectives of different people who may be relying on legacy for their work. 
 Once you’ve done that, set up a meeting to reflect to users and stakeholders what you have discovered. You will need to build confidence and trust that you aren’t missing anything important, and you need to visualize the dependencies that a legacy tool has to everyone involved. 
 Replacing a legacy system is never about legacy alone . It’s about the dependencies and workflows that rely on it, too. 
 Choose Your UX Migration Strategy 
 Once you have a big picture in front of you, you need to decide on what to do next. Big-bang relaunch or a small upgrade? Which approach would work best? You might consider the following options before you decide on how to proceed: 
 Big-bang relaunch . 
 Sometimes the only available option, but it’s very risky, expensive, and can take years, without any improvements to the existing setup in the meantime. 
 Incremental migration . 
 Slowly retire pieces of legacy by replacing small bits with new designs. This offers quicker wins in a Frankenstein style but can make the system unstable. 
 Parallel migration . 
 Run a public beta of the replacement alongside the legacy system to involve users in shaping the new design. Retire the old system when the new one is stable, but be prepared for the cost of maintaining both. 
 Incremental parallel migration . 
 List all business requirements the legacy system fulfills, then build a new product to meet them reliably, matching the old system from day one. Test early with power users, possibly offering an option to switch systems until the old one is fully retired. 
 Legacy UI upgrade + public beta . 
 Perform low-risk fine-tuning on the legacy system to align UX, while incrementally building a new system with a public beta. This yields quicker and long-term wins, ideal for fast results. 
 Replacing a system that has been carefully refined and heavily customized for a decade is a monolithic task. You can’t just rebuild something from scratch within a few weeks that others have been working on for years. 
 So whenever possible, try to increment gradually , involving users and stakeholders and engineers along the way — and with enough buffer time and continuous feedback loops . 
 Wrapping Up With legacy projects, failure is often not an option. You’re migrating not just components, but users and workflows . Because you operate on the very heart of the business , expect a lot of attention, skepticism, doubts, fears, and concerns. So build strong relationships with key stakeholders and key users and share ownership with them. You will need their support and their buy-in to bring your UX work in action. 
 Stakeholders will request old and new features. They will focus on edge cases, exceptions, and tiny tasks . They will question your decisions. They will send mixed signals and change their opinions. And they will expect the new system to run flawlessly from day one. 
 And the best thing you can do is to work with them throughout the entire design process, right from the very beginning. Run a successful pilot project to build trust . Report your progress repeatedly. And account for intense phases of rigorous testing with legacy users. 
 Revamping a legacy system is a tough challenge. But there is rarely any project that can have so much impact on such a scale. Roll up your sleeves and get through it successfully, and your team will be remembered, respected, and rewarded for years to come. 
 Meet “Measure UX & Design Impact” Meet Measure UX & Design Impact , Vitaly’s practical guide for designers and UX leads on how to track and visualize the incredible impact of your UX work on business — with a live UX training later this year. Jump to details . 
 Meet Measure UX and Design Impact , a practical video course for designers and UX leads. Video + UX Training 
 Video only 
 Video + UX Training 
 $ 495.00 $ 799.00 Get Video + UX Training 
 25 video lessons (8h) + Live UX Training . 
 100 days money-back-guarantee. 
 Video only 
 $ 250.00$ 350.00 
 Get the video course 
 25 video lessons (8h). Updated yearly. 
 Also available as a UX Bundle with 3 video courses. 
 Useful Resources UX Migration Strategy For Legacy Apps , by Tamara Chehayeb Makarem 
 How To Improve Legacy Systems , by Christopher Wong 
 Designing With Legacy , by Peter Zalman 
 Redesigning A Large Legacy System , by Pawel Halicki 
 How To Manage Legacy Code , by Nicolas Carlo 
 How To Transform Legacy , by Bansi Mehta 
 Design Debt 101 , by Alicja Suska 
 Practical Guide To Enterprise UX , by Yours Truly 
 Healthcare UX Design Playbook , by Yours Truly
```

---

## 9. Identifying Necessary Transparency Moments In Agentic AI (Part 1)

- 日期: 2026-04-07 10:00
- 链接: https://smashingmagazine.com/2026/04/identifying-necessary-transparency-moments-agentic-ai-part1/

```
Designing for autonomous agents presents a unique frustration. We hand a complex task to an AI, it vanishes for 30 seconds (or 30 minutes), and then it returns with a result. We stare at the screen. Did it work? Did it hallucinate? Did it check the compliance database or skip that step? 
 We typically respond to this anxiety with one of two extremes. We either keep the system a Black Box , hiding everything to maintain simplicity, or we panic and provide a Data Dump , streaming every log line and API call to the user. 
 Neither approach directly addresses the nuance needed to provide users with the ideal level of transparency. 
 The Black Box leaves users feeling powerless. The Data Dump creates notification blindness, destroying the efficiency the agent promised to provide. Users ignore the constant stream of information until something breaks, at which point they lack the context to fix it. 
 We need an organized way to find the balance. In my previous article, “ Designing For Agentic AI ”, we looked at interface elements that build trust, like showing the AI’s intended action beforehand (Intent Previews) and giving users control over how much the AI does on its own (Autonomy Dials). But knowing which elements to use is only part of the challenge. The harder question for designers is knowing when to use them. 
 How do you know which specific moment in a 30-second workflow requires an Intent Preview and which can be handled with a simple log entry? 
 This article provides a method to answer that question. We will walk through the Decision Node Audit . This process gets designers and engineers in the same room to map backend logic to the user interface. You will learn how to pinpoint the exact moments a user needs an update on what the AI is doing. We will also cover an Impact/Risk matrix that will help to prioritize which decision nodes to display and any associated design pattern to pair with that decision. 
 Transparency Moments: A Case Study Example Consider Meridian (not real name), an insurance company that uses an agentic AI to process initial accident claims. The user uploads photos of vehicle damage and the police report. The agent then disappears for a minute before returning with a risk assessment and a proposed payout range. 
 Initially, Meridian’s interface simply showed Calculating Claim Status. Users grew frustrated. They had submitted several detailed documents and felt uncertain about whether the AI had even reviewed the police report, which contained mitigating circumstances. The Black Box created distrust. 
 To fix this, the design team conducted a Decision Node Audit. They found that the AI performed three distinct, probability-based steps, with numerous smaller steps embedded: 
 Image Analysis 
 The agent compared the damage photos against a database of typical car crash scenarios to estimate the repair cost. This involved a confidence score. 
 Textual Review 
 It scanned the police report for keywords that affect liability (e.g., fault, weather conditions, sobriety). This involved a probability assessment of legal standing. 
 Policy Cross Reference 
 It matched the claim details against the user’s specific policy terms, searching for exceptions or coverage limits. This also involved probabilistic matching. 
 The team turned these steps into transparency moments. The interface sequence was updated to: 
 Assessing Damage Photos : Comparing against 500 vehicle impact profiles. 
 Reviewing Police Report : Analyzing liability keywords and legal precedent. 
 Verifying Policy Coverage : Checking for specific exclusions in your plan. 
 The system still took the same amount of time, but the explicit communication about the agent’s internal workings restored user confidence. Users understood that the AI was performing the complex task it was designed for, and they knew exactly where to focus their attention if the final assessment seemed inaccurate. This design choice transformed a moment of anxiety into a moment of connection with the user. 
 Applying the Impact/Risk Matrix: What We Chose to Hide 
 Most AI experiences have no shortage of events and decision nodes that could potentially be displayed during processing. One of the most critical outcomes of the audit was to decide what to keep invisible. In the Meridian example, the backend logs generated 50+ events per claim. We could have defaulted to displaying each event as they were processed as part of the UI. Instead, we applied the risk matrix to prune them: 
 Log Event: Pinging Server West-2 for redundancy check. Filter Verdict: Hide. (Low Stakes, High Technicality). 
 Log Event: Comparing repair estimate to BlueBook value. Filter Verdict: Show. (High Stakes, impacts user’s payout). 
 By cutting out the unnecessary details, the important information — like the coverage verification — was more impactful. We created an open interface and designed an open experience . 
 This approach uses the idea that people feel better about a service when they can see the work being done. By showing the specific steps (Assessing, Reviewing, Verifying), we changed a 30-second wait from a time of worry ( “Is it broken?” ) to a time of feeling like something valuable is being created ( “It’s thinking” ). 
 Let’s now take a closer look at how we can review the decision-making process in our products to identify key moments that require clear information. 
 The Decision Node Audit Transparency fails when we treat it as a style choice rather than a functional requirement. We have a tendency to ask, “What should the UI look like?” before we ask, “What is the agent actually deciding?” 
 The Decision Node Audit is a straightforward way to make AI systems easier to understand. It works by carefully mapping out the system’s internal process. The main goal is to find and clearly define the exact moments where the system stops following its set rules and instead makes a choice based on chance or estimation. By mapping this structure, creators can show these points of uncertainty directly to the people using the system. This changes system updates from being vague statements to specific, reliable reports about how the AI reached its conclusion. 
 In addition to the insurance case study above, I recently worked with a team building a procurement agent. The system reviewed vendor contracts and flagged risks. Originally, the screen displayed a simple progress bar: “Reviewing contracts.” Users hated it. Our research indicated they felt anxious about the legal implications of a missing clause. 
 We fixed this by conducting a Decision Node Audit. I’ve included a step-by-step checklist for conducting this audit at the conclusion of this article. 
 We ran a session with the engineers and outlined how the system works. We identified “Decision Points” — moments where the AI had to choose between two good options. 
 In standard computer programs, the process is clear: if A happens, then B will always happen. In AI systems, the process is often based on chance. The AI thinks A is probably the best choice, but it might only be 65% certain. 
 In the contract system, we found a moment when the AI checked the liability terms against our company rules. It was rarely a perfect match. The AI had to decide if a 90% match was good enough. This was a key decision point. 
 Once we identified this node, we exposed it to the user. Instead of “Reviewing contracts,” the interface updated to say: “Liability clause varies from standard template. Analyzing risk level.” 
 This specific update gave users confidence. They knew the agent checked the liability clause. They understood the reason for the delay and gained trust that the desired action was occurring on the back end. They also knew where to dig in deeper once the agent generated the contract. 
 To check how the AI makes decisions, you need to work closely with your engineers, product managers, business analysts, and key people who are making the choices (often hidden) that affect how the AI tool functions. Draw out the steps the tool takes. Mark every spot where the process changes direction because a probability is met. These are the places where you should focus on being more transparent. 
 As shown in Figure 2 below, the Decision Node Audit involves these steps: 
 Get the team together: Bring in the product owners, business analysts, designers, key decision-makers, and the engineers who built the AI. For example, 
 Think about a product team building an AI tool designed to review messy legal contracts. The team includes the UX designer, the product manager, the UX researcher, a practicing lawyer who acts as the subject-matter expert, and the backend engineer who wrote the text-analysis code. 
 Draw the whole process: Document every step the AI takes, from the user’s first action to the final result. 
 The team stands at a whiteboard and sketches the entire sequence for a key workflow that involves the AI searching for a liability clause in a complex contract. The lawyer uploads a fifty-page PDF → The system converts the document into readable text. → The AI scans the pages for liability clauses. → The user waits. → Moments or minutes later, the tool highlights the found paragraphs in yellow on the user interface. They do this for many other workflows that the tool accommodates as well. 
 Find where things are unclear: Look at the process map for any spot where the AI compares options or inputs that don’t have one perfect match. 
 The team looks at the whiteboard to spot the ambiguous steps. Converting an image to text follows strict rules. Finding a specific liability clause involves guesswork. Every firm writes these clauses differently, so the AI has to weigh multiple options and make a prediction instead of finding an exact word match. 
 Identify the ‘best guess’ steps: For each unclear spot, check if the system uses a confidence score (for example, is it 85% sure?). These are the points where the AI makes a final choice. 
 The system has to guess (give a probability) which paragraph(s) closely resemble a standard liability clause. It assigns a confidence score to its best guess. That guess is a decision node. The interface needs to tell the lawyer it is highlighting a potential match, rather than stating it found the definitive clause. 
 Examine the choice: For each choice point, figure out the specific internal math or comparison being done (e.g., matching a part of a contract to a policy or comparing a picture of a broken car to a library of damaged car photos). 
 The engineer explains that the system compares the various paragraphs against a database of standard liability clauses from past firm cases. It calculates a text similarity score to decide on a match based on probabilities. 
 Write clear explanations: Create messages for the user that clearly describe the specific internal action happening when the AI makes a choice. 
 The content designer writes a specific message for this exact moment. The text reads: Comparing document text to standard firm clauses to identify potential liability risks. 
 Update the screen: Put these new, clear explanations into the user interface, replacing vague messages like “Reviewing contracts.” 
 The design team removes the generic Processing PDF loading spinner. They insert the new explanation into a status bar located right above the document viewer while the AI thinks. 
 Check for Trust: Make sure the new screen messages give users a simple reason for any wait time or result, which should make them feel more confident and trusting. 
 The Impact/Risk Matrix 
 Once you look closely at the AI’s process, you’ll likely find many points where it makes a choice. An AI might make dozens of small choices for a single complex task. Showing them all creates too much unnecessary information. You need to group these choices. 
 You can use an Impact/Risk Matrix to sort these choices based on the types of action(s) the AI is taking. Here are examples of impact/risk matrices: 
 First, look for low-stakes and low-impact decisions. 
 Low Stakes / Low Impact 
 Example: Organizing a file structure or renaming a document. 
 Transparency Need: Minimal. A subtle toast notification or a log entry suffices. Users can undo these actions easily. 
 Then identify the high-stakes and high-impact decisions. 
 High Stakes / High Impact 
 Example: Rejecting a loan application or executing a stock trade. 
 Transparency Need: High. These actions require Proof of Work. The system must demonstrate the rationale before or immediately as it acts. 
 Consider a financial trading bot that treats all buy/sell orders the same. It executes a $5 trade with the same opacity as a $50,000 trade. Users might question whether the tool recognizes the potential impact of transparency on trading on a large dollar amount. They need the system to pause and show its work for the high-stakes trades. The solution is to introduce a Reviewing Logic state for any transaction exceeding a specific dollar amount, allowing the user to see the factors driving the decision before execution. 
 Mapping Nodes to Patterns: A Design Pattern Selection Rubric 
 Once you have identified your experience's key decision nodes, you must decide which UI pattern applies to each one you’ll display. In Designing For Agentic AI, we introduced patterns like the Intent Preview (for high-stakes control) and the Action Audit (for retrospective safety). The decisive factor in choosing between them is reversibility. 
 We filter every decision node through the impact matrix in order to assign the correct pattern: 
 High Stakes & Irreversible: These nodes require an Intent Preview. Because the user cannot easily undo the action (e.g., permanently deleting a database), the transparency moment must happen before execution. The system must pause, explain its intent, and require confirmation. 
 High Stakes & Reversible: These nodes can rely on the Action Audit & Undo pattern. If the AI-powered sales agent moves a lead to a different pipeline, it can do so autonomously as long as it notifies the user and offers an immediate Undo button. 
 By strictly categorizing nodes this way, we avoid “alert fatigue.” We reserve the high-friction Intent Preview only for the truly irreversible moments, while relying on the Action Audit to maintain speed for everything else. 
 Reversible Irreversible 
 Low Impact Type : Auto-Execute 
 UI : Passive Toast / Log 
 Ex: Renaming a file Type : Confirm 
 UI : Simple Undo option 
 Ex: Archiving an email 
 High Impact Type : Review 
 UI : Notification + Review Trail 
 Ex: Sending a draft to a client Type : Intent preview 
 UI : Modal / Explicit Permission 
 Ex: Deleting a server 
 Table 1: The impact and reversibility matrix can then be used to map your moments of transparency to design patterns. 
 Qualitative Validation: “The Wait, Why?” Test 
 You can identify potential nodes on a whiteboard, but you must validate them with human behavior. You need to verify whether your map matches the user’s mental model. I use a protocol called the “Wait, Why?” Test . 
 Ask a user to watch the agent complete a task. Instruct them to speak aloud. Whenever they ask a question, “Wait, why did it do that?” or “Is it stuck?” or “Did it hear me?” — you mark a timestamp. 
 These questions signal user confusion. The user feels their control slipping away. For example, in a study for a healthcare scheduling assistant, users watched the agent book an appointment. The screen sat static for four seconds. Participants consistently asked, “Is it checking my calendar or the doctor’s?” 
 That question revealed a missing Transparency Moment . The system needed to split that four-second wait into two distinct steps: “Checking your availability” followed by “Syncing with provider schedule.” 
 This small change reduced users’ expressed levels of anxiety. 
 Transparency fails when it only describes a system action. The interface must connect the technical process to the user’s specific goal. A screen displaying “Checking your availability” falls flat because it lacks context. The user understands that the AI is looking at a calendar, but they do not know why. 
 We must pair the action with the outcome. The system needs to split that four-second wait into two distinct steps. First, the interface displays “Checking your calendar to find open times.” Then it updates to “Syncing with the provider’s schedule to secure your appointment.” This grounds the technical process in the user’s actual life. 
 Consider an AI managing inventory for a local cafe. The system encounters a supply shortage. An interface reading “contacting vendor” or “reviewing options” creates anxiety. The manager wonders if the system is canceling the order or buying an expensive alternative. A better approach is to explain the intended result: “Evaluating alternative suppliers to maintain your Friday delivery schedule.” This tells the user exactly what the AI is trying to achieve. 
 Operationalizing the Audit You have completed the Decision Node Audit and filtered your list through the Impact and Risk Matrix. You now have a list of essential moments for being transparent. Next, you need to create them in the UI. This step requires teamwork across different departments. You can’t design transparency by yourself using a design tool. You need to understand how the system works behind the scenes. 
 Start with a Logic Review . Meet with your lead system designer. Bring your map of decision nodes. You need to confirm that the system can actually share these states. I often find that the technical system doesn’t reveal the exact state I want to show. The engineer might say the system just returns a general “working” status. You must push for a detailed update. You need the system to send a specific notice when it switches from reading text to checking rules. Without that technical connection, your design is impossible to build. 
 Next, involve the Content Design team. You have the technical reason for the AI’s action, but you need a clear, human-friendly explanation. Engineers provide the underlying process, but content designers provide the way it’s communicated. Do not write these messages alone. A developer might write “Executing function 402,” which is technically correct but meaningless to the user. A designer might write “Thinking,” which is friendly but too vague. A content strategist finds the right middle ground. They create specific phrases, such as “Scanning for liability risks” , that show the AI is working without confusing the user. 
 Finally, test the transparency of your messages. Don’t wait until the final product is built to see if the text works. I conduct comparison tests on simple prototypes where the only thing that changes is the status message. For example, I show one group (Group A) a message that says “Verifying identity” and another group (Group B) a message that says “Checking government databases” (these are made-up examples, but you understand the point). Then I ask them which AI feels safer. You’ll often discover that certain words cause worry, while others build trust. You must treat the wording as something you need to test and prove effective. 
 How This Changes the Design Process 
 Conducting these audits has the potential to strengthen how a team works together. We stop handing off polished design files. We start using messy prototypes and shared spreadsheets. The core tool becomes a transparency matrix . Engineers and the content designers edit this spreadsheet together. They map the exact technical codes to the words the user will read. 
 Teams will experience friction during the logic review. Imagine a designer asking the engineer how the AI decides to decline a transaction submitted on an expense report. The engineer might say the backend only outputs a generic status code like “Error: Missing Data”. The designer states that this isn’t actionable information on the screen. The designer negotiates with the engineer to create a specific technical hook. The engineer writes a new rule so the system reports exactly what is missing, such as a missing receipt image. 
 Content designers act as translators during this phase. A developer might write a technically accurate string like “Calculating confidence threshold for vendor matching.” A content designer translates that string into a phrase that builds trust for a specific outcome. The strategist rewrites it as “Comparing local vendor prices to secure your Friday delivery.” The user understands the action and the result. 
 The entire cross-functional team sits in on user testing sessions. They watch a real person react to different status messages. Seeing a user panic because the screen says “Executing trade” forces the team to rethink their approach. The engineers and designers align on better wording. They change the text to “Verifying sufficient funds” before buying stock. Testing together guarantees the final interface serves both the system logic and the user’s peace of mind. 
 It does require time to incorporate these additional activities into the team’s calendar. However, the end result should be a team that communicates more openly, and users who have a better understanding of what their AI-powered tools are doing on their behalf (and why). This integrated approach is a cornerstone of designing truly trustworthy AI experiences. 
 Trust Is A Design Choice We often view trust as an emotional byproduct of a good user experience. It is easier to view trust as a mechanical result of predictable communication. 
 We build trust by showing the right information at the right time. We destroy it by overwhelming the user or hiding the machinery completely. 
 Start with the Decision Node Audit, particularly for agentic AI tools and products. Find the moments where the system makes a judgment call. Map those moments to the Risk Matrix. If the stakes are high, open the box. Show the work. 
 In the next article, we will look at how to design these moments: how to write the copy, structure the UI, and handle the inevitable errors when the agent gets it wrong. 
 Appendix: The Decision Node Audit Checklist Phase 1: Setup and Mapping 
 ✅ Get the team together: Bring in the product owners, business analysts, designers, key decision-makers, and the engineers who built the AI. 
 Hint: You need the engineers to explain the actual backend logic. Do not attempt this step alone. 
 ✅ Draw the whole process: Document every step the AI takes, from the user’s first action to the final result. 
 Hint: A physical whiteboard session often works best for drawing out these initial steps. 
 Phase 2: Locating the Hidden Logic 
 ✅ Find where things are unclear: Look at the process map for any spot where the AI compares options or inputs that do not have one perfect match. 
 ✅ Identify the best guess steps: For each unclear spot, check if the system uses a confidence score. For example, ask if the system is 85 percent sure. These are the points where the AI makes a final choice. 
 ✅ Examine the choice: For each choice point, figure out the specific internal math or comparison being done. An example is matching a part of a contract to a policy. Another example involves comparing a picture of a broken car to a library of damaged car photos. 
 Phase 3: Creating the User Experience 
 ✅ Write clear explanations: Create messages for the user that clearly describe the specific internal action happening when the AI makes a choice. 
 Hint: Ground your messages in concrete reality. If an AI books a meeting with a client at a local cafe, tell the user the system is checking the cafe reservation system. 
 ✅ Update the screen: Put these new, clear explanations into the user interface. Replace vague messages like Reviewing contracts with your specific explanations. 
 ✅ Check for Trust: Make sure the new screen messages give users a simple reason for any wait time or result. This should make them feel confident and trusting. 
 Hint: Test these messages with actual users to verify they understand the specific outcome being achieved.
```

---

## 10. A Practical Guide To Design Principles

- 日期: 2026-04-01 10:00
- 链接: https://smashingmagazine.com/2026/04/practical-guide-design-principles/

```
We often see design principles as rigid guidelines that dictate design decisions. But actually, they are an incredible tool to rally the team around a shared purpose and document the values and beliefs that an organization embodies. 
 They align teams and inform decision-making. They also keep us afloat amidst all the hype, big assumptions, desire for faster delivery, and AI workslop. But how do we choose the right ones, and how do we get started? Let’s find out. 
 Real-World Design Principles In times when we can generate any passable design and code within minutes, we need to decide better what’s worth designing and building — and what values we want our products to embody. 
 It’s similar to voice and tone. You might not design it intentionally, but then end users will define it for you. And so, without principles, many company initiatives are random, sporadic, ad-hoc — and feel vague, inconsistent, or simply dull to the outside world. 
 Design principles are guidelines and design considerations that designers apply with discretion — by default, without debating or discussing what has already been agreed upon. 
 One fantastic resource that I keep coming back to after all these years is Ben Brignell’s Principles.design . It has 230 pointers for design principles and methods , searchable and tagged, covering everything from language and infrastructure to hardware and organizations. 
 10 Principles Of Good Design There is no shortage of principles out there. But the good ones are more than just being visionary — they have a point of view , and they explain what we don’t do as much as what we do. They also explain what we stand for in the world — beyond profits, stock prices, and all the hype and noise around us. 
 Many years ago, I encountered Dieter Rams’ 10 principles of good design (see above), a very humble, practical and tangible overview of principles that were informing, shaping, and guarding his design work at Braun. 
 There are no visionary claims , and no big bold statements: just a clear overview of what we do, and where our ambition and care lie for the products we are designing. It’s honest, sincere, and in many ways beautifully humane . 
 Examples Of Design Principles 
 There are plenty of wonderful examples that I keep close: 
 Anthropic’s Constitution 
 Principles of Product Design , by Joshua Porter 
 Guiding Principles for Experience Design , by Whitney Hess, PCC 
 Principles of Web Accessibility , by Heydon Pickering 
 Humane by Design , by Jon Yablonski 
 Designing Voice UX Principles , by Brian Colcord 
 Agentic Design Principles , by Linear 
 AI Chatbot Design Principles , by Emmet Connolly 
 Voice UX Principles , by Ben Sauer 
 Design Principles In Design Systems 
 18F 
 Audi 
 Carbon (IBM) 
 Firefox 
 Gov.uk 
 Intuit 
 NHS 
 Nordhealth 
 Uber 
 How To Establish Design Principles Design principles can be personal, but usually they are committed to and shaped by the entire product team . Design principles aren’t just for designers . User’s experience is everything from performance to support to customer service, and ideally, participants would cover these areas as well. 
 In practice, though, establishing principles might feel incredibly challenging. They are abstract and fluffy and often ambiguous, and often very difficult to agree upon. 
 You can get started with a simple 8-step workshop (inspired by Marcin Treder , Maria Meireles and Better ): 
 Pre-session Research 
 Study how users speak about the products, what they appreciate, and the words they use. 
 Get Into Principles Mode 
 Invite 6–8 participants, ask them to choose their favorite object, and describe it in 3 words. 
 Product Analogies 
 Compare product to tangible items (e.g., ‘A Porsche 911’ or ‘a Braun audio system’). 
 Extract Attributes 
 Individually, in silence, everyone writes 3–5 initial principles, which are then grouped by theme for review. 
 Link Attributes To Research 
 Link attributes to actual user pain points or desires, to make sure they are grounded in reality. 
 Value Statements 
 We write ‘We want X because of Y’ sentences that express the rationale behind our thinking. 
 Move to Principles 
 Remove analogies to create enduring rules that will guide our design process. 
 Reality Check 
 Search for both positive and negative examples in our products to see where principles are being met or ignored. 
 Useful Starter Kits For Principles Workshops 
 Design Principles Workshop (Figma Template) , by Maria Meireles 
 Design Principles Workshop (FigJam Template) , by Richard Picot 
 How to Create Design Principles (Miro Workshop Template) , by NanoGiants 
 Wrapping Up Creating principles is only a small portion of the work; most work is about effectively sharing and embedding them . It’s difficult to get anywhere without finding ways to make design principles a default — by revisiting settings, templates, naming conventions, and output. 
 Principles help avoid endless discussions that often stem from personal preferences or taste. But design should not be a matter of taste; it must be guided by our goals and values. Design principles can help with just that. 
 Meet “Design Patterns For AI Interfaces” Meet Design Patterns For AI Interfaces , Vitaly’s new video course with 100s of real-life examples and UX guidelines to design AI features that people actually use — with a live UX training later this year. Jump to a free preview . 
 Meet Design Patterns For AI Interfaces , Vitaly’s video course on interface design & UX. 
 Video + UX Training 
 Video only 
 Video + UX Training 
 $ 450.00 $ 799.00 Get Video + UX Training 
 30 video lessons (10h) + Live UX Training . 
 100 days money-back-guarantee. 
 Video only 
 $ 275.00$ 395.00 
 Get the video course 
 30 video lessons (10h). Updated yearly. 
 Also available as a UX Bundle with 3 video courses. 
 Useful Resources Design Principles Collection , by Ben Brignell 
 “ How To Establish Design Principles ”, by Marcin Treder 
 “ Establishing Design Principles for a Design System and What It Taught Us ”, by Better Design Team 
 Design Principles , by Jeremy Keith 
 Design Principles Collection , by Gabriel Svennerberg 
 Design Principles Workshop (Figma Template) , by Maria Meireles 
 Design Principles Workshop (FigJam Template) , by Richard Picot 
 How to Create Design Principles (Miro Workshop Template) , by NanoGiants 
 Modals in Design Systems
```

---

## 11. The Joy Of A Fresh Beginning (April 2026 Wallpapers Edition)

- 日期: 2026-03-31 11:00
- 链接: https://smashingmagazine.com/2026/03/desktop-wallpaper-calendars-april-2026/

```
Starting the new month with a little inspiration boost — that’s the idea behind our monthly wallpapers series which has been going on for more than 15 years already. Each month, the wallpapers are created by the community for the community , and everyone who has an idea for a design is welcome to join in — experienced designers just like aspiring artists. 
 For this edition, creative folks from across the globe once again got their ideas flowing and designed desktop wallpapers that are sure to bring some good vibes to your screens . You’ll find them compiled below, ready to be downloaded in a variety of screen resolutions. A huge thank-you to everyone who shared their designs with us — you’re truly smashing ! 
 If you too would like to get featured in one of our upcoming posts, please don’t hesitate to submit your wallpaper . We can’t wait to see what you’ll come up with! Happy April! 
 You can click on every image to see a larger preview . 
 We respect and carefully consider the ideas and motivation behind each and every artist’s work. This is why we give all artists the full freedom to explore their creativity and express emotions and experience through their works. This is also why the themes of the wallpapers weren’t anyhow influenced by us but rather designed from scratch by the artists themselves. 
 April Blooms “The search for colorful Easter eggs comes at just the right time. After long winter months of searching for sunlight and meaning, April blooms have never been more welcome.” — Designed by Ginger It Solutions from Serbia. 
 preview 
 with calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Happiness In Full Bloom Designed by Ricardo Gimenes from Spain. 
 preview 
 with calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Blade Dance Designed by Ricardo Gimenes from Spain. 
 preview 
 with calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Swing Into Spring “Our April calendar doesn’t need to mark any special occasion — April itself is a reason to celebrate. It was a breeze creating this minimal, pastel-colored calendar design with a custom lettering font and plant pattern for the ultimate spring feel.” — Designed by PopArt Studio from Serbia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Dreaming “The moment when you just walk and your imagination fills up your mind with thoughts.” — Designed by Gal Shir from Israel. 
 preview 
 without calendar: 340x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Clover Field Designed by Nathalie Ouederni from France. 
 preview 
 without calendar: 1024x768 , 1280x1024 , 1440x900 , 1680x1200 , 1920x1200 , 2560x1440 
 Spring Awakens “We all look forward to the awakening of a life that spreads its wings after a dormant winter and opens its petals to greet us. Long live spring, long live life.” — Designed by LibraFire from Serbia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Inspiring Blossom “‘Sweet spring is your time is my time is our time for springtime is lovetime and viva sweet love,’ wrote E. E. Cummings. And we have a question for you: Is there anything more refreshing, reviving, and recharging than nature in blossom? Let it inspire us all to rise up, hold our heads high, and show the world what we are made of.” — Designed by PopArt Studio from Serbia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Rainy Day Designed by Xenia Latii from Berlin, Germany. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 A Time For Reflection “‘We’re all equal before a wave.’ (Laird Hamilton)” — Designed by Shawna Armstrong from the United States. 
 preview 
 without calendar: 1440x900 , 1600x1200 , 1680x1050 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Wildest Dreams “We love the art direction, story, and overall cinematography of the ‘Wildest Dreams’ music video by Taylor Swift. It inspired us to create this illustration. Hope it will look good on your desktops.” — Designed by Kasra Design from Malaysia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Coffee Morning Designed by Ricardo Gimenes from Spain. 
 preview 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Sakura “Spring is finally here with its sweet Sakura flowers, which remind me of my trip to Japan.” — Designed by Laurence Vagner from France. 
 preview 
 without calendar: 1280x800 , 1280x1024 , 1680x1050 , 1920x1080 , 1920x1200 , 2560x1440 
 The Perpetual Circle “Inspired by the Black Forest, which is beginning right behind our office windows, so we can watch the perpetual circle of nature when we take a look outside.” — Designed by Nils Kunath from Germany. 
 preview 
 without calendar: 320x480 , 640x480 , 1024x768 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 The Loneliest House In The World “March 26 was Solitude Day. To celebrate it, here is the picture about the loneliest house in the world. It is a real house, I found it on Youtube .” — Designed by Vlad Gerasimov from Georgia. 
 preview 
 without calendar: 800x480 , 800x600 , 1024x600 , 1024x768 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1440x960 , 1600x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 2560x1600 , 2880x1800 , 3072x1920 , 3840x2160 , 5120x2880 
 Happy Easter Designed by Tazi Design from Australia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x600 , 1024x768 , 1152x864 , 1280x720 , 1280x960 , 1600x1200 , 1920x1080 , 1920x1440 , 2560x1440 
 Playful Alien “Everything would be more fun if a little alien had the controllers.” — Designed by Maria Keller from Mexico. 
 preview 
 without calendar: 320x480 , 640x480 , 640x1136 , 750x1334 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1242x2208 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 2880x1800 
 Springtime Sage “Spring and fresh herbs always feel like they compliment each other. Keeping it light and fresh with this wallpaper welcomes a new season!” — Designed by Susan Chiang from the United States. 
 preview 
 without calendar: 320x480 , 1024x768 , 1280x800 , 1280x1024 , 1400x900 , 1680x1200 , 1920x1200 , 1920x1440 
 April Showers Designed by Ricardo Gimenes from Spain. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Fairy Tale “A tribute to Hans Christian Andersen. Happy Birthday!” — Designed by Roxi Nastase from Romania. 
 preview 
 without calendar: 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 First Day Of Spring “April is my birthday month! Creating this wallpaper was a reminder of the new beginnings spring brings!” — Designed by Marykate Boyle from the United States. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Citrus Passion Designed by Nathalie Ouederni from France. 
 preview 
 without calendar: 320x480 , 1024x768 , 1200x1024 , 1440x900 , 1600x1200 , 1680x1200 , 1920x1200 , 2560x1440 
 I “Love” My Dog Designed by Ricardo Gimenes from Spain. 
 preview 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Ready For April “It is very common that it rains in April. This year, I am not sure… But whatever… we are just prepared!” — Designed by Verónica Valenzuela from Spain. 
 preview 
 without calendar: 800x480 , 1024x768 , 1152x864 , 1280x800 , 1280x960 , 1440x900 , 1680x1200 , 1920x1080 , 2560x1440 
 Good Day “Some pretty flowers and spring time always make for a good day.” — Designed by Amalia Van Bloom from the United States. 
 preview 
 without calendar: 640x1136 , 1024x768 , 1280x800 , 1280x1024 , 1440x900 , 1920x1200 , 2560x1440 
 Yellow Submarine “The Beatles — ‘Yellow Submarine’: This song is fun and at the same time there is a lot of interesting text that changes your thinking. Like everything that makes The Beatles.” — Designed by WebToffee from India. 
 preview 
 without calendar: 360x640 , 1024x768 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x900 , 1680x1200 , 1920x1080 
 Spring Fever “I created that mouse character for a series of illustrations about a poem my mom often told me when I was a child. In that poem the mouse goes on an adventure. Here it is after the adventure, ready for new ones.” — Designed by Anja Sturm from Germany. 
 preview 
 without calendar: 320x480 , 800x600 , 1024x768 , 1280x720 , 1440x900 , 1620x1050 , 1920x1080 
 In The River “Spring is here! Crocodiles search the hot and stay in the river.” — Designed by Veronica Valenzuela from Spain. 
 preview 
 without calendar: 640x480 , 800x480 , 1024x768 , 1280x720 , 1280x800 , 1440x900 , 1600x1200 , 1920x1080 , 1920x1440 , 2560x1440 
 Purple Rain “This month is International Guitar Month! Time to get out your guitar and play. As a graphic designer/illustrator seeing all the variations of guitar shapes begs to be used for a fun design. Search the guitar shapes represented and see if you see one similar to yours, or see if you can identify some of the different styles that some famous guitarists have played (BTW, Prince’s guitar is in there and purple is just a cool color).” — Designed by Karen Frolo from the United States. 
 preview 
 without calendar: 1024x768 , 1024x1024 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Get Featured Next Month Feeling inspired? We’ll publish the May wallpapers on April 30, so if you’d like to be a part of the collection, please don’t hesitate to submit your design . We are already looking forward to it!
```

---

## 12. The Site-Search Paradox: Why The Big Box Always Wins

- 日期: 2026-03-26 10:00
- 链接: https://smashingmagazine.com/2026/03/site-search-paradox-why-big-box-always-wins/

```
In the early days of the web, the search bar was a luxury, added to a site once it became “too big” to navigate by clicking. We treated it like an index at the back of a book: a literal, alphabetical list of words that pointed to specific pages. If you typed the exact word the author used, you found what you needed. If you didn’t, you were met with a “0 Results Found” screen that felt like a digital dead end. 
 Twenty-five years later, we are still building search bars that act like 1990s index cards, even though the humans using them have been fundamentally rewired. Today, when a user lands on your site and can’t find what they need in the global navigation within seconds, they don’t try to learn your taxonomy. They head for the search box. But if that box fails them, and demands they use your specific brand vocabulary, or punishes them for a typo, they do something that should keep every UX designer awake at night. They leave your site, go to Google, and type site:yourwebsite.com [query] . Or, worse still, they just type in their query and end up on a competitor’s website. I personally use Google over a site’s search nearly every time. 
 This is the Site-Search Paradox . In an era where we have more data and better tools than ever, our internal search experiences are often so poor that users prefer to use a trillion-dollar global search engine to find a single page on a local site. As Information Architects and UX designers, we have to ask, why does the “Big Box” win, and how can we take our users back? 
 The “Syntax Tax” And The Death Of Exact Match The primary reason site search fails is what I call the Syntax Tax . This is the cognitive load we place on users when we require them to guess the exact string of characters we’ve used in our database. 
 Research by Origin Growth on Search vs Navigate shows that roughly 50% of users go straight to the search bar upon landing on a site. For example, when a user types “sofa” into a furniture site that has categorised everything under “couches,” and the site returns nothing, the user doesn’t think, “Ah, I should try a synonym.” They think, “This site doesn’t have what I want.” 
 This is a failure of Information Architecture (IA) . We’ve built our systems to match strings (literal sequences of letters) rather than things (the concepts behind the words). When we force users to match our internal vocabulary, we are taxing their brainpower. 
 Why Google Wins: It’s Not Power, It’s Context It is easy to throw our hands up and say, “We can’t compete with Google’s engineering.” But Google’s success isn’t just about raw power; it’s about contextual understanding . While we often treat search as a technical utility, Google treats it as an IA challenge. 
 Data from the Baymard Institute reveals that 41% of e-commerce sites fail to support even basic symbols or abbreviations, and this often leads to users abandoning a site after a single failed search attempt. Google wins because it uses stemming and lemmatization — IA techniques that recognize “running” and “ran” are the same intent. Most internal searches are “blind” to this context, treating “Running Shoe” and “Running Shoes” as entirely different entities. 
 If your site search can’t handle a simple plural or a common misspelling, you are effectively charging your users a tax for being human. 
 The UX Of “Maybe”: Designing For Probabilistic Results In traditional IA, we think in binaries: A page is either in a category, or it isn’t. A search result is either a match or it isn’t. Modern search, which users now expect, is probabilistic . It deals in “confidence levels.” 
 According to Forresters , users who use search are 2–3 times more likely to convert than those who don’t, if the search works. And 80% of users on e-commerce sites exit a site due to poor search results. 
 As designers, we rarely design for the middle ground. We design a “ Results Found ” page and a “ No Results ” page. We miss the most important state: The “Did You Mean?” State. A well-designed search interface should provide “Fuzzy” matches. Instead of a cold “0 Results Found” screen, we should be using our metadata to say, “We didn’t find that in ‘Electronics,’ but we found 3 matches in ‘Accessories’.” By designing for “Maybe,” we can keep the user in the flow. 
 Case Study: The Cost Of “Invisible” Content To understand why IA is the fuel for the search engine, we must look at how data is structured behind the scenes. In my 25 years of practice, I’ve seen that the “findability” of a page is directly tied to its structured metadata. 
 Consider a large-scale enterprise I worked with that had over 5,000 technical documents. Their internal search was returning irrelevant results because the “Title” tag of every document was the internal SKU number (e.g., “DOC-9928-X”) rather than the human-readable name. 
 By reviewing the search logs, we discovered that users were searching for “installation guide.” Because that phrase didn’t appear in the SKU-based title, the engine ignored the most relevant files. We implemented a Controlled Vocabulary , which was a set of standardised terms that mapped SKUs to human language. Within three months, the “Exit Rate” from the search page dropped by 40%. This wasn’t an algorithmic fix; it was an IA fix. It proves that a search engine is only as good as the map we give it. 
 The Internal Language Gap Throughout my two decades in UX, I’ve noticed a recurring theme: internal teams often suffer from “The curse of knowledge.” We become so immersed in our own corporate vocabulary, or sometimes referred to as business jargon, that we forget the user doesn’t speak our language. 
 I once worked with a financial institution that was frustrated by high call volumes to their support centre. Users were complaining they couldn’t find “loan payoff” information on the site. When we looked at the search logs, “loan payoff” was the #1 searched term that resulted in zero hits. 
 Why? Because the institution’s IA team had labelled every relevant page under the formal term “Loan Release.” To the bank, a “payoff” was a process, but a “Loan Release” was the legal document that was the “thing” in the database. Because the search engine was looking for literal character strings, it refused to connect the user’s desperate need with the company’s official solution. 
 This is where the IA professional must act as a translator. By simply adding “loan payoff” as a hidden metadata keyword to the Loan Release pages, we solved a multi-million dollar support problem. We didn’t need a faster server; we needed a more empathetic taxonomy . 
 The 4-step Site-search Audit Framework If you want to reclaim your search box from Google, you cannot simply “set it and forget it.” You must treat search as a living product. Here is the framework I use to audit and optimise search experiences: 
 Phase 1: The “Zero-result” Audit 
 Pull your search logs from the last 90 days. Filter for all queries that returned zero results. Group these into three buckets: 
 True gaps 
 Content the user wants that you simply don’t have (a signal for your content strategy team). 
 Synonym gaps 
 Content you have, but described in words the user doesn’t use (e.g., “Sofa” vs “Couch”). 
 Format gaps 
 The user is looking for a “video” or “PDF,” but your search only indexes HTML text. 
 Phase 2: Query Intent Mapping 
 Analyse the top 50 most common queries. Are they Navigational (looking for a specific page), Informational (looking for “how to”), or Transactional (looking for a specific product)? Your search UI should look different for each. A navigational search should “Quick-Link” the user directly to the destination, bypassing the results page entirely. 
 Phase 3: The “Fuzzy” Matching Test 
 Intentionally mistype your top 10 products. Use plurals, common typos, and American vs. British English spellings (e.g., “Color” vs. “Colour”). If your search fails these tests, your engine lacks “stemming” support. This is a technical requirement you must advocate for to your engineering team. 
 Phase 4: Scoping And Filtering UX 
 Look at your results page. Does it offer filters that actually make sense? If a user searches for “shoes," they should see filters for Size and Colour . Generic filters can be as bad as no filters. 
 Reclaiming The Search Box: A Strategy For IA Professionals To stop the exodus to Google, we must move beyond the “Box” and look at the scaffolding . 
 Step A: Implement semantic scaffolding. 
 Don’t just return a list of links. Use your IA to provide context. If a user searches for a product, show them the product, but also show them the manual , the FAQs , and the related parts . This “associative” search mimics how the human brain works and how Google operates. 
 Step B: Stop being a librarian, start being a concierge. 
 A librarian tells you exactly where the book is on the shelf. A concierge listens to what you want to achieve and gives you a recommendation. Your search bar should use predictive text not just to complete words, but to suggest intentions . 
 Using A Google-powered Search Bar Using a “Google-powered” search bar, as seen on the University of Chicago website, is essentially an admission that a site’s internal organisation has become too complex for its own navigation to handle. While it is a quick “fix” for massive institutions to ensure users find something , it is generally a poor choice for businesses with deep content. 
 By delegating the search to Google, you surrender the user experience to an outside algorithm. You lose the ability to promote specific products, you expose your users to third-party ads, and you train your customers to leave your ecosystem the moment they need help. For a business, search should be a curated conversation that guides a customer toward a goal, not a generic list of links that pushes them back to the open web. 
 The Simple Search UX Checklist Here is a final checklist for reference when you are building the search experience for your users. Work with your product team to ensure you are engaging with the right team members. 
 Kill the dead-end. 
 Never just say “ No results found .” If an exact match isn’t there, suggest a similar category, a popular product, or a way to contact support. 
 Fix “almost” matches. 
 Make sure the search can handle plurals (like “plant” vs. “plants”) and common typos. Users shouldn’t be punished for a slip of the thumb. 
 Predict the user’s goal. 
 Use an “auto-suggest” menu to show helpful actions (like “Track my order”) or categories, not just a list of words. 
 Talk like a human. 
 Look at your search logs to see the words people actually use. If they type “couch” and you call it “sofa,” create a bridge in the background so they find what they need anyway. 
 Smart filtering. 
 Only show filters that matter. If someone searches for “shoes,” show them size and color filters, not a generic list that applies to the whole site. 
 Show, don’t just list. 
 Use small thumbnails and clear labels in the search results so users can see the difference between a product, a blog post, and a help article at a glance. 
 Speed is trust. 
 If the search takes more than a second, use a loading animation. If it’s too slow, people will immediately go back to Google. 
 Check the “failure” logs. 
 Once a month, look at what people searched for that returned zero results. This is your “to-do list” for fixing your site’s navigation. 
 Conclusion: The Search Bar Is A Conversation The search box is the only place on your site where the user tells us exactly, in their own words, what they want. When we fail to understand those words, when we let the “Big Box” of Google do the work for us, we aren’t just losing a page view. We are losing the opportunity to prove that we understand our customers. 
 Success in modern UX isn’t about having the most content; it’s about having the most findable content. It’s time to stop taxing users for their syntax and start designing for their intent. 
 By moving from literal string matching to semantic understanding, and by supporting our search engines with robust, human-centered Information Architecture, we can finally close the gap.
```

---

## 13. Testing Font Scaling For Accessibility With Figma Variables

- 日期: 2026-03-24 13:00
- 链接: https://smashingmagazine.com/2026/03/testing-font-scaling-accessibility-figma-variables/

```
Building a true culture of digital accessibility in a company is a mission of resilience and perseverance. It’s not difficult for the discourse on accessibility to fall into the usual clichés. Accessibility is very important for people. The accessibility of digital products and services promotes inclusion. Or even, all professionals on the teams should be involved in accessibility work. Of course. No one in their right mind will dispute any of these statements (I hope). 
 However, the second part of this conversation, which very few companies reach, is “how?” How do we make this happen in the midst of the day-to-day work of digital transformation teams, which, as we all know, are immersed in demanding scripts, often with a very limited number of people available? Most of the time, the choice ends up being between “we do this” and “that.” And it shouldn’t, because, in these cases, I never saw accessibility winning in this equation. 
 It shouldn’t be this way. You don’t need to be this way. First of all, because choosing between accessibility and anything else isn’t the right choice. Accessibility is no longer just another feature to be added to the others. It’s an added value for the business and, currently, a legal obligation that can have serious consequences for companies. On the other hand, there are intelligent, optimized, and impactful ways to incorporate accessibility principles into the natural dynamics of teams. It’s possible to work on accessibility without turning team operations upside down. In essence, that’s what AccessibilityOps does. Empowering people and providing teams with simple processes so they can integrate accessibility work into their daily routines without disproportionate effort. 
 Accessibility And Design Working on digital accessibility in design can involve several actions. It’s clear that we need to pay particular attention to color and how it’s used to convey meaning. Of course, the interaction sizes of elements must be comfortable. But, most importantly, we must think about design from a versatile perspective . An interface isn’t a poster. We can control many aspects of that design, but how users interact with the interface is subject to an endless number of variables. The type of device, context, purpose, network quality, etc. All of this greatly affects each person’s experience and interaction. Along with all this, when digital accessibility concerns are brought into the design process, it adds even more variables. 
 People often use what are called assistive technologies and strategies . Basically, these are technological tools or, at the very least, “tricks” that people resort to in order to find more comfortable usage models. The famous screen readers, commonly associated with the use of blind people (but which are not only useful to them), for example, are an assistive technology. Changing colors or color contrasts between different elements is also an assistive technology. Increasing the font size (which we discussed in this text) is another example. There are countless assistive technologies and strategies. Almost as many as the different contexts of use for each person. 
 We Don’t Control Everything In other words (and this is the “bad news” for us designers), “our design” is subject, from the users’ perspective, to transformations that we don’t control. It will be “transformed” by the user, ensuring that they can interact with the application and everything it offers in the most comfortable way possible. And that’s a good thing. If this happens and everything goes well, we will have surely done our accessibility work very well, and we all deserve congratulations. If the user applies any of these support technologies and strategies and still cannot use the digital application, it’s a sign that something is not working as it should. 
 Oh, and speaking of which. Don’t even think about blocking the use of these technologies or support strategies. They may be “destroying” your beautiful design, but they are allowing more and more people to actually use the app. In the end, wasn’t that exactly what we promised we wanted to do? Design for (all) people. Without exception? 
 Increase Font Size How many times have we heard someone — friends, family, or even colleagues — complaining that this or that text is too small? Text plays a very important role in the digital experience. Much information is conveyed through text: instructions for use, button captions, or interactive elements. All of this uses text as a communication tool. If reading all these elements is difficult, naturally, the experience is severely impaired. 
 Comfortable text reading, regardless of its function, is a non-negotiable principle. This reading can be facilitated by using comfortable sizes in the design. However, supporting technologies and strategies, through the functionality of increasing font size, can also help improve readability. According to APPT data, 26% of Android and iOS mobile device users increase the default font size (data from February 2026). One in four users increases the font size on their smartphone. This is a very significant sample of people, making this functionality unavoidable in design processes. 
 Compliance With Guidelines Increasing font size in interfaces can represent a huge design challenge. It’s important to understand that, suddenly, some text elements, due to user actions, can double in size from their initial size. 
 “With the exception of captions and text images, text can be resized without assistive technology up to 200% without loss of content or functionality.” 
 — Success criterion 1.4.4, “Resizing Text” of the Web Content Accessibility Guidelines (WCAG), version 2.2 
 This success criterion is at the AA compliance level, meaning this is an absolutely mandatory feature according to any legal framework. 
 It’s easy to understand the 200% in this success criterion. If we assume we design the interfaces at a 100% scale, meaning the element size is the initial size, then increasing the text by up to 200% will correspond to doubling the initial size. Other enlargement scales can also be used, such as 120%, 140%, and so on. In other words, we have to ensure that users can increase the text to double its initial size through supporting technologies or strategies (and this is not a minor detail). 
 To comply with this standard, we don’t need to provide text size increase tools in the interfaces. In practice, these features are nothing more than redundancy. Devices already allow this to be done in a standardized way. Users who really need this setting know it (because, without it, their lives would be much more difficult). Well, they already have this setting applied across their device. And that means we can eliminate these additional interface elements, simplifying the experience. 
 Standardized Access An important concept to remember about assistive technologies, particularly in this case regarding increasing font size, is that most devices already have many of these tools installed by default. In other words, in many cases, users don’t need to purchase their own software or buy a specific type of device just to have this functionality. 
 Whether on mobile devices or even in web browsers, in the vast majority of cases, it’s easy to find installed features that allow you to increase the default font size we’re using throughout the interface. This principle of increasing font size can be applied to digital products, such as apps, or even to any type of website running on the standard web browsers used today. 
 iPhones 
 On iPhone devices, the font size increase feature is integrated by default. To use this feature, simply access the “Settings” panel, select “Accessibility,” and within the “Vision” options group, access the “Text Size and Display” feature and configure the desired font size increase on that screen. 
 Google Chrome 
 Web browsers also offer, by default, the functionality to increase font size. For example, in Google Chrome, this feature is available in the “Options” panel, specifically in the “Appearance” area. In the list of options that appear in this group, simply select the “Font size” option. Normally, the “Medium — Recommended” option will be selected. You can change this setting to any other available font size. Try, for example, the “Very large” option. 
 Test In Figma To ensure that digital accessibility work becomes effective in the daily lives of teams, it is essential to find simple work processes . Actions or initiatives that can be integrated into the team’s routine, that address accessibility in an integrated way, and do not require a dramatic transformation of the current reality. If that were necessary, he believes, it wouldn’t happen most of the time. Therefore, designing simple work processes is half the battle for accessibility to truly happen, in this case, also within a design team. 
 Regarding testing font size increases in design, we have extraordinary tools at our disposal today. Those who remember the days of designing complex interfaces in Adobe Photoshop will recognize the differences in the tools we have today (and thankfully so). It’s now possible, through tools like Figma , to create such dynamism in design that testing font size increases for accessibility becomes almost unavoidable for the team. 
 Note : To take this test, you need to have a strong grasp of Figma’s text styles , auto layouts , and variables . These three are fundamental tools for success without much extra effort. If you haven’t yet mastered these features, it’s highly recommended that you start there. Don’t skip steps. Learning is a gradual process that must be followed in a structured, step-by-step manner. 
 Where Do We Want To Go? 
 The font size increase test in Figma that we want to perform is simple. We want to have a set of variables available for all the text styles we use in the interface, allowing us to choose whether we want to see the interface with the text at a scale of 100%, 120%, 140%, 160%, 180%, or 200%. As we apply this set of variables (much like applying variables for light and dark mode), we observe the transformations of the text in the interface and understand to what extent adaptations are needed in each version of the interface with different typographic scales. 
 How Do We Make This Happen? 
 For this test to go so smoothly, you need to do some groundwork. Design systems can greatly help optimize much of this initial work. But I won’t lie to you. For the test to work well, your design needs to have a very serious level of organization and systematization. 
 This isn’t really a guide, because each team will have its own work model, and these recommendations can be applied in different ways (and that’s okay). However, for this test to work, it’s important to ensure certain assumptions in the design. To help you phase the implementation of this test model, here are some steps to follow. Step-by-step instructions to guide you in organizing your files and ensuring you can fully execute this test in the simplest and most practical way possible. 
 1. Designing The Interfaces 
 It all starts with the design. Before any testing, the focus should, as it should, be on the design of each interface that we will want to test later. At this stage, there is still no specific concern with the font size increase test that we will perform later. Naturally, all interface design should, from the outset, follow the most basic accessibility recommendations applied to design. 
 2. Apply Auto Layouts To All Elements 
 In every screen design you create, you’ll need to ensure you apply auto layouts perfectly. This is a very important step. It’s this consistent application of auto layouts to the entire structure and design elements that will later guarantee the scalability of the interface when we start testing font size increases. You really can’t underestimate this step. If you don’t pay it the attention it deserves, you’ll see when we test typographic scaling in the interfaces, everything breaking down like an elephant in a china shop. 
 3. Structuring And Applying Text Styles 
 To perform our font size increase test, we’ll also need you to have applied text styles to each interface design. You probably even started creating them as you were drawing. Great. If you haven’t done so, it’s important that you do it now. For the test to work perfectly, we really need this. Don’t leave any text element in the design without a text style applied. 
 4. Define The Set Of Variables 100% 
 This test forces a fairly high degree of optimization. In practice, this means we will have to use Figma variables for all the characteristics of the text styles we have in the interface. At this stage, you must define Figma “number” variables for at least the font-size and line-height of the text styles you applied to the drawing. With this step, you are defining the font size increase scale values for a 100% visualization model, that is, the initial and reference version of the drawing. It is important that you structure these variables for each text style in the drawing because, subsequently, we will have to consider the enlargement scale of each of these text elements. 
 5. Apply The Variables To The Text Styles 
 Having defined the variables for the 100% scale text styles, you must now apply them to the elements of the text styles already created. Don’t forget to apply variables at least to the font-size and line-height characteristics. If you have more typographical variables, that’s fine. But you should at least have variables applied to font-size and line-height. This is really very important. 
 6. Define The Variables For Increasing The Text Size 
 Now that you have the variables applied to the 100% scale text styles, the next step is to create the variables for the other font size increase scales. In practice, you have to create the variables that will tell the system what font size each text style will grow to when the increase scale is 120%, 140%, 160%, etc. 
 To define the font-size and line-height values, simply multiply the initial value by the scale percentage. For example, if a text style has a font-size of 16px, the size for the 120% scale will be 16 multiplied by 1.2, which gives a result of 19.2. Repeat this calculation for all font-size and line-height values of the font size increase scale percentages you choose. 
 You can also choose whether or not to apply rounding to the final values. This is an approximate test, and therefore any differences that may arise from rounding will not affect the final perception of the test result. 
 7. Apply Variables To Different Scale Versions 
 The moment of truth has arrived. The next step is to understand if we have everything working so that the test runs perfectly. Therefore, you should copy the original interface and apply the set of variables for each of the font size increase rates that make sense to you. Repeat this process for all the font size increase percentages you have defined. 
 As a suggestion, you can use the 120%, 140%, 160%, 180%, and 200% increase percentages as a reference. If you want to simplify, you can reduce the number of scaling percentages you are working with. Regardless of the number of percentages you are working with, you should always work with the minimum of 100% and 200% scales. 
 8. Identify Areas For Improvement 
 By applying different font size increase scales to the same screen, it’s easy to understand where improvements might be needed. This is where the real test of increasing font size in interface design and the most interesting accessibility work begins. 
 In your analysis of the various screens, keep some important aspects in mind: 
 The fact that the text appears gigantic isn’t a problem and doesn’t “ruin” the design. Remember that this can mean the difference between someone being able to use a particular product or service or not. 
 An accessibility problem exists when increasing the font size makes it impossible for the user to read certain texts or to activate certain controls. 
 For text elements that are already very large, increasing the font size might not make sense. Doing so could make those elements disproportionate, which wouldn’t improve readability (since they are already a good size) and would occupy completely unnecessary space. 
 If there are elements that appear to be popping out of the screen, the first step is to confirm how you are applying auto layout . Many design aspects can be easily resolved with the proper use of auto layout. 
 Regardless of the scale of font size increase, it is essential to maintain the visual hierarchy of the typography , as this readability is important for perceiving the different levels of information present on the screen. 
 This test can help identify elements that may need adjustments directly in the code to function well at a given scale of increase. Not everything can be solved through design alone, and that’s perfectly fine. Accessibility is essentially a team effort. 
 9. Make Corrections And Adjustments To The Design 
 Finally, based on the various screens with different text enlargement scales applied, you can make the design changes that make sense. Some of these adjustments may only be necessary in code. In these cases, you document all these suggestions and pass them on to the development team. It is also crucial to reinforce (again) that some of the problems you may encounter in the design can be quickly resolved in the design process, with the simple and correct application of auto-layout properties. 
 10. Go Back To The Beginning And Repeat The Process 
 This is a cyclical approach. This means you should repeat these steps, or variations thereof, as many times as necessary throughout the project. It’s natural that, over time and with process optimization, some of these steps will cease to make sense. That’s absolutely not a problem. But the most important thing to realize here is that accessibility and this process of testing font size increases shouldn’t be done just once, and that’s it. It’s a test to be done many, many times throughout the day-to-day work of each project and team. 
 The Role Of Design Systems At first glance, this list of steps might seem like a complex exercise. But it’s not. This is because the vast majority, if not all, of these steps are easy to execute in any context where a design system exists. In fact, design systems have become an unavoidable standard in the Product Design industry. We can discuss what each team calls a design system, but the truth is that it’s very difficult today to find a Product Design team that doesn’t have, at the very least, a minimally structured library of components and styles. 
 With this foundation, whether more or less documented, it’s very easy to apply this type of font size increase test using Figma variables. Furthermore, if your design system already has, for example, structured variables for light and dark mode, it means you’re already applying the exact same principles we used to perform this test. So, nothing new. 
 Working with design systems involves a level of structuring and organization that is also very useful for creating this type of test. There’s a myth that design systems limit creativity. This is not true. Design systems help solve the “bureaucratic” part of design, so we can actually have more time for what matters: in this case, testing accessibility and building more and more products and services that are truly accessible to the greatest number of people. 
 Example File It’s always easier to see an example than just read a description of a process. If this is true in many disciplines of knowledge, in design, this premise makes even more sense. Therefore, in this Figma file , freely published and openly available to the community, you’ll find a practical example of the entire testing process described here. Remember that this is just an example. There may be countless ways to perform this type of test within the context of a Figma file. 
 Be sure to look at this approach with a critical eye. It’s a suggestion for testing font size increases that follows a specific process. Despite this, the approach should be adapted to your team’s specific reality, processes, and level of maturity. Simply copying formulas from other teams without understanding if they make sense in our own context is a sure way to make accessibility efforts disproportionate. Every situation is unique. This approach attempts to simplify accessibility work as much as possible in this specific context. And remember: if something happens, however small, it’s a step forward, not a step backward. And that should be celebrated by everyone on the team.
```

---

## 14. Modal vs. Separate Page: UX Decision Tree

- 日期: 2026-03-19 15:00
- 链接: https://smashingmagazine.com/2026/03/modal-separate-page-ux-decision-tree/

```
You probably have been there before. How do we choose between showing a modal to users, and when do we navigate them to a separate, new page? And does it matter at all? 
 Actually, it does. The decision influences users’ flow, their context, their ability to look up details, and with it error frequency and task completion . Both options can be disruptive and frustrating — at the wrong time, and at the wrong place. 
 So we’d better get it right. Well, let’s see how to do just that. 
 Modals vs. Dialogs vs. Overlays vs. Lightboxes While we often speak about a single modal UI component, we often ignore fine, intricate nuances between all the different types of modals. In fact, not every modal is the same . Modals, dialogs, overlays, and lightboxes — all sound similar, but they are actually quite different: 
 Dialog 
 A generic term for “conversation” (user ↔ system). 
 Overlay 
 A small content panel displayed on top of a page. 
 Modal 
 User must interact with overlay + background disabled . 
 Nonmodal 
 User must interact with overlay + background enabled . 
 Lightbox 
 Dimmed background to focus attention on the modal. 
 As Anna Kaley highlights , most overlays appear at the wrong time, interrupt users during critical tasks, use poor language, and break users’ flow. They are interruptive by nature , and typically with a high level of severity without a strong need for that. 
 Surely users must be slowed down and interrupted if the consequences of their action have a high impact, but for most scenarios non-modals are much more subtle and a more friendly option to bring something to the user’s attention. If anything, I always suggest it to be a default . 
 Modals → For Single, Self-Contained Tasks As designers, we often dismiss modals as irrelevant and annoying — and often they are! — yet they have their value as well. They can be very helpful to warn users about potential mistakes or help them avoid data loss. They can also help perform related actions or drill down into details without interrupting the current state of the page. 
 But the biggest advantage of modals is that they help users keep the context of the current screen. It doesn’t mean just the UI, but also edited input, scrolling position, state of accordions, selection of filters, sorting, and so on. 
 At times, users need to confirm a selection quickly (e.g., filters as shown above) and then proceed immediately from there. Auto-save can achieve the same, of course, but it’s not always needed or desired. And blocking the UI is often not a good idea. 
 However, modals aren’t used for any tasks. Typically, we use them for single, self-contained tasks where users should jump in, complete a task, and then return to where they were. Unsurprisingly, they do work well for high-priority, short interactions (e.g., alerts, destructive actions, quick confirmations). 
 When modals help : 
 🚫 Modals are often disruptive, invasive, and confusing. 
 🚫 They make it difficult to compare and copy-paste. 
 ✅ Yet modals allow users to maintain multiple contexts. 
 ✅ Useful to prevent irreversible errors and data loss. 
 ✅ Useful if sending users to a new page would be disruptive. 
 ✅ Show a modal only if users will value the disruption. 
 ✅ By default, prefer non-blocking dialogs (“nonmodals”). 
 ✅ Allow users to minimize, hide, or restore the dialog later. 
 ✅ Use a modal to slow users down, e.g., verify complex input. 
 ✅ Give a way out with “Close”, ESC key, or click outside the box. 
 Pages → For Complex, Multi-Step Workflows Wizards or tabbed navigation within modals doesn’t work too well, even in complex enterprise products — there, side panels or drawers typically work better. Troubles start when users need to compare or reference data points — yet modals block this behavior, so they re-open the same page in multiple tabs instead. 
 For more complex flows and multi-step processes, standalone pages work best . Pages also work better when they demand the user’s full attention, and reference to the previous screen isn’t very helpful. And drawers work for sub-tasks that are too complex for a simple modal, but don't need a full page navigation. 
 When to avoid modals : 
 🚫 Avoid modals for error messages . 
 🚫 Avoid modals for feature notifications . 
 🚫 Avoid modals for onboarding experience . 
 🚫 Avoid modals for complex, lengthy multi-step-tasks . 
 🚫 Avoid multiple nested modals and use prev/next instead. 
 🚫 Avoid auto-triggered modals unless absolutely necessary. 
 Avoid Both For Repeated Tasks In many complex, task-heavy products, users will find themselves performing the same tasks repeatedly, over and over again. There, both modals and new page navigations add friction because they interrupt the flow or force users to gather missing data between all the different tabs or views. 
 Too often, users end up with a broken experience, full of never-ending confirmations, exaggerated warnings, verbose instructions, or just missing reference points. As Saulius Stebulis mentioned , in these scenarios, expandable sections or in-place editing often work better — they keep the task anchored to the current screen. 
 In practice, in many scenarios, users don’t complete their tasks in isolation. They need to look up data, copy-paste values, refine entries in different places, or just review similar records as they work through their tasks. 
 Overlays and drawers are more helpful in maintaining access to background data during the task. As a result, the context always stays in its place, available for reference or copy-paste. Save modals and page navigation for moments where the interruption genuinely adds value — especially to prevent critical mistakes. 
 Modals vs. Pages: A Decision Tree A while back, Ryan Neufeld put together a very helpful guide to help designers choose between modals and pages . It comes with a handy PNG cheatsheet and a Google Doc template with questions broken down across 7 sections. 
 It’s lengthy, extremely thorough, but very easy to follow: 
 It might look daunting, but it's a quite simple 4-step process : 
 Context of the screen . 
 First, we check if users need to maintain the context of the underlying screen. 
 Task complexity and duration . 
 Simpler, focused, non-distracting tasks could use a modal, but long, complex flows need a page. 
 Reference to underlying page . 
 Then, we check if users often need to refer to data in the background or if the task is a simple confirmation or selection. 
 Choosing the right overlay . 
 Finally, if an overlay is indeed a good option, it guides us to choose between modal or nonmodal (leaning towards a nonmodal). 
 Wrapping Up Whenever possible, avoid blocking the entire UI. Have a dialog floating, partially covering the UI, but allowing navigation, scrolling, and copy-pasting. Or show the contents of the modal as a side drawer. Or use a vertical accordion instead. Or bring users to a separate page if you need to show a lot of detail. 
 But if you want to boost users’ efficiency and speed, avoid modals at all costs . Use them to slow users down, to bundle their attention, to prevent mistakes. As Therese Fessenden noted , no one likes to be interrupted, but if you must, make sure it’s absolutely worth the cost. 
 Meet “Smart Interface Design Patterns” You can find a whole section about modals and alternatives in Smart Interface Design Patterns , our 15h-video course with 100s of practical examples from real-life projects — with a live UX training later this year. Everything from mega-dropdowns to complex enterprise tables — with 5 new segments added every year. Jump to a free preview . Use code BIRDIE to save 15% off. 
 Meet Smart Interface Design Patterns , our video course on interface design & UX. Video + UX Training 
 Video only 
 Video + UX Training 
 $ 579.00 $ 699.00 Get Video + UX Training 
 25 video lessons (15h) + Live UX Training . 
 100 days money-back-guarantee. 
 Video only 
 $ 275.00$ 350.00 
 Get the video course 
 40 video lessons (15h). Updated yearly. 
 Also available as a UX Bundle with 2 video courses. 
 Useful Resources Different Types of Popups , by Anna Kaley 
 Best Practices for Designing UI Modals , by Uxcel 
 We Use Too Many Damn Modals: UX Guidelines , by Adrian Egger 
 Modal & Nonmodal Dialogs , by Therese Fessenden 
 Modern Enterprise UI Design: Modal Dialogs , by James Jacobs 
 Modals in Design Systems
```

---

## 15. Anime vs. Marvel/DC: Designing Digital Products With Emotion In Flow

- 日期: 2026-03-17 10:00
- 链接: https://smashingmagazine.com/2026/03/anime-marvel-dc-designing-digital-products-emotion-flow/

```
Design isn’t only pixels and patterns. It’s pacing and feelings, too. Some products feel cinematic as they guide us through uncertainty, relief, confidence, and calm without yanking us around. That’s Emotion in Flow . Others undercut their own moments with a joke in the wrong place, a surprise pop-up, or a jumpy transition. That’s Emotion in Conflict . 
 These aren’t UX-only ideas. You can see them everywhere in entertainment. And the clearest way to feel the difference is to compare how anime handles emotional shifts versus how Marvel and DC films stumble. We’ll use two specific examples, one from Dan da Dan (anime series on Netflix) and one from James Gunn’s Superman movie, to define the two concepts, and then translate them into practical product design patterns you can apply right away. 
 Note : We’ll focus on digital products , including apps, SaaS, and web. 
 Emotion In Flow (Anime: Dan da Dan) In Dan da Dan , the tonal range is wild, horror, comedy, tenderness, yet it flows . 
 Example: In one arc, the protagonists are on a bizarre, comedic quest involving the “golden genitals” of one of the main characters (yes, really), and in another, we’re drawn into a heartbreaking story of a mother whose child is kidnapped. On paper, that shift should be a car crash. On screen, it’s coherent and emotionally legible. 
 Why does this work on screen? 
 Continuity of stakes. 
 Even when a gag lands, the characters’ goals and danger stay intact. Humor releases tension after a mini‑resolution; it doesn’t deny the threat. 
 Clear mood cues. 
 Music, framing, pacing, and character reactions telegraph the next feeling. You’re primed for the shift, so you ride it rather than getting yanked. 
 One emotional anchor. 
 Relationships remain the North Star, so the scene’s heart doesn’t get lost when the tone moves. 
 How does this translate to UX? 
 Good products do the same: prepare , transition , resolve , so users stay immersed as the emotional tone shifts. 
 Emotion In Conflict (Marvel/DC: James Gunn’s Superman) Lois & Clark are having a heartfelt, intimate conversation, a slow, human moment, while in the background a running gag plays out (a monster getting clobbered with a giant baseball bat). The gag steals the focus right when the scene asks you to feel something real. The result is a tonal clash that punctures the emotion instead of releasing it. 
 Why does this fail on screen? 
 Increased cognitive load. 
 What’s happening here maps directly to cognitive load theory. When a scene (or interface) asks users to process two competing emotional signals at once, it introduces extraneous cognitive load , mental effort that has nothing to do with the task or moment itself. Instead of focusing on the emotional beat, attention is split between signals that don’t resolve each other. In products, this is what happens when humor, promotions, or unexpected UI changes intrude on high-stakes moments: users are forced to interpret tone and intent at the same time they’re trying to act, which slows comprehension and increases stress. 
 Competing beats at the same time. 
 The joke overlaps the climax of a serious beat; the audience pays attention to the switch rather than the feeling. 
 No tonal handoff. 
 There’s no transition that lands the intimacy before humor arrives, so the moment feels undercut rather than resolved. 
 How does this translate to UX? 
 In products, this is the confetti-before-confirmation problem, the cheeky error in a money flow, or the promo modal that appears right in the middle of a critical task. This also spikes cognitive load: users must process the humor while trying to fix a problem, which slows them down and increases stress. 
 Quick Definitions Emotion in Flow 
 Emotional shifts feel earned, telegraphed, and timed so they resolve prior beats. Immersion holds. 
 Emotion in Conflict 
 A jarring switch (or hard cut) that punctures a live emotional beat. Immersion breaks. 
 Now that we’ve named it: how does this connect to UX? 
 How Emotions Shape Product Memorability People don’t remember the average of an experience; they remember peaks and the ending. If your flow’s peak is frustration, or your ending is messy, that’s what sticks. So design the emotional curve on purpose. 
 Emotions live across three layers (from Don Norman’s Emotional Design ), and your product needs to line them up: 
 Visceral (gut): First-impression signals: visuals, motion, haptics, sound. 
 Examples: A steady skeleton loader calms more than a jittery spinner; a gentle success chime/haptic tap lets the win land without shouting; consistent easing/direction tells the eye what changed. 
 Behavioral (doing): Can I complete my task smoothly? Friction here means stress. 
 Examples: Three clear payment steps with predictable progress; error states that explain what happened and how to recover; inline validation instead of end-of-form explosions. 
 Reflective (meaning): The story I tell myself after, “Was that worth it? Do I trust this?” 
 Examples: A tidy wrap-up screen (“Done. You’ll get X by Friday.”) gives closure; a small recap (“You saved €18 this year”) creates pride without fireworks. 
 Microinteractions are the emotional glue. Each one has a trigger (I tap Pay), rules (what the system does), feedback (progress and a clear result), and loops or modes (what happens if the user tries again). Get these right, and your transitions bridge feelings. Get them wrong, and they break the flow. 
 The emotional beat sheet maps cleanly onto Norman’s layers of experience: 
 Uncertainty lives in the visceral and early behavioral layers, where users rely on sensory cues (motion, clarity, feedback) to understand what’s happening. 
 Clarity is firmly in the behavioral layer, the moment when the system’s intent and the user’s next action lock into place. 
 Anticipation is a blend of behavioral (the user is doing something with purpose) and reflective (the user is already predicting the outcome and imagining what comes next). 
 Achievement is a reflective peak , where the user evaluates success, trust, and whether the experience “felt right.” 
 Calm/Closure is primarily reflective , helping users wrap up the meaning of the interaction and decide if the product is trustworthy and worth returning to. 
 In real products, this sequence doesn’t disappear when things go wrong. Errors, latency, and degraded states are not exceptions to the emotional arc — they are part of it. Seen through a narrative lens, these moments are the obstacles in the hero’s journey. A well-designed recovery state acknowledges the setback, clarifies what happened, and guides the next step without introducing new emotional noise. When failure is treated as a beat instead of a rupture, emotional flow can be preserved even under stress. 
 UX Examples: Emotion In Flow vs. Emotion In Conflict Emotion In Flow 
 Checkout done right (Stripe/Apple Pay style): short steps, clear progress, and a crisp success state (a checkmark with an optional soft haptic). The peak (success) lands, and the end gives closure (receipt or next step). 
 Pickup status (ride‑hailing apps, e.g., Uber, Free Now, or Bolt): progressive updates maintain orientation and reduce anxiety (“Driver arriving”, “2 min away”, “Arrived”). Uncertainty turns into clarity, with gentle motion preparing each transition. 
 Emotion In Conflict 
 Note : We’re not naming specific products here — we respect the work behind them. Instead, we’re showing the patterns that cause emotional conflict and exactly how to fix them. 
 Jokes in serious moments. 
 Cheeky copy-in-error states for money/health/security. Users are stressed; humor amplifies irritation. 
 Celebration before resolution. 
 Confetti, fireworks, or loud sounds before confirmation. The party interrupts the climax. 
 Hard state jumps. 
 Surprise modals/promos mid‑task, full‑screen takeovers without preparation. Feels like an abrupt cut during an emotional beat. 
 What You Can Do To Ensure Emotion in Flow Here’s a Notion page with the full template you can duplicate: 
 Emotional beat sheet template . 
 1. Write The Emotional Beat Sheet First 
 For each core flow (onboarding, payment, recovery), map the feelings per step: uncertainty → clarity → anticipation → achievement → calm. Attach copy, motion, and microinteractions to each beat. (Who carries the emotion where?) 
 2. Align Tone With Task Risk 
 Create a tone matrix (risk level × state). In high‑risk errors, be calm, plain, and solution‑oriented. Save playfulness for low‑risk contexts. 
 Template snippets: 
 High‑risk error : “We couldn’t verify your ID. Try again or contact support.” 
 Low‑risk empty state : “Nothing here yet. Want to start with a sample?” 
 This is where many mature products quietly drift into emotional conflict. Over time, teams add delight by habit rather than intent. 
 A useful self-check is to ask: If we removed every playful or celebratory element from this step, would the flow still feel humane — or were those elements masking friction? 
 Good emotional design clarifies experience; great emotional design doesn’t need decoration to compensate for confusion. 
 3. Design Peak And End On Purpose 
 Engineer one clear peak (the moment of success) and one clean end (confirmation and what happens next). Measure recall and satisfaction at both points. 
 4. Use Microinteractions As Bridges, Not Spotlights 
 Prepare: Small, consistent motion hints before a big state change. 
 Confirm: Success gets a subtle settle, with a slightly slower ease-out and an optional light haptic. 
 Recover: Repeated failure gracefully shifts tone from upbeat to supportive and guides the next step. 
 5. Test For Emotional Continuity 
 In usability sessions, don’t just ask “Was that easy?” Instead, you can ask “What feeling changed here?” If you hear “confused → amused → confused,” you’ve got conflict, not flow. Iterate transitions, not just screens. 
 How To Avoid Emotion in Conflict: Fast Checklist Red flags → fixes: 
 Jokes in serious moments → swap for calm, direct language, and a clear recovery path. 
 Celebration before resolution → move celebration to after confirmation; tone it down for high‑risk tasks. 
 Hard state jumps → pre‑announce transitions; keep framing consistent; use meaningful motion to preserve continuity. 
 Cross‑team tone drift → centralize voice & tone guidelines with examples per risk level and state. 
 There are moments when breaking emotional flow is intentional and necessary. Security warnings, legal confirmations, and safety-critical alerts often benefit from abrupt tonal shifts. In these cases, disruption signals importance and demands attention. The problem isn’t emotional conflict itself; it’s accidental conflict . When designers choose disruption deliberately, users understand the stakes instead of feeling whiplash. 
 Conclusion Great experiences are directed experiences. Dan da Dan shows how to move through feelings without losing us: it prepares, transitions, and resolves. The Superman scene shows the opposite: a gag colliding with a heartfelt beat. 
 Do the former. Map your emotional beats, align tone to task risk, and let microinteractions bridge feelings so users remember the right peak and the right end, not the whiplash in the middle.
```

---

## 16. Moving From Moment.js To The JS Temporal API

- 日期: 2026-03-13 13:00
- 链接: https://smashingmagazine.com/2026/03/moving-from-moment-to-temporal-api/

```
Almost any kind of application written in JavaScript works with times or dates in some capacity. In the beginning, this was limited to the built-in Date API. This API includes basic functionality, but is quite limited in what it can do. 
 Third-party libraries like Moment.js, and later built-in APIs such as the Intl APIs and the new Temporal API , add much greater flexibility to working with times and dates. 
 The Rise And Fall Of Moment.js Moment.js is a JavaScript library with powerful utilities for working with times and dates. It includes missing features from the basic Date API , such as time zone manipulation, and makes many common operations simpler. Moment also includes functions for formatting dates and times. It became a widely used library in many different applications. 
 However, Moment also had its share of issues. It’s a large library, and can add significantly to an application’s bundle size. Because the library doesn’t support tree shaking (a feature of modern bundlers that can remove unused parts of libraries), the entire Moment library is included even if you only use one or two of its functions. 
 Another issue with Moment is the fact that the objects it creates are mutable . Calling certain functions on a Moment object has side effects and mutates the value of that object. This can lead to unexpected behavior or bugs. 
 In 2020, the maintainers of Moment decided to put the library into maintenance mode. No new feature development is being done, and the maintainers recommend against using it for new projects. 
 There are other JavaScript date libraries, such as date-fns , but there’s a new player in town, an API built directly into JavaScript: Temporal . It’s a new standard that fills in the holes of the original Date API as well as solves some of the limitations found in Moment and other libraries. 
 What Is Temporal? Temporal is a new time and date API being added to the ECMAScript standard, which defines modern JavaScript. As of March 2026, it has reached Stage 4 of the TC39 process (the committee that oversees proposals and additions to the JavaScript language), and will be included in the next version of the ECMAScript specification. It has already been implemented in several browsers: Chrome 144+ and Firefox 139+ , with Safari expected to follow soon . A polyfill is also available for unsupported browsers and Node.js. 
 The Temporal API creates objects that, generally, represent moments in time. These can be full-time and date stamps in a given time zone, or they can be a generic instance of “wall clock” time without any time zone or date information. Some of the main features of Temporal include: 
 Times with or without dates. 
 A Temporal object can represent a specific time on a specific date, or a time without any date information. A specific date, without a time, can also be represented. 
 Time zone support. 
 Temporal objects are fully time zone aware and can be converted across different time zones. Moment supports time zones, too, but it requires the additional moment-timezone library. 
 Immutability. 
 Once a Temporal object is created, it cannot be changed. Time arithmetic or time zone conversions do not modify the underlying object. Instead, they generate a new Temporal object. 
 1-based indexing. 
 A common source of bugs with the Date API (as well as with Moment) is that months are zero-indexed. This means that January is month 0 , rather than month 1 as we all understand in real life. Temporal fixes this by using 1-based indexing — January is month 1 . 
 It’s built into the browser. 
 Since Temporal is an API in the browser itself, it adds nothing to your application’s bundle size. 
 It’s also important to note that the Date API isn’t going away. While Temporal supersedes this API, it is not being removed or deprecated. Many applications would break if browsers suddenly removed the Date API. However, also keep in mind that Moment is now considered a legacy project in maintenance mode. 
 In the rest of the article, we’ll look at some “recipes” for migrating Moment-based code to the new Temporal API. Let’s start refactoring! 
 Creating Date And Time Objects Before we can manipulate dates and times, we have to create objects representing them. To create a Moment object representing the current date and time, use the moment function. 
 const now = moment();
console.log(now); 
// Moment<2026-02-18T21:26:29-05:00> This object can now be formatted or manipulated as needed. 
 // convert to UTC
// warning: This mutates the Moment object and puts it in UTC mode!
console.log(now.utc()); 
// Moment<2026-02-19T02:26:29Z>

// print a formatted string - note that it's using the UTC time now
console.log(now.format('MM/DD/YYYY hh:mm:ss a')); 
// 02/19/2026 02:27:07 am 
 The key thing to remember about Moment is that a Moment object always includes information about the time and the date. If you only need to work with time information, this is usually fine, but it can cause unexpected behavior in situations like Daylight Saving Time or leap years, where the date can have an effect on time calculations. 
 Temporal is more flexible. You can create an object representing the current date and time by creating a Temporal.Instant object. This represents a point in time defined by the time since “the epoch” (midnight UTC on January 1, 1970). Temporal can reference this instant in time with nanosecond-level precision. 
 const now = Temporal.Now.instant();

// see raw nanoseconds since the epoch
console.log(now.epochNanoseconds);
// 1771466342612000000n

// format for UTC
console.log(now.toString());
// 2026-02-19T01:55:27.844Z

// format for a particular time zone
console.log(now.toString({ timeZone: 'America/New_York' }));
// 2026-02-18T20:56:57.905-05:00 Temporal.Instant objects can also be created for a specific time and date by using the from static method. 
 const myInstant = Temporal.Instant.from('2026-02-18T21:10:00-05:00');

// Format the instant in the local time zone. Note that this only controls
// the formatting - it does not mutate the object like moment.utc does.
console.log(myInstant.toString({ timeZone: 'America/New_York' }));
// 2026-02-18T21:10:00-05:00 
 You can also create other types of Temporal objects, including: 
 Temporal.PlainDate : A date with no time information. 
 Temporal.PlainTime : A time with no date information. 
 Temporal.ZonedDateTime : A date and time in a specific time zone. 
 Each of these has a from method that can be called with an object specifying the date and/or time, or a date string to parse. 
 // Just a date
const today = Temporal.PlainDate.from({
 year: 2026,
 month: 2, // note we're using 2 for February
 day: 18
});
console.log(today.toString());
// 2026-02-18

// Just a time
const lunchTime = Temporal.PlainTime.from({
 hour: 12
});
console.log(lunchTime.toString());
// 12:00:00 

// A date and time in the US Eastern time zone
const dueAt = Temporal.ZonedDateTime.from({
 timeZone: 'America/New_York',
 year: 2026,
 month: 3,
 day: 1,
 hour: 12,
 minute: 0,
 second: 0
});
console.log(dueAt.toString());
// 2026-03-01T12:00:00-05:00[America/New_York] Parsing We’ve covered programmatic creation of date and time information. Now let’s look at parsing. Parsing is one area where Moment is more flexible than the built-in Temporal API. 
 You can parse a date string by passing it to the moment function. With a single argument, Moment expects an ISO date string, but you can use alternative formats if you provide a second argument specifying the date format being used. 
 const isoDate = moment('2026-02-21T09:00:00');
const formattedDate = moment('2/21/26 9:00:00', 'M/D/YY h:mm:ss');

console.log(isoDate);
// Moment<2026-02-21T09:00:00-05:00>

console.log(formattedDate);
// Moment<2026-02-21T09:00:00-05:00> 
 In older versions, Moment would make a best guess to parse any arbitrarily formatted date string. This could lead to unpredictable results. For example, is 02-03-2026 February 2 or March 3? For this reason, newer versions of Moment display a prominent deprecation warning if it’s called without an ISO formatted date string (unless the second argument with the desired format is also given). 
 Temporal will only parse a specifically formatted date string. The string must be compliant with the ISO 8601 format or its extension, RFC 9557. If a non-compliant date string is passed to a from method, Temporal will throw a RangeError . 
 // Using an RFC 9557 date string
const myDate = Temporal.Instant.from('2026-02-21T09:00:00-05:00[America/New_York]');
console.log(myDate.toString({ timeZone: 'America/New_York' }));
// 2026-02-21T09:00:00-05:00

// Using an unknown date string
const otherDate = Temporal.Instant.from('2/21/26 9:00:00');
// RangeError: Temporal error: Invalid character while parsing year value. 
 The exact requirements of the date string depend on which kind of Temporal object you’re creating. In the above example, Temporal.Instant requires a full ISO 8601 or RFC 9557 date string specifying the date and time with a time zone offset, but you can also create PlainDate or PlainTime objects using just a subset of the date format. 
 const myDate = Temporal.PlainDate.from('2026-02-21');
console.log(myDate.toString());
// 2026-02-21

const myTime = Temporal.PlainTime.from('09:00:00');
console.log(myTime.toString());
// 09:00:00 Note that these strings must still comply with the expected format, or an error will be thrown. 
 // Using a non-compliant time strings. These will all throw a RangeError.
Temporal.PlainTime.from('9:00');
Temporal.PlainTime.from('9:00:00 AM'); 
 Pro tip: Handling non-ISO strings 
 Because Temporal prioritizes reliability, it won’t try to guess the format of a string like 02-01-2026 . If your data source uses such strings, you will need to do some string manipulation to rearrange the values into an ISO string like 2026-02-01 before attempting to use it with Temporal. 
 Formatting Once you have a Moment or Temporal object, you’ll probably want to convert it to a formatted string at some point. 
 This is an instance where Moment is a bit more terse. You call the object’s format method with a string of tokens that describe the desired date format. 
 const date = moment();

console.log(date.format('MM/DD/YYYY'));
// 02/22/2026

console.log(date.format('MMMM Do YYYY, h:mm:ss a'));
// February 22nd 2026, 8:18:30 pm On the other hand, Temporal requires you to be a bit more verbose. Temporal objects, such as Instant , have a toLocaleString method that accepts various formatting options specified as properties of an object. 
 const date = Temporal.Now.instant();

// with no arguments, we'll get the default format for the current locale
console.log(date.toLocaleString());
// 2/22/2026, 8:23:36 PM (assuming a locale of en-US)

// pass formatting options to generate a custom format string
console.log(date.toLocaleString('en-US', {
 month: 'long',
 day: 'numeric',
 year: 'numeric',
 hour: '2-digit',
 minute: '2-digit'
}));
// February 22, 2026 at 8:23 PM

// only pass the fields you want in the format string
console.log(date.toLocaleString('en-US', {
 month: 'short',
 day: 'numeric'
}));
// Feb 22 
 Temporal date formatting actually uses the Intl.DateTimeFormat API (which is already readily available in modern browsers) under the hood. That means you can create a reusable DateTimeFormat object with your custom formatting options, then pass Temporal objects to its format method. Because of this, it doesn’t support custom date formats like Moment does. If you need something like 'Q1 2026' or other specialized formatting, you may need some custom date formatting code or reach for a third-party library. 
 const formatter = new Intl.DateTimeFormat('en-US', {
 month: '2-digit',
 day: '2-digit',
 year: 'numeric'
});

const date = Temporal.Now.instant();
console.log(formatter.format(date));
// 02/22/2026 Moment’s formatting tokens are simpler to write, but they aren’t locale-friendly. The format strings “hard code” things like month/day order. The advantage of using a configuration object, as Temporal does, is that it will automatically adapt to any given locale and use the correct format. 
 const date = Temporal.Now.instant();

const formatOptions = {
 month: 'numeric',
 day: 'numeric',
 year: 'numeric'
};

console.log(date.toLocaleString('en-US', formatOptions));
// 2/22/2026

console.log(date.toLocaleString('en-GB', formatOptions));
// 22/02/2026 Date calculations In many applications, you’ll need to end up performing some calculations on a date. You may want to add or subtract units of time (days, hours, seconds, etc.). For example, if you have the current date, you may want to show the user the date 1 week from now. 
 Moment objects have methods such as add and subtract that perform these operations. These functions take a value and a unit, for example: add(7, 'days') . One very important difference between Moment and Temporal, however, is that when performing these date calculations, the underlying object is modified and its original value is lost. 
 const now = moment();

console.log(now);
// Moment<2026-02-24T20:08:36-05:00>

const nextWeek = now.add(7, 'days');
console.log(nextWeek);
// Moment<2026-03-03T20:08:36-05:00>

// Gotcha - the original object was mutated
console.log(now);
// Moment<2026-03-03T20:08:36-05:00> To avoid losing the original date, you can call clone on the Moment object to create a copy. 
 const now = moment();
const nextWeek = now.clone().add(7, 'days');

console.log(now);
// Moment<2026-02-24T20:12:55-05:00>

console.log(nextWeek);
// Moment<2026-03-03T20:12:55-05:00> On the other hand, Temporal objects are immutable . Once you’ve created an object like an Instant , PlainDate , and so on, the value of that object will never change. Temporal objects also have add and subtract methods. 
 Temporal is a little picky about which time units can be added to which object types. For example, you can’t add days to an Instant : 
 const now = Temporal.Now.instant();
const nextWeek = now.add({ days: 7 });
// RangeError: Temporal error: Largest unit cannot be a date unit 
 This is because Instant objects represent a specific point in time in UTC and are calendar-agnostic. Because the length of a day can change based on time zone rules such as Daylight Saving Time, this calculation isn’t available on an Instant . You can , however, perform this operation on other types of objects, such as a PlainDateTime : 
 const now = Temporal.Now.plainDateTimeISO();
console.log(now.toLocaleString());
// 2/24/2026, 8:23:59 PM

const nextWeek = now.add({ days: 7 });

// Note that the original PlainDateTime remains unchanged
console.log(now.toLocaleString());
// 2/24/2026, 8:23:59 PM

console.log(nextWeek.toLocaleString());
// 3/3/2026, 8:23:59 PM You can also calculate how much time is between two Moment or Temporal objects. 
 With Moment’s diff function, you need to provide a unit for granularity, otherwise it will return the difference in milliseconds. 
 const date1 = moment('2026-02-21T09:00:00');
const date2 = moment('2026-02-22T10:30:00');

console.log(date2.diff(date1));
// 91800000

console.log(date2.diff(date1, 'days'));
// 1 To do this with a Temporal object, you can pass another Temporal object to its until or since methods. This returns a Temporal.Duration object containing information about the time difference. The Duration object has properties for each component of the difference, and also can generate an ISO 8601 duration string representing the time difference. 
 const date1 = Temporal.PlainDateTime.from('2026-02-21T09:00:00');
const date2 = Temporal.PlainDateTime.from('2026-02-22T10:30:00');

// largestUnit specifies the largest unit of time to represent
// in the duration calculation
const diff = date2.since(date1, { largestUnit: 'day' });

console.log(diff.days);
// 1

console.log(diff.hours);
// 1

console.log(diff.minutes);
// 30

console.log(diff.toString());
// P1DT1H30M
// (ISO 8601 duration string: 1 day, 1 hour, 30 minutes) 
 Comparing Dates And Times Moment and Temporal both let you compare dates and times to determine which comes before the other, but take different approaches with the API. 
 Moment provides methods such as isBefore , isAfter , and isSame to compare two Moment objects. 
 const date1 = moment('2026-02-21T09:00:00');
const date2 = moment('2026-02-22T10:30:00');

console.log(date1.isBefore(date2));
// true Temporal uses a static compare method to perform a comparison between two objects of the same type. It returns -1 if the first date comes before the second, 0 if they are equal, or 1 if the first date comes after the second. The following example shows how to compare two PlainDate objects. Both arguments to Temporal.PlainDate.compare must be PlainDate objects. 
 const date1 = Temporal.PlainDate.from({ year: 2026, month: 2, day: 24 });
const date2 = Temporal.PlainDate.from({ year: 2026, month: 3, day: 24 });

// date1 comes before date2, so -1
console.log(Temporal.PlainDate.compare(date1, date2));

// Error if we try to compare two objects of different types
console.log(Temporal.PlainDate.compare(date1, Temporal.Now.instant()));
// TypeError: Temporal error: Invalid PlainDate fields provided. 
 In particular, this makes it easy to sort an array of Temporal objects chronologically. 
 // An array of Temporal.PlainDate objects
const dates = [ ... ];

// use Temporal.PlainDate.compare as the comparator function
dates.sort(Temporal.PlainDate.compare); Time Zone Conversions The core Moment library doesn’t support time zone conversions. If you need this functionality, you also need to install the moment-timezone package. This package is not tree-shakable, and therefore can add significantly to your bundle size. Once you’ve installed moment-timezone , you can convert Moment objects to different time zones with the tz method. As with other Moment operations, this mutates the underlying object. 
 // Assuming US Eastern time
const now = moment();
console.log(now);
// Moment<2026-02-28T20:08:20-05:00>

// Convert to Pacific time.
// The original Eastern time is lost.
now.tz('America/Los_Angeles');
console.log(now);
// Moment<2026-02-28T17:08:20-08:00> Time zone functionality is built into the Temporal API when using a Temporal.ZonedDateTime object. These objects include a withTimeZone method that returns a new ZonedDateTime representing the same moment in time, but in the specified time zone. 
 // Again, assuming US Eastern time
const now = Temporal.Now.zonedDateTimeISO();
console.log(now.toLocaleString());
// 2/28/2026, 8:12:02 PM EST

// Convert to Pacific time
const nowPacific = now.withTimeZone('America/Los_Angeles');
console.log(nowPacific.toLocaleString());
// 2/28/2026, 5:12:02 PM PST

// Original object remains unchanged
console.log(now.toLocaleString());
// 2/28/2026, 8:12:02 PM EST Note: The formatted values returned by toLocaleString are, as the name implies, locale-dependent. The sample code was developed in the en-US locale, so the format is like this: 2/28/2026, 5:12:02 PM PST . In another locale, this may be different. For example, in the en-GB locale, you would get something like 28/2/2026, 17:12:02 GMT-8 . 
 A Real-world Refactoring Suppose we’re building an app for scheduling events across time zones. Part of this app is a function, getEventTimes , which takes an ISO 8601 string representing the time and date of the event, a local time zone, and a target time zone. The function creates formatted time and date strings for the event in both time zones. 
 If the function is given an input string that’s not a valid time/date string, it will throw an error. 
 Here’s the original implementation, using Moment (also requiring use of the moment-timezone package). 
 import moment from 'moment-timezone';

function getEventTimes(inputString, userTimeZone, targetTimeZone) {
 const timeFormat = 'MMM D, YYYY, h:mm:ss a z';

 // 1. Create the initial moment in the user's time zone
 const eventTime = moment.tz(
 inputString,
 moment.ISO_8601, // Expect an ISO 8601 string
 true, // Strict parsing
 userTimeZone
 );

 // Throw an error if the inputString did not represent a valid date
 if (!eventTime.isValid()) {
 throw new Error('Invalid date/time input');
 }

 // 2. Calculate the target time
 // CRITICAL: We must clone, or 'eventTime' changes forever!
 const targetTime = eventTime.clone().tz(targetTimeZone);

 return {
 local: eventTime.format(timeFormat),
 target: targetTime.format(timeFormat),
 };
}

const schedule = getEventTimes(
 '2026-03-05T15:00-05:00',
 'America/New_York',
 'Europe/London',
);

console.log(schedule.local);
// Mar 5, 2026, 3:00:00 pm EST

console.log(schedule.target); 
// Mar 5, 2026, 8:00:00 pm GMT 
 In this example, we’re using an expected date format of ISO 8601, which is helpfully built into Moment. We’re also using strict parsing, which means Moment won’t try to guess with a date string that doesn’t match the format. If a non-ISO date string is passed, it will result in an invalid date object, and we throw an error. 
 The Temporal implementation looks similar, but has a few key differences. 
 function getEventTimes(inputString, userTimeZone, targetTimeZone) {
 // 1. Parse the input directly into an Instant, then create
 // a ZonedDateTime in the user's zone.
 const instant = Temporal.Instant.from(inputString);
 const eventTime = instant.toZonedDateTimeISO(userTimeZone);

 // 2. Convert to the target zone
 // This automatically returns a NEW object; 'eventTime' is safe.
 const targetTime = eventTime.withTimeZone(targetTimeZone);

 // 3. Format using Intl (built-in)
 const options = {
 year: 'numeric',
 month: 'short',
 day: 'numeric',
 hour: 'numeric',
 minute: '2-digit',
 second: '2-digit',
 timeZoneName: 'short'
 };

 return {
 local: eventTime.toLocaleString(navigator.language, options),
 target: targetTime.toLocaleString(navigator.language, options)
 };
}

const schedule = getEventTimes(
 '2026-03-05T15:00-05:00',
 'America/New_York',
 'Europe/London',
);

console.log(schedule.local);
// Mar 5, 2026, 3:00:00 PM EST

console.log(schedule.target);
// Mar 5, 2026, 8:00:00 PM GMT 
 With Moment, we have to explicitly specify a format string for the resulting date strings. Regardless of the user’s location or locale, the event times will always be formatted as Mar 5, 2026, 3:00:00 pm EST . 
 Also, we don’t have to explicitly throw an exception. If an invalid string is passed to Temporal.Instant.from , Temporal will throw the exception for us. One thing to note is that even with strict parsing, the Moment version is still more lenient. Temporal requires the time zone offset at the end of the string. 
 You should also note that since we’re using navigator.language , this code will only run in a browser environment, as navigator is not defined in a Node.js environment. 
 The Temporal implementation uses the browser’s current locale ( navigator.language ), so the user will automatically get event times formatted in their local time format. In the en-US locale, this is Mar 5, 2026, 3:00:00 pm EST . However, if the user is in London, for example, the event times will be formatted as 5 Mar 2026, 15:00:00 GMT-5 . 
 Summary Action Moment.js Temporal 
 Current time moment() Temporal.Now.zonedDateTimeISO() 
 Parsing ISO moment(str) Temporal.Instant.from(str) 
 Add time .add(7, 'days') (mutates) .add({ days: 7 }) (new object) 
 Difference .diff(other, 'hours') .since(other).hours 
 Time zone .tz('Zone/Name') .withTimeZone('Zone/Name') 
 At first glance, the difference may be slightly different (and in the case of Temporal, sometimes more verbose and more strict) syntax, but there are several key advantages to using Temporal over Moment.js: 
 Being more explicit means fewer surprises and unintended bugs . Moment may appear to be more lenient, but it involves “guesswork,” which can sometimes result in incorrect dates. If you give Temporal something invalid, it throws an error. If the code runs, you know you’ve got a valid date. 
 Moment can add significant size to the application’s bundle, particularly if you’re using the moment-timezone package. Temporal adds nothing (once it’s shipped in your target browsers). 
 Immutability gives you the confidence that you’ll never lose or overwrite data when performing date conversions and operations. 
 Different representations of time ( Instant , PlainDateTime , ZonedDateTime ) depending on your requirements, where Moment is always a wrapper around a UTC timestamp. 
 Temporal uses the Intl APIs for date formatting , which means you can have locale-aware formatting without having to explicitly specify tokens. 
 Notes On The Polyfill As mentioned earlier, there is a Temporal polyfill available, distributed as an npm package named @js-temporal/polyfill . If you want to use Temporal today, you’ll need this polyfill to support browsers like Safari that haven’t shipped the API yet. The bad news with this is that it will add to your bundle size. The good news is that it still adds significantly less than moment or moment-timezone . Here is a comparison of the bundle sizes as reported by Bundlephobia.com, a website that presents information on npm package sizes (click on each package name to see the Bundlephobia analysis): 
 Package Minified Minified & gzipped 
 @js-temporal/polyfill 154.1 kB 44.1 kB 
 moment 294.4 kB 75.4 kB 
 moment-timezone 1 MB 114.2 kB 
 The polyfill also has historically had some performance issues around memory usage, and at the time of writing, it’s considered to be in an alpha state. Because of this, you may not want to use it in production until it reaches a more mature state. 
 The other good news is that hopefully the polyfill won’t be needed much longer (unless you need to support older browsers, of course). At the time of writing, Temporal has shipped in Chrome, Edge, and Firefox. It’s not quite ready in Safari yet, though it appears to be available with a runtime flag on the latest Technology Preview.
```

---

## 17. Beyond `border-radius`: What The CSS `corner-shape` Property Unlocks For Everyday UI

- 日期: 2026-03-12 10:00
- 链接: https://smashingmagazine.com/2026/03/beyond-border-radius-css-corner-shape-property-ui/

```
When I first started building websites, rounded corners required five background images, one for each corner, one for the body, and a prayer that the client wouldn’t ask for a different radius. Then the border-radius property landed, and the entire web collectively sighed with relief. That was over fifteen years ago, and honestly, we’ve been riding that same wave ever since. Just as then, I hope that we can look at this feature as a progressive enhancement slowly making its way to other browsers. 
 I like a good border-radius like any other guy, but the fact is that it only gives us one shape. Round. That’s it. Want beveled corners? Clip-path. Scooped ticket edges? SVG mask. Squircle app icons? A carefully tuned SVG that you hope nobody asks you to animate. We’ve been hacking around the limitations of border-radius for years, and those hacks come with real trade-offs: borders don’t follow clip-paths, shadows get cut off, and you end up with brittle code that breaks the moment someone changes a padding value. 
 Well, the new corner-shape changes all of that. 
 What Is corner-shape ? The corner-shape property is a companion to border-radius . It doesn’t replace it; it modifies the shape of the curve that border-radius creates. Without border-radius , corner-shape does nothing. But together, they’re a powerful pair. 
 The property accepts these values: 
 round : the default, same as regular border-radius , 
 squircle : a superellipse, the smooth Apple-style rounded square, 
 bevel : a straight line between the two radius endpoints (snipped corners), 
 scoop : an inverted curve, creating concave corners, 
 notch : sharp inward cuts, 
 square : effectively removes the rounding, overriding border-radius . 
 And you can set different values per corner, just like border-radius : 
 *corner-shape: bevel round scoop squircle;
/* top-left, top-right, bottom-right, bottom-left */ You can also use the superellipse() function with a numeric parameter for fine-grained control. 
 .element { 
 border-radius: 25px;
 corner-shape: superellipse(0); /* equal to 'bevel' */
} So the question here might be: why not call this property “ border-shape ” instead? Well, first of all, that is something completely different that we’ll get to play around with soon . Second, it does apply to a bit more than borders, such as outlines, box shadows, and backgrounds. That’s the thing that the clip-path property could never do. 
 Why Progressive Enhancement Matters Here At the time of writing (March 2026), corner-shape is only supported in Chrome 139+ and other Chromium-based browsers. That’s a significant chunk of users, but certainly not everyone. The temptation is to either ignore the property until it’s everywhere or to build demos that fall apart without it. 
 I don’t think either approach is right. The way I see it, corner-shape is the perfect candidate for progressive enhancement, just as border-radius was in the age of Internet Explorer 6. The baseline should use the techniques we already know, such as border-radius , clip-path , radial-gradient masks and look intentionally good. Then, for browsers that support corner-shape , we upgrade the experience. Sometimes this can be as simple as just providing a more basic default; sometimes it might need to be a bit more. 
 Every demo in this article is created with that progressive enhancement idea. The structure for the demos looks like: 
 @layer base, presentation, demo; The presentation layer contains the full polished UI using proven techniques. The demo layer wraps everything in @supports : 
 @layer demo {
 @supports (corner-shape: bevel) {
 /* upgrade styles here */
 }
} No fallback banners, no “your browser doesn’t support this” messages. Just two tiers of design: good and better. I thought it could be nice just to show some examples. There are a few out there already, but I hope I can add a bit of extra inspiration on top of those. 
 Demo 1: Product Cards With Ribbon Badges Every e-commerce site has them: those little “New” or “Sale” badges pinned to the corner of a product card. Traditionally, getting that ribbon shape means reaching for clip-path: polygon() or a rotated pseudo-element, let's call it “fiddly code” that has the chance to fall apart the moment someone changes a padding value. 
 But here’s the thing: we don’t need the ribbon shape in the baseline. A simple badge with slightly rounded corners tells the same story and looks perfectly fine: 
 .product__badge {
 border-radius: 0 4px 4px 0;
 background-color: var(--badge-bg);
} That’s it. A small, clean label sitting flush against the left edge of the card. Nothing fancy, nothing broken. It works in every browser. 
 For browsers that support corner-shape , we enhance: 
 @layer demo {
 /* If the browser supports `corner-shape` */
 @supports (corner-shape: bevel) {
 .product {
 border-radius: 40px;
 corner-shape: squircle;
 }

 .product__badge {
 padding: 0.35rem 1.4rem 0.35rem 1rem;
 border-radius: 0 16px 16px 0;
 corner-shape: round bevel bevel round;
 }
 }
} The round bevel bevel round combination creates a directional ribbon. Round where it meets the card edge, beveled to a point on the other side. No clip-path , no pseudo-element tricks. Borders, shadows, and backgrounds all follow the declared shape because it is the shape. 
 The cards themselves upgrade from border-radius: 12px to a larger size and the squircle corner-shape, that smooth superellipse curve that makes standard rounding look slightly off by comparison. Designers will notice immediately. Everyone else will just say it “feels more premium.” 
 Hot tip: Using the squircle value on card components is one of those upgrades where the before-and-after difference can be subtle in isolation, but transformative across an entire page. It’s the iOS effect: once everything uses superellipse curves, plain circular arcs start looking out of place. In this demo, I did exaggerate a bit. 
 The primary button starts beveled, faceted, and gem-like, and softens to squircle on hover. Because corner-shape values animate via their superellipse() equivalents, the transition is smooth. It’s a fun interaction that used to be hard to achieve but is now a single property (used alongside border-radius , of course). 
 The secondary button uses superellipse(0.5) , a value that is between a standard circle and a squircle, combined with a larger border-radius for a distinctive pill-like shape. The danger button gets a more prominent squircle with a generous radius. And notch and scoop each bring their own sharp or concave personality. 
 Beyond buttons, the status tags get corner-shape: notch , those sharp inward cuts that give them a machine-stamped look. The directional arrow tags use round bevel bevel round (and its reverse for the back arrow), replacing what used to require clip-path: polygon() . Now borders and shadows work correctly across all states. 
 Hot tip: corner-shape: scoop pairs beautifully with serif fonts and warm color palettes. The concave curves echo the organic shapes found in editorial design, calligraphy, and print layouts. For geometric sans-serif designs, stick with squircle or bevel . 
 What I like about this demo is how the shape hierarchy mirrors the content hierarchy. The most important element (featured plan) gets the most distinctive shape ( scoop ). The badge gets the sharpest shape ( bevel ). Everything else gets a simpler upgrade ( squircle ). Shape becomes a tool for visual emphasis, not just decoration. 
 Browser Support As of writing, corner-shape is available in Chrome 139+ and Chromium-based browsers. Firefox and Safari don’t support it yet. The spec lives in CSS Borders and Box Decorations Module Level 4 , which is a W3C Working Draft as of this writing. 
 For practical use, that’s fine. That’s the whole point of how these demos are built. The presentation layer delivers a polished, complete UI to every browser. The demo layer is a bonus for supporting browsers, wrapped in @supports (corner-shape: ...) . I lived through the time when border-radius was only available in Firefox. Somewhere along the line, it seems like we have forgotten that not every website needs to look exactly the same in every browser. What we really want is: no “broken” layouts and no “your browser doesn’t support this” messages, but rather a beautiful experience that just works, and can progressively enhance a bit of extra joy. In other words, we’re working with two tiers of design: good and better. 
 Wrapping Up The approach I keep coming back to is: don’t design for corner-shape , and don’t design around the lack of it. Design a solid baseline with border-radius and then enhance it. The presentation layer in every demo looks intentionally good. It’s not a degraded version waiting for a better browser. It’s a complete design . The demo layer adds a dimension that border-radius alone can’t express. 
 What surprises me most about corner-shape is the range it offers — the amazing powerhouse we have with this single property: squircle for that premium, superellipse feel on cards and avatars; bevel for directional elements and gem-like badges; scoop for editorial warmth and visual hierarchy; notch for mechanical precision on tags; and superellipse() for fine control between round and squircle . And the ability to mix values per corner ( round bevel bevel round , scoop round ) opens up shapes that would have required SVG masks or clip-path hacks. 
 We went from five background images to border-radius , to corner-shape . Each step removed a category of workarounds. I’m excited to see what designers do with this one. 
 Further Reading 
 corner-shape (MDN) 
 “ What Can We Actually Do With corner-shape ? ”, Daniel Schwarz 
 CSS Borders and Box Decorations Module Level 4 (W3C specification) 
 A fun demo for “eco-labels” , Sebastian on CodePen
```

---

## 18. Building Dynamic Forms In React And Next.js

- 日期: 2026-03-10 13:00
- 链接: https://smashingmagazine.com/2026/03/building-dynamic-forms-react-next-js/

```
This article is a sponsored by SurveyJS 
 There’s a mental model most React developers share without ever discussing it out loud. That forms are always supposed to be components. This means a stack like: 
 React Hook Form for local state (minimal re-renders, ergonomic field registration, imperative interaction). 
 Zod for validation (input correctness, boundary validation, type-safe parsing). 
 React Query for backend: submission, retries, caching, server sync, and so on. 
 And for the vast majority of forms — your login screens, your settings pages, your CRUD modals — this works really well. Each piece does its job, they compose cleanly, and you can move on to the parts of your application that actually differentiate your product. 
 But every once in a while, a form starts accumulating things like visibility rules that depend on earlier answers, or derived values that cascade through three fields. Maybe even entire pages that should be skipped or shown based on a running total. 
 You handle the first conditional with a useWatch and an inline branch, which is fine. Then another. Then you’re reaching for superRefine to encode cross-field rules that your Zod schema can’t express in the normal way. Then, step navigation starts leaking business logic. At some point, you look at what you’ve built and realize that the form isn’t really UI anymore. It’s more of a decision process, and the component tree is just where you happened to store it. 
 This is where I think the mental model for forms in React breaks down, and it’s really nobody’s fault. The RHF + Zod stack is excellent at what it was designed for. The issue is that we tend to keep using it past the point where its abstractions match the problem because the alternative requires a different way of thinking about forms entirely. 
 This article is about that alternative. To show this, we’ll build the exact same multi-step form twice: 
 With React Hook Form + Zod wired to React Query for submission, 
 With SurveyJS, which treats a form as data — a simple JSON schema — rather than a component tree. 
 Same requirements, same conditional logic, same API call at the end. Then we’ll map exactly what moved and what stayed, and lay out a practical way to decide which model you should use, and when. 
 The form we’re building: 
 This form will use a 4-step flow: 
 Step 1: Details 
 First name (required), 
 Email (required, valid format). 
 Step 2: Order 
 Unit price, 
 Quantity, 
 Tax rate, 
 Derived: Subtotal, 
 Tax, 
 Total. 
 Step 3: Account & Feedback 
 Do you have an account? (Yes/No) If Yes → username + password, both required. 
 If No → email already collected in step 1. 
 Satisfaction rating (1–5) If ≥ 4 → ask “What did you like?” 
 If ≤ 2 → ask “What can we improve?” 
 Step 4: Review 
 Only appears if total >= 100 
 Final submission. 
 This is not extreme. But it’s enough to expose architectural differences. 
 Part 1: Component-Driven (React Hook Form + Zod) Installation 
 npm install react-hook-form zod @hookform/resolvers @tanstack/react-query Zod Schema 
 Let’s start with the Zod schema, because that’s usually where the shape of the form gets established. For the first two steps — personal details and order inputs — everything is straightforward: required strings, numbers with minimums, and an enum. The interesting part starts when you try to express the conditional rules. 
 import { z } from "zod";

export const formSchema = z.object({ 
 firstName: z.string().min(1, "Required"), 
 email: z.string().email("Invalid email"), 
 price: z.number().min(0), 
 quantity: z.number().min(1), 
 taxRate: z.number(), 
 hasAccount: z.enum(["Yes", "No"]), 
 username: z.string().optional(), 
 password: z.string().optional(), 
 satisfaction: z.number().min(1).max(5), 
 positiveFeedback: z.string().optional(), 
 improvementFeedback: z.string().optional(), 
 }).superRefine((data, ctx) => { 
 if (data.hasAccount === "Yes") { 
 if (!data.username) { 
 ctx.addIssue({ code: "custom", path: ["username"], message: "Required" }); 
 } 
 if (!data.password || data.password.length < 6) { 
 ctx.addIssue({ code: "custom", path: ["password"], message: "Min 6 characters" }); 
 } 
 }

 if (data.satisfaction >= 4 && !data.positiveFeedback) { 
 ctx.addIssue({ code: "custom", path: ["positiveFeedback"], message: "Please share what you liked" }); 
 }

 if (data.satisfaction <= 2 && !data.improvementFeedback) { 
 ctx.addIssue({ code: "custom", path: ["improvementFeedback"], message: "Please tell us what to improve" }); 
 } 
 });

export type FormData = z.infer<typeof formSchema>; 
 Notice that username and password are typed as optional() even though they’re conditionally required because Zod’s type-level schema describes the shape of the object, not the rules governing when fields matter. 
 The conditional requirement has to live inside superRefine , which runs after the shape is validated and has access to the full object. That separation is not a flaw; it’s just what the tool is designed for: superRefine is where cross-field logic goes when it can’t be expressed in the schema structure itself. 
 What’s also notable here is what this schema doesn’t express. It has no concept of pages, no concept of which fields are visible at which point, and no concept of navigation. All of that will live somewhere else. 
 Form Component 
 import { useForm, useWatch } from "react-hook-form"; 
 import { zodResolver } from "@hookform/resolvers/zod"; 
 import { useMutation } from "@tanstack/react-query"; 
 import { useState, useMemo } from "react"; 
 import { formSchema, type FormData } from "./schema";

const STEPS = ["details", "order", "account", "review"];

type OrderPayload = FormData & { subtotal: number; tax: number; total: number };

export function RHFMultiStepForm() { 
 const [step, setStep] = useState(0);

 const mutation = useMutation({
 mutationFn: async (payload: OrderPayload) => {
 const res = await fetch("/api/orders", {
 method: "POST",
 headers: { "Content-Type": "application/json" },
 body: JSON.stringify(payload),
 });
 if (!res.ok) throw new Error("Failed to submit");
 return res.json();
 },
 });

 const { 
 register, 
 control, 
 handleSubmit, 
 formState: { errors }, 
 } = useForm<FormData>({ 
 resolver: zodResolver(formSchema), 
 defaultValues: { 
 price: 0, 
 quantity: 1, 
 taxRate: 0.1, 
 satisfaction: 3, 
 hasAccount: "No", 
 }, 
 }); 
 const price = useWatch({ control, name: "price" }); 
 const quantity = useWatch({ control, name: "quantity" }); 
 const taxRate = useWatch({ control, name: "taxRate" }); 
 const hasAccount = useWatch({ control, name: "hasAccount" }); 
 const satisfaction = useWatch({ control, name: "satisfaction" }); 
 const subtotal = useMemo(() => (price ?? 0) * (quantity ?? 1), [price, quantity]); 
 const tax = useMemo(() => subtotal * (taxRate ?? 0), [subtotal, taxRate]); 
 const total = useMemo(() => subtotal + tax, [subtotal, tax]); 
 const onSubmit = (data: FormData) => mutation.mutate({ ...data, subtotal, tax, total }); 
 const showSubmit = (step === 2 && total < 100) || (step === 3 && total >= 100)

 return ( 
 <form onSubmit={handleSubmit(onSubmit)}> 
 {step === 0 && ( 
 <> 
 <input {...register("firstName")} placeholder="First Name" /> 
 <input {...register("email")} placeholder="Email" /> 
 </> 
 )}

 {step === 1 && ( 
 <> 
 <input type="number" {...register("price", { valueAsNumber: true })} /> 
 <input type="number" {...register("quantity", { valueAsNumber: true })} /> 
 <select {...register("taxRate", { valueAsNumber: true })}> 
 <option value="0.05">5%</option> 
 <option value="0.1">10%</option> 
 <option value="0.15">15%</option> 
 </select>

 <div>Subtotal: {subtotal}</div> 
 <div>Tax: {tax}</div> 
 <div>Total: {total}</div> 
 </> 
 )}

 {step === 2 && ( 
 <> 
 <select {...register("hasAccount")}> 
 <option value="Yes">Yes</option> 
 <option value="No">No</option> 
 </select>

 {hasAccount === "Yes" && ( 
 <> 
 <input {...register("username")} placeholder="Username" /> 
 <input {...register("password")} placeholder="Password" /> 
 </> 
 )}

 <input type="number" {...register("satisfaction", { valueAsNumber: true })} />

 {satisfaction >= 4 && ( 
 <textarea {...register("positiveFeedback")} /> 
 )}

 {satisfaction <= 2 && ( 
 <textarea {...register("improvementFeedback")} /> 
 )} 
 </> 
 )}

 {step === 3 && total >= 100 && <div>Review and submit</div>}

 <div> 
 {step > 0 && <button type="button" onClick={() => setStep(step - 1)}>Back</button>} 
 {showSubmit ? ( 
 <button type="submit" disabled={mutation.isPending}> 
 {mutation.isPending ? "Submitting…" : "Submit"} 
 </button> 
 ) : step < STEPS.length - 1 ? ( 
 <button type="button" onClick={() => setStep(step + 1)}>Next</button> 
 ) : null} 
 </div> 
 {mutation.isError && <div>Error: {mutation.error.message}</div>} 
 </form> 
 ); 
 } 
 See the Pen SurveyJS-03-RHF [forked] by sixthextinction . 
 There’s quite a lot happening here, and it’s worth slowing down to notice where things ended up. 
 The derived values — subtotal , tax , total — are computed in the component via useWatch and useMemo because they depend on live field values and there’s no other natural place for them. 
 The visibility rules for username , password , positiveFeedback , and improvementFeedback live in JSX as inline conditionals. 
 The step-skipping logic — the review page only appearing when total >= 100 — is embedded into the showSubmit variable and the render condition on step 3. 
 Navigation itself is just a useState counter that we’re manually incrementing. 
 React Query handles retries, caching, and invalidation. The form just calls mutation.mutate with validated data. 
 None of this is wrong, per se. This is still idiomatic React, and the component is quite performant thanks to how RHF isolates re-renders. 
 But if you were to hand this to someone who hadn’t written it and ask them to explain under what conditions the review page appears , they’d have to trace through showSubmit , the step 3 render condition, and the nav button logic — three separate places — to reconstruct a rule that could have been stated in one line. 
 The form works, yes, but the behavior isn’t really inspectable as a system. It has to be executed mentally. 
 More importantly, changing it requires engineering involvement. Even a small tweak, like adjusting when the review step shows up, means editing the component, updating validation, opening a pull request, waiting for review, and deploying again. 
 Part 2: Schema-Driven (SurveyJS) Now let’s build the same flow using a schema. 
 Installation 
 npm install survey-core survey-react-ui @tanstack/react-query survey-core 
 The MIT-licensed platform-independent runtime engine that powers SurveyJS’s form rendering — the part we care about here. It takes a JSON schema, builds an internal model from it, and handles everything that would otherwise live in your React component: evaluating visibility expressions, computing derived values, managing page state, tracking validation, and deciding what “complete” means given which pages were actually shown. 
 survey-react-ui 
 The UI / rendering layer that connects that model to React. It’s essentially a <Survey model={model} /> component that re-renders whenever the engine’s state changes. SurveyJS UI libraries are also available for Angular , Vue3 , and many other frameworks. 
 Together, they give you a fully functional, multi-page form runtime without writing a single line of control flow. 
 The schema format itself is, as said before, just a JSON — no DSL or anything proprietary. You can inline it, import it from a file, fetch it from an API, or store it in a database column and hydrate it at runtime. 
 The Same Form, As Data 
 Here’s the same form, this time expressed as a JSON object. The schema defines everything: structure, validation, visibility rules, derived calculations, page navigation — and hands it to a Model that evaluates it at runtime. Here’s what that looks like in full: 
 export const surveySchema = { 
 title: "Order Flow", 
 showProgressBar: "top", 
 pages: [ 
 { 
 name: "details", 
 elements: [ 
 { type: "text", name: "firstName", isRequired: true }, 
 { type: "text", name: "email", inputType: "email", isRequired: true, validators: [{ type: "email", text: "Invalid email" }] } 
 ] 
 }, 
 { 
 name: "order", 
 elements: [ 
 { type: "text", name: "price", inputType: "number", defaultValue: 0 }, 
 { type: "text", name: "quantity", inputType: "number", defaultValue: 1 }, 
 { 
 type: "dropdown", 
 name: "taxRate", 
 defaultValue: 0.1, 
 choices: [ 
 { value: 0.05, text: "5%" }, 
 { value: 0.1, text: "10%" }, 
 { value: 0.15, text: "15%" } 
 ] 
 }, 
 { 
 type: "expression", 
 name: "subtotal", 
 expression: "{price} {quantity}" 
 }, 
 { 
 type: "expression", 
 name: "tax", 
 expression: "{subtotal} {taxRate}" 
 }, 
 { 
 type: "expression", 
 name: "total", 
 expression: "{subtotal} + {tax}" 
 } 
 ] 
 }, 
 { 
 name: "account", 
 elements: [ 
 { 
 type: "radiogroup", 
 name: "hasAccount", 
 choices: ["Yes", "No"] 
 }, 
 { 
 type: "text", 
 name: "username", 
 visibleIf: "{hasAccount} = 'Yes'", 
 isRequired: true 
 }, 
 { 
 type: "text", 
 name: "password", 
 inputType: "password", 
 visibleIf: "{hasAccount} = 'Yes'", 
 isRequired: true, 
 validators: [{ type: "text", minLength: 6, text: "Min 6 characters" }] 
 }, 
 { 
 type: "rating", 
 name: "satisfaction", 
 rateMin: 1, 
 rateMax: 5 
 }, 
 { 
 type: "comment", 
 name: "positiveFeedback", 
 visibleIf: "{satisfaction} >= 4" 
 }, 
 { 
 type: "comment", 
 name: "improvementFeedback", 
 visibleIf: "{satisfaction} <= 2" 
 } 
 ] 
 }, 
 { 
 name: "review", 
 visibleIf: "{total} >= 100", 
 elements: [] 
 } 
 ] 
 }; 
 Compare this to the RHF version for a moment. 
 The superRefine block that conditionally required username and password is gone. visibleIf: "{hasAccount} = 'Yes'" combined with isRequired: true handles both concerns together, on the field itself, where you'd expect to find them. 
 The useWatch + useMemo chain that computed subtotal , tax , and total is replaced by three expression fields that reference each other by name. 
 The review page condition, which in the RHF version was reconstructable only by tracing through showSubmit , the step 3 render branch. 
 And finally, the nav button logic is a single visibleIf property on the page object. 
 The same logic is there. It’s just that the schema gives it a place to live where it’s visible in isolation, rather than spread across the component. 
 Also, note that the schema uses type: 'expression' for subtotal, tax, and total. Expression is read-only and used mainly to display calculated values. SurveyJS also supports type: 'html' for static content, but for calculated values, expression is the right choice. 
 Now for the React side. 
 Rendering And Submission 
 Very simple. Wire onComplete to your API the same way — via useMutation or plain fetch : 
 import { useState, useEffect, useRef } from "react"; 
 import { useMutation } from "@tanstack/react-query"; 
 import { Model } from "survey-core"; 
 import { Survey } from "survey-react-ui"; 
 import "survey-core/survey-core.css";

export function SurveyForm() { 
 const [model] = useState(() => new Model(surveySchema));

 const mutation = useMutation({
 mutationFn: async (data) => {
 const res = await fetch("/api/orders", {
 method: "POST",
 headers: { "Content-Type": "application/json" },
 body: JSON.stringify(data),
 });
 if (!res.ok) throw new Error("Failed to submit");
 return res.json();
 },
 });

 const mutationRef = useRef(mutation);
 mutationRef.current = mutation;
 useEffect(() => { 
 const handler = (sender) => mutationRef.current.mutate(sender.data); 
 model.onComplete.add(handler); 
 return () => model.onComplete.remove(handler); 
 }, [model]); // ref avoids re-registering handler every render (mutation object identity changes)

 return (
 <>
 <Survey model={model} /> 
 {mutation.isError && <div>Error: {mutation.error.message}</div>}
 </>
 );
} 
 See the Pen SurveyJS-03-SurveyJS [forked] by sixthextinction . 
 onComplete fires when the user reaches the end of the last visible page. So if total never crosses 100 and the review page is skipped, it still fires correctly because SurveyJS evaluates visibility before deciding what “last page” means. 
 Then, sender.data contains all answers along with the calculated values ( subtotal , tax , total ) as first-class fields, so the API payload is identical to what the RHF version assembled manually in onSubmit . 
 The mutationRef pattern is the same one you’d reach for anywhere you need a stable event handler over a value that changes on every render — nothing SurveyJS-specific about it. 
 The React component no longer contains any business logic at all. There’s no useWatch , no conditional JSX, no step counter, no useMemo chain, no superRefine . React is doing what it’s actually good at: rendering a component and wiring it to an API call. 
 What Moved Out Of React? Concern RHF Stack SurveyJS 
 Visibility JSX branches visibleIf 
 Derived values useWatch / useMemo expression 
 Cross-field rules superRefine Schema conditions 
 Navigation step state Page visibleIf 
 Rule location Distributed across files Centralized in the schema 
 What stays in React is layout, styling, submission wiring, and app integration, which is to say, the things React is actually designed for . 
 Everything else moved into the schema, and because the schema is just a JSON object, it can be stored in a database, versioned independently of your application code, or edited through internal tooling without requiring a deploy. 
 A product manager who needs to change the threshold that triggers the review page can do that without touching the component. That’s a meaningful operational difference for teams where form behavior evolves frequently and isn’t always driven by engineers. 
 When To Use Each Approach? Here’s a good rule of thumb that works for me: imagine deleting the form entirely . What would you lose? 
 If it’s screens, you want component-driven forms. 
 If it’s business logic, like thresholds, branching rules, and conditional requirements that encode real decisions, you want a schema engine. 
 Similarly, if the changes coming your way are mostly about labels, fields, and layout, RHF will serve you fine. If they’re about conditions, outcomes, and rules that your ops or legal team might need to adjust on a Tuesday afternoon without filing a ticket, the schema model with SurveyJS is the more honest fit. 
 These two approaches are not really in competition with each other. They address different classes of problems, and the mistake worth avoiding is mismatching the abstraction to the weight of the logic — treating a rule system like a component because that’s the familiar tool, or reaching for a policy engine because a form grew to three steps and acquired a conditional field. 
 The form we built here sits near the boundary deliberately, complex enough to expose the difference but not so extreme that the comparison feels rigged. Most real forms that have gotten unwieldy in your codebase probably sit near that same boundary, and the question is usually just whether anyone has named what they actually are. 
 Use React Hook Form + Zod when: 
 Forms are CRUD-oriented; 
 Logic is shallow and UI-driven; 
 Engineers own all behavior; 
 Backend remains the source of truth. 
 Use SurveyJS when: 
 Forms encode business decisions; 
 Rules evolve independently of UI; 
 Logic must be visible, auditable, or versioned; 
 Non-engineers influence behavior; 
 The same form must run across multiple frontends.
```

---

## 19. Persuasive Design: Ten Years Later

- 日期: 2026-03-09 11:00
- 链接: https://smashingmagazine.com/2026/03/persuasive-design-ten-years-later/

```
Ten years ago, persuasive design was a relatively new frontier in the field of UX. In a 2015 Smashing article, I was among those who showed a way for practitioners to move from being primarily focused on improving usability and removing friction to also guide users toward a desired outcome. The premise was simple: by leveraging psychology , we could influence user behavior and drive outcomes like higher sign-ups, faster and richer onboarding, and stronger retention and engagement. 
 A decade later, that promise has proven true — but not in the same way many of us expected. Most product teams still face familiar problems: high bounce rates, weak activation, and users dropping off before experiencing core value. Usability improvements help, but they don’t always address the behavioral gap that sits underneath these patterns. 
 Persuasive design didn’t disappear — it matured. 
 Today, the more useful version of this work is often called behavioral design : a way to align product experiences with the real drivers of human behavior, with an ethical mindset. Done well, it can improve conversion, onboarding completion, engagement, and long-term use without slipping into manipulation. 
 Here’s what I’ll cover: 
 What has held up from the last decade of persuasive design; 
 What didn’t hold up, especially the limits of pattern-first gamification; 
 What changed in how we model behavior, from triggers to context and systems; 
 How to use modern behavioral frameworks to improve both discovery and ideation; 
 A practical way to run this work as a team, using a five-exercise workshop sequence , you can adapt to your product. 
 The goal is not to add more tactics to your toolkit. It’s to help you build a repeatable, shared approach to diagnosing behavioral barriers and designing solutions that support both users’ goals and business outcomes. 
 Is Persuasion The Same As Deception? Behavioral Design is not about slapping deceptive patterns or superficial “growth hacks” onto your UI. It’s about understanding what truly enables or hinders your users on their way to achieving their goal and then designing experiences that guide them to success. 
 Behavioral design is more about bridging the gap between what users want (achieving their goals, feeling value) and what businesses need (activation, retention, revenue), creating win-win outcomes where good UX and good business results align. 
 But like with all powerful tools, they can be used both for good and bad. The difference lies in the intention of the designer . Some designers argue for not promoting behavioral or persuasive design, while others argue that we need to understand the tools to learn how to use them well and how we can easily, and often mindlessly, fall into the trap of promoting an unethical lens. 
 If we are not enlightened, then how can we judge what represents good and bad practice? If we do not understand how psychology works, then we lack the awareness needed to spot our biases. If we don’t understand these tools, we can’t spot when they’re misused. 
 The difference between persuasion and deception is intention, plus accountability. 
 A Decade Later, What Have We learned? In the early 2010s, many teams treated persuasive design as almost synonymous with gamification. If you added points, badges, and leaderboards, you were doing psychology. And to be fair, those surface mechanics did work in some cases, at least in the short term. They could nudge people through onboarding flows or encourage a few extra logins. But over the decade, their limits became clear. Once the novelty wore off, many of these systems felt shallow. Users learned to ignore streaks that did not connect to anything meaningful or dropped out when they realized the game layer was not helping them reach a real goal. 
 This is where self-determination theory has quietly reshaped how serious teams think about motivation. It distinguishes between extrinsic motivators , such as rewards, points, and status, and intrinsic drivers like autonomy, competence, and relatedness. Put simply, if your “gamification” fights against what people actually care about, it will eventually fail. The interventions that have survived are the ones that support intrinsic needs. A language learning streak that makes you feel more capable and shows progress can work because it makes the core activity feel more meaningful and manageable. A badge that only exists to move a dashboard number, on the other hand, quickly becomes noise. 
 Lesson 1: From Quick Fixes To Behavioral Strategy One key lesson from the past decade is that behavioral design creates the most value when it moves beyond isolated fixes and becomes a deliberate strategy . Many product teams start with a narrow goal: improve a sign-up rate, reduce drop-off, or boost early retention. When standard UX optimizations plateau, they turn to psychology for a quick lift, often with success. 
 The biggest opportunity is not one more uplift on a stubborn metric, but having a systematic way to understand and shape behavior across the product. 
 Behavioral design isn’t about hacks. 
 It’s about helping people succeed. 
 Common signals are easy to recognize: people sign up but never finish onboarding; they click around once and never return; key features sit unused. A behavioral strategy doesn’t just ask “ What can we change on this screen?” It asks what is happening in the user’s mind and context at those moments. 
 That might lead you to design an onboarding experience that uses curiosity and the goal-gradient effect to guide people to a clear first win, instead of hoping they read a help doc. Or it might lead you to design for exploration and commitment over time: social proof where it actually matters, appropriate challenges that stretch but don’t overwhelm, progressive disclosure so advanced features show up when people are ready, and the right triggers at the most opportune moment instead of random nags. 
 Great products aren’t just easy to use. 
 They’re easier to commit to. 
 Product psychology has shifted from scattered hypotheses to a growing library of repeatable patterns . Those patterns only shine when they sit inside a coherent behavioral model: what users are trying to achieve, what blocks them, and which levers the team will pull at each stage. 
 Simple nudges, inspired by Thaler and Sunstein , have helped popularize behavioral thinking in design. But we’ve also learned that nudges alone rarely solve deeper behavioral challenges . A behavioral strategy goes further: it blends tactics, grounds them in real motivations, and ties experiments to a clear theory of change. The goal is not a one-off win on today’s dashboard, but a way of working that compounds over time. 
 Lesson 2: Game Mechanics Alone Are Not Enough 
 Game mechanics alone are no longer a credible behavioral strategy. Ten years ago, adding points, badges, and leaderboards was almost shorthand for “we’re doing psychology.” Today, most teams have learned the hard way that this is decoration unless it serves a real need. 
 A behavioral approach starts with a blunt question: What is the game layer in service of, and for whom? Does it help people make progress that matters to them, or does it just keep a dashboard happy? If it ignores intrinsic motivation, it will look clever in a slide deck and brittle in production. 
 In practice, that means points and streaks are not treated as automatic upgrades anymore. Teams ask whether a mechanic helps users feel more competent, more in control, or more connected to others. A streak only makes sense if it reflects real progress in a skill the user cares about. A leaderboard only adds value if people actually want to compare themselves and if the ranking helps them decide what to do next. If it does not pass those tests, it is clutter, not a motivational engine. 
 Streaks and badges only work when they support something users truly value. 
 The most effective products now start with the intrinsic side. They are clear about what the product helps users become or achieve, and only then ask whether a game mechanic can amplify that journey. When game elements are added, they live in the core loop rather than on top of it. They show mastery, mark meaningful milestones, and reinforce self-driven goals. That is the difference between treating gamification as a paint job and using it to support users on a path they already care about. 
 Lesson 3: From Cause And Effect To Holistic Systems Thinking 
 Early persuasive design often assumed a simple logic: find the broken step, add the right lever, and users move forward. Nice on a slide, rarely true in reality. 
 People don’t act for a single reason. They have context, history, competing goals, mood, time pressure, trust issues, and different definitions of success. Two users can take the same step for completely different reasons. The same user can behave differently on a different day. 
 That’s why systems thinking matters. Behavior is shaped by feedback loops and delays, not just one trigger. Outcomes we care about, trust, competence, and habit, are built over time. A change that boosts this week’s conversion can still weaken next month’s retention. 
 If you have ever shipped a “conversion win” and then watched support tickets, refunds, or churn go up, you have felt this. The local metric improved. The system got worse. 
 Your design structures either enable people or box them in. Defaults, navigation, feedback, pacing, rewards — each of these decisions reshapes the system and therefore the journeys people take through it. 
 So the job is not to perfect a single funnel. It is to build an environment where multiple valid paths can succeed, and where the system supports long-term goals, not just short-term clicks. 
 The job isn’t to perfect one funnel, but to support multiple valid paths. 
 A mature behavioral strategy is explicit about that. It is designed for several paths instead of one “happy flow,” supports autonomy instead of forcing compliance, and looks at downstream effects instead of only first-step conversion. 
 Lesson 4: From Triggers To Context 
 The same shift has happened in the frameworks we use. A decade ago, the Fogg Behavior Model (FBM) was everywhere. It gave teams a simple trio: motivation, ability, trigger — and a clear message: shouting louder with prompts does not fix low motivation or poor ability. That alone was a useful upgrade. 
 Fogg’s own work has moved on, too. With Tiny Habits, the focus leans more on identity, emotion, and making behaviors feel easy and personally meaningful. That mirrors a broader shift in the field: away from “fire more prompts” and toward designing environments where the right behavior feels natural. 
 Teams eventually ran into the same wall: prompts do not fix low capability or missing opportunity. You cannot nag people into skills they do not have or into contexts that do not exist. That is where many teams that work deeply with behavior change have gravitated toward COM-B as a more complete foundation. 
 COM-B breaks behavior into capability , opportunity , and motivation . It starts with a blunt check: can people actually do this, and does their environment let them? That maps well to modern products, where behavior happens across devices, channels, and moments, not on a single screen. It also plugs into broader behavior change work in health and public policy, so we do not have to reinvent everything inside UX. 
 Thinking this way nudges teams away from simple cause-and-effect stories. A drop in completion rate is no longer “the button is bad” or “we need more reminders,” but a question about how skills, context, and motivation interact. A capability issue might need a better interface and better education. An opportunity issue might be about device access, timing, or social surroundings, not layout. Motivation might be shaped as much by pricing and brand trust as by any in-product message. 
 Modern behavioral design is less about activating clicks and more about shaping conditions where action feels easy and meaningful. 
 This broader lens also makes cross-functional work simpler. Product, design, marketing, and data can share one behavior model and still see their own responsibilities in it. Designers shape perceived capability and opportunity in the interface, marketing shapes motivational framing and triggers, and operations shape the structural opportunity in the service. Instead of everyone pushing their own levers in isolation, COM-B helps teams see that they are working on different parts of the same system. 
 Lesson 5: Psychology Can Also Be Used To Design And Decode Discovery 
 COM-B is often used as a bridge between discovery and ideation. On the discovery side, it gives structure to research. You can use it to design interview guides, read analytics, and make sense of observational studies. It was built to diagnose what needs to change for a behavior to shift, which maps neatly onto early product discovery. 
 Good discovery doesn’t just ask what users say, but examines what their behavior reveals. 
 Instead of asking “Why did you stop using the product?” and writing down the first answer, you deliberately walk through capability, opportunity, and motivation. You ask things like: 
 Can users actually do this, given their skills and knowledge? 
 Does their context help or hinder them in practice? 
 How strong is their motivation compared with other demands on their time and money? 
 You walk through recent experiences in detail: which device they used, what time of day it was, who else was around, and what else they were juggling. You talk about how important this behavior is compared with everything else in their life and what trade-offs they make. To participants, these questions feel natural. Under the hood, you are systematically covering all three parts of COM-B, in line with how behavior change practitioners use the model in qualitative work. 
 You can look at behavioral data in the same way. Funnel drop-offs, time on task, and click patterns are clues: are people stuck because they cannot progress, because the environment gets in the way, or because they do not care enough to continue? Modern analytics tools make it easier to watch what people actually do rather than only what they report, and combining quantitative and qualitative data gives you a fuller picture than either alone. 
 When there is a gap between what people say and what they do, you treat it as a signal rather than an irritation. Someone might say that saving for retirement is very important, but never set up a recurring transfer. A user might claim that onboarding was simple, while their session shows repeated back and forth between steps. Those mismatches are often where biases, habits, and emotional barriers live. By labelling them in terms of capability, opportunity, and motivation, and linking them to specific barriers like risk aversion , analysis paralysis , status quo bias or present bias , you move from vague “insights” to a structured map of what is actually in the way. 
 The gap between what people say and what they do is not noise — it’s the map. 
 The output of this kind of discovery is not just personas and journeys. You also get a clear statement of the current behavior, the target behavior, and the behavioral barriers and enablers that sit between them. 
 Lesson 6: Use Behavioral Discovery In Your Ideation 
 The bridge from discovery to ideation can be a single sentence template: 
 From current behavior to target behavior , by doing X , because of barrier Y . 
 This “from–to–by–why” framing forces teams to say what they actually believe. You are not just saying “add a checklist.” You are saying: “We believe a checklist will help new users feel more capable, which will increase the chance they complete setup in their first session.” Now it is a behavioral hypothesis you can test with experiments , not just a design idea you hope for. 
 From there, you can generate several variants that express the same principle in different ways and design experiments around them. You might try a few messages that all lean on loss aversion , or several ways of simplifying a high-friction step, or different forms of social proof that vary in tone and proximity. 
 The important shift is that you are no longer throwing ideas at the wall. You are deliberately targeting the capability, opportunity, or motivation issues that discovery surfaced, and testing which levers actually work in your context. 
 Every idea should answer one question: which barrier are we trying to change? 
 Over time, this loop between behavioral discovery and ideation turns into a local playbook. You learn that in your product, some principles reliably help your users and others fall flat. You also learn that patterns from glowing case studies do not automatically transfer. Even gamification and behavior change research often emphasize context-specific , user-centred implementations rather than generic recipes. 
 This dual use of psychology in discovery and ideation is one of the bigger shifts of the past decade. A product trio can look at a stubborn drop-off point and ask, together, “Is this a capability, opportunity, or motivation issue?” Then they generate ideas that target that part of the system instead of guessing. That shared language makes behavioral design less of a specialist add-on and more of a normal way for cross-functional teams to reason about their work. 
 A Decade Later: What Has Proven To Work In Practice If the first decade of persuasive design taught us anything, it is that behavioral insight is cheap until a team can act on it together. 
 Methods matter. 
 Over time, a small set of workshop formats has consistently helped product teams uncover behavioral barriers, align on opportunities, and generate solutions grounded in real psychology instead of surface patterns. As behavioral design has grown from tactical nudges into a strategic discipline, an obvious question keeps coming up: How do teams actually do this work together in practice? 
 How do product managers, designers, researchers, and engineers move from scattered observations (“people seem confused here”) to a shared behavioral diagnosis, and then to targeted ideas that reflect the real drivers of capability, opportunity, and motivation? 
 One effective way to make this concrete is through a workshop format. The aim is to help teams: 
 Interpret research through a behavioral lens, 
 Surface capability, opportunity, and motivation gaps, 
 Prioritize high-potential opportunities, and 
 Generate ideas that are both psychologically sound and ethically considered. 
 Real product work is messy and full of feedback loops; nobody follows a perfect step-by-step checklist. But for learning, and especially for introducing behavioral design into a team for the first time, a structured sequence of exercises gives people a mental model. It shows the journey from early discovery to behavioral clarity, from opportunities to ideas, and finally to interventions that have been stress-tested through an ethical lens. 
 The exercises below are one such recipe. The order is intentional: each step builds on the previous one to move from empathy and insight to prioritized opportunities, concrete concepts, and responsible solutions. No team will follow it letter-perfect every time, but it reflects how behavioral design work tends to unfold when it goes well. 
 Before diving into the details, here is the full recipe and how each exercise contributes to the bigger behavioral design process: 
 Behavioral Empathy Mapping 
 Builds a shared understanding of the user’s psychological landscape: emotions, habits, misconceptions, and sources of friction. 
 Behavioral Journey Mapping 
 Maps the user’s flow over time, and overlays behavioral enablers and obstacles. 
 Behavior Scoring 
 Prioritizes which behavioral opportunities to tackle first based on impact, feasibility, and evidence. 
 Ideas First, Patterns Later 
 Encourages context-first ideation, then uses persuasive patterns to refine and strengthen promising concepts. 
 Dark Reality 
 Evaluates ethical risks, unintended consequences, and potential misuse. 
 A note on timing: In practice, this sequence can be run in different formats depending on constraints. For a compact format, teams often run Exercises 1–3 in a half-day workshop, and Exercises 4–5 in a second half-day session. With more time, the work can be spread across a full week: discovery synthesis early in the week, prioritization mid-week, and ideation plus ethical review toward the end. The structure matters more than the schedule; the goal is to preserve the progression from understanding → prioritization → ideation → reflection. 
 Below is a brief walkthrough of each exercise as I typically facilitate them in workshops in tandem with a library of persuasive patterns . 
 Exercise 1: Behavioral Empathy Mapping 
 The first step is building a shared, psychologically informed understanding of users. Behavioral Empathy Mapping extends traditional empathy mapping by paying attention to what users attempt, avoid, postpone, misunderstand, or feel uncertain about. These subtle behavioral signals often reveal more than stated needs or pain points. 
 Goal: Understand what drives or blocks the target behavior by capturing what users think, feel, say, and do — and spotting behavioral barriers and enablers. 
 Steps: 
 On a whiteboard or large paper, draw an empathy map: Thinking & Feeling, Seeing, Saying & Doing, and Hearing . 
 Add research insights by letting everyone silently add sticky notes from interviews, data, support logs, or observations into the quadrants. One insight per note. 
 Identify barriers and enablers. 
 Cluster notes that make the behavior harder (barriers) or easier (enablers). 
 Output: A focused map of the psychological and contextual forces shaping the target behavior, ready to feed into Behavioral Journey Mapping. 
 Exercise 2: Behavioral Journey Mapping 
 Once you understand the user’s mindset and context, the next step is to map how those forces play out across time. Behavioral Journey Mapping overlays the user’s goals, actions, emotions, and environment onto the product journey, highlighting the specific moments where behavior tends to stall or shift. 
 Unlike traditional journey maps, the behavioral version focuses on where capability breaks down, where the environment works against the user, and where motivation fades or conflicts arise. These become early signals of where change is both needed and possible. 
 The output shows the team precisely where the product is asking too much, where users lack support, or where additional motivation or clarity might be required. 
 Goal: Map the steps from the user’s starting point to the target behavior, and capture the key enablers and barriers along the way. 
 Steps: 
 Draw a horizontal line from A (starting point) to B (target behavior). 
 Have everyone write the steps a user takes from A to B on sticky notes (one per note). Include actions inside and outside the product. 
 Place the notes in order along the line. Merge duplicates and align on a shared sequence. 
 Extend the vertical axis with two rows: Enablers (what could help users move forward), 
 Barriers (what could slow or stop users). 
 Look for steps with many barriers or few enablers. These are behavioral hot spots. 
 Highlight the steps where a good nudge could meaningfully help users complete the journey. 
 Output: A clear, behavior-focused journey showing where users struggle, why, and which moments offer the most leverage for change . 
 Exercise 3: Behavior Scoring 
 With a clearer picture of the user journey and what moments could benefit from a behaviorally helpful hand, you are now ready to identify the behavior it makes most sense to focus on trying to influence. 
 Goal: Decide which potential target behaviors are worth focusing on first , based on impact, ease of change, and ease of measurement. 
 Steps: 
 List potential target behaviors. Based on the output of the Behavioral Journey Mapping, list behaviors that could potentially be targeted. One behavior per sticky note. Be as concrete as possible (what users do, where, and when). 
 Create a table with the following columns: Impact of behavior change (how much it could move the goal), 
 Ease of change (how realistic it is to influence), 
 Ease of measurement (how straightforward it is to track). 
 Potential target behaviors Impact of behavior change Ease of change Ease of measurement Total 
 … 
 … 
 … 
 Enter each listed behavior into the table and score them from 0 to 10 in each column. 
 Sort behaviors by total score and discuss the highest-scoring ones: Do they make sense given what you know about users and constraints? 
 Select the primary target behaviors you want to carry into the next exercises. 
 Optionally, note “bonus behaviors” that might follow as a side effect. 
 Output: A small set of prioritized target behaviors with a clear rationale for why they matter now, and a list of lower-priority behaviors you may revisit later. 
 A filled-out Behavior Scoring table could look like this: 
 Potential target behaviors Impact of behavior change Ease of change Ease of measurement Total 
 User completes onboarding checklist in first session. 8 6 9 23 
 User invites at least one teammate within 7 days. 9 4 8 21 
 User watches the full product tour video. 4 7 6 17 
 User reads help documentation during onboarding. 3 5 4 12 
 In this case, the checklist completion emerges as the strongest initial focus: it has high impact, is realistically influenceable through design changes, and can be measured reliably. Inviting a teammate may be strategically important, but it may require broader changes beyond interface design, making it a secondary focus. 
 Exercise 4: Ideas First, Patterns Later 
 Once the team has agreed on which behavior matters most, the next risk is jumping too quickly to familiar psychological tricks. One of the clearest lessons has been that starting with “the pattern” often leads to generic solutions that feel clever but fail in context. 
 This exercise deliberately separates idea generation from psychological framing . 
 Goal: Generate solutions grounded in user context first, then use psychological principles to sharpen and strengthen them. 
 Steps: 
 Start by restating the prioritized target behavior and the key barrier identified during journey mapping. Keep this visible throughout the exercise. 
 Then give the team a short, focused ideation window (10–15 minutes). 
 The rule here is simple: no references to behavioral models, cognitive biases, or persuasive patterns yet. Ideas should come directly from the user context, constraints, and moments uncovered earlier. 
 Collect ideas on a shared surface and group similar concepts. Look for multiple ways of solving the same underlying problem (cluster them together). 
 Only now do you introduce a library of psychological principles and techniques. I developed the persuasive patterns for this exact purpose. The goal of this step is not to replace ideas, but to refine them: 
 Which ideas could be strengthened by reducing friction? 
 Which might benefit from clearer feedback, social signals, or better timing? 
 Are there alternative ways to achieve the same effect more respectfully or more clearly? 
 Patterns are used as lenses, not prescriptions. If a pattern does not improve clarity, agency, or usefulness in this context, it is simply ignored. 
 Output: A refined set of solution concepts that are grounded in real user context and supported, where appropriate, by behavioral principles rather than driven by them. 
 This sequencing helps teams avoid “pattern-first design,” where ideas are reverse-engineered to fit a theory instead of addressing real human situations. 
 Exercise 5: Dark Reality 
 Before ideas turn into experiments or shipped features, they need one final test. Not for feasibility or metrics, but for ethics . 
 Over the years, this step has proven critical. Many persuasive solutions only reveal their downside when you imagine them working too well, or being applied in the wrong hands, or used on the wrong day by the wrong person. 
 Goal: Surface ethical risks, unintended consequences, and potential misuse before implementation. 
 Steps: 
 Take one or two of the strongest ideas from the previous exercise. 
 Imagine worst-case scenarios by asking the team to deliberately shift perspective: What if a competitor used this against us? 
 What if this nudges users when they’re stressed, tired, or vulnerable? 
 What happens if this works repeatedly over months, not once? 
 Could this create pressure, guilt, or dependence? 
 Capture concerns around autonomy, trust, fairness, inclusivity, or long-term well-being. 
 For each risk, explore ways to soften or counterbalance the effect: Clearer intent or transparency, 
 Lower frequency or gentler timing, 
 Explicit opt-outs, 
 Alternative paths forward. 
 Some ideas are reshaped. Some are paused. 
 Some survive intact, but now with greater confidence. 
 Output: Solutions that have been stress-tested ethically, with known risks acknowledged and mitigated rather than ignored. 
 Building A Shared Vocabulary For Product Psychology The teams that get the most out of behavioral design rarely have a single “psychology expert.” Instead, their team shares a vocabulary around product psychology and knows how to communicate around customer problem behaviorally. 
 A shared vocabulary turns psychology into cross-functional work. 
 When patterns and principles are shared: 
 Product, design, engineering, and marketing can talk about behavior without talking past each other. 
 Discovery insights are easier to interpret because common barriers and drivers have names. 
 Ideas can be framed as behavioral hypotheses (“we believe this will increase early competence…”) instead of vague guesses. 
 The Persuasive Patterns collection grew from this need: giving teams a common language and a concrete set of examples to point at. Whether used as a printed deck in a workshop or as long-form references during everyday work, the goal is the same: make product psychology something the whole team can see and discuss. 
 Persuasive design was often framed as a bag of tricks. Today, the work looks different: 
 Game mechanics are used to support intrinsic motivation , not drive vanity engagement. 
 Frameworks like COM-B and systems thinking help teams see behavior in context , not as a single trigger. 
 Behavioral insight is used to shape discovery and ideation , not just last-minute copy changes. 
 Ethics is part of the design brief, not an afterthought. 
 The next step is not more sophisticated nudges. It is a more systematic practice: simple methods, shared language, and a habit of asking “What is really going on in our users’ lives here?” 
 If you start by focusing on one behavioral problem, use a couple of the exercises in this article, and give your team a shared set of patterns to reference, you are already practicing persuasive design in the way it has evolved over the last ten years: grounded in evidence, respectful of users, and aimed at outcomes that matter on both sides of the screen.
```

---

## 20. Human Strategy In An AI-Accelerated Workflow

- 日期: 2026-03-06 08:00
- 链接: https://smashingmagazine.com/2026/03/human-strategy-ai-accelerated-workflow/

```
I’ve been working in User Experience design for more than twenty years. Long enough to have seen the many job titles, from when stakeholders asked us to “just make it pretty” to when wireframes were delivered as annotated PDFs. I’ve seen many tools come and go over the years, methodologies rise and fall, and entire platforms disappear. 
 Yet, nothing has unsettled designers quite like AI. 
 When generative AI tools first entered my workflow, my reaction wasn’t excitement — it was unease , with a little bit of curiosity . Watching an interface appear in seconds, complete with sensible spacing, readable typography, and halfway-decent copy, triggered a very real fear: If a machine can do this, where does that leave me? 
 That fear is now widespread. Designers at every level ask the same question, often quietly, “Will an AI agent replace me by next week/month/year?” While the difference between next week and next year seems a lot, it depends on where you are in your career and the speed at which your employer chooses to engage with AI tools. I have been lucky in several roles to be working with organisations that haven’t allowed the use of AI tools due to data security concerns. If you’re interested in any of these conversations, you can view the discussions happening on platforms like Reddit . 
 Fearing the takeover of AI in our roles is not irrational. We’re seeing AI generate wireframes, prototypes, personas, usability summaries, accessibility suggestions, and entire design systems. Tasks that once took days can now literally take minutes. 
 Here’s the uncomfortable truth: If your role is largely about producing artefacts, drawing buttons, aligning components, or translating instructions into screens, then parts of that work are already being automated. 
 Still, UX design has never truly been about just creating a user interface. 
 UX is about navigating ambiguity. It’s about advocating for humans in systems optimised for efficiency. It’s about translating messy human needs and equally messy business goals into experiences that feel coherent, fair, sensible, and usable. It’s about solving human problems by creating a useful and effective user experience. 
 AI isn’t replacing that work. Rather, it’s amplifying everything around it. The real shift happening is that designers are moving from being makers of outputs to directors of intent . From creators to curators. From hands-on executors to strategic decision-makers. That feels exciting to me. And the creativity and ingenuity this brings to the world of UX. 
 And that shift doesn’t reduce our value as UX designers, but it does redefine it. 
 What AI Does Better Than Us (The “Boring” Stuff) Let’s be clear, AI is better than humans at certain aspects of design work. Fighting that reality only keeps us stuck in fear. 
 Speed And Volume 
 AI is exceptionally good at generating large volumes of ideas quickly. For example, layout variations, copy options, component structures, and onboarding flows can all be produced in seconds. In early-stage design, this changes everything. Instead of spending hours sketching three concepts, you can review thirty. That doesn’t eliminate creativity but does expand the playground. 
 McKinsey estimates that generative AI can reduce the time spent on creative and design-related tasks by up to 70% , particularly during ideation and exploration phases. 
 AI can also help with the research side of UX, for example, exploring the habits of a certain demographic, and creating personas . While this can reduce research time required, the designer is still required to guardrail this by providing accurate prompts and reviewing generated responses . I have personally found that using AI to assist with the initial research for design projects is incredibly useful, specifically when there is limited time and access to users. 
 Consistency And Rule Adherence 
 Design systems live or die by consistency. AI excels at following rules relentlessly, colour tokens, spacing systems, typography scales, and accessibility standards. It doesn’t forget. It doesn’t get tired. It doesn’t “eyeball it.” 
 AI’s precision makes it incredibly valuable for maintaining large-scale design systems, especially in enterprise or government environments where consistency and compliance matter more than novelty. This is one component of my UX role that I am happy to hand over to AI to manage! 
 Data Processing At Scale 
 AI can analyse behavioural data at volumes challenging, if not impossible, for a human team to reasonably process. User journey paths, scroll depth, heatmaps to identify mouse interactions, conversion funnels — AI can identify patterns and anomalies almost instantly. 
 Behavioural analytics platforms increasingly rely on AI to surface insights that designers might otherwise miss. Contentsquare , an AI-powered analytics platform, talks about the impacts and benefits of utilising behavioural analytics data. I’ve always said that quantitative data tells us the “what”, and qualitative data tells us the “why”. This is the human component of research where we get to connect with the users to understand the reason driving the behaviour. 
 The key insight here is simple: Analysing large volumes of behavioural data was never where our highest value lay . 
 If AI can take on repetitive production, system enforcement, and raw data analysis, designers would be free to focus on interpretation, judgment, and human meaning, the hardest parts of the job. 
 What Humans Do Better Than AI (The “Heart” Stuff) For all its power, AI has a fundamental limitation: it has never and will never be human. 
 Empathy Is Lived Experience 
 AI can describe frustration. It can summarise user feedback. It can mimic empathetic language. But it has never felt the quiet rage of a broken form, the anxiety of submitting sensitive data, or the shame of not understanding an interface that assumes too much. 
 Empathy in UX isn’t a dataset. It’s a lived, embodied understanding of human vulnerability . This is why user interviews still matter. Why contextual inquiry still matters. Why designers who deeply understand their users consistently make better decisions. 
 In a previous role where I was designing an incredibly complex fraud alert platform, the key to successful outcomes of that design was based on my understanding of the variety of issues faced by customers. I accessed this information directly from members of the customer-facing team. This information was stored in their brain and based on direct experience with customers. No AI could know or access these goldmines of human experiences. 
 As the Nielsen Norman Group reminds us, good UX design is not about interfaces. It’s about communication and understanding . 
 Ethics Require Judgment 
 AI optimises for the objectives we give it. If the goal is engagement, it will try to maximise engagement — regardless of long-term harm. 
 It doesn’t inherently recognise dark patterns, manipulation, or emotional exploitation. Infinite scroll, variable rewards, and addictive loops are all patterns AI can enthusiastically optimise unless a human intervenes. 
 The Center for Humane Technology has documented how algorithmic optimisation can unintentionally undermine wellbeing. 
 Ethical UX design requires designers who can say, “We could do this, but we shouldn’t.” 
 Strategy Lives In Context 
 AI doesn’t sit in stakeholder meetings. It doesn’t hear what’s implied but not stated. It doesn’t understand organisational politics, regulatory nuance, or long-term positioning. 
 Designers act as translators between business intent and human impact. That translation relies on trust, relationships, and context, not pattern recognition. 
 This is why senior designers increasingly operate at the intersection of product, strategy, and culture. 
 The lesson is clear: As AI takes over execution, human designers become the guardians of intent. 
 How The Daily Work Of A Designer Is Changing This shift isn’t theoretical. It’s already reshaping daily design practice. 
 From Designing To Prompting 
 Designers are moving from manipulating pixels to articulating intent. Clear goals, constraints, and priorities become the input. 
 Instead of asking AI to “draw a dashboard,” the task becomes: 
 “Create a dashboard that reduces cognitive load for first-time users.” 
 “Explore layouts optimised for accessibility and low vision.” 
 Prompting isn’t about clever wording; it’s about clarity of thinking and understanding the intent of the outcomes . You may need to tweak your prompts as you go, but this is all part of the learning process of directing AI to deliver the outcomes needed. 
 From Making To Choosing 
 AI produces options. Designers make decisions. 
 A significant portion of future design work will involve reviewing, critiquing, and refining AI-generated outputs, and then selecting what best serves the user and aligns with ethical, business, and accessibility goals. 
 This mirrors how experienced designers already work: mentoring juniors, reviewing their concepts, and guiding direction, but at a much greater scale, given the sheer number of design options AI tools can generate. 
 The Movie Director Metaphor 
 I often describe the modern designer as a movie director. A director doesn’t operate the camera, build the set, or act every role, but they are responsible for the story, the emotional intent, and the audience experience. 
 AI tools are the crew. Designers are responsible for the meaning of the story. 
 A Real-World Shift: What This Looks Like In Practice To make this less abstract, let’s ground it in a familiar scenario. 
 Ten years ago, a designer might spend days producing wireframes for a new feature, carefully crafting each screen, annotating every interaction, and defending each decision in reviews. Much of the designer’s perceived value lived in the artefacts themselves. 
 Today, that same feature can be scaffolded in an afternoon with AI support. But here’s what hasn’t changed — the hard conversations. 
 The UX designer still has to ask: 
 Who is this actually for? 
 What problem are we solving, and for whom? 
 What happens when this fails? 
 Who might this unintentionally exclude or disadvantage? 
 In practice, I’ve seen senior designers spend less time inside design tools and more time facilitating workshops, synthesising messy inputs, mediating between stakeholders, and protecting user needs when trade-offs arise. 
 AI accelerates production, but it does not remove the designer’s responsibility. In fact, it increases it. When options are cheap and plentiful, discernment becomes a scarce skill. 
 Conclusion: How To Prepare Right Now Don’t panic — practice. 
 Avoiding AI won’t preserve your relevance. Learning to use it thoughtfully will. 
 Start small: 
 Explore Figma’s AI features . 
 Use AI for ideation, not final decisions. 
 Treat outputs as conversation starters, not answers. 
 Confidence comes from familiarity, not avoidance. 
 Invest In Human Skills. 
 The most resilient designers will double down on: 
 Psychology and behavioural science; 
 Communication and facilitation; 
 Ethics, accessibility, and inclusion; 
 Strategic thinking and storytelling. 
 These skills compound over time, and they can’t be automated. 
 The designer’s responsibility in an AI-accelerated world: 
 There’s an uncomfortable implication in all of this that we don’t talk about enough: when AI makes it easier to design anything , designers become more accountable for what gets released into the world. Bad design used to be excused by constraints. Limited time, limited tools, limited data. Those excuses are disappearing. When AI removes friction from execution, the ethical and strategic responsibility lands squarely on human shoulders. 
 This is where UX designers can, and must, step up as stewards of quality, accessibility, and humanity in digital systems. 
 Final Thought 
 AI won’t take your job. But a designer who knows how to think critically, direct intelligently, and collaborate effectively with AI might take the job of a designer who doesn’t. 
 The future of UX is no less human. It’s more intentional than ever.
```

---

## 21. Now Shipping: Accessible UX Research, A New Smashing Book By Michele Williams

- 日期: 2026-03-03 15:00
- 链接: https://smashingmagazine.com/2026/03/accessible-ux-research-release/

```
Good UX research is at the root of great products. It takes the guesswork out of our designs and helps us solve problems before they grow. One of the best ways to make our research effective is to keep it inclusive — testing with users with different needs and abilities, and using their feedback to build products that work for more people . 
 Our newest book, Accessible UX Research , can help you plan and execute great user research. Dr. Michele Williams draws from years of experience to build a clear, easy-to-follow roadmap. This book has something for everyone who wants to build digital products well: 
 If you are just getting started with research , you will find helpful tips for making your research more inclusive. You will also get a primer on how to ask better questions, understand your own biases, and how to use your limited time and budget effectively. 
 If you are an accessibility-minded professional , you will find a deep well of details on different assistive technologies, how to include them in your testing environment, and ways to record and share your results to create a real impact on the products you make. 
 If you are a developer , a manager , or just someone who wants to understand how different abilities impact each user’s experience, you will find the history, clear descriptions, and cultural touchpoints you need in order to make sense of all the accessibility and inclusion recommendations you encounter. 
 About The Book The book isn’t a checklist for you to complete as a part of your accessibility work. It’s a practical guide to inclusive UX research , from start to finish. If you’ve ever felt unsure how to include disabled participants, or worried about “getting it wrong,” this book is for you. You’ll get clear, practical strategies to make your research more inclusive, effective, and reliable. 
 Inside, you’ll learn how to: 
 Plan research that includes disabled participants from the start, 
 Recruit participants with disabilities, 
 Facilitate sessions that work for a range of access needs, 
 Ask better questions and avoid unintentionally biased research methods, 
 Build trust and confidence in your team around accessibility and inclusion. 
 The book also challenges common assumptions about disability and urges readers to rethink what inclusion really means in UX research and beyond. Let’s move beyond compliance and start doing research that reflects the full diversity of your users. Whether you’re in industry or academia, this book gives you the tools — and the mindset — to make it happen. 
 324 pages. Written by Dr. Michele A. Williams. Cover art by Espen Brunborg. Download a free sample (PDF, 2.3MB) or get the book right away. 
 Please note: We’ve found a way to get printed books to our US customers! After several months of dealing with customs and tariff issues, we are happy to announce that all of our books — including this brand-new one — are once again shipping worldwide . 
 With a foreword by Jared Smith of WebAIM and an extensive interview with a disabled researcher, “Accessible UX Research” brings together insights from throughout the Accessibility community. Photo by Marc Thiele. ( Large preview ) The book includes tips and strategies to help anyone doing research at any point in the product design cycle. Photo by Marc Thiele. ( Large preview )

Contents In Accessible UX Research , Michele Williams takes you on a deep dive into the real world of UX research , with a roadmap for including users with different abilities and needs. 
 1. Disability Mindset 
 + 
 For inclusive research to succeed, we must first confront our mindset about disability, typically influenced by ableism. 
 2. Diversity of Disability 
 + 
 Accessibility is not solely about blind screen reader users; disability categories help us unpack and process the diversity of disabled users. 
 3. Disability in the Stages of UX Research 
 + 
 Disabled participants can and should be part of every research phase — formative, prototype, and summative. 
 4. Recruiting Disabled Participants 
 + 
 Recruiting disabled participants is not always easy, but that simply means we need to learn strategies on where to look. 
 5. Designing Your Research 
 + 
 While our goal is to influence accessible products, our research execution must also be accessible. 
 6. Facilitating An Accessible Study 
 + 
 Preparation and communication with your participants can ensure your study logistics run smoothly. 
 7. Analyzing and Reporting with Accuracy and Impact 
 + 
 How you communicate your findings is just as important as gathering them in the first place — so prepare to be a storyteller, educator, and advocate. 
 8. Disability in the UX Research Field 
 + 
 Inclusion isn’t just for research participants , it’s important for our colleagues as well, as explained by blind UX Researcher Dr. Cynthia Bennett. 
 Appendix 
 + 
 In the appendix, you’ll find helpful summaries and tips to optimize your testing environment and your interactions with participants. 
 You’ll find plenty of useful references in the appendix at the end of the book. You’ll refer to these pages again and again. Photo by Marc Thiele. ( Large preview )

About the Author Dr. Michele A. Williams is owner of M.A.W. Consulting, LLC - Making Accessibility Work . Her 20+ years of experience include influencing top tech companies as a Senior User Experience (UX) Researcher and Accessibility Specialist and obtaining a PhD in Human-Centered Computing focused on accessibility. An international speaker, published academic author , and patented inventor , she is passionate about educating and advising on technology that does not exclude disabled users. 
 Testimonials “ Accessible UX Research stands as a vital and necessary resource. In addressing disability at the User Experience Research layer, it helps to set an equal and equitable tone for products and features that resonates through the rest of the creation process. The book provides a solid framework for all aspects of conducting research efforts, including not only process considerations, but also importantly the mindset required to approach the work. 
 This is the book I wish I had when I was first getting started with my accessibility journey. It is a gift, and I feel so fortunate that Michele has chosen to share it with us all.” 
 Eric Bailey, Accessibility Advocate 
 “User research in accessibility is non-negotiable for actually meeting users’ needs, and this book is a critical piece in the puzzle of actually doing and integrating that research into accessibility work day to day.” 
 Devon Pershing, Author of The Accessibility Operations Guidebook 
 “Our decisions as developers and designers are often based on recommendations, assumptions, and biases. Usually, this doesn’t work, because checking off lists or working solely from our own perspective can never truly represent the depth of human experience . Michele’s book provides you with the strategies you need to conduct UX research with diverse groups of people, challenge your assumptions, and create truly great products.” 
 Manuel Matuzović, Author of the Web Accessibility Cookbook 
 “This book is a vital resource on inclusive research. Michele Williams expertly breaks down key concepts, guiding readers through disability models, language, and etiquette. A strong focus on real-world application equips readers to conduct impactful, inclusive research sessions. By emphasizing diverse perspectives and proactive inclusion, the book makes a compelling case for accessibility as a core principle rather than an afterthought. It is a must-read for researchers, product-makers, and advocates!” 
 Anna E. Cook, Accessibility and Inclusive Design Specialist 
 Technical Details ISBN: 978-3-910835-03-0 (print) 
 Quality hardcover , stitched binding, ribbon page marker. 
 Free worldwide airmail shipping from Germany . 
 eBook available for download as PDF, ePUB, and Amazon Kindle . 
 Community Matters ❤️ Producing a book takes quite a bit of time, and we couldn’t pull it off without the support of our wonderful community . A huge shout-out to Smashing Members for the kind, ongoing support. The eBook is and always will be free for Smashing Members . Plus, Members get a friendly discount when purchasing their printed copy. Just sayin’! ;-) 
 More Smashing Books & Goodies Promoting best practices and providing you with practical tips to master your daily coding and design challenges has always been (and will be) at the core of everything we do at Smashing. 
 In the past few years, we were very lucky to have worked together with some talented, caring people from the web community to publish their wealth of experience as printed books that stand the test of time . Trine, Heather, and Steven are three of these people. Have you checked out their books already? 
 The Ethical Design Handbook 
 A practical guide on ethical design for digital products. 
 Add to cart $44 
 Understanding Privacy 
 Everything you need to know to put your users first and make a better web. 
 Add to cart $44 
 Touch Design for Mobile Interfaces 
 Learn how touchscreen devices really work — and how people really use them. 
 Add to cart $44
```

---

## 22. Getting Started With The Popover API

- 日期: 2026-03-02 10:00
- 链接: https://smashingmagazine.com/2026/03/getting-started-popover-api/

```
Tooltips feel like the smallest UI problem you can have. They’re tiny and usually hidden. When someone asks how to build one, the traditional answer almost always comes back using some JavaScript library. And for a long time, that was the sensible advice. 
 I followed it, too. 
 On the surface, a tooltip is simple. Hover or focus on an element, show a little box with some text, then hide it when the user moves away. But once you ship one to real users, the edges start to show. Keyboard users Tab into the trigger, but never see the tooltip. Screen readers announce it twice, or not at all. The tooltip flickers when you move the mouse too quickly. It overlaps content on smaller screens. Pressing Esc does not close it. Focus gets lost. 
 Over time, my tooltip code grew into something I didn’t really want to own anymore. Event listeners piled up. Hover and focus had to be handled separately. Outside clicks needed special cases. ARIA attributes had to be kept in sync by hand. Every small fix added another layer of logic. 
 Libraries helped, but they were also more like black boxes I worked around instead of fully understanding what was happening behind the scenes. 
 That was what pushed me to look at the newer Popover API . I wanted to see what would happen if I rebuilt a single tooltip using the browser’s native model without the aid of a library. 
 As we start, it’s worth noting that, as with any new feature, there are some things with it that are still being ironed out. That said, it currently enjoys great browser support, although there are several pieces to the overall API that are in flux. It’s worth keeping an eye on Caniuse in the meantime. 
 The “Old” Tooltip Before the Popover API, using a tooltip library was not a shortcut. It was the default. Browsers didn’t have a native concept of a tooltip that worked across mouse, keyboard, and assistive technology. If you cared about correctness, your only option was to use a library, and that is exactly what I did. 
 At a high level, the pattern was always the same: a trigger element, a hidden tooltip element, and JavaScript to coordinate the two. 
 <button class="info">?</button>
<div class="tooltip" role="tooltip">Helpful text</div> 
 The library handled the wiring that allowed the element to show on hover or focus, hide on blur or mouse leave, and reposition/resize on scroll. 
 Over time, the tooltip could become fragile. Small changes carried risk. Minor fixes caused regressions. Worse, adding new tooltips inherited the same complexity. Things technically worked, but never felt settled or complete. 
 That was the state of things when I decided to rebuild the tooltip using the browser’s native Popover API . 
 The Moment I Tried The Popover API I didn’t switch to using the Popover API because I wanted to experiment with something new. I switched because I was tired of maintaining tooltip behavior that I believed the browser should have already understood. 
 I was skeptical at first. Most new web APIs promise simplicity, but still require glue, edge-case handling, or fallback logic that quietly recreates the same complexity that you were trying to escape. 
 So, I tried the Popover API in the smallest way possible. Here’s what that looked like: 
 <!-- popovertarget creates the connection to id="tip-1" -->
<button popovertarget="tip-1">?</button>

<!-- popover="manual": browser manages this as a popover -->
<!-- role="tooltip": tells assistive technology what this is -->
<div id="tip-1" popover="manual" role="tooltip">
 This button triggers a helpful tip.
</div> 
 1. The Keyboard “Just Works” 
 Keyboard support depended on multiple layers lining up correctly: focus had to trigger the tooltip, blur had to hide it, Esc had to be wired manually, and timing mattered. If you missed one edge case, the tooltip would either stay open too long or disappear before it could be read. 
 With the popover attribute set to auto or manual , the browser takes over the basics: Tab and Shift + Tab behave normally, Esc closes the tooltip every time, and no extra listeners are required. 
 <div popover="manual">
 Helpful explanation
</div> What disappeared from my codebase were global keydown handlers, Esc -specific cleanup logic, and state checks during keyboard navigation. The keyboard experience stopped being something I had to maintain, and it became a browser guarantee. 
 2. Screenreader Predictability 
 This was the biggest improvement. Even with careful ARIA work, the behavior varied, as I outlined earlier. Every small change felt risky. Using a popover with a proper role looks and feels a lot more stable and predictable as far as what’s going to happen: 
 <div popover="manual" role="tooltip">
 Helpful explanation
</div> And here’s another win: After the switch, Lighthouse stopped flagging incorrect ARIA state warnings for the interaction, largely because there are no longer custom ARIA states for me to accidentally get wrong. 
 3. Focus Management 
 Focus used to be fragile. Before, I had rules like: let focus trigger show tooltip, move focus into tooltip and don’t close, blur trigger when it’s too close, and close tooltip and restore focus manually. This worked until it didn’t. 
 With the Popover API, the browser enforces a simpler model where focus can more naturally move into the popover. Closing the popover returns focus to the trigger, and there are no invisible focus traps or lost focus moments. And I didn’t add focus restoration code; I removed it. 
 Conclusion The Popover API means that tooltips are no longer something you simulate. They’re something the browser understands. Opening, closing, keyboard behavior, Escape handling, and a big chunk of accessibility now come from the platform itself, not from ad-hoc JavaScript. 
 That does not mean tooltip libraries are obsolete because they still make sense for complex design systems, heavy customization, or legacy constraints, but the default has shifted . For the first time, the simplest tooltip can also be the most correct one. If you are curious, try this experiment: Simply replace just one tooltip in your product with the Popover API, do not rewrite everything, do not migrate a whole system, and just pick one and see what disappears from your code. 
 When the platform gives you a better primitive, the win is not just fewer lines of JavaScript, but it is fewer things you have to worry about at all. 
 Check out the full source code in my GitHub repo . 
 Further Reading 
 For deeper dives into popovers and related APIs: 
 “ Poppin’ In ”, Geoff Graham 
 “ Clarifying the Relationship Between Popovers and Dialogs ”, Zell Liew 
 “ What is popover=hint? ”, Una Kravets 
 “ Invoker Commands ”, Daniel Schwarz 
 “ Creating an Auto-Closing Notification with an HTML Popover ”, Preethi 
 Open UI Popover API Explainer 
 “ Pop(over) the Balloons ”, John Rhea 
 “ CSS Anchor Positioning ”, Juan Diego Rodríguez 
 MDN also offers comprehensive technical documentation for the Popover API.
```

---

## 23. Fresh Energy In March (2026 Wallpapers Edition)

- 日期: 2026-02-28 09:00
- 链接: https://smashingmagazine.com/2026/02/desktop-wallpaper-calendars-march-2026/

```
Blooming flowers, longer days, milder temperatures — with March just around the corner, the world is slowly but surely awakening from its winter slumber , fueling us with fresh energy. And even if spring is far away in your part of the world, you might sense that 2026 has gained full speed by now, making it the perfect moment to turn those plans and ideas you’ve been carrying around into action. 
 To accompany you on all those adventures that March may bring, we have a new collection of desktop wallpapers for you, just as it has been a monthly tradition here at Smashing Magazine for more than 14 years already. Designed by artists and designers from across the globe, each wallpaper comes in a variety of screen resolutions and can be downloaded for free. A huge thank-you to everyone who shared their designs with us — this post wouldn’t be possible without your kind support! 
 If you , too, would like to get featured in one of our upcoming wallpapers editions, please don’t hesitate to submit your design . We can’t wait to see what you’ll come up with! Happy March! 
 You can click on every image to see a larger preview . 
 We respect and carefully consider the ideas and motivation behind each and every artist’s work. This is why we give all artists the full freedom to explore their creativity and express emotions and experience through their works. This is also why the themes of the wallpapers weren’t anyhow influenced by us but rather designed from scratch by the artists themselves. 
 Timid Blossom “With Spring knocking and other seasons fighting to get attention, March greets us with blossoms.” — Designed by Ginger It Solutions from Serbia. 
 preview 
 with calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1020 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1020 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Cascade Style Sheet Designed by Ricardo Gimenes from Spain. 
 preview 
 with calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 I’m Not Okay, But It’s Okay Designed by Ricardo Gimenes from Spain. 
 preview 
 with calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Let’s Spring “After some freezing months, it’s time to enjoy the sun and flowers. It’s party time, colors are coming, so let’s spring!” — Designed by Colorsfera from Spain. 
 preview 
 without calendar: 320x480 , 1024x768 , 1024x1024 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Spring Is Coming “This March, our calendar design epitomizes the heralds of spring. Soon enough, you’ll be waking up to the singing of swallows, in a room full of sunshine, filled with the empowering smell of daffodil, the first springtime flowers. Spring is the time of rebirth and new beginnings, creativity and inspiration, self-awareness, and inner reflection. Have a budding, thriving spring!” — Designed by PopArt Studio from Serbia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1440x900 , 1440x1050 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Explore The Forest “This month, I want to go to the woods and explore my new world in sunny weather.” — Designed by Zi-Cing Hong from Taiwan. 
 preview 
 without calendar: 1024x768 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Coffee Break Designed by Ricardo Gimenes from Spain. 
 preview 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Time To Wake Up “Rays of sunlight had cracked into the bear’s cave. He slowly opened one eye and caught a glimpse of nature in blossom. Is it spring already? Oh, but he is so sleepy. He doesn’t want to wake up, not just yet. So he continues dreaming about those sweet sluggish days while everything around him is blooming.” — Designed by PopArt Studio from Serbia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 So Tire Designed by Ricardo Gimenes from Spain. 
 preview 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Botanica Designed by Vlad Gerasimov from Georgia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Music From The Past Designed by Ricardo Gimenes from Spain. 
 preview 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3840x2160 
 Queen Bee “Spring is coming! Birds are singing, flowers are blooming, bees are flying… Enjoy this month!” — Designed by Melissa Bogemans from Belgium. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 MARCHing Forward “If all you want is a little orange dinosaur MARCHing (okay, I think you get the pun) across your monitor, this wallpaper was made just for you! This little guy is my design buddy at the office and sits by (and sometimes on top of) my monitor. This is what happens when you have designer’s block and a DSLR.” — Designed by Paul Bupe Jr from Statesboro, GA. 
 preview 
 without calendar: 1024x768 , 1280x1024 , 1440x900 , 1920x1080 , 1920x1200 , 2560x1440 
 Spring Bird Designed by Nathalie Ouederni from France. 
 preview 
 without calendar: 1024x768 , 1280x1024 , 1440x900 , 1680x1200 , 1920x1200 , 2560x1440 
 Awakening “I am the kind of person who prefers the cold but I do love spring since it’s the magical time when flowers and trees come back to life and fill the landscape with beautiful colors.” — Designed by Maria Keller from Mexico. 
 preview 
 without calendar: 320x480 , 640x480 , 640x1136 , 750x1334 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1242x2208 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Fresh Lemons Designed by Nathalie Ouederni from France. 
 preview 
 without calendar: 320x480 , 1024x768 , 1280x1024 , 1440x900 , 1600x1200 , 1680x1200 , 1920x1200 , 2560x1440 
 Jingzhe “Jīngzhé is the third of the 24 solar terms in the traditional East Asian calendars. The word 驚蟄 means ‘the awakening of hibernating insects’. 驚 is ‘to start’ and 蟄 means ‘hibernating insects’. Traditional Chinese folklore says that during Jingzhe, thunderstorms will wake up the hibernating insects, which implies that the weather is getting warmer.” — Designed by Sunny Hong from Taiwan. 
 preview 
 without calendar: 800x600 , 1280x720 , 1280x1024 , 1366x768 , 1400x1050 , 1680x1200 , 1920x1080 , 2560x1440 
 Waiting For Spring “As days are getting longer again and the first few flowers start to bloom, we are all waiting for spring to finally arrive.” — Designed by Naioo from Germany. 
 preview 
 without calendar: 1280x800 , 1366x768 , 1440x900 , 1680x1050 , 1920x1080 , 1920x1200 
 Happy Birthday Dr. Seuss! “March 2nd marks the birthday of the most creative and extraordinary author ever, Dr. Seuss! I have included an inspirational quote about learning to encourage everyone to continue learning new things every day.” — Designed by Safia Begum from the United Kingdom. 
 preview 
 without calendar: 800x450 , 1280x720 , 1366x768 , 1440x810 , 1600x900 , 1680x945 , 1920x1080 , 2560x1440 
 Spring Is Inevitable “Spring is round the corner. And very soon plants will grow on some other planets too. Let’s be happy about a new cycle of life.” — Designed by Igor Izhik from Canada. 
 preview 
 without calendar: 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 2560x1600 
 Ballet “A day, even a whole month, isn’t enough to show how much a woman should be appreciated. Dear ladies, any day or month are yours if you decide so.” — Designed by Ana Masnikosa from Belgrade, Serbia. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1040 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Pizza Time “Who needs an excuse to look at pizza all month?” — Designed by James Mitchell from the United Kingdom. 
 preview 
 without calendar: 1280x720 , 1280x800 , 1366x768 , 1440x900 , 1680x1050 , 1920x1080 , 1920x1200 , 2560x1440 , 2880x1800 
 Imagine Designed by Romana Águia Soares from Portugal. 
 preview 
 without calendar: 640x480 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Questions “Doodles are slowly becoming my trademark, so I just had to use them to express this phrase I’m fond of recently. A bit enigmatic, philosophical. Inspiring, isn’t it?” — Designed by Marta Paderewska from Poland. 
 preview 
 without calendar: 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 The Unknown “I made a connection, between the dark side and the unknown lighted and catchy area.” — Designed by Valentin Keleti from Romania. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Let’s Get Outside Designed by Lívia Lénárt from Hungary. 
 preview 
 without calendar: 1024x768 , 1280x1024 , 1366x768 , 1600x1200 , 1680x1200 , 1920x1080 , 1920x1200 , 2560x1440 
 Fresh Flow “It’s time for the water to go down the mountains, it’s time for the rivers to get rid of ice blocks, it’s time for the ground to feed the plants, it’s time to go out and take a deep breath. I imagined these ideas with interlacing colored lines.” — Designed by Philippe Brouard from France. 
 preview 
 without calendar: 1024x768 , 1366x768 , 1600x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 2560x1600 , 2880x1800 , 3840x2160 
 St. Patrick’s Day “On the 17th March, raise a glass and toast St. Patrick on St. Patrick’s Day, the Patron Saint of Ireland.” — Designed by Ever Increasing Circles from the United Kingdom. 
 preview 
 without calendar: 320x480 , 640x480 , 800x480 , 800x600 , 1024x768 , 1024x1024 , 1080x1080 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Sending FriendShips To March Designed by João Acácio from Portugal. 
 preview 
 without calendar: 800x600 , 1024x768 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1280x1024 , 1366x768 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1680x1200 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 
 Bee-utiful Smile Designed by Doreen Bethge from Germany. 
 preview 
 without calendar: 640x480 , 800x600 , 1024x768 , 1152x864 , 1280x720 , 1280x800 , 1280x960 , 1400x1050 , 1440x900 , 1600x1200 , 1680x1050 , 1920x1080 , 1920x1200 , 1920x1440 , 2560x1440 , 3200x2000 
 Sakura Designed by Evacomics from Singapore. 
 preview 
 without calendar: 320x480 , 768x1024 , 1024x768 , 1280x800 , 1280x1024 , 1440x900 , 1920x1080 , 2560x1440 
 Get Featured Next Month Feeling inspired? We’ll publish the April wallpapers on March 31, so if you’d like to be a part of the collection, please don’t hesitate to submit your design . We are already looking forward to it!
```

---

## 24. Say Cheese! Meet SmashingConf Amsterdam 🇳🇱

- 日期: 2026-02-26 11:00
- 链接: https://smashingmagazine.com/2026/02/meet-smashingconf-amsterdam/

```
We’ve been passionate about design & UX for years. We’ve published articles on design systems and usability , inclusive design and product design, UX research and enterprise UX. Now it’s time to bring it all together: In-person. In a new location. With a new spirit of curiosity and community. And it’s happening this April! 
 Meet the first SmashingConf Amsterdam 🇳🇱 taking place on April 13–16, 2026! A conference for designers and UI engineers all around UX and front-end: design systems, accessibility, Figma, UX writing, modern CSS and AI .. all while enjoying the best views, fun and gezelligheid that Amsterdam has to offer! 
 In-Person 
 Online 
 In-Person 
 € 72479 Get your ticket! Apr 13–16, 2026 . Amsterdam, the Netherlands. 
 Save up to 25% with Smashing Membership . 
 Online 
 € 20000 
 Live talks + Behind the scenes With all video recordings, of course. 
 Save up to 25% with Smashing Membership . 
 “Gezelligheid” Meets Modern Tech 
 Perhaps one of the most difficult Dutch words to translate directly into English is the Dutch word Gezelligheid (pronounced guh-ZELL-uhk-hyde). It’s a foundational concept in Dutch culture that translates loosely to coziness, conviviality, and a warm, social, or inviting atmosphere — and that’s exactly what SmashingConf Amsterdam has to offer! 🙌 
 What Should You Expect? Ever since launching our first-ever SmashingConf back in 2012, each one has always focused on how folks in the industry work, how they fail and how they succeed. We kindly encourage our speakers to share lessons learned and show how they work. Don’t be surprised by speakers sitting down and showing their design process, or setting up a Figma board and designing live with the audience! 
 SmashingConf Amsterdam is a premier, single-track conference curated for front-end developers, UI engineers, and UX designers. Unlike traditional conferences that rely on polished slide decks, SmashingConf is distinguished by its "live-work" philosophy . Speakers are encouraged to show their actual workflows—coding live, designing in Figma, and troubleshooting in real-time—to provide actionable insights rather than high-level theory. 
 All of our Smashing conferences are friendly and inclusive . In fact, we know many attendees by names, and we love friendships emerging as people get together and learn together, during the talks as well as in the workshops. Plus, we design our side events to help everyone take part in meaningful, respectful conversations. 
 Already convinced, but need to convince your manager? We’ve got your back! Download the Convince Your Boss PDF to tip the scales in your favor. We’ve prepared a “ letter to the boss ” template for you as well. Good luck! 
 Meet the Speakers Expect 10 practical talks from friendly, knowledgeable and approachable speakers who are bound to inspire you. See schedule → 
 Meet Kevin Powell , Nick DiLallo , Sara Soueidan , TJ Pitre , Calvin Robertson , Christine Vallaure , Nathan Curtis , Nadieh Bremer , Chris Kolb , and of course the Mystery Speaker . 
 Our speakers are very approachable and there is enough time for you to ask all your questions and get all the answers, in 1:1-conversations or in round tables. 
 Full-Day Workshops: Immersive, Hands-On Learning If you attend a conference, why not join a practical workshop as well? Beyond the main stage sessions, the event offers a curated selection of seven full-day workshops . These are designed for deep-dive practical learning, allowing you to spend an entire day mastering a specific topic of your choice under the guidance of a world-class expert. 
 On April 13 and April 16 , we run two full-days of training focusing around tangible, applicable insights that you can use right after the workshop. That way, you can dive even more into design systems, accessibility testing or complex interface design patterns. Plenty of topics to choose from, and bundle discounts are available, too: You can save €100 when signing up for the conference and a workshop → 
 Smashing In-Person Workshops 
 Figma Deep Dive with Christine Vallaure. 
 Building Context-Based Design Systems for AI-Driven Product Teams with TJ Pitre 
 Front-End Accessibility Workshop with Sara Soueidan . 
 Designing For Complex UIs, 2026 Edition with Vitaly Friedman 
 The New CSS Toolkit with Kevin Powell. 
 Architecting Component Anatomy, Props and Slots with Nathan Curtis. 
 How To Measure UX and Design Impact with Vitaly Friedman. 
 The Venue: Pathé Tuschinski We definitely don’t choose venues randomly. We love the contrast of beautiful historical venues and digital craftsmanship, so for Amsterdam, we’ve chosen the magnificent Pathé Tuschinski — an unforgettable venue that will make quite an impression on you! (Pathé Tuschinski will be our home for both conference days.) 
 Walking into Pathé Tuschinski feels like stepping into a living masterpiece . Opened in 1921, the legendary cinema contains so much detail — from the ornate ceilings to the glowing wall sconces. 
 The main auditorium is designed with comfort in mind. Plush, spacious seats ensure that you’ll be able to enjoy a perfectly unobstructed view of the stage or screen — no craning your neck, no dodging tall heads! 
 Side Events Before, During and After While in Amsterdam, Why not explore the neighborhood and the city itself? At the end of the day, it’s about the fringe experiences that transform into something unforgettable! 
 Friedman’s Fabulous Fries Feestje 🍟 
 Join the one-and-only Vitaly for a little feestje (that’s Dutch for “small party”) through a few cool neighborhoods of the city, sharing his best tips on bitterballen, fries, ice cream, and more. It’s a great way to connect with fellow attendees before the main event even begins, and bond over cones of perfectly crispy Dutch fries! 
 Smashing Sloep (Canal Tour) 🚤 
 Enjoy a chill, 2-hour cruise through the Amsterdam iconic canals, navigating past historic canal houses and under low stone bridges. You'll share a sloepje with 6–7 fellow attendees, and choose your own route. The fee of €30,– is not included in your conference ticket, so make sure you register separately (friends and family are welcome to join in, too!). 
 Jam Session 🎤 
 Lightning talks, drinks and snacks: it’s the perfect setting to meet fellow attendees and “geek out” the night before the conference. This event is for attendees only, and you can pick up your badge early and skip the registration lines on Tuesday morning. The atmosphere is open, friendly and energizing, so make sure to join in! 
 Sports & Morning Rituals 🧘 
 It’s all about keeping the energy high and clearing your head. Whether you’re a runner or more of a yoga cat, we’ve got just what you need. You can join speakers and attendees for a 5k run, and then if you like, join a mindfulness session with a few minutes of functional stretches followed by guided meditation and stillness. You do you! 
 Bitterballen & Beer 🍺 
 You can’t be in the Netherlands without embracing local flavor. Breaks come with bitterballen — the iconic Dutch crispy meat snacks — paired with cold beer. It’s not just catering; it’s culture. 
 Together, these side events turn a conference ticket into a full experience — part learning, part adventure, part community. Inside Pathé Tuschinski, you get the “back to the future” inspiration. Outside, you get the human connections that make it all more meaningful! 
 Team Tickets? 👫👭 Bring the entire team to SmashingConf, and save some of your training budget along the way as well. With our friendly bundle tickets and team discounts, we’ve got your back! If you want to come with a large team, or are interested in something special, please send us a short email and we’ll get back to you right away! 
 We Can’t Wait To See You! As we are getting ready for the event, we couldn’t be more excited to meet you in Amsterdam. Let’s boost our design and UX skills, together, and create memorable experiences that will last for a while. 🧡 
 In-Person 
 Online 
 In-Person 
 € 72479 Get your ticket! Apr 13–16, 2026 . Amsterdam, the Netherlands. 
 Save up to 25% with Smashing Membership . 
 Online 
 € 20000 
 Live talks + Behind the scenes With all video recordings, of course. 
 Save up to 25% with Smashing Membership . 
 Ah, perhaps your manager needs a little bit convincing ? We’ve got your back! Download the Convince Your Boss PDF to tip the scales in your favor. And we’ve prepared a “ letter to the boss ” template for you as well. Good luck! 🤞🤞🏼🤞🏾
```

---

## 25. A Designer’s Guide To Eco-Friendly Interfaces

- 日期: 2026-02-23 10:00
- 链接: https://smashingmagazine.com/2026/02/designer-guide-eco-friendly-interfaces/

```
I’ve spent over two decades in the trenches of user experience design. I remember the transition from table-based layouts to CSS, the pivot to responsive design when the iPhone launched, and the rise of the “attention economy.” But as we navigate 2026, the industry is facing its most significant shift yet. We are moving past the era of “design at any cost” into the era of Sustainable UX . 
 It’s not something most designers think about, including myself, until I was prompted by hearing about this as a concept. For years, we have treated the internet as an ethereal, weightless cloud. We have assumed that digital products were “green” simply because they weren't printed on paper. I used to think that too, and before the concept of climate change emerged, it was more about saving trees. 
 We were wrong. The cloud is a physical infrastructure, a sprawling network of data centres, undersea cables, and cooling systems that hum 24/7. While AI-focused data centers match the power consumption of massive aluminum smelters , their high geographic density creates an even more intense and localised environmental strain. 
 As UX designers, we are the architects of this energy consumption. Every high-resolution hero image, every auto-playing background video, and every complex JavaScript animation we approve is a direct instruction to a processor to consume power. If we want to build a future that lasts, we must stop designing for “wow” and start designing for efficiency. 
 Dark Mode In the early 2000s, white backgrounds were the standard because they mimicked the familiarity of paper. However, the hardware has evolved, and our design philosophy must follow. The shift from LCD to OLED (Organic Light Emitting Diode) technology has fundamentally changed how colour impacts energy. 
 The Logic 
 Unlike traditional LCD screens, which require a backlight that is always on (even when displaying black), OLED screens illuminate each pixel individually . When a pixel is set to true black ( #000000 ), that specific diode is turned completely off. It draws zero power. 
 By designing interfaces that favour darker palettes, we aren’t just following a trend; we are physically reducing the energy requirement of the user’s device. 
 The Data 
 The energy savings are far from negligible. A landmark study by Purdue University in 2021, which has become the gold standard for this discussion, revealed that at 100% brightness, switching from light mode to dark mode can save an average of 39% to 47% of battery power. On a global scale, if every major app defaulted to dark mode, the reduction in grid demand would be astronomical. 
 The Design Goal 
 In 2026, Dark Mode should no longer be a secondary “theme” tucked away in a settings menu. We should be designing with a “Dark-First” mentality. This doesn’t mean every site must look like The Matrix , but it does mean prioritising high-contrast dark themes as the default system-preferred state. This extends the hardware lifespan of the device and lowers the carbon footprint of every interaction. 
 I personally prefer Light-Mode for reading, so it makes sense to have both light and dark mode options available. There are also accessibility considerations with providing both options. 
 Image And Video Optimisation We have become lazy designers. With high-speed 5G and fibre optics, we’ve stopped worrying about file sizes. The average mobile page weight has increased by over 500% in the last decade, largely due to unoptimized visual assets. 
 The Logic 
 The “Digital Fat” of a website (those 4MB Unsplash photos and 15MB background videos) is the single largest contributor to page-load energy. Every megabyte transferred from a server to a client requires electricity for the transmission, the server’s processing, and the user’s rendering engine. When we use massive files, we are essentially “burning” energy to show a picture that could have been just as effective at a fraction of the size. Not to mention, you are also providing a better user experience with a page that loads much faster. 
 The Data 
 According to the HTTP Archive , images and video consistently account for the lion’s share of a page’s total weight. However, the shift to modern formats like AVIF and WebP can reduce image weight by up to 50% compared to JPEG, without any perceptible loss in quality. 
 Although these formats are not as familiar to me as JPG and PNG, I am definitely looking forward to using them to reduce page size. 
 The Design Goal 
 I recently led a redesign for a cybersecurity platform. By implementing a “Before and After” audit, we discovered that their homepage was loading 5.5MB of data. By replacing high-res photography with SVG (Scalable Vector Graphics) art and using clever CSS gradients instead of image assets, we dropped the load to 1.2MB. That is a 78% reduction in energy load! As a designer, your first question should always be: 
 “Do I need a photo for this, or can I achieve the same emotional resonance with code?” 
 Intentional Motion: Cutting “Loud" Animations We live in an era of “ scroll-jacking ” and complex 3D Parallax effects. While these might win awards on Awwwards.com, they are often ecological disasters. 
 The Logic 
 Animation is not free. To render a complex animation, the device’s GPU (Graphics Processing Unit) must work at high capacity. This increases the CPU temperature , triggers cooling fans (in laptops), and drains battery rapidly. “Loud” animations that run constantly in the background or trigger massive re-paints of the browser are the energy equivalent of leaving your car idling in the driveway. 
 The Data 
 Google’s Material Design guidelines emphasize “ Meaningful Motion .” They argue that animation should be used only to orient the user or provide feedback. And using WebP instead of JPEG can save 25-50% of data on a page. 
 The Design Goal 
 We must adopt Meaningful Motion. If an animation doesn’t help a user complete a task or understand a hierarchy, it is a waste. We should favour CSS transitions over heavy JavaScript libraries like GSAP or Lottie where possible, as CSS is hardware-accelerated and far more efficient for the browser to calculate. 
 As a UX designer, I can’t argue this approach. This not only helps reduce data waste but also improves UX for our users. 
 Setting A “Data Budget” For Every Project In my 20+ years of UX, the most successful projects have generally been the ones with the tightest constraints. 
 Just as a project has a financial budget, it should also have a carbon and data budget. 
 The Logic 
 A Data Budget is a hard cap on the total size of a page (e.g., “This landing page cannot exceed 1MB”). This forces the design team to make difficult, intentional choices. If you want to add a new tracking script or a fancy font weight, you have to “pay” for it by optimising or removing something else. This prevents “feature creep” from turning into “carbon creep.” 
 The Data 
 The Sustainable Web Design model , developed by pioneers like Wholegrain Digital , provides a formula to calculate the CO2 per page view. The average website produces about 0.5 grams of CO2 per view. For a site with 1 million monthly views, that’s 6 metric tons of CO2 a year, equivalent to driving a car 15,000 miles. 
 The Design Goal 
 The Sustainable UX Checklist 
 Reduce Images 
 Question the necessity of every visual and use the smallest resolution and most efficient file formats (like AVIF) to minimize data transfer. 
 Optimise Video 
 Eliminate auto-playing media and prioritise highly compressed, short loops to ensure energy is only spent on content the user intends to view. 
 Limit Fonts 
 Use a maximum of two web font weights or stick to classic system fonts to remove unnecessary server requests and rendering bloat. 
 Recycle Assets 
 Repurpose a single image or video multiple times using CSS filters and overlays to create visual variety without increasing the total page weight. 
 Choose Green Hosting 
 Host your digital products on servers verified by The Green Web Foundation to ensure they are powered by renewable energy sources. 
 Minimize Data Distance 
 Select server locations geographically close to your primary audience to reduce the energy required for data to travel through physical infrastructure. 
 The Business Case For Eco-friendly Design Some might argue that “Green UX” sounds like a compromise on quality. On the contrary, it is a competitive advantage. Sustainable design is performance design. 
 When you reduce page weight, your site loads faster. When your site loads faster, your Core Web Vitals improve. When your Core Web Vitals improve, your SEO ranking goes up. Furthermore, users on older devices or slower data plans (especially in emerging markets) can actually access your product. This is the definition of “Inclusive Design.” 
 By cutting the “digital fat,” we create a leaner, faster, and more accessible web. We are moving away from the “disposable design” of the 2010s toward a more permanent, respectful digital architecture. 
 Conclusion: The Future Of “Clean” Design In my two decades of design, I’ve seen many trends come and go. Skeuomorphism, Flat Design, Neumorphism — they were all aesthetic choices. But sustainable UX isn’t a trend; it’s now a necessity. We are the first generation of designers who have to reckon with the physical consequences of our digital work. 
 Sustainable UX is a “win-win-win.” It’s better for the planet because it reduces energy consumption. It’s better for the user because it results in faster, more responsive interfaces. And it’s better for the business because it lowers hosting costs AND improves conversion rates. 
 The era of “unlimited pixels” is over. In 2026, the most sophisticated design is the one that leaves the smallest footprint. We are no longer just designers; we are the guardians of the user’s battery, their data plan, and ultimately, the environment. 
 The Call To Action I challenge you to audit just one page of your current project today. Use a tool like the Website Carbon Calculator to see its impact. Then, look for the “invisible waste.” Can that image be an SVG? Can that video be a static hero? Can that “loud” animation be silenced? 
 Start small. The most elegant solution is often the one with the fewest bytes.
```

---

## 26. Designing A Streak System: The UX And Psychology Of Streaks

- 日期: 2026-02-18 15:00
- 链接: https://smashingmagazine.com/2026/02/designing-streak-system-ux-psychology/

```
I’m sure you’ve heard of streaks or used an app with one. But ever wondered why streaks are so popular and powerful? Well, there is the obvious one that apps want as much of your attention as possible, but aside from that, did you know that when the popular learning app Duolingo introduced iOS widgets to display streaks, user commitment surged by 60% . Sixty percent is a massive shift in behaviour and demonstrates how “streak” patterns can be used to increase engagement and drive usage. 
 At its most basic, a streak is the number of consecutive days that a user completes a specific activity . Some people also define it as a “gamified” habit or a metric designed to encourage consistent usage. 
 But streaks transcend beyond being a metric or a record in an app; it is more psychological than that. Human instincts are easy to influence with the right factors. Look at these three factors: progress , pride , and fear of missing out (commonly called FOMO ). What do all these have in common? Effort . The more effort you put into something, the more it shapes your identity, and that is how streaks crosses into the world of behavioural psychology. 
 Now, with great power comes great responsibility, and because of that, there’s a dark side to streaks. 
 In this article, we’ll be going into the psychology, UX, and design principles behind building an effective streak system. We’ll look at (1) why our brains almost instinctively respond to streak activity, (2) how to design streaks in ways that genuinely help users, and (3) the technical work involved in building a streak pattern. 
 The Psychology Behind Streaks To design and build an effective streak system, we need to understand how it aligns with how our brains are wired. Like, what makes it so effective to the extent that we feel so much intense dedication to protect our streaks? 
 There are three interesting, well-documented psychology principles that support what makes streaks so powerful and addictive. 
 Loss Aversion 
 This is probably the strongest force behind streaks. I say this because most times, you almost can’t avoid this in life. 
 Think of it this way: If a friend gives you $100, you’d be happy. But if you lost $100 from your wallet, that would hurt way more. The emotional weight of those situations isn’t equal. Loss hurts way more than gain feels good. 
 Let’s take it further and say that I give you $100 and ask you to play a gamble. There’s a 50% chance you win another $100 and a 50% chance you lose the original $100. Would you take it? I wouldn’t. Most people wouldn’t. That’s loss aversion. 
 If you think about it, it is logical, it is understandable, it is human. 
 The concept behind loss aversion is that we feel the pain of losing something twice as much as the pleasure of gaining something of equal value. In psychological terms, loss lingers more than gains do. 
 You probably see how this relates to streaks. To build a noticeable streak, it requires effort; as a streak grows, the motivation behind it begins to fade; or more accurately, it starts to become secondary. 
 Here’s an example: Say your friend has a three-day streak closing their “Move Rings” on their Apple Watch . They have almost nothing to lose beyond wanting to achieve their goal and be consistent. At the same time, you have an impressive 219-day streak going. Chances are that you are trapped by the fear of losing it . You most likely aren’t thinking about the achievement at this point; it’s more about protecting your invested effort, and that is loss aversion. 
 Duolingo explains how loss aversion contributes to a user’s reluctance to break a long streak , even on their laziest days. In a way, a streak can turn into a habit when loss aversion settles in. 
 The Fogg Behaviour Model (B = MAP) 
 Now that we understand the fear of losing the effort invested in longer streaks, another question is: What makes us do the thing in the first place, day after day, even before the streak gets big? 
 That’s what the Fogg Behaviour Model is about. It is relatively simple. A behaviour (B) only occurs when three factors — Motivation (M), Ability (A), and Prompt (P) — align at the same moment. Thus, the equation B=MAP. 
 If any of these factors, even one, is missing at that moment, the behaviour won’t happen. 
 So, for a streak system to be efficient and recurring, all three factors must be present: 
 Motivation 
 This is fragile and not something that is consistently present. There are days when you’re pumped to learn Spanish, and days you don’t even feel an iota of willpower to learn the language. Motivation by itself to build a habit is unreliable and a losing battle from day one. 
 Ability 
 To compensate for the limitations of motivation, ability is critical. In this context, ability means the ease of action, i.e, the effort is so easy that it’s unrealistic to say it isn’t possible. Most apps intentionally use this. Apple Fitness just needs you to stand for one minute in an hour to earn a tick towards your Stand goal. Duolingo only needs one completed lesson. These tasks do not require all that much effort. The barrier is so low that even on your worst days, you can do it. But the combined effort of an ongoing streak is where the idea of losing that streak kicks in. 
 Prompt 
 This is what completes the equation. Humans are naturally forgetful, so yes, ability can get us 90% there. But a prompt reminds us to act. Streaks are persistent by design, so users need to be constantly reminded to act. To see how powerful a prompt can be, Duolingo did an A/B test to see if a little red badge on the app’s icon increased consistent usage. It produced a 6% increase in daily active users. Just a red badge. 
 Model Limitations 
 All this being said, there is a limitation to the Fogg model whereby critics and modern research have noticed that a design that relies too heavily on prompts, like aggressive notifications, risks creating mental fatigue. Constant notifications and overtime could cause users to churn. So, watch out for that. 
 The Zeigarnik Effect 
 How do you feel when you leave a task of project half-done? That irritates many people because unfinished tasks occupy more mental space than the things we complete. When something is done and gone, we tend to forget it. When something is left undone, it tends to weigh on our minds. 
 This is exactly why digital products use artificial progress indicators, like Upwork's profile completion bar, to let a user know that their profile is only “60% complete”. It nudges the user to finish what they started. 
 Let’s look at another example. You have five tasks in a to-do list app, and at the end of the day, you only check four of them as completed. Many of us will feel unaccomplished because of that one unfinished task. That, right there, is the Zeigarnik effect . 
 The Zeigarnik effect he was demonstrated by psychologist Bluma Zeigarnik, who described that we tend to keep incomplete tasks active in our memory longer than completed tasks. 
 A streak pattern naturally taps into this in UX design. Let’s say you are on day 63 of a learning streak. At that point, you’re in an ongoing pattern of unfinished business. Your brain would rarely forget about it as it sits in the back of your mind. At this point, your brain becomes the one sending you notifications. 
 When you put these psychological forces together, you begin to truly understand why streaks aren’t just a regular app feature; they are capable of reshaping human behaviour. 
 But somewhere along the line — I can’t say exactly when, as it differs for everyone — things reach a point where a streak shifts from “fun” to something you feel you can’t afford to lose. You don’t want 58 days of effort to go to waste, do you? That is what makes a streak system effective. If done right, streaks help users build astounding habits that accomplish a goal . It could be reading daily or hitting the gym consistently. 
 These repeated actions (sometimes small) compound over time and become evident in our daily lives. But there are two sides to every coin. 
 The Thin Line Between Habit And Compulsion If you have been following along, you can already tell there’s a dark side to streak systems. Habit formation is about consistency with a repeated goal. Compulsion, however, is the consistency of working on a goal that is no longer needed but held onto out of fear or pressure. It is a razor-thin line. 
 You brush your teeth every morning without thinking; it is automatic and instinctive, with a clear goal of having good breath. That’s a streak that forms a good habit. An ethical streak system gives users space to breathe. If, for some reason, you don’t brush in the morning, you can brush at noon. Imperfection is allowed without fear of losing a long effort. 
 Compulsion takes the opposite route, whereby a streak makes you anxious, you feel guilty or even exhausted, and sometimes, it feels like you haven’t accomplished anything, despite all your work. You act not because you want to, but because you’re subconsciously terrified of seeing your progress reset to zero. 
 Someone even described this perfectly, “ I felt that I was cheating, but simply did not care. I am nothing without my streak ”. This shows the extreme hold streaks can have on an individual. To the extent that users begin to tie their self-worth to an arbitrary metric rather than the original goal or reason they started the streak in the first place. The streak becomes who they are, not just what they do. 
 A well-designed ethical streak system should feel like encouragement to the user, not pressure or obligation. This relates to the balance of intrinsic and extrinsic motivation. Extrinsic motivation (external rewards, avoiding punishment) might get users started, but intrinsic motivation (doing the task for a personal goal like learning Spanish because you genuinely want to communicate with a loved one) is stronger for long-term engagement. 
 A good system should gravitate towards intrinsic motivation with careful use of extrinsic elements, i.e., remind users of how far they have come, not threaten them with what they might lose. Again, it is a fine line. 
 A simple test when designing a streak system is to actually take some time and think whether your products make money by selling solutions to anxiety that your product created. If yes, there’s a high chance you are exploiting users. 
 So the next question becomes, If I choose to use streak, how do I design it in a way that genuinely helps users achieve their goals? 
 The UX of Good Streak System Design 
 I believe this is where most projects either nail an effective streak system or completely mess it up. Let’s go through some UX principles of a good streak design. 
 Keep It Effortless 
 You’ve probably heard this before, maybe from books like Atomic Habits , but it’s worth mentioning that one of the easiest ways habits can be formed is by making the action tiny and easy. This is similar to the ability factor we discussed from the Fogg Behaviour Model. 
 The first rule of any streak design should be making the required action as small as humanly possible while still achieving progress. 
 If a daily action requires willpower to complete, that action won’t make it past five days. Why? You can’t be motivated five days in a row. 
 Case in point: If you run a meditation app, you don’t need to make users go through a 20-minute session just to maintain the streak. Try a single minute, maybe even something as small as thirty seconds, instead. 
 As the saying goes, little drops of water make the mighty ocean ). Small efforts compile into big achievements with time. That should be the goal: remove friction, especially when the moment might be difficult. When users are stressed or overwhelmed, let them know that simply showing up, even for a few seconds, counts as effort. 
 Provide Clear Visual Feedback 
 Humans are visual by nature. Most times, we need to see something to believe; there’s this need to visualize things to understand them better and put things into perspective. 
 This is why streak patterns often use visual elements, like graphs, checkmarks, progress rings, and grids, to visualize effort. Look at GitHub’s contribution graph. It is a simple visualization of consistency. Yet developers breathe it in like oxygen. 
 The key is not to make a streak system feel abstract. It should feel real and earned. For instance, Duolingo and Apple’s Fitness activity rings use clean animation designs on completion of a streak, and GitHub shows historical data of a user’s consistency over time. 
 Use Good Timing 
 I mentioned earlierthat humans are generally forgetful by nature, and that prompts can help maintain forward momentum. Without prompts, most new users forget to keep going. Life can get busy, motivation disappears, and things happen. Even long-time users benefit from prompts, though most times, they are already locked inside the habit loop. Nevertheless, even the most committed person can accidentally miss a day. 
 Your streak system most definitely needs reminders. The most-used prompt reminders are push notifications . Timing really matters when working with push notifications. The type of app matters, too. Sending a notification at 9 a.m. saying “You haven’t practiced today” is just weird for a learning app because many have things to do in the day before they even think about completing a lesson. If we’re talking about a fitness app, though, it is reasonable and maybe even expected to be reminded earlier in the day. 
 Push notifications vary significantly by app category . Fitness apps, for instance, see higher engagement with early morning notifications (7–8 AM), while productivity apps might perform better in early noon. The key is to A/B test your app’s timing based on your users' behaviours rather than assuming things are one-size-fits-all. What works for a meditation app might not work for a coding tracker. 
 Other prompt methods are red dots on the app icon and even app widgets. Studies vary, but the average person unlocks their device between 50-150 times a day (PDF). If a user sees a red dot on an app or a widget that indicates a current streak every time they unlock their phone, it increases commitment. 
 Just don’t overdo it; the prompt should serve as a reminder, not a nag. 
 Celebrate Milestones 
 A streak system should try to celebrate milestones to reignite emotions, especially for users deep into a streak. 
 When a user hits Day 7, Day 30, Day 50, Day 100, Day 365, you should make a big deal out of it. Acknowledge achievements — especially for long-time users. 
 As we saw earlier, Duolingo figured this out and implemented an animated graphic that celebrates milestones with confetti. Some platforms even give substantial bonus rewards that validate users’ efforts. And this can be beneficial to apps, such that users tend to share their milestones publicly on social media. 
 Another benefit is the anticipation that comes before reaching milestones. It isn’t just keeping the streak alive endlessly; users have something to look forward to. 
 Use Grace Mechanisms 
 Life is unpredictable. People get distracted. Any good streak system should expect imperfection. One of the biggest psychological threats to a streak system is the hard reset to zero after just a single missed day. 
 An “ethical” streak system should provide the user with some slack. Let’s say you have a 90-day chess learning streak. You have been consistent for three good months, and one day, your phone dies while traveling, and just like that, 90 becomes 0 — everything, all that effort, is erased, and progress vanishes. The user might be completely devastated. The thought of rebuilding it from scratch is so demoralizing that the effort isn’t worth it. At worst, a user might abandon the app after feeling like a failure. 
 Consider adding a “grace” mechanism to your streak system: 
 Streak Freeze 
 Allow users to intentionally miss a day without penalties. 
 Extra Time 
 Allow a few hours (2–3) past the usual deadline before triggering a reset. 
 Decay Models 
 Instead of a hard reset, the streak decreases by a small amount, e.g., 10 days is deducted from the streak per missed day. 
 Use An Encouraging Tone 
 Let’s compare two messages shown to users when a streak breaks: 
 “You lost your 42-day streak. Start over.” 
 “You showed up for 42 days straight. That’s incredible progress! Wanna give it another try?” 
 Both convey the same information, but the emotional impact is different. The first message would most likely make a user feel demoralized and cause them to quit. The second message celebrates what has already been achieved and gently encourages the user to try again. 
 Streak Systems Design Challenges Before we go into the technical specifics of building a streak system, you should be aware of the challenges that you might face. Things can get complicated, as you might expect. 
 Handling Timezones 
 There is a reason why handling time and date is among the most difficult concepts developers deal with. There’s formatting, internationalization, and much more to consider. 
 Let me ask you this: What counts as a day? 
 We know the world runs on different time zones, and as if that is not enough, some regions have Daylight Saving Time (DST) that happens twice a year. Where do you even begin handling these edge cases? What counts as the “start” of tomorrow? 
 Some developers try to avoid this by using one central timezone, like UTC. For some users, this would yield correct results, but for some, it could be off by an hour, two hours, or more. This inconsistency ruins the user experience. Users care less how you handle the time behind the scenes; all they expect is that if they perform a streak action at 11:40 p.m., then it should register at that exact time, in their context. You should define “one day” based on the user’s local timezone, not the server time. 
 Sure, you can take the easy route and reset streaks globally for all users at midnight UTC, but you are very much creating unfairness. Someone in California always has eight extra hours to complete their task than someone living in London. That’s an unjust design flaw that punishes certain users because of their location. And what if that person in London is only visiting, completes a task, then returns to another timezone? 
 One effective solution to all these is to ask users to explicitly set their timezone during onboarding (preferably after first authentication). It’s a good idea to include a subtle note that providing timezone information is only used for the app to accurately track progress, rather than being used as personally identifiable data. And it’s another good idea to make that a changeable setting. 
 I suggest that anyone avoid directly handling timezone logic in an app. Use tried-and-true date libraries, like Moment.js or pytz (Python), etc. There’s no need to reinvent the wheel for something as complex as this. 
 Missed Days And Edge Cases 
 Another challenge you should worry about is uncontrollable edge cases like users oversleeping, server downtime, lag, network failures, and so on. Using the idea of grace mechanisms , like the ones we discussed earlier, can help. 
 A grace window of two hours might help both user and developer, in the sense that users are not rigidly punished for uncontrollable life circumstances. For developers, grace windows are helpful in those uncontrollable moments when the server goes down in the middle of the night. 
 Above all, never trust the client. Always validate on the server-side. The server should be the single source of truth. 
 Cheating Prevention 
 Again, I cannot stress this enough: Make sure to validate everything server-side. Users are humans, and humans might cheat if given the opportunity. It is unavoidable. 
 You might try: 
 Storing all actions with UTC timestamps. 
 The client can send their local time, but the server can immediately convert that to UTC and validate against the server time. That way, if the client's timestamp is suspiciously far, the system can reject it as an error, and the UI can respond accordingly. 
 Using event-based tracking. 
 In other words, store a record of each action with metadata including information like the user’s ID, the type of action performed, and the timestamp and timezone. This helps with validation. 
 Building A Streak System Engine This isn’t a code tutorial, so I will avoid dumping a bunch of code on you. I’ll keep this practical and describe how things generally operate a streak system engine as far as architecture, flow, and reliability. 
 Core Architecture 
 As I’ve said several times, make the serverthe single source of truth for streak data. The architecture can go something like this on the server: 
 Store each user’s data in a database. 
 Store the current streak store (default as 0) as an integer. 
 Store the timezone preference, i.e., IANA Timezone string (either implicitly from local timestamp or explicitly by asking user to select their timezone). For example, “America/New_York”. 
 Handle all logic to determine if the streak continues or breaks, with a timezone check that is relative to the user’s local timezone. 
 Meanwhile, on the client-side: 
 Display the current streak, normally fetched from the server. 
 Send action done in the form of metadata to the server to validate whether the user actually completed a qualifying streak action. 
 Provide visual feedback based on the server responses. 
 So, in short, the brain is on the server, and the client is for display purposes and submitting events. This saves you a lot of failures and edge cases, plus makes updates and fixes easier. 
 The Logical Flow 
 Let’s simulate a walkthrough of how a minimal efficient streak system engine would go when a user completes an action: 
 The user completes a qualifying streak action. 
 The client sends an event to the server as metadata. This could be “User X completed action Y at timestamp Z”. 
 The server receives this event and does basic validation. Is this a real user? Are they authenticated? Is the action valid? Is the timezone consistent? 
 If this passes, the server retrieves the user’s streak data from the database. 
 Then, convert the received action timestamp to the user’s local timezone. 
 Let the server compare the calendar dates (not timestamps) in the user's local timezone: If it is the same day, then the action is redundant and there is no change in the streak. 
 If it is the next day, then the streak extends and increments by 1. 
 If there is a gap of more than one day, the streak breaks. However, this is where you might apply grace mechanics. 
 If the grace mechanism is missed, then reset the streak to 1. 
 If you choose to save historical data for milestone achievements, then update variables like “longest streak” or “total active days”. 
 The server then updates the database and responds to the client. Something like this: 
 {
 "current_streak": 48,
 "longest_streak": 50,
 "total_active_days": 120,
 "streak_extended": true,
} As a further measure, the server should either retry or reject and notify the client when anything fails during the process. 
 Building For Resilience 
 As mentioned before, users losing a streak due to bugs or server downtime is terrible UX, and users don’t expect to take the fall for it. Thus, your streak system should have safeguards for those scenarios. 
 If the server is down for maintenance (or whatever reason), consider allowing a temporary window of additional hours to get it fixed so actions can be submitted late and still count. You can also choose to notify users, especially if the situation is capable of affecting an ongoing streak. 
 Note : Establish an admin backdoor where data can be manually restored. Bugs are inevitable, and some users would call your app out or reach out to support that their streak broke for a reason they could not control. You should be able to manually restore the streaks if, after investigation, the user is right. 
 Conclusion One thing remains clear: Streaks are really powerful because of how human psychology works on a fundamental level. 
 The best streak system out there is the one that users don’t think about consciously. It has become a routine of immediate results or visible progress, like brushing teeth, which becomes a regular habit. 
 And I’m just gonna say it: Not all products need a streak system. Should you really force consistency just because you want daily active users? The answer may very well be “no”.
```

---

## 27. Building Digital Trust: An Empathy-Centred UX Framework For Mental Health Apps

- 日期: 2026-02-13 15:00
- 链接: https://smashingmagazine.com/2026/02/building-empathy-centred-ux-framework-mental-health-apps/

```
Imagine a user opening a mental health app while feeling overwhelmed with anxiety. The very first thing they encounter is a screen with a bright, clashing colour scheme, followed by a notification shaming them for breaking a 5-day “mindfulness streak,” and a paywall blocking the meditation they desperately need at that very moment. This experience isn’t just poor design; it can be actively harmful. It betrays the user’s vulnerability and erodes the very trust the app aims to build. 
 When designing for mental health, this becomes both a critical challenge and a valuable opportunity. Unlike a utility or entertainment app, the user’s emotional state cannot be treated as a secondary context. It is the environment your product operates in. 
 With over a billion people living with mental health conditions and persistent gaps in access to care, safe and evidence-aligned digital support is increasingly relevant. The margin for error is negligible. Empathy-Centred UX becomes not a “nice to have” but a fundamental design requirement. It is an approach that moves beyond mere functionality to deeply understand, respect, and design for the user’s intimate emotional and psychological needs. 
 But how do we translate this principle into practice? How do we build digital products that are not just useful, but truly trustworthy? 
 Throughout my career as a product designer, I’ve found that trust is built by consistently meeting the user’s emotional needs at every stage of their journey. In this article, I will translate these insights into a hands-on empathy-centred UX framework . We will move beyond theory to dive deeper into applicable tools that help create experiences that are both humane and highly effective. 
 In this article, I’ll share a practical, repeatable framework built around three pillars: 
 Onboarding as a supportive first conversation. 
 Interface design for a brain in distress. 
 Retention patterns that deepen trust rather than pressure users. 
 Together, these pillars offer a grounded way to design mental health experiences that prioritise trust, emotional safety, and real user needs at every step. 
 The Onboarding Conversation: From a Checklist to a Trusted Companion Onboarding is “a first date” between a user and the app — and the first impression carries immense stakes, determining whether the user decides to continue engaging with the app. In mental health tech, with up to 20,000 mental-health-related apps on the market, product designers face a dilemma of how to integrate onboarding’s primary goals without making the design feel too clinical or dismissive for a user seeking help. 
 The Empathy Tool 
 In my experience, I have found it essential to design onboarding as the first supportive conversation. The goal is to help the user feel seen and understood by delivering a small dose of relief quickly, not just overload them with data and the app’s features. 
 Case Study: A Teenager’s Parenting Journey 
 At Teeni , an app for parents of teenagers, onboarding requires an approach that solves two problems: (1) acknowledge the emotional load of parenting teens and show how the app can share that load; (2) collect just enough information to make the first feed relevant. 
 Recognition And Relief 
 Interviews surfaced a recurring feeling among parents: “I’m a bad parent, I’ve failed at everything.” My design idea was to provide early relief and normalisation through a city-at-night metaphor with lit windows: directly after the welcome page, a user engages with three brief, animated and optional stories based on frequent challenges of teenage parenting, in which they can recognise themselves (e.g., a story of a mother learning to manage her reaction to her teen rolling their eyes). This narrative approach reassures parents that they are not alone in their struggles, normalising and helping them cope with stress and other complex emotions from the very beginning. 
 Note: Early usability sessions indicated strong emotional resonance, but post-launch analytics showed that the optionality of the storytelling must be explicit. The goal is to balance the storytelling to avoid overwhelming the distressed parent, directly acknowledging their reality: “Parenting is tough. You’re not alone.” 
 Progressive Profiling 
 To tailor guidance to each family, we defined the minimal data needed for personalisation. On the first run, we collect only the essentials for a basic setup (e.g., parent role, number of teens, and each teen’s age). Additional, yet still important, details (specific challenges, wishes, requests) are gathered gradually as users progress through the app, avoiding long forms for those who need support immediately. 
 The entire onboarding is centred around a consistently supportive choice of words, turning a typically highly practical, functional process into a way to connect with the vulnerable user on a deeper emotional level, while keeping an explicit fast path. 
 Your Toolbox 
 Use Validating Language 
 Start with “It’s okay to feel this way,” not “Allow notifications.” 
 Understand “Why”, not just “What” 
 Collect only what you’ll use now and defer the rest via progressive profiling. Use simple, goal-focused questions to personalise users’ experience. 
 Prioritise Brevity and Respect 
 Keep onboarding skimmable, make optionality explicit, and let user testing define the minimum effective length &mdashl the shorter is usually the better. 
 Keep an Eye on Feedback and Iterate 
 Track time-to-first-value and step drop-offs; pair these with quick usability sessions, then adjust based on what you learn. 
 This initial conversation sets the stage for trust. But this trust is fragile. The next step is to ensure the app’s very environment doesn’t break it. 
 The Emotional Interface: Maintaining Trust In A Safe Environment A user experiencing anxiety or depression often shows reduced cognitive capacity, which affects their attention span and the speed with which they process information and lowers tolerance for dense layouts and fast, highly stimulating visuals. This means that high-saturation palettes, abrupt contrast changes, flashing, and dense text can feel overwhelming for them. 
 The Empathy Tool 
 When designing a user flow for a mental health app, I always apply the Web Content Accessibility Guidelines 2.2 as a foundational baseline. On top of that, I choose a “low-stimulus” , “familiar and safe” visual language to minimise the user’s cognitive load and create a calm, predictable, and personalised environment. Where appropriate, I add subtle, opt-in haptics and gentle micro-interactions for sensory grounding, and offer voice features as an option in high-stress moments (alongside low-effort tap flows) to enhance accessibility. 
 Imagine you need to guide your users “by the hand”: we want to make sure their experience is as effortless as possible, and they are quickly guided to the support they need, so we avoid complicated forms and long wordings. 
 Case: Digital Safe Space 
 For the app focused on instant stress relief, Bear Room , I tested a “cosy room” design. My initial hypothesis was validated through a critical series of user interviews: the prevailing design language of many mental health apps appeared misaligned with the needs of our audience. Participants grappling with conditions such as PTSD and depression repeatedly described competing apps as “too bright, too happy, and too overwhelming,” which only intensified their sense of alienation instead of providing solace. This suggested a mismatch for our segment, which instead sought a sense of safety in the digital environment. 
 This feedback informed a low-arousal design strategy. Rather than treating “safe space” as a visual theme, we approached it as a holistic sensory experience . The resulting interface is a direct antithesis to digital overload; it gently guides the user through the flow, keeping in mind that they are likely in a state where they lack the capacity to concentrate. The text is divided into smaller parts and is easily scannable and quickly defined. The emotional support tools — such as a pillow — are highlighted on purpose for convenience. 
 The interface employs a carefully curated, non-neon, earthy palette that feels grounding rather than stimulating, and it rigorously eliminates any sudden animations or jarring bright alerts that could trigger a stress response. This deliberate calmness is not an aesthetic afterthought but the app’s most critical feature, establishing a foundational sense of digital safety . 
 To foster a sense of personal connection and psychological ownership, the room introduces three opt-in “personal objects”: Mirror, Letter, and Frame. Each invites a small, successful act of contribution (e.g., leaving a short message to one’s future self or curating a set of personally meaningful photos), drawing on the IKEA effect (PDF). 
 For instance, Frame functions as a personal archive of comforting photo albums that users can revisit when they need warmth or reassurance. Because Frame is represented in the digital room as a picture frame on the wall, I designed an optional layer of customisation to deepen this connection: users can replace the placeholder with an image from their collection — a loved one, a pet, or a favourite landscape — displayed in the room each time they open the app. This choice is voluntary, lightweight, and reversible, intended to help the space feel more “mine” and deepen attachment without increasing cognitive load. 
 Note: Always adapt to the context. Try to avoid making the colour palette too pastel. It is useful to balance the brightness based on the user research, to protect the right level of the app’s contrast. 
 Case: Emotional Bubbles 
 In Food for Mood , I used a visual metaphor: coloured bubbles representing goals and emotional states (e.g., a dense red bubble for “Performance”). This allows users to externalise and visualise complex feelings without the cognitive burden of finding the right words. It’s a UI that speaks the language of emotion directly. 
 In an informal field test with young professionals (the target audience) in a co-working space, participants tried three interactive prototypes and rated each on simplicity and enjoyment. The standard card layout scored higher on simplicity, but the bubble carousel scored better on engagement and positive affect — and became the preferred option for the first iteration. Given that the simplicity trade-off was minimal (4/5 vs. 5/5) and limited to the first few seconds of use, I prioritised the concept that made the experience feel more emotionally rewarding. 
 Case: Micro-interactions And Sensory Grounding 
 Adding a touch of tactile micro-interactions like bubble-wrap popping in Bear Room , may also offer users moments of kinetic relief. Integrating deliberate, tactile micro-interactions, such as the satisfying bubble-wrap popping mechanic, provides a focused act that can help an overwhelmed user feel more grounded. It offers a moment of pure, sensory distraction for a person stuck in a torrent of stressful thoughts. This isn’t about gamification in the traditional, points-driven sense; it’s about offering a controlled, sensory interruption to the cycle of anxiety . 
 Note: Make tactile effects opt-in and predictable. Unexpected sensory feedback can increase arousal rather than reduce it for some users. 
 Case: Voice Assistants 
 When a user is in a state of high anxiety or depression, it can become an extra effort for them to type something in the app or make choices. In moments when attention is impaired, and a simple, low-cognitive choice (e.g., ≤4 clearly labelled options) isn’t enough, voice input can offer a lower-friction way to engage and communicate empathy. 
 In both Teeni and Bear Room , voice was integrated as a primary path for flows related to fatigue, emotional overwhelm, and acute stress — always alongside a text input alternative. Simply putting feelings into words (affect labelling) has been shown to reduce emotional intensity for some users, and spoken input also provides a richer context for tailoring support. 
 For Bear Room , we give users a choice to share what’s on their mind via a prominent mic button (with text input available below. The app then analyses their response with AI (does not diagnose) and provides a set of tailored practices to help them cope. This approach gives users a space for the raw, unfiltered expression of emotion when texting feels too heavy. 
 Similarly, Teeni’s “Hot flow” lets parents vent frustration and describe a difficult trigger via voice. Based on the case description, AI gives a one-screen piece of psychoeducational content, and in a few steps, the app suggests an appropriate calming tool, uniting both emotional and relational support. 
 By meeting the user at their level of low cognitive capacity and accepting their input in the most accessible form, we build a deeper trust and reinforce the app as a truly adaptive, reliable, and non-judgmental space. 
 Note: Mental-health topics are highly sensitive, and many people feel uncomfortable sharing sensitive data with an app — especially amid frequent news about data breaches and data being sold to third parties. Before recording, show a concise notice that explains how audio is processed, where it’s processed, how long it’s stored, and that it is not sold or shared with third parties. Present this in a clear, consent step (e.g., GDPR-style). For products handling personal data, it’s also best practice to provide an obvious “Delete all data” option. 
 Your Toolbox 
 Accessibility-Friendly User Flow 
 Aim to become your user’s guide. Only use the text that is important, highlight key actions, and provide simple, step-by-step paths. 
 Muted Palettes 
 There’s no one-size-fits-all colour rule for mental-health apps. Align palette with purpose and audience; if you use muted palettes, verify WCAG 2.2 contrast thresholds and avoid flashing. 
 Tactile Micro-interactions 
 Use subtle, predictable, opt-in haptics and gentle micro-interactions for moments of kinetic relief. 
 Voice-First Design 
 Offer voice input as an alternative to typing or single-tap actions in low-energy/high-pressure states 
 Subtle Personalisation 
 Integrate small, voluntary customisations (like a personal photo in a digital frame) to foster a stronger emotional bond. 
 Privacy by Default 
 Ask for explicit consent to process personal data. State clearly how, where, and for how long data is processed, and that it’s not sold or shared — and honour it. 
 A safe interface builds trust in the moment. The final pillar is about earning the trust that brings users back, day after day. 
 The Retention Engine: Deepening Trust Through Genuine Connection Encouraging consistent use without manipulation often requires innovative solutions in mental health. The app, as a business, faces an ethical dilemma: its mission is to prioritise user wellbeing, which means it cannot indulge users simply to maximise their screen time. Streaks, points, and time limits can also induce anxiety and shame, negatively affecting the user’s mental health. The goal is not to maximise screen time, but to foster a supportive rhythm of use that aligns with the non-linear journey of mental health. 
 The Empathy Tool 
 I replace anxiety-inducing gamification with retention engines powered by empathy. This involves designing loops that intrinsically motivate users through three core pillars: granting them agency with customisable tools, connecting them to a supportive community , and ensuring the app itself acts as a consistent source of support , making return visits feel like a choice, not a chore or pressure. 
 Case: “Key” Economy 
 In search of reimagining retention mechanics away from punitive streaks and towards a model of compassionate encouragement, the Bear Room team came up with the idea of the so-called “Key” economy. Unlike a streak that shames users for missing a day, users are envisioned to earn “keys” for logging in every third day — a rhythm that acknowledges the non-linear nature of healing and reduces the pressure of daily performance. Keys never gate SOS sets or essential coping practices. Keys only unlock more objects and advanced content; the core toolkit is always free. The app should also preserve users’ progress regardless of their level of engagement. 
 The system’s most empathetic innovation, however, lies in the ability for users to gift their hard-earned keys to others in the community who may be in greater need (still in the process of making). This intends to transform the act of retention from a self-focused chore into a generous, community-building gesture. 
 It aims to foster a culture of mutual support , where consistent engagement is not about maintaining a personal score, but about accumulating the capacity to help others. 
 Why it Works 
 It’s Forgiving. 
 Unlike a streak, missing a day doesn’t reset progress; it just delays the next key. This removes shame. 
 It’s Community-driven. 
 Users can give their keys to others . This transforms retention from a selfish act into a generous one, reinforcing the app’s core value of community support. 
 Case: The Letter Exchange 
 Within Bear Room , users can write and receive supportive letters anonymously to other users around the world. This tool leverages AI-powered anonymity to create a safe space for radical vulnerability. It provides a real human connection while completely protecting user privacy, directly addressing the trust deficit. It shows users they are not alone in their struggles, a powerful retention driver. 
 Note: Data privacy is always a priority in product design, but (again) it’s crucial to approach it firsthand in mental health. In the case of the letter exchange, robust anonymity isn’t just a setting; it is the foundational element that creates the safety required for users to be vulnerable and supportive with strangers. 
 Case: Teenager Translator 
 The “Teenager Translator” in Teeni became a cornerstone of our retention strategy by directly addressing the moment of crisis where parents were most likely to disengage. When a parent inputs their adolescent’s angry words like “What’s wrong with you? It’s my phone, I will watch what I want, just leave me alone!” , the tool instantly provides an empathetic translation of the emotional subtext, a de-escalation guide, and a practical script for how to respond. 
 This immediate, actionable support at the peak of frustration transforms the app from a passive resource into an indispensable crisis-management tool . By delivering profound value exactly when and where users need it most, it creates powerful positive reinforcement that builds habit and loyalty , ensuring parents return to the app not just to learn, but to actively navigate their most challenging moments. 
 Your Toolbox 
 Reframe Metrics 
 Change “You broke your 7-day streak!” to “You’ve practiced 5 of the last 10 days. Every bit helps.” 
 Compassion Access Policy 
 Never gate crisis or core coping tools behind paywalls or keys. 
 Build Community Safely 
 Facilitate anonymous, moderated peer support. 
 Offer Choice 
 Let users control the frequency and type of reminders. 
 Keep an Eye on Reviews 
 Monitor app-store reviews and social mentions regularly; tag themes (bugs, UX friction, feature requests), quantify trends, and close the loop with quick fixes or clarifying updates. 
 Your Empathy-First Launchpad: Three Pillars To Trust Let’s return to the overwhelmed user from the introduction. They open an app that greets them with a tested, audience-aligned visual language, a validating first message, and a retention system that supports rather than punishes. 
 This is the power of an Empathy-Centred UX Framework . It forces us to move beyond pixels and workflows to the heart of the user experience: emotional safety. But to embed this philosophy in design processes, we need a structured, scalable approach. My designer path led me to the following three core pillars: 
 The Onboarding Conversation 
 Start by transforming the initial setup from a functional checklist into the first supportive, therapy-informed dialogue. This pillar is rooted in using validating language, keeping asking “why” to understand deeper needs, and prioritising brevity and respect to make the user feel seen and understood from their very first interactions. 
 The Emotional Interface 
 Adjust the design to a low-stimulus digital environment for a brain in distress. This pillar focuses on the visual and interactive tools: muted palettes, calming micro-interactions, voice-first features, and personalisation, to make sure a user enters a calm, predictable, and safe digital environment. Certainly, these tools are not limited to the ones I applied throughout my experience, and there is always room for creativity, keeping in mind users’ preferences and scientific research. 
 The Retention Engine 
 Be persistent in upholding genuine connection over manipulative gamification. This pillar focuses on building lasting engagement through forgiving systems (like the “Key” economy), community-driven support (like letter exchanges), and tools that offer profound value in moments of crisis (like the Teenager Translator). When creating such tools, aim for a supportive rhythm of use that aligns with the non-linear journey of mental health. 
 Trust Is The Success: Balancing Game While we, as designers, don’t directly define the app’s success metrics, we cannot deny that our work influences the final outcomes. This is where our practical tools in mental health apps may come in partnership with the product owner’s goals. All the tools are designed based on hypotheses, evaluations of whether users need them, further testing, and metric analysis. 
 I would argue that one of the most critical success components for a mental health app is trust . Although it is not easy to measure, our role as designers lies precisely in creating a UX Framework that respects and listens to its users and makes the app fully accessible and inclusive . 
 The trick is to achieve a sustainable balance between helping users reach their wellness goals and the gaming effect , so they also benefit from the process and atmosphere. It is a blend of enjoyment from the process and fulfillment from the health benefits, where we want to make a routine meditation exercise something pleasant. Our role as product designers is to always keep in mind that the end goal for the user is to achieve a positive psychological effect, not to remain in a perpetual gaming loop. 
 Of course, we need to keep in mind that the more responsibility the app takes for its users’ health, the more requirements there arise for its design. 
 When this balance is struck, the result is more than just better metrics; it’s a profound positive impact on your users’ lives. In the end, empowering a user’s well-being is the highest achievement our craft can aspire to.
```

---

## 28. Designing For Agentic AI: Practical UX Patterns For Control, Consent, And Accountability

- 日期: 2026-02-11 13:00
- 链接: https://smashingmagazine.com/2026/02/designing-agentic-ai-practical-ux-patterns/

```
In the first part of this series , we established the fundamental shift from generative to agentic artificial intelligence. We explored why this leap from suggesting to acting demands a new psychological and methodological toolkit for UX researchers, product managers, and leaders. We defined a taxonomy of agentic behaviors, from suggesting to acting autonomously, outlined the essential research methods, defined the risks of agentic sludge, and established the accountability metrics required to navigate this new territory. We covered the what and the why . 
 Now, we move from the foundational to the functional. This article provides the how : the concrete design patterns, operational frameworks, and organizational practices essential for building agentic systems that are not only powerful but also transparent , controllable , and worthy of user trust . If our research is the diagnostic tool, these patterns are the treatment plan . They are the practical mechanisms through which we can give users a palpable sense of control, even as we grant AI unprecedented autonomy. The goal is to create an experience where autonomy feels like a privilege granted by the user, not a right seized by the system. 
 Core UX Patterns For Agentic Systems Designing for agentic AI is designing for a relationship . This relationship, like any successful partnership, must be built on clear communication, mutual understanding, and established boundaries. 
 To manage the shift from suggestion to action, we utilize six patterns that follow the functional lifecycle of an agentic interaction: 
 Pre-Action (Establishing Intent) 
 The Intent Preview and Autonomy Dial ensure the user defines the plan and the agent’s boundaries before anything happens. 
 In-Action (Providing Context) 
 The Explainable Rationale and Confidence Signal maintain transparency while the agent works, showing the “why” and “how certain.” 
 Post-Action (Safety and Recovery) 
 The Action Audit & Undo and Escalation Pathway provide a safety net for errors or high-ambiguity moments. 
 Below, we will cover each pattern in detail, including recommendations for metrics for success. These targets are representative benchmarks based on industry standards; adjust them based on your specific domain risk. 
 1. The Intent Preview: Clarifying the What and How 
 This pattern is the conversational equivalent of saying, “Here’s what I’m about to do. Are you okay with that?” It’s the foundational moment of seeking consent in the user-agent relationship. 
 Before an agent takes any significant action, the user must have a clear, unambiguous understanding of what is about to happen. The Intent Preview, or Plan Summary, establishes informed consent. It is the conversational pause before action, transforming a black box of autonomous processes into a transparent, reviewable plan. 
 Psychological Underpinning 
 Presenting a plan before action reduces cognitive load and eliminates surprise, giving users a moment to verify the agent truly understands their intent. 
 Anatomy of an Effective Intent Preview: 
 Clarity and Conciseness 
 The preview must be immediately digestible. It should summarize the primary actions and outcomes in plain language, avoiding technical jargon. For instance, instead of “Executing API call to cancel_booking(id: 4A7B),” it should state, “Cancel flight AA123 to San Francisco.” 
 Sequential Steps 
 For multi-step operations, the preview should outline the key phases. This reveals the agent’s logic and allows users to spot potential issues in the proposed sequence. 
 Clear User Actions 
 The preview is a decision point, not just a notification. It must be accompanied by a clear set of choices. It’s a moment of intentional friction, a ‘speed bump’ in the process designed to ensure the user is making a conscious choice, particularly for irreversible or high-stakes actions. 
 Let’s revisit our travel assistant scenario from the first part of this series . We use this proactive assistant to illustrate how an agent handles a flight cancellation. The agent has detected a flight cancellation and has formulated a recovery plan. 
 The Intent Preview would look something like this: 
 Proposed Plan for Your Trip Disruption 
 I’ve detected that your 10:05 AM flight has been canceled. Here’s what I plan to do: Cancel Flight UA456 
 Process refund and confirm cancellation details. 
 Rebook on Flight DL789 
 Book a confirmed seat on a 2:30 PM non-stop flight, as this is the next available non-stop flight with a confirmed seat. 
 Update Hotel Reservation 
 Notify the Marriott that you will be arriving late. 
 Email Updated Itinerary 
 Send the new flight and hotel details to you and your assistant, Jane Doe. 
 [ Proceed with this Plan ] [ Edit Plan ] [ Handle it Myself ] 
 This preview is effective because it provides a complete picture, from cancellation to communication, and offers three distinct paths forward: full consent (Proceed), a desire for modification (Edit Plan), or a full override (Handle it Myself). This multifaceted control is the bedrock of trust. 
 When to Prioritize This Pattern 
 This pattern is non-negotiable for any action that is irreversible (e.g., deleting user data), involves a financial transaction of any amount, shares information with other people or systems, or makes a significant change that a user cannot easily undo. 
 Risk of Omission 
 Without this, users feel ambushed by the agent’s actions and will disable the feature to regain control. 
 Metrics for Success: 
 Acceptance Ratio 
 Plans Accepted Without Edit / Total Plans Displayed. Target > 85%. 
 Override Frequency 
 Total Handle it Myself Clicks / Total Plans Displayed. A rate > 10% triggers a model review. 
 Recall Accuracy 
 Percentage of test participants who can correctly list the plan’s steps 10 seconds after the preview is hidden. 
 Applying This to High-Stakes Domains 
 While travel plans are a relatable baseline, this pattern becomes indispensable in complex, high-stakes environments where an error results in more than an inconvenience for an individual traveling. Many of us work in settings where wrong decisions may result in a system outage, putting a patient’s safety at risk, or numerous other catastrophic outcomes that unreliable technology would introduce. 
 Consider a DevOps Release Agent tasked with managing cloud infrastructure. In this context, the Intent Preview acts as a safety barrier against accidental downtime. 
 In this interface, the specific terminology (Drain Traffic, Rollback) replaces generalities, and the actions are binary and impactful. The user authorizes a major operational shift based on the agent’s logic, rather than approving a suggestion. 
 2. The Autonomy Dial: Calibrating Trust With Progressive Authorization 
 Every healthy relationship has boundaries. The Autonomy Dial is how the user establishes it with their agent, defining what they are comfortable with the agent handling on its own. 
 Trust is not a binary switch; it’s a spectrum. A user might trust an agent to handle low-stakes tasks autonomously but demand full confirmation for high-stakes decisions. The Autonomy Dial, a form of progressive authorization, allows users to set their preferred level of agent independence, making them active participants in defining the relationship. 
 Psychological Underpinning 
 Allowing users to tune the agent’s autonomy grants them a locus of control, letting them match the system’s behavior to their personal risk tolerance. 
 Implementation 
 This can be implemented as a simple, clear setting within the application, ideally on a per-task-type basis. Using the taxonomy from our first article, the settings could be: 
 Observe & Suggest 
 I want to be notified of opportunities or issues, but the agent will never propose a plan. 
 Plan & Propose 
 The agent can create plans, but I must review every one before any action is taken. 
 Act with Confirmation 
 For familiar tasks, the agent can prepare actions, and I will give a final go/no-go confirmation. 
 Act Autonomously 
 For pre-approved tasks (e.g., disputing charges under $50), the agent can act independently and notify me after the fact. 
 An email assistant, for example, could have a separate autonomy dial for scheduling meetings versus sending emails on the user’s behalf. This granularity is key, as it reflects the nuanced reality of a user’s trust. 
 When to Prioritize This Pattern 
 Prioritize this in systems where tasks vary widely in risk and personal preference (e.g., financial management tools, communication platforms). It is essential for onboarding, allowing users to start with low autonomy and increase it as their confidence grows. 
 Risk of Omission 
 Without this, users who experience a single failure will abandon the agent completely rather than simply dialing back its permissions. 
 Metrics for Success: 
 Trust Density 
 Percentage breakdown of users per setting (e.g., 20% Suggest, 50% Confirm, 30% Auto). 
 Setting Churn 
 Number of Setting Changes / Total Active Users per month. High churn indicates trust volatility. 
 3. The Explainable Rationale: Answering Why? 
 After taking an action, a good partner explains their reasoning. This pattern is the open communication that follows an action, answering Why? before it’s even asked. “I did that because you’ve told me in the past that you prefer X.” 
 When an agent acts, especially autonomously, the immediate question in the user’s mind is often, Why did it do that? The Explainable Rationale pattern proactively answers this question, providing a concise justification for the agent’s decisions. This is not a technical log file. In my first article of this series, we discussed translating system primitives into user-facing language to prevent deception. This pattern is the practical application of that principle. It transforms the raw logic into a human-readable explanation grounded in the user’s own stated preferences and prior inputs. 
 Psychological Underpinning 
 When an agent’s actions are explainable, they feel logical rather than random, helping the user build an accurate mental model of how the agent thinks. 
 Effective Rationales: 
 Grounded in Precedent 
 The best explanations link back to a rule, preference, or prior action. 
 Simple and Direct 
 Avoid complex conditional logic. Use a simple “Because you said X, I did Y” structure. 
 Returning to the travel example, after the flight is rebooked autonomously, the user might see this in their notification feed: 
 I’ve rebooked your canceled flight. 
 New Flight: Delta 789, departing at 2:30 PM. 
 Why I took this action: Your original flight was canceled by the airline. 
 You’ve pre-approved autonomous rebooking for same-day, non-stop flights. 
 [ View New Itinerary ] [ Undo this Action ] 
 The rationale is clear, defensible, and reinforces the idea that the agent is operating within the boundaries the user established. 
 When to Prioritize This Pattern 
 Prioritize it for any autonomous action where the reasoning isn’t immediately obvious from the context, especially for actions that happen in the background or are triggered by an external event (like the flight cancellation example). 
 Risk of Omission 
 Without this, users interpret valid autonomous actions as random behavior or ‘bugs,’ preventing them from forming a correct mental model. 
 Metrics for Success: 
 Why? Ticket Volume 
 Number of support tickets tagged “Agent Behavior — Unclear” per 1,000 active users. 
 Rationale Validation 
 Percentage of users who rate the explanation as ‘Helpful’ in post-interaction microsurveys. 
 4. The Confidence Signal 
 This pattern is about the agent being self-aware in the relationship. By communicating its own confidence, it helps the user decide when to trust its judgment and when to apply more scrutiny. 
 To help users calibrate their own trust, the agent should surface its own confidence in its plans and actions. This makes the agent’s internal state more legible and helps the user decide when to scrutinize a decision more closely. 
 Psychological Underpinning 
 Surfacing uncertainty helps prevent automation bias, encouraging users to scrutinize low-confidence plans rather than blindly accepting them. 
 Implementation: 
 Confidence Score 
 A simple percentage (e.g., Confidence: 95%) can be a quick, scannable indicator. 
 Scope Declaration 
 A clear statement of the agent’s area of expertise (e.g., Scope: Travel bookings only) helps manage user expectations and prevents them from asking the agent to perform tasks it’s not designed for. 
 Visual Cues 
 A green checkmark can denote high confidence, while a yellow question mark can indicate uncertainty, prompting the user to review more carefully. 
 When to Prioritize This Pattern 
 Prioritize when the agent’s performance can vary significantly based on the quality of input data or the ambiguity of the task. It is especially valuable in expert systems (e.g., medical aids, code assistants) where a human must critically evaluate the AI’s output. 
 Risk of Omission 
 Without this, users will fall victim to automation bias, blindly accepting low-confidence hallucinations, or anxiously double-check high-confidence work. 
 Metrics for Success: 
 Calibration Score 
 Pearson correlation between Model Confidence Score and User Acceptance Rate. Target > 0.8. 
 Scrutiny Delta 
 Difference between the average review time of low-confidence plans and high-confidence plans. Expected to be positive (e.g., +12 seconds). 
 5. The Action Audit & Undo: The Ultimate Safety Net 
 Trust requires knowing you can recover from a mistake. The Undo function is the ultimate relationship safety net, assuring the user that even if the agent misunderstands, the consequences are not catastrophic. 
 The single most powerful mechanism for building user confidence is the ability to easily reverse an agent’s action. A persistent, easy-to-read Action Audit log, with a prominent Undo button for every possible action, is the ultimate safety net. It dramatically lowers the perceived risk of granting autonomy. 
 Psychological Underpinning 
 Knowing that a mistake can be easily undone creates psychological safety, encouraging users to delegate tasks without fear of irreversible consequences. 
 Design Best Practices: 
 Timeline View 
 A chronological log of all agent-initiated actions is the most intuitive format. 
 Clear Status Indicators 
 Show whether an action was successful, is in progress, or has been undone. 
 Time-Limited Undos 
 For actions that become irreversible after a certain point (e.g., a non-refundable booking), the UI must clearly communicate this time window (e.g., Undo available for 15 minutes). This transparency about the system’s limitations is just as important as the undo capability itself. Being honest about when an action becomes permanent builds trust. 
 When to Prioritize This Pattern 
 This is a foundational pattern that should be implemented in nearly all agentic systems. It is absolutely non-negotiable when introducing autonomous features or when the cost of an error (financial, social, or data-related) is high. 
 Risk of Omission 
 Without this, one error permanently destroys trust, as users realize they have no safety net. 
 Metrics for Success: 
 Reversion Rate 
 Undone Actions / Total Actions Performed. If the Reversion Rate > 5% for a specific task, disable automation for that task. 
 Safety Net Conversion 
 Percentage of users who upgrade to Act Autonomously within 7 days of successfully using Undo. 
 6. The Escalation Pathway: Handling Uncertainty Gracefully 
 A smart partner knows when to ask for help instead of guessing. This pattern allows the agent to handle ambiguity gracefully by escalating to the user, demonstrating a humility that builds, rather than erodes, trust. 
 Even the most advanced agent will encounter situations where it is uncertain about the user’s intent or the best course of action. How it handles this uncertainty is a defining moment. A well-designed agent doesn’t guess; it escalates. 
 Psychological Underpinning 
 When an agent acknowledges its limits rather than guessing, it builds trust by respecting the user’s authority in ambiguous situations. 
 Escalation Patterns Include: 
 Requesting Clarification 
 “You mentioned ‘next Tuesday.’ Do you mean September 30th or October 7th?” 
 Presenting Options 
 “I found three flights that match your criteria. Which one looks best to you?” 
 Requesting Human Intervention 
 For high-stakes or highly ambiguous tasks, the agent should have a clear pathway to loop in a human expert or support agent. The prompt might be: “This transaction seems unusual, and I’m not confident about how to proceed. Would you like me to flag this for a human agent to review?” 
 When to Prioritize This Pattern 
 Prioritize in domains where user intent can be ambiguous or highly context-dependent (e.g., natural language interactions, complex data queries). Use this whenever the agent operates with incomplete information or when multiple correct paths exist. 
 Risk of Omission 
 Without this, the agent will eventually make a confident, catastrophic guess that alienates the user. 
 Metrics for Success: 
 Escalation Frequency 
 Agent Requests for Help / Total Tasks. Healthy range: 5-15%. 
 Recovery Success Rate 
 Tasks Completed Post-Escalation / Total Escalations. Target > 90%. 
 Pattern Best For Primary Risk Key Metric 
 Intent Preview Irreversible or financial actions User feels ambushed >85% Acceptance Rate 
 Autonomy Dial Tasks with variable risk levels Total feature abandonment Setting Churn 
 Explainable Rationale Background or autonomous tasks User perceives bugs “Why?” Ticket Volume 
 Confidence Signal Expert or high-stakes systems Automation bias Scrutiny Delta 
 Action Audit & Undo All agentic systems Permanent loss of trust <5% Reversion Rate 
 Escalation Pathway Ambiguous user intent Confident, catastrophic guesses >90% Recovery Success 
 Table 1: Summary of Agentic AI UX patterns. Remember to adjust the metrics based on your specific domain risk and needs. 
 Designing for Repair and Redress This is learning how to apologize effectively. A good apology acknowledges the mistake, fixes the damage, and promises to learn from it. 
 Errors are not a possibility; they are an inevitability. 
 The long-term success of an agentic system depends less on its ability to be perfect and more on its ability to recover gracefully when it fails. A robust framework for repair and redress is a core feature, not an afterthought. 
 Empathic Apologies and Clear Remediation 
 When an agent makes a mistake, the error message is the apology. It must be designed with psychological precision. This moment is a critical opportunity to demonstrate accountability. From a service design perspective, this is where companies can use the service recovery paradox : the phenomenon where a customer who experiences a service failure, followed by a successful and empathetic recovery, can actually become more loyal than a customer who never experienced a failure at all. A well-handled mistake can be a more powerful trust-building event than a long history of flawless execution. 
 The key is treating the error as a relationship rupture that needs to be mended. This involves: 
 Acknowledge the Error 
 The message should state clearly and simply that a mistake was made. 
 Example: I incorrectly transferred funds. 
 State the Immediate Correction 
 Immediately follow up with the remedial action. 
 Example: I have reversed the action, and the funds have been returned to your account. 
 Provide a Path for Further Help 
 Always offer a clear link to human support. This de-escalates frustration and shows that there is a system of accountability beyond the agent itself. 
 A well-designed repair UI might look like this: 
 We made a mistake on your recent transfer. 
 I apologize. I transferred $250 to the wrong account. 
 ✔ Corrective Action: The transfer has been reversed, and your $250 has been refunded. 
 ✔ Next Steps: The incident has been flagged for internal review to prevent it from happening again. 
 Need further help? [ Contact Support ] 
 Building the Governance Engine for Safe Innovation The design patterns described above are the user-facing controls, but they cannot function effectively without a robust internal support structure. This is not about creating bureaucratic hurdles; it is about building a strategic advantage. An organization with a mature governance framework can ship more ambitious agentic features with greater speed and confidence, knowing that the necessary guardrails are in place to mitigate brand risk. This governance engine turns safety from a checklist into a competitive asset. 
 This engine should function as a formal governance body, an Agentic AI Ethics Council , comprising a cross-functional alliance of UX, Product, and Engineering, with vital support from Legal, Compliance, and Support. In smaller organizations, these ‘Council’ roles often collapse into a single triad of Product, Engineering, and Design leads. 
 A Checklist for Governance 
 Legal/Compliance 
 This team is the first line of defense, ensuring the agent’s potential actions stay within regulatory and legal boundaries. They help define the hard no-go zones for autonomous action. 
 Product 
 The product manager is the steward of the agent’s purpose. They define and monitor its operational boundaries through a formal autonomy policy that documents what the agent is and is not allowed to do. They own the Agent Risk Register. 
 UX Research 
 This team is the voice of the user’s trust and anxiety. They are responsible for a recurring process for running trust calibration studies, simulated misbehavior tests, and qualitative interviews to understand the user’s evolving mental model of the agent. 
 Engineering 
 This team builds the technical underpinnings of trust. They must architect the system for robust logging, one-click undo functionality, and the hooks needed to generate clear, explainable rationales. 
 Support 
 These teams are on the front lines of failure. They must be trained and equipped to handle incidents caused by agent errors, and they must have a direct feedback loop to the Ethics Council to report on real-world failure patterns. 
 This governance structure should maintain a set of living documents, including an Agent Risk Register that proactively identifies potential failure modes, Action Audit Logs that are regularly reviewed, and the formal Autonomy Policy Documentation. 
 Where to Start: A Phased Approach for Product Leaders 
 For product managers and executives, integrating agentic AI can feel like a monumental task. The key is to approach it not as a single launch, but as a phased journey of building both technical capability and user trust in parallel. This roadmap allows your organization to learn and adapt, ensuring each step is built on a solid foundation. 
 Phase 1: Foundational Safety (Suggest & Propose) 
 The initial goal is to build the bedrock of trust without taking significant autonomous risks. In this phase, the agent’s power is limited to analysis and suggestion. 
 Implement a rock-solid Intent Preview : This is your core interaction model. Get users comfortable with the idea of the agent formulating plans, while keeping the user in full control of execution. 
 Build the Action Audit & Undo infrastructure: Even if the agent isn’t acting autonomously yet, build the technical scaffolding for logging and reversal. This prepares your system for the future and builds user confidence that a safety net exists. 
 Phase 2: Calibrated Autonomy (Act with Confirmation) 
 Once users are comfortable with the agent’s proposals, you can begin to introduce low-risk autonomy. This phase is about teaching users how the agent thinks and letting them set their own pace. 
 Introduce the Autonomy Dial with limited settings: Start by allowing users to grant the agent the power to Act with Confirmation. 
 Deploy the Explainable Rationale : For every action the agent prepares, provide a clear explanation. This demystifies the agent’s logic and reinforces that it is operating based on the user’s own preferences. 
 Phase 3: Proactive Delegation (Act Autonomously) 
 This is the final step, taken only after you have clear data from the previous phases demonstrating that users trust the system. 
 Enable Act Autonomously for specific, pre-approved tasks: Use the data from Phase 2 (e.g., high Proceed rates, low Undo rates) to identify the first set of low-risk tasks that can be fully automated. 
 Monitor and Iterate : The launch of autonomous features is not the end, but the beginning of a continuous cycle of monitoring performance, gathering user feedback, and refining the agent’s scope and behavior based on real-world data. 
 Design As The Ultimate Safety Lever The emergence of agentic AI represents a new frontier in human-computer interaction. It promises a future where technology can proactively reduce our burdens and streamline our lives. But this power comes with profound responsibility . 
 Autonomy is an output of a technical system, but trustworthiness is an output of a design process. Our challenge is to ensure that the user experience is not a casualty of technical capability but its primary beneficiary. 
 As UX professionals, product managers, and leaders, our role is to act as the stewards of that trust. By implementing clear design patterns for control and consent, designing thoughtful pathways for repair, and building robust governance frameworks, we create the essential safety levers that make agentic AI viable. We are not just designing interfaces; we are architecting relationships . The future of AI’s utility and acceptance rests on our ability to design these complex systems with wisdom, foresight, and a deep-seated respect for the user’s ultimate authority.
```

---

## 29. CSS <code>@scope</code>: An Alternative To Naming Conventions And Heavy Abstractions

- 日期: 2026-02-05 08:00
- 链接: https://smashingmagazine.com/2026/02/css-scope-alternative-naming-conventions/

```
When learning the principles of basic CSS, one is taught to write modular, reusable, and descriptive styles to ensure maintainability. But when developers become involved with real-world applications, it often feels impossible to add UI features without styles leaking into unintended areas. 
 This issue often snowballs into a self-fulfilling loop; styles that are theoretically scoped to one element or class start showing up where they don’t belong. This forces the developer to create even more specific selectors to override the leaked styles, which then accidentally override global styles, and so on. 
 Rigid class name conventions, such as BEM , are one theoretical solution to this issue. The BEM (Block, Element, Modifier) methodology is a systematic way of naming CSS classes to ensure reusability and structure within CSS files. Naming conventions like this can reduce cognitive load by leveraging domain language to describe elements and their state , and if implemented correctly, can make styles for large applications easier to maintain . 
 In the real world, however, it doesn’t always work out like that. Priorities can change, and with change, implementation becomes inconsistent. Small changes to the HTML structure can require many CSS class name revisions. With highly interactive front-end applications, class names following the BEM pattern can become long and unwieldy (e.g., app-user-overview__status--is-authenticating ), and not fully adhering to the naming rules breaks the system’s structure, thereby negating its benefits. 
 Given these challenges, it’s no wonder that developers have turned to frameworks, Tailwind being the most popular CSS framework . Rather than trying to fight what seems like an unwinnable specificity war between styles, it is easier to give up on the CSS Cascade and use tools that guarantee complete isolation. 
 Developers Lean More On Utilities How do we know that some developers are keen on avoiding cascaded styles? It’s the rise of “modern” front-end tooling — like CSS-in-JS frameworks — designed specifically for that purpose. Working with isolated styles that are tightly scoped to specific components can seem like a breath of fresh air. It removes the need to name things — still one of the most hated and time-consuming front-end tasks — and allows developers to be productive without fully understanding or leveraging the benefits of CSS inheritance. 
 But ditching the CSS Cascade comes with its own problems. For instance, composing styles in JavaScript requires heavy build configurations and often leads to styles awkwardly intermingling with component markup or HTML. Instead of carefully considered naming conventions, we allow build tools to autogenerate selectors and identifiers for us (e.g., .jsx-3130221066 ), requiring developers to keep up with yet another pseudo-language in and of itself. (As if the cognitive load of understanding what all your component’s useEffect s do weren’t already enough!) 
 Further abstracting the job of naming classes to tooling means that basic debugging is often constrained to specific application versions compiled for development, rather than leveraging native browser features that support live debugging, such as Developer Tools. 
 It’s almost like we need to develop tools to debug the tools we’re using to abstract what the web already provides — all for the sake of running away from the “pain” of writing standard CSS. 
 Luckily, modern CSS features not only make writing standard CSS more flexible but also give developers like us a great deal more power to manage the cascade and make it work for us. CSS Cascade Layers are a great example, but there’s another feature that gets a surprising lack of attention — although that is changing now that it has recently become Baseline compatible . 
 The CSS @scope At-Rule I consider the CSS @scope at-rule to be a potential cure for the sort of style-leak-induced anxiety we’ve covered, one that does not force us to compromise native web advantages for abstractions and extra build tooling. 
 “The @scope CSS at-rule enables you to select elements in specific DOM subtrees, targeting elements precisely without writing overly-specific selectors that are hard to override, and without coupling your selectors too tightly to the DOM structure.” 
 — MDN 
 In other words, we can work with isolated styles in specific instances without sacrificing inheritance, cascading, or even the basic separation of concerns that has been a long-running guiding principle of front-end development. 
 Plus, it has excellent browser coverage . In fact, Firefox 146 added support for @scope in December, making it Baseline compatible for the first time. Here is a simple comparison between a button using the BEM pattern versus the @scope rule: 
 <!-- BEM --> 
<button class="button button--primary">
 <span class="button__text">Click me</span>
 <span class="button__icon">→</span>
</button>

<style>
 .button .button__text { /* button text styles */ }
 .button .button__icon { /* button icon styles */ }
 .button--primary { primary button styles */ }
</style> <!-- @scope --> 
<button class="primary-button">
 <span>Click me</span>
 <span>→</span>
</button>

<style>
 @scope (.primary-button) {
 span:first-child { /* button text styles */ }
 span:last-child { /* button icon styles */ }
 }
</style> The @scope rule allows for precision with less complexity . The developer no longer needs to create boundaries using class names, which, in turn, allows them to write selectors based on native HTML elements, thereby eliminating the need for prescriptive CSS class name patterns. By simply removing the need for class name management, @scope can alleviate the fear associated with CSS in large projects. 
 Basic Usage To get started, add the @scope rule to your CSS and insert a root selector to which styles will be scoped: 
 @scope (<selector>) {
 /* Styles scoped to the <selector> */
} So, for example, if we were to scope styles to a <nav> element, it may look something like this: 
 @scope (nav) {
 a { /* Link styles within nav scope */ }

 a:active { /* Active link styles */ }

 a:active::before { /* Active link with pseudo-element for extra styling */ }

 @media (max-width: 768px) {
 a { /* Responsive adjustments */ }
 }
} 
 This, on its own, is not a groundbreaking feature. However, a second argument can be added to the scope to create a lower boundary , effectively defining the scope’s start and end points. 
 /* Any a element inside ul will not have the styles applied */
@scope (nav) to (ul) {
 a {
 font-size: 14px;
 }
} 
 This practice is called donut scoping , and there are several approaches one could use, including a series of similar, highly specific selectors coupled tightly to the DOM structure, a :not pseudo-selector, or assigning specific class names to <a> elements within the <nav> to handle the differing CSS. 
 Regardless of those other approaches, the @scope method is much more concise. More importantly, it prevents the risk of broken styles if classnames change or are misused or if the HTML structure were to be modified. Now that @scope is Baseline compatible, we no longer need workarounds! 
 We can take this idea further with multiple end boundaries to create a “style figure eight”: 
 /* Any <a> or <p> element inside <aside> or <nav> will not have the styles applied */
@scope (main) to (aside, nav) {
 a {
 font-size: 14px;
 }
 p {
 line-height: 16px;
 color: darkgrey;
 }
} 
 Compare that to a version handled without the @scope rule, where the developer has to “reset” styles to their defaults: 
 main a {
 font-size: 14px;
}

main p {
 line-height: 16px;
 color: darkgrey;
}

main aside a,
main nav a {
 font-size: inherit; /* or whatever the default should be */
}

main aside p,
main nav p {
 line-height: inherit; /* or whatever the default should be */
 color: inherit; /* or a specific color */
} 
 Check out the following example. Do you notice how simple it is to target some nested selectors while exempting others? 
 See the Pen @scope example [forked] by Blake Lundquist . 
 Consider a scenario where unique styles need to be applied to slotted content within web components . When slotting content into a web component, that content becomes part of the Shadow DOM, but still inherits styles from the parent document. The developer might want to implement different styles depending on which web component the content is slotted into: 
 <!-- Same <user-card> content, different contexts -->
<product-showcase>
 <user-card slot="reviewer">
 <img src="avatar.jpg" slot="avatar">
 <span slot="name">Jane Doe</span>
 </user-card>
</product-showcase>

<team-roster>
 <user-card slot="member">
 <img src="avatar.jpg" slot="avatar">
 <span slot="name">Jane Doe</span>
 </user-card>
</team-roster> In this example, the developer might want the <user-card> to have distinct styles only if it is rendered inside <team-roster> : 
 @scope (team-roster) {
 user-card {
 display: inline-flex;
 align-items: center;
 gap: 0.5rem;
 }

 user-card img {
 border-radius: 50%;
 width: 40px;
 height: 40px;
 }
} More Benefits There are additional ways that @scope can remove the need for class management without resorting to utilities or JavaScript-generated class names. For example, @scope opens up the possibility to easily target descendants of any selector , not just class names: 
 /* Only div elements with a direct child button are included in the root scope */
@scope (div:has(> button)) {
 p {
 font-size: 14px;
 }
} 
 And they can be nested , creating scopes within scopes: 
 @scope (main) {
 p {
 font-size: 16px;
 color: black;
 }
 @scope (section) {
 p {
 font-size: 14px;
 color: blue;
 }
 @scope (.highlight) {
 p {
 background-color: yellow;
 font-weight: bold;
 }
 }
 }
} Plus, the root scope can be easily referenced within the @scope rule: 
 /* Applies to elements inside direct child section elements of main , but stops at any direct aside that is a direct chiled of those sections */
@scope (main > section) to (:scope > aside) {
 p {
 background-color: lightblue;
 color: blue;
 }
 /* Applies to ul elements that are immediate siblings of root scope */
 :scope + ul {
 list-style: none;
 }
} 
 The @scope at-rule also introduces a new proximity dimension to CSS specificity resolution. In traditional CSS, when two selectors match the same element, the selector with the higher specificity wins. With @scope , when two elements have equal specificity, the one whose scope root is closer to the matched element wins. This eliminates the need to override parent styles by manually increasing an element’s specificity, since inner components naturally supersede outer element styles. 
 <style>
 @scope (.container) {
 .title { color: green; } 
 }
 <!-- The <h2> is closer to .container than to .sidebar so "color: green" wins. -->
 @scope (.sidebar) {
 .title { color: red; }
 }
</style>

<div class="sidebar">
 <div class="container">
 <h2 class="title">Hello</h2>
 </div>
</div> 
 Conclusion Utility-first CSS frameworks, such as Tailwind, work well for prototyping and smaller projects. Their benefits quickly diminish, however, when used in larger projects involving more than a couple of developers. 
 Front-end development has become increasingly overcomplicated in the last few years, and CSS is no exception. While the @scope rule isn’t a cure-all, it can reduce the need for complex tooling. When used in place of, or alongside strategic class naming, @scope can make it easier and more fun to write maintainable CSS. 
 Further Reading 
 CSS @scope (MDN) 
 “ CSS @scope ”, Juan Diego Rodríguez (CSS-Tricks) 
 Firefox 146 Release Notes (Firefox) 
 Browser Support (CanIUse) 
 Popular CSS Frameworks (State of CSS 2024) 
 “ The “C” in CSS: Cascade ”, Thomas Yip (CSS-Tricks) 
 BEM Introduction (Get BEM)
```

---

## 30. Combobox vs. Multiselect vs. Listbox: How To Choose The Right One

- 日期: 2026-02-03 10:00
- 链接: https://smashingmagazine.com/2026/02/combobox-vs-multiselect-vs-listbox/

```
So what’s the difference between combobox, multiselect, listbox, and dropdown? While all these UI components might appear similar, they serve different purposes. The choice often comes down to the number of available options and their visibility. 
 Let’s see how they differ, what purpose they serve , and how to choose the right one — avoiding misunderstandings and wrong expectations along the way. 
 Not All List Patterns Are The Same All the UI components highlighted above have exactly one thing in common: they support users’ interactions with lists. However, they do so slightly differently. 
 Let’s take a look at each, one by one: 
 Dropdown → list is hidden until it’s triggered. 
 Combobox → type to filter + select 1 option. 
 Multiselect → type to filter + select many options. 
 Listbox → all list options visible by default (+ scroll). 
 Dual listbox → move items between 2 listboxes. 
 In other words, Combobox combines a text input field with a dropdown list, so users can type to filter and select a single option. With Multiselect , users can select many options (often displayed as pills or chips). 
 Listboxes display all list options visible by default, often with scrolling. It’s helpful when users need to see all available choices immediately. Dual listbox (also called transfer list ) is a variation of a listbox that allows users to move items between two listboxes (left ↔ right), typically for bulk selection. 
 Never Hide Frequently Used Options As mentioned above, the choice of the right UI component depends on 2 factors : how many list options are available, and if all these options need to be visible by default. All lists could have tree structures, nesting, and group selection, too. 
 There is one principle that I’ve been following for years for any UI component: never hide frequently used options . If users rely on a particular selection frequently, there is very little value in hiding it from them. 
 We could either make it pre-selected , or (if there are only 2–3 frequently used options) show them as chips or buttons , and then show the rest of the list on interaction. In general, it’s a good idea to always display popular options — even if it might clutter the UI. 
 How To Choose Which? Not every list needs a complex selection method. For lists with fewer than 5 items , simple radio buttons or checkboxes usually work best. But if users need to select from a large list of options (e.g., 200+ items), combobox + multiselect are helpful because of the faster filtering (e.g., country selection). 
 Listboxes are helpful when people need to access many options at once , especially if they need to choose many options from that list as well. They could be helpful for frequently used filters. 
 Dual listbox is often overlooked and ignored. But it can be very helpful for complex tasks, e..g bulk selection, or assigning roles, tasks, responsibilities. It’s the only UI component that allows users to review their full selection list side-by-side with the source list before committing (also called “Transfer list” ). 
 In fact, dual listbox is often faster, more accurate, and more accessible than drag-and-drop . 
 Usability Considerations One important note to keep in mind is that all list types need to support keyboard navigation (e.g., ↑/↓ arrow keys) for accessibility. Some people will almost always rely uponthe keyboard to select options once they start typing. 
 Beyond that: 
 For lists with 7+ options , consider adding “Select All” and “Clear All” functionalities to streamline user interaction. 
 For lengthy lists with a combobox, expose all options to users on click/tap, as otherwise they might never be seen, 
 Most important, don’t display non-interactive elements as buttons to avoid confusion — and don't display interactive elements as static labels. 
 Wrapping Up: Not Everything Is A Dropdown Names matter. A vertical list of options is typically described as a “dropdown” — but often it’s a bit too generic to be meaningful. “Dropdown” hints that the list is hidden by default. “Multiselect” implies multi-selection (checkbox) within a list. “Combobox” implies text input. And “Listbox” is simply a list of selectable items, visible at all times. 
 The goal isn’t to be consistent with the definitions above for the sake of it. But rather to align intentions — speak the same language when deciding on, designing, building, and then using these UI components. 
 It should work for everyone — designers, engineers, and end users — as long as static labels don’t look like interactive buttons, and radio buttons don’t act like checkboxes. 
 Meet “Design Patterns For AI Interfaces” Meet Design Patterns For AI Interfaces , Vitaly’s new video course with practical examples from real-life products — with a live UX training happening soon. Jump to a free preview . 
 Meet Design Patterns For AI Interfaces , Vitaly’s video course on interface design & UX. 
 Video + UX Training 
 Video only 
 Video + UX Training 
 $ 450.00 $ 799.00 Get Video + UX Training 
 30 video lessons (10h) + Live UX Training . 
 100 days money-back-guarantee. 
 Video only 
 $ 275.00$ 395.00 
 Get the video course 
 30 video lessons (10h). Updated yearly. 
 Also available as a UX Bundle with 3 video courses. 
 Useful Resources Autocomplete: UX Guidelines , by Vitaly Friedman 
 Combobox , by eBay 👍 
 Combobox , by Elastic 
 Combobox , by Elisa 
 Combobox , by MongoDB 👍 
 Combobox , by Visa 👍 
 Combobox , by Watson (Docplanner) 
 Combobox , by Wikimedia 
 Combobox , by Zendesk 
 Multiselect (MongoDB Combobox Design Docs) , by MongoDB 👍 
 Multiselect Lookup , by Wikimedia 
 Multi-select Combo Box , by Vaadin 
 Multiselect , by Visa 
 Transfer (Listbox example) , by Ant Design 
 Listbox , by Hopper 
 List Box , by Vaadin 
 Listbox , by Visa 
 Dual List Selector , by Red Hat (PatternFly) 
 Dual Listbox , by Salesforce (Lightning Design System) 
 Transfer List , by Mantine 
 Dual Listbox , by Dashlite 
 Badges vs. Pills vs. Chips vs. Tags , by Vitaly Friedman 
 Listboxes vs. Dropdown Lists , by Anna Kaley (NN/g)
```

---
