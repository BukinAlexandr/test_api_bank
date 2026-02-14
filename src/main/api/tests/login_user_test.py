import pytest
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestUserLogin:
    def test_login_admin(self, api_manager, create_user_request):

        """1) Авторизация админом"""

        login_user_request = LoginUserRequest(username="admin", password="123456")
        response = api_manager.admin_steps.login_user(login_user_request)

        assert login_user_request.username == response.user.username
        assert response.user.role == "ROLE_ADMIN"

        """2) Проверка списка пользователей"""

        users = api_manager.admin_steps.get_user()

        assert any(u.username == create_user_request.username for u in users)


    @pytest.mark.parametrize("create_user_request", [RandomModelGenerator.generate(CreateUserRequest)])
    def test_login_user(self, api_manager, create_user_request):

        """1) Авторизация админом и создание пользователя"""
        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

        """2) Проверка списка пользователей"""

        users = api_manager.admin_steps.get_user()

        assert any(u.username == create_user_request.username for u in users)

        """3) Авторизация созданным пользователем"""

        user_login = LoginUserRequest(
            username=create_user_request.username,
            password=create_user_request.password
        )

        user_resp = api_manager.admin_steps.login_user(user_login)

        assert user_resp.user.username == create_user_request.username
        assert user_resp.user.role == "ROLE_USER"

