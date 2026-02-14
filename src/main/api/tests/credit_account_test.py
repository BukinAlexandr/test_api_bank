import pytest
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.credit_account_request import CreditAccountRequest


@pytest.mark.api
class TestCreditAccount:

    def test_credit_account_valid(self, api_manager, create_credit_user_request):

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


    def test_credit_account_invalid(self, api_manager, create_credit_user_request):

        """1) Создание банковского счета пользователем с ролью CREDIT"""

        credit_account = api_manager.user_steps.create_credit_account(create_credit_user_request)

        assert credit_account.balance == 0
        account_id = credit_account.id


        """2) Проверка что пользователь создан"""

        users = api_manager.admin_steps.get_user()

        assert any(u.username == create_credit_user_request.username for u in users)

        """3) Запрос на получение кредита"""

        credit = CreditAccountRequest(accountId=account_id, amount=4999, termMonths=12)
        api_manager.user_steps.credit_request_invalid(credit)







