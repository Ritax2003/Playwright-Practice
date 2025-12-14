import pytest
from playwright.sync_api import Page
from playwright.sync_api import Playwright
#using playwright fixture
def test_playwrightbasics_using_fixture(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # launch new incognito session
    page = context.new_page()
    page.goto("https://en.wikipedia.org/")


# using playwright.page fixture
# chromium headless mode, 1 single context
def test_playwrightShortcut(page):
    page.goto("https://en.wikipedia.org/")
# add --headed to open browser (pytest test_playwrightbasics_fixture.py::test_playwrightShortcut2 --headed)
# pytest filename.py::test_name --headed
def test_playwrightShortcut2(page:Page):
    page.goto("https://en.wikipedia.org/")

def test_playwrightShortcut3(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://en.wikipedia.org/")
