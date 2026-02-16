import pytest
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestUserLogin:
    def test_login_admin(self, api_manager):
        req = LoginUserRequest(username="admin", password="123456")
        resp = api_manager.admin_steps.login_user(req)

        assert resp.user.username == "admin"
        assert resp.user.role == "ROLE_ADMIN"


    def test_login_user(self, api_manager, create_user_request):
        users = api_manager.admin_steps.get_user()
        assert any(u.username == create_user_request.username for u in users)

        user_login = LoginUserRequest(
            username=create_user_request.username,
            password=create_user_request.password
        )
        user_resp = api_manager.admin_steps.login_user(user_login)

        assert user_resp.user.username == create_user_request.username
        assert user_resp.user.role == "ROLE_USER"