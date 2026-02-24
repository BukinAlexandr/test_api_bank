import pytest

from src.main.api.models import deposit_account_request
from src.main.api.models.deposit_account_request import DepositAccountRequest


@pytest.mark.api
class TestDepositAccount:
    def test_deposit_account_valid(self, api_manager, deposit_account_request):

        deposit_response = api_manager.user_steps.deposit_account(deposit_account_request)

        assert deposit_response.balance == deposit_account_request.amount
        assert deposit_response.id == deposit_account_request.accountId
        trans = api_manager.user_steps.get_transactions(id=deposit_response.id)
        assert trans.balance == deposit_account_request.amount





    @pytest.mark.parametrize(
        "amount",[
            999,
            9001
        ]
    )
    def test_deposit_account_invalid(self, amount, api_manager, deposit_account_request):

        deposit_account = DepositAccountRequest(accountId=deposit_account_request.accountId, amount=amount)

        api_manager.user_steps.deposit_account_invalid(deposit_account)

