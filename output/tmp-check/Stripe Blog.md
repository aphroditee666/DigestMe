# Stripe Blog

> 分类: 大厂技术博客
> URL: https://stripe.com/blog/feed.rss
> 抓取: 10 篇

---

## 1. Everything we announced at Sessions 2026

- 日期: 2026-04-29 00:00
- 链接: https://stripe.com/blog/everything-we-announced-at-sessions-2026

```
Everything we announced at Sessions 2026
This morning at our annual conference, Stripe Sessions, we shared 288 new products and features with more than 9,000 business leaders and builders. We’re making Stripe even more programmable; protecting and propelling your business with the strength of the Stripe network; and building economic infrastructure for AI.
Here’s everything we announced.
Payments
Today, we launched and demoed payments infrastructure for the next era of commerce. We expanded the Agentic Commerce Suite through partnerships with Meta and Google; announced a new way to grant agents the ability to pay with Link’s agent wallet; and unveiled Checkout studio, which helps you build, analyze, and optimize high-converting checkouts in a few clicks. Here’s what’s new:
Agentic commerce
- You can now sell through AI agents by uploading your product catalog and managing agent access directly from the Stripe Dashboard with the Agentic Commerce Suite.
- We previewed the ability for platforms to use the Agentic Commerce Suite, allowing their connected accounts to become agent-ready with discovery, checkout, payments, and fraud detection handled through a single Stripe integration.
- We partnered with Meta to enable native checkout inside ads on Facebook so discovery and purchase happen in one flow.
- Customers will soon be able to buy your products in AI Mode and the Gemini app via the Universal Commerce Protocol (UCP), through a new partnership between Stripe and Google.
- Agents can now programmatically transact with your business via microtransactions, recurring payments, and more with the Machine Payments Protocol (MPP), co-authored by Stripe and Tempo.
- You can now accept payments from agents over MPP in stablecoins as well as fiat through cards, Klarna, and Affirm via Shared Payment Tokens (SPTs), using our Payment Intents API.
Link
- You can now grant agents the ability to pay with Link’s agent wallet, while maintaining control via spending approvals and full purchase visibility.
- Link now supports additional payment methods. Via Link, US businesses can now accept Pix in Brazil and stablecoins. We also previewed the ability for US businesses to accept UPI via Link in India.
- You can now see Link’s impact on your conversion, authorization rates, and payments costs in a dedicated tab in the Dashboard.
Optimized Checkout Suite
- We previewed Checkout studio, a new way for you to configure, analyze, and optimize your checkout with an AI assistant, live transaction replay, A/B testing, and personalized recommendations.
- We previewed Stripe Checkout’s new embedded form, built for embedded use cases like sidebars, chat boxes, and modals.
- More payment methods, including Pix and UPI, now support subscriptions, localized currency presentment, and cross-border payments.
- You can now accept Sunbit in the US, Bizum in Spain, and Pay by Bank in Finland.
- You can now accept Bizum, BLIK, and Pay by Bank for cross-border payments.
- You can now accept TWINT for recurring transactions.
- You can now automatically detect and display your customer’s preferred currency with a new Adaptive Pricing AI model that analyzes dozens of session signals in real time.
- You can now use Adaptive Pricing to localize subscription prices to your customer’s domestic currency.
- We previewed a new way for your customers to save a card in your app by tapping it on their Android device instead of manually entering the card information.
Stripe Terminal
- We announced the Stripe Reader T600, a new countertop device with an eight-inch screen and the power to run custom apps that support experiences like loyalty and upsells.
- We announced the ability to process in-person payments with Terminal in 15 additional markets, including Hong Kong and Mexico.
- We announced the ability to accept additional payment methods such as Alipay, Klarna, and UnionPay International for in-person payments with Terminal.
- We previewed Terminal’s standalone mode, so you can quickly start accepting payments on Stripe readers with no code or point of sale required.
Stripe Managed Payments
- All digital businesses can now use Managed Payments, Stripe’s merchant of record solution. It helps digital businesses sell globally by handling indirect tax compliance in 80+ countries, as well as fraud prevention, dispute management, and customer support.
Payments Intelligence Suite
- We previewed the ability to A/B test Authorization Boost against your existing payments performance.
- You can now use Authorization Boost’s new AI-powered optimizations, including support for Data Only authentication flows and PINless debit retries, helping increase acceptance rates by an average of 3.8% and lower processing costs by up to 3.3%.
- You can now use Stripe’s 3DS solution on a standalone basis—enabling regulatory compliance, including support for exemptions, and fraud protection to payments processed by another payment service provider.
- You can now use the Stripe Dashboard assistant for payments analytics, which investigates performance issues, diagnoses root causes, and recommends next steps in natural language.
Radar
Millions of global businesses use Stripe Radar to fight fraud, from leading AI companies like OpenAI, Anthropic, ElevenLabs, and Cursor to global enterprises like PepsiCo and Hertz. Today, we announced the biggest-ever upgrades to Radar, helping you to defend against new types of fraud—including token abuse and account fraud—protect more of your payments on and off Stripe, and win more disputes. Here’s what’s new:
- You can now identify high-risk trials without blocking legitimate customers using Radar’s free trial abuse prevention.
- We previewed Radar’s bot abuse prevention, designed to accurately distinguish legitimate AI agents from fraudulent actors.
- You can now use a new payment signal to identify fraudulent payments on and off Stripe with Stripe Signals.
- We previewed additional payment signals to predict disputes and early fraud warnings, and detect pay-as-you-go abuse before invoices go unpaid with Signals.
- We previewed new customer signals to detect multi-account abuse and account sharing abuse with Signals, helping you distinguish real customers from bad actors before they cost you money.
- We previewed new merchant signals to assess fraud risk for new accounts, predict merchant delinquency, and analyze websites for suspicious activity using LLM-powered reviews with Signals.
- We previewed new Stripe Issuing authorization signals that predict the likelihood that a card authorization is fraudulent, extending protection to non-Stripe issuers, banks, and fintechs.
- You can now use Radar’s fraud protection to block high-risk transactions on all supported payment methods, including bank debits; wallets; buy now, pay later (BNPL) options; and stablecoins.
- We announced custom Radar models that are trained on your business signals along with Stripe’s global network intelligence for more accurate fraud detection.
- You can now access upgraded fraud intervention models for Checkout that enable precise, low-friction interventions, such as targeted CAPTCHAs, to reduce fraud while improving conversion.
- You can now receive AI-powered recommendations for additional evidence fields, such as tracking number or customer usage logs, to supplement Smart Disputes evidence.
- You can now store persistent documentation, like terms and conditions, in your evidence library. Smart Disputes can pull from this library automatically, so you don’t have to submit the same materials repeatedly.
Revenue
Agentic activity requires new, real-time infrastructure for metering, rating, alerting, and payments. We upgraded our Revenue suite to support new AI-native business models with dimensional pricing and streaming payments. We also made Stripe more programmable with three new Stripe Billing customizations and expanded access to real-time, ready-to-query data. Here’s what’s new:
Stripe Billing
- You can now power a broader range of usage-based and hybrid pricing models with Metronome, a Stripe product. You can manage commits, multidimensional pricing structures, bespoke contracts, and more, with real-time revenue visibility down to the account, contract, and product level.
- You can now access and manage Metronome contracts, customers, and data directly in the Stripe Dashboard with the Metronome app.
- We announced the ability to support streaming payments by combining Metronome and Tempo, allowing you to get paid the instant value is delivered and cost incurred.
- You can now track credit balances at industry-leading rates, get instant low-balance alerts, and configure automatic credit top-ups.
- We previewed support for three new types of Billing customizations, allowing you to programmatically define how subscription items appear on invoices, how prorations behave, and how balances and credits are applied.
- We previewed payment plans that you can use to accept installment payments with automated collection, giving your customers more flexibility and improving cash flow.
- We previewed subscription invoice revisions, so you can edit finalized subscription invoices and automatically void the original invoice.
Stripe Tax
- You can now automate US tax filing, track status, and view filing details in the Stripe Dashboard, powered by TaxJar.
- We previewed additional Stripe Tax Connectors for Shopify and NetSuite, so you can extend Tax to platforms where you already do business.
- We previewed the ability for Tax to verify tax IDs against government databases during checkout flows, blocking invalid IDs.
- Payment Intents API users can now calculate and record tax on a payment with a single parameter—no separate API calls required.
- Businesses located in Liechtenstein and Mexico and digital sellers in Sri Lanka can now use Tax. We will also offer full support for businesses in Malaysia and remote sellers in French and Spanish territories soon.
Data
- We previewed the ability to retrieve real-time subscription metrics within AI agents using the Stripe MCP, or within Stripe Console.
- We previewed Stripe Database, giving you real-time Stripe data in a managed, hosted, read-only Postgres database. You can spin up the database with one click from the Dashboard or a single CLI command, allowing you to build and ship applications faster.
- We previewed the next generation of Stripe Data Pipeline, enabling real-time data syncs to Google Sheets with more data destinations coming soon.
- You can now sync all of your Stripe data directly to Databricks with Data Pipeline.
- We previewed the ability for you to programmatically retrieve prebuilt financial reports across accounts in your organization using the Reports API v2.
- We previewed the ability for businesses using Stripe Sigma to execute custom SQL queries programmatically for advanced data modeling and reporting with the Reports API v2.
Money Management
The AI economy is growing at breakneck speed, and more companies have a global footprint from day one. But the tools to manage your money haven’t kept up, with finances typically scattered across half a dozen apps and spreadsheets. We previewed new capabilities to help you store, spend, and manage money—including a Stripe card that rewards you for spending, free transfers to other Stripe Treasury users, and MCP support for Treasury APIs so you can build your own financial agents. Here’s what’s new:
Stripe Atlas
- We announced the ability for Atlas founders to track and receive SAFE funding from investors via ACH, wire transfer, or stablecoin transfer with a Treasury financial account.
Stripe Treasury
- We announced that for US and UK businesses, Treasury will support storage in 15 currencies by the end of the year.
- You can now instantly transfer funds between US businesses on Stripe for free.
- US users can now spend their settled Stripe earnings with a Stripe card powered by Mastercard, with 2% cashback on purchases.
- We announced that Treasury balances in the US will earn Stripe credits that you can apply toward your processing fees.
- You can now see a full view of balances, transactions, cards, and spending directly from your phone with the new mobile experience for Treasury within the Stripe app.
- We announced that Treasury will be available in Australia and Canada by the end of the year. We will also add stablecoin support for an additional 41 markets.
- We announced that Treasury balances will soon be backed by noncustodial wallets from Privy, enabling businesses in more than 150 markets to instantly move money across borders.
- We announced agent-ready financial accounts that enable agents to check balances, pay invoices, store funds, create cards, send money, and manage cash flow—with human-in-the-loop confirmation for key actions.
Stripe Global Payouts
- We previewed expanded Global Payouts coverage, so you can send payouts to recipients in more than 100 countries in fiat and 160 countries in stablecoins.
- We previewed the ability for Global Payouts users to send USD payouts to Link users instantly.
Embedded Finance
Stripe Connect powers more than 16,000 platforms, including Shopify, DoorDash, and Substack, which collectively help 11 million businesses accept payments. Today, we shared new ways to help platforms grow as AI reshapes software, including a new growth studio that uses Stripe data to surface actionable recommendations and the ability to launch new revenue streams through Treasury and Stripe Capital. Here’s what’s new:
Stripe Connect
- We previewed the platform growth studio, which generates recommendations directly in the Dashboard to help you expand your product offerings and grow faster. It includes AI-powered margin optimization recommendations, peer benchmarking, and no-code promotional pricing campaigns for local payment methods and Instant Payouts.
- Network cost passthrough (IC++) is now available to platforms in 45 markets, including the US, Canada, UK, and EU. You can now enable IC+ pricing and prebuilt reports for your connected accounts directly in the Dashboard.
- We previewed new embedded components for your connected accounts to order Terminal hardware, scan checks, view business performance charts, and access balance or payout reconciliation reports.
- We previewed the ability for you to use Stripe Managed Risk via API, allowing platforms and banks to outsource risk management to Stripe while maintaining full control over the user experience.
- Platforms will soon be able to launch full-scale financial services with less operational overhead using Managed Risk for Treasury.
- Platforms can now use Smart Disputes to automatically compile and submit dispute evidence on behalf of their connected accounts.
- Platforms can now mitigate risk across their business with Radar, featuring 0-to-100 fraud scores for every business and transaction, AI-powered insights that explain why accounts are flagged, and a comprehensive view of account activity.
- Your connected accounts can now onboard onto your platform in one click with networked onboarding. We also previewed support for Link wallet users to onboard in one click, even if they don’t already have a Stripe account.
- Marketplaces in the US, UK, European Economic Area (EEA), and Canada can now programmatically pay out funds to sellers’ connected accounts across any of these regions with cross-border payouts.
- We previewed the ability for marketplaces that sell in Europe to continue using multiple payment providers while making unified payouts through Stripe. This will help marketplaces comply with upcoming PSD3 regulations without disrupting their multiprocessor setups.
- We previewed wallets for marketplace sellers to receive earnings, hold funds, and make on-marketplace purchases using their financial account balance.
- We previewed the ability for marketplaces to allow both sellers and customers to spend their financial account balance on the marketplace and other businesses by issuing prepaid debit cards.
- We previewed how we will use stablecoin rails to allow Connect marketplaces to instantly transfer funds to sellers in 100 additional countries.
Stripe Treasury for platforms
- You will soon be able to offer Treasury and spend cards for your users in just a few lines of code with embedded components.
- We previewed several new features available through Treasury for platforms, including bill pay, automated cash rewards, cash acceptance, check acceptance, real-time payments, and accounting integrations.
Stripe Capital for platforms
- You can now offer Capital to your connected accounts in France and Germany, with Australia and Canada coming soon.
- We previewed lines of credit, so your connected accounts can draw funds repeatedly as needed, up to an approved amount.
- We previewed the ability for platforms to underwrite a business with no Stripe payment processing history through Capital, allowing them to receive capital and onboard to Stripe Payments in one unified flow.
Stripe Issuing
- We previewed Issuing for agents, which allows businesses and agentic platforms to programmatically issue single-use virtual cards, so agents can make purchases and manage financial workflows autonomously.
- We previewed the ability to launch a live card program for humans and agents in minutes, with self-serve onboarding, prebuilt program templates, and live funds.
- We previewed consumer debit issuing, so you can offer prepaid rewards cards, disbursements, and branded cards.
Stablecoins and Crypto
Stablecoins and crypto are helping you move money faster and more affordably around the world. We introduced a new primitive from Privy to manage multichain balances with one simple API, expanded Bridge’s Open Issuance so businesses can launch and manage their own stablecoins, and launched stablecoin-backed cards for recipients to spend funds locally or globally. Here’s what’s new:
- You can now accept stablecoin payments in 32 additional markets.
- We previewed the ability for US businesses to use Stripe Crypto Onramp to support headless implementations on web and mobile, custom stablecoins issued through Open Issuance, and a separate KYC mode on transactions up to $500.
- You can now enable consumer or commercial stablecoin-backed cards in 30 countries, enabling recipients to spend their funds locally or globally.
- Via Bridge, you can now onramp and offramp in COP and GBP, in addition to USD, BRL, EUR, and MXN.
- Via Bridge, you can now move and hold USDG and Bridge-issued stablecoins, including CASH, USDSui, and USDCBL.
- Via Bridge, you can move money across additional blockchains, including Tempo, Plasma, Celo, and Sui.
- Your customers can now hold, move, and grow stablecoin balances anywhere in the world with Privy digital asset accounts.
- We announced flexible custody via Privy, allowing you to configure wallets on a wallet-by-wallet basis with both custodial and self-custodial options for global reach.
- Via Privy, you can now provision custodial wallets operated with a licensed custodian of your choice.
- Via Privy, you can now earn on idle balances by connecting them directly to curated DeFi vaults on Morpho.
- Via Privy, you can now provision wallets for agents directly from the command line and track their spending through an agent-managed dashboard.
- Via Privy, you can now use an API integration with Bridge for bank transfer onramp and offramp flows.
- Via Privy, you can now enable AI agents to invest and transact securely with programmable wallets, including trigger-based micropayments and buy, sell, and hold crypto for investment use cases.
Stripe Platform
As agents become a foundational part of how developers build and operate on Stripe, we’re investing in three areas: making Stripe extensible and programmable with primitives like custom objects; giving agents reliable tools for building, integrating, and operating on Stripe; and introducing new agentic surfaces to help you analyze and act on your Stripe data. Here’s what’s new:
- We previewed Stripe Console, an agentic execution environment built directly into the Dashboard. Ask a business question in plain language and Console returns a structured diagnosis drawn from across your Stripe products. Or, give Console a Stripe-related task, and it will carry it out, asking for confirmation before taking consequential actions.
- AI partners and developer platforms can now use the Claimable Sandboxes API to embed Stripe into their platforms. We’ve also added more test data, including product catalogs, that you can push to your live Stripe account.
- We previewed the ability to securely create and pass live API keys to your platform on behalf of your users with automated key exchanges from Stripe’s claimable sandboxes.
- We previewed custom objects, so you can model your business data and logic inside Stripe. You can define, store, and manage custom objects with typed fields, relationships, methods, and the same APIs and operational controls as native Stripe resources.
- Stripe Workflows is now generally available. We also previewed new features, including looping, third-party custom actions, prebuilt actions for Mailchimp and Slack, programmatic invocation, and support for Connect.
- We previewed the ability for app developers to build full-page, multitab experiences inside the Stripe Dashboard.
- You can now provision, manage, and bill for your entire dev stack—including hosting, databases, authentication, observability, analytics, and AI—with Stripe Projects.
- We previewed the ability to set up agent guardrails in Stripe to assign agent identities, enforce scope rules, and configure approval flows for sensitive actions.
What’s coming later this year
Today, we launched our public roadmap: an itemized list with hundreds of detailed entries through Q1 2027, covering products, features, and improvements across Payments, Revenue, Money Management, and beyond. While it’s extensive, it’s noncomprehensive—we’re moving at breakneck speed, so you’ll see us ship even more things that aren’t on the roadmap, too.
Here’s what you can expect:
Payments
- [Q2, public preview] Agents can initiate payments using a customer’s permitted payment method, without exposing the underlying credentials.
- [Q2, GA] A native Link app for iOS and Android gives buyers a single place to manage payment methods, view transaction history, and automate purchases with configurable alerts.
- [Q2, GA] Route Apple Pay payments through the local eftpos network in Australia.
- [Q2, GA] Accept Satispay for cross-border payments.
- [Q2, GA] Accept Scalapay, an Italian buy now, pay later method, for cross-border and domestic payments.
- [Q2, GA] Legal CBD businesses can use Stripe.
- [Q2, public preview] Integrate Stripe Payments directly into Aptos ONE workflows.
- [Q3, public preview] Use an off-session payments API for transactions you initiate.
- [Q3, public preview] Build session-based payment flows that bill at the granularity of usage events like token consumption and API invocations.
- [Q3, GA] Dating service businesses can use Stripe.
- [Q4, GA] Convert 13+ currencies instantly in your Stripe Payments balance—from the Dashboard or via API—in 35 markets including the US, UK, EU, CH, SG, HK, AU, and NZ.
- [Q4, public preview] Stripe Terminal supports dynamic currency conversion to present pricing in the customer’s local currency.
- [Q4, GA] Stripe Terminal supports multicapture, so merchants can partially capture an authorized payment multiple times.
- [Q4, public preview] Use Tap to Pay on Android in Japan.
- [Q2, private preview] Use Stripe Financial Connections in Canada for payments, payouts, and bank data access.
- [Q3, public preview] Use Financial Connections in Canada for payments, payouts, and bank data access.
- [Q4, GA] Use Financial Connections in Canada for payments, payouts, and bank data access.
- [Q4, GA] Crypto businesses can sign up for Stripe via the Dashboard.
Radar
- [Q2, private preview] Custom Stripe Radar models pair Stripe’s global model with your business metadata to improve fraud detection.
- [Q2, GA] Access Stripe Radar risk scores for payments processed off Stripe via API.
- [Q2, private preview] Detect and manage fraud across your Stripe Treasury accounts.
- [Q3, GA] Stripe Radar automatically adjusts your transaction block threshold when new fraud attacks arise.
- [Q4, private preview] Set a dispute rate threshold, and Stripe’s AI will auto-resolve disputes.
- [Q4, private preview] Platforms can set custom Stripe Radar thresholds for connected accounts.
Revenue
- [Q2, private preview] Write custom logic to control when and how invoices are collected, including payment method selection, timing, and whether invoices are auto-advanced or held for review.
- [Q2, GA] Collect an up-front payment for monthly subscriptions with prebilling.
- [Q2, public preview] Temporarily pause active subscriptions without canceling them.
- [Q2, public preview] Offer custom trial offers to incentivize subscription conversion.
- [Q3, private preview] Bring both product-led and sales-led go-to-market motions into a single unified billing engine with Billing support for sold contracts.
- [Q1, private preview] Sync Metronome invoices to NetSuite to manage billing and revenue reconciliation.
- [Q1, GA] Configure packages for good-better-best plans in the Metronome UI, and manage product launches across each cohort.
- [Q2, private preview] Configure discounts on payment-gated and auto-recharge credits based on spend volume, and accept ACH payments from customers.
- [Q2, private preview] Model composite charges with minimums and reference subscriptions or nested composite charges across multiple contracts.
- [Q2, private preview] Reference Stripe e-mandates for off-session charges in India.
- [Q2, private preview] Export a complete, immutable record of every rated event after invoice finalization to your data warehouse.
- [Q2, private preview] Configure per-customer alerts to evaluate on sub-minute windows, with under a minute of latency.
- [Q3, GA] Model composite charges with minimums and reference subscriptions or nested composite charges across multiple contracts.
- [Q3, GA] Businesses and agents can purchase Metronome self-serve.
- [Q3, GA] Model Reserved Instance commitments as contract-level pricing logic for GPU cloud billing.
- [Q3, GA] Issue credits and prepaid commitments in usage units rather than custom pricing units or dollar amounts—for example, giving new users 1,000 free API calls or emails.
- [Q4, private preview] Charge for usage in real time with sub-second latency using Metronome.
- [Q2, GA] Streamline e-invoicing and e-reporting compliance with a fully integrated Stripe and Billit solution.
- [Q2, public preview] Calculate tax for industry-specific needs such as parking, ticketing, and events.
- [Q2, GA] Stripe Tax automatically tracks every tax rate and rule change applied to your transactions.
- [Q3, private preview] Platforms can use application fees to separate platform fees and related sales tax on user invoices.
- [Q4, GA] Download filing-ready reports formatted to meet requirements of supported jurisdictions, with audit-ready transaction details.
- [Q4, private preview] Remit tax payments to authorities automatically via Stripe Treasury.
- [Q1 2027, public preview] Platforms can use application fees to separate platform fees and related sales tax on user invoices.
- [Q2, public preview] Sync your Stripe data to BigQuery.
- [Q3, public preview] Sync real-time Stripe data to a broad range of data destinations.
- [Q4, GA] Sync your Stripe data to BigQuery.
- [Q2, GA] Self-serve CBMP analysis and reconcile reporting more accurately with a network-reported dispute date field in Stripe Sigma.
Money Management
- [Q3, GA] Incorporate a Delaware C corporation, file 83(b) elections, retrieve your EIN, and access formation documents using the Stripe CLI Atlas plugin.
- [Q2, private preview] Send physical checks directly from your Stripe Treasury balance.
- [Q2, private preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in BRL, AUD, GBP, and NGN.
- [Q2, private preview] Add cash to your Stripe Treasury balance at participating retail stores, including Walmart.
- [Q2, public preview] Stripe Treasury users in the US can access funds 24/7 and move money faster with stablecoins.
- [Q2, public preview] Founders anywhere in the world incorporating through Stripe Atlas can instantly access a US dollar–backed Stripe Treasury account to receive funds, store money in dollar-pegged stablecoins, and send money worldwide.
- [Q2, public preview] Schedule payouts to send funds to recipients on a future date.
- [Q2, public preview] Manage your business finances directly from the Stripe Dashboard: store funds, open local accounts, convert currencies, send money, manage expenses, borrow money, and earn rewards.
- [Q3, private preview] Treasury users storing stablecoins (USDC/EURC) can fund accounts from local currency bank accounts in MXN, BRL, GBP, AUD, COP, ARS, and NGN.
- [Q3, private preview] Manage and pay bills via the Stripe Dashboard.
- [Q3, private preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in ZAR, KES, GHS, NOK, DKK, SEK, and VND.
- [Q3, public preview] Fund and send money instantly with Stripe Treasury via Real-Time Payments (RTP).
- [Q3, public preview] Receive payments revenue in 10+ currencies—including AUD, CAD, EUR, GBP, HKD, SGD, and USD—and pay out to a local currency bank account or convert instantly on Stripe.
- [Q3, public preview] Receive payments revenue in 18 currencies—including USD, EUR, GBP, AUD, CAD, HKD, and SGD—and pay out to a local currency bank account or convert instantly on Stripe.
- [Q3, GA] Configure your Stripe account to receive all incoming card and nondebit payment earnings the next day.
- [Q3, GA] Manage your business finances directly from the Stripe Dashboard: store funds, open local accounts, convert currencies, send money, manage expenses, borrow money, and earn rewards.
- [Q4, public preview] Send physical checks directly from your Stripe Treasury balance.
- [Q4, public preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in BRL, AUD, GBP, and NGN.
- [Q4, public preview] Add cash to your Stripe Treasury balance at participating retail stores, including Walmart.
- [Q4, private preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in PEN, CLP, BOB, PLN, RON, and NZD.
- [Q4, private preview] Deposit money in high-yield investment accounts backed by fiat instruments directly from the Stripe Dashboard.
- [Q4, private preview] Configure your Stripe account to receive all incoming payment earnings instantly and on a recurring basis.
- [Q4, private preview] Businesses in Australia can receive funds in multiple currencies, convert between them, and send payouts via the Dashboard.
- [Q4, GA] Fund and send money instantly with Stripe Treasury via Real-Time Payments (RTP) in the US.
- [Q4, GA] Stripe Treasury users in the US can access funds 24/7 and move money faster with stablecoins.
- [Q4, GA] Founders anywhere in the world incorporating through Stripe Atlas can instantly access a US dollar–backed Stripe Treasury account to receive funds, store money in dollar-pegged stablecoins, and send money worldwide.
- [Q4, GA] Schedule payouts to send funds to recipients on a future date.
- [Q4, GA] Raise funds for your US C corp by sending, signing, and managing SAFE notes with investors and receiving funding via ACH, wire, or stablecoin transfer.
- [Q4, GA] Receive payments revenue in 15 currencies—including AUD, CAD, EUR, GBP, HKD, SGD, and USD—and pay out to a local currency bank account or convert instantly on Stripe.
- [Q4, GA] Manage your business finances directly from the Stripe Dashboard: store funds, open local accounts, convert currencies, send money, manage expenses, borrow money, and earn perks.
- [Q4, public preview] Transfer money between accounts in an organization without routing through an external bank account.
- [Q3, GA] Send money from the US and UK to local currency bank accounts in 30 additional countries (120+ total).
- [Q3, public preview] Individuals and businesses can share payment methods with Link to receive money faster and more securely.
- [Q3, GA] Receive same-day manual payouts in EUR in the eurozone.
- [Q3, GA] Send money from the US to recipients in 160 countries instantly in stablecoins via the Dashboard or API with Global Payouts.
- [Q3, private preview] Stablecoin payouts support USDT.
- [Q4, public preview] Send money from the eurozone to local currency bank accounts in 120 countries.
- [Q4, private preview] Send money from the EU to recipients in 160 countries instantly in stablecoins via the Dashboard or API with Global Payouts.
- [Q1, GA] Get financing through Stripe Capital in Australia.
- [Q2, public preview] Access a prequalified Capital line of credit that you can draw from multiple times.
- [Q3, private preview] Capital’s maximum offer size increases from $250K to $1M.
- [Q3, GA] Get financing through Stripe Capital in Canada.
- [Q3, GA] Access a prequalified Capital line of credit that you can draw from multiple times.
- [Q4, GA] Get financing through Stripe Capital in Ireland, Spain, the Netherlands, and Belgium.
- [Q3, private preview] Use Stripe Issuing for charge card programs in Hungary and Romania, based on EUR settlement.
Embedded Finance
- [Q1, GA] Stripe-integrated identity flows support 3D face verification.
- [Q1, GA] The Stripe Dashboard shows new data on financial performance, connected account growth, compliance, and revenue opportunities.
- [Q2, public preview] The Accounts v2 API gives users a unified account per customer with a single identity and KYC across Stripe products. Collect a customer’s payment details once and reuse them, view all customer activity in one place, and expand into new Stripe products without re-onboarding.
- [Q2, GA] Existing Connect platforms get access to the Accounts v2 API, with a simpler integration, credential reuse across Stripe products, lower costs on platform fee collection, and a unified user view.
- [Q2, GA] Control whether to collect
eventually_due
requirements from your users in the Express Dashboard. - [Q2, GA] Control whether connected accounts can edit their support details by specifying permissions during onboarding and management.
- [Q2, GA] Control whether connected accounts can edit their support details by specifying permissions during onboarding and management.
- [Q2, GA] Verify
proof_of_liveness
for connected accounts via the API. - [Q2, GA] Platforms can enable connected accounts to settle in multiple currencies without requiring them to provide foreign currency bank accounts up front.
- [Q2, private preview] Verify phone and email instantly, stepping up requirements only for risky users, via API.
- [Q2, private preview] Track performance, pinpoint drop-offs, and re-engage users across your connected account onboarding funnel.
- [Q2, private preview] Monitor the verification status of your connected accounts to identify and address issues.
- [Q3, public preview] Track performance, pinpoint drop-offs, and re-engage users across your connected account onboarding funnel.
- [Q4, GA] Connected accounts can view and export balance and payout reconciliation reports directly from your platform’s dashboard.
- [Q4, GA] Define a custom start of day to control how transactions roll up and when payouts trigger.
- [Q4, GA] Verify identities in 41 additional countries, bringing global coverage to over 90%.
- [Q4, GA] A new reporting chart embedded component can display net volume and gross volume charts in your platform’s dashboard.
- [Q4, GA] The Accounts v2 API gives users a unified account per customer with a single identity and KYC across Stripe products. Collect a customer’s payment details once and reuse them, view all customer activity in one place, and expand into new Stripe products without re-onboarding.
- [Q4, public preview] Businesses can scan checks directly from your platform’s dashboard via a new embedded component.
- [Q4, public preview] Verify phone and email instantly, stepping up requirements only for risky users, via API.
- [Q4, public preview] Stripe Connect marketplaces in the EU can onboard sellers in 100+ countries and transfer digital USD (i.e., stablecoins) to their accounts. Sellers can withdraw funds instantly in stablecoins, or choose to get paid out to a local currency bank account.
- [Q4, public preview] Monitor the verification status of your connected accounts to identify and address issues.
- [Q4, public preview] Marketplaces on Connect will be able to unify payouts across multiple processors in accordance with PSD2/3 compliance in the EU and UK.
- [Q3, private preview] Marketplaces on Connect will be able to unify payouts across multiple processors in accordance with PSD2/3 compliance in the EU and UK.
- [Q2, private preview] Platforms can embed financial accounts backed by stablecoins in 100 countries.
- [Q2, private preview] Platforms in eurozone countries can offer users financial accounts to receive, store, convert, and send funds in multiple currencies; users can spend funds directly with a Stripe-issued card.
- [Q3, private preview] Connected accounts can upload, manage, and pay bills via embedded component.
- [Q3, private preview] Offer consumers a wallet to store and respend earnings, and issue customers a branded prepaid debit card—with compliance, bank relationship management, and operations handled by Stripe.
- [Q3, private preview] Platforms in Canada can offer users financial accounts to receive, store, convert, and send funds in multiple currencies; users can spend funds directly with a Stripe-issued card.
- [Q3, public preview] Platforms in the UK can offer users financial accounts to receive, store, convert, and send funds in multiple currencies; users can spend funds directly with a Stripe-issued card.
- [Q4, public preview] Platforms can offer their customers financial accounts to receive, store, convert, and send funds, including stablecoin balances, in 100 countries. Their users can withdraw to a local currency bank account or spend directly with a Stripe-issued card in 60 countries.
- [Q4, private preview] Platforms in Australia can offer users financial accounts to receive, store, convert, and send funds in multiple currencies; users can spend funds directly with a Stripe-issued card.
- [Q4, public preview] Platforms in eurozone countries can offer users financial accounts to receive, store, convert, and send funds in multiple currencies; users can spend funds directly with a Stripe-issued card.
- [Q1 2027, public preview] Offer consumers a wallet to store and respend earnings, and issue customers a branded prepaid debit card—with compliance, bank relationship management, and operations handled by Stripe.
- [Q4, private preview] Platforms new to Stripe can offer financing to their users.
- [Q4, public preview] Offer financing to users with no Stripe payment processing history.
- [Q4, GA] Platforms in France, Germany, and Australia can extend business financing to their connected accounts.
- [Q4, GA] Platforms can give businesses access to lines of credit with flexible, on-demand funding up to an approved amount.
- [Q2, private preview] Platforms can offer customizable cashback rewards on card spend to connected accounts.
- [Q3, GA] Use Stripe for processing while maintaining your own banking relationship.
- [Q3, private preview] Platforms can issue cards for connected accounts in Canada.
- [Q3, private preview] Customers can spend from their stablecoin balances held in DeFi lending protocols.
- [Q3, public preview] Issue consumer or commercial stablecoin-backed cards in 60 countries.
- [Q4, public preview] Platforms can offer consumer debit cards backed by fiat or stablecoins, with Stripe handling program management.
- [Q4, public preview] Platforms can offer customizable cashback rewards on card spend to connected accounts.
- [Q4, public preview] Customers can spend from their stablecoin balances held in DeFi lending protocols.
- [Q4, private preview] Platforms can issue cards for connected accounts in Australia.
- [Q4, private preview] Customers can choose their funding source or payment type (such as credit or debit) before completing a purchase.
- [Q2, private preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in BRL, AUD, GBP, and NGN.
- [Q3, private preview] Treasury users storing stablecoins (USDC/EURC) can fund their account from local currency bank accounts in MXN, BRL, GBP, AUD, COP, ARS, and NGN.
- [Q3, private preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in ZAR, KES, GHS, NOK, DKK, SEK, and VND.
- [Q4, public preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in BRL, AUD, GBP, and NGN.
- [Q4, private preview] Open stablecoin-backed financial accounts in 50 additional countries (150 countries total) powered by Privy noncustodial wallets.
- [Q4, private preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in PEN, CLP, BOB, PLN, RON, and NZD.
- [Q2, private preview] Offload risk and connected account loss liability for white-labeled payments and marketplaces.
- [Q3, private preview] Managed Risk protects marketplaces and platforms that process payments on behalf of their sellers.
- [Q3, private preview] Managed Risk protects marketplaces and platforms that process payments on behalf of their sellers.
- [Q3, private preview] Offer financial accounts to businesses without taking on additional risk.
- [Q4, public preview] Offer financial accounts to businesses without taking on additional risk.
- [Q4, private preview] Let your connected accounts use Stripe’s AI to auto-resolve disputes in real time
- [Q2, private preview] Assume tax liability for connected accounts by calculating and collecting taxes on their invoices.
- [Q4, public preview] Assume tax liability for connected accounts by calculating and collecting taxes on their invoices.
Crypto
- [Q2, public preview] Accept USDT as a payment currency.
- [Q3, private preview] Use stable, user-specific deposit addresses to support ongoing transactions.
- [Q3, public preview] Accept stablecoin payments from customers in 33 additional countries.
- [Q4, GA] Accept stablecoin payments from customers in 33 additional countries.
- [Q4, private preview] Accept BTC, SOL, and ETH as payment currencies.
- [Q4, private preview] Settle crypto transactions into a stablecoin balance.
- [Q1, GA] Bridge Orchestration supports fixed-output foreign exchange, so recipients receive a specified amount while Bridge automatically determines how much source currency is needed.
- [Q2, GA] Bridge supports the Abstract blockchain.
- [Q2, GA] Bridge supports USDCBL and EURC on Stellar.
- [Q2, GA] Developers can pass fees through to their customers and set fixed fees for USD virtual account onramps with Bridge Orchestration.
- [Q2, GA] Bridge supports noncustodial card funding on the Tempo, World, Linea, and Base blockchains.
- [Q2, GA] Bridge Orchestration supports first-party SWIFT payments, FedNow for USD onramps, and ACH pulls from USD virtual accounts.
- [Q3, GA] Increase stablecoin distribution with cross-chain transfers.
- [Q3, GA] Increase stablecoin distribution via permissionless onchain swaps into Open Issuance stablecoins.
- [Q3, private preview] Bridge supports opening unique EUR virtual international bank account numbers registered in the end user’s name for improved deposit reconciliation and tracking.
- [Q3, public preview] Issue consumer or commercial stablecoin-backed cards in 60 countries.
- [Q3, private preview] Spend from stablecoin balances held in DeFi lending protocols.
- [Q4, public preview] Bridge supports customer-named virtual international bank account numbers and payouts.
- [Q4, public preview] Spend from stablecoin balances held in DeFi lending protocols.
- [Q3, private preview] Crypto Onramp supports KYC sharing, eliminating duplicate verification for customers.
- [Q4, private preview] Consumers can quickly offramp their crypto to existing payment methods.
- [Q4, public preview] Embed a fiat-to-crypto onramp into your web app with embedded components.
- [Q4, private preview] The Crypto Onramp embedded component supports BTC, SOL, and ETH.
- [Q4, public preview] Crypto Onramp supports a lightweight KYC flow for reduced friction.
- [Q2, private preview] Send money on Sui and Tempo blockchains.
- [Q3, private preview] Stablecoin payouts support USDT and Tether.
- [Q4, GA] Send money on Sui and Tempo blockchains.
- [Q1, GA] Enable end users to manage their keys and wallets directly in Privy Home, a unified hub to view and control embedded wallets across apps.
- [Q1, public preview] Users will be able to earn yield on assets in their Privy wallets through DeFi protocols, and you can surface those earnings in your app.
- [Q1, GA] Introduce human review for sensitive actions, allowing teams to approve, reject, or modify transactions, policies, and wallet changes.
- [Q1, GA] Define advanced, hierarchical approval structures that reflect real organizational workflows and authorization policies.
- [Q2, private preview] Spin up and fully manage your Privy account end-to-end from the command line.
- [Q2, GA] Swap assets with a single API call directly in Privy wallets, abstracting away routing, calldata, and execution complexity.
- [Q2, private preview] Issue stablecoin-backed cards on top of your existing noncustodial wallet.
- [Q3, private preview] Move fiat assets into Privy wallets via globally available onramps.
- [Q3, private preview] Bring your own cryptographic key material as part of key reconstitution.
- [Q4, private preview] Spin up an agent with spending capabilities using a preconfigured policy set.
- [Q4, private preview] Manage corporate treasury onchain with Privy.
- [Q2, public preview] Accept stablecoin payments through Link.
- [Q1 2027, GA] Accept stablecoin payments through Link.
- [Q4, public preview] Connect marketplaces in the EU can onboard sellers in 100+ countries and transfer digital USD (i.e., stablecoins) to their accounts. Sellers can withdraw funds instantly in stablecoins, or choose to get paid out to a local currency bank account.
- [Q3, private preview] Your users can spend from their stablecoin balances held in DeFi lending protocols.
- [Q3, public preview] Issue consumer or commercial stablecoin-backed cards in 60 countries.
- [Q4, public preview] Offer a consumer debit card backed by fiat or stablecoins, with Stripe handling program management.
- [Q4, public preview] Your users can spend from their stablecoin balances held in DeFi lending protocols.
- [Q2, private preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in BRL, AUD, GBP, and NGN.
- [Q3, private preview] Treasury users storing stablecoins (USDC/EURC) can fund their account from local currency bank accounts in MXN, BRL, GBP, AUD, COP, ARS, and NGN.
- [Q3, private preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in ZAR, KES, GHS, NOK, DKK, SEK, and VND.
- [Q4, public preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in BRL, AUD, GBP, and NGN.
- [Q4, private preview] Open stablecoin-backed financial accounts in 50 additional countries (150 countries total) powered by Privy noncustodial wallets.
- [Q4, private preview] Treasury users storing stablecoins (USDC/EURC) can offramp funds to local currency bank accounts in PEN, CLP, PLN, RON, and NZD.
- [Q4, GA] Treasury users in the US can access funds 24/7 and move money faster with stablecoins.
- [Q4, GA] Founders anywhere in the world incorporating through Stripe Atlas can instantly access a US dollar–backed Stripe Treasury account to receive funds, store money in dollar-pegged stablecoins, and send money worldwide.
- [Q4, private preview] Deposit money in high-yield investment accounts backed by fiat instruments directly from the Stripe Dashboard.
- [Q4, private preview] Treasury users in the US and UK can open investment accounts directly from the Stripe Dashboard and deposit funds in high-yield DeFi instruments, in addition to traditional fiat instruments.
- [Q4, GA] Raise funds for your US C corp by sending, signing, and managing SAFE notes with investors and receiving funding via ACH, wire, or stablecoin transfer.
- [Q2, private preview] Embed financial accounts backed by stablecoins in 100 countries.
- [Q4, public preview] Platforms can offer financial accounts to receive, store, convert, and send funds, including stablecoin balances, in 100 countries. Connected accounts can withdraw to a local currency bank account or spend directly with a Stripe-issued card in 60 countries.
Stripe Platform
- [Q2, private preview] Build, test, and deploy custom logic to Stripe.
- [Q3, GA] Get support in the Stripe app via a new chat interface optimized for mobile.
- [Q3, GA] Share customer information and payment methods across your Stripe accounts.
- [Q2, GA] Create sandboxes that are accessible by everyone within your account.
- [Q1, public preview] Automate user provisioning and deprovisioning with SCIM support.
- [Q2, GA] Automate user provisioning and deprovisioning with SCIM support.
- [Q3, private preview] Monitor API traffic, rate limit usage, and integration health directly in Workbench.
Stripe moves quickly, and we pride ourselves on our responsiveness to customer needs as they emerge. It is part of our process to revise our roadmap over time, and changes should be expected. The above is intended to outline our general product direction and our priorities as they stand today. It is intended for informational purposes only, and will not be incorporated into any contract. It is not a commitment to deliver any material, code, or functionality, and should not be relied upon in making purchasing decisions. The development, release, and timing of any features or functionality described for Stripe’s products remain at the sole discretion of Stripe.
If you have manually counted these entries, or used an agent to do so, you might have noted there are 334 items here, rather than the 288 we mentioned in the introduction. First of all: if you’re this type of person, we’re hiring. And secondly: some items are double-housed, where they apply to multiple product areas, and others are listed repeatedly if they have multiple release phase milestones on the roadmap (e.g., entries for both public preview and GA).
```

