from src.engine import run
def test_drops_unsafe_urls():
    out = run("climate")
    assert out["sources"]
    assert all(s.startswith("https://") for s in out["sources"])
