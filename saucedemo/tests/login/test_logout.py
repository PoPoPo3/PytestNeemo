import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_login_with_standard_user(page) -> None:
    page.goto("https://www.saucedemo.com/")
    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator("span.title")
    expect(products_header).to_have_text("Products")

    burger_menu = page.locator("#react-burger-menu-btn")
    burger_menu.click()

    logout_button = page.locator("#logout_sidebar_link")
    logout_button.click()

    homepage_logo = page.locator("//div[@class='login_logo']")
    expect(homepage_logo).to_contain_text("Swag Labs")
