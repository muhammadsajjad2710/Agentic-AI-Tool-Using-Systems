from __future__ import annotations
class Memory:
    def __init__(self):
        self._rows: dict[str, str] = {}
    def remember(self, key: str, value: str, consent: bool) -> bool:
        if not consent:
            return False
        self._rows[key] = value
        return True
    def get(self, key: str) -> str | None:
        return self._rows.get(key)
    def forget(self, key: str) -> None:
        self._rows.pop(key, None)
