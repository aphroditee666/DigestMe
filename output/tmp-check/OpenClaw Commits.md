# OpenClaw Commits

> 分类: AI专题
> URL: https://github.com/openclaw/openclaw/commits/main.atom
> 抓取: 20 篇

---

## 1. test: tighten runtime plan assertions

- 链接: https://github.com/openclaw/openclaw/commit/5d43e8336aaf13883e4d812c37bdb2c0c91982af

```
@@ -44,6 +44,44 @@ const gpt54Model = {
44
44
maxTokens : 8_192 ,
45
45
} as const ;
46
46
47
+ function expectExtraParams (
48
+ extraParams : Record < string , unknown > | undefined ,
49
+ expected : {
50
+ parallelToolCalls : boolean ;
51
+ textVerbosity : string ;
52
+ } ,
53
+ ) : void {
54
+ expect ( extraParams ?. parallel_tool_calls ) . toBe ( expected . parallelToolCalls ) ;
55
+ expect ( extraParams ?. text_verbosity ) . toBe ( expected . textVerbosity ) ;
56
+ }
57
+
58
+ function latestFollowupRouteCall ( ) : {
59
+ provider ?: unknown ;
60
+ runtimeHandle ?: Record < string , unknown > ;
61
+ context ?: Record < string , unknown > ;
62
+ } {
63
+ const call = vi . mocked ( resolveProviderFollowupFallbackRoute ) . mock . calls . at ( - 1 ) ?. [ 0 ] ;
64
+ if ( ! call || typeof call !== "object" ) {
65
+ throw new Error ( "expected follow-up route call" ) ;
66
+ }
67
+ const record = call as {
68
+ provider ?: unknown ;
69
+ runtimeHandle ?: unknown ;
70
+ context ?: unknown ;
71
+ } ;
72
+ return {
73
+ provider : record . provider ,
74
+ runtimeHandle :
75
+ record . runtimeHandle && typeof record . runtimeHandle === "object"
76
+ ? ( record . runtimeHandle as Record < string , unknown > )
77
+ : undefined ,
78
+ context :
79
+ record . context && typeof record . context === "object"
80
+ ? ( record . context as Record < string , unknown > )
81
+ : undefined ,
82
+ } ;
83
+ }
84
+
47
85
describe ( "AgentRuntimePlan" , ( ) => {
48
86
afterEach ( ( ) => {
49
87
resetConfigRuntimeState ( ) ;
@@ -65,9 +103,9 @@ describe("AgentRuntimePlan", () => {
65
103
} ) ;
66
104
67
105
expect ( prepareProviderExtraParamsMock ) . not . toHaveBeenCalled ( ) ;
68
- expect ( plan . transport . extraParams ) . toMatchObject ( {
69
- parallel_tool_calls : true ,
70
- text_verbosity : "low" ,
106
+ expectExtraParams ( plan . transport . extraParams , {
107
+ parallelToolCalls : true ,
108
+ textVerbosity : "low" ,
71
109
} ) ;
72
110
expect ( prepareProviderExtraParamsMock ) . toHaveBeenCalledTimes ( 1 ) ;
73
111
void plan . transport . extraParams ;
@@ -91,31 +129,28 @@ describe("AgentRuntimePlan", () => {
91
129
} ,
92
130
} ) ;
93
131
94
- expect ( plan . auth ) . toMatchObject ( {
95
- providerForAuth : "openai" ,
96
- authProfileProviderForAuth : "openai-codex" ,
97
- harnessAuthProvider : "openai-codex" ,
98
- forwardedAuthProfileId : "openai-codex:work" ,
99
- } ) ;
132
+ expect ( plan . auth . providerForAuth ) . toBe ( "openai" ) ;
133
+ expect ( plan . auth . authProfileProviderForAuth ) . toBe ( "openai-codex" ) ;
134
+ expect ( plan . auth . harnessAuthProvider ) . toBe ( "openai-codex" ) ;
135
+ expect ( plan . auth . forwardedAuthProfileId ) . toBe ( "openai-codex:work" ) ;
100
136
expect ( plan . delivery . isSilentPayload ( { text : '{"action":"NO_REPLY"}' } ) ) . toBe ( true ) ;
101
137
expect (
102
138
plan . delivery . isSilentPayload ( {
103
139
text : '{"action":"NO_REPLY"}' ,
104
140
mediaUrl : "file:///tmp/image.png" ,
105
141
} ) ,
106
142
) . toBe ( false ) ;
107
- expect ( plan . transport . extraParams ) . toMatchObject ( {
108
- parallel_tool_calls : true ,
109
- text_verbosity : "low" ,
143
+ expectExtraParams ( plan . transport . extraParams , {
144
+ parallelToolCalls : true ,
145
+ textVerbosity : "low" ,
110
146
} ) ;
111
- expect (
112
- plan . transport . resolveExtraParams ( {
113
- extraParamsOverride : { parallel_tool_calls : false } ,
114
- resolvedTransport : "websocket" ,
115
- } ) ,
116
- ) . toMatchObject ( {
117
- parallel_tool_calls : false ,
118
- text_verbosity : "low" ,
147
+ const resolvedExtraParams = plan . transport . resolveExtraParams ( {
148
+ extraParamsOverride : { parallel_tool_calls : false } ,
149
+ resolvedTransport : "websocket" ,
150
+ } ) ;
151
+ expectExtraParams ( resolvedExtraParams , {
152
+ parallelToolCalls : false ,
153
+ textVerbosity : "low" ,
119
154
} ) ;
120
155
expect (
121
156
plan . prompt . resolveSystemPromptContribution ( {
@@ -169,11 +204,9 @@ describe("AgentRuntimePlan", () => {
169
204
workspaceDir : "/tmp/openclaw-runtime-plan" ,
170
205
} ) ;
171
206
172
- expect ( plan . auth ) . toMatchObject ( {
173
- providerForAuth : "openai" ,
174
- authProfileProviderForAuth : "openai" ,
175
- harnessAuthProvider : "openai-codex" ,
176
- } ) ;
207
+ expect ( plan . auth . providerForAuth ) . toBe ( "openai" ) ;
208
+ expect ( plan . auth . authProfileProviderForAuth ) . toBe ( "openai" ) ;
209
+ expect ( plan . auth . harnessAuthProvider ) . toBe ( "openai-codex" ) ;
177
210
expect ( plan . auth . forwardedAuthProfileId ) . toBeUndefined ( ) ;
178
211
} ) ;
179
212
@@ -190,11 +223,9 @@ describe("AgentRuntimePlan", () => {
190
223
workspaceDir : "/tmp/openclaw-runtime-plan" ,
191
224
} ) ;
192
225
193
- expect ( plan . auth ) . toMatchObject ( {
194
- providerForAuth : "openai" ,
195
- authProfileProviderForAuth : "openai-codex" ,
196
- forwardedAuthProfileId : "openai-codex:work" ,
197
- } ) ;
226
+ expect ( plan . auth . providerForAuth ) . toBe ( "openai" ) ;
227
+ expect ( plan . auth . authProfileProviderForAuth ) . toBe ( "openai-codex" ) ;
228
+ expect ( plan . auth . forwardedAuthProfileId ) . toBe ( "openai-codex:work" ) ;
198
229
} ) ;
199
230
200
231
it ( "resolves follow-up routes with the prepared provider handle" , ( ) => {
@@ -228,18 +259,13 @@ describe("AgentRuntimePlan", () => {
228
259
route : "dispatcher" ,
229
260
reason : "prepared-route" ,
230
261
} ) ;
231
- expect ( resolveProviderFollowupFallbackRouteMock ) . toHaveBeenCalledWith (
232
- expect . objectContaining ( {
233
- provider : "openai" ,
234
- runtimeHandle : providerRuntimeHandle ,
235
- context : expect . objectContaining ( {
236
- provider : "openai" ,
237
- modelId : "gpt-5.4" ,
238
- originRoutable : false ,
239
- dispatcherAvailable : true ,
240
- } ) ,
241
- } ) ,
242
- ) ;
262
+ const followupCall = latestFollowupRouteCall ( ) ;
263
+ expect ( followupCall . provider ) . toBe ( "openai" ) ;
264
+ expect ( followupCall . runtimeHandle ?. provider ) . toBe ( providerRuntimeHandle . provider ) ;
265
+ expect ( followupCall . context ?. provider ) . toBe ( "openai" ) ;
266
+ expect ( followupCall . context ?. modelId ) . toBe ( "gpt-5.4" ) ;
267
+ expect ( followupCall . context ?. originRoutable ) . toBe ( false ) ;
268
+ expect ( followupCall . context ?. dispatcherAvailable ) . toBe ( true ) ;
243
269
} ) ;
244
270
245
271
it ( "resolves incomplete supplied provider handles before invoking runtime hooks" , ( ) => {
@@ -288,11 +314,8 @@ describe("AgentRuntimePlan", () => {
288
314
bundledProviderAllowlistCompat : undefined ,
289
315
bundledProviderVitestCompat : undefined ,
290
316
} ) ;
291
- expect ( resolveProviderFollowupFallbackRouteMock ) . toHaveBeenCalledWith (
292
- expect . objectContaining ( {
293
- runtimeHandle : resolvedHandle ,
294
- } ) ,
295
- ) ;
317
+ const followupCall = latestFollowupRouteCall ( ) ;
318
+ expect ( followupCall . runtimeHandle ) . toBe ( resolvedHandle ) ;
296
319
} ) ;
297
320
298
321
it ( "resolves incomplete supplied delivery handles before follow-up routing" , ( ) => {
@@ -338,11 +361,8 @@ describe("AgentRuntimePlan", () => {
338
361
bundledProviderAllowlistCompat : undefined ,
339
362
bundledProviderVitestCompat : undefined ,
340
363
} ) ;
341
- expect ( resolveProviderFollowupFallbackRouteMock ) . toHaveBeenCalledWith (
342
- expect . objectContaining ( {
343
- runtimeHandle : resolvedHandle ,
344
- } ) ,
345
- ) ;
364
+ const followupCall = latestFollowupRouteCall ( ) ;
365
+ expect ( followupCall . runtimeHandle ) . toBe ( resolvedHandle ) ;
346
366
} ) ;
347
367
348
368
it ( "plans tool metadata against the runtime source snapshot lazily" , ( ) => {
0 commit comments
```

---

## 2. test: tighten pi auth json assertions

- 链接: https://github.com/openclaw/openclaw/commit/e2aac4fbc18da6257bd5d038336e297fd6e9fc9c

```
@@ -31,6 +31,37 @@ async function readAuthJson(agentDir: string) {
31
31
return JSON . parse ( await fs . readFile ( authPath , "utf8" ) ) as Record < string , unknown > ;
32
32
}
33
33
34
+ function requireAuthEntry (
35
+ auth : Record < string , unknown > ,
36
+ provider : string ,
37
+ ) : Record < string , unknown > {
38
+ const entry = auth [ provider ] ;
39
+ if ( ! entry || typeof entry !== "object" ) {
40
+ throw new Error ( `expected auth entry ${ provider } ` ) ;
41
+ }
42
+ return entry as Record < string , unknown > ;
43
+ }
44
+
45
+ function expectApiKeyAuth ( auth : Record < string , unknown > , provider : string , key : string ) : void {
46
+ const entry = requireAuthEntry ( auth , provider ) ;
47
+ expect ( entry . type ) . toBe ( "api_key" ) ;
48
+ expect ( entry . key ) . toBe ( key ) ;
49
+ }
50
+
51
+ function expectOAuthAuth (
52
+ auth : Record < string , unknown > ,
53
+ provider : string ,
54
+ access : string ,
55
+ refresh ?: string ,
56
+ ) : void {
57
+ const entry = requireAuthEntry ( auth , provider ) ;
58
+ expect ( entry . type ) . toBe ( "oauth" ) ;
59
+ expect ( entry . access ) . toBe ( access ) ;
60
+ if ( refresh !== undefined ) {
61
+ expect ( entry . refresh ) . toBe ( refresh ) ;
62
+ }
63
+ }
64
+
34
65
describe ( "ensurePiAuthJsonFromAuthProfiles" , ( ) => {
35
66
it ( "writes openai-codex oauth credentials into auth.json for pi-coding-agent discovery" , async ( ) => {
36
67
const agentDir = await createAgentDir ( ) ;
@@ -49,11 +80,7 @@ describe("ensurePiAuthJsonFromAuthProfiles", () => {
49
80
expect ( first . wrote ) . toBe ( true ) ;
50
81
51
82
const auth = await readAuthJson ( agentDir ) ;
52
- expect ( auth [ "openai-codex" ] ) . toMatchObject ( {
53
- type : "oauth" ,
54
- access : "access-token" ,
55
- refresh : "refresh-token" ,
56
- } ) ;
83
+ expectOAuthAuth ( auth , "openai-codex" , "access-token" , "refresh-token" ) ;
57
84
58
85
const second = await ensurePiAuthJsonFromAuthProfiles ( agentDir ) ;
59
86
expect ( second . wrote ) . toBe ( false ) ;
@@ -74,10 +101,7 @@ describe("ensurePiAuthJsonFromAuthProfiles", () => {
74
101
expect ( result . wrote ) . toBe ( true ) ;
75
102
76
103
const auth = await readAuthJson ( agentDir ) ;
77
- expect ( auth [ "openrouter" ] ) . toMatchObject ( {
78
- type : "api_key" ,
79
- key : "sk-or-v1-test-key" ,
80
- } ) ;
104
+ expectApiKeyAuth ( auth , "openrouter" , "sk-or-v1-test-key" ) ;
81
105
} ) ;
82
106
83
107
it ( "writes token credentials as api_key into auth.json" , async ( ) => {
@@ -95,10 +119,7 @@ describe("ensurePiAuthJsonFromAuthProfiles", () => {
95
119
expect ( result . wrote ) . toBe ( true ) ;
96
120
97
121
const auth = await readAuthJson ( agentDir ) ;
98
- expect ( auth [ "anthropic" ] ) . toMatchObject ( {
99
- type : "api_key" ,
100
- key : "sk-ant-test-token" ,
101
- } ) ;
122
+ expectApiKeyAuth ( auth , "anthropic" , "sk-ant-test-token" ) ;
102
123
} ) ;
103
124
104
125
it ( "syncs multiple providers at once" , async ( ) => {
@@ -129,9 +150,9 @@ describe("ensurePiAuthJsonFromAuthProfiles", () => {
129
150
130
151
const auth = await readAuthJson ( agentDir ) ;
131
152
132
- expect ( auth [ "openrouter" ] ) . toMatchObject ( { type : "api_key" , key : "sk-or-key" } ) ;
133
- expect ( auth [ "anthropic" ] ) . toMatchObject ( { type : "api_key" , key : "sk-ant-token" } ) ;
134
- expect ( auth [ "openai-codex" ] ) . toMatchObject ( { type : "oauth" , access : "access" } ) ;
153
+ expectApiKeyAuth ( auth , "openrouter" , "sk-or-key" ) ;
154
+ expectApiKeyAuth ( auth , "anthropic" , "sk-ant-token" ) ;
155
+ expectOAuthAuth ( auth , "openai-codex" , "access" ) ;
135
156
} ) ;
136
157
137
158
it ( "skips profiles with empty keys" , async ( ) => {
@@ -180,7 +201,7 @@ describe("ensurePiAuthJsonFromAuthProfiles", () => {
180
201
expect ( result . wrote ) . toBe ( true ) ;
181
202
182
203
const auth = await readAuthJson ( agentDir ) ;
183
- expect ( auth [ "zai" ] ) . toMatchObject ( { type : "api_key" , key : "sk-zai" } ) ;
204
+ expectApiKeyAuth ( auth , "zai" , "sk-zai" ) ;
184
205
expect ( auth [ "z.ai" ] ) . toBeUndefined ( ) ;
185
206
} ) ;
186
207
@@ -205,8 +226,8 @@ describe("ensurePiAuthJsonFromAuthProfiles", () => {
205
226
await ensurePiAuthJsonFromAuthProfiles ( agentDir ) ;
206
227
207
228
const auth = await readAuthJson ( agentDir ) ;
208
- expect ( auth [ "legacy-provider" ] ) . toMatchObject ( { type : "api_key" , key : "legacy-key" } ) ;
209
- expect ( auth [ "openrouter" ] ) . toMatchObject ( { type : "api_key" , key : "new-key" } ) ;
229
+ expectApiKeyAuth ( auth , "legacy-provider" , "legacy-key" ) ;
230
+ expectApiKeyAuth ( auth , "openrouter" , "new-key" ) ;
210
231
} ) ;
211
232
212
233
it ( "treats malformed existing provider entries as stale and replaces them" , async ( ) => {
@@ -228,6 +249,6 @@ describe("ensurePiAuthJsonFromAuthProfiles", () => {
228
249
expect ( result . wrote ) . toBe ( true ) ;
229
250
230
251
const auth = await readAuthJson ( agentDir ) ;
231
- expect ( auth [ "openrouter" ] ) . toMatchObject ( { type : "api_key" , key : "new-key" } ) ;
252
+ expectApiKeyAuth ( auth , "openrouter" , "new-key" ) ;
232
253
} ) ;
233
254
} ) ;
0 commit comments
```

