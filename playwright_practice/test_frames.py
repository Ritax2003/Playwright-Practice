from playwright.sync_api import Playwright, expect
from time import sleep

def test_frameHandling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    sleep(4)

    # Switch to iframe
    course_frame = page.frame_locator("#courses-iframe")

    # Correct link text (remove quotes)
    course_frame.get_by_role("link", name="All-Access").click()

    sleep(5)

    # Assert something inside the frame
    body_content = course_frame.locator("body")
    expect(body_content).to_contain_text("Happy Subscribers")
    sleep(3)
