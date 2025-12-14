from playwright.sync_api import Playwright,expect
from time import sleep
import json
import pytest
from Utils.apiBase import APIUtils
from pageObjects.loginPage import LoginPage
with open(r'My_practice/playwright/Optimization_Practices/data/creden.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_creds_list = test_data['user_cred']

@pytest.mark.parametrize('current_user_detail',user_creds_list)
def test_method(playwright:Playwright, current_user_detail):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright,current_user_detail)

    userEmail = current_user_detail['userEmail']
    userPassword = current_user_detail["userPassword"]

    loginpage = LoginPage(page)
    loginpage.navigate()
    loginpage.login(userEmail,userPassword)

    order_page_button = page.get_by_role("button").filter(has_text="ORDERS")
    order_page_button.click()