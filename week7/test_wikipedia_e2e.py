from playwright.sync_api import expect


def test_search_wikipedia(page):
    page.goto("https://www.wikipedia.org/")

    page.locator("input[name='search']").fill("e2e")
    page.keyboard.press("Enter")

    expect(page.locator("#firstHeading")).to_contain_text("E2E")
