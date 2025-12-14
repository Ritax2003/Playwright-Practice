from playwright.sync_api import Playwright,expect
from time import sleep
def test_filter(playwright:Playwright):
    broswer = playwright.chromium.launch(headless=False)
    context = broswer.new_context() #for single page, no need for context line
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    username_field = page.get_by_label("Username:")
    username_field.fill("rahulshettyacademy")
    password_field = page.get_by_label("Password:")
    password_field.fill("learning")
    status = page.get_by_role("combobox")  # equivalent of dropdown
    status.select_option("teach")  # value
    sleep(2)
    sign_in = page.get_by_role("button", name='Sign In')  # particular button with text "Sign In"
    sign_in.click()
    sleep(2)
    iphoneX = page.locator("app-card").filter(has_text="iphone X")
    iphoneX.get_by_role("button").click()
    nokia = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia.get_by_role("button").click()
    sleep(3)
    page.get_by_text("Checkout").click()#matches also by partial text
    sleep(3)
    itemslist = page.locator(".media-body")
    expect(itemslist).to_have_count(2)