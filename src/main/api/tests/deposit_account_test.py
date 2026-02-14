import pytest
from src.main.api.models.deposit_account_request import DepositAccountRequest


@pytest.mark.api
class TestDepositAccount:
    def test_deposit_account_valid(self, api_manager, create_user_request):

        """1) Создание банковского счета"""
        response = api_manager.user_steps.create_account(create_user_request)

        account_id = response.id
        assert response.balance == 0

        """2) Пополнение банковского счета"""

        deposit_account = DepositAccountRequest(accountId=account_id, amount=7000)
        deposit_response = api_manager.user_steps.deposit_account(deposit_account)

        assert deposit_response.balance == 7000
        assert deposit_response.id == account_id




    @pytest.mark.parametrize(
        "amount",[
            999,
            9001
        ]
    )
    def test_deposit_account_invalid(self, amount, api_manager, create_user_request):

        """1) Создание банковского счета"""

        response = api_manager.user_steps.create_account(create_user_request)

        account_id = response.id
        assert response.balance == 0

        """2) Пополнение банковского счета"""

        deposit_account = DepositAccountRequest(accountId=account_id, amount=amount)
        api_manager.user_steps.deposit_account_invalid(deposit_account)

