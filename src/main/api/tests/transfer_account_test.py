import pytest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest

@pytest.mark.api
class TestTransferAccount:

    def test_transfer_account_valid(self, api_manager, create_user_request):

        """1) Создание первого банковского счета"""

        response = api_manager.user_steps.create_account(create_user_request)

        assert response.balance == 0
        account_one = response.id

        """2) Создание и пополнение второго банковского счета"""

        response = api_manager.user_steps.create_account(create_user_request)

        account_two = response.id
        assert response.balance == 0

        deposit_account = DepositAccountRequest(accountId=account_two, amount=7000)
        deposit_response = api_manager.user_steps.deposit_account(deposit_account)

        assert deposit_response.balance == 7000
        assert deposit_response.id == account_two

        """3) Перевод с банковского счет №1 на банковский счет №2"""

        transfer_account_request = TransferAccountRequest(fromAccountId=account_two,toAccountId=account_one,amount=4000)

        response = api_manager.user_steps.transfer_account(transfer_account_request)

        assert response.fromAccountIdBalance == 3000



    def test_transfer_account_invalid(self, api_manager, create_user_request):

        """1) Создание первого банковского счета"""

        response = api_manager.user_steps.create_account(create_user_request)

        assert response.balance == 0
        account_one = response.id

        """2) Создание и пополнение второго банковского счета"""

        response = api_manager.user_steps.create_account(create_user_request)

        account_two = response.id
        assert response.balance == 0

        deposit_account = DepositAccountRequest(accountId=account_two, amount=7000)
        deposit_response = api_manager.user_steps.deposit_account(deposit_account)

        assert deposit_response.balance == 7000
        assert deposit_response.id == account_two

        """3) Перевод с банковского счет №1 на банковский счет №2"""

        transfer_account_request = TransferAccountRequest(fromAccountId=account_two,toAccountId=account_one,amount=7001)

        api_manager.user_steps.transfer_account_invalid(transfer_account_request)
