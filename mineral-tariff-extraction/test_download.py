from playwright.sync_api import sync_playwright
import time

URL = "https://critmin.org/tariff-data/?reporter=USA&type=mfn&year=2010"

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    print("Opening page...")
    page.goto(URL)

    # Wait for page to fully load
    page.wait_for_load_state("networkidle")
    time.sleep(3)

    print("Looking for download button...")

    # Try clicking download button
    try:
        with page.expect_download() as download_info:
            page.click("text=Download")
        
        download = download_info.value
        file_path = f"US_2010.csv"
        download.save_as(file_path)

        print(f"Downloaded file saved as {file_path}")

    except Exception as e:
        print("Download failed. Likely selector issue.")
        print(e)

    print("Done. Closing browser in 5 seconds...")
    time.sleep(5)
    browser.close()
