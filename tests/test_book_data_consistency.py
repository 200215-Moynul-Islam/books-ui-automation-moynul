import random
from playwright.sync_api import Page

def test_book_data_consistency(page: Page):
    page.goto("/index.html")
    books = page.locator("article.product_pod").all()
    selected_books = random.sample(books, 5)

    for book in selected_books:
        homepage_tittle = book.locator("h3>a").get_attribute("title")
        homepage_price = book.locator("p.price_color").inner_text()

        book.locator("h3>a").click()

        detailspage_tittle = page.locator("//h1").inner_text()
        detailspage_price = page.locator("div.product_main p.price_color").inner_text()

        assert detailspage_tittle == homepage_tittle
        assert detailspage_price == homepage_price

        page.go_back()
