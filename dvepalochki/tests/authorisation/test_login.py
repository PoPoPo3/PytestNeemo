import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_login_with_standard_user(page) -> None:
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "User unable to login"
