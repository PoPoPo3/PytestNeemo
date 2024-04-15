

class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self._first_name = page.locator("[data-test='firstName']")
        self._last_name = page.locator("[data-test='lastName']")
        self._zipcode = page.locator("[data-test='postalCode']")
        self._continue = page.locator("#continue")
        self._finish_btn = page.locator("#finish")
        self._complete_msg = page.locator("h2.complete-header")

    def enter_first_name(self, f_name ):
        self._first_name.fill(f_name)
        return self

    def enter_last_name(self, l_name ):
        self._last_name.fill(l_name)
        return self

    def enter_zip(self, zip_code):
        self._zipcode.fill(zip_code)
        return self

    def enter_checkout_details(self, f_name, l_name, zip_code):
        self.enter_first_name(f_name)\
            .enter_last_name(l_name)\
            .enter_zip(zip_code)
        return self

    def click_continue(self):
        self._continue.click()
        return self

    def click_finish_btn(self):
        self._finish_btn.click()
        return self

    def get_confirm_msg(self):
        return self._complete_msg
