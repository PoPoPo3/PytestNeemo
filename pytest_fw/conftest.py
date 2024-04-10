import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.fixture()
def set_up_tear_down(page) -> None:
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    yield page


@pytest.fixture()
def set_up_tear_down_no_login(page) -> None:
    page.goto("https://www.saucedemo.com/")
    yield page