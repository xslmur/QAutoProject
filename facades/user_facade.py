import allure
from models.user import User


class UserFacade(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @allure.step("Login API user")
    def login(self):
        return super().login()

    @allure.step("Logout API user")
    def logout(self):
        return super().logout()

    @allure.step("Register user via API")
    def register(self):
        return super().register()

    @allure.step("Delete user via API")
    def delete(self):
        return super().delete()

    @allure.step("Get user profile via API")
    def get_profile(self):
        return super().get_profile()