---

## 3. test: tighten command delivery assertions

- 链接: https://github.com/openclaw/openclaw/commit/df8ccb00013468c983a0d2574f58b9535d91b47a

```
@@ -30,6 +30,13 @@ vi.mock("../../auto-reply/reply/reply-media-paths.runtime.js", () => ({
30
30
type NormalizeParams = Parameters < typeof normalizeAgentCommandReplyPayloads > [ 0 ] ;
31
31
type RunResult = NormalizeParams [ "result" ] ;
32
32
type DeliverParams = Parameters < typeof deliverAgentCommandResult > [ 0 ] ;
33
+ type TextPayloadLike = { text ?: unknown } ;
34
+ type MediaNormalizerOptions = {
35
+ sessionKey ?: unknown ;
36
+ agentId ?: unknown ;
37
+ workspaceDir ?: unknown ;
38
+ messageProvider ?: unknown ;
39
+ } ;
33
40
34
41
const slackOutboundForTest : ChannelOutboundAdapter = {
35
42
deliveryMode : "direct" ,
@@ -66,6 +73,38 @@ function createResult(overrides: Partial<RunResult> = {}): RunResult {
66
73
} as RunResult ;
67
74
}
68
75
76
+ function expectTextPayload ( payload : TextPayloadLike | undefined , text : string ) : void {
77
+ expect ( payload ?. text ) . toBe ( text ) ;
78
+ }
79
+
80
+ function requirePayload ( payloads : readonly ReplyPayload [ ] , index : number ) : ReplyPayload {
81
+ const payload = payloads . at ( index ) ;
82
+ if ( ! payload ) {
83
+ throw new Error ( `expected payload at index ${ index } ` ) ;
84
+ }
85
+ return payload ;
86
+ }
87
+
88
+ function latestNormalizerOptions ( ) : MediaNormalizerOptions {
89
+ const options = createReplyMediaPathNormalizerMock . mock . calls . at ( - 1 ) ?. [ 0 ] ;
90
+ if ( ! options || typeof options !== "object" ) {
91
+ throw new Error ( "expected media normalizer options" ) ;
92
+ }
93
+ return options as MediaNormalizerOptions ;
94
+ }
95
+
96
+ function latestOutboundDeliveryArgs ( ) : {
97
+ payloads : ReplyPayload [ ] ;
98
+ bestEffort ?: boolean ;
99
+ queuePolicy ?: string ;
100
+ } {
101
+ const args = deliverOutboundPayloadsMock . mock . calls . at ( - 1 ) ?. [ 0 ] ;
102
+ if ( ! args || typeof args !== "object" ) {
103
+ throw new Error ( "expected outbound delivery arguments" ) ;
104
+ }
105
+ return args as { payloads : ReplyPayload [ ] ; bestEffort ?: boolean ; queuePolicy ?: string } ;
106
+ }
107
+
69
108
async function deliverMediaReplyForTest ( outboundSession : DeliverParams [ "outboundSession" ] ) {
70
109
const runtime = { log : vi . fn ( ) , error : vi . fn ( ) } ;
71
110
return await deliverAgentCommandResult ( {
@@ -114,11 +153,8 @@ describe("normalizeAgentCommandReplyPayloads", () => {
114
153
result : createResult ( ) ,
115
154
} ) ;
116
155
117
- expect ( normalized ) . toMatchObject ( [
118
- {
119
- text : "Choose [[slack_buttons: Retry:retry]]" ,
120
- } ,
121
- ] ) ;
156
+ expect ( normalized ) . toHaveLength ( 1 ) ;
157
+ expectTextPayload ( normalized [ 0 ] , "Choose [[slack_buttons: Retry:retry]]" ) ;
122
158
} ) ;
123
159
124
160
it ( "renders response prefix templates with the selected runtime model" , ( ) => {
@@ -144,11 +180,8 @@ describe("normalizeAgentCommandReplyPayloads", () => {
144
180
} ) ,
145
181
} ) ;
146
182
147
- expect ( normalized ) . toMatchObject ( [
148
- {
149
- text : "[openai-codex/gpt-5.4] Ready." ,
150
- } ,
151
- ] ) ;
183
+ expect ( normalized ) . toHaveLength ( 1 ) ;
184
+ expectTextPayload ( normalized [ 0 ] , "[openai-codex/gpt-5.4] Ready." ) ;
152
185
} ) ;
153
186
154
187
it ( "keeps Slack options text intact for local preview when delivery is disabled" , async ( ) => {
@@ -178,7 +211,8 @@ describe("normalizeAgentCommandReplyPayloads", () => {
178
211
179
212
expect ( runtime . log ) . toHaveBeenCalledTimes ( 1 ) ;
180
213
expect ( runtime . log ) . toHaveBeenCalledWith ( "Options: on, off." ) ;
181
- expect ( delivered . payloads ) . toMatchObject ( [ { text : "Options: on, off." } ] ) ;
214
+ expect ( delivered . payloads ) . toHaveLength ( 1 ) ;
215
+ expectTextPayload ( delivered . payloads [ 0 ] , "Options: on, off." ) ;
182
216
} ) ;
183
217
184
218
it ( "normalizes reply-media paths before outbound delivery" , async ( ) => {
@@ -197,23 +231,19 @@ describe("normalizeAgentCommandReplyPayloads", () => {
197
231
agentId : "tester" ,
198
232
} as never ) ;
199
233
200
- expect ( createReplyMediaPathNormalizerMock ) . toHaveBeenCalledWith (
201
- expect . objectContaining ( {
202
- sessionKey : "agent:tester:slack:direct:alice" ,
203
- agentId : "tester" ,
204
- workspaceDir : "/tmp/agent-workspace" ,
205
- messageProvider : "slack" ,
206
- } ) ,
207
- ) ;
208
- expect ( normalizerFn ) . toHaveBeenCalledWith (
209
- expect . objectContaining ( { mediaUrls : [ "./out/photo.png" ] } ) ,
210
- ) ;
234
+ const normalizerOptions = latestNormalizerOptions ( ) ;
235
+ expect ( normalizerOptions . sessionKey ) . toBe ( "agent:tester:slack:direct:alice" ) ;
236
+ expect ( normalizerOptions . agentId ) . toBe ( "tester" ) ;
237
+ expect ( normalizerOptions . workspaceDir ) . toBe ( "/tmp/agent-workspace" ) ;
238
+ expect ( normalizerOptions . messageProvider ) . toBe ( "slack" ) ;
239
+
240
+ const normalizedInput = normalizerFn . mock . calls . at ( 0 ) ?. [ 0 ] ;
241
+ expect ( normalizedInput ?. mediaUrls ) . toStrictEqual ( [ "./out/photo.png" ] ) ;
211
242
expect ( deliverOutboundPayloadsMock ) . toHaveBeenCalledTimes ( 1 ) ;
212
- const [ firstCallArg ] = deliverOutboundPayloadsMock . mock . calls [ 0 ] ?? [ ] ;
213
- const deliverArgs = firstCallArg as { payloads : ReplyPayload [ ] } | undefined ;
214
- expect ( deliverArgs ?. payloads [ 0 ] ) . toMatchObject ( {
215
- mediaUrls : [ "/tmp/agent-workspace/out/photo.png" ] ,
216
- } ) ;
243
+ const deliverArgs = latestOutboundDeliveryArgs ( ) ;
244
+ expect ( requirePayload ( deliverArgs . payloads , 0 ) . mediaUrls ) . toStrictEqual ( [
245
+ "/tmp/agent-workspace/out/photo.png" ,
246
+ ] ) ;
217
247
} ) ;
218
248
219
249
it ( "reports successful requested delivery" , async ( ) => {
@@ -288,12 +318,9 @@ describe("normalizeAgentCommandReplyPayloads", () => {
288
318
289
319
expect ( delivered . deliverySucceeded ) . toBe ( false ) ;
290
320
expect ( runtime . error ) . toHaveBeenCalledWith ( expect . stringContaining ( "send failed" ) ) ;
291
- expect ( deliverOutboundPayloadsMock ) . toHaveBeenCalledWith (
292
- expect . objectContaining ( {
293
- bestEffort : true ,
294
- queuePolicy : "best_effort" ,
295
- } ) ,
296
- ) ;
321
+ const deliverArgs = latestOutboundDeliveryArgs ( ) ;
322
+ expect ( deliverArgs . bestEffort ) . toBe ( true ) ;
323
+ expect ( deliverArgs . queuePolicy ) . toBe ( "best_effort" ) ;
297
324
} ) ;
298
325
299
326
it ( "threads agentId into the normalizer when sessionKey is unresolved" , async ( ) => {
@@ -302,13 +329,10 @@ describe("normalizeAgentCommandReplyPayloads", () => {
302
329
303
330
await deliverMediaReplyForTest ( { agentId : "tester" } as never ) ;
304
331
305
- expect ( createReplyMediaPathNormalizerMock ) . toHaveBeenCalledWith (
306
- expect . objectContaining ( {
307
- agentId : "tester" ,
308
- sessionKey : undefined ,
309
- workspaceDir : "/tmp/agent-workspace" ,
310
- } ) ,
311
- ) ;
332
+ const normalizerOptions = latestNormalizerOptions ( ) ;
333
+ expect ( normalizerOptions . agentId ) . toBe ( "tester" ) ;
334
+ expect ( normalizerOptions . sessionKey ) . toBeUndefined ( ) ;
335
+ expect ( normalizerOptions . workspaceDir ) . toBe ( "/tmp/agent-workspace" ) ;
312
336
} ) ;
313
337
314
338
it ( "keeps LINE directive-only replies intact for local preview when delivery is disabled" , async ( ) => {
@@ -338,11 +362,11 @@ describe("normalizeAgentCommandReplyPayloads", () => {
338
362
expect ( runtime . log ) . toHaveBeenCalledWith (
339
363
"[[buttons: Release menu | Choose an action | Retry:retry, Ignore:ignore]]" ,
340
364
) ;
341
- expect ( delivered . payloads ) . toMatchObject ( [
342
- {
343
- text : "[[buttons: Release menu | Choose an action | Retry:retry, Ignore:ignore]]" ,
344
- } ,
345
- ] ) ;
365
+ expect ( delivered . payloads ) . toHaveLength ( 1 ) ;
366
+ expectTextPayload (
367
+ delivered . payloads [ 0 ] ,
368
+ "[[buttons: Release menu | Choose an action | Retry:retry, Ignore:ignore]]" ,
369
+ ) ;
346
370
} ) ;
347
371
348
372
it ( "merges result metadata overrides into JSON output and returned results" , async ( ) => {
@@ -382,10 +406,8 @@ describe("normalizeAgentCommandReplyPayloads", () => {
382
406
} ,
383
407
2 ,
384
408
) ;
385
- expect ( delivered . meta ) . toMatchObject ( {
386
- durationMs : 1 ,
387
- transport : "embedded" ,
388
- fallbackFrom : "gateway" ,
389
- } ) ;
409
+ expect ( delivered . meta . durationMs ) . toBe ( 1 ) ;
410
+ expect ( delivered . meta . transport ) . toBe ( "embedded" ) ;
411
+ expect ( delivered . meta . fallbackFrom ) . toBe ( "gateway" ) ;
390
412
} ) ;
391
413
} ) ;
0 commit comments
```

---

## 4. test: tighten codex oauth fallback assertions

- 链接: https://github.com/openclaw/openclaw/commit/0f8b52f99c9f3b0ae6cc2f600f2856ca2605d0f9

```
@@ -93,6 +93,25 @@ function resolveOpenAICodexProfile(params: { profileId: string; agentDir: string
93
93
} ) ;
94
94
}
95
95
96
+ function requireOAuthProfile ( store : AuthProfileStore , profileId : string ) : OAuthCredential {
97
+ const profile = store . profiles [ profileId ] ;
98
+ expect ( profile ?. type ) . toBe ( "oauth" ) ;
99
+ if ( ! profile || profile . type !== "oauth" ) {
100
+ throw new Error ( `expected OAuth profile ${ profileId } ` ) ;
101
+ }
102
+ return profile ;
103
+ }
104
+
105
+ function requireOAuthContext ( context : unknown ) : OAuthCredential {
106
+ expect ( context && typeof context === "object" ) . toBe ( true ) ;
107
+ if ( ! context || typeof context !== "object" ) {
108
+ throw new Error ( "expected OAuth credential context" ) ;
109
+ }
110
+ const credential = context as OAuthCredential ;
111
+ expect ( credential . type ) . toBe ( "oauth" ) ;
112
+ return credential ;
113
+ }
114
+
96
115
describe ( "resolveApiKeyForProfile openai-codex refresh fallback" , ( ) => {
97
116
const envSnapshot = captureEnv ( OAUTH_AGENT_ENV_KEYS ) ;
98
117
let tempRoot = "" ;
@@ -214,13 +233,11 @@ describe("resolveApiKeyForProfile openai-codex refresh fallback", () => {
214
233
} ) ;
215
234
216
235
const persisted = await readPersistedStore ( agentDir ) ;
217
- expect ( persisted . profiles [ profileId ] ) . toMatchObject ( {
218
- type : "oauth" ,
219
- provider : "openai-codex" ,
220
- access : "rotated-access-token" ,
221
- refresh : "rotated-refresh-token" ,
222
- accountId : "acct-rotated" ,
223
- } ) ;
236
+ const profile = requireOAuthProfile ( persisted , profileId ) ;
237
+ expect ( profile . provider ) . toBe ( "openai-codex" ) ;
238
+ expect ( profile . access ) . toBe ( "rotated-access-token" ) ;
239
+ expect ( profile . refresh ) . toBe ( "rotated-refresh-token" ) ;
240
+ expect ( profile . accountId ) . toBe ( "acct-rotated" ) ;
224
241
} ) ;
225
242
226
243
it ( "refreshes imported Codex credentials into the canonical auth store without writing back to .codex" , async ( ) => {
@@ -269,19 +286,12 @@ describe("resolveApiKeyForProfile openai-codex refresh fallback", () => {
269
286
email : undefined ,
270
287
} ) ;
271
288
const persisted = await readPersistedStore ( agentDir ) ;
272
- expect ( persisted . profiles [ profileId ] ) . toMatchObject ( {
273
- type : "oauth" ,
274
- provider : "openai-codex" ,
275
- access : "rotated-cli-access-token" ,
276
- refresh : "rotated-cli-refresh-token" ,
277
- accountId : "acct-rotated" ,
278
- } ) ;
279
- expect ( persisted . profiles [ profileId ] ) . not . toEqual (
280
- expect . objectContaining ( {
281
- provider : "openai-codex" ,
282
- access : "expired-access-token" ,
283
- } ) ,
284
- ) ;
289
+ const profile = requireOAuthProfile ( persisted , profileId ) ;
290
+ expect ( profile . provider ) . toBe ( "openai-codex" ) ;
291
+ expect ( profile . access ) . toBe ( "rotated-cli-access-token" ) ;
292
+ expect ( profile . refresh ) . toBe ( "rotated-cli-refresh-token" ) ;
293
+ expect ( profile . accountId ) . toBe ( "acct-rotated" ) ;
294
+ expect ( profile . access ) . not . toBe ( "expired-access-token" ) ;
285
295
} ) ;
286
296
287
297
it ( "ignores mismatched fresh Codex CLI credentials when canonical local auth is bound to another account" , async ( ) => {
@@ -306,11 +316,10 @@ describe("resolveApiKeyForProfile openai-codex refresh fallback", () => {
306
316
} ) ;
307
317
refreshProviderOAuthCredentialWithPluginMock . mockImplementationOnce (
308
318
async ( params ?: { context ?: unknown } ) => {
309
- expect ( params ?. context ) . toMatchObject ( {
310
- access : "expired-local-access-token" ,
311
- refresh : "local-refresh-token" ,
312
- accountId : "acct-local" ,
313
- } ) ;
319
+ const context = requireOAuthContext ( params ?. context ) ;
320
+ expect ( context . access ) . toBe ( "expired-local-access-token" ) ;
321
+ expect ( context . refresh ) . toBe ( "local-refresh-token" ) ;
322
+ expect ( context . accountId ) . toBe ( "acct-local" ) ;
314
323
return {
315
324
type : "oauth" ,
316
325
provider : "openai-codex" ,
@@ -335,18 +344,13 @@ describe("resolveApiKeyForProfile openai-codex refresh fallback", () => {
335
344
} ) ;
336
345
337
346
const persisted = await readPersistedStore ( agentDir ) ;
338
- expect ( persisted . profiles [ profileId ] ) . toMatchObject ( {
339
- access : "fresh-local-access-token" ,
340
- refresh : "fresh-local-refresh-token" ,
341
- accountId : "acct-local" ,
342
- } ) ;
343
- expect ( persisted . profiles [ profileId ] ) . not . toEqual (
344
- expect . objectContaining ( {
345
- access : "fresh-cli-access-token" ,
346
- refresh : "fresh-cli-refresh-token" ,
347
- accountId : "acct-external" ,
348
- } ) ,
349
- ) ;
347
+ const profile = requireOAuthProfile ( persisted , profileId ) ;
348
+ expect ( profile . access ) . toBe ( "fresh-local-access-token" ) ;
349
+ expect ( profile . refresh ) . toBe ( "fresh-local-refresh-token" ) ;
350
+ expect ( profile . accountId ) . toBe ( "acct-local" ) ;
351
+ expect ( profile . access ) . not . toBe ( "fresh-cli-access-token" ) ;
352
+ expect ( profile . refresh ) . not . toBe ( "fresh-cli-refresh-token" ) ;
353
+ expect ( profile . accountId ) . not . toBe ( "acct-external" ) ;
350
354
} ) ;
351
355
352
356
it ( "keeps the canonical refresh token when imported Codex CLI state is expired" , async ( ) => {
@@ -376,10 +380,9 @@ describe("resolveApiKeyForProfile openai-codex refresh fallback", () => {
376
380
} ) ;
377
381
refreshProviderOAuthCredentialWithPluginMock . mockImplementationOnce (
378
382
async ( params ?: { context ?: unknown } ) => {
379
- expect ( params ?. context ) . toMatchObject ( {
380
- access : "expired-local-access-token" ,
381
- refresh : "stale-local-refresh-token" ,
382
- } ) ;
383
+ const context = requireOAuthContext ( params ?. context ) ;
384
+ expect ( context . access ) . toBe ( "expired-local-access-token" ) ;
385
+ expect ( context . refresh ) . toBe ( "stale-local-refresh-token" ) ;
383
386
return {
384
387
type : "oauth" ,
385
388
provider : "openai-codex" ,
@@ -403,15 +406,10 @@ describe("resolveApiKeyForProfile openai-codex refresh fallback", () => {
403
406
} ) ;
404
407
405
408
const persisted = await readPersistedStore ( agentDir ) ;
406
- expect ( persisted . profiles [ profileId ] ) . toMatchObject ( {
407
- access : "fresh-access-token" ,
408
- refresh : "fresh-refresh-token" ,
409
- } ) ;
410
- expect ( persisted . profiles [ profileId ] ) . not . toEqual (
411
- expect . objectContaining ( {
412
- refresh : "fresh-cli-refresh-token" ,
413
- } ) ,
414
- ) ;
409
+ const profile = requireOAuthProfile ( persisted , profileId ) ;
410
+ expect ( profile . access ) . toBe ( "fresh-access-token" ) ;
411
+ expect ( profile . refresh ) . toBe ( "fresh-refresh-token" ) ;
412
+ expect ( profile . refresh ) . not . toBe ( "fresh-cli-refresh-token" ) ;
415
413
} ) ;
416
414
417
415
it ( "adopts fresher stored credentials after refresh_token_reused" , async ( ) => {
@@ -516,10 +514,9 @@ describe("resolveApiKeyForProfile openai-codex refresh fallback", () => {
516
514
517
515
expect ( getOAuthApiKeyMock ) . toHaveBeenCalledTimes ( 2 ) ;
518
516
const persisted = await readPersistedStore ( agentDir ) ;
519
- expect ( persisted . profiles [ profileId ] ) . toMatchObject ( {
520
- access : "retried-access-token" ,
521
- refresh : "retried-refresh-token" ,
522
- } ) ;
517
+ const profile = requireOAuthProfile ( persisted , profileId ) ;
518
+ expect ( profile . access ) . toBe ( "retried-access-token" ) ;
519
+ expect ( profile . refresh ) . toBe ( "retried-refresh-token" ) ;
523
520
} ) ;
524
521
525
522
it ( "keeps throwing for non-codex providers on the same refresh error" , async ( ) => {
0 commit comments
```

