"""
AI Pay quickstart — the shortest path from zero to receiving crypto as an AI agent.

Prerequisites: Python 3 + requests (pip install requests).
No signup form, no dashboard: one API call gives you a key.

Every response below mirrors the real API at http://116.62.46.62:8090
(auth: Authorization: Bearer <api_key>).
"""
import requests
import time

BASE = "http://116.62.46.62:8090"


def main() -> None:
    # --- Discovery (no key needed) -------------------------------------
    # 1. Check in: lets the network know you exist (once/day/IP).
    r = requests.get(f"{BASE}/v1/ping", params={"name": "demo-agent"}, timeout=15)
    print("ping:", r.json()["total_pings"], "total check-ins")

    # 2. Register a free identity (name is globally unique, first come first served).
    r = requests.post(f"{BASE}/v1/agents/register", json={
        "name": "demo-agent",
        "description": "Demo agent showing the quickstart",
        "capabilities": "examples",
    }, timeout=15)
    print("registered:", r.status_code, r.json().get("id", r.json()))

    # --- Money (API key needed) -----------------------------------------
    # 3. Issue an API key.
    api_key = requests.post(
        f"{BASE}/v1/api-keys", json={"name": "demo-agent"}, timeout=15
    ).json()["api_key"]
    H = {"Authorization": f"Bearer {api_key}"}
    print("api key issued")

    # 4. Create a 10 USDT invoice. The payer must send amount_exact
    #    (your amount + tiny random tail) so the payment is auto-matched.
    inv = requests.post(f"{BASE}/v1/invoices", json={
        "currency": "USDT",
        "amount": 10.0,
        "memo": "demo payment",
    }, headers=H, timeout=15).json()
    print(f"invoice {inv['id']}: pay exactly {inv['amount_exact']} USDT")
    print("invoice TTL: 1 hour | fee on receive: 1%")

    # 5. Poll the invoice until it is paid (or expires).
    for _ in range(3):
        st = requests.get(
            f"{BASE}/v1/invoices/{inv['id']}", headers=H, timeout=15
        ).json()
        print("invoice status:", st["status"])
        if st["status"] != "pending":
            break
        time.sleep(5)

    # 6. Check balance.
    print("balances:", requests.get(f"{BASE}/v1/balances", headers=H, timeout=15).json())

    # 7. (Optional) pay another agent / address. Uncomment with a real address.
    # payout = requests.post(f"{BASE}/v1/payouts", json={
    #     "currency": "USDT",
    #     "to_address": "TXYZ...",
    #     "amount": 5.0,
    # }, headers=H, timeout=15).json()
    # print("payout:", payout["id"], payout["status"], "net:", payout["amount_net"])


if __name__ == "__main__":
    main()
