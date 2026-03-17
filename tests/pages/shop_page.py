from playwright.sync_api import Page, expect


class ShopPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_count = page.locator("#cart-count")
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.checkout_message = page.locator("#checkout-message")

    def add_first_product(self) -> None:
        self.page.get_by_test_id("add-to-cart-1").click()

    def add_second_product(self) -> None:
        self.page.get_by_test_id("add-to-cart-2").click()

    def assert_cart_count(self, count: int) -> None:
        expect(self.cart_count).to_have_text(f"Cart Items: {count}")

    def checkout(self) -> None:
        self.checkout_button.click()
