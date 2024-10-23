class MainPage:
    def __init__(self, page):
        self.page = page
        self.header_title = page.locator('[class="sc-iBYQkv fzziLf"]')
        self.search_block = page.locator('[class="form-control"]')
        self.search_field = page.get_by_test_id('search-bar')
        self.searc_button = page.locator('[type="submit"]')
