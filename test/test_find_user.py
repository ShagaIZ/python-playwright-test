from playwright.sync_api import Page, expect  # type: ignore
from pages.info_block  import InfoBlock
from pages.user_block import UserBlock


def test_info_block_find_user(page: Page):
    info_block = InfoBlock(page)
    info_block.page.goto("https://gh-users-search.netlify.app/")
    info_block.fill_search_filed_find_user('ShagaIZ')
    expect(info_block.info_block.nth(0)).to_contain_text('7repos')
    expect(info_block.info_block.nth(1)).to_contain_text('2followers')
    expect(info_block.info_block.nth(2)).to_contain_text('3following')
    expect(info_block.info_block.nth(3)).to_contain_text('0gists')

def test_user_block_find_user(page: Page):
    user_block = UserBlock(page)
    user_block.page.goto("https://gh-users-search.netlify.app/")
    user_block.fill_search_filed_find_user('ShagaIZ')
    expect(user_block.user_block).to_be_visible()
    expect(user_block.user_icon).to_be_visible()
    expect(user_block.user_name).to_be_visible()
    expect(user_block.follow_button).to_be_visible()
   