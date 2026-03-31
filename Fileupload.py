import pytest
from playwright.sync_api import sync_playwright

def test_file_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://practice.expandtesting.com/upload")
        page.set_input_files("#fileInput", r"C:\Users\SivaSolai\Downloads\PradeepKumarS-1.pdf")
        page.click("#fileSubmit")

        page.wait_for_load_state("networkidle")

        page.wait_for_selector("h1", timeout=10000)
        assert page.locator("h1").text_content() == "File Uploaded!"

        page.wait_for_load_state("networkidle")

        browser.close()

if __name__ == "__main__":
    pytest.main([
        __file__,
        "-v",
        "--html=report.html",
        "--self-contained-html"
    ])