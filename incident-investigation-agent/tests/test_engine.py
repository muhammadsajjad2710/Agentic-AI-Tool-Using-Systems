from src.engine import investigate, remediate
def test_requires_approval():
    inv = investigate("spike in 401s")
    assert remediate(inv["plan"], False)["executed"] is False
    assert remediate(inv["plan"], True)["executed"] is True
