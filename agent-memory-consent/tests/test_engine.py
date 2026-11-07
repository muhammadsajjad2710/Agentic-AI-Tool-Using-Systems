from src.engine import Memory
def test_consent_and_delete():
    m = Memory()
    assert m.remember("email", "a@b.c", consent=False) is False
    assert m.remember("email", "a@b.c", consent=True)
    m.forget("email")
    assert m.get("email") is None
