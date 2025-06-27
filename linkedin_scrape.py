import os, time, urllib.parse
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
COOKIE = os.getenv("LI_AT")
SEARCH = "Data Scientist"
LOCATION = "United States"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(storage_state={
            "cookies": [{
                "name": "li_at",
                "value": COOKIE,
                "domain": ".www.linkedin.com",
                "path": "/",
                "httpOnly": True,
                "secure": True
            }]
        })
        page = ctx.new_page()
        q = urllib.parse.quote_plus(SEARCH)
        loc = urllib.parse.quote_plus(LOCATION)
        url = (f"https://www.linkedin.com/jobs/search/?keywords={q}"
               f"&location={loc}&f_AL=true")
        page.goto(url, timeout=0)
        page.wait_for_selector("ul.jobs-search__results-list li")
        page.mouse.wheel(0, 3000); time.sleep(1)

        soup = BeautifulSoup(page.content(), "html.parser")
        for link in soup.select("a.base-card__full-link"):
            title = link.get_text(" ", strip=True)
            print(f"{title}  →  {link['href'].split('?')[0]}")

        browser.close()

if __name__ == "__main__":
    main()
