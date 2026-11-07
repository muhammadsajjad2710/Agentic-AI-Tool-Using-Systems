from __future__ import annotations
def purchase(item: str, amount: float, budget: float, approved: bool = False, threshold: float = 100) -> dict:
    if amount > budget:
        return {"ok": False, "error": "over_budget"}
    if amount > threshold and not approved:
        return {"ok": False, "error": "approval_required"}
    return {"ok": True, "item": item, "amount": amount}
