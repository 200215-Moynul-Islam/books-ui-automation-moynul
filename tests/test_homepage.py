def test_homepage_loads(page):
    page.goto("/index.html")
    assert page.url == "https://books.toscrape.com/index.html"
