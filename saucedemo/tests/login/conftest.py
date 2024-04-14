import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.fixture()
def set_up_tear_down(page) -> None:
    page.goto("https://www.saucedemo.com/")
    yield page