---

## 5. fix: load linked plugin facades when bundled fallback is off

- 链接: https://github.com/openclaw/openclaw/commit/f1406b1b56ef6476b41e80150e0c3ad70d3ace13

```
We read every piece of feedback, and take your input very seriously.
To see all available qualifiers, see our documentation.
There was an error while loading. Please reload this page.
1 parent 9b17c98 commit f1406b1Copy full SHA for f1406b1
2 files changed
CHANGELOG.md
@@ -8,6 +8,7 @@ Docs: https://docs.openclaw.ai
8
9
### Fixes
10
11
+- Plugin SDK: keep activated linked plugin runtime facades loadable when bundled plugin fallback is disabled. Thanks @shakkernerd.
12
- Feishu: auto-thread `message(action="send")` replies inside the topic when the active session is group_topic or group_topic_sender, and propagate `replyInThread` through text, card, and media outbound adapters so topic-scoped sessions no longer post at the group root. Fixes #74903. (#77151) Thanks @ai-hpc.
13
- WhatsApp: pass routing context into voice-note transcript echo preflight so echoed transcripts can deliver to the originating chat. Fixes #79778. (#79788) Thanks @hclsys.
14
- Cron/failover: classify structured OpenAI-compatible `server_error` payloads as `server_error`, expose that reason in cron state, and let one-shot cron retry policy honor `retryOn: ["server_error"]` without requiring raw `5xx` text. (#45594) Thanks @clovericbot.
src/plugin-sdk/facade-runtime.ts
@@ -75,18 +75,17 @@ function resolveFacadeModuleLocationUncached(params: {
75
env?: NodeJS.ProcessEnv;
76
}): { modulePath: string; boundaryRoot: string } | null {
77
const env = params.env ?? process.env;
78
- if (areBundledPluginsDisabled(env)) {
79
- return null;
80
- }
81
- const bundledPluginsDir = resolveBundledPluginsDir(env);
82
- const bundledLocation = resolveBundledFacadeModuleLocation({
83
- ...params,
84
- currentModulePath: CURRENT_MODULE_PATH,
85
- packageRoot: OPENCLAW_PACKAGE_ROOT,
86
- bundledPluginsDir,
87
- });
88
- if (bundledLocation) {
89
- return bundledLocation;
+ if (!areBundledPluginsDisabled(env)) {
+ const bundledPluginsDir = resolveBundledPluginsDir(env);
+ const bundledLocation = resolveBundledFacadeModuleLocation({
+ ...params,
+ currentModulePath: CURRENT_MODULE_PATH,
+ packageRoot: OPENCLAW_PACKAGE_ROOT,
+ bundledPluginsDir,
+ });
+ if (bundledLocation) {
+ return bundledLocation;
+ }
90
}
91
return resolveRegistryPluginModuleLocation(params);
92
0 commit comments
```

---

## 6. test: tighten subagent context assertions

- 链接: https://github.com/openclaw/openclaw/commit/9b17c98429bae410d354af38514a297d712f7df1

```
@@ -49,6 +49,48 @@ describe("sessions_spawn context modes", () => {
49
49
} ) ;
50
50
}
51
51
52
+ function requireAcceptedResult ( result : Awaited < ReturnType < typeof spawnSubagentDirect > > ) {
53
+ expect ( result . status ) . toBe ( "accepted" ) ;
54
+ if ( result . status !== "accepted" ) {
55
+ throw new Error ( `expected accepted result, got ${ result . status } ` ) ;
56
+ }
57
+ return result ;
58
+ }
59
+
60
+ function requireStoreEntry ( store : SessionStore , key : string ) : Record < string , unknown > {
61
+ const entry = store [ key ] ;
62
+ if ( ! entry ) {
63
+ throw new Error ( `expected session store entry ${ key } ` ) ;
64
+ }
65
+ return entry ;
66
+ }
67
+
68
+ function requireChildSessionKey ( result : Awaited < ReturnType < typeof spawnSubagentDirect > > ) : string {
69
+ const key = result . childSessionKey ;
70
+ if ( ! key ) {
71
+ throw new Error ( "expected child session key" ) ;
72
+ }
73
+ return key ;
74
+ }
75
+
76
+ function requireFirstMockArg ( mock : ReturnType < typeof vi . fn > ) : Record < string , unknown > {
77
+ const arg = mock . mock . calls . at ( 0 ) ?. [ 0 ] ;
78
+ if ( ! arg || typeof arg !== "object" ) {
79
+ throw new Error ( "expected first mock argument object" ) ;
80
+ }
81
+ return arg as Record < string , unknown > ;
82
+ }
83
+
84
+ function requireGatewayRequest ( method : string ) : GatewayRequest {
85
+ const request = callGatewayMock . mock . calls
86
+ . map ( ( [ arg ] ) => arg as GatewayRequest )
87
+ . find ( ( candidate ) => candidate . method === method ) ;
88
+ if ( ! request ) {
89
+ throw new Error ( `expected gateway request ${ method } ` ) ;
90
+ }
91
+ return request ;
92
+ }
93
+
52
94
it ( "forks the requester transcript when context=fork" , async ( ) => {
53
95
const store : SessionStore = {
54
96
main : {
@@ -71,27 +113,26 @@ describe("sessions_spawn context modes", () => {
71
113
{ agentSessionKey : "main" } ,
72
114
) ;
73
115
74
- expect ( result ) . toMatchObject ( { status : "accepted" , runId : "run-1" } ) ;
116
+ const accepted = requireAcceptedResult ( result ) ;
117
+ expect ( accepted . runId ) . toBe ( "run-1" ) ;
75
118
expect ( forkSessionFromParentMock ) . toHaveBeenCalledWith ( {
76
119
parentEntry : store . main ,
77
120
agentId : "main" ,
78
121
sessionsDir : path . dirname ( storePath ) ,
79
122
} ) ;
80
- expect ( store [ result . childSessionKey ?? "" ] ) . toMatchObject ( {
81
- sessionId : "forked-session-id" ,
82
- sessionFile : "/tmp/forked-session.jsonl" ,
83
- forkedFromParent : true ,
84
- } ) ;
85
- expect ( prepareSubagentSpawn ) . toHaveBeenCalledWith (
86
- expect . objectContaining ( {
87
- parentSessionKey : "main" ,
88
- childSessionKey : result . childSessionKey ,
89
- contextMode : "fork" ,
90
- parentSessionId : "parent-session-id" ,
91
- childSessionId : "forked-session-id" ,
92
- childSessionFile : "/tmp/forked-session.jsonl" ,
93
- } ) ,
94
- ) ;
123
+ const childSessionKey = requireChildSessionKey ( accepted ) ;
124
+ const childEntry = requireStoreEntry ( store , childSessionKey ) ;
125
+ expect ( childEntry . sessionId ) . toBe ( "forked-session-id" ) ;
126
+ expect ( childEntry . sessionFile ) . toBe ( "/tmp/forked-session.jsonl" ) ;
127
+ expect ( childEntry . forkedFromParent ) . toBe ( true ) ;
128
+
129
+ const prepareContext = requireFirstMockArg ( prepareSubagentSpawn ) ;
130
+ expect ( prepareContext . parentSessionKey ) . toBe ( "main" ) ;
131
+ expect ( prepareContext . childSessionKey ) . toBe ( childSessionKey ) ;
132
+ expect ( prepareContext . contextMode ) . toBe ( "fork" ) ;
133
+ expect ( prepareContext . parentSessionId ) . toBe ( "parent-session-id" ) ;
134
+ expect ( prepareContext . childSessionId ) . toBe ( "forked-session-id" ) ;
135
+ expect ( prepareContext . childSessionFile ) . toBe ( "/tmp/forked-session.jsonl" ) ;
95
136
} ) ;
96
137
97
138
it ( "keeps the default spawn context isolated" , async ( ) => {
@@ -106,13 +147,10 @@ describe("sessions_spawn context modes", () => {
106
147
107
148
expect ( result . status ) . toBe ( "accepted" ) ;
108
149
expect ( forkSessionFromParentMock ) . not . toHaveBeenCalled ( ) ;
109
- expect ( prepareSubagentSpawn ) . toHaveBeenCalledWith (
110
- expect . objectContaining ( {
111
- parentSessionKey : "main" ,
112
- childSessionKey : result . childSessionKey ,
113
- contextMode : "isolated" ,
114
- } ) ,
115
- ) ;
150
+ const prepareContext = requireFirstMockArg ( prepareSubagentSpawn ) ;
151
+ expect ( prepareContext . parentSessionKey ) . toBe ( "main" ) ;
152
+ expect ( prepareContext . childSessionKey ) . toBe ( requireChildSessionKey ( result ) ) ;
153
+ expect ( prepareContext . contextMode ) . toBe ( "isolated" ) ;
116
154
} ) ;
117
155
118
156
it ( "falls back to isolated context when requested fork is too large" , async ( ) => {
@@ -133,17 +171,15 @@ describe("sessions_spawn context modes", () => {
133
171
{ agentSessionKey : "main" } ,
134
172
) ;
135
173
136
- expect ( result ) . toMatchObject ( { status : "accepted" , runId : "run-1" } ) ;
137
- expect ( result . note ) . toContain ( "Parent context is too large to fork" ) ;
174
+ const accepted = requireAcceptedResult ( result ) ;
175
+ expect ( accepted . runId ) . toBe ( "run-1" ) ;
176
+ expect ( accepted . note ) . toContain ( "Parent context is too large to fork" ) ;
138
177
expect ( forkSessionFromParentMock ) . not . toHaveBeenCalled ( ) ;
139
- expect ( prepareSubagentSpawn ) . toHaveBeenCalledWith (
140
- expect . objectContaining ( {
141
- parentSessionKey : "main" ,
142
- childSessionKey : result . childSessionKey ,
143
- contextMode : "isolated" ,
144
- parentSessionId : "parent-session-id" ,
145
- } ) ,
146
- ) ;
178
+ const prepareContext = requireFirstMockArg ( prepareSubagentSpawn ) ;
179
+ expect ( prepareContext . parentSessionKey ) . toBe ( "main" ) ;
180
+ expect ( prepareContext . childSessionKey ) . toBe ( requireChildSessionKey ( accepted ) ) ;
181
+ expect ( prepareContext . contextMode ) . toBe ( "isolated" ) ;
182
+ expect ( prepareContext . parentSessionId ) . toBe ( "parent-session-id" ) ;
147
183
} ) ;
148
184
149
185
it ( "forks by default for thread-bound subagent sessions" , async ( ) => {
@@ -179,16 +215,10 @@ describe("sessions_spawn context modes", () => {
179
215
agentId : "main" ,
180
216
sessionsDir : path . dirname ( storePath ) ,
181
217
} ) ;
182
- expect ( callGatewayMock ) . toHaveBeenCalledWith (
183
- expect . objectContaining ( {
184
- method : "sessions.delete" ,
185
- params : expect . objectContaining ( {
186
- key : result . childSessionKey ,
187
- deleteTranscript : true ,
188
- emitLifecycleHooks : false ,
189
- } ) ,
190
- } ) ,
191
- ) ;
218
+ const cleanupRequest = requireGatewayRequest ( "sessions.delete" ) ;
219
+ expect ( cleanupRequest . params ?. key ) . toBe ( result . childSessionKey ) ;
220
+ expect ( cleanupRequest . params ?. deleteTranscript ) . toBe ( true ) ;
221
+ expect ( cleanupRequest . params ?. emitLifecycleHooks ) . toBe ( false ) ;
192
222
expect ( prepareSubagentSpawn ) . not . toHaveBeenCalled ( ) ;
193
223
} ) ;
194
224
@@ -234,7 +264,8 @@ describe("sessions_spawn context modes", () => {
234
264
235
265
const result = await spawnSubagentDirect ( { task : "clean worker" } , { agentSessionKey : "main" } ) ;
236
266
237
- expect ( result ) . toMatchObject ( { status : "error" , error : "agent start failed" } ) ;
267
+ expect ( result . status ) . toBe ( "error" ) ;
268
+ expect ( result . error ) . toBe ( "agent start failed" ) ;
238
269
expect ( rollback ) . toHaveBeenCalledTimes ( 1 ) ;
239
270
expect ( callGatewayMock . mock . calls . map ( ( call ) => ( call [ 0 ] as GatewayRequest ) . method ) ) . toContain (
240
271
"sessions.delete" ,
0 commit comments
```

---

## 7. test: tighten run wait assertions

- 链接: https://github.com/openclaw/openclaw/commit/f3e752ccf8197f0b690a144eae9782be29557c47

