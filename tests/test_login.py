from playwright.sync_api import Page, expect

from tests.pages.login_page import LoginPage


def test_successful_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("student", "playwright123")
    expect(login_page.message).to_have_text("Login successful")


def test_invalid_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("student", "wrong-password")
    expect(login_page.message).to_have_text("Invalid credentials")
