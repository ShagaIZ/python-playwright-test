
from pages.info_block import InfoBlock


class UserBlock(InfoBlock):
    def __init__(self, page):
        super().__init__(page) 
        self.user_block = page.locator('[class="sc-dkrFOg bHWDWn"]')
        self.user_icon = page.locator('[alt="Ilyas  Shagaleev"]')
        self.user_name = page.get_by_text('Ilyas  Shagaleev')
        self.follow_button = page.locator('text="follow"')

  