```
@@ -15,6 +15,55 @@ import {
15
15
waitForAgentRunAndReadUpdatedAssistantReply ,
16
16
} from "./run-wait.js" ;
17
17
18
+ type AgentWaitGatewayRequest = {
19
+ method ?: string ;
20
+ params ?: {
21
+ runId ?: string ;
22
+ timeoutMs ?: unknown ;
23
+ } ;
24
+ timeoutMs ?: unknown ;
25
+ } ;
26
+
27
+ function expectNumber ( value : unknown , label : string ) : number {
28
+ expect ( typeof value ) . toBe ( "number" ) ;
29
+ if ( typeof value !== "number" ) {
30
+ throw new Error ( `expected ${ label } to be a number` ) ;
31
+ }
32
+ return value ;
33
+ }
34
+
35
+ function gatewayWaitRequests ( ) : AgentWaitGatewayRequest [ ] {
36
+ return callGatewayMock . mock . calls . map ( ( [ request ] ) => request as AgentWaitGatewayRequest ) ;
37
+ }
38
+
39
+ function requireRequestAt (
40
+ requests : readonly AgentWaitGatewayRequest [ ] ,
41
+ index : number ,
42
+ ) : AgentWaitGatewayRequest {
43
+ const request = requests . at ( index ) ;
44
+ if ( ! request ) {
45
+ throw new Error ( `expected gateway request at index ${ index } ` ) ;
46
+ }
47
+ return request ;
48
+ }
49
+
50
+ function expectAgentWaitRequest (
51
+ request : AgentWaitGatewayRequest ,
52
+ runId : string ,
53
+ maxParamTimeoutMs : number ,
54
+ ) : void {
55
+ expect ( request . method ) . toBe ( "agent.wait" ) ;
56
+ expect ( request . params ?. runId ) . toBe ( runId ) ;
57
+
58
+ const paramTimeoutMs = expectNumber ( request . params ?. timeoutMs , `${ runId } param timeoutMs` ) ;
59
+ const requestTimeoutMs = expectNumber ( request . timeoutMs , `${ runId } request timeoutMs` ) ;
60
+ expect ( requestTimeoutMs ) . toBeGreaterThan ( 0 ) ;
61
+ expect ( requestTimeoutMs ) . toBeLessThanOrEqual ( maxParamTimeoutMs + 2_000 ) ;
62
+ expect ( paramTimeoutMs ) . toBe ( requestTimeoutMs - 2_000 ) ;
63
+ expect ( paramTimeoutMs ) . toBeGreaterThan ( 0 ) ;
64
+ expect ( paramTimeoutMs ) . toBeLessThanOrEqual ( maxParamTimeoutMs ) ;
65
+ }
66
+
18
67
describe ( "readLatestAssistantReply" , ( ) => {
19
68
beforeEach ( ( ) => {
20
69
callGatewayMock . mockClear ( ) ;
@@ -287,29 +336,14 @@ describe("waitForAgentRunsToDrain", () => {
287
336
getPendingRunIds : ( ) => activeRunIds ,
288
337
} ) ;
289
338
290
- expect ( result ) . toEqual ( {
291
- timedOut : false ,
292
- pendingRunIds : [ ] ,
293
- deadlineAtMs : expect . any ( Number ) ,
294
- } ) ;
295
- expect ( callGatewayMock . mock . calls . map ( ( call ) => call [ 0 ] ) ) . toEqual ( [
296
- {
297
- method : "agent.wait" ,
298
- params : {
299
- runId : "run-1" ,
300
- timeoutMs : expect . any ( Number ) ,
301
- } ,
302
- timeoutMs : expect . any ( Number ) ,
303
- } ,
304
- {
305
- method : "agent.wait" ,
306
- params : {
307
- runId : "run-2" ,
308
- timeoutMs : expect . any ( Number ) ,
309
- } ,
310
- timeoutMs : expect . any ( Number ) ,
311
- } ,
312
- ] ) ;
339
+ expect ( result . timedOut ) . toBe ( false ) ;
340
+ expect ( result . pendingRunIds ) . toStrictEqual ( [ ] ) ;
341
+ expectNumber ( result . deadlineAtMs , "deadlineAtMs" ) ;
342
+
343
+ const requests = gatewayWaitRequests ( ) ;
344
+ expect ( requests ) . toHaveLength ( 2 ) ;
345
+ expectAgentWaitRequest ( requireRequestAt ( requests , 0 ) , "run-1" , 1_000 ) ;
346
+ expectAgentWaitRequest ( requireRequestAt ( requests , 1 ) , "run-2" , 1_000 ) ;
313
347
} ) ;
314
348
315
349
it ( "deduplicates and trims pending run ids" , async ( ) => {
@@ -344,15 +378,9 @@ describe("waitForAgentRunsToDrain", () => {
344
378
} ) ;
345
379
346
380
expect ( result . timedOut ) . toBe ( false ) ;
347
- expect ( callGatewayMock . mock . calls . map ( ( call ) => call [ 0 ] ) ) . toEqual ( [
348
- expect . objectContaining ( {
349
- method : "agent.wait" ,
350
- params : expect . objectContaining ( { runId : "run-1" } ) ,
351
- } ) ,
352
- expect . objectContaining ( {
353
- method : "agent.wait" ,
354
- params : expect . objectContaining ( { runId : "run-2" } ) ,
355
- } ) ,
356
- ] ) ;
381
+ const requests = gatewayWaitRequests ( ) ;
382
+ expect ( requests ) . toHaveLength ( 2 ) ;
383
+ expectAgentWaitRequest ( requireRequestAt ( requests , 0 ) , "run-1" , 1_000 ) ;
384
+ expectAgentWaitRequest ( requireRequestAt ( requests , 1 ) , "run-2" , 1_000 ) ;
357
385
} ) ;
358
386
} ) ;
0 commit comments
```

---

## 8. test: tighten coding tools assertions

- 链接: https://github.com/openclaw/openclaw/commit/2f0b0befbaee027061f58e1bdeb050419a9ab6eb

```
@@ -93,6 +93,7 @@ function applyRuntimeToolsAllow<T extends { name: string }>(tools: T[], toolsAll
93
93
}
94
94
95
95
type OpenClawCodingTool = ReturnType < typeof createOpenClawCodingTools > [ number ] ;
96
+ type OpenClawToolsOptions = NonNullable < Parameters < typeof createOpenClawTools > [ 0 ] > ;
96
97
97
98
function toolNameList ( tools : readonly { name : string } [ ] ) : string [ ] {
98
99
return tools . map ( ( tool ) => tool . name ) ;
@@ -113,6 +114,28 @@ function requireToolExecute(tool: OpenClawCodingTool): NonNullable<OpenClawCodin
113
114
return tool . execute ;
114
115
}
115
116
117
+ function latestCreateOpenClawToolsOptions ( ) : OpenClawToolsOptions {
118
+ const calls = vi . mocked ( createOpenClawTools ) . mock . calls ;
119
+ const lastCall = calls . at ( - 1 ) ;
120
+ const options = lastCall ?. [ 0 ] ;
121
+ if ( ! options ) {
122
+ throw new Error ( "expected createOpenClawTools call" ) ;
123
+ }
124
+ return options ;
125
+ }
126
+
127
+ function expectListIncludes (
128
+ list : readonly string [ ] | undefined ,
129
+ expected : readonly string [ ] ,
130
+ ) : void {
131
+ if ( ! list ) {
132
+ throw new Error ( "expected string list" ) ;
133
+ }
134
+ for ( const value of expected ) {
135
+ expect ( list . includes ( value ) ) . toBe ( true ) ;
136
+ }
137
+ }
138
+
116
139
describe ( "createOpenClawCodingTools" , ( ) => {
117
140
const testConfig : OpenClawConfig = { } ;
118
141
@@ -129,9 +152,7 @@ describe("createOpenClawCodingTools", () => {
129
152
const values = new Set < string > ( ) ;
130
153
collectActionValues ( action , values ) ;
131
154
132
- expect ( [ ...values ] ) . toEqual (
133
- expect . arrayContaining ( [ "restart" , "config.get" , "config.patch" , "config.apply" ] ) ,
134
- ) ;
155
+ expectListIncludes ( [ ...values ] , [ "restart" , "config.get" , "config.patch" , "config.apply" ] ) ;
135
156
} ) ;
136
157
137
158
it ( "exposes only an explicitly authorized owner-only tool to non-owner sessions" , ( ) => {
@@ -193,11 +214,9 @@ describe("createOpenClawCodingTools", () => {
193
214
runtimeToolAllowlist : [ "memory_search" , "memory_get" ] ,
194
215
} ) ;
195
216
196
- expect ( createOpenClawToolsMock ) . toHaveBeenCalledWith (
197
- expect . objectContaining ( {
198
- pluginToolAllowlist : expect . arrayContaining ( [ "memory_search" , "memory_get" ] ) ,
199
- } ) ,
200
- ) ;
217
+ expect ( createOpenClawToolsMock ) . toHaveBeenCalledTimes ( 1 ) ;
218
+ const options = latestCreateOpenClawToolsOptions ( ) ;
219
+ expectListIncludes ( options . pluginToolAllowlist , [ "memory_search" , "memory_get" ] ) ;
201
220
} ) ;
202
221
203
222
it ( "passes source reply delivery mode to OpenClaw tool construction" , ( ) => {
@@ -210,11 +229,8 @@ describe("createOpenClawCodingTools", () => {
210
229
sourceReplyDeliveryMode : "message_tool_only" ,
211
230
} ) ;
212
231
213
- expect ( createOpenClawToolsMock ) . toHaveBeenCalledWith (
214
- expect . objectContaining ( {
215
- sourceReplyDeliveryMode : "message_tool_only" ,
216
- } ) ,
217
- ) ;
232
+ expect ( createOpenClawToolsMock ) . toHaveBeenCalledTimes ( 1 ) ;
233
+ expect ( latestCreateOpenClawToolsOptions ( ) . sourceReplyDeliveryMode ) . toBe ( "message_tool_only" ) ;
218
234
} ) ;
219
235
220
236
it ( "skips unrelated tool families when construction is planned from a narrow allowlist" , ( ) => {
@@ -258,11 +274,8 @@ describe("createOpenClawCodingTools", () => {
258
274
} ,
259
275
} ) ;
260
276
261
- expect ( createOpenClawToolsMock ) . toHaveBeenCalledWith (
262
- expect . objectContaining ( {
263
- disablePluginTools : true ,
264
- } ) ,
265
- ) ;
277
+ expect ( createOpenClawToolsMock ) . toHaveBeenCalledTimes ( 1 ) ;
278
+ expect ( latestCreateOpenClawToolsOptions ( ) . disablePluginTools ) . toBe ( true ) ;
266
279
} ) ;
267
280
268
281
it ( "keeps plugin-only construction off the OpenClaw core factory" , ( ) => {
@@ -293,11 +306,11 @@ describe("createOpenClawCodingTools", () => {
293
306
config : { tools : { alsoAllow : [ "lobster" ] } } ,
294
307
} ) ;
295
308
296
- expect ( createOpenClawToolsMock ) . toHaveBeenCalledWith (
297
- expect . objectContaining ( {
298
- pluginToolAllowlist : [ "lobster" , DEFAULT_PLUGIN_TOOLS_ALLOWLIST_ENTRY ] ,
299
- } ) ,
300
- ) ;
309
+ expect ( createOpenClawToolsMock ) . toHaveBeenCalledTimes ( 1 ) ;
310
+ expect ( latestCreateOpenClawToolsOptions ( ) . pluginToolAllowlist ) . toStrictEqual ( [
311
+ "lobster" ,
312
+ DEFAULT_PLUGIN_TOOLS_ALLOWLIST_ENTRY ,
313
+ ] ) ;
301
314
} ) ;
302
315
303
316
it ( "passes explicit denylist entries to OpenClaw tool factory planning" , ( ) => {
@@ -308,11 +321,8 @@ describe("createOpenClawCodingTools", () => {
308
321
config : { tools : { deny : [ "pdf" ] } } ,
309
322
} ) ;
310
323
311
- expect ( createOpenClawToolsMock ) . toHaveBeenCalledWith (
312
- expect . objectContaining ( {
313
- pluginToolDenylist : expect . arrayContaining ( [ "pdf" ] ) ,
314
- } ) ,
315
- ) ;
324
+ expect ( createOpenClawToolsMock ) . toHaveBeenCalledTimes ( 1 ) ;
325
+ expectListIncludes ( latestCreateOpenClawToolsOptions ( ) . pluginToolDenylist , [ "pdf" ] ) ;
316
326
} ) ;
317
327
318
328
it ( "records core tool-prep stages for hot-path diagnostics" , ( ) => {
@@ -324,23 +334,21 @@ describe("createOpenClawCodingTools", () => {
324
334
senderIsOwner : true ,
325
335
} ) ;
326
336
327
- expect ( stages ) . toEqual (
328
- expect . arrayContaining ( [
329
- "tool-policy" ,
330
- "workspace-policy" ,
331
- "base-coding-tools" ,
332
- "shell-tools" ,
333
- "openclaw-tools:test-helper" ,
334
- "openclaw-tools" ,
335
- "message-provider-policy" ,
336
- "model-provider-policy" ,
337
- "authorization-policy" ,
338
- "schema-normalization" ,
339
- "tool-hooks" ,
340
- "abort-wrappers" ,
341
- "deferred-followup-descriptions" ,
342
- ] ) ,
343
- ) ;
337
+ expectListIncludes ( stages , [
338
+ "tool-policy" ,
339
+ "workspace-policy" ,
340
+ "base-coding-tools" ,
341
+ "shell-tools" ,
342
+ "openclaw-tools:test-helper" ,
343
+ "openclaw-tools" ,
344
+ "message-provider-policy" ,
345
+ "model-provider-policy" ,
346
+ "authorization-policy" ,
347
+ "schema-normalization" ,
348
+ "tool-hooks" ,
349
+ "abort-wrappers" ,
350
+ "deferred-followup-descriptions" ,
351
+ ] ) ;
344
352
expect ( stages . indexOf ( "tool-policy" ) ) . toBeLessThan ( stages . indexOf ( "workspace-policy" ) ) ;
345
353
expect ( stages . indexOf ( "workspace-policy" ) ) . toBeLessThan ( stages . indexOf ( "base-coding-tools" ) ) ;
346
354
expect ( stages . indexOf ( "openclaw-tools:test-helper" ) ) . toBeLessThan (
0 commit comments
```

---

## 9. test: tighten tool result context guard assertions

- 链接: https://github.com/openclaw/openclaw/commit/60cb2325a1ce1fd20691882f45102a95180ebdf4

