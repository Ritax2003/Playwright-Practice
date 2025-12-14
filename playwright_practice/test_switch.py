from playwright.sync_api import Playwright,expect
from time import sleep

#selectorshub extension for chrome
def test_switchnewWindow(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newpage_info:
        page.locator(".blinkingText").click()

    childPage = newpage_info.value #new page
    redtext = childPage.locator(".red")
    expect(redtext).to_be_visible()
    text = redtext.text_content()
    lis = text.split("at")
    email = lis[1].split(" ")[1]
    print(text,end='\n')
    print(lis,end='\n')
    print(email)
    assert email == "mentor@rahulshettyacademy.com"
    sleep(4)