---

## 2. Giving agents the ability to pay

- 日期: 2026-04-29 00:00
- 链接: https://stripe.com/blog/giving-agents-the-ability-to-pay

```
Giving agents the ability to pay
In the Sessions keynote, we talked about how agents are becoming active participants in the internet economy, and how we’re building the infrastructure to support them.
Agents have become increasingly capable in recent months, but making purchases across the internet remains difficult. While machine payments protocols are still gaining adoption, agents need to work with the payment options sellers and consumers use today.
Today we’re launching Link’s wallet for agents, built on top of Stripe’s new Issuing for agents. You can now give agents programmatic access to Link and the ability to get a one-time-use card or a Shared Payment Token (SPT), backed by the cards and bank accounts already in your wallet. The agent never gets access to your raw payment credentials.
You can review and approve each spend request from the agent on the web, or in Link’s new iOS and Android apps. This makes it easy for consumers to enable personal AI agents such as OpenClaw to make an authorized purchase on their behalf.
If you’re a developer or business building consumer-facing agents, such as personal assistants, Link’s wallet for agents removes the need to build wallet infrastructure from scratch. Link handles the abstraction across payment options your agent might need—like cards and SPTs (with stablecoins and other payment methods coming soon). It also takes care of fund flow complexity and helps you reach Link’s customer base of more than 200 million consumers.
How Link’s wallet for agents works
Imagine you are building a shopping agent that recommends apparel to your consumers. First, the consumer grants your agent access to their Link wallet via a standard OAuth flow.
Once your agent has access, it can create a spend request to get either a one-time-use card or an SPT to complete the transaction. Your agent provides context on the transaction, so the person can understand and approve the request. In both card and machine-native flows, the payment credential can be scoped with controls like amount, currency, and merchant. Support for agentic tokens, stablecoins, and other payment types are coming soon.
The consumer gets a notification and approves the spend request in Link (on the web, or in the Link iOS or Android app). Today, each request requires the person’s review before the credential is shared with your agent. We’re planning on expanding these controls to let people set spending limits, and choose when agents can act without additional approval.
After approval, Link returns the one-time-use card or SPT to your agent for it to complete the purchase. The person can track agent spending and manage connected agents directly in Link.
Stripe Issuing for agents
Link’s wallet for agents is built directly on top of Stripe’s Issuing primitives. For businesses that want to build and customize their own agentic wallets and cards, Issuing for agents gives developers access to the full set of Issuing APIs to power agentic spending and custom financial workflows for agents and their users.
Businesses can design user-facing experiences to fit their product, including onboarding, fund flows, and spending controls. They can define when and how agents move funds, set permissions at the card level, introduce fraud controls at transaction authorization, and gain visibility into historical and real-time card activity.
Issuing for agents provides the underlying infrastructure for these experiences, from single-use virtual cards and fund storage to spending controls, transaction monitoring, and advanced fraud tools. This infrastructure supports a range of use cases:
- Developers can use agents to automate their own business spend, allowing them to create programmatic workflows and recurring purchases.
- Fintech providers can embed agent-issued cards to control and reconcile spend for expense management in real time.
- Vertical SaaS platforms can issue agent cards to SMB customers, letting agents automate spend under the platform’s own brand.
- Marketplaces can issue cards to sellers, so their agents can automate supplier payments, logistics, and fulfillment purchases.
Get started
Get started today with Link’s wallet for agents, and read our docs to learn more about Issuing for agents.
```

