import pytest
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.credit_account_request import CreditAccountRequest


@pytest.mark.api
class TestCreditAccount:

    def test_credit_account_valid(self, api_manager, create_credit_account):

        credit = api_manager.user_steps.credit_request(create_credit_account)

        assert credit.balance == create_credit_account.amount
        credit_history = api_manager.user_steps.get_credit_history()
        assert credit_history.credits[-1].amount == credit.balance


    @pytest.mark.parametrize(
        "amount", [
            4999,
            15001
        ]
    )
    def test_credit_account_invalid(self, api_manager, create_credit_account_invalid, amount):

        credit_request = CreditAccountRequest(accountId=create_credit_account_invalid.accountId, amount=amount, termMonths=create_credit_account_invalid.termMonths)

        api_manager.user_steps.credit_request_invalid(credit_request)
