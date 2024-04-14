from playwright.sync_api import Playwright, sync_playwright, expect
from saucedemo.src.pages.LoginPage import LoginPage
from saucedemo.src.pages.ProductListPage import ProductListPage
from saucedemo.src.pages.CartPage import CartPage
from saucedemo.src.pages.CheckoutPage import CheckoutPage


def test_place_order(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    # Login
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(products_p._products_header).to_have_text("Products")

    product_name = 'Sauce Labs Fleece Jacket'
    checkout_p = products_p.click_add_to_cart_or_remove(product_name).click_card_icon().click_checkout_btn().enter_checkout_details("F1", "F2", "123141421").click_continue().click_finish_btn()

    expect(checkout_p.get_confirm_msg()).to_have_text("Thank you for your order!")