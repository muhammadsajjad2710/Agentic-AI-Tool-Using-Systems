from __future__ import annotations
def score(plan: list[str], used: list[str], success: bool) -> dict:
    tool_ok = used == ["search", "write"]
    plan_ok = 2 <= len(plan) <= 6
    return {"tool_use": tool_ok, "planning": plan_ok, "completion": success, "pass": tool_ok and plan_ok and success}
