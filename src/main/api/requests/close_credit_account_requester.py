from http import HTTPStatus

import requests
from requests import Response

from src.main.api.models.close_credit_request import CloseCreditRequest
from src.main.api.models.close_credit_response import CloseCreditResponse
from src.main.api.requests.requester import Requester


class CloseCreditRequester(Requester):
    def post(self, credit_account_request: CloseCreditRequest) -> CloseCreditResponse | Response:
        url=f"{self.base_url}/credit/repay"
        response = requests.post(
            url=url,
            json=credit_account_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return CloseCreditResponse(**response.json())
        return response