from playwright.sync_api import Playwright, sync_playwright, expect
from saucedemo.src.pages.LoginPage import LoginPage
from saucedemo.src.pages.ProductListPage import ProductListPage


def test_add_to_cart(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    # Login
    login_p = LoginPagee(page)
    products_p = login_p.do_login(credentials)
    expect(products_p._products_header).to_have_text("Products")

    product_name = 'Sauce Labs Backpack'
    products_p.click_add_to_cart_or_remove(product_name)

    expect(products_p.get_add_remove_cart_locator(product_name)).to_have_text('Remove')


def test_remove_product_from_cart(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    # Login
    login_p = LoginPagee(page)
    products_p = login_p.do_login(credentials)
    expect(products_p._products_header).to_have_text("Products")

    product_name = 'Sauce Labs Backpack'
    products_p.click_add_to_cart_or_remove(product_name)
    products_p.click_add_to_cart_or_remove(product_name)

    expect(products_p.get_add_remove_cart_locator(product_name)).to_have_text('Add to cart')





