import pytest
from playwright.sync_api import Playwright
"""
Scopes: "session", "package", "module", "class", "function"
"""
@pytest.fixture(scope="function")
def prework():
    print(f"before test\n")

@pytest.fixture(scope="session")
def current_user_detail(request):
    return request.param

@pytest.fixture(scope='session')
def browserInstance(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page