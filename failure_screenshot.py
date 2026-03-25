from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        page.goto("https://Facebook.com")
        try:
            page.click("#login")
        except:
            page.screenshot(path="failure.png")
            raise

        
        browser.close()

if __name__ == "__main__":
    main()