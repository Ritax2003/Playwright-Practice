from playwright.sync_api import Playwright,expect
from time import sleep
import pytest
#selectorshub extension for chrome , run with pytest -m smoke
#pytest -k <pattern of test file names. like any word that is common>
#for parallel execution : pytest-xdist
# pytest -n auto : for all test parallel
# pytest -n 3 : max 3 tests can run parallel
@pytest.mark.smoke
def test_assertion(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    textbox = page.get_by_placeholder("Hide/Show Example")
    expect(textbox).to_be_visible()
    sleep(3)
    page.get_by_role("button",name='Hide').click()
    sleep(5)
    expect(textbox).to_be_hidden()