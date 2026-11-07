from __future__ import annotations
from urllib.parse import urlparse
def researcher(topic: str) -> list[str]:
    return [f"https://example.com/{topic.replace(' ', '-')}", "javascript:alert(1)", "ftp://files.example"]
def verifier(urls: list[str]) -> list[str]:
    ok = []
    for u in urls:
        p = urlparse(u)
        if p.scheme in {"http", "https"} and p.netloc:
            ok.append(u)
    return ok
def run(topic: str) -> dict:
    raw = researcher(topic)
    return {"sources": verifier(raw)}
