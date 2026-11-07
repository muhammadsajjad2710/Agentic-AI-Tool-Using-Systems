from src.engine import score
def test_benchmark():
    good = score(["search docs", "draft answer"], ["search", "write"], True)
    assert good["pass"]
    bad = score(["do everything"], ["shell"], False)
    assert bad["pass"] is False
