import pytest

@pytest.mark.api
class TestCloseCreditAccount:
    def test_close_credit_account_valid(self, api_manager, issued_credit, close_credit_request_factory):
        req = close_credit_request_factory(
            issued_credit["credit_id"],
            issued_credit["account_id"],
            issued_credit["amount"]
        )

        resp = api_manager.user_steps.close_credit(req)
        assert resp.amountDeposited == issued_credit["amount"]

        history = api_manager.user_steps.get_credit_history()
        credit = next(c for c in history.credits if c.creditId == issued_credit["credit_id"])
        assert credit.balance == 0

    def test_close_credit_account_invalid(self, api_manager, issued_credit, close_credit_request_factory):
        req = close_credit_request_factory(
            issued_credit["credit_id"],
            issued_credit["account_id"],
            issued_credit["amount"] - 1
        )

        api_manager.user_steps.close_credit_invalid(req)

        history = api_manager.user_steps.get_credit_history()
        credit = next(c for c in history.credits if c.creditId == issued_credit["credit_id"])
        assert credit.balance != 0

