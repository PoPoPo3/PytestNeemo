import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from saucedemo.src.pages.LoginPage import LoginPage


def test_login_with_standard_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    # Login
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(products_p._products_header).to_have_text("Products")


def xtest_login_with_invalid_user(page) -> None:
    page.goto("https://www.saucedemo.com/")

    # Login invalid user
    page.locator("#user-name").fill("invalid_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expected_fail_msg = "Username and password do not match any user in this service"
    err_smg_locator = page.locator("//h3[@data-test='error']")

    expect(err_smg_locator).to_contain_text(expected_fail_msg)


def xtest_login_with_empty_user(page) -> None:
    page.goto("https://www.saucedemo.com/")

    # Login empty user
    page.locator("#login-button").click()

    expected_fail_msg = "Username is required"
    err_smg_locator = page.locator("//h3[@data-test='error']")

    expect(err_smg_locator).to_contain_text(expected_fail_msg)
