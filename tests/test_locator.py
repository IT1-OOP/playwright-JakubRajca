import os
from playwright.sync_api import sync_playwright

def test_page_title():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/index.html"))

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file://{file_path}")
        title = page.title()
        print(title)
        