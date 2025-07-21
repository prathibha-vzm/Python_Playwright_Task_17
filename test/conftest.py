import pytest                                                # For writing and running test cases
from playwright.sync_api import sync_playwright              # To import the sync.api

@pytest.fixture                                             # Marking as fixture
def setup(scope="session"):                                 # Creating test run environment
    with sync_playwright() as playwright:
        browser=playwright.chromium.launch(headless=False)  # opening the browser
        yield browser                                       # returning the browser
        browser.close()                                     # closing the browser

@pytest.fixture                                             # Marking as fixture
def page(browser):
    context = browser.new_context()                         # Create a new browser context
    page = context.new_page()                               # Open a new page in that context
    yield page                                              # Provide the page to the test
    context.close()                                         # Close the context after the test


