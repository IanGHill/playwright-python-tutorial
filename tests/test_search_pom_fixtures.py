from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage
from playwright.sync_api import Page, expect

# uses POM with fixtures


def test_basic_duckduckgo_search(
    page: Page, search_page: DuckDuckGoSearchPage, result_page: DuckDuckGoResultPage
) -> None:

    # Given the DuckDuckGo page is displayed
    search_page.load()

    # When the user searches for a phrase
    search_page.search("panda")

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value("panda")

    # And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase("panda")

    # And the search result title contains the phrase
    expect(page).to_have_title("panda at DuckDuckGo")