```
@@ -220,8 +220,12 @@ describe("installToolResultContextGuard", () => {
220
220
221
221
expectPiStyleTruncation ( newResultText ) ;
222
222
expect ( result . details ) . toBeUndefined ( ) ;
223
- expect ( ( contextForNextCall [ 0 ] as { details ?: unknown } ) . details ) . toMatchObject ( {
224
- truncation : { truncated : true } ,
223
+ const originalDetails = ( contextForNextCall [ 0 ] as { details ?: { truncation ?: unknown } } )
224
+ . details ;
225
+ expect ( originalDetails ?. truncation ) . toEqual ( {
226
+ truncated : true ,
227
+ outputLines : 100 ,
228
+ content : "d" . repeat ( 8_000 ) ,
225
229
} ) ;
226
230
} ) ;
227
231
@@ -290,22 +294,23 @@ describe("installToolResultContextGuard", () => {
290
294
makeToolResult ( "call_big" , "x" . repeat ( 80_000 ) ) ,
291
295
] ;
292
296
293
- await expect (
294
- applyMidTurnPrecheckGuardToContext ( agent , contextForNextCall , {
297
+ try {
298
+ await applyMidTurnPrecheckGuardToContext ( agent , contextForNextCall , {
295
299
contextWindowTokens : 200_000 ,
296
300
contextTokenBudget : 20_000 ,
297
301
reserveTokens : 12_000 ,
298
302
toolResultMaxChars : 16_000 ,
299
303
prePromptMessageCount : 1 ,
300
- } ) ,
301
- ) . rejects . toMatchObject ( {
302
- name : "MidTurnPrecheckSignal" ,
303
- request : expect . objectContaining ( {
304
- route : "compact_then_truncate" ,
305
- overflowTokens : expect . any ( Number ) ,
306
- toolResultReducibleChars : expect . any ( Number ) ,
307
- } ) ,
308
- } ) ;
304
+ } ) ;
305
+ throw new Error ( "expected mid-turn precheck signal" ) ;
306
+ } catch ( err ) {
307
+ expect ( err ) . toBeInstanceOf ( MidTurnPrecheckSignal ) ;
308
+ const signal = err as MidTurnPrecheckSignal ;
309
+ expect ( signal . name ) . toBe ( "MidTurnPrecheckSignal" ) ;
310
+ expect ( signal . request . route ) . toBe ( "compact_then_truncate" ) ;
311
+ expect ( typeof signal . request . overflowTokens ) . toBe ( "number" ) ;
312
+ expect ( typeof signal . request . toolResultReducibleChars ) . toBe ( "number" ) ;
313
+ }
309
314
} ) ;
310
315
311
316
it ( "does not run mid-turn precheck when no new tool result was appended" , async ( ) => {
@@ -481,10 +486,9 @@ describe("installContextEngineLoopHook", () => {
481
486
await callTransform ( agent , messages ) ;
482
487
483
488
expect ( engine . afterTurn ) . toHaveBeenCalledTimes ( 1 ) ;
484
- expect ( engine . afterTurn . mock . calls [ 0 ] ?. [ 0 ] ) . toMatchObject ( {
485
- prePromptMessageCount : 1 ,
486
- messages,
487
- } ) ;
489
+ const afterTurnParams = engine . afterTurn . mock . calls [ 0 ] ?. [ 0 ] ;
490
+ expect ( afterTurnParams ?. prePromptMessageCount ) . toBe ( 1 ) ;
491
+ expect ( afterTurnParams ?. messages ) . toBe ( messages ) ;
488
492
expect ( engine . assemble ) . toHaveBeenCalledTimes ( 1 ) ;
489
493
} ) ;
490
494
@@ -504,15 +508,14 @@ describe("installContextEngineLoopHook", () => {
504
508
await callTransform ( agent , messages ) ;
505
509
506
510
expect ( engine . afterTurn ) . toHaveBeenCalledTimes ( 1 ) ;
507
- expect ( engine . afterTurn . mock . calls [ 0 ] ?. [ 0 ] ) . toMatchObject ( {
508
- prePromptMessageCount : 1 ,
509
- runtimeContext : {
510
- provider : "anthropic" ,
511
- modelId,
512
- promptCache : {
513
- retention : "short" ,
514
- lastCacheTouchAt : 123 ,
515
- } ,
511
+ const afterTurnParams = engine . afterTurn . mock . calls [ 0 ] ?. [ 0 ] ;
512
+ expect ( afterTurnParams ?. prePromptMessageCount ) . toBe ( 1 ) ;
513
+ expect ( afterTurnParams ?. runtimeContext ) . toEqual ( {
514
+ provider : "anthropic" ,
515
+ modelId,
516
+ promptCache : {
517
+ retention : "short" ,
518
+ lastCacheTouchAt : 123 ,
516
519
} ,
517
520
} ) ;
518
521
} ) ;
@@ -548,10 +551,9 @@ describe("installContextEngineLoopHook", () => {
548
551
await callTransform ( agent , withNew ) ;
549
552
550
553
expect ( engine . afterTurn ) . toHaveBeenCalledTimes ( 1 ) ;
551
- expect ( engine . afterTurn . mock . calls [ 0 ] ?. [ 0 ] ) . toMatchObject ( {
552
- prePromptMessageCount : 2 ,
553
- messages : withNew ,
554
- } ) ;
554
+ const afterTurnParams = engine . afterTurn . mock . calls [ 0 ] ?. [ 0 ] ;
555
+ expect ( afterTurnParams ?. prePromptMessageCount ) . toBe ( 2 ) ;
556
+ expect ( afterTurnParams ?. messages ) . toBe ( withNew ) ;
555
557
expect ( engine . assemble ) . toHaveBeenCalledTimes ( 1 ) ;
556
558
} ) ;
557
559
@@ -774,11 +776,10 @@ describe("installContextEngineLoopHook", () => {
774
776
await callTransform ( agent , messages ) ;
775
777
776
778
expect ( engine . ingest ) . toHaveBeenCalledTimes ( 1 ) ;
777
- expect ( engine . ingest . mock . calls [ 0 ] ?. [ 0 ] ) . toMatchObject ( {
778
- sessionId,
779
- sessionKey,
780
- message : toolResult ,
781
- } ) ;
779
+ const ingestParams = engine . ingest . mock . calls [ 0 ] ?. [ 0 ] ;
780
+ expect ( ingestParams ?. sessionId ) . toBe ( sessionId ) ;
781
+ expect ( ingestParams ?. sessionKey ) . toBe ( sessionKey ) ;
782
+ expect ( ingestParams ?. message ) . toBe ( toolResult ) ;
782
783
expect ( engine . assemble ) . toHaveBeenCalledTimes ( 1 ) ;
783
784
} ) ;
784
785
0 commit comments
```

---

## 10. test: tighten sandbox create arg assertions

- 链接: https://github.com/openclaw/openclaw/commit/34d040644d098794bddff67f408025d1bb1730c8

```
@@ -38,6 +38,26 @@ describe("buildSandboxCreateArgs", () => {
38
38
) . toThrow ( expectedMessage ) ;
39
39
}
40
40
41
+ function valuesForFlag ( args : string [ ] , flag : string ) : string [ ] {
42
+ const values : string [ ] = [ ] ;
43
+ for ( let i = 0 ; i < args . length ; i += 1 ) {
44
+ if ( args [ i ] === flag ) {
45
+ const value = args [ i + 1 ] ;
46
+ if ( value ) {
47
+ values . push ( value ) ;
48
+ }
49
+ }
50
+ }
51
+ return values ;
52
+ }
53
+
54
+ function expectFlagValues ( args : string [ ] , flag : string , expectedValues : string [ ] ) : void {
55
+ const values = valuesForFlag ( args , flag ) ;
56
+ for ( const value of expectedValues ) {
57
+ expect ( values ) . toContain ( value ) ;
58
+ }
59
+ }
60
+
41
61
it ( "includes hardening and resource flags" , ( ) => {
42
62
const cfg : SandboxDockerConfig = {
43
63
image : "openclaw-sandbox:bookworm-slim" ,
@@ -72,69 +92,32 @@ describe("buildSandboxCreateArgs", () => {
72
92
labels : { "openclaw.sandboxBrowser" : "1" } ,
73
93
} ) ;
74
94
75
- expect ( args ) . toEqual (
76
- expect . arrayContaining ( [
77
- "create" ,
78
- "--name" ,
79
- "openclaw-sbx-test" ,
80
- "--label" ,
81
- "openclaw.sandbox=1" ,
82
- "--label" ,
83
- "openclaw.sessionKey=main" ,
84
- "--label" ,
85
- "openclaw.createdAtMs=1700000000000" ,
86
- "--label" ,
87
- "openclaw.sandboxBrowser=1" ,
88
- "--read-only" ,
89
- "--tmpfs" ,
90
- "/tmp" ,
91
- "--network" ,
92
- "none" ,
93
- "--user" ,
94
- "1000:1000" ,
95
- "--cap-drop" ,
96
- "ALL" ,
97
- "--security-opt" ,
98
- "no-new-privileges" ,
99
- "--security-opt" ,
100
- "seccomp=/tmp/seccomp.json" ,
101
- "--security-opt" ,
102
- "apparmor=openclaw-sandbox" ,
103
- "--dns" ,
104
- "1.1.1.1" ,
105
- "--add-host" ,
106
- "internal.service:10.0.0.5" ,
107
- "--pids-limit" ,
108
- "256" ,
109
- "--memory" ,
110
- "512m" ,
111
- "--memory-swap" ,
112
- "1024" ,
113
- "--cpus" ,
114
- "1.5" ,
115
- ] ) ,
116
- ) ;
117
- expect ( args ) . toEqual (
118
- expect . arrayContaining ( [
119
- "--env" ,
120
- "LANG=C.UTF-8" ,
121
- "--env" ,
122
- `OPENCLAW_CLI=${ OPENCLAW_CLI_ENV_VALUE } ` ,
123
- ] ) ,
124
- ) ;
125
-
126
- const ulimitValues : string [ ] = [ ] ;
127
- for ( let i = 0 ; i < args . length ; i += 1 ) {
128
- if ( args [ i ] === "--ulimit" ) {
129
- const value = args [ i + 1 ] ;
130
- if ( value ) {
131
- ulimitValues . push ( value ) ;
132
- }
133
- }
134
- }
135
- expect ( ulimitValues ) . toEqual (
136
- expect . arrayContaining ( [ "nofile=1024:2048" , "nproc=128" , "core=0" ] ) ,
137
- ) ;
95
+ expect ( args [ 0 ] ) . toBe ( "create" ) ;
96
+ expectFlagValues ( args , "--name" , [ "openclaw-sbx-test" ] ) ;
97
+ expectFlagValues ( args , "--label" , [
98
+ "openclaw.sandbox=1" ,
99
+ "openclaw.sessionKey=main" ,
100
+ "openclaw.createdAtMs=1700000000000" ,
101
+ "openclaw.sandboxBrowser=1" ,
102
+ ] ) ;
103
+ expect ( args ) . toContain ( "--read-only" ) ;
104
+ expectFlagValues ( args , "--tmpfs" , [ "/tmp" ] ) ;
105
+ expectFlagValues ( args , "--network" , [ "none" ] ) ;
106
+ expectFlagValues ( args , "--user" , [ "1000:1000" ] ) ;
107
+ expectFlagValues ( args , "--cap-drop" , [ "ALL" ] ) ;
108
+ expectFlagValues ( args , "--security-opt" , [
109
+ "no-new-privileges" ,
110
+ "seccomp=/tmp/seccomp.json" ,
111
+ "apparmor=openclaw-sandbox" ,
112
+ ] ) ;
113
+ expectFlagValues ( args , "--dns" , [ "1.1.1.1" ] ) ;
114
+ expectFlagValues ( args , "--add-host" , [ "internal.service:10.0.0.5" ] ) ;
115
+ expectFlagValues ( args , "--pids-limit" , [ "256" ] ) ;
116
+ expectFlagValues ( args , "--memory" , [ "512m" ] ) ;
117
+ expectFlagValues ( args , "--memory-swap" , [ "1024" ] ) ;
118
+ expectFlagValues ( args , "--cpus" , [ "1.5" ] ) ;
119
+ expectFlagValues ( args , "--env" , [ "LANG=C.UTF-8" , `OPENCLAW_CLI=${ OPENCLAW_CLI_ENV_VALUE } ` ] ) ;
120
+ expectFlagValues ( args , "--ulimit" , [ "nofile=1024:2048" , "nproc=128" , "core=0" ] ) ;
138
121
} ) ;
139
122
140
123
it ( "preserves the OpenClaw exec marker when strict env sanitization is enabled" , ( ) => {
@@ -154,14 +137,7 @@ describe("buildSandboxCreateArgs", () => {
154
137
} ,
155
138
} ) ;
156
139
157
- expect ( args ) . toEqual (
158
- expect . arrayContaining ( [
159
- "--env" ,
160
- "NODE_ENV=test" ,
161
- "--env" ,
162
- `OPENCLAW_CLI=${ OPENCLAW_CLI_ENV_VALUE } ` ,
163
- ] ) ,
164
- ) ;
140
+ expectFlagValues ( args , "--env" , [ "NODE_ENV=test" , `OPENCLAW_CLI=${ OPENCLAW_CLI_ENV_VALUE } ` ] ) ;
165
141
} ) ;
166
142
167
143
it ( "emits Docker GPU passthrough as a separate argument" , ( ) => {
@@ -176,7 +152,7 @@ describe("buildSandboxCreateArgs", () => {
176
152
createdAtMs : 1700000000000 ,
177
153
} ) ;
178
154
179
- expect ( args ) . toEqual ( expect . arrayContaining ( [ "--gpus" , "device=GPU-123" ] ) ) ;
155
+ expectFlagValues ( args , "--gpus" , [ "device=GPU-123" ] ) ;
180
156
} ) ;
181
157
182
158
it ( "emits -v flags for safe custom binds" , ( ) => {
@@ -308,7 +284,7 @@ describe("buildSandboxCreateArgs", () => {
308
284
bindSourceRoots : [ "/tmp/workspace" , "/tmp/agent" ] ,
309
285
allowSourcesOutsideAllowedRoots : true ,
310
286
} ) ;
311
- expect ( args ) . toEqual ( expect . arrayContaining ( [ "-v" , "/opt/external:/data:rw" ] ) ) ;
287
+ expectFlagValues ( args , "-v" , [ "/opt/external:/data:rw" ] ) ;
312
288
} ) ;
313
289
314
290
it ( "blocks reserved /workspace target bind mounts by default" , ( ) => {
@@ -325,7 +301,7 @@ describe("buildSandboxCreateArgs", () => {
325
301
createdAtMs : 1700000000000 ,
326
302
allowReservedContainerTargets : true ,
327
303
} ) ;
328
- expect ( args ) . toEqual ( expect . arrayContaining ( [ "-v" , "/tmp/override:/workspace:rw" ] ) ) ;
304
+ expectFlagValues ( args , "-v" , [ "/tmp/override:/workspace:rw" ] ) ;
329
305
} ) ;
330
306
331
307
it ( "allows container namespace join with explicit dangerous override" , ( ) => {
@@ -339,6 +315,6 @@ describe("buildSandboxCreateArgs", () => {
339
315
scopeKey : "main" ,
340
316
createdAtMs : 1700000000000 ,
341
317
} ) ;
342
- expect ( args ) . toEqual ( expect . arrayContaining ( [ "--network" , "container:peer" ] ) ) ;
318
+ expectFlagValues ( args , "--network" , [ "container:peer" ] ) ;
343
319
} ) ;
344
320
} ) ;
0 commit comments
```

---

## 11. test: tighten embedded subscribe assertions

- 链接: https://github.com/openclaw/openclaw/commit/5d8ce65a8e5c4ae900b20a4751fb70247782c02f

