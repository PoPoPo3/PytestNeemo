import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


# @pytest.mark.xfail(reason="BUG 666")


@pytest.mark.regression
def test_01_login_with_valid_credentials(set_up_tear_down) -> None:
    page = set_up_tear_down

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "User unable to login"


@pytest.mark.sainty
def test_02_logout(set_up_tear_down) -> None:
    page = set_up_tear_down

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "User unable to login"

    burger_menu = page.locator("#react-burger-menu-btn")
    burger_menu.click()

    logout_button = page.locator("#logout_sidebar_link")
    logout_button.click()

    login_btn = page.locator("#login-button")
    assert login_btn.is_visible(), "Logout is successful"


@pytest.mark.regression
def test_01_login_with_invalid_credentials(set_up_tear_down_no_login) -> None:
    page = set_up_tear_down_no_login

    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_sauce")
    page.locator("#login-button").click()

    error_text = page.locator("//div[@class='error-message-container error']/h3")
    error_text.wait_for()
    print(error_text.inner_text())
    actual_error_text = "Epic sadface: Username and password do not match any user in this service"
    assert actual_error_text in error_text.inner_text(), "User no login"
