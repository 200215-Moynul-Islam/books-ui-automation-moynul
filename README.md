# Enterprise UI Automation Framework – Books to Scrape

A production-ready UI automation framework built with **Playwright** and **Pytest** that validates website functionality, data consistency, UI elements, navigation behavior, and quality assurance scenarios for [books.toscrape.com](https://books.toscrape.com/index.html).

---

## Project Overview

This framework automates end-to-end UI testing for the Books to Scrape website. It covers homepage validation, book navigation, data consistency, broken link detection, and product image verification across paginated pages. The framework is designed following OOP, SOLID, and DRY principles with reusable fixtures, clean test structure, and comprehensive local reporting.

---

## Features

- Automated homepage validation (URL, title, headings, book section)
- Random book navigation and detail page verification
- Book data consistency checks (title and price matching)
- Broken link detection across all anchor elements
- Product image attribute validation with pagination support
- HTML report generation via `pytest-html`
- Allure results generation via `allure-pytest`
- No hardcoded waits — relies on Playwright's built-in auto-waiting

---

## Tech Stack

| Tool              | Version | Purpose                           |
| ----------------- | ------- | --------------------------------- |
| Python            | 3.12    | Runtime                           |
| Playwright        | 1.60.0  | Browser automation                |
| pytest            | 9.1.1   | Test framework                    |
| pytest-playwright | 0.8.0   | Playwright-pytest integration     |
| pytest-html       | 4.2.0   | HTML report generation            |
| allure-pytest     | 2.16.0  | Allure results generation         |
| pytest-base-url   | 2.1.0   | Base URL configuration            |
| requests          | 2.34.2  | HTTP requests for link validation |

---

## Installation Guide

### Prerequisites

- Python 3.12+
- Git
- pip

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/200215-Moynul-Islam/books-ui-automation-moynul.git
cd books-ui-automation-moynul
```

**2. Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install Python dependencies**

```bash
pip install -r requirements.txt
```

**4. Install Playwright browsers**

```bash
playwright install --with-deps
```

---

## Environment Setup

No environment variables or external configuration are required. The base URL is configured in `pytest.ini`:

```ini
base_url = https://books.toscrape.com
```

All tests use this base URL automatically through the `pytest-base-url` plugin.

---

## Running Tests

### Run all tests

```bash
pytest --html=test-results/report.html --self-contained-html --alluredir=allure-results
```

### Run a specific test file

```bash
pytest tests/test_homepage.py
pytest tests/test_random_book_navigation.py
pytest tests/test_book_data_consistency.py
pytest tests/test_broken_link.py
pytest tests/test_product_image.py
```

### Run tests with verbose output

```bash
pytest -v
```

### Run tests in headed mode (see the browser)

```bash
pytest --headed
```

---

## Project Structure

```
books-ui-automation-moynul/
├── tests/
│   ├── test_homepage.py                # Test Case 1: Homepage validation
│   ├── test_random_book_navigation.py  # Test Case 2: Random book navigation
│   ├── test_book_data_consistency.py   # Test Case 3: Data consistency
│   ├── test_broken_link.py             # Test Case 4: Broken link validation
│   └── test_product_image.py           # Test Case 5: Product image validation
├── allure-results/                     # Allure raw results (generated at runtime)
│   └── .gitkeep
├── test-results/                       # HTML report output (generated at runtime)
│   └── .gitkeep
├── conftest.py                         # Shared fixtures
├── pytest.ini                          # Pytest configuration
├── requirements.txt                    # Python dependencies
├── .gitignore
└── README.md
```

---

## Test Case Coverage

### Test Case 1 — Homepage Validation (`test_homepage.py`)

Verifies that the homepage loads successfully and displays all expected content.

- Navigates to `https://books.toscrape.com/index.html`
- Asserts correct page URL and title
- Verifies all headings (h1–h6) are visible and contain non-empty text
- Confirms the books section is visible and contains at least one book

### Test Case 2 — Random Book Navigation (`test_random_book_navigation.py`)

Verifies that randomly selected books open the correct detail pages.

- Collects all book items from the homepage
- Randomly selects 5 books
- For each book: captures the title, clicks through, verifies the H1 on the detail page matches, and confirms book information table is visible
- Navigates back to the homepage after each book

### Test Case 3 — Book Data Consistency (`test_book_data_consistency.py`)

Verifies that book data on the homepage matches data on the detail page.

- Randomly selects 5 books from the homepage
- For each book: captures title and price from the homepage, then opens the detail page and captures the same fields
- Asserts homepage title matches detail page title
- Asserts homepage price matches detail page price

### Test Case 4 — Broken Link Validation (`test_broken_link.py`)

Verifies that all hyperlinks on the homepage return successful HTTP responses.

- Collects all anchor elements and extracts href values
- Deduplicates URLs
- Sends an HTTP GET request to each URL using Playwright's request context
- Asserts every URL returns HTTP 200

### Test Case 5 — Product Image Validation (`test_product_image.py`)

Verifies that product images are correctly rendered and have the required attributes across paginated pages.

- Validates all product images on the current page
- For each image: checks visibility, non-empty `src`, non-empty `alt`, and presence of `thumbnail` class
- Clicks the Next button and repeats for up to 5 pages or until pagination ends

---

## Report Generation Guide

### HTML Report

**Generate locally:**

```bash
pytest --html=test-results/report.html --self-contained-html --alluredir=allure-results
```

The report is saved to `test-results/report.html`. Open it in any browser:

```bash
xdg-open test-results/report.html
```

### Allure Report

Allure raw results are generated during the test run. To view the full interactive Allure report, you need the [Allure CLI](https://allurereport.org/docs/install/) installed separately.

**Generate raw results locally:**

```bash
pytest --html=test-results/report.html --self-contained-html --alluredir=allure-results
```

Raw JSON results are saved to `allure-results/`.

**View the Allure report (requires Allure CLI):**

```bash
allure serve allure-results
```

> **Note:** The Allure CLI must be installed separately to view the interactive report. Raw results in `allure-results/` are not viewable directly in a browser.

---

## Design Decisions

- **No Page Object Model (POM):** Given the limited scope of 5 test cases targeting a single website, introducing a full POM layer would add unnecessary abstraction. Locators are kept inline and are self-descriptive.
- **Playwright auto-waiting:** All interactions rely on Playwright's built-in auto-waiting mechanisms. No `time.sleep()` or hardcoded waits are used anywhere in the framework.
- **`pytest-base-url` for URL management:** The base URL is declared once in `pytest.ini` and used across all tests via `page.goto("/path")`, making it easy to retarget a different environment.
- **`random.sample` for book selection:** Ensures exactly 5 unique books are selected per test run without repetition.
- **`page.request` for link validation:** Uses Playwright's built-in HTTP request context instead of a separate `requests` session, keeping the tool footprint minimal.
- **Explicit report flags on the CLI:** Report flags (`--html`, `--alluredir`) are passed explicitly on the command line rather than via `addopts` in `pytest.ini`, keeping the config file focused on test discovery and base URL only.

---

## Known Limitations

- **Broken link test scope:** Only links on the homepage are validated. Links on inner pages are not checked.
- **Random test variability:** Tests 2 and 3 use `random.sample`, so different books are tested on each run. A fixed seed could be used for fully deterministic runs but is not implemented.
- **Single browser:** Tests run on Chromium only (Playwright default). Cross-browser runs are not configured.
- **No screenshots or video:** Failure screenshots and video recording are not enabled. These can be added via `pytest.ini` or `conftest.py` using Playwright's `--screenshot` and `--video` flags.
