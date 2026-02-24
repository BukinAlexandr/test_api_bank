import pytest
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.fixtures.user_fixture import create_user_request
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestUserLogin:
    @pytest.mark.parametrize("login_user_request", [LoginUserRequest(username="admin", password="123456")])
    def test_login_admin(self, api_manager, login_user_request):

        response = api_manager.admin_steps.login_user(login_user_request)

        assert login_user_request.username == response.user.username
        assert response.user.role == "ROLE_ADMIN"
        users = api_manager.admin_steps.get_user()
        assert any(u.username == login_user_request.username for u in users)


    def test_login_user(self, api_manager, create_user_request):

        user_resp = api_manager.admin_steps.login_user(create_user_request)

        assert user_resp.user.username == create_user_request.username
        assert user_resp.user.role == "ROLE_USER"
        users = api_manager.admin_steps.get_user()
        assert any(u.username == create_user_request.username for u in users)

