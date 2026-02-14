import pytest
from src.main.api.models.close_credit_request import CloseCreditRequest
from src.main.api.models.credit_account_request import CreditAccountRequest


@pytest.mark.api
class TestCloseCreditAccount:

    def test_close_credit_account_valid(self, api_manager, create_credit_user_request):

        """1) Создание банковского счета пользователем с ролью CREDIT"""

        credit_account = api_manager.user_steps.create_credit_account(create_credit_user_request)

        assert credit_account.balance == 0
        account_id = credit_account.id


        """2) Проверка что пользователь создан"""

        users = api_manager.admin_steps.get_user()

        assert any(u.username == create_credit_user_request.username for u in users)

        """3) Запрос на получение кредита"""

        credit = CreditAccountRequest(accountId=account_id, amount=5000, termMonths=12)
        credit_response = api_manager.user_steps.credit_request(credit)

        assert credit_response.amount == 5000
        credit_id = credit_response.creditId

        """4) Погашение кредита"""

        close_credit_account = CloseCreditRequest(creditId=credit_id, accountId=account_id, amount=5000)

        response = api_manager.user_steps.close_credit(close_credit_account)

        assert response.amountDeposited == 5000

    def test_close_credit_account_invalid(self, api_manager, create_credit_user_request):

        """1) Создание банковского счета пользователем с ролью CREDIT"""

        credit_account = api_manager.user_steps.create_credit_account(create_credit_user_request)

        assert credit_account.balance == 0
        account_id = credit_account.id

        """2) Проверка что пользователь создан"""

        users = api_manager.admin_steps.get_user()

        assert any(u.username == create_credit_user_request.username for u in users)

        """3) Запрос на получение кредита"""

        credit = CreditAccountRequest(accountId=account_id, amount=5000, termMonths=12)
        credit_response = api_manager.user_steps.credit_request(credit)

        assert credit_response.amount == 5000
        credit_id = credit_response.creditId

        """4) Погашение кредита"""

        close_credit_account = CloseCreditRequest(creditId=credit_id, accountId=account_id, amount=4999)

        api_manager.user_steps.close_credit_invalid(close_credit_account)
