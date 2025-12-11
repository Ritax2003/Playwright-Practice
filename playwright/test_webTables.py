from playwright.sync_api import Playwright,expect
from time import sleep

#selectorshub extension for chrome
def test_webtables(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")