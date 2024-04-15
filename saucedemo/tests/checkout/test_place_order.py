from playwright.sync_api import expect

from saucedemo.src.pages.LoginPage import LoginPage


def test_place_order(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    # Login
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(products_p._products_header).to_have_text("Products")

    product_name = 'Sauce Labs Fleece Jacket'
    checkout_p = products_p.click_add_to_cart_or_remove(product_name) \
        .click_cart_icon() \
        .click_checkout_btn() \
        .enter_checkout_details("Fn12", "Ln12", "00110707") \
        .click_continue() \
        .click_finish_btn()

    expect(checkout_p.get_confirm_msg()).to_have_text("Thank you for your order!")