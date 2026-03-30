from playwright.sync_api import sync_playwright,expect

class loginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#submit")
    
    def login (self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
        self.page.wait_for_load_state("networkidle")