from src.engine import run
def test_resume():
    first = run(["fetch", "validate", "post"], {"done": ["fetch"]})
    assert first["done"] == ["fetch", "validate", "post"]
    assert first["complete"]
