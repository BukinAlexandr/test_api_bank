from typing import List, Any

from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models import create_user_request, create_credit_user_request
from src.main.api.models.close_credit_request import CloseCreditRequest
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_account_request import CreditAccountRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def __init__(self, created_obj: List[Any]):
        super().__init__(created_obj)
        self._username = None
        self._password = None

    def create_account(self, create_user_request: CreateUserRequest):
        self._username = create_user_request.username
        self._password = create_user_request.password

        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def deposit_account(self, deposit_account_request: DepositAccountRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=self._username, password=self._password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_account_request)
        return response

    def deposit_account_invalid(self, deposit_account_request: DepositAccountRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=self._username, password=self._password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(deposit_account_request)

    def transfer_account(self, transfer_account_request: TransferAccountRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=self._username, password=self._password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(transfer_account_request)
        return response

    def transfer_account_invalid(self, transfer_account_request: TransferAccountRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=self._username, password=self._password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_entity()
        ).post(transfer_account_request)

    def create_credit_account(self, create_credit_user_request: CreateCreditUserRequest):
        self._username = create_credit_user_request.username
        self._password = create_credit_user_request.password

        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_credit_user_request.username, password=create_credit_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def credit_request(self, credit_account_request: CreditAccountRequest):
       response = ValidateCrudRequester(
           RequestSpecs.auth_headers(username=self._username, password=self._password),
           Endpoint.CREDIT_ACCOUNT,
           ResponseSpecs.request_created()
       ).post(credit_account_request)
       return response

    def credit_request_invalid(self, credit_account_request: CreditAccountRequest):
       CrudRequester(
           RequestSpecs.auth_headers(username=self._username, password=self._password),
           Endpoint.CREDIT_ACCOUNT,
           ResponseSpecs.request_bad()
       ).post(credit_account_request)

    def close_credit(self, close_credit_request: CloseCreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=self._username, password=self._password),
            Endpoint.CLOSE_CREDIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(close_credit_request)
        return response

    def close_credit_invalid(self, close_credit_request: CloseCreditRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=self._username, password=self._password),
            Endpoint.CLOSE_CREDIT_ACCOUNT,
            ResponseSpecs.request_entity()
        ).post(close_credit_request)