---

## 3. How agents, digital wallets, and trust are rewriting checkout

- 日期: 2026-04-07 00:00
- 链接: https://stripe.com/blog/global-checkout-trends

```
How agents, digital wallets, and trust are rewriting checkout
Changes in the internet economy are prompting businesses to take a more tailored approach to checkout. On Stripe, 65% of transactions under $50 now happen on mobile, and shoppers are increasingly staying on their phones for higher-value purchases, too. Digital wallets cut average mobile checkout time in half, but wallet preferences vary widely by region and generation, shaping checkout design. Local payment methods are becoming a bigger driver of conversion, and offering the right one—or the right mix—can substantially improve performance.
Checkout is also being redesigned for a new kind of buyer: agents. As customers grow more comfortable with AI-assisted purchases across a range of categories, businesses are rethinking how they manage risk and convert increasingly fragmented demand.
We analyzed checkout and payment activity from nearly 20,000 B2C businesses on the Stripe network from August 2023 through February 2026, and combined those insights with Stripe-commissioned surveys to understand the latest trends in consumer preferences.
The resulting report examines how customer purchase behavior is changing, how those shifts are showing up in the checkout flow, and what they mean for businesses.
A few takeaways stand out:
1. Shoppers are increasingly making big-ticket purchases on mobile
Mobile already dominates smaller purchases, but the old habit of moving to desktop for bigger purchases is starting to fade. Stripe data shows shoppers are increasingly completing higher-value purchases on mobile, including purchases over $500. While that shift is most pronounced in APAC and EMEA—where mobile is the preferred checkout device—mobile in the US gained share across every purchase size we measured in the last two years. Canada is the outlier: shoppers there tend to switch to desktop in the $100–$249 price range, based on our data.
2. As digital wallets spread globally, wallet preference is generational and regional
Digital wallets now account for about 30% of global point-of-sale volume. In our global survey, 61% of shoppers said they would use a digital wallet. And in traditionally card-led markets like the US and Japan, they’re among the fastest-growing checkout methods.
Here, we’re seeing a generational divide.
That preference also extends across purchase sizes. In our survey, 50% of shoppers ages 18–29 said they use wallets for purchases under $25, and $33% said they use them for purchases over $250. A driving factor here is speed: Stripe data shows that using a digital wallet cuts average mobile checkout time in half.
But while wallets are becoming the default checkout layer across markets, the leading wallet still varies by region—from MB WAY in Portugal to MobilePay in Denmark to Alipay in China. Those regional differences shape how businesses design checkout. Supporting wallets is no longer enough on its own; checkout needs to reflect how people actually pay in each market. In some regions, adding Apple Pay, Google Pay, and Link might cover most checkout volume. In others, a different wallet mix might do more to improve conversion.
3. As global demand broadens, checkout expectations become more market-specific
In a YouGov consumer survey commissioned by Stripe, 45% of respondents said they had made at least one international online purchase in the past year. However, global demand doesn’t automatically translate into conversion. Businesses need to localize checkout—but even localization strategy is market-specific. What customers expect from checkout differs by market.
In some places, like Indonesia and Vietnam, payment preference is more fragmented. Consumer preferences are distributed across digital wallets, bank transfers, debit-linked apps, and other local payment methods. In these markets, localization means adapting the full checkout experience: payment method mix, currency, and the way options are presented.
In other markets, preferences are more concentrated. There, conversion depends on centering a single, dominant payment method.
Shoppers notice when checkout feels unfamiliar, and missing relevant payment methods—or showing irrelevant ones—can hurt performance. Our experiments on the Stripe network found that showing just one payment method that’s not geographically relevant can reduce conversion rates by up to 15%.
Supporting the leading method can have an outsized effect. For example, Stripe data shows that offering BLIK to customers in Poland increases checkout conversion by 46% on average, while offering Pix in Brazil increases conversion by 31% on average.
4. AI-assisted shopping and agents are starting to change the path to checkout
AI is reshaping checkout from both sides of the transaction. On the front end, shoppers are becoming more receptive to agent-assisted buying. In a survey conducted by Stripe and Visa of more than 3,500 consumers, a majority across markets said they’re open to AI agents helping them make purchasing decisions.
On the back end, AI is also changing how payment performance is managed. As automated attacks such as card testing become easier to scale, businesses often respond by tightening risk controls, which can inadvertently reject legitimate customers in the process. New payment models help balance that trade-off by evaluating more signals in real time, requesting authentication more selectively, and improving how payments are routed and retried. Stripe’s AI-driven interventions can reduce fraud by 30% without lowering conversion, by decreasing false declines and issuer rejections.
Together, these shifts are changing checkout from a simple payment step into the point where identity, intent, and authorization are verified. Product discovery and purchasing are increasingly happening inside AI interfaces, including general purpose assistants like Google Gemini and Microsoft Copilot, visual search tools such as OpenAI’s image-based shopping, and business-specific tools such as Stitch Fix Vision and Walmart’s Sparky AI shopping assistant. As a result, checkout now needs to recognize who is buying, confirm that the shopper or agent is authorized to complete the purchase, and make it easy to finish the transaction quickly.
Download the full report to see the data behind these shifts and what businesses are doing to adapt.
```

