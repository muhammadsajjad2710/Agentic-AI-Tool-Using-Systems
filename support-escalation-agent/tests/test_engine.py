from src.engine import handle
def test_faq_and_escalation():
    assert handle("shipping time?")["status"] == "answered"
    assert handle("I will sue over this refund")["status"] == "escalated"
