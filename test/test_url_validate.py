import re
from playwright.sync_api import Page, expect  # type: ignore


def test_has_valid_url(page: Page):
    page.goto("https://gh-users-search.netlify.app/")
    # Проверка корректности урла
    expect(page).to_have_url("https://gh-users-search.netlify.app/")

def test_url_check_regex(page:Page):
    page.goto("https://gh-users-search.netlify.app/")
    regex_url = re.compile(r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$")
    expect(page).to_have_url(regex_url)