---

## 4. Insights from Shoptalk 2026: How agents are changing retail

- 日期: 2026-04-02 00:00
- 链接: https://stripe.com/blog/shoptalk-2026

```
Insights from Shoptalk 2026: How agents are changing retail
More than 10,000 retail and commerce leaders gathered in Las Vegas last week for Shoptalk 2026. Across sessions with Coach, OpenAI, Wayfair, Meta, Sephora, and others, the conversation around agentic commerce centered less on future potential and more on what’s already live: conversational assistants shaping product discovery, in-ad buying flows tightening the path to conversion, on-site agents driving brand engagement, and third-party shopping surfaces creating new ways for brands to reach and convert customers off-site.
For all the momentum, many leaders we spoke with are still working out their agentic strategy. In conversations throughout the week, retailers described a persistent gap between what they see happening now and what they can confidently plan for next. We heard broad consensus that search and discovery have already shifted, but much less certainty about how the market will develop from here. Three themes stood out.
1. Agentic commerce is gaining traction, but retailers need a standard framework
Because agentic commerce is still early, brands are assessing where to start, who to partner with, how to structure their product data, and how that data should be syndicated across AI surfaces without an established playbook.
At the same time, the market is evolving at an unprecedented pace. In the three months since NRF, loyalty data has moved from a theoretical advantage to a live product. Sephora’s global chief digital officer described how the brand is now using loyalty data in its ChatGPT app to personalize recommendations and surface benefits like samples and free shipping.
Discovery is where the urgency feels most acute. In the Women in AI session with PwC, Klarna, Novi, and Stripe, Novi’s CEO argued that AI agents are a new storefront: if your brand is not discoverable there, it risks becoming invisible. In a keynote, OpenAI’s product partnerships lead for search and commerce said that more than half of searches on the platform are discovery-based, and 70% of those include constraints. That means shoppers aren’t just typing in keywords; they’re entering context-rich prompts around scenarios like planning a trip to Greece, organizing a Super Bowl party, or comparing appliances.
For businesses, that raises the question of what a product needs to look like to be found by agents. In Tapestry’s session with Stripe, the company’s SVP of global digital product and omnichannel innovation emphasized the importance of direct product feeds, which give agents more structured, up-to-date product data than web crawling alone. Stripe’s Agentic Commerce Suite is helping leading retailers syndicate their product catalogs across supported agents—without requiring separate integrations.
Many retailers we talked to are taking a similar test-and-learn approach, running experiments to track how their products are being found, recommended, and purchased across AI surfaces.
2. Agents are extending beyond the chat window
Agentic commerce and its primitives are showing up across a widening set of surfaces, each with its own level of maturity and its own path from discovery to conversion. This shift is expanding into native checkout, customer service, and the behind-the-scenes systems that shape whether a customer can find, buy, and receive the right product smoothly.
Meta offered one example with a new Facebook checkout flow—built on the Agentic Commerce Protocol (ACP)—that takes shoppers from an ad click to product details, AI-generated review summaries, and the option to purchase without leaving the app. Though not every embedded checkout flow is agentic, it reflects a broader shift toward more embedded commerce.
In a session on the future of retail, Shoptalk’s head of content and insights predicted a new wave of consumer brands will be built natively on agentic infrastructure, helped by lower customer acquisition costs and less reliance on their own websites as the main entry point. AI startups exhibiting at Shoptalk covered every layer of the commerce stack, from catalog enrichment and discovery to post-purchase.
Agentic commerce will not be defined by one LLM or channel. As more category-specific apps are being built across fashion, beauty, home decor, and beyond, retailers are choosing whether to invest limited time and resources into first-party or third-party agentic experiences.
3. In an AI world, brand matters more than ever
When AI makes discovery and product comparison easier, trust and brand affinity need to do more of the work in convincing shoppers to choose your brand.
That theme ran through Shoptalk sessions. New Balance’s president and CEO talked about building customer preference through consistency, rather than constant sales. The company invested over $25 million in store updates in 2025, and is training store associates to explain technical products in more detail to reinforce credibility among customers. Tapestry pointed to Coach’s ongoing research on Gen Z as part of the brand’s continued relevance over time. Victoria’s Secret’s CEO suggested that customers are increasingly drawn to store experiences that feel comforting and confidence-building, a dynamic she referred to as the “soothing economy.” And Stitch Fix’s CEO described Stitch Fix Vision—a new AI-powered visualization tool for personalized outfit discovery built on the company’s deep first-party client data.
As agentic commerce accelerates, the infrastructure behind the brand experience will have to work across more surfaces. Retailers will need unified customer data and systems that can carry identity and context across channels.
How Stripe can help
In agent-driven journeys, customers often arrive at checkout ready to buy and less willing to tolerate friction. That makes payment performance key. Stripe’s Optimized Checkout Suite dynamically surfaces payment methods most likely to convert based on more than 100 signals. Businesses see a 2%–3% increase in conversion on average after adopting Stripe’s optimized payment surfaces, demonstrating how better payment method presentation, fraud decisions, and checkout flow can drive revenue.
New agentic flows still depend on the same fundamentals that drive retail performance today: fast, branded checkout; the right payment methods; strong fraud controls; and unified commerce data. By connecting those systems across online, in-store, and in-app channels, Stripe makes it easier to deliver more personalized, consistent experiences wherever customers interact with your brand.
With the Agentic Commerce Suite, businesses can connect their catalog and commerce infrastructure once, then extend into compatible agents and surfaces as they emerge.
To learn more about the Agentic Commerce Suite, sign up for the waitlist and read our integration guides.
```

