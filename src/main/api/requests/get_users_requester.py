from typing import List

import requests
from src.main.api.models.get_users_response import GetUsersResponse
from src.main.api.requests.requester import Requester


class GetUsersRequester(Requester):
    def get(self, model=None) -> List[GetUsersResponse]:
        url=f"{self.base_url}/admin/users"
        response = requests.get(
            url=url,
            headers=self.headers,
        )
        self.response_spec(response)
        return [GetUsersResponse(**item) for item in response.json()]

