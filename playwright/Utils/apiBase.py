from playwright.sync_api import Playwright
orderPayLoad= {"orders":[{"country":"India","productOrderId":"6581ca399fd99c85e8e7f45"}]}
class APIUtils:
    def createOrder(self,playwright:Playwright):
        api_req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_req_context.post("/api/ecom/order/create-order",
                             data=orderPayLoad,
                             headers={"Authorization":token,
                                      "Content-Type":"application/json"
                                      })
        print(response.json())