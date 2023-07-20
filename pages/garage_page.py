from selenium.webdriver.common.by import By
from .base_page_with_driver import BasePageWithDriver
from controls.button import Button
from controls.selectbox import SelectBox
from controls.textbox import TextBox


class GaragePage(BasePageWithDriver):
    def __init__(self):
        super().__init__()

    def get_my_profile_button(self):
        return Button(self._driver.find_element(By.ID, "userNavDropdown"))
