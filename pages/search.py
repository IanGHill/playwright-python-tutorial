from playwright.sync_api import Page


class DuckDuckGoSearchPage:

    URL = "https://www.duckduckgo.com"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_input = page.get_by_placeholder("Search without being tracked")
        self.search_button = page.get_by_label("Search", exact=True)

    def load(self) -> None:
        self.page.goto(self.URL)

    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.search_button.click()
