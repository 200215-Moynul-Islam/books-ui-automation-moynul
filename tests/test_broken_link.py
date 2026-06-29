from urllib.parse import urljoin
from playwright.sync_api import Page

def test_broken_links(page: Page):
    page.goto("/index.html")

    links = page.locator("//a").all()
    urls = set() # Remove duplicate urls

    for link in links:
        href = link.get_attribute("href")
        if href:
            urls.add(urljoin(page.url, href))

    for url in urls:
        response = page.request.get(url)
        assert response.status == 200, f"{url} returned {response.status_code}"
