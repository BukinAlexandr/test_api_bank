import pytest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.models.credit_account_request import CreditAccountRequest
from src.main.api.models.close_credit_request import CloseCreditRequest



@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def create_credit_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateCreditUserRequest)
    api_manager.admin_steps.create_credit_user(user_request)
    return user_request


@pytest.fixture
def account(api_manager, create_user_request):
    return api_manager.user_steps.create_account(create_user_request)


@pytest.fixture
def two_accounts(api_manager, create_user_request):
    a1 = api_manager.user_steps.create_account(create_user_request)
    a2 = api_manager.user_steps.create_account(create_user_request)
    return a1, a2


@pytest.fixture
def deposit_request(account):
    return DepositAccountRequest(accountId=account.id, amount=7000)


@pytest.fixture
def deposit_request_factory():
    def _make(account_id: int, amount: int):
        return DepositAccountRequest(accountId=account_id, amount=amount)
    return _make


@pytest.fixture
def account_deposited(api_manager, account):
    dep = api_manager.user_steps.deposit_account(
        DepositAccountRequest(accountId=account.id, amount=7000)
    )
    return {"account": account, "deposit": dep}

@pytest.fixture
def two_accounts_with_money_on_source(api_manager, two_accounts):
    src, dst = two_accounts
    api_manager.user_steps.deposit_account(DepositAccountRequest(accountId=src.id, amount=7000))
    return src, dst


@pytest.fixture
def transfer_request_factory():
    def _make(from_id: int, to_id: int, amount: int):
        return TransferAccountRequest(fromAccountId=from_id, toAccountId=to_id, amount=amount)
    return _make


@pytest.fixture
def credit_request(credit_account):
    return CreditAccountRequest(accountId=credit_account.id, amount=5000, termMonths=12)


@pytest.fixture
def credit_account(api_manager, create_credit_user_request):
    return api_manager.user_steps.create_credit_account(create_credit_user_request)

@pytest.fixture
def issued_credit(api_manager, credit_account):
    req = CreditAccountRequest(accountId=credit_account.id, amount=5000, termMonths=12)
    credit_resp = api_manager.user_steps.credit_request(req)
    return {"account_id": credit_account.id, "credit_id": credit_resp.creditId, "amount": 5000}

@pytest.fixture
def close_credit_request_factory():
    def _make(credit_id: int, account_id: int, amount: int):
        return CloseCreditRequest(creditId=credit_id, accountId=account_id, amount=amount)
    return _make


@pytest.fixture
def users_list(api_manager):
    return api_manager.admin_steps.get_user()


@pytest.fixture
def account_snapshot(api_manager):
    def _snap(account_id: int):
        resp = api_manager.user_steps.get_account_transactions(account_id)
        return resp.balance, len(resp.transactions)
    return _snap


@pytest.fixture
def credit_history(api_manager):
    return api_manager.user_steps.get_credit_history()


@pytest.fixture
def credit_history_snapshot(api_manager):
    def _snap():
        return api_manager.user_steps.get_credit_history()
    return _snap