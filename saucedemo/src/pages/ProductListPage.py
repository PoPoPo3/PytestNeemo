

class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("span.title")

    @property
    def product_header(self):
        return self._product_header
