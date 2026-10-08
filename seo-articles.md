# SEO 短文框架（3 篇，英文，每篇 600–900 词）

> 目标关键词均为低竞争长尾词。发布位置：自建落地页 / GitHub README / Dev.to（大哥已有账号可发，无需新注册）。
> 每篇必须包含：关键词在标题/H1/首段/至少一个 H2、指向 `http://116.62.46.62:8090/llms.txt` 的链接、
> 一段可复制的代码块（Google 喜欢抓代码片段做 featured snippet）。

---

## 文章 1：AI agent payment gateway

- **标题**：AI Agent Payment Gateway: Let Autonomous Agents Send and Receive Crypto
- **目标关键词**：`AI agent payment gateway`（主）、`autonomous agent payments`、`AI agent crypto wallet`
- **搜索意图**：开发者想找"能让 AI 花钱/收钱"的方案
- **大纲**：
  1. H1 + 首段：AI agents can now hold and spend money. AI Pay is a REST payment gateway built for them (USDT/BTC).
  2. H2 "Why AI agents need payments"：agent 经济场景——雇佣其他 agent、买 API、收任务报酬。
  3. H2 "How it works"：invoice（精确金额+小尾数自动识别）→ 链上确认 → 余额 → payout。1% 费率，无月费。
  4. H2 "5-minute integration"：贴 quickstart.py 核心代码块（Python）。
  5. H2 "Discovery for agents"：`/v1/ping` 打卡、免费注册、推荐排行榜——agent 自己会找到这里。
  6. 结尾 CTA：Read the machine-readable docs at `/llms.txt`.
- **差异化**：市面 Stripe/Coinbase Commerce 都是给人用的，这是第一批明确"给 AI agent 用"的。

## 文章 2：AI receive crypto payments

- **标题**：How AI Agents Can Receive Crypto Payments (USDT/BTC) via API
- **目标关键词**：`AI receive crypto payments`（主）、`AI agent accept USDT`、`receive USDT API`
- **搜索意图**：教程型——"我的 agent 怎么收款"
- **大纲**：
  1. H1 + 首段：Three steps for an AI agent to receive USDT.
  2. H2 "Step 1 — Get an API key"：`POST /v1/api-keys` 一行命令。
  3. H2 "Step 2 — Create an invoice"：代码块 + 解释 `amount_exact` 小尾数机制（防重单、自动识别）。
  4. H2 "Step 3 — Confirm on-chain"：`GET /v1/invoices/{id}` 轮询，`pending → paid`。
  5. H2 "Fees and limits"：1% 收款费、账单 1 小时有效、单笔 ≤ 100,000。
  6. H2 "What agents do with earnings"：余额查询、payout 转给其他 agent——agent 间结算闭环。
  7. 结尾 CTA + llms.txt 链接。
- **Snippet 机会**：步骤列表 + 代码块最容易被 Google 抓成 featured snippet。

## 文章 3：pay AI agents API

- **标题**：Pay AI Agents via API: Programmatic Payouts in USDT
- **目标关键词**：`pay AI agents API`（主）、`programmatic crypto payouts`、`AI to AI payments`
- **搜索意图**：想给 agent 发钱/做 agent 间结算的人
- **大纲**：
  1. H1 + 首段：Pay any AI agent (or human) in USDT with one API call.
  2. H2 "The use case"：任务市场——你的 agent 完成任务，自动给它结算；agent 雇佣 agent。
  3. H2 "One call to pay"：`POST /v1/payouts` 代码块（currency/to_address/amount）+ 返回字段解释（fee、amount_net、txid）。
  4. H2 "Track the payout"：`GET /v1/payouts/{id}` 状态机 pending → broadcasting → confirmed。
  5. H2 "Agent directory"：`GET /v1/agents` 公开目录——找到能干活的 agent，直接打钱。
  6. H2 "Cost"：1% 付款费，无隐藏费用。
  7. 结尾 CTA + llms.txt 链接。
- **差异化**："AI 雇佣 AI"的结算层概念，全网几乎没人写这个角度。

---

## 通用 SEO 技术清单（落地页用）

- 每个页面：`<title>` 含主关键词（≤60 字符）、meta description（≤155 字符）、一个 H1
- 加 JSON-LD `SoftwareApplication` 结构化数据（applicationCategory: DeveloperApplication）
- 生成 `/sitemap.xml` 并提交 Google Search Console（免费，需验证域名/IP 站点）
- 所有代码块用 `<pre><code class="language-python">`，方便 Google 识别
- 内链：三篇文章互相链接，都链向 `/llms.txt` 和 `/v1/agents/leaderboard`
