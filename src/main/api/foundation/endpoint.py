from enum import Enum

from src.main.api.models.account_transactions_response import AccountTransactionsResponse
from src.main.api.models.base_model import BaseModel
from typing import Optional, Type
from dataclasses import dataclass
from src.main.api.models.close_credit_request import CloseCreditRequest
from src.main.api.models.close_credit_response import CloseCreditResponse
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.credit_account_request import CreditAccountRequest
from src.main.api.models.credit_account_response import CreditAccountResponse
from src.main.api.models.credit_history_response import CreditHistoryResponse
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.deposit_account_response import DepositAccountResponse
from src.main.api.models.get_users_response import GetUsersResponse
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.models.transfer_account_response import TransferAccountResponse


@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]

class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model = CreateUserRequest,
        url = "/admin/create",
        response_model = CreateUserResponse
    )

    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model = None,
        url = "/admin/users",
        response_model = None
    )

    ADMIN_GET_USER = EndpointConfiguration(
        request_model = None,
        url = "/admin/users",
        response_model = list[GetUsersResponse]
    )

    LOGIN_USER = EndpointConfiguration(
        request_model = LoginUserRequest,
        url = "/auth/token/login",
        response_model = LoginUserResponse
    )

    CREATE_ACCOUNT = EndpointConfiguration(
        request_model = None,
        url = "/account/create",
        response_model = CreateAccountResponse
    )

    DEPOSIT_ACCOUNT = EndpointConfiguration(
        request_model = DepositAccountRequest,
        url = "/account/deposit",
        response_model = DepositAccountResponse
    )

    TRANSFER_ACCOUNT = EndpointConfiguration(
        request_model = TransferAccountRequest,
        url = "/account/transfer",
        response_model = TransferAccountResponse
    )

    CREDIT_ACCOUNT = EndpointConfiguration(
        request_model = CreditAccountRequest,
        url = "/credit/request",
        response_model = CreditAccountResponse
    )

    CLOSE_CREDIT_ACCOUNT = EndpointConfiguration(
        request_model = CloseCreditRequest,
        url = "/credit/repay",
        response_model = CloseCreditResponse
    )

    ADMIN_CREATE_CREDIT_USER = EndpointConfiguration(
        request_model=CreateCreditUserRequest,
        url="/admin/create",
        response_model=CreateUserResponse
    )

    ACCOUNT_TRANSACTIONS = EndpointConfiguration(
        request_model=None,
        url="/account/transactions/{id}",
        response_model=AccountTransactionsResponse
    )

    CREDIT_HISTORY = EndpointConfiguration(
        request_model=None,
        url="/credit/history",
        response_model=CreditHistoryResponse
    )