---

## 5. How Stripe Radar helps prevent free trial abuse

- 日期: 2026-03-24 00:00
- 链接: https://stripe.com/blog/how-stripe-radar-helps-prevent-free-trial-abuse

```
How Stripe Radar helps prevent free trial abuse
Earlier this month, we analyzed hundreds of millions of transactions across Stripe to identify first-party fraud trends. One of the biggest findings: free trial abuse is rapidly accelerating. From November 2025 to February 2026, our models detected 6.2x more abusive free trials across Stripe’s network.
Free trial abuse isn’t new, but users are increasingly targeting AI companies and driving much of the increase we’re seeing today. These businesses run on expensive compute resources and rely on free trials to acquire customers, making them a target for abuse.
Bad actors have become as sophisticated at stealing compute as they have money, cycling through trials or signing up with invalid payment methods without ever converting to paid subscriptions. This puts AI companies at risk of losing hundreds of thousands of dollars. AI startups are particularly impacted: those that offer free trials with self-serve signups and direct API access see 10x more attempted abuse than enterprise AI companies.
However, these fraud patterns aren’t limited to just one industry. We’re seeing similar free trial abuse across SaaS platforms, marketplaces, and other businesses that offer free trials.
Helping prevent free trial abuse in one click
Stripe Radar, our AI-powered fraud tool, now helps prevent free trial abuse with just one click. When enabled, Radar predicts the presence of abusive behavior that violates common trial terms, such as repeated trial signup or missed cancellations, with 90% accuracy. We also introduced a new analytics page that shows all high-risk payments that are blocked. For businesses that have not yet enabled the control, the analytics page shows which payments would have been blocked.
Our free trial abuse solution is powered by a new AI model trained on payment instrument (such as cards), device, and payment history across the entire Stripe ecosystem. For example, we can see if a certain card has been used on converted free trials before, and whether that card has led to a successful or failed charge. We have an industry-leading understanding of bank identification number (BIN) ranges, which helps us identify virtual card brands, and we know if email domains are new or temporary. This information helps us detect high-risk patterns including suspicious session timing and card characteristics that correlate with nonpayment.
AI companies such as Cursor are already using Radar to prevent free trial abuse. By identifying fraudulent actors at signup, the Cursor team can block high-risk trials before bad actors drive up their compute costs.
In the first 2 months, across 4 high-growth AI businesses, we blocked more than 550,000 free trials with a high risk of abuse, preventing an estimated $4.4 million in downstream losses from compute costs.
Identifying first-party fraud for all industries
Our free trial abuse solution is available to all businesses, making Radar more effective at identifying and blocking first-party fraud regardless of your industry or business model.
If you are interested in using our free trial abuse control, email us at trial-abuse-prevention@stripe.com for early access. To hear more about how Radar is adapting to additional fraud types, join us at Stripe Sessions.
```

