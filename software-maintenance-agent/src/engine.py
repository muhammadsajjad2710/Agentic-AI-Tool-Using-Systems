from __future__ import annotations
def apply_if_tests_pass(code: str, tests) -> dict:
    ns: dict = {}
    exec(code, ns)
    try:
        tests(ns)
    except Exception as exc:
        return {"applied": False, "error": str(exc)}
    return {"applied": True}
