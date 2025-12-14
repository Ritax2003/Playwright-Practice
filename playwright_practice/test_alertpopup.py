from playwright.sync_api import Playwright,expect
from time import sleep

from streamlit import dialog


def test_alert(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    sleep(2)
    page.on("dialog",lambda dialog:dialog.accept()) #alert == dialog box
    page.get_by_role("button",name='Confirm').click()
    sleep(3)