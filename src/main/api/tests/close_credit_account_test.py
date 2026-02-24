import pytest


@pytest.mark.api
class TestCloseCreditAccount:

    def test_close_credit_account_valid(self, api_manager, close_credit_account):

        close_credit = api_manager.user_steps.close_credit(close_credit_account)

        assert close_credit.amountDeposited == close_credit_account.amount
        credit_history = api_manager.user_steps.get_credit_history()
        assert credit_history.credits[-1].amount == close_credit.amountDeposited


    def test_close_credit_account_invalid(self, api_manager, close_credit_account_invalid):

        api_manager.user_steps.close_credit_invalid(close_credit_account_invalid)
