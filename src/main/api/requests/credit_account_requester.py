from http import HTTPStatus

import requests
from requests import Response

from src.main.api.models.credit_account_request import CreditAccountRequest
from src.main.api.models.credit_account_response import CreditAccountResponse
from src.main.api.requests.requester import Requester


class CreditAccountRequester(Requester):
    def post(self, credit_account_request: CreditAccountRequest) -> CreditAccountResponse | Response:
        url=f"{self.base_url}/credit/request"
        response = requests.post(
            url=url,
            json=credit_account_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return CreditAccountResponse(**response.json())
        return response