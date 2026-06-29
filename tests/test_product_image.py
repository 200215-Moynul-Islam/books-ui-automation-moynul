from playwright.sync_api import Page, expect


def test_product_image_validation(page: Page):
    page.goto("/index.html")

    for _ in range(5):
        images = page.locator("//article[@class='product_pod']//img").all()

        for image in images:
            expect(image).to_be_visible()

            src = image.get_attribute("src")
            alt = image.get_attribute("alt")
            image_class = image.get_attribute("class")

            assert src, "Image src attribute is missing."
            assert alt, "Image alt attribute is missing."
            assert "thumbnail" in image_class, "Image does not have the 'thumbnail' class."

        next_button = page.locator("//li[@class='next']/a")

        if next_button.count() == 0:
            break

        next_button.click()
