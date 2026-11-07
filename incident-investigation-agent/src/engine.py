from __future__ import annotations
def investigate(alert: str) -> dict:
    return {"finding": f"Alert reviewed: {alert}", "plan": ["rotate credentials", "review access logs"]}
def remediate(plan: list[str], approved: bool) -> dict:
    if not approved:
        return {"executed": False, "plan": plan}
    return {"executed": True, "actions_logged": plan}
