from __future__ import annotations
FAQ = {"hours": "We are open 9 to 5.", "shipping": "Ships in 3 days."}
def handle(message: str) -> dict:
    text = message.lower()
    if any(k in text for k in ("lawyer", "sue", "refund", "chargeback")):
        return {"status": "escalated", "queue": "human"}
    for key, ans in FAQ.items():
        if key in text:
            return {"status": "answered", "answer": ans}
    return {"status": "escalated", "queue": "human"}
