from saucedemo.src.pages.CheckoutPage import CheckoutPage


class CartPage:
    def __init__(self, page):
        self.page = page
        self._checkout_btn = page.locator('#checkout')

    def click_checkout_btn(self):
        self._checkout_btn.click()
        return CheckoutPage(self.page)