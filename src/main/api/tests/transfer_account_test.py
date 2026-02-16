import pytest

@pytest.mark.api
class TestTransferAccount:
    def test_transfer_account_valid(self, api_manager, two_accounts_with_money_on_source, transfer_request_factory, account_snapshot):
        src, dst = two_accounts_with_money_on_source

        b1s, n1s = account_snapshot(src.id)
        b1d, n1d = account_snapshot(dst.id)

        api_manager.user_steps.transfer_account(
            transfer_request_factory(src.id, dst.id, 4000)
        )

        b2s, n2s = account_snapshot(src.id)
        b2d, n2d = account_snapshot(dst.id)

        assert b2s == b1s - 4000
        assert b2d == b1d + 4000
        assert n2s == n1s + 1
        assert n2d == n1d + 1

    def test_transfer_account_invalid(self, api_manager, two_accounts, transfer_request_factory, account_snapshot):
        src, dst = two_accounts

        b1s, n1s = account_snapshot(src.id)
        b1d, n1d = account_snapshot(dst.id)


        api_manager.user_steps.transfer_account_invalid(
            transfer_request_factory(src.id, dst.id, 500)
        )

        b2s, n2s = account_snapshot(src.id)
        b2d, n2d = account_snapshot(dst.id)

        assert b2s == b1s
        assert b2d == b1d
        assert n2s == n1s
        assert n2d == n1d
