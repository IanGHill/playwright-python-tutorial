from playwright.sync_api import Page, expect


def test_basic_duckduckgo_search(page: Page) -> None:
    # Given the DuckDuckGo page is displayed
    page.goto("https://www.duckduckgo.com")
    # When the user searches for a phrase
    page.get_by_placeholder("Search without being tracked").fill("pandas")
    page.get_by_label("Search", exact=True).click()
    # Then the search result query is the phrase
    expect(page.locator("#search_form_input")).to_have_value("pandas")
    # And the search result links pertain to the phrase
    # And the search result title contains the phrase
    pass
