from src.engine import safe_eval
import pytest
def test_math_and_block():
    assert safe_eval("2 + 3 * 4") == 14
    with pytest.raises(ValueError):
        safe_eval("__import__('os').system('echo hi')")
