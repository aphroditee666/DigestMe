# Node.js Blog

> 分类: 大厂技术博客
> URL: https://nodejs.org/en/feed/blog.xml
> 抓取: 30 篇

---

## 1. Node.js 26.1.0 (Current)

- 日期: 2026-05-07 10:09
- 链接: https://nodejs.org/en/blog/release/v26.1.0

```
Node.js 26.1.0 (Current)
Antoine du Hamel
2026-05-07, Version 26.1.0 (Current), @aduh95
Notable Changes
Experimental node:ffi
module
Node.js now includes an experimental node:ffi
module for loading dynamic
libraries and calling native symbols from JavaScript.
The API is gated behind the --experimental-ffi
flag and, when the Permission
Model is enabled, requires --allow-ffi
.
This API is inherently unsafe. Invalid pointers, incorrect signatures, or accessing memory after it has been freed can crash the process or corrupt memory.
Contributed by Paolo Insogna in #62072.
Other Notable Changes
- [
34a6454fe3
] - (SEMVER-MINOR) buffer: addend
parameter (Robert Nagy) #62390 - [
073e84d7fe
] - (SEMVER-MINOR) crypto: accept key data incrypto.diffieHellman()
and cleanup DH jobs (Filip Skokan) #62527 - [
5b9cb10a5f
] - (SEMVER-MINOR) crypto: implementrandomUUIDv7()
(nabeel378) #62553 - [
98f9becd16
] - (SEMVER-MINOR) debugger: add edit-free runtime expression probes tonode inspect
(Joyee Cheung) #62713 - [
06defaa2ea
] - (SEMVER-MINOR) fs: addsignal
option tofs.stat()
(Mert Can Altin) #57775 - [
db66a963bf
] - (SEMVER-MINOR) fs: exposefrsize
field instatfs
(Jinho Jang) #62277 - [
87adb3472b
] - (SEMVER-MINOR) http: hardenClientRequest
options merge (Matteo Collina) #63082 - [
9047ec12ce
] - (SEMVER-MINOR) http: addreq.signal
toIncomingMessage
(Akshat) #62541 - [
ab66de8eaa
] - (SEMVER-MINOR) process: throw onexecve(2)
failure instead of aborting (Bryan English) #62878 - [
8273682c87
] - (SEMVER-MINOR) src: allow empty--experimental-config-file
(Marco Ippolito) #61610 - [
fbff28f7e6
] - (SEMVER-MINOR) stream: propagate destruction induplexPair
(Ahmed Elhor) #61098 - [
a8c773a0c7
] - (SEMVER-MINOR) test_runner: align mock timeout api (sangwook) #62820 - [
b883a5eaea
] - (SEMVER-MINOR) test_runner: add mock-timers support forAbortSignal.timeout
(DeveloperViraj) #60751 - [
a21ae1771e
] - (SEMVER-MINOR) test_runner: support test order randomization (Pietro Marchini) #61747 - [
b85c73ff10
] - (SEMVER-MINOR) util: colorize text with hex colors (Guilherme Araújo) #61556
Commits
- [
1b959d02c2
] - assert,util: fix stale nested cycle memo entries (Ruben Bridgewater) #62509 - [
bbeb38d210
] - buffer: fix end parameter bugs in indexOf/lastIndexOf (Robert Nagy) #62711 - [
34a6454fe3
] - (SEMVER-MINOR) buffer: add end parameter (Robert Nagy) #62390 - [
8b91526cd5
] - build: track PDL files as inputs in inspector GN build (Robo) #62888 - [
da40ed7842
] - build: remove armv6 from experimental platforms (René) #63063 - [
b36e55a23e
] - build: make test-addons dependency-free (Joyee Cheung) #62388 - [
c27f3cf8f2
] - build: add --enable-all-experimentals build flag (Paolo Insogna) #62755 - [
0d73b63a76
] - build: fix cargo check when Temporal is disabled (Antoine du Hamel) #62730 - [
d8f97e6f7b
] - build: fix ffi dependency compilation (Paolo Insogna) #62731 - [
d1eb7b340f
] - build: fix stray debug string in LIEF defines (Om Ghante) #62683 - [
845283009d
] - build: remove redundant -fuse-linker-plugin from GCC LTO flags (Daniel Lando) #62667 - [
a6e99879f4
] - build,win: enable x64 PGO (Stefan Stojanovic) #62761 - [
38befee0fb
] - crypto: add JWK support for ML-KEM and SLH-DSA key types (Filip Skokan) #62706 - [
b10653ad87
] - crypto: add guards and adjust tests for BoringSSL (Filip Skokan) #62883 - [
2a7a69c6b0
] - crypto: reject unintended raw key format string input (Filip Skokan) #62974 - [
bad1e2fe6a
] - crypto: fix unsigned conversion of 4-byte RSA publicExponent (DeepView Autofix) #62839 - [
c9d5bae598
] - crypto: remove Argon2 KDF derivation from its job setup (Filip Skokan) #62863 - [
6eea52426f
] - crypto: reject duplicate ML-KEM JWK key_ops (Filip Skokan) #62905 - [
80d4836616
] - crypto: deduplicate and canonicalize CryptoKey usages (Filip Skokan) #62902 - [
8950247027
] - crypto: reject inherited key type names (Jonathan Lopes) #62875 - [
3f42f9615a
] - crypto: strengthen argument CHECKs in TurboSHAKE (Tobias Nießen) #62763 - [
28346d999b
] - crypto: guard against size_t overflow on experimental 32-bit arch (Filip Skokan) #62626 - [
d4cec263c4
] - (SEMVER-MINOR) crypto: align key argument names in docs and error messages (Filip Skokan) #62527 - [
073e84d7fe
] - (SEMVER-MINOR) crypto: accept key data in crypto.diffieHellman() and cleanup DH jobs (Filip Skokan) #62527 - [
518b578fe7
] - crypto: add memory tracking for secureContext openssl objects (Mert Can Altin) #59051 - [
5b9cb10a5f
] - (SEMVER-MINOR) crypto: implement randomUUIDv7() (nabeel378) #62553 - [
7133826053
] - debugger: move ProbeInspectorSession and helpers to separate files (Joyee Cheung) #63013 - [
98f9becd16
] - (SEMVER-MINOR) debugger: add edit-free runtime expression probes tonode inspect
(Joyee Cheung) #62713 - [
94ac62a2d1
] - deps: update undici to 8.2.0 (Node.js GitHub Bot) #63092 - [
ef71de87e6
] - deps: update amaro to 1.1.9 (Node.js GitHub Bot) #63090 - [
c4f0ef881a
] - deps: update llhttp to 9.4.1 (Node.js GitHub Bot) #63045 - [
d29fbc0029
] - deps: fix integration issues with the latest nghttp2 (Tim Perry) #62891 - [
537825acee
] - deps: update nghttp2 to 1.69.0 (Node.js GitHub Bot) #62891 - [
4446bf694d
] - deps: update corepack to 0.34.7 (Node.js GitHub Bot) #62810 - [
8f55327f1c
] - deps: fix libffi macos build (Paolo Insogna) #63006 - [
3dee18f72f
] - deps: patch V8 to 14.6.202.34 (Node.js GitHub Bot) #62964 - [
e281b247e6
] - deps: update timezone to 2026b (Node.js GitHub Bot) #62962 - [
4dd982df13
] - deps: upgrade npm to 11.13.0 (npm team) #62898 - [
61c0ff4a13
] - deps: cherry-pick libuv/libuv@439a54b (skooch) #62881 - [
d26ca462ae
] - deps: update undici to 8.1.0 (Node.js GitHub Bot) #62728 - [
6f08489ac9
] - deps: update sqlite to 3.53.0 (Node.js GitHub Bot) #62699 - [
713601e8bd
] - deps: update nbytes to 0.1.4 (Node.js GitHub Bot) #62698 - [
578cf1c0c1
] - deps: update archs files for openssl-3.5.6 (Node.js GitHub Bot) #62629 - [
4a4ef13c67
] - deps: upgrade openssl sources to openssl-3.5.6 (Node.js GitHub Bot) #62629 - [
2f3eca8c1e
] - deps: update perfetto to 54.0 (Chengzhong Wu) #62397 - [
944ed9b739
] - deps: add perfetto build files (Chengzhong Wu) #62397 - [
15530a7484
] - deps: update ngtcp2 to 1.22.0 (Node.js GitHub Bot) #62595 - [
b813b4c4b5
] - deps: update minimatch to 10.2.5 (Node.js GitHub Bot) #62594 - [
38e7ce58c5
] - deps: update googletest to d72f9c8aea6817cdf1ca0ac10887f328de7f3da2 (Node.js GitHub Bot) #62593 - [
b5c573ed14
] - deps: update simdjson to 4.6.1 (Node.js GitHub Bot) #62592 - [
318e2c7cd3
] - deps: libuv: cherry-pick aabb7651de (Santiago Gimeno) #62561 - [
c6ccbd742a
] - deps: libuv: reapply 3a9a6e3e6b (Andy Pan) #62561 - [
4ad07de7ae
] - diagnostics_channel: add BoundedChannel and scopes (Stephen Belanger) #61680 - [
44416ea3fd
] - doc: fix documentation history missing 25.9.0 (Antoine du Hamel) #63151 - [
5f6dfbf68e
] - doc: fix changelog for chromium numbering (Rafael Gonzaga) #63133 - [
30c4b3658c
] - doc: fix the TypeScript Execute (tsx) project link (David Thornton) #63093 - [
ca3c3097f1
] - doc: minor structural stream/iter edits (René) #63089 - [
92324aab6f
] - doc: remove typo comma from man page (Vas Sudanagunta) #63080 - [
712a15da73
] - doc: correct diagnostics_channel built-in channel names (Bryan English) #62995 - [
c92cb6fe0d
] - doc: use mjs/cjs blocks for callbackify null reason example (Daijiro Wachi) #62884 - [
020776d4d6
] - doc: fix typo in test.md (Rich Trott) #62960 - [
7d52f2061e
] - doc: correct typo in PR contribution instructions (Mike McCready) #62738 - [
70e8944676
] - doc: fix duplicate word "of of" in postMessageToThread (Daijiro Wachi) #62917 - [
11c6c29284
] - doc: fix duplicate word "to to" in util.styleText (Daijiro Wachi) #62917 - [
242adab671
] - doc: fix duplicate word "for for" in compile cache (Daijiro Wachi) #62917 - [
b9f3abd63e
] - doc: fix doubled word typo in stream_iter.md (Daijiro Wachi) #62916 - [
7a52fd0448
] - doc: fix typo in dns.lookup options description (Daijiro Wachi) #62882 - [
acd7e18a8c
] - doc: fix Argon2 parameter bounds (Tobias Nießen) #62868 - [
b43ecf40bb
] - doc: trust FFI in the threat model (Paolo Insogna) #62852 - [
981ce96b03
] - doc: fix typos and inconsistencies in crypto.md and webcrypto.md (Filip Skokan) #62828 - [
acc52ef257
] - doc: clarify diffieHellman.generateKeys recomputes same key (Kit Dallege) #62205 - [
ae87597c07
] - doc: remove Ayase-252 and meixg from triagger team (Antoine du Hamel) #62841 - [
1cd3694a5f
] - doc: clarify dns.lookup() callback signature when all is true (eungi) #62800 - [
40a4337d65
] - doc: add experimental modules lifetime policy (Paolo Insogna) #62753 - [
46f48222f8
] - doc: clarify process._debugProcess() in Permission Model (Fahad Khan) #62537 - [
6eb9917497
] - doc: fix typo in devcontainer guide (Rohan Santhosh Kumar) #62687 - [
3826c5ed7e
] - doc: clarify Backport-PR-URL metadata added automatically (Mike McCready) #62668 - [
5d7e0dbbd8
] - doc: update WPT test runner README.md (Filip Skokan) #62680 - [
e9d76b2a75
] - doc: fix spelling in release announcement guidance (Rohan Santhosh Kumar) #62663 - [
1ae41cebb0
] - doc: note GCC >= 14 requirement for native riscv64 builds (Jamie Magee) #62607 - [
9b29be6a28
] - doc: note non-monotonic clock in crypto.randomUUIDv7 (nabeel378) #62600 - [
5ae59553f6
] - doc: update bug bounty program (Rafael Gonzaga) #62590 - [
ce3f4c85dd
] - doc: document TransformStream transformer.cancel option (Tom Pereira) #62566 - [
08a9ba73e4
] - doc: mention test runner retry attemp is zero based (Moshe Atlow) #62504 - [
32f2169ede
] - doc,src,test: fix dead inspector help URL (semimikoh) #62745 - [
870c1cd3f4
] - doc,test: mem protection must be observed in ffi (Bryan English) #62818 - [
3d5cf171dc
] - esm: addERR_REQUIRE_ESM_RACE_CONDITION
(Antoine du Hamel) #62462 - [
2004d8d6db
] - ffi: makeFFIFunctionInfo
aBaseObject
subclass (Anna Henningsen) #63071 - [
53eb7abeba
] - ffi: prevent premature GC of DynamicLibrary (semimikoh) #63024 - [
58dc92f502
] - ffi: support Symbol.dispose on DynamicLibrary (Matteo Collina) #62925 - [
528f8b2bae
] - ffi: add shared-buffer fast path for numeric and pointer signatures (Bryan English) #62918 - [
42ac8b9ae7
] - fs: add followSymlinks option to glob (Matteo Collina) #62695 - [
873c2bca70
] - fs: restore fs patchability in ESM loader (Joyee Cheung) #62835 - [
349c7502c3
] - fs: validate position argument before length === 0 early return (Edy Silva) #62674 - [
06defaa2ea
] - (SEMVER-MINOR) fs: add signal option to fs.stat() (Mert Can Altin) #57775 - [
db66a963bf
] - (SEMVER-MINOR) fs: expose frsize field in statfs (Jinho Jang) #62277 - [
3191d2936a
] - http: emit 'drain' on OutgoingMessage only after buffers drain (Robert Nagy) #62936 - [
87adb3472b
] - (SEMVER-MINOR) http: harden ClientRequest options merge (Matteo Collina) #63082 - [
e0b79633f6
] - http: fix leaked error listener on sync HTTP req create + destroy (Tim Perry) #62872 - [
70c5491f53
] - http: fix no_proxy leading-dot suffix matching (Daijiro Wachi) #62333 - [
60a585e68a
] - http: cleanup pipeline queue (Robert Nagy) #62534 - [
9047ec12ce
] - (SEMVER-MINOR) http: add req.signal to IncomingMessage (Akshat) #62541 - [
01eed5901b
] - http2: expose writable stream state on compat response (T) #63003 - [
19b7adf3ba
] - inspector: fix absolute URLs in network http (bugyaluwang) #62955 - [
4d10823fbb
] - inspector: coerce key and value to string in webstorage events (Ali Hassan) #62616 - [
9a3ac66cc5
] - inspector: return errors when CDP protocol event emission fails (Ryuhei Shima) #62162 - [
c89501c6e5
] - inspector: auto collect webstorage data (Ryuhei Shima) #62145 - [
ef08c5016a
] - lib: refactor internal webidl converters (Filip Skokan) #62979 - [
d0744c6a99
] - lib: add Temporal to frozen intrinsics (René) #63029 - [
6d81cb17b3
] - lib: avoid quadratic shift() in startup snapshot callback (Daijiro Wachi) #62914 - [
3491f73051
] - lib: fix FLOAT_32 and FLOAT_64 type constants in ffi (Daijiro Wachi) #62892 - [
c4ca303b36
] - lib: harden kKeyOps lookup with null prototype (Filip Skokan) #62877 - [
2e612fe070
] - lib: short-circuit WebIDL BufferSource SAB check (Filip Skokan) #62833 - [
e850ee9c69
] - lib: add new methods and error codes (Paolo Insogna) #62762 - [
e21b873589
] - lib: use js-only implementation ofisDataView()
(René) #62780 - [
f454d1719d
] - lib: fix lint in internal/webstreams/util.js (Filip Skokan) #62806 - [
fbd8ededba
] - lib: fix sequence argument handling in Blob constructor (Ms2ger) #62179 - [
16860e6abd
] - lib: improve Web Cryptography key validation ordering (Filip Skokan) #62749 - [
ba3f3e1753
] - lib: reject SharedArrayBuffer in web APIs per spec (Ali Hassan) #62632 - [
d065e996bb
] - lib: defer AbortSignal.any() following (sangwook) #62367 - [
2a711f4b0c
] - (SEMVER-MINOR) lib,src,test,doc: add node:ffi module (Colin Ihrig) #62072 - [
d578343582
] - meta: bump github/codeql-action from 4.35.1 to 4.35.3 (dependabot[bot]) #63074 - [
1b4b90d544
] - meta: bump Mozilla-Actions/sccache-action from 0.0.9 to 0.0.10 (dependabot[bot]) #63073 - [
1477349e47
] - meta: bump actions/upload-artifact from 7.0.0 to 7.0.1 (dependabot[bot]) #63072 - [
ecb7de271a
] - meta: bump cachix/install-nix-action from 31.10.3 to 31.10.5 (dependabot[bot]) #62846 - [
fb91408312
] - meta: bump actions/upload-artifact from 7.0.0 to 7.0.1 (dependabot[bot]) #62850 - [
7eb9a6be68
] - meta: add automation policy (Chengzhong Wu) #62871 - [
6f053a4cb8
] - meta: update CODEOWNERS for FFI (Paolo Insogna) #62853 - [
88fe50a725
] - meta: move VoltrexKeyva to emeritus (Matteo Collina) #62895 - [
42e770bdd0
] - meta: bump peter-evans/create-pull-request from 8.1.0 to 8.1.1 (dependabot[bot]) #62845 - [
952d005233
] - meta: bump step-security/harden-runner from 2.16.1 to 2.19.0 (dependabot[bot]) #62844 - [
1bd19d9768
] - meta: bump actions/github-script from 8.0.0 to 9.0.0 (dependabot[bot]) #62843 - [
386244a7dd
] - meta: bump actions/setup-node from 6.3.0 to 6.4.0 (dependabot[bot]) #62842 - [
16b2c41f70
] - meta: broaden stale bot (Aviv Keller) #62658 - [
41e7a4ba82
] - meta: pass release version to release worker (flakey5) #62777 - [
632821db85
] - meta: add QUIC to CODEOWNERS (Tim Perry) #62652 - [
4a7ad93ed8
] - meta: move Michael to emeritus (Michael Dawson) #62536 - [
44d5a33efb
] - meta: populate apt list for slim runner in update-openssl workflow (René) #62628 - [
d874596aa3
] - meta: bump cachix/install-nix-action from 31.9.1 to 31.10.3 (dependabot[bot]) #62551 - [
1631b27e2b
] - meta: bump step-security/harden-runner from 2.15.0 to 2.16.1 (dependabot[bot]) #62550 - [
4de376894d
] - meta: bump actions/download-artifact from 8.0.0 to 8.0.1 (dependabot[bot]) #62549 - [
39da4d7bd6
] - meta: bump actions/setup-node from 6.2.0 to 6.3.0 (dependabot[bot]) #62548 - [
62e3aa55ad
] - meta: bump github/codeql-action from 4.32.4 to 4.35.1 (dependabot[bot]) #62547 - [
83986de8a2
] - meta: bump codecov/codecov-action from 5.5.2 to 6.0.0 (dependabot[bot]) #62545 - [
18e56861dc
] - meta: bump cachix/cachix-action from 16 to 17 (dependabot[bot]) #62544 - [
d4e49d567a
] - meta: bump actions/cache from 5.0.3 to 5.0.4 (dependabot[bot]) #62543 - [
2c5a914af4
] - meta: require DCO signoff in commit message guidelines (James M Snell) #62510 - [
f21039ce59
] - meta: expand memory leak DoS criteria to all DoS (Joyee Cheung) #62505 - [
824ac6b5bf
] - module: excludenode:ffi
frombuiltinModules
when not enabled (Jordan Harband) #63158 - [
bb6293ab7c
] - module: remove duplicated checks from_resolveFilename
(Antoine du Hamel) #62729 - [
34ec8c9f5c
] - module,win: fix long subpath import (Stefan Stojanovic) #62101 - [
de46e68918
] - node-api: update libuv ABI stability note (Chengzhong Wu) #62789 - [
78c7d77bbf
] - node-api: add napi_create_external_sharedarraybuffer (Ben Noordhuis) #62623 - [
a0ccf94f61
] - node-api: execute tsfn finalizer after queue drains when aborted (Kevin Eady) #61956 - [
ab66de8eaa
] - (SEMVER-MINOR) process: throw on execve(2) failure instead of aborting (Bryan English) #62878 - [
20151be8cb
] - process: handle rejections only when needed (Gürgün Dayıoğlu) #62919 - [
9b24a815a2
] - quic: add QuicEndpoint.listening & QuicStream.destroy() and tests (Tim Perry) #62648 - [
761a96740c
] - quic: fixup token verification to handle zero expiration (James M Snell) #62620 - [
4ade02ac85
] - quic: support multiple ALPN negotiation (James M Snell) #62620 - [
b2e2e648e4
] - quic: apply multiple TLS context improvements and SNI support (James M Snell) #62620 - [
56b941af4a
] - quic: implement rapidhash for hashing improvements (James M Snell) #62620 - [
7cda4300b8
] - quic: use arena allocation for packets (James M Snell) #62589 - [
1e8fa2f1bd
] - sqlite: use OneByte for ASCII text and internalize col names (Ali Hassan) #61954 - [
3af44ee508
] - sqlite: add serialize() and deserialize() (Ali Hassan) #62579 - [
6386914b4b
] - src: decouple KeyObject and CryptoKey and move CryptoKey to src (Filip Skokan) #62924 - [
2dc1d205ee
] - src: replace uses of deprecated v8::External APIs (gahaas) #61898 - [
cb33a794a5
] - src: remove license headers for new node_profiling files (Chengzhong Wu) #63066 - [
59860eb798
] - src: swap dotenv and config file parsing order (Marco Ippolito) #63035 - [
fda439cb58
] - src: useunique_ptr
for ffi memory management (Anna Henningsen) #63071 - [
56917afc57
] - src: split profiling helpers from util (Ilyas Shabi) #63008 - [
fca56a409d
] - src: add missing <cstdlib> for abort() declaration (Charles Kerr) #63001 - [
d49c89e915
] - src: make node.config.json throw at unknown fields (Marco Ippolito) #62992 - [
e89c8e9b68
] - src: fix crash in GetErrorSource() for invalid using syntax (semimikoh) #62770 - [
d89f719ce0
] - src: remove outdated comments in contextify (Chengzhong Wu) #62932 - [
5117a3e52b
] - src: simplifyTCPWrap::Connect
signature (Anna Henningsen) #62929 - [
41bd288ec7
] - src: align FFI error handling with Node.js source (Anna Henningsen) #62858 - [
faaccfb9df
] - src: simplify and fix FFI ArrayBuffer accesses (Anna Henningsen) #62857 - [
43bf39c350
] - src: use DCHECK in AsyncWrap::MakeCallback instead emiting a warning (Gerhard Stöbich) #62795 - [
da52b09859
] - src: fix MaybeStackBuffer char_traits deprecation warning (om-ghante) #62507 - [
2b12bca317
] - src: use context-free V8 message column getters (René) #62778 - [
7efc2ce7b3
] - src: clean up experimental flag variables (Antoine du Hamel) #62759 - [
8273682c87
] - (SEMVER-MINOR) src: allow empty --experimental-config-file (Marco Ippolito) #61610 - [
b844c24395
] - src: coercespawnSync
args to string once (Antoine du Hamel) #62633 - [
28679d76c4
] - src: use stack allocation for small string encoding (Ali Hassan) #62431 - [
144ef93735
] - src: add contextify interceptor debug logs (Chengzhong Wu) #62460 - [
d34cfb512e
] - stream: remove redundant method check from iter.pipeToSync (René) #63099 - [
a95830b72a
] - stream: copyeditwebstreams/adapter.js
(Antoine du Hamel) #63034 - [
4bf3e1e084
] - stream: remove duplicated utility (Antoine du Hamel) #63031 - [
214a8c197b
] - stream: simplifysetPromiseHandled
utility (Antoine du Hamel) #63032 - [
c12a767ff2
] - stream: validate ReadableStream.from iterator objects (Daeyeon Jeong) #62911 - [
b09953d2d4
] - stream: reject duplicate nested transferables (Daeyeon Jeong) #62831 - [
b9929622f3
] - stream: ensuring cross-destruction in _duplexify to prevent leaks (Daijiro Wachi) #62824 - [
c51a39b3ec
] - stream: simplifyreadableStreamFromIterable
(Antoine du Hamel) #62651 - [
36078574b9
] - stream: fix nested compose error propagation (Matteo Collina) #62556 - [
e1928cd481
] - stream: allow shared array buffer sources in writable webstream adapter (René) #62163 - [
450e0519d9
] - stream: simplifycreatePromiseCallback
(Antoine du Hamel) #62650 - [
57e59ea070
] - stream: fix writev unhandled rejection in fromWeb (sangwook) #62297 - [
958373413c
] - stream: noop pause/resume on destroyed streams (Robert Nagy) #62557 - [
ee38d2c43d
] - stream: refactor duplexify to be less suceptible to prototype pollution (Antoine du Hamel) #62559 - [
fbff28f7e6
] - (SEMVER-MINOR) stream: propagate destruction in duplexPair (Ahmed Elhor) #61098 - [
d7317f4f90
] - stream: add stream/iter to classic stream adapters (James M Snell) #62469 - [
55298c443f
] - test: accept OpenSSL 4 generic internal error for DH key-type mismatches (Filip Skokan) #62805 - [
96581bccc7
] - test: update WPT for url to 258f285de0 (Node.js GitHub Bot) #63087 - [
c73aba07fb
] - test: run Temporal presence checks without V8 flag (René) #63028 - [
9c94dce55b
] - test: export isRiscv64 from common module (Jamie Magee) #62609 - [
33c5f7fdbf
] - test: normalize known inspector crash as completion (Joyee Cheung) #62851 - [
8146a97bc3
] - test: update WPT for streams to f8f26a372f (Node.js GitHub Bot) #62864 - [
7c77c301c9
] - test: account for RFC 7919 FFDHE negotiation in OpenSSL 4.0 (Filip Skokan) #62805 - [
9bf7604eb6
] - test: skip tls-deprecated secp256k1 on OpenSSL 4.0 (Filip Skokan) #62805 - [
d173604b53
] - test: use an always invalid cipher and cover OpenSSL 4.0 behaviours (Filip Skokan) #62805 - [
72f52163b4
] - test: use valid DER OCSP responses (Filip Skokan) #62805 - [
e242394ad9
] - test: skip test-tls-error-stack when engines are unsupported (Filip Skokan) #62805 - [
9bff52ebf8
] - test: accept renamed OpenSSL 4.0 error code and reason (Filip Skokan) #62805 - [
d9b8cc1b68
] - test: update test/addons/openssl-binding for OpenSSL 4.0 (Filip Skokan) #62805 - [
960fb16287
] - test: mark test-snapshot-reproducible flaky (Filip Skokan) #62808 - [
7a12dd58cf
] - test: check contextify contextual store behavior in strict mode (René) #62571 - [
c73c8e603f
] - test: skiptest-temporal-with-zoneinfo
on system-icu builds (Antoine du Hamel) #62754 - [
48a3ca303e
] - test: generatelocalstorage.db
in a temp dir (Chengzhong Wu) #62660 - [
1a41c2c5db
] - test: update tls junk data error expectations (Filip Skokan) #62629 - [
115e8c2052
] - test: ensure WPT report is in out/wpt (Filip Skokan) #62637 - [
cb07b918bd
] - test: improve WPT runner summary (Filip Skokan) #62636 - [
7f48438380
] - test: skip url WPT subtests instead of modifying test script (Filip Skokan) #62635 - [
4097fb95d7
] - test: capture negative utimes mtime at call time (Yuya Inoue) #62490 - [
e29f46df81
] - test: allow skipping individual WPT subtests (Filip Skokan) #62517 - [
4d546886c3
] - test: use on-disk fixture for test-npm-install (Joyee Cheung) #62584 - [
5b35eb02ec
] - test: update WPT for url to 7a3645b79a (Node.js GitHub Bot) #62591 - [
7a8610835d
] - test_runner: fix failing suite hooks when marked withtodo
(Moshe Atlow) #63097 - [
a8c773a0c7
] - (SEMVER-MINOR) test_runner: align mock timeout api (sangwook) #62820 - [
dc0d757c8a
] - test_runner: fix suite rerun edge case (Moshe Atlow) #62860 - [
b883a5eaea
] - (SEMVER-MINOR) test_runner: add mock-timers support for AbortSignal.timeout (DeveloperViraj) #60751 - [
6fa62b7d58
] - test_runner: addtestId
to test events (Moshe Atlow) #62772 - [
39e08340ff
] - test_runner: publish to TracingChannel for OTel instrumentation (Moshe Atlow) #62502 - [
a21ae1771e
] - (SEMVER-MINOR) test_runner: support test order randomization (Pietro Marchini) #61747 - [
cf0edeb65d
] - test_runner: add passed, attempt, and diagnostic to SuiteContext (Moshe Atlow) #62504 - [
644e2399d6
] - test_runner: addgetTestContext()
(Moshe Atlow) #62501 - [
480d538830
] - tools: usenpm ci
in Undici update script (Antoine du Hamel) #63098 - [
9afb013edd
] - tools: update nixpkgs-unstable to c6d65881c5624c9cae5ea6cedef24699b0c (Node.js GitHub Bot) #63091 - [
b9f2f5a90a
] - tools: bump postcss from 8.5.8 to 8.5.10 in /tools/doc (dependabot[bot]) #62966 - [
09e4f4caca
] - tools: use LTS Node.js in notify-on-push workflow (Nenad Spasenic) #63084 - [
2af4c89774
] - tools: implements a few nits onbuild-aarch64-linux-v8
(Antoine du Hamel) #63048 - [
cf9c1849ca
] - tools: update gr2m/create-or-update-pull-request-action to v1.10.1 (Mike McCready) #63065 - [
96370a57ed
] - tools: simplifyupdate-undici.sh
(Antoine du Hamel) #63044 - [
b90486edd8
] - tools: do not runtest-linux
on unrelated tools changes (Antoine du Hamel) #63037 - [
ac49e7c9fc
] - tools: migrate fromopenssl-matrix.json
toopenssl-matrix.nix
(Antoine du Hamel) #63036 - [
a9df3e37fd
] - tools: update labels for nixpkgs pin bumps (Antoine du Hamel) #62994 - [
cee0154af8
] - tools: reuse V8 builds even without Cachix on test-shared (Antoine du Hamel) #62980 - [
78c183da6b
] - tools: do not include HTML docs in slim tarball (Antoine du Hamel) #62989 - [
04ce9df084
] - tools: bump the eslint group in /tools/eslint with 4 updates (dependabot[bot]) #62848 - [
4d2952c00a
] - tools: update nixpkgs-unstable to 01fbdeef22b76df85ea168fbfe1bfd9e636 (Node.js GitHub Bot) #62963 - [
555ad12f27
] - tools: update gyp-next to 0.22.1 (Node.js GitHub Bot) #62961 - [
f92cbc2c81
] - tools: fix commit linter for semver-major release proposals (Antoine du Hamel) #62993 - [
3b5bb4d758
] - tools: consolidate and simplify .editorconfig deps section (Daijiro Wachi) #62887 - [
027bef4f3e
] - tools: add non-default OpenSSL versions to the test-shared workflow (Filip Skokan) #62862 - [
fdcd7752de
] - tools: set bot as author of tools-deps-update PRs (Antoine du Hamel) #62856 - [
ab7be6d987
] - tools: bump brace-expansion from 5.0.4 to 5.0.5 in /tools/eslint (dependabot[bot]) #62458 - [
82281ffd59
] - tools: bump brace-expansion in /tools/clang-format (dependabot[bot]) #62467 - [
48bb51b3d7
] - tools: update nixpkgs-unstable to ab72be9733b41190ea34f1422a3e4e243ed (Node.js GitHub Bot) #62821 - [
67baa3254b
] - tools: bump @node-core/doc-kit in /tools/doc in the doc group (dependabot[bot]) #62512 - [
bdee0a859d
] - tools: exclude @node-core/doc-kit from dependabot cooldown (Levi Zim) #62775 - [
9e19f55214
] - tools: re-enable undici WPTs in daily wpt.fyi job (Filip Skokan) #62677 - [
1eedbdded9
] - tools: use upstream version of OpenSSL intest-shared
(Antoine du Hamel) #62679 - [
3490c1fba1
] - tools: pass the Temporal disable flag when disabled inshell.nix
(Antoine du Hamel) #62733 - [
3a29dafd2d
] - tools: fix--shared-ffi
compilation on macOS (Antoine du Hamel) #62737 - [
5cb9108b9c
] - tools: update nixpkgs-unstable to 13043924aaa7375ce482ebe2494338e0582 (Node.js GitHub Bot) #62700 - [
757cd21ea0
] - tools: update gyp-next to 0.22.0 (Node.js GitHub Bot) #62697 - [
fad51c2f03
] - tools: add a check for clean git tree after tests (Antoine du Hamel) #62661 - [
d1c517fd61
] - tools: improve backport review script (Antoine du Hamel) #62573 - [
6d169c75f7
] - tools: makev8.nix
more stable (Antoine du Hamel) #62508 - [
1587a60bf8
] - tools: add perfetto updater (Chengzhong Wu) #62397 - [
f54d74a5e7
] - tools: improve output for unexpected passes in WTP tests (Antoine du Hamel) #62587 - [
a86c96333c
] - tools: revert OpenSSL update workflow to ubuntu-latest (Richard Lau) #62627 - [
c9860f5800
] - tools: update nixpkgs-unstable to a6522db5b947cd7026a40d02acc3ca26136 (Node.js GitHub Bot) #62596 - [
ae41e2a141
] - tools: bump the eslint group in /tools/eslint with 2 updates (dependabot[bot]) #62552 - [
e2ba824407
] - tools: allow triagers to queue a PR for CI until it's reviewed (Antoine du Hamel) #62524 - [
899d780f15
] - tools: do not runcommit-lint
on release proposals (Antoine du Hamel) #62523 - [
102da27b4e
] - url: process crash via malformed UNC hostname in pathToFileURL() (Nicola Del Gobbo) #62574 - [
3abd78c3e5
] - url: optimize URLSearchParams set/delete duplicate handling (Gürgün Dayıoğlu) #62266 - [
fd3bf3830b
] - url: align default argument handling for URLPattern with webidl (Filip Skokan) #62719 - [
b85c73ff10
] - (SEMVER-MINOR) util: colorize text with hex colors (Guilherme Araújo) #61556 - [
c1d6b3db73
] - v8: add cpu profile options (Ilyas Shabi) #62684 - [
717d9a7fda
] - v8: add heap profile API (Ilyas Shabi) #62273 - [
2b885667a9
] - watch: track worker entry files in watch mode (SudhansuBandha) #62368 - [
457fb55193
] - watch: fix --env-file-if-exists crashing on linux if the file is missing (Efe) #61870
Windows 64-bit Installer: https://nodejs.org/dist/v26.1.0/node-v26.1.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v26.1.0/node-v26.1.0-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v26.1.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v26.1.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v26.1.0/node-v26.1.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v26.1.0/node-v26.1.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v26.1.0/node-v26.1.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v26.1.0/node-v26.1.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v26.1.0/node-v26.1.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v26.1.0/node-v26.1.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v26.1.0/node-v26.1.0-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v26.1.0/node-v26.1.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v26.1.0/node-v26.1.0.tar.gz
Other release files: https://nodejs.org/dist/v26.1.0/
Documentation: https://nodejs.org/docs/v26.1.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
67808a758620e6c9cc075b5c9c77600a3793c7be6d4610c7066ae6794e91db0b node-v26.1.0-aix-ppc64.tar.gz
1b16ac3cc9ba73efdb65f1b2b39ddb746e55c3affc9684c1b6f10ecefb25639c node-v26.1.0-arm64.msi
91063f665c2f5d6e69e4f8fcb66d3d476bc2785ace82267274bf4da789985ceb node-v26.1.0-darwin-arm64.tar.gz
c4b028b1ab7c01e4a526524d732522f71b0ea08e8859e29514d535ce2e17d443 node-v26.1.0-darwin-arm64.tar.xz
33519b28a352de668ab0a2a64366db032a45cb629d5353f86e4576e2780f4fcf node-v26.1.0-darwin-x64.tar.gz
6cbc3e8f528abaceca02d65e9f7df787ee7a49c245708d5bca6bc9c7c3cbf71f node-v26.1.0-darwin-x64.tar.xz
ffae4d3d81ba3a5e88579fa36aecb3ba9b4d5ed59dbe35233df7dce035402bb0 node-v26.1.0-headers.tar.gz
3147480b0957fcd4a515078c1b16948512a273264b018b159e1896e075852a1d node-v26.1.0-headers.tar.xz
fcb4c339eef70c909cae72091008a6497278e2d0fcd221c0653068cf4ea4f0c7 node-v26.1.0-linux-arm64.tar.gz
058f00fe6c84f804b4b96aab377f76ed57dd0be5f10af4dcc0fded172746f366 node-v26.1.0-linux-arm64.tar.xz
f3ee72a29d3d25a626bae1672667a500b12c284fcfc00f5d6162e3762ebf173f node-v26.1.0-linux-ppc64le.tar.gz
dbe65c537c7ce339a6e193c0aa9ac5b092b92589e1c1f12c3ac8eef4f18742ff node-v26.1.0-linux-ppc64le.tar.xz
6e381e4a3b353f335d297abfe4c7d9485459247519df10445b17cc89d8c7f7a5 node-v26.1.0-linux-s390x.tar.gz
d484cea6da8b734986786b8711652da927ba7508c044930401c66206d55577a3 node-v26.1.0-linux-s390x.tar.xz
62d555c329e05e3625109f2e3a8b5195b368d5ef38266292469d32f63cd98ffd node-v26.1.0-linux-x64.tar.gz
9fc6f21b6c4a62439727123e510e9c39febb2f563738f4927cd3e0b288c9b3c9 node-v26.1.0-linux-x64.tar.xz
c48f0cd097575dd3fcac777421fb427cc2076895990163cb4fc0de0b9eefddaf node-v26.1.0-win-arm64.7z
0b913d67ccef3e7e62edcecd2daf31de5fd9551936501ccd3cd5c027ada089ee node-v26.1.0-win-arm64.zip
645eb4944098148c58fb1864e9084610ede8e630eaa36d203f0883489ca56a93 node-v26.1.0-win-x64.7z
089a02c4c687451c9f0b7f1bfd252dae85a7ba27df0295a14096bdcc956fdc92 node-v26.1.0-win-x64.zip
64a9313ae5334a3ce3e482b92d79ae4f9d62764c69d90849ec83c22854f7b0da node-v26.1.0-x64.msi
1cf43d1e8cba1f407ddb6a683e79ccb648d2465c1c0486943b00b3dabdaa021a node-v26.1.0.pkg
ccaf9bfea12ec3d2beb36f5a1d54483f2620ad9de007e551fb8640ed82d29989 node-v26.1.0.tar.gz
779a1364889575d44e0215adc381806bbd0d9437557b59893e172f5b9d35a990 node-v26.1.0.tar.xz
d2da4369f98ca3333f3374128237916e91bd4c9a42cfa952e085a6b42e94f41a win-arm64/node.exe
376eb35054756d8493adc1f26495fba0b7bda7365cdb7c132130044a622d6c31 win-arm64/node.lib
703253747a04e5660756d42a4c49760a67e029cc433bf47ff5363a2291d1e3af win-arm64/node_pdb.7z
80ef6b8b87a28f041fec9ff0bb1a4f8eaa3af457ff550361c4360c7acfb894aa win-arm64/node_pdb.zip
35ebb74da6acb56fdf570de64f1ae510d6d18ca09da494a3e1ac87edd32d263b win-x64/node.exe
9c236a87f9c50a26099d74f35883c28c6b279585ccc5849aa640ff23de7be9b8 win-x64/node.lib
154c4f86083a255aabe3a95dea05b2557a04674505a9c00542ecf239539c5d6d win-x64/node_pdb.7z
28d09820ad0228f3b7e1085ade8ae38895b76ea96baee12e020c2fd88c4d1c50 win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iHUEARYIAB0WIQRb6KP2yKXAHRBsCtggsaOQsWjTVgUCafxkYgAKCRAgsaOQsWjT
VqUsAQDS9Mx+1Igqr9+8eUuVZoEqwb/Ps9JetNgrC2xonjB4JQD/Xi9Snnbu+88Z
mkEFu14+D5hcDCmaGgkUjoYU7bsPGQg=
=Be6F
-----END PGP SIGNATURE-----
```

---

## 2. Node.js 26.0.0 (Current)

- 日期: 2026-05-05 14:26
- 链接: https://nodejs.org/en/blog/release/v26.0.0

```
Node.js 26.0.0 (Current)
Rafael Gonzaga
2026-05-05, Version 26.0.0 (Current), @RafaelGSS
We're excited to announce the release of Node.js 26! Highlights include the Temporal API enabled by default, updates to the V8 JavaScript engine to 14.6, Undici to 8.0, and several important deprecations and removals as we continue to modernize the platform.
As a reminder, Node.js 26 will enter long-term support (LTS) in October, but until then, it will be the "Current" release for the next six months. We encourage you to explore the new features and benefits offered by this latest release and evaluate their potential impact on your applications.
Notable Changes
Temporal API
The Temporal API is now enabled by default in Node.js 26. Temporal is a modern date/time API for JavaScript
that provides a more robust and feature-rich alternative to the legacy Date
object.
Contributed by Richard Lau in #61806.
V8 14.6
The V8 engine is updated to version 14.6.202.33, which is part of Chromium 146.
This version also includes:
- Upsert (https://github.com/tc39/proposal-upsert):
[Weak]Map.prototype.getOrInsert()
,[Weak]Map.prototype.getOrInsertComputed()
- Iterator sequencing (https://github.com/tc39/proposal-iterator-sequencing):
Iterator.concat()
Contributed by Michaël Zasso in #61898.
Undici 8
Undici has been updated to version 8.0.2, bringing new features and improvements to Node.js's HTTP client implementation.
Deprecations and Removals
-
[
dff46c07c3
] - (SEMVER-MAJOR) crypto: move DEP0182 to End-of-Life (Tobias Nießen) #61084 -
[
93c25815ee
] - (SEMVER-MAJOR) http: move writeHeader to end-of-life (Sebastian Beltran) #60635http.Server.prototype.writeHeader()
is now fully removed. Usehttp.Server.prototype.writeHead()
instead. -
[
c755b0113c
] - (SEMVER-MAJOR) stream: move _stream_* to end-of-life (Sebastian Beltran) #60657The legacy
_stream_wrap
,_stream_readable
,_stream_writable
,_stream_duplex
,_stream_transform
, and_stream_passthrough
modules are now fully removed. -
[
adac077484
] - (SEMVER-MAJOR) crypto: runtime-deprecate DEP0203 and DEP0204 (Filip Skokan) #62453 -
[
ac6375417a
] - (SEMVER-MAJOR) stream: promote DEP0201 to runtime deprecation (René) #62173 -
[
98907f560f
] - (SEMVER-MAJOR) module: runtime-deprecate module.register() (Geoffrey Booth) #62401 -
[
89f4b6cddb
] - (SEMVER-MAJOR) module: remove --experimental-transform-types (Marco Ippolito) #61803
Semver-Major Commits
- [
d3f79aa65d
] - (SEMVER-MAJOR) assert: allow printf-style messages as assertion error (Ruben Bridgewater) #58849 - [
f6ce381fec
] - (SEMVER-MAJOR) build: bump GCC requirement to 13.2 (Michaël Zasso) #62555 - [
bff81fca46
] - (SEMVER-MAJOR) build: enable Temporal by default (Richard Lau) #61806 - [
6ddb1643e1
] - (SEMVER-MAJOR) build: enable V8_VERIFY_WRITE_BARRIERS in debug build (Joyee Cheung) #61898 - [
a8ab08b373
] - (SEMVER-MAJOR) build: reset embedder string to "-node.0" (Michaël Zasso) #61898 - [
0998c37eb6
] - (SEMVER-MAJOR) build: target Power 9 for AIX/IBM i (Richard Lau) #62296 - [
d73c49e849
] - (SEMVER-MAJOR) build: drop support for Python 3.9 (Mike McCready) #61177 - [
3c92ee1008
] - (SEMVER-MAJOR) build: enable maglev for Linux on s390x (Richard Lau) #60863 - [
908c468828
] - (SEMVER-MAJOR) build: reset embedder string to "-node.0" (Michaël Zasso) #60488 - [
6380fbb5ee
] - (SEMVER-MAJOR) build: reset embedder string to "-node.0" (Michaël Zasso) #60111 - [
089d6c77e7
] - (SEMVER-MAJOR) (CVE-2026-21717) build,test: test array index hash collision (Joyee Cheung) #61898 - [
f9bd0165c4
] - (SEMVER-MAJOR) build,win: fix Temporal build (StefanStojanovic) #61806 - [
6cc4cf8fe8
] - (SEMVER-MAJOR) crypto: unify asymmetric key import through KeyObjectHandle::Init (Filip Skokan) #62499 - [
adac077484
] - (SEMVER-MAJOR) crypto: runtime-deprecate DEP0203 and DEP0204 (Filip Skokan) #62453 - [
74509b166a
] - (SEMVER-MAJOR) crypto: decorate async crypto job errors with OpenSSL error details (Filip Skokan) #62348 - [
da5843b91d
] - (SEMVER-MAJOR) crypto: default ML-KEM and ML-DSA pkcs8 export to seed-only format (Filip Skokan) #62178 - [
dff46c07c3
] - (SEMVER-MAJOR) crypto: move DEP0182 to End-of-Life (Tobias Nießen) #61084 - [
94cd600542
] - (SEMVER-MAJOR) crypto: fix DOMException name for non-extractable key error (Filip Skokan) #60830 - [
dae2219cca
] - (SEMVER-MAJOR) deps: V8: cherry-pick 0f024d4e66e0 (ishabi) #62408 - [
15d406c1b1
] - (SEMVER-MAJOR) deps: fix V8 race condition for AIX (Abdirahim Musse) #61898 - [
46852d2d7a
] - (SEMVER-MAJOR) deps: V8: cherry-pick cd2c216e7658 (LuYahan) #61898 - [
784431d6fc
] - (SEMVER-MAJOR) deps: V8: backport 088b7112e7ab (Igor Sheludko) #61898 - [
3839c4a756
] - (SEMVER-MAJOR) deps: V8: cherry-pick 00f6e834029f (Joyee Cheung) #61898 - [
44f64f1dd9
] - (SEMVER-MAJOR) deps: V8: backport bef0d9c1bc90 (Joyee Cheung) #61898 - [
1f8f288e22
] - (SEMVER-MAJOR) deps: V8: cherry-pick cf1bce40a5ef (Richard Lau) #61898 - [
d7eccac9ad
] - (SEMVER-MAJOR) deps: V8: cherry-pick daf4656ba85e (Milad Fa) #61898 - [
3ee1ea7d0b
] - (SEMVER-MAJOR) deps: V8: cherry-pick d83f479604c8 (Joyee Cheung) #61898 - [
80907c0239
] - (SEMVER-MAJOR) deps: V8: cherry-pick edeb0a4fa181 (Joyee Cheung) #61898 - [
5e0dc169e9
] - (SEMVER-MAJOR) deps: V8: cherry-pick aa0b288f87cc (Richard Lau) #61898 - [
8c1f7adbcd
] - (SEMVER-MAJOR) deps: patch V8 to fix Windows build (StefanStojanovic) #61898 - [
3cbd3404d9
] - (SEMVER-MAJOR) deps: V8: cherry-pick highway@989a498fdf3 (Richard Lau) #61898 - [
9f2b7d4031
] - (SEMVER-MAJOR) deps: support madvise(3C) across ALL illumos revisions (Dan McDonald) #61898 - [
947ec32118
] - (SEMVER-MAJOR) deps: patch V8 for illumos (Dan McDonald) #61898 - [
0660b942b2
] - (SEMVER-MAJOR) deps: remove problematic comment from v8-internal (Michaël Zasso) #61898 - [
bef7b31a3f
] - (SEMVER-MAJOR) deps: define V8_PRESERVE_MOST as no-op on Windows (Stefan Stojanovic) #61898 - [
a10bf1e6ce
] - (SEMVER-MAJOR) deps: patch V8 to avoid duplicated zlib symbol (Michaël Zasso) #61898 - [
cc547428e1
] - (SEMVER-MAJOR) deps: update V8 to 14.6.202.33 (Michaël Zasso) #61898 - [
b81d2cbcae
] - (SEMVER-MAJOR) deps: update undici to 8.0.2 (Node.js GitHub Bot) #62384 - [
bf5c6a8bd4
] - (SEMVER-MAJOR) deps: V8: backport 151d0a44a1b2 (Abdirahim Musse) #60488 - [
b59af772dc
] - (SEMVER-MAJOR) deps: V8: cherry-pick 47800791b35c (Jakob Kummerow) #60488 - [
5e41e5228a
] - (SEMVER-MAJOR) deps: patch V8 for illumos (Dan McDonald) #59805 - [
2243e58e43
] - (SEMVER-MAJOR) deps: use std::map in MSVC STL for EphemeronRememberedSet (Joyee Cheung) #58070 - [
4157964c42
] - (SEMVER-MAJOR) deps: remove problematic comment from v8-internal (Michaël Zasso) #58070 - [
7c8483a4e9
] - (SEMVER-MAJOR) deps: patch V8 to avoid duplicated zlib symbol (Michaël Zasso) #54077 - [
53379f3706
] - (SEMVER-MAJOR) deps: update V8 to 14.3.127.12 (Michaël Zasso) #60488 - [
f819aec288
] - (SEMVER-MAJOR) deps: V8: cherry-pick ff34ae20c8e3 (Chengzhong Wu) #60111 - [
1acd8df36f
] - (SEMVER-MAJOR) deps: V8: backport fed47445bbdd (Abdirahim Musse) #60111 - [
46f72577a4
] - (SEMVER-MAJOR) deps: patch V8 for illumos (Dan McDonald) #59805 - [
39eb88eaa8
] - (SEMVER-MAJOR) deps: use std::map in MSVC STL for EphemeronRememberedSet (Joyee Cheung) #58070 - [
ea3d14eadb
] - (SEMVER-MAJOR) deps: remove problematic comment from v8-internal (Michaël Zasso) #58070 - [
7bc0f245b4
] - (SEMVER-MAJOR) deps: patch V8 to avoid duplicated zlib symbol (Michaël Zasso) #54077 - [
c2843b722c
] - (SEMVER-MAJOR) deps: update V8 to 14.2.231.9 (Michaël Zasso) #60111 - [
b4ea323833
] - (SEMVER-MAJOR) diagnostics_channel: ensure tracePromise consistency with non-Promises (René) #61766 - [
0c08835f71
] - (SEMVER-MAJOR) doc: remove extensionless CJS exception for type:module packages (Matteo Collina) #62176 - [
ef0f0b0865
] - (SEMVER-MAJOR) doc: update supported Windows SDK version to 11 (Mike McCready) #61973 - [
a00d95c73d
] - (SEMVER-MAJOR) doc: drop p8 and z13 support (Milad Fa) #61005 - [
93c25815ee
] - (SEMVER-MAJOR) http: move writeHeader to end-of-life (Sebastian Beltran) #60635 - [
4346c0f7a7
] - (SEMVER-MAJOR) http: fix handling of HTTP upgrades with bodies (Tim Perry) #60016 - [
fa70327610
] - (SEMVER-MAJOR) lib: return undefined for localStorage without file (Matteo Collina) #61333 - [
b328bf74bd
] - (SEMVER-MAJOR) lib,src: implement QuotaExceededError as DOMException-derived interface (Filip Skokan) #62293 - [
98907f560f
] - (SEMVER-MAJOR) module: runtime-deprecate module.register() (Geoffrey Booth) #62401 - [
89f4b6cddb
] - (SEMVER-MAJOR) module: remove --experimental-transform-types (Marco Ippolito) #61803 - [
5334433437
] - (SEMVER-MAJOR) src: replace uses of deprecated v8::External APIs (gahaas) #61898 - [
46e75f4874
] - (SEMVER-MAJOR) src: stop usingv8::PropertyCallbackInfo<T>::This()
(Igor Sheludko) #61898 - [
54fefda0aa
] - (SEMVER-MAJOR) src: avoid deprecated Wasm API (Clemens Backes) #61898 - [
840f509bd1
] - (SEMVER-MAJOR) src: avoid deprecatedFixedArray::Get
(Clemens Backes) #61898 - [
75c3bcc3ec
] - (SEMVER-MAJOR) src: update NODE_MODULE_VERSION to 147 (Michaël Zasso) #61898 - [
8480f87375
] - (SEMVER-MAJOR) src: remove deprecated and unused isolate fields (Michaël Zasso) #60488 - [
70b6bd8e19
] - (SEMVER-MAJOR) src: update NODE_MODULE_VERSION to 144 (Michaël Zasso) #60488 - [
7d2bc5249b
] - (SEMVER-MAJOR) src: includenode_api_types.h
instead ofnode_api.h
innode.h
(Anna Henningsen) #60496 - [
91ab1101bc
] - (SEMVER-MAJOR) src: update NODE_MODULE_VERSION to 142 (Michaël Zasso) #60111 - [
ac6375417a
] - (SEMVER-MAJOR) stream: promote DEP0201 to runtime deprecation (René) #62173 - [
c755b0113c
] - (SEMVER-MAJOR) stream: move _stream_* to end-of-life (Sebastian Beltran) #60657 - [
fadb214d95
] - (SEMVER-MAJOR) stream: readable read one buffer at a time (Robert Nagy) #60441 - [
4fe325d93d
] - (SEMVER-MAJOR) stream: preserve AsyncLocalStorage on finished only when needed (avcribl) #59873 - [
7682e7e9c5
] - (SEMVER-MAJOR) test: skip wasm allocation tests in workers (Michaël Zasso) #61898 - [
ebfaf25870
] - (SEMVER-MAJOR) test: update wpt Wasm jsapi expectations (Michaël Zasso) #61898 - [
ece6a17574
] - (SEMVER-MAJOR) test: support presence of Temporal global (Michaël Zasso) #61898 - [
75b8d7a912
] - (SEMVER-MAJOR) test: add type tags to uses of v8::External (gahaas) #61898 - [
092a448ad0
] - (SEMVER-MAJOR) test: fix test-linux-perf-logger for V8 14.3 (Michaël Zasso) #60488 - [
8eb9c8f794
] - (SEMVER-MAJOR) tools: remove v8_initializers_slow workaround from v8.gyp (Michaël Zasso) #61898 - [
a34fe77fe7
] - (SEMVER-MAJOR) tools: add Rust args totools/make-v8.sh
(Richard Lau) #61898 - [
f4666bd6e3
] - (SEMVER-MAJOR) tools: update V8 gypfiles for 14.6 (Michaël Zasso) #61898 - [
3c23d217a6
] - (SEMVER-MAJOR) tools: update V8 gypfiles for 14.5 (Michaël Zasso) #61898 - [
e508489e37
] - (SEMVER-MAJOR) tools: update V8 gypfiles for 14.4 (Michaël Zasso) #61898 - [
dc97b507d0
] - (SEMVER-MAJOR) util: mark proxied objects as such when inspecting them (Ruben Bridgewater) #61029 - [
ddbe1365ff
] - (SEMVER-MAJOR) util: reduce TextEncoder.encodeInto function size (Yagiz Nizipli) #60339
Semver-Minor Commits
- [
d4fa60cf9f
] - (SEMVER-MINOR) crypto: add raw key formats support to the KeyObject APIs (Filip Skokan) #62240
Semver-Patch Commits
- [
4d8834fbef
] - build: add rust target for macOS cross compiles (Richard Lau) #63015 - [
a4edab8dfb
] - build: useCARGO
environment variable if set (Richard Lau) #62421 - [
ecf8721076
] - build: add weak symbol detection to export script (Abdirahim Musse) #62656 - [
5b9f811662
] - build: filter hidden visibility symbols on AIX (Abdirahim Musse) #62656 - [
2e724793e6
] - build: aix add conditonal flags for clang builds (Abdirahim Musse) #62656 - [
f212aee483
] - build: enable temporal on GHA macOS build (Chengzhong Wu) #61691 - [
159ae48f8c
] - build: addcargo
andrustc
checks for Temporal (Richard Lau) #61467 - [
a004535617
] - build: add temporal to linux GHA build (Chengzhong Wu) #60942 - [
9df9b66c18
] - crypto: add support for Ed25519 context parameter (Filip Skokan) #62474 - [
c3042c605b
] - crypto: recognize raw formats in keygen (Filip Skokan) #62480 - [
ce0f498def
] - deps: V8: cherry-pick fcf8b990c73c (Abdirahim Musse) #62894 - [
b7fab70d56
] - Revert "deps: V8: cherry-pick 7107287" (Richard Lau) #62894 - [
d936c30fb4
] - deps: V8: cherry-pick 7107287 (Abdirahim Musse) #62656 - [
c91d00b6d4
] - deps: fix aix implicit declaration in OpenSSL (Abdirahim Musse) #62656 - [
0474a27c06
] - deps: libuv: revert 3a9a6e3e6b (Antoine du Hamel) #62511 - [
7547e795ef
] - deps: update icu to 78.3 (Node.js GitHub Bot) #62324 - [
5bebd7eaea
] - deps: update libuv to 1.52.1 (Node.js GitHub Bot) #61829 - [
87d7db1918
] - deps: patch V8 to 14.3.127.18 (Node.js GitHub Bot) #61421 - [
9d27d9a393
] - deps: patch V8 to 14.3.127.17 (Node.js GitHub Bot) #61058 - [
bfc729cf19
] - deps: patch V8 to 14.3.127.16 (Node.js GitHub Bot) #60819 - [
8716146d5b
] - deps: patch V8 to 14.3.127.14 (Node.js GitHub Bot) #60743 - [
da71ab6895
] - deps: V8: cherry-pick highway@989a498fdf3 (Richard Lau) #60682 - [
72d719dc00
] - deps: support madvise(3C) across ALL illumos revisions (Dan McDonald) #58237 - [
ecca2b0d64
] - deps: define V8_PRESERVE_MOST as no-op on Windows (Stefan Stojanovic) #56238 - [
baefd4d5e2
] - deps: patch V8 to 14.2.231.17 (Node.js GitHub Bot) #60647 - [
76d6be5fc5
] - deps: patch V8 to 14.2.231.16 (Node.js GitHub Bot) #60544 - [
e0ca993514
] - deps: patch V8 to 14.2.231.14 (Node.js GitHub Bot) #60413 - [
de8386de4d
] - deps: V8: cherry-pick f93055fbd5aa (Olivier Flückiger) #60105 - [
710105bab5
] - deps: support madvise(3C) across ALL illumos revisions (Dan McDonald) #58237 - [
6e5f3b9fe1
] - deps: define V8_PRESERVE_MOST as no-op on Windows (Stefan Stojanovic) #56238 - [
b2c5235254
] - doc: fix stray carriage return in packages.md (Filip Skokan) #62350 - [
f38a739623
] - doc: reserve NMV 146 for Electron 42 (Niklas Wenzel) #62124 - [
a57893b799
] - doc: add Temporal section to Table of Contents (Richard Lau) #61805 - [
d4cc54b8c8
] - doc: fix v24 changelog after security release (Marco Ippolito) #61371 - [
659fd01b3e
] - doc: fix v22 changelog after security release (Marco Ippolito) #61371 - [
6c96a63891
] - doc: fix v20 changelog after security release (Marco Ippolito) #61371 - [
a18f8c1693
] - doc: reserve NMV 145 for Electron 41 (Niklas Wenzel) #61291 - [
253b16fe14
] - doc: add note about rust toolchain version requirement (Chengzhong Wu) #60942 - [
0177491df2
] - doc: restore REPLACEME on assert change (Michaël Zasso) #60848 - [
dec0213c83
] - doc: add known issue to v24.11.0 release notes (Richard Lau) #60467 - [
f7ca0ae765
] - doc: remove Corepack documentation page (Antoine du Hamel) #57663 - [
a7d9c49490
] - doc: reserve NMV 143 for Electron 40 (Shelley Vohr) #60386 - [
04a086a1f4
] - esm: use wasm version of cjs-module-lexer (Joyee Cheung) #60663 - [
a27052f2e0
] - Revert "inspector: fix compressed responses" (Antoine du Hamel) #61502 - [
186c7a9c74
] - inspector: fix compressed responses (Ruben Nogueira) #61226 - [
012bf70908
] - process: optimize asyncHandledRejections by using FixedQueue (Gürgün Dayıoğlu) #60854 - [
1a88acbfa2
] - quic: fixup linting/formatting issues (James M Snell) #62387 - [
79b960a2bc
] - quic: update http3 impl details (James M Snell) #62387 - [
57186e5827
] - quic: fix a handful of bugs and missing functionality (James M Snell) #62387 - [
637bda0238
] - sqlite: enable Percentile extension (Jurj Andrei George) #61295 - [
e619adfb86
] - src: workaround AIX libc++ std::filesystem bug (Richard Lau) #62788 - [
79262ff860
] - src: do not enable wasm trap handler if there's not enough vmem (Joyee Cheung) #62132 - [
2422ed8b5b
] - src: remove redundantexperimental_transform_types
from node_options.h (沈鸿飞) #62058 - [
a86db6be70
] - src: simplify handling of kNoAuthTagLength (Tobias Nießen) #61192 - [
d546e7fd0b
] - src: tag more v8 aligned pointer slots (Chengzhong Wu) #60666 - [
b8e264d3c3
] - src: tag v8 aligned pointer slots with embedder data type tags (Chengzhong Wu) #60602 - [
cd391b5f11
] - test: wpt for Wasm jsapi including new ESM Integration tests (Guy Bedford) #59034 - [
1baafcc882
] - test: update WPT resources, interfaces and WebCryptoAPI (Node.js GitHub Bot) #62389 - [
6a84d4a17c
] - tools: update nixpkgs-unstable to 832efc09b4caf6b4569fbf9dc01bec3082a (Node.js GitHub Bot) #62486 - [
a98d9f6ad7
] - tools: update nixpkgs-unstable to 9cf7092bdd603554bd8b63c216e8943cf9b (Node.js GitHub Bot) #62383 - [
f6d02af01f
] - tools: update nixpkgs-unstable to f82ce7af0b79ac154b12e27ed800aeb9741 (Node.js GitHub Bot) #62258 - [
5b5f069a27
] - tools: bump nixpkgs-unstable pin to e38213b91d3786389a446dfce4ff5a8aaf6 (Node.js GitHub Bot) #62052 - [
13eb80f3b7
] - tools: update nixpkgs-unstable to d1c15b7d5806069da59e819999d70e1cec0 (Node.js GitHub Bot) #61931 - [
4d1557a744
] - tools: update nixpkgs-unstable to 2343bbb58f99267223bc2aac4fc9ea301a1 (Node.js GitHub Bot) #61831 - [
ecd979c95a
] - tools: update nixpkgs-unstable to ae67888ff7ef9dff69b3cf0cc0fbfbcd3a7 (Node.js GitHub Bot) #61733 - [
7de56bdee2
] - tools: update nixpkgs-unstable to 6308c3b21396534d8aaeac46179c14c439a (Node.js GitHub Bot) #61606 - [
e33ce7a6fe
] - tools: update nixpkgs-unstable to ab9fbbcf4858bd6d40ba2bbec37ceb4ab6e (Node.js GitHub Bot) #61513 - [
ba05a66774
] - tools: update nixpkgs-unstable to be5afa0fcb31f0a96bf9ecba05a516c66fc (Node.js GitHub Bot) #61420 - [
bb5d066989
] - tools: update nixpkgs-unstable to 3146c6aa9995e7351a398e17470e15305e6 (Node.js GitHub Bot) #61340 - [
d050aa87e8
] - tools: update nixpkgs-unstable to 16c7794d0a28b5a37904d55bcca36003b91 (Node.js GitHub Bot) #61272 - [
2696391b18
] - tools: update nixpkgs-unstable to 3edc4a30ed3903fdf6f90c837f961fa6b49 (Node.js GitHub Bot) #61188 - [
c5d3f5f9c8
] - tools: update nixpkgs-unstable to 7d853e518814cca2a657b72eeba67ae20eb (Node.js GitHub Bot) #61137 - [
dcb9573d0f
] - tools: update nixpkgs-unstable to f997fa0f94fb1ce55bccb97f60d41412ae8 (Node.js GitHub Bot) #61057 - [
bd426739dc
] - tools: update nixpkgs-unstable to a672be65651c80d3f592a89b3945466584a (Node.js GitHub Bot) #60980 - [
85852a3221
] - tools: update nixpkgs-unstable to 59b6c96beacc898566c9be1052ae806f383 (Node.js GitHub Bot) #60900 - [
1e7eb90b39
] - tools: update nixpkgs-unstable to a8d610af3f1a5fb71e23e08434d8d61a466 (Node.js GitHub Bot) #60818 - [
fb6b83c9ef
] - tools: lint Temporal global (René) #60793 - [
adb40439ca
] - tools: update nixpkgs-unstable to 71cf367cc2c168b0c2959835659c38f0a34 (Node.js GitHub Bot) #60742 - [
8a76958005
] - tools: update nixpkgs-unstable to ffcdcf99d65c61956d882df249a9be53e59 (Node.js GitHub Bot) #60315 - [
9120924de1
] - util: fix nested proxy inspection (Ruben Bridgewater) #61077
Windows 64-bit Installer: https://nodejs.org/dist/v26.0.0/node-v26.0.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v26.0.0/node-v26.0.0-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v26.0.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v26.0.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v26.0.0/node-v26.0.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v26.0.0/node-v26.0.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v26.0.0/node-v26.0.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v26.0.0/node-v26.0.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v26.0.0/node-v26.0.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v26.0.0/node-v26.0.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v26.0.0/node-v26.0.0-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v26.0.0/node-v26.0.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v26.0.0/node-v26.0.0.tar.gz
Other release files: https://nodejs.org/dist/v26.0.0/
Documentation: https://nodejs.org/docs/v26.0.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
159ac4d97c5e9f9b58279933d877bd1aedcd8b99c069b7f93cc00d11e45c8dc3 node-v26.0.0-aix-ppc64.tar.gz
f3a6db3b60b4019a7ef67db9885b2b06aa756953e15db36602279c04cd10ea46 node-v26.0.0-arm64.msi
dcee8564c1a9342f9594dd5e52d533894dfef6b85aa771bbbb870baa3c403235 node-v26.0.0-darwin-arm64.tar.gz
880cf6f35eb9dea84b2373adba13b6023b50cc0decbad47b57824d146373265a node-v26.0.0-darwin-arm64.tar.xz
f488ab543fe202d8a2d56e661682117d3c56903a2bf64f2ec1ff7bd421cfd875 node-v26.0.0-darwin-x64.tar.gz
f4f05e8621191a4bef042e93881114429415f57a3b46411acd5fd94a87b7d660 node-v26.0.0-darwin-x64.tar.xz
cefe207f1f02075ed0e72dac1799188841b5d1e50eea83074feaea3d26960b11 node-v26.0.0-headers.tar.gz
222e3ef1477097190838f1a60c6ef6f00ce76ac2c8ff671a223bee1cfbac9d1d node-v26.0.0-headers.tar.xz
c802664b5770102999efacf5717854f7652797db522e8cc5727a6209afea824d node-v26.0.0-linux-arm64.tar.gz
f0f94e55142149a4d34634dc3d7e103921d898512dd0cef995ecb62c5ebd3f29 node-v26.0.0-linux-arm64.tar.xz
5e587ff6af1b837330e84d9bdcee3e5245839133f9ee5316da7363558996cd8a node-v26.0.0-linux-ppc64le.tar.gz
4b7f76967a93fea8cda11554f2a7904744afaef65dc3f48c345e99828f50ef4d node-v26.0.0-linux-ppc64le.tar.xz
b0b261771569352b62fde896447a7b8e40d9021555f1e0b6ee1edc7944889ac2 node-v26.0.0-linux-s390x.tar.gz
e3bd9df41f777dbb227b1261ea81b1fa9b654901bac8cace50a0b918b5160ab5 node-v26.0.0-linux-s390x.tar.xz
42cee4d7ec80b7f7c89281cf00726b14840ac674462404dd4fd36f03964dc0af node-v26.0.0-linux-x64.tar.gz
345d558514c62622b5c7d1f7b5f2a19c31ab1405d217df49f010c5ea8decc0f4 node-v26.0.0-linux-x64.tar.xz
480db15247e5362fd38a9a61093d07cac72a20e33439f30a6ceacc02e553f8f5 node-v26.0.0-win-arm64.7z
1931cebf3cda89dab7cc5d4d0bf1923b8eff8a4b054b6aaa8904be0c14a070a4 node-v26.0.0-win-arm64.zip
c94726676f5683b008b7fc6638e5ee9e8ea1cd25b72f20d66753e7cde2f69e1a node-v26.0.0-win-x64.7z
d0418640a36096e00bddb57761aa0b1b98f91904ec4ed2b9dd75cbad723becd7 node-v26.0.0-win-x64.zip
677460c6f7df29a97986e73daa931b4590a6fa841030f2c73f6b8186ee078868 node-v26.0.0-x64.msi
2fe389c0e111992b691b320bc00f83b69119ead702eef7cdec639e19796b24db node-v26.0.0.pkg
db0b0db9238d93e41a110d6f14bd43984e56475cb7d8e218d1f73b6ad39b71c7 node-v26.0.0.tar.gz
fcb5e5c06a5c2ec9e669801248657aafaa2291f8760dac7bfb639f878318c592 node-v26.0.0.tar.xz
1f0beb48cfd080c56d94a3eaae1da1f2dd3ec42d0028457c16667248c04f4e32 win-arm64/node.exe
77b20d81472caffdcf60bbd76d623961c81208af359b97f19e215f8c85943942 win-arm64/node.lib
531b9f46d2d3a2ca35421d7f5f8eea3ca7802cdafb27b4ab954e08396772d2cb win-arm64/node_pdb.7z
1e5a847170bb96a302c478a03a178a32f6099cb7128ca95bbcd7e5959581ccb6 win-arm64/node_pdb.zip
2d0458fa3dc95948f2101fa9ea0840321e14c117379f422ee4cec8bd802d08b2 win-x64/node.exe
f870fc3af0b3d8c6e79b5d10f5872e472beefc6e4051b97eb825a801bc00eb52 win-x64/node.lib
7c7102fca58274d9740b027c7461c14d754a50b1c0cae2c510b76da831548ed9 win-x64/node_pdb.7z
44778c071d6d715cf266e095fdd72a4a5d25e2e857f12c2347e96e3ff994766d win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQGzBAEBCAAdFiEEiQwI24V5Fi/uDfnbi+q0389VXvQFAmn5/KgACgkQi+q0389V
XvTjxwv+MBmEKWdgo2Jlk8YlyijOB0DWUhVHIcgYCoWMUWF5gojrhd2VXi8dWNPL
rEM9271reuZ2mAf5N+jYY+nP/CgxTpwvMmcgG4V+XlCEQ/arW15Jwox8tBuzWqmM
Dw8+UTW+W0ura/UMaBJkFU01IfsYI6r6xG4Ek/3aq1JBFVvNIQTxk0LFl7hiFh6v
9Ip/sQ8L/HM3uvaenPMpfHb4htYEvWhLJ7iaXszhhplAdBskGSjR2SQttQNvPcDM
9RDN0/xNIQq76wgy+SvzrREvCZarOLOOzo7Ij+346H7aRpquwMagCSG/WAteXBqc
JgBQyCpYGZz1C6/ACcqhI8xVm2Duz1iw/JzGZE9V4DHVoFAR4OZUb6xkENrW3vob
AlXrqrAvs5T+wXkEJ6UQySrEgAAfczrgYiwqfbDZlnxEMnwSPRR50b2ozaJv9i4K
3fLD6G26/mhd8dnlejc0uXIepNTjGNQbiS+xoyNAqn/hDlZj8v2UqhFVOlTdpZ1D
t7tZbpQ/
=aRkl
-----END PGP SIGNATURE-----
```

---

## 3. Trip report: Node.js collaboration summit (2026 London)

- 日期: 2026-04-24 00:00
- 链接: https://nodejs.org/en/blog/events/collab-summit-2026-london

```
Trip report: Node.js collaboration summit (2026 London)
Chengzhong Wu, Joyee Cheung
This April, the first Node.js Collaboration Summit of 2026 was hosted by Bloomberg in London. In this edition, we welcomed over 40 in-person participants, and around a dozen more joined remotely.
The recording of the summit is available in this playlist. Here is a recap of what happened at the summit.
Next 10
In this session, Jacob Smith reviewed results from the Collaborator Health survey and compared health numbers between 2025 and 2026, as well as some key highlights from the 2025 user survey (including new areas, which have generally different usage); he and Marco Ippolito led an on-site review of the questions that would be asked in the Next-10 survey for 2026, including suggestions to existing questions, questions and options to add or remove, and recent AI discussions.
New Release Schedule
Rafael Gonzaga walked the audience through the new release schedule that will go into effect starting with Node.js v27. TL;DR, starting with Node.js v27, the Node.js version numbers align with the calendar year of their initial Current release!
This is a reflection of the current Node.js volunteer-based maintenance and an effort to keep the Node.js project sustainable in the long run. When it comes to security vulnerabilities, managing security releases across four or five active release lines has become difficult to sustain in the current Node.js voluntary work model. By reducing the number of concurrent release lines, the project can focus on better supporting the releases people actually use.
Read more about the new release schedule in this blog post.
New Streams API
James Snell presented a new, more unified Streams API for the Web and Node.js. Historically, Node.js has relied on the highly optimized node:stream
. In recent years, Node.js has also implemented WHATWG Web Streams to ensure cross-platform compatibility with browsers, Deno, Bun, and edge environments (like Cloudflare Workers). However, managing two different stream ecosystems has created friction for developers.
The Web Streams API has significant promise and allocation overhead. It was designed primarily for browsers, and when applied to high-throughput backend environments, the architectural cost becomes obvious.
The proposed New Streams API takes advantage of modern JavaScript Async Iteration, treats streams natively as async iterables, leaning heavily into async/await
and for await...of
loops, which is how modern developers naturally write code. Handling a filled data buffer has historically been a confusing black box. The new API also proposes forcing developers to explicitly choose a backpressure strategy when a buffer is full.
The new stream/iter
API has landed in Node.js core and shipped in v25.9.0 as an experimental feature. At the summit, we collected feedback on the design, compatibility with existing stream APIs, performance implications, additional use cases, whether the new proposal can help address some common issues in the existing APIs, and discussed whether the new Streams API can be implemented on the Web.
Node.js Collaboratorship
Jacob Smith led the session on exploring ways to lower the barrier to entry for developers who want to contribute to the Node.js core, ensuring the project remains accessible to new talent.
Triaging issues and reviewing pull requests takes a massive amount of maintainer bandwidth. At the session, we discussed ideas to enforce code ownership to encourage collaborators to take over more review work. Since in the Node.js voluntary work model, this can come with difficulties, we also brainstormed ideas about decoupling collaboratorship from the commit bits and extending reviewership to working group/team members, in order to encourage non-collaborators to review and build trust. We'll continue the discussions on GitHub.
OpenTelemetry
Chengzhong Wu presented the CNCF OpenTelemetry project. The session was prompted by a pull request from Bryan English to add Node.js built-in OpenTelemetry support. OpenTelemetry is one of the most active projects in the Cloud Native Computing Foundation, right after Kubernetes. OpenTelemetry has emerged as the de-facto standard in the world of observability with three pillars: traces, metrics, and logs. The project defines a vendor-neutral API for instrumentation and an SDK with a data processing pipeline. Apart from the OpenTelemetry API and SDK, there are also efforts to define Semantic Conventions (SemConv) and the native data format OpenTelemetry Protocol (OTLP) for sending telemetry data to backends. OpenTelemetry is an open governance project and consists of contributors from both vendors and users.
Observability Infrastructure
Stephen Belanger shared thoughts and work on improving Node.js observability infrastructure. The presentation covered using
syntax support for AsyncLocalStorage
and a new diagnostic_channel
API BoundedChannel
. Furthermore, Stephen presented ideas about new Node.js built-in modules for metrics and traces respectively, and the potential to add built-in support for the OpenTelemetry OTLP data protocol, improving OpenTelemetry serialization performance.
Node.js use of AI contributions
A few weeks before the summit, a large pull request implementing VFS in Node.js with the assistance of an AI coding agent led to debates over the use of AI in Node.js core. In this session, Jacob Smith walked the audience through the background of this controversy, the legal opinion from the OpenJS foundation, and the current status of the use of AI in other OSS projects.
We then started listing pros & cons, concerns and thoughts about the use of AI in Node.js core using a retrospective board. There were a lot of diverse opinions about this topic. At the session, we discussed the challenges from reviewer bandwidth exacerbated by the use of AI, the ethical concerns about AI, whether a ban is feasible or desirable, whether a disclosure on the use of AI may help or draw further legal and ethical concerns, how AI may help maintenance and lower barrier of entry, and ideas on reducing the amount of noise caused by the use of AI.
We also brainstormed how to adapt open-source governance for the modern era. Strategies discussed include enforcing a process that requires lightweight design documents, RFCs, explicit maintainer buy-in before a large PR, and pledge from the human contributor submitting the code who should take full responsibility for its quality, security, and integration. We'll continue the discussions and iteration of the policy documents on GitHub.
Userland migrations
Jacob Smith and Bruno Rodrigues presented increased usage of userland migrations. Migrations for Node.js 22.x to 24.x deprecations are almost complete. For Node.js 25.9.0, a codemod was published along side the deprecation introduced.
Stabilization of module customization hooks and vm.Modules
Joyee Cheung facilitated a session to discuss the stabilization of module loader hooks and the vm Module API.
As module.register()
is set to be doc-deprecated for 25 and below and runtime-deprecated for 26 and above due to maintenance issues, we are looking into helping the ecosystem migrate to the module.registerHooks()
API. Ideas include providing a userland ponyfill that re-implements most of the module.register()
functionality using module.registerHooks()
, and having some userland-migration automation tools to help facilitate migration.
Joyee also presented a new design for the vm Module APIs that have been experimental for 9 years in order to address known issues and finally bring it to stabilization. We collected feedback on how to integrate it with WebAssembly modules to ensure it's future-proof with ongoing ESM integration proposals in standardization bodies. We'll continue iterating on the design in the GitHub issue.
Libuv v2
Santiago Gimeno shared that after more than a decade on version 1, there is a renewed push to launch libuv v2, which introduces necessary breaking changes to clean up the codebase, remove legacy APIs, and improve cross-platform consistency—capabilities already being leveraged by Julia.
As migrating to libuv v2 can break the ABI, we discussed ideas on how to mitigate it, for example by leveraging Node-API, and the nuances in this approach e.g. napi_get_uv_event_loop
can still be impacted by libuv ABI changes, though its use is limited and its ABI stability is warned in the documentation. We also discussed getting help to maintain v1 with security patches for a limited timespan, how to bring back io_uring
, and which Node.js can start to ship libuv v2 (a very tentative timeline could be in 27).
Node.js Virtual File System
Matteo Collina presented the proposal for a Node.js built-in Virtual File System. By taking concepts previously explored in userland libraries (like @platformatic/vfs
) and standardizing them into a core node:vfs
module, Node.js can intercept standard filesystem calls and route them through a virtualized, memory-based layer. Developers can define specific data sources in memory (providers) and "mount" them so the runtime treats them exactly like local directories. The proposal also provides the ability to layer virtual filesystems on top of one another, or place a virtual layer directly over the physical disk to safely mock or override files.
In this session, Matteo walked the audience through the motivation of this feature: making file system virtualization easier for single-executable applications and testing, and replaces existing brittle practices that achieve this through user-land monkey-patching. Following a brief overview of the implementation architecture and the design choices, we collected more feedback on the PR, including stack trace visibility, observability, security, worker thread propagation, the ability to toggle it in specific paths, and support in native code. We'll continue iterating on this PR in GitHub.
Node.js Security - State of the Ecosystem & What's Next
Rafael Gonzaga shared that the security team has recently advanced the ecosystem through a refined threat model, improved permission models, and enhanced release automation, and the new VEX (Vulnerability Exploitability eXchange) files that the security team is working on to reduce false positives for security scanners.
These efforts are currently being overshadowed by a massive influx of AI-generated vulnerability reports. This industry-wide surge, driven largely by users seeking CVE attribution and financial bounties, has severely strained maintainer capacity with high-noise, duplicative submissions that often lack reproduction steps or misclassify standard bugs as severe security threats. Despite attempted mitigations like pausing bug bounties, raising HackerOne signal requirements, and clarifying guidelines, the overwhelming volume has significantly driven up resolution times. To combat this bottleneck, the team is exploring strategies such as securing early access for proactive testing, attempting to alter reporting agent behaviors, and adopting a public security flow to bypass embargoes and speed up CI testing.
In the session we revisited a thought-provoking proposal of making the security triage and bugfix process completely public to prevent a false sense of security in the age of AI, and to get rid of the CI embargo that has made testing inefficient. We discussed a few middle ground solutions, including keeping extending the visibility to more members in the organization, handling vulnerabilities of different severity with different visibility settings, and creating better documentations to drive AI agents away from generating false positive reports.
Thanks
Thank you to all the attendees! Special appreciation goes to Bloomberg for hosting the summit and creating a welcoming space for the Node.js community.
A big thanks as well to Thomas Chetwin (@tchetwin), Chengzhong Wu, Matteo Collina, Joyee Cheung, and the OpenJS Foundation for organizing and making this event possible.
The Node.js Collaboration Summit recordings are now available at YouTube.
```

---

## 4. Node.js 24.15.0 (LTS)

- 日期: 2026-04-15 18:17
- 链接: https://nodejs.org/en/blog/release/v24.15.0

```
Node.js 24.15.0 (LTS)
Antoine du Hamel
2026-04-15, Version 24.15.0 'Krypton' (LTS), @aduh95
Notable Changes
- [
3d87ecacbc
] - (SEMVER-MINOR) cli: add --max-heap-size option (tannal) #58708 - [
83c38672f7
] - cli: add --require-module/--no-require-module (Joyee Cheung) #60959 - [
54ef940e01
] - (SEMVER-MINOR) crypto: add raw key formats support to the KeyObject APIs (Filip Skokan) #62240 - [
f4a3edc47a
] - (SEMVER-MINOR) fs: addthrowIfNoEntry
option for fs.stat and fs.promises.stat (Juan José) #61178 - [
5cdcba17cc
] - (SEMVER-MINOR) http2: add http1Options for HTTP/1 fallback configuration (Amol Yadav) #61713 - [
8b6be3fe14
] - module: mark require(esm) as stable (Joyee Cheung) #60959 - [
68fbc0c6cc
] - module: mark module compile cache as stable (Joyee Cheung) #60971 - [
c851e76f8c
] - (SEMVER-MINOR) net: addsetTOS
andgetTOS
toSocket
(Amol Yadav) #61503 - [
6ac4304c87
] - (SEMVER-MINOR) sqlite: add limits property to DatabaseSync (Mert Can Altin) #61298 - [
aaf9af1672
] - sqlite: mark as release candidate (Matteo Collina) #61262 - [
eb77a7a297
] - (SEMVER-MINOR) src: add C++ support for diagnostics channels (RafaelGSS) #61869 - [
6834ca13bb
] - (SEMVER-MINOR) stream: renameDuplex.toWeb()
type option toreadableType
(René) #61632 - [
f5f21d36a6
] - test_runner: add exports option for module mocks (sangwook) #61727 - [
1f2025fd1e
] - (SEMVER-MINOR) test_runner: expose worker ID for concurrent test execution (Ali Hassan) #61394 - [
1ca20fc33d
] - (SEMVER-MINOR) test_runner: show interrupted test on SIGINT (Matteo Collina) #61676
Commits
- [
148373cea1
] - assert,util: improve comparison performance (Ruben Bridgewater) #61176 - [
e5558b0859
] - assert,util: fix deep comparing invalid dates skipping properties (Ruben Bridgewater) #61076 - [
83cffd92b5
] - async_hooks: enabledHooksExist shall return if hooks are enabled (Gerhard Stöbich) #61054 - [
2c9436b43d
] - benchmark: fix destructuring in dgram/single-buffer (Ali Hassan) #62084 - [
837acd7382
] - benchmark: add startup benchmark for ESM entrypoint (Joyee Cheung) #61769 - [
a6ced7d272
] - buffer: improve performance of multiple Buffer operations (Ali Hassan) #61871 - [
a82003bf8b
] - buffer: optimize buffer.concat performance (Mert Can Altin) #61721 - [
83dfd0be1d
] - buffer: disallow ArrayBuffer transfer on pooled buffer (Chengzhong Wu) #61372 - [
ed2d0cb1bf
] - build: support empty libname flags inconfigure.py
(Antoine du Hamel) #62477 - [
09f7920267
] - build: fix timezone-update path references (Chengzhong Wu) #62280 - [
af46b15b91
] - build: use path-ignore in GHA coverage-windows.yml (Chengzhong Wu) #61811 - [
2cf77eadd1
] - build: generate_config_gypi.py generates valid JSON (Shelley Vohr) #61791 - [
e0220f0c35
] - build: build with v8 gdbjit support on supported platform (Joyee Cheung) #61010 - [
5505511dcb
] - build: enable -DV8_ENABLE_CHECKS flag (Ryuhei Shima) #61327 - [
5f8ecf3940
] - build: add --debug-symbols to build with -g without enabling DCHECKs (Joyee Cheung) #61100 - [
ab18c0867b
] - build: fix --node-builtin-modules-path (Filip Skokan) #62115 - [
bfa60d5782
] - build: fix GN for new merve dep (Shelley Vohr) #61984 - [
0d1975fe3a
] - build,win: add WinGet Visual Studio 2022 Build Tools Edition config (Mike McCready) #61652 - [
10b2bb5fa6
] - child_process: add tracing channel for spawn (Marco) #61836 - [
3d87ecacbc
] - (SEMVER-MINOR) cli: add --max-heap-size option (tannal) #58708 - [
83c38672f7
] - cli: add --require-module/--no-require-module (Joyee Cheung) #60959 - [
9d37233824
] - crypto: update root certificates to NSS 3.121 (Node.js GitHub Bot) #62485 - [
b0cbfe38a4
] - crypto: add crypto::GetSSLCtx API for addon access to OpenSSL contexts (Tim Perry) #62254 - [
dc034a4ac9
] - crypto: reject ML-KEM/ML-DSA PKCS#8 import without seed in SubtleCrypto (Filip Skokan) #62218 - [
8aa6e706df
] - crypto: refactor WebCrypto AEAD algorithms auth tag handling (Filip Skokan) #62169 - [
20cb932bcf
] - crypto: read algorithm name property only once in normalizeAlgorithm (Filip Skokan) #62170 - [
e2934162b4
] - crypto: add missing AES dictionaries (Filip Skokan) #62099 - [
8b8db52f65
] - crypto: fix importKey required argument count check (Filip Skokan) #62099 - [
bd5458db29
] - crypto: fix missing nullptr check on RSA_new() (ndossche) #61888 - [
7302c7ed22
] - crypto: fix handling of null BUF_MEM* in ToV8Value() (Nora Dossche) #61885 - [
8d0c22ea20
] - crypto: fix potential null pointer dereference when BIO_meth_new() fails (Nora Dossche) #61788 - [
72aad8b40f
] - crypto: always return certificate serial numbers as uppercase (Anna Henningsen) #61752 - [
2395fc0f4d
] - crypto: rename CShakeParams and KmacParams length to outputLength (Filip Skokan) #61875 - [
541be3aaf2
] - crypto: recognize raw formats in keygen (Filip Skokan) #62480 - [
54ef940e01
] - (SEMVER-MINOR) crypto: add raw key formats support to the KeyObject APIs (Filip Skokan) #62240 - [
bef1949823
] - deps: V8: cherry-pick 33e7739c134d (Thibaud Michaud) #62567 - [
2e1a565a55
] - deps: update ada to 3.4.4 (Node.js GitHub Bot) #62414 - [
d0418bad10
] - deps: update timezone to 2026a (Node.js GitHub Bot) #62164 - [
53aad66415
] - deps: update googletest to 2461743991f9aa53e9a3625eafcbacd81a3c74cd (Node.js GitHub Bot) #62484 - [
90fab71a84
] - deps: update simdjson to 4.5.0 (Node.js GitHub Bot) #62382 - [
a416ddf6d9
] - deps: V8: cherry-pick cf1bce40a5ef (Richard Lau) #62449 - [
4d9123e57d
] - deps: upgrade npm to 11.12.1 (npm team) #62448 - [
952d715028
] - deps: update sqlite to 3.51.3 (Node.js GitHub Bot) #62256 - [
f3fd7ed426
] - deps: update googletest to 73a63ea05dc8ca29ec1d2c1d66481dd0de1950f1 (Node.js GitHub Bot) #61927 - [
71a2f82d7c
] - deps: upgrade npm to 11.11.1 (npm team) #62216 - [
84f60c26f7
] - deps: update amaro to 1.1.8 (Node.js GitHub Bot) #62151 - [
43159d0e5f
] - deps: update sqlite to 3.52.0 (Node.js GitHub Bot) #62150 - [
b887657b38
] - deps: V8: cherry-pick aa0b288f87cc (Richard Lau) #62136 - [
7ab885b323
] - deps: update ada to 3.4.3 (Node.js GitHub Bot) #62049 - [
671ddec2b9
] - deps: update minimatch to 10.2.4 (Node.js GitHub Bot) #62016 - [
290fe37d4d
] - deps: update simdjson to 4.3.1 (Node.js GitHub Bot) #61930 - [
a13bee76b5
] - deps: update acorn-walk to 8.3.5 (Node.js GitHub Bot) #61928 - [
f0e40b35b9
] - deps: update acorn to 8.16.0 (Node.js GitHub Bot) #61925 - [
463dfa023a
] - deps: update minimatch to 10.2.2 (Node.js GitHub Bot) #61830 - [
4b2e4bb108
] - deps: update nbytes to 0.1.3 (Node.js GitHub Bot) #61879 - [
5626cb83d0
] - deps: remove stale OpenSSL arch configs (René) #61834 - [
52668874fd
] - deps: update llhttp to 9.3.1 (Node.js GitHub Bot) #61827 - [
b3387b07b1
] - deps: update googletest to 5a9c3f9e8d9b90bbbe8feb32902146cb8f7c1757 (Node.js GitHub Bot) #61731 - [
196268cb4c
] - deps: V8: cherry-pick c5ff7c4d6cde (Chengzhong Wu) #61372 - [
36869b52de
] - deps: update merve to 1.2.2 (Node.js GitHub Bot) #62213 - [
3cbac055de
] - deps: update merve to 1.2.0 (Node.js GitHub Bot) #62149 - [
7757cc3495
] - deps: V8: backport 6a0a25abaed3 (Vivian Wang) #61670 - [
359797c2fb
] - deps,src: prepare for cpplint update (Michaël Zasso) #60901 - [
ace802e59b
] - diagnostics_channel: add diagnostics channels for web locks (Ilyas Shabi) #62123 - [
a072411b03
] - doc: remove spawn with shell example from bat/cmd section (Kit Dallege) #62243 - [
0b152449af
] - doc: fix typo in --disable-wasm-trap-handler description (Dmytro Semchuk) #61820 - [
73ea387ad7
] - doc: remove obsolete Boxstarter automated install (Mike McCready) #61785 - [
7f234add8e
] - doc: deprecatemodule.register()
(DEP0205) (Geoffrey Booth) #62395 - [
12fc3c6a30
] - doc: clarify that features cannot be both experimental and deprecated (Antoine du Hamel) #62456 - [
1ecc5962a2
] - doc: fix 'transfered' typo in quic.md (lilianakatrina684-a11y) #62492 - [
56741a1303
] - doc: move sqlite type conversion section to correct level (René) #62482 - [
12b04d17d5
] - doc: add Rafael to last security release steward (Rafael Gonzaga) #62423 - [
c4567e4a8d
] - doc: fix overstated Date header requirement in response.sendDate (Kit Dallege) #62206 - [
384a41047f
] - doc: enhance clarification about the main field (Mowafak Almahaini) #62302 - [
93d19b1a1c
] - doc: minor typo fix (Jeff Matson) #62358 - [
3db35d2c59
] - doc: add path to vulnerabilities.json mention (Rafael Gonzaga) #62355 - [
57b105c9d5
] - doc: deprecate CryptoKey use in node:crypto (Filip Skokan) #62321 - [
490168c993
] - doc: fix small environment_variables typo (chris) #62279 - [
0291be584b
] - doc: test and test-only targets do not run linter (Xavier Stouder) #62120 - [
ba0a82a1e1
] - doc: clarify fs.ReadStream and fs.WriteStream are not constructable (Kit Dallege) #62208 - [
125bdbf504
] - doc: clarify that any truthy value ofshell
is part of DEP0190 (Antoine du Hamel) #62249 - [
a141ad0aeb
] - doc: remove outdated Chrome 66 and ndb references from debugger (Kit Dallege) #62202 - [
44bde8e573
] - doc: add note (and caveat) formock.module
about customization hooks (Jacob Smith) #62075 - [
8c46a1ca1a
] - doc: copyeditaddons.md
(Antoine du Hamel) #62071 - [
7f989f02f7
] - doc: correctutil.convertProcessSignalToExitCode
validation behavior (René) #62134 - [
a4466ebdac
] - doc: add efekrskl as triager (Efe) #61876 - [
db516eca3a
] - doc: fix markdown forexpectFailure
values (Jacob Smith) #62100 - [
ad97045125
] - doc: include url.resolve() in DEP0169 application deprecation (Mike McCready) #62002 - [
309f37ba42
] - doc: expand SECURITY.md with non-vulnerability examples (Rafael Gonzaga) #61972 - [
dbb3551b7b
] - doc: separate in-types and out-types in SQLite conversion docs (René) #62034 - [
191c433db8
] - doc: fix small logic error in DETECT_MODULE_SYNTAX (René) #62025 - [
8511b1c784
] - doc: fix module.stripTypeScriptTypes indentation (René) #61992 - [
dd1139f52c
] - doc: update DEP0040 (punycode) to application type deprecation (Mike McCready) #61916 - [
54009e9c62
] - doc: explicitly mention Slack handle (Rafael Gonzaga) #61986 - [
78fa1a1a49
] - doc: support toolchain Visual Studio 2022 & 2026 + Windows 11 SDK (Mike McCready) #61864 - [
d8204d3cdb
] - doc: rename invalidfunction
parameter (René) #61942 - [
a5a14482fb
] - doc: clarify status of feature request issues (Antoine du Hamel) #61505 - [
bd0688feb6
] - doc: add esm and cjs examples to node:vm (Alfredo González) #61498 - [
240b512f9f
] - doc: clarify build environment is trusted in threat model (Matteo Collina) #61865 - [
5dd48e3456
] - doc: remove incorrect mention ofmodule
intypescript.md
(Rob Palmer) #61839 - [
9502c22055
] - doc: simplify addAbortListener example (Chemi Atlow) #61842 - [
6fec397828
] - doc: clean up globals.md (René) #61822 - [
a810f5ccef
] - doc: clarify async caveats forevents.once()
(René) #61572 - [
2bf990bb1a
] - doc: update Juan's security steward info (Juan José) #61754 - [
0312db948d
] - doc: fix methods being documented as properties inprocess.md
(Antoine du Hamel) #61765 - [
e558b26e7f
] - doc: add riscv64 info into platform list (Lu Yahan) #42251 - [
49254e3dc0
] - doc: fix dropdown menu being obscured at <600px due to stacking context (Jeff) #61735 - [
4ff01b5c10
] - doc: fix spacing in process message event (Aviv Keller) #61756 - [
94097a79d6
] - doc: move describe/it aliases section before expectFailure (Luca Raveri) #61567 - [
b7cd31acbe
] - doc: fix broken links of net.md (YuSheng Chen) #61673 - [
ae5e353fe2
] - doc: clean up Windows code snippet inchild_process.md
(reillylm) #61422 - [
ea9beb6a3c
] - doc: update to Visual Studio 2026 manual install (Mike McCready) #61655 - [
42057c84e2
] - doc,module: add missing doc for syncHooks.deregister() (Joyee Cheung) #61959 - [
a035bd5235
] - doc,test: clarify --eval syntax for leading '-' scripts (kovan) #62244 - [
deb0b78460
] - esm: fix typo in worker loader hook comment (jakecastelli) #62475 - [
b93bf7dbfc
] - esm: fix source phase identity bug in loadCache eviction (Guy Bedford) #62415 - [
679d18b57f
] - esm: fix path normalization infinalizeResolution
(Antoine du Hamel) #62080 - [
171e9fc268
] - esm: update outdated FIXME comment in translators.js (Karan Mangtani) #61715 - [
cc19728228
] - events: avoid cloning listeners array on every emit (Gürgün Dayıoğlu) #62261 - [
458c92be52
] - events: don't call resume after close (Сковорода Никита Андреевич) #60548 - [
4691f3e7fb
] - fs: fix cpSync to handle non-ASCII characters (Stefan Stojanovic) #61950 - [
f4a3edc47a
] - (SEMVER-MINOR) fs: addthrowIfNoEntry
option for fs.stat and fs.promises.stat (Juan José) #61178 - [
58e4d50cd0
] - http: fix use-after-free when freeParser is called during llhttp_execute (Gerhard Stöbich) #62095 - [
0a4ad85ab0
] - http: validate ClientRequest path on set (Matteo Collina) #62030 - [
f8178ac3e6
] - http: validate headers in writeEarlyHints (Richard Clarke) #61897 - [
899884d0ed
] - http: remove redundant keepAliveTimeoutBuffer assignment (Efe) #61743 - [
08d2e40694
] - http: attach error handler to socket synchronously in onSocket (RajeshKumar11) #61770 - [
1c2064c1f8
] - http: fix keep-alive socket reuse race in requestOnFinish (Martin Slota) #61710 - [
38e9c66e0f
] - http2: add strictSingleValueFields option to relax header validation (Tim Perry) #59917 - [
5cdcba17cc
] - (SEMVER-MINOR) http2: add http1Options for HTTP/1 fallback configuration (Amol Yadav) #61713 - [
687c0acd00
] - http2: fix FileHandle leak in respondWithFile (sangwook) #61707 - [
0c8f802ec2
] - inspector: add Target.getTargets and extract TargetManager (Kohei) #62487 - [
7de8a303c1
] - inspector: unwrap internal/debugger/inspect imports (René) #61974 - [
59ac10a4fd
] - lib: make SubtleCrypto.supports enumerable (Filip Skokan) #62307 - [
9dc102ba90
] - lib: prefer primordials in SubtleCrypto (Filip Skokan) #62226 - [
78a9aa8f32
] - lib: fix source map url parse in dynamic imports (Chengzhong Wu) #61990 - [
16b8cc6643
] - lib: improve argument handling in Blob constructor (Ms2ger) #61980 - [
a03b5d39b8
] - lib: reduce cycles in esm loader and load it in snapshot (Joyee Cheung) #61769 - [
1017bf5f86
] - lib: remove top-level getOptionValue() calls in lib/internal/modules (Joyee Cheung) #61769 - [
d79984b41b
] - lib: optimize styleText when validateStream is false (Rafael Gonzaga) #61792 - [
6462b89d10
] - meta: bump actions/download-artifact from 7.0.0 to 8.0.0 (dependabot[bot]) #62063 - [
5bb89916ea
] - meta: bump actions/upload-artifact from 6.0.0 to 7.0.0 (dependabot[bot]) #62062 - [
b067d74d94
] - meta: bump step-security/harden-runner from 2.14.2 to 2.15.0 (dependabot[bot]) #62064 - [
830e5cd125
] - meta: bump github/codeql-action from 4.32.0 to 4.32.4 (dependabot[bot]) #61911 - [
16c839a3dd
] - meta: bump step-security/harden-runner from 2.14.1 to 2.14.2 (dependabot[bot]) #61909 - [
498abf661e
] - meta: bump actions/stale from 10.1.1 to 10.2.0 (dependabot[bot]) #61908 - [
78ac17f426
] - module: fix coverage of mocked CJS modules imported from ESM (Marco) #62133 - [
46cfad4138
] - module: run require.resolve through module.registerHooks() (Joyee Cheung) #62028 - [
8b6be3fe14
] - module: mark require(esm) as stable (Joyee Cheung) #60959 - [
68fbc0c6cc
] - module: mark module compile cache as stable (Joyee Cheung) #60971 - [
c851e76f8c
] - (SEMVER-MINOR) net: addsetTOS
andgetTOS
toSocket
(Amol Yadav) #61503 - [
4c206ecb31
] - quic: remove CryptoKey support from session keys option (Filip Skokan) #62335 - [
2f9c085cf5
] - sqlite: handle stmt invalidation (Guilherme Araújo) #61877 - [
6ac4304c87
] - (SEMVER-MINOR) sqlite: add limits property to DatabaseSync (Mert Can Altin) #61298 - [
aaf9af1672
] - sqlite: mark as release candidate (Matteo Collina) #61262 - [
7d67e5d693
] - src: convert context_frame field in AsyncWrap to internal field (Anna Henningsen) #62103 - [
d8ea1aaa8a
] - src: make AsyncWrap subclass internal field counts explicit (Anna Henningsen) #62103 - [
1dbf3bedbe
] - src: improve EC JWK import performance (Filip Skokan) #62396 - [
cd84af747b
] - src: handle null backing store in ArrayBufferViewContents::Read (Mert Can Altin) #62343 - [
4f553cdc01
] - src: enable compilation/linking with OpenSSL 4.0 (Filip Skokan) #62410 - [
70f8057258
] - src: use stack allocation in indexOf latin1 path (Mert Can Altin) #62268 - [
d788467b6a
] - src: expose async context frame debugging helper to JS (Anna Henningsen) #62103 - [
4213f893ec
] - src: release context frame in AsyncWrap::EmitDestroy (Gerhard Stöbich) #61995 - [
79fb8cbcf5
] - src: use validate_ascii_with_errors instead of validate_ascii (Сковорода Никита Андреевич) #61122 - [
2df328d59e
] - src: fix flags argument offset in JSUdpWrap (Weixie Cui) #61948 - [
eb77a7a297
] - (SEMVER-MINOR) src: add C++ support for diagnostics channels (RafaelGSS) #61869 - [
6cda3d30c0
] - src: remove unnecessaryc_str()
conversions in diagnostic messages (Anna Henningsen) #61786 - [
26c6045363
] - src: use bool literals in TraceEnvVarOptions (Tobias Nießen) #61425 - [
3c8f700fd7
] - src: track allocations made by zstd streams (Anna Henningsen) #61717 - [
94dbb36d4d
] - src: do not store compression methods on Brotli classes (Anna Henningsen) #61717 - [
bef661f182
] - src: extract zlib allocation tracking into its own class (Anna Henningsen) #61717 - [
e8079a8297
] - src: release memory for zstd contexts inClose()
(Anna Henningsen) #61717 - [
6e1197a3cc
] - src: add more checks and clarify docs for external references (Joyee Cheung) #61719 - [
c28a22c4be
] - src: fix cjs_lexer external reference registration (Joyee Cheung) #61718 - [
9e2c5fd7c9
] - src: simply uint32 to string as it must not fail (Chengzhong Wu) #60846 - [
df435d32b8
] - src: build v8 tick processor as built-in source text modules (Joyee Cheung) #60518 - [
2cb3573735
] - src,sqlite: fix filterFunc dangling reference (Edy Silva) #62281 - [
c44f53b544
] - stream: preserve error over AbortError in pipeline (Marco) #62113 - [
dc541370b4
] - stream: replace bind with arrow function for onwrite callback (Ali Hassan) #62087 - [
f6cdfbfaa7
] - stream: optimize webstreams pipeTo (Mattias Buelens) #62079 - [
fcf2a9f788
] - stream: fix brotli error handling in web compression streams (Filip Skokan) #62107 - [
cdec579c6b
] - stream: improve Web Compression spec compliance (Filip Skokan) #62107 - [
dbe5898379
] - stream: fix UTF-8 character corruption in fast-utf8-stream (Matteo Collina) #61745 - [
531e62cd74
] - stream: fix TransformStream race on cancel with pending write (Marco) #62040 - [
a3751f2249
] - stream: accept ArrayBuffer in CompressionStream and DecompressionStream (조수민) #61913 - [
65aa8f68d0
] - stream: fix pipeTo to defer writes per WHATWG spec (Matteo Collina) #61800 - [
15f32b4935
] - stream: fix decoded fromList chunk boundary check (Thomas Watson) #61884 - [
569767e52e
] - stream: add fast paths for webstreams read and pipeTo (Matteo Collina) #61807 - [
6834ca13bb
] - (SEMVER-MINOR) stream: renameDuplex.toWeb()
type option toreadableType
(René) #61632 - [
5ed5474437
] - test: update WPT for WebCryptoAPI to 2cb332d710 (Node.js GitHub Bot) #62483 - [
3c9c0f8577
] - test: fix test-buffer-zero-fill-cli to be effective (Сковорода Никита Андреевич) #60623 - [
19a52a1abe
] - test: update WPT for url to fc3e651593 (Node.js GitHub Bot) #62379 - [
111ba9bd5b
] - test: wait for reattach before initial break on restart (Yuya Inoue) #62471 - [
0897c6cc08
] - test: disable flaky WPT Blob test on AIX (James M Snell) #62470 - [
1c3d93bfab
] - test: avoid flaky run wait in debugger restart test (Yuya Inoue) #62112 - [
83416a640a
] - test: skip test-cluster-dgram-reuse on AIX 7.3 (Stewart X Addison) #62238 - [
af8d0922dd
] - test: add WebCrypto Promise.prototype.then pollution regression tests (Filip Skokan) #62226 - [
fc9a60ec74
] - test: update WPT for WebCryptoAPI to 6a1c545d77 (Node.js GitHub Bot) #62187 - [
12ba2d74fe
] - test: update WPT for url to c928b19ab0 (Node.js GitHub Bot) #62148 - [
4e15e5b647
] - test: update WPT for WebCryptoAPI to c9e955840a (Node.js GitHub Bot) #62147 - [
dc66a05558
] - test: improve WPT report runner (Filip Skokan) #62107 - [
9536e5621b
] - test: update WPT compression to ae05f5cb53 (Filip Skokan) #62107 - [
fb1c0bda0a
] - test: update WPT for WebCryptoAPI to 42e47329fd (Node.js GitHub Bot) #62048 - [
d886f27485
] - test: fix skipping behavior fortest-runner-run-files-undefined
(Antoine du Hamel) #62026 - [
f79df03e0b
] - test: remove unnecessaryprocess.exit
calls from test files (Antoine du Hamel) #62020 - [
1319295467
] - test: skiptest-url
on--shared-ada
builds (Antoine du Hamel) #62019 - [
2ea06727c6
] - test: skip strace test with shared openssl (Richard Lau) #61987 - [
c0680d5df7
] - test: avoid flaky debugger restart waits (Yuya Inoue) #61773 - [
22b748ef72
] - test: fix typos in test files (Daijiro Wachi) #61408 - [
a20bf9a84d
] - test: allow filtering async internal frames in assertSnapshot (Joyee Cheung) #61769 - [
ec2913f036
] - test: unify assertSnapshot stacktrace transform (Chengzhong Wu) #61665 - [
460f41233d
] - test: check stability block position in API markdown (René) #58590 - [
9ad02065d5
] - test: adapt buffer test for v8 sandbox (Shelley Vohr) #61772 - [
5cf001736e
] - test: update FileAPI tests from WPT (Ms2ger) #61750 - [
84c7a23223
] - test: update WPT for WebCryptoAPI to 7cbe7e8ed9 (Node.js GitHub Bot) #61729 - [
276a32fd10
] - test: update WPT for url to efb889eb4c (Node.js GitHub Bot) #61728 - [
f5f21d36a6
] - test_runner: add exports option for module mocks (sangwook) #61727 - [
bfc8a12977
] - test_runner: make it compatible with fake timers (Matteo Collina) #59272 - [
e0cde40e1d
] - test_runner: set non-zero exit code when suite errors occur (Edy Silva) #62282 - [
d74efd6834
] - test_runner: run afterEach on runtime skip (Igor Shevelenkov) #61525 - [
8287ca749e
] - test_runner: expose expectFailure message (sangwook) #61563 - [
1f2025fd1e
] - (SEMVER-MINOR) test_runner: expose worker ID for concurrent test execution (Ali Hassan) #61394 - [
b1199c7bb4
] - test_runner: replace native methods with primordials (Ayoub Mabrouk) #61219 - [
1ca20fc33d
] - (SEMVER-MINOR) test_runner: show interrupted test on SIGINT (Matteo Collina) #61676 - [
207ba4f89f
] - test_runner: fix suite rerun (Moshe Atlow) #61775 - [
9927335c11
] - tls: forward keepAlive, keepAliveInitialDelay, noDelay to socket (Sergey Zelenov) #62004 - [
a1c3c901c0
] - tools: bump picomatch from 4.0.3 to 4.0.4 in /tools/eslint (dependabot[bot]) #62439 - [
1c6f5ed7c2
] - tools: adopt the--check-for-duplicates
NCU flag (Antoine du Hamel) #62478 - [
b53377e8fe
] - tools: bump flatted from 3.4.1 to 3.4.2 in /tools/eslint (dependabot[bot]) #62375 - [
f102e79b80
] - tools: bump eslint deps (Huáng Jùnliàng) #62356 - [
f5d74f8216
] - tools: add eslint-plugin-regexp (Huáng Jùnliàng) #62093 - [
bc5b9a04ad
] - tools: bump flatted from 3.3.3 to 3.4.1 in /tools/eslint (dependabot[bot]) #62255 - [
bad48b9700
] - tools: validate all commits that are pushed tomain
(Antoine du Hamel) #62246 - [
795d663ff4
] - tools: keep GN files when updating Merve (Antoine du Hamel) #62167 - [
0b6fa913f1
] - tools: revert timezone update GHA workflow to ubuntu-latest (Richard Lau) #62140 - [
840e098e99
] - tools: improve error handling in test426 update script (Rich Trott) #62121 - [
bd34e53a8e
] - tools: bump the eslint group across 1 directory with 2 updates (dependabot[bot]) #62092 - [
54dc797644
] - tools: fix daily wpt workflow nighly release version lookup (Filip Skokan) #62076 - [
30476ddff7
] - tools: fix example in release proposal linter (Richard Lau) #62074 - [
5245900c05
] - tools: bump minimatch from 3.1.3 to 3.1.5 in /tools/clang-format (dependabot[bot]) #62013 - [
59ad1e4503
] - tools: bump eslint to v10, babel to v8.0.0-rc.2 (Huáng Jùnliàng) #61905 - [
6f93c4b287
] - tools: fix parsing of commit trailers inlint-release-proposal
GHA (Antoine du Hamel) #62077 - [
de1bcfd54c
] - tools: bump minimatch from 3.1.2 to 3.1.3 in/tools/clang-format
(dependabot[bot]) #61977 - [
492868a7aa
] - tools: fix permissions for merve update script (Richard Lau) #62023 - [
774d0be1b3
] - tools: revert tools GHA workflow to ubuntu-latest (Richard Lau) #62024 - [
d91a689d6f
] - tools: bump minimatch from 3.1.2 to 3.1.3 in /tools/eslint (dependabot[bot]) #61976 - [
34b6305933
] - tools: roll back to x86 runner onscorecard.yml
(Antoine du Hamel) #61944 - [
937cd97a63
] - tools: fix auto-start-ci (Antoine du Hamel) #61900 - [
0958f9a9c7
] - tools: do not checkout repo inauto-start-ci.yml
(Antoine du Hamel) #61874 - [
c7607b9208
] - tools: automate updates for test/fixtures/test426 (Rich Trott) #60978 - [
00df3c1273
] - tools: bump unist-util-visit in /tools/doc in the doc group (dependabot[bot]) #61646 - [
fe15b0d65e
] - tools: bump the eslint group in /tools/eslint with 6 updates (dependabot[bot]) #61628 - [
bc38db51fc
] - tools: fix small inconsistencies in JSON doc output (Antoine du Hamel) #61757 - [
3e7010d47f
] - tools: refloat 10 Node.js patches to cpplint.py (Michaël Zasso) #60901 - [
583e6c67ea
] - tools: update cpplint to 2.0.2 (Michaël Zasso) #60901 - [
4c12ab8abc
] - typings: rationalise TypedArray types (René) #62174 - [
8357ebfe54
] - url: suppress warnings from url.format/url.resolve inside node_modules (René) #62005 - [
aad7b3cfca
] - url: enable simdutf for ada (Yagiz Nizipli) #61477 - [
7b28fb9812
] - util: allow color aliases in styleText (sangwook) #62180 - [
8bbe0138ce
] - util: add fast path to stripVTControlCharacters (Hiroki Osame) #61833 - [
f7a408d6f7
] - wasm: support js string constant esm import (Guy Bedford) #62198 - [
a0316d33b5
] - watch: get flags from execArgv (Efe) #61779 - [
eee96f7f5d
] - worker: heap profile optimizations (Ilyas Shabi) #62201 - [
deeeb22e1a
] - worker: eliminate race condition in process.cwd() (giulioAZ) #61664 - [
b15ea64ed9
] - zlib: fix use-after-free when reset() is called during write (Matteo Collina) #62325 - [
a9c5bd29c9
] - zlib: add support for brotli compression dictionary (Andy Weiss) #61763
Windows 64-bit Installer: https://nodejs.org/dist/v24.15.0/node-v24.15.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v24.15.0/node-v24.15.0-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v24.15.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v24.15.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v24.15.0/node-v24.15.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v24.15.0/node-v24.15.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v24.15.0/node-v24.15.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v24.15.0/node-v24.15.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v24.15.0/node-v24.15.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v24.15.0/node-v24.15.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v24.15.0/node-v24.15.0-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v24.15.0/node-v24.15.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v24.15.0/node-v24.15.0.tar.gz
Other release files: https://nodejs.org/dist/v24.15.0/
Documentation: https://nodejs.org/docs/v24.15.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
dd4bc77dcb5f4c9a2c9643739bb593500ccb09413ec42caa0f8ef0e5ef116095 node-v24.15.0-aix-ppc64.tar.gz
68fad9ef14f93bacf0a6e767269d92bec6b57289f6badae6be2796f25914f8e7 node-v24.15.0-arm64.msi
372331b969779ab5d15b949884fc6eaf88d5afe87bde8ba881d6400b9100ffc4 node-v24.15.0-darwin-arm64.tar.gz
af5cfaeafe603aaf7599f287fd9d100bb41f16794f49788fa59dd3f25546930f node-v24.15.0-darwin-arm64.tar.xz
ffd5ee293467927f3ee731a553eb88fd1f48cf74eebc2d74a6babe4af228673b node-v24.15.0-darwin-x64.tar.gz
5d627245b9f53cb2512cc21b7aa6aad693106affadd91e0c8f42d600fb7ba444 node-v24.15.0-darwin-x64.tar.xz
9a9250039fef572d0bcc110ac5e78055faf5604421211d2d5f578ebc5a34e703 node-v24.15.0-headers.tar.gz
896d142ce64c8a8847d8f469e99e3b081bc31936d308bfbe3f8c32f3209b55b8 node-v24.15.0-headers.tar.xz
73afc234d558c24919875f51c2d1ea002a2ada4ea6f83601a383869fefa64eed node-v24.15.0-linux-arm64.tar.gz
f3d5a797b5d210ce8e2cb265544c8e482eaedcb8aa409a8b46da7e8595d0dda0 node-v24.15.0-linux-arm64.tar.xz
b1f88900a4b16365eaba56269304fc11da7581dbf03552d4495f9ace1fc05f6d node-v24.15.0-linux-ppc64le.tar.gz
6a6560a27bd2817013c28c3d917bfe9eebf26bbd4b1d88475190f216cc411fbb node-v24.15.0-linux-ppc64le.tar.xz
f985455439d52fe9b8de6a8f6d07bfeccc736dea527e87eacafe5a8d7516a380 node-v24.15.0-linux-s390x.tar.gz
940d4cbfadf736b34519630a05d144c09f8a5aca291a802f2f559ee1562f6f24 node-v24.15.0-linux-s390x.tar.xz
44836872d9aec49f1e6b52a9a922872db9a2b02d235a616a5681b6a85fec8d89 node-v24.15.0-linux-x64.tar.gz
472655581fb851559730c48763e0c9d3bc25975c59d518003fc0849d3e4ba0f6 node-v24.15.0-linux-x64.tar.xz
36fdb8eb5255001133b057e54eb982d385b993c0185a8d22ad1532b763511a5d node-v24.15.0-win-arm64.7z
c9eb7402eda26e2ba7e44b6727fc85a8de56c5095b1f71ebd3062892211aa116 node-v24.15.0-win-arm64.zip
38edda3e8f02841bc336c8c1a85626e8e1f8f0da9ef981110863451ed5ae3a5f node-v24.15.0-win-x64.7z
cc5149eabd53779ce1e7bdc5401643622d0c7e6800ade18928a767e940bb0e62 node-v24.15.0-win-x64.zip
feffb8e5cb5ac47f793666636d496ef3e975be82c84c4da5d20e6aa8fa4eb806 node-v24.15.0-x64.msi
179cdd07168002ed8395ed63d43dc12e4ac1ab8d375f608eabfb9aff2706ff53 node-v24.15.0.pkg
729de494dd2872e5a3a6c32a1cd156a5413d4aca2772b2d873ee86bb5531bcd9 node-v24.15.0.tar.gz
a4f653d79ed140aaad921e8c22a3b585ca85cfdab80d4030f6309e4663a8a1c8 node-v24.15.0.tar.xz
49a54c103f4919ce64199a043ef5cd309507de491d718085edee089cd8e87543 win-arm64/node.exe
5eefacb0514b137a1dfcf7b2d4d83418aca7eea4895d086e6ca9254d29f83ba8 win-arm64/node.lib
d7b4dbdee2929ad92b05f72fba3c4b631f1a8058265e323b997d23a014cf0b7f win-arm64/node_pdb.7z
ba80d81fb52907e60280556cc45b9b5a6d52d19a0e08da1472fe562716194754 win-arm64/node_pdb.zip
3331e1ffe19874215472217c5e94f5a0c6d8e18c4ac7111d3937aa0ad5e9b4a5 win-x64/node.exe
2dad98cd40967a4fd4a97195979e0e237e09ec292483700a51d2c20fe5a97c87 win-x64/node.lib
c93cd9d634ebcb184779bf969bf361c0d6f81b0bf8667dce328522a91a5c146d win-x64/node_pdb.7z
87a283c70e77cc3fc81ca20d3a07bd6df91f778c640d8ca1e8bbe33ff5e405e3 win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iHUEARYIAB0WIQRb6KP2yKXAHRBsCtggsaOQsWjTVgUCaeCMlQAKCRAgsaOQsWjT
VrtOAQC4lCL7LUownrhmHRjwAAIGJga6ADo+flP6/k6ZPP3zfgD7BztVRifnjHcf
9ZbiuHxcvnZVh7mp1t5E7qmriVLJqw8=
=B7+X
-----END PGP SIGNATURE-----
```

---

## 5. Security Bug Bounty Program Paused Due to Loss of Funding

- 日期: 2026-04-02 12:00
- 链接: https://nodejs.org/en/blog/announcements/discontinuing-security-bug-bounties

```
Security Bug Bounty Program Paused Due to Loss of Funding
The Node.js Project
The Node.js project's security bug bounty program is being paused due to the discontinuation of its external funding source.
Background
Since 2016, the Node.js project has participated in the Internet Bug Bounty (IBB) program through HackerOne, offering monetary rewards to security researchers who responsibly disclosed vulnerabilities in Node.js. The program was a meaningful part of our security ecosystem, and we're grateful to the researchers who participated.
Why
The Internet Bug Bounty (IBB) program, which supported bounty rewards for Node.js through a pooled donation-funded initiative, has been paused. You can read more about the pause here. This decision was not made by the Node.js project.
As a volunteer-driven open-source project, Node.js does not have an independent budget to sustain a bounty program on its own. Without external support, we are not able to offer monetary rewards for vulnerability reports at this time.
What This Means
- Security reporting remains unchanged. We still accept and triage vulnerability reports through HackerOne. If you discover a security issue, please continue to report it responsibly.
- No monetary rewards. Reports will no longer be eligible for bounty payouts.
- Same commitment to security. The Node.js Security Team continues to treat security with the highest priority. Our disclosure policy, response times, and release process remain the same.
A Thank You to Researchers
We want to sincerely thank every researcher who has reported vulnerabilities through the bounty program over the years. Your contributions have made Node.js safer for millions of users. We hope you will continue to report security issues even without financial incentives — responsible disclosure is critical to the health of the open-source ecosystem.
Looking Ahead
We will re-evaluate resuming the bounty program if dedicated funding becomes available again. If your organization depends on Node.js and is interested in sponsoring a bug bounty program, please reach out through the OpenJS Foundation.
For questions or to report a vulnerability, see our security reporting page.
```

---

## 6. Node.js 25.9.0 (Current)

- 日期: 2026-04-01 14:46
- 链接: https://nodejs.org/en/blog/release/v25.9.0

```
Node.js 25.9.0 (Current)
Antoine du Hamel
2026-04-01, Version 25.9.0 (Current), @aduh95
Notable Changes
Test runner module mocking improvements
MockModuleOptions.defaultExport
and MockModuleOptions.namedExports
have been
consolidated into a single option MockModuleOptions.exports
to align with user
expectations and other test runners.
A default
property on MockModuleOptions.exports
represents the default
export, and own enumerable properties are treated as named exports.
An automated migration is available to update user code: https://github.com/nodejs/userland-migrations/tree/main/recipes/mock-module-exports
npx codemod @nodejs/mock-module-exports
Contributed by sangwook in #61727.
Other notable changes
- [
312476cb84
] - (SEMVER-MINOR) async_hooks: add using scopes toAsyncLocalStorage
(Stephen Belanger) #61674 - [
62d2cd473b
] - (SEMVER-MINOR) cli: add--max-heap-size
option (tannal) #58708 - [
d0ebf0e44b
] - (SEMVER-MINOR) crypto: addTurboSHAKE
andKangarooTwelve
Web Cryptography algorithms (Filip Skokan) #62183 - [
f85b9d9fa8
] - (SEMVER-MINOR) repl: add customizable error handling (Anna Henningsen) #62188 - [
67b854d407
] - (SEMVER-MINOR) repl: remove dependency onnode:domain
(Matteo Collina) #61227 - [
966b700623
] - (SEMVER-MINOR) sea: support code cache for ESM entrypoint in SEA (Joyee Cheung) #62158 - [
e1f0d2a014
] - (SEMVER-MINOR) stream: add stream/iter Implementation (James M Snell) #62066
Commits
- [
312476cb84
] - (SEMVER-MINOR) async_hooks: add using scopes to AsyncLocalStorage (Stephen Belanger) #61674 - [
bfff8cb2ab
] - (SEMVER-MINOR) benchmark: add benchmarks for experimental stream/iter (James M Snell) #62066 - [
c721d68502
] - benchmark: fix destructuring in dgram/single-buffer (Ali Hassan) #62084 - [
e2f03c8e92
] - buffer: improve performance of multiple Buffer operations (Ali Hassan) #61871 - [
2fcd07f1ba
] - build: support empty libname flags inconfigure.py
(Antoine du Hamel) #62477 - [
b800c57fce
] - build: fix timezone-update path references (Chengzhong Wu) #62280 - [
7dc5a1e9b4
] - build: skip dockit on IBMi (SRAVANI GUNDEPALLI) #62189 - [
f0eea0f905
] - build: fix --node-builtin-modules-path (Filip Skokan) #62115 - [
62d2cd473b
] - (SEMVER-MINOR) cli: add --max-heap-size option (tannal) #58708 - [
ac4b485698
] - crypto: update root certificates to NSS 3.121 (Node.js GitHub Bot) #62485 - [
d0ebf0e44b
] - (SEMVER-MINOR) crypto: add TurboSHAKE and KangarooTwelve Web Cryptography algorithms (Filip Skokan) #62183 - [
3009980d9d
] - crypto: add crypto::GetSSLCtx API for addon access to OpenSSL contexts (Tim Perry) #62254 - [
f5725ca81d
] - crypto: reject ML-KEM/ML-DSA PKCS#8 import without seed in SubtleCrypto (Filip Skokan) #62218 - [
f69ed4bc3f
] - crypto: rename CShakeParams and KmacParams length to outputLength (Filip Skokan) #61875 - [
4d96e53570
] - crypto: refactor WebCrypto AEAD algorithms auth tag handling (Filip Skokan) #62169 - [
93d77719e8
] - crypto: read algorithm name property only once in normalizeAlgorithm (Filip Skokan) #62170 - [
3d2e23a981
] - deps: update ada to 3.4.4 (Node.js GitHub Bot) #62414 - [
176d6d2205
] - deps: update timezone to 2026a (Node.js GitHub Bot) #62164 - [
95c7fc67ba
] - deps: update googletest to 2461743991f9aa53e9a3625eafcbacd81a3c74cd (Node.js GitHub Bot) #62484 - [
e5e9f2044a
] - deps: update simdjson to 4.5.0 (Node.js GitHub Bot) #62382 - [
905b94266a
] - deps: update ngtcp2 to 1.21.0 (Node.js GitHub Bot) #62051 - [
180c150122
] - deps: V8: cherry-pick cf1bce40a5ef (Richard Lau) #62449 - [
bc265aa003
] - deps: upgrade npm to 11.12.1 (npm team) #62448 - [
f1b28612c4
] - deps: V8: cherry-pick b25cd62c7ba2 (Yagiz Nizipli) #62354 - [
757719d2af
] - deps: disable rust icu compiled_data features (Chengzhong Wu) #62284 - [
3bdc955b63
] - deps: update sqlite to 3.51.3 (Node.js GitHub Bot) #62256 - [
a9703d194a
] - deps: update googletest to 73a63ea05dc8ca29ec1d2c1d66481dd0de1950f1 (Node.js GitHub Bot) #61927 - [
85138935cb
] - deps: update merve to 1.2.2 (Node.js GitHub Bot) #62213 - [
231521e75e
] - diagnostics_channel: add diagnostics channels for web locks (Ilyas Shabi) #62123 - [
0093863664
] - doc: deprecatemodule.register()
(DEP0205) (Geoffrey Booth) #62395 - [
0b96ece6be
] - doc: clarify that features cannot be both experimental and deprecated (Antoine du Hamel) #62456 - [
8d3ea975f5
] - doc: fix 'transfered' typo in quic.md (lilianakatrina684-a11y) #62492 - [
08ff16e0ba
] - doc: move sqlite type conversion section to correct level (René) #62482 - [
61cc747dd8
] - doc: add Rafael to last security release steward (Rafael Gonzaga) #62423 - [
64cfa5a6fa
] - doc: use npm-published version of doc-kit (Aviv Keller) #62139 - [
1020321fb0
] - doc: fix overstated Date header requirement in response.sendDate (Kit Dallege) #62206 - [
9caa7855b2
] - doc: fix guaranteed typo (lilianakatrina684-a11y) #62374 - [
e254f65306
] - doc: enhance clarification about the main field (Mowafak Almahaini) #62302 - [
9e724b53f8
] - doc: remove spawn with shell example from bat/cmd section (Kit Dallege) #62243 - [
7f37c17516
] - doc: minor typo fix (Jeff Matson) #62358 - [
eb0ca98f01
] - doc: add path to vulnerabilities.json mention (Rafael Gonzaga) #62355 - [
198b6e0932
] - doc: deprecate CryptoKey use in node:crypto (Filip Skokan) #62321 - [
17e5aee6c5
] - doc: fix small environment_variables typo (chris) #62279 - [
193d629895
] - doc: test and test-only targets do not run linter (Xavier Stouder) #62120 - [
4a1f20ec4a
] - doc: clarify fs.ReadStream and fs.WriteStream are not constructable (Kit Dallege) #62208 - [
f976c9214d
] - doc: clarify that any truthy value ofshell
is part of DEP0190 (Antoine du Hamel) #62249 - [
4d83972681
] - doc: remove outdated Chrome 66 and ndb references from debugger (Kit Dallege) #62202 - [
71f2eada5b
] - doc: add throwIfNoEntry version history to fs.stat (kovan) #62204 - [
670c80893b
] - doc: add note (and caveat) formock.module
about customization hooks (Jacob Smith) #62075 - [
2ff5cb13f5
] - doc,test: clarify --eval syntax for leading '-' scripts (kovan) #62244 - [
6c6c9004c4
] - esm: fix typo in worker loader hook comment (jakecastelli) #62475 - [
1cdd23c9f3
] - esm: fix source phase identity bug in loadCache eviction (Guy Bedford) #62415 - [
4f4ff15794
] - esm: fix path normalization infinalizeResolution
(Antoine du Hamel) #62080 - [
088167d102
] - events: avoid cloning listeners array on every emit (Gürgün Dayıoğlu) #62261 - [
0250b436ee
] - fs: fix cpSync to handle non-ASCII characters (Stefan Stojanovic) #61950 - [
b67a8fb171
] - inspector: add Target.getTargets and extract TargetManager (Kohei) #62487 - [
ffcc5a5722
] - lib: make SubtleCrypto.supports enumerable (Filip Skokan) #62307 - [
92ef2ad8fa
] - lib: prefer primordials in SubtleCrypto (Filip Skokan) #62226 - [
40a43ac4d0
] - module: fix coverage of mocked CJS modules imported from ESM (Marco) #62133 - [
3ef0a5b90e
] - quic: remove CryptoKey support from session keys option (Filip Skokan) #62335 - [
3c8dd8eb8e
] - repl: use vm DONT_CONTEXTIFY context (Chengzhong Wu) #62371 - [
f85b9d9fa8
] - (SEMVER-MINOR) repl: add customizable error handling (Anna Henningsen) #62188 - [
e4c164e045
] - repl: handle exceptions from async context after close (Anna Henningsen) #62165 - [
67b854d407
] - (SEMVER-MINOR) repl: remove dependency on domain module (Matteo Collina) #61227 - [
966b700623
] - (SEMVER-MINOR) sea: support code cache for ESM entrypoint in SEA (Joyee Cheung) #62158 - [
fe82baf970
] - src: improve EC JWK import performance (Filip Skokan) #62396 - [
d490b171e0
] - src: handle null backing store in ArrayBufferViewContents::Read (Mert Can Altin) #62343 - [
0e4af848bc
] - src: convert context_frame field in AsyncWrap to internal field (Anna Henningsen) #62103 - [
02980b8c8f
] - src: enable compilation/linking with OpenSSL 4.0 (Filip Skokan) #62410 - [
064f7c2fa6
] - src: use stack allocation in indexOf latin1 path (Mert Can Altin) #62268 - [
ede52bc2dc
] - src,sqlite: fix filterFunc dangling reference (Edy Silva) #62281 - [
e1f0d2a014
] - (SEMVER-MINOR) stream: add stream/iter Implementation (James M Snell) #62066 - [
03839fb087
] - stream: preserve error over AbortError in pipeline (Marco) #62113 - [
0000d2f011
] - stream: replace bind with arrow function for onwrite callback (Ali Hassan) #62087 - [
3796a73719
] - test: update WPT for WebCryptoAPI to 2cb332d710 (Node.js GitHub Bot) #62483 - [
ad8309415b
] - test: update WPT for url to fc3e651593 (Node.js GitHub Bot) #62379 - [
bed89b037e
] - test: wait for reattach before initial break on restart (Yuya Inoue) #62471 - [
c9ffffcc55
] - test: disable flaky WPT Blob test on AIX (James M Snell) #62470 - [
fd41ef31f6
] - (SEMVER-MINOR) test: add tests for experimental stream/iter implementation (James M Snell) #62066 - [
1b9d8d3eec
] - test: avoid flaky run wait in debugger restart test (Yuya Inoue) #62112 - [
cb08a29d51
] - test: skip test-cluster-dgram-reuse on AIX 7.3 (Stewart X Addison) #62238 - [
abea0af8a9
] - test: add WebCrypto Promise.prototype.then pollution regression tests (Filip Skokan) #62226 - [
47a2132269
] - test: update WPT for WebCryptoAPI to 6a1c545d77 (Node.js GitHub Bot) #62187 - [
2c63d3006c
] - test_runner: add exports option for module mocks (sangwook) #61727 - [
44ac0e1302
] - test_runner: make it compatible with fake timers (Matteo Collina) #59272 - [
1865691275
] - test_runner: set non-zero exit code when suite errors occur (Edy Silva) #62282 - [
0252b2bab8
] - tools: bump picomatch from 4.0.3 to 4.0.4 in /tools/eslint (dependabot[bot]) #62439 - [
3368155267
] - tools: bump yaml from 2.8.2 to 2.8.3 in /tools/doc (dependabot[bot]) #62437 - [
5e47c359f5
] - tools: adopt the--check-for-duplicates
NCU flag (Antoine du Hamel) #62478 - [
4a604e82d0
] - tools: bump picomatch in /tools/doc (dependabot[bot]) #62438 - [
d1a98b4ddb
] - tools: bump flatted from 3.4.1 to 3.4.2 in /tools/eslint (dependabot[bot]) #62375 - [
c32daa1ab4
] - tools: bump eslint deps (Huáng Jùnliàng) #62356 - [
7a2fcc6d41
] - tools: do not swallow error inlint-nix
workflow (Antoine du Hamel) #62292 - [
c41a2871b5
] - tools: add eslint-plugin-regexp (Huáng Jùnliàng) #62093 - [
56dfeb06df
] - tools: fix timeout errors inlint-nix
job (Antoine du Hamel) #62265 - [
22fc8078e8
] - tools: bump flatted from 3.3.3 to 3.4.1 in /tools/eslint (dependabot[bot]) #62255 - [
409b0663bd
] - tools: bump undici from 6.23.0 to 6.24.1 in /tools/doc (dependabot[bot]) #62250 - [
67c69750f4
] - tools: validate all commits that are pushed tomain
(Antoine du Hamel) #62246 - [
7d9db8cd21
] - tools: keep GN files when updating Merve (Antoine du Hamel) #62167 - [
6c8fa42ba2
] - typings: rationalise TypedArray types (René) #62174 - [
531c64d04e
] - url: enable simdutf for ada (Yagiz Nizipli) #61477 - [
2000caccde
] - util: allow color aliases in styleText (sangwook) #62180 - [
0aed332ab4
] - wasm: support js string constant esm import (Guy Bedford) #62198 - [
d3fd4a978b
] - worker: heap profile optimizations (Ilyas Shabi) #62201 - [
e992a34a18
] - zlib: fix use-after-free when reset() is called during write (Matteo Collina) #62325
Windows 64-bit Installer: https://nodejs.org/dist/v25.9.0/node-v25.9.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v25.9.0/node-v25.9.0-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v25.9.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v25.9.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v25.9.0/node-v25.9.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v25.9.0/node-v25.9.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v25.9.0/node-v25.9.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v25.9.0/node-v25.9.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v25.9.0/node-v25.9.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v25.9.0/node-v25.9.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v25.9.0/node-v25.9.0-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v25.9.0/node-v25.9.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v25.9.0/node-v25.9.0.tar.gz
Other release files: https://nodejs.org/dist/v25.9.0/
Documentation: https://nodejs.org/docs/v25.9.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
f7e119831209e9c001dc1fbf798d23e71cc5af540e06984e9e76c2d0fc7b5fe3 node-v25.9.0-aix-ppc64.tar.gz
2e95e8cd93bd4ce3336db9afad95d482bb2b29a74300f2a45223412508ece63f node-v25.9.0-arm64.msi
e479f3c469d3d9303a44f00a8ea37a3788395d171bb8059c48a4bbbd2e371b59 node-v25.9.0-darwin-arm64.tar.gz
15eeeb03c60691a4764effa6cee920217f72058a70bcffe5f4c1209bbe4ad5a3 node-v25.9.0-darwin-arm64.tar.xz
7d737b53ce191142bfa1c17cfa5b070d96e84eebf76b8dd06d84981cbdc3f7e3 node-v25.9.0-darwin-x64.tar.gz
824d667ee88ca3e10e9917c9032937e6d1f5042aeb32affd145702d9ff877704 node-v25.9.0-darwin-x64.tar.xz
de7a1b69ceee1a8a29a98d005d1edb642e917e5fed801fcadfd678d6f618c77a node-v25.9.0-headers.tar.gz
2ca4f3657b6033096f0d0154fde413f4ac583ed9b0ecf709c8ab3bbcbdef4ea3 node-v25.9.0-headers.tar.xz
8fb4283301b8c720fc9f18bffff0f659e72cc14d0cf207a3bb411808aaa73a57 node-v25.9.0-linux-arm64.tar.gz
bf007bf0dcc2fddd90888fde374a1ad33c1ab2ca2ad324c645dd7aed0f9f1460 node-v25.9.0-linux-arm64.tar.xz
e727611129ae0703f0cd2b28d8d4bdff150723581280570f66bc54ac5b092dba node-v25.9.0-linux-ppc64le.tar.gz
5b602d6f4167d4853cdbb5439738ac0a7dc60568ebe49eb25c70825bced1eb1b node-v25.9.0-linux-ppc64le.tar.xz
7ad2dc045c6bba89ac3d0ac9dd7d4818bf0bbfe4675e4e427bf1dce94eaae91e node-v25.9.0-linux-s390x.tar.gz
6511af1eaf69f0e806dc47f4e102bddb25eb76fe2b398f06f3ac460dee3334e2 node-v25.9.0-linux-s390x.tar.xz
134e55b2408448a219760fe04dc44d6851f9de8a79549021ffd870e9082d9e7b node-v25.9.0-linux-x64.tar.gz
1d8db7d6e291d167e8c467ae4094be175e1a0b3969c7ae1f8955b9f7824f7b2e node-v25.9.0-linux-x64.tar.xz
36f46d727cf2ac0df953ad1a154d48feede7a4aefb937dd9810306b3a6dbd2ce node-v25.9.0.pkg
d55d77187039d4cd85c732f76838f44e3be552054473459dfa9cc0eb611ea664 node-v25.9.0.tar.gz
8f78af3ee55fb278668b5f801db58bd1a38ea161318eb5ce2128ddbc9cd813aa node-v25.9.0.tar.xz
0e9706b4237cae58192177f2b18e362403ed842d480027565d5fd467a7e0ac40 node-v25.9.0-win-arm64.7z
6b499bcaf16c86fe1a98c8e2874fd1980b23b5c90ea412983db4392d7e08c36b node-v25.9.0-win-arm64.zip
064e90165f1c4bce4b208b05105f6a2aaa714b93ef218358f218245ef47611b2 node-v25.9.0-win-x64.7z
929552b8305effac843ba7b4270c437aefb702fc3fbd73fcd1bffd35d4ac284e node-v25.9.0-win-x64.zip
e469104e5d0c99f9185fbf17179fbb1d732261e6e1f9d281b6b2308a0126fb6d node-v25.9.0-x64.msi
6f7a7c2a12b95acd70e0cfdb9b3ef498c9664f45399f2e9f283630d274124f44 win-arm64/node.exe
646759ca31c8168f2f91d7a67c4a495fb79beb8fde841690c041fd55b2255065 win-arm64/node.lib
f14c4c40f31bd7bf6e0d9d03fcc3d0bc6a9b09d8af499771f96504bf17401244 win-arm64/node_pdb.7z
a5982280f975c59bbb884ef7d0d3453d6ee3d089d36374cb74f3ce2622d2bac4 win-arm64/node_pdb.zip
98843732431bad6c2c165908bb7dde6fe2a221ddbc491a955d548a2e6ab9ebff win-x64/node.exe
e3577a5a4a772b21646fe05a24d53ce3727395bbbc412f326889ddf7129bc7a9 win-x64/node.lib
3c134d585c4dd483ff577c310eb63bc9b7537e99fc5e9d169b7c4101416c0ca6 win-x64/node_pdb.7z
0a04298910ac07d7db8d4c03659bf4f552874703f9a980963f670e29a8ac36b6 win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iHUEARYIAB0WIQRb6KP2yKXAHRBsCtggsaOQsWjTVgUCac0vegAKCRAgsaOQsWjT
VlHCAQC6K+H0bPBZ59f2+7L0JxbVA5Inl3JSdayCCx32VPkXQQEA0/A1cJGR+FqR
T+d7Z5UkJL2HOohK4ZhiyrdvAfXVngI=
=rCoy
-----END PGP SIGNATURE-----
```

---

## 7. Developing a minimally HashDoS resistant, yet quickly reversible integer hash for V8

- 日期: 2026-03-24 20:50
- 链接: https://nodejs.org/en/blog/vulnerability/march-2026-hashdos

```
Developing a minimally HashDoS resistant, yet quickly reversible integer hash for V8
Joyee Cheung
What happens when a hashing scheme needs to be both HashDoS resistant and quickly reversible? That's the puzzle we tried to solve for addressing CVE-2026-21717 in the March 2026 Node.js security release. This led to the development of an integer hash that we believe is unpredictable enough to prevent a blind attacker from reliably triggering severe performance degradation in our threat model. At the same time, it is also a permutation that can be efficiently inverted to recover the original integer value by the runtime holding the secret random keys, which is important for maintaining V8's performance optimizations.
In this post, we will go into the details of this vulnerability, explain why and how the design tried to meet the two seemingly contradictory requirements, and sample the statistical analysis we performed to evaluate the quality of the hash. Along the way, we will also discuss some specifics of how V8 stores and uses string hashes internally that lead to these constraints, the implementation techniques, and the performance analysis.
What is HashDoS and why does it matter for Node.js?
Hash tables are one of the most important data structures in software, and Node.js/V8 are no exceptions. With hash tables, there comes the problem of collisions - while hash tables are designed to have O(1) average time complexity for, e.g., single lookup and insertion, when there are so many keys whose hashed values can be mapped to the same slot that the table has to walk through many locations to insert a new key, it's theoretically possible to degrade to O(n2) in total for inserting n keys.
In many applications, the worst-case performance of hash tables is usually just a theoretical concern and maybe an occasional nuisance, but for servers that need to process untrusted input, this can be an attack vector. If an attacker manages to find a path that allows them to cause a large number of collisions in the server's internal hash table with a small number of inputs, they can effectively "freeze" the thread without much effort. And, with enough threads frozen, they could render the service unavailable for a sustained period of time. This is commonly called a hash flooding or Hash-DoS (Denial of Service) attack.
HashDoS vulnerabilities can show up in a wide range of platforms. In the case of V8, when it's used in a browser, DoS issues are not considered vulnerabilities because they typically only affect the tab that processes the malicious input, and users can simply close the tab. But when it's used in event-loop-based server-side runtimes, a single malicious request that manages to block the entire event loop for a sustained period of time has a much bigger impact. As one of the most widely deployed server-side runtimes, Node.js draws extensive scrutiny from security researchers, which helps us find and address weak spots like these.
Unlike other DoS attack vectors that can be more easily mitigated by userland restrictions, HashDoS vulnerabilities are particularly tricky because they lurk inside widely used internal data structures and well-defined operations trusted by developers. For V8 embedders, this means fixes for HashDoS vulnerabilities usually fall on the runtime maintainers, and they are a critical part of maintaining the security and reliability of the ecosystem.
Mitigating HashDoS with seeded hashes
The core of HashDoS vulnerabilities lies in deterministic hash functions - if the attacker can predict the hash values of their inputs, they can craft inputs that reliably trigger worst-case performance in the target server. The standard mitigation is to mix a seed value into the computation of the hash, and make sure that the seed is randomly generated at program initialization. This way, even if the attacker knows the hash function, they can't predict the hash values without knowing the seed that changes whenever the server restarts, and therefore can't craft inputs that will reliably collide.
In Node.js/V8, HashDoS vulnerabilities tend to center around misconfigurations that lead to unseeded hashes or hashes seeded by a constant value. For an early history of HashDoS vulnerabilities in Node.js/V8 and their mitigations, check out this V8 blog post. A more recent example is CVE-2025-27209, reported by Mate Marjanović and addressed in Node.js's July 2025 security release: during V8's switch to rapidhash, a configuration gap left the constants used by rapidhash hard-coded in V8 without seeding. To mitigate this, Node.js temporarily reverted back to a seeded hash in its copy of V8. Later, Gus Caplan from Deno ported rapidhash's secret generation code to V8 and wired it up to seed the constants used by rapidhash at runtime, which became the eventual mitigation that shipped in newer versions of Node.js. The generation of rapidhash secrets turned out to be important to our later design for the seeded integer hash, which we will discuss below.
Until recently, most HashDoS discoveries in V8 had centered on hashing of regular strings, since they are more commonly found in paths exposed to server handlers. It wasn't until the recent HackerOne report by Mate Marjanović that our attention was drawn to an elephant in the room: array index strings (those that look like non-negative integers and fit within 24 bits) in V8 used a different deterministic hash that can be trivially predicted.
What string hashes look like in V8
To understand the vulnerability, let's look at how V8 stores string hashes internally.
Every v8::internal::Name
object (the superclass of v8::internal::String
in V8) carries a 32-bit raw_hash_field
. The composition of this field varies depending on the type of string. The bottom 2 bits (HashFieldTypeBits
) determine the interpretation, and two of the most common types are:
- Regular strings (type
kHash = 0b10
): bits 2-31 store a 30-bit hash value computed by rapidhash, seeded with randomly generated secrets. This is considered to be "minimally HashDoS resistant", which we will discuss later. - Array index strings (type
kIntegerIndex = 0b00
): these are decimal-integer-looking strings whose numeric value fits in 24 bits. bits 2-25 (24 bits) hold the numeric value of the integer (ArrayIndexValueBits
), and bits 26-31 (6 bits) hold the string length (ArrayIndexLengthBits
).
The layout of the hash fields looks like this (the least significant bits are on the right):
"hello" (type: kHash = 0b10):
+-----------------------------------+---+
| 30-bit rapidhash |1 0|
+-----------------------------------+---+
31 2 1 0
"1234" (length=4, value=1234, type: kIntegerIndex = 0b00):
+--------+--------------------------+---+
| 000100 | 000000000000010011010010 |0 0|
| length | numeric value | |
+--------+--------------------------+---+
31 26 25 2 1 0
As you can see, the hash for array index strings is fully deterministic and there's no seeding involved. An attacker can easily predict their hash values, and with a bit of effort, craft colliding inputs.
Exploiting the deterministic hash for array index strings
One of the most commonly used hash tables in V8 is the string table, which is used for string internalization - deduplicating and caching strings in a global table for time and memory efficiency. The string table uses open addressing with quadratic probing to deal with collisions. The probing sequence is:
The string table grows by adding 50% slack and rounding the capacity to a power of two, so hash & (capacity - 1)
equals hash mod capacity
, and two strings with congruent hashes land on the same first-probe slot. For array index strings, the hash is (length << 24) | value
- but because the capacity is usually smaller than 224, the length bits are usually masked away and the slot depends only on the numeric value mod capacity. Take a table with initial capacity 32768
for example:
All three collide on slot 1234. The attacker can fill the probing sequence from the target value's first-probe slot to cause severe performance degradation, as demonstrated in the PoC in the HackerOne report.
const payload = [];
const val = 1234;
const MOD = 2 ** 19;
const CHN = 2 ** 17; // chain length
const REP = 2 ** 17; // repetitions of the target value
// Build the quadratic probing chain
let j = val + MOD;
for (let i = 1; i < CHN; i++) {
payload.push(`${j}`);
j = (j + i) % MOD;
}
// Repeat the target value to force lookups through the chain
for (let k = 0; k < REP; k++) {
payload.push(`${val}`);
}
// On the client side: attacker crafts an adversarial JSON payload
// and sends it to the remote server.
const string = JSON.stringify({ data: payload });
// On the server side: V8 inserts the numeric strings in a hash table
// for internalization, the collisions lead to extreme amplification
// in resource consumption.
JSON.parse(string);
With a ~2 MB payload, this can significantly slow down the JSON parsing - even on a powerful MacBook, this can hang for about half a minute. This means for servers that parse JSON from untrusted sources, a remote attacker can cause significant disruption via extreme asymmetric resource consumption. Since the same hashing scheme is also used for many other V8 internals, e.g., Map keys, this has a wide attack surface.
HashDoS resistant vs. efficiently reversible
As mentioned above, the standard mitigation for HashDoS is to seed the hash function, so we need to look for a more robust, seeded hashing scheme for array index strings.
When we talk about hashes for security purposes, we often naturally think of cryptographic hashes - which are, by design, irreversible. And here we have a dilemma: V8's array index hash is not just a hash - it's a reversible encoding. This enables an important optimization that happens everywhere in V8: for example, in many fast paths that involve string-to-integer conversion, like parseInt("42")
or obj["42"] = 1
, instead of trying to parse the number from the string (whose content is not necessarily in CPU cache), V8 simply reads the raw_hash_field
of the string and extracts the numeric value directly from the hash field. V8 also takes advantage of this encoding in e.g., string equality checks, where it would just compare two integer strings by their hashes. By nature, an irreversible cryptographic hash would break these optimizations and could lead to significant performance regressions in many hot paths.
So it looks like we are in a bind: do we have to either live with this vulnerability because of the reversibility requirement, or accept the performance regression?
Finding a middle ground: minimal HashDoS resistance
Now is the time to take a step back and think about what exactly makes a hash resistant to HashDoS attacks. It turned out that those who looked into rapidhash wondered the same and proposed the idea of "minimal HashDoS resistance", with constraints that apply to our case:
- The attacker cannot observe the hash output: The hash values are internal to V8 and not exposed directly to JavaScript or network responses. The attacker has to work blind.
- Node.js trusts the code it is asked to run and the infrastructure that runs it. The attacker should be sending untrusted input from a remote machine, and network jitter, garbage collection latency, server load etc. typically render the cost of exploiting timing side channels prohibitive.
In the specific context of Node.js/V8 servers, there are also a few other important factors in play:
- The attacker needs to work with a noisy table with application-specific entries out of their control. It is shared by both array-index strings and regular strings hashed by rapidhash, and the capacity growth can also be affected by pre-existing entries, making it harder for the attacker to predict the exact probe chain consistently.
- Standard operational practices in production servers typically enforce payload size limits and rate limits. Without them, the server can already be exposed to simpler resource exhaustion attacks. These bound how many collisions an attacker can inject per request and how often they can retry. Other common practices like load balancing can further complicate the attacker's ability to accumulate collisions on the same server.
- Hash table entries held weakly are subject to V8's garbage collection. For example, between requests, internalized strings that become unreachable are cleaned, which helps prevent collisions from accumulating across requests and limit what an attacker can achieve in each payload. If the server allows an attacker to keep unlimited entries alive across GC cycles, no hash is strong enough to fix the off-table memory growth and it's that unbounded retention path that needs to be fixed.
These contributed to the evaluation of high attack complexity in CVE-2026-21717 since the extreme amplification cannot be consistently reproduced against all Node.js servers, e.g., an Express server with its default 100 KB body limit.
That said, for servers with fewer guardrails or simpler states, a fully deterministic hash still makes the attack feasible. So while we don't need the hash to be cryptographically secure (or due to the reversibility requirement it just can't be), we still need to find an efficiently invertible, randomly keyed permutation with good diffusion on the 24-bit space, in order to bring the unpredictability of array index string hashes up to a level similar to randomly keyed rapidhash's unpredictability for regular strings.
Exploring candidate hashes
Some naive hashes and why they fail
We first prototyped with a few naive hashes, partly to identify all the code paths in V8 that would need updating, and partly to see whether something simple might be good enough in practice.
Multiply a secret, then add another
const uint32_t kMask = (1 << 24) - 1; // 24-bit mask
uint32_t SeedArrayIndexValue(uint32_t value, uint32_t secrets[2]) {
return (secrets[0] * value + secrets[1]) & kMask;
}
The first naive idea that came to mind was the classic linear congruential generator (LCG) construction, but applied individually on the input instead of on a sequence. This is bijective when secrets[0]
is odd, and can be quickly inverted (just subtract and multiply by the modular inverse). Unfortunately, this construction preserves linear relationships, and the low bits of the output depend only on the low bits of the input. As mentioned before, in many hash tables only the lower bits matter in probing, so an attacker can still generate collisions by picking values that are congruent modulo a guessed capacity.
XOR with a secret
uint32_t SeedArrayIndexValue(uint32_t value, uint32_t secrets[1]) {
return value ^ secrets[0]; // Both secrets and values are already 24-bit.
}
Another suggestion that came up during the development to minimize the overhead was to XOR the value with the randomly generated seed. This is also bijective and the inversion is extremely fast (just XOR the secret again), but each bit of the output depends on exactly one bit of the input. An attacker can still construct collisions just by choosing values that agree in the low bits.
These were clearly not good enough. We needed something with genuine bit diffusion, where changing a single input bit would affect many output bits in an unpredictable way for the attacker.
The xorshift-multiply mixers
The search for bijective integer hash functions led us to Christopher Wellons' hash-prospector project, which generates billions of integer hash functions at random from a selection of nine reversible operations, then evaluates and ranks them. This project showed that many of the best-performing functions came from the same family of constructions that use alternating rounds of two operations:
- (right xorshift): this is bijective and invertible. The top k bits are unchanged, and we can recover the next k bits by XORing with them, then repeat until all bits are restored. A particularly elegant aspect of xorshift is that when the shift k is at least half the bit width, this is an involution: . It is linear over GF(2), but nonlinear over ℤ/2N .
- (multiplication): this is bijective when m is odd, and invertible by multiplying with , the modular inverse of m mod . It is linear over ℤ/2N , but nonlinear over GF(2).
This family of xorshift-multiply constructions is used in many pseudorandom number generators/mixers like Java's SplittableRandom and MurmurHash3's finalizer. A great explanation of this construction can be found in this article (and this): multiplication propagates information upward through its carry chain, while XOR-shift propagates information downward by folding high bits into low positions. By mixing operations from different algebraic groups, this construction helps break the patterns each one preserves.
Since our multipliers are random secrets, the interaction between the two operations differs for each set of secrets, and multiple rounds of alternation helps spread the uncertainty across all bits. Applying this structure to our 24-bit input space, we first came up with the following design:
const uint32_t kMask = (1 << 24) - 1; // 24-bit mask
const uint32_t kShift = 12; // half the bit width, so the xorshift is an involution
// Multipliers in m[] are odd and randomly generated at startup.
uint32_t SeedArrayIndexValue(uint32_t value, uint32_t m[2]) {
uint32_t m1 = m[0], m2 = m[1];
uint32_t x = value;
x ^= x >> kShift; x = (x * m1) & kMask; // round 1
x ^= x >> kShift; x = (x * m2) & kMask; // round 2
x ^= x >> kShift; // finalize
return x;
}
To recover the original value, we can simply apply the steps in reverse order, replacing each multiplier with its modular inverse. This looks nicely symmetric:
// Modular inverses in m_inv[] are precomputed using Newton's method at startup.
uint32_t UnseedArrayIndexValue(uint32_t hash, uint32_t m_inv[2]) {
uint32_t m1_inv = m_inv[0], m2_inv = m_inv[1];
uint32_t x = hash;
x ^= x >> kShift; x = (x * m2_inv) & kMask; // undo round 2
x ^= x >> kShift; x = (x * m1_inv) & kMask; // undo round 1
x ^= x >> kShift; // finalize
return x;
}
Multiplier generation
Now that we had found a(nother) plausible structure to mix the bits, the next step was to find a way to generate good multipliers. The multipliers need to be 24-bit since the permutation needs to operate on the 24-bit modular arithmetic space, and they also need to be chosen well - if the multiplier is 1, for example, it won't mix the bits at all. On the other hand, since they need to be generated at startup, we need to minimize the cost of finding good multipliers.
We turned to the existing rapidhash secrets that V8 already generates at startup, which appeared to be a decent fit for our needs. While there is a width mismatch (rapidhash secrets are 64-bit), the secrets still retain some desirable properties after truncation. For example, each byte in the secrets must have exactly 4 bits set, and the generation ensures the secrets are odd, which is needed for the permutation to work. So we ended up just taking the lowest 24 bits of each rapidhash secret to derive the multipliers:
const uint32_t kMask = (1 << 24) - 1; // 24-bit mask
uint32_t derive_multiplier(uint64_t secret) {
// The | 1 ensures the multiplier is odd, which is redundant in practice
// but serves as a safeguard.
return ((uint32_t)secret & kMask) | 1;
}
And because V8 already has to generate them anyway, we essentially get these multipliers for free and can reuse a good chunk of the infrastructure around its management.
Statistical evaluation
With the construction taking shape, we'd like to see some empirical evidence about how well it diffuses the bits. While our threat model primarily relies on the secrecy of the multipliers and the invisibility of hash output, good diffusion is needed for that secrecy to reach every output bit. One common way to quantify diffusion for a hash function is to check its avalanche effect, which measures how a small change in the input affects the output bits. For example, if for each input x and each input bit position j, we compute the hash of both x and x with bit j flipped, then count how often each output bit k changed, the ideal hash function should have each output bit flipped 50% of the time for each input bit flip, known as the strict avalanche criterion (SAC). We adapted the code in hash-prospector to evaluate the bias (root-mean-square relative deviation) from the SAC for our 24-bit input space (scaled by 1000 for readability):
where is the bit width. A bias of 0 means perfect avalanche, and 1000 means zero diffusion.
We ran this on the original deterministic hash (identity function) as a baseline, then on a few naive ideas mentioned above, and finally on 1 and 2 rounds of xorshift-multiply with rapidhash's default secrets as multipliers:
While there's still room for improvement, it already looked very promising, so this was what our initial implementation used. But since our multipliers are derived from randomly generated rapidhash secrets, how do we know that the avalanche properties will be consistently good across different randomly generated secrets? We needed to verify that as well.
We ran the same analysis on multipliers derived from 50 sets of randomly generated rapidhash secrets, which revealed that the quality of the 2-round scheme can fluctuate quite a bit when the multipliers don't mix well.
We went with 2 rounds initially because that is the minimum to ensure every input bit reaches every output bit through at least one multiplication, providing nonlinear mixing rather than a single XOR fold. The fluctuations across the test runs, however, seemed to warrant another round, so we tested a 3-round version that looks like this:
const uint32_t kMask = (1 << 24) - 1; // 24-bit mask
const uint32_t kShift = 12; // half the bit width
// Multipliers in m[] are odd and randomly generated at startup.
uint32_t SeedArrayIndexValue(uint32_t value, uint32_t m[3]) {
uint32_t m1 = m[0], m2 = m[1], m3 = m[2];
uint32_t x = value;
x ^= x >> kShift; x = (x * m1) & kMask; // round 1
x ^= x >> kShift; x = (x * m2) & kMask; // round 2
x ^= x >> kShift; x = (x * m3) & kMask; // round 3
x ^= x >> kShift; // finalize
return x;
}
// Modular inverses in m_inv[] are precomputed using Newton's method at startup.
uint32_t UnseedArrayIndexValue(uint32_t hash, uint32_t m_inv[3]) {
uint32_t m1_inv = m_inv[0], m2_inv = m_inv[1], m3_inv = m_inv[2];
uint32_t x = hash;
x ^= x >> kShift; x = (x * m3_inv) & kMask; // undo round 3
x ^= x >> kShift; x = (x * m2_inv) & kMask; // undo round 2
x ^= x >> kShift; x = (x * m1_inv) & kMask; // undo round 1
x ^= x >> kShift; // finalize
return x;
}
This turned out to be quite effective in improving the stability of the avalanche effect:
Visualizing the hashes
Now let's look at some visualizations to get an intuitive sense of the hash. For the seeded hashes, we derived the constants from the default rapidhash secrets for the visualization, but the variation analysis above should also help you extrapolate the variance in these visualizations when different secrets are applied.
First, we take sequential inputs (spaced by an interval for better visibility) and plot their hash outputs. This helps us easily spot any linear relationships or patterns.
As you can see, 2-round and 3-round xorshift-multiply both look significantly more random and less predictable than the naive constructions.
Another way to visualize it is to look at the avalanche matrix. Here we take 50,000 random inputs, flip each input bit one at a time, and record how often each output bit changes. Each cell (row i, column j) shows the probability that flipping input bit i causes output bit j to flip - green means it's close to the ideal 50%, red means it's strongly biased toward never or always flipping. The more green there is, the better.
Once again, the 2-round and 3-round xorshift-multiply constructions show much better avalanche properties than the naive constructions.
Limitations
The SAC is a necessary but insufficient condition for a good hash function. Since this hashing scheme was developed to address a specific vulnerability, not to be a general-purpose PRNG or a non-cryptographic hash, we only measured bias from SAC as an empirical smoke test to guide the development, which happened in a limited timeframe. We have been exploring other evaluations, but to keep this post focused we won't go into them here. To avoid falling into the trap of identifying weaknesses in a spherical cow, it's important to keep in mind that structural weaknesses that cannot be exploited by a blind attacker to cause worst-case performance would only be informative rather than actionable in our threat model. The defense lies not only in the hash construction itself, but also in the lack of visibility of the randomly generated multipliers and the hash output.
Implementation
With a security release deadline to meet, we iterated on the hash design and V8 implementation in parallel, using the statistical analysis above to guide our choices while finding ways to reduce the impact on performance and code complexity.
Improving the access to hash secrets
Since our design will require even more frequent access to the hash secrets in hot paths, we need to ensure the access to them is efficient. In V8, the hash seed and the derived rapidhash secrets are stored in a ByteArray
in the read-only roots, which in the default configuration of Node.js, are shared across isolates and initialized during process startup. The layout of the ByteArray
was as follows:
Offset (bytes) | Content
---------------|-----------------------------
0 | seed (8 bytes)
8 | secrets[0] (8 bytes)
16 | secrets[1] (8 bytes)
24 | secrets[2] (8 bytes)
The roots tend to be hot and in cache, so reading the secrets from the roots directly should be efficient. However, like most heap objects in V8, the ByteArray
was previously allocated with the default 4-byte alignment. To deal with the potential misalignment when reading 8-byte secrets, the HashSeed
struct that was used to map them for access in C++ was passed around by value, with each part memcpy
-ed from the ByteArray
, or copied from another HashSeed
that's not necessarily in cache. To reduce the overhead, we updated the ByteArray
to be allocated with 8-byte alignment, and changed the HashSeed
to only hold a pointer to the beginning of the ByteArray
in the read-only roots. Accesses to individual parts of the structure were then just direct loads from a pointer that points to the roots without copying, and in code they are just simple field accesses from a HashSeed
struct reinterpreted over the ByteArray
.
Extending the HashSeed
for the new hash
For our new hashing scheme, during hash seed initialization, we derive the multipliers from the rapidhash secrets by taking the lowest 24 bits, compute their modular inverses using Newton's method, and store them all in the ByteArray
that HashSeed
maps onto. When we initially implemented the 2-round xorshift-multiply scheme, the layout of the ByteArray
became:
Offset (bytes) | Content
---------------|-----------------------------
0 | seed (8 bytes)
8 | secrets[0] (8 bytes)
16 | secrets[1] (8 bytes)
24 | secrets[2] (8 bytes)
32 | m1 (4 bytes)
36 | m2 (4 bytes)
40 | m1_inv (4 bytes)
44 | m2_inv (4 bytes)
This was later extended to include m3
and m3_inv
for the 3-round scheme, with m3
and m3_inv
derived from secrets[2]
.
Applying the new hashing scheme across V8
To implement the new seeded hashing scheme, we consolidated all the code paths that treated the value bits as the original numeric value to go through a few helpers and enforce seeding when it's enabled:
- In runtime C++, e.g., slow paths for JS operations that involve conversions between strings and integers, numeric string parsing, equality checks in internal tables: when the code needs to encode or decode an array index hash, it will first load the
HashSeed
from the read-only roots of either the current isolate group or the shared read-only heap, then call the new encoding and decoding helpers we added that perform the xorshift-multiply-based seeding and unseeding. - In JIT-compiled code, e.g., fast paths for JS operations that involve conversions between strings and integers like
parseInt
: the secrets need to be loaded from the roots of the current isolate. We added Torque macros to facilitate generating code that encodes and decodes array index hashes, while code generation for seeding/unseeding algorithms was implemented in theCodeStubAssembler
instead since the necessary operations were not yet well supported in Torque.
After the changes, the layout of the raw_hash_field
for array index strings looks like this:
"1234" (length=4, value=1234, type: kIntegerIndex = 0b00):
+--------+-------------------------------------+---+
| 000100 | 0010 0000 1101 0101 1100 1010 |0 0|
| length | 1234 seeded with xorshift-multiply | |
+--------+-------------------------------------+---+
31 26 25 2 1 0
Performance evaluation
At first glance, adding 3 rounds of xorshift-multiply to every array index string's decoding might seem like a lot. The encoding direction has less impact since it only runs once during string construction, and would be dwarfed by the cost of the initial string-to-integer conversion. But what about decoding, which is where the optimization that requires reversibility lies?
Decoding cost showdown
- Without seeding: recovering the integer from
raw_hash_field
is essentially(raw_hash_field >> 2) & 0xFFFFFF
, which is just one shift and one mask. - With seeding: on top of 1, this adds 4 xors, 4 shifts, 3 multiplies, 3 masks, and 3 loads of precomputed modular inverses from read-only roots that are likely in cache.
- Re-parsing the string: if we used an irreversible hash and had to recover the integer by parsing the string content, the CPU would need to read the string's content (a potential cache miss), then loop over each character doing
result = result * 10 + (c - '0')
.
Compared to unseeded decoding, the seeded decoding incurs a few more ALU instructions. But these are still a lot cheaper than any memory access that could happen around them, and can be offset by the improvements in hash diffusion - the previous scheme produced consecutive hashes for consecutive integers, which can already lead to worst-case performance issues in real-world workloads. As for reparsing, at length 5 the ALU costs alone would add up to be comparable to the seeded decoding, and when the string content is not in cache, the memory access cost would dominate.
Benchmark results
To quantify the performance impact of the changes, we ran four JavaScript benchmark suites - Octane, SunSpider, Kraken, JetStream 3 - with and without v8_enable_seeded_array_index_hash
on an x64 Linux server. The performance impact appeared neutral and within noise, which was adequate since our goal was to fix the vulnerability without causing a significant performance regression.
Deployment
The new seeded hashing scheme for array index strings has been merged into V8, gated by v8_enable_seeded_array_index_hash = true
, and it needs to be used together with v8_use_default_hasher_secret = false
for HashDoS resistance. For Chrome, where DoS attacks are not applicable, this will be disabled. In Node.js, this is enabled and shipped to v25, v24, v22, and v20 in the March 2026 security release.
We have also notified other V8 embedders (Deno and Cloudflare workers) about the vulnerability and the fix during the development and the rollout.
Acknowledgments
This fix was developed and backported to Node.js LTS branches by Joyee Cheung (Igalia, under the sponsorship of Bloomberg). Thanks to Mate Marjanović for identifying and reporting the vulnerability, Leszek Swirski from the Google V8 team for reviewing and providing feedback on the design and implementation, Chengzhong Wu (Bloomberg) for reviewing the V8 patches for Node.js, Matteo Collina (Platformatic) for triaging and investigating the mitigations, Olivier Flückiger (Google V8) for helping with the coordination, Antoine du Hamel, Juan José Arboleda, Marco Ippolito, and Rafael Gonzaga for preparing the security releases.
```

---

## 8. Node.js 25.8.2 (Current)

- 日期: 2026-03-24 20:43
- 链接: https://nodejs.org/en/blog/release/v25.8.2

```
Node.js 25.8.2 (Current)
Rafael Gonzaga
2026-03-24, Version 25.8.2 (Current), @RafaelGSS
This is a security release.
Notable Changes
- (CVE-2026-21637) wrap
SNICallback
invocation intry
/catch
(Matteo Collina) - High - (CVE-2026-21710) use null prototype for
headersDistinct
/trailersDistinct
(Matteo Collina) - High - (CVE-2026-21711) include permission check to
pipe_wrap.cc
(RafaelGSS) - Medium - (CVE-2026-21712) handle url crash on different url formats (RafaelGSS) - Medium
- (CVE-2026-21713) use timing-safe comparison in Web Cryptography HMAC and KMAC (Filip Skokan) - Medium
- (CVE-2026-21714) handle
NGHTTP2_ERR_FLOW_CONTROL
error code (RafaelGSS) - Medium - (CVE-2026-21717) test array index hash collision (Joyee Cheung) - Medium
- (CVE-2026-21715) add permission check to
realpath.native
(RafaelGSS) - Low - (CVE-2026-21716) include permission check on
lib/fs/promises
(RafaelGSS) - Low
Commits
- [
2086b7477b
] - (CVE-2026-21717) build,test: test array index hash collision (Joyee Cheung) nodejs-private/node-private#834 - [
0f9332a40a
] - (CVE-2026-21713) crypto: use timing-safe comparison in Web Cryptography HMAC and KMAC (Filip Skokan) nodejs-private/node-private#822 - [
2b6937ddb2
] - deps: update undici to 7.24.4 (Node.js GitHub Bot) #62271 - [
bfb8ad5787
] - deps: update undici to 7.24.3 (Node.js GitHub Bot) #62233 - [
be6384727f
] - deps: upgrade npm to 11.11.1 (npm team) #62216 - [
2feea5bb97
] - deps: V8: overridedepot_tools
version (Richard Lau) #62344 - [
86c04784dd
] - (CVE-2026-21710) http: use null prototype for headersDistinct/trailersDistinct (Matteo Collina) nodejs-private/node-private#821 - [
5197a56a34
] - (CVE-2026-21711) permission: include permission check to pipe_wrap.cc (RafaelGSS) nodejs-private/node-private#820 - [
04a886c735
] - (CVE-2026-21716) permission: include permission check on lib/fs/promises (RafaelGSS) nodejs-private/node-private#795 - [
9a7f80f2b0
] - (CVE-2026-21715) permission: add permission check to realpath.native (RafaelGSS) nodejs-private/node-private#794 - [
d9c9b628cf
] - (CVE-2026-21714) src: handle NGHTTP2_ERR_FLOW_CONTROL error code (RafaelGSS) nodejs-private/node-private#832 - [
45b55dc786
] - (CVE-2026-21712) src: handle url crash on different url formats (RafaelGSS) nodejs-private/node-private#816 - [
4bfda307c0
] - (CVE-2026-21637) tls: wrap SNICallback invocation in try/catch (Matteo Collina) nodejs-private/node-private#819
Windows 64-bit Installer: https://nodejs.org/dist/v25.8.2/node-v25.8.2-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v25.8.2/node-v25.8.2-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v25.8.2/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v25.8.2/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v25.8.2/node-v25.8.2.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v25.8.2/node-v25.8.2-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v25.8.2/node-v25.8.2-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v25.8.2/node-v25.8.2-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v25.8.2/node-v25.8.2-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v25.8.2/node-v25.8.2-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v25.8.2/node-v25.8.2-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v25.8.2/node-v25.8.2-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v25.8.2/node-v25.8.2.tar.gz
Other release files: https://nodejs.org/dist/v25.8.2/
Documentation: https://nodejs.org/docs/v25.8.2/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
d9fd5dcbfa95727bf30eed1ba1587cbb956a9e5364cf280e0bee2cfa7253802f node-v25.8.2-aix-ppc64.tar.gz
1d8e77a827bd19bac021fccd1f4b0e1f53ef2c4963c40aa2cfadfb8426486351 node-v25.8.2-arm64.msi
fb8dabfda3232ef90d992e6439824fc3237356c04d182f3fa883bebeef31e871 node-v25.8.2-darwin-arm64.tar.gz
ed0d0d6a1a2594d557f36f451ff34dff321d37b7ecb0d24b87c9ff2051086a18 node-v25.8.2-darwin-arm64.tar.xz
530ffb419789f843215375a65b8fcf4cf010735e99276f512a241a31ba8e5e13 node-v25.8.2-darwin-x64.tar.gz
16ccd800deb1a3de28cc71c77226608aa6dc380f86609fd810be3b60a3da1460 node-v25.8.2-darwin-x64.tar.xz
0592acd2a654d1c03360827774b3106453044b42b6d56cc70898f8edf7ac253d node-v25.8.2-headers.tar.gz
15ccf7adaff8a2d665fd2e7e32c0c106231eeb4bee2fe493e8a829701da60512 node-v25.8.2-headers.tar.xz
2f823ecd4f9331d6492fedbe50c5a610be3084521f3a5af146875e00a52f2e63 node-v25.8.2-linux-arm64.tar.gz
b7e8e0c9d48b6d9a43cf6e8d3960127473db001d60e964cb5e955e95603666eb node-v25.8.2-linux-arm64.tar.xz
8910cb32177b689620282859ce19a2c0285e55eeedef4854ff9af3da3bb54b5e node-v25.8.2-linux-ppc64le.tar.gz
6eda60bf124af0469be1045def9e1421c389ca0e2a67ab93834c5d7a41ed7f8f node-v25.8.2-linux-ppc64le.tar.xz
71af59d9a2e40cee6740084c40ae28138eff4d5fbf1ba81dbc729dffc5c71f7c node-v25.8.2-linux-s390x.tar.gz
fcd6dcc95564e293762b81699ee4614d0d867a26614a6549600b28751910834f node-v25.8.2-linux-s390x.tar.xz
e06c7069012d40914c57b31157c69d4ce83ea1fe9d63bbb7d26e0509a4535d21 node-v25.8.2-linux-x64.tar.gz
13a4c88c391aade2b7afba799ff27d09773b04e8a6c27f52908f79ff0e3787f5 node-v25.8.2-linux-x64.tar.xz
e850a0f2ff0fc8ffd93218ef0a5bf9d5e2ddaab50a3953d3676662584534fb93 node-v25.8.2-win-arm64.7z
a08e817d3ca86e065898c7d926f9c0c9a6d812ac9888f7f7cfd8c147ee8cbb29 node-v25.8.2-win-arm64.zip
e50bc4b23c85eeaa782423846c837fdd613dfb4cf5acf7841ca1048b4c66372b node-v25.8.2-win-x64.7z
51815d5b0256b947d27d614de04060fcfdbdb830d2c86e63e6f33dbf7964cca7 node-v25.8.2-win-x64.zip
176cc1d25eaacf1d8058bc319214ca156a4ad7b985d5ae0f239dbc26aa42ffd5 node-v25.8.2-x64.msi
90b364d8d6e6faabe13525c107f626cbfd69b9536aa87c5f2997ad81461b4fe6 node-v25.8.2.pkg
10335f268f7ffacd4f2b4f48d91dc5b19b1577a2861248ca414614ea24ebee65 node-v25.8.2.tar.gz
3efb19e757dc59bb21632507200d2de782369d5226a68955e9372c925fdf2471 node-v25.8.2.tar.xz
4c82a15e4af72881f8f4942506da1b56f2c4b2095924d8442de9f0ad96727834 win-arm64/node.exe
47750ee99207e5b621671565852cf7385f27bf664470886b9437137342a497c9 win-arm64/node.lib
2ed75e3a7fe8a85aa034c7c9c009bab8d65ce08722f5ab9c3bb3c5588ff6798d win-arm64/node_pdb.7z
e9e90a2fcf1db28870dbb9750326892e9574130602ab6114d1504d4219763d62 win-arm64/node_pdb.zip
f8d22c62786c547dc76b15c744e86c0ac1fe9dc38f2e0610dbad4d2b223a4544 win-x64/node.exe
f7201b932d898bdbf78aee7add288d2263c4791f1502068ad11b6c14675c6324 win-x64/node.lib
28288d282ef8043712bc227d43c475a4b60f42b6a1cd8007954e785e5220550c win-x64/node_pdb.7z
9c82e8c3931b46b7b975c41246e097d8980a68ea020e69ca9ad685b53179bbb6 win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQGzBAEBCAAdFiEEiQwI24V5Fi/uDfnbi+q0389VXvQFAmnC9sAACgkQi+q0389V
XvS4Ugv/Y074JLw5sr2pwbNhqLJCT2Jq7IHvYcOSsZ7VRIbmkOajhYKkVY9bKmoj
ELdk1qpkQYYH1cEEE7YRBqJGwEVChLu//GgvnLgwopR0QRn4Si+2EuSUYUmBXkAx
nLAHthd6HgSVF0A61jsNiTNlyS3tSkubfSGo82OuBMFtiD6n8A5ilgT4zeG+7ydB
tFv+jL5FevUdmYxC7rglSjdrZ/J/uyh2VGnbh1BOwdKSirYrMTEzvpJpX+v4lXHe
vlqvY2KIgR9g4f0pMMqZQ6Gx4MTfXfZYWPajLkHgdtMVe1Bsc82hfWwbHpzcCQFT
j5E0L1HzEC+ornLuv6o+muyX6Yj2weDNhfpIPQWARchcSgKrHZiG3yeEzlj0HLm6
mn+rDRVLSqK8FwERn/rxHCUZHBzfupF2970a3APB6fXwYXt4u94qCpFsRthoJeA+
GZ+elk0wLrKpwZs8bnz00RSAfqZ9Uy8PKGGVlelahE4mhjxHs7SbjC381xAwsAVC
LCDG1U7a
=8GXb
-----END PGP SIGNATURE-----
```

---

## 9. Node.js 24.14.1 (LTS)

- 日期: 2026-03-24 20:43
- 链接: https://nodejs.org/en/blog/release/v24.14.1

```
Node.js 24.14.1 (LTS)
Rafael Gonzaga
2026-03-24, Version 24.14.1 'Krypton' (LTS), @RafaelGSS prepared by @juanarbol
This is a security release.
Notable Changes
- (CVE-2026-21710) use null prototype for headersDistinct/trailersDistinct (Matteo Collina) - High
- (CVE-2026-21637) wrap SNICallback invocation in try/catch (Matteo Collina) - High
- (CVE-2026-21717) test array index hash collision (Joyee Cheung) - Medium
- (CVE-2026-21713) use timing-safe comparison in Web Cryptography HMAC and KMAC (Filip Skokan) - Medium
- (CVE-2026-21714) handle NGHTTP2_ERR_FLOW_CONTROL error code (RafaelGSS) - Medium
- (CVE-2026-21712) handle url crash on different url formats (RafaelGSS) - Medium
- (CVE-2026-21716) include permission check on lib/fs/promises (RafaelGSS) - Low
- (CVE-2026-21715) add permission check to realpath.native (RafaelGSS) - Low
Commits
- [
6fae244080
] - (CVE-2026-21717) build,test: test array index hash collision (Joyee Cheung) nodejs-private/node-private#828 - [
cc0910c62e
] - (CVE-2026-21713) crypto: use timing-safe comparison in Web Cryptography HMAC and KMAC (Filip Skokan) nodejs-private/node-private#822 - [
80cb042cf3
] - deps: update undici to 7.24.4 (Node.js GitHub Bot) #62271 - [
f5b8667dc2
] - deps: update undici to 7.24.3 (Node.js GitHub Bot) #62233 - [
08852637d9
] - deps: update undici to 7.22.0 (Node.js GitHub Bot) #62035 - [
61097db9fb
] - deps: upgrade npm to 11.11.0 (npm team) #61994 - [
9ac0f9f81e
] - deps: upgrade npm to 11.10.1 (npm team) #61892 - [
3dab3c4698
] - deps: V8: overridedepot_tools
version (Richard Lau) #62344 - [
87521e99d1
] - deps: V8: backport 1361b2a49d02 (Joyee Cheung) nodejs-private/node-private#828 - [
045013366f
] - deps: V8: backport 185f0fe09b72 (Joyee Cheung) nodejs-private/node-private#828 - [
af22629ea8
] - deps: V8: backport 0a8b1cdcc8b2 (snek) nodejs-private/node-private#828 - [
380ea72eef
] - (CVE-2026-21710) http: use null prototype for headersDistinct/trailersDistinct (Matteo Collina) nodejs-private/node-private#821 - [
d6b6051e08
] - (CVE-2026-21716) permission: include permission check on lib/fs/promises (RafaelGSS) nodejs-private/node-private#795 - [
bfdecef9da
] - (CVE-2026-21715) permission: add permission check to realpath.native (RafaelGSS) nodejs-private/node-private#794 - [
c015edf313
] - (CVE-2026-21714) src: handle NGHTTP2_ERR_FLOW_CONTROL error code (RafaelGSS) nodejs-private/node-private#832 - [
cba66c48a5
] - (CVE-2026-21712) src: handle url crash on different url formats (RafaelGSS) nodejs-private/node-private#816 - [
df8fbfb93d
] - (CVE-2026-21637) tls: wrap SNICallback invocation in try/catch (Matteo Collina) nodejs-private/node-private#819
Windows 64-bit Installer: https://nodejs.org/dist/v24.14.1/node-v24.14.1-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v24.14.1/node-v24.14.1-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v24.14.1/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v24.14.1/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v24.14.1/node-v24.14.1.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v24.14.1/node-v24.14.1-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v24.14.1/node-v24.14.1-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v24.14.1/node-v24.14.1-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v24.14.1/node-v24.14.1-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v24.14.1/node-v24.14.1-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v24.14.1/node-v24.14.1-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v24.14.1/node-v24.14.1-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v24.14.1/node-v24.14.1.tar.gz
Other release files: https://nodejs.org/dist/v24.14.1/
Documentation: https://nodejs.org/docs/v24.14.1/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
56f6c18c5e97beb00594c24eb3cfa3c70b7247c403b00ca7eae75bba30b85ce5 node-v24.14.1-aix-ppc64.tar.gz
4013ca42741ae0fd599d432985834d0ad4f565b1e4c59f8975d561f105f4af5c node-v24.14.1-arm64.msi
25495ff85bd89e2d8a24d88566d7e2f827c6b0d3d872b2cebf75371f93fcb1fe node-v24.14.1-darwin-arm64.tar.gz
0e2e679d76743d6d9225e61327a1ddc324e4a89a80891c78c337208601d98f77 node-v24.14.1-darwin-arm64.tar.xz
2526230ad7d922be82d4fdb1e7ee1e84303e133e3b4b0ec4c2897ab31de0253d node-v24.14.1-darwin-x64.tar.gz
a87a37a10c2faf65742c7d5812f5bab878eee52b0dffdf578f49b7a808d96ddd node-v24.14.1-darwin-x64.tar.xz
282103054f841fe75ecbbfdd8bb7334d0a4bb693191d97c5770ac6ae9acdd4ff node-v24.14.1-headers.tar.gz
4c7a978a22ae662b48d1225310c294239ca0e67d8ecd1b02c49def3536941459 node-v24.14.1-headers.tar.xz
734ff04fa7f8ed2e8a78d40cacf5ac3fc4515dac2858757cbab313eb483ba8a2 node-v24.14.1-linux-arm64.tar.gz
71e427e28b78846f201d4d5ecc30cb13d1508ca099ef3871889a1256c7d6f67e node-v24.14.1-linux-arm64.tar.xz
06824292e8b40b7f65a6f9973f3d60f3cc0001a9168234bc3d6e30aa13649fd2 node-v24.14.1-linux-ppc64le.tar.gz
95bf0c8dbb73144edb79a57399f03c70af6995b78e1c632926e53e6404662ef5 node-v24.14.1-linux-ppc64le.tar.xz
3ae573f43c93dafdafedc80863fa2a040bfeaa15e6ab83c1a8e0101f09952dc4 node-v24.14.1-linux-s390x.tar.gz
ed3bfbc0ff418b0ec4633f23d53a12a691717a34b041c3fbdb296c8774e5a98a node-v24.14.1-linux-s390x.tar.xz
ace9fa104992ed0829642629c46ca7bd7fd6e76278cb96c958c4b387d29658ea node-v24.14.1-linux-x64.tar.gz
84d38715d449447117d05c3e71acd78daa49d5b1bfa8aacf610303920c3322be node-v24.14.1-linux-x64.tar.xz
2aaeb742f6aa924da6fbee5c79d7c602b8bfcec45457eb6b738717c3052a14d6 node-v24.14.1-win-arm64.7z
a7b7c68490e4a8cde1921fe5a0cfb3001d53f9c839e416903e4f28e727b62f60 node-v24.14.1-win-arm64.zip
05024009bab2fed64b1143c3cc9931441cc1b902acd16f5880404db94beb3543 node-v24.14.1-win-x64.7z
6e50ce5498c0cebc20fd39ab3ff5df836ed2f8a31aa093cecad8497cff126d70 node-v24.14.1-win-x64.zip
fd8ba3e8262738959cad50e6f6e71d689eab7dd09fc7231b51d78abe7852d4ec node-v24.14.1-x64.msi
643b518b5b33dfb5e199e6268307266add568fe8cc981c82e255c9cd1ac51a29 node-v24.14.1.pkg
8298cf1f5774093ca819f41b8dd392fd2cff058688b4d5c8805026352e2d31b3 node-v24.14.1.tar.gz
7822507713f202cf2a551899d250259643f477b671706db421a6fb55c4aa0991 node-v24.14.1.tar.xz
557ba2ad04fd08464edc2ee3e399b58ff11eaba35a00bb05671661557dc6f79e win-arm64/node.exe
59f1c42e5962e9333bb1673c21125b7a7ce9a6908299aee8f7673803c2e24212 win-arm64/node.lib
ab56402e34b2a385ba6987cb7e022b377bbdcba068886d0f6d61beaf71e26e79 win-arm64/node_pdb.7z
223757455be292ec8a00404e0890f6e345d76824875e188e0be30710ebbe4cf4 win-arm64/node_pdb.zip
58e74bf02fc5bbacc41dcb8bef089961cd5bddd37830b87784e4fc624d145d1f win-x64/node.exe
35fcdd35d3d22e283c0e2e095cc43ef676301bb85f950c344a73d59231bd7e61 win-x64/node.lib
005ea57d4ebca610dcf87a08668977f701cbe91d28595f143c0511c344f675f2 win-x64/node_pdb.7z
4a755bfa6387bbe68a586e4beb8153891ec7f55df772147f59f9fccdf5f0b57c win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQGzBAEBCAAdFiEEiQwI24V5Fi/uDfnbi+q0389VXvQFAmnC9lsACgkQi+q0389V
XvSHhQwAgWVhmIyXzkWwA2f1Yfh63Xwzlqp/lj82kPI3jCcHmf1K8XFXnAM7Tqfh
4o5tenOo3RXjG1Ap24UBuXmw5iLpvJ6uvnZsRgvmUs0wVCrYMzF0isznrOYd6qYo
wZreGxXF/EFEd6sGmCaEpD5g4yvhcvE+6SwSfxpHdDZuuL50gEKHmG2WU4/oCIU4
+89CBr4BjMsX63fgwHyD3bI4SaWxcncKGHtPgWldmCrNSz80HhtXqxEinaz79H4n
+jaozyEo6x8YL3VKIIzNKRKgw2/7rVui4ydwAP190CiIEEVAffaIlnbaVOYBp5Zy
J2qTcwCLy0YIB1VnDK+6/sdGoLMOmuRhK2/rRVYAN9X/glPzcKProkL/h4Jhs5RL
b9QwMv9I7pzcff+mshUDWECOr/Y+/AwyISLADfTGHtPq4cenhTq5f4C1lgGIgAQl
/Ci+l+sv/Yo5uteRe9uauhy+p6+XkGzpb8/gbkPTBCiRNWnW0pcVwjLoHaZrZGD3
mmI22SyF
=AqPu
-----END PGP SIGNATURE-----
```

---

## 10. Node.js 22.22.2 (LTS)

- 日期: 2026-03-24 20:43
- 链接: https://nodejs.org/en/blog/release/v22.22.2

```
Node.js 22.22.2 (LTS)
Rafael Gonzaga
2026-03-24, Version 22.22.2 'Jod' (LTS), @RafaelGSS prepared by @aduh95
This is a security release.
Notable Changes
- (CVE-2026-21637) wrap
SNICallback
invocation intry
/catch
(Matteo Collina) - High - (CVE-2026-21710) use null prototype for
headersDistinct
/trailersDistinct
(Matteo Collina) - High - (CVE-2026-21713) use timing-safe comparison in Web Cryptography HMAC (Filip Skokan) - Medium
- (CVE-2026-21714) handle
NGHTTP2_ERR_FLOW_CONTROL
error code (RafaelGSS) - Medium - (CVE-2026-21717) test array index hash collision (Joyee Cheung) - Medium
- (CVE-2026-21715) add permission check to
realpath.native
(RafaelGSS) - Low - (CVE-2026-21716) include permission check on
lib/fs/promises
(RafaelGSS) - Low
Commits
- [
6f14ee5101
] - (CVE-2026-21717) build,test: test array index hash collision (Joyee Cheung) nodejs-private/node-private#809 - [
52a52ef619
] - (CVE-2026-21713) crypto: use timing-safe comparison in Web Cryptography HMAC (Filip Skokan) nodejs-private/node-private#822 - [
30a3ab11e2
] - (CVE-2026-21717) deps: V8: cherry-pick aac14dd95e5b (Joyee Cheung) nodejs-private/node-private#809 - [
e3f4d6a42e
] - (CVE-2026-21717) deps: V8: backport 1361b2a49d02 (Joyee Cheung) nodejs-private/node-private#809 - [
7dc00fa5f4
] - (CVE-2026-21717) deps: V8: backport 185f0fe09b72 (Joyee Cheung) nodejs-private/node-private#809 - [
076acd052d
] - (CVE-2026-21717) deps: V8: backport 0a8b1cdcc8b2 (snek) nodejs-private/node-private#809 - [
963c60a951
] - deps: V8: overridedepot_tools
version (Richard Lau) #62344 - [
a688117d5d
] - deps: upgrade npm to 10.9.7 (npm team) #62330 - [
859c8c761b
] - deps: update undici to v6.24.1 (Matteo Collina) #62285 - [
d5ed384a2f
] - deps: upgrade npm to 10.9.6 (npm team) #62215 - [
a2fe9fd81a
] - (CVE-2026-21710) http: use null prototype for headersDistinct/trailersDistinct (Matteo Collina) nodejs-private/node-private#821 - [
73deff77c1
] - lib: backport_tls_common
and_tls_wrap
refactors (Dario Piotrowicz) #57643 - [
06fc3436f6
] - (CVE-2026-21716) permission: include permission check on lib/fs/promises (RafaelGSS) nodejs-private/node-private#795 - [
db48d9c675
] - (CVE-2026-21715) permission: add permission check to realpath.native (RafaelGSS) nodejs-private/node-private#794 - [
2a6105a63b
] - (CVE-2026-21714) src: handle NGHTTP2_ERR_FLOW_CONTROL error code (RafaelGSS) nodejs-private/node-private#832 - [
91b970886f
] - (CVE-2026-21637) tls: wrap SNICallback invocation in try/catch (Matteo Collina) nodejs-private/node-private#819
Windows 32-bit Installer: https://nodejs.org/dist/v22.22.2/node-v22.22.2-x86.msi
Windows 64-bit Installer: https://nodejs.org/dist/v22.22.2/node-v22.22.2-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v22.22.2/node-v22.22.2-arm64.msi
Windows 32-bit Binary: https://nodejs.org/dist/v22.22.2/win-x86/node.exe
Windows 64-bit Binary: https://nodejs.org/dist/v22.22.2/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v22.22.2/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v22.22.2/node-v22.22.2.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v22.22.2/node-v22.22.2-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v22.22.2/node-v22.22.2-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v22.22.2/node-v22.22.2-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v22.22.2/node-v22.22.2-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v22.22.2/node-v22.22.2-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v22.22.2/node-v22.22.2-aix-ppc64.tar.gz
ARMv7 32-bit Binary: https://nodejs.org/dist/v22.22.2/node-v22.22.2-linux-armv7l.tar.xz
ARMv8 64-bit Binary: https://nodejs.org/dist/v22.22.2/node-v22.22.2-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v22.22.2/node-v22.22.2.tar.gz
Other release files: https://nodejs.org/dist/v22.22.2/
Documentation: https://nodejs.org/docs/v22.22.2/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
31e8cdaf9921589c2978fd224aa5ae51e470577df63435ebfff16b715ed8d4d3 node-v22.22.2-aix-ppc64.tar.gz
1ec02aeb76d716ce15915bed10c0a4dcf9a6224e9a4f4d1645ddca4985a7bc06 node-v22.22.2-arm64.msi
db4b275b83736df67533529a18cc55de2549a8329ace6c7bcc68f8d22d3c9000 node-v22.22.2-darwin-arm64.tar.gz
f8655beb4b86ff6588ed7e02c37f8574b58557bd3e880012814b1a4956fd9d88 node-v22.22.2-darwin-arm64.tar.xz
12a6abb9c2902cf48a21120da13f87fde1ed1b71a13330712949e8db818708ba node-v22.22.2-darwin-x64.tar.gz
b6a384bba1a7ec585e5a91a452b63f676b940584ff57b5c9cf0541c8db60023e node-v22.22.2-darwin-x64.tar.xz
90e5ef0fdf02f88487f904a798836b35bd44896046d502873bc625ac2baeded2 node-v22.22.2-headers.tar.gz
b4dde76c01769ae141de9228cc47dd53853cde2fd94f7d40192273ec79dd405b node-v22.22.2-headers.tar.xz
b2f3a96f31486bfc365192ad65ced14833ad2a3c2e1bcefec4846902f264fa28 node-v22.22.2-linux-arm64.tar.gz
e9e1930fd321a470e29bb68f30318bf58e3ecb4acb4f1533fb19c58328a091fe node-v22.22.2-linux-arm64.tar.xz
465162c9e1821b2168b2740351ae8f191b24b58313f0cf9873a7ccd200a66e12 node-v22.22.2-linux-armv7l.tar.gz
2ebc6746e517f345da340ec76a108203eb6c2365391eb525c0e0dd6135b0b9df node-v22.22.2-linux-armv7l.tar.xz
f661dd525231faf113bd484129169d222b84ef40c091b5dca04a104d43e25d07 node-v22.22.2-linux-ppc64le.tar.gz
14045b5a5030d35ca0030fb7e870bd11a651eb9b57323ebc0021e8d78ac6bac9 node-v22.22.2-linux-ppc64le.tar.xz
4c28684a4c75683c491464f7fa168cd37752ed343fc27fb85b75806517e340cb node-v22.22.2-linux-s390x.tar.gz
9e4a07c291b8949289c6ea8ee61b1d14666a4810feae776a8d1eb1f57e03a2fb node-v22.22.2-linux-s390x.tar.xz
978978a635eef872fa68beae09f0aad0bbbae6757e444da80b570964a97e62a3 node-v22.22.2-linux-x64.tar.gz
88fd1ce767091fd8d4a99fdb2356e98c819f93f3b1f8663853a2dee9b438068a node-v22.22.2-linux-x64.tar.xz
ed1b73ffb642978e669786f9115d2579e890a3f9bf3dcd7c73272047b4895a17 node-v22.22.2-win-arm64.7z
380d375cf650c5a7f2ef3ce29ac6ea9a1c9d2ec8ea8e8391e1a34fd543886ab3 node-v22.22.2-win-arm64.zip
c87622c838f312d1fcc635e09034013e983ebe8df039a62ab46c22b34b9b8a0c node-v22.22.2-win-x64.7z
7c93e9d92bf68c07182b471aa187e35ee6cd08ef0f24ab060dfff605fcc1c57c node-v22.22.2-win-x64.zip
d73718f162d286d1deaf911d8bf224ba823a877cd0ed23c0d09b43923f6bd699 node-v22.22.2-win-x86.7z
ca892f829a733109e341c43585fd2094177e9d2f2c45f97c7ed3cf329d5427c5 node-v22.22.2-win-x86.zip
57456aa33fcd6fb6a9418e09227de0b0ca604f7b2123566acc66b555cb2f42e5 node-v22.22.2-x64.msi
e43cf42f461cbfea23a079925cfdd132a18cf66d4e30f64ec5ab4ec31dbb41f3 node-v22.22.2-x86.msi
ff08ad19678de4ca2af34b58b73b272c555449c6f2d91487ca6fe0a697f9eabe node-v22.22.2.pkg
f4b9606f33aef725a77b6292460102b48b80902571a8bb94cd769837ee0577df node-v22.22.2.tar.gz
b6bedd3a8cacd5df7df015a5088264b12c74a277ba60684cb9642ae8eb743132 node-v22.22.2.tar.xz
1a338f2467a566197ed8b309240a3a372f5d72458f9c7e5c9613ad6ccae1e0c0 win-arm64/node.exe
9b75bbc3be72c84f1d41cd6abb6e5ecc333836015e40a6267ce755554874a13a win-arm64/node.lib
d8439627dd1081c37267c77a79cf7f21c0a7cfd85c582fc3d6361d4b6a720388 win-arm64/node_pdb.7z
76a309aae5afd000b87359a4d26c2392dfc231ef626c1a77ec103452677edad4 win-arm64/node_pdb.zip
ae1a50511be58e987483fdbc12125407443926d2d394669ade2352776e920dd3 win-x64/node.exe
0d8d8bcc11daea60f5dd4da414e72ccb785718345ec8fbec52cfc7d1a2326293 win-x64/node.lib
0431a2383c9ceec6bd46d5d96fec1342c0adf7bd57528312fe4812e32e1d2e5c win-x64/node_pdb.7z
7a5071732adc414638f4a8e06926820410dfd6421badbe0221dfa594ec2a766f win-x64/node_pdb.zip
ed2aff66c21ea111e517b3c8a6857c35d222cc83e12ff66d9c03b61e2e0558e7 win-x86/node.exe
a07e94777fb491c1a59103b6987417df35a1dd0a9682220bba43d3c602b8b414 win-x86/node.lib
0f43bd6b98aa25bc7067cf374de59ec853035778ff4b6ce2fb118dc67f5eaee9 win-x86/node_pdb.7z
ffd472e223a8dbde11867016e51744dadb3e55af8dc3d663fb605a1560a63017 win-x86/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQGzBAEBCAAdFiEEiQwI24V5Fi/uDfnbi+q0389VXvQFAmnC9gcACgkQi+q0389V
XvR1ugwAiiv5SVNLVMJa5ww1CtXHbVX7Kd1vGXw9INsK1iIUrwT4T2lZa+KnztYx
ngwaxIa8h4/x9IS262tRYJUHqcQtRP+J8pD7ahnf+JW5BZN9HQ+C1jEy6TWrH5rt
zQfFUYrRM7jbWPXlDmFecBPpOC48mZyOe8I7UzDjQGY1KYx6HHutUi28bAbPxzi+
CzcpgsdhD/y/qhQW/DtlmFj4AWh1oFzZZW3C0mNRNgC96FVs61Xp4CXfiPO9vFwY
VjB2JHYkxVx2K1m5O4CcrtEEtg7LBpuzCNke/INnKXdh4UDqSBGXm/oAvl71VLgH
aICjDIKcS4TXmWmaSbPN4y6Lfe30a8CESRolX/5nvzAyQy/pVmmhyi1l15IzAQDu
b/efW5bZn7wJTcNJz64vqXNPE1eKfJES7cAabDkvxnAWQhf9JtZf406QH5c+Ygig
Yo/97a00Pv6/nBJLF4woxYBjG5/2hKxuhkOKQ9QnDqCXW0ACpWHn1aX+Stv5s6Ps
JNKkGS1v
=uiHn
-----END PGP SIGNATURE-----
```

---

## 11. Node.js 20.20.2 (LTS)

- 日期: 2026-03-24 20:35
- 链接: https://nodejs.org/en/blog/release/v20.20.2

```
Node.js 20.20.2 (LTS)
Marco Ippolito
2026-03-24, Version 20.20.2 'Iron' (LTS), @marco-ippolito
This is a security release.
Notable Changes
- (CVE-2026-21717) fix array index hash collision (Joyee Cheung) https://github.com/nodejs-private/node-private/pull/834
- (CVE-2026-21713) use timing-safe comparison in Web Cryptography HMAC and KMAC (Filip Skokan) https://github.com/nodejs-private/node-private/pull/822
- (CVE-2026-21710) use null prototype for headersDistinct/trailersDistinct (Matteo Collina) https://github.com/nodejs-private/node-private/pull/821
- (CVE-2026-21716) include permission check on lib/fs/promises (RafaelGSS) https://github.com/nodejs-private/node-private/pull/795
- (CVE-2026-21715) add permission check to realpath.native (RafaelGSS) https://github.com/nodejs-private/node-private/pull/794
- (CVE-2026-21714) handle NGHTTP2_ERR_FLOW_CONTROL error code (RafaelGSS) https://github.com/nodejs-private/node-private/pull/832
- (CVE-2026-21637) wrap SNICallback invocation in try/catch (Matteo Collina) https://github.com/nodejs-private/node-private/pull/819
Commits
- [
cfb51fa9ce
] - (CVE-2026-21713) crypto: use timing-safe comparison in Web Cryptography HMAC (Filip Skokan) nodejs-private/node-private#831 - [
f333d0be5f
] - deps: V8: overridedepot_tools
version (Richard Lau) #62344 - [
2acd5d1226
] - deps: update undici to v6.24.1 (Matteo Collina) #62285 - [
af5c144ebc
] - (CVE-2026-21717) deps,build,test: fix array index hash collision (Joyee Cheung) nodejs-private/node-private#834 - [
00ad47a28e
] - (CVE-2026-21710) http: use null prototype for headersDistinct/trailersDistinct (Matteo Collina) nodejs-private/node-private#821 - [
0123309566
] - (CVE-2026-21716) permission: include permission check on lib/fs/promises (RafaelGSS) nodejs-private/node-private#840 - [
00830712bc
] - (CVE-2026-21715) permission: add permission check to realpath.native (RafaelGSS) nodejs-private/node-private#838 - [
a0c73425da
] - (CVE-2026-21714) src: handle NGHTTP2_ERR_FLOW_CONTROL error code (RafaelGSS) nodejs-private/node-private#832 - [
cc3f294507
] - (CVE-2026-21637) tls: wrap SNICallback invocation in try/catch (Matteo Collina) nodejs-private/node-private#839
Windows 32-bit Installer: https://nodejs.org/dist/v20.20.2/node-v20.20.2-x86.msi
Windows 64-bit Installer: https://nodejs.org/dist/v20.20.2/node-v20.20.2-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v20.20.2/node-v20.20.2-arm64.msi
Windows 32-bit Binary: https://nodejs.org/dist/v20.20.2/win-x86/node.exe
Windows 64-bit Binary: https://nodejs.org/dist/v20.20.2/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v20.20.2/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v20.20.2/node-v20.20.2.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v20.20.2/node-v20.20.2-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v20.20.2/node-v20.20.2-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v20.20.2/node-v20.20.2-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v20.20.2/node-v20.20.2-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v20.20.2/node-v20.20.2-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v20.20.2/node-v20.20.2-aix-ppc64.tar.gz
ARMv7 32-bit Binary: https://nodejs.org/dist/v20.20.2/node-v20.20.2-linux-armv7l.tar.xz
ARMv8 64-bit Binary: https://nodejs.org/dist/v20.20.2/node-v20.20.2-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v20.20.2/node-v20.20.2.tar.gz
Other release files: https://nodejs.org/dist/v20.20.2/
Documentation: https://nodejs.org/docs/v20.20.2/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
3c60f54069a53ad8ffeef2b0f11e1f88333b12decfed755b26ce3fcb5e2d97e4 node-v20.20.2-aix-ppc64.tar.gz
1473f48d689627ec35eb4147d0f22ee60c694f16719c20a7c129b925c60f3a2f node-v20.20.2-arm64.msi
466e05f3477c20dfb723054dfebffe55bc74660ee77f612166fca121dacb65b6 node-v20.20.2-darwin-arm64.tar.gz
6375a1d4421bc04ab284ba89459df788a78c49c89e83c463d0eede47e2efc07b node-v20.20.2-darwin-arm64.tar.xz
8be6f5e4bb128c82774f8a0b8d7a1cc1365a7977d9657cece0ca647b3fe04e61 node-v20.20.2-darwin-x64.tar.gz
4d4c020eb534497e616de38f3733289ff33c615ddab38c048edec6547b7f76ea node-v20.20.2-darwin-x64.tar.xz
6de0e836efa9f32512e61db3dfd08b3d97a015b7e828d1a5efdf281a56a692d9 node-v20.20.2-headers.tar.gz
46573741c48c20c6bcfc71450e2fc56b4d1156d72c3d6cc9917fa8b1cbc6e836 node-v20.20.2-headers.tar.xz
47ef73d543ecf6eb19435f6c03a0ac4809b3bf0dd6b26c7c571efc2a6572a74d node-v20.20.2-linux-arm64.tar.gz
73093db209e4e9e09dd7d15a47aeaab1b74833830df03efa5f942a1122c5fa71 node-v20.20.2-linux-arm64.tar.xz
8e15f121e721c9354132053188d4c1a18ea9e345c019ee440fb256e3dda7df15 node-v20.20.2-linux-armv7l.tar.gz
f704ce75d9a194c30c378049b516000e49612c2f046ac83c7435eb33ec2926f0 node-v20.20.2-linux-armv7l.tar.xz
5f2fd0e0cd67aeac0db800b334151cae6ea70ea337487b26f79ac90e3fe126e1 node-v20.20.2-linux-ppc64le.tar.gz
4ee91307b3b517f880cd63d3f75fc91f4afc926ad9447661b755d50060ba2816 node-v20.20.2-linux-ppc64le.tar.xz
ee1ca1193e75a6d31b6007c575deca11b116e84a6bda136ae0e0dbe19399889c node-v20.20.2-linux-s390x.tar.gz
00590e7e1295d265fd22706e10467c03ecf170873b76c1835ff74b47b90ce6e0 node-v20.20.2-linux-s390x.tar.xz
19e56f0825510207dd904f087fe52faa0a4eb6b2aab5f0ea7a33830d04888b8b node-v20.20.2-linux-x64.tar.gz
df770b2a6f130ed8627c9782c988fda9669fa23898329a61a871e32f965e007d node-v20.20.2-linux-x64.tar.xz
63be4e81a9248c5a5ff5f4a67efffef6a4eaa976f5c7fb0b93027db36342e9a3 node-v20.20.2.pkg
8cb85a81f75169eb811f7b2512cf17a646826430debbe016a7461f31e286fdef node-v20.20.2.tar.gz
7aeeacdb858299e09a3e0510d4bb8b266923894a9e3ac0058ba89d4ecf4a4cca node-v20.20.2.tar.xz
f066ba3f80363f8e16a2737a945052ea910733f22c93821519f53667614bafd0 node-v20.20.2-win-arm64.7z
d5c5b1d56f7f9469830eb1f57efeec0a6a9078c0a9e88cd5b4b4b48f46c22069 node-v20.20.2-win-arm64.zip
1bbbfd0312335a95e86642c3beef98bb84def4cca85cd879f3da0baca6797422 node-v20.20.2-win-x64.7z
dc3700fdd57a63eedb8fd7e3c7baaa32e6a740a1b904167ff4204bc68ed8bf77 node-v20.20.2-win-x64.zip
4103cb79dba8c0272e309f8b337c2240369fcba5454bf10c2c4b23932a3c6033 node-v20.20.2-win-x86.7z
cd34d5da2f36ebd84ed57252756ee512447db4502d9f9e38ca8dccb511b0b352 node-v20.20.2-win-x86.zip
9a283dcdb771793d6492235e81f3fc80048db8a37497a0af87b0a9f450d10fa6 node-v20.20.2-x64.msi
5bd11635c4d46a14e5f712ffbddf07a8dc01d6e62c5ac1d20cab47b4fd7f5ce0 node-v20.20.2-x86.msi
a6c4adc2ea22256b5d2df57a981f1538d56d44fc845646a8bdbf66740ac1e948 win-arm64/node.exe
deacf784c804e5ab9df886b2de4c7a04d77ee1c722e2e4f1567aac62391ec4c4 win-arm64/node.lib
46512faa28642586c97e61b1a1431bc0a3b2a85e1d63a22794df3b7ebf8d4cfd win-arm64/node_pdb.7z
9a6ba8c56d58883584a27f861c784f203455e9ae4dd882836b16980c95dfa84c win-arm64/node_pdb.zip
56c1520ee33b801e8bdb92fb321cf2e98529735b6d12bd4a2a6dec0ac0bab937 win-x64/node.exe
c4a794e993d9304238523230885e9ec00ca052c73b9558471858eef14916d91f win-x64/node.lib
e190b1166cce167651d3bd544881420e4642ef2dfc643da0023dee9f91f44046 win-x64/node_pdb.7z
656f2062e5cb3057651381d0916ad79b9e2113625572a0745b70bc6844e4196a win-x64/node_pdb.zip
33379026333558256e5f467d80c67ba20f6b8e77e8d3ab72ad4dc005f6e11845 win-x86/node.exe
962e762b899969e773dc1163d53f1dca10a7769d73217b727a94574d2613355b win-x86/node.lib
a1f7bfe7e5536488b9270f1c1ea1d5b259753b7ee89dabf8eaabc59bfc26fb60 win-x86/node_pdb.7z
f9d592b4c57c9749d33570e80f6d63c4aaa2441fb86347c25b81d988c5955889 win-x86/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQIzBAEBCAAdFiEEzGj1oxBv9EgyLkjtJ/XjjVsKIV8FAmnC9VIACgkQJ/XjjVsK
IV//Pw//am3VN5wTtH+XMPNIyiFk7yrJPYKFhUPchoYVhKSjmnbdD6zn8F4n5KO6
t3P5mORXBai0GDBZA219moPX4CpBlVMDWUm87SPndc2nzS0PiGn/9b2vBOYErvel
lGPVaRq6MYE4mTKLIFBoApjJ5mBPPWWnzPOgB0nRw08Uv4rjWS88P4R7qohz2+V0
L/Szen1f/9F3ev9mGpFXlx4ylNww0ZDu0uJySweZEJE/9s5fq1EkGNQA4zpYpnyU
oqWHcL7ugQI7/2pQbUYk2W8WXTLi8bBuzjmP6mqetXDzltwchjtB8tmZhBqTKtPP
QrS0EcS3POe3hrriuqbm/VarpoRiOgexAG4YuzAMIldcSxNYMteSiP95WvPUfa9i
R7gcZ3KVyOVTtXUTTTqLWQrmzFeDmJNm1Y2n3B+mhKub8PuDwOMbvb77IoV51Azu
NpFSA+QmosLN3G/ydJI4L4JDme9MaYHPRSmBvEMryvpqNWjVoUn8OkHlmgGGreFu
QjyfxBzpYXkxkUHHt68wgIC/odUMxuiBWzLQ3pDlKgnR4bLL/uc+GnzXR6JES71X
NhZAwfLVFTQSBd6oq1ibU1SEObAVe4cIQEezwqT0qy2WFiyikXlgCNRHYtSPtjsf
A5s7j3cE8/naM28vHrt3kLmLIb5Gik5SL+N4Hig18vwKCyk+KkI=
=CXge
-----END PGP SIGNATURE-----
```

---

## 12. Tuesday, March 24, 2026 Security Releases

- 日期: 2026-03-24 03:00
- 链接: https://nodejs.org/en/blog/vulnerability/march-2026-security-releases

```
Tuesday, March 24, 2026 Security Releases
The Node.js Project
Security releases available
Updates are now available for the 25.x, 24.x, 22.x, 20.x Node.js release lines for the following issues.
This security release includes the following dependency updates to address public vulnerabilities:
- undici (6.24.1, 7.24.4) on 22.x, 24.x, 25.x
Incomplete fix for CVE-2026-21637: loadSNI()
in _tls_wrap.js
lacks try
/catch
leading to Remote DoS (CVE-2026-21637) - (High)
A flaw in Node.js TLS error handling leaves SNICallback
invocations unprotected against synchronous exceptions, while the equivalent ALPN and PSK callbacks were already addressed in CVE-2026-21637. This represents an incomplete fix of that prior vulnerability.
When an SNICallback
throws synchronously on unexpected input the exception bypasses TLS error handlers and propagates as an uncaught exception, crashing the Node.js process.
- This vulnerability affects all Node.js versions that received the CVE-2026-21637 fix, including 20.x, 22.x, 24.x, and 25.x, on any TLS server where
SNICallback
may throw on unexpectedservername
input.
Thank you, to mbarbs for reporting this vulnerability and thank you mcollina for fixing it.
Denial of Service via __proto__
header name in req.headersDistinct
(Uncaught TypeError
crashes Node.js process) (CVE-2026-21710) - (High)
A flaw in Node.js HTTP request handling causes an uncaught TypeError
when a request is received with a header named __proto__
and the application accesses req.headersDistinct
.
When this occurs, dest["__proto__"]
resolves to Object.prototype
rather than undefined
, causing .push()
to be called on a non-array. This exception is thrown synchronously inside a property getter and cannot be intercepted by error
event listeners, meaning it cannot be handled without wrapping every req.headersDistinct
access in a try/catch
.
- This vulnerability affects all Node.js HTTP servers on 20.x, 22.x, 24.x, and v25.x
Thank you, to yushengchen for reporting this vulnerability and thank you mcollina for fixing it.
Node.js Permission Model bypass: UDS server bind/listen works without --allow-net
(CVE-2026-21711) - (Medium)
A flaw in Node.js Permission Model network enforcement leaves Unix Domain Socket (UDS) server operations without the required permission checks, while all comparable network paths correctly enforce them.
As a result, code running under --permission
without --allow-net
can create and expose local IPC endpoints, allowing communication with other processes on the same host outside of the intended network restriction boundary.
- This vulnerability affects Node.js 25.x processes using the Permission Model where
--allow-net
is intentionally omitted to restrict network access. Note that--allow-net
is currently an experimental feature.
Thank you, to xavlimsg for reporting this vulnerability and thank you RafaelGSS for fixing it.
Assertion error in node_url.cc
via malformed URL format leads to Node.js crash (CVE-2026-21712) - (Medium)
A flaw in Node.js URL processing causes an assertion failure in native code when url.format()
is called with a malformed internationalized domain name (IDN) containing invalid characters, crashing the Node.js process.
- This vulnerability affects 24.x and 25.x.
Thank you, to wooffie for reporting this vulnerability and thank you RafaelGSS for fixing it.
Timing side-channel in HMAC verification via memcmp()
in crypto_hmac.cc
leads to potential MAC forgery (CVE-2026-21713) - (Medium)
A flaw in Node.js HMAC verification uses a non-constant-time comparison when validating user-provided signatures, potentially leaking timing information proportional to the number of matching bytes. Under certain threat models where high-resolution timing measurements are possible, this behavior could be exploited as a timing oracle to infer HMAC values.
Node.js already provides timing-safe comparison primitives used elsewhere in the codebase, indicating this is an oversight rather than an intentional design decision.
- This vulnerability affects 20.x, 22.x, 24.x, and 25.x.
Thank you, to x_probe for reporting this vulnerability and thank you panva for fixing it.
Memory leak in Node.js HTTP/2 server via WINDOW_UPDATE
on stream 0 leads to resource exhaustion (CVE-2026-21714) - (Medium)
A memory leak occurs in Node.js HTTP/2 servers when a client sends WINDOW_UPDATE
frames on stream 0 (connection-level) that cause the flow control window to exceed the maximum value of 2³¹-1. The server correctly sends a GOAWAY frame, but the Http2Session object is never cleaned up.
- This vulnerability affects HTTP2 users on Node.js 20, 22, 24 and 25.
Thank you, to galbarnahum for reporting this vulnerability and thank you RafaelGSS for fixing it.
HashDoS in V8 (CVE-2026-21717) - (Medium)
A flaw in V8's string hashing mechanism causes integer-like strings to be hashed to their numeric value, making hash collisions trivially predictable. By crafting a request that causes many such collisions in V8's internal string table, an attacker can significantly degrade performance of the Node.js process.
The most common trigger is any endpoint that calls JSON.parse()
on attacker-controlled input, as JSON parsing automatically internalizes short strings into the affected hash table.
- This vulnerability affects 20.x, 22.x, 24.x, and 25.x.
Thank you, to sharp_edged for reporting this vulnerability and thank you joyeecheung for fixing it.
Permission Model Bypass in realpathSync.native Allows File Existence Disclosure (CVE-2026-21715) - (Low)
A flaw in Node.js Permission Model filesystem enforcement leaves fs.realpathSync.native()
without the required read permission checks, while all comparable filesystem functions correctly enforce them.
As a result, code running under --permission
with restricted --allow-fs-read
can still use fs.realpathSync.native()
to check file existence, resolve symlink targets, and enumerate filesystem paths outside of permitted directories.
- This vulnerability affects 20.x, 22.x, 24.x, and 25.x processes using the Permission Model where
--allow-fs-read
is intentionally restricted.
Thank you, to stif for reporting this vulnerability and thank you RafaelGSS for fixing it.
CVE-2024-36137 Patch Bypass - FileHandle.chmod/chown (CVE-2026-21716) - (Low)
An incomplete fix for CVE-2024-36137 leaves FileHandle.chmod()
and FileHandle.chown()
in the promises API without the required permission checks, while their callback-based equivalents (fs.fchmod()
, fs.fchown()
) were correctly patched.
As a result, code running under --permission
with restricted --allow-fs-write
can still use promise-based FileHandle
methods to modify file permissions and ownership on already-open file descriptors, bypassing the intended write restrictions.
- This vulnerability affects 20.x, 22.x, 24.x, and 25.x processes using the Permission Model where
--allow-fs-write
is intentionally restricted.
Thank you, to wooseokdotkim for reporting this vulnerability and thank you RafaelGSS for fixing it.
Downloads and release details
Summary
The Node.js project will release new versions of the 25.x, 24.x, 22.x, 20.x releases lines on or shortly after, Tuesday, March 24, 2026 in order to address:
- 2 high severity issues.
- 5 medium severity issues.
- 2 low severity issues.
Impact
The 25.x release line of Node.js is vulnerable to 2 high severity issues, 5 medium severity issues, 2 low severity issues. The 24.x release line of Node.js is vulnerable to 2 high severity issues, 4 medium severity issues, 2 low severity issues. The 22.x release line of Node.js is vulnerable to 2 high severity issues, 4 medium severity issues, 2 low severity issues. The 20.x release line of Node.js is vulnerable to 2 high severity issues, 4 medium severity issues, 2 low severity issues.
It's important to note that End-of-Life versions are always affected when a security release occurs. To ensure your system's security, please use an up-to-date version as outlined in our Release Schedule.
Release timing
Releases will be available on, or shortly after, Tuesday, March 24, 2026.
Contact and future updates
The current Node.js security policy can be found at https://nodejs.org/en/security/. Please follow the process outlined in https://github.com/nodejs/node/blob/master/SECURITY.md if you wish to report a vulnerability in Node.js.
Subscribe to the low-volume announcement-only nodejs-sec mailing list at https://groups.google.com/forum/#!forum/nodejs-sec to stay up to date on security vulnerabilities and security-related releases of Node.js and the projects maintained in the nodejs GitHub organization.
```

---

## 13. Node.js 25.8.1 (Current)

- 日期: 2026-03-11 09:02
- 链接: https://nodejs.org/en/blog/release/v25.8.1

```
Node.js 25.8.1 (Current)
Antoine du Hamel
2026-03-11, Version 25.8.1 (Current), @aduh95
Notable Changes
- [
ea87eea71a
] - module: fix extensionless CJS files in"type": "module"
packages (Matteo Collina) #62083
Commits
- [
bab750d1b3
] - build: do not depend on V8 deps on--without-bundled-v8
builds (Antoine du Hamel) #62033 - [
b26d1c7fcb
] - crypto: make --use-system-ca per-env rather than per-process (Aditi) #60678 - [
e362635abf
] - crypto: add missing AES dictionaries (Filip Skokan) #62099 - [
6f975db8af
] - crypto: fix importKey required argument count check (Filip Skokan) #62099 - [
3beaf9c5fc
] - deps: update amaro to 1.1.8 (Node.js GitHub Bot) #62151 - [
53afb0edd8
] - deps: update sqlite to 3.52.0 (Node.js GitHub Bot) #62150 - [
a13ed052a1
] - deps: update merve to 1.2.0 (Node.js GitHub Bot) #62149 - [
2c850577b7
] - deps: patch resb crate (Richard Lau) #62138 - [
37862a6728
] - deps: V8: cherry-pick aa0b288f87cc (Richard Lau) #62136 - [
09191ad8b4
] - deps: update ada to 3.4.3 (Node.js GitHub Bot) #62049 - [
8d63a178fd
] - doc: copyeditaddons.md
(Antoine du Hamel) #62071 - [
83719ffb64
] - doc: correctutil.convertProcessSignalToExitCode
validation behavior (René) #62134 - [
eeee7c7fb1
] - doc: add efekrskl as triager (Efe) #61876 - [
db150b2e69
] - doc: fix markdown forexpectFailure
values (Jacob Smith) #62100 - [
d55a441e60
] - doc: add title to index (Aviv Keller) #62046 - [
cc46204b48
] - doc: include url.resolve() in DEP0169 application deprecation (Mike McCready) #62002 - [
1d91a7261e
] - doc,module: add missing doc for syncHooks.deregister() (Joyee Cheung) #61959 - [
5198573bee
] - http: fix use-after-free when freeParser is called during llhttp_execute (Gerhard Stöbich) #62095 - [
f8793f80df
] - lib: fix source map url parse in dynamic imports (Chengzhong Wu) #61990 - [
5439d0e0cf
] - meta: bump actions/download-artifact from 7.0.0 to 8.0.0 (dependabot[bot]) #62063 - [
27fd21943a
] - meta: bump actions/upload-artifact from 6.0.0 to 7.0.0 (dependabot[bot]) #62062 - [
5b266f3295
] - meta: bump step-security/harden-runner from 2.14.2 to 2.15.0 (dependabot[bot]) #62064 - [
ea87eea71a
] - module: fix extensionless CJS files in"type": "module"
packages (Matteo Collina) #62083 - [
851228cd60
] - sqlite: handle stmt invalidation (Guilherme Araújo) #61877 - [
19efe60548
] - src: expose async context frame debugging helper to JS (Anna Henningsen) #62103 - [
0257e8072f
] - src: make AsyncWrap subclass internal field counts explicit (Anna Henningsen) #62103 - [
975dafbe3b
] - src: release context frame in AsyncWrap::EmitDestroy (Gerhard Stöbich) #61995 - [
f2c08c7888
] - src: use validate_ascii_with_errors instead of validate_ascii (Сковорода Никита Андреевич) #61122 - [
0278461d83
] - stream: optimize webstreams pipeTo (Mattias Buelens) #62079 - [
4d62e95bfa
] - stream: fix brotli error handling in web compression streams (Filip Skokan) #62107 - [
4bdcaf2865
] - stream: improve Web Compression spec compliance (Filip Skokan) #62107 - [
a5b1be2045
] - stream: fix UTF-8 character corruption in fast-utf8-stream (Matteo Collina) #61745 - [
5632446c4e
] - stream: fix TransformStream race on cancel with pending write (Marco) #62040 - [
f90fa9cd1a
] - stream: accept ArrayBuffer in CompressionStream and DecompressionStream (조수민) #61913 - [
00319eaa3a
] - test: update WPT for url to c928b19ab0 (Node.js GitHub Bot) #62148 - [
456abc7d20
] - test: update WPT for WebCryptoAPI to c9e955840a (Node.js GitHub Bot) #62147 - [
82770cb7d3
] - test: improve WPT report runner (Filip Skokan) #62107 - [
cfc847d233
] - test: update WPT compression to ae05f5cb53 (Filip Skokan) #62107 - [
80f78f2737
] - test: update WPT for WebCryptoAPI to 42e47329fd (Node.js GitHub Bot) #62048 - [
8048e0508c
] - test: fix skipping behavior fortest-runner-run-files-undefined
(Antoine du Hamel) #62026 - [
699a6214c6
] - tools: revert timezone update GHA workflow to ubuntu-latest (Richard Lau) #62140 - [
1a453b550c
] - tools: improve error handling in test426 update script (Rich Trott) #62121 - [
710dde5ee2
] - tools: fix--node-builtin-modules-path
value inshell.nix
(Antoine du Hamel) #62102 - [
dcb1cbb21f
] - tools: bump the eslint group across 1 directory with 2 updates (dependabot[bot]) #62092 - [
7d0b758583
] - tools: fix daily wpt workflow nighly release version lookup (Filip Skokan) #62076 - [
3e8c816f2e
] - tools: fix example in release proposal linter (Richard Lau) #62074 - [
772d3d270d
] - tools: bump minimatch from 3.1.3 to 3.1.5 in /tools/clang-format (dependabot[bot]) #62013 - [
92f3b42672
] - tools: bump eslint to v10, babel to v8.0.0-rc.2 (Huáng Jùnliàng) #61905 - [
deead95ec5
] - url: suppress warnings from url.format/url.resolve inside node_modules (René) #62005
Windows 64-bit Installer: https://nodejs.org/dist/v25.8.1/node-v25.8.1-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v25.8.1/node-v25.8.1-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v25.8.1/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v25.8.1/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v25.8.1/node-v25.8.1.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v25.8.1/node-v25.8.1-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v25.8.1/node-v25.8.1-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v25.8.1/node-v25.8.1-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v25.8.1/node-v25.8.1-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v25.8.1/node-v25.8.1-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v25.8.1/node-v25.8.1-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v25.8.1/node-v25.8.1-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v25.8.1/node-v25.8.1.tar.gz
Other release files: https://nodejs.org/dist/v25.8.1/
Documentation: https://nodejs.org/docs/v25.8.1/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
4b1c7bd9c1648cfe751088e45d1f233be0bc00139a647312a6271b5a54db1f70 node-v25.8.1-aix-ppc64.tar.gz
3a43f14bb621b7702d7b69b08e771f521ccc50c30e6205c295fb028012be1798 node-v25.8.1-arm64.msi
c667629236e3213616f0917b84eb52706e213c0e8a2312402335fff6fc7463c4 node-v25.8.1-darwin-arm64.tar.gz
f213fc27a210b0c37a1499cc5d5aeb751df7d327ea7dffee22d6f5fefdd56cd7 node-v25.8.1-darwin-arm64.tar.xz
1e5ebf69955e01216f5c60b9c989d1bdda8e5022e2f60c75e1baf309c5bff50e node-v25.8.1-darwin-x64.tar.gz
88a7f357c95f3de40f68f5bee5c89152e50629b19413d1515c3a08a3c7c8d15c node-v25.8.1-darwin-x64.tar.xz
ebbc965a58ebb4e4cf7f2abe6629e7afaa80a4396fb25a57a6097f14ee9ee666 node-v25.8.1-headers.tar.gz
0630c301cd04dc356867ef5b3d4f016c4fad44a54dcc67a876b3f4118b89a712 node-v25.8.1-headers.tar.xz
d990ec3c21ce8bdb6f76ed4e1c875d6e3e4b75a02d018e85df0662c0bad83b53 node-v25.8.1-linux-arm64.tar.gz
7786cee7ed4cc166b2d0ecbd3220a5a595290fdf6da898a348a8ff9f37d1f10e node-v25.8.1-linux-arm64.tar.xz
b14c43fba9fdd3cd2ceedf558233502a1e6fc7a604c7bc633018d6d61d92bd1d node-v25.8.1-linux-ppc64le.tar.gz
569e25fed50abdb481b3b72694da07c25dac590e1df07dd818aa72a558c9cc1f node-v25.8.1-linux-ppc64le.tar.xz
7c7826f9a879d11720d1c68aca36ac3d1d9eec697982139e6b45f42e260d0391 node-v25.8.1-linux-s390x.tar.gz
e5d944362b4fb8a8b0b60baad797b03e4e0e46b6b0d3f4d28500c9ab215852d4 node-v25.8.1-linux-s390x.tar.xz
6fe3b8fa448579f728f7a0e5bbb3ab6a352d2c6307e13ae37a86106a3e4c9aaf node-v25.8.1-linux-x64.tar.gz
8c13c85f73b1f8e57d5fff0732b3f25880910aafa6d5c811073a2ec7fcd45b4c node-v25.8.1-linux-x64.tar.xz
6c780bb368eb1f76f4900892e82be4872f67d2dd089f04c9113e4372ae7bea08 node-v25.8.1-win-arm64.7z
0c5be793a169db0812f8549b367fc1591bd3e4c401a5c700dd8b8b2cc2e74c5e node-v25.8.1-win-arm64.zip
bb1518746cab560370fb402c3fe17ddd527141a2a341043d5e7db5d39b98d4be node-v25.8.1-win-x64.7z
09a5a0dbb2f4cefa800880012810e2dfaac0016a62e75f064c4ab7f3606b2d78 node-v25.8.1-win-x64.zip
7d9968aba0b0a9c4410a4e8cef882e96dca620c7e184bd3924902783d0f1432c node-v25.8.1-x64.msi
06560beed6b74fea37e5c52b65e958718b659a07c36e9b36e0a12ef40a7fd106 node-v25.8.1.pkg
e7dd99bb71ed406d2604180f14d6ee5789fbaf48f5cff9bae72bdb32c8df7457 node-v25.8.1.tar.gz
0b25b2b5fab80ea8b43fdaa7451f50065571e0bfda2524ca42bde8b98fe4d2d9 node-v25.8.1.tar.xz
4e455096a1cea3dbfb90fb685cc713211dbf5c830cc249de7cb75a332222479b win-arm64/node.exe
47750ee99207e5b621671565852cf7385f27bf664470886b9437137342a497c9 win-arm64/node.lib
2c765bdae94193494779d3f14c9f280f027c5b31ffcceed0f1012ae8c4936d51 win-arm64/node_pdb.7z
8742a1419a3df14b39fc0d3d235073be6bbc4dc435322a36c608bda55ff9d14e win-arm64/node_pdb.zip
8ccfc9b16942fd1f4154e160a249805dd88eb0d253b789aa669b91cf0ade6e57 win-x64/node.exe
f7201b932d898bdbf78aee7add288d2263c4791f1502068ad11b6c14675c6324 win-x64/node.lib
481bd002f65388f9f9b2471418f20dd0dcf0150b667f0078be21ee2fd536c6d5 win-x64/node_pdb.7z
4f47a9c0785ed00a3cdd0aeba8ba214e0399d4a5fb988dae543b9238182467df win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iHUEARYIAB0WIQRb6KP2yKXAHRBsCtggsaOQsWjTVgUCabEvWQAKCRAgsaOQsWjT
Vt5kAP40TQ2UotUW/yCG47JnY7o7odnKhgtTEd8fHDSGhkrHPgEA3t+b44YZc8nL
9hDpIi0xnrLGVriH9JfQ5r3M4KccxAE=
=Rekf
-----END PGP SIGNATURE-----
```

---

## 14. Evolving the Node.js Release Schedule

- 日期: 2026-03-10 16:00
- 链接: https://nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule

```
Evolving the Node.js Release Schedule
Node.js Releasers
Starting with 27.x, Node.js will move from two major releases per year to one. This post explains what's changing, why, and what it means for users. For the full discussion and background, see nodejs/Release#1113.
TL;DR: If you already only upgrade to LTS versions, little changes beyond version numbering. LTS support windows remain similar, and now every release becomes LTS.
Library authors: Please integrate Alpha releases to your CI as early as possible; if you only test on LTS releases, you will not be able to report bugs before they affect your users.
Why This Change
The current release schedule is 10 years old. It was created during the io.js merger to balance the needs of a growing ecosystem. As one contributor put it at the time, it was "an educated guess of what enterprises would need."
We now have a decade of data showing how people actually use Node.js:
- Odd-numbered releases see minimal adoption. Most users wait for Long-Term Support.
- The odd/even distinction confuses newcomers.
- Many organizations skip odd releases entirely, upgrading only to LTS versions.
We also recognize that enterprises need predictability. The new schedule is designed to be well-defined, so teams can plan upgrades and allocate resources accordingly.
Volunteer Sustainability
Node.js is maintained primarily by volunteers. While some contributors receive sponsorship, most of the work (reviewing Pull Requests, handling security issues, cutting releases, backporting fixes) is done by people in their spare time.
Managing security releases across four or five active release lines has become difficult to sustain. Each additional line increases backporting complexity. By reducing the number of concurrent release lines, we can focus on better supporting the releases people actually use.
What's Changing
As of October 2026:
- One major release per year (April), with LTS promotion in October.
- Every release becomes LTS. No more odd/even distinction - Node.js 27 will become LTS.
- Alpha channel for early testing with semver-major changes allowed.
- Alpha versioning follows semver prerelease format (e.g.,
27.0.0-alpha.1
). - Version numbers align with the calendar year of their initial Current release: 27.0.0 in 2027, 28.0.0 in 2028.
- Reduced Releasers' burden.
New Schedule
Total support: 36 months from first Current release to End of Life (EOL).
About the Alpha Channel
The Alpha channel fills the early-testing role that odd-numbered releases once served, but with a key difference: semver-major changes are allowed during Alpha. Alpha releases are signed, tagged, and tested through CITGM. CITGM (Canary in the Goldmine) is a tool we maintain that runs the test suite of major open-source packages on the upcoming version of Node.js, which can let us detect ecosystem breakage and notify the package authors ahead of the release.
This is different from Nightly builds, which remain
available as automated untested builds from main
– Alpha releases may not contain all changes from
main
, a change may not be included in an Alpha release if:
- during Pull Request review, reviewers add a label requesting the change not to be backported (e.g. if an API is getting runtime deprecated in an Alpha release, the change actually removing that API should not land until the next release line).
- during the Alpha release preparation, the releaser ultimately decides which commits actually make the release (e.g. if a dependency update contains a major bug).
Who it's for: Library authors and CI pipelines testing compatibility with upcoming breaking changes. Not intended for production use.
What to expect:
- Releases are signed and tagged (unlike nightly).
- API may change between releases.
- The release cadence is flexible; the Release Team will determine the timing and frequency of Alpha releases based on the volume of changes and project needs.
Why: Provides early feedback on breaking changes with quality gates that Nightly builds lack. Also allows landing V8 updates earlier in the cycle.
The rules for shipping semver-major commits in Alpha versions will be defined by the Release Team and documented in the Release repository.
What's NOT Changing
- Long-Term Support duration remains similar (30 months).
- Migration windows preserved. Overlap between LTS versions remains.
- Quality standards unchanged. Same testing, same CITGM, same security process.
- Predictable schedule. April releases, October LTS promotion.
- V8 adoption cycle. Node.js latest releases will still include a version of V8 that's at most about 6 months old.
Timeline
Node.js 26 Schedule (existing model)
Node.js 26 follows the existing schedule. This is the last release line under the current model.
Node.js 27 Schedule (new model)
Node.js 27 is the first release line under the new schedule.
The Next 10 Years
This schedule is not final and may be amended. Refer to the
schedule.json
for an up-to-date
record of the support claims from the project.
Thank You
This change is the result of discussions across GitHub issues, Release Working Group meetings, and the Collaboration Summit Chesapeake 2025. We will continue discussing this topic at the upcoming Collaboration Summit in London. We thank everyone who contributed feedback.
For questions or comments, see nodejs/Release#1113.
```

---

## 15. Node.js 22.22.1 (LTS)

- 日期: 2026-03-05 14:36
- 链接: https://nodejs.org/en/blog/release/v22.22.1

```
Node.js 22.22.1 (LTS)
Marco Ippolito
2026-03-05, Version 22.22.1 'Jod' (LTS), @marco-ippolito prepared by @aduh95
Notable Changes
- [
7b93a65f27
] - build: test on Python 3.14 (Christian Clauss) #59983 - [
6063d888fe
] - cli: mark--heapsnapshot-near-heap-limit
as stable (Joyee Cheung) #60956 - [
d950b151a2
] - crypto: update root certificates to NSS 3.119 (Node.js GitHub Bot) #61419 - [
4f42f8c428
] - crypto: update root certificates to NSS 3.117 (Node.js GitHub Bot) #60741 - [
b6ebf2cd53
] - doc: add avivkeller to collaborators (Aviv Keller) #61115 - [
35854f424d
] - doc: add gurgunday to collaborators (Gürgün Dayıoğlu) #61094 - [
5c6a076e5d
] - meta: add Renegade334 to collaborators (Renegade334) #60714
Commits
- [
5f773488c2
] - assert: use a set instead of an array for faster lookup (Ruben Bridgewater) #61076 - [
feecbb0eab
] - assert,util: fix deep comparison for sets and maps with mixed types (Ruben Bridgewater) #61388 - [
096095b127
] - benchmark: add SQLite benchmarks (Guilherme Araújo) #61401 - [
b5fe481415
] - benchmark: use boolean options in benchmark tests (SeokhunEom) #60129 - [
fa9faacacb
] - benchmark: allow boolean option values (SeokhunEom) #60129 - [
ba8714ac21
] - benchmark: fix incorrect base64 input in byteLength benchmark (semimikoh) #60841 - [
53596de876
] - benchmark: use typescript for import cjs benchmark (Joyee Cheung) #60663 - [
e8930e9d7c
] - benchmark: focus on import.meta intialization in import-meta benchmark (Joyee Cheung) #60603 - [
1155e412b1
] - benchmark: add per-suite setup option (Joyee Cheung) #60574 - [
e01903d304
] - benchmark: improve cpu.sh for safety and usability (Nam Yooseong) #60162 - [
623a405747
] - benchmark: add benchmark for leaf source text modules (Joyee Cheung) #60205 - [
7f5e7b9f7f
] - benchmark: add microbench on isInsideNodeModules (Chengzhong Wu) #60991 - [
db132b85a8
] - bootstrap: initialize http proxy after user module loader setup (Joyee Cheung) #58938 - [
66aab9f987
] - buffer: let Buffer.of use heap (Сковорода Никита Андреевич) #60503 - [
c3cf00c671
] - buffer: speed up concat via TypedArray#set (Gürgün Dayıoğlu) #60399 - [
f6fad231e9
] - build: skip sscache action on non-main branches (Joyee Cheung) #61790 - [
2145f91f6b
] - build: update android-patches/trap-handler.h.patch (Mo Luo) #60369 - [
5b49759dd8
] - build: update devcontainer.json to use paired nix env (Joyee Cheung) #61414 - [
24724cde40
] - build: fix misplaced comma in ldflags (hqzing) #61294 - [
c57a19934e
] - build: fix crate vendor file checksums on windows (Chengzhong Wu) #61329 - [
8659d7cd07
] - build: fix inconsistent quoting inMakefile
(Antoine du Hamel) #60511 - [
44f339b315
] - build: remove temporal updater (Chengzhong Wu) #61151 - [
d60a6cebd5
] - build: update test-wpt-report to use NODE instead of OUT_NODE (Filip Skokan) #61024 - [
34ccf187f5
] - build: skip build-ci on actions with a separate test step (Chengzhong Wu) #61073 - [
7b19e101a2
] - build: run embedtest with node_g when BUILDTYPE=Debug (Chengzhong Wu) #60850 - [
9408c4459f
] - build: upgrade Python linter ruff, add rules ASYNC,PERF (Christian Clauss) #59984 - [
2166ec7f0f
] - build: use call command when calling python configure (Jacob Nichols) #60098 - [
73ef70145d
] - build: remove V8_COMPRESS_POINTERS_IN_ISOLATE_CAGE defs (Joyee Cheung) #60296 - [
7b93a65f27
] - build: test on Python 3.14 (Christian Clauss) #59983 - [
508ce6ec6c
] - build, src: fix include paths for vtune files (Rahul) #59999 - [
c89d3cd570
] - build,tools: fix addon build deadlock on errors (Vladimir Morozov) #61321 - [
40904a0591
] - build,win: update WinGet configurations to Python 3.14 (Mike McCready) #61431 - [
6d6742e7db
] - child_process: treat ipc length header as unsigned uint32 (Ryuhei Shima) #61344 - [
6063d888fe
] - cli: mark --heapsnapshot-near-heap-limit as stable (Joyee Cheung) #60956 - [
3d324a0f88
] - cluster: fix port reuse between cluster (Ryuhei Shima) #60141 - [
40a58709b4
] - console: optimize single-string logging (Gürgün Dayıoğlu) #60422 - [
d950b151a2
] - crypto: update root certificates to NSS 3.119 (Node.js GitHub Bot) #61419 - [
4f42f8c428
] - crypto: update root certificates to NSS 3.117 (Node.js GitHub Bot) #60741 - [
a87499ae25
] - crypto: ensure documented RSA-PSS saltLength default is used (Filip Skokan) #60662 - [
8c65cc11e2
] - crypto: update root certificates to NSS 3.116 (Node.js GitHub Bot) #59956 - [
91dc00a2c1
] - debugger: fix event listener leak in the run command (Joyee Cheung) #60464 - [
bfc2b55c5a
] - deps: update minimatch to 10.2.4 (Node.js GitHub Bot) #62016 - [
7d318a0ba8
] - deps: update minimatch to 10.2.2 (Node.js GitHub Bot) #61830 - [
87351a42b5
] - deps: update minimatch to 10.1.2 (Node.js GitHub Bot) #61732 - [
0781bd3764
] - deps: V8: backport 6a0a25abaed3 (Vivian Wang) #61688 - [
0cf1f9c3e9
] - deps: update googletest to 85087857ad10bd407cd6ed2f52f7ea9752db621f (Node.js GitHub Bot) #61417 - [
521b4b1f07
] - deps: update sqlite to 3.51.2 (Node.js GitHub Bot) #61339 - [
58b9d219a3
] - deps: update icu to 78.2 (Node.js GitHub Bot) #60523 - [
cbc1e4306d
] - deps: update zlib to 1.3.1-e00f703 (Node.js GitHub Bot) #61135 - [
db59c35ed8
] - deps: update cjs-module-lexer to 2.2.0 (Node.js GitHub Bot) #61271 - [
c18518ee3c
] - deps: update nbytes to 0.1.2 (Node.js GitHub Bot) #61270 - [
376df62d63
] - deps: update timezone to 2025c (Node.js GitHub Bot) #61138 - [
993e905302
] - deps: update simdjson to 4.2.4 (Node.js GitHub Bot) #61056 - [
b72fd2a5d3
] - deps: update googletest to 065127f1e4b46c5f14fc73cf8d323c221f9dc68e (Node.js GitHub Bot) #61055 - [
d765147405
] - deps: update sqlite to 3.51.1 (Node.js GitHub Bot) #60899 - [
37abe2a7d2
] - deps: update zlib to 1.3.1-63d7e16 (Node.js GitHub Bot) #60898 - [
97241fcb86
] - deps: update sqlite to 3.51.0 (Node.js GitHub Bot) #60614 - [
3669c7b4f4
] - deps: update simdjson to 4.2.2 (Node.js GitHub Bot) #60740 - [
9a056ec89c
] - deps: update googletest to 1b96fa13f549387b7549cc89e1a785cf143a1a50 (Node.js GitHub Bot) #60739 - [
b5803b3ea0
] - deps: update minimatch to 10.1.1 (Node.js GitHub Bot) #60543 - [
5bf99f3d46
] - deps: update cjs-module-lexer to 2.1.1 (Node.js GitHub Bot) #60646 - [
801f187357
] - deps: update simdjson to 4.2.1 (Node.js GitHub Bot) #60644 - [
03c16e5a4c
] - deps: update simdjson to 4.1.0 (Node.js GitHub Bot) #60542 - [
2ebfc2ca56
] - deps: update amaro to 1.1.5 (Node.js GitHub Bot) #60541 - [
d24ba4fed6
] - deps: update simdjson to 4.0.7 (Node.js GitHub Bot) #59883 - [
9480a139bf
] - deps: update googletest to 279f847 (Node.js GitHub Bot) #60219 - [
635e67379e
] - deps: update archs files for openssl-3.5.5 (Node.js GitHub Bot) #61547 - [
c7b774047d
] - deps: upgrade openssl sources to openssl-3.5.5 (Node.js GitHub Bot) #61547 - [
5b324d7d7f
] - deps: update corepack to 0.34.6 (Node.js GitHub Bot) #61510 - [
eef8ba0667
] - deps: update corepack to 0.34.5 (Node.js GitHub Bot) #60842 - [
490f7c7fb1
] - deps: update corepack to 0.34.4 (Node.js GitHub Bot) #60643 - [
66903ea3b3
] - deps: update corepack to 0.34.2 (Node.js GitHub Bot) #60550 - [
a2f0b69282
] - deps: update corepack to 0.34.1 (Node.js GitHub Bot) #60314 - [
c8044a48a6
] - deps: V8: backport 2e4c5cf9b112 (Michaël Zasso) #60654 - [
642f518198
] - doc: supported toolchain with Visual Studio 2022 only (Mike McCready) #61451 - [
625f674487
] - doc: move Security-Team from TSC to SECURITY (Rafael Gonzaga) #61495 - [
029e32f8ba
] - doc: addedrequestOCSP
option totls.connect
(ikeyan) #61064 - [
68e33dfa89
] - doc: restore @ChALkeR to collaborators (Сковорода Никита Андреевич) #61553 - [
e016770d62
] - doc: update IBM/Red Hat volunteers with dedicated project time (Beth Griggs) #61588 - [
ec63954657
] - doc: mention constructor comparison in assert.deepStrictEqual (Hamza Kargin) #60253 - [
c8e1563a98
] - doc: add CVE delay mention (Rafael Gonzaga) #61465 - [
4b00cf2b54
] - doc: include OpenJSF handle for security stewards (Rafael Gonzaga) #61454 - [
4b73bf5bc8
] - doc: clarify process.argv[1] behavior for -e/--eval (Jeevankumar S) #61366 - [
d3151df4b3
] - doc: remove Windows Dev Home instructions from BUILDING (Mike McCready) #61434 - [
2323462e35
] - doc: clarify TypedArray properties on Buffer (Roman Reiss) #61355 - [
6c5478c8b2
] - doc: note resume build should not be done on node-test-commit (Stewart X Addison) #61373 - [
ba4a043103
] - doc: refine WebAssembly error documentation (sangwook) #61382 - [
cd315ea589
] - doc: add deprecation history for url.parse (Eng Zer Jun) #61389 - [
42db0c392d
] - doc: add marco and rafael in last sec release (Marco Ippolito) #61383 - [
4c3b680fc7
] - doc: packages: example of private import switch to internal (coderaiser) #61343 - [
684d15e421
] - doc: add esm and cjs examples to node:v8 (Alfredo González) #61328 - [
c3f9c7a7d9
] - doc: added 'secure' event to tls.TLSSocket (ikeyan) #61066 - [
aa9acad5ca
] - doc: restore @watilde to collaborators (Daijiro Wachi) #61350 - [
9cafec084e
] - doc: run license-builder (github-actions[bot]) #61348 - [
cdb12ccbc6
] - doc: document ALPNCallback option for TLSSocket constructor (ikeyan) #61331 - [
461c5e65c5
] - doc: update MDN links (Livia Medeiros) #61062 - [
dde45baeab
] - doc: add documentation for process.traceProcessWarnings (Alireza Ebrahimkhani) #53641 - [
59a7aeec92
] - doc: fix filename typo (Hardanish Singh) #61297 - [
9a0a40d1ed
] - doc: fix typos and grammar inBUILDING.md
&onboarding.md
(Hardanish Singh) #61267 - [
dca7005f9d
] - doc: mention --newVersion release script (Rafael Gonzaga) #61255 - [
c0dc8ddf85
] - doc: correct typo in api contributing doc (Mike McCready) #61260 - [
066af38fe1
] - doc: add PR-URL requirement for security backports (Rafael Gonzaga) #61256 - [
71dd46bd0c
] - doc: add reusePort error behavior to net module (mag123c) #61250 - [
f6abe3ba33
] - doc: note corepack package removal in distribution doc (Mike McCready) #61207 - [
9059d49d8c
] - doc: fix tls.connect() timeout documentation (Azad Gupta) #61079 - [
e7b34b76b0
] - doc: missingpassed
,error
andpassed
properties onTestContext
(Xavier Stouder) #61185 - [
9ae2dcfbb6
] - doc: clarify threat model for application-level API exposure (Rafael Gonzaga) #61184 - [
9902331a7c
] - doc: correct options for net.Socket class and socket.connect (Xavier Stouder) #61179 - [
a80122d2fe
] - doc: document error event on readline InterfaceConstructor (Xavier Stouder) #61170 - [
38d73c9cfa
] - doc: add a smooth scrolling effect to the sidebar (btea) #59007 - [
95c51fa984
] - doc: correct invalid collaborator profile (JJ) #61091 - [
f5a044763c
] - doc: exclude compile-time flag features from security policy (Matteo Collina) #61109 - [
b6ebf2cd53
] - doc: add @avivkeller to collaborators (Aviv Keller) #61115 - [
35854f424d
] - doc: add gurgunday to collaborators (Gürgün Dayıoğlu) #61094 - [
4932322c29
] - doc: add File modes cross-references in fs methods (Mohit Raj Saxena) #60286 - [
c84904e047
] - doc: add missingzstd
to mjs example of zlib (Deokjin Kim) #60915 - [
e615b9e2f2
] - doc: clarify fileURLToPath security considerations (Rafael Gonzaga) #60887 - [
99e384e6d4
] - doc: replace column with columnNumber in example ofutil.getCallSites
(Deokjin Kim) #60881 - [
9351bb4d02
] - doc: correct spelling in BUILDING.md (Rich Trott) #60875 - [
e1f6e7fc4d
] - doc: update debuglog examples to use 'foo-bar' instead of 'foo' (xiaoyao) #60867 - [
ccbb2d7300
] - doc: fix typos in changelogs (Rich Trott) #60855 - [
1cb2fe8b35
] - doc: mark module.register as active development (Chengzhong Wu) #60849 - [
ceeb4968a6
] - doc: add fullName property to SuiteContext (PaulyBearCoding) #60762 - [
56155909dd
] - doc: keep sidebar module visible when navigating docs (Botato) #60410 - [
6b637763d5
] - doc: correct concurrency wording in test() documentation (Azad Gupta) #60773 - [
7183e8ffa1
] - doc: clarify that CQ only picks up PRs targetingmain
(René) #60731 - [
d5d94303be
] - doc: clarify license section and add contributor note (KaleruMadhu) #60590 - [
e0210c8f53
] - doc: correct tls ALPNProtocols types (René) #60143 - [
eff87b498a
] - doc: remove mention of SMS 2FA (Antoine du Hamel) #60707 - [
e77ef94a51
] - doc:domain.add()
does not accept timer objects (René) #60675 - [
4fe19c95ea
] - doc: update Collaborators list to reflect hybrist handle change (Antoine du Hamel) #60650 - [
eece59b6ce
] - doc: fix linter issues (Antoine du Hamel) #60636 - [
6e17e596e4
] - doc: correct values/references for buffer.kMaxLength (René) #60305 - [
ac327ae9a7
] - doc: recommend events.once to manage 'close' event (Dan Fabulich) #60017 - [
d9b149ea42
] - doc: highlight module loading difference between import and require (Ajay A) #59815 - [
f6d62cb22c
] - doc: fix typo inprocess.unref
documentation (우혁) #59698 - [
6d5078b196
] - doc: add some entries toglossary.md
(Mohataseem Khan) #59277 - [
b0a5820dea
] - doc: improve agent.createConnection docs for http and https agents (JaeHo Jang) #58205 - [
b5db02fe67
] - doc: fix pseudo code in modules.md (chirsz) #57677 - [
e9b912d481
] - doc: add missing variable in code snippet (Koushil Mankali) #55478 - [
44c06c7812
] - doc: add missing word insingle-executable-applications.md
(Konstantin Tsabolov) #53864 - [
482b43f160
] - doc: fix typo in http.md (Michael Solomon) #59354 - [
cd323bc718
] - doc: update devcontainer.json and add documentation (Joyee Cheung) #60472 - [
c7c70f3a16
] - doc: add haramj as triager (Haram Jeong) #60348 - [
04b8c4d14e
] - doc: clarify require(esm) description (dynst) #60520 - [
de382dc832
] - doc: instantiate resolver object (Donghoon Nam) #60476 - [
b6845ce460
] - doc: clarify --use-system-ca support status (Joyee Cheung) #60340 - [
0894dae9bc
] - doc: add missing CAA type to dns.resolveAny() & dnsPromises.resolveAny() (Jimmy Leung) #58899 - [
c86a69f692
] - doc: useany
forworker_threads.Worker
'error' event argumenterr
(Jonas Geiler) #60300 - [
0c5031e233
] - doc: update decorator documentation to reflect actual policy (Muhammad Salman Aziz) #60288 - [
b01f710175
] - doc: document wildcard supported by tools/test.py (Joyee Cheung) #60265 - [
b4524dabcc
] - doc: fixblob.bytes()
heading level (XTY) #60252 - [
5df02776e3
] - doc: fix not working code example in vm docs (Artur Gawlik) #60224 - [
6a4359a0b5
] - doc: improve code snippet alternative of url.parse() using WHATWG URL (Steven) #60209 - [
ad06bee70d
] - doc: use markdown when branch-diff major release (Rafael Gonzaga) #60179 - [
c0d4b11ed4
] - doc: update teams in collaborator-guide.md and add links (Bart Louwers) #60065 - [
20b5ffcac3
] - doc: update previous version links in BUILDING (Mike McCready) #61457 - [
de345ea3a3
] - doc: correct description oferror.stack
accessor behavior (René) #61090 - [
d8418d9de7
] - doc: fix link in--env-file=file
section (N. Bighetti) #60563 - [
1107bda21e
] - doc: fix v22 changelog after security release (Marco Ippolito) #61371 - [
42aab9469a
] - doc: add missing history entry forsqlite.md
(Antoine du Hamel) #60607 - [
deb6d5deff
] - doc, module: change async customization hooks to experimental (Gerhard Stöbich) #60302 - [
c659add7d1
] - doc,src,lib: clarify experimental status of Web Storage support (Antoine du Hamel) #60708 - [
dda95e91b9
] - esm: avoid throw when module specifier is not url (Craig Macomber (Microsoft)) #61000 - [
912945be89
] - events: remove redundant todo (Gürgün Dayıoğlu) #60595 - [
22e156eb10
] - events: remove eventtarget custom inspect branding (Efe) #61128 - [
df6fd9b03f
] - fs: remove duplicate getValidatedPath calls (Mert Can Altin) #61359 - [
6ea3e4d850
] - fs: fix errorOnExist behavior for directory copy in fs.cp (Nicholas Paun) #60946 - [
dd918b9980
] - fs: fix ENOTDIR in globSync when file is treated as dir (sangwook) #61259 - [
4908e67ba0
] - fs: remove duplicate fd validation in sync functions (Mert Can Altin) #61361 - [
4a27bce3d9
] - fs: detect dot files when using globstar (Robin van Wijngaarden) #61012 - [
b0186ff65c
] - fs: validate statfs path (Efe) #61230 - [
6689775023
] - gyp: aix: change gcc version detection so CXX="ccache g++" works (Stewart X Addison) #61464 - [
5c4f4db663
] - http: fix rawHeaders exceeding maxHeadersCount limit (Max Harari) #61285 - [
7599e2eccd
] - http: replace startsWith with strict equality (btea) #59394 - [
99a85213bf
] - http: lazy allocate cookies array (Robert Nagy) #59734 - [
7669e6a5ad
] - http: fix http client leaky with double response (theanarkh) #60062 - [
f074c126a8
] - http,https: fix double ERR_PROXY_TUNNEL emission (Shima Ryuhei) #60699 - [
d8ac368363
] - http2: add diagnostics channels for client stream request body (Darshan Sen) #60480 - [
e26a7e464d
] - http2: rename variable to additionalPseudoHeaders (Tobias Nießen) #60208 - [
5df634f46e
] - http2: validate initialWindowSize per HTTP/2 spec (Matteo Collina) #61402 - [
2ccc9a6205
] - http2: do not crash on mismatched ping buffer length (René) #60135 - [
3e68a5f78a
] - inspector: inspect HTTP response body (Chengzhong Wu) #60572 - [
a86ffa9a5d
] - inspector: add network payload buffer size limits (Chengzhong Wu) #60236 - [
ea60ef5d74
] - lib: fix typo inutil.js
comment (Taejin Kim) #61365 - [
9d8d9322a4
] - lib: fix TypeScript support check in jitless mode (sangwook) #61382 - [
fc26f5c78f
] - lib: gbk decoder is gb18030 decoder per spec (Сковорода Никита Андреевич) #61099 - [
3b87030012
] - lib: enforce use ofURLParse
(Antoine du Hamel) #61016 - [
2a7479d4fc
] - lib: useFastBuffer
for empty buffer allocation (Gürgün Dayıoğlu) #60558 - [
7cf4c43582
] - lib: fix constructor in _errnoException stack tree (SeokHun) #60156 - [
f9d87fbfaa
] - lib: fix typo in QuicSessionStats (SeokHun) #60155 - [
8d26ccc652
] - lib: remove redundant destroyHook checks (Gürgün Dayıoğlu) #60120 - [
705832a1be
] - lib,src: isInsideNodeModules should test on the first non-internal frame (Chengzhong Wu) #60991 - [
6f39ad190b
] - meta: do not fast-track npm updates (Antoine du Hamel) #61475 - [
a6a0ff9486
] - meta: fix typos in issue template config (Daijiro Wachi) #61399 - [
ec88c9b378
] - meta: label v8 module PRs (René) #61325 - [
83143835de
] - meta: bump step-security/harden-runner from 2.13.2 to 2.14.0 (dependabot[bot]) #61245 - [
0802dc663a
] - meta: bump actions/setup-node from 6.0.0 to 6.1.0 (dependabot[bot]) #61244 - [
587db55796
] - meta: bump actions/cache from 4.3.0 to 5.0.1 (dependabot[bot]) #61243 - [
262c9d37a6
] - meta: bump github/codeql-action from 4.31.6 to 4.31.9 (dependabot[bot]) #61241 - [
d9763b5afd
] - meta: bump codecov/codecov-action from 5.5.1 to 5.5.2 (dependabot[bot]) #61240 - [
0af73d1811
] - meta: bump peter-evans/create-pull-request from 7.0.9 to 8.0.0 (dependabot[bot]) #61237 - [
8be6afd239
] - meta: move lukekarrys to emeritus (Node.js GitHub Bot) #60985 - [
c497de5c74
] - meta: bump actions/setup-python from 6.0.0 to 6.1.0 (dependabot[bot]) #60927 - [
774920f169
] - meta: bump github/codeql-action from 4.31.3 to 4.31.6 (dependabot[bot]) #60926 - [
ef3b1e5991
] - meta: bump peter-evans/create-pull-request from 7.0.8 to 7.0.9 (dependabot[bot]) #60924 - [
3ed667379f
] - meta: bump github/codeql-action from 4.31.2 to 4.31.3 (dependabot[bot]) #60770 - [
7c0cefb126
] - meta: bump step-security/harden-runner from 2.13.1 to 2.13.2 (dependabot[bot]) #60769 - [
5c6a076e5d
] - meta: add Renegade334 to collaborators (Renegade334) #60714 - [
4f4dda2a18
] - meta: bump actions/download-artifact from 5.0.0 to 6.0.0 (dependabot[bot]) #60532 - [
c436f8d57c
] - meta: bump actions/upload-artifact from 4.6.2 to 5.0.0 (dependabot[bot]) #60531 - [
402d9f87a6
] - meta: bump github/codeql-action from 3.30.5 to 4.31.2 (dependabot[bot]) #60533 - [
61be78e326
] - meta: bump actions/setup-node from 5.0.0 to 6.0.0 (dependabot[bot]) #60529 - [
7e4164a623
] - meta: bump actions/stale from 10.0.0 to 10.1.0 (dependabot[bot]) #60528 - [
1bf6e1d010
] - meta: move one or more collaborators to emeritus (Node.js GitHub Bot) #60325 - [
c66fc0e9cf
] - meta: loop userland-migrations in deprecations (Chengzhong Wu) #60299 - [
e4be0791e7
] - meta: callcreate-release-post.yml
post release (Aviv Keller) #60366 - [
8674f6527f
] - module: preserve URL in the parent created by createRequire() (Joyee Cheung) #60974 - [
41db87a975
] - msi: fix WiX warnings (Stefan Stojanovic) #60251 - [
884f313f40
] - node-api: use Node-API in comments (Vladimir Morozov) #61320 - [
375164190b
] - node-api: use local files for instanceof test (Vladimir Morozov) #60190 - [
972a1107c0
] - os: freeze signals constant (Xavier Stouder) #61038 - [
e992057ab7
] - perf_hooks: fix stack overflow error (Antoine du Hamel) #60084 - [
0bb1814fdf
] - repl: fix pasting after moving the cursor to the left (Ruben Bridgewater) #60470 - [
35a12fb996
] - src: replaceranges::sort
for libc++13 compatibility on armhf (Rebroad) #61789 - [
dbf00d4664
] - src: add missing override specifier to Clean() (Tobias Nießen) #61429 - [
140eba35d3
] - src: cache context lookup in vectored io loops (Mert Can Altin) #61387 - [
93e7e1708b
] - src: use C++ nullptr in webstorage (Tobias Nießen) #61407 - [
ef868447bc
] - src: fix pointer alignment (jhofstee) #61336 - [
a96256524c
] - src: dump snapshot source with node:generate_default_snapshot_source (Joyee Cheung) #61101 - [
ec051b9efd
] - src: add HandleScope to edge loop in heap_utils (Mert Can Altin) #60885 - [
41749eb5d6
] - src: remove redundant CHECK (Tobias Nießen) #61130 - [
57c81e5af3
] - src: fix off-thread cert loading in bundled cert mode (Joyee Cheung) #60764 - [
4b0616e024
] - src: handle DER decoding errors from system certificates (Joyee Cheung) #60787 - [
93393371f9
] - src: use static_cast instead of C-style cast (Michaël Zasso) #60868 - [
900445b655
] - src: move Node-API version detection to where it is used (Anna Henningsen) #60512 - [
8353a6da2a
] - src: avoid C strings in more C++ exception throws (Anna Henningsen) #60592 - [
27c860c51f
] - src: movenapi_addon_register_func
tonode_api_types.h
(Anna Henningsen) #60512 - [
e0517752e7
] - src: remove unconditional NAPI_EXPERIMENTAL in node.h (Chengzhong Wu) #60345 - [
21e2a52f8e
] - src: clean up generic counter implementation (Anna Henningsen) #60447 - [
aed23cb8ca
] - src: add enum handle for ToStringHelper + formatting (Burkov Egor) #56829 - [
2e93650ebc
] - src: fix timing of snapshot serialize callback (Joyee Cheung) #60434 - [
ece4acc18f
] - src: add COUNT_GENERIC_USAGE utility for tests (Joyee Cheung) #60434 - [
31c8e9d9ff
] - src: use cached primordials_string (Sohyeon Kim) #60255 - [
7f0ffddc14
] - src: implement Windows-1252 encoding support and update related tests (Mert Can Altin) #60893 - [
c2ba56d6b2
] - src,permission: fix permission.has on empty param (Rafael Gonzaga) #60674 - [
e55a2b895a
] - src,permission: add debug log on is_tree_granted (Rafael Gonzaga) #60668 - [
902a78b43c
] - stream: fix isErrored/isWritable for WritableStreams (René) #60905 - [
221b77cf41
] - stream: don't try to read more if reading (Robert Nagy) #60454 - [
46d12d826f
] - test: skip strace test with shared openssl (Richard Lau) #61987 - [
52e6b01a44
] - test: marktest-strace-openat-openssl
as flaky (Antoine du Hamel) #61921 - [
4d7468d0e0
] - test: skip --build-sea tests on platforms where SEA is flaky (Joyee Cheung) #61504 - [
f604b7ae67
] - test: fix flaky debugger test (Ryuhei Shima) #58324 - [
fc2dc4024b
] - test: ensure removeListener event fires for once() listeners (sangwook) #60137 - [
5fba382816
] - test: delay writing the files only on macOS (Luigi Pinca) #61532 - [
85cc9e20e4
] - test: asserts that import.meta.resolve invokes sync loader hooks (Chengzhong Wu) #61158 - [
13831685ca
] - test: check util.parseArgs argv parsing with actual process execution (René) #61089 - [
ec4b722cb8
] - test: remove unneccessary repl magic_mode tests (Dario Piotrowicz) #61053 - [
5c811106bc
] - test: skip sea tests on riscv64 (Stewart X Addison) #61111 - [
4e4a631c07
] - test: mark stringbytes-external-max flaky on AIX (Stewart X Addison) #60995 - [
9af0787043
] - test: update test426 fixtures (Rich Trott) #60982 - [
277f16d247
] - test: skip SEA inspect test if inspector is not available (Livia Medeiros) #60872 - [
7dfa8c96bf
] - test: useassert.match
for non-literal regexp tests (René) #60879 - [
41e6cd8ce5
] - test: fix embedtest in debug windows (Vladimir Morozov) #60806 - [
f65147b226
] - test: fix debug test crashes caused by sea tests (Vladimir Morozov) #60807 - [
a93dff9e92
] - test: replace deprecated regex test assertions in http trailers test (Aditya Chopra) #60831 - [
f90d5b954f
] - test: prefer major GC in cppgc-object teardown (sangwook) #60672 - [
e1645cc78d
] - test: skip test that cause timeout on IBM i (SRAVANI GUNDEPALLI) #60700 - [
4f23eba22f
] - test: limit the concurrency of WPTRunner for RISC-V (Levi Zim) #60591 - [
c2bef6522b
] - test: fix test-strace-openat-openssl for RISC-V (Levi Zim) #60588 - [
4c03a7f864
] - test: fix status when compiled without inspector (Antoine du Hamel) #60289 - [
2ef146a074
] - test: apply a delay towatch-mode-kill-signal
tests (Joyee Cheung) #60610 - [
dc3000c504
] - test: async iife in repl (Tony Gorez) #44878 - [
5e06e84db1
] - test: parallelize sea tests when there's enough disk space (Joyee Cheung) #60604 - [
940d2752bc
] - test: only show overridden env in child process failures (Joyee Cheung) #60556 - [
558a5743c6
] - test: add more logs to test-esm-loader-hooks-inspect-wait (Joyee Cheung) #60466 - [
10fac8de45
] - test: mark stringbytes-external-exceed-max tests as flaky on AIX (Joyee Cheung) #60565 - [
8bc84046be
] - test: correct conditional secure heap flags test (Shelley Vohr) #60385 - [
ccc805f184
] - test: fix flaky test-watch-mode-kill-signal-* (Joyee Cheung) #60443 - [
1b8274453d
] - test: capture stack trace in debugger timeout errors (Joyee Cheung) #60457 - [
9fcf889279
] - test: ensure assertions are reachable intest/async-hooks
(Antoine du Hamel) #60150 - [
7f5230333e
] - test: increase debugger waitFor timeout on macOS (Chengzhong Wu) #60367 - [
0e5ea3b795
] - test: fix small compile warning in test_network_requests_buffer.cc (xiaocainiao633) #60281 - [
012780c7e8
] - test: split test-runner-watch-mode-kill-signal (Joyee Cheung) #60298 - [
b53d35a8f8
] - test: fix incorrect calculation in test-perf-hooks.js (Joyee Cheung) #60271 - [
b8ef464c08
] - test: skip sea tests on x64 macOS (Joyee Cheung) #60250 - [
a3c4d905da
] - test: move sea tests into test/sea (Joyee Cheung) #60250 - [
80bec9fd07
] - test: skip tests that cause timeouts on IBM i (SRAVANI GUNDEPALLI) #60148 - [
1d05b44c7c
] - test: deflake test-fs-promises-watch-iterator (Luigi Pinca) #60060 - [
8958096840
] - test: deflaketest-repl-paste-big-data
(Livia Medeiros) #60975 - [
e261a59ca4
] - test: add newstartNewREPLSever
testing utility (Dario Piotrowicz) #59964 - [
d4a2d8aa8a
] - test: skip failing tests when compiled without amaro (Yuki Okita) #60815 - [
0e407a88bb
] - test: skip failing test on macOS 15.7+ (Antoine du Hamel) #60419 - [
a253b7b6dc
] - tools: switch to ARM runners on GHA jobs (Antoine du Hamel) #61903 - [
8862c41494
] - tools: avoid building twice in coverage jobs (Antoine du Hamel) #61899 - [
7d11a22802
] - tools: use ubuntu-slim runner in GHA (Antoine du Hamel) #61759 - [
d0e7d6cb89
] - tools: use ubuntu-slim runner in GHA (Antoine du Hamel) #61734 - [
cf5ddd1811
] - tools: use ubuntu-latest runner innotify-on-push
workflow (Antoine du Hamel) #61742 - [
18bcf8e260
] - tools: use ubuntu-slim runner in meta GitHub Actions (Tierney Cyren) #61663 - [
db76733b55
] - tools: update gyp-next to 0.21.1 (Node.js GitHub Bot) #61528 - [
1dd9d8a3b2
] - tools: fix vcbuild lint-js-build (Vladimir Morozov) #61318 - [
ec67f8f9b5
] - tools: only report commit validation failure on Slack (Antoine du Hamel) #61124 - [
8e385c8c66
] - tools: use sparse-checkout in linter jobs (Antoine du Hamel) #61123 - [
aed2e9c8eb
] - tools: simplifynotify-on-push
(Antoine du Hamel) #61050 - [
32680feefb
] - tools: fix update-nghttp2 signature verification (Richard Lau) #61035 - [
c5f68f41e6
] - tools: improve log output ofcreate-release-proposal
(Antoine du Hamel) #61028 - [
32e0ae0ec7
] - tools: fixvcbuild test
when path contain spaces (stduhpf) #56481 - [
9e0858e4a2
] - tools: do not runtest-linux
workflow for changes onvcbuild.bat
(Antoine du Hamel) #60979 - [
fd656a79fc
] - tools: disable some new cpplint rules before update (Michaël Zasso) #60901 - [
df4df52e67
] - tools: don't fetch V8 deps in the source tree (Richard Lau) #60883 - [
e5c2fe8d6d
] - tools: add temporal updater (Chengzhong Wu) #60828 - [
7f031e097e
] - tools: dump config.gypi as json (Chengzhong Wu) #60794 - [
5e69488a5a
] - tools: bump js-yaml from 4.1.0 to 4.1.1 in /tools/lint-md (dependabot[bot]) #60781 - [
5119c50931
] - tools: bump js-yaml from 4.1.0 to 4.1.1 in /tools/doc in the doc group (dependabot[bot]) #60766 - [
a4b073123d
] - tools: remove unsupportedcooldown
from Dependabot config (Antoine du Hamel) #60747 - [
a3df6b87bb
] - tools: update sccache to v0.12.0 (Michaël Zasso) #60723 - [
2efbd54a4a
] - tools: update gyp-next to 0.21.0 (Node.js GitHub Bot) #60645 - [
bb7876e4f9
] - tools: replace invalid expression in dependabot config (Riddhi) #60649 - [
e444e44d6a
] - tools: skip unaffected GHA jobs for changes intest/internet
(Antoine du Hamel) #60517 - [
a6a0ec107c
] - tools: do not use short hashes for deps versioning to avoid collision (Antoine du Hamel) #60407 - [
c6e2eed65f
] - tools: fix update-icu script (Michaël Zasso) #60521 - [
76fb3d123b
] - tools: fix linter for semver-major release proposals (Antoine du Hamel) #60481 - [
f02889e24e
] - tools: fix failing release-proposal linter for LTS transitions (Antoine du Hamel) #60465 - [
8203df4432
] - tools: remove undici from daily wpt.fyi job (Filip Skokan) #60444 - [
a58242b666
] - tools: add lint rule to ensure assertions are reached (Antoine du Hamel) #60125 - [
58e3ef398f
] - tools: update gyp-next to 0.20.5 (Node.js GitHub Bot) #60313 - [
996494482a
] - tools: optimize wildcard execution in tools/test.py (Joyee Cheung) #60266 - [
cf84756d0d
] - tools: use cooldown property correctly (Rafael Gonzaga) #60134 - [
5469cb2651
] - tools: validate release commit diff as part oflint-release-proposal
(Antoine du Hamel) #61440 - [
1b9eab4a1c
] - tools,doc: fix format-md files list (Stefan Stojanovic) #61147 - [
b20d9c2ce7
] - tools,doc: update JavaScript primitive types to match MDN Web Docs (JustApple) #60581 - [
31760b1beb
] - typings: add typing for string_decoder (Taejin Kim) #61368 - [
d6b908917c
] - typings: add missing properties and method in Worker (Woohyun Sung) #60257 - [
1e8b6d5686
] - typings: add missing properties in HTTPParser (Woohyun Sung) #60257 - [
27ae9b4a26
] - typings: delete undefined property in ConfigBinding (Woohyun Sung) #60257 - [
f43c6434e2
] - typings: add buffer internalBinding typing (방진혁) #60163 - [
e7f954f63a
] - url: add fast path to getPathFromURL decoder (Gürgün Dayıoğlu) #60749 - [
c149b64473
] - url: remove array.reduce usage (Gürgün Dayıoğlu) #60748 - [
0bd291bff1
] - util: optimize toASCIILower function using V8s native toLowerCase (Mert Can Altin) #61107 - [
bbc54b3c96
] - util: limitinspect
to only show own properties (Ruben Bridgewater) #61032 - [
78e5fa23c4
] - util: fix parseArgs skipping positional arg with --eval and --print (azadgupta1) #60814 - [
f75ec19105
] - util: assert getCallSites does not invoke Error.prepareStackTrace (Chengzhong Wu) #60922 - [
d77da9306c
] - util: fix stylize of special properties in inspect (Ge Gao) #60479 - [
3a4edc8f6d
] - util: use more defensive code when inspecting error objects (Antoine du Hamel) #60139 - [
25c33af752
] - util: mark special properties when inspecting them (Ruben Bridgewater) #60131 - [
3f98b46716
] - vm: make vm.Module.evaluate() conditionally synchronous (Joyee Cheung) #60205 - [
f64a691493
] - win: upgrade Visual Studio workload from 2019 to 2022 (Jiawen Geng) #60318 - [
8e04327954
] - worker: update code examples fornode:worker_threads
module (fisker Cheung) #58264 - [
c4440dcc60
] - worker: remove not implemented declarations (Artur Gawlik) #60655 - [
df4cc62954
] - zlib: validate write_result array length (Ryuhei Shima) #61342
Windows 32-bit Installer: https://nodejs.org/dist/v22.22.1/node-v22.22.1-x86.msi
Windows 64-bit Installer: https://nodejs.org/dist/v22.22.1/node-v22.22.1-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v22.22.1/node-v22.22.1-arm64.msi
Windows 32-bit Binary: https://nodejs.org/dist/v22.22.1/win-x86/node.exe
Windows 64-bit Binary: https://nodejs.org/dist/v22.22.1/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v22.22.1/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v22.22.1/node-v22.22.1.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v22.22.1/node-v22.22.1-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v22.22.1/node-v22.22.1-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v22.22.1/node-v22.22.1-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v22.22.1/node-v22.22.1-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v22.22.1/node-v22.22.1-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v22.22.1/node-v22.22.1-aix-ppc64.tar.gz
ARMv7 32-bit Binary: https://nodejs.org/dist/v22.22.1/node-v22.22.1-linux-armv7l.tar.xz
ARMv8 64-bit Binary: https://nodejs.org/dist/v22.22.1/node-v22.22.1-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v22.22.1/node-v22.22.1.tar.gz
Other release files: https://nodejs.org/dist/v22.22.1/
Documentation: https://nodejs.org/docs/v22.22.1/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
dd75425fe7875b04fbdbbeeead9bb271daacff84b75d0ba1d4f6ccbee515eae1 node-v22.22.1-aix-ppc64.tar.gz
ede430968a987a1e5a8c59291ced0768dd8f38e140af50e50312c0fbc008043a node-v22.22.1-arm64.msi
679ad4966339e4ef4900f57996714864e4211b898825bb840c3086c419fbcef2 node-v22.22.1-darwin-arm64.tar.gz
261da057fb25ff2912dd6abb7842fc915ddf7947a2cb3c8cce90875d2b9bb667 node-v22.22.1-darwin-arm64.tar.xz
07b13722d558790fca20bb1ecf61bde24b7a4863111f7be77fc57251a407359a node-v22.22.1-darwin-x64.tar.gz
91227fa5a3bfd988be1953c0384ceb98bd69a6a377a7416c40eb39779d6ab17f node-v22.22.1-darwin-x64.tar.xz
0f76c31ce76a623a6a3a4038cb62eae281b2e33ad189dcf2d514ec32ae74d9b2 node-v22.22.1-headers.tar.gz
3f435f2ac1ab363f8220f4beb60c7493a3f680918a7426ff83b7d4c6e1d314fa node-v22.22.1-headers.tar.xz
1d1690e9aba47e887a275abc6d8f7317e571a0700deaef493f768377e99155f5 node-v22.22.1-linux-arm64.tar.gz
0f3550d58d45e5d3cf7103d9e3f69937f09fe82fb5dd474c66a5d816fa58c9ee node-v22.22.1-linux-arm64.tar.xz
2b592d21609ef299d1e3918bb806ed62ba715d4109b0f8ec11b132af9fa42d70 node-v22.22.1-linux-armv7l.tar.gz
c3906440501e5e5f6be79c8f9ea9467451c2adeec8ebdb734cd388214b5036a3 node-v22.22.1-linux-armv7l.tar.xz
18f9ab7da4f3a04ec213590b14e5d78b60bfb5c6b8bf53541e7eaf1adf9d270a node-v22.22.1-linux-ppc64le.tar.gz
a65a44cf0224505f052b90357b763dbc1ea9148f4f5f2284f0596cf2000f819b node-v22.22.1-linux-ppc64le.tar.xz
6128f9d54a1b43258144d7ac074a82d3b6c96d8e9cb3a8e14e4722a66990adbe node-v22.22.1-linux-s390x.tar.gz
e08b3a73d0bd840e008f589e4be4a2ef3d4a0c59015f4f20a04ed7fc968042a2 node-v22.22.1-linux-s390x.tar.xz
07c8aafa60644fb81adefa1ee7da860eb1920851ffdc9a37020ab0be47fbc10e node-v22.22.1-linux-x64.tar.gz
9a6bc82f9b491279147219f6a18add1e18424dce90d41d2a5fcd69d4924ba3aa node-v22.22.1-linux-x64.tar.xz
ac8cb570db59cb399be96978c194f6c4fc91ffcf11a197ebd5461083c0cf1dfd node-v22.22.1.pkg
20da57e24be78d0bd54175de1a23ab897bf7340c4ad9f32ff257b98ea9a825c5 node-v22.22.1.tar.gz
87104b07e7acee748bcc5391e1bc69cf3571caa0fdfb8b1d6b5fd3f9599b7849 node-v22.22.1.tar.xz
c772ad9da497e34e0e6a4abccbd71f21ef5f54059790da1f8f8e7b64ccc63e2d node-v22.22.1-win-arm64.7z
d0722fcdefa1c08e4af31809e91ad4f23282f6c535c261607e8aa372d0ce61dd node-v22.22.1-win-arm64.zip
07d6fdf3677e077a6f6b7906b9a770a78d852ae455ec37d7aa4df180e16728cd node-v22.22.1-win-x64.7z
877cb93829e14fffbbc7903e7d8037336c9a79f3ea43c5d0b8c2379b79da56de node-v22.22.1-win-x64.zip
a70d42ec48ae3dd58f89d705c4fd2026b03e47baa2eb5f7660ad3688d38e5040 node-v22.22.1-win-x86.7z
afe3d23563a8cc36759b4c60645d12f3cf2807d0100564dcdc6f381fa0715217 node-v22.22.1-win-x86.zip
444c1c325dc26b7237ffc521b092aa778400665e9757e97405ab95a7584053c8 node-v22.22.1-x64.msi
0079710a64714bbb55e8e18f3292345cc146777d04d87c33af272c1e6a64e78b node-v22.22.1-x86.msi
993b56091266aec4a41653ea3e70b5b18fadc78952030ca0329309240030859c win-arm64/node.exe
9b75bbc3be72c84f1d41cd6abb6e5ecc333836015e40a6267ce755554874a13a win-arm64/node.lib
37e2b27fce010bf6be2b8cd23ebd406644ad222d1edf2513576c477a4cac3396 win-arm64/node_pdb.7z
cf321e6de92f0ae7120927e729888612545633d0d0bdae9459947085a8aa67d2 win-arm64/node_pdb.zip
923a41f268ab49ede2e3363fbdd9e790609e385c6f3ca880b4ee9a56a8133e5a win-x64/node.exe
0d8d8bcc11daea60f5dd4da414e72ccb785718345ec8fbec52cfc7d1a2326293 win-x64/node.lib
3f77017f7a77d9effbf8932be543cc464503b1de156b7836d3de1468dee5bdd1 win-x64/node_pdb.7z
c9fad5ad8d08f517a8e1546704855a2cf7ec1d46b821d8e298717b559e0befd3 win-x64/node_pdb.zip
5c16964f34454ca58f45497c2ebab0d977288759cb932d00d070eca895300542 win-x86/node.exe
a07e94777fb491c1a59103b6987417df35a1dd0a9682220bba43d3c602b8b414 win-x86/node.lib
ae1859b221f541f3cc0e348b11df4cdd172cd178b0199726772432bcd525f4c0 win-x86/node_pdb.7z
ba2fb73584cf395cdf910d335140ac3b6ad0c1e1ac84a83ecb8a86ac699c1000 win-x86/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQIzBAEBCAAdFiEEzGj1oxBv9EgyLkjtJ/XjjVsKIV8FAmmpk9EACgkQJ/XjjVsK
IV+27g/7B7m3xJMBa+xixzMlBXRFsGyfXFqRiHvi0xrqi3DJPkfaU7eab5iL4yxx
h8yMbXZO6xB2xC+yLCkdJc5ueqOs2VDTH3Kbf56IMUvuTbYXxZ/sPUHxLGC3kqwG
q8CjmXnuDTKqS4n3m00YRGDoGEVwJqMoMsn+NU2zheFvponGeVg0irI8Low+qjPd
4wQ1KtMSNsKlRrCqqM1KYDadvQWOv1KojGaZRbS3k9aMP4irEIvTqwTmqqSnl0Uk
81wR7Aq9gkWqwk4YdJHafKbO6nbtGUzlcQujB1fYg20XTyUxkexXPxkz1kGS/7NA
GLhlh3lvcAMBwG1kBIGSKnCIRnbm7xU1s5UkZd/PpBxDBxdaJvD91CzcoFcV6UaE
VWWCb+s/yUmv90fKsohILXACr43ZnXHSFheXTtlgVOkCDtWz6iPgMriGoQj6pUmN
gq4SGnzBfUiEFIiE5bUQb3EHlwjP4Edn683mVuDxxQnGoHgSzHFu4Y8K2l7quCjR
JI06fvTUn0KHSRJv2BXGMqQz/WGfk5v/6ZdUZV1dYROrSCwR0WZJwE40sGEpB/ik
s5iS0vAWtdLSJJgq/ZkMwHWsVZaar3BeKw8j5u6vxuRW0ejhUxdX7tXGjHxepLG1
gsCv5tZG4n8Ipix8XLV1p/SFCMxGONKqlyVG7H7ppV2mXqzL/kg=
=y2UM
-----END PGP SIGNATURE-----
```

---

## 16. Node.js 20.20.1 (LTS)

- 日期: 2026-03-05 14:22
- 链接: https://nodejs.org/en/blog/release/v20.20.1

```
Node.js 20.20.1 (LTS)
Marco Ippolito
2026-03-05, Version 20.20.1 'Iron' (LTS), @marco-ippolito
Notable Changes
- [
91a66e671c
] - build: test on Python 3.14 (Christian Clauss) #59983 - [
f66056054b
] - crypto: update root certificates to NSS 3.119 (Node.js GitHub Bot) #61419 - [
80feacaddb
] - crypto: update root certificates to NSS 3.117 (Node.js GitHub Bot) #60741
Commits
- [
6f580d5399
] - assert: fix deepEqual always return true on URL (Xuguang Mei) #50853 - [
91a66e671c
] - build: test on Python 3.14 (Christian Clauss) #59983 - [
cc4f7af6f3
] - build: skip sscache action on non-main branches (Joyee Cheung) #61790 - [
f66056054b
] - crypto: update root certificates to NSS 3.119 (Node.js GitHub Bot) #61419 - [
80feacaddb
] - crypto: update root certificates to NSS 3.117 (Node.js GitHub Bot) #60741 - [
fa88cc07e2
] - crypto: ensure documented RSA-PSS saltLength default is used (Filip Skokan) #60662 - [
88b2eec88a
] - deps: update minimatch to 10.2.2 (Node.js GitHub Bot) #61830 - [
5c053264f1
] - deps: V8: backport 6a0a25abaed3 (Vivian Wang) #61687 - [
4a398699d0
] - deps: update googletest to 5a9c3f9e8d9b90bbbe8feb32902146cb8f7c1757 (Node.js GitHub Bot) #61731 - [
4fa43adf15
] - deps: update googletest to 56efe3983185e3f37e43415d1afa97e3860f187f (Node.js GitHub Bot) #61605 - [
1a855d490c
] - deps: update googletest to 85087857ad10bd407cd6ed2f52f7ea9752db621f (Node.js GitHub Bot) #61417 - [
d8a9359826
] - deps: update icu to 78.2 (Node.js GitHub Bot) #60523 - [
e79cd3a0bb
] - deps: update acorn-walk to 8.3.5 (Node.js GitHub Bot) #61928 - [
0707ade464
] - deps: update acorn to 8.16.0 (Node.js GitHub Bot) #61925 - [
dc5a3cddef
] - deps: update llhttp to 9.3.1 (Node.js GitHub Bot) #61827 - [
46043b94c7
] - deps: update zlib to 1.3.1-e00f703 (Node.js GitHub Bot) #61135 - [
6be15a596e
] - deps: update cjs-module-lexer to 2.2.0 (Node.js GitHub Bot) #61271 - [
10881404cd
] - deps: update timezone to 2025c (Node.js GitHub Bot) #61138 - [
1594a78c85
] - deps: update googletest to 065127f1e4b46c5f14fc73cf8d323c221f9dc68e (Node.js GitHub Bot) #61055 - [
7fa2ee1933
] - deps: update zlib to 1.3.1-63d7e16 (Node.js GitHub Bot) #60898 - [
09259532ef
] - deps: update googletest to 1b96fa13f549387b7549cc89e1a785cf143a1a50 (Node.js GitHub Bot) #60739 - [
aa8bdb6886
] - deps: update cjs-module-lexer to 2.1.1 (Node.js GitHub Bot) #60646 - [
cc849fde27
] - deps: update googletest to 279f847 (Node.js GitHub Bot) #60219 - [
a99ba553a2
] - deps: update googletest to 50b8600 (Node.js GitHub Bot) #59955 - [
6349a79f5f
] - deps: update googletest to 7e17b15 (Node.js GitHub Bot) #59131 - [
8ba759f1a0
] - deps: update googletest to 35b75a2 (Node.js GitHub Bot) #58710 - [
927d906850
] - deps: update googletest to e9092b1 (Node.js GitHub Bot) #58565 - [
bf8919f5c2
] - deps: update googletest to 0bdccf4 (Node.js GitHub Bot) #57380 - [
ae6231dac0
] - deps: update googletest to e235eb3 (Node.js GitHub Bot) #56873 - [
0561c62e85
] - deps: update minimatch to 10.1.2 (Node.js GitHub Bot) #61732 - [
f0ef221b0d
] - deps: update minimatch to 10.1.1 (Node.js GitHub Bot) #60543 - [
15bd0da404
] - deps: update archs files for openssl (Antoine du Hamel) #61912 - [
04d439323f
] - deps: upgrade openssl sources to openssl-3.0.19 (Antoine du Hamel) #61912 - [
2ea16d3bd6
] - deps: update corepack to 0.34.6 (Node.js GitHub Bot) #61510 - [
622f973d1c
] - deps: update corepack to 0.34.5 (Node.js GitHub Bot) #60842 - [
2cd265d8b9
] - deps: update corepack to 0.34.4 (Node.js GitHub Bot) #60643 - [
65e839687b
] - deps: update corepack to 0.34.2 (Node.js GitHub Bot) #60550 - [
2dc99d2771
] - dns: fix Windows SRV ECONNREFUSED by adjusting c-ares fallback detection (notvivek12) #61453 - [
2c7b84b1d8
] - doc: fix typo in http.md (Michael Solomon) #59354 - [
a84b42667c
] - doc: fix grammar in global dispatcher usage (Eng Zer Jun) #59344 - [
ffd0ada45f
] - doc: fix typo intest/common/README.md
(Yoo) #59180 - [
b4d9d006e7
] - doc: fix broken sentence inURL.parse
(Superchupu) #59164 - [
45e9971d9c
] - doc: fix typo in writing-test.md (SeokHun) #59123 - [
e9fd10b5d6
] - doc: fixfetch
subsections inglobals.md
(Antoine du Hamel) #58933 - [
3715dd1c2b
] - doc: fix wrong RFC number in http2 (Deokjin Kim) #58753 - [
098c017eac
] - doc: punctuation fix for Node-API versioning clarification (Jiacai Liu) #58599 - [
545bf434e1
] - doc: fix typo of filehttp.md
,outgoingMessage.setTimeout
section (yusheng chen) #58188 - [
b3d6683e7b
] - doc: support toolchain with Visual Studio 2019 & 2022 only (Mike McCready) #61450 - [
8fdde5d110
] - doc: fix v20 changelog after security release (Marco Ippolito) #61371 - [
31d04599be
] - http: fix keep-alive not timing out after post-request empty line (Shima Ryuhei) #58178 - [
5ec7d1eba0
] - http2: validate initialWindowSize per HTTP/2 spec (Matteo Collina) #61402 - [
5c091d5a96
] - meta: persist sccache daemon until end of build workflows (René) #61639 - [
183353aba0
] - path,win: fix bug in resolve and normalize (Hüseyin Açacak) #55623 - [
dbe9e5091b
] - src: fix flags argument offset in JSUdpWrap (Weixie Cui) #61948 - [
4106bfc775
] - test: mark stringbytes-external-max flaky on AIX (Stewart X Addison) #60995 - [
de51937306
] - test: mark stringbytes-external-exceed-max tests as flaky on AIX (Joyee Cheung) #60565 - [
368b221be3
] - test: fix flaky test-performance-eventloopdelay (Matteo Collina) #61629 - [
e134912a33
] - test: fix flaky test-worker-message-port-transfer-filehandle test (Alex Yang) #59158 - [
5630170d3e
] - test: account for truthy signal in flaky async_hooks tests (Darshan Sen) #58478 - [
1e5363bb63
] - test: marktest-http2-debug
as flaky on LinuxONE (Richard Lau) #58494 - [
662998787a
] - test: settest-fs-cp
as flaky (Stefan Stojanovic) #56799 - [
0807127339
] - test: marktest-esm-loader-hooks-inspect-wait
flaky (Richard Lau) #56803 - [
6320cd0721
] - test: skip strace test with shared openssl (Richard Lau) #61987 - [
83b9f8ee02
] - tools: make nodedownload module compatible with Python 3.14 (Lumír 'Frenzy' Balhar) #58752 - [
6cf9b5786e
] - tools: enforce removal oflts-watch-*
labels on release proposals (Antoine du Hamel) #61672 - [
cd4161499c
] - tools: use ubuntu-slim runner in meta GitHub Actions (Tierney Cyren) #61663 - [
6dc2a99a0d
] - tools: validate release commit diff as part oflint-release-proposal
(Antoine du Hamel) #61440 - [
5014f22332
] - tools: add read permission to workflows that read contents (Antoine du Hamel) #58255 - [
6c3ad2a5a3
] - tools: switch to ARM runners on GHA jobs (Antoine du Hamel) #61903 - [
1abada9c34
] - tools: avoid building twice in coverage jobs (Antoine du Hamel) #61899 - [
f260e40127
] - tools: use ubuntu-slim runner in GHA (Antoine du Hamel) #61759 - [
64beca5e01
] - tools: use ubuntu-slim runner in GHA (Antoine du Hamel) #61734
Windows 32-bit Installer: https://nodejs.org/dist/v20.20.1/node-v20.20.1-x86.msi
Windows 64-bit Installer: https://nodejs.org/dist/v20.20.1/node-v20.20.1-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v20.20.1/node-v20.20.1-arm64.msi
Windows 32-bit Binary: https://nodejs.org/dist/v20.20.1/win-x86/node.exe
Windows 64-bit Binary: https://nodejs.org/dist/v20.20.1/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v20.20.1/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v20.20.1/node-v20.20.1.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v20.20.1/node-v20.20.1-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v20.20.1/node-v20.20.1-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v20.20.1/node-v20.20.1-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v20.20.1/node-v20.20.1-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v20.20.1/node-v20.20.1-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v20.20.1/node-v20.20.1-aix-ppc64.tar.gz
ARMv7 32-bit Binary: https://nodejs.org/dist/v20.20.1/node-v20.20.1-linux-armv7l.tar.xz
ARMv8 64-bit Binary: https://nodejs.org/dist/v20.20.1/node-v20.20.1-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v20.20.1/node-v20.20.1.tar.gz
Other release files: https://nodejs.org/dist/v20.20.1/
Documentation: https://nodejs.org/docs/v20.20.1/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
6565a303b13143bf74d65a90eb32f67d97bccbfacbd7c13f9130212756b5966c node-v20.20.1-aix-ppc64.tar.gz
cc0004c14866004c7fb35a3cfabf66d6cfacc963121cb112b9bbe1a0962747c5 node-v20.20.1-arm64.msi
36c5ef36d955995ea2dea700b16b8e79bedeb1ecb4569e77ddc8fc739aa56bac node-v20.20.1-darwin-arm64.tar.gz
7ccad11f66d39bbf3a35b9b6f3b65bafde481cb76bbef902d0a153fdfa321360 node-v20.20.1-darwin-arm64.tar.xz
ea8d2cd7280d935232bae5456704843aa50cf452e10b95abd92a721db6496965 node-v20.20.1-darwin-x64.tar.gz
0d4130046901c9b249563d6053b1512217a14c1dde164b15713fb8a25b914650 node-v20.20.1-darwin-x64.tar.xz
18561cca368164e7d20e9967568a174ca8f01b91092b2ca46210ff443c3fedce node-v20.20.1-headers.tar.gz
33f134077a58e7285514456aa24f0d177ff6a13a7af420067f6070a8688804ad node-v20.20.1-headers.tar.xz
d6947e10ddc124284aee92981cc739cd4581a6b4bf89520792f2b582600195fa node-v20.20.1-linux-arm64.tar.gz
f9a7b07fafd1adaf2c375af2ede31f462395377a8a6c9427d32793a68135e774 node-v20.20.1-linux-arm64.tar.xz
6d7b0f1f3a88004b251fd4d2ee2f5c4faca15587a3cdaaefae11e655b9e01cde node-v20.20.1-linux-armv7l.tar.gz
483fb1370a2111be05294f38dc0255e6982ab69904380ff6f63f2a54ce136eb9 node-v20.20.1-linux-armv7l.tar.xz
d885a22c1a08bd2d2f91c290770f3a9762075c4ec222fcd9d9fc921b0c8294b9 node-v20.20.1-linux-ppc64le.tar.gz
214db347255f28ac8f6cc3c4bf5743f729e0b9e8cb9fb478258d981031fcce6f node-v20.20.1-linux-ppc64le.tar.xz
7f0688d98fce89a9d7c623a3b0d2eab8374333f31461c8cb8b9d34712c45a1ba node-v20.20.1-linux-s390x.tar.gz
daa1bd477346861291d1e0f92b99bd671323061f92577905647f7145348d1116 node-v20.20.1-linux-s390x.tar.xz
6362e50804cdcc110592201f67beda93bcd702fdcbe1c42840a50d590e3af0ce node-v20.20.1-linux-x64.tar.gz
1592ef30f7a63309581a130f7fd8b3311a3e08ee0c609a3d13234590fe35409f node-v20.20.1-linux-x64.tar.xz
7560c232ce06f2fff19f0b43e6b56cf7bb86e43c98005dd95487085dfd2c9378 node-v20.20.1.pkg
1b6eaf0fa2b99a19ec682149faa0aabbea5bb7f8af2f44ee6f6491d5ff6a9235 node-v20.20.1.tar.gz
e540efdd6750f838e867daf9ab9d90ea195423f915613d05d87105f4d2ecd186 node-v20.20.1.tar.xz
c0128606ebd275db161ccc90b103a01dba2698bc66bb17b87515cde8814b3a75 node-v20.20.1-win-arm64.7z
2de4684a20c98a50bbf0e5cc7cadd94abe6341c0fa3830a49f384deaf4457ff7 node-v20.20.1-win-arm64.zip
6c96f5deebd2efc622397758bbcdadb10a0d8db0cecbb12577a2c183751708b6 node-v20.20.1-win-x64.7z
499e886ed617abb37d5e3a2b87a3f737e3c673b146361fb5ee70d08d7fdf6d2b node-v20.20.1-win-x64.zip
1756fde9976a040c9187075c65d781380b1cd8b35caa56fa30e2ea12a6e88a1e node-v20.20.1-win-x86.7z
9d7b464e77a4aa28f425d94230b632ce65d0caed52cf4e2c50bc3217e862ab33 node-v20.20.1-win-x86.zip
ce635af568160648e67121b14620771f1e9199194fd0c7c4886ce676c938f0a9 node-v20.20.1-x64.msi
986a9ba871e30242f3e9588d38f9949f1cbc672b6348d43c14be8d9e29eddf44 node-v20.20.1-x86.msi
55548a2e02ce19b1b2a48da3c1f332d9174487a3396399ee3a270fcf442d1331 win-arm64/node.exe
deacf784c804e5ab9df886b2de4c7a04d77ee1c722e2e4f1567aac62391ec4c4 win-arm64/node.lib
12c490748993a1a39c58723354276809cc388cfa88d02760037747aba80104f3 win-arm64/node_pdb.7z
3644b1ddb8661c6c3191e4ec10b56047e7cb477adbc41fbe01e758277f8f2fc0 win-arm64/node_pdb.zip
c0e91d79c5541a733999101578f2febbc2c4ca48bb9727cad3c5ed874805d84a win-x64/node.exe
6b9b49107d47c9f94b8cb191be208a303560e8ebb88bccfbd8a43ca0dc33cf99 win-x64/node.lib
282e9f621b564b28c2ed922fc1d8e8b2c084f295e80461bca707bb034f4dbe49 win-x64/node_pdb.7z
342e06e0ba7e5d84688b7177978b8ab2788f4b13e0b872209a04305832c2269d win-x64/node_pdb.zip
08bcde38088527bf56fbee5978c02f71919e9c571ae5c4b2d6077969cf70331f win-x86/node.exe
eeb5cad8803c51da6031c3617b469d539511a7ef1d659a046a13f467af313562 win-x86/node.lib
64b6f00e31a687726b75613a815f2c71c2b586e7fd984188c981f6b5dbefa6fb win-x86/node_pdb.7z
a0f2e63f7a3d7e4801355ca71edc36c90f244aee0d9519297532d09702c748fe win-x86/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQIzBAEBCAAdFiEEzGj1oxBv9EgyLkjtJ/XjjVsKIV8FAmmpjYEACgkQJ/XjjVsK
IV+BLg//au5QL89m4AR95rosHUkCelwigFowaMzyPgg402M9ZQhDFesrb8pH5VaG
pAgWXxwHJxgLfnc1m4a3fzuioIlk+Nky6TBeyFblbzACHvvVo2tc/n+NMKQcFRzu
paE957VhAokaty/OjMVsEYWyVoS2vMaH53/ja97Ggj7GCU4MI9FfD+qn141PXYhQ
MN5e02qrU0r19q1eWjBnBz55VHE2fGzow7Q+aJZaqTrAzRszBPpvwY1cEMjMLsOD
dd+pP6kJZqcsdnuHVbdDdaZE/45rGvUxBqtIoe9JzSRHvERB6DeDxKD8itH/wXQK
jrP1rYMTt6GGiTQxt6ncZ4t4mTEQ2buRgHWL3D9bik8wxGnHZggT7QGNvO9Rs3R9
hKKA4nUfHKtZ2Z5TKOFMWOF6m0TMGcI1XZSzVpfWQt3xI+jdzTSLyKItCLg0hveK
A9ZQuz6ivUnm5fp2LqYD+QnqSyjfclqTx3R0WycBEn1j0MB9dQmMtHF1tYU/PMLd
2tZn6y61XCZruKITV9VnzL3vnBY4mbV1uHDAWoGJTr3+oL2QOpn61zPRBTkwIdqm
Nu96f8nIYLmYuqGTQqzgxVT59eQU9ev6tF5fyeIz6amc1BRasMHxdMWQqGRt88nk
AQYIYe3men0WDNwMKD/G95OI92gnH+4kFhJxxkvEMwaqNgSWoOU=
=nBV4
-----END PGP SIGNATURE-----
```

---

## 17. Node.js 25.8.0 (Current)

- 日期: 2026-03-03 17:07
- 链接: https://nodejs.org/en/blog/release/v25.8.0

```
Node.js 25.8.0 (Current)
Richard Lau
2026-03-03, Version 25.8.0 (Current), @richardlau
Notable Changes
- [
e55eddea2a
] - build, doc: use new api doc tooling (flakey5) #57343 - [
4c181e2277
] - (SEMVER-MINOR) sqlite: add limits property to DatabaseSync (Mert Can Altin) #61298 - [
46ee1eddd7
] - (SEMVER-MINOR) src: add C++ support for diagnostics channels (RafaelGSS) #61869 - [
9ddd1a9c27
] - (SEMVER-MINOR) src,permission: add --permission-audit (RafaelGSS) #61869 - [
0d97ec4044
] - (SEMVER-MINOR) test_runner: expose worker ID for concurrent test execution (Ali Hassan) #61394
Commits
- [
940b58c8c1
] - buffer: optimize buffer.concat performance (Mert Can Altin) #61721 - [
0589b0e5a1
] - build: fix GN for new merve dep (Shelley Vohr) #61984 - [
f3d3968dcd
] - Revert "build: add temporal test on GHA windows" (Antoine du Hamel) #61810 - [
e55eddea2a
] - build, doc: use new api doc tooling (flakey5) #57343 - [
b7715292f8
] - child_process: add tracing channel for spawn (Marco) #61836 - [
a32a598748
] - crypto: fix missing nullptr check on RSA_new() (ndossche) #61888 - [
dc384f95b3
] - crypto: fix handling of null BUF_MEM* in ToV8Value() (Nora Dossche) #61885 - [
3337b095db
] - crypto: fix potential null pointer dereference when BIO_meth_new() fails (Nora Dossche) #61788 - [
51ded81139
] - deps: update undici to 7.22.0 (Node.js GitHub Bot) #62035 - [
8aa2fde931
] - deps: update minimatch to 10.2.4 (Node.js GitHub Bot) #62016 - [
57dc092eaf
] - deps: upgrade npm to 11.11.0 (npm team) #61994 - [
705bbd60a9
] - deps: update simdjson to 4.3.1 (Node.js GitHub Bot) #61930 - [
4d411d72e5
] - deps: update acorn-walk to 8.3.5 (Node.js GitHub Bot) #61928 - [
f53a32ab84
] - deps: update acorn to 8.16.0 (Node.js GitHub Bot) #61925 - [
9b483fbb27
] - deps: update minimatch to 10.2.2 (Node.js GitHub Bot) #61830 - [
bdc18940ad
] - doc: expand SECURITY.md with non-vulnerability examples (Rafael Gonzaga) #61972 - [
4e54c103cb
] - doc: separate in-types and out-types in SQLite conversion docs (René) #62034 - [
ca78ebbeaa
] - doc: fix small logic error in DETECT_MODULE_SYNTAX (René) #62025 - [
e6b131f3fe
] - doc: fix module.stripTypeScriptTypes indentation (René) #61992 - [
7508540e19
] - doc: update DEP0040 (punycode) to application type deprecation (Mike McCready) #61916 - [
33a364cb62
] - doc: explicitly mention Slack handle (Rafael Gonzaga) #61986 - [
46a61922bd
] - doc: support toolchain Visual Studio 2022 & 2026 + Windows 11 SDK (Mike McCready) #61864 - [
dc12a257aa
] - doc: rename invalidfunction
parameter (René) #61942 - [
6259abcf55
] - http: validate ClientRequest path on set (Matteo Collina) #62030 - [
dafdc0a5b8
] - http: validate headers in writeEarlyHints (Richard Clarke) #61897 - [
3c94b56fa6
] - inspector: unwrap internal/debugger/inspect imports (René) #61974 - [
8a24c17648
] - lib: improve argument handling in Blob constructor (Ms2ger) #61980 - [
21d4baf256
] - meta: bump github/codeql-action from 4.32.0 to 4.32.4 (dependabot[bot]) #61911 - [
59a726a8e3
] - meta: bump step-security/harden-runner from 2.14.1 to 2.14.2 (dependabot[bot]) #61909 - [
0072b7f991
] - meta: bump actions/stale from 10.1.1 to 10.2.0 (dependabot[bot]) #61908 - [
3d160cd049
] - module: run require.resolve through module.registerHooks() (Joyee Cheung) #62028 - [
999bf22f47
] - repl: keep reference count forprocess.on('newListener')
(Anna Henningsen) #61895 - [
4c181e2277
] - (SEMVER-MINOR) sqlite: add limits property to DatabaseSync (Mert Can Altin) #61298 - [
aee2a18257
] - src: fix flags argument offset in JSUdpWrap (Weixie Cui) #61948 - [
46ee1eddd7
] - (SEMVER-MINOR) src: add C++ support for diagnostics channels (RafaelGSS) #61869 - [
9ddd1a9c27
] - (SEMVER-MINOR) src,permission: add --permission-audit (RafaelGSS) #61869 - [
ea2df2a16f
] - stream: fix pipeTo to defer writes per WHATWG spec (Matteo Collina) #61800 - [
aa0c7b09e0
] - test: remove unnecessaryprocess.exit
calls from test files (Antoine du Hamel) #62020 - [
ad96a6578f
] - test: skiptest-url
on--shared-ada
builds (Antoine du Hamel) #62019 - [
7c72a31e4b
] - test: skip strace test with shared openssl (Richard Lau) #61987 - [
604456c163
] - test: avoid flaky debugger restart waits (Yuya Inoue) #61773 - [
4890d6bd43
] - test_runner: run afterEach on runtime skip (Igor Shevelenkov) #61525 - [
fce2930110
] - test_runner: expose expectFailure message (sangwook) #61563 - [
0d97ec4044
] - (SEMVER-MINOR) test_runner: expose worker ID for concurrent test execution (Ali Hassan) #61394 - [
243e6b2009
] - test_runner: replace native methods with primordials (Ayoub Mabrouk) #61219 - [
bf1ed7e647
] - tls: forward keepAlive, keepAliveInitialDelay, noDelay to socket (Sergey Zelenov) #62004 - [
746d0cebbf
] - tools: fix parsing of commit trailers inlint-release-proposal
GHA (Antoine du Hamel) #62077 - [
0f15079d94
] - tools: remove custom logic for skippingtest-strace-openat-openssl
(Antoine du Hamel) #62038 - [
54a055a59d
] - tools: bump minimatch from 3.1.2 to 3.1.3 in/tools/clang-format
(dependabot[bot]) #61977 - [
a28744cb62
] - tools: fix permissions for merve update script (Richard Lau) #62023 - [
31e7936354
] - tools: revert tools GHA workflow to ubuntu-latest (Richard Lau) #62024 - [
0a96a16e1f
] - tools: bump minimatch from 3.1.2 to 3.1.3 in /tools/eslint (dependabot[bot]) #61976 - [
f279233412
] - tools: roll back to x86 runner onscorecard.yml
(Antoine du Hamel) #61944 - [
192c0382f4
] - util: add fast path to stripVTControlCharacters (Hiroki Osame) #61833
Windows 64-bit Installer: https://nodejs.org/dist/v25.8.0/node-v25.8.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v25.8.0/node-v25.8.0-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v25.8.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v25.8.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v25.8.0/node-v25.8.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v25.8.0/node-v25.8.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v25.8.0/node-v25.8.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v25.8.0/node-v25.8.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v25.8.0/node-v25.8.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v25.8.0/node-v25.8.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v25.8.0/node-v25.8.0-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v25.8.0/node-v25.8.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v25.8.0/node-v25.8.0.tar.gz
Other release files: https://nodejs.org/dist/v25.8.0/
Documentation: https://nodejs.org/docs/v25.8.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
0af74f04ecd2b939d75ae5bab45e76cd8c5b684c796c7cbc6c497481613d87a0 node-v25.8.0-aix-ppc64.tar.gz
9761b59bcf92ebd572b1023d550d5d6c848adc3cac51ff523e55adee6e65e664 node-v25.8.0-arm64.msi
75ff6fd07e0a85fb4d2529f6189c996014b1d3d83180c31e65feb2b3eaeec5d9 node-v25.8.0-darwin-arm64.tar.gz
53d08ed5b3a3ab7fb098e8d82421b18cf0a6ac4e7403bb2ab43e33f5fb89a395 node-v25.8.0-darwin-arm64.tar.xz
03fb559600c3ede0228d8b588ac6ad8b7b2cd0bac9422b56e7e2ef7f5c11b67c node-v25.8.0-darwin-x64.tar.gz
f126dcc12d8f79d7ab438fcc7ceb91e3efe656d2b2a26160212a4c8215800dd8 node-v25.8.0-darwin-x64.tar.xz
dd6779bc4f8b4eed917da7833585b416b8673968e74c62a7e8d9ca413fbde365 node-v25.8.0-headers.tar.gz
c83752605618b3efefc6c19bd10c9b710ead18ba70d9b036cd75a2adfbced5da node-v25.8.0-headers.tar.xz
54c128f5286a4392a1fd1c765729b074a6873abff8a4f9bb3d63d571c2855e41 node-v25.8.0-linux-arm64.tar.gz
024740906d9af0b9c9fe1a2843447c9eae5dc8cb44d2c5391c2bdf2afccb2bf1 node-v25.8.0-linux-arm64.tar.xz
3ecd09ca302967c858281e494728257db226dd623b464f2b9d8dd88fdaba16e6 node-v25.8.0-linux-ppc64le.tar.gz
b82bf28c1cfeed9862dd0849e548ea0cef8f60edb0a519ebbf9defc52307f91a node-v25.8.0-linux-ppc64le.tar.xz
c48338493b98b24c0a8665a9b5d527c95925d769fe0852e6c8573b2e0264c122 node-v25.8.0-linux-s390x.tar.gz
4b3f40fab11183c69ee3b35db08c0bc8f706e04899407620be58569e89de463b node-v25.8.0-linux-s390x.tar.xz
2ae6f70d74a459c0a96456e486dc60f3e7e65d7752ad302771834e58b27500af node-v25.8.0-linux-x64.tar.gz
f0a38698e3a49105f7323b6bda8f70d864ce853da17c6260a5e1798234d0f87d node-v25.8.0-linux-x64.tar.xz
0fb9beb89195bb01af17c246f7e00b8cb85d55f1e15003b833bcfad014773963 node-v25.8.0.pkg
ba7cb39b3d8d3744385109bfea1f94ed466400452e11b24672c54e645689c521 node-v25.8.0.tar.gz
5d00429cb856cc72200ec6c08e8cdda75ea9618256de8d899fa049c23f4a2eee node-v25.8.0.tar.xz
2e3b464fee036495d46c4ea80b7c1ad06755e102b38187ddf2e7d4717e390051 node-v25.8.0-win-arm64.7z
efdadd968946f58be79bcda43cf2704b5bfaec5db48c8c502583b20f795af298 node-v25.8.0-win-arm64.zip
9ddb70ed2a31db4f36e241c69e527feb72aac710ebcacb1a2de97310da0ee19f node-v25.8.0-win-x64.7z
5744746371a417179a701044739b5fa2b3164e943aa57f86059fb312f8032e86 node-v25.8.0-win-x64.zip
d60366f4a727d09281d1ec1f9c6bff491197796497e0a8f183390b55f18429ed node-v25.8.0-x64.msi
281f54c055c150ad9e5b4c8481dc902d532a750a279d614c131289988020ed19 win-arm64/node.exe
47750ee99207e5b621671565852cf7385f27bf664470886b9437137342a497c9 win-arm64/node.lib
7d7766c0d008c0a6f764e7f4bd0068d036b5cfb69abf8352dad316a69dcc54f8 win-arm64/node_pdb.7z
e1640ebf920ee352782b721e28cb778b40abb3b6c01dd25cd078473cdbb516c9 win-arm64/node_pdb.zip
d0100ef59988cdfcb48a6876b36ea98b1ce006470de24e1e59ab7d5752750c21 win-x64/node.exe
f7201b932d898bdbf78aee7add288d2263c4791f1502068ad11b6c14675c6324 win-x64/node.lib
5abd5051b99140b8cdb26aaf0f46b7aa7a8ca56921fe1e9fe31f3684ee5e9a6a win-x64/node_pdb.7z
b87bfb142fc5b122af8dda75b542866b707ad5c38c3a0aad982346b706fdc80a win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQIzBAEBCAAdFiEEyC+jrhy+3Gvka5NgxDzsRcF6uTwFAmmnBPoACgkQxDzsRcF6
uTwyzhAAl3ymmojzrQPLvR+nHACQD0sfaG3Topx+xAJT3HOCzsF9CZelbaK23Rz3
5xm+FM2zuYBKVLfPnmFyZkLE3myfCClhE2N20KcvokKY0UJ7yZTcmKYW52jWulXv
+RJuNKQJIShC4rVFwoj0JgAnT+iobdD0QjnmixlyL+9OhrpfU5EXiZUD87BIY1go
Ms2Vd58K9+2DBIdEL2zzFyOedBSpM26VcQA30YhvDKGjc2RcEPNVgVhGHI56u+3A
H6yzWyv7GGC9jj4IphKlNkuAV9KqH+KvEl7AcqV5LV5N1JfaJ9WC5JWVQPyONT6/
BZW/exqQ0pNvjubJslf+LKx8tv9gEGiIVhTdL3Gh5/7plph34oAIwTq4lVO/PLTt
yVgR64AVhZWKdUymkY8hIpgJr0CewmIzHeSbk2nSX0fwd0sZaZoQdw3CiTNlH5Uo
LrDvvPoNTZYaS9P+hgMEs3bRK9iztjvs7U/gRwfKdLmLiIu3+YAmZ+DRunB+oZlN
eNyGlhU/um3UfPumO8TegTX06t1pcyiO0ZnY/qd6eOoEDlKFNVmudh4xzpIMaatg
5UqYF432iCCfeUxLORDMORr/CXI7cMHlf0reX0quu7dd6X26wSQotwoRVkAQEigC
Gk7258DoWyo+ZWEBlmoVCmpe3IiqbJq0rA4xQHTRnjqmB0RAKGw=
=liCO
-----END PGP SIGNATURE-----
```

---

## 18. Node.js 25.7.0 (Current)

- 日期: 2026-02-24 15:38
- 链接: https://nodejs.org/en/blog/release/v25.7.0

```
Node.js 25.7.0 (Current)
Ruy Adorno
2026-02-24, Version 25.7.0 (Current), @ruyadorno prepared by @aduh95
Notable Changes
- [
b0a79b10f0
] - (SEMVER-MINOR) http2: add http1Options for HTTP/1 fallback configuration (Amol Yadav) #61713 - [
2d874dfb8e
] - (SEMVER-MINOR) sea: support ESM entry point in SEA (Joyee Cheung) #61813 - [
ee59127664
] - sqlite: mark as release candidate (Matteo Collina) #61262 - [
608736e19e
] - (SEMVER-MINOR) stream: renameDuplex.toWeb()
type option toreadableType
(René) #61632 - [
a43375999f
] - (SEMVER-MINOR) test_runner: show interrupted test on SIGINT (Matteo Collina) #61676
Commits
- [
ab4375e141
] - benchmark: add startup benchmark for ESM entrypoint (Joyee Cheung) #61769 - [
8d83d8026b
] - build: add temporal test on GHA windows (Chengzhong Wu) #61810 - [
aab153eec3
] - build: skip sscache action on non-main branches (Joyee Cheung) #61790 - [
9e40fb93bc
] - build: use path-ignore in GHA coverage-windows.yml (Chengzhong Wu) #61811 - [
4896653361
] - build: generate_config_gypi.py generates valid JSON (Shelley Vohr) #61791 - [
bb82b44de0
] - build: build with v8 gdbjit support on supported platform (Joyee Cheung) #61010 - [
e7173a093a
] - build: show cc outputs when version detection failed (Chengzhong Wu) #61700 - [
848050d38f
] - build,win: add WinGet Visual Studio 2022 Build Tools Edition config (Mike McCready) #61652 - [
938841e1cd
] - crypto: always return certificate serial numbers as uppercase (Anna Henningsen) #61752 - [
dba9001d6f
] - deps: upgrade npm to 11.10.1 (npm team) #61892 - [
75c8e18d2f
] - deps: update nbytes to 0.1.3 (Node.js GitHub Bot) #61879 - [
4ca1597f25
] - deps: remove stale OpenSSL arch configs (René) #61834 - [
c4f298c729
] - deps: update llhttp to 9.3.1 (Node.js GitHub Bot) #61827 - [
7d63a2df93
] - deps: V8: cherry-pick 64b36b441179 (Rafael Magrin) #61712 - [
241a6b7088
] - deps: update googletest to 5a9c3f9e8d9b90bbbe8feb32902146cb8f7c1757 (Node.js GitHub Bot) #61731 - [
eec896c0e0
] - deps: V8: backport 6a0a25abaed3 (Vivian Wang) #61666 - [
5a9874af09
] - doc: clarify status of feature request issues (Antoine du Hamel) #61505 - [
0648ac64aa
] - doc: add esm and cjs examples to node:vm (Alfredo González) #61498 - [
8b38718294
] - doc: clarify build environment is trusted in threat model (Matteo Collina) #61865 - [
10e86818ee
] - doc: remove incorrect mention ofmodule
intypescript.md
(Rob Palmer) #61839 - [
b50376f527
] - doc: simplify addAbortListener example (Chemi Atlow) #61842 - [
dea0e7a856
] - doc: fix typo in --disable-wasm-trap-handler description (Dmytro Semchuk) #61820 - [
57ac1f5aa0
] - doc: clean up globals.md (René) #61822 - [
4c30d2bb4d
] - doc: remove obsolete Boxstarter automated install (Mike McCready) #61785 - [
db610b9e32
] - doc: clarify async caveats forevents.once()
(René) #61572 - [
b4a826b11c
] - doc: update Juan's security steward info (Juan José) #61754 - [
7d9cc5dc54
] - doc: fix methods being documented as properties inprocess.md
(Antoine du Hamel) #61765 - [
aa0362c26a
] - doc: add riscv64 info into platform list (Lu Yahan) #42251 - [
9b0101b65b
] - doc: fix dropdown menu being obscured at <600px due to stacking context (Jeff) #61735 - [
df2c65b3e4
] - doc: fix spacing in process message event (Aviv Keller) #61756 - [
01018559f5
] - doc: move describe/it aliases section before expectFailure (Luca Raveri) #61567 - [
49443583af
] - doc: fix broken links of net.md (YuSheng Chen) #61673 - [
af7c927a2a
] - doc: clean up Windows code snippet inchild_process.md
(reillylm) #61422 - [
221648a687
] - esm: update outdated FIXME comment in translators.js (Karan Mangtani) #61715 - [
4484e14a31
] - events: don't call resume after close (Сковорода Никита Андреевич) #60548 - [
4cecbe1f53
] - fs: addthrowIfNoEntry
option for fs.stat and fs.promises.stat (Juan José) #61178 - [
2c94967684
] - http: remove redundant keepAliveTimeoutBuffer assignment (Efe) #61743 - [
435f3dd8e4
] - http: attach error handler to socket synchronously in onSocket (RajeshKumar11) #61770 - [
ce0ebd853d
] - http: fix keep-alive socket reuse race in requestOnFinish (Martin Slota) #61710 - [
8103a78b6a
] - http2: add strictSingleValueFields option to relax header validation (Tim Perry) #59917 - [
b0a79b10f0
] - (SEMVER-MINOR) http2: add http1Options for HTTP/1 fallback configuration (Amol Yadav) #61713 - [
c589b6b23c
] - http2: fix FileHandle leak in respondWithFile (sangwook) #61707 - [
df477202ae
] - lib: reduce cycles in esm loader and load it in snapshot (Joyee Cheung) #61769 - [
deda50a819
] - lib: remove top-level getOptionValue() calls in lib/internal/modules (Joyee Cheung) #61769 - [
b1c1ddff79
] - lib: optimize styleText when validateStream is false (Rafael Gonzaga) #61792 - [
df334f7fa0
] - meta: use SCCACHE_GHA_ENABLED for shared build workflows (René) #61640 - [
e1b2cd605f
] - meta: bump cachix/install-nix-action from 31.9.0 to 31.9.1 (dependabot[bot]) #61910 - [
24b858547a
] - module: fix extensionless entry with explicit type=commonjs (Yuya Inoue) #61600 - [
4f2f8006bd
] - repl: fix FileHandle leak in history initialization (sangwook) #61706 - [
2d874dfb8e
] - (SEMVER-MINOR) sea: support ESM entry point in SEA (Joyee Cheung) #61813 - [
ee59127664
] - sqlite: mark as release candidate (Matteo Collina) #61262 - [
f14ff14473
] - src: remove unnecessaryc_str()
conversions in diagnostic messages (Anna Henningsen) #61786 - [
26a09e541d
] - src: use bool literals in TraceEnvVarOptions (Tobias Nießen) #61425 - [
62b0758c47
] - src: fix--build-sea
default executable path (Alex Schwartz) #61708 - [
b5724921b1
] - src: track allocations made by zstd streams (Anna Henningsen) #61717 - [
3d1d1523a5
] - src: do not store compression methods on Brotli classes (Anna Henningsen) #61717 - [
b2915cda77
] - src: extract zlib allocation tracking into its own class (Anna Henningsen) #61717 - [
3032a7e3c6
] - src: release memory for zstd contexts inClose()
(Anna Henningsen) #61717 - [
bc2287db74
] - src: add more checks and clarify docs for external references (Joyee Cheung) #61719 - [
5daf282e33
] - src: fix cjs_lexer external reference registration (Joyee Cheung) #61718 - [
fb2db5f947
] - src: support import() and import.meta in embedder-run modules (Joyee Cheung) #61654 - [
e146591002
] - stream: fix decoded fromList chunk boundary check (Thomas Watson) #61884 - [
065200a5f0
] - stream: add fast paths for webstreams read and pipeTo (Matteo Collina) #61807 - [
608736e19e
] - (SEMVER-MINOR) stream: renameDuplex.toWeb()
type option toreadableType
(René) #61632 - [
51587d684d
] - test: fix typos in test files (Daijiro Wachi) #61408 - [
17b2361360
] - test: allow filtering async internal frames in assertSnapshot (Joyee Cheung) #61769 - [
3f6a5f5f7f
] - test: unify assertSnapshot stacktrace transform (Chengzhong Wu) #61665 - [
c8dac320de
] - test: check stability block position in API markdown (René) #58590 - [
6809ef8d04
] - test: adapt buffer test for v8 sandbox (Shelley Vohr) #61772 - [
60f5771a74
] - test: update FileAPI tests from WPT (Ms2ger) #61750 - [
d2fef4a31a
] - test: update WPT for WebCryptoAPI to 7cbe7e8ed9 (Node.js GitHub Bot) #61729 - [
d7a87f14da
] - test: update WPT for url to efb889eb4c (Node.js GitHub Bot) #61728 - [
b6ae1fc4b8
] - test: split test-embedding.js and run tests in parallel (Joyee Cheung) #61571 - [
a43375999f
] - (SEMVER-MINOR) test_runner: show interrupted test on SIGINT (Matteo Collina) #61676 - [
1c02aa09b0
] - test_runner: fix suite rerun (Moshe Atlow) #61775 - [
47821ec609
] - tools: switch to ARM runners on GHA jobs (Antoine du Hamel) #61903 - [
1630a56370
] - tools: avoid building twice in coverage jobs (Antoine du Hamel) #61899 - [
89318b0a02
] - tools: fix auto-start-ci (Antoine du Hamel) #61900 - [
ee107f5e84
] - tools: do not checkout repo inauto-start-ci.yml
(Antoine du Hamel) #61874 - [
c2de1fa619
] - tools: cache V8 build on test-shared workflow (Antoine du Hamel) #61860 - [
111c77ec94
] - tools: automate updates for test/fixtures/test426 (Rich Trott) #60978 - [
ea8886f7d5
] - tools: use ubuntu-slim runner in GHA (Antoine du Hamel) #61759 - [
9db82ba786
] - tools: bump unist-util-visit in /tools/doc in the doc group (dependabot[bot]) #61646 - [
c8e58c56b9
] - tools: bump the eslint group in /tools/eslint with 6 updates (dependabot[bot]) #61628 - [
2518ec77e8
] - tools: use ubuntu-slim runner in GHA (Antoine du Hamel) #61734 - [
c5ad2beba3
] - tools: fix small inconsistencies in JSON doc output (Antoine du Hamel) #61757 - [
a9f90bee0a
] - tools: use ubuntu-latest runner innotify-on-push
workflow (Antoine du Hamel) #61742 - [
30e38182d9
] - watch: get flags from execArgv (Efe) #61779 - [
da1a08a3a5
] - worker: eliminate race condition in process.cwd() (giulioAZ) #61664 - [
dfac82a235
] - zlib: add support for brotli compression dictionary (Andy Weiss) #61763
Windows 64-bit Installer: https://nodejs.org/dist/v25.7.0/node-v25.7.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v25.7.0/node-v25.7.0-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v25.7.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v25.7.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v25.7.0/node-v25.7.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v25.7.0/node-v25.7.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v25.7.0/node-v25.7.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v25.7.0/node-v25.7.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v25.7.0/node-v25.7.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v25.7.0/node-v25.7.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v25.7.0/node-v25.7.0-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v25.7.0/node-v25.7.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v25.7.0/node-v25.7.0.tar.gz
Other release files: https://nodejs.org/dist/v25.7.0/
Documentation: https://nodejs.org/docs/v25.7.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
500805d140c6eae59705c12eeb4c59954c872b345be3a880dd59d7fa4d134abb node-v25.7.0-aix-ppc64.tar.gz
39d400db485fdb261981849a15c52c1f051ff8356c0f75c02bb09151498c290d node-v25.7.0-arm64.msi
d4e3cfe5e6bddda41ba0c683e37329632465b93371ddc538c763578758d5bc35 node-v25.7.0-darwin-arm64.tar.gz
6745e61fc00c87f20a3584591275d55b1712891eaa06d28a6bf7e97bc91262ec node-v25.7.0-darwin-arm64.tar.xz
f83929f4a84ae5a88c2a5333466b100dd101658063592497626ae9eea15b3b1b node-v25.7.0-darwin-x64.tar.gz
4843ab17e74d088a6d20d6a30589d648205a261c5b9c7f0d50235610aff2ff1b node-v25.7.0-darwin-x64.tar.xz
62b6ce65475bd3ac88f4f3f7e31c8c9f35b9c9631296e82a62670b72d1234fe1 node-v25.7.0-headers.tar.gz
b6646b9ceba75246021f3f6db4e9863dc6ee9ec87d93a3be1382fb9da1f6e1ad node-v25.7.0-headers.tar.xz
3a73c9145547b5d2e29491b0ed6a37b95306b784eb83cdb2361f1e2e76fa237f node-v25.7.0-linux-arm64.tar.gz
4aad827d8ecce8143624e09b98946e23c96a270a1407e9c13a56ceec163b4205 node-v25.7.0-linux-arm64.tar.xz
c2b5e162efb21a1d41c026bf5b08b3798e2e813b969031b1ed069b167cce77a0 node-v25.7.0-linux-ppc64le.tar.gz
59076fc29ca75b73caeafa91bb627e0c5fe083b0b7d3077389459bfea7712b78 node-v25.7.0-linux-ppc64le.tar.xz
c53a17fb58b0d8ec3001268bc69fbd4e3ec97034b7fde7c95b422d5734c52cd5 node-v25.7.0-linux-s390x.tar.gz
048749b91d9d0946b684a487c465adf56bff983949d8610ba6c0951ae61142ce node-v25.7.0-linux-s390x.tar.xz
033ad3a740d62d3c7e3aaa1fecfeec16a719d4af33ab030666bf171057b070d9 node-v25.7.0-linux-x64.tar.gz
2af25e8fc301bb3bbf02874f7d07e1d00483dc143fbd0eb56ee844c17849168e node-v25.7.0-linux-x64.tar.xz
477eb8f5499904b2eb76212e0f14f40965c693795b0af8e1500cc7aeaa1c18b8 node-v25.7.0.pkg
2a36edd1c8cc4d275464ff873a199937c8237c13f6943db5f7879f8a83ceddbe node-v25.7.0.tar.gz
8f13df7e8f79c3e8f227ad713c754592293c98f70e9e29e8fcee974e62a000e1 node-v25.7.0.tar.xz
297368ae8d82b138ad604a52578b4e2144e802d4c2855be8d3ea60ef7bf6b455 node-v25.7.0-win-arm64.7z
8b824eb15ae95d24bd082cee9637f74d5850ba5c8649bd65c5f108e360835f1e node-v25.7.0-win-arm64.zip
388fd0d55294854a132adb3bd4deee8b5afef431b7d8a3babc34ae0931ca00e8 node-v25.7.0-win-x64.7z
4a66eac416c30474fe9c3f0ef7d4ffc85a8797cbc35f6b8566dfbce02789a9c4 node-v25.7.0-win-x64.zip
5cb49889fd408ab9fe19471b0ab52badaf5724e47a6f824b0e11cafd09576838 node-v25.7.0-x64.msi
3e29601f88368da267420815f89e7bc73d67de7793a60b70a25c0c25dd6c6843 win-arm64/node.exe
47750ee99207e5b621671565852cf7385f27bf664470886b9437137342a497c9 win-arm64/node.lib
c9357f6f020191a72159acfcffc5f1c0828d841dc8d247e9af37798b97e55dca win-arm64/node_pdb.7z
279f034bebb2750f18e9bfe54688c301b517398f0cf6e1e09df57d90ab8b552d win-arm64/node_pdb.zip
6d27b928592496d739f97eb0dec6818fd7b23089ef4626f8967ece5907d23d36 win-x64/node.exe
f7201b932d898bdbf78aee7add288d2263c4791f1502068ad11b6c14675c6324 win-x64/node.lib
406b61316a6d06a0e7396d98ada6e3bd76de5ca9d8fc454fafc867c59341c060 win-x64/node_pdb.7z
1e0e09b139fa8e116b339a9f8c27f5235ffee457d6ee4bc133f07671a5aa5521 win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQIzBAEBCAAdFiEEEI9StI21e7DMQ5spl7AUGb2S+AoFAmmdxT4ACgkQl7AUGb2S
+Aq13A/+LZPSUeuaxLXPqztZV4GYmt35Z1JEyXou4AZp2asnAVEvLKy49hIm82cQ
Carn4LlOKLXuvEh0ZdYs53iT+xX+gIJfTQdXC/Kjaa61Rj4rdXeCP6qL1WuL39oN
FWYyk/ubhrFFWC8KV0UbGGf9Zv9wICSSDsFsdfxpkuO0aOfpC3Bj1I2j8JrlHlTP
L9mgZJs47ymlx5GGVIvK/niPBJh0znzDilQjAAj8txU6QSD+GA75ovkBkQd5s3jV
sgGTz0tRCUn8II7enmV/dfDgF9b50xP4k6vyqsNaV3WDtra7rTgehnYXgBK8lqiz
ajcaXNDd1+25pL7bkth1icAFODvZqOv8lywUlsdX1ufg8ZIP8+k/+H5Q7vsBCApH
+wapAEG5sUzN+tydJD0Xn73UNlOo+r+kLWndFD27Pfg/v4oP76fX9JNEEUEvryxT
qsqk87hL9dZkID+wOvgDpZR2md09bq2Ra4Jq1K20VaRjlfvd9zI8vcxktIdUZ2ha
7Y333TasoBl1zlM507X2Z7vvnTDWOKsZ4mDtPwSFXy09puJBexa32X0BWU0TzPqR
Qeb3b3voysIwk9KoILOrzdukb3BKXeIJul3Y/1vAyO3kolLFE/O+80Sm6TxfZ8SX
mDM7qdAGxX+TJ/AJHf+bBkEjxYim0VMwplD0LrT5HQvQ3qmzauk=
=58BT
-----END PGP SIGNATURE-----
```

---

## 19. Node.js 24.14.0 (LTS)

- 日期: 2026-02-24 15:38
- 链接: https://nodejs.org/en/blog/release/v24.14.0

```
Node.js 24.14.0 (LTS)
Ruy Adorno
2026-02-24, Version 24.14.0 'Krypton' (LTS), @ruyadorno prepared by @aduh95
Notable Changes
- [
8b6d31d379
] - (SEMVER-MINOR) async_hooks: addtrackPromises
option tocreateHook()
(Joyee Cheung) #61415 - [
68da144b4e
] - build,deps: replace cjs-module-lexer with merve (Yagiz Nizipli) #61456 - [
f3a24c76e4
] - (SEMVER-MINOR) deps: add LIEF as a dependency (Joyee Cheung) #61167 - [
1948861d23
] - (SEMVER-MINOR) events: repurposeevents.listenerCount()
to accept EventTargets (René) #60214 - [
d6f7c8d06f
] - (SEMVER-MINOR) fs: addignore
option tofs.watch
(Matteo Collina) #61433 - [
cb54b3ca6e
] - (SEMVER-MINOR) http: addhttp.setGlobalProxyFromEnv()
(Joyee Cheung) #60953 - [
35b1759d06
] - (SEMVER-MINOR) module: allow subpath imports that start with#/
(Jan Martin) #60864 - [
2d72ea66f2
] - (SEMVER-MINOR) process: preserveAsyncLocalStorage
inqueueMicrotask
only when needed (Gürgün Dayıoğlu) #60913 - [
6f4a4f6c8e
] - (SEMVER-MINOR) sea: split sea binary manipulation code (Joyee Cheung) #61167 - [
c0ceb9b065
] - (SEMVER-MINOR) sqlite: enable defensive mode by default (Bart Louwers) #61266 - [
33d8e8303b
] - (SEMVER-MINOR) sqlite: add sqlite prepare options args (Guilherme Araújo) #61311 - [
563ab699eb
] - (SEMVER-MINOR) src: add initial support for ESM in embedder API (Joyee Cheung) #61548 - [
4c80031000
] - (SEMVER-MINOR) stream: addbytes()
method tonode:stream/consumers
(wantaek) #60426 - [
f5233df4ff
] - (SEMVER-MINOR) stream: do not passreadable.compose()
output viaReadable.from()
(René) #60907 - [
345a40fda3
] - (SEMVER-MINOR) test: use fixture directories for sea tests (Joyee Cheung) #61167 - [
972f82411d
] - (SEMVER-MINOR) test_runner: addenv
option torun
function (Ethan Arrowood) #61367 - [
d77f98c4b6
] - (SEMVER-MINOR) test_runner: support expecting a test-case to fail (Jacob Smith) #60669 - [
8e900af6ba
] - (SEMVER-MINOR) util: addconvertProcessSignalToExitCode
utility (Erick Wendel) #60963
Commits
- [
180778fb9a
] - assert: fix loose deepEqual arrays with undefined and null failing (Ruben Bridgewater) #61587 - [
8b6d31d379
] - (SEMVER-MINOR) async_hooks: add trackPromises option to createHook() (Joyee Cheung) #61415 - [
83bcd38d35
] - benchmark: add streaming TextDecoder benchmark (Сковорода Никита Андреевич) #61549 - [
4c105844c5
] - build: add support for Visual Studio 2026 (Michaël Zasso) #60727 - [
1f84fd91d9
] - build: skip sscache action on non-main branches (Joyee Cheung) #61790 - [
30601b680f
] - build: add--shared-nbytes
configure flag (Antoine du Hamel) #61341 - [
c6253eda49
] - build: add--shared-hdr-histogram
configure flag (Antoine du Hamel) #61280 - [
584c189037
] - build: add--shared-gtest
configure flag (Antoine du Hamel) #61279 - [
5998987881
] - build: aix: deoptimize implementation-visitor.cc with --shared (Stewart X Addison) #61550 - [
68da144b4e
] - build,deps: replace cjs-module-lexer with merve (Yagiz Nizipli) #61456 - [
6a4511bafb
] - build,win: fix vs2022 compilation (Stefan Stojanovic) #61530 - [
2d6735db8a
] - deps: upgrade npm to 11.9.0 (npm team) #61685 - [
699e2f8f81
] - deps: update amaro to 1.1.7 (Node.js GitHub Bot) #61730 - [
7be76316d6
] - deps: update minimatch to 10.1.2 (Node.js GitHub Bot) #61732 - [
97e5a65013
] - deps: update undici to 7.21.0 (Node.js GitHub Bot) #61683 - [
74e4710ee7
] - deps: update googletest to 56efe3983185e3f37e43415d1afa97e3860f187f (Node.js GitHub Bot) #61605 - [
b5113e2a2a
] - deps: update amaro to 1.1.6 (Node.js GitHub Bot) #61603 - [
f3a24c76e4
] - (SEMVER-MINOR) deps: add LIEF as a dependency (Joyee Cheung) #61167 - [
c370c3dc06
] - (SEMVER-MINOR) deps: add tools and scripts to pull LIEF as a dependency (Joyee Cheung) #61167 - [
e54975e17d
] - deps: V8: cherry-pick highway@dcc0ca1cd42 (Richard Lau) #61008 - [
625b90b76b
] - deps: update undici to 7.19.2 (Node.js GitHub Bot) #61566 - [
05e9a9fb5e
] - deps: update undici to 7.19.1 (Node.js GitHub Bot) #61514 - [
3d41643e38
] - deps: update undici to 7.19.0 (Node.js GitHub Bot) #61470 - [
17b363a66c
] - dns: fix Windows SRV ECONNREFUSED by adjusting c-ares fallback detection (notvivek12) #61453 - [
33d0a8c22d
] - doc: clarify EventEmitter error handling in threat model (Matteo Collina) #61701 - [
5b8e72cf85
] - doc: mention default option for test runner env (Steven) #61659 - [
f44e67fac2
] - doc: fix --inspect security warning section (Tim Perry) #61675 - [
a0e09c9043
] - doc: documenturl.format(urlString)
as deprecated under DEP0169 (René) #61644 - [
5e719248fe
] - doc: deprecation add more codemod (Augustin Mauroy) #61642 - [
8f5a3e5df4
] - doc: fix grammatical error in README.md (ayj8201) #61653 - [
d52b535163
] - doc: correct tools README Boxstarter link (Mike McCready) #61638 - [
4889dc4f59
] - doc: updateserver.dropMaxConnection
link (YuSheng Chen) #61584 - [
8e48e72f2a
] - doc: clean up writing-and-running-benchmarks.md (Hardanish Singh) #61345 - [
1948861d23
] - (SEMVER-MINOR) events: repurposeevents.listenerCount()
to accept EventTargets (René) #60214 - [
d6f7c8d06f
] - (SEMVER-MINOR) fs: add ignore option to fs.watch (Matteo Collina) #61433 - [
2d7e5f9581
] - http: implement slab allocation for HTTP header parsing (Mert Can Altin) #61375 - [
cb54b3ca6e
] - (SEMVER-MINOR) http: add http.setGlobalProxyFromEnv() (Joyee Cheung) #60953 - [
6df8be48ce
] - lib: use utf8 fast path for streaming TextDecoder (Сковорода Никита Андреевич) #61549 - [
830fff0aca
] - lib: recycle queues (Robert Nagy) #61461 - [
069874bdbd
] - lib: use StringPrototypeStartsWith from primordials in locks (Taejin Kim) #61492 - [
7824c7589e
] - lib: unify ICU and no-ICU TextDecoder (Сковорода Никита Андреевич) #61409 - [
f81430702a
] - lib: prefercall()
overapply()
if argument list is not array (Livia Medeiros) #60796 - [
a723f72e1e
] - lib: add support for readable byte streams to .toWeb() (Hans Klunder) #58664 - [
b78d814b3d
] - meta: persist sccache daemon until end of build workflows (René) #61639 - [
40a872a4b9
] - meta: bump github/codeql-action from 4.31.9 to 4.32.0 (dependabot[bot]) #61622 - [
0637bdb3be
] - meta: bump step-security/harden-runner from 2.14.0 to 2.14.1 (dependabot[bot]) #61621 - [
e8d9bd9fc5
] - meta: bump actions/setup-python from 6.1.0 to 6.2.0 (dependabot[bot]) #61627 - [
c517df2b65
] - meta: bump actions/setup-node from 6.1.0 to 6.2.0 (dependabot[bot]) #61625 - [
9a64f2f25d
] - meta: bump actions/cache from 5.0.1 to 5.0.3 (dependabot[bot]) #61624 - [
0e5922e95e
] - meta: bump peter-evans/create-pull-request from 8.0.0 to 8.1.0 (dependabot[bot]) #61623 - [
5da7b51091
] - meta: bump actions/stale from 10.1.0 to 10.1.1 (dependabot[bot]) #61620 - [
c085c8a43f
] - meta: bump actions/checkout from 6.0.1 to 6.0.2 (dependabot[bot]) #61619 - [
ce2acf0275
] - meta: bump actions/download-artifact from 6.0.0 to 7.0.0 (dependabot[bot]) #61242 - [
629f0eaac5
] - meta: bump actions/checkout from 6.0.0 to 6.0.1 (dependabot[bot]) #61239 - [
cd80d369c9
] - meta: bump actions/upload-artifact from 5.0.0 to 6.0.0 (dependabot[bot]) #61238 - [
8c75e4e1fa
] - meta: bump actions/checkout from 5.0.1 to 6.0.0 (dependabot[bot]) #60925 - [
5a9e9f4127
] - meta: bump actions/checkout from 5.0.0 to 5.0.1 (dependabot[bot]) #60767 - [
1519251dd1
] - module: do not invoke resolve hooks twice for imported cjs (Joyee Cheung) #61529 - [
8d7190b3fe
] - module: do not wrap module._load when tracing is not enabled (Joyee Cheung) #61479 - [
35b1759d06
] - (SEMVER-MINOR) module: allow subpath imports that start with#/
(Jan Martin) #60864 - [
7a83b38921
] - net: defer synchronous destroy calls in internalConnect (RajeshKumar11) #61658 - [
16bab79421
] - process: do not truncate long strings in--print
(Mohamed Akram) #61497 - [
2d72ea66f2
] - (SEMVER-MINOR) process: preserve AsyncLocalStorage in queueMicrotask only when needed (Gürgün Dayıoğlu) #60913 - [
9cc1c4604f
] - repl: fix getters triggering side effects during completion (Dario Piotrowicz) #61043 - [
93703306a1
] - repl: tab completion targets<class>
instead ofnew <class>
(Đỗ Trọng Hải) #60319 - [
6f4a4f6c8e
] - (SEMVER-MINOR) sea: split sea binary manipulation code (Joyee Cheung) #61167 - [
46a2dad4db
] - sqlite: avoid extra copy for large text binds (Ali Hassan) #61580 - [
f91a377f7e
] - sqlite: use DictionaryTemplate for run() result (Mert Can Altin) #61432 - [
0e7571ae3e
] - sqlite: change approach to fix segfault SQLTagStore (Bart Louwers) #60462 - [
8e8f70524a
] - sqlite: reserve vectors space (Guilherme Araújo) #61540 - [
c0ceb9b065
] - (SEMVER-MINOR) sqlite: enable defensive mode by default (Bart Louwers) #61266 - [
33d8e8303b
] - (SEMVER-MINOR) sqlite: add sqlite prepare options args (Guilherme Araújo) #61311 - [
f0d8f37002
] - src: elide heap allocation in structured clone implementation (Anna Henningsen) #61703 - [
db478c4336
] - src: use simdutf for one-byte string UTF-8 write in stringBytes (Mert Can Altin) #61696 - [
563ab699eb
] - (SEMVER-MINOR) src: add initial support for ESM in embedder API (Joyee Cheung) #61548 - [
da13186a15
] - src: throw RangeError on failed ArrayBuffer BackingStore allocation (Chengzhong Wu) #61480 - [
4c80031000
] - (SEMVER-MINOR) stream: add bytes() method to stream/consumers (wantaek) #60426 - [
f5233df4ff
] - (SEMVER-MINOR) stream: do not passreadable.compose()
output viaReadable.from()
(René) #60907 - [
ad04a469c8
] - test: restraint version replacement pattern in snapshots (Chengzhong Wu) #61748 - [
2d3b4a8d65
] - test: print stack immediately avoiding GC interleaving (Chengzhong Wu) #61699 - [
38f43a6d4e
] - test: fix case-insensitive path matching on Windows (Matteo Collina) #61682 - [
06513f5ff2
] - test: fix flaky test-performance-eventloopdelay (Matteo Collina) #61629 - [
9d79c66c61
] - test: remove duplicate wpt tests (Filip Skokan) #61617 - [
eac9f4f401
] - test: fix race condition in watch mode tests (Matteo Collina) #61615 - [
ecf5947575
] - test: update WPT for url to e3c46fdf55 (Node.js GitHub Bot) #61602 - [
356ff5fece
] - test: use the skipIfNoWatch() utility function (Luigi Pinca) #61531 - [
4b2187aea2
] - test: unify assertSnapshot common patterns (Chengzhong Wu) #61590 - [
8c25489d63
] - test: split test-fs-watch-ignore-* (Luigi Pinca) #61494 - [
43b8a2b7e7
] - test: add some validation for JSON doc output (Antoine du Hamel) #61413 - [
345a40fda3
] - (SEMVER-MINOR) test: use fixture directories for sea tests (Joyee Cheung) #61167 - [
24cf6b8326
] - test: reveal wpt evaluation errors in status files (Chengzhong Wu) #61358 - [
d4034dfb62
] - test: forbid use of named imports for fixtures (Antoine du Hamel) #61228 - [
4f871ee897
] - test: enforce better never-settling-promise detection (Antoine du Hamel) #60976 - [
8e9adedf02
] - test: ensure assertions are reached on all tests (Antoine du Hamel) #60845 - [
273832802e
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60763 - [
e06adcb52f
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60760 - [
aeed0ccc02
] - test: useRegExp.escape
to improve test reliability (Antoine du Hamel) #60803 - [
74bcd0adab
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60728 - [
407807b08e
] - test: skip tests not passing withoutNODE_OPTIONS
support (Antoine du Hamel) #60912 - [
a9e70cefb0
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60634 - [
21b23cd0d0
] - test_runner: fix test enqueue when test file has syntax error (Edy Silva) #61573 - [
6a4de694b2
] - test_runner: fix passingexpectFailure
(Moshe Atlow) #61568 - [
6640de2b0f
] - test_runner: differentiate todo and failure styles (Moshe Atlow) #61564 - [
972f82411d
] - (SEMVER-MINOR) test_runner: add env option to run function (Ethan Arrowood) #61367 - [
d77f98c4b6
] - (SEMVER-MINOR) test_runner: support expecting a test-case to fail (Jacob Smith) #60669 - [
f98986cbb9
] - tools: switch to ARM runners on GHA jobs (Antoine du Hamel) #61903 - [
034589dd93
] - tools: avoid building twice in coverage jobs (Antoine du Hamel) #61899 - [
e50e2f00bb
] - tools: use ubuntu-slim runner in GHA (Antoine du Hamel) #61759 - [
f658f48ccb
] - tools: use ubuntu-slim runner in GHA (Antoine du Hamel) #61734 - [
65c77d74ff
] - tools: use ubuntu-latest runner innotify-on-push
workflow (Antoine du Hamel) #61742 - [
605905556a
] - tools: enforce removal oflts-watch-*
labels on release proposals (Antoine du Hamel) #61672 - [
f0f98d4c03
] - tools: use ubuntu-slim runner in meta GitHub Actions (Tierney Cyren) #61663 - [
ab63ddf354
] - tools: add LIEF to license builder (Chengzhong Wu) #61523 - [
8a0f6192c9
] - tools: enforce trailing commas intest/es-module
(Antoine du Hamel) #60891 - [
4afbbcf39e
] - tools: enforce trailing commas intest/sequential
(Antoine du Hamel) #60892 - [
4c1abf752c
] - tools,win: upgrade install additional tools to Visual Studio 2026 (Mike McCready) #61562 - [
8e900af6ba
] - (SEMVER-MINOR) util: add convertProcessSignalToExitCode utility (Erick Wendel) #60963
Windows 64-bit Installer: https://nodejs.org/dist/v24.14.0/node-v24.14.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v24.14.0/node-v24.14.0-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v24.14.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v24.14.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v24.14.0/node-v24.14.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v24.14.0/node-v24.14.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v24.14.0/node-v24.14.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v24.14.0/node-v24.14.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v24.14.0/node-v24.14.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v24.14.0/node-v24.14.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v24.14.0/node-v24.14.0-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v24.14.0/node-v24.14.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v24.14.0/node-v24.14.0.tar.gz
Other release files: https://nodejs.org/dist/v24.14.0/
Documentation: https://nodejs.org/docs/v24.14.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
27ac48f94c7e88f4b0c5d9077f0fec10256289c7dca21e0d9f82cbaad13d6e3d node-v24.14.0-aix-ppc64.tar.gz
63d07136eead197b66c58f4ee6c4343e0b4027cc3a1f852ada45b081250e21b7 node-v24.14.0-arm64.msi
a1a54f46a750d2523d628d924aab61758a51c9dad3e0238beb14141be9615dd3 node-v24.14.0-darwin-arm64.tar.gz
448f01d4dfa5a21d280cfbacf00abc22b51aad52f38db0f4886e0e5d00df541d node-v24.14.0-darwin-arm64.tar.xz
f2879eb810e25993a0578e5d878930266fd2eafcffe9f2839b3d8db354d4879e node-v24.14.0-darwin-x64.tar.gz
c17b234c4db75eeb03c3a86664428ec25ee849e1ebbe8cb05c4a70f282187866 node-v24.14.0-darwin-x64.tar.xz
bc1505c8e2b2b1f7b7cf3808bf53691e5d110c816d1bc1a48075195c5dcafe05 node-v24.14.0-headers.tar.gz
87d1a7d80599ce330de0f0832f6b85c7d93c5be7b6a203725afa016405227988 node-v24.14.0-headers.tar.xz
f44740cd218de8127f1c44c41510a3a740fa5c9c8d1cdce1c3bedada79f3cde7 node-v24.14.0-linux-arm64.tar.gz
e7adfca03d9173276114a6f2219df1a7d25e1bfd6bbd771d3f839118a2053094 node-v24.14.0-linux-arm64.tar.xz
83b263f9c2ea946c0c4a15c3caea6470dc49fe0beb6f33dfd29aa9128250637a node-v24.14.0-linux-ppc64le.tar.gz
33beedaf3ff82ee511cfc5ca0cc7076161a54a982321d061409299e27bc5f41e node-v24.14.0-linux-ppc64le.tar.xz
8fa220a1f7b7769605c2e929fdbf736822997bf4cf88a3db05188eabd7712328 node-v24.14.0-linux-s390x.tar.gz
d133f1aac2d6dbaa4de9fe183184e57adbc9f45d62e37f55a864c8af92d4cb5a node-v24.14.0-linux-s390x.tar.xz
dbf5b8665dec15e59e6359a517fefb47b23fdb9152d8def975b9bca3dfc6d355 node-v24.14.0-linux-x64.tar.gz
41cd79bb7877c81605a9e68ec4c91547774f46a40c67a17e34d7179ef11729df node-v24.14.0-linux-x64.tar.xz
5514f833980f172088ce22883000d1aea9db9eea41cb1a306154eb4f333ec1c0 node-v24.14.0.pkg
852c73dd5b6ba15b231d036da6312dbcdabd6295adc3940586f3187b77731cf3 node-v24.14.0.tar.gz
9fe025ef4028aba95d16e7810518bf4a5e8abfb0bdc07d8a3fdbb0afd538d77f node-v24.14.0.tar.xz
6cd8d95799dc70e89585522e5cfe5d576b6ac44f6ff5afc0a4b0318c9f7aa8cd node-v24.14.0-win-arm64.7z
88d36e8109736a2fa9bdc596f2cf507a3c52c69cdf96e54f8acd473ec14be853 node-v24.14.0-win-arm64.zip
90f18586ef8ca13dd94e7f571d27b8a5120116fea218bcc41e3ef6697dcbc777 node-v24.14.0-win-x64.7z
313fa40c0d7b18575821de8cb17483031fe07d95de5994f6f435f3b345f85c66 node-v24.14.0-win-x64.zip
e75802e82be6875b03b63377a9e12e4416799d0fb6dd460f0605d29144d386a6 node-v24.14.0-x64.msi
8c5fd45a4a1fd3cc4a6f07da8803b05194108906cb6fb7d962448a12582a5922 win-arm64/node.exe
59f1c42e5962e9333bb1673c21125b7a7ce9a6908299aee8f7673803c2e24212 win-arm64/node.lib
5a7c7261b40fd4e39bc4410e23d31e48857d737d830434ea2dc215fec892a8dd win-arm64/node_pdb.7z
3bf09a2b133893208ad48b3c439dad570aa4cc2a5fe842bc137f795aa4e72944 win-arm64/node_pdb.zip
63c259c81e5d472b5f11c8d506070130cb04a1ecf84b80377a34ed6ec9048088 win-x64/node.exe
35fcdd35d3d22e283c0e2e095cc43ef676301bb85f950c344a73d59231bd7e61 win-x64/node.lib
802553494ca6c8049aa542ddcc54e2616a0a1819ae23f894767a4110a1ec0b5a win-x64/node_pdb.7z
b8e1aee14390b2828ede1f4b89ed8a8b0c5da40e43fbfe14dc4b42dc14ed3710 win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQIzBAEBCAAdFiEEEI9StI21e7DMQ5spl7AUGb2S+AoFAmmdxM8ACgkQl7AUGb2S
+AqtGg//VNRQePlUD0cVBO0AnCnV4LlkmkIdxYDmD1Myk2blqC1rvLsGDj1kwfp0
cOrDI1PvnYrasK9N5Q1cF+g9ZJDgv59v8lLkPYng8hYPiVgyYE4e00QSPMebDzwu
jwIZtNdR0sdD6nAq3WLQQFqkvytj2y4OhL1w4+OiXomBXYRC7CU3/ZwzEsrJ/od6
QeO10KezF3luDGiMXVoJzn1pxm6Itvcdyqu0DZkBsbX6IrzR+Kbb2wv/dWUafas+
PM9J89QhV4UTgRSHo6O5FnG6ZStcOpa/o4yCWmO9EA1GBv/n3Jnr/uk8zNE2ODwe
TV0OiJnbUrCx0dQQTx42wVQL+Ust/PLu5m5csnO0R5E/QCVBxwwF6+CnPyNP6HgF
fA+2PoKuv5pSCbfupfJg0KLSxToX6p3wO02sRzQnpzY8usdEel071n6246TjYRqM
o4nS5FgLlBLd1djKjOna62QYsKtOvldZ1+R96rQBOW7oYeAG9vggGcbuWN2y2zvu
ctcVpC3+cj2wEQ/N2NQOz/Zd//m8j19XgIoNxHuU6w0xGXxHnyTpJhrd5bI3L3R4
QMK+v67uM9qVLPPZdEFbRpwVv/UhtM2jewcQtwnplo2dseWO3n+CXgRs8DOK5JKX
RN7ozy+bCPm3ayU6O01MmUiUaD9PQA/lIE2M4jZ9qfmhWuTlk20=
=i+aM
-----END PGP SIGNATURE-----
```

---

## 20. New HackerOne Signal Requirement for Vulnerability Reports

- 日期: 2026-02-19 12:00
- 链接: https://nodejs.org/en/blog/announcements/hackerone-signal-requirement

```
New HackerOne Signal Requirement for Vulnerability Reports
The Node.js Project
UPDATE 2026-02-19: New researchers without signal can no longer submit reports through HackerOne. If you are a new researcher and would like to report a potential vulnerability, please reach out to the Node.js security release stewards through the OpenJS Foundation Slack.
We have updated our HackerOne program to require a Signal of 1.0 or higher to submit vulnerability reports to the Node.js project.
Why This Change
The Node.js security team has experienced a significant increase in low-quality reports. This trend has been increasing over the years, and over the holidays it crossed the threshold that we can actually handle. Between December 15th and January 15th, we received over 30 reports. Triaging these reports consumes time and energy that could be spent on legitimate security work.
By requiring a minimum Signal score, we ensure that reporters have a proven track record of submitting valid security reports, while still allowing newer researchers to participate with a limited number of submissions.
What This Means for You
- New researchers or researchers with signal >= 1.0: You can continue reporting vulnerabilities through HackerOne as usual
- Those below the threshold: You can still reach the security team through the
OpenJS Foundation Slack (channel:
#nodejs-security-wg
for help). Contact us directly using direct messages there to discuss potential vulnerabilities. You can find the users listed in security release stewards.
About HackerOne Signal
Signal is HackerOne's reputation metric that reflects the quality of a researcher's past submissions. A higher Signal indicates a history of valid, impactful reports. This requirement helps us prioritize reports from researchers with demonstrated expertise while reducing the burden of triaging invalid submissions.
We appreciate the security community's understanding and continued collaboration in keeping Node.js secure.
```

---

## 21. Node.js 25.6.1 (Current)

- 日期: 2026-02-10 13:37
- 链接: https://nodejs.org/en/blog/release/v25.6.1

```
Node.js 25.6.1 (Current)
Antoine du Hamel
2026-02-10, Version 25.6.1 (Current), @aduh95
Notable Changes
- [
47df4328d7
] - build,deps: replacecjs-module-lexer
withmerve
(Yagiz Nizipli) #61456
Commits
- [
47df4328d7
] - build,deps: replace cjs-module-lexer with merve (Yagiz Nizipli) #61456 - [
a727054503
] - deps: upgrade npm to 11.9.0 (npm team) #61685 - [
c78c49ed6b
] - deps: update amaro to 1.1.7 (Node.js GitHub Bot) #61730 - [
4790816d9b
] - deps: update minimatch to 10.1.2 (Node.js GitHub Bot) #61732 - [
8c71740e8a
] - deps: update undici to 7.21.0 (Node.js GitHub Bot) #61683 - [
e559ef6ab1
] - deps: update googletest to 56efe3983185e3f37e43415d1afa97e3860f187f (Node.js GitHub Bot) #61605 - [
300de2bb5a
] - deps: update amaro to 1.1.6 (Node.js GitHub Bot) #61603 - [
e71e9505ef
] - dns: fix Windows SRV ECONNREFUSED by adjusting c-ares fallback detection (notvivek12) #61453 - [
439b816bc7
] - doc: clarify EventEmitter error handling in threat model (Matteo Collina) #61701 - [
c1c6641f23
] - doc: mention default option for test runner env (Steven) #61659 - [
41ec451f98
] - doc: fix --inspect security warning section (Tim Perry) #61675 - [
bb90ef2356
] - doc: documenturl.format(urlString)
as deprecated under DEP0169 (René) #61644 - [
513df82e6f
] - doc: update to Visual Studio 2026 manual install (Mike McCready) #61655 - [
9409d30736
] - doc: deprecation add more codemod (Augustin Mauroy) #61642 - [
75a7a67151
] - doc: fix grammatical error in README.md (ayj8201) #61653 - [
821e59e884
] - doc: correct tools README Boxstarter link (Mike McCready) #61638 - [
4998f539a0
] - doc: updateserver.dropMaxConnection
link (YuSheng Chen) #61584 - [
9383ac4ab7
] - http: implement slab allocation for HTTP header parsing (Mert Can Altin) #61375 - [
e90eb1d561
] - meta: persist sccache daemon until end of build workflows (René) #61639 - [
ade36ac367
] - meta: bump github/codeql-action from 4.31.9 to 4.32.0 (dependabot[bot]) #61622 - [
26638bd67f
] - meta: bump step-security/harden-runner from 2.14.0 to 2.14.1 (dependabot[bot]) #61621 - [
eaa9a96cb6
] - meta: bump actions/setup-python from 6.1.0 to 6.2.0 (dependabot[bot]) #61627 - [
fd98187828
] - meta: bump cachix/cachix-action (dependabot[bot]) #61626 - [
820c1d021c
] - meta: bump actions/setup-node from 6.1.0 to 6.2.0 (dependabot[bot]) #61625 - [
72a4136bd5
] - meta: bump actions/cache from 5.0.1 to 5.0.3 (dependabot[bot]) #61624 - [
e3ef6cb3bc
] - meta: bump peter-evans/create-pull-request from 8.0.0 to 8.1.0 (dependabot[bot]) #61623 - [
020a836202
] - meta: bump actions/stale from 10.1.0 to 10.1.1 (dependabot[bot]) #61620 - [
0df72f07c8
] - meta: bump actions/checkout from 6.0.1 to 6.0.2 (dependabot[bot]) #61619 - [
d147c08b83
] - module: do not invoke resolve hooks twice for imported cjs (Joyee Cheung) #61529 - [
a2843f8556
] - net: defer synchronous destroy calls in internalConnect (RajeshKumar11) #61658 - [
7fb7030781
] - repl: fix flaky test-repl-programmatic-history (Matteo Collina) #61614 - [
d4c9b5cf5b
] - sqlite: avoid extra copy for large text binds (Ali Hassan) #61580 - [
aa1b3661d9
] - sqlite: use DictionaryTemplate for run() result (Mert Can Altin) #61432 - [
9c8ad7e881
] - src: elide heap allocation in structured clone implementation (Anna Henningsen) #61703 - [
c4ecfef93d
] - src: use simdutf for one-byte string UTF-8 write in stringBytes (Mert Can Altin) #61696 - [
28905b9734
] - src: consolidate C++ ReadFileSync/WriteFileSync utilities (Joyee Cheung) #61662 - [
e90cec2f69
] - test: restraint version replacement pattern in snapshots (Chengzhong Wu) #61748 - [
adce20c0a1
] - test: print stack immediately avoiding GC interleaving (Chengzhong Wu) #61699 - [
7643bc8999
] - test: fix case-insensitive path matching on Windows (Matteo Collina) #61682 - [
23d1ecf66f
] - test: fix flaky test-performance-eventloopdelay (Matteo Collina) #61629 - [
99012a88ed
] - test: remove duplicate wpt tests (Filip Skokan) #61617 - [
a8b32b8ce1
] - test: fix race condition in watch mode tests (Matteo Collina) #61615 - [
086a5a5a25
] - test: update WPT for url to e3c46fdf55 (Node.js GitHub Bot) #61602 - [
f0574fd419
] - test: use the skipIfNoWatch() utility function (Luigi Pinca) #61531 - [
b064ddc221
] - test: unify assertSnapshot common patterns (Chengzhong Wu) #61590 - [
17122e521b
] - test_runner: fix test enqueue when test file has syntax error (Edy Silva) #61573 - [
bad3f02dd9
] - tools: enforce removal oflts-watch-*
labels on release proposals (Antoine du Hamel) #61672 - [
a8f33fd6bd
] - tools: use ubuntu-slim runner in meta GitHub Actions (Tierney Cyren) #61663 - [
c843e447ca
] - tools: test--shared-merve
intest-shared
workflow (Antoine du Hamel) #61649 - [
2fedc03f96
] - tools: update OpenSSL to 3.5.5 intest-shared
(Antoine du Hamel) #61551 - [
1c1db94670
] - tools,win: upgrade install additional tools to Visual Studio 2026 (Mike McCready) #61562
Windows 64-bit Installer: https://nodejs.org/dist/v25.6.1/node-v25.6.1-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v25.6.1/node-v25.6.1-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v25.6.1/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v25.6.1/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v25.6.1/node-v25.6.1.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v25.6.1/node-v25.6.1-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v25.6.1/node-v25.6.1-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v25.6.1/node-v25.6.1-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v25.6.1/node-v25.6.1-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v25.6.1/node-v25.6.1-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v25.6.1/node-v25.6.1-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v25.6.1/node-v25.6.1-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v25.6.1/node-v25.6.1.tar.gz
Other release files: https://nodejs.org/dist/v25.6.1/
Documentation: https://nodejs.org/docs/v25.6.1/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
21eacf97f520b95b8e6d774e68832c323a8118767f3c1a95a431de7169c89c2f node-v25.6.1-aix-ppc64.tar.gz
4b1d58e83a854481e87e21ce636ada04364c8b952095e545cbf91435911027a5 node-v25.6.1-arm64.msi
a80cb252d170a4730f78f5950cf19a46106f156e5886e5c1cc8c5602aea60243 node-v25.6.1-darwin-arm64.tar.gz
d5c37f04d4006741574730871148839f254f3b3940f5afd70f7d1e70970c90e3 node-v25.6.1-darwin-arm64.tar.xz
3b68f847d9d8861c7c8bfef32c540d14f6ca18bfcbf5f6495a595b9529063a9b node-v25.6.1-darwin-x64.tar.gz
7b6211bdb2a90834422f0243274ff1ca5deee309ca12a21329edcf1f775f8113 node-v25.6.1-darwin-x64.tar.xz
0fa0c1aa6dda46d9595e860635e1edcbb7d0c9f0c42da316e37f293ab90a6412 node-v25.6.1-headers.tar.gz
31c82dd9d6837b2bce85652623f6c712769dd546cdf96282a558d661af1922d3 node-v25.6.1-headers.tar.xz
90fea701897ecb424aafa2824539476598437ad9f21e649732a85cc2d955d845 node-v25.6.1-linux-arm64.tar.gz
157e76f7eee66cff1492489c94c801c48b2b0859e7f352f28b12e855ead301ff node-v25.6.1-linux-arm64.tar.xz
28bdd63dc0540d4fb1f5fbd200212d50e5cc09c40b3eb4ce2fe0c4c09f542e06 node-v25.6.1-linux-ppc64le.tar.gz
2824e6d443d0feb82d2c934c2cc364c3becf5c24be438451487aea4fd62bf158 node-v25.6.1-linux-ppc64le.tar.xz
0e819251ac30d8aaceaa0dbc3012472c8d624f14327ae7b3a184876b929c2a67 node-v25.6.1-linux-s390x.tar.gz
4f8201e701e505624f7d470586364e35d4d41ce6a3832b7c4ad192969f9234e8 node-v25.6.1-linux-s390x.tar.xz
3809fdbfd54829bad363b9db8e96ca3600509e2ff20ede74181cfc1ca8451ce3 node-v25.6.1-linux-x64.tar.gz
97eec07e2a43c5a39e4968c1ae554461783914d872c27d856e98d2751094f5be node-v25.6.1-linux-x64.tar.xz
87f13e0aba0e02e4aee57ca586da59aea1b503d5e98aa5a100eba8e4b42ee26d node-v25.6.1-win-arm64.7z
e11f610f584261617259aba8cbb8d2af6d1eb726cc0a433197572e5882d0bf77 node-v25.6.1-win-arm64.zip
76281226593d12ccbd775e9553ee259ef06cd2bece7d6daabb26eaaa5406f0ca node-v25.6.1-win-x64.7z
0ae2300cdf44c399b5b351edbefb3534d1342a6fabd64302ca8c8e2fb86b0445 node-v25.6.1-win-x64.zip
8906e19ae88fdfa2dab2e140667dfa05a70b746bd0ca4d1b849aa5c7cbb71dc9 node-v25.6.1-x64.msi
153e0e33c9b8f9945cb02f639d435388f606220fcf7beda5010b5a6aba624c67 node-v25.6.1.pkg
a72bb2b274e8ddf3c933ea7a73d5ac4fce7503e45edc9d541fc75d104fa848c3 node-v25.6.1.tar.gz
cf756781c8b4dc5ee030f87ddf9d51b8d5bf219ad56cbd9855c4a3bdc832c78e node-v25.6.1.tar.xz
1ece331f8d170fba2ea1523f6cdfec4fc95c22c0758aa6c8aaa0140918509f09 win-arm64/node.exe
47750ee99207e5b621671565852cf7385f27bf664470886b9437137342a497c9 win-arm64/node.lib
1968da8c616e14213e38c3940d3796615b2c9264bcb597be97c4007465483b3c win-arm64/node_pdb.7z
7b05ee18d9b73e3704da7d30d57dd24f4b97d3850afa02ec229673e4b67c19e4 win-arm64/node_pdb.zip
677507a667c7fc0be6162312a260eb996202f127255f72357708cdb6f412429b win-x64/node.exe
f7201b932d898bdbf78aee7add288d2263c4791f1502068ad11b6c14675c6324 win-x64/node.lib
b2ef067a44da18d3751a67e0c5299c75be0f02f5dcce46effa0c29b69cf4cf44 win-x64/node_pdb.7z
992a113f23de308552f894f0de2ae9810d2f633d021c8c199ab9c6795e0439cc win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iHUEARYIAB0WIQRb6KP2yKXAHRBsCtggsaOQsWjTVgUCaYs0AwAKCRAgsaOQsWjT
ViwdAQCRnKxMteNgIdARF/OCughVAML9+gyQNYFa02XEJAN0wwD9HDmiadFdOvV4
gmK6dSHrqxTz99irXvJZx8Z0tewW0wY=
=FpZa
-----END PGP SIGNATURE-----
```

---

## 22. Node.js 24.13.1 (LTS)

- 日期: 2026-02-10 13:37
- 链接: https://nodejs.org/en/blog/release/v24.13.1

```
Node.js 24.13.1 (LTS)
Antoine du Hamel
2026-02-10, Version 24.13.1 'Krypton' (LTS), @aduh95
Notable Changes
- [
1f64d6841e
] - build: add support for Python 3.14 (Christian Clauss) #59983 - [
30e500fc09
] - cli: mark--heapsnapshot-near-heap-limit
as stable (Joyee Cheung) #60956 - [
bc0a55f086
] - crypto: update root certificates to NSS 3.119 (Node.js GitHub Bot) #61419 - [
8a67c00bf5
] - doc: mark--build-snapshot
and--build-snapshot-config
as stable (Joyee Cheung) #60954 - [
3999c2a910
] - meta: add avivkeller to collaborators (Aviv Keller) #61115 - [
fa542fbae6
] - meta: add gurgunday to collaborators (Gürgün Dayıoğlu) #61094 - [
ff11eda2f2
] - meta: add Renegade334 to collaborators (Renegade334) #60714 - [
2e387fb969
] - url: update ada to v3.4.2 and support unicode 17 (Yagiz Nizipli) #61593 - [
bb206782d4
] - v8: markv8.queryObjects()
as stable (Joyee Cheung) #60957
Commits
- [
a73279c60d
] - assert: use a set instead of an array for faster lookup (Ruben Bridgewater) #61076 - [
6a61bcd73c
] - assert,util: fix deep comparison for sets and maps with mixed types (Ruben Bridgewater) #61388 - [
cf0eabcd42
] - assert,util: improve deep comparison performance (Ruben Bridgewater) #61076 - [
ff3b9ac183
] - benchmark: add SQLite benchmarks (Guilherme Araújo) #61401 - [
e1f7d68c94
] - benchmark: use boolean options in benchmark tests (SeokhunEom) #60129 - [
91127c91cd
] - benchmark: allow boolean option values (SeokhunEom) #60129 - [
170fda55f6
] - benchmark: add microbench on isInsideNodeModules (Chengzhong Wu) #60991 - [
3976381b41
] - benchmark: fix incorrect base64 input in byteLength benchmark (semimikoh) #60841 - [
c702fccd76
] - benchmark: use typescript for import cjs benchmark (Joyee Cheung) #60663 - [
92c517c62d
] - buffer: make methods work on Uint8Array instances (Neal Beeken) #56578 - [
be95382edb
] - buffer: let Buffer.of use heap (Сковорода Никита Андреевич) #60503 - [
1f64d6841e
] - build: test on Python 3.14 (Christian Clauss) #59983 - [
ea4687981b
] - build: update android-patches/trap-handler.h.patch (Mo Luo) #60369 - [
b3a7a8c780
] - build: update devcontainer.json to use paired nix env (Joyee Cheung) #61414 - [
7168d0b5e3
] - build: add embedtest into native suite (Joyee Cheung) #61357 - [
e00755a977
] - build: fix misplaced comma in ldflags (hqzing) #61294 - [
72fcc3ee9d
] - build: fix crate vendor file checksums on windows (Chengzhong Wu) #61329 - [
76a73d68fd
] - build: expose libplatform symbols in shared libnode (Joyee Cheung) #61144 - [
ef8d26ce5c
] - build: fix inconsistent quoting inMakefile
(Antoine du Hamel) #60511 - [
2d23968783
] - build: remove temporal updater (Chengzhong Wu) #61151 - [
4c2655f1c2
] - build: update test-wpt-report to use NODE instead of OUT_NODE (Filip Skokan) #61024 - [
eaea6821fc
] - build: skip build-ci on actions with a separate test step (Chengzhong Wu) #61073 - [
dfd4e12037
] - build: run embedtest with node_g when BUILDTYPE=Debug (Chengzhong Wu) #60850 - [
775c77234b
] - build,tools: fix addon build deadlock on errors (Vladimir Morozov) #61321 - [
5deafc10fa
] - build,win: improve logs when ClangCL is missing (Mike McCready) #61438 - [
e2481c5c6e
] - build,win: update WinGet configurations to Python 3.14 (Mike McCready) #61431 - [
d2586b7e4c
] - child_process: treat ipc length header as unsigned uint32 (Ryuhei Shima) #61344 - [
30e500fc09
] - cli: mark --heapsnapshot-near-heap-limit as stable (Joyee Cheung) #60956 - [
2c7da15612
] - cluster: fix port reuse between cluster (Ryuhei Shima) #60141 - [
bc0a55f086
] - crypto: update root certificates to NSS 3.119 (Node.js GitHub Bot) #61419 - [
2d5f20e9c3
] - crypto: update root certificates to NSS 3.117 (Node.js GitHub Bot) #60741 - [
fba95be188
] - deps: update archs files for openssl-3.5.5 (Node.js GitHub Bot) #61547 - [
08697289e0
] - deps: upgrade openssl sources to openssl-3.5.5 (Node.js GitHub Bot) #61547 - [
403c50c04d
] - deps: update corepack to 0.34.6 (Node.js GitHub Bot) #61510 - [
3b24691aeb
] - deps: upgrade npm to 11.8.0 (npm team) #61466 - [
2bba7efdc4
] - deps: update googletest to 85087857ad10bd407cd6ed2f52f7ea9752db621f (Node.js GitHub Bot) #61417 - [
8f8c6f6162
] - deps: update sqlite to 3.51.2 (Node.js GitHub Bot) #61339 - [
c46009053c
] - deps: update icu to 78.2 (Node.js GitHub Bot) #60523 - [
b46b8dd91b
] - deps: update ada to v3.4.0 (Yagiz Nizipli) #61315 - [
88c6b17e18
] - deps: update zlib to 1.3.1-e00f703 (Node.js GitHub Bot) #61135 - [
0030c05ba9
] - deps: update cjs-module-lexer to 2.2.0 (Node.js GitHub Bot) #61271 - [
77437cff89
] - deps: update nbytes to 0.1.2 (Node.js GitHub Bot) #61270 - [
fb0f05a937
] - deps: update timezone to 2025c (Node.js GitHub Bot) #61138 - [
b426a47c05
] - deps: nghttp2: revert 7784fa979d0b (Antoine du Hamel) #61136 - [
c07a38f700
] - deps: update nghttp2 to 1.68.0 (nodejs-github-bot) #61136 - [
c2ddc9a18b
] - deps: update simdjson to 4.2.4 (Node.js GitHub Bot) #61056 - [
f38cd6da8e
] - deps: update googletest to 065127f1e4b46c5f14fc73cf8d323c221f9dc68e (Node.js GitHub Bot) #61055 - [
a9a6a4cdb2
] - deps: brotli: cherry-pick e230f474b87 (liujiahui) #61003 - [
5a40023aae
] - deps: upgrade npm to 11.7.0 (npm team) #61011 - [
4121e7a413
] - deps: update sqlite to 3.51.1 (Node.js GitHub Bot) #60899 - [
e8a09fc896
] - deps: update zlib to 1.3.1-63d7e16 (Node.js GitHub Bot) #60898 - [
8df5862ee5
] - deps: upgrade npm to 11.6.4 (npm team) #60853 - [
6c1c8cbdcc
] - deps: update sqlite to 3.51.0 (Node.js GitHub Bot) #60614 - [
2d1efc7c1b
] - deps: upgrade npm to 11.6.3 (npm team) #60785 - [
3a2de1c23b
] - deps: update brotli to 1.2.0 (Node.js GitHub Bot) #60540 - [
58c5d40bd1
] - deps: update simdjson to 4.2.2 (Node.js GitHub Bot) #60740 - [
e6b607ef50
] - deps: update googletest to 1b96fa13f549387b7549cc89e1a785cf143a1a50 (Node.js GitHub Bot) #60739 - [
650c9e0305
] - deps: update minimatch to 10.1.1 (Node.js GitHub Bot) #60543 - [
ef1951d5d5
] - deps: update inspector_protocol to 1b1bcbbe060e8c8cd8704f00f78978c50991 (Node.js GitHub Bot) #60705 - [
eb068305dd
] - deps: update cjs-module-lexer to 2.1.1 (Node.js GitHub Bot) #60646 - [
ee1d99131c
] - deps: update simdjson to 4.2.1 (Node.js GitHub Bot) #60644 - [
23582967b7
] - deps: V8: cherry-pick 1441665e0d87 (Domagoj Stolfa) #60989 - [
155eaedff2
] - deps: V8: cherry-pick 394a8053b59e (Lu Yahan) #60962 - [
c95a4a0f43
] - deps: V8: backport bbaae8e36164 (Lu Yahan) #60962 - [
6f123f186d
] - doc: move Security-Team from TSC to SECURITY (Rafael Gonzaga) #61495 - [
2e3337d15b
] - doc: addedrequestOCSP
option totls.connect
(ikeyan) #61064 - [
f505f81577
] - doc: restore @ChALkeR to collaborators (Сковорода Никита Андреевич) #61553 - [
12fb95d0c9
] - doc: update IBM/Red Hat volunteers with dedicated project time (Beth Griggs) #61588 - [
283ab61ed2
] - doc: align Buffer.concat documentation with behavior (Gürgün Dayıoğlu) #60405 - [
fc9c906d5f
] - doc: removev
prefix for version references (Mike McCready) #61488 - [
4a88ed09e8
] - doc: mention constructor comparison in assert.deepStrictEqual (Hamza Kargin) #60253 - [
9b29d56491
] - doc: add CVE delay mention (Rafael Gonzaga) #61465 - [
4815e4ac52
] - doc: update previous version links in BUILDING (Mike McCready) #61457 - [
8a43244e6c
] - doc: include OpenJSF handle for security stewards (Rafael Gonzaga) #61454 - [
89a7f184a1
] - doc: clarify process.argv[1] behavior for -e/--eval (Jeevankumar S) #61366 - [
b4041aba1c
] - doc: remove Windows Dev Home instructions from BUILDING (Mike McCready) #61434 - [
fa7830bac0
] - doc: clarify TypedArray properties on Buffer (Roman Reiss) #61355 - [
45663c8956
] - doc: update Python 3.14 manual install instructions (Windows) (Mike McCready) #61428 - [
0248357f26
] - doc: note resume build should not be done on node-test-commit (Stewart X Addison) #61373 - [
b254bab513
] - doc: refine WebAssembly error documentation (sangwook) #61382 - [
8aca37c6ef
] - doc: add deprecation history for url.parse (Eng Zer Jun) #61389 - [
8047ac3aac
] - doc: add marco and rafael in last sec release (Marco Ippolito) #61383 - [
61190bf4b4
] - doc: packages: example of private import switch to internal (coderaiser) #61343 - [
346311c42f
] - doc: add esm and cjs examples to node:v8 (Alfredo González) #61328 - [
c07c80717c
] - doc: added 'secure' event to tls.TLSSocket (ikeyan) #61066 - [
9f68d30f11
] - doc: restore @watilde to collaborators (Daijiro Wachi) #61350 - [
a3b08ddb51
] - doc: run license-builder (github-actions[bot]) #61348 - [
4990812dd9
] - doc: document ALPNCallback option for TLSSocket constructor (ikeyan) #61331 - [
89e9d19693
] - doc: update MDN links (Livia Medeiros) #61062 - [
dcffa88fec
] - doc: correct description oferror.stack
accessor behavior (René) #61090 - [
31476cd4d1
] - doc: add documentation for process.traceProcessWarnings (Alireza Ebrahimkhani) #53641 - [
99c783b9ec
] - doc: add sqlite session disposal method (René) #61273 - [
c7764bed35
] - doc: fix filename typo (Hardanish Singh) #61297 - [
0f16bca9d8
] - doc: fix typos and grammar inBUILDING.md
&onboarding.md
(Hardanish Singh) #61267 - [
4b691b562d
] - doc: mention --newVersion release script (Rafael Gonzaga) #61255 - [
32e56ab71f
] - doc: correct typo in api contributing doc (Mike McCready) #61260 - [
9ebf1ffbeb
] - doc: add PR-URL requirement for security backports (Rafael Gonzaga) #61256 - [
940f83d95d
] - doc: add reusePort error behavior to net module (mag123c) #61250 - [
8881859ee0
] - doc: note corepack package removal in distribution doc (Mike McCready) #61207 - [
03a1540cd1
] - doc: fix tls.connect() timeout documentation (Azad Gupta) #61079 - [
816ce7530d
] - doc: missingpassed
,error
andpassed
properties onTestContext
(Xavier Stouder) #61185 - [
d825c8858a
] - doc: clarify threat model for application-level API exposure (Rafael Gonzaga) #61184 - [
a3dd30d0e0
] - doc: correct options for net.Socket class and socket.connect (Xavier Stouder) #61179 - [
c3e776becd
] - doc: document error event on readline InterfaceConstructor (Xavier Stouder) #61170 - [
05a6372d30
] - doc: add a smooth scrolling effect to the sidebar (btea) #59007 - [
76a7eb09ef
] - doc: fix test settime docs (Efe) #61117 - [
bcbbde6ccc
] - doc: correct invalid collaborator profile (JJ) #61091 - [
084741d09d
] - doc: add a tip about developer mode on Windows (Joyee Cheung) #61112 - [
ed4de371d3
] - doc: exclude compile-time flag features from security policy (Matteo Collina) #61109 - [
3999c2a910
] - doc: add @avivkeller to collaborators (Aviv Keller) #61115 - [
f3ec066f1a
] - doc: warn about short GCM tags visibly (Tobias Nießen) #61082 - [
fa542fbae6
] - doc: add gurgunday to collaborators (Gürgün Dayıoğlu) #61094 - [
49f36722dc
] - doc: mark sync module hooks as release candidate (Joyee Cheung) #60960 - [
a0adc6afd2
] - doc: reorganize docs of module customization hooks (Joyee Cheung) #60960 - [
a4097ca048
] - doc: mark crypto.hash as stable (Joyee Cheung) #60994 - [
8a67c00bf5
] - doc: mark --build-snapshot and --build-snapshot-config as stable (Joyee Cheung) #60954 - [
0c83169c35
] - doc: add File modes cross-references in fs methods (Mohit Raj Saxena) #60286 - [
dae815262a
] - doc: add missingzstd
to mjs example of zlib (Deokjin Kim) #60915 - [
28b284880e
] - doc: clarify fileURLToPath security considerations (Rafael Gonzaga) #60887 - [
6c440af39b
] - doc: show the use of string expressions in the SQLTagStore example (schliepa) #60873 - [
4c5b62209c
] - doc: replace column with columnNumber in example ofutil.getCallSites
(Deokjin Kim) #60881 - [
8875c9148e
] - doc: correct spelling in BUILDING.md (Rich Trott) #60875 - [
d6cb762426
] - doc: update debuglog examples to use 'foo-bar' instead of 'foo' (xiaoyao) #60867 - [
9eae518796
] - doc: correct 'event handle' to 'event handler' in Utf8Stream drop event (Riddhi) #60692 - [
c3c3ed27c1
] - doc: fix typos in changelogs (Rich Trott) #60855 - [
1b975e3017
] - doc: mark module.register as active development (Chengzhong Wu) #60849 - [
6a6fc0c851
] - doc: add fullName property to SuiteContext (PaulyBearCoding) #60762 - [
8347d734e6
] - doc: add additional codemods for deprecation (Augustin Mauroy) #60811 - [
7cc87037c3
] - doc: keep sidebar module visible when navigating docs (Botato) #60410 - [
1c6618f643
] - doc: correct concurrency wording in test() documentation (Azad Gupta) #60773 - [
488208004e
] - doc: clarify that CQ only picks up PRs targetingmain
(René) #60731 - [
34517940c2
] - doc: clarify license section and add contributor note (KaleruMadhu) #60590 - [
f080721df4
] - doc: correct and expand documentation for SQLTagStore (René) #60200 - [
be3d26709d
] - doc: correct tls ALPNProtocols types (René) #60143 - [
ef82c53131
] - doc: remove mention of SMS 2FA (Antoine du Hamel) #60707 - [
11b190f63e
] - doc: add info about renamed flag incli.md
(Antoine du Hamel) #60690 - [
59db9bc654
] - doc: fix incorrect slh-dsa oids in crypto.md (Artsiom Malakhau) #60681 - [
ad52750cf6
] - doc:domain.add()
does not accept timer objects (René) #60675 - [
2592d94e29
] - doc: fix v24 changelog after security release (Marco Ippolito) #61371 - [
e0f4ad0af0
] - doc,test: add documentation and test on how to use addons in SEA (Joyee Cheung) #59582 - [
13af640d94
] - esm: ensure watch mode restarts after syntax errors (Xavier Stouder) #61232 - [
31afe95d15
] - esm: avoid throw when module specifier is not url (Craig Macomber (Microsoft)) #61000 - [
311a04cf2d
] - esm: improve error messages for ambiguous module syntax (mag123c) #60376 - [
cacef92937
] - events: remove redundant todo (Gürgün Dayıoğlu) #60595 - [
42e1f72561
] - events: remove eventtarget custom inspect branding (Efe) #61128 - [
fd8b61369b
] - fs: remove duplicate getValidatedPath calls (Mert Can Altin) #61359 - [
9bb9fc7f2c
] - fs: fix errorOnExist behavior for directory copy in fs.cp (Nicholas Paun) #60946 - [
55a3c70780
] - fs: fix ENOTDIR in globSync when file is treated as dir (sangwook) #61259 - [
073a145095
] - fs: remove duplicate fd validation in sync functions (Mert Can Altin) #61361 - [
b132ecdf60
] - fs: validate statfs path (Efe) #61230 - [
0ed0a30f74
] - fs: fix rmSync to handle non-ASCII characters (Yeaseen) #61108 - [
99632b1a3b
] - fs: remove broken symlinks in rmSync (sangwook) #61040 - [
9cb6757a67
] - fs: detect dot files when using globstar (Robin van Wijngaarden) #61012 - [
e22aad19e0
] - gyp: aix: change gcc version detection so CXX="ccache g++" works (Stewart X Addison) #61464 - [
59d94ba7e7
] - http: fix rawHeaders exceeding maxHeadersCount limit (Max Harari) #61285 - [
ae6a1fd40a
] - http,https: fix double ERR_PROXY_TUNNEL emission (Shima Ryuhei) #60699 - [
53bfbaa4b1
] - http2: validate initialWindowSize per HTTP/2 spec (Matteo Collina) #61402 - [
14b421b677
] - http2,zlib: prefercall()
overapply()
if argument list is not array (Livia Medeiros) #60834 - [
32b03d0604
] - (CVE-2025-59465) lib: add TLSSocket default error handler (RafaelGSS) nodejs-private/node-private#750 - [
4ef7a6c77e
] - lib: backport_tls_common
and_tls_wrap
refactors (Dario Piotrowicz) #57643 - [
820e0a5cfa
] - lib: fix typo inutil.js
comment (Taejin Kim) #61365 - [
8de391e1cb
] - lib: fix TypeScript support check in jitless mode (sangwook) #61382 - [
f22f622b3e
] - lib: add lint rules for reflective function calls (Michaël Zasso) #60825 - [
603f0bf8e1
] - lib: implement all 1-byte encodings in js (Сковорода Никита Андреевич) #61093 - [
1c0a1aa5ef
] - lib: gbk decoder is gb18030 decoder per spec (Сковорода Никита Андреевич) #61099 - [
2cf963df73
] - lib: enforce use ofURLParse
(Antoine du Hamel) #61016 - [
bb90630470
] - lib: useFastBuffer
for empty buffer allocation (Gürgün Dayıoğlu) #60558 - [
10893a6f13
] - lib: refactor JWK import PQC support check (Filip Skokan) #60586 - [
d43806291f
] - lib,src: isInsideNodeModules should test on the first non-internal frame (Chengzhong Wu) #60991 - [
0bb8f5fe03
] - lib,src,test: fix tests without SQLite (Antoine du Hamel) #60906 - [
f3fe0e7fc2
] - lib,test: enforce use ofassert.fail
via a lint rule (Antoine du Hamel) #61004 - [
8b783d46ef
] - meta: do not fast-track npm updates (Antoine du Hamel) #61475 - [
de4a11b50e
] - meta: fix typos in issue template config (Daijiro Wachi) #61399 - [
97b1492783
] - meta: label v8 module PRs (René) #61325 - [
9bf899b743
] - meta: bump step-security/harden-runner from 2.13.2 to 2.14.0 (dependabot[bot]) #61245 - [
4df7134324
] - meta: bump actions/setup-node from 6.0.0 to 6.1.0 (dependabot[bot]) #61244 - [
ff98f610d8
] - meta: bump actions/cache from 4.3.0 to 5.0.1 (dependabot[bot]) #61243 - [
86950a41ab
] - meta: bump github/codeql-action from 4.31.6 to 4.31.9 (dependabot[bot]) #61241 - [
96901b4828
] - meta: bump codecov/codecov-action from 5.5.1 to 5.5.2 (dependabot[bot]) #61240 - [
c90fc7c0d3
] - meta: bump peter-evans/create-pull-request from 7.0.9 to 8.0.0 (dependabot[bot]) #61237 - [
f130d4b6de
] - meta: move lukekarrys to emeritus (Node.js GitHub Bot) #60985 - [
416f34ccfc
] - meta: bump actions/setup-python from 6.0.0 to 6.1.0 (dependabot[bot]) #60927 - [
2239939305
] - meta: bump github/codeql-action from 4.31.3 to 4.31.6 (dependabot[bot]) #60926 - [
7f146b6a97
] - meta: bump peter-evans/create-pull-request from 7.0.8 to 7.0.9 (dependabot[bot]) #60924 - [
d9020f0089
] - meta: bump github/codeql-action from 4.31.2 to 4.31.3 (dependabot[bot]) #60770 - [
4bba259d3b
] - meta: bump step-security/harden-runner from 2.13.1 to 2.13.2 (dependabot[bot]) #60769 - [
ff11eda2f2
] - meta: add Renegade334 to collaborators (Renegade334) #60714 - [
e3b5593c0f
] - module: fix sync resolve hooks for require with node: prefixes (Joyee Cheung) #61088 - [
edec5be805
] - module: preserve URL in the parent created by createRequire() (Joyee Cheung) #60974 - [
5cc3596eb4
] - node-api: fix node_api_create_object_with_properties name (Vladimir Morozov) #61319 - [
179162fe42
] - node-api: use Node-API in comments (Vladimir Morozov) #61320 - [
b3fe457a89
] - node-api: add napi_set_prototype (siaeyy) #60711 - [
1e13e84f16
] - node-api: fix data race and use-after-free in napi_threadsafe_function (Mika Fischer) #55877 - [
36ce6d636d
] - node-api: add support for Float16Array (Ilyas Shabi) #58879 - [
95e6659e2b
] - node-api: support SharedArrayBuffer in napi_create_dataview (Kevin Eady) #60473 - [
54f58e2fb2
] - os: freeze signals constant (Xavier Stouder) #61038 - [
31489310f8
] - process: improve process.cwd() error message (TseIan) #61164 - [
f7450a90ed
] - repl: move completion logic to internal module (Dario Piotrowicz) #59889 - [
27117625df
] - sqlite: add some tests (Guilherme Araújo) #61410 - [
d56066ce8c
] - sqlite: improve error messages for tag store (Pramit Sharma) #61096 - [
9d993be6c1
] - sqlite: makeSQLTagStore.prototype.size
a getter (René) #60246 - [
ceaa200d16
] - src: improve StringBytes::Encode perf on UTF8 (Сковорода Никита Андреевич) #61131 - [
034a5f2346
] - src: add missing override specifier to Clean() (Tobias Nießen) #61429 - [
977f46cc20
] - src: cache context lookup in vectored io loops (Mert Can Altin) #61387 - [
bb9e4e0784
] - src: cache missing package.json files in the C++ package config cache (Michael Smith) #60425 - [
c1aa9f49cd
] - src: use starts_with instead of rfind/find (Tobias Nießen) #61426 - [
d3676d0a82
] - src: use C++ nullptr in sqlite (Tobias Nießen) #61416 - [
001be8aa7c
] - src: use C++ nullptr in webstorage (Tobias Nießen) #61407 - [
4f832b1e3d
] - src: fix pointer alignment (jhofstee) #61336 - [
a0a8c96fd1
] - src: dump snapshot source with node:generate_default_snapshot_source (Joyee Cheung) #61101 - [
b6d3caeda8
] - src: improve StringBytes::Encode perf on ASCII (Сковорода Никита Андреевич) #61119 - [
9c80e5ac87
] - src: add HandleScope to edge loop in heap_utils (Mert Can Altin) #60885 - [
09ccd94312
] - src: remove redundant CHECK (Tobias Nießen) #61130 - [
6008354b8a
] - src: remove unused private field inSQLTagStore
(Michaël Zasso) #61027 - [
7484a34a7d
] - src: implement Windows-1252 encoding support and update related tests (Mert Can Altin) #60893 - [
47851db855
] - src: fix off-thread cert loading in bundled cert mode (Joyee Cheung) #60764 - [
4702a8696b
] - src: handle DER decoding errors from system certificates (Joyee Cheung) #60787 - [
19a4926965
] - src: use static_cast instead of C-style cast (Michaël Zasso) #60868 - [
6529334dec
] - src: add test flag to config file (Marco Ippolito) #60798 - [
d153b30773
] - src: split inspector protocol domains files (Chengzhong Wu) #60754 - [
7191b847c6
] - src,permission: fix permission.has on empty param (Rafael Gonzaga) #60674 - [
a188b954bb
] - src,permission: add debug log on is_tree_granted (Rafael Gonzaga) #60668 - [
b483b5a8ea
] - stream: export namespace object from internal end-of-stream module (René) #61455 - [
0472104536
] - stream: fix isErrored/isWritable for WritableStreams (René) #60905 - [
dd13f1046f
] - test: skip --build-sea tests on platforms where SEA is flaky (Joyee Cheung) #61504 - [
6c18bf26f4
] - test: update WPT for url to 81a2aed262 (Node.js GitHub Bot) #61509 - [
f511c24d6b
] - test: fix flaky debugger test (Ryuhei Shima) #58324 - [
41710ba953
] - test: ensure removeListener event fires for once() listeners (sangwook) #60137 - [
0035f3fa0f
] - test: delay writing the files only on macOS (Luigi Pinca) #61532 - [
99c29eb261
] - test: add implicit test for fs dispose handling with using (Ilyas Shabi) #61140 - [
e349d34c8a
] - test: check new WebCryptoAPI enum values (Filip Skokan) #61406 - [
e75617d25f
] - test: split test-esm-loader-hooks (Joyee Cheung) #61374 - [
42110af62a
] - test: aix: mark test-emit-on-destroyed as flaky (Stewart X Addison) #61381 - [
180fdbf188
] - test: update url web-platform tests (Yagiz Nizipli) #61315 - [
4bac4ecd9d
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60761 - [
39ca74e57e
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60759 - [
7327b04875
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60726 - [
fd6601c710
] - test: asserts that import.meta.resolve invokes sync loader hooks (Chengzhong Wu) #61158 - [
da4d4d4fde
] - test: check util.parseArgs argv parsing with actual process execution (René) #61089 - [
368b32d410
] - test: update WPT for urlpattern to a2e15ad405 (Node.js GitHub Bot) #61134 - [
e880062de8
] - test: make buffer sizes 32bit-aware in test-internal-util-construct-sab (René) #61026 - [
f2706e1166
] - test: remove unneccessary repl magic_mode tests (Dario Piotrowicz) #61053 - [
327dd25f86
] - test: skip sea tests on riscv64 (Stewart X Addison) #61111 - [
6da34027e2
] - test: simplifytest-cli-node-options-docs
(Antoine du Hamel) #61006 - [
74df70d1da
] - test: mark stringbytes-external-max flaky on AIX (Stewart X Addison) #60995 - [
5513338446
] - test: update test426 fixtures (Rich Trott) #60982 - [
9f594f53a7
] - test: update WPT for urlpattern to aed1f3d244 (Node.js GitHub Bot) #60642 - [
18e3b91bf1
] - test: deflaketest-repl-paste-big-data
(Livia Medeiros) #60975 - [
28ecdc5c98
] - test: skip SEA inspect test if inspector is not available (Livia Medeiros) #60872 - [
24a50b31e0
] - test: update WPT for WebCryptoAPI to 1e4933113d (Node.js GitHub Bot) #60896 - [
78ad2f4dad
] - test: lint moreassert(regexp.test(...))
cases (René) #60878 - [
280d567e1c
] - test: useassert.match
for non-literal regexp tests (René) #60879 - [
74b14258cb
] - test: fix embedtest in debug windows (Vladimir Morozov) #60806 - [
163c17de51
] - test: skip failing tests when compiled without amaro (Yuki Okita) #60815 - [
5763a304d2
] - test: fix debug test crashes caused by sea tests (Vladimir Morozov) #60807 - [
1fb83e240d
] - test: add lint rule to forbid use ofassert.ok(/regex/.test(…))
(Antoine du Hamel) #60832 - [
8c97827913
] - test: replace deprecated regex test assertions in http trailers test (Aditya Chopra) #60831 - [
a88bffeedc
] - test: prefer major GC in cppgc-object teardown (sangwook) #60672 - [
2e2963f3ed
] - test: ensure assertions are reached on HTTP2 tests (Antoine du Hamel) #60730 - [
9b748942ec
] - test: ensure assertions are reached on HTTP tests (Antoine du Hamel) #60729 - [
37947e0adf
] - test: skip test that cause timeout on IBM i (SRAVANI GUNDEPALLI) #60700 - [
357825979e
] - test: add missing r.close() calls in REPL multiline tests (sangwook) #60226 - [
ccecbd9f80
] - test: update WPT for WebCryptoAPI to c58b6f4e0e (Node.js GitHub Bot) #60702 - [
63a2400c64
] - test: limit the concurrency of WPTRunner for RISC-V (Levi Zim) #60591 - [
ec40989dfb
] - test: fix test-strace-openat-openssl for RISC-V (Levi Zim) #60588 - [
b09129df18
] - test: split test-runner-run-watch.mjs (Joyee Cheung) #60653 - [
0f05221aec
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60641 - [
078cfa2cd6
] - test_runner: fix memory leaks in runner (Abhishek Kv. Savani) #60860 - [
73146e9c50
] - test_runner: fix coverage report when a directory is named file (Heath Dutton🕴️) #61169 - [
8fc61e45e2
] - test_runner: print info when test restarts (Xavier Stouder) #61160 - [
9382be5b16
] - test_runner: fix rerun ambiguous test failures (Moshe Atlow) #61392 - [
ce417b14c0
] - test_runner: nix dead reporter code (Vas Sudanagunta) #59700 - [
ce79c72829
] - test_runner: fix lazytest.assert
accessor (René) #61097 - [
9a25541bd2
] - test_runner: propagate V8 options to child process (Pietro Marchini) #60999 - [
d61b0584ca
] - test_runner: fix line feed escaping in JUnit (Aliaksandr) #60274 - [
fc98343591
] - test_runner: simplify code and make it more consistent (Antoine du Hamel) #60777 - [
36e29bf400
] - (CVE-2026-21637) tls: route callback exceptions through error handlers (Matteo Collina) nodejs-private/node-private#782 - [
bc610a825d
] - tools: update gyp-next to 0.21.1 (Node.js GitHub Bot) #61528 - [
c335462a6a
] - tools: validate release commit diff as part oflint-release-proposal
(Antoine du Hamel) #61440 - [
0e53c48ab6
] - tools: fix vcbuild lint-js-build (Vladimir Morozov) #61318 - [
f989fdc469
] - tools: bump the eslint group in /tools/eslint with 2 updates (dependabot[bot]) #61246 - [
f104719490
] - tools: only report commit validation failure on Slack (Antoine du Hamel) #61124 - [
0267293e79
] - tools: use sparse-checkout in linter jobs (Antoine du Hamel) #61123 - [
2c861d4bd4
] - tools: simplifynotify-on-push
(Antoine du Hamel) #61050 - [
678f2caa71
] - tools: fix update-nghttp2 signature verification (Richard Lau) #61035 - [
2ef5be0570
] - tools: improve log output ofcreate-release-proposal
(Antoine du Hamel) #61028 - [
cd5c76cffe
] - tools: fixvcbuild test
when path contain spaces (stduhpf) #56481 - [
da6cb8e1d2
] - tools: do not runtest-linux
workflow for changes onvcbuild.bat
(Antoine du Hamel) #60979 - [
49f7a8c07a
] - tools: bump mdast-util-to-hast from 13.2.0 to 13.2.1 in /tools/doc (dependabot[bot]) #60930 - [
4f12d38359
] - tools: replace deprecated eslint-plugin-markdown (Michaël Zasso) #60908 - [
78aef6c098
] - tools: remove deprecated ESLint plugins (Michaël Zasso) #60908 - [
de57704198
] - tools: update ESLint dependencies (Michaël Zasso) #60908 - [
fd155c9764
] - tools: disable some new cpplint rules before update (Michaël Zasso) #60901 - [
f7f987305b
] - tools: don't fetch V8 deps in the source tree (Richard Lau) #60883 - [
f7a7e363f9
] - tools: add temporal updater (Chengzhong Wu) #60828 - [
a7bb9746ba
] - tools: dump config.gypi as json (Chengzhong Wu) #60794 - [
23792b1334
] - tools: bump js-yaml from 4.1.0 to 4.1.1 in /tools/lint-md (dependabot[bot]) #60781 - [
5b75fec005
] - tools: bump js-yaml from 4.1.0 to 4.1.1 in /tools/doc in the doc group (dependabot[bot]) #60766 - [
a8cf03323b
] - tools: update install_tools.bat old echo from 2019 to 2022 (David Hidalgo) #60736 - [
1e9281e147
] - tools: remove unsupportedcooldown
from Dependabot config (Antoine du Hamel) #60747 - [
497184baff
] - tools: update sccache to v0.12.0 (Michaël Zasso) #60723 - [
0a33189050
] - tools: update gyp-next to 0.21.0 (Node.js GitHub Bot) #60645 - [
d2c8dd29cc
] - tools,doc: fix format-md files list (Stefan Stojanovic) #61147 - [
0ca4fac44a
] - typings: add typing for string_decoder (Taejin Kim) #61368 - [
2e387fb969
] - url: update ada to v3.4.2 and support unicode 17 (Yagiz Nizipli) #61593 - [
d65326c4e6
] - url: add fast path to getPathFromURL decoder (Gürgün Dayıoğlu) #60749 - [
77f72e0bfc
] - url: remove array.reduce usage (Gürgün Dayıoğlu) #60748 - [
bfee9d0187
] - util: optimize toASCIILower function using V8s native toLowerCase (Mert Can Altin) #61107 - [
6acc9d75ec
] - util: limitinspect
to only show own properties (Ruben Bridgewater) #61032 - [
bb6e680eb1
] - util: fix parseArgs skipping positional arg with --eval and --print (azadgupta1) #60814 - [
b97081a7ba
] - util: assert getCallSites does not invoke Error.prepareStackTrace (Chengzhong Wu) #60922 - [
722094ca3a
] - util: safely inspect getter errors whose message throws (Yves M.) #60684 - [
746206b6ee
] - v8: add GCProfiler support for erm (Ilyas Shabi) #61191 - [
bb206782d4
] - v8: mark v8.queryObjects() as stable (Joyee Cheung) #60957 - [
e0ff861a8e
] - worker: update code examples fornode:worker_threads
module (fisker Cheung) #58264 - [
06be1db72c
] - worker: remove not implemented declarations (Artur Gawlik) #60655 - [
c9b0dc60ec
] - zlib: validate write_result array length (Ryuhei Shima) #61342 - [
ba318c5d44
] - zlib: add CHECK to validate fast path input (Matteo Collina) #61175
Windows 64-bit Installer: https://nodejs.org/dist/v24.13.1/node-v24.13.1-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v24.13.1/node-v24.13.1-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v24.13.1/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v24.13.1/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v24.13.1/node-v24.13.1.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v24.13.1/node-v24.13.1-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v24.13.1/node-v24.13.1-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v24.13.1/node-v24.13.1-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v24.13.1/node-v24.13.1-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v24.13.1/node-v24.13.1-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v24.13.1/node-v24.13.1-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v24.13.1/node-v24.13.1-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v24.13.1/node-v24.13.1.tar.gz
Other release files: https://nodejs.org/dist/v24.13.1/
Documentation: https://nodejs.org/docs/v24.13.1/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
8ae06649ee9da6d9eadbd2a1a0b091c3b93c78c91b6a6ec89909993ab5bae2ae node-v24.13.1-aix-ppc64.tar.gz
0b1d9dead92e68d05011d14bb31c113336e9090315f2b7027e04444bacc693fd node-v24.13.1-arm64.msi
8c039d59f2fec6195e4281ad5b0d02b9a940897b4df7b849c6fb48be6787bba6 node-v24.13.1-darwin-arm64.tar.gz
d82a321541d65109c696505135be3b7dd46e3358f0f04d664f50f0d1e1ccb8a6 node-v24.13.1-darwin-arm64.tar.xz
527f0578d9812e7dfa225121bda0b1546a6a0e4b5f556295fc8299c272de5fbf node-v24.13.1-darwin-x64.tar.gz
013a8f786a022ad1729cf435e3675e097a77d5a42eaf139a2d5d1d5309a027d4 node-v24.13.1-darwin-x64.tar.xz
0e0073cb62a38c0d41c08df0311a60b755c68edcd4e4dbb04b0a3bbe0083e186 node-v24.13.1-headers.tar.gz
59f1e5011268052f75eba3fac375e9a3b2ea6710301677528e5453090d85e8b8 node-v24.13.1-headers.tar.xz
4873459d7c9b28feaa1f0fade9bb9c81cb702670991ff80a51d805325c5e3456 node-v24.13.1-linux-arm64.tar.gz
c827d3d301e2eed1a51f36d0116b71b9e3d9e3b728f081615270ea40faac34c1 node-v24.13.1-linux-arm64.tar.xz
da86a0a04b622cabc0c9de83616ea937c1d8a05a8eaff88955bdc1c7e0eced1d node-v24.13.1-linux-ppc64le.tar.gz
fb712a08d317655dbf776c90f60ac2105109d802e33811df6c9ed33d12f801c6 node-v24.13.1-linux-ppc64le.tar.xz
d45e5e337a8d37b557d75bfaa4f854f32588c2acf975ff7c39e4fd93ae21d630 node-v24.13.1-linux-s390x.tar.gz
8e2c0d9b5545c3db22623e8cb8d6f0c28fcd470f29d32dbeabf9432dda289de2 node-v24.13.1-linux-s390x.tar.xz
7ad28fb172a9ab0593f86c1a39e5c268d0d8fc3d6cb0167f455b5655a7a6e2fd node-v24.13.1-linux-x64.tar.gz
30215f90ea3cd04dfbc06e762c021393fa173a1d392974298bbc871a8e461089 node-v24.13.1-linux-x64.tar.xz
ddab0c1e3878034f047797d11f259052a995cc1b18397055e08d522da823e806 node-v24.13.1-win-arm64.7z
0cd29eeb64f3c649db2c4c868779ca277f5a4c49e26c69e5928d01fe0ae06da8 node-v24.13.1-win-arm64.zip
cd182025ae2f7c8143541677df0aa3721a5aa248b11a95ee713cf9158299b9d9 node-v24.13.1-win-x64.7z
fba577c4bb87df04d54dd87bbdaa5a2272f1f99a2acbf9152e1a91b8b5f0b279 node-v24.13.1-win-x64.zip
03fe815e236ad8fb6fa4289921a746e1492571acee49105154f2cc0b07021515 node-v24.13.1-x64.msi
8760ca4ba16ed660ce8ff634d23e56ff887eed3e408df5f31c60fddb69aa45ec node-v24.13.1.pkg
16f241ebb9429d76936021a51d477d1ed7310ffbff71753c65c4b8805210d3ae node-v24.13.1.tar.gz
b227bc868fb5e9ec8670620e2b25530eb12c17d43e6c7bc51bb38a660684192d node-v24.13.1.tar.xz
303124c8c13d0f90492c247d76b6275a8f6bba6c1ad83443d4b6d14fef58edaf win-arm64/node.exe
5388c2e591e3469856cfc3cf0d538fc6d9bcf895a8452b316f9c592aab11f048 win-arm64/node.lib
e769755e4495d300bf9cf94c950c4b9a562a8aa87d322fb093bdd892ac0822af win-arm64/node_pdb.7z
f00e9641e8809f636e24f5de79d9b70db2354a50dcab54ba84ad9fd79279ad6c win-arm64/node_pdb.zip
e3be0545990c90995d7bf3a7af5d64af1f2e0fc1bbd9b79c27f7abc1e9676e50 win-x64/node.exe
437cc33eb3f9ad8b90737dd930b7344dd88481ab803ffe9818dbe3973e49341f win-x64/node.lib
7db7f82190bef75c3b12e60299f8214da62e6567f423c1b8b749a332e7f0e99b win-x64/node_pdb.7z
ac832bdb279adb8451c7619dc88b3cceb137d48c3edd5657756d653fbf966bb2 win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iHUEARYIAB0WIQRb6KP2yKXAHRBsCtggsaOQsWjTVgUCaYszxgAKCRAgsaOQsWjT
VjCDAP4jWJH0ZT+BZryLNqPf+kFcLrC47hqPSDaWAi+M7/znUgEA85cNqoDgXfbn
aUNrL6zfP6jKPKz6+FSZc131R06V8wg=
=1xXm
-----END PGP SIGNATURE-----
```

---

## 23. Node.js 25.6.0 (Current)

- 日期: 2026-02-03 11:42
- 链接: https://nodejs.org/en/blog/release/v25.6.0

```
Node.js 25.6.0 (Current)
Antoine du Hamel
2026-02-03, Version 25.6.0 (Current), @aduh95
Notable Changes
- [
796ff46ae6
] - (SEMVER-MINOR) async_hooks: addtrackPromises
option tocreateHook()
(Joyee Cheung) #61415 - [
4cf94fae17
] - (SEMVER-MINOR) net: addsetTOS
andgetTOS
toSocket
(Amol Yadav) #61503 - [
dce657071e
] - (SEMVER-MINOR) src: add initial support for ESM in embedder API (Joyee Cheung) #61548 - [
e62608bbcf
] - src: improveTextEncoder
encode performance withsimdutf
(Mert Can Altin) #61496 - [
93938a4738
] - (SEMVER-MINOR) stream: addbytes()
method tonode:stream/consumers
(wantaek) #60426 - [
5fe2582329
] - (SEMVER-MINOR) test_runner: addenv
option torun
function (Ethan Arrowood) #61367 - [
a181d0c43d
] - url: update Ada to v3.4.2 and support Unicode 17 (Yagiz Nizipli) #61593
Commits
- [
9c8d1b0278
] - assert: fix loose deepEqual arrays with undefined and null failing (Ruben Bridgewater) #61587 - [
796ff46ae6
] - (SEMVER-MINOR) async_hooks: add trackPromises option to createHook() (Joyee Cheung) #61415 - [
d23ee89693
] - benchmark: add streaming TextDecoder benchmark (Сковорода Никита Андреевич) #61549 - [
8759db9d21
] - buffer: disallow ArrayBuffer transfer on pooled buffer (Chengzhong Wu) #61372 - [
b2fb82946b
] - build: add--shared-lief
configure flag (Antoine du Hamel) #61536 - [
0ef99de9da
] - build: aix: deoptimize implementation-visitor.cc with --shared (Stewart X Addison) #61550 - [
8f2083e73a
] - build: enable -DV8_ENABLE_CHECKS flag (Ryuhei Shima) #61327 - [
150910da70
] - build,test: add tests for binary linked with shared libnode (Joyee Cheung) #61463 - [
fb7868ba98
] - build,win: fix vs2022 compilation (Stefan Stojanovic) #61530 - [
2c39a9234c
] - deps: update undici to 7.19.2 (Node.js GitHub Bot) #61566 - [
2a74379367
] - deps: update archs files for openssl-3.5.5 (Node.js GitHub Bot) #61547 - [
9e26a15c29
] - deps: upgrade openssl sources to openssl-3.5.5 (Node.js GitHub Bot) #61547 - [
f16b532e97
] - deps: update corepack to 0.34.6 (Node.js GitHub Bot) #61510 - [
780e65c5c5
] - deps: V8: cherry-pick c5ff7c4d6cde (Chengzhong Wu) #61372 - [
2eb8e9d760
] - deps: update nghttp3 to 1.15.0 (Node.js GitHub Bot) #61512 - [
a999edd8fd
] - deps: update ngtcp2 to 1.20.0 (Node.js GitHub Bot) #61511 - [
eedd3bb6b6
] - deps: update undici to 7.19.1 (Node.js GitHub Bot) #61514 - [
7d2bd59984
] - deps: update undici to 7.19.0 (Node.js GitHub Bot) #61470 - [
3ad4d9b11b
] - doc: align Buffer.concat documentation with behavior (Gürgün Dayıoğlu) #60405 - [
7e3eab5963
] - doc: fix node-config-schema (Сковорода Никита Андреевич) #61596 - [
cbcfaf9a35
] - doc: update IBM/Red Hat volunteers with dedicated project time (Beth Griggs) #61588 - [
3d68811d1a
] - doc: regeneratenode.1
usingdoc-kit
(Aviv Keller) #61535 - [
71702c581a
] - doc: restore @ChALkeR to collaborators (Сковорода Никита Андреевич) #61553 - [
0ceb8cad59
] - doc: addedrequestOCSP
option totls.connect
(ikeyan) #61064 - [
da93e2178c
] - doc: move Security-Team from TSC to SECURITY (Rafael Gonzaga) #61495 - [
4bea821b4c
] - lib: use utf8 fast path for streaming TextDecoder (Сковорода Никита Андреевич) #61549 - [
f05bad91d8
] - lib: recycle queues (Robert Nagy) #61461 - [
44b1927938
] - lib: use StringPrototypeStartsWith from primordials in locks (Taejin Kim) #61492 - [
a78259828a
] - lib: unify ICU and no-ICU TextDecoder (Сковорода Никита Андреевич) #61409 - [
a28ddd4594
] - module: do not wrap module._load when tracing is not enabled (Joyee Cheung) #61479 - [
4cf94fae17
] - (SEMVER-MINOR) net: addsetTOS
andgetTOS
toSocket
(Amol Yadav) #61503 - [
b861451d57
] - process: do not truncate long strings in--print
(Mohamed Akram) #61497 - [
4a2e184753
] - sea: print error information when fs operations fail (Joyee Cheung) #61581 - [
45d25c47da
] - sqlite: change approach to fix segfault SQLTagStore (Bart Louwers) #60462 - [
6993386320
] - sqlite: reserve vectors space (Guilherme Araújo) #61540 - [
dce657071e
] - (SEMVER-MINOR) src: add initial support for ESM in embedder API (Joyee Cheung) #61548 - [
e62608bbcf
] - src: improve textEncoder encode performance with simdutf (Mert Can Altin) #61496 - [
0fce52d22c
] - src: expose help texts into node-config-schema.json (Pietro Marchini) #58680 - [
be644e2569
] - src: throw RangeError on failed ArrayBuffer BackingStore allocation (Chengzhong Wu) #61480 - [
93938a4738
] - (SEMVER-MINOR) stream: add bytes() method to stream/consumers (wantaek) #60426 - [
83b2bf8ea2
] - test: split test-fs-watch-ignore-* (Luigi Pinca) #61494 - [
4726627443
] - test: aix: unflake test_threadsafe_function/test flaky on AIX (Stewart X Addison) #61560 - [
6fbb0b7572
] - test: delay writing the files only on macOS (Luigi Pinca) #61532 - [
0a952b88bb
] - test: ensure removeListener event fires for once() listeners (sangwook) #60137 - [
945b141c5d
] - test: fix flaky debugger test (Ryuhei Shima) #58324 - [
256fc6770b
] - test: update WPT for url to 81a2aed262 (Node.js GitHub Bot) #61509 - [
7725c8d596
] - test: skip --build-sea tests on platforms where SEA is flaky (Joyee Cheung) #61504 - [
915d105ffd
] - test_runner: update node-config-schema (Pietro Marchini) #58680 - [
fd8be14b33
] - test_runner: fix passingexpectFailure
(Moshe Atlow) #61568 - [
c0dd9826bd
] - test_runner: differentiate todo and failure styles (Moshe Atlow) #61564 - [
5fe2582329
] - (SEMVER-MINOR) test_runner: add env option to run function (Ethan Arrowood) #61367 - [
39bea2236e
] - tools: update gyp-next to 0.21.1 (Node.js GitHub Bot) #61528 - [
d5beb4fe1c
] - tools: move Quic dependencies behind ad-hoc flag (Antoine du Hamel) #61446 - [
5c26087c29
] - tools: add LIEF to license builder (Chengzhong Wu) #61523 - [
a181d0c43d
] - url: update ada to v3.4.2 and support unicode 17 (Yagiz Nizipli) #61593
Windows 64-bit Installer: https://nodejs.org/dist/v25.6.0/node-v25.6.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v25.6.0/node-v25.6.0-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v25.6.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v25.6.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v25.6.0/node-v25.6.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v25.6.0/node-v25.6.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v25.6.0/node-v25.6.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v25.6.0/node-v25.6.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v25.6.0/node-v25.6.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v25.6.0/node-v25.6.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v25.6.0/node-v25.6.0-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v25.6.0/node-v25.6.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v25.6.0/node-v25.6.0.tar.gz
Other release files: https://nodejs.org/dist/v25.6.0/
Documentation: https://nodejs.org/docs/v25.6.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
b85011754ca4e373f69e7e2e6c6d77fcafa089325f5a1c051742a9303abfcc51 node-v25.6.0-aix-ppc64.tar.gz
8d21c43d734400b1d63b1a48a0e08545e6920e6d810166ccc0887426448e4db0 node-v25.6.0-arm64.msi
5bfb537a913368152c5eba6aafe43ec834b23ee0ca4b96e5e18253937fe4103e node-v25.6.0-darwin-arm64.tar.gz
4404c6e228e8e0aa35c95cdd5d375021e900f771de1d8ba7e0fc8ce47a4c6b91 node-v25.6.0-darwin-arm64.tar.xz
b8bb25a7fd2fa5c638aa0fa9722ba351b5393ac5ca00aceea6578164b88e7761 node-v25.6.0-darwin-x64.tar.gz
633e0267b7a690437ad407e531e8708af288074711647ae89dc727e295ff12c2 node-v25.6.0-darwin-x64.tar.xz
6e6662d6081f36bb3896df42a331e9ccbb4286fda72daf7bc7fb5bfb18fa8ed0 node-v25.6.0-headers.tar.gz
233a11bf1c03a3a3ed2e635bc2d6d9c011d52a78f5147df44f3b7a27e1cafba1 node-v25.6.0-headers.tar.xz
2e66dabc6cb170347058132d164acca15b61503a0f998346c5134ce3072e003b node-v25.6.0-linux-arm64.tar.gz
e5509c8954771ea0f9291a65e71d2e3dee84b713cdd4e9a55432ca91b75a1922 node-v25.6.0-linux-arm64.tar.xz
76844c065754cbc0df946c185c048d9564508632b5f1899dc82e46fa586d7ad5 node-v25.6.0-linux-ppc64le.tar.gz
124460aae0eb06e66bf716dff0a3f5032759e68740db75b4d7afc9720315a741 node-v25.6.0-linux-ppc64le.tar.xz
54ec956b95461fefba40cbc202558cbe9b25c646bc251a49ff1ee2811a31594b node-v25.6.0-linux-s390x.tar.gz
9598e0fb01bc0da328129dbae7e2efa82730e65a0d074bc0bacb1c31abc8e0cf node-v25.6.0-linux-s390x.tar.xz
a218fdaee14cb399f6b33925d4615a4046ba8db144f6e883c3b81e78937429eb node-v25.6.0-linux-x64.tar.gz
f61908298ba1c8e1802ac00283cee678e0eb4035e1c74f094b06b1620423fcf2 node-v25.6.0-linux-x64.tar.xz
34188b91d682958b6a20822fbb93d99975f52bc777052da564802f82b10ef426 node-v25.6.0-win-arm64.7z
0124a8041cdde07c068c08fdcf4cdc59f83bde8d4b78dc9eca3b5d80672b9e40 node-v25.6.0-win-arm64.zip
b7836c90cfa8458234b21cca33958d289b113fed5609ac648b339f41bb4d3a46 node-v25.6.0-win-x64.7z
133686ade5cd1e1686afcf2d688530fc35afef649ddf6a491e4705610727bd23 node-v25.6.0-win-x64.zip
9a60c1001dc34d108f9e031d8fad2125d407c9a7efdb865e3e00b7c3a34a32d3 node-v25.6.0-x64.msi
335a3556a275302fcd47a5434e7946e0d6a5eafd984f762774ab59c057c24774 node-v25.6.0.pkg
4f9567884d604f900c13cf83919654a55e6808538ed88f25cc9cdfc84ebb70ea node-v25.6.0.tar.gz
9db6848c802b1981c0faeb71a5b8cc79913f82a747f7f1d50260c6d2f781ef7e node-v25.6.0.tar.xz
123b693d8befc1c92d2eb36380c203e061f684f488524569b42460b27f434565 win-arm64/node.exe
47750ee99207e5b621671565852cf7385f27bf664470886b9437137342a497c9 win-arm64/node.lib
551e4bea971fe2b619a02081a23e04cc5884c2c53abefe090b506c7a99a9a891 win-arm64/node_pdb.7z
6131eaeb067affbc2e2e0c505937af90fc3aa981a3aa82fe6390218292018274 win-arm64/node_pdb.zip
1448db441895712bf3eb82102cb6bac80f7b95a62c83ecbc856021d4f9e4d50c win-x64/node.exe
f7201b932d898bdbf78aee7add288d2263c4791f1502068ad11b6c14675c6324 win-x64/node.lib
1cdad9f74c065b8eb60fe913c28e27fa71daebeda805ec9ff90605929df74e84 win-x64/node_pdb.7z
9e8b51e31ebe03bd4e9b1a3fcdfdd0a9534b0c372a1e8c43696f6809fd44fb15 win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iHUEARYIAB0WIQRb6KP2yKXAHRBsCtggsaOQsWjTVgUCaYHeiAAKCRAgsaOQsWjT
VgDjAP0akxoTw9nCYELhzIH9cNc30Jg/YcOxxDxAcGmX4SohbQD+OnlXvqu2otYs
KUo2SVRj8TqZ+sEySyrVLpMC+911YAg=
=ged4
-----END PGP SIGNATURE-----
```

---

## 24. OpenSSL Security Advisory Assessment, January 2026

- 日期: 2026-01-28 17:00
- 链接: https://nodejs.org/en/blog/vulnerability/openssl-fixes-in-regular-releases-jan2026

```
OpenSSL Security Advisory Assessment, January 2026
The Node.js Project
Summary
The OpenSSL project released a security advisory that includes 12 CVEs. After assessment, we have concluded that three CVEs affect Node.js (severity Low to Moderate). Given the limited attack surface, the OpenSSL updates will be included in upcoming regular Node.js releases rather than dedicated security releases.
Analysis
All three vulnerabilities relate to how Node.js processes PFX (PKCS#12) certificate files,
which are used when configuring TLS connections via the pfx
option.
An attacker would need to provide a specially crafted PFX file to trigger any of these issues.
Since PFX files typically come from trusted local sources (e.g., your own private keys
and certificates), the attack surface is limited in practice.
CVE-2025-11187: Stack buffer overflow in PBMAC1 MAC verification - Moderate
OpenSSL 3.0 (used by v20.x) does not support PBMAC1 and is therefore not affected.
CVE-2025-69421: NULL pointer dereference in PKCS12_item_decrypt_d2i_ex() - Low
This function is called internally by PKCS12_parse()
. All branches are affected.
CVE-2026-22795: Type confusion during PKCS#12 parsing - Low
Both OpenSSL 3.0 and 3.5 are vulnerable. All branches are affected.
CVEs that do not affect Node.js
The following 9 CVEs do not affect Node.js on any branch:
- CVE-2025-15467 (High, CMS AuthEnvelopedData): Node.js does not use CMS APIs.
- CVE-2025-15468 (Low, SSL_CIPHER_find + QUIC): Node.js never calls
SSL_CIPHER_find()
. - CVE-2025-15469 (Low, openssl dgst truncation): Command-line tool only.
- CVE-2025-66199 (Low, TLS 1.3 CompressedCertificate): Node.js builds with
OPENSSL_NO_COMP
on all branches, so certificate compression is disabled. - CVE-2025-68160 (Low, BIO_f_linebuffer): Node.js does not use this BIO filter.
- CVE-2025-69418 (Low, low-level OCB): Node.js uses the EVP API, which the advisory confirms avoids the vulnerable path.
- CVE-2025-69419 (Low, PKCS12_get_friendlyname): Node.js does not call this function; the advisory notes
PKCS12_parse()
uses a separate safe path. - CVE-2025-69420 (Low, TS_RESP_verify_response): Node.js does not use timestamp protocol APIs.
- CVE-2026-22796 (Low, PKCS7_digest_from_attributes): Node.js does not call PKCS#7 signature verification APIs.
Contact and future updates
The current Node.js security policy can be found at https://github.com/nodejs/node/security/policy#security, including information on how to report a vulnerability in Node.js.
Subscribe to the low-volume announcement-only nodejs-sec mailing list at https://groups.google.com/forum/#!forum/nodejs-sec to stay up to date on security vulnerabilities and security-related releases of Node.js and the projects maintained in the nodejs GitHub organization.
```

---

## 25. Node.js 25.5.0 (Current)

- 日期: 2026-01-26 20:40
- 链接: https://nodejs.org/en/blog/release/v25.5.0

```
Node.js 25.5.0 (Current)
Antoine du Hamel
2026-01-26, Version 25.5.0 (Current), @aduh95
Notable Changes
Streamlined building process of Single Executable Applications (SEA)
This release introduces a new --build-sea
command-line flag that simplifies the process of building Single Executable Applications (SEA) using Node.js.
Previously, SEA generation involved copying the executable, generating the preparation blob with --experimental-sea-config
, and injecting the blob into the copy using nodejs/postject. With the new --build-sea
flag, these steps are now consolidated into a single step available from Node.js core.
$ echo 'console.log("Hello")' > hello.js
$ echo '{ "main": "hello.js", "output": "sea" }' > sea-config.json
$ node --build-sea sea-config.json
$ ./sea
Hello
For the time being, backward compatibility with the postject-based SEA building process as well as the --experimental-sea-config
will be maintained, until there's motivation to break it (e.g. for optimizations).
See the documentation for more details.
Contributed by Joyee Cheung in #61167.
Other Notable Changes
- [
99a4e51f93
] - crypto: update root certificates to NSS 3.119 (Node.js GitHub Bot) #61419 - [
fbe4da5725
] - (SEMVER-MINOR) deps: add LIEF as a dependency (Joyee Cheung) #61167 - [
0feab0f083
] - (SEMVER-MINOR) deps: add tools and scripts to pull LIEF as a dependency (Joyee Cheung) #61167 - [
e91b296001
] - (SEMVER-MINOR) fs: add ignore option to fs.watch (Matteo Collina) #61433 - [
b351910af1
] - (SEMVER-MINOR) sea: add--build-sea
to generate SEA directly with Node.js binary (Joyee Cheung) #61167 - [
957292e233
] - (SEMVER-MINOR) sea: split sea binary manipulation code (Joyee Cheung) #61167 - [
f289817ff8
] - (SEMVER-MINOR) sqlite: enable defensive mode by default (Bart Louwers) #61266 - [
069f3603e2
] - (SEMVER-MINOR) sqlite: add sqlite prepare options args (Guilherme Araújo) #61311 - [
5a984b9a09
] - src: use node- prefix on thread names (Stewart X Addison) #61307 - [
75c06bc2a8
] - (SEMVER-MINOR) test: migrate to--build-sea
in existing SEA tests (Joyee Cheung) #61167 - [
cabd58f1cb
] - (SEMVER-MINOR) test: use fixture directories for sea tests (Joyee Cheung) #61167 - [
ff1fcabfc9
] - (SEMVER-MINOR) test_runner: support expecting a test-case to fail (Jacob Smith) #60669
Commits
- [
778a56f3c9
] - assert,util: fix deep comparison for sets and maps with mixed types (Ruben Bridgewater) #61388 - [
32cd18e37f
] - async_hooks: enabledHooksExist shall return if hooks are enabled (Gerhard Stöbich) #61054 - [
482b2568bc
] - benchmark: add SQLite benchmarks (Guilherme Araújo) #61401 - [
e9a34263bb
] - buffer: make methods work on Uint8Array instances (Neal Beeken) #56578 - [
8255cdefcf
] - build: add--shared-nbytes
configure flag (Antoine du Hamel) #61341 - [
8dd379d110
] - build: update android-patches/trap-handler.h.patch (Mo Luo) #60369 - [
1b4b5eb0e4
] - build: update devcontainer.json to use paired nix env (Joyee Cheung) #61414 - [
86e2a763ad
] - build: infer cargo mode with gyp var build_type directly (Chengzhong Wu) #61354 - [
7e211e6942
] - build: add embedtest into native suite (Joyee Cheung) #61357 - [
637470e79f
] - build: fix misplaced comma in ldflags (hqzing) #61294 - [
a1a0f77a45
] - build: fix crate vendor file checksums on windows (Chengzhong Wu) #61329 - [
d597b8e342
] - build,tools: fix addon build deadlock on errors (Vladimir Morozov) #61321 - [
b5cdc27ba4
] - build,win: improve logs when ClangCL is missing (Mike McCready) #61438 - [
ef01f0c033
] - build,win: update WinGet configurations to Python 3.14 (Mike McCready) #61431 - [
d8a1cdeefe
] - child_process: treat ipc length header as unsigned uint32 (Ryuhei Shima) #61344 - [
588b00fafa
] - cluster: fix port reuse between cluster (Ryuhei Shima) #60141 - [
99a4e51f93
] - crypto: update root certificates to NSS 3.119 (Node.js GitHub Bot) #61419 - [
048f7a5c9c
] - deps: upgrade npm to 11.8.0 (npm team) #61466 - [
fbe4da5725
] - (SEMVER-MINOR) deps: add LIEF as a dependency (Joyee Cheung) #61167 - [
0feab0f083
] - (SEMVER-MINOR) deps: add tools and scripts to pull LIEF as a dependency (Joyee Cheung) #61167 - [
4bb00d7e3c
] - deps: update googletest to 85087857ad10bd407cd6ed2f52f7ea9752db621f (Node.js GitHub Bot) #61417 - [
6a3c614f27
] - deps: update sqlite to 3.51.2 (Node.js GitHub Bot) #61339 - [
13c0397d6d
] - deps: update icu to 78.2 (Node.js GitHub Bot) #60523 - [
098ec6f196
] - deps: update ada to v3.4.0 (Yagiz Nizipli) #61315 - [
320b576125
] - deps: update zlib to 1.3.1-e00f703 (Node.js GitHub Bot) #61135 - [
98f5e7cf51
] - deps: V8: cherry-pick highway@dcc0ca1cd42 (Richard Lau) #61008 - [
e326df79c9
] - deps: V8: backport 209d2db9e24a (Zhijin Zeng) #61322 - [
ccfd9d9b30
] - doc: removev
prefix for version references (Mike McCready) #61488 - [
b6cc5d77a1
] - doc: mention constructor comparison in assert.deepStrictEqual (Hamza Kargin) #60253 - [
236d7ee635
] - doc: add CVE delay mention (Rafael Gonzaga) #61465 - [
0729fb6ee7
] - doc: update previous version links in BUILDING (Mike McCready) #61457 - [
0fb464252f
] - doc: include OpenJSF handle for security stewards (Rafael Gonzaga) #61454 - [
3331bdca7c
] - doc: clarify process.argv[1] behavior for -e/--eval (Jeevankumar S) #61366 - [
94b34c38e2
] - doc: remove Windows Dev Home instructions from BUILDING (Mike McCready) #61434 - [
a17016ee81
] - doc: clarify TypedArray properties on Buffer (Roman Reiss) #61355 - [
214fac9d7e
] - doc: update Python 3.14 manual install instructions (Windows) (Mike McCready) #61428 - [
6a32a685a6
] - doc: note resume build should not be done on node-test-commit (Stewart X Addison) #61373 - [
2a8e8dfaf3
] - doc: refine WebAssembly error documentation (sangwook) #61382 - [
f3caf27f8b
] - doc: add deprecation history for url.parse (Eng Zer Jun) #61389 - [
5ab8057856
] - doc: add marco and rafael in last sec release (Marco Ippolito) #61383 - [
f83cb1e785
] - doc: packages: example of private import switch to internal (coderaiser) #61343 - [
3d23bcd0e2
] - doc: add esm and cjs examples to node:v8 (Alfredo González) #61328 - [
1d159550e0
] - doc: added 'secure' event to tls.TLSSocket (ikeyan) #61066 - [
90080d2892
] - doc: restore @watilde to collaborators (Daijiro Wachi) #61350 - [
a87f7a50f8
] - doc: run license-builder (github-actions[bot]) #61348 - [
adf5c84701
] - doc: clean up writing-and-running-benchmarks.md (Hardanish Singh) #61345 - [
2be98add0c
] - doc: document ALPNCallback option for TLSSocket constructor (ikeyan) #61331 - [
2db4893c8d
] - esm: ensure watch mode restarts after syntax errors (Xavier Stouder) #61232 - [
828feb2e6b
] - events: remove redundant todo (Gürgün Dayıoğlu) #60595 - [
e91b296001
] - (SEMVER-MINOR) fs: add ignore option to fs.watch (Matteo Collina) #61433 - [
606184fae5
] - fs: remove duplicate getValidatedPath calls (Mert Can Altin) #61359 - [
434fcd7f8f
] - fs: fix errorOnExist behavior for directory copy in fs.cp (Nicholas Paun) #60946 - [
bacba16f5e
] - fs: fix ENOTDIR in globSync when file is treated as dir (sangwook) #61259 - [
7697ce0310
] - fs: remove duplicate fd validation in sync functions (Mert Can Altin) #61361 - [
8abd54f597
] - gyp: aix: change gcc version detection so CXX="ccache g++" works (Stewart X Addison) #61464 - [
24033ee7ea
] - http: fix rawHeaders exceeding maxHeadersCount limit (Max Harari) #61285 - [
cf56327939
] - http2: validate initialWindowSize per HTTP/2 spec (Matteo Collina) #61402 - [
696935eeeb
] - inspector: initial support storage inspection (Ryuhei Shima) #61139 - [
3d5e718e38
] - lib: fix typo inutil.js
comment (Taejin Kim) #61365 - [
f55a5fea00
] - lib: fix TypeScript support check in jitless mode (sangwook) #61382 - [
b3fbc3c375
] - meta: do not fast-track npm updates (Antoine du Hamel) #61475 - [
2423ecdaef
] - meta: fix typos in issue template config (Daijiro Wachi) #61399 - [
e2df85a33a
] - meta: label v8 module PRs (René) #61325 - [
bc9e5f7d4d
] - node-api: fix node_api_create_object_with_properties name (Vladimir Morozov) #61319 - [
4f30c21c59
] - node-api: use Node-API in comments (Vladimir Morozov) #61320 - [
62d71eb28d
] - quic: copy options.certs buffer instead of detaching (Chengzhong Wu) #61403 - [
4bbbe75ba1
] - quic: move quic behind compile time flag (Matteo Collina) #61444 - [
b351910af1
] - (SEMVER-MINOR) sea: add --build-sea to generate SEA directly with Node.js binary (Joyee Cheung) #61167 - [
957292e233
] - (SEMVER-MINOR) sea: split sea binary manipulation code (Joyee Cheung) #61167 - [
f289817ff8
] - (SEMVER-MINOR) sqlite: enable defensive mode by default (Bart Louwers) #61266 - [
6442229880
] - sqlite: add some tests (Guilherme Araújo) #61410 - [
069f3603e2
] - (SEMVER-MINOR) sqlite: add sqlite prepare options args (Guilherme Araújo) #61311 - [
df02d00d61
] - src: improve StringBytes::Encode perf on UTF8 (Сковорода Никита Андреевич) #61131 - [
e35814ba80
] - src: add missing override specifier to Clean() (Tobias Nießen) #61429 - [
803ff7d3de
] - src: cache context lookup in vectored io loops (Mert Can Altin) #61387 - [
58abe99cbf
] - src: cache missing package.json files in the C++ package config cache (Michael Smith) #60425 - [
2a542094e4
] - src: use starts_with instead of rfind/find (Tobias Nießen) #61426 - [
77cacf6d9d
] - src: use C++ nullptr in sqlite (Tobias Nießen) #61416 - [
344cc629d4
] - src: use C++ nullptr in webstorage (Tobias Nießen) #61407 - [
9f25cad26c
] - src: fix pointer alignment (jhofstee) #61336 - [
5a984b9a09
] - src: use node- prefix on thread names (Stewart X Addison) #61307 - [
d4cf423a65
] - stream: export namespace object from internal end-of-stream module (René) #61455 - [
7d8232e34c
] - test: add some validation for JSON doc output (Antoine du Hamel) #61413 - [
75c06bc2a8
] - (SEMVER-MINOR) test: migrate to --build-sea in existing SEA tests (Joyee Cheung) #61167 - [
cabd58f1cb
] - (SEMVER-MINOR) test: use fixture directories for sea tests (Joyee Cheung) #61167 - [
bcffca8911
] - test: aix: mark test_threadsafe_function/test flaky on AIX (Stewart X Addison) #61452 - [
29399501c1
] - test: add implicit test for fs dispose handling with using (Ilyas Shabi) #61140 - [
3bb481571a
] - test: reveal wpt evaluation errors in status files (Chengzhong Wu) #61358 - [
a132be7f71
] - test: check new WebCryptoAPI enum values (Filip Skokan) #61406 - [
72f1463735
] - test: split test-esm-loader-hooks (Joyee Cheung) #61374 - [
39105e4c5f
] - test: aix: mark test-emit-on-destroyed as flaky (Stewart X Addison) #61381 - [
3f17acfb1c
] - test: add webidl web-platform tests (Yagiz Nizipli) #61316 - [
89983cf747
] - test: update url web-platform tests (Yagiz Nizipli) #61315 - [
73c0a242d7
] - test: forbid use of named imports for fixtures (Antoine du Hamel) #61228 - [
a49d54308e
] - test: enforce better never-settling-promise detection (Antoine du Hamel) #60976 - [
335cb0b5cc
] - test: ensure assertions are reached on all tests (Antoine du Hamel) #60845 - [
5ee02c789a
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60763 - [
141fb82ffb
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60760 - [
edf90ce457
] - test: useRegExp.escape
to improve test reliability (Antoine du Hamel) #60803 - [
f5f9b2dcf6
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60728 - [
ec1cbbe0b6
] - test_runner: fix memory leaks in runner (Abhishek Kv. Savani) #60860 - [
399ac68427
] - test_runner: fix coverage report when a directory is named file (Heath Dutton🕴️) #61169 - [
6e1beda333
] - test_runner: print info when test restarts (Xavier Stouder) #61160 - [
f5803ccb86
] - test_runner: fix rerun ambiguous test failures (Moshe Atlow) #61392 - [
a5a4c3eb44
] - test_runner: nix dead reporter code (Vas Sudanagunta) #59700 - [
ff1fcabfc9
] - (SEMVER-MINOR) test_runner: support expecting a test-case to fail (Jacob Smith) #60669 - [
ade4fc2338
] - tools: copyedit Nix files (Antoine du Hamel) #61447 - [
7c2242beb9
] - tools: validate release commit diff as part oflint-release-proposal
(Antoine du Hamel) #61440 - [
ca4ebed258
] - tools: use ad-hoc flag to lint Nix files (Antoine du Hamel) #61405 - [
05ce2c87f3
] - tools: fix vcbuild lint-js-build (Vladimir Morozov) #61318 - [
41adb54a37
] - tools: enforce trailing commas intest/es-module
(Antoine du Hamel) #60891 - [
eebd732a52
] - tools: enforce trailing commas intest/sequential
(Antoine du Hamel) #60892 - [
8b73739e03
] - typings: add typing for string_decoder (Taejin Kim) #61368 - [
e88dd012ad
] - v8: changing total_allocated_bytes to avoid ABI changes (Caio Lima) #60800 - [
c75ad3d87d
] - v8: add GCProfiler support for erm (Ilyas Shabi) #61191 - [
611c179663
] - zlib: validate write_result array length (Ryuhei Shima) #61342
Windows 64-bit Installer: https://nodejs.org/dist/v25.5.0/node-v25.5.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v25.5.0/node-v25.5.0-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v25.5.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v25.5.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v25.5.0/node-v25.5.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v25.5.0/node-v25.5.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v25.5.0/node-v25.5.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v25.5.0/node-v25.5.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v25.5.0/node-v25.5.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v25.5.0/node-v25.5.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v25.5.0/node-v25.5.0-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v25.5.0/node-v25.5.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v25.5.0/node-v25.5.0.tar.gz
Other release files: https://nodejs.org/dist/v25.5.0/
Documentation: https://nodejs.org/docs/v25.5.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
a355ab5635db4f170bddaa7c2c384b22afc4da7072add6f6ad1fb6f355e17e2b node-v25.5.0-aix-ppc64.tar.gz
864c58b9a092a35653a5e5f4d5961a54c1428e9dc9d4b7ac826ca229bbc6996a node-v25.5.0-arm64.msi
568ff9aae73e82499346be25250c7caacab2ca4bbb697bc73056cf3b983b8211 node-v25.5.0-darwin-arm64.tar.gz
11097658094eeceed26b96ebcb6acac349795e9a4b74cb59d2820c5ac8374cd6 node-v25.5.0-darwin-arm64.tar.xz
c36d2db9afc900b2cfa45b60a9423b4991ad86976acd3fe5b500abda91f21243 node-v25.5.0-darwin-x64.tar.gz
c61a93d569f31d2e40eedd988a06362a7d247112f51310756db99ec6722645bc node-v25.5.0-darwin-x64.tar.xz
c86f5090635bedb03b8f8832ebcbcc00cb07f2fd83f3528a826d3bd57c7624af node-v25.5.0-headers.tar.gz
70dd8582d7905cf5f2e72158cce0b57cecd3253e208ff7542889a44c1db71bd4 node-v25.5.0-headers.tar.xz
20f9aa9f2174786754f1941a178a62b906216fcdcd923400817f4bfa72e12336 node-v25.5.0-linux-arm64.tar.gz
2e5264c7e08c1693fce40a6fb604569272438f4bafe93066fa0f00a5ee7bacd6 node-v25.5.0-linux-arm64.tar.xz
c5ca7fee6f0a969e16c6152650ddf4553274d53dc6f81ebee25cfee8c70999cf node-v25.5.0-linux-ppc64le.tar.gz
1db6f6292e6b6f0b25fcb6ff6fbe4d52d4d6d6b4b2131980ecc715854ddb1749 node-v25.5.0-linux-ppc64le.tar.xz
2092f336a60191a44e4b99e87a5278fffa4e4a9dc786b7b657756c2c75460af5 node-v25.5.0-linux-s390x.tar.gz
65736df156468dc40ad3798de2a0f95bd4f227c012d5527ae678b0d9ced84581 node-v25.5.0-linux-s390x.tar.xz
e8e50aee2e5328bcbc2ead32d86d0b577220ccdd80c438583dca3aa2965873f2 node-v25.5.0-linux-x64.tar.gz
8223dca08b48b927acafaae7595dc670c86f7aa1855a20019bd43f8ea890851c node-v25.5.0-linux-x64.tar.xz
06e6ef9670b91f485f733be66dcf173dde50181a644cc2841cbaa732ce8a3adc node-v25.5.0-win-arm64.7z
7ca3d9bb4bf745e4bcd7b6ae6840c37fbd12da909ee5df6b932af42cdd997a19 node-v25.5.0-win-arm64.zip
3b8fb60f80b0cc5bf2abd74dd2b7f853e88f39d2dbca269818742ad7ca0713d2 node-v25.5.0-win-x64.7z
4d2773e98d3f35d172478d5101de1f571d851053d2ed67bbe39a5bdeae87d804 node-v25.5.0-win-x64.zip
af80a24744ff17c98818699da9680f805bb332708ff535967e39940b4bf1195d node-v25.5.0-x64.msi
fba3d55e76190fa381355489e3b63715cd5449a3aeac4d57274e8f3efd07005d node-v25.5.0.pkg
334569dc43eb427af5ca97e330ab8752cbac19a2a70d476a97aa194f79010b07 node-v25.5.0.tar.gz
7e35efaf63c8fe7737b8c62792ec547e5a95a69f1f813fcfba28566aecc9fd92 node-v25.5.0.tar.xz
7f75694e0a071b6f5ffa570fd62c7050b265376252a1db272dcdef81d0fc78e7 win-arm64/node.exe
5ffc9eea8fd5d23619dd28489ec2dc08b994d4f0eacda475ecff0921e80c1b01 win-arm64/node.lib
813fe4fcaba63a89f56152289d3fc4a26d76767064c478a23a47fd74c65670ec win-arm64/node_pdb.7z
7931397d581cf60581ee52dd56d9b5d3920dd8c54580914e68b3975968860ef5 win-arm64/node_pdb.zip
d7f55cbc1b1ca9cc2815d7b8c58f94e4822a68cdf5ca55b4f2c9625581b92839 win-x64/node.exe
19f7d769cb12fc0eb7eaf2a5d3db2d1f70b80d1172aa302dfbdb7d719e0dab46 win-x64/node.lib
fe8e38ba5d145b75b793c8076778fb83e1112fde39bbd7514dd92cbe296f2bb5 win-x64/node_pdb.7z
05a1d0a1126783e0e9ab334805002a1f26a421b987618d500558a23bd14df4ff win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iHUEARYIAB0WIQRb6KP2yKXAHRBsCtggsaOQsWjTVgUCaXfQigAKCRAgsaOQsWjT
VqfOAQCHFSxCgUYXnScTqtnXVzjBcOjnMO4OLbrIN/aKLA/inAD9Em8opoDHOwRz
UjgG3zEoZnpV+uBm7C7jqZsD9dcWNA0=
=rrpu
-----END PGP SIGNATURE-----
```

---

## 26. Chalk to Node.js util styleText

- 日期: 2026-01-23 00:00
- 链接: https://nodejs.org/en/blog/migrations/chalk-to-styletext

```
Chalk to Node.js util styleText
richiemccoll
Migrate from Chalk to Node.js util styleText
chalk-to-util-styletext
This codemod aims to help you reduce external dependencies by transforming chalk method calls to use the native Node.js styling functionality. It will also handle automatic removal of the chalk
package from the package.json.
Compatible Features:
- Basic colors (red, green, blue, yellow, etc.)
- Bright colors (redBright, greenBright, etc.)
- Background colors (bgRed, bgGreen, etc.)
- Text modifiers (bold, dim, italic, underline, strikethrough, etc.)
- Style chaining via array syntax
- Environment variable support (NO_COLOR, NODE_DISABLE_COLORS, FORCE_COLOR)
Incompatible Features:
- Custom RGB colors (chalk.rgb(), chalk.hex())
- 256-color palette (chalk.ansi256())
- Template literal syntax (chalk...``)
- Advanced modifiers with limited terminal support (overline, blink, etc.)
Prerequisites:
Node.js Version Requirements
- Node.js v20.12.0 or later (for util.styleText)
util.styleText
became stable in Node.js v22.13.0 (and v23.5.0)
If your package currently supports Node.js versions earlier than v20.12.0, you cannot migrate to util.styleText without dropping support for those versions. This requires bumping the major version of your package AND updating the engines field in your package.json to require Node.js >= v20.12.0.
Usage:
The source code for this codemod can be found in the chalk-to-util-styletext directory.
You can find this codemod in the Codemod Registry.
npx codemod @nodejs/chalk-to-util-styletext
Example:
import from 'chalk';
.(.red('Error message'));
.(.red.bold('Important error'));
const = .red;
.(('Error'));
const = .blue.bold;
.(('Info'));
Recognition
We would like to thank the maintainers of chalk
for their support of the package over time and for its contributions to the ecosystem.
```

---

## 27. Node.js 25.4.0 (Current)

- 日期: 2026-01-19 17:06
- 链接: https://nodejs.org/en/blog/release/v25.4.0

```
Node.js 25.4.0 (Current)
Rafael Gonzaga
2026-01-19, Version 25.4.0 (Current), @RafaelGSS
Notable Changes
- [
8f6fada8f1
] - cli: add --require-module/--no-require-module (Joyee Cheung) #60959 - [
bf8e738df4
] - cli: mark --heapsnapshot-near-heap-limit as stable (Joyee Cheung) #60956 - [
7930d7a19b
] - crypto: update root certificates to NSS 3.117 (Node.js GitHub Bot) #60741 - [
44f61dfb92
] - doc: add @avivkeller to collaborators (Aviv Keller) #61115 - [
45903ee884
] - doc: add gurgunday to collaborators (Gürgün Dayıoğlu) #61094 - [
77faa14d99
] - doc: mark --build-snapshot and --build-snapshot-config as stable (Joyee Cheung) #60954 - [
aefbe4ba47
] - (SEMVER-MINOR) events: repurposeevents.listenerCount()
to accept EventTargets (René) #60214 - [
8470e2993b
] - (SEMVER-MINOR) http: add http.setGlobalProxyFromEnv() (Joyee Cheung) #60953 - [
24384d7438
] - meta: add Renegade334 to collaborators (Renegade334) #60714 - [
c1acef6d0f
] - module: mark require(esm) as stable (Joyee Cheung) #60959 - [
2e39f3ed6b
] - module: mark module compile cache as stable (Joyee Cheung) #60971 - [
e6a05cfb4f
] - (SEMVER-MINOR) module: allow subpath imports that start with#/
(Jan Martin) #60864 - [
fa927c31da
] - (SEMVER-MINOR) process: preserve AsyncLocalStorage in queueMicrotask only when needed (Gürgün Dayıoğlu) #60913 - [
bd0942f4f5
] - (SEMVER-MINOR) stream: do not passreadable.compose()
output viaReadable.from()
(René) #60907 - [
5051d90100
] - (SEMVER-MINOR) util: add convertProcessSignalToExitCode utility (Erick Wendel) #60963 - [
408f024906
] - v8: mark v8.queryObjects() as stable (Joyee Cheung) #60957
Commits
- [
e61cfdbf50
] - assert: use a set instead of an array for faster lookup (Ruben Bridgewater) #61076 - [
11861084fd
] - assert,util: improve comparison performance (Ruben Bridgewater) #61176 - [
4ef4f759cb
] - assert,util: fix deep comparing invalid dates skipping properties (Ruben Bridgewater) #61076 - [
c8fccd585f
] - assert,util: improve deep comparison performance (Ruben Bridgewater) #61076 - [
13661a0123
] - benchmark: use boolean options in benchmark tests (SeokhunEom) #60129 - [
36dead3433
] - benchmark: allow boolean option values (SeokhunEom) #60129 - [
376056eaef
] - benchmark: add microbench on isInsideNodeModules (Chengzhong Wu) #60991 - [
22d3e85b7a
] - benchmark: fix incorrect base64 input in byteLength benchmark (semimikoh) #60841 - [
5016f75522
] - benchmark: use typescript for import cjs benchmark (Joyee Cheung) #60663 - [
012a08f6eb
] - buffer: let Buffer.of use heap (Сковорода Никита Андреевич) #60503 - [
65696e42ba
] - build: add--shared-hdr-histogram
configure flag (Antoine du Hamel) #61280 - [
6155b8836e
] - build: add--shared-gtest
configure flag (Antoine du Hamel) #61279 - [
e80127f49c
] - build: expose libplatform symbols in shared libnode (Joyee Cheung) #61144 - [
d99805049e
] - build: fix inconsistent quoting inMakefile
(Antoine du Hamel) #60511 - [
3213de08e8
] - build: support building crates (temporal) on windows (沈鸿飞) #61163 - [
1ad8788391
] - build: remove temporal updater (Chengzhong Wu) #61151 - [
e6e25d65be
] - build: add --debug-symbols to build with -g without enabling DCHECKs (Joyee Cheung) #61100 - [
7040ec94c8
] - build: update test-wpt-report to use NODE instead of OUT_NODE (Filip Skokan) #61024 - [
990da3518d
] - build: skip build-ci on actions with a separate test step (Chengzhong Wu) #61073 - [
3259e395c9
] - build: run embedtest with node_g when BUILDTYPE=Debug (Chengzhong Wu) #60850 - [
af42ca569f
] - build: ignore built-in temporal when building with shared lib (Chengzhong Wu) #60703 - [
bec7fce07a
] - build: add temporal_capi gyp (Chengzhong Wu) #60703 - [
d2f50047f7
] - build: fix OpenSSL version parsing for OpenSSL < 3 (Richard Lau) #60775 - [
91b20c52df
] - build: add flag to compile V8 with Temporal support (Antoine du Hamel) #60701 - [
0aaed248f0
] - build: add support for Visual Studio 2026 (Michaël Zasso) #60727 - [
8f6fada8f1
] - cli: add --require-module/--no-require-module (Joyee Cheung) #60959 - [
bf8e738df4
] - cli: mark --heapsnapshot-near-heap-limit as stable (Joyee Cheung) #60956 - [
7930d7a19b
] - crypto: update root certificates to NSS 3.117 (Node.js GitHub Bot) #60741 - [
1b15453602
] - deps: update cjs-module-lexer to 2.2.0 (Node.js GitHub Bot) #61271 - [
118fa97c95
] - deps: update nbytes to 0.1.2 (Node.js GitHub Bot) #61270 - [
9b136db814
] - deps: update ngtcp2 to 1.19.0 (Node.js GitHub Bot) #61156 - [
5635f23a50
] - deps: update nghttp3 to 1.14.0 (Node.js GitHub Bot) #61187 - [
9ec35c0977
] - deps: update nghttp3 to 1.13.1 (Node.js GitHub Bot) #60046 - [
4d7d37f701
] - deps: update timezone to 2025c (Node.js GitHub Bot) #61138 - [
2c1e3ab19d
] - deps: nghttp2: revert 7784fa979d0b (Antoine du Hamel) #61136 - [
56a6513648
] - deps: update nghttp2 to 1.68.0 (nodejs-github-bot) #61136 - [
f2692c5534
] - deps: remove independent temporal (Chengzhong Wu) #61072 - [
3acbf3f129
] - deps: apply cargo vendor (Chengzhong Wu) #61072 - [
d2759f4805
] - deps: add vendor depenency crate (Chengzhong Wu) #61072 - [
6330385174
] - deps: update simdjson to 4.2.4 (Node.js GitHub Bot) #61056 - [
9835860115
] - deps: update googletest to 065127f1e4b46c5f14fc73cf8d323c221f9dc68e (Node.js GitHub Bot) #61055 - [
d2e6dff2f9
] - deps: brotli: cherry-pick e230f474b87 (liujiahui) #61003 - [
27da9ca1c7
] - deps: upgrade npm to 11.7.0 (npm team) #61011 - [
398ba68793
] - deps: V8: cherry-pick 72b0e27bd936 (pthier) #60706 - [
a8ae3b9557
] - deps: update sqlite to 3.51.1 (Node.js GitHub Bot) #60899 - [
4e1edae655
] - deps: update zlib to 1.3.1-63d7e16 (Node.js GitHub Bot) #60898 - [
49b5954e74
] - deps: update corepack to 0.34.5 (Node.js GitHub Bot) #60842 - [
6ae415361f
] - deps: upgrade npm to 11.6.4 (npm team) #60853 - [
3cc857001a
] - deps: add temporal_rs 0.1.0 (Chengzhong Wu) #60703 - [
660788cd4b
] - deps: update sqlite to 3.51.0 (Node.js GitHub Bot) #60614 - [
c6d7a7b7cd
] - deps: upgrade npm to 11.6.3 (npm team) #60785 - [
062e15bddf
] - deps: update brotli to 1.2.0 (Node.js GitHub Bot) #60540 - [
db053988db
] - deps: update simdjson to 4.2.2 (Node.js GitHub Bot) #60740 - [
ea5deab531
] - deps: update googletest to 1b96fa13f549387b7549cc89e1a785cf143a1a50 (Node.js GitHub Bot) #60739 - [
c23f40cca4
] - deps: update minimatch to 10.1.1 (Node.js GitHub Bot) #60543 - [
479c9290b9
] - deps: update corepack to 0.34.4 (Node.js GitHub Bot) #60643 - [
e42911eddd
] - deps: update inspector_protocol to 1b1bcbbe060e8c8cd8704f00f78978c50991 (Node.js GitHub Bot) #60705 - [
d908c83330
] - deps: update cjs-module-lexer to 2.1.1 (Node.js GitHub Bot) #60646 - [
96530a4ca6
] - deps: update simdjson to 4.2.1 (Node.js GitHub Bot) #60644 - [
6b0926ef20
] - deps,src: prepare for cpplint update (Michaël Zasso) #60901 - [
5ed71efa3e
] - doc: fix v25 changelog after security release (Marco Ippolito) #61371 - [
c2791069a2
] - doc: correct description oferror.stack
accessor behavior (René) #61090 - [
134780c035
] - doc: add documentation for process.traceProcessWarnings (Alireza Ebrahimkhani) #53641 - [
3b08efcebb
] - doc: add sqlite session disposal method (René) #61273 - [
ec1847a097
] - doc: fix filename typo (Hardanish Singh) #61297 - [
2c651ce460
] - doc: fix typos and grammar inBUILDING.md
&onboarding.md
(Hardanish Singh) #61267 - [
28fe6ea4a8
] - doc: mention --newVersion release script (Rafael Gonzaga) #61255 - [
2fb35d897d
] - doc: correct typo in BUILDING doc (Mike McCready) #61261 - [
8dc2501a25
] - doc: correct typo in api contributing doc (Mike McCready) #61260 - [
69e357a9d4
] - doc: add PR-URL requirement for security backports (Rafael Gonzaga) #61256 - [
73326ae103
] - doc: add reusePort error behavior to net module (mag123c) #61250 - [
67fbf4d371
] - doc: note corepack package removal in distribution doc (Mike McCready) #61207 - [
0792859e49
] - doc: fix tls.connect() timeout documentation (Azad Gupta) #61079 - [
72f42b9985
] - doc: missingpassed
,error
andpassed
properties onTestContext
(Xavier Stouder) #61185 - [
f418fcc635
] - doc: clarify threat model for application-level API exposure (Rafael Gonzaga) #61184 - [
bd4710769a
] - doc: correct options for net.Socket class and socket.connect (Xavier Stouder) #61179 - [
387b65ca08
] - doc: document error event on readline InterfaceConstructor (Xavier Stouder) #61170 - [
6d886e10e4
] - doc: add a smooth scrolling effect to the sidebar (btea) #59007 - [
23fb3a64ec
] - doc: fix test settime docs (Efe) #61117 - [
808eb437ee
] - doc: correct invalid collaborator profile (JJ) #61091 - [
5e8eb5fe6c
] - doc: add a tip about developer mode on Windows (Joyee Cheung) #61112 - [
a4248776da
] - doc: exclude compile-time flag features from security policy (Matteo Collina) #61109 - [
44f61dfb92
] - doc: add @avivkeller to collaborators (Aviv Keller) #61115 - [
08b5347b41
] - doc: warn about short GCM tags visibly (Tobias Nießen) #61082 - [
45903ee884
] - doc: add gurgunday to collaborators (Gürgün Dayıoğlu) #61094 - [
ce5d6e22ef
] - doc: update MDN links (Livia Medeiros) #61062 - [
657cbd4af3
] - doc: mark sync module hooks as release candidate (Joyee Cheung) #60960 - [
a46368a82b
] - doc: reorganize docs of module customization hooks (Joyee Cheung) #60960 - [
9851278e99
] - doc: mark crypto.hash as stable (Joyee Cheung) #60994 - [
77faa14d99
] - doc: mark --build-snapshot and --build-snapshot-config as stable (Joyee Cheung) #60954 - [
6d5f9ffc6d
] - doc: add File modes cross-references in fs methods (Mohit Raj Saxena) #60286 - [
521b25a27d
] - doc: add missingzstd
to mjs example of zlib (Deokjin Kim) #60915 - [
9a9bed9b3a
] - doc: clarify fileURLToPath security considerations (Rafael Gonzaga) #60887 - [
bebb4731b1
] - doc: show the use of string expressions in the SQLTagStore example (schliepa) #60873 - [
f247c24cb0
] - doc: replace column with columnNumber in example ofutil.getCallSites
(Deokjin Kim) #60881 - [
487c1080aa
] - doc: correct spelling in BUILDING.md (Rich Trott) #60875 - [
5751e3f736
] - doc: update debuglog examples to use 'foo-bar' instead of 'foo' (xiaoyao) #60867 - [
ec8336b7a0
] - doc: correct 'event handle' to 'event handler' in Utf8Stream drop event (Riddhi) #60692 - [
95ef052751
] - doc: fix typos in changelogs (Rich Trott) #60855 - [
a10b3130c6
] - doc: mark module.register as active development (Chengzhong Wu) #60849 - [
bfe8c62a2d
] - doc: add fullName property to SuiteContext (PaulyBearCoding) #60762 - [
2799f594e3
] - doc: add additional codemods for deprecation (Augustin Mauroy) #60811 - [
2b51d5d113
] - doc: keep sidebar module visible when navigating docs (Botato) #60410 - [
2fa9917b07
] - doc: fix webstorage config file property (Marco Ippolito) #60798 - [
a0691d6eb6
] - doc: correct concurrency wording in test() documentation (Azad Gupta) #60773 - [
d26842c523
] - doc: clarify that CQ only picks up PRs targetingmain
(René) #60731 - [
3e84428ffe
] - doc: clarify license section and add contributor note (KaleruMadhu) #60590 - [
745ea1d61f
] - doc: correct and expand documentation for SQLTagStore (René) #60200 - [
a442c27c0a
] - doc: correct tls ALPNProtocols types (René) #60143 - [
d90001a579
] - doc: remove mention of SMS 2FA (Antoine du Hamel) #60707 - [
7525a3fa4b
] - doc: add info about renamed flag incli.md
(Antoine du Hamel) #60690 - [
db0a86897b
] - doc: fix incorrect slh-dsa oids in crypto.md (Artsiom Malakhau) #60681 - [
e5ede89a94
] - doc:domain.add()
does not accept timer objects (René) #60675 - [
36ba9d99ba
] - Revert "doc, assert: correct order of changes entries" (Michaël Zasso) #60774 - [
e6e5ed7665
] - doc,test: add documentation and test on how to use addons in SEA (Joyee Cheung) #59582 - [
f12eb28489
] - esm: avoid throw when module specifier is not url (Craig Macomber (Microsoft)) #61000 - [
a7b92e0677
] - esm: improve error messages for ambiguous module syntax (mag123c) #60376 - [
6da85b576b
] - events: remove eventtarget custom inspect branding (Efe) #61128 - [
aefbe4ba47
] - (SEMVER-MINOR) events: repurposeevents.listenerCount()
to accept EventTargets (René) #60214 - [
dc19409f36
] - fs: validate statfs path (Efe) #61230 - [
206e353a4a
] - fs: fix rmSync to handle non-ASCII characters (Yeaseen) #61108 - [
feee377b83
] - fs: remove broken symlinks in rmSync (sangwook) #61040 - [
6b577c80bb
] - fs: detect dot files when using globstar (Robin van Wijngaarden) #61012 - [
8470e2993b
] - (SEMVER-MINOR) http: add http.setGlobalProxyFromEnv() (Joyee Cheung) #60953 - [
a731463a60
] - http,https: fix double ERR_PROXY_TUNNEL emission (Shima Ryuhei) #60699 - [
b2736646b6
] - http2,zlib: prefercall()
overapply()
if argument list is not array (Livia Medeiros) #60834 - [
86bce15e96
] - lib: implement all 1-byte encodings in js (Сковорода Никита Андреевич) #61093 - [
8156738b97
] - lib: gbk decoder is gb18030 decoder per spec (Сковорода Никита Андреевич) #61099 - [
d8f1dea0d3
] - lib: enforce use ofURLParse
(Antoine du Hamel) #61016 - [
9023b3f9ce
] - lib: add lint rules for reflective function calls (Antoine du Hamel) #60825 - [
2979113136
] - lib: prefercall()
overapply()
if argument list is not array (Livia Medeiros) #60796 - [
2b36433f4a
] - lib: add support for readable byte streams to .toWeb() (Hans Klunder) #58664 - [
1a0c3dddb9
] - lib: useFastBuffer
for empty buffer allocation (Gürgün Dayıoğlu) #60558 - [
9209cf67a4
] - lib: refactor JWK import PQC support check (Filip Skokan) #60586 - [
42666c241a
] - lib,src: isInsideNodeModules should test on the first non-internal frame (Chengzhong Wu) #60991 - [
4a22647609
] - lib,src,test: fix tests without SQLite (Antoine du Hamel) #60906 - [
24795530bb
] - lib,test: enforce use ofassert.fail
via a lint rule (Antoine du Hamel) #61004 - [
1977348ae0
] - lib,test: fix jsdoc comments (Michaël Zasso) #60870 - [
3549cf14ce
] - meta: remove t.js (RafaelGSS) #61369 - [
5cf54abad7
] - meta: bump step-security/harden-runner from 2.13.2 to 2.14.0 (dependabot[bot]) #61245 - [
b57bab72e1
] - meta: bump actions/setup-node from 6.0.0 to 6.1.0 (dependabot[bot]) #61244 - [
42117b5069
] - meta: bump actions/cache from 4.3.0 to 5.0.1 (dependabot[bot]) #61243 - [
fee3edd38e
] - meta: bump actions/download-artifact from 6.0.0 to 7.0.0 (dependabot[bot]) #61242 - [
a96c3160ff
] - meta: bump github/codeql-action from 4.31.6 to 4.31.9 (dependabot[bot]) #61241 - [
b4233e18a9
] - meta: bump codecov/codecov-action from 5.5.1 to 5.5.2 (dependabot[bot]) #61240 - [
c5d7dd3731
] - meta: bump actions/checkout from 6.0.0 to 6.0.1 (dependabot[bot]) #61239 - [
d83cec1534
] - meta: bump actions/upload-artifact from 5.0.0 to 6.0.0 (dependabot[bot]) #61238 - [
d4bfd26f06
] - meta: bump peter-evans/create-pull-request from 7.0.9 to 8.0.0 (dependabot[bot]) #61237 - [
9246c6ab12
] - meta: bump cachix/install-nix-action from 31.8.4 to 31.9.0 (dependabot[bot]) #61236 - [
1b378cfd5e
] - meta: move lukekarrys to emeritus (Node.js GitHub Bot) #60985 - [
f3bfa68d78
] - meta: bump actions/setup-python from 6.0.0 to 6.1.0 (dependabot[bot]) #60927 - [
f1935d19e9
] - meta: bump github/codeql-action from 4.31.3 to 4.31.6 (dependabot[bot]) #60926 - [
0a4a4c090d
] - meta: bump actions/checkout from 5.0.1 to 6.0.0 (dependabot[bot]) #60925 - [
d76f95117b
] - meta: bump peter-evans/create-pull-request from 7.0.8 to 7.0.9 (dependabot[bot]) #60924 - [
4dd153f8c3
] - meta: bump github/codeql-action from 4.31.2 to 4.31.3 (dependabot[bot]) #60770 - [
a90bf3ece1
] - meta: bump step-security/harden-runner from 2.13.1 to 2.13.2 (dependabot[bot]) #60769 - [
ecc945d7ec
] - meta: bump cachix/install-nix-action from 31.8.2 to 31.8.4 (dependabot[bot]) #60768 - [
5578327a4f
] - meta: bump actions/checkout from 5.0.0 to 5.0.1 (dependabot[bot]) #60767 - [
24384d7438
] - meta: add Renegade334 to collaborators (Renegade334) #60714 - [
2d560e42fa
] - module: fix sync resolve hooks for require with node: prefixes (Joyee Cheung) #61088 - [
15c3655b9a
] - module: preserve URL in the parent created by createRequire() (Joyee Cheung) #60974 - [
c1acef6d0f
] - module: mark require(esm) as stable (Joyee Cheung) #60959 - [
2e39f3ed6b
] - module: mark module compile cache as stable (Joyee Cheung) #60971 - [
e6a05cfb4f
] - (SEMVER-MINOR) module: allow subpath imports that start with#/
(Jan Martin) #60864 - [
1983cd6692
] - node-api: add napi_set_prototype (siaeyy) #60711 - [
350b0ea895
] - node-api: fix data race and use-after-free in napi_threadsafe_function (Mika Fischer) #55877 - [
cb3f79273a
] - node-api: add support for Float16Array (Ilyas Shabi) #58879 - [
bdf359b3d1
] - node-api: support SharedArrayBuffer in napi_create_dataview (Kevin Eady) #60473 - [
3c5dc03f06
] - os: freeze signals constant (Xavier Stouder) #61038 - [
ca5c4c9752
] - process: improve process.cwd() error message (TseIan) #61164 - [
fa927c31da
] - (SEMVER-MINOR) process: preserve AsyncLocalStorage in queueMicrotask only when needed (Gürgün Dayıoğlu) #60913 - [
571cec49e0
] - repl: fix getters triggering side effects during completion (Dario Piotrowicz) #61043 - [
377aed336c
] - repl: tab completion targets<class>
instead ofnew <class>
(Đỗ Trọng Hải) #60319 - [
cb8bc3466d
] - sqlite: improve error messages for tag store (Pramit Sharma) #61096 - [
324ea4fa2d
] - sqlite: makeSQLTagStore.prototype.size
a getter (René) #60246 - [
874c50296d
] - src: dump snapshot source with node:generate_default_snapshot_source (Joyee Cheung) #61101 - [
0692b4f014
] - src: improve StringBytes::Encode perf on ASCII (Сковорода Никита Андреевич) #61119 - [
754271a1f0
] - src: add HandleScope to edge loop in heap_utils (Mert Can Altin) #60885 - [
8f46bd9352
] - src: remove redundant CHECK (Tobias Nießen) #61130 - [
5e6ffd9aa0
] - src: remove unused private field inSQLTagStore
(Michaël Zasso) #61027 - [
550e8a7a69
] - src: implement Windows-1252 encoding support and update related tests (Mert Can Altin) #60893 - [
3f9c0e07b4
] - src: fix off-thread cert loading in bundled cert mode (Joyee Cheung) #60764 - [
7eaf815341
] - src: handle DER decoding errors from system certificates (Joyee Cheung) #60787 - [
6e76cec44a
] - src: use static_cast instead of C-style cast (Michaël Zasso) #60868 - [
103e55487e
] - src: handle indexed properties inprocess.env
(Michaël Zasso) #60826 - [
83d1f41752
] - src: simply uint32 to string as it must not fail (Chengzhong Wu) #60846 - [
2dfdc6f01e
] - src: mark unused private field as such (Michaël Zasso) #60802 - [
920f02539e
] - src: implicitly enable namespace in config (Marco Ippolito) #60798 - [
47c5bd9b7c
] - src: add permission flag to config file (Marco Ippolito) #60798 - [
d9df3f710d
] - src: add test flag to config file (Marco Ippolito) #60798 - [
831256cb92
] - src: rename config file testRunner to test (Marco Ippolito) #60798 - [
6c2b75ba87
] - src: split inspector protocol domains files (Chengzhong Wu) #60754 - [
51cf032a5e
] - src: add permission support to config file (Marco Ippolito) #60746 - [
413db7c635
] - src: build v8 tick processor as built-in source text modules (Joyee Cheung) #60518 - [
428d24acf5
] - src,permission: fix permission.has on empty param (Rafael Gonzaga) #60674 - [
a60aa72a87
] - src,permission: add debug log on is_tree_granted (Rafael Gonzaga) #60668 - [
bd0942f4f5
] - (SEMVER-MINOR) stream: do not passreadable.compose()
output viaReadable.from()
(René) #60907 - [
90c12a252a
] - stream: fix isErrored/isWritable for WritableStreams (René) #60905 - [
9ac774c15b
] - test: asserts that import.meta.resolve invokes sync loader hooks (Chengzhong Wu) #61158 - [
c08afc5712
] - test: check util.parseArgs argv parsing with actual process execution (René) #61089 - [
182f2e4b5a
] - test: update WPT for urlpattern to a2e15ad405 (Node.js GitHub Bot) #61134 - [
9f7cc779f5
] - test: make buffer sizes 32bit-aware in test-internal-util-construct-sab (René) #61026 - [
c6a8234963
] - test: remove unneccessary repl magic_mode tests (Dario Piotrowicz) #61053 - [
fa2fe0930f
] - test: skip sea tests on riscv64 (Stewart X Addison) #61111 - [
b209f6ba19
] - test: simplifytest-cli-node-options-docs
(Antoine du Hamel) #61006 - [
c9153c7d4f
] - test: mark stringbytes-external-max flaky on AIX (Stewart X Addison) #60995 - [
2cbddfefb7
] - test: update test426 fixtures (Rich Trott) #60982 - [
c7190e6876
] - test: update WPT for urlpattern to aed1f3d244 (Node.js GitHub Bot) #60642 - [
92649e2873
] - test: deflaketest-repl-paste-big-data
(Livia Medeiros) #60975 - [
e4bc345442
] - test: skip tests not passing withoutNODE_OPTIONS
support (Antoine du Hamel) #60912 - [
63299a47ec
] - test: improve config-file permission test coverage (Rafael Gonzaga) #60929 - [
9a0c420a33
] - test: skip SEA inspect test if inspector is not available (Livia Medeiros) #60872 - [
e97daea17c
] - test: update WPT for WebCryptoAPI to 1e4933113d (Node.js GitHub Bot) #60896 - [
ac367b3550
] - test: lint moreassert(regexp.test(...))
cases (René) #60878 - [
ca5720e7b5
] - test: useassert.match
for non-literal regexp tests (René) #60879 - [
5d30d3fc2d
] - test: fix embedtest in debug windows (Vladimir Morozov) #60806 - [
8caeb03a52
] - test: skip failing tests when compiled without amaro (Yuki Okita) #60815 - [
242e20bf9a
] - test: fix debug test crashes caused by sea tests (Vladimir Morozov) #60807 - [
b890362e1a
] - test: add lint rule to forbid use ofassert.ok(/regex/.test(…))
(Antoine du Hamel) #60832 - [
b08cb5657e
] - test: replace deprecated regex test assertions in http trailers test (Aditya Chopra) #60831 - [
47ed95965e
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60761 - [
79d48f9441
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60759 - [
585e200b40
] - test: prefer major GC in cppgc-object teardown (sangwook) #60672 - [
9426ff6b08
] - test: add basic temporal presence check (Chengzhong Wu) #60703 - [
ffebf8e55c
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60726 - [
adc6776c6a
] - test: ensure assertions are reached on HTTP2 tests (Antoine du Hamel) #60730 - [
3dae49c6ce
] - test: ensure assertions are reached on HTTP tests (Antoine du Hamel) #60729 - [
5203b09fea
] - test: skip test that cause timeout on IBM i (SRAVANI GUNDEPALLI) #60700 - [
6d2fe36747
] - test: add missing r.close() calls in REPL multiline tests (sangwook) #60226 - [
bbee2ef5e0
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60634 - [
a2764d450d
] - test: update WPT for WebCryptoAPI to c58b6f4e0e (Node.js GitHub Bot) #60702 - [
1176fe43a7
] - test: fix test-buffer-zero-fill-cli to be effective (Сковорода Никита Андреевич) #60623 - [
1a66dc1292
] - test: limit the concurrency of WPTRunner for RISC-V (Levi Zim) #60591 - [
36076846d4
] - test: fix test-strace-openat-openssl for RISC-V (Levi Zim) #60588 - [
5a976cb507
] - test: split test-runner-run-watch.mjs (Joyee Cheung) #60653 - [
8f611b9bce
] - test: ensure assertions are reached on more tests (Antoine du Hamel) #60641 - [
3e550d30d6
] - test_runner: fix lazytest.assert
accessor (René) #61097 - [
ec142be1ed
] - test_runner: propagate V8 options to child process (Pietro Marchini) #60999 - [
3127a2b1e7
] - test_runner: fix line feed escaping in JUnit (Aliaksandr) #60274 - [
08fb6c9ba4
] - test_runner: simplify code and make it more consistent (Antoine du Hamel) #60777 - [
102b217cf3
] - tools: bump the eslint group in /tools/eslint with 2 updates (dependabot[bot]) #61246 - [
97b6b61165
] - tools: unpin ngtcp2 version updates (Michaël Zasso) #61155 - [
7e95edc3de
] - tools: only report commit validation failure on Slack (Antoine du Hamel) #61124 - [
3a7ed257a3
] - tools: use sparse-checkout in linter jobs (Antoine du Hamel) #61123 - [
b655edf1bf
] - tools: simplifynotify-on-push
(Antoine du Hamel) #61050 - [
230155749d
] - tools: fix update-nghttp2 signature verification (Richard Lau) #61035 - [
e8646a7d10
] - tools: improve log output ofcreate-release-proposal
(Antoine du Hamel) #61028 - [
a4b2614912
] - tools: fixvcbuild test
when path contain spaces (stduhpf) #56481 - [
9769c359f8
] - tools: do not runtest-linux
workflow for changes onvcbuild.bat
(Antoine du Hamel) #60979 - [
2ceaf6eb3c
] - tools: add some options and comments toshell.nix
(Antoine du Hamel) #60911 - [
611135abdc
] - tools: bump mdast-util-to-hast from 13.2.0 to 13.2.1 in /tools/doc (dependabot[bot]) #60930 - [
b4bad20a6c
] - tools: ignore more paths in GHA CI (Antoine du Hamel) #60920 - [
47b7cb4e9e
] - tools: run tests--without-amaro
on test-shared macOS (Antoine du Hamel) #60902 - [
b0ec8c9c2a
] - tools: replace deprecated eslint-plugin-markdown (Michaël Zasso) #60908 - [
46dacf686e
] - tools: remove deprecated ESLint plugins (Michaël Zasso) #60908 - [
1a4ec6e830
] - tools: update ESLint dependencies (Michaël Zasso) #60908 - [
4e442b286d
] - tools: refloat 10 Node.js patches to cpplint.py (Michaël Zasso) #60901 - [
fa90d09de6
] - tools: update cpplint to 2.0.2 (Michaël Zasso) #60901 - [
4d944c5198
] - tools: disable some new cpplint rules before update (Michaël Zasso) #60901 - [
eaebae1eed
] - tools: don't fetch V8 deps in the source tree (Richard Lau) #60883 - [
256770944a
] - tools: add temporal updater (Chengzhong Wu) #60828 - [
1c38f808bd
] - tools: dump config.gypi as json (Chengzhong Wu) #60794 - [
ed89b35291
] - tools: bump js-yaml from 4.1.0 to 4.1.1 in /tools/lint-md (dependabot[bot]) #60781 - [
c98c0881c5
] - tools: fix linter warning intest-shared.yml
(Antoine du Hamel) #60772 - [
aa44406ed7
] - tools: bump js-yaml from 4.1.0 to 4.1.1 in /tools/doc in the doc group (dependabot[bot]) #60766 - [
b756154ed9
] - tools: fixpaths-ignore
in gha files (Antoine du Hamel) #60753 - [
18ed53fb7a
] - tools: update install_tools.bat old echo from 2019 to 2022 (David Hidalgo) #60736 - [
cf79940d5c
] - tools: remove unsupportedcooldown
from Dependabot config (Antoine du Hamel) #60747 - [
8ea73ffd64
] - tools: update sccache to v0.12.0 (Michaël Zasso) #60723 - [
578f8bdfa0
] - tools: update x64 macOS runner (Antoine du Hamel) #60676 - [
3b6cf316c0
] - tools: update gyp-next to 0.21.0 (Node.js GitHub Bot) #60645 - [
7d55b8c00f
] - tools,doc: fix format-md files list (Stefan Stojanovic) #61147 - [
a617942a4a
] - url: add fast path to getPathFromURL decoder (Gürgün Dayıoğlu) #60749 - [
a6ac8bd2a5
] - url: remove array.reduce usage (Gürgün Dayıoğlu) #60748 - [
09b5396523
] - util: optimize toASCIILower function using V8s native toLowerCase (Mert Can Altin) #61107 - [
1dd15c9502
] - util: limitinspect
to only show own properties (Ruben Bridgewater) #61032 - [
5051d90100
] - (SEMVER-MINOR) util: add convertProcessSignalToExitCode utility (Erick Wendel) #60963 - [
98b6dc1181
] - util: fix parseArgs skipping positional arg with --eval and --print (azadgupta1) #60814 - [
862eaf8a09
] - util: assert getCallSites does not invoke Error.prepareStackTrace (Chengzhong Wu) #60922 - [
c2e79aa5fb
] - util: improve textencoder encodeInto performance (Yagiz Nizipli) #60843 - [
b6903aaf8d
] - util: safely inspect getter errors whose message throws (Yves M.) #60684 - [
408f024906
] - v8: mark v8.queryObjects() as stable (Joyee Cheung) #60957 - [
b00ee5222c
] - worker: update code examples fornode:worker_threads
module (fisker Cheung) #58264 - [
2409839f19
] - worker: remove not implemented declarations (Artur Gawlik) #60655 - [
c09417a2b1
] - zlib: add CHECK to validate fast path input (Matteo Collina) #61175
Windows 64-bit Installer: https://nodejs.org/dist/v25.4.0/node-v25.4.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v25.4.0/node-v25.4.0-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v25.4.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v25.4.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v25.4.0/node-v25.4.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v25.4.0/node-v25.4.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v25.4.0/node-v25.4.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v25.4.0/node-v25.4.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v25.4.0/node-v25.4.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v25.4.0/node-v25.4.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v25.4.0/node-v25.4.0-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v25.4.0/node-v25.4.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v25.4.0/node-v25.4.0.tar.gz
Other release files: https://nodejs.org/dist/v25.4.0/
Documentation: https://nodejs.org/docs/v25.4.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
df2993c0317188ffff1711fbfcd8e5b9596367b7833d6e2d42fdb2a119bd3035 node-v25.4.0-aix-ppc64.tar.gz
d89169c597bb7f13a5295ad05c3b640b0068c9d0493e39d33df022de0caf6ba1 node-v25.4.0-arm64.msi
bfa7af56c0f24074d7a6c5b08d837b8be211f44db5fcc93dcb2cb96153e49b65 node-v25.4.0-darwin-arm64.tar.gz
82fe1e7c2b851ebd4ae3413bf1347990e4c351884c7d5983da895c6c8562573b node-v25.4.0-darwin-arm64.tar.xz
1c75d67c9416c61a948c7cd5662b4293daa0e5a9ddac664f17921ccd5d41a016 node-v25.4.0-darwin-x64.tar.gz
9036701ff6e4b6e52096a32b2ebcd05e1a560e50fb0c3a9afa23642d9c023e74 node-v25.4.0-darwin-x64.tar.xz
b79d50770ed78a2282673fb18745dba6a0ed5fac0f4ee06d0d3e9ff343a7b884 node-v25.4.0-headers.tar.gz
44debda47bf2a00d34cbc4acd21249e519c2021c3720d95229c3effdcb26f13a node-v25.4.0-headers.tar.xz
b059f504162053f4a5d71e85f3d1d89032a7c14eb1a7223c76ef2ff9ce34612c node-v25.4.0-linux-arm64.tar.gz
1e8c471a0c4693cb8b592bcde86be0bf4b7bf8efb28b196e52fc6fa4b486f2e9 node-v25.4.0-linux-arm64.tar.xz
d663ba430f03b033aba5ea84fb1f61c7f34f752e14b95b70cdc49867e19cba32 node-v25.4.0-linux-ppc64le.tar.gz
379d45275167e7214b28a63c2ef06964211383d528748e9ae95ad3d562a96fab node-v25.4.0-linux-ppc64le.tar.xz
885cd50dfa58220e6d6ac7b2534663b766e988e55b87c772788dbfb4c05fd807 node-v25.4.0-linux-s390x.tar.gz
631622dd50b509732f519f12d2bff1072ba1421bfe4ceb17fb9683f30099ba31 node-v25.4.0-linux-s390x.tar.xz
5951a889ab65b3a73cc88e6d412d70499f523a89fe553b5349471af7586f2be2 node-v25.4.0-linux-x64.tar.gz
f3bde66a96c232f34cdd9f4fea6b551f915f8f3ac0952793eef903b3e35df037 node-v25.4.0-linux-x64.tar.xz
e349a266077b138435a0da3afa843d32837652fd76199cccf898f884f5c8ee96 node-v25.4.0-win-arm64.7z
ab747b4d8579aa95ef7148a883fea5a5577dfbcc1bfbc4f62bb4257c26b27acc node-v25.4.0-win-arm64.zip
9aa12c81be9ca56953fd875de2dd625718d767a3ee482d00ab5f69993be392be node-v25.4.0-win-x64.7z
5a5fcd17bc7567645c85b016cd428e4cd9e54796994651be3f3709768714e002 node-v25.4.0-win-x64.zip
54e212e905be2d71145ab986834ec53116303a8a8b6f1162084983b8bd8b46fd node-v25.4.0-x64.msi
f1db8a93f7d9280205c61ebcc199cdfced821cf07f65651d4d24d1f98aa993ec node-v25.4.0.pkg
aa85eaa3c2c81c8b755039018d725bc140c409c2100508785bc8275e610b0e81 node-v25.4.0.tar.gz
04e365aadcd7bf4cf1a6001723ea41035bfb118d78f8a8ee2054b37fc5cb67d6 node-v25.4.0.tar.xz
f94f9de59d8418346386852ad1ffc1caa7276e3a7040a4f36b3032046c025564 win-arm64/node.exe
313755ba5970fbe0b2af34583654bbc0f4c5121dc5e5b06e12deee958f6a5d24 win-arm64/node.lib
687814c2738106514cc8510cc33224190c339b32bcfac9d8f282424b754367ae win-arm64/node_pdb.7z
08c62e194d14a7e2270c49fbd1d51c834e816a93555c8b9f40cc8ddd64d32852 win-arm64/node_pdb.zip
39a867f03ecb065ac3e7944361c0fc2a22ec466fdff2dc3281a068a09bffe810 win-x64/node.exe
e1c02915c1020765f2373e792022936c6ebace7f8449657a60c1b01ed1a9a1da win-x64/node.lib
6c1240160c948a4ba5c4915720e5467cd8fe8b76c9c4e9f421ede2f3fe3496b9 win-x64/node_pdb.7z
249ccf6bd7d893fb06af8ff3700de5a640811036747de62c2c080de2749f2f71 win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQGzBAEBCAAdFiEEiQwI24V5Fi/uDfnbi+q0389VXvQFAmluY9QACgkQi+q0389V
XvQWOgwAhsuVxCkSREU8AVdUVTMwLNJQWgwAtmIiN6enp6XZ1tzr5OQPrjyAJnQS
JDH9ZbRQcCQOBqloRLrPHxV9SYKhSJuHKhBAY3+I6ZJVJYt2uBhDiR8cSFjxwCpC
JLywnqFOjfmltOSpDhIzgM7/fqDVcIP7sGXGGH57hw9iNtKTtjgEeUKI7cuSiPs6
i5PCy9LSA6H+unoJ4DNwPjbq0I3Tg1B62T6mWNfdElsAKOdMUsOFxEhQFR2EZfs3
ri/BpTJOtiqoLiJ/ip/PG5OkOcbHL3cEo5Gf808kphFv+TiptB4gga0ftIy6K+z7
nl+8FdreEQMgp9ri/Rp6FyHwq/akA1y6cyumrsK2CkVndYGvg0DOS2E9ZPvY3qUw
3FHX82/ULRIbS30Yxcz7VvDljhVhdLDwpjdZw+3aY4Hsw9eX3hpIFED3LAK5iwen
ev/GwoYespRJpkUJOkPDZPoMEHRufoUDy3ZDi/uH4n+FSb2HszR2xkf/x6aX+cPJ
Mhm6DuuF
=uWLl
-----END PGP SIGNATURE-----
```

---

## 28. Mitigating Denial-of-Service Vulnerability from Unrecoverable Stack Space Exhaustion for React, Next.js, and APM Users

- 日期: 2026-01-13 17:00
- 链接: https://nodejs.org/en/blog/vulnerability/january-2026-dos-mitigation-async-hooks

```
Mitigating Denial-of-Service Vulnerability from Unrecoverable Stack Space Exhaustion for React, Next.js, and APM Users
Matteo Collina, Joyee Cheung
TL;DR
Node.js/V8 makes a best-effort attempt to recover from stack space exhaustion with a catchable error, which frameworks have come to rely on for service availability. An edge case that reproduces only when async_hooks
are enabled breaks this recovery path: when recursion in user code exhausts stack space, Node.js exits immediately with exit code 7 instead of throwing a recoverable error. This can be reproduced in countless applications because:
- React Server Components use
AsyncLocalStorage
- Next.js uses
AsyncLocalStorage
for request context tracking - Other frameworks may also use
AsyncLocalStorage
for request context tracking - Most APM tools (Datadog, New Relic, Dynatrace, Elastic APM, OpenTelemetry) use
AsyncLocalStorage
orasync_hooks.createHook
to trace requests
The weakness ultimately lies in the ecosystem's reliance on an unspecified behavior in the language - recovery from stack space exhaustion - for service availability (CWE-758). Given the widespread use of async_hooks
by popular frameworks and APM tools, the aforementioned edge case can expose this weakness more frequently and can present a Denial‑of‑Service vector for many applications. Node.js shipped a mitigation in the January 2026 security release to make this unspecified behavior more consistent, reducing the chance of reproduction. However, the weakness remains in the ecosystem until applications and frameworks move away from relying on unspecified behavior for availability.
For users of these frameworks/tools and server hosting providers: Update as soon as possible.
For libraries and frameworks: apply more robust defenses against stack space exhaustion to ensure service availability (e.g., limit recursion depth or avoid recursion if the depth can be controlled by an attacker). A recoverable RangeError: Maximum call stack size exceeded
is only an unspecified behavior maintained with best-effort, and cannot be depended on for security guarantees.
The Reproduction
When a stack overflow occurs in user code while async_hooks
is enabled, Node.js immediately exits with code 7
instead of allowing try-catch
blocks to catch the error. This is a special condition in Node.js that skips the process.on('uncaughtException')
handlers, making the exception uncatchable.
import { createHook } from 'node:async_hooks';
// This simulates what APM tools do
createHook({ init() {} }).enable();
function recursive() {
new Promise(() => {}); // Creates async context
return recursive();
}
try {
recursive();
} catch (err) {
console.log('This never runs', err);
}
- Expected:
try-catch
catches theRangeError
- Actual: Immediate crash with exit code 7
Why This Affects React and Next.js
React Server Components
React 18+ uses AsyncLocalStorage
(which is built on async_hooks
) to track the rendering context for Server Components:
// Inside React's internals
import { AsyncLocalStorage } from 'node:async_hooks';
const asyncLocalStorage = new AsyncLocalStorage();
// Every server component render creates async context
async function renderServerComponent(Component, props) {
return asyncLocalStorage.run({ request: currentRequest }, async () => {
return <Component {...props} />;
});
}
Next.js Request Context
Next.js uses AsyncLocalStorage
to track request context, cookies, headers, and more:
// Simplified from Next.js internals
import { AsyncLocalStorage } from 'node:async_hooks';
export const requestAsyncStorage = new AsyncLocalStorage();
// Every request creates async context
export function handleRequest(req, res) {
return requestAsyncStorage.run({ req, res }, async () => {
// Your page/API handler runs here
});
}
The Real-World Scenario
Consider a Next.js API route that processes user-submitted JSON:
// pages/api/process.js
export default async function handler(req, res) {
try {
const data = req.body;
const result = processNestedData(data); // Deeply nested = stack overflow
res.json({ success: true, result });
} catch (err) {
// THIS CATCH BLOCK NEVER RUNS
console.error('Processing failed:', err);
res.status(500).json({ error: 'Processing failed' });
}
}
function processNestedData(data) {
if (Array.isArray(data)) {
return data.map(item => processNestedData(item));
}
return transform(data);
}
A user sending deeply nested JSON can crash your entire server:
[
[
[
[
[
[
[
[
[
[
[
[
[
[
[
[
[
[
[
[
[
[
[
[
/* 50,000 levels deep */
]
]
]
]
]
]
]
]
]
]
]
]
]
]
]
]
]
]
]
]
]
]
]
]
- Without
async_hooks
:try-catch
catches theRangeError
, returns 500, server continues - With
async_hooks
(React/Next.js): Server crashes immediately with exit code 7
Why the Use of APM Tools Makes It Easier to Reproduce
Application Performance Monitoring (APM) tools are essential infrastructure for production applications. They track request latency, identify bottlenecks, trace errors to their source, and alert teams when something goes wrong. Companies use APM tools like Datadog, New Relic, Dynatrace, Elastic APM, and OpenTelemetry to maintain visibility into their distributed systems.
To provide this functionality, APM tools need to follow a request as it flows through your application, even across async boundaries. When an HTTP request comes in, is processed by middleware, queries a database, calls an external API, and finally returns a response, the APM needs to correlate all of these operations into a single trace. This requires async context tracking.
Most modern APM tools use AsyncLocalStorage
(which is built on async_hooks
in versions of Node.js before Node 24) to propagate trace context across async operations. The moment you require('dd-trace')
, require('newrelic')
, or initialize OpenTelemetry, your application has async_hooks
enabled.
The irony is notable: the tools you install to monitor and debug crashes can make a category of crashes behave differently. This is not the fault of the APM tools; they are using Node.js APIs exactly as intended.
Why This Is Only a Mitigation, and The Vulnerability Lies Elsewhere
While this issue has significant practical impact, we want to be clear about why Node.js is treating this fix as a mere mitigation of security vulnerability risks at large:
Stack Space Exhaustion Behavior Is Not Specified
The "Maximum call stack size exceeded" error is not part of the ECMAScript specification. The specification does not impose any limit and assumes infinite stack space. Imposing a limit and throwing a recoverable error are only behaviors that JavaScript engines implement with best-effort. Applications and frameworks are already at risk when they build a security model on top of these unspecified behaviors that are not guaranteed to reproduce consistently, see:
- CWE-758: Reliance on Undefined, Unspecified, or Implementation-Defined Behavior
- CWE-674: Uncontrolled Recursion
It's worth noting that even when ECMAScript specifies that proper tail calls should reuse stack frames, this is not implemented by most JavaScript engines today, including V8. And in the few JavaScript engines that do implement it, proper tail calls (as used in the reproduction above) can block an application with infinite recursion instead of hitting the stack size limit at some point and stopping with an error, which is another Denial-of-Service vector. This reinforces that stack overflow behavior cannot be relied upon for defending against Denial-of-Service attacks.
This Behavior Is Not Part of The Security Guarantees of V8
In Node.js, the stack space usage from JavaScript function calls is primarily implemented by V8. JavaScript engines developed for browsers have a different security model, and they do not triage crashes like this as security vulnerabilities. This means similar behavior inconsistencies reported in the upstream (like this) are not guaranteed to go through vulnerability disclosure procedures, making any security classification by Node.js alone ineffective.
uncaughtException Limitations
The uncaughtException
handler is not designed to recover the process after it fires. The Node.js documentation explicitly warns against this pattern. Specifically, the documentation states that "Exceptions thrown from within the event handler will not be caught. Instead, the process will exit with a non-zero exit code, and the stack trace will be printed. This is to avoid infinite recursion."
Trying to invoke the handler after the call stack size is exceeded would itself throw. The fact that it works without promise hooks is largely coincidental rather than guaranteed behavior.
Why We Put It In a Security Release
Although it is a patch for an unspecified behavior, we chose to include it in the security release because of its widespread impact on the ecosystem. The prevalence of async_hooks
usage by React Server Components, Next.js, and APM tools makes it a practical Denial-of-Service vector for many applications.
Making the unspecified behavior more consistent in Node.js improves developer experience and makes error handling more predictable.
However, it's important to note that we were fortunate to be able to fix this particular case. There's no guarantee that similar edge cases involving stack overflow and async_hooks
can always be addressed. For mission-critical paths that must defend against infinite recursion or stack overflow from recursion whose depth can be controlled by an attacker, always sanitize the input or impose a limit on the depth of recursion by other means.
It's worth noting that large array allocations can suffer from similar issues, like the recent qs
vulnerability CVE-2025-15284 showed. It's paramount that developers validate and constrain resource usage that could be controlled by an attacker. The runtime cannot always recover reliably from resource exhaustion after-the-fact.
Technical Deep Dive
How async_hooks Works
When you create a Promise, async_hooks
fires callbacks to track the async context:
new Promise()
→ V8 promise hook triggered
→ async_hooks init callback runs
→ Your hook code executes (e.g., APM span creation)
The Fatal TryCatchScope
Node.js wraps async_hooks
callbacks in a special error handler called TryCatchScope
with CatchMode::kFatal
:
// From Node.js internals
void EmitAsyncInit(/* ... */) {
TryCatchScope try_catch(env, TryCatchScope::CatchMode::kFatal);
// Run async_hooks callback
}
kFatal
means: "If any error occurs here, it's unrecoverable. Exit immediately."
This behavior is documented and intentional. From the async_hooks documentation:
If any
AsyncHook
callbacks throw, the application will print the stack trace and exit. The exit path does follow that of an uncaught exception, but all'uncaughtException'
listeners are removed, thus forcing the process to exit.The reason for this error handling behavior is that these callbacks are running at potentially volatile points in an object's lifetime, for example during class construction and destruction. Because of this, it is deemed necessary to bring down the process quickly in order to prevent an unintentional abort in the future.
This design makes sense: if your APM tool's init
callback throws an error, the application is in an undefined state. The hook might have partially executed, resources might be leaked, and continuing could cause data corruption. Better to crash fast and loud.
But stack overflow is different. The error doesn't originate in the hook. Instead, it originates in user code. The stack just happens to overflow while the hook is on the call stack. The hook itself is fine; there's no corrupted state to worry about.
The Bug Explained
To understand the bug, we need to understand how promise hooks work.
When you enable async_hooks
with an init
callback, Node.js registers a promise hook with V8. This hook is invoked by V8 itself every time a Promise is created, not by Node.js JavaScript code. The critical detail is that V8 calls this hook synchronously during the Promise constructor, before new Promise()
returns to your code.
The call sequence looks like this:
Your code: new Promise()
→ V8 Promise constructor
→ V8 calls promise hook (synchronous, before constructor returns)
→ Node.js promiseInitHook() [JavaScript]
→ emitInitNative() [JavaScript]
→ Your async_hooks init callback
→ V8 Promise constructor returns
Your code continues...
This means that async_hooks
callbacks don't run in isolation. They run on the same call stack as user code. Every new Promise()
call adds several stack frames for the hook machinery on top of whatever is already on the stack.
Here's what the stack looks like during deep recursion:
[bottom of stack]
recursive() frame #1
new Promise()
V8 promise hook
async_hooks init callback ← TryCatchScope::kFatal active here
recursive() frame #2
new Promise()
V8 promise hook
async_hooks init callback ← TryCatchScope::kFatal active here
recursive() frame #3
new Promise()
V8 promise hook
async_hooks init callback ← STACK OVERFLOW HAPPENS HERE
[top of stack - limit reached]
Each recursive call adds frames for both the user code AND the async_hooks machinery. When the stack finally overflows, the currently executing code is the async_hooks callback, so the TryCatchScope::kFatal
catches it.
The complete sequence when stack overflow occurs:
- User code calls
new Promise()
recursively - Each
new Promise()
synchronously triggers V8's promise hook - V8 calls into Node.js's
promiseInitHook()
, thenemitInitNative()
- The stack fills up with interleaved user code and hook frames
- Stack overflow throws a
RangeError
while inside the hook callback TryCatchScope::kFatal
catches the errorTryCatchScope::~TryCatchScope()
callsenv_->Exit(ExitCode::kExceptionInFatalExceptionHandler)
- Node.js exits with code 7
The error originated in user code (the recursive pattern), but because it manifests while the hook callback is the active frame, it's treated as a fatal hook error.
The Fix
The fix detects stack overflow errors and re-throws them to user code instead of treating them as fatal:
TryCatchScope::~TryCatchScope() {
// ... simplified
if (HasCaught() && mode_ == CatchMode::kFatal) {
Local<Value> exception = Exception();
// Stack overflow? Re-throw to user code instead of exiting
if (IsStackOverflowError(env_->isolate(), exception)) {
ReThrow();
Reset();
return;
}
// Other fatal errors: exit as before
FatalException(/* ... */);
}
}
After this fix:
try-catch
blocks catch theRangeError
as expected- Applications can handle the error gracefully
- Behavior is more consistent with and without
async_hooks
enabled
A Brief History: From async_hooks to AsyncContextFrame
Understanding this bug requires knowing how Node.js evolved its async context tracking.
The async_hooks Era
async_hooks
was introduced in Node.js 8 (2017) as a low-level API to track asynchronous resources. It provides callbacks (init
, before
, after
, destroy
) that fire at key points in an async resource's lifecycle. APM tools immediately adopted it to trace requests across async boundaries.
However, async_hooks
has significant performance overhead. Every Promise creation, every timer, and every I/O operation triggers these callbacks. This cost is unavoidable when the hooks are enabled.
AsyncLocalStorage
Node.js 12.17.0 (2020) introduced AsyncLocalStorage
, a higher-level API built on top of async_hooks
. It provides a cleaner interface for the most common use case: storing context that flows through async operations (like request IDs, user sessions, or tracing spans).
React Server Components and Next.js adopted AsyncLocalStorage
for request context tracking, unknowingly inheriting all of async_hooks
behaviors, including this bug.
The AsyncContextFrame Revolution (Node.js 24+)
In Node.js 24, AsyncLocalStorage
was reimplemented using a new V8 feature called AsyncContextFrame
. This approach integrates context tracking directly into V8's Promise implementation, eliminating the need for JavaScript callbacks on every async operation.
The result is dramatically better performance. Importantly for this bug, AsyncLocalStorage
no longer uses async_hooks.createHook()
internally. This is why React and Next.js are not affected by this bug on Node.js 24+.
Note: AsyncLocalStorage
is still exported from the async_hooks
module for backwards compatibility, even though it no longer uses the async_hooks
machinery internally on Node.js 24+. It's also available from node:async_hooks
and the newer node:async_context
module.
For more details on this evolution and its performance implications, see The Hidden Cost of Context.
Affected Versions
Patched releases available for:
- Node.js 20.20.0 (LTS)
- Node.js 22.22.0 (LTS)
- Node.js 24.13.0 (LTS)
- Node.js 25.3.0 (Current)
Also affected (no patches, end-of-life):
- All Node.js versions from 8.x to 18.x (8.x was the first version with
async_hooks
)
Users on Node.js versions prior to 20.x who cannot upgrade should reach out for commercial support for EOL versions.
Important: React and Next.js Impact by Version
The impact on React Server Components and Next.js varies by Node.js version:
*Node.js 24+ reimplemented AsyncLocalStorage
without using async_hooks.createHook()
, so React and Next.js are not affected on these versions.
**APM tools that use only AsyncLocalStorage
are not affected on Node.js 24+. APM tools that directly use async_hooks.createHook()
are still affected on all versions.
Mitigation
Recommended: Upgrade to the patched versions released on January 13th, 2026.
If you cannot upgrade immediately, consider altering your application to avoid deep recursion, particularly when allocating promises within recursive functions.
Timeline
- December 7, 2025: React/Next.js team contacted Matteo Collina to report this issue
- December 8, 2025: Vercel Security team opens the HackerOne report #3456295
- December 9, 2025: Matteo Collina starts working on a first patch that would defer the stack overflow error to the next macrotick.
- December 10, 2025: The React/Next.js team validates that this patch did not fix the problem.
- December 10, 2025: Matteo Collina prepares a different patch that rethrows the error immediately, freeing the stack.
- December 11, 2025: The React/Next.js team validates that this patch fixes the problem.
- December 12, 2025: Anna Henningsen identifies a blocker for this strategy. The Node.js team starts brainstorming on alternative solutions.
- December 16, 2025: Joyee Cheung communicates that Node.js cannot treat this as a vulnerability for the reasons listed in this blog post.
- December 17, 2025: Anna Henningsen fixes the blocking issue for the patch.
- January 13, 2026: Patched versions released and disclosure published
Conclusion
This bug highlights how deeply async_hooks
has become embedded in the Node.js ecosystem. What started as a low-level debugging API is now a critical dependency for React Server Components, Next.js, every major APM tool, and any code using AsyncLocalStorage
.
The fix improves the consistency of stack size limit errors caused by deep recursions. While we were able to address this particular case, developers should be aware that stack overflow behavior is not specified by ECMAScript and should not be relied upon for service availability. If the depth of recursion can be controlled by an attacker, always sanitize the input or impose a limit by other means to restrict the depth, instead of counting on the JS runtime to impose a limit or recover from it with a catchable error.
Users running React RSC, Next.js, or any other framework using AsyncLocalStorage
, as well as any APM tool in production, should upgrade to the patched versions released on January 13th, 2026.
Acknowledgments
This fix was developed by Matteo Collina and Anna Henningsen. Thanks to Marco Ippolito for preparing the release and to Rafael Gonzaga, Joyee Cheung, and James Snell for helping with the triaging.
Thanks to Andrew MacPherson for reporting the bug in Next.js/React and to the React and Next.js teams at Meta and Vercel for reporting this issue and providing additional evidence that helped refine the fix. Special thanks to Jimmy Jai, Sebastian Markbage, and Sebastian Silbermann.
```

---

## 29. Node.js 22.22.0 (LTS)

- 日期: 2026-01-13 14:18
- 链接: https://nodejs.org/en/blog/release/v22.22.0

```
Node.js 22.22.0 (LTS)
Marco Ippolito
2026-01-13, Version 22.22.0 'Jod' (LTS), @marco-ippolito
This is a security release.
Notable Changes
- (CVE-2025-59465) add TLSSocket default error handler
- (CVE-2025-55132) disable futimes when permission model is enabled
- (CVE-2025-55130) require full read and write to symlink APIs
- (CVE-2025-59466) rethrow stack overflow exceptions in async_hooks
- (CVE-2025-55131) refactor unsafe buffer creation to remove zero-fill toggle
- (CVE-2026-21637) route callback exceptions through error handlers
Commits
- [
6badf4e6f4
] - deps: update c-ares to v1.34.6 (Node.js GitHub Bot) #60997 - [
37509c3ff0
] - deps: update undici to 6.23.0 (Matteo Collina) nodejs-private/node-private#791 - [
eb8e41f8db
] - (CVE-2025-59465) lib: add TLSSocket default error handler (RafaelGSS) nodejs-private/node-private#797 - [
ebbf942a83
] - (CVE-2025-55132) lib: disable futimes when permission model is enabled (RafaelGSS) nodejs-private/node-private#748 - [
6b4849583a
] - (CVE-2025-55130) lib,permission: require full read and write to symlink APIs (RafaelGSS) nodejs-private/node-private#760 - [
ddadc31f09
] - (CVE-2025-59466) src: rethrow stack overflow exceptions in async_hooks (Matteo Collina) nodejs-private/node-private#773 - [
d4d9f3915f
] - (CVE-2025-55131) src,lib: refactor unsafe buffer creation to remove zero-fill toggle (Сковорода Никита Андреевич) nodejs-private/node-private#759 - [
25d6799df6
] - (CVE-2026-21637) tls: route callback exceptions through error handlers (Matteo Collina) nodejs-private/node-private#796
Windows 32-bit Installer: https://nodejs.org/dist/v22.22.0/node-v22.22.0-x86.msi
Windows 64-bit Installer: https://nodejs.org/dist/v22.22.0/node-v22.22.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v22.22.0/node-v22.22.0-arm64.msi
Windows 32-bit Binary: https://nodejs.org/dist/v22.22.0/win-x86/node.exe
Windows 64-bit Binary: https://nodejs.org/dist/v22.22.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v22.22.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v22.22.0/node-v22.22.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v22.22.0/node-v22.22.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v22.22.0/node-v22.22.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v22.22.0/node-v22.22.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v22.22.0/node-v22.22.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v22.22.0/node-v22.22.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v22.22.0/node-v22.22.0-aix-ppc64.tar.gz
ARMv7 32-bit Binary: https://nodejs.org/dist/v22.22.0/node-v22.22.0-linux-armv7l.tar.xz
ARMv8 64-bit Binary: https://nodejs.org/dist/v22.22.0/node-v22.22.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v22.22.0/node-v22.22.0.tar.gz
Other release files: https://nodejs.org/dist/v22.22.0/
Documentation: https://nodejs.org/docs/v22.22.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
b5ab6deeb8d54b9738039a8ffdc4781cc4b81b291e79b20d3600f830d1d669cb node-v22.22.0-aix-ppc64.tar.gz
26b66be5f735426dce7355d629246f704be08b377f3382de293a6513676cf051 node-v22.22.0-arm64.msi
5ed4db0fcf1eaf84d91ad12462631d73bf4576c1377e192d222e48026a902640 node-v22.22.0-darwin-arm64.tar.gz
2bd596bbfc4a275ceb8721a5954ee97daea5ebe673e96a185ebd732f6fb023ac node-v22.22.0-darwin-arm64.tar.xz
5ea50c9d6dea3dfa3abb66b2656f7a4e1c8cef23432b558d45fb538c7b5dedce node-v22.22.0-darwin-x64.tar.gz
48bc437e00e0c1483da34c21dca196efcb8d22e5dcb0bc7c65386afb00fabb85 node-v22.22.0-darwin-x64.tar.xz
670494f0cc674059596222c60e5db84fbe80c849d7ffb1c3fbd20e4f55b8ea85 node-v22.22.0-headers.tar.gz
58e1483493244a4f8aa7d21ad8b21fc4f72cc3ca669fdf292089cad9de221fde node-v22.22.0-headers.tar.xz
25ba95dfb96871fa2ef977f11f95ea90818c8fa15c0f2110771db08d4ba423be node-v22.22.0-linux-arm64.tar.gz
1bf1eb9ee63ffc4e5d324c0b9b62cf4a289f44332dfef9607cea1a0d9596ba6f node-v22.22.0-linux-arm64.tar.xz
a92684d8720589f19776fb186c5a3a4d273c13436fc8c44b61dd3eeef81f0d3a node-v22.22.0-linux-armv7l.tar.gz
a8b4f15f6e1f371422f1f7abcca4c46bd7abc1c732c274bc5cb108b841c1f0ff node-v22.22.0-linux-armv7l.tar.xz
54680eec598330b9863ab37ada46456415b776e46345958476fcd2212abdf0f3 node-v22.22.0-linux-ppc64le.tar.gz
d83b9957431cc18e1fc143a4b99f89cde7b8a18f53ef392231b4336afd058865 node-v22.22.0-linux-ppc64le.tar.xz
9b24cc6dd17106725d79645adf0a3b62fa3310e4d30aa11147dd3fe2d8325ef4 node-v22.22.0-linux-s390x.tar.gz
5aa0e520689448c4233e8d73f284e8e0634fdcd32b479735698494be5641f3e4 node-v22.22.0-linux-s390x.tar.xz
c33c39ed9c80deddde77c960d00119918b9e352426fd604ba41638d6526a4744 node-v22.22.0-linux-x64.tar.gz
9aa8e9d2298ab68c600bd6fb86a6c13bce11a4eca1ba9b39d79fa021755d7c37 node-v22.22.0-linux-x64.tar.xz
0e437be47d67d916c2b94073321dfdaffef85ef6e527d509588d00994e9036af node-v22.22.0.pkg
5a4585d7f26bfb283267194b299243efea5ee6edd2fbf887825469b4ac94aece node-v22.22.0.tar.gz
4c138012bb5352f49822a8f3e6d1db71e00639d0c36d5b6756f91e4c6f30b683 node-v22.22.0.tar.xz
31bad2fed05553bd4709851e5269ec953c744ee5845d2962564f37fcff634a53 node-v22.22.0-win-arm64.7z
5b44fd410df7b4cd0a1891a05a7b606f8fb7d8786a94997b996a372e82478d7a node-v22.22.0-win-arm64.zip
98758c6ec0b29a03b4e1ec0ace7671a8ac57839034d23a1a62e91fc782fb97d2 node-v22.22.0-win-x64.7z
c97fa376d2becdc8863fcd3ca2dd9a83a9f3468ee7ccf7a6d076ec66a645c77a node-v22.22.0-win-x64.zip
3cf831dc2ae1a53da6baee772388b7cd5635617c8a133fbaf92269fde3336686 node-v22.22.0-win-x86.7z
5d7f6cfc50474cf784027ce9ddabf47a0198ea4b588301ab8675de8c56217247 node-v22.22.0-win-x86.zip
b10f88c6ded24ca487839b3eccb8870a08d7f9fc2b9bb3b463fc72a3a40bcdb1 node-v22.22.0-x64.msi
ec3eeb357dbb980aea936afb8ce8b279f12cf0bec03fd7781ddcfad44f01cba6 node-v22.22.0-x86.msi
fd44256121597d6a3707f4c7730b4e3733eacb5a95cc78a099f601d7e7f8290d win-arm64/node.exe
48839df5eda1889bf704353d35699a4b0d379ee3b2c87d9bfdf0d2d22b182c18 win-arm64/node.lib
8497008940246b148cf9e4455568adbc1a4d5b71f52ebd236dc4f90e5f30142d win-arm64/node_pdb.7z
ded8b2b2c37f93017d8d565f4b32db5278283d3d9527803008ee1aa282c3a084 win-arm64/node_pdb.zip
bae898add4643fcf890a83ad8ae56e20dce7e781cab161a53991ceba70c99ffb win-x64/node.exe
29b1f8c74cb600ff522dcb9da5807c752fae6f510868b7f3079851ebf27154ea win-x64/node.lib
549027ada17424c185a545cf09b3fad7a1d769777ec587481cefe694447728c6 win-x64/node_pdb.7z
1b3fad691fc6f0c1bf679e5999de3d4e16a506e54e404e7e5f9459c9e1e9e1cb win-x64/node_pdb.zip
65fff00e7d40f9a7fc7fb7a64e0d3a595adb6807eeafc8ed8477850eedc90e68 win-x86/node.exe
03c89ca02b018a620471a8411881ab90f472b9e88e5b150cf58b075afb7ce2e9 win-x86/node.lib
fc2cd7abd2c3ee99de42b16bb86e1ecf4fed6d87b714d4827f1e26c4a7e17e51 win-x86/node_pdb.7z
28561a9939829dc3d32ac6b6bc478a1614fbe3992657ab45d1926a0007c2e8fd win-x86/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQIzBAEBCAAdFiEEzGj1oxBv9EgyLkjtJ/XjjVsKIV8FAmlmTlkACgkQJ/XjjVsK
IV8/DRAAoFQH3kAks0aVWHG0/v8+rdRbWiIJxNffnfeudYYCm7xcz9JKHo+NhjyY
LQCqoaZUnCo7HJa0y3UypKHC0Jho2WdueyfW6/U/e5wpGt38N4UMaz8tbAGBk48Y
72esD5RnYwA1JEGTtO6JIY8tcLC4NwIMT81WIQaTsGEKtNcJpu8F9AvQGxe0TKuT
RGIcT6IKRuIU0heRYdbmQ85jK9p/pukGdlMoz5/DSDDYQnE3ZRyokdXsnyPn3xx6
2OEfEL+bjzyDj76zBLuZJSL4Dzm8UC43YTcZHFXKUHyyKNNx9lIOd/LD9Xzujkr4
HZT4VhOJqQYZuEaVNTapDZzUe2LCoLH+iHmAndUyWL5w94yf6C9/M5hCSfKdVWQV
L4B453tDc1SI7m1GaQlngBb7bfL/b4dKQeoOrwDCqp8nYkg41CMN+FnJ74fzxNEn
in2HIDEfcEWhs+5aQr+ITH29c0V5jufrsnle0I82FQ93BZ9JVLq1WTe5xgrp9wjU
zNM4v7BuBRMQP0qSv1mc3xuwu1Wr837NhTZh+vjYI++DhkL5GTUJ6MH2R3m58+Hg
kcyXQet+YEs8cFbs12Tq47KMsn9rTsOfksubyLJxxz/XRRkgv6HE0m9c5jlbF+uV
gZJILw7c8UopZWoVtuRaZxFFQCipWUcT+NBENDUZnetaHN7KuQo=
=vkw+
-----END PGP SIGNATURE-----
```

---

## 30. Node.js 25.3.0 (Current)

- 日期: 2026-01-13 13:58
- 链接: https://nodejs.org/en/blog/release/v25.3.0

```
Node.js 25.3.0 (Current)
Rafael Gonzaga
2026-01-13, Version 25.3.0 (Current), @RafaelGSS
This is a security release.
Notable Changes
- (CVE-2025-59465) add TLSSocket default error handler (RafaelGSS) https://github.com/nodejs-private/node-private/pull/750
- (CVE-2026-21636) add network check on pipe_wrap connect (RafaelGSS) https://github.com/nodejs-private/node-private/pull/784
- (CVE-2025-55130) require full read and write to symlink APIs (RafaelGSS) https://github.com/nodejs-private/node-private/pull/760
- (CVE-2025-55132) disable futimes when permission model is enabled (RafaelGSS) https://github.com/nodejs-private/node-private/pull/748
- (CVE-2025-59466) rethrow stack overflow exceptions in async_hooks (Matteo Collina) https://github.com/nodejs-private/node-private/pull/773
- (CVE-2025-55131) refactor unsafe buffer creation to remove zero-fill toggle (Сковорода Никита Андреевич) https://github.com/nodejs-private/node-private/pull/759
- (CVE-2026-21637) route callback exceptions through error handlers (Matteo Collina) https://github.com/nodejs-private/node-private/pull/790
Commits
- [
a6a74b89a7
] - deps: update c-ares to v1.34.6 (Node.js GitHub Bot) #60997 - [
5100614e26
] - deps: update undici to 7.18.2 (Node.js GitHub Bot) #61283 - [
f0a8916887
] - (CVE-2025-59465) lib: add TLSSocket default error handler (RafaelGSS) nodejs-private/node-private#750 - [
b4b887c5f7
] - (CVE-2025-55132) lib: disable futimes when permission model is enabled (RafaelGSS) nodejs-private/node-private#748 - [
26be208039
] - (CVE-2025-55130) lib,permission: require full read and write to symlink APIs (RafaelGSS) nodejs-private/node-private#760 - [
bdf5873d44
] - (CVE-2026-21636) permission: add network check on pipe_wrap connect (RafaelGSS) nodejs-private/node-private#784 - [
0578e3e921
] - (CVE-2025-59466) src: rethrow stack overflow exceptions in async_hooks (Matteo Collina) nodejs-private/node-private#773 - [
4d6b55a6d1
] - (CVE-2025-55131) src,lib: refactor unsafe buffer creation to remove zero-fill toggle (Сковорода Никита Андреевич) nodejs-private/node-private#759 - [
c357a39e14
] - (CVE-2026-21637) tls: route callback exceptions through error handlers (Matteo Collina) nodejs-private/node-private#790
Windows 64-bit Installer: https://nodejs.org/dist/v25.3.0/node-v25.3.0-x64.msi
Windows ARM 64-bit Installer: https://nodejs.org/dist/v25.3.0/node-v25.3.0-arm64.msi
Windows 64-bit Binary: https://nodejs.org/dist/v25.3.0/win-x64/node.exe
Windows ARM 64-bit Binary: https://nodejs.org/dist/v25.3.0/win-arm64/node.exe
macOS 64-bit Installer: https://nodejs.org/dist/v25.3.0/node-v25.3.0.pkg
macOS Apple Silicon 64-bit Binary: https://nodejs.org/dist/v25.3.0/node-v25.3.0-darwin-arm64.tar.gz
macOS Intel 64-bit Binary: https://nodejs.org/dist/v25.3.0/node-v25.3.0-darwin-x64.tar.gz
Linux 64-bit Binary: https://nodejs.org/dist/v25.3.0/node-v25.3.0-linux-x64.tar.xz
Linux PPC LE 64-bit Binary: https://nodejs.org/dist/v25.3.0/node-v25.3.0-linux-ppc64le.tar.xz
Linux s390x 64-bit Binary: https://nodejs.org/dist/v25.3.0/node-v25.3.0-linux-s390x.tar.xz
AIX 64-bit Binary: https://nodejs.org/dist/v25.3.0/node-v25.3.0-aix-ppc64.tar.gz
ARMv8 64-bit Binary: https://nodejs.org/dist/v25.3.0/node-v25.3.0-linux-arm64.tar.xz
Source Code: https://nodejs.org/dist/v25.3.0/node-v25.3.0.tar.gz
Other release files: https://nodejs.org/dist/v25.3.0/
Documentation: https://nodejs.org/docs/v25.3.0/api/
SHASUMS
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
2b281c24a295d517fec0e31f0508810b229e2377cefdf97798c74fa8c7de8163 node-v25.3.0-aix-ppc64.tar.gz
6f6d3bbc3edf9f52e168fcacb065bdb6ab8a496b9a6e75ee11637fc3a79cb873 node-v25.3.0-arm64.msi
d80f384c182971724a7aa819173084e1d8244338fa8e9271a1961d38274d7209 node-v25.3.0-darwin-arm64.tar.gz
2a59bb95e3025f2928f7c6383c98f5c000845ff9f2b847063fa1dc72ecf3b9b2 node-v25.3.0-darwin-arm64.tar.xz
d6d494e5deca973556e146555cdd29b927b0adb3cae2f234b8e1a92310657c39 node-v25.3.0-darwin-x64.tar.gz
979d124e178a24c56eebe9786f359ea9ad533aab8ef39c4941fa0c72f1c37f77 node-v25.3.0-darwin-x64.tar.xz
aff7dc51eca4c08e025785674047e4e0b8cf3cf0481e8bcc5870b7b56ecea39d node-v25.3.0-headers.tar.gz
8ba495ef14af626b44b4cfc463e3cbd7c976d130c79f465d32bda33e0efe9c2c node-v25.3.0-headers.tar.xz
8098e098dc91ec3bf98035eeebff8d9b3e46fb9e14c1e8c377986f76e0b8368f node-v25.3.0-linux-arm64.tar.gz
7d216a3fd253221da593d06d53fb201da01bd89ac6b3618c91740f379706d71a node-v25.3.0-linux-arm64.tar.xz
7564e1fea56baca6fb701dc625ddff239371b7ca63be5691dad6f6911dae85eb node-v25.3.0-linux-ppc64le.tar.gz
552f7176bc10997e8a3c0c13a2b94638d5a11f39200e115d5978dc1d2305a823 node-v25.3.0-linux-ppc64le.tar.xz
53798fa258a37a353395e97d6ffb25d1a8e42258ebc933041b20b55bab1104c4 node-v25.3.0-linux-s390x.tar.gz
aa8ed1656774ab90ae26266f72f6ce78f4ba3feb0d52dca880f29d662888a923 node-v25.3.0-linux-s390x.tar.xz
cc91362eb9a009efa26117c39c7bd55fe130123f01cf60d300b8b57e9501c27c node-v25.3.0-linux-x64.tar.gz
31d124b6b56a83173a7b3bb9ab2c0ec58a0bfcb4e00864707807318ba3ddfa6d node-v25.3.0-linux-x64.tar.xz
088391dd77fbd92a2dd495615cdea92fdf11ec5dc70f3e724b8b7f2f0965bf6e node-v25.3.0-win-arm64.7z
ef217b4313cc6e9bd34a599e4d90f2e40a7ca5c30ae5a3098b32054b1c0d1727 node-v25.3.0-win-arm64.zip
61eac0c670c86a34c3764a0e9c301aa2f7260ccb80adc13c3e53280fdff2f04f node-v25.3.0-win-x64.7z
3c138ba2cd835b1af70ae2813422f544b2e786bdff8c0885ffb89fb7d407148e node-v25.3.0-win-x64.zip
3f8c82f6d7edc2b00a1c9852e3bdd16feb6dbf8990279da9650a2fca9ebfdd65 node-v25.3.0-x64.msi
09bd3f5619aed0dc5f3aaf9de50cea52ffbabc79b5bda36e8e88dbed26405710 node-v25.3.0.pkg
36cf586c51f20832ad27790f278f89f98a8dd957c4d6593d4f34e492249b3352 node-v25.3.0.tar.gz
97939099edd035a0c1a2d1fc849cac018ec2a38c0c28dd8e8246fd883cdb9e9e node-v25.3.0.tar.xz
ec945fb2f2ee283225de505b58518d40e31dfa20fdedbb5b35e44ab173dca456 win-arm64/node.exe
8505f43c0673d071ace6d57c0008eae3b7eca1b7cd6d334c7a632eff056a090e win-arm64/node.lib
6a3d1f7b9bc4c2953fd0ea3991ab4b6b1f03174d0691013a129f5ec5414ce058 win-arm64/node_pdb.7z
4c1aa600d3eff04cd43677539271ef2fd3400ceb1101b9af1257470dfd79dae5 win-arm64/node_pdb.zip
660281da866a222495759906d4ad90f84549f9cca8aa7fff3559df087140bd28 win-x64/node.exe
d5fa10f3ab2f43420a7f2253a14508802e42541b14cd805e5f04d51cc0caa21f win-x64/node.lib
424950cb1c34dad3216753308922f7ecb5a0d1773900c5f2b1bf95ed22b29cf1 win-x64/node_pdb.7z
349af8b9a1a4ceea98ab2a814c32dc6ac3e8724334fa1ca35439602a6b696476 win-x64/node_pdb.zip
-----BEGIN PGP SIGNATURE-----
iQGzBAEBCAAdFiEEiQwI24V5Fi/uDfnbi+q0389VXvQFAmlmTWMACgkQi+q0389V
XvSCcgv+JHQgZ1ZTToSsl6QgpghY0GdIk1gsycd4qVBrdRRevRv1j7JjyhFegdCf
zr1DLU+Ze0h2VdetrGoPUHD/xpJ4ZjnK2dATQcx6kDNuXoTIJhuFXRBiWuWH8D+Y
bBhAQJaRYs3tbsE2w+0DbbGG3mqqHalu7Ft+v4OYAVXOYoGf/c7bKWykax0/0tv/
sxugysrx/QdMRTfq91kDXQ9cvAZENHPc2SCD+dV+6pCTIJEEecsZ0gS/1z9FROZc
qUudaN8/cqeh6qGLixIMmBEkH7zwDBAKXCT2ZLtivsw7eh2UtafoZzEGOUVAUh+a
BHCWzFQYO3JEOtwrx0O3kKI9nPpshiTjqpZfbiPsd6/hOZ+1eqqVcYTTmCQBaq/x
bsYOfd5Ccow9ARuqYQh6/8gfgFYV8dzLWY7OlXjuOLCXSVY6/ppjuFg7cq+69eKC
RaKrNU9NAx+uWYos8ky6wpblieILwBh37TlAB7FUODwEqOXDYhUezxtQMJsoH2N3
6WYmaOmU
=ftL2
-----END PGP SIGNATURE-----
```

---
