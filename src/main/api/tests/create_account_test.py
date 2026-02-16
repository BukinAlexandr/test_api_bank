import pytest

@pytest.mark.api
class TestCreateAccount:
    def test_create_account(self, account):
        assert account.id is not None
        assert account.balance == 0