---

## 6. Three of the biggest fraud trends from MRC Vegas 2026

- 日期: 2026-03-20 00:00
- 链接: https://stripe.com/blog/three-fraud-trends-from-mrc-vegas-2026

```
Three of the biggest fraud trends from MRC Vegas 2026
Earlier this week, more than 2,000 payments leaders gathered at the Merchant Risk Council (MRC) Vegas 2026 conference to discuss new fraud patterns, authentication strategies, and agentic commerce. One theme emerged: fraud has become more automated and increasingly difficult to detect with traditional tools.
The most sophisticated fraud teams are responding by shifting from one-size-fits-all fraud approaches to more dynamic, tailored interventions. They are removing friction for trusted users, embedding fraud detection directly into agentic transactions, and investing in multilayered identity verification to combat deepfakes.
Here’s how leading enterprises are evolving their fraud strategy.
1. Successful fraud teams are dynamically authenticating users based on intent
Many businesses add authentication requirements universally to all customers or businesses, to increase the likelihood of finding every bad actor. The cost of this approach is often underestimated, said Roberta Del Monte Radford, payment risk operations lead, strategy and innovation at Airbnb, during her session on connecting refund fraud and reseller fraud. A false positive leads to a declined transaction and losing the potential lifetime value of a legitimate customer.
Her proposed alternative is to build a behavioral picture of each user over time and use it to understand intent—what she calls high-trust velocity. And if you can gauge intent with precision, you can strategically introduce authentication requirements to some users, but not all.
“If we have high-trust velocity, why would we put that entity through friction? We don’t need to; we know they’re good, so they don’t need any friction whatsoever. We’ll reserve the friction package to the 1% of the traffic that actually is proven to be risky,” said Del Monte Radford.
Stripe is building with this principle in mind. Stripe Radar’s adaptive 3DS applies friction dynamically, using AI to assess risk level and only triggering an authentication challenge when something looks unusual. Businesses on Stripe have seen an over 30% reduction in fraud on eligible transactions, representing one of our largest ever improvements.
2. Agentic commerce is challenging rules-based fraud detection
Ashley Furniture has built a sophisticated rules-based fraud operation. The company handles both products that ship within a few days alongside custom orders that take more than 30 days to manufacture; each type of order requires a different authorization cycle. That infrastructure works when humans are managing the process, but Ashley Furniture’s team realized its fraud strategy needed to evolve when it launched its agentic commerce offering.
“Rule-based fraud detection was not going to be sufficient,” said Kyle Dorcas, head of product management at Ashley Global Retail, during his session on building payments and fraud infrastructure for AI agents. “We firmly believe that in order to combat fraud, [detection] really has to be in the payment fabric.”
When agents are making purchases across channels, fraud detection can’t evaluate transactions after the fact. Instead, fraud detection has to be embedded in the payment infrastructure itself, adapting in real time to patterns that static rules can’t anticipate.
Stripe’s Shared Payment Tokens allow AI agents to initiate payments using a buyer’s saved payment method without exposing payment credentials. When used with Stripe Radar, they also relay underlying risk signals in real time—including likelihood of fraudulent dispute, card testing, stolen card use, and issuer declines—helping differentiate between high-intent agents and low-trust automated bots.
3. Deepfakes and synthetic identities require new fraud tactics
Producing a convincing fake identity used to require criminal infrastructure, specialist knowledge, and meaningful effort. That barrier is largely gone. Bad actors now have easy access to templates for driver’s licenses, bank statements, utility bills, and government IDs. Generative AI has also accelerated impersonation capabilities. Gordon Sheppard, head of fraud operations at H&R Block, demonstrated this during his session on strengthening identity verification to combat ecommerce fraud. Using a single still photo, a 30-second audio clip, and about 20 minutes of work, he generated a convincing video of himself speaking fluent Mandarin, Italian, and Russian. The same tools are available to anyone.
Gordon says identity verification now depends on finding the anomalies fraudulent actors can’t get perfectly right every time, such as an incorrect signature or a mirror-image headshot. He shared an example where everything on a fraudulent license was flawless except one detail: the expiration date didn’t match what the authoritative data source had on file for that license. The implication, Gordon argued, is that no single check is sufficient because a convincing forgery will fail somewhere.
With Stripe Identity, businesses can programmatically confirm the identity of global customers to prevent attacks from bad actors. We can detect fake IDs and spoofed photos with AI, match the ID photo with selfies of the document holder, and validate SSN and addresses against global databases.
To learn more about how Stripe can help your business fight fraud, contact us or sign up for an account.
```

---

## 7. Testing the impact of Adaptive Pricing across 1.5M subscription checkout sessions

- 日期: 2026-03-19 00:00
- 链接: https://stripe.com/blog/adaptive-pricing-for-subscriptions

```
Testing the impact of Adaptive Pricing across 1.5M subscription checkout sessions
Subscription businesses are more global than ever, driven in large part by the growth of AI companies. But as they expand into more markets, setting the right price in the right currency is still incredibly complex.
Localizing even a one-time purchase is difficult: because exchange rates move, keeping prices localized requires businesses to absorb foreign exchange (FX) risk, pay conversion fees, and continually manage price lists across currencies, while also taking on the ongoing finance and accounting work of adjusting, reconciling, and reporting on those changes over time.
Subscriptions add another layer of complexity. Localizing a subscription means keeping pricing predictable across every billing cycle, even as exchange rates fluctuate. Consistency is especially important for recurring purchases, where small, unexpected changes can cause a customer to cancel. Renewals are also more likely to fail when the charge is processed cross-border rather than in a local currency. In 2025, 80% of subscription transactions were still priced in the business’s default currency.
To address these challenges, Adaptive Pricing for subscriptions is now available as part of the Optimized Checkout Suite, so businesses can automatically present prices in a customer’s local currency while Stripe handles the currency conversion and the operational work behind it. Adaptive Pricing supports both subscription signups and subsequent renewals and includes a stability buffer that helps keep renewal amounts consistent across billing cycles, despite changes in exchange rates. For example, a customer who signs up at R$49.60/month in Brazil continues to see R$49.60 each month, instead of a different amount every time their bank converts from USD.
If rates move significantly, renewal amounts for that billing cycle may be adjusted to reflect the latest exchange rate—similar to the experience customers have today with their card issuers.
Measuring the impact of Adaptive Pricing on subscriptions
To understand how localized pricing affects subscription performance, we analyzed 1.5 million subscription checkout sessions across businesses in our private preview, comparing sessions that offered Adaptive Pricing with a 1% randomized holdback group. We evaluated both session-level outcomes, which capture the total value generated per checkout session, and subscription-level outcomes, which capture the total value of the subscription over time, including the initial transaction and renewals.
We analyzed the impact of Adaptive Pricing at signup and through the first three months:
At signup:
- Conversion rate
- Authorization rate
Over time:
- Subscription duration per session
- Subscription lifetime value (LTV) per session
Adaptive Pricing improves subscription signup performance
At signup, offering Adaptive Pricing increased conversion by 4.7% on average and authorization by 1.9% on average across sessions. In practice, that means more customers made it to payment, and more of those payments were approved—together increasing the number of successful subscription signups.
Those gains also carried through to downstream outcomes, including a 5.4% increase in LTV per session on average. Results varied across businesses, with some seeing increases of more than 30%. Runway, for example, saw a 14% increase in LTV per session, and subscriptions using Adaptive Pricing generated 17.7% more LTV per subscription.
People are more likely to complete a purchase when they see prices in a currency they immediately recognize and understand, without needing to mentally convert the total cost. Localized pricing can make subscriptions feel more transparent, since customers are committing to an ongoing charge rather than a one-time payment.
Charging in local currency also improves payment performance. Cross-border transactions are more likely to be declined, so presenting and charging in a customer’s local currency can increase the likelihood that the payment is approved. In the sessions we analyzed, offering Adaptive Pricing increased authorization rates by 1.9%, helping more subscription purchases go through at signup.
Taken together, these results show that Adaptive Pricing helps convert more checkout sessions into paying subscriptions, leading to more subscription LTV per session.
Higher signup conversion can translate into more value over time
In addition to the stronger signup performance, customers who paid in their local currency consistently showed higher retention than those who paid in a business’s default currency. This suggests that localized pricing can support continued renewals, beyond the initial signup.
That has implications for customer lifetime value. When more customers start subscriptions—and more of those subscriptions remain active, as successful renewals add up—the value of each subscriber grows. Even modest improvements in conversion and payment success can increase subscriber value over time.
Scale subscriptions globally with localized pricing
Businesses that don’t localize prices are likely leaving revenue behind. Our analysis shows that Adaptive Pricing helps subscription businesses capture more of that revenue by showing prices in a customer’s local currency, increasing conversion, improving authorization at signup, and driving more value from every checkout session.
It also means businesses don’t need to build and maintain their own FX infrastructure, localized price lists, and renewal logic across currencies. More than 500,000 businesses, including 16,000+ subscription companies like Cursor, Perplexity, and Runway, already use Adaptive Pricing to offer subscription pricing in local currencies to customers worldwide.
To learn more about Adaptive Pricing for subscriptions, read our docs or get in touch.
```

