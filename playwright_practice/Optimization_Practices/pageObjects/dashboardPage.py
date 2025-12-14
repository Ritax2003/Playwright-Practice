from time import sleep
class DashboardPage:
    def __init__(self, page):
        self.page = page

    def selectOrderNavLink(self):
        order_page_button = self.page.get_by_role("button").filter(has_text="ORDERS")
        order_page_button.click()
        sleep(4)