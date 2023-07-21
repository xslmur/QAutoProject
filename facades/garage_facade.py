import allure
from facades.facade_base import FacadeBase


class GarageFacade(FacadeBase):
    def __init__(self):
        super().__init__()

    @allure.step("Search for Profile button")
    def get_my_profile_button(self):
        return self._garage_page.get_my_profile_button()
