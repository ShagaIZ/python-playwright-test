import re
from playwright.sync_api import Page, expect  # type: ignore
from pages.main_page import MainPage


def test_header_title(page: Page):
    main_page = MainPage(page)
    main_page.page.goto("https://gh-users-search.netlify.app/")
    # Проверка корректности урла
    expect(main_page.header_title).to_be_visible()