---

## 8. Introducing the Machine Payments Protocol

- 日期: 2026-03-18 00:00
- 链接: https://stripe.com/blog/machine-payments-protocol

```
Introducing the Machine Payments Protocol
AI is evolving from question-and-answer chatbots to autonomous agents that can make comprehensive plans, execute actions, and evaluate outcomes. We believe agents will become an integral part of the internet economy, and they need the ability to transact with businesses and one another.
However, the tools of the current financial system were built for humans, so agents struggle to use them. Making a purchase today can require an agent to create an account, navigate a pricing page, choose between subscription tiers, enter payment details, and set up billing—steps that often require human intervention.
To help eliminate these challenges, we’re launching the Machine Payments Protocol (MPP), an open standard, internet-native way for agents to pay—co-authored by Tempo and Stripe. MPP provides a specification for agents and services to coordinate payments programmatically, enabling microtransactions, recurring payments, and more.
Stripe users can accept payments over MPP in a few lines of code using our PaymentIntents API. Businesses can then accept payments directly from agents, in stablecoins as well as fiat with cards and buy now, pay later payment methods via Shared Payment Tokens (SPTs).
MPP is already powering new agentic business models on Stripe. Browserbase, a browser infrastructure provider, now lets agents spin up headless browsers and pay per session. PostalForm helps agents pay to print and send physical mail. Prospect Butcher Co. lets agents order sandwiches for human pickup or delivery to anywhere in New York City. And agents can now programmatically contribute to Stripe Climate.
“Parallel is built for a world where agents are the primary users of the web. We integrated machine payments with Stripe in just a few lines of code, and now agents can autonomously pay per API call for web access. This allows us to reach any agent developer in the world on the same Stripe stack we already run on,” said Parag Agrawal, founder of Parallel Web Systems.
How MPP works
An agent can request a resource from a service, API, Model Context Protocol (MCP), or any HTTP addressable endpoint, and the service responds with a payment request. The agent authorizes the payment, and the resource is delivered to the agent.
For Stripe businesses, these payments appear in the Stripe API and Dashboard like any other transaction; the funds settle into a business’s existing balance, in their default currency, and on their standard payout schedule. The same Stripe infrastructure businesses rely on for human payments can work for agents, including tax calculation, fraud protection, reporting, accounting integrations, and refunds.
Building for the agent economy
Agents represent an entirely new category of users to build for—and increasingly, sell to. Stripe is building a broad set of agentic financial infrastructure to enable these important new patterns, via our Agentic Commerce Suite, Agentic Commerce Protocol (ACP), MCP integrations, and payment support for both MPP and x402.
To get started with MPP using Stripe, read our docs and sign up for early access.
```

---

## 9. 10 things we learned building for the first generation of agentic commerce

- 日期: 2026-03-12 00:00
- 链接: https://stripe.com/blog/10-lessons

```
10 things we learned building for the first generation of agentic commerce
A future where we buy with AI agents feels inevitable. Making it actually work is another story. The moment agents meet live product catalogs, inventory, fraud systems, and customer support queues, sellers quickly run into a long list of real-world edge cases to solve for.
Over the past six months, we launched the Agentic Commerce Protocol (ACP), an open checkout specification that lets buyers, AI agents, and sellers transact through APIs; introduced a complete agentic solution with the Agentic Commerce Suite; integrated businesses such as Etsy and URBN; and powered AI shopping experiences across agents. That’s given us an insider’s view into what matters in production, from the unglamorous integration work to the failure modes we’ve seen early adopters grapple with.
These lessons from the first generation of agentic commerce are meant to help sellers decide what to tackle first, avoid common bottlenecks, and be proactive about what’s coming.
1. Getting product catalog syndication right is the biggest up-front time-saver
Your product catalog is the entry point to agents, but different AI agents want your data in different formats. One needs an SFTP file drop. Another wants a custom API integration. A third has its own feed spec entirely. We’ve seen brands reformat the same product catalog in six different ways to get listed across multiple AI agents. It creates an ongoing maintenance burden that’s a drag on time and resources.
We’ve heard frustration from sellers about having to build (and rebuild) custom integrations for every agent. It’s why we designed the Agentic Commerce Suite: to prevent catalog fragmentation and support the full transaction lifecycle, from discovery to checkout. Upload your product catalog data to Stripe, and we syndicate it across supported agents. No duplicate work or reformatting required.
In practice, getting “ingestion-ready” product data is what determines whether you show up reliably across agent surfaces.
2. Always-on agents raise the bar for real-time responsiveness
Formatting your catalog is the starting point. Sellers are also increasingly focused on avoiding data lag. When a potential customer is looking at a specific product in an agentic channel, the agent needs to verify it’s in stock right now, not 15 minutes ago. One platform recently asked us if inventory verification happens down to the millisecond, underscoring how close to real time agents must confirm availability before showing customers a checkout option.
This gets even more complicated when you add variants to the mix, which are difficult to format in a way that agents can reliably understand. Take a shirt where the shopper can choose a size, a color, and even add custom embroidery. Or consider a sneaker in 14 different colorways, each with its own size availability. In cases like these, agents will need real-time checks to confirm that a specific item or combination is actually in stock, or to know when to prompt the customer with alternative options.
We worked with partners like OpenAI to stress-test the ACP against market complexity. With your Stripe-hosted ACP endpoint (via the Agentic Commerce Suite), you can share availability with AI agents in the checkout API call. As agentic commerce scales, real-time systems will be key for customer trust and brand reputation.
3. Protocol change is inevitable: Interoperability is the hedge
Since we codeveloped ACP with OpenAI in September 2025, we’ve shipped four releases and added payment handlers, scoped tokens, extensions (starting with discounts), built-in buyer auth, and native MCP transport. That protocol work is important, but sellers can’t afford to rebuild their stack every time a protocol changes. We built the Agentic Commerce Suite as a protocol-agnostic commerce layer that works across standards, including Google’s UCP, so sellers don’t have to bet their roadmap on any single spec.
The businesses we talk to are wary of building zombie integrations: something they ship for a specific AI agent that becomes obsolete six months later after a strategic pivot. Unless you want to staff a team dedicated to tracking protocol changes, you need a partner that can absorb that volatility. Integrate with Stripe once, and we’ll keep you compatible across agents as protocols evolve.
4. Payments are just one piece of being agent-ready
One key link between agents and existing payment rails is the token layer. To enable agentic transactions, the Agentic Commerce Suite handles and processes Shared Payment Tokens (SPTs), a payment primitive built for agentic commerce that allows agents to initiate payments with a buyer’s permission and preferred payment method, without exposing credentials. For many retailers, especially large enterprises, this token layer is where Stripe adds particular value. They need infrastructure that makes agentic transactions possible in the first place: secure, scoped tokens that let agents transact on behalf of buyers.
But agentic transactions aren’t only about the payment. There are multiple steps that have to work correctly in the flow: catalog discovery, checkout state management, shipping, and post-sale details such as returns and refunds. Stripe has a part in all of them.
We’re playing an open source role by bringing a protocol into the world alongside OpenAI. But we’re also building the business layer on top, providing fraud tools, onboarding of businesses, catalog management, and more, so businesses can support agent-driven commerce end to end, not just at the moment of payment.
5. Fraud looks different when agents are buying
One of the most common questions we hear from sellers is about whether we’re seeing an uptick in fraud as agentic commerce grows in volume. The answer is reassuring: since launching the Agentic Commerce Suite with major retailers like Coach, Kate Spade, and Ashley Furniture, fraud rates have been near zero.
Traditional fraud detection relies on signals tuned to human traffic: everything from browser fingerprinting and mouse movements to device battery level and window size. Those signals vanish in an agentic world where there’s no human buyer on the frontend. Instead, we leverage the density of the Stripe network. Even if an agentic purchase is “new” to a given business, the end customer and their payment method likely aren’t new to Stripe, which gives an immediate source of history and risk context.
By using SPTs (described above), Stripe Radar can apply the same scrutiny to agentic transactions as it does to direct checkout flows, even when authorization happens off-Stripe. The result is enterprise-grade fraud protection that works without needing weeks of seller-specific data history.
6. Start with targeted products and roll out in phases
Don’t flip the switch on your entire catalog. One approach we’ve seen work is to start with a focused set of SKUs you believe will convert, so you can measure performance and watch how the channel actually behaves. When starting out, stick to straightforward products that ship directly to the buyer’s home (nothing that requires installation or complex fulfillment coordination) as the frontend user experience develops.
URBN, the parent company of Anthropologie, Free People, and Urban Outfitters, sells everything from plants to custom furniture. When launching agentic commerce, the brand focused on a subset of its most popular products (dresses and denim) that would provide value early.
For sellers, the early phase of agentic commerce means being strategic about which SKUs, payment methods, and fulfillment options you enable first. Think of it as gathering data so you can scale intelligently. The good news is that the scope of what’s possible is expanding quickly. In time, agents will enable new buying experiences beyond single-item, single-business carts. Starting small positions sellers to take advantage of those capabilities as they go live.
7. Agentic commerce is more than a new distribution channel
Early retail happened in store. First-wave ecommerce happened on your site. Mobile maintains your brand’s look and feel. Agentic commerce shifts buying intent onto AI surfaces. That changes how sellers need to think about discovery, brand control, dispute resolution, and trust.
It also demands a strategic reframe. Agents often sit between the seller and the customer; they’re helping people discover products and decide where to buy. “Showing up” starts to look less like launching a new channel and more like work you already do for SEO and performance marketing: making sure you’re easy to find and choose. Commerce has always been about meeting customers where they are. It’s the “where” (and who controls it) that’s shifting.
Visibility isn’t the only challenge. Once an agent is in the loop, the messy parts of commerce don’t go away, but they pop up in different places. If an agent confirms an order but a legacy backend rejects it after a fraud check, how do you notify the customer? If a customer returns to an AI surface and says, “Cancel my order,” does the agent reliably route that request to the seller? We’re working with sellers and our AI partners to anticipate these issues and build solutions proactively.
8. Identity resolution is the new checkout friction
The logged-in state is the holy grail for sellers. It allows them to recognize customers across sessions and channels, personalize experiences, and apply benefits such as loyalty and saved preferences. Right now, most agentic commerce still behaves like a guest checkout: the agent acts as proxy, and the customer’s identity isn’t revealed until the moment they hit “buy.” Identity signals exist, but sellers have to do a lot of manual work to capture what’s available and map it into existing customer and order management systems.
As a result, brands we talk to are struggling to honor loyalty benefits, apply targeted discounts, and attribute conversion (or diagnose abandoned carts) with the same fidelity they’re used to. And as agents get better at making timely, relevant recommendations, the decision to buy can happen faster. If checkout then forces extra steps (whether that’s a click-out to a business’s site or additional confirmation and form-fills), sellers risk losing that intent.
It’s one reason we’re continuing to improve Link, a digital wallet built by Stripe. For returning Link customers, shipping and payment details are already saved, so checkout is faster. Link can also give agents a safer way to complete purchases without exposing a shopper’s personal or payment details.
Over time, as the agentic ecosystem matures, we expect to see loyalty programs plug in, more complex fulfillment options supported, and upgrades to post-purchase engagement.
9. First-party and third-party agentic experiences serve different needs
A recurring question we’re hearing from sellers: should you build a first-party agentic experience (like a brand-owned assistant on your site or app), or lean into third-party agentic commerce on external AI agents? In practice, this isn’t an either-or decision so much as a measurement challenge. The two approaches show up in different points in the customer journey.
First-party agents, such as NikeAI, Magic Apron from Home Depot, or Ask Ralph from Ralph Lauren, are primarily about engagement. They deepen relationships with known customers, preserve brand control, and make it easier to maintain customer context like identity and preferences. Third-party agent surfaces are largely about acquisition. They meet customers where they already are and help capture net-new demand. We’ve seen this dynamic emerge early on with Etsy, for example.
There’s an opportunity to design for both. Use first-party agentic experiences to improve retention and lifetime value, and treat third-party surfaces as a new distribution surface that can bring customers to your owned channels over time.
10. Agents-to-agent payments are emerging
Most of what we’ve covered here is everyday checkout, where a person decides to buy and pays through familiar rails. In parallel, we’re starting to see agents pay other services directly, per request, while they’re completing a task. That’s outside the standard ACP flow. It’s not a checkout session with shipping, loyalty, and a human confirmation step. It’s typically a fast, programmatic payment inside an HTTP call.
Agents also don’t pay like humans. They might make thousands of small decisions a day and need low-latency, HTTP-native payments for pay-per-call or pay-per-task business models. Builders tell us they want to charge agents directly for things like tool usage, data access, or automated workflows, but the existing tooling is mostly built around human checkout.
To help bridge the gap, we previewed machine payments using stablecoins on Stripe. With a few lines of code, you can use the PaymentIntents API to charge agents for things such as API usage, MCP calls, or HTTP requests. You specify the amount and currency, then Stripe generates a unique deposit address for that transaction.
From there, you return the deposit address to the agent, so it can pay programmatically. In an x402 flow, for example, the protocol passes the address back to the agent so it knows exactly where to remit payment. You can track status via API, webhooks, or the Stripe Dashboard, and funds settle into your Stripe balance. We’re starting with support for x402 using USDC on Base, with more protocols coming.
We’re already seeing early examples, like charging agents per API call for inventory, pricing, delivery quotes, or pick-up-slot holds, and charging per task for automation such as fitment checks, bundle building, quote generation, or replenishment. This isn’t common in traditional retail yet, and today it’s stablecoin-based, but it points to where agent-native monetization can go as protocols and rails mature.
What’s next
Agentic commerce is changing fast. In the near future, agents, humans, and businesses will be able to transact as reliably as today’s checkout, with richer context and better controls. Stripe is building the economic infrastructure for that future.
As agents start buying, selling, and coordinating work on our behalf, we want it to be easy for any business to show up on AI surfaces and get paid reliably. If you already use Stripe for payments, you’re well positioned as agentic commerce expands.
To get there, we’re continuing to improve the Agentic Commerce Suite: pushing more real-time updates, expanding SPT support to more payment methods, strengthening fraud signals as new vectors emerge, and building the identity resolution logic that helps sellers recognize customers across agentic surfaces. In addition, as agentic commerce becomes more global, we’re investing in broader geographic coverage and support for new verticals.
To learn more about how we’re expanding our agentic commerce solutions, join us at Stripe Sessions.
```

