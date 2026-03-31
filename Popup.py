from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        page.goto("https://vinothqaacademy.com/alert-and-popup/")

        page.locator(has_text="Alert Box").click()  
              
        with page.expect_popup() as popup_info:
            page.click("text=Try it")
        popup = popup_info.value
        print(popup.url)
        
        popup.close()
        browser.close()

if __name__ == "__main__":
    main()