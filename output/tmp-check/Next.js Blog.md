# Next.js Blog

> 分类: 大厂技术博客
> URL: https://nextjs.org/feed.xml
> 抓取: 30 篇

---

## 1. Next.js Across Platforms: Adapters, OpenNext, and Our Commitments

- 日期: 2026-03-25 17:00
- 链接: https://nextjs.org/blog/nextjs-across-platforms

```
Wednesday, March 25th 2026
Next.js Across Platforms: Adapters, OpenNext, and Our Commitments
Posted byNext.js 16.2 introduced a stable Adapter API, built in collaboration with OpenNext, Netlify, Cloudflare, AWS Amplify, and Google Cloud. This post covers how that happened, and the commitments we're making to ensure Next.js works well on every platform:
- Adapter API (stable): A typed, versioned description of your application that any platform can target.
- Test suite: Shared correctness tests for every adapter, including Vercel's.
- Verified adapters: Open-source, community-owned adapters hosted under the Next.js organization.
- Ecosystem Working Group: A standing forum for coordinating changes across providers.
How we got here
Many Next.js apps are deployed as a single Node.js server running next start
. Hundreds of thousands of teams do this today across any number of platforms, without limitations.
But scaling apps usually involves running multiple server instances. When you do, some things need to work correctly out of the box: cached content needs to stay synchronized across instances, on-demand revalidation needs to propagate, and streaming needs to work reliably. These are functional requirements, not optimizations.
Then there are the performance choices you opt into: serving cached content from a global CDN, running compute at the edge, optimizing cold starts with serverless functions. Each of these adds architectural complexity on top of what already needs to be correct.
Depending on the platform and architecture, the full surface area adds up: streaming, Server Components, Partial Prerendering, middleware, Cache Components, on-demand revalidation. Each capability and how they interact with one another was never formally documented. For platform providers looking to support Next.js at full fidelity in a multi-tenant environment across evolving releases, these challenges compounded:
When the Next.js team reached out with an offer to discuss Netlify's challenges, we started compiling a laundry list of specific issues to share, but it quickly became clear that the common thread among 90% of these was simply the lack of a documented, stable mechanism to configure and read build output. That was what we needed above all. So that's what we told Jimmy, and we're glad we did.
— Philippe Serhal, Engineer at Netlify
The missing piece was an upstream, stable, public contract that providers could build against.
OpenNext built the bridge
OpenNext filled that gap. It translated Next.js build output into something providers could consume, mapping framework semantics onto each provider's primitives. What started as a compatibility layer became an early production-grade adapter, especially on AWS, with Cloudflare and Netlify joining the effort later. OpenNext showed that Next.js build output can serve as a stable, defined interface that adapters target directly.
That insight led to a broader collaboration between the Next.js team and the OpenNext maintainers, along with engineers from Netlify, Cloudflare, AWS Amplify, and Google Cloud. We published a Build Adapters RFC in April 2025, formed a working group, and have been working together with these partners since then to design, test, and validate the API.
The Adapter API
Next.js 16.2 ships with a stable, public Adapter API.
On build, Next.js now produces a typed, versioned description of your application: routes, prerenders, static assets, runtime targets, dependencies, caching rules, and routing decisions. The adapter consumes this output and maps it onto a provider's infrastructure.
Adapters implement two hooks: modifyConfig
(when configuration loads) and onBuildComplete
(when the full output is available). Breaking changes require a new major version of Next.js.
Vercel's adapter uses this same public contract, with no private hooks or special integration path. It is open source.
As part of the working group's feedback, we have also reworked large sections of our documentation to better explain the platform integration surface. New guides cover the Rendering Philosophy, the Deploying to Platforms feature matrix, PPR Platform Guide, How Revalidation Works, and CDN Caching.
The test suite
We have made the Next.js test suite available for adapter authors. It covers streaming behavior, caching interactions, client navigation, and real-world edge cases. When a new feature ships, its behavior is encoded in these tests.
You can read more in the adapter testing documentation.
Adapter authors can run the suite using any adapter and get a pass/fail answer for each feature. This is the same test suite Vercel uses for its own adapter, so the correctness bar is shared across all providers.
Verified adapters
To become a verified adapter (hosted under the Next.js GitHub organization and listed in the Deploying to Platforms docs), two things are required: it must be open source and pass the full test suite. By making the adapter open source it ensures there is a place for the maintenance of the adapter, so that issues can be reported and triaged. The test suite ensures the adapter's compatibility with Next.js can be measured.
Each verified adapter is owned by the team that builds it. Publishing rights, release cadence, and implementation decisions are theirs, because platforms can be very different and we can't prescribe a specific implementation.
Providers can also build and ship closed-source adapters on the same public API.
The public Adapters API ships today with:
- Vercel adapter: open source, maps Next.js output to Vercel's serverless and CDN infrastructure.
- Bun adapter: a reference adapter showing how to build a complete Next.js deployment target on an alternative runtime.
Adapters for Netlify, Cloudflare, and AWS through OpenNext are in active development, with expected releases later this year.
Cloudflare has been part of OpenNext since the beginning because we believed developers deserve a stable, open contract for deploying Next.js apps anywhere. The official Next.js Adapter API makes that vision real. Developers running Next.js on Cloudflare's global developer platform will now have a shared foundation to build on, one designed in collaboration with the Next.js team to keep pace as the framework evolves. We are excited to be partners in this shared effort.
— Fred K Schott, Engineer at Cloudflare
The ecosystem working group
We are establishing the Next.js Ecosystem Working Group, a standing forum between the Next.js team, hosting providers, and adapter maintainers. Meeting notes will be public. If you want to join the group, please reach out to Jimmy.
We want providers to have early visibility into upcoming changes, not find out after a release. Breaking changes come with lead time proportional to their scope. New features are tested across environments before release. The full governance document covers the commitments in detail.
Read more from our partners:
- The Next.js Adapter API Just Shipped: Here's What Comes Next (Netlify)
- 3 Years of OpenNext (OpenNext)
- Next.js Deployment Adapters: A Bright Future for Next.js on Google Cloud (Google Cloud / Firebase)
The collaboration between OpenNext and the Next.js team transformed a community-driven workaround into an official standard, proving that the future of web frameworks is built on openness and shared innovation.
— Dorseuil Nicolas, OpenNext
Thank you to the members of the Build Adapters working group: engineers at Netlify, Cloudflare, Google Cloud, AWS Amplify, and OpenNext who invested their time co-designing this API and validating it for their platforms. Thank you to every contributor who built adapters, filed bugs, and shipped workarounds.
Next.js is used by millions of developers, and many of them run on infrastructure that isn't Vercel. They deserve the same level of reliability and the same access to new features. The Adapter API provides that: a shared contract that any platform can build on, with a public test suite that holds everyone, including us, to the same standard.
Every new feature we develop will be documented in the adapter contract. The RFC process remains open, coordinated with adapter authors as the API evolves.
```

---

## 2. Next.js 16.2: AI Improvements

- 日期: 2026-03-18 20:00
- 链接: https://nextjs.org/blog/next-16-2-ai

```
Wednesday, March 18th 2026
Next.js 16.2: AI Improvements
Posted byNext.js 16.2 includes several improvements designed for AI-assisted development. These changes make it easier for agents to understand your project, debug issues from the terminal, and inspect running apps — all without requiring a browser.
- Agent-ready
create-next-app
: Scaffold AI-ready projects out of the box - Browser Log Forwarding: Forward browser errors to the terminal for agent-powered debugging
- Dev Server Lock File: Actionable error messages when a second dev server tries to start
- Experimental Agent DevTools: Give AI agents terminal access to React DevTools and Next.js diagnostics
Agent-ready create-next-app
create-next-app
now includes an AGENTS.md
file by default, giving AI coding agents access to version-matched Next.js documentation from the start of your project.
This builds on our research into AGENTS.md
, which found that giving agents access to bundled documentation achieved a 100% pass rate on Next.js evals — outperforming skill-based approaches that maxed out at 79%. The key insight: always-available context works better than on-demand retrieval, because agents often fail to recognize when they should search for documentation.
The AGENTS.md
file is a short directive that tells agents to read the docs bundled at node_modules/next/dist/docs/
before writing any code. The Next.js npm package now includes the full documentation as plain Markdown files, giving agents accurate version-matched references locally without fetching external data.
For existing projects, the setup depends on your Next.js version.
On 16.2 or later, the docs are already bundled in the next
package. Add these two files to the root of your project:
<!-- BEGIN:nextjs-agent-rules -->
# Next.js: ALWAYS read docs before coding
Before any Next.js work, find and read the relevant doc in `node_modules/next/dist/docs/`. Your training data is outdated — the docs are the source of truth.
<!-- END:nextjs-agent-rules -->
The comment markers delimit the Next.js-managed section. You can add your own project-specific instructions outside them — future updates will only replace content between the markers.
CLAUDE.md
is the instruction file for Claude Code. The @
directive tells it to include AGENTS.md
as additional context:
@AGENTS.md
On earlier versions, use the codemod to generate these files automatically:
npx @next/codemod@latest agents-md
For more details, see the AI agents setup guide.
Browser Log Forwarding
Next.js now forwards browser errors to the terminal by default during development, so you can see client-side errors without switching to the browser console. This is especially helpful for AI agents that operate primarily through the terminal and can't access a browser console.
By default, only errors are forwarded to the terminal. You can control the level of forwarding with logging.browserToTerminal
in your next.config.ts
:
const nextConfig = {
logging: {
browserToTerminal: true,
// 'error' — errors only (default)
// 'warn' — warnings and errors
// true — all console output
// false — disabled
},
};
export default nextConfig;
Dev Server Lock File
Next.js now writes the running dev server's PID, port, and URL into the .next/dev/lock
file. When a second next dev
process starts in the same project directory, Next.js reads the lock file and prints an actionable error:
Error: Another next dev server is already running.
- Local: http://localhost:3000
- PID: 12345
- Dir: /path/to/project
- Log: .next/dev/logs/next-development.log
Run kill 12345 to stop it.
This is especially useful for AI coding agents, which frequently attempt to start next dev
without knowing a server is already running. The structured error gives the agent the PID to kill the existing process or the URL to connect to it — no manual intervention required.
The lock file also prevents two next build
processes from running simultaneously, which could otherwise corrupt build artifacts.
Experimental Agent DevTools
The features above help agents understand your project and debug issues. @vercel/next-browser
extends this by letting agents inspect a running Next.js application.
next-browser
is an experimental CLI that exposes browser-level data — screenshots, network requests, console logs — along with framework-specific insights from React DevTools and the Next.js dev overlay, like component trees, props, hooks, Partial Prerendering (PPR) shells, and errors. All returned as structured text via shell commands.
An LLM can't read a DevTools panel, but it can run next-browser tree
, parse the output, and decide what to inspect next. Each command is a one-shot request against a persistent browser session, so agents can query the app repeatedly without managing browser state. This turns the browser into something an agent can reason about, instead of a UI it can't access.
What it can do today
The feature set is evolving quickly. As of this release, next-browser
supports:
- Inspect React component trees — view props, hooks, state, and source-mapped file locations
- Analyze PPR shells — identify static vs dynamic regions and blocked Suspense boundaries
- Access errors and logs — retrieve build and runtime issues from the dev server
- Monitor network activity — track requests since navigation, including server actions
- Capture visuals — take screenshots or record loading filmstrips
Getting started
Install it as a skill (a reusable capability for AI agents):
npx skills add vercel-labs/next-browser
Then type /next-browser
in Claude Code, Cursor, or any AI agent that supports skills. The CLI manages a Chromium instance with React DevTools pre-loaded — no browser configuration required.
Example: Growing the static shell
With Partial Prerendering (PPR), Next.js can serve a static shell instantly from the edge — the parts of your page that don't depend on per-request data — then stream in the rest. The more content that fits in the static shell, the faster users see a meaningful page.
In practice, a single per-request fetch can accidentally make an entire page dynamic. Consider a blog post with a visitor counter:
export async function generateStaticParams() {
const posts = await getAllPosts();
return posts.map((post) => ({ slug: post.slug }));
}
export default async function BlogPost({ params }) {
const post = await getPost(params.slug);
const views = await getVisitorCount(params.slug); // per-request
return (
<article>
<h1>{post.title}</h1>
<span>{views} views</span>
<div>{post.content}</div>
</article>
);
}
Every slug is enumerated in generateStaticParams
, so the post content could be prerendered at build time. But getVisitorCount
runs on every request — and because it sits at the top level of the component, it makes the entire page dynamic. As a result, the entire page waits behind a loading skeleton instead of streaming in progressively.
An agent can use next-browser
to diagnose this. Locking PPR mode shows only the static shell — in this case, the app/blog/[slug]/loading.tsx
skeleton, because nothing in the page made it into the shell:
next-browser ppr lock # Enter PPR mode
next-browser goto /blog/hello # The entire page is a loading skeleton
The agent then runs ppr unlock
to find out what went wrong:
next-browser ppr unlock
# PPR Shell Analysis
# 1 dynamic hole, 1 static
blocked by:
- getVisitorCount (server-fetch)
owner: BlogPost at app/blog/[slug]/page.tsx:5
next step: Push the fetch into a smaller Suspense leaf
The report tells the agent exactly what to do: getVisitorCount
is the blocker, it lives in BlogPost
, and the fix is to push it into its own Suspense boundary. The agent wraps just the counter:
export default async function BlogPost({ params }) {
const post = await getPost(params.slug);
return (
<article>
<h1>{post.title}</h1>
<Suspense fallback={<span>— views</span>}>
<VisitorCount slug={params.slug} />
</Suspense>
<div>{post.content}</div>
</article>
);
}
Running ppr lock
again confirms the shell grew — the post content now prerenders instantly. Only the visitor count shows a fallback:
next-browser
is still evolving, but it points toward a future where agents can debug and optimize apps with the same visibility as a developer.
Feedback and Community
Share your feedback and help shape the future of Next.js:
```

---

## 3. Turbopack: What's New in Next.js 16.2

- 日期: 2026-03-18 20:00
- 链接: https://nextjs.org/blog/next-16-2-turbopack

```
Wednesday, March 18th 2026
Turbopack: What's New in Next.js 16.2
Posted byTwo releases after Turbopack became the default bundler for Next.js, we're focused on improving performance, fixing bugs, and increasing parity. Here are some of the latest features shipping as part of Next.js 16.2.
- Server Fast Refresh: Fine-grained server-side hot reloading
- Web Worker Origin: Increasing support for WASM libraries in Workers
- Subresource Integrity Support: Subresource Integrity for JavaScript files
- Tree Shaking of Dynamic Imports: Unused exports removed from dynamic
import()
- Inline Loader Configuration: Per-import loader configuration via import attributes
- Lightning CSS Configuration: Experimental LightningCSS configuration options
- Log Filtering: Suppressing noisy logs and warnings with
ignoreIssue
postcss.config.ts
Support: TypeScript PostCSS configuration- Performance Improvements and Bug Fixes: Over 200 changes and bug fixes
Looking forward towards our next release, we'll be focused on speeding up compiler performance and reducing memory usage.
Server Fast Refresh
We've reworked how server-side code is reloaded during development. The previous system cleared the require.cache
for the changed module and all other modules in its import chain. This approach often reloaded more code than necessary, including unchanged node_modules
.
The new system brings the same Fast Refresh approach used in the browser to your server code. Turbopack's knowledge of the module graph means only the module that actually changed is reloaded, leaving the rest intact. This makes server-side hot reloading significantly more efficient.
In real-world Next.js applications, we've seen 67-100% faster application refresh and 400-900% faster compile time inside Next.js. These results scale from the smallest "hello world" starter project to large sites like vercel.com
.
Server refresh time on a sample Next.js site
375% faster
Before
59ms
After
12.4ms
Next.js (40ms → 2.7ms)
Application (19ms → 9.7ms)
Today we're enabling this feature for all developers, by default. Proxy and Route Handlers will use the existing system today, but support for those is arriving in a future release. Share your feedback or any issues with this new feature on GitHub.
Web Worker Origin
Previously, Web Workers were bootstrapped through a blob://
URL. This streamlined loading the worker, but it set an empty location.origin
value. Web Worker code that tried to use importScripts()
or fetch()
(usually in third-party libraries) would have been unable to resolve the request without changes.
With the updated Worker bootstrap code, the origin
correctly points to your domain name, and relative fetches succeed. This should unblock anyone who had trouble running WASM code inside a Worker in previous versions.
Subresource Integrity Support
Turbopack now supports Subresource Integrity (SRI). SRI generates cryptographic hashes of your JavaScript files at build time, allowing browsers to verify that files haven't been modified.
Browsers provide a technology called Content Security Policy that allows sites to restrict the JavaScript that can run, eliminating entire classes of security issues. However, the typical nonce
-based method for implementing this requires all pages to be dynamically rendered, impacting performance. Subresource Integrity is an alternative that computes a hash of each script ahead of time, and only allows the browser to execute scripts with approved hashes.
const nextConfig = {
experimental: {
sri: {
algorithm: 'sha256',
},
},
};
module.exports = nextConfig;
Tree Shaking of Dynamic Imports
Turbopack now tree shakes destructured dynamic imports the same way it does static imports. Unused exports are removed from the bundle:
const { cat } = await import('./lib');
This is now equivalent to a static import for tree shaking purposes — any exports from ./lib
that aren't used will be tree-shaken.
Inline Loader Configuration
Turbopack now supports per-import loader configuration via import attributes. Instead of applying loaders globally through turbopack.rules
, you can configure them on individual imports using the with
clause:
import rawText from './data.txt' with {
turbopackLoader: 'raw-loader',
turbopackAs: '*.js',
};
import value from './data.js' with {
turbopackLoader: 'string-replace-loader',
turbopackLoaderOptions: '{"search":"PLACEHOLDER","replace":"replaced value"}',
};
This is useful when only a specific import needs special treatment, avoiding side effects on other imports of the same file type. The available attributes are turbopackLoader
, turbopackLoaderOptions
, turbopackAs
, and turbopackModuleType
.
You should still prefer configuring your loaders in next.config.ts
when possible, since code using inline loaders is less portable. This option is more useful for code generated from plugins or loaders.
Lightning CSS Configuration
Lightning CSS is a fast, Rust-based CSS transformer used by Turbopack for CSS minification and prefixing. It also allows implementation of modern CSS features on older browsers, similar to what Babel or SWC do for JavaScript. Previously, the only way to toggle these settings was through a Browserslist configuration. Now with the experimental lightningCssFeatures
option, you can force certain features to always or never transpile.
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
useLightningcss: true,
lightningCssFeatures: {
include: ['light-dark', 'oklab-colors'],
exclude: ['nesting'],
},
},
};
export default nextConfig;
Log Filtering
Turbopack can now suppress noisy or expected warnings from streaming logs with the turbopack.ignoreIssue
config option. This is useful for suppressing warnings from third-party code, generated files, or optional dependencies, as well as hiding expected errors from the Next.js error overlay.
You can match logs generated from specific code paths, as well as filter for specific title/description strings or patterns.
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
turbopack: {
ignoreIssue: [
{ path: '**/vendor/**' },
{ path: 'app/**', title: 'Module not found' },
{ path: /generated\/.*\.ts/, description: /expected error/i },
],
},
};
export default nextConfig;
postcss.config.ts
Support
Turbopack now supports postcss.config.ts
in addition to the existing .js
and .cjs
variants.
Performance Improvements and Bug Fixes
We've continued to invest in improving Turbopack internals. Over 200 changes and bug fixes have improved stability and compatibility across a wide range of projects. Optimizations in data encoding, internal representation formats, and hashing algorithms have improved memory usage and build time. We've made error logs clearer and expanded diagnostics to help you better understand compiler errors. We've also used your GitHub Issues as a guide for which features were missing since the 16.1 release.
Feedback and Community
Share your feedback and help shape the future of Next.js:
```

---

## 4. Next.js 16.2

- 日期: 2026-03-18 20:00
- 链接: https://nextjs.org/blog/next-16-2

```
Wednesday, March 18th 2026
Next.js 16.2
Posted byNext.js 16.2 includes performance improvements, better debugging, improvements for Agents, and over 200 Turbopack fixes and improvements.
- Faster Time-to-URL: ~400% faster
next dev
startup - Faster Rendering: ~50% faster rendering
- New Default Error Page: Redesigned built-in 500 page
- Server Function Logging: Dev terminal logs for Server Function execution
- Hydration Diff Indicator: Clear server/client diff in the error overlay
--inspect
fornext start
: Attach the Node.js debugger to your production server
We also published dedicated deep-dive posts for two major areas of this release:
- Turbopack: Faster builds, SRI support,
postcss.config.ts
, tree shaking improvements, Server Fast Refresh, and 200+ bug fixes - AI Improvements:
AGENTS.md
increate-next-app
, browser log forwarding, andnext-browser
(experimental)
Upgrade today, or get started with:
# Use the automated upgrade CLI
npx @next/codemod@canary upgrade latest
# ...or upgrade manually
npm install next@latest react@latest react-dom@latest
# ...or start a new project
npx create-next-app@latest
Faster Time-to-URL in Development
We've significantly improved the time it takes before localhost:3000
is ready during next dev
. On the same machine and project, startup is ~87% faster compared to Next.js 16.1 on the default application.
Faster Rendering
We contributed a change to React that makes Server Components payload deserialization up to 350% faster. The previous implementation used a JSON.parse
reviver callback, which crosses the C++/JavaScript boundary in V8 for every key-value pair in the parsed JSON. Even a trivial no-op reviver makes JSON.parse
roughly 4x slower than without one.
The new approach uses a two-step process: plain JSON.parse()
followed by a recursive walk in pure JavaScript. This eliminates the boundary-crossing overhead and adds optimizations like short-circuiting plain strings that don't need transformation.
In real-world Next.js applications, this translates to 25% to 60% faster rendering to HTML, depending on the RSC payload size.
Server render time
Server Component Table with 1000 items
26% faster
Before
19ms
After
15ms
Server Component with nested Suspense
33% faster
Before
80ms
After
60ms
Payload CMS homepage
34% faster
Before
43ms
After
32ms
Payload CMS with rich text
60% faster
Before
52ms
After
33ms
New Default Error Page
The default error page shown in production has been redesigned. When your application encounters an error and you haven't defined a custom global-error.tsx
or error.tsx
, Next.js renders a built-in fallback page. This fallback has been updated with a cleaner, more modern design.
Server Function Logging
Next.js now logs Server Function execution in the terminal during development. Each log shows the function name, its arguments, execution time, and the file it's defined in.
Hydration Diff Indicator
When a hydration mismatch occurs, the error overlay now clearly labels which content came from the server and which from the client. The diff uses a + Client
/ - Server
legend, making it immediately clear what diverged.
--inspect
for next start
Next.js 16.1 introduced next dev --inspect
for attaching the Node.js debugger during development. In 16.2, this extends to next start
, allowing you to attach a Node.js debugger to your production server.
next start --inspect
This is useful for debugging issues or profiling CPU and memory usage.
For more information on how to use the Node.js debugger, see the Chrome documentation.
transitionTypes
Prop for next/link
The <Link>
component now accepts a transitionTypes
prop — an array of strings that specifies the types of View Transitions to apply when navigating. Each type is passed to React.addTransitionType
during the navigation Transition, allowing you to trigger different animations based on the navigation direction or context.
<Link href="/about" transitionTypes={['slide']}>
About
</Link>
This is only supported in the App Router, since the Pages Router does not use React Transitions for navigation. transitionTypes
on Pages Router links is silently ignored, so shared link components work across both routers.
To learn more about view transitions, see the documentation.
Faster ImageResponse
ImageResponse
has been updated with significant improvements:
- 2x faster
ImageResponse
for basic images, up to 20x faster for complex images - Improved CSS and SVG coverage, including support for inline CSS variables,
text-indent
,text-decoration-skip-ink
,box-sizing
,display: contents
,position: static
, and percentage values forgap
- Default font changed from Noto Sans to Geist Sans
Learn more about ImageResponse.
Error Causes in the Dev Overlay
The error overlay now displays Error.cause
chains, making it easier to debug errors that wrap other errors. Causes are shown in a flat list below the top-level error, up to 5 levels deep.
Adapters
Adapters are now stable. This is a new API that allows platforms to customize the build process.
This is useful for deployment platforms or custom build integrations that need to modify the Next.js configuration or process the build output.
We will share a more detailed overview of Adapters next week.
Multiple Icon Formats
Multiple icon files with the same base name but different extensions are now handled automatically in your app directory (e.g., icon.png
and icon.svg
). This is useful for browser fallback support. Modern browsers can use SVG icons while older browsers fall back to PNG. Both formats are rendered as separate <link>
tags.
Experimental Features
unstable_catchError()
Extending the error recovery experience with the error.js
file convention, unstable_catchError()
provides more granular control of the error boundaries on the component level. By creating a custom error boundary using unstable_catchError()
, you can place it anywhere in your component tree.
Compared to a custom React error boundary, unstable_catchError()
is designed to work with Next.js out of the box:
- Built-in error recovery:
unstable_retry()
re-renders the page from the server in transition. - Framework-aware integration: APIs like
redirect()
andnotFound()
work by throwing special errors under the hood.unstable_catchError()
handles these seamlessly, so they're not accidentally caught by your error boundary. - Client navigation handling: The error state automatically clears when you do a client navigation to a different route.
The error boundary created by unstable_catchError()
receives the props passed from the call site and the ErrorInfo
value as the second argument, which is the same shape as the props passed to the error.js
file convention.
Just like error.js
, unstable_catchError()
can only be called from Client Components.
'use client';
import { unstable_catchError, type ErrorInfo } from 'next/error';
function CustomErrorBoundary(
props: { title: string },
{ error, unstable_retry }: ErrorInfo,
) {
return (
<div>
<h2>{props.title}</h2>
<p>{error.message}</p>
<button onClick={() => unstable_retry()}>Try again</button>
</div>
);
}
export default unstable_catchError(CustomErrorBoundary);
import CustomErrorBoundary from './custom-error-boundary';
export default function Page() {
return (
<CustomErrorBoundary title="Oops! Something went wrong!">
<Component />
</CustomErrorBoundary>
);
}
unstable_retry()
in error.tsx
A new unstable_retry()
prop is now available in error.tsx
components. Previously, the reset()
prop only cleared the error state and re-rendered the children, which works for temporary rendering errors but doesn't help when the error originates from data fetching or the RSC phase.
unstable_retry()
calls router.refresh()
and reset()
within a startTransition()
, providing built-in retry logic that re-fetches data and re-renders the segment. This is expected to be preferred over reset()
for most error recovery scenarios.
'use client';
import type { ErrorInfo } from 'next/error';
export default function Error({ error, unstable_retry }: ErrorInfo) {
return (
<div>
<h2>Something went wrong</h2>
<p>{error.message}</p>
<button onClick={() => unstable_retry()}>Try again</button>
</div>
);
}
experimental.prefetchInlining
Next.js 16 introduced per-segment prefetching, where the client issues individual requests for each segment in the route tree. This improves cache efficiency as shared layouts between sibling routes are fetched once and reused, but increases request volume.
The new experimental.prefetchInlining
option bundles all segment data for a route into a single response, reducing the number of prefetch requests to one per link. The trade-off is that shared layout data is duplicated across inlined responses rather than being cached and reused.
const nextConfig = {
experimental: {
prefetchInlining: true,
},
};
export default nextConfig;
This is a stepping stone toward a size-based heuristic where small segments are inlined automatically and larger segments remain separate.
experimental.cachedNavigations
This flag independently controls the Cached Navigations behavior, which caches static and dynamic Server Components data from navigations and the initial HTML loads so that repeat visits can be served instantly. Requires cacheComponents
to be enabled.
experimental.appNewScrollHandler
A reworked scroll and focus management system for App Router using React Fragment refs. The new handler improves how focus is managed after navigations. Instead of focusing the first focusable descendant deep within a segment (which could skip past content), it now blurs the active element, matching how browser navigations work.
const nextConfig = {
experimental: {
appNewScrollHandler: true,
},
};
export default nextConfig;
Feedback and Community
Share your feedback and help shape the future of Next.js:
Contributors
Next.js is the result of the combined work of over 3,770 individual developers. This release was brought to you by:
- The Next.js team: Andrew, Hendrik, Janka, Jiachi, Jimmy, Jiwon, JJ, Josh, Jude, Sam, Sebbie, Tim, and Zack.
- The Turbopack team: Benjamin, Andrew, Luke, Niklas, Tobias, and Will.
- The Next.js Docs team: Delba, Rich, Ismael, Joseph and Aurora.
Huge thanks to @acdlite, @unstubbable, @mischnic, @sokra, @ztanner, @mmastrac, @bgw, @lukesandberg, @wyattjoh, @huozhi, @eps1lon, @jwueller, @brookemosby, @delbaoliveira, @icyJoseph, @gaojude, @hanzala-sohrab, @dango0812, @ijjk, @msmx-mnakagawa, @Juneezee, @davidgolden, @LucianBuzzo, @devjiwonchoi, @alexcarpenter, @jaffarkeikei, @BradErz, @mintydev789, @naaa760, @Suhaib3100, @pavan-sh, @amannn, @fireairforce, @JamBalaya56562, @wheresrhys, @ericrav, @lubieowoce, @Thomas465xd, @bgub, @wbinnssmith, @Netail, @robert-j-webb, @bencmbrook, @shadcn, @sigmachirality, @abhishekmardiya, @vvscode, @feedthejim, @freek-boon-greenberry, @andrewimm, @alubbe, @FurryR, @01-binary, @andrewdamelio, @swarnava, @gnoff, @kristiyan-velkov, @styfle, @haydenbleasel, @rishishanbhag, @tdarthur, @lavanitha, and @karlhorky for helping!
```

---

## 5. Building Next.js for an agentic future

- 日期: 2026-02-12 00:00
- 链接: https://nextjs.org/blog/agentic-future

```
Thursday, February 12th 2026
Building Next.js for an agentic future
Posted byWe've spent the past year improving the Next.js agent experience. Along the way, we built and sunset an in-browser agent, shipped MCP integration, and learned that the real answer to better agent support is thinking from the agent's perspective.
Agents couldn't see the browser
Earlier this summer, we were working on improving the Next.js devtools when we noticed a pattern. Developers would see an error in the browser, copy the details, paste them into an AI editor, and ask the agent to fix it.
The problem was that agents can't see the browser. Runtime errors, client-side warnings, and rendered components are all invisible to them. When a user says "fix the error," the agent doesn't know what error they mean.
Our first response was updating the copy button to capture structured error data. Then we added a feature that forwards browser logs to the terminal. Small fixes, but they pointed toward a bigger realization. We needed to make Next.js itself visible to agents.
Experimenting with an in-browser agent
That led to an ambitious idea. What if we built an agent directly inside Next.js that worked like smart devtools?
We built an in-browser chat agent called Vector. Similar to react-grab
but integrated with Next.js, Vector let you select elements on the page, see their source code, and prompt for changes. It had Next.js best practices baked in to help agents avoid hallucination.
Subtitle: Vector's interface showing error detection and suggested fixes.
Vector was useful, but it overlapped with general coding agents like Cursor and Claude Code. Most developers were already using those tools for all of their projects anyway, not just Next.js. The UI selection made it easy to point at exactly what you wanted to change, but it wasn't something people needed every day.
We sunset Vector, but took what made it useful (structured visibility and framework-specific knowledge) and decided to build those into Next.js itself.
MCP made Next.js state visible to agents
Around the Next.js v16 release in October 2025, users were struggling to debug with agents. The common prompt was "fix the error," asking agents to resolve issues from the browser overlay. But agents would request the page HTML and find nothing wrong.
Runtime failures, browser JavaScript errors, and async errors all lived in the browser, not in the HTML. The rendered page, layout segments, routes, and other internal state were invisible to agents.
MCP gave us a way to expose this data. The first version surfaced internal states like errors, routes, and rendered segments, but exposing data alone wasn't enough. Agents also needed to discover running dev servers and communicate with them, which led to next-devtools-mcp
.
Subtitle: The Next.js MCP responding to "whats use cache?" with documentation and context.
The MCP also packages prompts and tools to help with upgrades and cache component migrations. There's a detailed talk about the MCP integration if you want to learn more.
The answer is to think like an agent
MCP confirmed what Vector taught us. Agents need visibility into what Next.js is doing, but that's only part of the story. The deeper lesson was treating agents as first-class users of Next.js and thinking from their perspective. What information do they need? When do they need it? How do they consume it?
This mindset led to practical changes. If agents read terminal output during development, then logging Server Action invocations and forwarding browser errors gives them the hints they need. If agents struggle with framework concepts not in their training data, then embedding a compressed docs index agents.md
or providing structured workflows (Next.js skills) gives them better context than documentation alone.
Those questions run through everything we built. The need for visibility led to better logging, the need for knowledge led to agents.md, and the need for discovery led to MCP. When you treat agents as first-class users and meet them where they are, debugging becomes a tight feedback loop between code, runtime, and AI.
What's next
We're now working on making this easier to adopt. You can already run npx @next/codemod
to generate an up-to-date docs index for your project, and we're expanding our eval suite to cover more Next.js 16 APIs so we can measure what actually helps agents. Longer term, we want this built into next dev
so agents get the right context automatically without any setup.
We're eager to hear your feedback and ideas on how to make Next.js work even better with agents.
```

---

## 6. Inside Turbopack: Building Faster by Building Less

- 日期: 2026-01-20 17:00
- 链接: https://nextjs.org/blog/turbopack-incremental-computation

```
Tuesday, January 20th 2026
Inside Turbopack: Building Faster by Building Less
Posted byEdit. Save. Refresh. Wait… Wait… Wait…
Compiling code usually means waiting, but Turbopack makes iteration loops fast with caching and incremental computation. Not every modern bundler uses an incremental approach, and that’s with good reason. Incremental computation can introduce significant complexity and opportunities for bugs. Caches require extra tracking and copies of data, adding both CPU and memory overhead. When applied poorly, caching can actually make performance worse.
Despite all of this, we took on these challenges because we knew that an incremental architecture would be critical to Turbopack’s success. Turbopack is the new default bundler for Next.js, a framework that is used to build some of the largest web applications in the world. We needed to enable instant builds and a fast as-you-type interactive React Fast Refresh experience, even for the largest and most challenging workloads. Our incremental architecture is core to achieving this.
Turbopack’s architecture was built ground-up with caching in mind. Its incremental design is based on over a decade of research. We built on first-hand experience from challenges in implementing caching in webpack and drew inspiration from Salsa (which powers Rust-Analyzer and Ruff), Parcel, the Rust compiler’s query system, Adapton, and many others.
Turbopack achieves a fine-grained cache by automatically tracking how internal functions are called and what values they depend on. When something changes we know how to recompute the results with minimal work.
Background: Manual incremental computation
Many build systems include explicit dependency graphs that must be manually populated when evaluating build rules. Explicitly declaring your dependency graph can theoretically give optimal results, but in practice it leaves room for errors.
The difficulty of specifying an explicit dependency graph means that usually caching is done at a coarse file-level granularity. This granularity does have some benefits: fewer incremental results means less data to cache, which might be worth it if you have limited disk space or memory.
An example of such an architecture is GNU Make, where output targets and prerequisites are manually configured and represented as files. Systems like GNU Make miss caching opportunities due to their coarse granularity: they do not understand and cannot cache internal data structures within the compiler.
Function-level fine-grained automatic incremental computation
In Turbopack, the relationship between input files and resulting build artifacts isn’t straightforward. Bundlers employ whole-program analysis for dead code elimination ("tree shaking") and clustering of common dependencies in the module graph. Consequently, the build artifacts (JavaScript files shared across multiple application routes) form complex many-to-many relationships with input files.
Turbopack uses a very fine-grained caching architecture. Because manually declaring and adding dependencies to a graph is prone to human errors, Turbopack needs an automated solution that can scale.
Tracking the compilation graph with value cells
To facilitate automatic caching and dependency tracking, Turbopack introduces a concept of “value cells” (Vc<…>
). Each value cell represents a fine-grained piece of execution, like a cell in a spreadsheet. When reading a cell, it records the currently executing function and all of its cells as dependent on that cell. This is similar to how signals work in frameworks like SolidJS.
By not marking cells as dependencies until they are read, Turbopack achieves finer-grained caching than a traditional top-down memoization approach would provide. For example, an argument might be an object or mapping of many value cells. Instead of needing to recompute our tracked function when any part of the object or mapping changes, it only needs to recompute the tracked function when a cell that it has actually read changes.
Value cells represent nearly everything inside of Turbopack, such as a file on disk, an abstract syntax tree (AST), metadata about imports and exports of modules, or clustering information used for chunking and bundling.
Marking dirty and propagating changes
When Turbopack executes functions for the first time, it builds a graph of functions and the value cells they create or depend on. The graph’s roots are the requested outputs (bundled assets), and the leaves are source code files. There are intermediate representations in the middle, such as ASTs, metadata, partially-transformed modules, or chunking information.
When our file system watcher finds source code that has changed, it marks all functions that read the file’s value cell as “dirty” and queues them for re-computation.
The dirtied function reading the file might parse or transform the JavaScript module and produce a new intermediate representation. Recomputing the function update cells containing changed intermediate representations, which may mark more functions as dirty. Cell updates are skipped if the cell contents are equal. This propagation bubbles up the graph until all affected functions have been recomputed.
As an additional optimization, execution is "demand-driven," meaning the system defers re-execution of dirty functions until they become part of an "active query". In development, an active query could be a currently open webpage with hot reloading enabled. In builds, this is a request for the full production app.
Aggregation graphs
While most operations, like the dirty propagation algorithm, only require information about adjacent edges and neighboring nodes in the graph, some operations need to query information about more significant portions of the dependency graph:
- Finding all dirty nodes when a sub-graph becomes part of a new active query, so we can schedule re-computation.
- Collecting errors, warnings, or lints of a sub-graph.
- Waiting for computation of a sub-graph to finish.
Because we maintain a fine-grained cache, the graph can contain hundreds of thousands or even millions of intermediate results. Visiting significant portions of this graph would be expensive.
To make these queries efficient, Turbopack uses an additional data structure on top of the dependency graph, called the “aggregation graph”.
When we build or update the dependency graph, we maintain parallel nodes in the aggregation graph that summarize part of the dependency graph. Some frequently accessed information, like emitted errors or warnings, is attached to the aggregation nodes.
This aggregation graph has multiple layers of resolution, with higher aggregation layers referencing more functions in each node, decreasing the resolution, and reducing the number of nodes that must be traversed when collecting information.
Every potential active query (e.g. an application entrypoint or route) represents a root in the aggregation graph. At the final aggregation graph layer, each root represents the information for itself and all of the children in the original dependency graph. Adding roots to the dependency graph can require a reorganization of the aggregation graph, but that’s an infrequent operation.
File system caching
Until our recent Next.js 16.1 release, all of these caches were stored only in memory.
In this new release, we shipped file system caching for next dev
as stable and on-by-default. This cache allows us to persist the dependency graph, the aggregation graph, and all of the intermediate results stored in value cells to disk. When next dev
is restarted, it can quickly resume from this warm cache.
File system caching came with its own set of challenges, and it took us over a year of dedicated work to meet our own high performance and quality bar. We'll dive into that soon in an upcoming engineering blog post.
Feedback and Community
Share your feedback and help shape the future of Next.js:
```

---

## 7. Next.js 16.1

- 日期: 2025-12-18 20:00
- 链接: https://nextjs.org/blog/next-16-1

```
Thursday, December 18th 2025
Next.js 16.1
Posted byNext.js 16.1 focuses on faster development workflows and improved stability, with major updates to Turbopack and tooling.
- Turbopack File System Caching for
next dev
(stable): Improved compile times fornext dev
by default. - Next.js Bundle Analyzer (experimental): Optimize your code with our new interactive tool.
- Easier debugging: Debug your Next.js app with
next dev --inspect
. - Transitive external dependencies: Turbopack can automatically handle transitive external dependencies with no warnings.
Upgrade Today
# Use the automated upgrade CLI
npx @next/codemod@canary upgrade latest
# ...or upgrade manually
npm install next@latest react@latest react-dom@latest
# ...or start a new project
npx create-next-app@latest
Turbopack File System Caching for next dev
Turbopack file system caching for next dev
is now stable and on by default. Compiler artifacts are stored on disk, leading to significantly faster compile times when restarting your development server, especially in large projects.
First route compile time
~10× faster
Cold
Cached
~5× faster
Cold
Cached
Large internal Vercel app
~14× faster
Cold
Cached
Internal applications at Vercel have been dogfooding this for the past year. To learn more about how we built file system caching for Turbopack, watch Luke Sandberg's talk at Next.js Conf.
Following this release, we'll be stabilizing file system caching for next build
. See our documentation for more information, and share your feedback on the dedicated GitHub discussion.
Next.js Bundle Analyzer (experimental)
Next.js 16.1 includes a new experimental Bundle Analyzer that works with Turbopack. It makes it easier to optimize bundle sizes for both server and client code—helping improve Core Web Vitals, reduce lambda cold start times, and identify bloated dependencies.
next experimental-analyze
Running the command launches an interactive UI to inspect production bundles, identify large modules, and see why they're included.
Try it yourself: Open the interactive Bundle Analyzer demo to explore the module graph.
The Bundle Analyzer is deeply integrated into Next.js, allowing you to:
- Filter bundles by route
- View the full import chain showing why a module is included
- Trace imports across server-to-client component boundaries and dynamic imports
- View CSS and other imported asset sizes
- Switch between client and server views
The Bundle Analyzer is in early development and will be improved further in future releases. Share your feedback on the dedicated GitHub discussion.
Easier Debugging with next dev --inspect
You can now enable the Node.js debugger by passing --inspect
to next dev
. Previously this required passing NODE_OPTIONS=--inspect
and would attach the inspector to all processes spawned by Next.js instead of only to the process running your code.
Improved Handling of serverExternalPackages
Next.js allows you to keep dependencies unbundled using serverExternalPackages
. Previously, this only worked reliably for direct dependencies. If you used a library that internally depends on something like sqlite
, and needed to externalize sqlite
, you'd have to add it to your own package.json
—even though it's not your direct dependency. This workaround leaked internal implementation details, created maintenance burden, and could lead to impossible version conflicts when multiple packages required different versions of the same dependency.
Next.js 16.1 fixes this for Turbopack, which now correctly resolves and externalizes transitive dependencies in serverExternalPackages
without additional configuration.
Other Updates
- 20MB smaller installs: Next.js installs are about 20MB smaller thanks to simplifications in the Turbopack file system caching layer.
- New
next upgrade
command: A newnext upgrade
command makes upgrading easier. Going forward, you can just run this to upgrade Next.js versions. - MCP
get_routes
tool: The Next.js DevTools MCP server now has aget_routes
tool to get the full list of routes in your application. generateStaticParams
timing: Time spent ongenerateStaticParams
is now logged as part of the timings shown for requests in development.- Build worker logging:
next build
"Collecting page data" and "Generating static pages" now log the number of worker threads used. - Improved async import bundling: Turbopack has improved bundling of async imports in dev to reduce the number of chunks produced, avoiding certain pathological but real-world cases.
- Relative source map paths: Turbopack now produces source maps with relative file paths for server-side code, improving compatibility with Node.js and other ecosystem tools.
Feedback and Community
Share your feedback and help shape the future of Next.js:
Contributors
Next.js is the result of the combined work of over 3,700 individual developers. This release was brought to you by:
- The Next.js team: Andrew, Hendrik, Janka, Jiachi, Jimmy, Jiwon, JJ, Josh, Jude, Sam, Sebastian, Sebbie, Wyatt, and Zack.
- The Turbopack team: Benjamin, Luke, Niklas, Tim, Tobias, and Will.
- The Next.js Docs team: Delba, Rich, Ismael, and Joseph.
Huge thanks to @kdy1, @eps1lon, @SyMind, @bgw, @swarnava, @devjiwonchoi, @ztanner, @ijjk, @huozhi, @icyJoseph, @acdlite, @unstubbable, @gnoff, @gusfune, @lukesandberg, @sokra, @hayes, @shuding, @wyattjoh, @marjan-ahmed, @timneutkens, @ajstrongdev, @zigang93, @mischnic, @Nayeem-XTREME, @hamirmahal, @eli0shin, @tessamero, @gaojude, @jamesdaniels, @georgesfarah, @timeyoutakeit, @sequencerr, @Strernd, @lucasadrianof, @wbinnssmith, @hamidreza-nateghi, @jokokoloko, @dijonmusters, @H01001000, @xusd320, @lubieowoce, @KaziMahbuburRahman, @zhiyanzhaijie, @feedthejim, @that-one-arab, @JamBalaya56562, @shrink, @florianliebig, @allenzhou101, @benmerckx, @ymc9, @Marukome0743, @pyrytakala, @danpeleg4, @gaearon, @styfle, @jhuleatt, @muhammadsyaddad, @roelvan, and @SukkaW for helping!
```

---

## 8. Next.js Security Update: December 11, 2025

- 日期: 2025-12-11 16:00
- 链接: https://nextjs.org/blog/security-update-2025-12-11

```
Thursday, December 11th 2025
Next.js Security Update: December 11, 2025
Posted byTwo additional vulnerabilities have been identified in the React Server Components (RSC) protocol. These issues were discovered while security researchers examined the patches for React2Shell. Importantly, neither of these new issues allow for Remote Code Execution. The patch for React2Shell remains fully effective.
These vulnerabilities originate in the upstream React implementation (CVE-2025-55183, CVE-2025-55184). This advisory tracks the downstream impact on Next.js applications using the App Router. For full details, see the React blog post.
Addendum: The initial fix for CVE-2025-55184 was incomplete. A complete fix has been issued under CVE-2025-67779. If you previously upgraded to one of the initially recommended versions, please upgrade again to the latest patched versions listed below.
Impact
Denial of Service: CVE-2025-55184 (High Severity)
A specifically crafted HTTP request can be sent to any App Router endpoint that, when deserialized, can cause an infinite loop that hangs the server process and prevents future HTTP requests from being served.
Note: The initial fix for this vulnerability was incomplete. A complete fix has been issued under CVE-2025-67779. Users who previously upgraded must upgrade again to the latest patched versions.
Source Code Exposure: CVE-2025-55183 (Medium Severity)
A specifically crafted HTTP request can cause a Server Function to return the compiled source code of other Server Functions in your application. This could reveal business logic. Secrets could also be exposed if they are defined directly in your code (rather than accessed via environment variables at runtime) and referenced within a Server Function. Depending on your bundler configuration, these values may be inlined into the compiled function output.
Affected and Fixed Next.js Versions
Applications using React Server Components with the App Router are affected. The table below shows which versions are affected by each vulnerability and the corresponding fix:
Pages Router applications are not affected, but we still recommend upgrading to a patched version.
Required Action
All users should upgrade to the latest patched version in their release line:
If you are on Next.js >=13.3, 14.0.x, or 14.1.x, upgrade to the latest 14.2.x release.
npm install next@14.2.35 # for 14.x
npm install next@15.0.7 # for 15.0.x
npm install next@15.1.11 # for 15.1.x
npm install next@15.2.8 # for 15.2.x
npm install next@15.3.8 # for 15.3.x
npm install next@15.4.10 # for 15.4.x
npm install next@15.5.9 # for 15.5.x
npm install next@16.0.10 # for 16.0.x
npm install next@15.6.0-canary.60 # for 15.x canary releases
npm install next@16.1.0-canary.19 # for 16.x canary releases
Run npx fix-react2shell-next
to launch an interactive tool which can check versions and perform deterministic version bumps per the recommended versions above. See the GitHub repository for full details.
npx fix-react2shell-next
There is no workaround. Upgrading to a patched version is required.
Resources
- CVE-2025-67779 (Complete DoS Fix): CVE, Next.js
- CVE-2025-55184 (DoS): React, Next.js
- CVE-2025-55183 (Source Code Exposure): React, Next.js
- React blog: Denial of Service and Source Code Exposure in React Server Components
- Previous Security Advisory: CVE-2025-66478
Discovery
Thank you to RyotaK from GMO Flatt Security Inc. and Andrew MacPherson for discovering and responsibly disclosing these vulnerabilities. We are intentionally limiting technical detail in this advisory to protect developers who have not yet upgraded.
```

---

## 9. Security Advisory: CVE-2025-66478

- 日期: 2025-12-03 16:00
- 链接: https://nextjs.org/blog/CVE-2025-66478

```
Wednesday, December 3rd 2025
Security Advisory: CVE-2025-66478
Posted byDecember 06, 9:05 PM PST: If your application was online and unpatched as of December 4th, 2025 at 1:00 PM PT, we strongly encourage you to rotate any secrets it uses, starting with your most critical ones.
December 06, 7:29 AM PST: An npm package has been released to update affected Next.js apps. Use
npx fix-react2shell-next
to update now, or visit the GitHub repository to learn more.
A critical vulnerability has been identified in the React Server Components (RSC) protocol. The issue is rated CVSS 10.0 and can allow remote code execution when processing attacker-controlled requests in unpatched environments.
This vulnerability originates in the upstream React implementation (CVE-2025-55182). This advisory (CVE-2025-66478) tracks the downstream impact on Next.js applications using the App Router.
Impact
The vulnerable RSC protocol allowed untrusted inputs to influence server-side execution behavior. Under specific conditions, an attacker could craft requests that trigger unintended server execution paths. This can result in remote code execution in unpatched environments.
All users should upgrade to a patched version immediately. See the required action section for specific instructions.
Affected Next.js Versions
Applications using React Server Components with the App Router are affected when running:
- Next.js 15.x
- Next.js 16.x
- Next.js 14.3.0-canary.77 and later canary releases
Next.js 13.x, Next.js 14.x stable, Pages Router applications, and the Edge Runtime are not affected.
Fixed Versions
The vulnerability is fully resolved in the following patched Next.js releases:
- 15.0.5
- 15.1.9
- 15.2.6
- 15.3.6
- 15.4.8
- 15.5.7
- 16.0.7
We also released patched canary releases for Next.js 15 and 16:
- 15.6.0-canary.58 (for 15.x canary releases)
- 16.1.0-canary.12 (for 16.x canary releases)
These versions include the hardened React Server Components implementation.
Required Action
All users should upgrade to the latest patched version in their release line:
npm install next@15.0.5 # for 15.0.x
npm install next@15.1.9 # for 15.1.x
npm install next@15.2.6 # for 15.2.x
npm install next@15.3.6 # for 15.3.x
npm install next@15.4.8 # for 15.4.x
npm install next@15.5.7 # for 15.5.x
npm install next@16.0.7 # for 16.0.x
npm install next@15.6.0-canary.58 # for 15.x canary releases
npm install next@16.1.0-canary.12 # for 16.x canary releases
If you are on Next.js 14.3.0-canary.77 or a later canary release, downgrade to the latest stable 14.x release:
npm install next@14
If you're currently using canary releases to enable PPR, you can update to 15.6.0-canary.58, which includes a fix for the vulnerability while continuing to support PPR. For other ways to patch older versions, see this discussion post.
Run npx fix-react2shell-next
to launch an interactive tool which can check versions and perform deterministic version bumps per the recommended versions above. See the GitHub repository for full details.
npx fix-react2shell-next
There is no workaround—upgrading to a patched version is required.
Rotating environment variables
Once you have patched your version and re-deployed your application, we recommend rotating all your application secrets. Learn about working with environment variables in the documentation here.
Resources
- Security advisories: React (CVE-2025-55182), Next.js (CVE-2025-66478)
- React blog: Critical Security Vulnerability in React Server Components
- Vercel Knowledge Base: React2Shell Security Bulletin
- Netlify Blog: Netlify's response to the critical React security vulnerability
- AWS Security Blog: China-nexus cyber threat groups rapidly exploit React2Shell vulnerability
- Google Cloud Blog: Responding to CVE-2025-55182: Secure your React and Next.js workloads
- Fastly Blog: Fastly's Proactive Protection for React2Shell, Critical React RCE CVE-2025-55182 and CVE-2025-66478
- Akamai Blog: CVE-2025-55182: React and Next.js Server Functions Deserialization RCE
Discovery
Thank you to Lachlan Davidson for discovering and responsibly disclosing this vulnerability. We are intentionally limiting technical detail in this advisory to protect developers who have not yet upgraded.
```

---

## 10. Next.js 16

- 日期: 2025-10-21 20:00
- 链接: https://nextjs.org/blog/next-16

```
Tuesday, October 21st 2025
Next.js 16
Posted byAhead of our upcoming Next.js Conf 2025, Next.js 16 is now available.
This release provides the latest improvements to Turbopack, caching, and the Next.js architecture. Since the previous beta release, we added several new features and improvements:
- Cache Components: New model using Partial Pre-Rendering (PPR) and use cache for instant navigation.
- Next.js Devtools MCP: Model Context Protocol integration for improved debugging and workflow.
- Proxy: Middleware replaced by
proxy.ts
to clarify network boundary. - DX: Improved logging for builds and development requests.
For reminder, those features were available since the previous beta release:
- Turbopack (stable): Default bundler for all apps with up to 5-10x faster Fast Refresh, and 2-5x faster builds
- Turbopack File System Caching (beta): Even faster startup and compile times for the largest apps
- React Compiler Support (stable): Built-in integration for automatic memoization
- Build Adapters API (alpha): Create custom adapters to modify the build process
- Enhanced Routing: Optimized navigations and prefetching with layout deduplication and incremental prefetching
- Improved Caching APIs: New
updateTag()
and refinedrevalidateTag()
- React 19.2: View Transitions,
useEffectEvent()
,<Activity/>
- Breaking Changes: Async params,
next/image
defaults, and more
Upgrade to Next.js 16:
# Use the automated upgrade CLI
npx @next/codemod@canary upgrade latest
# ...or upgrade manually
npm install next@latest react@latest react-dom@latest
# ...or start a new project
npx create-next-app@latest
For cases where the codemod can't fully migrate your code, please read the upgrade guide.
New Features and Improvements
Cache Components
Cache Components are a new set of features designed to make caching in Next.js both more explicit, and more flexible. They center around the new "use cache"
directive, which can be used to cache pages, components, and functions, and which leverages the compiler to automatically generate cache keys wherever it’s used.
Unlike the implicit caching found in previous versions of the App Router, caching with Cache Components is entirely opt-in. All dynamic code in any page, layout, or API route is executed at request time by default, giving Next.js an out-of-the-box experience that’s better aligned with what developers expect from a full-stack application framework.
Cache Components also complete the story of Partial Prerendering (PPR), which was first introduced in 2023. Prior to PPR, Next.js had to choose whether to render each URL statically or dynamically; there was no middle ground. PPR eliminated this dichotomy, and let developers opt portions of their static pages into dynamic rendering (via Suspense) without sacrificing the fast initial load of fully static pages.
You can enable Cache Components in your next.config.ts
file:
const nextConfig = {
cacheComponents: true,
};
export default nextConfig;
We will be sharing more about Cache Components and how to use them at Next.js Conf 2025 on October 22nd, and we will be sharing more content in our blog and documentation in the coming weeks.
Note: as previously announced in the beta release, the previous experimental
experimental.ppr
flag and configuration options have been removed in favor of the Cache Components configuration.
Learn more in the documentation here.
Next.js Devtools MCP
Next.js 16 introduces Next.js DevTools MCP, a Model Context Protocol integration for AI-assisted debugging with contextual insight into your application.
The Next.js DevTools MCP provides AI agents with:
- Next.js knowledge: Routing, caching, and rendering behavior
- Unified logs: Browser and server logs without switching contexts
- Automatic error access: Detailed stack traces without manual copying
- Page awareness: Contextual understanding of the active route
This enables AI agents to diagnose issues, explain behavior, and suggest fixes directly within your development workflow.
Learn more in the documentation here.
proxy.ts
(formerly middleware.ts
)
proxy.ts
replaces middleware.ts
and makes the app’s network boundary explicit. proxy.ts
runs on the Node.js runtime.
- What to do: Rename
middleware.ts
→proxy.ts
and rename the exported function toproxy
. Logic stays the same. - Why: Clearer naming and a single, predictable runtime for request interception.
export default function proxy(request: NextRequest) {
return NextResponse.redirect(new URL('/home', request.url));
}
Note: The
middleware.ts
file is still available for Edge runtime use cases, but it is deprecated and will be removed in a future version.
Learn more in the documentation here.
Logging Improvements
In Next.js 16 the development request logs are extended showing where time is spent.
- Compile: Routing and compilation
- Render: Running your code and React rendering
The build is also extended to show where time is spent. Each step in the build process is now shown with the time it took to complete.
▲ Next.js 16 (Turbopack)
✓ Compiled successfully in 615ms
✓ Finished TypeScript in 1114ms
✓ Collecting page data in 208ms
✓ Generating static pages in 239ms
✓ Finalizing page optimization in 5ms
The following features were previously announced in the beta release:
Developer Experience
Turbopack (stable)
Turbopack has reached stability for both development and production builds, and is now the default bundler for all new Next.js projects. Since its beta release earlier this summer, adoption has scaled rapidly: more than 50% of development sessions and 20% of production builds on Next.js 15.3+ are already running on Turbopack.
With Turbopack, you can expect:
- 2–5× faster production builds
- Up to 10× faster Fast Refresh
We're making Turbopack the default to bring these performance gains to every Next.js developer, no configuration required. For apps with custom webpack setups, you can continue using webpack by running:
next dev --webpack
next build --webpack
Turbopack File System Caching (beta)
Turbopack now supports filesystem caching in development, storing compiler artifacts on disk between runs for significantly faster compile times across restarts, especially in large projects.
Enable filesystem caching in your configuration:
const nextConfig = {
experimental: {
turbopackFileSystemCacheForDev: true,
},
};
export default nextConfig;
All internal Vercel apps are already using this feature, and we’ve seen notable improvements in developer productivity across large repositories.
We’d love to hear your feedback as we iterate on filesystem caching. Please try it out and share your experience.
Simplified create-next-app
create-next-app
has been redesigned with a simplified setup flow, updated project structure, and improved defaults. The new template includes the App Router by default, TypeScript-first configuration, Tailwind CSS, and ESLint.
Build Adapters API (alpha)
Following the Build Adapters RFC, we've worked with the community and deployment platforms to deliver the first alpha version of the Build Adapters API.
Build Adapters allow you to create custom adapters that hook into the build process, enabling deployment platforms and custom build integrations to modify Next.js configuration or process build output.
const nextConfig = {
experimental: {
adapterPath: require.resolve('./my-adapter.js'),
},
};
module.exports = nextConfig;
Share your feedback in the RFC discussion.
React Compiler Support (stable)
Built-in support for the React Compiler is now stable in Next.js 16 following the React Compiler's 1.0 release. The React Compiler automatically memoizes components, reducing unnecessary re-renders with zero manual code changes.
The reactCompiler
configuration option has been promoted from experimental
to stable. It is not enabled by default as we continue gathering build performance data across different application types. Expect compile times in development and during builds to be higher when enabling this option as the React Compiler relies on Babel.
const nextConfig = {
reactCompiler: true,
};
export default nextConfig;
Install the latest version of the React Compiler plugin:
npm install babel-plugin-react-compiler@latest
Core Features & Architecture
Enhanced Routing and Navigation
Next.js 16 includes a complete overhaul of the routing and navigation system, making page transitions leaner and faster.
Layout deduplication: When prefetching multiple URLs with a shared layout, the layout is downloaded once instead of separately for each Link. For example, a page with 50 product links now downloads the shared layout once instead of 50 times, dramatically reducing the network transfer size.
Incremental prefetching: Next.js only prefetches parts not already in cache, rather than entire pages. The prefetch cache now:
- Cancels requests when the link leaves the viewport
- Prioritizes link prefetching on hover or when re-entering the viewport
- Re-prefetches links when their data is invalidated
- Works seamlessly with upcoming features like Cache Components
Trade-off: You may see more individual prefetch requests, but with much lower total transfer sizes. We believe this is the right trade-off for nearly all applications. If the increased request count causes issues, please let us know. We're working on additional optimizations to inline data chunks more efficiently.
These changes require no code modifications and are designed to improve performance across all apps.
Improved Caching APIs
Next.js 16 introduces refined caching APIs for more explicit control over cache behavior.
revalidateTag()
(updated)
revalidateTag()
now requires a cacheLife
profile as the second argument to enable stale-while-revalidate (SWR) behavior:
import { revalidateTag } from 'next/cache';
// ✅ Use built-in cacheLife profile (we recommend 'max' for most cases)
revalidateTag('blog-posts', 'max');
// Or use other built-in profiles
revalidateTag('news-feed', 'hours');
revalidateTag('analytics', 'days');
// Or use an inline object with a custom revalidation time
revalidateTag('products', { expire: 3600 });
// ⚠️ Deprecated - single argument form
revalidateTag('blog-posts');
The profile argument accepts built-in cacheLife
profile names (like 'max'
, 'hours'
, 'days'
) or custom profiles defined in your next.config
. You can also pass an inline { expire: number }
object. We recommend using 'max'
for most cases, as it enables background revalidation for long-lived content. When users request tagged content, they receive cached data immediately while Next.js revalidates in the background.
Use revalidateTag()
when you want to invalidate only properly tagged cached entries with stale-while-revalidate behavior. This is ideal for static content that can tolerate eventual consistency.
Migration guidance: Add the second argument with a
cacheLife
profile (we recommend'max'
) for SWR behavior, or useupdateTag()
in Server Actions if you need read-your-writes semantics.
updateTag()
(new)
updateTag()
is a new Server Actions-only API that provides read-your-writes semantics, expiring and immediately reading fresh data within the same request:
'use server';
import { updateTag } from 'next/cache';
export async function updateUserProfile(userId: string, profile: Profile) {
await db.users.update(userId, profile);
// Expire cache and refresh immediately - user sees their changes right away
updateTag(`user-${userId}`);
}
This ensures interactive features reflect changes immediately. Perfect for forms, user settings, and any workflow where users expect to see their updates instantly.
refresh()
(new)
refresh()
is a new Server Actions-only API for refreshing uncached data only. It doesn't touch the cache at all:
'use server';
import { refresh } from 'next/cache';
export async function markNotificationAsRead(notificationId: string) {
// Update the notification in the database
await db.notifications.markAsRead(notificationId);
// Refresh the notification count displayed in the header
// (which is fetched separately and not cached)
refresh();
}
This API is complementary to the client-side router.refresh()
. Use it when you need to refresh uncached data displayed elsewhere on the page after performing an action. Your cached page shells and static content remain fast while dynamic data like notification counts, live metrics, or status indicators refresh.
React 19.2 and Canary Features
The App Router in Next.js 16 uses the latest React Canary release, which includes the newly released React 19.2 features and other features being incrementally stabilized. Highlights include:
- View Transitions: Animate elements that update inside a Transition or navigation
useEffectEvent
: Extract non-reactive logic from Effects into reusable Effect Event functions- Activity: Render "background activity" by hiding UI with
display: none
while maintaining state and cleaning up Effects
Learn more in the React 19.2 announcement.
Breaking Changes and Other Updates
Version Requirements
Removals
These features were previously deprecated and are now removed:
Behavior Changes
These features have new default behaviors in Next.js 16:
Deprecations
These features are deprecated in Next.js 16 and will be removed in a future version:
Additional Improvements
- Performance improvements: Significant performance optimizations for
next dev
andnext start
commands - Node.js native TypeScript for
next.config.ts
: Runnext dev
,next build
, andnext start
commands with--experimental-next-config-strip-types
flag to enable native TypeScript fornext.config.ts
.
We'll aim to share a more comprehensive migration guide ahead of the stable release in our documentation.
Feedback and Community
Share your feedback and help shape the future of Next.js:
Contributors
Next.js is the result of the combined work of over 3,000 individual developers. This release was brought to you by:
- The Next.js team: Andrew, Hendrik, Janka, Jiachi, Jimmy, Jiwon, JJ, Josh, Jude, Sam, Sebastian, Sebbie, Wyatt, and Zack.
- The Turbopack team: Benjamin, Josh, Luke, Niklas, Tim, Tobias, and Will.
- The Next.js Docs team: Delba, Rich, Ismael, and Joseph.
Huge thanks to @mischnic, @timneutkens, @unstubbable, @wyattjoh, @Cy-Tek, @lukesandberg, @OoMNoO, @ztanner, @icyJoseph, @huozhi, @gnoff, @ijjk, @povilasv, @dwrth, @obendev, @aymericzip, @devjiwonchoi, @SyMind, @vercel-release-bot, @Shireee, @eps1lon, @dharun36, @kachkaev, @bgw, @yousefdawood7, @TheAlexLichter, @sokra, @ericx0099, @leerob, @Copilot, @fireairforce, @fufuShih, @anvibanga, @hayes, @Milancen123, @martinfrancois, @lubieowoce, @gaojude, @lachlanjc, @liketiger, @styfle, @aaronbrown-vercel, @Samii2383, @FelipeChicaiza, @kevva, @m1abdullahh, @F7b5, @Anshuman71, @RobertFent, @poteto, @chloe-yan, @sireesha-siri, @brian-lou, @joao4xz, @stefanprobst, @samselikoff, @acdlite, @gwkline, @bgub, @brock-statsig, and @karlhorky for helping!
```

---

## 11. Next.js 16 (beta)

- 日期: 2025-10-09 20:00
- 链接: https://nextjs.org/blog/next-16-beta

```
Thursday, October 9th 2025
Next.js 16 (beta)
Posted byNext.js 16 (beta) is now available. This early release provides access to the latest improvements to Turbopack, caching, and the Next.js architecture ahead of the stable release. Highlights for this release include:
- Turbopack (stable): Default bundler for all apps with up to 5-10x faster Fast Refresh, and 2-5x faster builds
- Turbopack File System Caching (beta): Even faster startup and compile times for the largest apps
- React Compiler Support (stable): Built-in integration for automatic memoization
- Build Adapters API (alpha): Create custom adapters to modify the build process
- Enhanced Routing: Optimized navigations and prefetching with layout deduplication and incremental prefetching
- Improved Caching APIs: New
updateTag()
and refinedrevalidateTag()
- React 19.2: View Transitions,
useEffectEvent()
,<Activity/>
- Breaking Changes: Async params,
next/image
defaults, and more
We encourage you to try the beta and share your feedback. Your testing helps us identify issues and improve Next.js before the stable release. Please report any bugs or issues you encounter on GitHub.
Upgrade to the beta:
# Use the automated upgrade CLI
npx @next/codemod@canary upgrade beta
# ...or upgrade manually
npm install next@beta react@latest react-dom@latest
# ...or start a new project
npx create-next-app@beta
Developer Experience
Turbopack (stable)
Turbopack has reached stability for both development and production builds, and is now the default bundler for all new Next.js projects. Since its beta release earlier this summer, adoption has scaled rapidly: more than 50% of development sessions and 20% of production builds on Next.js 15.3+ are already running on Turbopack.
With Turbopack, you can expect:
- 2–5× faster production builds
- Up to 10× faster Fast Refresh
We're making Turbopack the default to bring these performance gains to every Next.js developer, no configuration required. For apps with custom webpack setups, you can continue using webpack by running:
next dev --webpack
next build --webpack
Turbopack File System Caching (beta)
Turbopack now supports filesystem caching in development, storing compiler artifacts on disk between runs for significantly faster compile times across restarts, especially in large projects.
Enable filesystem caching in your configuration:
const nextConfig = {
experimental: {
turbopackFileSystemCacheForDev: true,
},
};
export default nextConfig;
All internal Vercel apps are already using this feature, and we’ve seen notable improvements in developer productivity across large repositories.
We’d love to hear your feedback as we iterate on filesystem caching. Please try it out and share your experience.
Simplified create-next-app
create-next-app
has been redesigned with a simplified setup flow, updated project structure, and improved defaults. The new template includes the App Router by default, TypeScript-first configuration, Tailwind CSS, and ESLint.
Build Adapters API (alpha)
Following the Build Adapters RFC, we've worked with the community and deployment platforms to deliver the first alpha version of the Build Adapters API.
Build Adapters allow you to create custom adapters that hook into the build process, enabling deployment platforms and custom build integrations to modify Next.js configuration or process build output.
const nextConfig = {
experimental: {
adapterPath: require.resolve('./my-adapter.js'),
},
};
module.exports = nextConfig;
Share your feedback in the RFC discussion.
React Compiler Support (stable)
Built-in support for the React Compiler is now stable in Next.js 16 following the React Compiler's 1.0 release. The React Compiler automatically memoizes components, reducing unnecessary re-renders with zero manual code changes.
The reactCompiler
configuration option has been promoted from experimental
to stable. It is not enabled by default as we continue gathering build performance data across different application types. Expect compile times in development and during builds to be higher when enabling this option as the React Compiler relies on Babel.
const nextConfig = {
reactCompiler: true,
};
export default nextConfig;
Install the latest version of the React Compiler plugin:
npm install babel-plugin-react-compiler@latest
Core Features & Architecture
Enhanced Routing and Navigation
Next.js 16 includes a complete overhaul of the routing and navigation system, making page transitions leaner and faster.
Layout deduplication: When prefetching multiple URLs with a shared layout, the layout is downloaded once instead of separately for each Link. For example, a page with 50 product links now downloads the shared layout once instead of 50 times, dramatically reducing the network transfer size.
Incremental prefetching: Next.js only prefetches parts not already in cache, rather than entire pages. The prefetch cache now:
- Cancels requests when the link leaves the viewport
- Prioritizes link prefetching on hover or when re-entering the viewport
- Re-prefetches links when their data is invalidated
- Works seamlessly with upcoming features like Cache Components
Trade-off: You may see more individual prefetch requests, but with much lower total transfer sizes. We believe this is the right trade-off for nearly all applications. If the increased request count causes issues, please let us know. We're working on additional optimizations to inline data chunks more efficiently.
These changes require no code modifications and are designed to improve performance across all apps.
PPR and Cache Components
Next.js 16 removes the experimental Partial Pre-Rendering (PPR) flag and configuration options. PPR is being integrated into Cache Components.
Starting with Next.js 16, you can opt into PPR using the experimental.cacheComponents
configuration. There are differences in the implementation and Cache Components brings additional features and behaviors that will be documented and announced ahead of Next.js Conf and the Next.js 16 stable release.
If your application relies on PPR (
experimental.ppr = true
): Stay on the pinned version of Next.jscanary
you currently use. If you have trouble migrating, stay on your current version for now, and we will provide a migration guide ahead of the stable release.
Improved Caching APIs
Next.js 16 introduces refined caching APIs for more explicit control over cache behavior.
revalidateTag()
(updated)
revalidateTag()
now requires a cacheLife
profile as the second argument to enable stale-while-revalidate (SWR) behavior:
import { revalidateTag } from 'next/cache';
// ✅ Use built-in cacheLife profile (we recommend 'max' for most cases)
revalidateTag('blog-posts', 'max');
// Or use other built-in profiles
revalidateTag('news-feed', 'hours');
revalidateTag('analytics', 'days');
// Or use an inline object with a custom revalidation time
revalidateTag('products', { revalidate: 3600 });
// ⚠️ Deprecated - single argument form
revalidateTag('blog-posts');
The profile argument accepts built-in cacheLife
profile names (like 'max'
, 'hours'
, 'days'
) or custom profiles defined in your next.config
. You can also pass an inline { revalidate: number }
object. We recommend using 'max'
for most cases, as it enables background revalidation for long-lived content. When users request tagged content, they receive cached data immediately while Next.js revalidates in the background.
Use revalidateTag()
when you want to invalidate only properly tagged cached entries with stale-while-revalidate behavior. This is ideal for static content that can tolerate eventual consistency.
Migration guidance: Add the second argument with a
cacheLife
profile (we recommend'max'
) for SWR behavior, or useupdateTag()
in Server Actions if you need read-your-writes semantics.
updateTag()
(new)
updateTag()
is a new Server Actions-only API that provides read-your-writes semantics, expiring and immediately refreshing cached data within the same request:
'use server';
import { updateTag } from 'next/cache';
export async function updateUserProfile(userId: string, profile: Profile) {
await db.users.update(userId, profile);
// Expire cache and refresh immediately - user sees their changes right away
updateTag(`user-${userId}`);
}
This ensures interactive features reflect changes immediately. Perfect for forms, user settings, and any workflow where users expect to see their updates instantly.
refresh()
(new)
refresh()
is a new Server Actions-only API for refreshing uncached data only. It doesn't touch the cache at all:
'use server';
import { refresh } from 'next/cache';
export async function markNotificationAsRead(notificationId: string) {
// Update the notification in the database
await db.notifications.markAsRead(notificationId);
// Refresh the notification count displayed in the header
// (which is fetched separately and not cached)
refresh();
}
This API is complementary to the client-side router.refresh()
. Use it when you need to refresh uncached data displayed elsewhere on the page after performing an action. Your cached page shells and static content remain fast while dynamic data like notification counts, live metrics, or status indicators refresh.
React 19.2 and Canary Features
The App Router in Next.js 16 uses the latest React Canary release, which includes the newly released React 19.2 features and other features being incrementally stabilized. Highlights include:
- View Transitions: Animate elements that update inside a Transition or navigation
useEffectEvent
: Extract non-reactive logic from Effects into reusable Effect Event functions- Activity: Render "background activity" by hiding UI with
display: none
while maintaining state and cleaning up Effects
Learn more in the React 19.2 announcement.
Breaking Changes and Other Updates
Version Requirements
Removals
These features were previously deprecated and are now removed:
Behavior Changes
These features have new default behaviors in Next.js 16:
Deprecations
These features are deprecated in Next.js 16 and will be removed in a future version:
Additional Improvements
- Performance improvements: Significant performance optimizations for
next dev
andnext start
commands - Node.js native TypeScript for
next.config.ts
: Runnext dev
,next build
, andnext start
commands with--experimental-next-config-strip-types
flag to enable native TypeScript fornext.config.ts
.
We'll aim to share a more comprehensive migration guide ahead of the stable release in our documentation.
Feedback and Community
Share your feedback and help shape the future of Next.js:
Contributors
Next.js is the result of the combined work of over 3,000 individual developers. This release was brought to you by:
- The Next.js team: Andrew, Hendrik, Janka, Jiachi, Jimmy, Jiwon, JJ, Josh, Jude, Sam, Sebastian, Sebbie, Wyatt, and Zack.
- The Turbopack team: Benjamin, Josh, Luke, Niklas, Tim, Tobias, and Will.
- The Next.js Docs team: Delba, Rich, Ismael, and Joseph.
Huge thanks to @mischnic, @timneutkens, @unstubbable, @wyattjoh, @Cy-Tek, @lukesandberg, @OoMNoO, @ztanner, @icyJoseph, @huozhi, @gnoff, @ijjk, @povilasv, @dwrth, @obendev, @aymericzip, @devjiwonchoi, @SyMind, @vercel-release-bot, @Shireee, @eps1lon, @dharun36, @kachkaev, @bgw, @yousefdawood7, @TheAlexLichter, @sokra, @ericx0099, @leerob, @Copilot, @fireairforce, @fufuShih, @anvibanga, @hayes, @Milancen123, @martinfrancois, @lubieowoce, @gaojude, @lachlanjc, @liketiger, @styfle, @aaronbrown-vercel, @Samii2383, @FelipeChicaiza, @kevva, @m1abdullahh, @F7b5, @Anshuman71, @RobertFent, @poteto, @chloe-yan, @sireesha-siri, @brian-lou, @joao4xz, @stefanprobst, @samselikoff, @acdlite, @gwkline, @bgub, @brock-statsig, and @karlhorky for helping!
```

---

## 12. Next.js 15.5

- 日期: 2025-08-18 20:00
- 链接: https://nextjs.org/blog/next-15-5

```
Monday, August 18th 2025
Next.js 15.5
Posted byNext.js 15.5 includes Turbopack builds in beta, stable Node.js middleware, TypeScript improvements, next lint
deprecation, and deprecation warnings for Next.js 16. Highlights for this release include:
- Turbopack Builds (beta): Production turbopack builds (
next build --turbopack
) now in beta - Node.js Middleware (stable): Node.js runtime support for middleware is now stable
- TypeScript Improvements: Typed routes, route export validation, and route types helpers
next lint
: Deprecation ofnext lint
command- Next.js 16: Deprecation warnings for Next.js 16
Upgrade today, or get started with:
# Use the automated upgrade CLI
npx @next/codemod@canary upgrade latest
# ...or upgrade manually
npm install next@latest react@latest react-dom@latest
# ...or start a new project
npx create-next-app@latest
Turbopack Builds (beta)
We're excited to announce next build --turbopack
in beta. Turbopack now powers Vercel websites including vercel.com, v0.app, and nextjs.org, accelerating iteration velocity through faster preview and production deployment builds.
These applications powered by Turbopack have been battle tested serving over 1.2 billion requests since the rollout.
Performance & Production Results
One of the original design goals for Turbopack was to be able to help developers scale build performance as their applications and codebases grow. To achieve this, Turbopack was designed from the ground up to take advantage of multiple CPU cores throughout all phases of the build.
We've deployed builds with Turbopack across many Vercel products and saw consistent improvements in compilation time:
- Customer site: 2x faster on a 4 core machine
- Customer site: 2.2x faster on a 14 core machine
- Small site (10K modules): 4x faster on a 30 core machine
- Medium site (40K modules): 2.5x faster on a 30 core machine
- Large site (70K modules): 5x faster on a 30 core machine
As we rolled out Turbopack to our major web applications, we closely monitored for production performance regressions and breakages.
When compared with Webpack, our production metrics monitoring shows that sites built with Turbopack serve similar or smaller amounts of JavaScript and CSS across fewer requests, leading to comparable or better FCP, LCP and TTFB metrics.
For teams that have adopted Turbopack in development, we now recommend trying Turbopack for builds.
Known Differences
Smaller projects: On smaller machines or smaller projects, we measured marginal or neutral improvements to the build times due to Webpack's built-in persistent cache. We are currently working on a Persistent Caching solution for Turbopack to deliver on our design goal of making all builds incremental and fast.
Bundle optimization: In some edge cases, we measured that webpack produced more optimized bundles. We are tracking those scenarios and are working on closing the gap before the stable release. See the documentation on bundle sizes for more information.
CSS ordering: Due to different heuristics about side-effects handling in Turbopack, CSS files can be concatenated in a different order than webpack, leading to potential visual differences. See the documentation for a more detailed explanation and suggested solutions.
Note: These differences are documented and we're actively working on improvements. For detailed information and workarounds, see our Turbopack documentation.
As we iterate towards the stable release, please report any issues on GitHub.
Node.js Middleware (stable)
After introducing experimental support for the Node.js runtime in our 15.2 release and testing extensively on our production applications, we're excited to announce stable support for Node.js middleware runtime.
Previously, Next.js middleware only supported the Edge Runtime, which provided better performance and isolation but had limitations when integrating with Node.js-specific libraries and APIs.
import { NextRequest, NextResponse } from 'next/server';
export const config = {
runtime: 'nodejs', // Now stable!
};
export function middleware(request: NextRequest) {
// Access to full Node.js APIs and npm packages
const fs = require('fs');
const crypto = require('crypto');
// Complex authentication logic
const token = request.headers.get('authorization');
if (!isValidToken(token)) {
return NextResponse.redirect(new URL('/login', request.url));
}
return NextResponse.next();
}
function isValidToken(token: string | null): boolean {
// Use Node.js crypto for validation
// Access file system, databases, etc.
return true;
}
This change enables middleware to handle more complex use cases while maintaining the same developer experience.
Although Node.js runtime won't be the default in Next.js 16, we are exploring making it the default starting with Next.js 17 based on community feedback and usage patterns.
TypeScript Improvements
Next.js 15.5 brings major TypeScript improvements to the App Router, with full Turbopack compatibility and comprehensive type safety for routing.
Typed Routes (stable)
Typed routes provide compile-time type safety for your application's routes, catching invalid links before they reach production. This feature automatically generates types based on your file structure, ensuring that every <Link>
component points to a valid route.
This feature is available behind the typedRoutes
flag, which was previously experimental and is now stable. Statically typed routes now work with Turbopack through a new implementation that provides type safety across both Webpack and Turbopack builds:
const nextConfig = {
typedRoutes: true, // Now stable!
};
export default nextConfig;
import Link from 'next/link'
// Full type safety for route paths
<Link href="/blog/example-slug?ui=dark">Read Post</Link>
// TypeScript catches invalid routes at compile time
<Link href="/invalid-route">Broken Link</Link> // ← Type error
Route Export Validation (Turbopack)
Route export validation also works on Turbopack through a new system that generates a type guard file, validating pages, layouts, and route handlers using TypeScript's satisfies
operator.
This catches invalid exports like incorrect dynamic
values during compilation when running next build
, replacing the old Webpack plugin with a more performant solution that works across both build systems.
Route Props Helpers
Next.js automatically generates globally available PageProps
, LayoutProps
, and RouteContext
types with full parameter typing and no imports required:
Before: Manual typing and imports
import { Metadata } from 'next';
interface Props {
params: Promise<{ slug: string }>;
children: React.ReactNode;
analytics: React.ReactNode; // Manual parallel route typing
team: React.ReactNode; // Manual parallel route typing
}
export default function DashboardLayout(props: Props) {
return (
<div>
{props.children}
{props.analytics} {/* No type safety for parallel routes */}
{props.team} {/* No type safety for parallel routes */}
</div>
);
}
After: Automatic typing with parallel route support
// No need to import LayoutProps - globally available
export default function DashboardLayout(props: LayoutProps<'/dashboard'>) {
return (
<div>
{props.children}
{props.analytics} {/* Fully typed parallel route slot */}
{props.team} {/* Fully typed parallel route slot */}
</div>
);
}
The system automatically discovers routes from your file structure, supporting dynamic routes, parallel routes, and custom routes from next.config.js
. Type generation runs in both development and build modes, immediately regenerating types when your file structure changes in development, and scales efficiently to large projects by generating only a few optimized files instead of the many individual files used in the previous implementation.
next typegen
We've added a next typegen
command for manual type generation without running next dev
or next build
. This is particularly useful for external type validation scenarios.
next typegen [directory]
Previously, route types were only generated during next dev
or next build
, which meant running tsc --noEmit
directly wouldn't validate your route types. Now you can generate types independently and validate them externally:
# Generate route types first, then validate with TypeScript
next typegen && tsc --noEmit
# Or in CI workflows for type checking without building
next typegen && npm run type-check
next lint
Deprecation
Starting with Next.js 15.5, the next lint
command shows a deprecation warning and will be removed in Next.js 16. This modernizes the linting experience by transitioning to explicit ESLint configurations and introducing Biome as a fast alternative.
When creating a new Next.js project, you can now choose between ESLint (comprehensive rules), Biome (fast with fewer rules), or no linter. ESLint projects now generate explicit eslint.config.mjs
files instead of relying on the next lint
command wrapper, providing complete transparency into your linting rules.
Biome projects receive optimized configurations with Next.js and React rules plus built-in formatting capabilities. Generated package.json
scripts now call linters directly:
{
"scripts": {
// ESLint projects
"lint": "eslint", // Instead of "next lint"
"lint:fix": "eslint --fix",
// For Biome projects
"lint": "biome check",
"format": "biome format --write"
}
}
For existing projects, a new codemod automates the migration from next lint
to ESLint CLI:
npx @next/codemod@latest next-lint-to-eslint-cli .
The codemod intelligently transforms package.json
scripts while preserving functionality, mapping Next.js-specific flags like --strict
to --max-warnings 0
, and automatically installing required dependencies.
This transition gives developers direct control over their linting setup with better ecosystem compatibility.
Note:
next build
will still run a linting validation step if an ESLint config is present. This automatic linting during builds will also be removed in Next.js 16, giving you complete control over when and how linting runs.
Deprecation Warnings for Next.js 16
Next.js 15.5 introduces deprecation warnings to help you prepare for the upcoming Next.js 16 release. These warnings appear in development and build logs, giving you time to migrate before these features are removed.
legacyBehavior
for next/link
The legacyBehavior
prop for next/link
will be removed in Next.js 16. This prop was introduced as a temporary compatibility layer during the Next.js 12 to 13 transition.
// ❌ Will be removed in Next.js 16
<Link href="/about" legacyBehavior>
<a>About</a>
</Link>
// ✅ Modern approach (no changes needed)
<Link href="/about">About</Link>
Migration: Remove the legacyBehavior
prop and any child <a>
elements. The Link
component now handles styling and accessibility automatically.
AMP Support
Next.js AMP support will be removed in Next.js 16. AMP adoption has declined significantly, and maintaining this feature adds complexity to the framework. All AMP-related APIs and configurations will be removed.
// ❌ Will be removed in Next.js 16
import { useAmp } from 'next/amp';
export const config = { amp: true };
export default function AmpPage() {
const isAmp = useAmp();
return <div>AMP Page: {isAmp ? 'AMP' : 'HTML'}</div>;
}
const nextConfig = {
amp: {
// ❌ Will be removed in Next.js 16
canonicalBase: 'https://example.com',
},
};
export default nextConfig;
Migration: Remove all AMP-related code including:
export const config = { amp: true }
from pagesamp
configuration from yournext.config.ts
next/amp
hook imports and usage (useAmp
)- Any other AMP-specific APIs
Evaluate if AMP is still necessary for your use case. Most performance benefits can now be achieved through Next.js's built-in optimizations and modern web standards.
next/image
Quality Settings
Starting in Next.js 16, the quality
prop will be restricted to only 75
by default. Currently in Next.js 15, you can use any integer from 1 to 100, but Next.js 16 will require explicit configuration for qualities other than 75.
// ⚠️ Will show deprecation warning in Next.js 15.5
// when images.qualities is undefined and quality !== 75
<Image src="/photo.jpg" quality={100} alt="Photo" />
// ✅ Explicit configuration required for Next.js 16
const nextConfig = {
images: {
qualities: [75, 100], // Explicitly allow quality={100}
},
};
export default nextConfig;
Migration: If you use quality
props other than 75, explicitly configure images.qualities
in your next.config.ts
to include the quality values you need for Next.js 16.
next/image
Local Patterns
Starting in Next.js 16, using query strings with local image src
paths will require explicit configuration in images.localPatterns
. This affects images with query parameters like cache-busting or versioning.
// ⚠️ Will show deprecation warning in Next.js 15.5
// when images.localPatterns is not configured
<Image src="/photo.jpg?v=1" alt="Test" />
// ✅ Explicit configuration required for Next.js 16
const nextConfig = {
images: {
localPatterns: [
{
pathname: '/photo.jpg', // allow exact path
// omitting "search" will allow all query parameters
},
{
pathname: '/photo.jpg', // allow exact path
search: '?v=1', // allow exact query parameters
},
{
pathname: '/assets/**', // allow wildcard path
search: '', // empty search will block all query parameters
},
],
},
};
export default nextConfig;
Migration: Configure images.localPatterns
in your next.config.ts
to explicitly allow query strings in your image paths. This provides better security and performance optimization.
Timeline
These deprecation warnings will appear starting with Next.js 15.5. The features will be completely removed in Next.js 16. We recommend migrating as soon as possible to avoid issues during the upgrade.
Share your feedback and help shape the future of Next.js:
Contributors
Next.js is the result of the combined work of over 3,000 individual developers. This release was brought to you by:
- The Next.js team: Andrew, Ben, Hendrik, Janka, Jiachi, Jimmy, Jiwon, JJ, Josh, Jude, Rob, Sam, Sebastian, Sebbie, Wyatt, and Zack.
- The Turbopack team: Benjamin, Josh, Luke, Maia, Niklas, Tim, Tobias, and Will.
- The Next.js Docs team: Delba, Rich, Ismael, Joseph, and Lee.
Huge thanks to @unstubbable, @gnoff, @RobPruzan, @mischnic, @huozhi, @delbaoliveira, @styfle, @ankur-arch, @skt-t1-byungi, @ijjk, @Han5991, @SyMind, @Anas-github-acc, @hf, @bgw, @wyattjoh, @ztanner, @prateekkish, @eps1lon, @lubieowoce, @timneutkens, @acdlite, @lukesandberg, @bgub, @Cy-Tek, @padmaia, @raunofreiberg, @devjiwonchoi, @sokra, @MidnightDesign, @stephenliang, @allenzhou101, @icyJoseph, @gaojude, @remcohaszing, @wesjune, @wbinnssmith, @m1abdullahh, @Sayakie, @startracex, @chadfennell, @dlehmhus, @Jarred-Sumner, @candymask0712, @stepan662, @PuppyOne, @huperniketes, @xusd320, @MichalMoravik, @fireairforce, @kitfoster, @feedthejim, and @r34son for helping!
```

---

## 13. Next.js 15.4

- 日期: 2025-07-14 20:00
- 链接: https://nextjs.org/blog/next-15-4

```
Monday, July 14th 2025
Next.js 15.4
Posted byNext.js 15.4 includes updates to performance, stability, and Turbopack compatibility. Highlights for this release include:
- Turbopack Builds: 100% integration test compatibility for
next build --turbopack
- Stability Improvements: Numerous stability and performance improvements to Next.js and Turbopack
This blog post also includes an early preview of what's coming in Next.js 16, our next major release.
Upgrade today, or get started with:
# Use the automated upgrade CLI
npx @next/codemod@canary upgrade latest
# ...or upgrade manually
npm install next@latest react@latest react-dom@latest
# ...or start a new project
npx create-next-app@latest
Turbopack Builds
next build --turbopack
now passes all 8298 integration tests for production builds and now powers vercel.com
. This is a crucial milestone towards marking Turbopack in Next.js stable.
The team's current priority is to finish the swing on bundling optimizations via production chunking and to fix reported bugs from early adopters of the Alpha release. We've also made numerous stability and performance improvements to Turbopack under the hood.
We are confident that Turbopack will soon be ready for production use, and we're working towards a beta release in Next.js 16. If you had tried Turbopack previously, now is a good time to try again. If you run into any issues let us know on GitHub Issues.
Looking Ahead: Next.js 16
Over the past few months, we've been iterating on major improvements to Next.js, focusing on both the developer experience with Turbopack and the core capacities of the App Router with PPR
and use cache
. While we are not ready to enable those features on by default, we are looking to lay the groundwork for our users to try it out in Next.js 16 this summer.
Here’s a preview of what's coming in Next.js 16:
- Cache Components (beta): Consolidates experimental caching features (Dynamic IO,
use cache
, and Partial Prerendering) into a unifiedcacheComponents
flag, simplifying performance optimization strategies. The Next.js 16 blog post will detail our vision. - Turbopack Builds (beta): Introduces
next build --turbopack
, fully passing integration tests, and validated internally on high-traffic sites like vercel.com. Ready for expanded public beta use in Next.js 16. - Optimized Client-Side Routing: Enhances App Router navigation with smarter prefetching, improved cache invalidation strategies, and reduced bandwidth usage, resulting in faster and more responsive navigation.
- DevTools & Debugging: Adds Route Info to inspect app structure and toggle components like
loading.tsx
. Adds experimental browser log forwarding to the terminal to support AI-powered debugging workflows. - Node.js Middleware (stable): Promotes the previously experimental Node.js runtime support for Middleware, initially introduced in Next.js 15.2, to stable status.
- Deployment Adapters (alpha): Enables developers to create custom deployment adapters for finer control over build and deploy targets.
- Minor Deprecations and Changes: Deprecates Node.js 18 support, AMP, and changes to select
next/image
APIs with appropriate migration guidance.
Our goal is to make this update as smooth and straightforward as possible. We're managing these changes carefully to minimize disruption and will provide clear guidance and tools to support your transition to Next.js 16.
Preview Upcoming Features
You can start experimenting with many of these features today by using the canary
channel and enabling the following flags in your next.config.js
:
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
// Forward browser logs to the terminal for easier debugging
browserDebugInfoInTerminal: true,
// Enable new caching and pre-rendering behavior
dynamicIO: true, // will be renamed to cacheComponents in Next.js 16
// Activate new client-side router improvements
clientSegmentCache: true,
// Explore route composition and segment overrides via DevTools
devtoolSegmentExplorer: true,
// Enable support for `global-not-found`, which allows you to more easily define a global 404 page.
globalNotFound: true,
// Enable persistent caching for the turbopack dev server and build.
turbopackPersistentCaching: true,
},
};
export default nextConfig;
Notable Changes
- [Improvement] Preserve RSC query during redirects (#77963)
- [Improvement] Graceful error fallback for bots (#77916)
- [Improvement] Disallow
unstable_rootParams
in client components (#79471) - [Improvement] Fix
bodySizeLimit
errors and non-multipart actions (#77746) - [Improvement] Respond with 404 for unknown action IDs (#77012)
- [Improvement] Check cache-busting params on RSC requests (#80669)
- [Improvement] Upgrade Vercel OG to 0.7.2 (#81447)
- [Improvement] List
assert/strict
as external (#80884) - [Improvement] Omit searchParam data from
FlightRouterState
before transport (#80734) - [Improvement] Render streaming metadata on the top level (#80566)
- [Fix] Clone the config module to avoid mutation (#80573)
- [Fix] Bugfix: Propagate
staleTime
to seeded prefetch entry (#81263) - [Fix] Reinstate vary (#79939)
- [Fix] Fix interestingness detection for React Compiler (#79558)
- [Fix] Fix react compiler usefulness detector (#79480)
- [Fix] Better handle edge-case file paths in launchEditor (#79526)
- [Fix] Client router should discard stale prefetch entries for static pages (#79362)
- [Feature] Add
onInvalidate
torouter.prefetch
(#77880) - [Feature] Add
prefetch="auto"
as an alias toprefetch={undefined}
to Link (#78689) - [Feature] Support metadata in global-not-found (#78961)
- [Feature] Restart dev server from error overlay (#80060)
- [Feature] Restart dev server from indicator preferences (#80072)
- [Feature] Add
--debug-prerender
option fornext build
(#80667) - [Feature] Add htmlrewriter to server externals (#80819)
- [Feature] Allow partially prerendering intercepted dynamic routes (#80851)
- [Performance] Check files with SWC before React Compiler (#75605)
- [Performance] Improve static path generation performance and parameter handling (#81254)
- [Misc] Fix
NEXT_CPU_PROF
usage during development to allow capturing CPU traces (#81248)
Share your feedback and help shape the future of Next.js:
Contributors
Next.js is the result of the combined work of over 3,000 individual developers. This release was brought to you by:
- The Next.js team: Andrew, Ben, Hendrik, Janka, Jiachi, Jimmy, Jiwon, JJ, Josh, Jude, Rob, Sam, Sebastian, Sebbie, Wyatt, and Zack.
- The Turbopack team: Benjamin, Donny, Josh, Luke, Maia, Niklas, Tim, Tobias, and Will.
- The Next.js Docs team: Delba, Rich, Ismael, Joseph, and Lee.
Huge thanks to @sokra, @huozhi, @Marukome0743, @mischnic, @wbinnssmith, @eps1lon, @razzeee, @delbaoliveira, @kdy1, @wyattjoh, @acdlite, @ztanner, @bgw, @jantimon, @lubieowoce, @Fonger, @ospira, @gnoff, @styfle, @Cy-Tek, @timneutkens, @raunofreiberg, @devchaudhary24k, @Neschadin, @OreQr, @drewlong314, @ijjk, @praizjosh, @unstubbable, @lukesandberg, @ScriptedAlchemy, @sqidermad, @Juneezee, @devjiwonchoi, @Kamitenshi, @feedthejim, @leerob, @mauerbac, @miki-tebe, @gaearon, @mrbadri, @luwes, @lucacasonato, @M4xymm, @jirihofman, @vicb, @jackwilson323, @SyMind, @kevva, @xyf7, @gaojude, @dario-piotrowicz, @mastoj, @nicole0707, @lourd, @Karibash, @chipit24, @icyJoseph, @xusd320, @fireairforce, @GenhaoLi, @igas, @Macw07, @amannn, @bcdipesh, @r34son, @ivasilov, @lpalmes, @imskyleen, @teamleaderleo, @vitaliemiron, @agadzik, @chdeskur, @nakanoh, @luiscobot, @GameRoMan, @dferber90, @maurobonfietti, @navandstokes, @sajadtorkamani, @bobziroll, @lumirlumir, @KkOoSsTtAa, @msabramo, @sommeeeer, @schoenwaldnils, @remcohaszing, @HerringtonDarkholme, @bgub, @RobPruzan, @lmammino, @MohammedYehia, @extoci, @padmaia, @aacosta11, @vercel-release-bot, @maral, @ethanniser, @MichalMoravik, @rajrawat37, @kidonng, @dnhn, @kristian240, @rachnac-emeritus, @rortan134, and @nick20name17 for helping!
```

---

## 14. Next.js 15.3

- 日期: 2025-04-09 20:00
- 链接: https://nextjs.org/blog/next-15-3

```
Wednesday, April 9th 2025
Next.js 15.3
Posted byNext.js 15.3 includes Turbopack for builds, new client instrumentation and navigation hooks, and more:
- Turbopack for builds (alpha): Faster production builds passing 8000+ tests (99%)
- Community support for Rspack (experimental): Alternative bundler with Webpack compatibility
- Client Instrumentation hook: Early monitoring and analytics setup
- Navigation hooks: Control routing with
onNavigate
anduseLinkStatus
- TypeScript plugin improvements: Improved support for large codebases
Upgrade today, or get started with:
# Use the automated upgrade CLI
npx @next/codemod@canary upgrade latest
# ...or upgrade manually
npm install next@latest react@latest react-dom@latest
# ...or start a new project
npx create-next-app@latest
Turbopack Builds (alpha)
Following the stable release of next dev --turbopack
, over 50% of development sessions on Next.js 15 are now using Turbopack.
This release includes our alpha release of next build --turbopack
, bringing the same performance improvements from local development to production builds.
Try Turbopack for production builds by upgrading to 15.3 and running:
next build --turbopack
Functionality
99.3% of integration tests for next build
are already passing. You can track our progress towards 100% at areweturboyet.com. If your application already works with Turbopack for dev
, then it should work as-is with build
.
Turbopack builds are in alpha. We don’t recommend using them in production for mission-critical applications at this stage. Instead, try them in a preview or staging environment, or run the build locally to observe differences in bundle size and performance.
We’re actively working to close these performance gaps through scope hoisting, improved chunking, and other optimizations.
Build performance
We’ve been validating Turbopack on Vercel’s large internal monorepo and early partner codebases. One advantage of Turbopack’s architecture versus our previous Webpack implementation is that performance scales when adding CPU cores:
- At 4 cores: 28% faster than Webpack
- At 16 cores: 60% faster than Webpack
- At 30 cores: 83% faster than Webpack
These build times drop even further with our experimental work on persistent caching. We will share more on that in a future release.
Ecosystem
We’re working with commonly used integrations like Sentry to make sure they’re compatible with next build --turbopack
before the stable release. Please reach out to @leerob on X if you are a tool author who would like to work with us to ensure compatibility.
Feedback
Please share your feedback, even if it goes smoothly, to help us prepare a stable release:
- GitHub discussions for general feedback
- GitHub issues for reproductions
Turbopack configuration in next.config.ts
(stable)
Turbopack configuration in next.config.ts
has moved from experimental.turbo
to the top-level turbopack
key:
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
turbopack: {
rules: {
'*.svg': {
loaders: ['@svgr/webpack'],
as: '*.js',
},
},
},
};
export default nextConfig;
For compatibility, the experimental.turbo
option will continue to be supported until the next major release of Next.js.
For a complete list of Turbopack configuration options, see the Turbopack API Reference.
Community support for Rspack (experimental)
The Rspack team has created a community plugin for Next.js.
This provides an option for Next.js users who need near-exact Webpack API compatibility, but cannot yet move to Turbopack, to improve their local compilation and build times. We’re confident in our progress with Turbopack and will continue to provide an incremental path forward for Webpack users.
While this is not an official Next.js plugin, we are partnering with the Rspack team. Both teams will collaborate on shared foundations like SWC and Lightning CSS, benefiting all Next.js users and the broader ecosystem.
If you want to explore using Rspack with Next.js, you can use the next-rspack
adapter. We are running the adapter against our integration test suite. It currently passes ~96% of tests.
View an example or learn more in the Rspack docs.
Client Instrumentation Hook
The instrumentation-client.js|ts
file allows you to add monitoring and analytics code that runs before your application's frontend code starts executing.
This is ideal for setting up performance tracking, error monitoring, or other client-side observability tools as early as possible in the lifecycle.
// Set up performance monitoring
performance.mark('app-init');
// Initialize analytics
console.log('Analytics initialized');
// Set up error tracking
window.addEventListener('error', (event) => {
// Send to your error tracking service
reportError(event.error);
});
Place this file at the root of your project similar to server-side instrumentation.
Learn more in the instrumentation-client file documentation.
Navigation Hooks
We're introducing new navigation hooks that enhance client-side routing capabilities in Next.js 15.3, allowing you to more easily develop localized loading states and implement complex controls like navigation cancelation.
onNavigate
This event handler is a new property of the Link
component and executes during client-side navigations, giving you precise control over your application's routing behavior.
Unlike the onClick
event, which fires for all clicks, onNavigate
can be used for Single-Page App (SPA) navigations, allowing you to execute code or even cancel navigation with preventDefault()
.
This API can be used to implement transition animations, navigation guards, or analytics tracking that should only run during actual page transitions.
Learn more by visiting the onNavigate
documentation.
useLinkStatus
The useLinkStatus
Client Component hook returns a pending
boolean that indicates when navigation is in progress, giving you localized control over loading states.
This API is modeled after useFormStatus
from React, and is helpful for adding custom loading indicators during page transitions, especially when prefetching is disabled or when your linked routes don't have dedicated loading states.
By placing a component that uses useLinkStatus
as a descendant of your <Link>
component, you can create responsive UI elements that react to navigation events in real-time.
Learn more by visiting the useLinkStatus
documentation.
TypeScript Plugin Performance Improvements
The Next.js TypeScript language server plugin (LSP) is now faster.
The LSP provides inline Intellisense features such as server/client boundary validation, component prop hints, configuration autocompletion, and error detection for disallowed APIs in React Server Components. In very large codebases, the plugin could previously cause the TypeScript language service to hang or crash.
We’ve made significant performance improvements to resolve these issues. In our internal testing, plugin response times have improved ~60% with no freezing or crashes.
Other Changes
- [Feature] Support
new URL()
inimages.remotePatterns
(#77692) - [Feature] Viewport options are now separate from
metadata
(#77427) - [Feature] Add
unstable_dynamicOnHover
option (#77866) - [Feature] Add support for Pinterest Rich Pins (#76988)
- [Improvement] Make revalidate work when followed by a redirect in Route Handlers (#77090)
- [Improvement] Ensure strong consistency after calling revalidate in Server Actions (#76885)
- [Improvement] Upgrade
sharp
for faster PNG to AVIF conversion (#77839)
Contributors
Next.js is the result of the combined work of over 3,000 individual developers. This release was brought to you by:
- The Next.js team: Andrew, Hendrik, Janka, Jiachi, Jimmy, Jiwon, JJ, Josh, Jude, Sam, Sebastian, Sebbie, Wyatt, and Zack.
- The Turbopack team: Benjamin, Donny, Josh, Maia, Niklas, Tim, Tobias, and Will.
- The Next.js Docs team: Delba, Rich, Ismael, and Lee.
Huge thanks to @raunofreiberg, @huozhi, @ijjk, @timneutkens, @gaojude, @leerob, @mezotv, @bgw, @samcx, @ztanner, @sokra, @mischnic, @wbinnssmith, @kdy1, @unstubbable, @ahabhgk, @ScriptedAlchemy, @SukkaW, @wyattjoh, @eps1lon, @Amirroid, @Netail, @lubieowoce, @gnoff, @jackwilson323, @acdlite, @sbougerel, @kevva, @kasperpeulen, @Cy-Tek, @dvoytenko, @husseinraoouf, @isBatak, @iamkd, @delbaoliveira, @jantimon, @padmaia, @Bernardoow, @styfle, @devjiwonchoi, @JamBalaya56562, and @Marukome0743 for helping!
```

---

## 15. Building APIs with Next.js

- 日期: 2025-02-28 14:00
- 链接: https://nextjs.org/blog/building-apis-with-nextjs

```
Friday, February 28th 2025
Building APIs with Next.js
Posted byThis guide will cover how you can build APIs with Next.js, including setting up your project, understanding the App Router and Route Handlers, handling multiple HTTP methods, implementing dynamic routing, creating reusable middleware logic, and deciding when to spin up a dedicated API layer.
- 1. Getting started
- 2. Why (and when) to build APIs with Next.js
- 3. Creating an API with Route Handlers
- 4. Working with Web APIs
- 5. Dynamic routes
- 6. Using Next.js as a proxy or forwarding layer
- 7. Building shared “middleware” logic
- 8. Deployment and “SPA Mode” considerations
- 9. When to skip creating an API endpoint
- 10. Putting It All Together
- Conclusion
- Frequently Asked Questions
1. Getting started
1.1 Create a Next.js app
If you’re starting fresh, you can create a new Next.js project using:
npx create-next-app@latest --api
Note: The
--api
flag automatically includes an exampleroute.ts
in your new project’sapp/
folder, demonstrating how to create an API endpoint.
1.2 App Router vs. Pages Router
- Pages Router: Historically, Next.js used
pages/api/*
for APIs. This approach relied on Node.js request/response objects and an Express-like API. - App Router (Default): Introduced in Next.js 13, the App Router fully embraces web standard Request/Response APIs. Instead of
pages/api/*
, you can now placeroute.ts
orroute.js
files anywhere inside theapp/
directory.
Why switch? The App Router’s “Route Handlers” lean on the Web Platform Request/Response APIs rather than Node.js-specific APIs. This simplifies learning, reduces friction, and helps you reuse your knowledge across different tools.
2. Why (and when) to build APIs with Next.js
-
Public API for Multiple Clients
- You can build a public API that’s consumed by your Next.js web app, a separate mobile app, or any third-party service. For example, you might fetch from /api/users both in your React website and a React Native mobile app.
-
Proxy to an Existing Backend
- Sometimes you want to hide or consolidate external microservices behind a single endpoint. Next.js Route Handlers can act as a proxy or middle layer to another existing backend. For instance, you might intercept requests, handle authentication, transform data, and then pass the request along to an upstream API.
-
Webhooks and Integrations
- If you receive external callbacks or webhooks (e.g., from Stripe, GitHub, Twilio), you can handle them with Route Handlers.
-
Custom Authentication
- If you need sessions, tokens, or other auth logic, you can store cookies, read headers, and respond with the appropriate data in your Next.js API layer.
Note: If you only need server-side data fetching for your own Next.js app (and you don’t need to share that data externally), Server Components might be sufficient to fetch data directly during render—no separate API layer is required.
3. Creating an API with Route Handlers
3.1 Basic file setup
In the App Router (app/
), create a folder that represents your route, and inside it, a route.ts
file.
For example, to create an endpoint at /api/users
:
app
└── api
└── users
└── route.ts
3.2 Multiple HTTP methods in one file
Unlike the Pages Router API routes (which had a single default export), you can export multiple functions representing different HTTP methods from the same file.
export async function GET(request: Request) {
// For example, fetch data from your DB here
const users = [
{ id: 1, name: 'Alice' },
{ id: 2, name: 'Bob' }
];
return new Response(JSON.stringify(users), {
status: 200,
headers: { 'Content-Type': 'application/json' }
});
}
export async function POST(request: Request) {
// Parse the request body
const body = await request.json();
const { name } = body;
// e.g. Insert new user into your DB
const newUser = { id: Date.now(), name };
return new Response(JSON.stringify(newUser), {
status: 201,
headers: { 'Content-Type': 'application/json' }
});
}
Now, sending a GET request to /api/users
returns your list of users, while a POST
request to the same URL will insert a new one.
4. Working with Web APIs
4.1 Directly using Request & Response
By default, your Route Handler methods (GET
, POST
, etc.) receive a standard Request object, and you must return a standard Response object.
4.2 Query parameters
import { NextRequest } from 'next/server';
export function GET(request: NextRequest) {
const searchParams = request.nextUrl.searchParams;
const query = searchParams.get('query'); // e.g. `/api/search?query=hello`
return new Response(
JSON.stringify({ result: `You searched for: ${query}` }),
{
headers: { 'Content-Type': 'application/json' },
},
);
}
4.3 Headers and cookies
import { NextRequest } from 'next/server';
import { cookies, headers } from 'next/headers';
export async function GET(request: NextRequest) {
// 1. Using 'next/headers' helpers
const cookieStore = await cookies();
const token = cookieStore.get('token');
const headersList = await headers();
const referer = headersList.get('referer');
// 2. Using the standard Web APIs
const userAgent = request.headers.get('user-agent');
return new Response(JSON.stringify({ token, referer, userAgent }), {
headers: { 'Content-Type': 'application/json' },
});
}
The cookies()
and headers()
functions can be helpful if you plan to re-use shared logic across other server-side code in Next.js. You'll notice Next.js also provides NextRequest
and NextResponse
which extend the base Web APIs.
5. Dynamic routes
To create dynamic paths (e.g. /api/users/:id
), use Dynamic Segments in your folder structure:
app
└── api
└── users
└── [id]
└── route.ts
This file corresponds to a URL like /api/users/123
, with the 123
captured as a parameter.
import { NextRequest } from 'next/server';
export async function GET(
request: NextRequest,
{ params }: { params: Promise<{ id: string }> },
) {
const id = (await params).id;
// e.g. Query a database for user with ID `id`
return new Response(JSON.stringify({ id, name: `User ${id}` }), {
status: 200,
headers: { 'Content-Type': 'application/json' },
});
}
export async function DELETE(
request: NextRequest,
{ params }: { params: Promise<{ id: string }> },
) {
const id = (await params).id;
// e.g. Delete user with ID `id` in DB
return new Response(null, { status: 204 });
}
Here, params.id
gives you the dynamic segment.
6. Using Next.js as a proxy or forwarding layer
A common scenario is proxying an existing backend service. You can authenticate requests, handle logging, or transform data before sending it to a remote server or backend:
import { NextRequest } from 'next/server';
export async function GET(request: NextRequest) {
const response = await fetch('https://example.com/api/data', {
// Optional: forward some headers, add auth tokens, etc.
headers: { Authorization: `Bearer ${process.env.API_TOKEN}` },
});
// Transform or forward the response
const data = await response.json();
const transformed = { ...data, source: 'proxied-through-nextjs' };
return new Response(JSON.stringify(transformed), {
headers: { 'Content-Type': 'application/json' },
});
}
Now your clients only need to call /api/external
, and Next.js will handle the rest. This is also sometimes called a “Backend for Frontend” or BFF.
7. Building shared “middleware” logic
If you want to apply the same logic (e.g. authentication checks, logging) across multiple Route Handlers, you can create reusable functions that wrap your handlers:
import { NextRequest } from 'next/server';
type Handler = (req: NextRequest, context?: any) => Promise<Response>;
export function withAuth(handler: Handler): Handler {
return async (req, context) => {
const token = req.cookies.get('token')?.value;
if (!token) {
return new Response(JSON.stringify({ error: 'Unauthorized' }), {
status: 401,
headers: { 'Content-Type': 'application/json' },
});
}
// If authenticated, call the original handler
return handler(req, context);
};
}
Then in your Route Handler:
import { NextRequest } from 'next/server';
import { withAuth } from '@/lib/with-auth';
async function secretGET(request: NextRequest) {
return new Response(JSON.stringify({ secret: 'Here be dragons' }), {
headers: { 'Content-Type': 'application/json' },
});
}
export const GET = withAuth(secretGET);
8. Deployment and “SPA Mode” considerations
8.1 Standard Node.js deployment
The standard Next.js server deployment using next start enables you to use features like Route Handlers, Server Components, Middleware and more – while taking advantage of dynamic, request time information.
There is no additional configuration required. See Deploying for more details.
8.2 SPA/Static Export
Next.js also supports outputting your entire site as a static Single-Page Application (SPA).
You can enable this by setting:
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
output: 'export',
};
export default nextConfig;
In static export mode, Next.js will generate purely static HTML, CSS, and JS. You cannot run server-side code (like API endpoints). If you still need an API, you’d have to host it separately (e.g., a standalone Node.js server).
Note:
- GET Route Handlers can be statically exported if they don’t rely on dynamic request data. They become static files in your out folder.
- All other server features (dynamic requests, rewriting cookies, etc.) are not supported in a pure SPA export.
8.3 Deploying APIs on Vercel
If you are deploying your Next.js application to Vercel, we have a guide on deploying APIs. This includes other Vercel features like programmatic rate-limiting through the Vercel Firewall. Vercel also offers Cron Jobs, which are commonly needed with API approaches.
9. When to skip creating an API endpoint
With the App Router’s React Server Components, you can fetch data directly on the server without exposing a public endpoint:
// (Server Component)
export default async function UsersPage() {
// This fetch runs on the server (no client-side code needed here)
const res = await fetch('https://api.example.com/users');
const data = await res.json();
return (
<main>
<h1>Users</h1>
<ul>
{data.map((user: any) => (
<li key={user.id}>{user.name}</li>
))}
</ul>
</main>
);
}
If your data is only used inside your Next.js app, you may not need a public API at all.
10. Putting It All Together
- Create a new Next.js project:
npx create-next-app@latest --api
. - Add Route Handlers inside the
app/
directory (e.g.,app/api/users/route.ts
). - Export HTTP methods (
GET
,POST
,PUT
,DELETE
, etc.) in the same file. - Use Web Standard APIs to interact with the
Request
object and return aResponse
. - Build a public API if you need other clients to consume your data, or to proxy a backend service.
- Fetch your new API routes from the client (e.g., within a Client Component or with
fetch('/api/...')
). - Or skip creating an API altogether if a Server Component can just fetch data.
- Add a shared “middleware” pattern (e.g.,
withAuth()
) for auth or other repeated logic. - Deploy to a Node.js-capable environment for server features, or export statically if you only need a static SPA.
Conclusion
Using the Next.js App Router and Route Handlers gives you a flexible, modern way to build APIs that embrace the Web Platform directly. You can:
- Create a full public API to be shared by web, mobile, or third-party clients.
- Proxy and customize calls to existing external services.
- Implement a reusable “middleware” layer for authentication, logging, or any repeated logic.
- Dynamically route requests using the
[id]
segment folder structure.
Frequently Asked Questions
What about Server Actions?
You can think of Server Actions like automatically generated POST
API routes that can be called from the client.
They are designed for mutation operations, such as creating, updating, or deleting data. You call a Server Action like a normal JavaScript function, versus making an explicit fetch
to a defined API route.
While there is still a network request happening, you don't need to manage it explicitly. The URL path is auto-generated and encrypted, so you can't manually access a route like /api/users
in the browser.
If you plan to use Server Actions and expose a public API, we recommend moving the core logic to a Data Access Layer and calling the same logic from both the Server Action and the API route.
Can I use TypeScript with Route Handlers?
Yes, you can use TypeScript with Route Handlers. For example, defining the Request
and Response
types in your route
file.
Learn more about TypeScript with Next.js.
What are the best practices for authentication?
Learn more in our authentication documentation.
```

---

## 16. Next.js 15.2

- 日期: 2025-02-26 20:00
- 链接: https://nextjs.org/blog/next-15-2

```
Wednesday, February 26th 2025
Next.js 15.2
Posted byNext.js 15.2 includes updates for debugging errors, metadata, Turbopack, and more:
- Redesigned error UI and improved stack traces: A redesigned debugging experience
- Streaming metadata: Async metadata will no longer block page rendering or client-side page transitions
- Turbopack performance improvements: Faster compile times and reduced memory usage
- React View Transitions (experimental): Experimental support for React's new View Transitions API
- Node.js Middleware (experimental): Experimental support for using the Node.js runtime in Middleware
Upgrade today, or get started with:
# Use the automated upgrade CLI
npx @next/codemod@canary upgrade latest
# ...or upgrade manually
npm install next@latest react@latest react-dom@latest
# ...or start a new project
npx create-next-app@latest
Redesigned error UI and improved stack traces
We've added both visual and quality improvements to errors you may encounter while building your application. Let's walk through each area of improvements:
Error overlay
We've overhauled the UI and presentation of error messages in Next.js, making them easier to understand. The new design highlights the core details of the error—such as the message, the relevant code frame, and the call stack—while reducing noise from code in libraries or dependencies. This means you can quickly get to the root of what went wrong and start fixing it faster.
Leveraging the newly introduced owner stacks feature in React, we're now able to provide higher fidelity into where your errors are coming from. Next.js will now be able to surface the subcomponent responsible for throwing the error, skipping over intermediary elements that weren't responsible for creating the element that caused the error.
We're also making it easier to customize your indicator preferences without needing to add additional configuration.
We've added a feedback section at the bottom of error overlays that lets you rate how helpful the error message was. Your opinion helps us understand common pain points and improve error messages to make debugging easier.
Dev indicator
We've consolidated development information into a new, streamlined indicator that shows details like rendering mode and build status.
During compilation, you'll notice a dimmed, animated Next.js logo when navigating between routes. The logo brightens once compilation is complete and React begins rendering, providing a visual cue of your application's state.
Opening the dev indicator now displays:
- Your current route's rendering mode (static/dynamic)
- Turbopack compilation status
- Active errors with quick access to the error overlay
Future updates will expand this menu to include:
- PPR (Partial Prerendering) debugging tools
- Cache monitoring features
- Additional developer tooling
This unified approach puts all crucial development information in one accessible location. We'll continue to refine and expand this feature in future releases based on your feedback.
Streaming metadata
It can often be necessary to fetch dynamic data, or perform some async operation, in generateMetadata
. In prior versions of Next.js, this metadata needed to finish generating before the initial UI would be sent so it could be included in the document <head>
.
This meant that for many pages where a fast initial UI was available, the initial paint was still delayed by data requirements that did not affect what the user would see visually. We've improved this in 15.2 by allowing the initial UI to be sent to the browser even before generateMetadata
has completed.
However, to maintain compatibility with bots and crawlers that expect metadata to be available in the <head>
of the document, we continue to delay sending HTML to certain bot user agents. If you need more fine-grained control over which bots receive this treatment, you can customize the regex used to serve them via the htmlLimitedBots
option in next.config.js
.
Learn more about streaming metadata.
Turbopack performance improvements
Turbopack was marked stable with Next.js 15.
We've been working on improving Turbopack's performance, particularly in scenarios without persistent caching. As part of this release, we've introduced the following enhancements:
- Faster compile times: Early adopters have reported up to 57.6% faster compile times when accessing routes compared to Next.js 15.1.
- Reduced memory usage: For the vercel.com application, we observed a 30% decrease in memory usage during local development.
With these improvements, Turbopack should now be faster than Webpack in virtually all cases. If you encounter a scenario where this isn't true for your application, please reach out—we want to investigate these.
We've also made progress on persistent caching and production builds. Although these features aren't ready for an experimental release yet, we've started testing them on real-world projects. We'll share more detailed metrics once they're available for broader use.
React View Transitions (experimental)
We've added a feature flag to enable the new experimental View Transitions API in React. This new API allows you to animate between different views and components in your application.
To enable this feature, add the following to your next.config.js
:
module.exports = {
experimental: {
viewTransition: true,
},
};
Note: This feature is highly experimental and may change in future releases.
For more information on how to use this feature, please refer to the original View Transition pull request in the React repository. This work builds on the native browser implementation of View Transitions.
We will be publishing more documentation and examples as stability progresses.
Node.js Middleware (experimental)
We've been working on a new experimental flag to allow using the Node.js runtime for the Next.js Middleware.
To enable this feature, add the following to your next.config.js
:
module.exports = {
experimental: {
nodeMiddleware: true,
},
};
You can then specify the Node.js runtime in your Middleware config
export:
import bcrypt from 'bcrypt';
const API_KEY_HASH = process.env.API_KEY_HASH; // Pre-hashed API key in env
export default async function middleware(req) {
const apiKey = req.headers.get('x-api-key');
if (!apiKey || !(await bcrypt.compare(apiKey, API_KEY_HASH))) {
return new Response('Forbidden', { status: 403 });
}
console.log('API key validated');
}
export const config = {
runtime: 'nodejs',
};
Note: This feature is not yet recommended for production use. Therefore, Next.js will throw an error unless you are using the
next@canary
release instead of the stable release.
We are planning to take this opportunity to improve and reshape the Middleware API. If you have any suggestions or requests, please let us know. Node.js Middleware was a top community request and we are excited to have this addressed.
Coming soon
- "use cache" (beta): We've been working on stabilizing
"use cache"
as a standalone feature. Stay tuned for more details in the coming releases. Learn more about"use cache"
. - Turbopack persistent caching (experimental): We've been dogfooding persistent caching at Vercel with positive performance improvements. Once we've stabilized it further, we'll release it behind a feature flag for additional feedback and testing.
Other Changes
- [Feature] Add
--api
flag to create a headless API-only withcreate-next-app
(PR) - [Feature] Add support for
images.qualities
withnext/image
(PR) - [Deprecation] Warn about i18n configuration deprecation in App Router (PR)
- [Improvement] Improve lint performance of
no-html-link-for-pages
(PR) - [Improvement] Emit build error if
"use action"
directive is incorrectly used (PR) - [Improvement] Display
global-error
alongside dev overlay during development (PR) - [Improvement] Allow disabling HTTP request logs in development server (PR)
- [Improvement] Add pagination SEO link tags (PR)
- [Improvement] Improve JSDocs for
metadata
and<Link>
components (PR) - [Improvement] Middleware should match
next/image
requests (PR) - [Improvement] Add hostname to default error boundary message (PR)
- [Improvement] Send errors not handled by explicit error boundaries through
reportError
(PR)
Contributors
Next.js is the result of the combined work of over 3,000 individual developers. This release was brought to you by:
- The Next.js team: Andrew, Hendrik, Janka, Jiachi, Jimmy, Jiwon, JJ, Josh, Jude, Sam, Sebastian, Sebbie, Wyatt, and Zack.
- The Turbopack team: Benjamin, Donny, Maia, Niklas, Tim, Tobias, and Will.
- The Next.js Docs team: Delba, Rich, Ismael, and Lee.
Huge thanks to @mischnic, @Marukome0743, @JamBalaya56562, @creationix, @noreiller, @styfle, @abdonrd, @ollyw, @aymericzip, @davidhu2000, @attilarepka, @devpla, @dydals3440, @huozhi, @wbinnssmith, @suu3, @PapatMayuri, @Sahil4883, @abyii, @molebox, @sokra, @maciej-ka, @abvthecity, @damiensedgwick, @alitas, @RiskyMH, @ytreister, @sommeeeer, @n1ckoates, @yongholeeme, @spidersouris, @gurkerl83, @cassiossantos, @Netail, @tknickman, @eur00t, @cseas, @nnnnoel, @Manoj-M-S, @lfades, @matmannion, @mikeboensel, @nphmuller, @apostolos, @k15a, @pavelee, @locothedev, @vexcat, @Zach-Jaensch, @decepulis, @gadcam, @lukahartwig, @jsanford8, @RobinMalfait, @raunofreiberg, @mohsen1, @skushagra, @amannn, @HQidea, @jrandolf, @smit-err, @littledivy, @k35o, @martinsione, @CvX, @msereniti, @Timer, @Iftee97, @chibicode, @RobPruzan, @PlagueFPS, @bjunix, @maximevtush, @michaelven, @sedlukha, @johannpinson, @AxelUser, @Nayeem-XTREME, @IcaroG, @blurrah, @lachlanjc, @ashi009, @conico974, @raphaelcosta, @dulmandakh, @khuezy, @Knoa0405, @wangsijie, @stefanprobst, @wentsul, @loopy-lim, @bratvanov, @hedgeday, and @cassian-goode for helping!
```

---

## 17. Composable Caching with Next.js

- 日期: 2025-01-03 14:00
- 链接: https://nextjs.org/blog/composable-caching

```
Friday, January 3rd 2025
Composable Caching with Next.js
Posted byWe’re working on a simple and powerful caching model for Next.js. In a previous post, we talked about our journey with caching and how we’ve arrived at the 'use cache'
directive.
This post will discuss the API design and benefits of 'use cache'
.
What is 'use cache'
?
'use cache'
makes your application faster by caching data or components as needed.
It’s a JavaScript “directive”—a string literal you add in your code—which signals to the Next.js compiler to enter a different “boundary”. For example, going from the server to the client.
This is a similar idea to React directives like 'use client'
and 'use server'
. Directives are compiler instructions that define where code should run, allowing the framework to optimize and orchestrate individual pieces for you.
How does it work?
Let’s start with a simple example:
async function getUser(id) {
'use cache';
let res = await fetch(`https://api.vercel.app/user/${id}`);
return res.json();
}
Behind the scenes, Next.js transforms this code into a server function due to the 'use cache'
directive. During compilation, the “dependencies” of this cache entry are found and used as part of the cache key.
For example, id
becomes part of the cache key. If we call getUser(1)
multiple times, we return the memoized output from the cached server function. Changing this value will create a new entry in the cache.
Let’s look at an example using the cached function in a server component with a closure.
function Profile({ id }) {
async function getNotifications(index, limit) {
'use cache';
return await db
.select()
.from(notifications)
.limit(limit)
.offset(index)
.where(eq(notifications.userId, id));
}
return <User notifications={getNotifications} />;
}
This example is more difficult. Can you spot all the dependencies which need to be part of the cache key?
The arguments index
and limit
make sense—if these values change, we select a different slice of the notifications. However, what about the user id
? It’s value is coming from the parent component.
The compiler is able to understand getNotifications
also depends on id
, and it’s value is automatically included in the cache key. This prevents an entire category of caching issues from incorrect or missing dependencies in the cache key.
Why not use a cache function?
Let’s revisit the last example. Could we instead use a cache()
function instead of a directive?
function Profile({ id }) {
async function getNotifications(index, limit) {
return await cache(async () => {
return await db
.select()
.from(notifications)
.limit(limit)
.offset(index)
// Oops! Where do we include id in the cache key?
.where(eq(notifications.userId, id));
});
}
return <User notifications={getNotifications} />;
}
A cache()
function wouldn’t be able to look into the closure and see the id
value should be part of the cache key. You would need to manually specify that id
is part of your key. If you forget to do so, or do it incorrectly, you risk cache collisions or stale data.
Closures can capture all sorts of local variables. A naive approach could accidentally bake in (or omit) variables you didn’t intend to. That can lead to caching the wrong data, or it might risk cache poisoning if sensitive info bleeds into the cache key.
'use cache'
gives the compiler enough context to handle closures safely and produce cache keys correctly. A runtime-only solution, like cache()
, would require you to do everything manually—and it’s easy to make mistakes. By contrast, a directive can be statically analyzed to reliably handle all your dependencies under the hood.
How are non-serialized input values handled?
We have two different types of input values to cache:
- Serializable: Here, “serializable” means an input can be turned into a stable, string-based format without losing meaning. While many people think first of
JSON.stringify
, we actually use React’s serialization (e.g., via Server Components) to handle a broader range of inputs—including promises, circular data structures, and other complex objects. This goes beyond what plain JSON can do. - Non-serializable: These inputs are not part of the cache key. When we attempt to cache these values, we return a server "reference". This reference is then used by Next.js to restore back the original value at runtime.
Let’s say we remembered to include id
in the cache key:
await cache(async () => {
return await db
.select()
.from(notifications)
.limit(limit)
.offset(index)
.where(eq(notifications.userId, id));
}, [id, index, limit]);
This works if the input values can be serialized. But if id
was a React element or more complex value, we’d have to manually serialize the input keys. Consider a server component which fetches the current user based on an id
prop:
async function Profile({ id, children }) {
'use cache';
const user = await getUser(id);
return (
<>
<h1>{user.name}</h1>
{/* Changing children doesn’t break the cache... why? */}
{children}
</>
);
}
Let’s step through how this works:
- During compilation, Next.js sees the
'use cache'
directive and transforms the code to create a special server function that supports caching. No caching happens during compilation, but rather Next.js is setting up the mechanism needed for runtime caching. - When your code calls the "cache function", Next.js serializes the function's arguments. Anything that is not directly serializable, like JSX, is replaced with a "reference" placeholder.
- Next.js checks whether a cached result exists for the given serialized arguments. If no result is found, the function computes the new value to cache.
- After the function finishes, the return value is serialized. Non-serializable parts of the return value are turned back into references.
- The code which called the cache function deserializes the output and evaluates the references. This allows Next.js to swap the references with their actual objects or values, meaning non-serializable inputs like
children
can keep their original, uncached values.
This means we can safely cache just the <Profile>
component and not the children. On subsequent renders, getUser()
is not called again. The value of children
might be dynamic or a separately cached element with a different cache life. This is composable caching.
This seems familiar…
If you’re thinking “that feels like the same model of server and client composition”—you’re absolutely right. This is sometimes called the “donut” pattern:
- The outer part of the donut is a server component that handles data fetching or heavy logic.
- The hole in the middle is a child component that might have some interactivity
export default function Page() {
return (
<ServerComponent>
{/* Create a hole to the client */}
<ClientComponent />
<ServerComponent />
);
}
'use cache'
is the same. The donut is the outer component’s cached value and the hole is the references that get filled in at runtime. This is why changing children
does not invalidate the entire cached output. The children are just some reference that gets filled in later.
What about tagging and invalidation?
You can define the life of the cache with different profiles. We include a set of default profiles, but you can define your own custom values if desired.
async function getUser(id) {
'use cache';
cacheLife('hours');
let res = await fetch(`https://api.vercel.app/user/${id}`);
return res.json();
}
To invalidate a specific cache entry, you can tag the cache and then call revalidateTag()
. One powerful pattern is that you can tag the cache after you have fetched your data (e.g. from a CMS):
async function getPost(postId) {
'use cache';
let res = await fetch(`https://api.vercel.app/blog/${postId}`);
let data = await res.json();
cacheTag(postId, data.authorId);
return data;
}
Simple and powerful
Our goal with 'use cache'
is to make authoring caching logic simple and powerful.
- Simple: You can create cache entries with local reasoning. You don’t need to worry about global side effects, like forgotten cache key entries or unintended changes to other parts of your codebase.
- Powerful: You can cache more than just statically analyzable code. For example, values which might change at runtime, yet you still want to cache the output result after it’s been evaluated.
'use cache
is still experimental inside Next.js. We’d love your early feedback as you test it out.
```

---

## 18. Next.js 15.1

- 日期: 2024-12-10 20:00
- 链接: https://nextjs.org/blog/next-15-1

```
Tuesday, December 10th 2024
Next.js 15.1
Posted byNext.js 15.1 brings core upgrades, new APIs, and improvements to the developer experience. Key updates include:
- React 19 (stable): Support for React 19 is officially available in both Pages Router & App Router.
- Improved Error Debugging: Enhanced DX and better source maps for the browser and the terminal.
after
(stable): New API to execute code after a response has finished streaming.forbidden
/unauthorized
(experimental): New APIs to enable more granular authentication error handling.
Upgrade today, or get started with:
# Use the automated upgrade CLI
npx @next/codemod@canary upgrade latest
# ...or upgrade manually
npm install next@latest react@latest react-dom@latest
# ...or start a new project
npx create-next-app@latest
React 19 (stable)
Next.js 15.1 now fully supports React 19:
- For the Pages Router: you can now use React 19 stable without needing the Release Candidate or Canary releases, alongside continued support for React 18.
- For the App Router: we will continue to provide React Canary releases built-in. These include all the stable React 19 changes, as well as newer features being validated in frameworks, prior to a new React release.
Since the Next.js 15 release, a significant addition to React 19 was “sibling pre-warming”.
For a comprehensive overview of React 19’s updates, please refer to the official React 19 blog post.
Improved Error Debugging
We’ve made improvements to error debugging in Next.js, ensuring you can quickly locate the source of issues, whether they appear in the terminal, browser, or attached debuggers. These enhancements apply to both Webpack and Turbopack (now stable with Next.js 15).
Source Maps Enhancements
Errors are now easier to trace back to their origin through the improved use of source maps. We’ve implemented the ignoreList
property of source maps, which allows Next.js to hide stack frames for external dependencies, making your application code the primary focus.
For slightly more accurate source mapping of method names, we suggest adopting Turbopack (now stable), which has improved handling and detection of source maps over Webpack.
For library authors: We recommend populating the
ignoreList
property in sourcemaps when publishing your libraries, especially if they are configured as external (e.g. in theserverExternalPackages
config).
Collapsed Stack Frames
We’ve improved the logic for collapsing stack frames to highlight the most relevant parts of your code.
- In the browser and error overlay: Stack frames from third-party dependencies are hidden by default, focusing on your application code. You can reveal the hidden frames by clicking “Show ignored frames” in the devtools or the overlay.
- In the terminal: Third-party dependency frames are also collapsed by default, and error formatting now aligns with the browser output for a consistent debugging experience. Errors are replayed in the browser to ensure you don’t miss important information during development if you need the entire stack trace.
Enhanced Profiling
Ignored stack frames are also recognized by built-in browser profilers. This makes profiling your application easier, allowing you to pinpoint slow functions in your code without noise from external libraries.
Improved with the Edge Runtime
When using the Edge runtime, errors are now displayed consistently across development environments, ensuring seamless debugging. Previously, logged errors would only include the message and not the stack.
Before and after
Terminal Before:
⨯ app/page.tsx (6:11) @ eval
⨯ Error: boom
at eval (./app/page.tsx:12:15)
at Page (./app/page.tsx:11:74)
at AsyncLocalStorage.run (node:async_hooks:346:14)
at stringify (<anonymous>)
at AsyncLocalStorage.run (node:async_hooks:346:14)
at AsyncResource.runInAsyncScope (node:async_hooks:206:9)
digest: "380744807"
4 | export default function Page() {
5 | const throwError = myCallback(() => {
> 6 | throw new Error('boom')
| ^
7 | }, [])
8 |
9 | throwError()
GET / 500 in 2354ms
Terminal After:
⨯ Error: boom
at eval (app/page.tsx:6:10)
at Page (app/page.tsx:5:32)
4 | export default function Page() {
5 | const throwError = myCallback(() => {
> 6 | throw new Error('boom')
| ^
7 | }, [])
8 |
9 | throwError() {
digest: '225828171'
}
Error Overlay Before
Error Overlay After
These improvements make errors clearer and more intuitive, allowing you to focus your time building your application rather than debugging.
We’re also thrilled to announce the introduction of a redesigned UI for the error overlay, coming in upcoming releases.
after
(stable)
The after()
API is now stable following its introduction in the first Next.js 15 RC.
after()
provides a way to perform tasks such as logging, analytics, and other system synchronization after the response has finished streaming to the user, without blocking the primary response.
Key changes
Since its introduction, we’ve stabilized after()
and addressed feedback including:
- Improved support for self-hosted Next.js servers.
- Bug fixes for scenarios where
after()
interacted with other Next.js features. - Enhanced extensibility, enabling other platforms to inject their own
waitUntil()
primitives to powerafter()
. - Support for runtime APIs such as
cookies()
andheaders()
in Server Actions and Route Handlers.
import { after } from 'next/server';
import { log } from '@/app/utils';
export default function Layout({ children }) {
// Secondary task
after(() => {
log();
});
// Primary task
return <>{children}</>;
}
Read more about the after
API and how to leverage it in the documentation.
forbidden
and unauthorized
(experimental)
Next.js 15.1 includes two experimental APIs, forbidden()
and unauthorized()
, based on community feedback.
We’d love your feedback — please try it in your development environments and share your thoughts in this discussion thread.
Overview
If you’re familiar with the App Router, you’ve likely used notFound()
to trigger 404 behavior alongside the customizable not-found.tsx
file. With version 15.1, we’re extending this approach to authorization errors:
• forbidden()
triggers a 403 error with customizable UI via forbidden.tsx
.
• unauthorized()
triggers a 401 error with customizable UI via unauthorized.tsx
.
Good to know: As with
notFound()
errors, the status code will be200
if the error is triggered after initial response headers have been sent. Learn more.
Enabling the feature
As this feature is still experimental, you’ll need to enable it in your next.config.ts
file:
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
authInterrupts: true,
},
};
export default nextConfig;
Note:
next.config.ts
support was introduced in Next.js 15. Learn more.
Using forbidden()
and unauthorized()
You can use forbidden()
and unauthorized()
in Server Actions, Server Components, Client Components, or Route Handlers. Here’s an example:
import { verifySession } from '@/app/lib/dal';
import { forbidden } from 'next/navigation';
export default async function AdminPage() {
const session = await verifySession();
// Check if the user has the 'admin' role
if (session.role !== 'admin') {
forbidden();
}
// Render the admin page for authorized users
return <h1>Admin Page</h1>;
}
Creating custom error pages
To customize the error pages, create the following files:
import Link from 'next/link';
export default function Forbidden() {
return (
<div>
<h2>Forbidden</h2>
<p>You are not authorized to access this resource.</p>
<Link href="/">Return Home</Link>
</div>
);
}
import Link from 'next/link';
export default function Unauthorized() {
return (
<div>
<h2>Unauthorized</h2>
<p>Please log in to access this page.</p>
<Link href="/login">Go to Login</Link>
</div>
);
}
We'd like to thank Clerk for proposing this feature through a PR and assisting us in prototyping the API. Before we stabilize this feature in 15.2, we're planning on adding more capabilities and improvements to the APIs to support a wider range of use cases.
Read the documentation for the unauthorized
and forbidden
APIs for more details.
Other Changes
- [Feature] Use ESLint 9 in
create-next-app
(PR) - [Feature] Increase max cache tags to 128 (PR)
- [Feature] Add an option to disable experimental CssChunkingPlugin (PR)
- [Feature] Add experimental CSS inlining support (PR)
- [Improvement] Silence Sass
legacy-js-api
warning (PR) - [Improvement] Fix unhandled rejection when using rewrites (PR)
- [Improvement] Ensure parent process exits when webpack worker fails (PR)
- [Improvement] Fixed route interception on a catch-all route (PR)
- [Improvement] Fixed response cloning issue in request deduping (PR)
- [Improvement] Fixed Server Action redirects between multiple root layouts (PR)
- [Improvement] Support providing MDX plugins as strings for Turbopack compatibility (PR)
Contributors
Next.js is the result of the combined work of over 3,000 individual developers. This release was brought to you by:
- The Next.js team: Andrew, Hendrik, Janka, Jiachi, Jimmy, Jiwon, JJ, Josh, Jude, Sam, Sebastian, Sebbie, Wyatt, and Zack.
- The Turbopack team: Alex, Benjamin, Donny, Maia, Niklas, Tim, Tobias, and Will.
- The Next.js Docs team: Delba, Rich, Ismael, and Lee.
Huge thanks to @sokra, @molebox, @delbaoliveira, @eps1lon, @wbinnssmith, @JamBalaya56562, @hyungjikim, @adrian-faustino, @mottox2, @lubieowoce, @bgw, @mknichel, @wyattjoh, @huozhi, @kdy1, @mischnic, @ijjk, @icyJoseph, @acdlite, @unstubbable, @gaojude, @devjiwonchoi, @cena-ko, @lforst, @devpla, @samcx, @styfle, @ztanner, @Marukome0743, @timneutkens, @JeremieDoctrine, @ductnn, @karlhorky, @reynaldichernando, @chogyejin, @y-yagi, @philparzer, @alfawal, @Rhynden, @arlyon, @MJez29, @Goodosky, @themattmayfield, @tobySolutions, @kevinmitch14, @leerob, @emmanuelgautier, @mrhrifat, @lid0a, @boar-is, @nisabmohd, @PapatMayuri, @ovogmap, @Reflex2468, @LioRael, @betterthanhajin, @HerringtonDarkholme, @bpb54321, @ahmoin, @Kikobeats, @abdelrahmanAbouelkheir, @lumirlumir, @yeeed711, @petter, and @suu3 for helping!
```

---

## 19. Our Journey with Caching

- 日期: 2024-10-24 14:00
- 链接: https://nextjs.org/blog/our-journey-with-caching

```
Thursday, October 24th 2024
Our Journey with Caching
Posted byFrontend performance can be hard to get right. Even in highly optimized apps, the most common culprit by far is client-server waterfalls. When introducing Next.js App Router, we knew we wanted to solve this issue. To do that, we needed to move client-server REST fetches to the server using React Server Components in a single roundtrip. This meant the server had to sometimes be dynamic, sacrificing the great initial loading performance of Jamstack. We built partial prerendering to solve this tradeoff and have the best of both worlds.
However, along the way, the developer experience suffered due to the caching defaults and controls we provided. The default for fetch()
changed to favor performance by caching by default, but quick prototyping and highly dynamic apps suffered. We didn't provide enough control over local database access that wasn't using fetch()
. We had unstable_cache()
, but it wasn't ergonomic. This led to the need for segment-level configs, such as export const dynamic, runtime, fetchCache, dynamicParams, revalidate = ...
, as an escape hatch.
We'll continue supporting that for backward compatibility, of course. But for a moment, I'd like you to forget about all that. We think we have an idea for something simpler.
We've been cooking on a new experimental mode that builds on just two concepts: <Suspense>
and use cache
.
Choose your adventure
The first thing you'll notice is that when you add data to your components, you will now get an error.
async function Component() {
return fetch(...) // error
}
export default async function Page() {
return <Component />
}
To use data, cookies, headers, current time or random values, you now have a choice: do you want the data to be cached (server or client-side) or executed on every request? I'm using fetch()
as an example, but this applies to any async Node API, such as databases or timers.
Dynamic
If you're still iterating or building a highly dynamic dashboard, you can wrap the component in a <Suspense>
boundary. <Suspense>
opts into dynamic data fetching and streaming.
async function Component() {
return fetch(...) // no error
}
export default async function Page() {
return <Suspense fallback="..."><Component /></Suspense>
}
You can also do this in your root layout or use loading.tsx
.
This ensures that the shell of your app remains instant. You can continue adding more data inside your Page, knowing it will all be dynamic by default. Nothing is cached by default. No more hidden caches.
Static
If you're building something static and don't want to use dynamic functionality, you can use the new use cache
directive.
"use cache"
export default async function Page() {
return fetch(...) // no error
}
By marking the Page with use cache
, you're indicating that the entire segment should be cached. This means any data you fetch can now be cached, allowing the page to be statically rendered. No <Suspense>
boundary is used for static content. You can add more data to the page, and it will all be cached.
Partial
You can also mix and match. For example, you can put use cache
in your root layout to ensure it is cached. Each layout or page can be cached independently.
"use cache"
export default async function Layout({ children }) {
const response = await fetch(...)
const data = await response.json()
return <html>
<body>
<div>{data.notice}</div>
{children}
</body>
</html>
}
While using dynamic data within a specific Page:
import { Suspense } from 'react'
async function Component() {
return fetch(...) // no error
}
export default async function Page() {
return <Suspense fallback="..."><Component /></Suspense>
}
Cached functions
When using a hybrid approach like this, it might be more convenient to add caching closer to the API calls.
You can add use cache
to any async function, just like use server
. Think of it as a Server Action but instead of calling a Server you're calling a Cache. It supports the same rich types of arguments and return values beyond just JSON. The cache key automatically includes any arguments and closures, so you don't need to specify a cache key manually.
async function getNotice() {
"use cache"
const response = await fetch(...)
const data = await response.json()
return data.notice;
}
export default async function Layout({ children }) {
return <html>
<body>
<h1>{await getNotice()}</h1>
{children}
</body>
</html>
}
Since no other data was used in this layout, it can remain static. A benefit of this approach is that if you accidentally add new dynamic data to the layout, it will trigger an error during the build, forcing you to make a new choice. If you add use cache
to the entire layout, it will be cached with no error. Which approach you choose depends on your use case.
Tagging a cache
If you want to explicitly clear a cache entry by tag, you can use the new cacheTag()
API inside the use cache
function.
import { cacheTag } from 'next/cache';
async function getNotice() {
'use cache';
cacheTag('my-tag');
}
Then, just call revalidateTag('my-tag')
from a Server Action as before.
Since this API can be called after data loading, you can now use data to tag your cache entries.
import { cacheTag } from 'next/cache';
async function getBlogPosts(page) {
'use cache';
const posts = await fetchPosts(page);
for (let post of posts) {
cacheTag('blog-post-' + post.id);
}
return posts;
}
Defining the lifetime of a cache
If you want to control how long a particular entry or page should live in the cache, you can use the cacheLife()
API:
"use cache"
import { cacheLife } from 'next/cache'
export default async function Page() {
cacheLife("minutes")
return ...
}
By default, it accepts the following values:
"seconds"
"minutes"
"hours"
"days"
"weeks"
"max"
Choose a rough range that bests fits your use case. No need to specify an exact number and calculate how many seconds (or was it milliseconds?) are in a week. However, you can also specify specific values or configure your own named cache profiles.
In addition to revalidate
, this API can control the stale
time of the client cache as well as expire
, which dictates when a Page should expire if it hasn't had much traffic for a while.
Experimental
This is still very much an experimental project. It's not production-ready yet and still has missing features and bugs. In particular, we know we need to improve the error stacks for this new type of error. However, if you're feeling adventurous, we'd love your early feedback.
We will publish a more detailed upgrade path. Aside from the early errors, the main breaking change here is undoing the default caching of fetch()
. That said, we recommend experimenting only on greenfield projects at this early experimental stage. If it pans out well we hope to ship an opt-in version in a minor and make it the default in a future major.
To play with it, you must be on the canary
version of Next.js:
npx create-next-app@canary
You must also enable the experimental dynamicIO flag in next.config.ts
:
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
dynamicIO: true,
}
};
export default nextConfig;
Read more about use cache
, cacheLife
, and cacheTag
in our documentation.
```

---

## 20. Next.js 15

- 日期: 2024-10-21 17:00
- 链接: https://nextjs.org/blog/next-15

```
Monday, October 21st 2024
Next.js 15
Posted byNext.js 15 is officially stable and ready for production. This release builds on the updates from both RC1 and RC2. We've focused heavily on stability while adding some exciting updates we think you'll love. Try Next.js 15 today:
# Use the new automated upgrade CLI
npx @next/codemod@canary upgrade latest
# ...or upgrade manually
npm install next@latest react@rc react-dom@rc
We're also excited to share more about what's coming next at Next.js Conf this Thursday, October 24th.
Here's what is new in Next.js 15:
@next/codemod
CLI: Easily upgrade to the latest Next.js and React versions.- Async Request APIs (Breaking): Incremental step towards a simplified rendering and caching model.
- Caching Semantics (Breaking):
fetch
requests,GET
Route Handlers, and client navigations are no longer cached by default. - React 19 Support: Support for React 19, React Compiler (Experimental), and hydration error improvements.
- Turbopack Dev (Stable): Performance and stability improvements.
- Static Indicator: New visual indicator shows static routes during development.
unstable_after
API (Experimental): Execute code after a response finishes streaming.instrumentation.js
API (Stable): New API for server lifecycle observability.- Enhanced Forms (
next/form
): Enhance HTML forms with client-side navigation. next.config
: TypeScript support fornext.config.ts
.- Self-hosting Improvements: More control over
Cache-Control
headers. - Server Actions Security: Unguessable endpoints and removal of unused actions.
- Bundling External Packages (Stable): New config options for App and Pages Router.
- ESLint 9 Support: Added support for ESLint 9.
- Development and Build Performance: Improved build times and Faster Fast Refresh.
Smooth upgrades with @next/codemod
CLI
We include codemods (automated code transformations) with every major Next.js release to help automate upgrading breaking changes.
To make upgrades even smoother, we've released an enhanced codemod CLI:
npx @next/codemod@canary upgrade latest
This tool helps you upgrade your codebase to the latest stable or prerelease versions. The CLI will update your dependencies, show available codemods, and guide you through applying them.
The canary
tag uses the latest version of the codemod while the latest specifies the Next.js version. We recommend using the canary version of the codemod even if you are upgrading to the latest Next.js version, as we plan to continue adding improvements to the tool based on your feedback.
Learn more about Next.js codemod CLI.
Async Request APIs (Breaking Change)
In traditional Server-Side Rendering, the server waits for a request before rendering any content. However, not all components depend on request-specific data, so it's unnecessary to wait for the request to render them. Ideally, the server would prepare as much as possible before a request arrives. To enable this, and set the stage for future optimizations, we need to know when to wait for the request.
Therefore, we are transitioning APIs that rely on request-specific data—such as headers
, cookies
, params
, and searchParams
—to be asynchronous.
import { cookies } from 'next/headers';
export async function AdminPanel() {
const cookieStore = await cookies();
const token = cookieStore.get('token');
// ...
}
This is a breaking change and affects the following APIs:
cookies
headers
draftMode
params
inlayout.js
,page.js
,route.js
,default.js
,generateMetadata
, andgenerateViewport
searchParams
inpage.js
For an easier migration, these APIs can temporarily be accessed synchronously, but will show warnings in development and production until the next major version. A codemod is available to automate the migration:
npx @next/codemod@canary next-async-request-api .
For cases where the codemod can't fully migrate your code, please read the upgrade guide. We have also provided an example of how to migrate a Next.js application to the new APIs.
Caching Semantics
Next.js App Router launched with opinionated caching defaults. These were designed to provide the most performant option by default with the ability to opt out when required.
Based on your feedback, we re-evaluated our caching heuristics and how they would interact with projects like Partial Prerendering (PPR) and with third party libraries using fetch
.
With Next.js 15, we're changing the caching default for GET
Route Handlers and the Client Router Cache from cached by default to uncached by default. If you want to retain the previous behavior, you can continue to opt-into caching.
We're continuing to improve caching in Next.js in the coming months and we'll share more details soon.
GET
Route Handlers are no longer cached by default
In Next 14, Route Handlers that used the GET
HTTP method were cached by default unless they used a dynamic function or dynamic config option. In Next.js 15, GET
functions are not cached by default.
You can still opt into caching using a static route config option such as export dynamic = 'force-static'
.
Special Route Handlers like sitemap.ts
, opengraph-image.tsx
, and icon.tsx
, and other metadata files remain static by default unless they use dynamic functions or dynamic config options.
Client Router Cache no longer caches Page components by default
In Next.js 14.2.0, we introduced an experimental staleTimes
flag to allow custom configuration of the Router Cache.
In Next.js 15, this flag still remains accessible, but we are changing the default behavior to have a staleTime
of 0
for Page segments. This means that as you navigate around your app, the client will always reflect the latest data from the Page component(s) that become active as part of the navigation. However, there are still important behaviors that remain unchanged:
- Shared layout data won't be refetched from the server to continue to support partial rendering.
- Back/forward navigation will still restore from cache to ensure the browser can restore scroll position.
loading.js
will remain cached for 5 minutes (or the value of thestaleTimes.static
configuration).
You can opt into the previous Client Router Cache behavior by setting the following configuration:
const nextConfig = {
experimental: {
staleTimes: {
dynamic: 30,
},
},
};
export default nextConfig;
React 19
As part of the Next.js 15 release, we've made the decision to align with the upcoming release of React 19.
In version 15, the App Router uses React 19 RC, and we've also introduced backwards compatibility for React 18 with the Pages Router based on community feedback. If you're using the Pages Router, this allows you to upgrade to React 19 when ready.
Although React 19 is still in the RC phase, our extensive testing across real-world applications and our close work with the React team have given us confidence in its stability. The core breaking changes have been well-tested and won't affect existing App Router users. Therefore, we've decided to release Next.js 15 as stable now, so your projects are fully prepared for React 19 GA.
To ensure the transition is as smooth as possible, we've provided codemods and automated tools to help ease the migration process.
Read the Next.js 15 upgrade guide, the React 19 upgrade guide, and watch the React Conf Keynote to learn more.
Pages Router on React 18
Next.js 15 maintains backward compatibility for the Pages Router with React 18, allowing users to continue using React 18 while benefiting from improvements in Next.js 15.
Since the first Release Candidate (RC1), we've shifted our focus to include support for React 18 based on community feedback. This flexibility enables you to adopt Next.js 15 while using the Pages Router with React 18, giving you greater control over your upgrade path.
Note: While it is possible to run the Pages Router on React 18 and the App Router on React 19 in the same application, we don't recommend this setup. Doing so could result in unpredictable behavior and typings inconsistencies, as the underlying APIs and rendering logic between the two versions may not fully align.
React Compiler (Experimental)
The React Compiler is a new experimental compiler created by the React team at Meta. The compiler understands your code at a deep level through its understanding of plain JavaScript semantics and the Rules of React, which allows it to add automatic optimizations to your code. The compiler reduces the amount of manual memoization developers have to do through APIs such as useMemo
and useCallback
- making code simpler, easier to maintain, and less error prone.
With Next.js 15, we've added support for the React Compiler. Learn more about the React Compiler, and the available Next.js config options.
Note: The React Compiler is currently only available as a Babel plugin, which will result in slower development and build times.
Hydration error improvements
Next.js 14.1 made improvements to error messages and hydration errors. Next.js 15 continues to build on those by adding an improved hydration error view. Hydration errors now display the source code of the error with suggestions on how to address the issue.
For example, this was a previous hydration error message in Next.js 14.1:
Next.js 15 has improved this to:
Turbopack Dev
We are happy to announce that next dev --turbo
is now stable and ready to speed up your development experience. We've been using it to iterate on vercel.com, nextjs.org, v0, and all of our other applications with great results.
For example, with vercel.com
, a large Next.js app, we've seen:
- Up to 76.7% faster local server startup.
- Up to 96.3% faster code updates with Fast Refresh.
- Up to 45.8% faster initial route compile without caching (Turbopack does not have disk caching yet).
You can learn more about Turbopack Dev in our new blog post.
Static Route Indicator
Next.js now displays a Static Route Indicator during development to help you identify which routes are static or dynamic. This visual cue makes it easier to optimize performance by understanding how your pages are rendered.
You can also use the next build output to view the rendering strategy for all routes.
This update is part of our ongoing efforts to enhance observability in Next.js, making it easier for developers to monitor, debug, and optimize their applications. We're also working on dedicated developer tools, with more details to come soon.
Learn more about the Static Route Indicator, which can be disabled.
Executing code after a response with unstable_after
(Experimental)
When processing a user request, the server typically performs tasks directly related to computing the response. However, you may need to perform tasks such as logging, analytics, and other external system synchronization.
Since these tasks are not directly related to the response, the user should not have to wait for them to complete. Deferring the work after responding to the user poses a challenge because serverless functions stop computation immediately after the response is closed.
after()
is a new experimental API that solves this problem by allowing you to schedule work to be processed after the response has finished streaming, enabling secondary tasks to run without blocking the primary response.
To use it, add experimental.after
to next.config.js
:
const nextConfig = {
experimental: {
after: true,
},
};
export default nextConfig;
Then, import the function in Server Components, Server Actions, Route Handlers, or Middleware.
import { unstable_after as after } from 'next/server';
import { log } from '@/app/utils';
export default function Layout({ children }) {
// Secondary task
after(() => {
log();
});
// Primary task
return <>{children}</>;
}
Learn more about unstable_after
.
instrumentation.js
(Stable)
The instrumentation
file, with the register()
API, allows users to tap into the Next.js server lifecycle to monitor performance, track the source of errors, and deeply integrate with observability libraries like OpenTelemetry.
This feature is now stable and the experimental.instrumentationHook
config option can be removed.
In addition, we've collaborated with Sentry on designing a new onRequestError
hook that can be used to:
- Capture important context about all errors thrown on the server, including:
- Router: Pages Router or App Router
- Server context: Server Component, Server Action, Route Handler, or Middleware
- Report the errors to your favorite observability provider.
export async function onRequestError(err, request, context) {
await fetch('https://...', {
method: 'POST',
body: JSON.stringify({ message: err.message, request, context }),
headers: { 'Content-Type': 'application/json' },
});
}
export async function register() {
// init your favorite observability provider SDK
}
Learn more about the onRequestError
function.
<Form>
Component
The new <Form>
component extends the HTML <form>
element with prefetching, client-side navigation, and progressive enhancement.
It is useful for forms that navigate to a new page, such as a search form that leads to a results page.
import Form from 'next/form';
export default function Page() {
return (
<Form action="/search">
<input name="query" />
<button type="submit">Submit</button>
</Form>
);
}
The <Form>
component comes with:
- Prefetching: When the form is in view, the layout and loading UI are prefetched, making navigation fast.
- Client-side Navigation: On submission, shared layouts and client-side state are preserved.
- Progressive Enhancement: If JavaScript hasn't loaded yet, the form still works via full-page navigation.
Previously, achieving these features required a lot of manual boilerplate. For example:
Example
// Note: This is abbreviated for demonstration purposes.
// Not recommended for use in production code.
'use client'
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
export default function Form(props) {
const action = props.action
const router = useRouter()
useEffect(() => {
// if form target is a URL, prefetch it
if (typeof action === 'string') {
router.prefetch(action)
}
}, [action, router])
function onSubmit(event) {
event.preventDefault()
// grab all of the form fields and trigger a `router.push` with the data URL encoded
const formData = new FormData(event.currentTarget)
const data = new URLSearchParams()
for (const [name, value] of formData) {
data.append(name, value as string)
}
router.push(`${action}?${data.toString()}`)
}
if (typeof action === 'string') {
return <form onSubmit={onSubmit} {...props} />
}
return <form {...props} />
}
Learn more about the <Form>
Component.
Support for next.config.ts
Next.js now supports the TypeScript next.config.ts
file type and provides a NextConfig
type for autocomplete and type-safe options:
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
/* config options here */
};
export default nextConfig;
Learn more about TypeScript support in Next.js.
Improvements for self-hosting
When self-hosting applications, you may need more control over Cache-Control
directives.
One common case is controlling the stale-while-revalidate
period sent for ISR pages. We've implemented two improvements:
- You can now configure the
expireTime
value innext.config
. This was previously theexperimental.swrDelta
option. - Updated the default value to one year, ensuring most CDNs can fully apply the
stale-while-revalidate
semantics as intended.
We also no longer override custom Cache-Control
values with our default values, allowing full control and ensuring compatibility with any CDN setup.
Finally, we've improved image optimization when self-hosting. Previously, we recommended you install sharp
for optimizing images on your Next.js server. This recommendation was sometimes missed. With Next.js 15, you no longer need to manually install sharp
— Next.js will use sharp
automatically when using next start
or running with standalone output mode.
To learn more, see our new demo and tutorial video on self-hosting Next.js.
Enhanced Security for Server Actions
Server Actions are server-side functions that can be called from the client. They are defined by adding the 'use server'
directive at the top of a file and exporting an async function.
Even if a Server Action or utility function is not imported elsewhere in your code, it's still a publicly accessible HTTP endpoint. While this behavior is technically correct, it can lead to unintentional exposure of such functions.
To improve security, we've introduced the following enhancements:
- Dead code elimination: Unused Server Actions won't have their IDs exposed to the client-side JavaScript bundle, reducing bundle size and improving performance.
- Secure action IDs: Next.js now creates unguessable, non-deterministic IDs to allow the client to reference and call the Server Action. These IDs are periodically recalculated between builds for enhanced security.
// app/actions.js
'use server';
// This action **is** used in our application, so Next.js
// will create a secure ID to allow the client to reference
// and call the Server Action.
export async function updateUserAction(formData) {}
// This action **is not** used in our application, so Next.js
// will automatically remove this code during `next build`
// and will not create a public endpoint.
export async function deleteUserAction(formData) {}
You should still treat Server Actions as public HTTP endpoints. Learn more about securing Server Actions.
Optimizing bundling of external packages (Stable)
Bundling external packages can improve the cold start performance of your application. In the App Router, external packages are bundled by default, and you can opt-out specific packages using the new serverExternalPackages
config option.
In the Pages Router, external packages are not bundled by default, but you can provide a list of packages to bundle using the existing transpilePackages
option. With this configuration option, you need to specify each package.
To unify configuration between App and Pages Router, we're introducing a new option, bundlePagesRouterDependencies
to match the default automatic bundling of the App Router. You can then use serverExternalPackages
to opt-out specific packages, if needed.
const nextConfig = {
// Automatically bundle external packages in the Pages Router:
bundlePagesRouterDependencies: true,
// Opt specific packages out of bundling for both App and Pages Router:
serverExternalPackages: ['package-name'],
};
export default nextConfig;
Learn more about optimizing external packages.
ESLint 9 Support
Next.js 15 also introduces support for ESLint 9, following the end-of-life for ESLint 8 on October 5, 2024.
To ensure a smooth transition, Next.js remain backwards compatible, meaning you can continue using either ESLint 8 or 9.
If you upgrade to ESLint 9, and we detect that you haven't yet adopted the new config format, Next.js will automatically apply the ESLINT_USE_FLAT_CONFIG=false
escape hatch to ease migration.
Additionally, deprecated options like —ext
and —ignore-path
will be removed when running next lint
. Please note that ESLint will eventually disallow these older configurations in ESLint 10, so we recommend starting your migration soon.
For more details on these changes, check out the migration guide.
As part of this update, we've also upgraded eslint-plugin-react-hooks
to v5.0.0
, which introduces new rules for React Hooks usage. You can review all changes in the changelog for eslint-plugin-react-hooks@5.0.0.
Development and Build Improvements
Server Components HMR
During development, Server components are re-executed when saved. This means, any fetch
requests to your API endpoints or third-party services are also called.
To improve local development performance and reduce potential costs for billed API calls, we now ensure Hot Module Replacement (HMR) can re-use fetch
responses from previous renders.
Learn more about the Server Components HMR Cache.
Faster Static Generation for the App Router
We've optimized static generation to improve build times, especially for pages with slow network requests.
Previously, our static optimization process rendered pages twice—once to generate data for client-side navigation and a second time to render the HTML for the initial page visit. Now, we reuse the first render, cutting out the second pass, reducing workload and build times.
Additionally, static generation workers now share the fetch
cache across pages. If a fetch
call doesn't opt out of caching, its results are reused by other pages handled by the same worker. This reduces the number of requests for the same data.
Advanced Static Generation Control (Experimental)
We've added experimental support for more control over the static generation process for advanced use cases that would benefit from greater control.
We recommend sticking to the current defaults unless you have specific requirements as these options can lead to increased resource usage and potential out-of-memory errors due to increased concurrency.
const nextConfig = {
experimental: {
// how many times Next.js will retry failed page generation attempts
// before failing the build
staticGenerationRetryCount: 1
// how many pages will be processed per worker
staticGenerationMaxConcurrency: 8
// the minimum number of pages before spinning up a new export worker
staticGenerationMinPagesPerWorker: 25
},
}
export default nextConfig;
Learn more about the Static Generation options.
Other Changes
- [Breaking] next/image: Removed
squoosh
in favor ofsharp
as an optional dependency (PR) - [Breaking] next/image: Changed default
Content-Disposition
toattachment
(PR) - [Breaking] next/image: Error when
src
has leading or trailing spaces (PR) - [Breaking] Middleware: Apply
react-server
condition to limit unrecommended React API imports (PR) - [Breaking] next/font: Removed support for external
@next/font
package (PR) - [Breaking] next/font: Removed
font-family
hashing (PR) - [Breaking] Caching:
force-dynamic
will now set ano-store
default to the fetch cache (PR) - [Breaking] Config: Enable
swcMinify
(PR),missingSuspenseWithCSRBailout
(PR), andoutputFileTracing
(PR) behavior by default and remove deprecated options - [Breaking] Remove auto-instrumentation for Speed Insights (must now use the dedicated @vercel/speed-insights package) (PR)
- [Breaking] Remove
.xml
extension for dynamic sitemap routes and align sitemap URLs between development and production (PR) - [Breaking] We've deprecated exporting
export const runtime = "experimental-edge"
in the App Router. Users should now switch toexport const runtime = "edge"
. We've added a codemod to perform this (PR) - [Breaking] Calling
revalidateTag
andrevalidatePath
during render will now throw an error (PR) - [Breaking] The
instrumentation.js
andmiddleware.js
files will now use the vendored React packages (PR) - [Breaking] The minimum required Node.js version has been updated to 18.18.0 (PR)
- [Breaking]
next/dynamic
: the deprecatedsuspense
prop has been removed and when the component is used in the App Router, it won't insert an empty Suspense boundary anymore (PR) - [Breaking] When resolving modules on the Edge Runtime, the
worker
module condition will not be applied (PR) - [Breaking] Disallow using
ssr: false
option withnext/dynamic
in Server Components (PR) - [Improvement] Metadata: Updated environment variable fallbacks for
metadataBase
when hosted on Vercel (PR) - [Improvement] Fix tree-shaking with mixed namespace and named imports from
optimizePackageImports
(PR) - [Improvement] Parallel Routes: Provide unmatched catch-all routes with all known params (PR)
- [Improvement] Config
bundlePagesExternals
is now stable and renamed tobundlePagesRouterDependencies
- [Improvement] Config
serverComponentsExternalPackages
is now stable and renamed toserverExternalPackages
- [Improvement] create-next-app: New projects ignore all
.env
files by default (PR) - [Improvement] The
outputFileTracingRoot
,outputFileTracingIncludes
andoutputFileTracingExcludes
have been upgraded from experimental and are now stable (PR) - [Improvement] Avoid merging global CSS files with CSS module files deeper in the tree (PR)
- [Improvement] The cache handler can be specified via the
NEXT_CACHE_HANDLER_PATH
environment variable (PR) - [Improvement] The Pages Router now supports both React 18 and React 19 (PR)
- [Improvement] The Error Overlay now displays a button to copy the Node.js Inspector URL if the inspector is enabled (PR)
- [Improvement] Client prefetches on the App Router now use the
priority
attribute (PR) - [Improvement] Next.js now provides an
unstable_rethrow
function to rethrow Next.js internal errors in the App Router (PR) - [Improvement]
unstable_after
can now be used in static pages (PR) - [Improvement] If a
next/dynamic
component is used during SSR, the chunk will be prefetched (PR) - [Improvement] The
esmExternals
option is now supported on the App Router (PR) - [Improvement] The
experimental.allowDevelopmentBuild
option can be used to allowNODE_ENV=development
withnext build
for debugging purposes (PR) - [Improvement] The Server Action transforms are now disabled in the Pages Router (PR)
- [Improvement] Build workers will now stop the build from hanging when they exit (PR)
- [Improvement] When redirecting from a Server Action, revalidations will now apply correctly (PR)
- [Improvement] Dynamic params are now handled correctly for parallel routes on the Edge Runtime (PR)
- [Improvement] Static pages will now respect staleTime after initial load (PR)
- [Improvement]
vercel/og
updated with a memory leak fix (PR) - [Improvement] Patch timings updated to allow usage of packages like
msw
for APIs mocking (PR) - [Improvement] Prerendered pages should use static staleTime (PR)
To learn more, check out the upgrade guide.
Contributors
Next.js is the result of the combined work of over 3,000 individual developers, industry partners like Google and Meta, and our core team at Vercel. This release was brought to you by:
- The Next.js team: Andrew, Hendrik, Janka, Jiachi, Jimmy, Jiwon, JJ, Josh, Sam, Sebastian, Sebbie, Shu, Wyatt, and Zack.
- The Turbopack team: Alex, Benjamin, Donny, Maia, Niklas, Tim, Tobias, and Will.
- The Next.js Docs team: Delba, Rich, Ismael, and Lee.
Huge thanks to @AbhiShake1, @Aerilym, @AhmedBaset, @AnaTofuZ, @Arindam200, @Arinji2, @ArnaudFavier, @ArnoldVanN, @Auxdible, @B33fb0n3, @Bhavya031, @Bjornnyborg, @BunsDev, @CannonLock, @CrutchTheClutch, @DeepakBalaraman, @DerTimonius, @Develliot, @EffectDoplera, @Ehren12, @Ethan-Arrowood, @FluxCapacitor2, @ForsakenHarmony, @Francoscopic, @Gomah, @GyoHeon, @Hemanshu-Upadhyay, @HristovCodes, @HughHzyb, @IAmKushagraSharma, @IDNK2203, @IGassmann, @ImDR, @IncognitoTGT, @Jaaneek, @JamBalaya56562, @Jeffrey-Zutt, @JohnGemstone, @JoshuaKGoldberg, @Julian-Louis, @Juneezee, @KagamiChan, @Kahitar, @KeisukeNagakawa, @KentoMoriwaki, @Kikobeats, @KonkenBonken, @Kuboczoch, @Lada496, @LichuAcu, @LorisSigrist, @Lsnsh, @Luk-z, @Luluno01, @M-YasirGhaffar, @Maaz-Ahmed007, @Manoj-M-S, @ManuLpz4, @Marukome0743, @MaxLeiter, @MehfoozurRehman, @MildTomato, @MonstraG, @N2D4, @NavidNourani, @Nayeem-XTREME, @Netail, @NilsJacobsen, @Ocheretovich, @OlyaPolya, @PapatMayuri, @PaulAsjes, @PlagueFPS, @ProchaLu, @Pyr33x, @QiuranHu, @RiskyMH, @Sam-Phillemon9493, @Sayakie, @Shruthireddy04, @SouthLink, @Strift, @SukkaW, @Teddir, @Tim-Zj, @TrevorSayre, @Unsleeping, @Willem-Jaap, @a89529294, @abdull-haseeb, @abhi12299, @acdlite, @actopas, @adcichowski, @adiguno, @agadzik, @ah100101, @akazwz, @aktoriukas, @aldosch, @alessiomaffeis, @allanchau, @alpedia0, @amannn, @amikofalvy, @anatoliik-lyft, @anay-208, @andrii-bodnar, @anku255, @ankur-dwivedi, @aralroca, @archanaagivale30, @arlyon, @atik-persei, @avdeev, @baeharam, @balazsorban44, @bangseongbeom, @begalinsaf, @bennettdams, @bewinsnw, @bgw, @blvdmitry, @bobaaaaa, @boris-szl, @bosconian-dynamics, @brekk, @brianshano, @cfrank, @chandanpasunoori, @chentsulin, @chogyejin, @chrisjstott, @christian-bromann, @codeSTACKr, @coderfin, @coltonehrman, @controversial, @coopbri, @creativoma, @crebelskydico, @crutchcorn, @darthmaim, @datner, @davidsa03, @delbaoliveira, @devjiwonchoi, @devnyxie, @dhruv-kaushik, @dineshh-m, @diogocapela, @dnhn, @domdomegg, @domin-mnd, @dvoytenko, @ebCrypto, @ekremkenter, @emmerich, @flybayer, @floriangosse, @forsakenharmony, @francoscopic, @frys, @gabrielrolfsen, @gaojude, @gdborton, @greatvivek11, @gnoff, @guisehn, @GyoHeon, @hamirmahal, @hiro0218, @hirotomoyamada, @housseindjirdeh, @hungdoansy, @huozhi, @hwangstar156, @iampoul, @ianmacartney, @icyJoseph, @ijjk, @imddc, @imranolas, @iscekic, @jantimon, @jaredhan418, @jeanmax1me, @jericopulvera, @jjm2317, @jlbovenzo, @joelhooks, @joeshub, @jonathan-ingram, @jonluca, @jontewks, @joostmeijles, @jophy-ye, @jordienr, @jordyfontoura, @kahlstrm, @karlhorky, @karlkeefer, @kartheesan05, @kdy1, @kenji-webdev, @kevva, @khawajaJunaid, @kidonng, @kiner-tang, @kippmr, @kjac, @kjugi, @kshehadeh, @kutsan, @kwonoj, @kxlow, @leerob, @lforst, @li-jia-nan, @liby, @lonr, @lorensr, @lovell, @lubieowoce, @luciancah, @luismiramirez, @lukahartwig, @lumirlumir, @luojiyin1987, @mamuso, @manovotny, @marlier, @mauroaccornero, @maxhaomh, @mayank1513, @mcnaveen, @md-rejoyan-islam, @mehmetozguldev, @mert-duzgun, @mirasayon, @mischnic, @mknichel, @mobeigi, @molebox, @mratlamwala, @mud-ali, @n-ii-ma, @n1ckoates, @nattui, @nauvalazhar, @neila-a, @neoFinch, @niketchandivade, @nisabmohd, @none23, @notomo, @notrab, @nsams, @nurullah, @okoyecharles, @omahs, @paarthmadan, @pathliving, @pavelglac, @penicillin0, @phryneas, @pkiv, @pnutmath, @qqww08, @r34son, @raeyoung-kim, @remcohaszing, @remorses, @rezamauliadi, @rishabhpoddar, @ronanru, @royalfig, @rubyisrust, @ryan-nauman, @ryohidaka, @ryota-murakami, @s-ekai, @saltcod, @samcx, @samijaber, @sean-rallycry, @sebmarkbage, @shubh73, @shuding, @sirTangale, @sleevezip, @slimbde, @soedirgo, @sokra, @sommeeeer, @sopranopillow, @souporserious, @srkirkland, @steadily-worked, @steveluscher, @stipsan, @styfle, @stylessh, @syi0808, @symant233, @tariknh, @theoludwig, @timfish, @timfuhrmann, @timneutkens, @tknickman, @todor0v, @tokkiyaa, @torresgol10, @tranvanhieu01012002, @txxxxc, @typeofweb, @unflxw, @unstubbable, @versecafe, @vicb, @vkryachko, @wbinnssmith, @webtinax, @weicheng95, @wesbos, @whatisagi, @wiesson, @woutvanderploeg, @wyattjoh, @xiaohanyu, @xixixao, @xugetsu, @yosefbeder, @ypessoa, @ytori, @yunsii, @yurivangeffen, @z0n, @zce, @zhawtof, @zsh77, and @ztanner for helping!
```

---

## 21. Turbopack Dev is Now Stable

- 日期: 2024-10-21 16:50
- 链接: https://nextjs.org/blog/turbopack-for-development-stable

```
Monday, October 21st 2024
Turbopack Dev is Now Stable
Posted byIt's been a long road, but we are happy to announce that next dev --turbo
is now stable and ready to speed up your development experience. We've been using it to iterate on vercel.com, nextjs.org, v0, and all of our other applications with great results.
Since its release 8 years ago, Next.js has been used to build everything, from weekend hobby projects to sophisticated enterprise applications. When Next.js was first released, webpack was clearly the best choice for the framework's bundling foundation, but over time it has struggled to keep up with the needs of modern web developers. Our community started to find it painfully slow to iterate while waiting for routes to load, code changes to reflect, and production builds to deploy.
We invested a lot of time and effort optimizing webpack, but at a certain point, we felt we weren't getting enough improvement for the effort involved. We needed a new foundation that could support the many Next.js applications already in production today, as well as the future innovations we had planned, like React Server Components.
These were our requirements for this new bundler:
- Minimal breaking changes
- Support for both App Router and Pages Router
- Faster compile times for codebases of all sizes
- Development builds that closely match production
- Advanced production optimizations (e.g. tree shaking within modules)
- Module graph that supports multiple environments like Node.js and the browser
- Full observability for maintainers and advanced users
We evaluated all existing solutions at the time and found that each one had trade-offs that didn't align with our requirements and goals. It made sense for us to design something from the ground up that could accomplish exactly what Next.js needs today and own the roadmap so we can build and experiment with what it will need tomorrow. This was our motivation to create Turbopack.
We started out by optimizing the development experience, and that's what we're releasing as stable today. We've been extensively dogfooding Turbopack with Vercel's applications, and have noticeably improved the iteration velocity of our developers. For example, with vercel.com
, a large Next.js app, we've seen:
- Up to 76.7% faster local server startup.
- Up to 96.3% faster code updates with Fast Refresh.
- Up to 45.8% faster initial route compile without caching (Turbopack does not have disk caching yet).
In this post, we'll discuss how we achieved these results, along with some other highlights. We'll also clarify exactly what to expect from this release and provide a roadmap for what to expect next.
Highlights
Faster initial compile of a route
One of the biggest issues we were hearing from our community was that routes were taking too long to load in development, which came down to webpack's compilation speed. Next.js compiles routes on-demand to avoid having to compile all possible routes before they are needed, which keeps the initial startup fast and memory usage lower, but even then, you could still find yourself tapping your feet while waiting for a single page to load.
To be fair, bundlers like webpack are doing a lot underneath the hood. When compiling a route for the first time, the bundler starts at an “entrypoint”. In the case of Next.js, it's a combination of page.tsx
and all related files for that route, like layout.tsx
and loading.tsx
, etc. These entrypoints are parsed to find import
statements that get resolved to files, which then get processed the same as the entrypoints, and this cycle continues until no more imports are found. This process builds a graph of modules, which can be made up of not just TypeScript / JavaScript modules (including node_modules
), but also CSS files (both global and CSS modules), and static files like imported images for next/image
.
After all modules are collected, the module graph is used to create bundles of JavaScript, often referred to as “chunks.” These chunks are the outputs of the compiler that run on the server (at build-time or runtime) or in the browser.
webpack does not support creating graphs that produce outputs for multiple environments, so we have to run at least two separate compilers in Next.js with webpack today, one for the server and one for the browser. We must compile the server module graph first so that all references to "use client"
can be found. Once the server is built, we traverse its graph to create the relevant entrypoints for the browser compiler. Since this is a separate webpack compiler, there's some overhead in this process, like parsing the same code twice across client and server.
With Turbopack, we set out to remove the overhead of running multiple compilers and coordinating between them. The solution was to make the compiler aware of multiple different output targets. Internally, these are called target “transitions”. We can mark an import as a transition from server to browser or from browser to server. This is what allows Turbopack to efficiently bundle Server Components and Client Components, as well as Server Functions imported from Client Components.
In addition to improving performance, having a single compiler that can handle multiple environments in a single pass has reliability and debugging benefits, as we no longer have to coordinate between two separate compiler processes in Next.js.
Another big difference between webpack and Turbopack is that Turbopack can parallelize work across multiple CPUs, whereas with webpack, only the TypeScript / JavaScript transformation step using SWC is parallelized.
webpack doesn't support parallelizing across CPUs because, in order to parallelize effectively, data must be easily accessible across threads. webpack was built in a way that heavily uses large JavaScript objects, which can't be shared across threads easily without expensive serialization and deserialization. This overhead often negates the performance improvement of leveraging multiple CPUs. Turbopack is written in Rust, which does not have the same limitations, and was built with parallelization in mind from the start.
We were also able to achieve performance wins with faster filesystem reads and writes, faster module resolution, and by skipping more work on side-effect free modules.
When using Turbopack on vercel.com
, a large Next.js application, we've seen up to 45.8% faster initial compilation compared to Next.js with webpack.
Faster Fast Refresh
Fast Refresh is the system that bundlers use to propagate changes to the route you're currently looking at in the browser, sometimes referred to as Hot Module Replacement (HMR).
Next.js has a deeper integration that connects Fast Refresh to React, making sure that React doesn't lose state whenever you change a component.
With webpack, we found there is a limit to the performance of Fast Refresh when you hit a certain number of JavaScript modules. Webpack needs to do graph traversal and generate outputs even for modules that have not changed, scaling linearly with the amount of JavaScript modules.
We found that at around 30,000 modules, code changes consistently have at least 1 second of overhead to process an update, regardless of whether the change is small. For example, changing a color in a CSS file could take 1 second to show up on screen.
This performance was not acceptable for us. We believe that incremental builds should scale with only the size of local changes, not the size of the route or application. When button.tsx
changes, the compiler should only have to run the work related to that file change instead of having to recompute other modules and output files that are not affected by the change. To combat this, we prioritized a foundation in Turbopack that allows very granular recomputing of work.
This effort turned into the underlying library, Turbo Engine, which uses an automatic demand-driven incremental computation architecture to provide interactive hot-reloading of massive Next.js and React applications in tens of milliseconds. This architecture is based on over a decade of research and prior art, including webpack, Salsa, Parcel, Adapton, and the Rust compiler's query system.
Now with Turbopack, Fast Refresh speed scales with the size of your changes, which is how we've been able to achieve 96.3% faster code updates with Fast Refresh on large Next.js apps like vercel.com.
Advanced Tracing
As Next.js has grown in adoption over the years, we've found it increasingly hard to reproduce reported issues on GitHub, especially related to compiler performance and memory usage. This is because most people can't share their application code, or when they share the code, the application can't run because it requires a database or other setup.
To begin to address this, we added tracing to the internals of Next.js. These traces are written to a file in the .next
folder and do not include application code — only the file path, the time the compiler took on it, and other timings like individual transforms. However, with webpack, we never had a good way to clearly distinguish memory usage of the compiler from memory usage of framework or application code, as they all run in the same Node.js instance.
With Turbopack, we were able to design with instrumentation from the beginning. We implemented an instrumentation layer in Turbo Engine that allows for collecting timings of each individual function. We were able to extend these traces to also keep track of the memory allocation, deallocation, and persisted memory across every function.
This new, advanced tracing gives us all the information needed to investigate slowdowns and memory usage deeply; it only requires a trace instead of a full codebase.
In order to process these new traces, we've implemented a custom trace viewer that stays performant regardless of application and trace size. It's a trace viewer specifically built for investigating slowdowns and memory usage for Turbopack and has allowed us to optimize performance across many early adopter applications as it shortens the feedback loop.
While the trace viewer was initially built for internal usage (and it's intended for situations where a deep technical dive is needed), we've landed the required pieces to run it yourself in Next.js. You can generate a Turbopack trace using these instructions. Then, when the trace is generated, you can use next internal turbo-trace-server .next/trace-turbopack
to start the server that allows for inspecting the trace. There is a quick video overview of the trace viewer available here.
Less flakiness in compile times
When using Next.js with webpack, compile times are often not transparent enough. In one case, it may take 10 seconds to open a page, and in another, it may take 20 seconds. While a cache may be present, it sometimes doesn't have enough impact to produce consistent results. Even on compilation without caches, we've seen some variance.
The underlying architecture of Turbopack ensures variance in compile times is much more consistent. The compile times for routes only vary a few percent, allowing us to consistently optimize the compiler performance.
Development builds that closely match production
In order to optimize for compilation speed with webpack, we had to accept some trade-offs that resulted in divergent development and production environments. Some examples of those trade-offs are that we use style-loader
, which injects the style into the page and allows for Fast Refreshing them, without reloading the page. However, this means that the styles are injected by JavaScript in development, which causes a flash of unstyled content. We work around this flash of unstyled content, so you don't see it. Another example is that Next.js with webpack uses eval-source-map
, meaning that all code is wrapped in eval
and the sourcemaps are included in that, which ensures sourcemaps are available in development at the expense of the bundled code being harder to inspect and debug. While webpack supports outputting full sourcemaps using the source-map
option, it causes an outsized impact on compilation time and memory usage.
For Turbopack, we set out to solve these by default, outputting CSS files and sourcemaps without using eval
. Turbopack leverages sections
sourcemaps, a relatively new part of the source-map specification that allows for more efficient merging of sourcemaps outputs. Where we previously had to generate all mappings in one place, we're now able to generate and cache them much more granularly.
The CSS handling in Turbopack always outputs CSS files, and similar to JavaScript handling it can update the CSS file without refreshing the browser by a mechanism that is part of the Turbopack development runtime.
We can now confidently say that when something works in development with Turbopack, it also works and behaves the same in production.
Our first stable release
Two years ago, we introduced Turbopack as an alpha with Next.js 13, offering a preview of its performance potential. While initial results were promising, it only supported basic usage—many Next.js features, like basePath
, weren't yet implemented.
Over the following year, we focused on adding missing Next.js and bundling features. Based on community feedback, we decided to fully focus on the next dev
experience so we could address the most common iteration velocity complaints. By last year's Next.js Conf, 90% of development tests were passing, and Vercel developers were already using Turbopack in day-to-day development.
In April, we announced Next.js 14.2 with 99.8% of tests passing, reaching 100% soon after. Since then, we've addressed GitHub-reported issues, especially around npm packages, Fast Refresh, and error location accuracy.
Admittedly, the road to stability has taken a long time, but that mostly comes down to Next.js's extensive test suite, which sets a high bar for stability. We've had 8 years to uncover edge cases and add 6,599 development tests that also needed to pass with Turbopack. An additional factor is that we designed Turbopack with a completely different architecture than webpack. Simply porting webpack to Rust would have been easier but wouldn't have unlocked the performance wins we want to achieve.
Now that Turbopack passes all tests, has been validated with top npm packages, and feedback from early adopters is addressed, we're ready to stamp it as stable.
What exactly is stable?
This has been a point of confusion in the past, so we'll take this section to clarify what this release unlocks for the Next.js community.
This release specifically marks the next dev --turbo
command as stable. Production builds (next build --turbo
) are not supported yet, but keep reading for an update as they are in progress. We eventually plan to release a standalone version of Turbopack outside of Next.js, but we want to prove its merit by enhancing the Next.js community's experience first.
Other than the unsupported features we will cover in the next section, Turbopack should work with all stable features of Next.js. For clarity, Turbopack supports both App Router and Pages Router. Experimental features may or may not work with Turbopack, but they certainly will by the time they are marked stable.
If your application has webpack customization but only adds webpack loaders, you might be able to already use Turbopack by configuring the loaders for Turbopack. You can read the documentation for webpack loader support in Turbopack.
Here's a list of webpack loaders that are verified to work with Turbopack:
@svgr/webpack
babel-loader
url-loader
file-loader
raw-loader
tsconfig-paths-webpack-plugin
— supported out of the box, no plugin needed.- Most other loaders also work, as we support a subset of the webpack loader API.
Most CSS and CSS-in-JS libraries are supported:
- Supported
- Tailwind CSS
- @emotion/react
- Sass
- styled-components
- Bootstrap
- Antd
- node-sass
- JSS
- Emotion
- theme-ui (uses Emotion)
- @chakra-ui/core (with Emotion)
- aphrodite
- Not supported currently
- Less — You can add less-loader. Next.js with webpack doesn't support Less out of the box either.
- @vanilla-extract/css — Uses a custom webpack plugin — We're going to look into what it takes to support the required hooks in the future.
- StyleX — Requires a Babel transform and support for
data:
attributes — We're going to look into supporting StyleX afternext build --turbo
is stable.
Performance
We want to call out that the performance of the version released today is significantly better than that of the webpack, but it is not the final performance number. We've been following Kent Beck's famous formula of “Make it work. Make it good. Make it fast." So far, a large portion of our effort has gone towards the “Make it work” stage since we have to catch up to the scope of Next.js and webpack, which have matured for close to a decade.
Turbopack is betting heavily on its caching infrastructure, but as you may know, caching is one of the only two hard things in software development. From experience, we knew that adding caching to an architecture that wasn't explicitly built for it can lead to undesirable results, so we enabled caching for even the most granular functions. This means that rebuilds are extremely fast at the cost of cold builds and memory usage, and we are working towards a better balance. The neat thing is that we can use our advanced tracing mentioned earlier in the post to find inefficiencies and profile which functions are most worthwhile to cache.
Over the past 3 months, we've already made some significant improvements. Comparing Turbopack in Next.js 15 RC 2 versus Turbopack in 15 RC 1 shows the results of these optimizations:
- A 25-35% average reduction in memory usage.
- A 30-50% faster initial compilation for large pages with thousands of modules.
The stable version of Turbopack contains an in-memory cache that must be rebuilt on every restart of the development server, which can take ten or more seconds for large applications. Something we're extremely excited about are the big wins we're seeing when testing on-disk persistent caching, which we will cover later in this post.
Breaking changes
A huge motivation for building our own bundler was the need to match the existing behaviors of webpack as much as possible, which is something we couldn't guarantee with any existing solution at the time. This includes the way files are resolved and smaller features of webpack, such as the webpackIgnore
comment that some npm packages use.
Unfortunately, we did have to remove some features in order to future-proof Turbopack and the related Next.js implementation. Those features will still be supported when you use webpack.
There are a few highlights, let's dig into the reasons why we had to change them:
webpack()
configuration is not supported. Turbopack is not webpack, it doesn't have the same configuration option structure, though it does support many of the same features. Specifically we have implemented support for webpack loaders and resolve aliases. Most webpack loaders that are transforming code are supported out of the box. Some webpack loaders that do exotic things, like a webpack child compiler and emitting files, are not supported.
.babelrc
will not automatically transform code. Turbopack leverages SWC by default. You're still able to add babel-loader
as needed, but we're ensuring the defaults are always fast and that these make sense in terms of architecture too. We always have to run SWC, even if you configure .babelrc
, in order to process other optimizations. This is similar to how webpack always has to run the acorn
parser to do further optimizations. If you use SWC instead of Babel with Turbopack, we can parse once and leverage the same abstract syntax tree (AST) end-to-end throughout Turbopack.
Some lesser-used CSS Modules features. We've switched the processing of CSS from PostCSS to Lightning CSS. Lightning CSS is a significantly faster CSS compiler that supports CSS transformations, minification, and CSS Modules out of the box. The trade-off is that some lesser-used features are not supported. Specifically :global
and :local
pseudo selectors (their function variant :global()
and :local()
still work), @value
, and :import / :export
ICSS rules. It's also a bit stricter than other CSS parsers and will point to errors in code rather than ignore them.
In the process of adding Lightning CSS we've contributed back to the project. For example, we implemented granular options for CSS Modules to disable CSS grid prefixing and the pure
mode for CSS Modules. This makes it easier to adopt Lightning CSS for CSS Modules when coming from css-loader in webpack. We have also improved errors for the unsupported CSS Modules features.
We are thankful to Devon Govett, the author and maintainer of Lightning CSS, for the continued collaboration on the project.
Experimental features. As we are focused on Turbopack's stability in Next.js, we've decided to focus on the stable features that are available in Next.js first.
For the full list, see the documentation page.
Roadmap
Turbopack has come a long way, but there's still a lot of work to be done. The two exciting features coming down the pipeline are persistent caching and production builds. We expect the rollout to look something like the following order:
- Persistent caching — Future Minor
- Builds beta — Future Minor
- Builds release candidate — Future Minor
- Builds stable — Future Minor
- Recommended in create-next-app for new applications — Future Minor
- Default in Next.js when you don't have custom webpack configuration — Future Major
While webpack will stay in Next.js, we're expecting that because of the benefits of Turbopack, the majority of Next.js applications will want to use it. Once Turbopack for production builds is complete we'll start work to support commonly used webpack plugins.
We have loose plans for Turbopack beyond that, but we'd like to keep this post constrained to what we can confidently ship in the foreseeable future. We may only be talking about two features, but there's a lot that goes into them, so it's worth diving into.
Persistent caching (Fast Refresh across restarts)
Persistent caching means storing the work done by the compiler in a way that allows it to be reused across restarts of the development server or across multiple production builds.
In short, Turbopack avoids redoing the same work, even if you restart.
As mentioned in the Faster Fast Refresh section, we built Turbo Engine to ensure work can be parallelized and cached, so that whenever you make a file change, we only have to run the work related to that file change. What if we could give you this experience across restarts and when opening a route? We wouldn't have to redo compilation work that was already done in a previous development session. What if we could get the benefits of Fast Refresh but for opening routes compiled in previous development sessions and across multiple builds with the next build
?
That's exactly what we've been working on: a new storage layer for Turbo Engine that supports persisting the compilation work to disk and restoring it when starting the development server or building again.
While webpack does have disk caching enabled by default in Next.js, it has quite a few limitations. It's notable that a large portion of the cache has to be restored from disk and read into memory in order to function. It never quite felt like there is a granular enough cache. For example, on larger applications at Vercel, we found that the webpack disk cache could even be slower than doing all the work from scratch when the cache had grown to a sufficiently large size.
Unlike the existing disk caching with webpack, the persistent cache with Turbopack truly feels like Fast Refresh across restarts. Routes that take over 10 seconds to compile the very first time take less than 500ms to restore from cache once they've been compiled once.
We have seen similar results for next build
with Turbopack, where only the changed files are recompiled, and everything else stays as-is. In the multiple steps that next build
takes, this moves the majority of time spent from running compilation and bundling to running TypeScript type checking.
The persistent caching is currently a work in progress, as we want to verify it using our internal Next.js applications first. The initial results are very promising, and performance will get even better over time as we keep optimizing these hot paths.
Once the persistent cache is stable, it will be enabled by default. Enabling persistent caching will not require changes to your codebase.
If you are interested in testing out persistent caching, please reach out!
Production Builds
We're excited to share that we're making substantial progress towards stable production builds with Turbopack. Currently, 96% of our production tests are passing, which is a big step forward. However, there are still areas that need more work before we can confidently recommend Turbopack for production at scale.
Production builds bring their own unique challenges compared to development, and we're actively working to address them. Below, we'll go over what's already been optimized and what's still in progress.
Production Optimizations
Correctness
Ensuring correctness is essential for reliable production builds. Here's the current status:
- CSS Chunking: In progress. This feature is crucial for splitting CSS into smaller chunks, allowing only the necessary CSS to load for each part of the application, which helps reduce load times and ensures correct ordering of CSS rules..
- Production JS Runtime: Completed. This ensures that the JavaScript runtime behaves as expected in a production environment, providing reliability and stability.
- Content-Based File Name Hashing: Not yet implemented. Content-based hashing will allow us to generate filenames based on content, enabling more efficient long-term caching in browsers.
UX Performance Optimizations
UX Performance is key to delivering fast load times and efficient resource usage. Here's what we're working on:
- JS Minify: Completed. We've implemented SWC Minify, which Next.js already uses with webpack since Next.js 13.
- CSS Minify: Completed. CSS minification with Lightning CSS, which is important for reducing the size of stylesheets.
- Global Information (Whole Application Optimizations): Completed. Turbopack can apply optimizations that require data about all routes in the application, for example module id hashing.
- Tree Shaking: Partially completed. In progress. We have partial support for tree-shaking, which helps eliminate unused code and reduce bundle sizes. However, there are scenarios where tree-shaking is not fully effective yet:
- Dynamic Imports: Tree shaking is limited for dynamic imports like using
next/dynamic
. - Complex Exports: Certain types of exports, like
export { foo as "string name" }
. - Non-ES Modules: CommonJS modules are not tree-shakeable.
- Barrel Files: Re-exports from barrel files are inefficient, with limitations in skipping side-effect-free modules.
- Fragmentation: In some cases, tree-shaking can create too many fragments, leading to inefficient bundles.
- Dynamic Imports: Tree shaking is limited for dynamic imports like using
- Module ID Hashing (Partial): In progress. Module ID hashing is partially implemented but we're working on improving the performance. Once fully enabled, it will help reduce the final bundle size.
- Export Name Mangling: In progress. This involves reducing the size of exported names to reduce the final bundle size.
- Scope Hoisting: Not yet implemented. Scope hoisting will help reduce bundle size by merging smaller JavaScript modules into a single scope, which reduces overhead and improves performance.
- Production Optimized JS Chunking: Not yet implemented. Chunking JavaScript to minimize duplication is essential for improving load performance, especially for larger applications.
Stay Tuned
We're thrilled to confidently recommend the next dev --turbo
, and we can't wait to hear how it improves your development experience. Give it a try today and see the performance gains for yourself.
This is just the beginning—persistent caching and production builds are on the horizon, which will bring even more speed and reliability to your workflow.
We'll share more updates as we progress towards ensuring correctness and optimizing performance to handle even the largest applications seamlessly. Stay tuned for future releases and improvements as we work towards making Turbopack the best solution for both development and production builds.
Contributors
We are thankful to the thousands of developers who participated in testing, reporting issues, and verifying fixes throughout the Turbopack beta and release candidate phases.
This release was brought to you by:
```

---

## 22. Next.js 15 RC 2

- 日期: 2024-10-15 02:00
- 链接: https://nextjs.org/blog/next-15-rc2

```
Tuesday, October 15th 2024
Next.js 15 RC 2
Posted byFollowing the announcement of the first Next.js 15 Release Candidate back in May, we’ve been preparing a second Release Candidate based on your feedback. Here’s what we’ve been working on:
@next/codemod upgrade
: Easily upgrade to the latest Next.js and React versions.- Turbopack for development: Performance improvements and Next.js 15 stability target.
- Async Request APIs (Breaking): Incremental step towards a simplified rendering and caching model.
- Server Actions: Enhanced security with unguessable endpoints and removal of unused actions.
- Static Indicator: New visual indicator shows static routes during development.
next/form
: Enhance HTML forms with client-side navigation.next.config.ts
: TypeScript support for the Next.js configuration file.instrumentation.js
(Stable): New API for server lifecycle observability.- Development and Build improvements: Improved build times and Faster Fast Refresh.
- Self-hosting: More control over
Cache-Control
headers. - Linting: Added support for ESLint 9.
Try the Next.js 15 Release Candidate (RC2) today:
# Use the new automated upgrade CLI
npx @next/codemod@canary upgrade rc
# ...or upgrade manually
npm install next@rc react@rc react-dom@rc
Note: This Release Candidate includes all changes from the previous RC.
Smooth upgrades with codemod CLI
We include codemods (automated code transformations) with every major Next.js release to help automate upgrading breaking changes.
To make upgrades even smoother, we've released an enhanced codemod CLI:
npx @next/codemod@canary upgrade rc
This tool helps you upgrade your codebase to the latest stable or prerelease versions. The CLI will update your dependencies, show available codemods, and guide you through applying them. The specified dist tag on the command line (@rc
, @canary
, etc.) determines the version to upgrade to.
Learn more about Next.js codemods.
Turbopack for Development
Turbopack for local development will become stable in the general release of Next.js 15, while remaining opt-in. You can try it today by running:
next dev --turbo
Thanks to the thousands of developers who participated in testing, reporting issues, and verifying fixes throughout the Turbopack beta and release candidate phases, we've resolved 54 GitHub issues since the first Next.js 15 Release Candidate. Alongside this community effort, our internal testing on vercel.com, v0.app, and nextjs.org helped identify numerous additional improvements.
In the last three months, we've focused on optimizing cold compilation performance. Compared to the previous release, we've seen:
- 25–35% reduction in memory usage.
- 30–50% faster compilation for large pages with thousands of modules.
We will continue to optimize these areas in future releases.
Looking ahead, the Turbopack team is making significant progress on persistent caching, memory usage reduction, and Turbopack for next build
—with 96% of tests passing.
Note: See all of the supported and unsupported features of Turbopack.
Async Request APIs (Breaking Change)
In traditional Server-Side Rendering, the server waits for a request before rendering any content. However, not all components depend on request-specific data, so it's unnecessary to wait for the request to render them. Ideally, the server would prepare as much as possible before a request arrives. To enable this, and set the stage for future optimizations, we need to know when to wait for the request.
Therefore, we are transitioning APIs that rely on request-specific data—such as headers
, cookies
, params
, and searchParams
—to be asynchronous.
import { cookies } from 'next/headers';
export async function AdminPanel() {
const cookieStore = await cookies();
const token = cookieStore.get('token');
// ...
}
This is a breaking change and affects the following APIs:
cookies
headers
draftMode
params
inlayout.js
,page.js
,route.js
,default.js
,generateMetadata
, andgenerateViewport
searchParams
inpage.js
For an easier migration, these APIs can temporarily be accessed synchronously, but will show warnings in development and production until the next major version. A codemod is available to automate the migration:
npx @next/codemod@canary next-async-request-api .
For cases where the codemod can't fully migrate your code, please read the upgrade guide. We have also provided an example of how to migrate a Next.js application to the new APIs.
Enhanced Security for Server Actions
Server Actions are server-side functions that can be called from the client. They are defined by adding the 'use server'
directive at the top of a file and exporting an async function.
Even if a Server Action or utility function is not imported elsewhere in your code, it’s still a publicly accessible HTTP endpoint. While this behavior is technically correct, it can lead to unintentional exposure of such functions.
To improve security, we’ve introduced the following enhancements:
- Dead code elimination: Unused Server Actions won’t have their IDs exposed to the client-side JavaScript bundle, reducing bundle size and improving performance.
- Secure action IDs: Next.js now creates unguessable, non-deterministic IDs to allow the client to reference and call the Server Action. These IDs are periodically recalculated between builds for enhanced security.
// app/actions.js
'use server';
// This action **is** used in our application, so Next.js
// will create a secure ID to allow the client to reference
// and call the Server Action.
export async function updateUserAction(formData) {}
// This action **is not** used in our application, so Next.js
// will automatically remove this code during `next build`
// and will not create a public endpoint.
export async function deleteUserAction(formData) {}
You should still treat Server Actions as public HTTP endpoints. Learn more about securing Server Actions.
Static Route Indicator
Next.js now displays a Static Route Indicator during development to help you identify which routes are static or dynamic. This visual cue makes it easier to optimize performance by understanding how your pages are rendered.
You can also use the next build output to view the rendering strategy for all routes.
This update is part of our ongoing efforts to enhance observability in Next.js, making it easier for developers to monitor, debug, and optimize their applications. We're also working on dedicated developer tools, with more details to come soon.
Learn more about the Static Route Indicator, which can be disabled.
<Form>
Component
The new <Form>
component extends the HTML <form>
element with prefetching, client-side navigation, and progressive enhancement.
It is useful for forms that navigate to a new page, such as a search form that leads to a results page.
import Form from 'next/form';
export default function Page() {
return (
<Form action="/search">
<input name="query" />
<button type="submit">Submit</button>
</Form>
);
}
The <Form>
component comes with:
- Prefetching: When the form is in view, the layout and loading UI are prefetched, making navigation fast.
- Client-side Navigation: On submission, shared layouts and client-side state are preserved.
- Progressive Enhancement: If JavaScript hasn’t loaded yet, the form still works via full-page navigation.
Previously, achieving these features required a lot of manual boilerplate. For example:
Example
// Note: This is abbreviated for demonstration purposes.
// Not recommended for use in production code.
'use client'
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
export default function Form(props) {
const action = props.action
const router = useRouter()
useEffect(() => {
// if form target is a URL, prefetch it
if (typeof action === 'string') {
router.prefetch(action)
}
}, [action, router])
function onSubmit(event) {
event.preventDefault()
// grab all of the form fields and trigger a `router.push` with the data URL encoded
const formData = new FormData(event.currentTarget)
const data = new URLSearchParams()
for (const [name, value] of formData) {
data.append(name, value as string)
}
router.push(`${action}?${data.toString()}`)
}
if (typeof action === 'string') {
return <form onSubmit={onSubmit} {...props} />
}
return <form {...props} />
}
Learn more about the <Form>
Component.
Support for next.config.ts
Next.js now supports the TypeScript next.config.ts
file type and provides a NextConfig
type for autocomplete and type-safe options:
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
/* config options here */
};
export default nextConfig;
Learn more about TypeScript support in Next.js.
instrumentation.js
(Stable)
The instrumentation
file, with the register()
API, allows users to tap into the Next.js server lifecycle to monitor performance, track the source of errors, and deeply integrate with observability libraries like OpenTelemetry.
This feature is now stable and the experimental.instrumentationHook
config option can be removed.
In addition, we’ve collaborated with Sentry on designing a new onRequestError
hook that can be used to:
- Capture important context about all errors thrown on the server, including:
- Router: Pages Router or App Router
- Server context: Server Component, Server Action, Route Handler, or Middleware
- Report the errors to your favorite observability provider.
export async function onRequestError(err, request, context) {
await fetch('https://...', {
method: 'POST',
body: JSON.stringify({ message: err.message, request, context }),
headers: { 'Content-Type': 'application/json' },
});
}
export async function register() {
// init your favorite observability provider SDK
}
Learn more about the onRequestError
function.
Development and Build Improvements
Server Components HMR
During development, Server components are re-executed when saved. This means, any fetch
requests to your API endpoints or third-party services are also called.
To improve local development performance and reduce potential costs for billed API calls, we now ensure Hot Module Replacement (HMR) can re-use fetch
responses from previous renders.
Learn more about the Server Components HMR Cache.
Faster Static Generation for the App Router
We've optimized static generation to improve build times, especially for pages with slow network requests.
Previously, our static optimization process rendered pages twice—once to generate data for client-side navigation and a second time to render the HTML for the initial page visit. Now, we reuse the first render, cutting out the second pass, reducing workload and build times.
Additionally, static generation workers now share the fetch
cache across pages. If a fetch
call doesn’t opt out of caching, its results are reused by other pages handled by the same worker. This reduces the number of requests for the same data.
Advanced Static Generation Control (Experimental)
We’ve added experimental support for more control over static generation process for advanced use cases that would benefit from greater control.
We recommend sticking to the current defaults unless you have specific requirements as these options can lead to increased resource usage and potential out-of-memory errors due to increased concurrency.
const nextConfig = {
experimental: {
// how many times Next.js will retry failed page generation attempts
// before failing the build
staticGenerationRetryCount: 1
// how many pages will be processed per worker
staticGenerationMaxConcurrency: 8
// the minimum number of pages before spinning up a new export worker
staticGenerationMinPagesPerWorker: 25
},
}
export default nextConfig;
Learn more about the Static Generation options.
Improvements for self-hosting
When self-hosting applications, you may need more control over Cache-Control
directives.
One common case is controlling the stale-while-revalidate
period sent for ISR pages. We've implemented two improvements:
- You can now configure the
expireTime
value innext.config
. This was previously theexperimental.swrDelta
option. - Updated the default value to one year, ensuring most CDNs can fully apply the
stale-while-revalidate
semantics as intended.
We also no longer override custom Cache-Control
values with our default values, allowing full control and ensuring compatibility with any CDN setup.
Finally, we've improved image optimization when self-hosting. Previously, we recommended you install sharp
for optimizing images on your Next.js server. This recommendation was sometimes missed. With Next.js 15, you no longer need to manually install sharp
— Next.js will use sharp
automatically when using next start
or running with standalone output mode.
To learn more, see our new demo and tutorial video on self-hosting Next.js.
ESLint 9 Support
Next.js 15 also introduces support for ESLint 9, following the end-of-life for ESLint 8 on October 5, 2024.
To ensure a smooth transition, Next.js remain backwards compatible, meaning you can continue using either ESLint 8 or 9.
If you upgrade to ESLint 9, and we detect that you haven’t yet adopted the new config format, Next.js will automatically apply the ESLINT_USE_FLAT_CONFIG=false
escape hatch to ease migration.
Additionally, deprecated options like —ext
and —ignore-path
will be removed when running next lint
. Please note that ESLint will eventually disallow these older configurations in ESLint 10, so we recommend starting your migration soon.
For more details on these changes, check out the migration guide.
As part of this update, we’ve also upgraded eslint-plugin-react-hooks
to v5.0.0
, which introduces new rules for React Hooks usage. You can review all changes in the changelog for eslint-plugin-react-hooks@5.0.0.
Other Changes
- All of the changes previously described in the RC 1 blog post
- [Breaking] We’ve deprecated exporting
export const runtime = "experimental-edge"
in the App Router. Users should now switch toexport const runtime = "edge"
. We’ve added a codemod to perform this (PR) - [Breaking] Calling
revalidateTag
andrevalidatePath
during render will now throw an error (PR) - [Breaking] The
instrumentation.js
andmiddleware.js
files will now use the vendored React packages (PR) - [Breaking] The minimum required Node.js version has been updated to 18.18.0 (PR)
- [Breaking]
next/dynamic
: the deprecatedsuspense
prop has been removed and when the component is used in the App Router, it won't insert an empty Suspense boundary anymore (PR) - [Breaking] When resolving modules on the Edge Runtime, the
worker
module condition will not be applied (PR) - [Breaking] Disallow using
ssr: false
option withnext/dynamic
in Server Components (PR) - [Improvement] The
outputFileTracingRoot
,outputFileTracingIncludes
andoutputFileTracingExcludes
have been upgraded from experimental and are now stable (PR) - [Improvement] Avoid merging global CSS files with CSS module files deeper in the tree (PR)
- [Improvement] The cache handler can be specified via the
NEXT_CACHE_HANDLER_PATH
environment variable (PR) - [Improvement] The Pages Router now supports both React 18 and React 19 (PR)
- [Improvement] The Error Overlay now displays a button to copy the Node.js Inspector URL if the inspector is enabled (PR)
- [Improvement] Client prefetches on the App Router now use the
priority
attribute (PR) - [Improvement] Next.js now provides an
unstable_rethrow
function to rethrow Next.js internal errors in the App Router (PR) - [Improvement]
unstable_after
can now be used in static pages (PR) - [Improvement] If a
next/dynamic
component is used during SSR, the chunk will be prefetched (PR) - [Improvement] The
esmExternals
option is now supported on the App Router (PR) - [Improvement] The
experimental.allowDevelopmentBuild
option can be used to allowNODE_ENV=development
withnext build
for debugging purposes (PR) - [Improvement] The Server Action transforms are now disabled in the Pages Router (PR)
- [Improvement] Build workers will now stop the build from hanging when they exit (PR)
- [Improvement] When redirecting from a Server Action, revalidations will now apply correctly (PR)
- [Improvement] Dynamic params are now handled correctly for parallel routes on the Edge Runtime (PR)
- [Improvement] Static pages will now respect staleTime after initial load (PR)
- [Improvement]
vercel/og
updated with a memory leak fix (PR) - [Improvement] Patch timings updated to allow usage of packages like
msw
for APIs mocking (PR)
Contributors
Next.js is the result of the combined work of over 3,000 individual developers, and our core team at Vercel. This release was brought to you by:
- The Next.js team: Andrew, Hendrik, Janka, Jiachi, Jimmy, Jiwon, JJ, Josh, Sam, Sebastian, Sebbie, Shu, Wyatt, and Zack.
- The Turbopack team: Alex, Benjamin, Donny, Maia, Niklas, Tim, Tobias, and Will.
- The Next.js Docs team: Delba, Rich, Ismael, and Lee.
Huge thanks to @huozhi, @shuding, @wyattjoh, @PaulAsjes, @mcnaveen, @timneutkens, @stipsan, @aktoriukas, @sirTangale, @greatvivek11, @sokra, @anatoliik-lyft, @wbinnssmith, @coltonehrman, @hungdoansy, @kxlow, @ztanner, @manovotny, @leerob, @ryota-murakami, @ijjk, @pnutmath, @feugy, @Jeffrey-Zutt, @wiesson, @eps1lon, @devjiwonchoi, @Ethan-Arrowood, @kenji-webdev, @domdomegg, @samcx, @Jaaneek, @evanwinter, @kdy1, @balazsorban44, @feedthejim, @ForsakenHarmony, @kwonoj, @delbaoliveira, @xiaohanyu, @dvoytenko, @bobaaaaa, @bgw, @gaspar09, @souporserious, @unflxw, @kiner-tang, @Ehren12, @EffectDoplera, @IAmKushagraSharma, @Auxdible, @sean-rallycry, @jeanmax1me, @unstubbable, @NilsJacobsen, @adiguno, @ryan-nauman, @zsh77, @KagamiChan, @steveluscher, @MehfoozurRehman, @vkryachko, @chentsulin, @samijaber, @begalinsaf, @FluxCapacitor2, @lukahartwig, @brianshano, @pavelglac, @styfle, @symant233, @HristovCodes, @karlhorky, @jonluca, @jonathan-ingram, @mknichel, @sopranopillow, @Gomah, @imddc, @notrab, @gabrielrolfsen, @remorses, @AbhiShake1, @agadzik, @rishabhpoddar, @rezamauliadi, @IncognitoTGT, @webtinax, @BunsDev, @nisabmohd, @z0n, @bennettdams, @joeshub, @n1ckoates, @srkirkland, @RiskyMH, @coopbri, @okoyecharles, @diogocapela, @dnhn, @typeofweb, @davidsa03, @imranolas, @lubieowoce, @maxhaomh, @mirasayon, @blvdmitry, @hwangstar156, @lforst, @emmerich, @christian-bromann, @Lsnsh, @datner, @hiro0218, @flybayer, @ianmacartney, @ypessoa, @ryohidaka, @icyJoseph, @Arinji2, @lovell, @nsams, @Nayeem-XTREME, @JamBalaya56562, @Arindam200, @gaojude, @qqww08, @todor0v, @tokkiyaa, @arlyon, @lorensr, @Juneezee, @Sayakie, @IGassmann, @bosconian-dynamics, @phryneas, @akazwz, @atik-persei, @shubh73, @alpedia0, @chogyejin, @notomo, @ArnoldVanN, @dhruv-kaushik, @kevva, @Kahitar, @anay-208, @boris-szl, @devnyxie, @LorisSigrist, @M-YasirGhaffar, @Lada496, @kippmr, @torresgol10, @pkiv, @Netail, @jontewks, @ArnaudFavier, @chrisjstott, @mratlamwala, @mayank1513, @karlkeefer, @kshehadeh, @Marukome0743, @a89529294, @anku255, @KeisukeNagakawa, @andrii-bodnar, @aldosch, @versecafe, @steadily-worked, @cfrank, @QiuranHu, @farsabbutt, @joostmeijles, @saltcod, @archanaagivale30, @crutchcorn, @crebelskydico, @Maaz-Ahmed007, @jophy-ye, @remcohaszing, @JoshuaKGoldberg, @creativoma, @GyoHeon, @SukkaW, @MaxLeiter, @neila-a, @stylessh, @Teddir, @ManuLpz4, @Julian-Louis, @syi0808, @mert-duzgun, @amannn, @MonstraG, @hamirmahal, @tariknh, @Kikobeats, @LichuAcu, @Kuboczoch, @himself65, @Sam-Phillemon9493, @Shruthireddy04, @Hemanshu-Upadhyay, @timfuhrmann, @controversial, @pathliving, @mischnic, @mauroaccornero, @NavidNourani, @allanchau, @ekremkenter, @yurivangeffen, @gnoff, @darthmaim, @gdborton, @Willem-Jaap, @KentoMoriwaki, @TrevorSayre, @marlier, @Luluno01, @xixixao, @domin-mnd, @niketchandivade, @N2D4, @kjugi, @luciancah, @mud-ali, @codeSTACKr, @luojiyin1987, @mehmetozguldev, @ronanru, @tknickman, @joelhooks, @khawajaJunaid, @rubyisrust, @abdull-haseeb, @bewinsnw, @housseindjirdeh, @li-jia-nan, @aralroca, @s-ekai, @ah100101, @jantimon, @jordienr, @iscekic, @Strift, @slimbde, @nauvalazhar, @HughHzyb, @guisehn, @wesbos, @OlyaPolya, @paarthmadan, @AhmedBaset, @dineshh-m, @avdeev, @Bhavya031, @MildTomato, @Bjornnyborg, @amikofalvy, @yosefbeder, @kjac, @woutvanderploeg, @Ocheretovich, @ProchaLu, @luismiramirez, @omahs, @theoludwig, @abhi12299, @sommeeeer, @lumirlumir, @royalfig, @iampoul, @molebox, @txxxxc, @zce, @mamuso, @kahlstrm, @vercel-release-bot, @zhawtof, @PapatMayuri, @PlagueFPS, @IDNK2203, @jericopulvera, @liby, @CannonLock, @timfish, @whatisagi, @none23, @haouvw, @Pyr33x, @SouthLink, @frydj, @CrutchTheClutch, @sleevezip, @r34son, @yunsii, @md-rejoyan-islam, @kartheesan05, @nattui, @KonkenBonken, @weicheng95, @brekk, @Francoscopic, @B33fb0n3, @ImDR, @nurullah, @hdodov, @ebCrypto, @soedirgo, @floriangosse, @Tim-Zj, @raeyoung-kim, @erwannbst, @DerTimonius, @hirotomoyamada, @Develliot, @chandanpasunoori, @vicb, @ankur-dwivedi, @kidonng, @baeharam, @AnaTofuZ, @coderfin, @xugetsu, @alessiomaffeis, @kutsan, @jordyfontoura, @sebmarkbage, @tranvanhieu01012002, @jlbovenzo, @Luk-z, @jaredhan418, @bangseongbeom, @penicillin0, @neoFinch, @DeepakBalaraman, @Manoj-M-S, @Unsleeping, @lonr, @Aerilym, @ytori, @acdlite, @actopas, @n-ii-ma, @adcichowski, @mobeigi, @JohnGemstone, and @jjm2317 for helping!
```

---

## 23. Next.js 15 RC

- 日期: 2024-05-23 17:00
- 链接: https://nextjs.org/blog/next-15-rc

```
Thursday, May 23rd 2024
Next.js 15 RC
Posted byThe Next.js 15 Release Candidate (RC) is now available. This early version allows you to test the latest features before the upcoming stable release.
- React: Support for the React 19 RC, React Compiler (Experimental), and hydration error improvements
- Caching:
fetch
requests,GET
Route Handlers, and client navigations are no longer cached by default - Partial Prerendering (Experimental): New Layout and Page config option for incremental adoption
next/after
(Experimental): New API to execute code after a response has finished streamingcreate-next-app
: Updated design and a new flag to enable Turbopack in local development- Bundling external packages (Stable): New config options for App and Pages Router
Try the Next.js 15 RC today:
npm install next@rc react@rc react-dom@rc
React 19 RC
The Next.js App Router is built on the React canary channel for frameworks, which has allowed developers to use and provide feedback on these new React APIs before the v19 release.
Next.js 15 RC now supports React 19 RC, which includes new features for both the client and server like Actions.
Read the Next.js 15 upgrade guide, the React 19 upgrade guide, and watch the React Conf Keynote to learn more.
Note: Some third party libraries may not be compatible with React 19 yet.
React Compiler (Experimental)
The React Compiler is a new experimental compiler created by the React team at Meta. The compiler understands your code at a deep level through its understanding of plain JavaScript semantics and the Rules of React, which allows it to add automatic optimizations to your code. The compiler reduces the amount of manual memoization developers have to do through APIs such as useMemo
and useCallback
- making code simpler, easier to maintain, and less error prone.
With Next.js 15, we've added support for the React Compiler.
Install babel-plugin-react-compiler
:
npm install babel-plugin-react-compiler
Then, add experimental.reactCompiler
option in next.config.js
:
const nextConfig = {
experimental: {
reactCompiler: true,
},
};
module.exports = nextConfig;
Optionally, you can configure the compiler to run in "opt-in" mode as follows:
const nextConfig = {
experimental: {
reactCompiler: {
compilationMode: 'annotation',
},
},
};
module.exports = nextConfig;
Note: The React Compiler is currently only possible to use in Next.js through a Babel plugin, which could result in slower build times.
Learn more about the React Compiler, and the available Next.js config options.
Hydration error improvements
Next.js 14.1 made improvements to error messages and hydration errors. Next.js 15 continues to build on those by adding an improved hydration error view. Hydration errors now display the source code of the error with suggestions on how to address the issue.
For example, this was a previous hydration error message in Next.js 14.1:
Next.js 15 RC has improved this to:
Caching updates
Next.js App Router launched with opinionated caching defaults. These were designed to provide the most performant option by default with the ability to opt out when required.
Based on your feedback, we re-evaluated our caching heuristics and how they would interact with projects like Partial Prerendering (PPR) and with third party libraries using fetch
.
With Next.js 15, we’re changing the caching default for fetch
requests, GET
Route Handlers, and Client Router Cache from cached by default to uncached by default. If you want to retain the previous behavior, you can continue to opt-into caching.
We're continuing to improve caching in Next.js in the coming months and we'll share more details in the Next.js 15 GA announcement.
fetch
Requests are no longer cached by default
Next.js uses the Web fetch
API cache option to configure how a server-side fetch request interacts with the framework's persistent HTTP cache:
fetch('https://...', { cache: 'force-cache' | 'no-store' });
no-store
- fetch a resource from a remote server on every request and do not update the cacheforce-cache
- fetch a resource from the cache (if it exists) or a remote server and update the cache
In Next.js 14, force-cache
was used by default if a cache
option was not provided, unless a dynamic function or dynamic config option was used.
In Next.js 15, no-store
is used by default if a cache
option is not provided. This means fetch requests will not be cached by default.
You can still opt into caching fetch
requests by:
- Setting the
cache
option toforce-cache
in a singlefetch
call - Setting the
dynamic
route config option to'force-static'
for a single route - Setting the
fetchCache
route config option to'default-cache'
to override allfetch
requests in a Layout or Page to useforce-cache
unless they explicitly specify their owncache
option
GET
Route Handlers are no longer cached by default
In Next 14, Route Handlers that used the GET
HTTP method were cached by default unless they used a dynamic function or dynamic config option. In Next.js 15, GET
functions are not cached by default.
You can still opt into caching using a static route config option such as export dynamic = 'force-static'
.
Special Route Handlers like sitemap.ts
, opengraph-image.tsx
, and icon.tsx
, and other metadata files remain static by default unless they use dynamic functions or dynamic config options.
Client Router Cache no longer caches Page components by default
In Next.js 14.2.0, we introduced an experimental staleTimes
flag to allow custom configuration of the Router Cache.
In Next.js 15, this flag still remains accessible, but we are changing the default behavior to have a staleTime
of 0
for Page segments. This means that as you navigate around your app, the client will always reflect the latest data from the Page component(s) that become active as part of the navigation. However, there are still important behaviors that remain unchanged:
- Shared layout data won't be refetched from the server to continue to support partial rendering.
- Back/forward navigation will still restore from cache to ensure the browser can restore scroll position.
- Loading.js will remain cached for 5 minutes (or the value of the
staleTimes.static
configuration).
You can opt into the previous Client Router Cache behavior by setting the following configuration:
const nextConfig = {
experimental: {
staleTimes: {
dynamic: 30,
},
},
};
module.exports = nextConfig;
Incremental adoption of Partial Prerendering (Experimental)
In Next.js 14, we introduced Partial Prerendering (PPR) - an optimization that combines static and dynamic rendering on the same page.
Next.js currently defaults to static rendering unless you use dynamic functions such as cookies()
, headers()
, and uncached data requests. These APIs opt an entire route into dynamic rendering. With PPR, you can wrap any dynamic UI in a Suspense boundary. When a new request comes in, Next.js will immediately serve a static HTML shell, then render and stream the dynamic parts in the same HTTP request.
To allow for incremental adoption, we’ve added an experimental_ppr
route config option for opting specific Layouts and Pages into PPR:
import { Suspense } from "react"
import { StaticComponent, DynamicComponent } from "@/app/ui"
export const experimental_ppr = true
export default function Page() {
return {
<>
<StaticComponent />
<Suspense fallback={...}>
<DynamicComponent />
</Suspense>
</>
};
}
To use the new option, you’ll need to set the experimental.ppr
config in your next.config.js
file to 'incremental'
:
const nextConfig = {
experimental: {
ppr: 'incremental',
},
};
module.exports = nextConfig;
Once all the segments have PPR enabled, it’ll be considered safe for you to set the ppr
value to true
, and enable it for the entire app and all future routes.
We will share more about our PPR roadmap in our Next.js 15 GA blog post.
Learn more about Partial Prerendering.
Executing code after a response with next/after
(Experimental)
When processing a user request, the server typically performs tasks directly related to computing the response. However, you may need to perform tasks such as logging, analytics, and other external system synchronization.
Since these tasks are not directly related to the response, the user should not have to wait for them to complete. Deferring the work after responding to the user poses a challenge because serverless functions stop computation immediately after the response is closed.
after()
is a new experimental API that solves this problem by allowing you to schedule work to be processed after the response has finished streaming, enabling secondary tasks to run without blocking the primary response.
To use it, add experimental.after
to next.config.js
:
const nextConfig = {
experimental: {
after: true,
},
};
module.exports = nextConfig;
Then, import the function in Server Components, Server Actions, Route Handlers, or Middleware.
import { unstable_after as after } from 'next/server';
import { log } from '@/app/utils';
export default function Layout({ children }) {
// Secondary task
after(() => {
log();
});
// Primary task
return <>{children}</>;
}
Learn more about next/after
.
create-next-app
updates
For Next.js 15, we've updated create-next-app
with a new design.
When running create-next-app
, there is a new prompt asking if you want to enable Turbopack for local development (defaults to No
).
✔ Would you like to use Turbopack for next dev? … No / Yes
The --turbo
flag can be used to enable Turbopack.
npx create-next-app@rc --turbo
To make getting started on a new project even easier, a new --empty
flag has been added to the CLI. This will remove any extraneous files and styles, resulting in a minimal "hello world" page.
npx create-next-app@rc --empty
Optimizing bundling of external packages (Stable)
Bundling external packages can improve the cold start performance of your application. In the App Router, external packages are bundled by default, and you can opt-out specific packages using the new serverExternalPackages
config option.
In the Pages Router, external packages are not bundled by default, but you can provide a list of packages to bundle using the existing transpilePackages
option. With this configuration option, you need to specify each package.
To unify configuration between App and Pages Router, we’re introducing a new option, bundlePagesRouterDependencies
to match the default automatic bundling of the App Router. You can then use serverExternalPackages
to opt-out specific packages, if needed.
const nextConfig = {
// Automatically bundle external packages in the Pages Router:
bundlePagesRouterDependencies: true,
// Opt specific packages out of bundling for both App and Pages Router:
serverExternalPackages: ['package-name'],
};
module.exports = nextConfig;
Learn more about optimizing external packages.
Other Changes
- [Breaking] Minimum React version is now 19 RC
- [Breaking] next/image: Removed
squoosh
in favor ofsharp
as an optional dependency (PR) - [Breaking] next/image: Changed default
Content-Disposition
toattachment
(PR) - [Breaking] next/image: Error when
src
has leading or trailing spaces (PR) - [Breaking] Middleware: Apply
react-server
condition to limit unrecommended react API imports (PR) - [Breaking] next/font: Removed support for external
@next/font
package (PR) - [Breaking] next/font: Removed
font-family
hashing (PR) - [Breaking] Caching:
force-dynamic
will now set ano-store
default to the fetch cache (PR) - [Breaking] Config: Enable
swcMinify
(PR),missingSuspenseWithCSRBailout
(PR), andoutputFileTracing
(PR) behavior by default and remove deprecated options - [Breaking] Remove auto-instrumentation for Speed Insights (must now use the dedicated @vercel/speed-insights package) (PR)
- [Breaking] Remove
.xml
extension for dynamic sitemap routes and align sitemap URLs between development and production (PR) - [Improvement] Metadata: Updated environmental variable fallbacks for
metadataBase
when hosted on Vercel (PR) - [Improvement] Fix tree-shaking with mixed namespace and named imports from
optimizePackageImports
(PR) - [Improvement] Parallel Routes: Provide unmatched catch-all routes with all known params (PR)
- [Improvement] Config
bundlePagesExternals
is now stable and renamed tobundlePagesRouterDependencies
- [Improvement] Config
serverComponentsExternalPackages
is now stable and renamed toserverExternalPackages
- [Improvement] create-next-app: New projects ignore all
.env
files by default (PR) - [Docs] Improve auth documentation (PR)
- [Docs]
@next/env
package (PR)
To learn more, check out the upgrade guide.
Contributors
Next.js is the result of the combined work of over 3,000 individual developers, industry partners like Google and Meta, and our core team at Vercel. This release was brought to you by:
- The Next.js team: Andrew, Balazs, Ethan, Janka, Jiachi, Jimmy, JJ, Josh, Sam, Sebastian, Sebbie, Shu, Steven, Tim, Wyatt, and Zack.
- The Turbopack team: Alex, Benjamin, Donny, Leah, Maia, OJ, Tobias, and Will.
- Next.js Docs: Delba, Steph, Michael, Anthony, and Lee.
Huge thanks to @devjiwonchoi, @ijjk, @Ethan-Arrowood, @sokra, @kenji-webdev, @wbinnssmith, @huozhi, @domdomegg, @samcx, @Jaaneek, @evanwinter, @wyattjoh, @kdy1, @balazsorban44, @feedthejim, @ztanner, @ForsakenHarmony, @kwonoj, @delbaoliveira, @stipsan, @leerob, @shuding, @xiaohanyu, @timneutkens, @dvoytenko, @bobaaaaa, @bgw, @gaspar09, @souporserious, @unflxw, @kiner-tang, @Ehren12, @EffectDoplera, @IAmKushagraSharma, @Auxdible, @sean-rallycry, @Jeffrey-Zutt, @eps1lon, @jeanmax1me, @unstubbable, @NilsJacobsen, @PaulAsjes, @adiguno, @ryan-nauman, @zsh77, @KagamiChan, @steveluscher, @MehfoozurRehman, @vkryachko, @chentsulin, @samijaber, @begalinsaf, @FluxCapacitor2, @lukahartwig, @brianshano, @pavelglac, @styfle, @symant233, @HristovCodes, @karlhorky, @jonluca, @jonathan-ingram, @mknichel, @sopranopillow, @Gomah, @imddc, @notrab, @gabrielrolfsen, @remorses, @AbhiShake1, @agadzik, @ryota-murakami, @rishabhpoddar, @rezamauliadi, @IncognitoTGT, @webtinax, @BunsDev, @nisabmohd, @z0n, @bennettdams, @joeshub, @n1ckoates, @srkirkland, @RiskyMH, @coopbri, @okoyecharles, @diogocapela, @dnhn, @typeofweb, @davidsa03, @imranolas, @lubieowoce, @maxhaomh, @mirasayon, @blvdmitry, @hwangstar156, @lforst, @emmerich, @christian-bromann, @Lsnsh, @datner, @hiro0218, @flybayer, @ianmacartney, @ypessoa, @ryohidaka, @icyJoseph, @Arinji2, @lovell, @nsams, @Nayeem-XTREME, @JamBalaya56562, @Arindam200, @gaojude, @qqww08, @todor0v, @coltonehrman, and @wiesson for helping!
```

---

## 24. Next.js 14.2

- 日期: 2024-04-11 17:00
- 链接: https://nextjs.org/blog/next-14-2

```
Thursday, April 11th 2024
Next.js 14.2
Posted byNext.js 14.2 includes development, production, and caching improvements.
- Turbopack for Development (Release Candidate): 99.8% tests passing for
next dev --turbo
. - Build and Production Improvements: Reduced build memory usage and CSS optimizations.
- Caching Improvements: Configurable invalidation periods with
staleTimes
. - Error DX Improvements: Better hydration mismatch errors and design updates.
Upgrade today or get started with:
npx create-next-app@latest
Turbopack for Development (Release Candidate)
Over the past few months, we’ve been working on improving local development performance with Turbopack. In version 14.2, the Turbopack Release Candidate is now available for local development:
- 99.8% of integrations tests are now passing.
- We’ve verified the top 300
npm
packages used in Next.js applications can compile with Turbopack. - All Next.js examples work with Turbopack.
- We’ve integrated Lightning CSS, a fast CSS bundler and minifier, written in Rust.
We’ve been extensively dogfooding Turbopack with Vercel’s applications. For example, with vercel.com
, a large Next.js app, we've seen:
- Up to 76.7% faster local server startup.
- Up to 96.3% faster code updates with Fast Refresh.
- Up to 45.8% faster initial route compile without caching (Turbopack does not have disk caching yet).
Turbopack continues to be opt-in and you can try it out with:
next dev --turbo
We will now be focusing on improving memory usage, implementing persistent caching, and next build --turbo
.
- Memory Usage - We’ve built low-level tools for investigating memory usage. You can now generate traces that include both performance metrics and broad memory usage information. These traces allows us to investigate performance and memory usage without needing access to your application’s source code.
- Persistent Caching - We’re also exploring the best architecture options, and we’re expecting to share more details in a future release.
next build
- While Turbopack is not available for builds yet, 74.7% of tests are already passing. You can follow the progress at areweturboyet.com/build.
To see a list of supported and unsupported features in Turbopack, please refer to our documentation.
Build and Production Improvements
In addition to bundling improvements with Turbopack, we’ve worked to improve overall build and production performance for all Next.js applications (both Pages and App Router).
Tree-shaking
We identified an optimization for the boundary between Server and Client Components that allows for tree-shaking unused exports. For example, importing a single Icon
component from a file that has "use client"
no longer includes all the other icons from that package. This can largely reduce the production JavaScript bundle size.
Testing this optimization on a popular library like react-aria-components
reduced the final bundle size by -51.3%.
Note: This optimization does not currently work with barrel files. In the meantime, you can use the
optimizePackageImports
config option:next.config.tsmodule.exports = { experimental: { optimizePackageImports: ['package-name'], }, };
Build Memory Usage
For extremely large-scale Next.js applications, we noticed out-of-memory crashes (OOMs) during production builds. After investigating user reports and reproductions, we identified the root issue was over-bundling and minification (Next.js created fewer, larger JavaScript files with duplication). We’ve refactored the bundling logic and optimized the compiler for these cases.
Our early tests show that on a minimal Next.js app, memory usage and cache file size decreased from 2.2GB to under 190MB on average.
To make it easier to debug memory performance, we’ve introduced a --experimental-debug-memory-usage
flag to next build
. Learn more in our documentation.
CSS
We updated how CSS is optimized during production Next.js builds by chunking CSS to avoid conflicting styles when you navigate between pages.
The order and merging of CSS chunks are now defined by the import order. For example, base-button.module.css
will be ordered before page.module.css
:
import styles from './base-button.module.css';
export function BaseButton() {
return <button className={styles.primary} />;
}
import { BaseButton } from './base-button';
import styles from './page.module.css';
export function Page() {
return <BaseButton className={styles.primary} />;
}
To maintain the correct CSS order, we recommend:
- Using CSS Modules over global styles.
- Only import a CSS Module in a single JS/TS file.
- If using global class names, import the global styles in the same JS/TS too.
We don’t expect this change to negatively impact the majority of applications. However, if you see any unexpected styles when upgrading, please review your CSS import order as per the recommendations in our documentation.
Caching Improvements
Caching is a critical part of building fast and reliable web applications. When performing mutations, both users and developers expect the cache to be updated to reflect the latest changes. We've been exploring how to improve the Next.js caching experience in the App Router.
staleTimes
(Experimental)
The Client-side Router Cache is a caching layer designed to provide a fast navigation experience by caching visited and prefetched routes on the client.
Based on community feedback, we’ve added an experimental staleTimes
option to allow the client-side router cache invalidation period to be configured.
By default, prefetched routes (using the <Link>
component without the prefetch
prop) will be cached for 30 seconds, and if the prefetch
prop is set to true
, 5 minutes. You can overwrite these default values by defining custom revalidation times in next.config.js
:
const nextConfig = {
experimental: {
staleTimes: {
dynamic: 30,
static: 180,
},
},
};
module.exports = nextConfig;
staleTimes
aims to improve the current experience of users who want more control over caching heuristics, but it is not intended to be the complete solution. In upcoming releases, we will focus on improving the overall caching semantics and providing more flexible solutions.
Learn more about staleTimes
in our documentation.
Parallel and Intercepting Routes
We are continuing to iterate on on Parallel and Intercepting Routes, now improving the integration with the Client-side Router Cache.
- Parallel and Intercepting routes that invoke Server Actions with
revalidatePath
orrevalidateTag
will revalidate the cache and refresh the visible slots while maintaining the user’s current view. - Similarly, calling
router.refresh
now correctly refreshes visible slots, maintaining the current view.
Errors DX Improvements
In version 14.1, we started working on improving the readability of error messages and stack traces when running next dev
. This work has continued into 14.2 to now include better error messages, overlay design improvements for both App Router and Pages Router, light and dark mode support, and clearer dev
and build
logs.
For example, React Hydration errors are a common source of confusion in our community. While we made improvements to help users pinpoint the source of hydration mismatches (see below), we're working with the React team to improve the underlying error messages and show the file name where the error occurred.
Before:
After:
React 19
In February, the React team announced the upcoming release of React 19. To prepare for React 19, we're working on integrating the latest features and improvements into Next.js, and plan on releasing a major version to orchestrate these changes.
New features like Actions and their related hooks, which have been available within Next.js from the React canary channel, will now all be available for all React applications (including client-only applications). We're excited to see wider adoption of these features in the React ecosystem.
Other Improvements
- [Docs] New documentation on Video Optimization (PR).
- [Docs] New documentation on
instrumentation.ts
(PR) - [Feature] New
overrideSrc
prop fornext/image
(PR). - [Feature] New
revalidateReason
argument togetStaticProps
(PR). - [Improvement] Refactored streaming logic, reducing the time to stream pages in production (PR).
- [Improvement] Support for nested Server Actions (PR).
- [Improvement] Support for localization in generated Sitemaps (PR).
- [Improvement] Visual improvements to dev and build logs (PR)
- [Improvement] Skew protection is stable on Vercel (Docs).
- [Improvement] Make
useSelectedLayoutSegment
compatible with the Pages Router (PR). - [Improvement] Skip
metadataBase
warnings when absolute URLs don’t need to be resolved (PR). - [Improvement] Fix Server Actions not submitting without JavaScript enabled when deployed to Vercel (PR)
- [Improvement] Fix error about a Server Action not being found in the actions manifest if triggered after navigating away from referring page, or if used inside of an inactive parallel route segment (PR)
- [Improvement] Fix CSS imports in components loaded by
next/dynamic
(PR). - [Improvement] Warn when animated image is missing
unoptimized
prop (PR). - [Improvement] Show an error message if
images.loaderFile
doesn't export a default function (PR)
Community
Next.js now has over 1 million monthly active developers. We're grateful for the community's support and contributions. Join the conversation on GitHub Discussions, Reddit, and Discord.
Contributors
Next.js is the result of the combined work of over 3,000 individual developers, industry partners like Google and Meta, and our core team at Vercel. This release was brought to you by:
- The Next.js team: Andrew, Balazs, Ethan, Janka, Jiachi, Jimmy, JJ, Josh, Sam, Sebastian, Sebbie, Shu, Steven, Tim, Wyatt, and Zack.
- The Turbopack team: Donny, Leah, Maia, OJ, Tobias, and Will.
- Next.js Docs: Delba, Steph, Michael, Anthony, and Lee.
Huge thanks to @taishikato, @JesseKoldewijn, @Evavic44, @feugy, @liamlaverty, @dvoytenko, @SukkaW, @wbinnssmith, @rishabhpoddar, @better-salmon, @ziyafenn, @A7med3bdulBaset, @jasonuc, @yossydev, @Prachi-meon, @InfiniteCodeMonkeys, @ForsakenHarmony, @miketimmerman, @kwonoj, @williamli, @gnoff, @jsteele-stripe, @chungweileong94, @WITS, @sogoagain, @junioryono, @eisafaqiri, @yannbolliger, @aramikuto, @rocketman-21, @kenji-webdev, @michaelpeterswa, @Dannymx, @vpaflah, @zeevo, @chrisweb, @stefangeneralao, @tknickman, @Kikobeats, @ubinatus, @code-haseeb, @hmmChase, @byhow, @DanielRivers, @wojtekmaj, @paramoshkinandrew, @OMikkel, @theitaliandev, @oliviertassinari, @Ishaan2053, @Sandeep-Mani, @alyahmedaly, @Lezzio, @devjiwonchoi, @juliusmarminge, @szmazhr, @eddiejaoude, @itz-Me-Pj, @AndersDJohnson, @gentamura, @tills13, @dijonmusters, @SaiGanesh21, @vordgi, @ryota-murakami, @tszhong0411, @officialrajdeepsingh, @alexpuertasr, @AkifumiSato, @Jonas-PFX, @icyJoseph, @florian-lp, @pbzona, @erfanium, @remcohaszing, @bernardobelchior, @willashe, @kevinmitch14, @smakosh, @mnjongerius, @asobirov, @theoholl, @suu3, @ArianHamdi, @adrianha, @Sina-Abf, @kuzeykose, @meenie, @nphmuller, @javivelasco, @belgattitude, @Svetoslav99, @johnslemmer, @colbyfayock, @mehranmf31, @m-nakamura145, @ryo8000, @aryaemami59, @bestlyg, @jinsoul75, @petrovmiroslav, @nattui, @zhuyedev, @dongwonnn, @nhducit, @flotwig, @Schmavery, @abhinaypandey02, @rvetere, @coffeecupjapan, @cjimmy, @Soheiljafarnejad, @jantimon, @zengspr, @wesbos, @neomad1337, @MaxLeiter, and @devr77 for helping!
```

---

## 25. Next.js 14.1

- 日期: 2024-01-18 16:00
- 链接: https://nextjs.org/blog/next-14-1

```
Thursday, January 18th 2024
Next.js 14.1
Posted byNext.js 14.1 includes developer experience improvements including:
- Improved Self-Hosting: New documentation and custom cache handler
- Turbopack Improvements: 5,600 tests passing for
next dev --turbo
- DX Improvements: Improved error messages,
pushState
andreplaceState
support - Parallel & Intercepted Routes: 20 bug fixes based on your feedback
next/image
Improvements:<picture>
, art direction, and dark mode support
Upgrade today or get started with:
npx create-next-app@latest
Improved Self-Hosting
We've heard your feedback for improved clarity on how to self-host Next.js with a Node.js server, Docker container, or static export. We've overhauled our self-hosting documentation on:
- Runtime environment variables
- Custom cache configuration for ISR
- Custom image optimization
- Middleware
With Next.js 14.1, we've also stabilized providing custom cache handlers for Incremental Static Regeneration and the more granular Data Cache for the App Router:
module.exports = {
cacheHandler: require.resolve('./cache-handler.js'),
cacheMaxMemorySize: 0, // disable default in-memory caching
};
Using this configuration when self-hosting is important when using container orchestration platforms like Kubernetes, where each pod will have a copy of the cache. Using a custom cache handler will allow you to ensure consistency across all pods hosting your Next.js application.
For instance, you can save the cached values anywhere, like Redis or Memcached. We'd like to thank @neshca
for their Redis cache handler adapter and example.
Turbopack Improvements
We're continuing to focus on the reliability and performance of local Next.js development:
- Reliability: Turbopack passing the entire Next.js development test suite and dogfooding Vercel's applications
- Performance: Improving Turbopack initial compile times and Fast Refresh times
- Memory Usage: Improving Turbopack memory usage
We plan to stabilize next dev --turbo
in an upcoming release with it still being opt-in.
Reliability
Next.js with Turbopack now passes 5,600 development tests (94%), 600 more since the last update. You can follow the progress on areweturboyet.com.
We have continued dogfooding next dev --turbo
on all Vercel's Next.js applications, including vercel.com and v0.app. All engineers working on these applications are using Turbopack daily.
We've found and fixed a number of issues for very large Next.js applications using Turbopack. For these fixes, we've added new tests to the existing development test suites in Next.js.
Performance
For vercel.com
, a large Next.js application, we've seen:
- Up to 76.7% faster local server startup
- Up to 96.3% faster code updates with Fast Refresh
- Up to 45.8% faster initial route compile without caching (Turbopack does not have disk caching yet)
In v0.app, we identified an opportunity to optimize the way React Client Components are discovered and bundled in Turbopack - resulting in up to 61.5% faster initial compile time. This performance improvement was also observed in vercel.com.
Future Improvements
Turbopack currently has in-memory caching, which improves incremental compilation times for Fast Refresh.
However, the cache is currently not preserved when restarting the Next.js development server. The next big step for Turbopack performance is disk caching, which will allow the cache to be preserved when restating the development server.
Developer Experience Improvements
Improved Error Messages and Fast Refresh
We know how critical clear error messages are to your local development experience. We've made a number of fixes to improve the quality of stack traces and error messages you see when running next dev
.
- Errors that previously displayed bundler errors like
webpack-internal
now properly display the source code of the error and the affected file. - After seeing an error in a client component, and then fixing the error in your editor, the Fast Refresh did not clear the error screen. It required a hard reload. We've fixed a number of these instances. For example, trying to export
metadata
from a Client Component.
For example, this was a previous error message:
Next.js 14.1 has improved this to:
window.history.pushState
and window.history.replaceState
The App Router now allows the usage of the native pushState
and replaceState
methods to update the browser's history stack without reloading the page.
pushState
and replaceState
calls integrate into the Next.js App Router, allowing you to sync with usePathname
and useSearchParams
.
This is helpful when needing to immediately update the URL when saving state like filters, sort order, or other information desired to persist across reloads.
'use client';
import { useSearchParams } from 'next/navigation';
export default function SortProducts() {
const searchParams = useSearchParams();
function updateSorting(sortOrder: string) {
const params = new URLSearchParams(searchParams.toString());
params.set('sort', sortOrder);
window.history.pushState(null, '', `?${params.toString()}`);
}
return (
<>
<button onClick={() => updateSorting('asc')}>Sort Ascending</button>
<button onClick={() => updateSorting('desc')}>Sort Descending</button>
</>
);
}
Learn more about using the native History API with Next.js.
Data Cache Logging
For improved observability of your cached data in your Next.js application when running next dev
, we've made a number of improvements to the logging
configuration option.
You can now display whether there was a cache HIT
or SKIP
and the full URL requested:
GET / 200 in 48ms
✓ Compiled /fetch-cache in 117ms
GET /fetch-cache 200 in 165ms
│ GET https://api.vercel.app/products/1 200 in 14ms (cache: HIT)
✓ Compiled /fetch-no-store in 150ms
GET /fetch-no-store 200 in 548ms
│ GET https://api.vercel.app/products/1 200 in 345ms (cache: SKIP)
│ │ Cache missed reason: (cache: no-store)
This can be enabled through next.config.js
:
module.exports = {
logging: {
fetches: {
fullUrl: true,
},
},
};
next/image
support for <picture>
and Art Direction
The Next.js Image component now supports more advanced use cases through getImageProps()
(stable) which don't require using <Image>
directly. This includes:
- Working with
background-image
orimage-set
- Working with canvas
context.drawImage()
ornew Image()
- Working with
<picture>
media queries to implement Art Direction or Light/Dark Mode images
import { getImageProps } from 'next/image';
export default function Page() {
const common = { alt: 'Hero', width: 800, height: 400 };
const {
props: { srcSet: dark },
} = getImageProps({ ...common, src: '/dark.png' });
const {
props: { srcSet: light, ...rest },
} = getImageProps({ ...common, src: '/light.png' });
return (
<picture>
<source media="(prefers-color-scheme: dark)" srcSet={dark} />
<source media="(prefers-color-scheme: light)" srcSet={light} />
<img {...rest} />
</picture>
);
}
Learn more about getImageProps()
.
Parallel & Intercepted Routes
In Next.js 14.1, we've made 20 improvements to Parallel & Intercepted Routes.
For the past two releases, we've been focused on improving performance and reliability of Next.js. We've now been able to make many improvements to Parallel & Intercepted Routes based on your feedback. Notably, we've added support for catch-all routes and Server Actions.
- Parallel Routes allow you to simultaneously or conditionally render one or more pages in the same layout. For highly dynamic sections of an app, such as dashboards and feeds on social sites, Parallel Routes can be used to implement complex routing patterns.
- Intercepted Routes allow you to load a route from another part of your application within the current layout. For example, when clicking on a photo in a feed, you can display the photo in a modal, overlaying the feed. In this case, Next.js intercepts the
/photo/123
route, masks the URL, and overlays it over/feed
.
Learn more about Parallel & Intercepted Routes or view an example.
Other Improvements
Since 14.0
, we've fixed a number of highly upvoted bugs from the community.
We've also recently published videos explaining caching and some common mistakes with the App Router that you might find helpful.
- [Docs] New documentation on Redirecting
- [Docs] New documentation on Testing
- [Docs] New documentation with a Production Checklist
- [Feature] Add
<GoogleAnalytics />
component tonext/third-parties
(Docs) - [Improvement]
create-next-app
is now smaller and faster to install (PR) - [Improvement] Nested routes throwing errors can still be caught be
global-error
(PR) - [Improvement]
redirect
now respectsbasePath
when used in a server action (PR) - [Improvement] Fix
next/script
andbeforeInteractive
usage with App Router (PR) - [Improvement] Automatically transpile
@aws-sdk
andlodash
for faster route startup (PR) - [Improvement] Fix flash of unstyled content with
next dev
andnext/font
(PR) - [Improvement] Propagate
notFound
errors past a segment's error boundary (PR) - [Improvement] Fix serving public files from locale domains with Pages Router i18n (PR)
- [Improvement] Error if an invalidate
revalidate
value is passed (PR) - [Improvement] Fix path issues on linux machines when build created on windows (PR)
- [Improvement] Fix Fast Refresh / HMR when using a multi-zone app with
basePath
(PR) - [Improvement] Improve graceful shutdown from termination signals (PR)
- [Improvement] Modal routes clash when intercepting from different routes (PR)
- [Improvement] Fix intercepting routes when using
basePath
config (PR) - [Improvement] Show warning when a missing parallel slot results in 404 (PR)
- [Improvement] Improve intercepted routes when used with catch-all routes (PR)
- [Improvement] Improve intercepted routes when used with
revalidatePath
(PR) - [Improvement] Fix usage of
@children
slots with parallel routes (PR) - [Improvement] Fix Fix TypeError when using params with parallel routes (PR)
- [Improvement] Fix catch-all route normalization for default parallel routes (PR)
- [Improvement] Fix display of parallel routes in the
next build
summary (PR) - [Improvement] Fix for route parameters when using intercepted routes (PR)
- [Improvement] Improve deeply nested parallel/intercepted routes (PR)
- [Improvement] Fix 404 with intercepted routes paired with route groups (PR)
- [Improvement] Fix parallel routes with server actions / revalidating router cache (PR)
- [Improvement] Fix usage of
rewrites
with an intercepted route (PR) - [Improvement] Server Actions now work from third-party libraries (PR)
- [Improvement] Next.js can now be used within an ESM package (PR)
- [Improvement] Barrel file optimizations for libraries like Material UI (PR)
- [Improvement] Builds will now fail on incorrect usage of
useSearchParams
withoutSuspense
(PR)
Contributors
Next.js is the result of the combined work of over 3,000 individual developers, industry partners like Google and Meta, and our core team at Vercel. Join the community on GitHub Discussions, Reddit, and Discord.
This release was brought to you by:
- The Next.js team: Andrew, Balazs, Jiachi, Jimmy, JJ, Josh, Sebastian, Shu, Steven, Tim, Wyatt, and Zack.
- The Turbopack team: Donny, Leah, Maia, OJ, Tobias, and Will.
- Next.js Docs: Delba, Steph, Michael, and Lee.
And the contributions of: @OlehDutchenko, @eps1lon, @ebidel, @janicklas-ralph, @JohnPhamous, @chentsulin, @akawalsky, @BlankParticle, @dvoytenko, @smaeda-ks, @kenji-webdev, @rv-david, @icyJoseph, @dijonmusters, @A7med3bdulBaset, @jenewland1999, @mknichel, @kdy1, @housseindjirdeh, @max-programming, @redbmk, @SSakibHossain10, @jamesmillerburgess, @minaelee, @officialrajdeepsingh, @LorisSigrist, @yesl-kim, @StevenKamwaza, @manovotny, @mcexit, @remcohaszing, @ryo-manba, @TranquilMarmot, @vinaykulk621, @haritssr, @divquan, @IgorVaryvoda, @LukeSchlangen, @RiskyMH, @ash2048, @ManuWeb3, @msgadi, @dhayab, @ShahriarKh, @jvandenaardweg, @DestroyerXyz, @SwitchBladeAK, @ianmacartney, @justinh00k, @tiborsaas, @ArianHamdi, @li-jia-nan, @aramikuto, @jquinc30, @samcx, @Haosik, @AkifumiSato, @arnabsen, @nfroidure, @clbn, @siddtheone, @zbauman3, @anthonyshew, @alexfradiani, @CalebBarnes, @adk96r, @pacexy, @hichemfantar, @michaldudak, @redonkulus, @k-taro56, @mhughdo, @tknickman, @shumakmanohar, @vordgi, @hamirmahal, @gaspar09, @JCharante, @sjoerdvanBommel, @mass2527, @N-Ziermann, @tordans, @davidthorand, @rmathew8-gh, @chriskrogh, @shogunsea, @auipga, @SukkaW, @agustints, @OXXD, @clarencepenz, @better-salmon, @808vita, @coltonehrman, @tksst, @hugo-syn, @JakobJingleheimer, @Willem-Jaap, @brandonnorsworthy, @jaehunn, @jridgewell, @gtjamesa, @mugi-uno, @kentobento, @vivianyentran, @empflow, @samennis1, @mkcy3, @suhaotian, @imevanc, @d3lm, @amannn, @hallatore, @Dylan700, @mpsq, @mdio, @christianvuerings, @karlhorky, @simonhaenisch, @olci34, @zce, @LavaToaster, @rishabhpoddar, @jirihofman, @codercor, @devjiwonchoi, @JackieLi565, @thoushif, @pkellner, @jpfifer, @quisido, @tomfa, @raphaelbadia, @j9141997, @hongaar, @MadCcc, @luismulinari, @dumb-programmer, @nonoakij, @franky47, @robbertstevens, @bryndyment, @marcosmartini, @functino, @Anisi, @AdonisAgelis, @seangray-dev, @prkagrawal, @heloineto, @kn327, @ihommani, @MrNiceRicee, @falsepopsky, @thomasballinger, @tmilewski, @Vadman97, @dnhn, @RodrigoTomeES, @sadikkuzu, @gffuma, @Schniz, @joulev, @Athrun-Judah, @rasvanjaya21, @rashidul0405, @nguyenbry, @Mwimwii, @molebox, @mrr11k, @philwolstenholme, @IgorKowalczyk, @Zoe-Bot, @HanCiHu, @JackHowa, @goncy, @hirotomoyamada, @pveyes, @yeskunall, @ChendayUP, @hmaesta, @ajz003, @its-kunal, @joelhooks, @blurrah, @tariknh, @Vinlock, @Nayeem-XTREME, @aziyatali, @aspehler, and @moka-ayumu.
```

---

## 26. Next.js 14

- 日期: 2023-10-26 16:00
- 链接: https://nextjs.org/blog/next-14

```
Thursday, October 26th 2023
Next.js 14
Posted byAs we announced at Next.js Conf, Next.js 14 is our most focused release with:
- Turbopack: 5,000 tests passing for App & Pages Router
- 53% faster local server startup
- 94% faster code updates with Fast Refresh
- Server Actions (Stable): Progressively enhanced mutations
- Integrated with caching & revalidating
- Simple function calls, or works natively with forms
- Partial Prerendering (Preview): Fast initial static response + streaming dynamic content
- Next.js Learn (New): Free course teaching the App Router, authentication, databases, and more.
Upgrade today or get started with:
npx create-next-app@latest
Next.js Compiler: Turbocharged
Since Next.js 13, we've been working to improve local development performance in Next.js in both the Pages and App Router.
Previously, we were rewriting next dev
and other parts of Next.js to support this effort. We have since changed our approach to be more incremental. This means our Rust-based compiler will reach stability soon, as we've refocused on supporting all Next.js features first.
5,000 integration tests for next dev
are now passing with Turbopack, our underlying Rust engine. These tests include 7 years of bug fixes and reproductions.
While testing on vercel.com
, a large Next.js application, we've seen:
- Up to 53.3% faster local server startup
- Up to 94.7% faster code updates with Fast Refresh
This benchmark is a practical result of performance improvements you should expect with a large application (and large module graph). With 90% of tests for next dev
now passing, you should see faster and more reliable performance consistently when using next dev --turbo
.
Once we hit 100% of tests passing, we'll move Turbopack to stable in an upcoming minor release. We'll also continue to support using webpack for custom configurations and ecosystem plugins.
You can follow the percentage of tests passing at areweturboyet.com.
Forms and Mutations
Next.js 9 introduced API Routes—a way to quickly build backend endpoints alongside your frontend code.
For example, you would create a new file in the api/
directory:
import type { NextApiRequest, NextApiResponse } from 'next';
export default async function handler(
req: NextApiRequest,
res: NextApiResponse,
) {
const data = req.body;
const id = await createItem(data);
res.status(200).json({ id });
}
Then, on the client-side, you could use React and an event handler like onSubmit
to make a fetch
to your API Route.
import { FormEvent } from 'react';
export default function Page() {
async function onSubmit(event: FormEvent<HTMLFormElement>) {
event.preventDefault();
const formData = new FormData(event.currentTarget);
const response = await fetch('/api/submit', {
method: 'POST',
body: formData,
});
// Handle response if necessary
const data = await response.json();
// ...
}
return (
<form onSubmit={onSubmit}>
<input type="text" name="name" />
<button type="submit">Submit</button>
</form>
);
}
Now with Next.js 14, we want to simplify the developer experience of authoring data mutations. Further, we want to improve the user experience when the user has a slow network connection, or when submitting a form from a lower-powered device.
Server Actions (Stable)
What if you didn't need to manually create an API Route? Instead, you could define a function that runs securely on the server, called directly from your React components.
The App Router is built on the React canary
channel, which is stable for frameworks to adopt new features. As of v14, Next.js has upgraded to the latest React canary
, which includes stable Server Actions.
The previous example from the Pages Router can be simplified to one file:
export default function Page() {
async function create(formData: FormData) {
'use server';
const id = await createItem(formData);
}
return (
<form action={create}>
<input type="text" name="name" />
<button type="submit">Submit</button>
</form>
);
}
Server Actions should feel familiar for any developers who have previously used server-centric frameworks in the past. It's built on web fundamentals like forms and the FormData Web API.
While using Server Actions through a form is helpful for progressive enhancement, it is not a requirement. You can also call them directly as a function, without a form. When using TypeScript, this gives you full end-to-end type-safety between the client and server.
Mutating data, re-rendering the page, or redirecting can happen in one network roundtrip, ensuring the correct data is displayed on the client, even if the upstream provider is slow. Further, you can compose and reuse different actions, including many different actions in the same route.
Caching, Revalidating, Redirecting, and more
Server Actions are deeply integrated into the entire App Router model. You can:
- Revalidate cached data with
revalidatePath()
orrevalidateTag()
- Redirect to different routes through
redirect()
- Set and read cookies through
cookies()
- Handle optimistic UI updates with
useOptimistic()
- Catch and display errors from the server with
useFormState()
- Display loading states on the client with
useFormStatus()
Learn more about Forms and Mutations with Server Actions or about the security model and best practices for Server Components and Server Actions.
Partial Prerendering (Preview)
We'd like to share a preview of Partial Prerendering — a compiler optimization for dynamic content with a fast initial static response — that we're working on for Next.js.
Partial Prerendering builds on a decade of research and development into server-side rendering (SSR), static-site generation (SSG), and incremental static revalidation (ISR).
Motivation
We've heard your feedback. There's currently too many runtimes, configuration options, and rendering methods to have to consider. You want the speed and reliability of static, while also supporting fully dynamic, personalized responses.
Having great performance globally and personalization shouldn't come at the cost of complexity.
Our challenge was to create a better developer experience, simplifying the existing model without introducing new APIs for developers to learn. While partial caching of server-side content has existed, these approaches still need to meet the developer experience and composability goals we aim for.
Partial Prerendering requires no new APIs to learn.
Built on React Suspense
Partial Prerendering is defined by your Suspense boundaries. Here's how it works. Consider the following ecommerce page:
export default function Page() {
return (
<main>
<header>
<h1>My Store</h1>
<Suspense fallback={<CartSkeleton />}>
<ShoppingCart />
</Suspense>
</header>
<Banner />
<Suspense fallback={<ProductListSkeleton />}>
<Recommendations />
</Suspense>
<NewProducts />
</main>
);
}
With Partial Prerendering enabled, this page generates a static shell based on your <Suspense />
boundaries. The fallback
from React Suspense is prerendered.
Suspense fallbacks in the shell are then replaced with dynamic components, like reading cookies to determine the cart, or showing a banner based on the user.
When a request is made, the static HTML shell is immediately served:
<main>
<header>
<h1>My Store</h1>
<div class="cart-skeleton">
<!-- Hole -->
</div>
</header>
<div class="banner" />
<div class="product-list-skeleton">
<!-- Hole -->
</div>
<section class="new-products" />
</main>
Since <ShoppingCart />
reads from cookies
to look at the user session, this component is then streamed in as part of the same HTTP request as the static shell. There are no extra network roundtrips needed.
import { cookies } from 'next/headers'
export default function ShoppingCart() {
const cookieStore = cookies()
const session = cookieStore.get('session')
return ...
}
To have the most granular static shell, this may require adding additional Suspense boundaries. However, if you're already using loading.js
today, this is an implicit Suspense boundary, so no changes would be required to generate the static shell.
Coming soon
Partial prerendering is under active development. We'll be sharing more updates in an upcoming minor release.
Metadata Improvements
Before your page content can be streamed from the server, there's important metadata about the viewport, color scheme, and theme that need to be sent to the browser first.
Ensuring these meta
tags are sent with the initial page content helps a smooth user experience, preventing the page from flickering by changing the theme color, or shifting layout due to viewport changes.
In Next.js 14, we've decoupled blocking and non-blocking metadata. Only a small subset of metadata options are blocking, and we want to ensure non-blocking metadata will not prevent a partially prerendered page from serving the static shell.
The following metadata options are now deprecated and will be removed from metadata
in a future major version:
viewport
: Sets the initial zoom and other properties of the viewportcolorScheme
: Sets the support modes (light/dark) for the viewportthemeColor
: Sets the color the chrome around the viewport should render with
Starting with Next.js 14, there are new options viewport
and generateViewport
to replace these options. All other metadata
options remain the same.
You can start adopting these new APIs today. The existing metadata
options will continue to work.
Next.js Learn Course
Today we're releasing a brand new, free course on Next.js Learn. This course teaches:
- The Next.js App Router
- Styling and Tailwind CSS
- Optimizing Fonts and Images
- Creating Layouts and Pages
- Navigating Between Pages
- Setting Up Your Postgres Database
- Fetching Data with Server Components
- Static and Dynamic Rendering
- Streaming
- Partial Prerendering (Optional)
- Adding Search and Pagination
- Mutating Data
- Handling Errors
- Improving Accessibility
- Adding Authentication
- Adding Metadata
Next.js Learn has taught millions of developers about the foundations of the framework, and we can't wait to hear your feedback on our new addition. Head to nextjs.org/learn to take the course.
Other Changes
- [Breaking] Minimum Node.js version is now
18.17
- [Breaking] Removes WASM target for
next-swc
build (PR) - [Breaking] Dropped support for
@next/font
in favor ofnext/font
(Codemod) - [Breaking] Changed
ImageResponse
import fromnext/server
tonext/og
(Codemod) - [Breaking]
next export
command has been removed in favor ofoutput: 'export'
config (Docs) - [Deprecation]
onLoadingComplete
fornext/image
is deprecated in favor ofonLoad
- [Deprecation]
domains
fornext/image
is deprecated in favor ofremotePatterns
- [Feature] More verbose logging around
fetch
caching can be enabled (Docs) - [Improvement] 80% smaller function size for a basic
create-next-app
application - [Improvement] Enhanced memory management when using
edge
runtime in development
Contributors
Next.js is the result of the combined work of over 2,900 individual developers, industry partners like Google and Meta, and our core team at Vercel. Join the community on GitHub Discussions, Reddit, and Discord.
This release was brought to you by:
- The Next.js team: Andrew, Balazs, Jiachi, Jimmy, JJ, Josh, Sebastian, Shu, Steven, Tim, Wyatt, and Zack.
- The Turbopack team: Donny, Justin, Leah, Maia, OJ, Tobias, and Will.
- Next.js Learn: Delba, Steph, Emil, Balazs, Hector, and Amy.
And the contributions of: @05lazy, @0xadada, @2-NOW, @aarnadlr, @aaronbrown-vercel, @aaronjy, @abayomi185, @abe1272001, @abhiyandhakal, @abstractvector, @acdlite, @adamjmcgrath, @AdamKatzDev, @adamrhunter, @ademilter, @adictonator, @adilansari, @adtc, @afonsojramos, @agadzik, @agrattan0820, @akd-io, @AkifumiSato, @akshaynox, @alainkaiser, @alantoa, @albertothedev, @AldeonMoriak, @aleksa-codes, @alexanderbluhm, @alexkirsz, @alfred-mountfield, @alpha-xek, @andarist, @Andarist, @andrii-bodnar, @andykenward, @angel1254mc, @anonrig, @anthonyshew, @AntoineBourin, @anujssstw, @apeltop, @aralroca, @aretrace, @artdevgame, @artechventure, @arturbien, @Aryan9592, @AviAvinav, @aziyatali, @BaffinLee, @Banbarashik, @bencmbrook, @benjie, @bennettdams, @bertho-zero, @bigyanse, @Bitbbot, @blue-devil1134, @bot08, @bottxiang, @Bowens20832, @bre30kra69cs, @BrennanColberg, @brkalow, @BrodaNoel, @Brooooooklyn, @brunoeduardodev, @brvnonascimento, @carlos-menezes, @cassidoo, @cattmote, @cesarkohl, @chanceaclark, @charkour, @charlesbdudley, @chibicode, @chrisipanaque, @ChristianIvicevic, @chriswdmr, @chunsch, @ciruz, @cjmling, @clive-h-townsend, @colinhacks, @colinking, @coreyleelarson, @Cow258, @cprussin, @craigwheeler, @cramforce, @cravend, @cristobaldominguez95, @ctjlewis, @cvolant, @cxa, @danger-ahead, @daniel-web-developer, @danmindru, @dante-robinson, @darshanjain-entrepreneur, @darshkpatel, @davecarlson, @David0z, @davidnx, @dciug, @delbaoliveira, @denchance, @DerTimonius, @devagrawal09, @DevEsteves, @devjiwonchoi, @devknoll, @DevLab2425, @devvspaces, @didemkkaslan, @dijonmusters, @dirheimerb, @djreillo, @dlehmhus, @doinki, @dpnolte, @Drblessing, @dtinth, @ducanhgh, @DuCanhGH, @ductnn, @duncanogle, @dunklesToast, @DustinsCode, @dvakatsiienko, @dvoytenko, @dylanjha, @ecklf, @EndangeredMassa, @eps1lon, @ericfennis, @escwxyz, @Ethan-Arrowood, @ethanmick, @ethomson, @fantaasm, @feikerwu, @ferdingler, @FernandVEYRIER, @feugy, @fgiuliani, @fomichroman, @Fonger, @ForsakenHarmony, @franktronics, @FSaldanha, @fsansalvadore, @furkanmavili, @g12i, @gabschne, @gaojude, @gdborton, @gergelyke, @gfgabrielfranca, @gidgudgod, @Gladowar, @Gnadhi, @gnoff, @goguda, @greatSumini, @gruz0, @Guilleo03, @gustavostz, @hanneslund, @HarshaVardhanReddyDuvvuru, @haschikeks, @Heidar-An, @heyitsuzair, @hiddenest, @hiro0218, @hotters, @hsrvms, @hu0p, @hughlilly, @HurSungYun, @hustLer2k, @iamarpitpatidar, @ianldgs, @ianmacartney, @iaurg, @ibash, @ibrahemid, @idoob, @iiegor, @ikryvorotenko, @imranbarbhuiya, @ingovals, @inokawa, @insik-han, @isaackatayev, @ishaqibrahimbot, @ismaelrumzan, @itsmingjie, @ivanhofer, @IvanKiral, @jacobsfletch, @jakemstar, @jamespearson, @JanCizmar, @janicklas-ralph, @jankaifer, @JanKaifer, @jantimon, @jaredpalmer, @javivelasco, @jayair, @jaykch, @Jeffrey-Zutt, @jenewland1999, @jeremydouglas, @JesseKoldewijn, @jessewarren-aa, @jimcresswell, @jiwooIncludeJeong, @jocarrd, @joefreeman, @JohnAdib, @JohnAlbin, @JohnDaly, @johnnyomair, @johnta0, @joliss, @jomeswang, @joostdecock, @Josehower, @josephcsoti, @josh, @joshuabaker, @JoshuaKGoldberg, @joshuaslate, @joulev, @jsteele-stripe, @JTaylor0196, @JuanM04, @jueungrace, @juliusmarminge, @Juneezee, @Just-Moh-it, @juzhiyuan, @jyunhanlin, @kaguya3222, @karlhorky, @kevinmitch14, @keyz, @kijikunnn, @kikobeats, @Kikobeats, @kleintorres, @koba04, @koenpunt, @koltong, @konomae, @kosai106, @krmeda, @kvnang, @kwonoj, @ky1ejs, @kylemcd, @labyrinthitis, @lachlanjc, @lacymorrow, @laityned, @Lantianyou, @leerob, @leodr, @leoortizz, @li-jia-nan, @loettz, @lorenzobloedow, @lubakravche, @lucasassisrosa, @lucasconstantino, @lucgagan, @LukeSchlangen, @LuudJanssen, @lycuid, @M3kH, @m7yue, @manovotny, @maranomynet, @marcus-rise, @MarDi66, @MarkAtOmniux, @martin-wahlberg, @masnormen, @matepapp, @matthew-heath, @mattpr, @maxleiter, @MaxLeiter, @maxproske, @meenie, @meesvandongen, @mhmdrioaf, @michaeloliverx, @mike-plummer, @MiLk, @milovangudelj, @Mingyu-Song, @mirismaili, @mkcy3, @mknichel, @mltsy, @mmaaaaz, @mnajdova, @moetazaneta, @mohanraj-r, @molebox, @morganfeeney, @motopods, @mPaella, @mrkldshv, @mrxbox98, @nabsul, @nathanhammond, @nbouvrette, @nekochantaiwan, @nfinished, @Nick-Mazuk, @nickmccurdy, @niedziolkamichal, @niko20, @nikolovlazar, @nivak-monarch, @nk980113, @nnnnoel, @nocell, @notrab, @nroland013, @nuta, @nutlope, @obusk, @okcoker, @oliviertassinari, @omarhoumz, @opnay, @orionmiz, @ossan-engineer, @patrick91, @pauek, @peraltafederico, @Phiction, @pn-code, @pyjun01, @pythagoras-yamamoto, @qrohlf, @raisedadead, @reconbot, @reshmi-sriram, @reyrodrigez, @ricardofiorani, @rightones, @riqwan, @rishabhpoddar, @rjsdnql123, @rodrigofeijao, @runjuu, @Ryan-Dia, @ryo-manba, @s0h311, @sagarpreet-xflowpay, @sairajchouhan, @samdenty, @samsisle, @sanjaiyan-dev, @saseungmin, @SCG82, @schehata, @Schniz, @sepiropht, @serkanbektas, @sferadev, @ShaunFerris, @shivanshubisht, @shozibabbas, @silvioprog, @simonswiss, @simPod, @sivtu, @SleeplessOne1917, @smaeda-ks, @sonam-serchan, @SonMooSans, @soonoo, @sophiebits, @souporserious, @sp00ls, @sqve, @sreetamdas, @stafyniaksacha, @starunaway, @steebchen, @stefanprobst, @steppefox, @steven-tey, @suhaotian, @sukkaw, @SukkaW, @superbahbi, @SuttonJack, @svarunid, @swaminator, @swarnava, @syedtaqi95, @taep96, @taylorbryant, @teobler, @Terro216, @theevilhead, @thepatrick00, @therealrinku, @thomasballinger, @thorwebdev, @tibi1220, @tim-hanssen, @timeyoutakeit, @tka5, @tknickman, @tomryanx, @trigaten, @tristndev, @tunamagur0, @tvthatsme, @tyhopp, @tyler-lutz, @UnknownMonk, @v1k1, @valentincostam, @valentinh, @valentinpolitov, @vamcs, @vasucp1207, @vicsantizo, @vinaykulk621, @vincenthongzy, @visshaljagtap, @vladikoff, @wherehows, @WhoAmIRUS, @WilderDev, @Willem-Jaap, @williamli, @wiredacorn, @wiscaksono, @wojtekolek, @ws-jm, @wxh06, @wyattfry, @wyattjoh, @xiaolou86, @y-tsubuku, @yagogmaisp, @yangshun, @yasath, @Yash-Singh1, @yigithanyucedag, @ykzts, @Yovach, @yutsuten, @yyuemii, @zek, @zekicaneksi, @zignis, and @zlrlyy
```

---

## 27. How to Think About Security in Next.js

- 日期: 2023-10-23 14:00
- 链接: https://nextjs.org/blog/security-nextjs-server-components-actions

```
Monday, October 23rd 2023
How to Think About Security in Next.js
Posted byReact Server Components (RSC) in App Router is a novel paradigm that eliminates much of the redundancy and potential risks linked with conventional methods. Given the newness, developers and subsequently security teams may find it challenging to align their existing security protocols with this model.
This document is meant to highlight a few areas to look out for, what protections are built-in, and include a guide for auditing applications. We focus especially on the risks of accidental data exposure.
Choosing Your Data Handling Model
React Server Components blur the line between server and client. Data handling is paramount in understanding where information is processed and subsequently made available.
The first thing we need to do is pick what data handling approach is appropriate for our project.
- HTTP APIs (recommended for existing large projects / orgs)
- Data Access Layer (recommended for new projects)
- Component Level Data Access (recommended for prototyping and learning)
We recommend that you stick to one approach and don't mix and match too much. This makes it clear for both developers working in your code base and security auditors for what to expect. Exceptions pop out as suspicious.
HTTP APIs
If you're adopting Server Components in an existing project, the recommended approach is to handle Server Components at runtime as unsafe/untrusted by default like SSR or within the client. So there is no assumption of an internal network or zones of trust and engineers can apply the concept of Zero Trust. Instead, you only call custom API endpoints such as REST or GraphQL using fetch()
from Server Components just like if it was executing on the client. Passing along any cookies.
If you had existing getStaticProps
/getServerSideProps
connecting to a database, you might want to consolidate the model and move these to API end points as well so you have one way to do things.
Look out for any access control that assumes fetches from the internal network are safe.
This approach lets you keep existing organizational structures where existing backend teams, specialized in security can apply existing security practices. If those teams use languages other than JavaScript, that works well in this approach.
It still takes advantage of many of the benefits of Server Components by sending less code to the client and inherent data waterfalls can execute with low latency.
Data Access Layer
Our recommended approach for new projects is to create a separate Data Access Layer inside your JavaScript codebase and consolidate all data access in there. This approach ensures consistent data access and reducing the chance of authorization bugs occurring. It's also easier to maintain given you're consolidating into a single library. Possibly providing better team cohesion with a single programming language. You also get to take advantage of better performance with lower runtime overhead, the ability to share an in-memory cache across different parts of a request.
You build an internal JavaScript library that provides custom data access checks before giving it to the caller. Similar to HTTP endpoints but in the same memory model. Every API should accept the current user and check if the user can see this data before returning it. The principle is that a Server Component function body should only see data that the current user issuing the request is authorized to have access to.
From this point, normal security practices for implementing APIs take over.
import { cache } from 'react';
import { cookies } from 'next/headers';
// Cached helper methods makes it easy to get the same value in many places
// without manually passing it around. This discourages passing it from Server
// Component to Server Component which minimizes risk of passing it to a Client
// Component.
export const getCurrentUser = cache(async () => {
const token = cookies().get('AUTH_TOKEN');
const decodedToken = await decryptAndValidate(token);
// Don't include secret tokens or private information as public fields.
// Use classes to avoid accidentally passing the whole object to the client.
return new User(decodedToken.id);
});
import 'server-only';
import { getCurrentUser } from './auth';
function canSeeUsername(viewer: User) {
// Public info for now, but can change
return true;
}
function canSeePhoneNumber(viewer: User, team: string) {
// Privacy rules
return viewer.isAdmin || team === viewer.team;
}
export async function getProfileDTO(slug: string) {
// Don't pass values, read back cached values, also solves context and easier to make it lazy
// use a database API that supports safe templating of queries
const [rows] = await sql`SELECT * FROM user WHERE slug = ${slug}`;
const userData = rows[0];
const currentUser = await getCurrentUser();
// only return the data relevant for this query and not everything
// <https://www.w3.org/2001/tag/doc/APIMinimization>
return {
username: canSeeUsername(currentUser) ? userData.username : null,
phonenumber: canSeePhoneNumber(currentUser, userData.team)
? userData.phonenumber
: null,
};
}
These methods should expose objects that are safe to be transferred to the client as is. We like to call these Data Transfer Objects (DTO) to clarify that they're ready to be consumed by the client.
They might only get consumed by Server Components in practice. This creates a layering where security audits can focus primarily on the Data Access Layer while the UI can rapidly iterate. Smaller surface area and less code to cover makes it easier to catch security issues.
import {getProfile} from '../../data/user'
export async function Page({ params: { slug } }) {
// This page can now safely pass around this profile knowing
// that it shouldn't contain anything sensitive.
const profile = await getProfile(slug);
...
}
Secret keys can be stored in environment variables but only the data access layer should access process.env
in this approach.
Component Level Data Access
Another approach is to just put your database queries directly in your Server Components. This approach is only appropriate for rapid iteration and prototyping. E.g. for a small product with a small team where everyone is aware of the risks and how to watch for them.
In this approach you'll want to audit your "use client"
files carefully. While auditing and reviewing PRs, look at all the exported functions and if the type signature accepts overly broad objects like User
, or contains props like token
or creditCard
. Even privacy sensitive fields like phoneNumber
need extra scrutiny. A Client Component should not accept more data than the minimal data it needs to perform its job.
import Profile from './components/profile.tsx';
export async function Page({ params: { slug } }) {
const [rows] = await sql`SELECT * FROM user WHERE slug = ${slug}`;
const userData = rows[0];
// EXPOSED: This exposes all the fields in userData to the client because
// we are passing the data from the Server Component to the Client.
// This is similar to returning `userData` in `getServerSideProps`
return <Profile user={userData} />;
}
'use client';
// BAD: This is a bad props interface because it accepts way more data than the
// Client Component needs and it encourages server components to pass all that
// data down. A better solution would be to accept a limited object with just
// the fields necessary for rendering the profile.
export default async function Profile({ user }: { user: User }) {
return (
<div>
<h1>{user.name}</h1>
...
</div>
);
}
Always use parameterized queries, or a db library that does it for you, to avoid SQL injection attacks.
Server Only
Code that should only ever execute on the server can be marked with:
import 'server-only';
This will cause the build to error if a Client Component tries to import this module. This can be used to ensure that proprietary/sensitive code or internal business logic doesn't accidentally leak to the client.
The primary way to transfer data is using the React Server Components protocol which happens automatically when passing props to the Client Components. This serialization supports a superset of JSON. Transferring custom classes is not supported and will result in an error.
Therefore, a nice trick to avoid too large objects being accidentally exposed to the client is to use class
for your data access records.
In the upcoming Next.js 14 release, you can also try out the experimental React Taint APIs by enable the taint
flag in next.config.js
.
module.exports = {
experimental: {
taint: true,
},
};
This lets you mark an object that should not be allowed to be passed to the client as is.
import { experimental_taintObjectReference } from 'react';
export async function getUserData(id) {
const data = ...;
experimental_taintObjectReference(
'Do not pass user data to the client',
data
);
return data;
}
import { getUserData } from './data';
export async function Page({ searchParams }) {
const userData = getUserData(searchParams.id);
return <ClientComponent user={userData} />; // error
}
This does not protect against extracting data fields out of this object and passing them along:
export async function Page({ searchParams }) {
const { name, phone } = getUserData(searchParams.id);
// Intentionally exposing personal data
return <ClientComponent name={name} phoneNumber={phone} />;
}
For unique strings such as tokens, the raw value can be blocked as well using taintUniqueValue
.
import { experimental_taintObjectReference, experimental_taintUniqueValue } from 'react';
export async function getUserData(id) {
const data = ...;
experimental_taintObjectReference(
'Do not pass user data to the client',
data
);
experimental_taintUniqueValue(
'Do not pass tokens to the client',
data,
data.token
);
return data;
}
However, even this doesn't block derived values.
It's better to avoid data getting into the Server Components in the first place - using a Data Access Layer. Taint checking provides an additional layer of protection against mistakes by specifying the value, please be mindful that functions and classes are already blocked from being passed to Client Components. More layers the minimize risk of something slipping through.
By default, environment variables are only available on the Server. By convention, Next.js also exposes any environment variable prefixed with NEXT_PUBLIC_
to the client. This lets you expose certain explicit configuration that should be available to the client.
SSR vs RSC
For initial load Next.js will run both the Server Components and the Client Components on the server to produce HTML.
Server Components (RSC) execute in a separate module system from the Client Components to avoid accidentally exposing information between the two modules.
Client Components that render through Server-side Rendering (SSR) should be considered as the same security policy as the browser client. It should not gain access to any privileged data or private APIs. It's highly discouraged to use hacks to try to circumvent this protection (such as stashing data on the global object). The principle is that this code should be able to execute the same on the server as the client. In alignment with secure by default practices, Next.js will fail the build if server-only
modules are imported from a Client Component.
Read
In Next.js App Router, reading data from a database or API is implemented by rendering Server Component pages.
The input to pages are searchParams in the URL, dynamic params mapped from the URL and headers. These can be abused to be different values by the Client. They should not be trusted and needs to be re-verified each time they are read. E.g. a searchParam should not be used to track things like ?isAdmin=true
. Just because the user is on /[team]/
doesn't mean that they have access to that team, that needs to be verified when reading data. The principle is to always re-read access control and cookies()
whenever reading data. Don't pass it as props or params.
Rendering a Server Component should never perform side-effects like mutations. This is not unique to Server Components. React naturally discourages side-effects even when rendering Client Components (outside useEffect), by doing things like double-rendering.
Additionally, in Next.js there's no way to set cookies or trigger revalidation of caches during rendering. This also discourages the use of renders for mutations.
E.g. searchParams
should not be used to perform side-effects like saving changes or logging out. Server Actions should be used for this instead.
This means that the Next.js model never uses GET requests for side-effects when used as intended. This helps avoid a large source of CSRF issues.
Next.js does have support for Custom Route Handlers (route.tsx
), which can set cookies on GET. It's considered an escape hatch and not part of the general model. These have to explicitly opt-in to accepting GET requests. There's no catch-all handler that might accidentally receive GET requests. If you do decide to create a custom GET handler, these might need extra auditing.
Write
The idiomatic way to perform writes or mutations in Next.js App Router is using Server Actions.
'use server';
export function logout() {
cookies().delete('AUTH_TOKEN');
}
The "use server"
annotation exposes an end point that makes all exported functions invokable by the client. The identifiers is currently a hash of the source code location. As long as a user gets the handle to the id of an action, it can invoke it with any arguments.
As a result, those functions should always start by validating that the current user is allowed to invoke this action. Functions should also validate the integrity of each argument. This can be done manually or with a tool like zod
.
"use server";
export async function deletePost(id: number) {
if (typeof id !== 'number') {
// The TypeScript annotations are not enforced so
// we might need to check that the id is what we
// think it is.
throw new Error();
}
const user = await getCurrentUser();
if (!canDeletePost(user, id)) {
throw new Error();
}
...
}
Closures
Server Actions can also be encoded in closures. This lets the action be associated with a snapshot of data used at the time of rendering so that you can use this when the action is invoked:
export default function Page() {
const publishVersion = await getLatestVersion();
async function publish() {
"use server";
if (publishVersion !== await getLatestVersion()) {
throw new Error('The version has changed since pressing publish');
}
...
}
return <button action={publish}>Publish</button>;
}
The snapshot of the closure must be sent to the client and back when the server is invoked.
In Next.js 14, the closed over variables are encrypted with the action ID before sent to the client. By default a private key is generated automatically during the build of a Next.js project. Each rebuild generates a new private key which means that each Server Action can only be invoked for a specific build. You might want to use Skew Protection to ensure that you always invoke the correction version during redeploys.
If you need a key that rotates more frequently or is persistent across multiple builds, you can configure it manually using NEXT_SERVER_ACTIONS_ENCRYPTION_KEY
environment variable.
By encrypting all closed over variables, you don't accidentally expose any secrets in them. By signing it, it makes it harder for an attacker to mess with the input to the action.
Another alternative to using closures is to use the .bind(...)
function in JavaScript. These are NOT encrypted. This provides an opt-out for performance and is also consistent with .bind()
on the client.
async function deletePost(id: number) {
"use server";
// verify id and that you can still delete it
...
}
export async function Page({ slug }) {
const post = await getPost(slug);
return <button action={deletePost.bind(null, post.id)}>
Delete
</button>;
}
The principle is that the argument list to Server Actions ("use server"
) must always be treated as hostile and the input has to be verified.
CSRF
All Server Actions can be invoked by plain <form>
, which could open them up to CSRF attacks. Behind the scenes, Server Actions are always implemented using POST and only this HTTP method is allowed to invoke them. This alone prevents most CSRF vulnerabilities in modern browsers, particularly due to Same-Site cookies being the default.
As an additional protection Server Actions in Next.js 14 also compares the Origin
header to the Host
header (or X-Forwarded-Host
). If they don't match, the Action will be rejected. In other words, Server Actions can only be invoked on the same host as the page that hosts it. Very old unsupported and outdated browsers that don't support the Origin
header could be at risk.
Server Actions doesn't use CSRF tokens, therefore HTML sanitization is crucial.
When Custom Route Handlers (route.tsx
) are used instead, extra auditing can be necessary since CSRF protection has to be done manually there. The traditional rules apply there.
Error Handling
Bugs happen. When errors are thrown on the Server they are eventually rethrown in Client code to be handled in the UI. The error messages and stack traces might end up containing sensitive information. E.g. [credit card number] is not a valid phone number
.
In production mode, React doesn't emit errors or rejected promises to the client. Instead a hash is sent representing the error. This hash can be used to associate multiple of the same errors together and associate the error with server logs. React replaces the error message with its own generic one.
In development mode, server errors are still sent in plain text to the client to help with debugging.
It's important to always run in Next.js in production mode for production workloads. Development mode does not optimize for security and performance.
Custom Routes and Middleware
Custom Route Handlers and Middleware are considered low level escape hatches for features that cannot be implemented using any other built-in functionality. This also opens up potential footguns that the framework otherwise protects against. With great power comes great responsibility.
As mentioned above, route.tsx
routes can implement custom GET and POST handlers which may suffer from CSRF issues if not done correctly.
Middleware can be used to limit access to certain pages. Usually it's best to do this with an allow list rather than a deny list. That's because it can be tricky to know all the different ways there is to get access to data, such as if there's a rewrite or client request.
For example, it's common to only think about the HTML page. Next.js also supports client navigation that can load RSC/JSON payloads. In Pages Router, this used to be in a custom URL.
To make writing matchers easier Next.js App Router always uses the page's plain URL for both initial HTML, client navigations and Server Actions. Client navigations use ?_rsc=...
search param as a cache breaker.
Server Actions live on the page they're used on and as such inherit the same access control. If Middleware allows reading a page, you can also invoke actions on that page. To limit access to Server Actions on a page, you can ban the POST HTTP method on that page.
Audit
If you're doing an audit of a Next.js App Router project here are a few things we recommend looking extra at:
- Data Access Layer. Is there an established practice for an isolated Data Access Layer? Verify that database packages and environment variables are not imported outside the Data Access Layer.
"use client"
files. Are the Component props expecting private data? Are the type signatures overly broad?"use server"
files. Are the Action arguments validated in the action or inside the Data Access Layer? Is the user re-authorized inside the action?/[param]/
. Folders with brackets are user input. Are params validated?middleware.tsx
androute.tsx
have a lot of power. Spend extra time auditing these using traditional techniques. Perform Penetration Testing or Vulnerability Scanning regularly or in alignment with your team's software development lifecycle.
```

---

## 28. Next.js 13.5

- 日期: 2023-09-19 18:00
- 链接: https://nextjs.org/blog/next-13-5

```
Tuesday, September 19th 2023
Next.js 13.5
Posted byNext.js 13.5 improves local dev performance and reliability with:
- 22% faster local server startup: Iterate faster with the App & Pages Router
- 29% faster HMR (Fast Refresh): For faster iterations when saving changes
- 40% less memory usage: Measured when running
next start
- Optimized Package Imports: Faster updates when using popular icon and component libraries
next/image
Improvements:<picture>
, art direction, and dark mode support- And over 438 bugs patched!
Upgrade today and register for Next.js Conf on Oct 26:
npm i next@latest react@latest react-dom@latest eslint-config-next@latest
Improving startup and Fast Refresh time
We're excited to see the continued adoption of the App Router, now growing 80% MoM when looking at the top 10 million origins crawled by the HTTP Archive.
Since Next.js 13.4, our focus has been on improving performance and reliability for App Router applications. Comparing 13.4 to 13.5, we've seen the following improvements on a new application:
- 22% faster local server startup
- 29% faster HMR (Fast Refresh)
- 40% less memory usage
We were able to achieve this performance increase through optimizations like:
- Doing less work by caching or minimizing slow operations
- Optimizing expensive file system operations
- Better incremental tree traversal during compilation
- Moving unnecessary blocking synchronous calls to be lazy
- Automatically configuring large icon libraries
Next.js user Lattice reported between 87-92% faster compilation in their testing.
While we continue to iterate and improve our current bundler performance, we're also working on Turbopack (Beta) in parallel to further increase performance. With 13.5, next dev --turbo
now supports more features.
Optimized Package Imports
We've made an exciting breakthrough to optimize package imports, improving both local dev performance and production cold starts, when using large icon or component libraries or other dependencies that re-export hundreds or thousands of modules.
Previously, we added support for modularizeImports
, enabling you to configure how imports should resolve when using these libraries. In 13.5, we have superseeded this option with optimizePackageImports
, which doesn't require you to specify the mapping of imports, but instead will automatically optimize imports for you.
Libraries like @mui/icons-material
, @mui/material
, date-fns
, lodash
, lodash-es
, ramda
, react-bootstrap
, @headlessui/react
,@heroicons/react
, and lucide-react
are now automatically optimized, only loading the modules you are actually using, while still giving you the convenience of writing import
statements with many named exports.
View the PR or learn more about optimizePackageImports
in our documentation.
next/image
Improvements
Based on community feedback, we've added a new experimental function unstable_getImgProps()
to support advanced use cases without using the <Image>
component directly, including:
- Working with
background-image
orimage-set
- Working with canvas
context.drawImage()
ornew Image()
- Working with
<picture>
media queries to implement Art Direction or Light/Dark Mode images
import { unstable_getImgProps as getImgProps } from 'next/image';
export default function Page() {
const common = { alt: 'Hero', width: 800, height: 400 };
const {
props: { srcSet: dark },
} = getImgProps({ ...common, src: '/dark.png' });
const {
props: { srcSet: light, ...rest },
} = getImgProps({ ...common, src: '/light.png' });
return (
<picture>
<source media="(prefers-color-scheme: dark)" srcSet={dark} />
<source media="(prefers-color-scheme: light)" srcSet={light} />
<img {...rest} />
</picture>
);
}
Additionally, the placeholder
prop now supports providing arbitrary data:image/
for placeholder images that shouldn't be blurred (demo).
Learn more about next/image
in our documentation.
Other Improvements
Since 13.4.0
, we've fixed over 438 bugs and made various improvements including:
- [Docs] New documentation on Forms and Mutations
- [Docs] New documentation on Server and Client Components
- [Docs] New documentation on Content Security Policy and Nonces
- [Docs] New documentation on Caching and Revalidating
- [Feature]
useParams
anduseSearchParams
fromnext/navigation
now work in the Pages Router for incremental adoption - [Feature] Support for
scroll: false
onrouter.push
/router.replace
- [Feature] Support for
scroll={false}
onnext/link
- [Feature] HTTPS support for development:
next dev --experimental-https
- [Feature] Added support for
cookies().has()
(Docs) - [Feature] Added support for IPv6 hostnames
- [Feature] Added support for Yarn PnP with the App Router
- [Feature] Added support for
redirect()
in Server Actions - [Feature] Added support for using Bun with creating projects:
bunx create-next-app
(Docs) - [Feature] Draft Mode support for use inside Middleware and the Edge Runtime
- [Feature]
cookies()
andheaders()
are now supported inside Middleware - [Feature] Metadata API now supports
summary_large_image
in Twitter cards - [Feature]
RedirectType
is now exported fromnext/navigation
- [Feature] Added experimental test mode for Playwright (Docs)
- [Improvement] Refactored
next start
to handle 1062% more requests/second - [Improvement] Optimized Next.js internals to improve cold starts (up to 40% faster, tested on Vercel)
- [Improvement] Better Jest support for the App Router (PR)
- [Improvement] Redesigned
next dev
output (PR) - [Improvement] Server Actions now work with fully static routes (including revalidating data with ISR)
- [Improvement] Server Actions no longer block navigation between routes
- [Improvement] Server Actions can no longer trigger multiple concurrent actions
- [Improvement] Server Actions calling
redirect()
now push into the history stack instead of replacing the current entry to ensure the back button works - [Improvement] Server Actions add
no-cache, no-store
cache-control
header to prevent browser caching - [Improvement] Fixed a bug where Server Actions could be called twice after navigating
- [Improvement] Improved support for Emotion CSS with Server Components
- [Improvement] Support for
scroll-behavior: smooth
for hash url changes - [Improvement] Added polyfill for
Array.prototype.at
in all browsers - [Improvement] Fixed race condition in
next dev
cache when handling multiple parallel requests - [Improvement]
fetch
output in console now shows requests that skipped cache withcache: SKIP
- [Improvement]
usePathname
now properly stripsbasePath
- [Improvement]
next/image
now properly preloads images in App Router - [Improvement]
not-found
no longer renders the root layout twice - [Improvement]
NextRequest
can now be cloned (i.enew NextRequest(request)
) - [Improvement]
app/children/page.tsx
now properly works for literal/children
routes - [Improvement] Content Security Policy now supports
nonce
for preinitialized scripts - [Improvement] Using
redirect
fromnext/navigation
now supportsbasePath
- [Improvement] Fixed
process.env
not being available during rendering inoutput: 'standalone'
mode - [Improvement] Improved error message when using a Static Export with unsupported features
- [Improvement] Improved recursive readdir implementation (~3x faster)
- [Improvement] Fixed
fallback: false
with dynamic route segments previously causing hanging requests - [Improvement] Fixed error where
signal
was passed to revalidate requests, causing them to fail when the request was already aborted - [Improvement] Removed
fetch
polling on 404 page in favor of websocket events, preventing unnecessary reloads when runningnext dev
- [Improvement]
performance.measure
no longer can cause a hydration mismatch - [Improvement] Fixed cases where an unexpected full reload could happen editing
pages/_app
- [Improvement]
ImageResponse
now extendsResponse
for improved type checking (PR) - [Improvement]
pages
is no longer shown when there is nopages
output innext build
- [Improvement] Fixed
skipTrailingSlashRedirect
being ignored in<Link>
- [Improvement] Fixed duplicated dynamic metadata routes in dev mode
Contributors
Next.js is the result of the combined work of over 2,800 individual developers, industry partners like Google and Meta, and our core team at Vercel. Join the community on GitHub Discussions, Reddit, and Discord.
This release was brought to you by:
- The Next.js team: Andrew, Balazs, Jiachi, Jimmy, JJ, Josh, Sebastian, Shu, Steven, Tim, Wyatt, and Zack.
- The Turbopack team: Donny, Justin, Leah, Maia, OJ, Tobias, and Will.
And the contributions of: @opnay, @vinaykulk621, @goguda, @coreyleelarson, @bencmbrook, @cramforce, @williamli, @stefanprobst, @feugy, @Kikobeats, @dvoytenko, @MaxLeiter, @devjiwonchoi, @lacymorrow, @kylemcd, @tibi1220, @iamarpitpatidar, @pythagoras-yamamoto, @alexkirsz, @jsteele-stripe, @tknickman, @gaojude, @janicklas-ralph, @ericfennis, @JohnAdib, @MiLk, @delbaoliveira, @leerob, @LuudJanssen, @lucasconstantino, @davecarlson, @colinhacks, @jantimon, @Banbarashik, @ForsakenHarmony, @arturbien, @gnoff, @hsrvms, @DuCanhGH, @tim-hanssen, @Aryan9592, @rishabhpoddar, @Lantianyou, @joulev, @AkifumiSato, @trigaten, @HurSungYun, @DevLab2425, @SukkaW, @daniel-web-developer, @ky1ejs, @wyattjoh, @ShaunFerris, @syedtaqi95, @Heidar-An, @Jeffrey-Zutt, @Ryan-Dia, @steppefox, @hiro0218, @rjsdnql123, @fgiuliani, @steven-tey, @AntoineBourin, @adamrhunter, @darshanjain-entrepreneur, @s0h311, @djreillo, @dijonmusters, @cassidoo, @anonrig, @gfgabrielfranca, @Bitbbot, @BrennanColberg, @Nick-Mazuk, @thomasballinger, @lucgagan, @nroland013, @SonMooSans, @jenewland1999, @thorwebdev, @jyunhanlin, @Gnadhi, @yagogmaisp, @carlos-menezes, @ryo-manba, @vamcs, @matepapp, @SleeplessOne1917, @ecklf, @karlhorky, @starunaway, @FernandVEYRIER, @Terro216, @anthonyshew, @suhaotian, @simonswiss, @feikerwu, @lubakravche, @masnormen, @bottxiang, @mhmdrioaf, @tyler-lutz, @vincenthongzy, @yigithanyucedag, @doinki, @danger-ahead, @bre30kra69cs, @Yash-Singh1, @krmeda, @bigyanse, @2-NOW, @Mingyu-Song, @morganfeeney, @aralroca, @nickmccurdy, @adamjmcgrath, @angel1254mc, @cxa, @ibash, @mohanraj-r, @kevinmitch14, @iaurg, @steebchen, @Cow258, @charlesbdudley, @tyhopp, @Drblessing, @milovangudelj, @jacobsfletch, @JoshuaKGoldberg, @zignis, @ChristianIvicevic, @mrxbox98, @oliviertassinari, @fsansalvadore, @tvthatsme, @dvakatsiienko, @brunoeduardodev, @sonam-serchan, @vicsantizo, @leodr, @wiscaksono, @hustLer2k, @joshuabaker, @shozibabbas, @omarhoumz, @jamespearson, @tristndev, @AldeonMoriak, @manovotny, @mirismaili, @SuttonJack, @jeremydouglas, @JanCizmar, @mltsy, @WilderDev, @Guilleo03, @Willem-Jaap, @escwxyz, @wiredacorn, @Ethan-Arrowood, @BaffinLee, @greatSumini, @ciruz, @kijikunnn, @DustinsCode, @riqwan, @joostdecock, @nikolovlazar, @Bowens20832, @JohnAlbin, @gidgudgod, @maxproske, @dunklesToast, @yyuemii, @mPaella, @mknichel, @niko20, @mkcy3, @valentinpolitov, @smaeda-ks, @keyz, @Schniz, @koba04, @jiwooIncludeJeong, @ethanmick, @didemkkaslan, @itsmingjie, @v1k1, @thepatrick00, @taylorbryant, @kvnang, @alainkaiser, @simPod, @svarunid, @pauek, @lycuid, @MarkAtOmniux, @darshkpatel, @johnta0, @devagrawal09, @ibrahemid, @JesseKoldewijn, @javivelasco, @05lazy, @alexanderbluhm, @Fonger, @souporserious, @DevEsteves, @sanjaiyan-dev, @g12i, @cesarkohl, @josh, @li-jia-nan, @gabschne, @akd-io, @runjuu, @jocarrd, @nnnnoel, @ferdingler, and @ikryvorotenko
```

---

## 29. Next.js App Router Update

- 日期: 2023-06-22 14:00
- 链接: https://nextjs.org/blog/june-2023-update

```
Thursday, June 22nd 2023
Next.js App Router Update
Posted byThe App Router represents a new foundation for the future of Next.js, but we recognize there are opportunities to make the experience better. We'd like to give an update on what our current priorities are.
For the upcoming releases of Next.js, we are focusing on the following areas:
- Improving Performance
- Improving Stability
- Improving Developer Education
The App Router
First, it's helpful to provide some context on how the App Router has been designed.
Growing Beyond the Pages Router by Aligning with React
As we saw increased adoption and larger scale applications being built with Next.js, we received feedback from the community and identified areas where we started to reach the limits of the Pages Router.
Most notably, the Next.js Pages Router was not designed for streaming, a cornerstone primitive in modern React, that helps us address the limitations we were facing and realize our long-term vision for Next.js.
Making streaming-friendly framework APIs for data fetching, asset loading, and page metadata, as well as taking advantage of React's newer primitives required large changes to the core architecture of Next.js.
We took the opportunity to build on top of the latest React concurrent features, like Server Components, Suspense, and more, which have been designed for streaming architectures.
Incremental Adoption is Non-Negotiable
We didn't want our community to have to rebuild their entire applications from the ground up to update to the latest version of Next.js. We believe incremental adoption is the best strategy for evolving applications over time.
- Per-route incremental migration: Without a major rewrite of your application, you can move a single route of your application over the App Router and start to take advantage of new features at your own pace. See our incremental adoption guide or watch a tutorial.
- Easily rollback: If you are not satisifed with the performance or developer experience of the App Router, you can easily rollback to the Pages Router for that specific route.
We are exploring further opportunities to make incremental adoption even easier.
Road to Stability
We began building the Next.js App Router over a year ago and have been steadily releasing new features and improvements since then.
- Initial Announcement: In May of that year, we released an RFC to outline our plans for making routing and layouts more flexible.
- Early Beta: In Next.js 13, we released the first version of the App Router, allowing the community to try it out and provide early feedback.
- Stable API: Responding to feedback, we focused our efforts on finalizing the core API. In 13.4, we marked the core API of the App Router as stable and ready for wider adoption.
Our Current Focus
Marking stability signaled to the community that the core API was settled and would not go through major breaking changes that would require rewrites.
Since then, we've received lots of valuable feedback and increased adoption has inevitably revealed bugs and opportunities for further improvement.
We want you to know that we are not yet satisfied with the experience of using the App Router and it is our top priority moving forward. So, let's talk about the work we're doing to make this experience better.
Improving Performance
Over the coming months, we're focused on three aspects of performance: local iteration speed, production build times, and serverless performance.
Local development performance
As Next.js has matured, and the size of applications built with it have grown, we've slowly and incrementally been replacing pieces of its underlying architecture with faster, more scalable tools.
-
Migration Progress: We started with replacing Babel (compilation) and Terser (minification) with SWC. This has helped improve local iteration speeds and production build times.
-
Long-term Investment: Keeping great Fast Refresh performance regardless of an applications size means making Next.js operate as incremental as possible during local development, by only bundling and compiling code as needed.
This is why we're currently working on replacing webpack (bundling) with Turbopack, which is built on a low-level incremental computation engine that enables caching down to the level of individual functions.
Next.js applications that move to Turbopack will see sustained improvements in Fast Refresh speed even as they grow in size.
In the past few months, the Turbo team has been focused on improving Turbopack performance and support for all Next.js features and App Router APIs.
Turbopack is currently available in beta (
next dev --turbo
). -
Improving Today's Architecture: In addition to investing in the future, we are continuing to make performance improvements to our existing webpack architecture.
For certain Next.js applications, especially those refreshing thousands of modules, we have seen reports of flakiness with local development and Fast Refresh. We're working to improve performance and reliability here. For example, we recently added in pre-configured settings (
modularizeImports
) to handle large icon libraries that might accidentally force thousands of modules to reload on every request.
Build-time performance
We are also working on production builds with Turbopack (next build --turbo
) and have started to land the first pieces of this work. Expect more updates on this in the coming releases.
Production performance
Finally, on Vercel, we're working to optimize the performance and memory usage of Vercel Functions defined through Next.js application code, ensuring minimal cold starts while retaining the benefits of a scalable serverless architecture. This work has resulted in new tracing capabilities (experimental) in Next.js and early explorations into server-side developer tools.
Improving Stability
The Pages Router has been around for six years now. The release of the App Router meant the introduction of new APIs which are still young, with just six months of usage. We've come a long way in a short amount of time, but there are still opportunities to improve as we learn more from our community and how they're using it.
We appreciate the community's willingness to eagerly adopt the App Router and provide feedback. There's been a number of bug reports we're investigating and we're thankful for the minimal reproductions you have created to help isolate issues and verify fixes.
Since 13.4, we've already patched a number of high impact bugs around stability that are available in the latest patch release (13.4.7
). We will be continuing to focus on performance and stability with high intensity.
Improving Developer Education
While we believe the new features of the App Router and modern React are powerful, they also require additional education and documentation to help teach these new concepts.
Next.js features
We've been working over the past year to re-write the Next.js documentation from scratch. This work is now live on nextjs.org/docs. We'd like to highlight some important pieces:
- Pages and App toggles: You can switch between learning the Pages Router or App Router documentation using the button on the left side of the documentation. Further, you can filter search results based on your router choice.
- Improved content and information architecture: Almost every single page of the App Router documentation has been refreshed, including more clear structure and cohesiveness between pages, and hundreds of new illustrations to visually explain how Next.js works.
- More to come: We have more work to do here. The Developer Experience team at Vercel is working hard to provide additional learning resources (including an updated course on
/learn
teaching the App Router) and real world codebase examples (including a rewrite of Next.js Commerce).
We'll be releasing new content in the documentation, on Twitter, YouTube, and more.
New React features
We've also heard your feedback about the education around new React features that are available in the Next.js App Router.
-
Server Components: It's important to note that features like Server Components and conventions like the
"use client"
directive are not Next.js specific, but a larger part of the React ecosystem.Our team, our partners at Meta, and other independent contributors are working to provide more education around these topics. It's early days for these concepts, but we're confident in the React ecosystem and continued education.
-
Client Components: With the recent conversation around Server Components, it's important to note the client components are not a de-optimization. The client is a valid part of the React model and is not going away.
You can think of client components as the existing Next.js ecosystem today, where your favorite libraries and tools continue to work. For example, a common question we've seen is whether
"use client"
needs to be added to every single file to make it a client component. This is not necessary, but we understand these concepts are new and will take time to learn. You only need to mark the top level boundary where you code moves between the server to the client. This architecture allows you to interweave server and client components together. -
Growing third-party ecosystem: In addition to education, the ecosystem around React's newer features is still growing. For example, Panda CSS, a CSS-in-JS library from the makers of Chakra UI, just announced support for React Server Components.
-
Server Actions (Alpha): Server Actions enable server-side data mutations, reduced client-side JavaScript, and progressively enhanced forms. We do not recommend using Server Actions in production yet. We appreciate early feedback from alpha testers helping us shape the future of this feature.
Thank you
We're thankful many of you have chosen to learn and build with Next.js.
Our focus on performance, stability, and developer experience will be reflected in the upcoming releases of Next.js. We want using Next.js to be delightful—and to make you (and your team) more productive.
As always, we greatly appreciate your feedback. If you are experiencing any issues with Next.js, please open an issue, or start a new discussion, and we will investigate.
```

---

## 30. Next.js 13.4

- 日期: 2023-05-04 18:00
- 链接: https://nextjs.org/blog/next-13-4

```
Thursday, May 4th 2023
Next.js 13.4
Posted byNext.js 13.4 is a foundational release, marking stability for the App Router:
- App Router (Stable):
- React Server Components
- Nested Routes & Layouts
- Simplified Data Fetching
- Streaming & Suspense
- Built-in SEO Support
- Turbopack (Beta): Your local dev server, faster and with improved stability
- Server Actions (Alpha): Mutate data on the server with zero client JavaScript
Since the release of Next.js 13 six months ago, we've been focused on building the foundations for the future of Next.js—App Router—in a way that can be incrementally adopted without unnecessary breaking changes.
Today, with the release of 13.4, you can now start adopting the App Router for production.
npm i next@latest react@latest react-dom@latest eslint-config-next@latest
Next.js App Router
We released Next.js in 2016 to provide an easy way to server-render React applications, with our goal to create a more dynamic, personalized, and global web.
In the original announcement post, we shared some design principles of Next.js:
- Zero setup. Use the filesystem as an API
- Only JavaScript. Everything is a function
- Automatic server rendering and code splitting
- Data fetching is up to the developer
Next.js is now six years old. Our original design principles have remained—and as Next.js has been adopted by more developers and companies, we have been working on a foundational upgrade to the framework to better achieve these principles.
We've been working on the next generation of Next.js, and today with 13.4
, this next generation is stable and ready for adoption. This post will share more about our design decisions and choices for the App Router.
Zero setup. Use the filesystem as an API
File-system based routing has been a core feature of Next.js. In our original post, we showed this example of creating a route from a single React component:
// Pages Router
import React from 'react';
export default () => <h1>About us</h1>;
There was nothing additional to configure. Drop a file inside pages/
and the Next.js router would take care of the rest. We still love this simplicity with routing. But as usage of the framework grew, so have the types of interfaces developers are looking to build with it.
Developers have asked for improved support for defining layouts, nesting pieces of UI as layouts, and having more flexibility over defining loading and error states. This wasn't an easy thing to retrofit into the existing Next.js router.
Every part of the framework has to be designed around the router. Page transitions, data fetching, caching, mutating and revalidating data, streaming, styling content, and more.
To make our router compatible with streaming, and to solve these requests for enhanced support for layouts, we set out to build a new version of our router.
This is where we landed after our initial release of our Layouts RFC.
// New: App Router ✨
export default function RootLayout({ children }) {
return (
<html lang="en">
<body>{children}</body>
</html>
);
}
export default function Page() {
return <h1>Hello, Next.js!</h1>;
}
What's more important than what you see here is what you don't see. This new router (which can be incrementally adopted through the app/
directory) has an entirely different architecture, built on the foundation of React Server Components and Suspense.
This foundation has allowed us to remove Next.js specific APIs that were initially developed to extend the React primitives. For example, you no longer have to use a custom _app
file to customize the global shared layout:
// Pages Router
// This "global layout" wraps all routes. There's no way to
// compose other layout components, and you cannot fetch global
// data from this file.
export default function MyApp({ Component, pageProps }) {
return <Component {...pageProps} />;
}
With the Pages Router, layouts were not able to be composed, and data fetching could not be colocated with the component. With the new App Router, this is now supported.
// New: App Router ✨
// The root layout is shared for the entire application
export default function RootLayout({ children }) {
return (
<html lang="en">
<body>{children}</body>
</html>
);
}
// Layouts can be nested and composed
export default function DashboardLayout({ children }) {
return (
<section>
<h1>Dashboard</h1>
{children}
</section>
);
}
With the Pages Router, _document
was used to customize the initial payload from the server.
// Pages Router
// This file allows you to customize the <html> and <body> tags
// for the server request, but adds framework-specific features
// rather than writing HTML elements.
import { Html, Head, Main, NextScript } from 'next/document';
export default function Document() {
return (
<Html>
<Head />
<body>
<Main />
<NextScript />
</body>
</Html>
);
}
With the App Router, you no longer need to import <Html>
, <Head>
, and <Body>
from Next.js. Instead, you just use React.
// New: App Router ✨
// The root layout is shared for the entire application
export default function RootLayout({ children }) {
return (
<html lang="en">
<body>{children}</body>
</html>
);
}
The opportunity to build a new file-system router was also the right time to address many other related feature requests with our routing system. For example:
- Previously, you could only import global stylesheets from external npm packages (like component libraries) in
_app.js
. This was a less-than-ideal developer experience. With the App Router, you can import (and colocate) any CSS file in any component. - Previously, opt-ing into server-side rendering with Next.js (through
getServerSideProps
) meant that interacting with your application was blocked until the entire page was hydrated. With the App Router, we've refactored the architecture to be deeply integrated with React Suspense, meaning we can selectively hydrate parts of the page, without blocking other components in the UI from being interactive. Content can be instantly streamed from the server, improving the perceived loading performance of a page.
The router is the core of what makes Next.js work. But it's not about the router itself, but how it integrates the rest of the pieces of the framework—like data fetching.
Only JavaScript. Everything is a function
Next.js and React developers want to write JavaScript and TypeScript code and compose application components together. From our original post:
import React from 'react';
import Head from 'next/head';
export default () => (
<div>
<Head>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</Head>
<h1>Hi. I'm mobile-ready!</h1>
</div>
);
In future versions of Next.js, we added a DX improvement to automatically import React for you.
This component encapsulates logic that can be reused and composed anywhere in your application. Paired with file-system routing, this meant an easy way to get started building React applications that felt like writing JavaScript and HTML.
For example, if you wanted to fetch some data, the original version of Next.js looked like this:
import React from 'react';
import 'isomorphic-fetch';
export default class extends React.Component {
static async getInitialProps() {
const res = await fetch('https://api.company.com/user/123');
const data = await res.json();
return { username: data.profile.username };
}
}
In future versions of Next.js, we added a DX improvement that polyfilled fetch so you didn't need to import
isomorphic-fetch
ornode-fetch
, and could use the Webfetch API
on both the client and server.
As adoption grew and the framework matured, we explored new patterns for data fetching.
getInitialProps
ran both the server and client. This API extended the React component, allowing you to make a Promise
and forward the results to the component's props
.
While getInitialProps
does still work today, we then iterated forward on the next generation of data fetching APIs based on customer feedback: getServerSideProps
and getStaticProps
.
// Generate a static version of the route
export async function getStaticProps(context) {
return { props: {} };
}
// Or dynamically server-render the route
export async function getServerSideProps(context) {
return { props: {} };
}
These APIs made it more clear where your code was running, either the client or server, and allowed Next.js applications to be automatically statically optimized. Further, it allowed for static exports, enabling Next.js to be deployed to places that don't support a server (e.g. AWS S3 bucket).
However, this was not "just JavaScript", and we wanted to adhere closer to our original design principle.
Since Next.js was created, we've worked closely with the React core team at Meta to build framework features on top of React primitives. Our partnership, in combination with the years of research and development from the React core team, has led to an opportunity for Next.js to achieve our goals through the latest version of the React architecture, including Server Components.
With the App Router, you fetch data using the familiar async
and await
syntax. There are no new APIs to learn. By default, all components are React Server Components, so data fetching happens securely on the server. For example:
export default async function Page() {
const res = await fetch('https://api.example.com/...');
// The return value is *not* serialized
// You can use Date, Map, Set, etc.
const data = res.json();
return '...';
}
Critically, the "data fetching is up to the developer" principle is realized. You can fetch data and compose any component. And not just first-party components, but any component in the Server Components ecosystem, like a Twitter embed react-tweet
, which has been designed to integrate with Server Components and run entirely on the server.
import { Tweet } from 'react-tweet';
export default async function Page() {
return <Tweet id="790942692909916160" />;
}
Since the router is integrated with React Suspense, you can more fluidly display fallback content while parts of your content are loading, and progressively reveal content as desired.
import { Suspense } from 'react';
import { PostFeed, Weather } from './components';
export default function Page() {
return (
<section>
<Suspense fallback={<p>Loading feed...</p>}>
<PostFeed />
</Suspense>
<Suspense fallback={<p>Loading weather...</p>}>
<Weather />
</Suspense>
</section>
);
}
Further, the router marks page navigations as transitions, enabling route transitions to be interruptible.
Automatic server rendering and code splitting
When we created Next.js, it was still common for developers to manually configure webpack, babel, and other tooling to get a React application running. Adding further optimizations like server rendering or code splitting was often not implemented in custom solutions. Next.js, as well as other React frameworks, created an abstraction layer to implement and force these best practices.
Route-based code splitting meant that each file in your pages/
directory would be code split into its own JavaScript bundle, helping reduce the file system and improve initial page load performance.
This was beneficial for both server-rendered applications as well as single-page applications with Next.js, as the latter often loaded a single large JavaScript bundle on application startup. However, to implement component-level code splitting, developers needed to use next/dynamic
to dynamically import components.
import dynamic from 'next/dynamic';
const DynamicHeader = dynamic(() => import('../components/header'), {
loading: () => <p>Loading...</p>,
});
export default function Home() {
return <DynamicHeader />;
}
With the App Router, Server Components are not included in the JavaScript bundle for the browser. Client components are automatically code split by default (either with webpack or Turbopack in Next.js). Further, since the entire router architecture is streaming and Suspense enabled, you can progressively send parts of your UI from the server to the client.
For example, you can code split entire code paths with conditional logic. In this example, you would not need to load the dashboard's client-side JavaScript for logged-out users.
import { getUser } from './auth';
import { Dashboard, Landing } from './components';
export default async function Layout() {
const isLoggedIn = await getUser();
return isLoggedIn ? <Dashboard /> : <Landing />;
}
Turbopack (Beta)
Turbopack, our new bundler we're testing and stabilizing through Next.js, helps speed up local iterations while working on your Next.js application (through next dev --turbo
) and soon your production builds (next build --turbo
).
Since the alpha release in Next.js 13, we've seen a steady growth in adoption as we've worked to patch bugs and add support for missing features. We've been dogfooding Turbopack on Vercel.com and with many Vercel customers operating large Next.js websites to gather feedback and improve stability. We are grateful for the community's support in testing and reporting bugs to our team.
Now six months later, we're ready to move forward into the beta phase.
Turbopack does not yet have full feature parity with webpack and Next.js. We are tracking support for those features in this issue. However, the majority of use cases should now be supported. Our goal with this beta is to continue addressing remaining bugs from increased adoption and prepare for stability in a future version.
Our investment into improving the incremental engine and caching layer of Turbopack will not only speed up local development, but also production builds soon. Stay tuned for a future Next.js version where you'll be able to run next build --turbo
for instant builds.
Try out the Turbopack beta today in Next.js 13.4 with next dev --turbo
.
Server Actions (Alpha)
The React ecosystem has seen a lot of innovation and exploration of ideas around forms, managing form state, and caching and revalidating of data. Over time, React has become more opinionated about some of these patterns. For example, recommended "uncontrolled components" for form state.
The current ecosystem of solutions has either been reusable client-side solutions or primitives built into frameworks. Until now, there hasn't been a way to compose server mutations and data primitives. The React team has been working on a first-party solution for mutations.
We're excited to announce support for experimental Server Actions in Next.js, enabling you to mutate data on the server, calling functions directly without needing to create an in-between API layer.
import kv from './kv';
export default function Page({ params }) {
async function increment() {
'use server';
await kv.incr(`post:id:${params.id}`);
}
return (
<form action={increment}>
<button type="submit">Like</button>
</form>
);
}
With Server Actions, you have powerful server-first data mutations, less client-side JavaScript, and progressively enhanced forms.
import db from './db';
import { redirect } from 'next/navigation';
async function create(formData: FormData) {
'use server';
const post = await db.post.insert({
title: formData.get('title'),
content: formData.get('content'),
});
redirect(`/blog/${post.slug}`);
}
export default function Page() {
return (
<form action={create}>
<input type="text" name="title" />
<textarea name="content" />
<button type="submit">Submit</button>
</form>
);
}
Server Actions in Next.js have been designed for deep integration with the rest of the data lifecycle, including the Next.js Cache, Incremental Static Regeneration (ISR), and the client router.
Revalidating data through new APIs revalidatePath
and revalidateTag
mean that mutating, re-rendering the page, or redirecting can happen in one network roundtrip, ensuring the correct data is displayed on the client, even if the upstream provider is slow.
import db from './db';
import { revalidateTag } from 'next/cache';
async function update(formData: FormData) {
'use server';
await db.post.update({
title: formData.get('title'),
});
revalidateTag('posts');
}
export default async function Page() {
const res = await fetch('https://...', { next: { tags: ['posts'] } });
const data = await res.json();
// ...
}
Server Actions are designed to be composable. Anyone in the React community can build and publish Server Actions and distribute them in the ecosystem. Just like Server Components, we're excited about the new era of composable primitives for both the client and the server.
Server Actions are available today in alpha with Next.js 13.4. By opting into using Server Actions, Next.js will use the experimental release channel of React.
/** @type {import('next').NextConfig} */
const nextConfig = {
experimental: {
serverActions: true,
},
};
module.exports = nextConfig;
Other Improvements
- Draft Mode: Fetch and render draft content from your headless CMS. Draft mode works in both
pages
andapp
. We've enhanced and simplified the existing Preview Mode API, which continues to work forpages
. Preview Mode does not work inapp
—you should use Draft Mode.
Frequently Asked Questions
What does App Router stability mean?
Marking the App Router as stable today does not mean our work is done. Stability means that the core of the App Router is ready for production and has been validated by both our own internal testing, as well as many Next.js early adopters.
There are still additional optimizations we'd like to make in the future, including Server Actions reaching full stability. It was important for us to push towards core stability to help provide clarity for the community on where they should begin learning and building applications today.
The App Router is built on top of the React canary
channel, which is now ready for framework adoption of features like Server Components. Learn more.
What does this mean for the Next.js beta docs?
Starting today, we recommend building new applications with the App Router. The Next.js beta documentation, which has been used to explain the App Router and re-written from the ground up, is now merged back into the stable Next.js documentation. You can now easily toggle between the App or Pages Router.
We recommend reading the App Router Incremental Adoption Guide to learn how to adopt the App Router.
Is the Pages Router going away?
No. We are committed to supporting pages/
development, including bug fixes, improvements, and security patches, for multiple major versions moving forward. We want to ensure developers have enough time to incrementally adopt the App Router as they're ready.
Using both pages/
and app/
in production together is supported and encouraged. The App Router can be adopted on a per-route basis.
Does this mean Server Components are "complete"?
Next.js is one framework that is choosing the build on the React architecture, which includes Server Components. We hope that the experience provided with the App Router will encourage other frameworks (or new frameworks) to consider using this architecture, as well.
There are still patterns yet to be defined in this ecosystem, like handling infinite scroll. For now, we recommend using client solutions for these patterns while the ecosystem grows and libraries are created or updated.
Community
Next.js is the result of the combined work of over 2,600 individual developers, industry partners like Google and Meta, and our core team at Vercel. Join the community on GitHub Discussions, Reddit, and Discord.
This release was brought to you by:
- The Next.js team: Andrew, Balazs, Jan, Jiachi, Jimmy, JJ, Josh, Sebastian, Shu, Steven, Tim, and Wyatt.
- The Turbopack team: Alex, Donny, Justin, Leah, Maia, OJ, Tobias, and Will.
And the contributions of: @shuding, @huozhi, @wyattfry, @styfle, @sreetamdas, @afonsojramos, @timneutkens, @alexkirsz, @chriswdmr, @jankaifer, @pn-code, @kdy1, @sokra, @kwonoj, @martin-wahlberg, @Kikobeats, @JTaylor0196, @sebmarkbage, @ijjk, @gnoff, @jridgewell, @sagarpreet-xflowpay, @balazsorban44, @cprussin, @ForsakenHarmony, @li-jia-nan, @dciug, @albertothedev, @DuCanhGH, @feedthejim, @patrick91, @padmaia, @sophiebits, @eps1lon, @reconbot, @acdlite, @cjmling, @nabsul, @motopods, @hanneslund, @tunamagur0, @devknoll, @apeltop, @maranomynet, @y-tsubuku, @EndangeredMassa, @ykzts, @AviAvinav, @adilansari, @wyattjoh, @charkour, @delbaoliveira, @agadzik, @Just-Moh-it, @rodrigofeijao, @leerob, @juliusmarminge, @koba04, @Phiction, @jessewarren-aa, @ryo-manba, @Yovach, and @dylanjha.
```

---
