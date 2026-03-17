from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.message = page.locator("#login-message")

    def open(self) -> None:
        self.page.goto("/")
        expect(self.page.get_by_role("heading", name="Demo Shop")).to_be_visible()

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
