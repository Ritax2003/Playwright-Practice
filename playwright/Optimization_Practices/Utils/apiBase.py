from playwright.sync_api import Playwright
orderPayLoad= {"orders":[{"country":"India","productOrderedId":"693af1b432ed8658712d6844"}]}
class APIUtils:
    def getToken(self,playwright:Playwright,current_user_detail):
        api_req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_req_context.post("/api/ecom/auth/login",
                             data={"userEmail":current_user_detail["userEmail"],
                                   "userPassword":current_user_detail["userPassword"]
                                   })
        assert response.ok
        print(response.json())
        resp_body = response.json()
        return resp_body["token"]

    def createOrder(self,playwright:Playwright,current_user_detail):
        api_req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_req_context.post("/api/ecom/order/create-order",
                             data=orderPayLoad,
                             headers={"Authorization":self.getToken(playwright,current_user_detail),
                                      "Content-Type":"application/json"
                                      })
        print(response.json())
        response_body = response.json()
        print(response_body["orders"][0])
        order_id = response_body["orders"][0]
        return order_id