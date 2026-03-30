import pytest
from .Login_page import loginPage

def test_login(page):
    login_page = loginPage(page)
    page.goto("https://practicetestautomation.com/practice-test-login/")
    login_page.login("student", "Password123")
    assert page.locator("h1").text_content() == "Logged In Successfully"