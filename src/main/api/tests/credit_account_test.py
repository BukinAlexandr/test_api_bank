import pytest
from src.main.api.models.credit_account_request import CreditAccountRequest

@pytest.mark.api
class TestCreditAccount:
    @pytest.mark.parametrize("amount, ok", [(5000, True), (4999, False)])
    def test_credit_request(self, amount, ok, api_manager, credit_account, credit_history_snapshot):
        before = credit_history_snapshot()

        req = CreditAccountRequest(accountId=credit_account.id, amount=amount, termMonths=12)

        if ok:
            resp = api_manager.user_steps.credit_request(req)
            assert resp.amount == amount

            after = credit_history_snapshot()
            assert len(after.credits) == len(before.credits) + 1
        else:
            api_manager.user_steps.credit_request_invalid(req)

            after = credit_history_snapshot()
            assert len(after.credits) == len(before.credits)







