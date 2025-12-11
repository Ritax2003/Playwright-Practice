from playwright.sync_api import Playwright,expect
from time import sleep

#selectorshub extension for chrome
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