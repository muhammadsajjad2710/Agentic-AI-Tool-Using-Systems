from src.engine import purchase
def test_rules():
    assert purchase("pens", 20, 500)["ok"]
    assert purchase("laptop", 200, 150)["error"] == "over_budget"
    assert purchase("chair", 120, 500)["error"] == "approval_required"
    assert purchase("chair", 120, 500, approved=True)["ok"]
