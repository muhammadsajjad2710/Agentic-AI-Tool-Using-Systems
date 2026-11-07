from src.engine import call
def test_scope_and_approval():
    assert call("search", {"read"})["ok"]
    assert call("delete", {"read"})["error"] == "forbidden"
    assert call("export", {"read"})["error"] == "approval_required"
    assert call("export", {"read"}, approved=True)["ok"]
