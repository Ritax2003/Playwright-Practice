from playwright.sync_api import Playwright,expect
from time import sleep

def test_tableAuto(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() == 1:
            colValue = index
            print(f"Index of Price: {colValue}")
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
    price_of_rice = riceRow.locator("td").nth(colValue)
    expect(price_of_rice).to_contain_text("37")