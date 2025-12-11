from playwright.sync_api import Playwright, expect
from playwright.sync_api import Page
from time import sleep
#run command: pytest test_locators.py::test_coreLocators --headed
def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    #the input field should be wrapped by label tags or for attribute should direct to input field id
    username_field = page.get_by_label("Username:")
    username_field.fill("rahulshettyacademy")
    sleep(2)
    password_field = page.get_by_label("Password:")
    password_field.fill("learning")
    sleep(2)
    status = page.get_by_role("combobox") #equivalent of dropdown
    status.select_option("teach") #value
    sleep(4)
    tandc = page.get_by_role("link",name='terms and conditions')
    tandc.click()
    sleep(2)
    sign_in = page.get_by_role("button",name='Sign In') #particular button with text "Sign In"
    sign_in.click()
    sleep(4)


# run command: pytest test_locators.py::test_cssSelector --headed
def test_cssSelector(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    sleep(4)
    page.locator("#terms").check() #id of checkbox
    sleep(4)

# run command: pytest test_locators.py::test_wrongCreds --headed
def test_wrongCreds(page:Page):
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
    #playwright waits unlike selenium
    error_txt = page.get_by_text("Incorrect username/password.")
    #assertion for the message.
    expect(error_txt).to_be_visible()


