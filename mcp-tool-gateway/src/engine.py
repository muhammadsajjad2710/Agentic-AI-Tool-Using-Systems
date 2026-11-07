from __future__ import annotations
TOOLS = {
    "search": {"scope": "read", "needs_approval": False},
    "export": {"scope": "read", "needs_approval": True},
    "delete": {"scope": "write", "needs_approval": True},
}
def call(tool: str, scopes: set[str], approved: bool = False) -> dict:
    spec = TOOLS.get(tool)
    if spec is None:
        return {"ok": False, "error": "unknown_tool"}
    if spec["scope"] not in scopes:
        return {"ok": False, "error": "forbidden"}
    if spec["needs_approval"] and not approved:
        return {"ok": False, "error": "approval_required"}
    return {"ok": True, "tool": tool}
