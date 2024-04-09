from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
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

    page.pause()

    logout_button = page.locator("#logout_sidebar_link")
    logout_button.click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
