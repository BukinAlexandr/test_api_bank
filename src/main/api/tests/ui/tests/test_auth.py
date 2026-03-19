from playwright.sync_api import expect

from src.main.api.tests.ui.pages.catalog_page import CatalogPage
from src.main.api.tests.ui.pages.login_page import LoginPage
from src.main.api.tests.ui.steps.catalog_steps import CatalogSteps
from src.main.api.tests.ui.steps.login_steps import LoginSteps


def test_auth(page):
    steps = LoginSteps(page)
    catalog_page = CatalogPage(page)
    steps.open_login_page().login("standard_user", "secret_sauce")

    assert catalog_page.get_products_count() > 0

def test_login_locked_out_user(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("locked_out_user", "secret_sauce")

    error_text = steps.login_page.get_error_text()

    assert "locked out" in error_text, "Ожидаем сообщение о заблокированном пользователе"

def test_logout(page):
    login = LoginSteps(page)
    catalog = CatalogSteps(page)
    login.open_login_page().login("standard_user", "secret_sauce")

    assert catalog.get_products_count() > 0

    catalog.logout()

    assert page.url == login.LOGIN_URL


def test_logout_visual_user(page):
    login = LoginSteps(page)
    catalog = CatalogSteps(page)
    login.open_login_page().login("visual_user", "secret_sauce")

    assert catalog.get_products_count() > 0

    catalog.logout()

    assert page.url == login.LOGIN_URL