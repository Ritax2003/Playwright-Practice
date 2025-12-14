from playwright.sync_api import Playwright,expect
from time import sleep
from Utils.apiBase import APIUtils
#selectorshub extension for chrome
def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #create order
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button",name="Login").click()
    api_utils = APIUtils()
    order_id  = api_utils.createOrder(playwright)

    #order page verify
    order_page_button = page.get_by_role("button").filter(has_text="ORDERS")
    order_page_button.click()
    sleep(4)
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you")
    sleep(3)

    context.close()




    