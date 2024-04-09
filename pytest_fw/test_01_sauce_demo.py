import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

# @pytest.mark.xfail(reason="BUG 666")


@pytest.mark.regression
def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(slow_mo=1000)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name666").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "User unable to login"

    context.close()
    browser.close()


# @pytest.mark.skip(reason="Not want")


@pytest.mark.sainty
def test_logout(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(slow_mo=1000)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "User unable to login"

    burger_menu = page.locator("#react-burger-menu-btn")
    burger_menu.click()

    logout_button = page.locator("#logout_sidebar_link")
    logout_button.click()

    context.close()
    browser.close()
