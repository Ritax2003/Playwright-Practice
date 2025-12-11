from playwright.sync_api import Playwright,expect
from time import sleep

#selectorshub extension for chrome
def test_webtables(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    sleep(4)
    page.locator("#mousehover").scroll_into_view_if_needed()
    sleep(3)
    page.locator("#mousehover").hover()
    sleep(3)
    page.get_by_role("link",name="Top").click()
    sleep(2)