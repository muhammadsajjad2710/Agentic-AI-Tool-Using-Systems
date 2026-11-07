from __future__ import annotations
def run(steps: list[str], checkpoint: dict | None = None) -> dict:
    state = dict(checkpoint or {"done": []})
    for step in steps:
        if step in state["done"]:
            continue
        state["done"].append(step)
        state["last"] = step
    state["complete"] = state["done"] == steps
    return state
