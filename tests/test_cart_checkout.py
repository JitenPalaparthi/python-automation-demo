from playwright.sync_api import Page, expect

from tests.pages.login_page import LoginPage
from tests.pages.shop_page import ShopPage


def test_add_to_cart_and_checkout(page: Page) -> None:
    login_page = LoginPage(page)
    shop_page = ShopPage(page)

    login_page.open()
    login_page.login("student", "playwright123")
    expect(login_page.message).to_have_text("Login successful")

    shop_page.add_first_product()
    shop_page.add_second_product()
    shop_page.assert_cart_count(2)
    shop_page.checkout()
    expect(shop_page.checkout_message).to_have_text("Order confirmed for 2 item(s)")


def test_checkout_without_login(page: Page) -> None:
    login_page = LoginPage(page)
    shop_page = ShopPage(page)

    login_page.open()
    shop_page.add_first_product()
    shop_page.checkout()
    expect(shop_page.checkout_message).to_have_text("Please login before checkout")
