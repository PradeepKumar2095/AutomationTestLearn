from playwright.sync_api import sync_playwright,expect

class loginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#submit")

    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")
        self.page.wait_for_load_state("networkidle")  # optional but good
        return self  # return self so chaining works

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
        self.page.wait_for_load_state("networkidle")
        return homePage(self.page)
    
class homePage:
    def __init__(self, page):
        self.page = page
        self.page.wait_for_load_state("networkidle")
        self.welcome = page.locator("h1")

def test_login(page):
    login_page = loginPage(page)
    home_page = login_page.navigate().login("student", "Password123")
    expect(home_page.welcome).to_be_visible()

# if __name__ == "__main__":
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
        
#         # Run the test manually if needed
#         test_login(page)
        
#         # Keep browser open for debugging
#         input("Press Enter to close browser...")
#         browser.close()