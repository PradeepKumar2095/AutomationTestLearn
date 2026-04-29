import os
from playwright.sync_api import sync_playwright
import pytest

user_name = '#txt-username'
user = "John Doe"
password = '#txt-password'
login = 'button[type="submit"]'
pwd = "ThisIsNotAPassword"
Patient_Search = '#patient-search'
name = "John Doe S"
search_patient = '#search-btn'
patient_detail = 'table#results tbody tr'

# Page Object for Login
class LoginPage:
    def __init__(self, page):
        self.page = page
    def login(self):
        self.page.fill(user_name, user)
        self.page.fill(password, pwd)
        self.page.click(login)

# Page Object for Patient Search
class PatientSearchPage:
    def __init__(self, page):
        self.page = page
    def search(self):
        self.page.fill(Patient_Search, name)
        self.page.click(search_patient)
        self.page.wait_for_load_state("networkidle")
    def result_count(self):
        return self.page.locator(patient_detail).count()

# Test case
def test_patient_search():
    headless = os.getenv("HEADLESS", "true").lower() in ("1", "true", "yes")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        page.goto("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        LoginPage(page).login()
        page.wait_for_url("**/dashboard")
        search_pg = PatientSearchPage(page)
        page.goto("https://app.example.com/patients")
        search_pg.search()
        assert search_pg.result_count() > 0
        browser.close()

if __name__ == "__main__":
    pytest.main([
        __file__,
        "-v",
        "--html=report.html",
        "--self-contained-html"
    ])