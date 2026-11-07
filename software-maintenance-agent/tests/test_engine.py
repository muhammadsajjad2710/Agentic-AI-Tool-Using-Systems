from src.engine import apply_if_tests_pass
def test_gated_patch():
    good = apply_if_tests_pass("def add(a,b):\n    return a+b\n", lambda ns: exec("assert ns['add'](1,2)==3", {"ns": ns}))
    # simpler validator
    def ok(ns):
        assert ns["add"](1, 2) == 3
    assert apply_if_tests_pass("def add(a,b):\n    return a+b\n", ok)["applied"]
    def fail(ns):
        assert ns["add"](1, 2) == 0
    assert apply_if_tests_pass("def add(a,b):\n    return a+b\n", fail)["applied"] is False