```
@@ -112,6 +112,42 @@ describe("subscribeEmbeddedPiSession", () => {
112
112
} ) ;
113
113
}
114
114
115
+ function findBlockReplyPayload (
116
+ onBlockReply : { mock : { calls : unknown [ ] [ ] } } ,
117
+ text : string ,
118
+ ) : { mediaUrls ?: unknown } | undefined {
119
+ return onBlockReply . mock . calls
120
+ . map ( ( call ) => call [ 0 ] as { text ?: unknown ; mediaUrls ?: unknown } )
121
+ . find ( ( payload ) => payload . text === text ) ;
122
+ }
123
+
124
+ function expectBlockReplyPayload (
125
+ onBlockReply : { mock : { calls : unknown [ ] [ ] } } ,
126
+ expected : { text : string ; mediaUrls ?: string [ ] } ,
127
+ ) : void {
128
+ const payload = findBlockReplyPayload ( onBlockReply , expected . text ) ;
129
+ expect ( payload ) . toBeDefined ( ) ;
130
+ if ( ! payload ) {
131
+ throw new Error ( `Expected block reply text: ${ expected . text } ` ) ;
132
+ }
133
+ if ( expected . mediaUrls !== undefined ) {
134
+ expect ( payload . mediaUrls ) . toStrictEqual ( expected . mediaUrls ) ;
135
+ }
136
+ }
137
+
138
+ function expectLifecyclePayload (
139
+ payloads : Array < Record < string , unknown > > ,
140
+ expected : { phase : string ; livenessState : string ; replayInvalid : boolean } ,
141
+ ) : void {
142
+ const payload = payloads . find (
143
+ ( item ) =>
144
+ item . phase === expected . phase &&
145
+ item . livenessState === expected . livenessState &&
146
+ item . replayInvalid === expected . replayInvalid ,
147
+ ) ;
148
+ expect ( payload ) . toBeDefined ( ) ;
149
+ }
150
+
115
151
it ( "captures usage from completions timings on done events" , ( ) => {
116
152
const { emit, subscription } = createSubscribedSessionHarness ( { runId : "run" } ) ;
117
153
@@ -362,12 +398,10 @@ describe("subscribeEmbeddedPiSession", () => {
362
398
} ) ;
363
399
await flushBlockReplyCallbacks ( ) ;
364
400
365
- expect ( onBlockReply ) . toHaveBeenCalledWith (
366
- expect . objectContaining ( {
367
- text : "Here is the image." ,
368
- mediaUrls : [ "/tmp/generated.png" ] ,
369
- } ) ,
370
- ) ;
401
+ expectBlockReplyPayload ( onBlockReply , {
402
+ text : "Here is the image." ,
403
+ mediaUrls : [ "/tmp/generated.png" ] ,
404
+ } ) ;
371
405
} ) ;
372
406
373
407
it ( "does not duplicate generated image media when the assistant reply has MEDIA lines" , async ( ) => {
@@ -417,12 +451,10 @@ describe("subscribeEmbeddedPiSession", () => {
417
451
} ) ;
418
452
await flushBlockReplyCallbacks ( ) ;
419
453
420
- expect ( onBlockReply ) . toHaveBeenCalledWith (
421
- expect . objectContaining ( {
422
- text : "Here is the selected image." ,
423
- mediaUrls : [ "./selected.png" ] ,
424
- } ) ,
425
- ) ;
454
+ expectBlockReplyPayload ( onBlockReply , {
455
+ text : "Here is the selected image." ,
456
+ mediaUrls : [ "./selected.png" ] ,
457
+ } ) ;
426
458
} ) ;
427
459
428
460
it ( "does not attach generated image media to an early streamed chunk before explicit MEDIA" , async ( ) => {
@@ -465,11 +497,9 @@ describe("subscribeEmbeddedPiSession", () => {
465
497
emit ( { type : "message_start" , message : { role : "assistant" } } ) ;
466
498
emitAssistantTextDelta ( emit , "Generated 1 image.\n" ) ;
467
499
468
- expect ( onBlockReply ) . toHaveBeenCalledWith (
469
- expect . objectContaining ( {
470
- text : "Generated 1 image." ,
471
- } ) ,
472
- ) ;
500
+ expectBlockReplyPayload ( onBlockReply , {
501
+ text : "Generated 1 image." ,
502
+ } ) ;
473
503
const earlyMediaPayloads = onBlockReply . mock . calls
474
504
. map ( ( [ payload ] ) => payload )
475
505
. filter ( ( payload ) => payload . mediaUrls ?. length ) ;
@@ -542,12 +572,10 @@ describe("subscribeEmbeddedPiSession", () => {
542
572
emit ( { type : "agent_end" } ) ;
543
573
await flushBlockReplyCallbacks ( ) ;
544
574
545
- expect ( onBlockReply ) . toHaveBeenCalledWith (
546
- expect . objectContaining ( {
547
- text : "Here it is." ,
548
- mediaUrls : [ "/tmp/lobster-boss.mp3" ] ,
549
- } ) ,
550
- ) ;
575
+ expectBlockReplyPayload ( onBlockReply , {
576
+ text : "Here it is." ,
577
+ mediaUrls : [ "/tmp/lobster-boss.mp3" ] ,
578
+ } ) ;
551
579
} ) ;
552
580
553
581
it . each ( [
@@ -610,11 +638,9 @@ describe("subscribeEmbeddedPiSession", () => {
610
638
emit ( { type : "message_start" , message : { role : "assistant" } } ) ;
611
639
emitAssistantTextDelta ( emit , firstChunk ) ;
612
640
613
- expect ( onBlockReply ) . toHaveBeenCalledWith (
614
- expect . objectContaining ( {
615
- text : firstChunk . trim ( ) ,
616
- } ) ,
617
- ) ;
641
+ expectBlockReplyPayload ( onBlockReply , {
642
+ text : firstChunk . trim ( ) ,
643
+ } ) ;
618
644
const earlyMediaPayloads = onBlockReply . mock . calls
619
645
. map ( ( [ payload ] ) => payload )
620
646
. filter ( ( payload ) => payload . mediaUrls ?. length ) ;
@@ -1031,9 +1057,10 @@ describe("subscribeEmbeddedPiSession", () => {
1031
1057
// Look for lifecycle:error event
1032
1058
const lifecycleError = findLifecycleErrorAgentEvent ( onAgentEvent . mock . calls ) ;
1033
1059
1034
- expect ( lifecycleError ) . toMatchObject ( {
1035
- data : { error : expect . stringContaining ( "API rate limit reached" ) } ,
1036
- } ) ;
1060
+ expect ( lifecycleError ) . toBeDefined ( ) ;
1061
+ const error = ( lifecycleError ?. data as { error ?: unknown } | undefined ) ?. error ;
1062
+ expect ( typeof error ) . toBe ( "string" ) ;
1063
+ expect ( error ) . toContain ( "API rate limit reached" ) ;
1037
1064
} ) ;
1038
1065
1039
1066
it ( "preserves replay-invalid lifecycle truth across compaction retries after mutating tools" , ( ) => {
@@ -1067,13 +1094,11 @@ describe("subscribeEmbeddedPiSession", () => {
1067
1094
hadPotentialSideEffects : true ,
1068
1095
} ) ;
1069
1096
const payloads = extractAgentEventPayloads ( onAgentEvent . mock . calls ) ;
1070
- expect ( payloads ) . toContainEqual (
1071
- expect . objectContaining ( {
1072
- phase : "end" ,
1073
- livenessState : "abandoned" ,
1074
- replayInvalid : true ,
1075
- } ) ,
1076
- ) ;
1097
+ expectLifecyclePayload ( payloads , {
1098
+ phase : "end" ,
1099
+ livenessState : "abandoned" ,
1100
+ replayInvalid : true ,
1101
+ } ) ;
1077
1102
} ) ;
1078
1103
1079
1104
it ( "preserves deterministic side-effect liveness across compaction retries" , ( ) => {
@@ -1099,12 +1124,10 @@ describe("subscribeEmbeddedPiSession", () => {
1099
1124
emit ( { type : "agent_end" } ) ;
1100
1125
1101
1126
const payloads = extractAgentEventPayloads ( onAgentEvent . mock . calls ) ;
1102
- expect ( payloads ) . toContainEqual (
1103
- expect . objectContaining ( {
1104
- phase : "end" ,
1105
- livenessState : "working" ,
1106
- replayInvalid : true ,
1107
- } ) ,
1108
- ) ;
1127
+ expectLifecyclePayload ( payloads , {
1128
+ phase : "end" ,
1129
+ livenessState : "working" ,
1130
+ replayInvalid : true ,
1131
+ } ) ;
1109
1132
} ) ;
1110
1133
} ) ;
0 commit comments
```

---

## 12. test: canonicalize gemini live probe model

- 链接: https://github.com/openclaw/openclaw/commit/5d451a5f3c480bd0fb92d9ea18d93228b743e9b1

```
@@ -48,10 +48,14 @@ describe("live model turn probes", () => {
48
48
49
49
it ( "builds an image probe with native image content" , ( ) => {
50
50
const context = buildLiveModelImageProbeContext ( { } ) ;
51
- expect ( context . messages [ 0 ] ?. content ) . toEqual ( [
52
- expect . objectContaining ( { type : "text" } ) ,
53
- expect . objectContaining ( { type : "image" , mimeType : "image/png" } ) ,
54
- ] ) ;
51
+ const content = context . messages [ 0 ] ?. content ;
52
+ expect ( Array . isArray ( content ) ) . toBe ( true ) ;
53
+ if ( ! Array . isArray ( content ) ) {
54
+ throw new Error ( "Expected image probe content blocks" ) ;
55
+ }
56
+ expect ( content [ 0 ] ?. type ) . toBe ( "text" ) ;
57
+ expect ( content [ 1 ] ?. type ) . toBe ( "image" ) ;
58
+ expect ( content [ 1 ] ) . toHaveProperty ( "mimeType" , "image/png" ) ;
55
59
} ) ;
56
60
57
61
it ( "extracts assistant text blocks only" , ( ) => {
@@ -88,7 +92,7 @@ describe("live model turn probes", () => {
88
92
89
93
it ( "skips known stale file probe routes" , ( ) => {
90
94
expect ( shouldSkipLiveModelFileProbe ( { provider : "opencode-go" , id : "glm-5" } ) ) . toBe ( true ) ;
91
- expect ( shouldSkipLiveModelFileProbe ( { provider : "google" , id : "gemini-3-pro-preview" } ) ) . toBe (
95
+ expect ( shouldSkipLiveModelFileProbe ( { provider : "google" , id : "gemini-3.1 -pro-preview" } ) ) . toBe (
92
96
true ,
93
97
) ;
94
98
expect ( shouldSkipLiveModelFileProbe ( { provider : "opencode-go" , id : "mimo-v2-omni" } ) ) . toBe (
0 commit comments
```

---

## 13. test: tighten plugin context assertions

- 链接: https://github.com/openclaw/openclaw/commit/cb86388cec1993f725c19f00a1a5052c929dbfd2

```
@@ -14,12 +14,8 @@ describe("openclaw plugin tool context", () => {
14
14
} ,
15
15
} ) ;
16
16
17
- expect ( result . context ) . toEqual (
18
- expect . objectContaining ( {
19
- requesterSenderId : "trusted-sender" ,
20
- senderIsOwner : true ,
21
- } ) ,
22
- ) ;
17
+ expect ( result . context . requesterSenderId ) . toBe ( "trusted-sender" ) ;
18
+ expect ( result . context . senderIsOwner ) . toBe ( true ) ;
23
19
} ) ;
24
20
25
21
it ( "forwards fs policy for plugin tool sandbox enforcement" , ( ) => {
@@ -30,11 +26,7 @@ describe("openclaw plugin tool context", () => {
30
26
} ,
31
27
} ) ;
32
28
33
- expect ( result . context ) . toEqual (
34
- expect . objectContaining ( {
35
- fsPolicy : { workspaceOnly : true } ,
36
- } ) ,
37
- ) ;
29
+ expect ( result . context . fsPolicy ) . toStrictEqual ( { workspaceOnly : true } ) ;
38
30
} ) ;
39
31
40
32
it ( "forwards ephemeral sessionId" , ( ) => {
@@ -46,12 +38,8 @@ describe("openclaw plugin tool context", () => {
46
38
} ,
47
39
} ) ;
48
40
49
- expect ( result . context ) . toEqual (
50
- expect . objectContaining ( {
51
- sessionKey : "agent:main:telegram:direct:12345" ,
52
- sessionId : "a1b2c3d4-e5f6-7890-abcd-ef1234567890" ,
53
- } ) ,
54
- ) ;
41
+ expect ( result . context . sessionKey ) . toBe ( "agent:main:telegram:direct:12345" ) ;
42
+ expect ( result . context . sessionId ) . toBe ( "a1b2c3d4-e5f6-7890-abcd-ef1234567890" ) ;
55
43
} ) ;
56
44
57
45
it ( "infers the default agent workspace when workspaceDir is omitted" , ( ) => {
@@ -74,12 +62,8 @@ describe("openclaw plugin tool context", () => {
74
62
} as never ,
75
63
} ) ;
76
64
77
- expect ( result . context ) . toEqual (
78
- expect . objectContaining ( {
79
- agentId : "main" ,
80
- workspaceDir,
81
- } ) ,
82
- ) ;
65
+ expect ( result . context . agentId ) . toBe ( "main" ) ;
66
+ expect ( result . context . workspaceDir ) . toBe ( workspaceDir ) ;
83
67
} ) ;
84
68
85
69
it ( "infers the session agent workspace when workspaceDir is omitted" , ( ) => {
@@ -101,12 +85,8 @@ describe("openclaw plugin tool context", () => {
101
85
resolvedConfig : config ,
102
86
} ) ;
103
87
104
- expect ( result . context ) . toEqual (
105
- expect . objectContaining ( {
106
- agentId : "support" ,
107
- workspaceDir : supportWorkspace ,
108
- } ) ,
109
- ) ;
88
+ expect ( result . context . agentId ) . toBe ( "support" ) ;
89
+ expect ( result . context . workspaceDir ) . toBe ( supportWorkspace ) ;
110
90
} ) ;
111
91
112
92
it ( "uses requester agent override for synthetic embedded session keys" , ( ) => {
@@ -129,12 +109,8 @@ describe("openclaw plugin tool context", () => {
129
109
resolvedConfig : config ,
130
110
} ) ;
131
111
132
- expect ( result . context ) . toEqual (
133
- expect . objectContaining ( {
134
- agentId : "recall" ,
135
- workspaceDir : recallWorkspace ,
136
- } ) ,
137
- ) ;
112
+ expect ( result . context . agentId ) . toBe ( "recall" ) ;
113
+ expect ( result . context . workspaceDir ) . toBe ( recallWorkspace ) ;
138
114
} ) ;
139
115
140
116
it ( "forwards browser session wiring" , ( ) => {
@@ -146,14 +122,10 @@ describe("openclaw plugin tool context", () => {
146
122
} ,
147
123
} ) ;
148
124
149
- expect ( result . context ) . toEqual (
150
- expect . objectContaining ( {
151
- browser : {
152
- sandboxBridgeUrl : "http://127.0.0.1:9999" ,
153
- allowHostControl : true ,
154
- } ,
155
- } ) ,
156
- ) ;
125
+ expect ( result . context . browser ) . toStrictEqual ( {
126
+ sandboxBridgeUrl : "http://127.0.0.1:9999" ,
127
+ allowHostControl : true ,
128
+ } ) ;
157
129
} ) ;
158
130
159
131
it ( "forwards gateway subagent binding" , ( ) => {
@@ -178,16 +150,12 @@ describe("openclaw plugin tool context", () => {
178
150
} ,
179
151
} ) ;
180
152
181
- expect ( result . context ) . toEqual (
182
- expect . objectContaining ( {
183
- deliveryContext : {
184
- channel : "slack" ,
185
- to : "channel:C123" ,
186
- accountId : "work" ,
187
- threadId : "1710000000.000100" ,
188
- } ,
189
- } ) ,
190
- ) ;
153
+ expect ( result . context . deliveryContext ) . toStrictEqual ( {
154
+ channel : "slack" ,
155
+ to : "channel:C123" ,
156
+ accountId : "work" ,
157
+ threadId : "1710000000.000100" ,
158
+ } ) ;
191
159
} ) ;
192
160
193
161
it ( "does not inject ambient thread defaults into plugin tools" , async ( ) => {
0 commit comments
```

---

## 14. test: tighten model auth assertions

- 链接: https://github.com/openclaw/openclaw/commit/59b88e4f018a12ddbf629a2abe213a1bee46511c

```
@@ -227,6 +227,21 @@ async function resolveCustomProviderAuth(
227
227
} ) ;
228
228
}
229
229
230
+ function expectAuthFields (
231
+ auth : Awaited < ReturnType < typeof resolveApiKeyForProvider > > ,
232
+ expected : {
233
+ apiKey : string ;
234
+ mode : "api-key" | "oauth" ;
235
+ source ?: string ;
236
+ } ,
237
+ ) {
238
+ expect ( auth . apiKey ) . toBe ( expected . apiKey ) ;
239
+ expect ( auth . mode ) . toBe ( expected . mode ) ;
240
+ if ( expected . source !== undefined ) {
241
+ expect ( auth . source ) . toBe ( expected . source ) ;
242
+ }
243
+ }
244
+
230
245
describe ( "resolveAwsSdkEnvVarName" , ( ) => {
231
246
it ( "prefers bearer token over access keys and profile" , ( ) => {
232
247
const env = {
@@ -735,7 +750,7 @@ describe("resolveApiKeyForProvider", () => {
735
750
} ) ,
736
751
) ;
737
752
738
- expect ( resolved ) . toMatchObject ( {
753
+ expectAuthFields ( resolved , {
739
754
apiKey : "plugin-web-fallback-key" ,
740
755
source : "plugins.entries.plugin-web.config.webSearch.apiKey" ,
741
756
mode : "api-key" ,
@@ -779,7 +794,7 @@ describe("resolveApiKeyForProvider", () => {
779
794
} ) ,
780
795
) ;
781
796
782
- expect ( resolved ) . toMatchObject ( {
797
+ expectAuthFields ( resolved , {
783
798
apiKey : "plugin-web-runtime-key" ,
784
799
source : "plugins.entries.plugin-web.config.webSearch.apiKey" ,
785
800
mode : "api-key" ,
@@ -861,7 +876,7 @@ describe("resolveApiKeyForProvider", () => {
861
876
} ,
862
877
} ) ;
863
878
864
- expect ( resolved ) . toMatchObject ( {
879
+ expectAuthFields ( resolved , {
865
880
apiKey : "sk-config-live" ,
866
881
source : "models.json" ,
867
882
mode : "api-key" ,
@@ -885,7 +900,7 @@ describe("resolveApiKeyForProvider", () => {
885
900
} ) ,
886
901
) ;
887
902
888
- expect ( resolved ) . toMatchObject ( {
903
+ expectAuthFields ( resolved , {
889
904
apiKey : "ollama-local" ,
890
905
mode : "api-key" ,
891
906
} ) ;
@@ -1002,7 +1017,7 @@ describe("resolveApiKeyForProvider – synthetic local auth for custom providers
1002
1017
store : { version : 1 , profiles : { } } ,
1003
1018
} ) ;
1004
1019
1005
- expect ( auth ) . toMatchObject ( {
1020
+ expectAuthFields ( auth , {
1006
1021
apiKey : "ollama-local" ,
1007
1022
source : "models.json (local marker)" ,
1008
1023
mode : "api-key" ,
@@ -1036,7 +1051,7 @@ describe("resolveApiKeyForProvider – synthetic local auth for custom providers
1036
1051
store : { version : 1 , profiles : { } } ,
1037
1052
} ) ;
1038
1053
1039
- expect ( auth ) . toMatchObject ( {
1054
+ expectAuthFields ( auth , {
1040
1055
apiKey : "ollama-local" ,
1041
1056
source : "models.providers.ollama-gpu1 (synthetic local key)" ,
1042
1057
mode : "api-key" ,
@@ -1071,7 +1086,7 @@ describe("resolveApiKeyForProvider – synthetic local auth for custom providers
1071
1086
store : { version : 1 , profiles : { } } ,
1072
1087
} ) ;
1073
1088
1074
- expect ( auth ) . toMatchObject ( {
1089
+ expectAuthFields ( auth , {
1075
1090
apiKey : CUSTOM_LOCAL_AUTH_MARKER ,
1076
1091
source : "models.json (local marker)" ,
1077
1092
mode : "api-key" ,
@@ -1226,10 +1241,8 @@ describe("applyLocalNoAuthHeaderOverride", () => {
1226
1241
} ,
1227
1242
) ;
1228
1243
1229
- expect ( model . headers ) . toMatchObject ( {
1230
- Authorization : null ,
1231
- "X-Test" : "1" ,
1232
- } ) ;
1244
+ expect ( model . headers ?. Authorization ) . toBeNull ( ) ;
1245
+ expect ( model . headers ?. [ "X-Test" ] ) . toBe ( "1" ) ;
1233
1246
} ) ;
1234
1247
} ) ;
1235
1248
0 commit comments
```

