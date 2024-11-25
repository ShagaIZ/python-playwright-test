from playwright.sync_api import Page, expect  # type: ignore
from pages.main_page import MainPage


def test_header_title(page: Page):
    main_page = MainPage(page)
    main_page.page.goto("https://gh-users-search.netlify.app/")
    expect(main_page.header_title).to_be_visible()


def test_search_block(page: Page):
    main_page = MainPage(page)
    main_page.page.goto("https://gh-users-search.netlify.app/")
    expect(main_page.search_block).to_be_visible()


def test_search_field(page: Page):
    main_page = MainPage(page)
    main_page.page.goto("https://gh-users-search.netlify.app/")
    expect(main_page.search_field).to_be_visible()
    expect(main_page.search_field).to_have_attribute('placeholder', 'enter github user name')


def test_search_button(page: Page):
    main_page = MainPage(page)
    main_page.page.goto("https://gh-users-search.netlify.app/")
    expect(main_page.searc_button).to_be_visible()
    expect(main_page.searc_button).to_have_text('search')
