import re
from playwright.sync_api import Page, expect  # type: ignore


def test_has_valid_url(page: Page):
    page.goto("https://gh-users-search.netlify.app/")
    # Проверка корректности урла
    expect(page).to_have_url("https://gh-users-search.netlify.app/")
