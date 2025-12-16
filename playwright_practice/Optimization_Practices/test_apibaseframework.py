from playwright.sync_api import Playwright,expect
from time import sleep
import json
import pytest
from Utils.apiBase import APIUtils
from pageObjects.loginPage import LoginPage
from pageObjects.dashboardPage import DashboardPage

with open(r'data/creden.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_creds_list = test_data['user_cred']

@pytest.mark.parametrize('current_user_detail',user_creds_list)
def test_method(playwright:Playwright,browserInstance, current_user_detail):

    userEmail = current_user_detail['userEmail']
    userPassword = current_user_detail["userPassword"]

    loginpage = LoginPage(browserInstance)
    loginpage.navigate()
    loginpage.login(userEmail,userPassword)

    dashboardPage = DashboardPage(browserInstance)
    dashboardPage.selectOrderNavLink()

#for firefox:  pytest test_framework_parametrize.py --browser_name firefox
#for chrome:  pytest test_framework_parametrize.py --browser_name chrome