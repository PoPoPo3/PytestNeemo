import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from saucedemo.src.pages.LoginPage import LoginPage
from saucedemo.src.pages.ProductListPage import ProductListPage


def test_logout(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    # Login
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.do_logout()

    expect(login_p.login_button).to_have_text("Login")