---

## 15. test: tighten external cli auth assertions

- 链接: https://github.com/openclaw/openclaw/commit/9931cafe705f13a525131ef348c3864bf147af75

```
@@ -43,6 +43,36 @@ function makeStore(profileId?: string, credential?: OAuthCredential): AuthProfil
43
43
} ;
44
44
}
45
45
46
+ function expectSingleProfileCredential (
47
+ profiles : ReturnType < typeof resolveExternalCliAuthProfiles > ,
48
+ profileId : string ,
49
+ ) {
50
+ expect ( profiles ) . toHaveLength ( 1 ) ;
51
+ expect ( profiles [ 0 ] ?. profileId ) . toBe ( profileId ) ;
52
+ expect ( profiles [ 0 ] ?. credential ) . toBeTruthy ( ) ;
53
+ return profiles [ 0 ] ?. credential as Record < string , unknown > ;
54
+ }
55
+
56
+ function expectCredentialFields (
57
+ credential : Record < string , unknown > | undefined ,
58
+ expected : Record < string , unknown > ,
59
+ ) {
60
+ expect ( credential ) . toBeTruthy ( ) ;
61
+ for ( const [ key , value ] of Object . entries ( expected ) ) {
62
+ expect ( credential ?. [ key ] ) . toBe ( value ) ;
63
+ }
64
+ }
65
+
66
+ function expectReaderPolicyCall ( mock : { mock : { calls : unknown [ ] [ ] } } ) {
67
+ expect ( mock . mock . calls ) . toHaveLength ( 1 ) ;
68
+ const [ arg ] = mock . mock . calls [ 0 ] ?? [ ] ;
69
+ expect ( arg ) . toBeTruthy ( ) ;
70
+ if ( ! arg || typeof arg !== "object" ) {
71
+ throw new Error ( "Expected CLI reader options" ) ;
72
+ }
73
+ expect ( ( arg as { allowKeychainPrompt ?: unknown } ) . allowKeychainPrompt ) . toBe ( false ) ;
74
+ }
75
+
46
76
describe ( "external cli oauth resolution" , ( ) => {
47
77
beforeEach ( async ( ) => {
48
78
vi . resetModules ( ) ;
@@ -258,17 +288,15 @@ describe("external cli oauth resolution", () => {
258
288
providerIds : [ "openai-codex" ] ,
259
289
} ) ;
260
290
261
- expect ( profiles ) . toEqual ( [
291
+ expectCredentialFields (
292
+ expectSingleProfileCredential ( profiles , OPENAI_CODEX_DEFAULT_PROFILE_ID ) ,
262
293
{
263
- profileId : OPENAI_CODEX_DEFAULT_PROFILE_ID ,
264
- credential : expect . objectContaining ( {
265
- provider : "openai-codex" ,
266
- access : "codex-cli-access" ,
267
- refresh : "codex-cli-refresh" ,
268
- accountId : "acct-codex" ,
269
- } ) ,
294
+ provider : "openai-codex" ,
295
+ access : "codex-cli-access" ,
296
+ refresh : "codex-cli-refresh" ,
297
+ accountId : "acct-codex" ,
270
298
} ,
271
- ] ) ;
299
+ ) ;
272
300
} ) ;
273
301
274
302
it ( "keeps any existing default codex oauth over Codex CLI bootstrap credentials" , ( ) => {
@@ -324,17 +352,12 @@ describe("external cli oauth resolution", () => {
324
352
providerIds : [ "claude-cli" ] ,
325
353
} ) ;
326
354
327
- expect ( profiles ) . toEqual ( [
328
- {
329
- profileId : CLAUDE_CLI_PROFILE_ID ,
330
- credential : expect . objectContaining ( {
331
- type : "oauth" ,
332
- provider : "claude-cli" ,
333
- access : "claude-cli-access" ,
334
- refresh : "claude-cli-refresh" ,
335
- } ) ,
336
- } ,
337
- ] ) ;
355
+ expectCredentialFields ( expectSingleProfileCredential ( profiles , CLAUDE_CLI_PROFILE_ID ) , {
356
+ type : "oauth" ,
357
+ provider : "claude-cli" ,
358
+ access : "claude-cli-access" ,
359
+ refresh : "claude-cli-refresh" ,
360
+ } ) ;
338
361
} ) ;
339
362
340
363
it ( "skips external cli readers outside the scoped provider set" , ( ) => {
@@ -382,15 +405,10 @@ describe("external cli oauth resolution", () => {
382
405
} ) ,
383
406
) ;
384
407
385
- expect ( profiles ) . toEqual ( [
386
- {
387
- profileId : CLAUDE_CLI_PROFILE_ID ,
388
- credential : expect . objectContaining ( {
389
- provider : "claude-cli" ,
390
- access : "claude-cli-fresh-access" ,
391
- } ) ,
392
- } ,
393
- ] ) ;
408
+ expectCredentialFields ( expectSingleProfileCredential ( profiles , CLAUDE_CLI_PROFILE_ID ) , {
409
+ provider : "claude-cli" ,
410
+ access : "claude-cli-fresh-access" ,
411
+ } ) ;
394
412
} ) ;
395
413
396
414
it ( "passes non-prompting keychain policy to scoped Claude CLI credential reads" , ( ) => {
@@ -407,18 +425,11 @@ describe("external cli oauth resolution", () => {
407
425
allowKeychainPrompt : false ,
408
426
} ) ;
409
427
410
- expect ( profiles ) . toEqual ( [
411
- {
412
- profileId : CLAUDE_CLI_PROFILE_ID ,
413
- credential : expect . objectContaining ( {
414
- type : "oauth" ,
415
- provider : "claude-cli" ,
416
- } ) ,
417
- } ,
418
- ] ) ;
419
- expect ( mocks . readClaudeCliCredentialsCached ) . toHaveBeenCalledWith (
420
- expect . objectContaining ( { allowKeychainPrompt : false } ) ,
421
- ) ;
428
+ expectCredentialFields ( expectSingleProfileCredential ( profiles , CLAUDE_CLI_PROFILE_ID ) , {
429
+ type : "oauth" ,
430
+ provider : "claude-cli" ,
431
+ } ) ;
432
+ expectReaderPolicyCall ( mocks . readClaudeCliCredentialsCached ) ;
422
433
expect ( mocks . readCodexCliCredentialsCached ) . not . toHaveBeenCalled ( ) ;
423
434
expect ( mocks . readMiniMaxCliCredentialsCached ) . not . toHaveBeenCalled ( ) ;
424
435
} ) ;
@@ -437,18 +448,14 @@ describe("external cli oauth resolution", () => {
437
448
allowKeychainPrompt : false ,
438
449
} ) ;
439
450
440
- expect ( profiles ) . toEqual ( [
451
+ expectCredentialFields (
452
+ expectSingleProfileCredential ( profiles , OPENAI_CODEX_DEFAULT_PROFILE_ID ) ,
441
453
{
442
- profileId : OPENAI_CODEX_DEFAULT_PROFILE_ID ,
443
- credential : expect . objectContaining ( {
444
- type : "oauth" ,
445
- provider : "openai-codex" ,
446
- } ) ,
454
+ type : "oauth" ,
455
+ provider : "openai-codex" ,
447
456
} ,
448
- ] ) ;
449
- expect ( mocks . readCodexCliCredentialsCached ) . toHaveBeenCalledWith (
450
- expect . objectContaining ( { allowKeychainPrompt : false } ) ,
451
457
) ;
458
+ expectReaderPolicyCall ( mocks . readCodexCliCredentialsCached ) ;
452
459
expect ( mocks . readClaudeCliCredentialsCached ) . not . toHaveBeenCalled ( ) ;
453
460
expect ( mocks . readMiniMaxCliCredentialsCached ) . not . toHaveBeenCalled ( ) ;
454
461
} ) ;
@@ -495,7 +502,7 @@ describe("external cli oauth resolution", () => {
495
502
const profilesById = new Map (
496
503
profiles . map ( ( profile ) => [ profile . profileId , profile . credential ] ) ,
497
504
) ;
498
- expect ( profilesById . get ( MINIMAX_CLI_PROFILE_ID ) ) . toMatchObject ( {
505
+ expectCredentialFields ( profilesById . get ( MINIMAX_CLI_PROFILE_ID ) as Record < string , unknown > , {
499
506
access : "minimax-fresh-access" ,
500
507
refresh : "minimax-fresh-refresh" ,
501
508
} ) ;
0 commit comments
```

---

## 16. test: tighten music background assertions

- 链接: https://github.com/openclaw/openclaw/commit/75d44714dc21225cb9a1459ce60699d200fc8467

```
@@ -21,6 +21,24 @@ const {
21
21
wakeMusicGenerationTaskCompletion,
22
22
} = await import ( "./music-generate-background.js" ) ;
23
23
24
+ function getDeliveredInternalEvents ( ) : Array < Record < string , unknown > > {
25
+ const params = announceDeliveryMocks . deliverSubagentAnnouncement . mock . calls [ 0 ] ?. [ 0 ] as
26
+ | { internalEvents ?: unknown }
27
+ | undefined ;
28
+ expect ( params ?. internalEvents ) . toBeTruthy ( ) ;
29
+ if ( ! Array . isArray ( params ?. internalEvents ) ) {
30
+ throw new Error ( "Expected delivered internal events" ) ;
31
+ }
32
+ return params . internalEvents as Array < Record < string , unknown > > ;
33
+ }
34
+
35
+ function expectReplyInstructionContains ( text : string ) {
36
+ const event = getDeliveredInternalEvents ( ) . find (
37
+ ( item ) => typeof item . replyInstruction === "string" && item . replyInstruction . includes ( text ) ,
38
+ ) ;
39
+ expect ( event ) . toBeDefined ( ) ;
40
+ }
41
+
24
42
describe ( "music generate background helpers" , ( ) => {
25
43
beforeEach ( ( ) => {
26
44
resetMediaBackgroundMocks ( {
@@ -45,11 +63,13 @@ describe("music generate background helpers", () => {
45
63
providerId : "google" ,
46
64
} ) ;
47
65
48
- expect ( handle ) . toMatchObject ( {
49
- taskId : "task-123" ,
50
- requesterSessionKey : "agent:main:discord:direct:123" ,
51
- taskLabel : "night-drive synthwave" ,
52
- } ) ;
66
+ expect ( handle ) . not . toBeNull ( ) ;
67
+ if ( ! handle ) {
68
+ throw new Error ( "Expected music generation task handle" ) ;
69
+ }
70
+ expect ( handle . taskId ) . toBe ( "task-123" ) ;
71
+ expect ( handle . requesterSessionKey ) . toBe ( "agent:main:discord:direct:123" ) ;
72
+ expect ( handle . taskLabel ) . toBe ( "night-drive synthwave" ) ;
53
73
expectQueuedTaskRun ( {
54
74
taskExecutorMocks,
55
75
taskKind : MUSIC_GENERATION_TASK_KIND ,
@@ -115,28 +135,8 @@ describe("music generate background helpers", () => {
115
135
} ,
116
136
} ) ;
117
137
118
- expect ( announceDeliveryMocks . deliverSubagentAnnouncement ) . toHaveBeenCalledWith (
119
- expect . objectContaining ( {
120
- internalEvents : expect . arrayContaining ( [
121
- expect . objectContaining ( {
122
- replyInstruction : expect . stringContaining (
123
- "the user will NOT see your normal assistant final reply" ,
124
- ) ,
125
- } ) ,
126
- ] ) ,
127
- } ) ,
128
- ) ;
129
- expect ( announceDeliveryMocks . deliverSubagentAnnouncement ) . toHaveBeenCalledWith (
130
- expect . objectContaining ( {
131
- internalEvents : expect . arrayContaining ( [
132
- expect . objectContaining ( {
133
- replyInstruction : expect . stringContaining (
134
- "Do not put MEDIA: lines only in your final answer" ,
135
- ) ,
136
- } ) ,
137
- ] ) ,
138
- } ) ,
139
- ) ;
138
+ expectReplyInstructionContains ( "the user will NOT see your normal assistant final reply" ) ;
139
+ expectReplyInstructionContains ( "Do not put MEDIA: lines only in your final answer" ) ;
140
140
} ) ;
141
141
142
142
it ( "queues a completion event when direct send is enabled globally" , async ( ) => {
0 commit comments
```

---

## 17. test: tighten message tool assertions

- 链接: https://github.com/openclaw/openclaw/commit/bafe49f0620d9ddc76e45448646c755563a472ad

```
@@ -237,6 +237,23 @@ function getActionEnum(properties: Record<string, unknown>) {
237
237
return ( properties . action as { enum ?: string [ ] } | undefined ) ?. enum ?? [ ] ;
238
238
}
239
239
240
+ function expectStringSchema (
241
+ schema : unknown ,
242
+ expected ?: {
243
+ descriptionIncludes ?: string ;
244
+ } ,
245
+ ) {
246
+ expect ( schema ) . toBeTruthy ( ) ;
247
+ if ( ! schema || typeof schema !== "object" ) {
248
+ throw new Error ( "Expected string schema" ) ;
249
+ }
250
+ const record = schema as Record < string , unknown > ;
251
+ expect ( record . type ) . toBe ( "string" ) ;
252
+ if ( expected ?. descriptionIncludes ) {
253
+ expect ( record . description ) . toEqual ( expect . stringContaining ( expected . descriptionIncludes ) ) ;
254
+ }
255
+ }
256
+
240
257
beforeAll ( async ( ) => {
241
258
( { resetPluginRuntimeStateForTest, setActivePluginRegistry } =
242
259
await import ( "../../plugins/runtime.js" ) ) ;
@@ -641,14 +658,10 @@ describe("message tool Telegram topic targets", () => {
641
658
} ,
642
659
} ) ;
643
660
644
- expect ( call ?. params ) . toEqual (
645
- expect . objectContaining ( {
646
- channel : "telegram" ,
647
- target : "-1001234567890:topic:42" ,
648
- threadId : "42" ,
649
- message : "topic hello" ,
650
- } ) ,
651
- ) ;
661
+ expect ( call ?. params ?. channel ) . toBe ( "telegram" ) ;
662
+ expect ( call ?. params ?. target ) . toBe ( "-1001234567890:topic:42" ) ;
663
+ expect ( call ?. params ?. threadId ) . toBe ( "42" ) ;
664
+ expect ( call ?. params ?. message ) . toBe ( "topic hello" ) ;
652
665
} ) ;
653
666
} ) ;
654
667
@@ -920,19 +933,17 @@ describe("message tool schema scoping", () => {
920
933
requesterSenderId : "user-42" ,
921
934
} ) ;
922
935
923
- expect ( seenContexts ) . toContainEqual (
924
- expect . objectContaining ( {
925
- currentChannelProvider : "discord" ,
926
- currentChannelId : "channel:123" ,
927
- currentThreadTs : "thread-456" ,
928
- currentMessageId : "msg-789" ,
929
- accountId : "ops" ,
930
- sessionKey : "agent:alpha:main" ,
931
- sessionId : "session-123" ,
932
- agentId : "alpha" ,
933
- requesterSenderId : "user-42" ,
934
- } ) ,
935
- ) ;
936
+ const context = seenContexts . find ( ( item ) => item . phase === "describeMessageTool" ) ;
937
+ expect ( context ) . toBeDefined ( ) ;
938
+ expect ( context ?. currentChannelProvider ) . toBe ( "discord" ) ;
939
+ expect ( context ?. currentChannelId ) . toBe ( "channel:123" ) ;
940
+ expect ( context ?. currentThreadTs ) . toBe ( "thread-456" ) ;
941
+ expect ( context ?. currentMessageId ) . toBe ( "msg-789" ) ;
942
+ expect ( context ?. accountId ) . toBe ( "ops" ) ;
943
+ expect ( context ?. sessionKey ) . toBe ( "agent:alpha:main" ) ;
944
+ expect ( context ?. sessionId ) . toBe ( "session-123" ) ;
945
+ expect ( context ?. agentId ) . toBe ( "alpha" ) ;
946
+ expect ( context ?. requesterSenderId ) . toBe ( "user-42" ) ;
936
947
} ) ;
937
948
938
949
it ( "forwards senderIsOwner into plugin action discovery" , ( ) => {
@@ -967,18 +978,18 @@ describe("message tool schema scoping", () => {
967
978
968
979
expect ( getActionEnum ( getToolProperties ( ownerTool ) ) ) . toContain ( "set-profile" ) ;
969
980
expect ( getActionEnum ( getToolProperties ( nonOwnerTool ) ) ) . not . toContain ( "set-profile" ) ;
970
- expect ( seenContexts ) . toContainEqual ( expect . objectContaining ( { senderIsOwner : true } ) ) ;
971
- expect ( seenContexts ) . toContainEqual ( expect . objectContaining ( { senderIsOwner : false } ) ) ;
981
+ expect ( seenContexts . some ( ( context ) => context . senderIsOwner === true ) ) . toBe ( true ) ;
982
+ expect ( seenContexts . some ( ( context ) => context . senderIsOwner === false ) ) . toBe ( true ) ;
972
983
} ) ;
973
984
974
985
it ( "keeps core send and broadcast actions in unscoped schemas" , ( ) => {
975
986
const tool = createMessageTool ( {
976
987
config : { } as never ,
977
988
} ) ;
978
989
979
- expect ( getActionEnum ( getToolProperties ( tool ) ) ) . toEqual (
980
- expect . arrayContaining ( [ "send" , "broadcast" ] ) ,
981
- ) ;
990
+ const actionEnum = getActionEnum ( getToolProperties ( tool ) ) ;
991
+ expect ( actionEnum ) . toContain ( "send" ) ;
992
+ expect ( actionEnum ) . toContain ( "broadcast" ) ;
982
993
} ) ;
983
994
984
995
it ( "advertises Slack download-file fileId in scoped schemas" , ( ) => {
@@ -1001,7 +1012,7 @@ describe("message tool schema scoping", () => {
1001
1012
const properties = getToolProperties ( tool ) ;
1002
1013
1003
1014
expect ( getActionEnum ( properties ) ) . toContain ( "download-file" ) ;
1004
- expect ( properties . fileId ) . toMatchObject ( { type : "string" } ) ;
1015
+ expectStringSchema ( properties . fileId ) ;
1005
1016
} ) ;
1006
1017
1007
1018
it ( "advertises messageId for read actions" , ( ) => {
@@ -1024,10 +1035,7 @@ describe("message tool schema scoping", () => {
1024
1035
const properties = getToolProperties ( tool ) ;
1025
1036
1026
1037
expect ( getActionEnum ( properties ) ) . toContain ( "read" ) ;
1027
- expect ( properties . messageId ) . toMatchObject ( {
1028
- type : "string" ,
1029
- description : expect . stringContaining ( "read" ) ,
1030
- } ) ;
1038
+ expectStringSchema ( properties . messageId , { descriptionIncludes : "read" } ) ;
1031
1039
} ) ;
1032
1040
} ) ;
1033
1041
0 commit comments
```

