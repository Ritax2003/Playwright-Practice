from playwright.sync_api import Playwright,expect
from time import sleep

#mock request that will hit the server, unauthorized as it is not the same order from same account
def intercept_request(route):
    route.continue_(
        url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=2"
    )


def test_Network_1(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",
               intercept_request)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    order_page_button = page.get_by_role("button").filter(has_text="ORDERS")
    order_page_button.click()
    page.get_by_role("button",name="View").first.click() #clicks on first one
    sleep(3)
    msg = page.locator(".blink_me").text_content()
    print(msg)