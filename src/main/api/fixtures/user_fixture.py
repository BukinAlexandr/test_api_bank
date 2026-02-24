import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.close_credit_request import CloseCreditRequest
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_account_request import CreditAccountRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest


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
def login_user_request(api_manager, create_user_request):
    login = api_manager.admin_steps.login_user(create_user_request)
    return login

@pytest.fixture
def create_deposit_account_request(api_manager, create_user_request):
    create_account = api_manager.user_steps.create_account(create_user_request)
    return create_account

@pytest.fixture
def deposit_account_request(api_manager, create_deposit_account_request):
    depo = DepositAccountRequest(accountId=create_deposit_account_request.id, amount=7000)
    return depo

@pytest.fixture
def transfer_request(api_manager, create_user_request):

    acc1 = api_manager.user_steps.create_account(create_user_request).id
    acc2 = api_manager.user_steps.create_account(create_user_request).id

    depo = api_manager.user_steps.deposit_account(
        DepositAccountRequest(accountId=acc1, amount=7000)
    )
    balance = depo.balance

    transfer = TransferAccountRequest(fromAccountId=acc1, toAccountId=acc2, amount=4000)
    return transfer, balance

@pytest.fixture
def transfer_request_invalid(api_manager, create_user_request):

    acc1 = api_manager.user_steps.create_account(create_user_request).id
    acc2 = api_manager.user_steps.create_account(create_user_request).id

    api_manager.user_steps.deposit_account(
        DepositAccountRequest(accountId=acc1, amount=7000)
    )

    transfer = TransferAccountRequest(fromAccountId=acc1, toAccountId=acc2, amount=7001)
    return transfer

@pytest.fixture
def create_credit_account(api_manager, create_credit_user_request):

    cred_account = api_manager.user_steps.create_credit_account(create_credit_user_request)
    credit = CreditAccountRequest(accountId=cred_account.id, amount=5000, termMonths=12)
    return credit

@pytest.fixture
def create_credit_account_invalid(api_manager, create_credit_user_request):

    cred_account = api_manager.user_steps.create_credit_account(create_credit_user_request)
    credit = CreditAccountRequest(accountId=cred_account.id, amount=15001, termMonths=12)
    return credit

@pytest.fixture
def close_credit_account(api_manager, create_credit_account):

    credit = api_manager.user_steps.credit_request(create_credit_account)
    close_credit = CloseCreditRequest(accountId=credit.accountId, creditId=credit.creditId, amount=5000)
    return close_credit

@pytest.fixture
def close_credit_account_invalid(api_manager, create_credit_account):

    credit = api_manager.user_steps.credit_request(create_credit_account)
    close_credit = CloseCreditRequest(accountId=credit.accountId, creditId=credit.creditId, amount=4999)
    return close_credit

