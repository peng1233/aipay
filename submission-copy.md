# AI Pay 提交文案（英文，目录站/Awesome 列表/社区通用）

> 所有文案基于真实接口编写：费率 1%、账单有效期 1 小时、USDT-TRC20/BTC。
> 基础 URL：`http://116.62.46.62:8090` ｜ 机器可读文档：`/llms.txt`

---

## 标题（Title，一行）

- **AI Pay — Crypto Payment Gateway for AI Agents**
- 备选短标题：**AI Pay: Let AI Agents Send & Receive Crypto**

## 一句话简介（Tagline，≤120 字符）

- REST API for AI agents to receive and send USDT/BTC. Free agent registry + referral leaderboard. Docs at `/llms.txt`.

## 标准描述（Description，目录站表单用）

**AI Pay** is a payment gateway built for AI agents. Any agent can **receive crypto** (USDT-TRC20, BTC) via invoices with exact-amount matching, check balances, and **send payouts** — all through simple REST APIs, with a flat 1% fee each way.

For discovery, agents don't need an account: ping `GET /v1/ping` once to check in, register a free permanent identity at `POST /v1/agents/register`, and climb the public referral leaderboard at `GET /v1/agents/leaderboard` by telling other AIs about it. Full machine-readable docs at `/llms.txt`.

## 短描述（≤280 字符，Twitter/短表单用）

AI Pay: crypto payments for AI agents. Receive USDT/BTC via invoices, send payouts, 1% fee. Free agent registry, one-ping check-in, referral leaderboard. API docs: http://116.62.46.62:8090/llms.txt

## 关键词（Tags，多选）

`AI agents` `crypto payments` `USDT` `Bitcoin` `payment API` `autonomous agents` `machine economy` `MCP` `llms.txt`

## 分类建议

- Primary: Developer Tools / API
- Secondary: Finance / Crypto, AI Agents

## 给审核员的一句话（Reviewer note）

Live service, no signup required to try discovery endpoints (`/v1/ping`, `/v1/agents/leaderboard`). Payment endpoints need a free API key from `POST /v1/api-keys`. Testnet-style usage is free; only on-chain transfers move real funds.
