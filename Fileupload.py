from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) 
        page = await browser.new_page()
        await page.goto("https://practice.expandtesting.com/upload")
        await page.set_input_files("#fileInput", r"C:\Users\SivaSolai\Downloads\PradeepKumarS-1.pdf")
        await page.click("#fileSubmit")
        
        await browser.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())        