import random
from playwright.sync_api import Page, expect

def test_random_book_navigation(page: Page):
    page.goto("/index.html")
    books = page.locator("article.product_pod").all()
    selected_books = random.sample(books, 5)

    for book in selected_books:
        expected_tittle = book.locator("h3>a").get_attribute("title")
        book.locator("h3>a").click()

        expect(page.locator("//h1")).to_be_visible()
        retrieved_tittle = page.locator("//h1").inner_text()
        assert retrieved_tittle == expected_tittle

        expect(page.locator("//table[contains(@class, 'table')]")).to_be_visible()
        page.go_back()