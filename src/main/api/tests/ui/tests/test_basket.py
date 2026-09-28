from src.main.api.tests.ui.steps.basket_steps import BasketSteps
from src.main.api.tests.ui.steps.catalog_steps import CatalogSteps
from src.main.api.tests.ui.steps.checkout_steps import CheckoutSteps


def test_add_items_and_check_in_cart(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)

    catalog.login("standard_user", "secret_sauce")
    catalog.add_to_cart("Sauce Labs Backpack")
    catalog.add_to_cart("Sauce Labs Bolt T-Shirt")
    catalog.add_to_cart("Sauce Labs Fleece Jacket")

    basket.open_cart()
    basket.expect_item_in_cart("Sauce Labs Backpack")
    basket.expect_item_in_cart("Sauce Labs Bolt T-Shirt")
    basket.expect_item_in_cart("Sauce Labs Fleece Jacket")



def test_remove_items_from_cart(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)

    catalog.login("standard_user", "secret_sauce")
    catalog.add_to_cart("Sauce Labs Backpack")
    catalog.add_to_cart("Sauce Labs Bolt T-Shirt")
    catalog.add_to_cart("Sauce Labs Fleece Jacket")

    basket.open_cart()
    basket.expect_item_in_cart("Sauce Labs Backpack")
    basket.expect_item_in_cart("Sauce Labs Bolt T-Shirt")
    basket.expect_item_in_cart("Sauce Labs Fleece Jacket")

    basket.remove_item("Sauce Labs Backpack")
    basket.remove_item("Sauce Labs Bolt T-Shirt")
    basket.remove_item("Sauce Labs Fleece Jacket")

    basket.expect_item_not_in_cart("Sauce Labs Backpack")
    basket.expect_item_not_in_cart("Sauce Labs Bolt T-Shirt")
    basket.expect_item_not_in_cart("Sauce Labs Fleece Jacket")

def test_checkout_multiple_items(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)
    checkout = CheckoutSteps(page)

    catalog.login("standard_user", "secret_sauce")
    catalog.add_to_cart("Sauce Labs Backpack")
    catalog.add_to_cart("Sauce Labs Bolt T-Shirt")
    catalog.add_to_cart("Sauce Labs Fleece Jacket")

    basket.open_cart()
    basket.expect_item_in_cart("Sauce Labs Backpack")
    basket.expect_item_in_cart("Sauce Labs Bolt T-Shirt")
    basket.expect_item_in_cart("Sauce Labs Fleece Jacket")

    basket_total = basket.get_items_total_price()
    basket.checkout()
    checkout.start_checkout(first_name="Test", last_name="User", postal_code="12345")
    checkout_total = checkout.get_item_total_after_continue()

    assert checkout_total == basket_total


def test_checkout_without_items(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)
    checkout = CheckoutSteps(page)

    catalog.login("standard_user", "secret_sauce")
    catalog.add_to_cart("Sauce Labs Backpack")

    basket.open_cart()

    assert "Sauce Labs Backpack" in basket.get_item_names()

    basket.checkout()
    checkout.start_checkout(first_name="Test", last_name="User", postal_code="")

    assert checkout.get_error_text() == "Error: Postal Code is required"