from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # # Start tracing before creating / navigating a page.
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://dvepalochki.ru/spb/")
    page.get_by_role("button", name="OK").click()
    page.locator("[data-test-id=\"categories-tabs-item-rolls\"]").click()
    page.locator("div:nth-child(2) > .dish > .dish__wrapper > .dish__toppings > .v-dish-toppings > div > .d-flex > .v-order-button > .v-order-button--elem").first.click()
    page.locator("[data-test-id=\"dishes-item-to-cart-roll-filadelfiya-hit\"]").click()
    page.locator("[data-test-id=\"dishes-item-to-cart-roll-karamelnaya-filadelfiya1\"]").click()
    page.locator("[data-test-id=\"dishes-item-to-cart-roll-krevetkoj-avokado-i-mango-1\"]").click()
    page.locator("[data-test-id=\"header-basket-btn\"]").click()
    page.locator("[data-test-id=\"cart-modal-submit-btn\"]").click()
    page.locator("[data-test-id=\"auth-phone-input\"]").click()
    page.locator("[data-test-id=\"auth-phone-input\"]").fill("+7 (999) 888 8888")
    page.locator("[data-test-id=\"auth-submit-btn\"]").click()
    page.locator("[data-test-id=\"auth-code-input\"]").click()
    page.locator("[data-test-id=\"auth-code-input\"]").fill("8888")
    page.locator("[data-test-id=\"auth-submit-btn\"]").click()
    # page.locator("[data-test-id=\"delivery-address-input\"]").click()
    # page.locator("[data-test-id=\"delivery-address-input\"]").fill("8 ")
    # page.get_by_text("Санкт-Петербург, 8-я Советская улица, 4").click()
    # page.locator("[data-test-id=\"delivery-flat-input\"]").click()
    # page.locator("[data-test-id=\"delivery-flat-input\"]").fill("1")
    # page.locator("[data-test-id=\"delivery-textarea-comment-input\"]").click()
    # page.locator("[data-test-id=\"delivery-textarea-comment-input\"]").fill("Тест не готовить Автоматический заказ")
    if page.locator("[data-test-id=\"pay-type-open-button\"]").inner_text() == "Наличными курьеру":
        # Продолжать выполнение кода
        pass
    else:
        # Выполнить следующие действия
        page.locator("[data-test-id=\"pay-type-open-button\"]").click()
        page.locator("label").filter(has_text="Наличными курьеру").locator("i").click()
    # page.wait_for_timeout(3000)
    # page.locator("[data-test-id=\"pay-type-close-button\"]").click()
    # page.locator("label").filter(has_text="Картой курьеру").locator("i").click()
    page.locator("[data-test-id=\"pay-type-close-button\"]").click()
    # page.locator("[data-test-id=\"order-check-email-input\"]").click()
    # page.locator("[data-test-id=\"order-check-email-input\"]").fill("xs1089@gmai.com")
    # page.locator("[data-test-id=\"cart-comment-input\"]").click()
    # page.locator("[data-test-id=\"cart-comment-input\"]").fill("")
    page.locator("[data-test-id=\"cart-cutlery-btn-minus\"]").click()
    # page.locator("[data-test-id=\"order-submit-btn\"]").click()
    # page.get_by_text("Заказ №240317287378").click()
    # page.locator("[data-test-id=\"order-modal-apply-btn\"]").click()


    # -------------------

    # # Stop tracing and export it into a zip archive.
    # context.tracing.stop(path="../trace.zip")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
