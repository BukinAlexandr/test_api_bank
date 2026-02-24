import pytest

@pytest.mark.api
class TestTransferAccount:

    def test_transfer_account_valid(self, api_manager, transfer_request):
        transfer, balance = transfer_request

        response = api_manager.user_steps.transfer_account(transfer)

        assert response.fromAccountIdBalance == balance - transfer.amount
        transaction = api_manager.user_steps.get_transactions(id=transfer.toAccountId)
        assert transaction.balance == transfer.amount


    def test_transfer_account_invalid(self, api_manager, transfer_request_invalid):

        api_manager.user_steps.transfer_account_invalid(transfer_request_invalid)
