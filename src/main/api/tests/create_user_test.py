import pytest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest

@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize("create_user_request", [RandomModelGenerator.generate(CreateUserRequest)])
    def test_create_user_valid(self, api_manager, create_user_request):
        resp = api_manager.admin_steps.create_user(create_user_request)

        assert resp.username == create_user_request.username
        assert resp.role == create_user_request.role

        users = api_manager.admin_steps.get_user()
        assert any(u.username == create_user_request.username for u in users)

    @pytest.mark.parametrize(
        "username,password",
        [
            ("авб", "Pas!sw0rd"),
            ("ab", "Pas!sw0rd"),
            ("abc!", "Pas!sw0rd"),
            ("Maxx1", "Pas!sw0rд"),
            ("Maxx2", "Pas!sw0"),
            ("Maxx3", "pas!sw0d"),
            ("Maxx4", "PAS!SW0RD"),
            ("Maxx5", "Password"),
        ]
    )
    def test_create_user_invalid(self, username, password, api_manager):
        req = CreateUserRequest(username=username, password=password, role="ROLE_USER")
        api_manager.admin_steps.create_invalid_user(req)

