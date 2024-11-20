import re
from playwright.sync_api import Page, expect  # type: ignore
from pages.info_block  import InfoBlock


def test_find_valid_user(page: Page):
    info_block = InfoBlock(page)
    info_block.page.goto("https://gh-users-search.netlify.app/")
    info_block.fill_search_filed_find_user('ShagaIZ')
    expect(info_block.info_block.nth(0)).to_contain_text('7repos')
    expect(info_block.info_block.nth(1)).to_contain_text('2followers')
    expect(info_block.info_block.nth(2)).to_contain_text('3following')
    expect(info_block.info_block.nth(3)).to_contain_text('0gists')
