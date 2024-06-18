from playwright.sync_api import Page, expect

# uses raw calls, ok for a quick hacky thing, but for a serious enterprise automation suite
# use design patterns for resuability for example Page Object Model


def test_basic_duckduckgo_search(page: Page) -> None:
    # Given the DuckDuckGo page is displayed
    page.goto("https://www.duckduckgo.com")

    # When the user searches for a phrase
    page.get_by_placeholder("Search without being tracked").fill("panda")
    page.get_by_label("Search", exact=True).click()

    # Then the search result query is the phrase
    expect(page.locator("#search_form_input")).to_have_value("panda")

    # And the search result links pertain to the phrase
    page.get_by_role("link").nth(12).wait_for()
    titles = page.get_by_role("link").all_text_contents()
    matches = [t for t in titles if "panda" in t.lower()]
    assert len(matches) > 0

    # And the search result title contains the phrase
    expect(page).to_have_title("panda at DuckDuckGo")