---

## 18. test: tighten subagent announce assertions

- 链接: https://github.com/openclaw/openclaw/commit/7f59a5e1287b8cce6bb997f5faffc5d59c55b5c2

```
@@ -69,6 +69,50 @@ function visibleAgentResponse(runId = "run-main") {
69
69
} ;
70
70
}
71
71
72
+ function expectInputProvenance (
73
+ params : Record < string , unknown > | undefined ,
74
+ sourceSessionKey : string ,
75
+ ) {
76
+ const inputProvenance = params ?. inputProvenance ;
77
+ expect ( inputProvenance ) . toBeTruthy ( ) ;
78
+ if ( ! inputProvenance || typeof inputProvenance !== "object" ) {
79
+ throw new Error ( "Expected input provenance" ) ;
80
+ }
81
+ const provenance = inputProvenance as Record < string , unknown > ;
82
+ expect ( provenance . kind ) . toBe ( "inter_session" ) ;
83
+ expect ( provenance . sourceSessionKey ) . toBe ( sourceSessionKey ) ;
84
+ expect ( provenance . sourceTool ) . toBe ( "subagent_announce" ) ;
85
+ }
86
+
87
+ function getAgentCall ( index = 0 ) : AgentCallRequest {
88
+ const call = agentSpy . mock . calls [ index ] ?. [ 0 ] ;
89
+ expect ( call ) . toBeDefined ( ) ;
90
+ if ( ! call ) {
91
+ throw new Error ( `Expected agent call at index ${ index } ` ) ;
92
+ }
93
+ return call ;
94
+ }
95
+
96
+ function expectAgentCallFields (
97
+ call : AgentCallRequest ,
98
+ expected : {
99
+ channel ?: string ;
100
+ deliver ?: boolean ;
101
+ sessionKey : string ;
102
+ to ?: string ;
103
+ } ,
104
+ ) {
105
+ expect ( call . method ) . toBe ( "agent" ) ;
106
+ expect ( call . params ?. sessionKey ) . toBe ( expected . sessionKey ) ;
107
+ expect ( call . params ?. deliver ) . toBe ( expected . deliver ) ;
108
+ if ( "channel" in expected ) {
109
+ expect ( call . params ?. channel ) . toBe ( expected . channel ) ;
110
+ }
111
+ if ( "to" in expected ) {
112
+ expect ( call . params ?. to ) . toBe ( expected . to ) ;
113
+ }
114
+ }
115
+
72
116
const agentSpy = vi . fn ( async ( _req : AgentCallRequest ) => visibleAgentResponse ( ) ) ;
73
117
const sendSpy = vi . fn ( async ( _req : AgentCallRequest ) => ( { runId : "send-main" , status : "ok" } ) ) ;
74
118
const sessionsDeleteSpy = vi . fn ( ( _req : AgentCallRequest ) => undefined ) ;
@@ -695,11 +739,7 @@ describe("subagent announce formatting", () => {
695
739
expect ( call ?. params ?. channel ) . toBe ( "discord" ) ;
696
740
expect ( call ?. params ?. to ) . toBe ( "channel:12345" ) ;
697
741
expect ( call ?. params ?. sessionKey ) . toBe ( "agent:main:main" ) ;
698
- expect ( call ?. params ?. inputProvenance ) . toMatchObject ( {
699
- kind : "inter_session" ,
700
- sourceSessionKey : "agent:main:subagent:test" ,
701
- sourceTool : "subagent_announce" ,
702
- } ) ;
742
+ expectInputProvenance ( call ?. params , "agent:main:subagent:test" ) ;
703
743
expect ( msg ) . toContain ( "final answer: 2" ) ;
704
744
expect ( msg ) . not . toContain ( "✅ Subagent" ) ;
705
745
} ) ;
@@ -1171,9 +1211,8 @@ describe("subagent announce formatting", () => {
1171
1211
const directTargets = agentSpy . mock . calls . map (
1172
1212
( call ) => ( call ?. [ 0 ] as { params ?: { to ?: string } } ) ?. params ?. to ,
1173
1213
) ;
1174
- expect ( directTargets ) . toEqual (
1175
- expect . arrayContaining ( [ "channel:thread-child-a" , "channel:thread-child-b" ] ) ,
1176
- ) ;
1214
+ expect ( directTargets ) . toContain ( "channel:thread-child-a" ) ;
1215
+ expect ( directTargets ) . toContain ( "channel:thread-child-b" ) ;
1177
1216
expect ( directTargets ) . not . toContain ( "channel:main-parent-channel" ) ;
1178
1217
} ) ;
1179
1218
@@ -1859,12 +1898,9 @@ describe("subagent announce formatting", () => {
1859
1898
expect ( didAnnounce ) . toBe ( true ) ;
1860
1899
expect ( sendSpy ) . toHaveBeenCalledTimes ( 0 ) ;
1861
1900
expect ( agentSpy ) . toHaveBeenCalledTimes ( 1 ) ;
1862
- expect ( agentSpy . mock . calls [ 0 ] ?. [ 0 ] ) . toMatchObject ( {
1863
- method : "agent" ,
1864
- params : {
1865
- sessionKey : "agent:main:main" ,
1866
- deliver : false ,
1867
- } ,
1901
+ expectAgentCallFields ( getAgentCall ( ) , {
1902
+ sessionKey : "agent:main:main" ,
1903
+ deliver : false ,
1868
1904
} ) ;
1869
1905
} ) ;
1870
1906
@@ -1888,14 +1924,11 @@ describe("subagent announce formatting", () => {
1888
1924
expect ( didAnnounce ) . toBe ( true ) ;
1889
1925
expect ( sendSpy ) . not . toHaveBeenCalled ( ) ;
1890
1926
expect ( agentSpy ) . toHaveBeenCalledTimes ( 1 ) ;
1891
- expect ( agentSpy . mock . calls [ 0 ] ?. [ 0 ] ) . toMatchObject ( {
1892
- method : "agent" ,
1893
- params : {
1894
- sessionKey : "agent:main:main" ,
1895
- channel : "discord" ,
1896
- to : "channel:12345" ,
1897
- deliver : true ,
1898
- } ,
1927
+ expectAgentCallFields ( getAgentCall ( ) , {
1928
+ sessionKey : "agent:main:main" ,
1929
+ channel : "discord" ,
1930
+ to : "channel:12345" ,
1931
+ deliver : true ,
1899
1932
} ) ;
1900
1933
} ) ;
1901
1934
@@ -2118,7 +2151,8 @@ describe("subagent announce formatting", () => {
2118
2151
const accountIds = agentSpy . mock . calls . map (
2119
2152
( call ) => ( call ?. [ 0 ] as { params ?: { accountId ?: string } } ) ?. params ?. accountId ,
2120
2153
) ;
2121
- expect ( accountIds ) . toEqual ( expect . arrayContaining ( [ "acct-a" , "acct-b" ] ) ) ;
2154
+ expect ( accountIds ) . toContain ( "acct-a" ) ;
2155
+ expect ( accountIds ) . toContain ( "acct-b" ) ;
2122
2156
} ) ;
2123
2157
2124
2158
it . each ( [
@@ -2206,11 +2240,7 @@ describe("subagent announce formatting", () => {
2206
2240
expect ( call ?. params ?. channel ) . toBeUndefined ( ) ;
2207
2241
expect ( call ?. params ?. to ) . toBeUndefined ( ) ;
2208
2242
expect ( ( call ?. params as { role ?: unknown } | undefined ) ?. role ) . toBeUndefined ( ) ;
2209
- expect ( call ?. params ?. inputProvenance ) . toMatchObject ( {
2210
- kind : "inter_session" ,
2211
- sourceSessionKey : "agent:main:subagent:worker" ,
2212
- sourceTool : "subagent_announce" ,
2213
- } ) ;
2243
+ expectInputProvenance ( call ?. params , "agent:main:subagent:worker" ) ;
2214
2244
} ) ;
2215
2245
2216
2246
it ( "keeps completion-mode announce internal for nested requester subagent sessions" , async ( ) => {
@@ -2234,11 +2264,7 @@ describe("subagent announce formatting", () => {
2234
2264
expect ( call ?. params ?. deliver ) . toBe ( false ) ;
2235
2265
expect ( call ?. params ?. channel ) . toBeUndefined ( ) ;
2236
2266
expect ( call ?. params ?. to ) . toBeUndefined ( ) ;
2237
- expect ( call ?. params ?. inputProvenance ) . toMatchObject ( {
2238
- kind : "inter_session" ,
2239
- sourceSessionKey : "agent:main:subagent:orchestrator:subagent:worker" ,
2240
- sourceTool : "subagent_announce" ,
2241
- } ) ;
2267
+ expectInputProvenance ( call ?. params , "agent:main:subagent:orchestrator:subagent:worker" ) ;
2242
2268
const message = typeof call ?. params ?. message === "string" ? call . params . message : "" ;
2243
2269
expect ( message ) . toContain (
2244
2270
"Convert this completion into a concise internal orchestration update for your parent agent" ,
0 commit comments
```

---

## 19. test: avoid duplicate session event wait

- 链接: https://github.com/openclaw/openclaw/commit/29661a317901216ba278ea763b0eccf41861d122

```
@@ -119,21 +119,16 @@ async function emitTranscriptUpdateAndCollectEvents(params: {
119
119
120
120
async function expectNoMessageWithin ( params : {
121
121
action ?: ( ) => Promise < void > | void ;
122
- watch : ( ) => Promise < unknown > ;
122
+ watch : ( timeoutMs : number ) => Promise < unknown > ;
123
123
timeoutMs ?: number ;
124
124
} ) : Promise < void > {
125
125
const timeoutMs = params . timeoutMs ?? 300 ;
126
- let received = false ;
127
- const watch = params
128
- . watch ( )
129
- . then ( ( ) => {
130
- received = true ;
131
- } )
132
- . catch ( ( ) => undefined ) ;
126
+ const received = params . watch ( timeoutMs ) . then (
127
+ ( ) => true ,
128
+ ( ) => false ,
129
+ ) ;
133
130
await params . action ?.( ) ;
134
- await new Promise ( ( resolve ) => setTimeout ( resolve , timeoutMs ) ) ;
135
- expect ( received ) . toBe ( false ) ;
136
- await watch ;
131
+ await expect ( received ) . resolves . toBe ( false ) ;
137
132
}
138
133
139
134
describe ( "session.message websocket events" , ( ) => {
@@ -226,19 +221,19 @@ describe("session.message websocket events", () => {
226
221
event : "session.message" ,
227
222
} ) ;
228
223
await expectNoMessageWithin ( {
229
- watch : ( ) =>
224
+ watch : ( timeoutMs ) =>
230
225
onceMessage (
231
226
unsubscribedWs ,
232
227
( message ) => message . type === "event" && message . event === "session.message" ,
233
- 300 ,
228
+ timeoutMs ,
234
229
) ,
235
230
} ) ;
236
231
await expectNoMessageWithin ( {
237
- watch : ( ) =>
232
+ watch : ( timeoutMs ) =>
238
233
onceMessage (
239
234
nodeWs ,
240
235
( message ) => message . type === "event" && message . event === "session.message" ,
241
- 300 ,
236
+ timeoutMs ,
242
237
) ,
243
238
} ) ;
244
239
} finally {
@@ -644,15 +639,15 @@ describe("session.message websocket events", () => {
644
639
expect ( mainAppend . ok ) . toBe ( true ) ;
645
640
646
641
await expectNoMessageWithin ( {
647
- watch : ( ) =>
642
+ watch : ( timeoutMs ) =>
648
643
onceMessage (
649
644
ws ,
650
645
( message ) =>
651
646
message . type === "event" &&
652
647
message . event === "session.message" &&
653
648
( message . payload as { sessionKey ?: string } | undefined ) ?. sessionKey ===
654
649
"agent:main:worker" ,
655
- 300 ,
650
+ timeoutMs ,
656
651
) ,
657
652
action : async ( ) => {
658
653
const workerAppend = await appendAssistantMessageToSessionTranscript ( {
@@ -671,15 +666,15 @@ describe("session.message websocket events", () => {
671
666
expect ( unsubscribeRes . payload ?. subscribed ) . toBe ( false ) ;
672
667
673
668
await expectNoMessageWithin ( {
674
- watch : ( ) =>
669
+ watch : ( timeoutMs ) =>
675
670
onceMessage (
676
671
ws ,
677
672
( message ) =>
678
673
message . type === "event" &&
679
674
message . event === "session.message" &&
680
675
( message . payload as { sessionKey ?: string } | undefined ) ?. sessionKey ===
681
676
"agent:main:main" ,
682
- 300 ,
677
+ timeoutMs ,
683
678
) ,
684
679
action : async ( ) => {
685
680
const hiddenAppend = await appendAssistantMessageToSessionTranscript ( {
0 commit comments
```

---

## 20. test: narrow session search registry helpers

- 链接: https://github.com/openclaw/openclaw/commit/7e3a25f5dc77f75c4ad04a8f6750bcdfabc207e5

```
We read every piece of feedback, and take your input very seriously.
To see all available qualifiers, see our documentation.
There was an error while loading. Please reload this page.
1 parent 8f84263 commit 7e3a25fCopy full SHA for 7e3a25f
1 file changed
src/gateway/session-utils.search.test.ts
@@ -5,7 +5,7 @@ import { afterEach, describe, expect, test } from "vitest";
5
import {
6
addSubagentRunForTests,
7
resetSubagentRegistryForTests,
8
-} from "../agents/subagent-registry.js";
+} from "../agents/subagent-registry.test-helpers.js";
9
import type { OpenClawConfig } from "../config/config.js";
10
import type { SessionEntry } from "../config/sessions.js";
11
import { registerAgentRunContext, resetAgentRunContextForTest } from "../infra/agent-events.js";
@@ -118,7 +118,7 @@ function listSingleSession(params: {
118
119
describe("listSessionsFromStore search", () => {
120
afterEach(() => {
121
- resetSubagentRegistryForTests({ persist: false });
+ resetSubagentRegistryForTests();
122
resetAgentRunContextForTest();
123
});
124
0 commit comments
```

---