---

## 10. Analyzing first-party fraud trends: Account, free trial, and refund abuse

- 日期: 2026-03-10 00:00
- 链接: https://stripe.com/blog/analyzing-first-party-fraud-trends-account-free-trial-and-refund-abuse

```
Analyzing first-party fraud trends: Account, free trial, and refund abuse
From November 2025 to February 2026, we detected a significant increase in abusive free trials across Stripe’s network.
This is part of a broader shift toward first-party fraud, where legitimate users abuse policies by setting up multiple accounts, cycling through free trials, or exploiting refunds. In fact, 62% of merchants have experienced an increase in disputes due to first-party fraud over the past year. Managing it costs businesses $35 for every $100 in disputes.
Businesses facing these losses ask us the same questions: is first-party fraud increasing industry-wide as much as it is for my business? What can we do about it?
We analyzed hundreds of millions of transactions across the Stripe network to find answers. We identified three of the fastest growing types of first-party fraud, each occurring at a distinct point in the customer lifecycle: account abuse at sign-up, free trial abuse during product evaluation, and refund fraud after a customer has already received goods or services.
Here’s what we found about the prevalence of each and how Stripe Radar, our AI-powered fraud product, can help protect your business.
Account abuse is especially costly for AI companies, where expensive compute costs are tied directly to usage
One in five consumers admit to using different email addresses or contact information to access promotions and discounts multiple times—rising to 29% of Gen Z and 27% of millennials, according to 451 Research’s Voice of the Connected User Landscape: Connected Customer, Trust and Privacy 2025. This behavior, known as account abuse or multi-account abuse, occurs when a single person creates several accounts to repeatedly abuse free trials, use promotional coupons over and over again, or use their multiple accounts to spread stolen card use and avoid detection for longer.
The fraud pattern forms a giant web with a single payment method identifier getting attached to dozens, if not hundreds, of emails, IP addresses, and names.
Any business that offers something valuable—a free trial or a free perk with a new account—can be a target. But AI companies are particularly impacted.
Based on a Stripe analysis, 7.4% of customer sign-ups at AI companies are implicated in suspected multi-account abuse. AI tools run on compute resources, which makes multi-account abuse especially costly. Users might breach a business’s terms to create multiple accounts to get repeated access to free tiers or perks that come with new account sign-ups, such as free tokens. When a bad actor spins up five accounts instead of one, they consume five times the compute resources.
In response, we are rolling out a new Radar feature to help you evaluate potential abuse during customer account registration and login events. You can see which new sign-ups are real customers, who might be likely to convert to a paid subscription, rather than fraudulent actors looking to repeatedly exploit new account perks. Sign up for early access.
Free trial abuse is accelerating, driven by AI companies and the legitimate use of virtual cards
Free trials are necessary for customer evaluation, but they can be abused by users who violate common trial terms, such as cycling through multiple trials to get prolonged free access to a product or service.
We found that this type of abuse is accelerating for two reasons: AI companies’ free trial acquisition strategies and the breakdown of traditional prevention methods that businesses have previously relied on.
- AI companies face acute exposure. Free trial abuse isn’t new, but AI companies are driving much of the increase we’re seeing today. These businesses run on expensive compute resources and rely on free trials to acquire customers, making them especially vulnerable to abuse. In fact, AI startups that offer free trials with self-serve sign-ups and direct API access see 10x more attempted abuse than enterprise AI solutions.
- Traditional prevention methods no longer work. In an effort to reduce free trial abuse, businesses used to block high-risk payment methods such as virtual cards at sign-up. However, today, many virtual cards are legitimately used by customers for privacy and security. Blanket blocking them means rejecting legitimate sign-ups and hurting conversion rates. This leaves AI companies in a bind: they need free trials for customer acquisition, but those trials create financial exposure that traditional fraud tools weren’t designed to address.
Radar launched a new solution that predicts common free trial terms abuse with 90% accuracy. We also introduced a new analytics page that shows all high-risk payments that are blocked. For businesses that have not yet enabled the control, we show which payments would have been blocked if you had turned it on. Email us at trial-abuse-prevention@stripe.com for early access.
Refund abuse costs businesses worldwide $100 billion each year
Many retailers offer generous refund policies to stay competitive and improve the customer experience. However, lenient policies can be abused, with customers falsely claiming items never arrived or are defective in order to receive a refund—and keep the product. It’s an expensive problem: we estimate that global losses from refund abuse reach approximately $100 billion each year.
Customers might buy expensive clothing, wear it for a short time, and then return it—behavior known as “wardrobing.” According to the National Retail Federation’s 2025 Retail Returns Landscape report, 27% of shoppers that returned at least 1 online purchase in a 12-month period admitted to wardrobing, and that increased to 49% for Gen Z shoppers.
Retailers tell us that social media has amplified this behavior: influencers might purchase large shopping hauls for content and then return the clothes once the video is created. Retailers absorb the cost on both ends—two-way shipping, processing fees, and markdowns on items they may no longer be able to sell as new.
There are also more sophisticated operations. We’ve seen bad actors use more than 100 email variations and multiple payment cards to systematically exploit refund policies, such as “no questions asked” refund policies. When retailers implement refund limits, like charging a fee for frequent returns, these bad actors simply create new accounts with different cards to bypass the restrictions.
In both cases, there are real customers with valid payment credentials making genuine purchases. This makes it very difficult to detect refund abuse at the point of transaction; the fraud only becomes apparent later, once the refund is processed.
We are actively building solutions to help businesses identify and prevent refund abuse. Please contact us at refund-abuse-prevention@stripe.com to be part of the preview for this feature.
What we’re building to help
Our goal is to equip businesses on Stripe with tools to identify, reduce, and monitor first-party fraud and abuse. We process billions of transactions across millions of businesses, which gives us visibility into comprehensive fraud patterns, such as repeat abusers, networks of fake accounts, and emerging tactics. We plan to continue using our existing AI infrastructure and Radar’s capabilities to extend fraud protection to first-party fraud.
To hear more about how Radar is adapting to additional fraud and abuse vectors, join us at Stripe Sessions.
```

---
