from playwright.sync_api import Playwright,expect
from time import sleep
from Utils.apiBase import APIUtils
#mock request that will hit the server, unauthorized as it is not the same order from same account
def intercept_request(route):
    route.continue_(
        url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=2"
    )


def test_Network_1(playwright:Playwright):
    api_utils = APIUtils()
    tokenValue = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #script to inject token in session , for JS it is in triple quotes
    page.add_init_script(f""" localStorage.setItem('token','{tokenValue}')""")
    page.goto("https://rahulshettyacademy.com/client")

    order_page_button = page.get_by_role("button").filter(has_text="ORDERS")
    order_page_button.click()

    expect(page.get_by_text('Your Orders')).to_be_visible()
    sleep(3)