import pytest
from src.main.api.models.deposit_account_request import DepositAccountRequest

@pytest.mark.api
class TestDepositAccount:
    def test_deposit_account_valid(self, api_manager, account, account_snapshot):
        b1, n1 = account_snapshot(account.id)

        api_manager.user_steps.deposit_account(
            DepositAccountRequest(accountId=account.id, amount=7000)
        )

        b2, n2 = account_snapshot(account.id)
        assert b2 == b1 + 7000
        assert n2 == n1 + 1

    @pytest.mark.parametrize("amount", [999, 9001])
    def test_deposit_account_invalid(self, amount, api_manager, account, account_snapshot):
        b1, n1 = account_snapshot(account.id)

        api_manager.user_steps.deposit_account_invalid(
            DepositAccountRequest(accountId=account.id, amount=amount)
        )

        b2, n2 = account_snapshot(account.id)
        assert b2 == b1
        assert n2 == n1


