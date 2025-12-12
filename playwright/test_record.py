from playwright.sync_api import Playwright,expect
from time import sleep

#selectorshub extension for chrome
#command: playwright codegen https://rahulshettyacademy.com/client
# do whatever,start recording and playwright inspector will record all operations and will generate code.
def test_record(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")