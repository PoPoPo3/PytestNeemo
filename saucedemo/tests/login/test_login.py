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


def test_login_with_invalid_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'invalid_user', 'password': 'secret_sauce'}
    # Login
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    expected_fail_msg = "Username and password do not match any user in this service"

    expect(login_p._error_massage).to_contain_text(expected_fail_msg)


def test_login_with_empty_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    # Login
    login_p = LoginPage(page)
    login_p.click_login()

    expected_fail_msg = "Username is required"
    expect(login_p.err_msg_loc).to_contain_text(expected_fail_msg)


def test_access_inventory_without_login(set_up_tear_down) -> None:
    page = set_up_tear_down
    page.goto("https://www.saucedemo.com/inventory.html")
    login_p = LoginPage(page)
    expect(login_p.err_msg_loc).to_contain_text("You can only access '/inventory.html' when you are logged in.")
