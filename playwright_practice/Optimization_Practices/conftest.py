import pytest
from playwright.sync_api import Playwright
"""
Scopes: "session", "package", "module", "class", "function"
"""

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="chrome",help="browser selection"
    )
@pytest.fixture(scope="function")
def prework():
    print(f"before test\n")

@pytest.fixture(scope="session")
def current_user_detail(request):
    return request.param

@pytest.fixture(scope='session')
def browserInstance(playwright:Playwright,request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()