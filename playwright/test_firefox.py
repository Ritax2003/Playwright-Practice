from playwright.sync_api import Playwright,expect
from time import sleep
def test_firefoxbrowser(playwright:Playwright):
    firefox = playwright.firefox.launch(headless=False)
    context = firefox.new_context() #for single page, no need for context line
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    username_field = page.get_by_label("Username:")
    username_field.fill("rahulshettyacademy")
    password_field = page.get_by_label("Password:")
    password_field.fill("learningXXX")
    status = page.get_by_role("combobox")  # equivalent of dropdown
    status.select_option("teach")  # value
    sleep(2)
    sign_in = page.get_by_role("button", name='Sign In')  # particular button with text "Sign In"
    sign_in.click()
    # playwright waits unlike selenium
    error_txt = page.get_by_text("Incorrect username/password.")
    # assertion for the message.
    expect(error_txt).to_be_visible()