from playwright.sync_api import Page, expect


def test_homepage(page: Page):
    page.goto("/index.html")

    expect(page).to_have_url("https://books.toscrape.com/index.html")
    expect(page).to_have_title("All products | Books to Scrape - Sandbox")

    headings = page.locator("h1, h2, h3, h4, h5, h6")

    for heading in headings.all():
        expect(heading).to_be_visible()
        assert heading.inner_text().strip() != ""

    books_section = page.locator("//section")
    expect(books_section).to_be_visible()
    assert books_section.locator("article.product_pod").all(), "Books section is empty."
