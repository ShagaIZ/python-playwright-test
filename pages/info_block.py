from pages.main_page import MainPage


class InfoBlock(MainPage):
    def __init__(self, page):
        super().__init__(page) 
        self.info_block = page.locator('[class="item"]')
    def fill_search_filed_find_user(self,user_name):
        self.search_field.focus()
        self.search_field.fill(user_name)
        self.searc_button.click()
