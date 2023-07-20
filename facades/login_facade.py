import allure
from facades.facade_base import FacadeBase


class LoginFacade(FacadeBase):
    def __init__(self):
        super().__init__()

    @allure.step("Fill email and password fields")
    def fill_credentials(self, email, password):
        self._login_page.fill_credentials(email, password)

    @allure.step("Click Sign-in button")
    def click_signin_button(self):
        self._login_page.get_sign_in_button().click()

    @allure.step("Get Login button")
    def get_login_button(self):
        return self._login_page.get_login_button()

    @allure.step("Click Login button")
    def click_login_button(self):
        self._login_page.get_login_button().click()

    @allure.step("get Login form close button")
    def get_login_close_button(self):
        return self._login_page.get_login_close_button()

    @allure.step("get login form title")
    def get_login_form_title(self):
        return self._login_page.get_login_form_title()

    @allure.step("wait for login form title to disappear")
    def wait_for_login_form_title_to_disappear(self):
        self._login_page.wait_for_login_form_title_to_disappear()

    @allure.step("get login feedback")
    def get_login_feedback(self):
        return self._login_page.get_login_feedback()

    @allure.step("get email validation feedback")
    def get_email_validation_feedback(self):
        return self._login_page.get_email_validation_feedback()

    @allure.step("wait for email field css property value")
    def wait_email_field_css_property(self, css_property: str, value: str):
        return self._login_page.wait_email_field_css_property(css_property, value)

    @allure.step("get password validation feedback")
    def get_password_validation_feedback(self):
        return self._login_page.get_password_validation_feedback()

    @allure.step("get email field")
    def get_email_field(self):
        return self._login_page.get_email_field()

    @allure.step("do WEB UI login")
    def do_login(self, email, password):
        self.click_signin_button()
        self.fill_credentials(email, password)
        self.click_login_button()

    def check_if_profile_displayed(self):
        return self._garage_page.get_my_profile_button().is_displayed()

    def get_login_locators(self):
        return self._login_page.Locators

    def wait_element_css_property(self, locator, css_property: str, value: str):
        return self._login_page.wait_element_css_property(locator, css_property, value)

    def wait_element_css_property_color_hex(self, locator, css_property: str, value: str):
        return self._login_page.wait_element_css_property_color_hex(locator, css_property, value)

    @allure.step("Get Remember Me checkbox")
    def get_remember_me_checkbox(self):
        return self._login_page.get_remember_me_checkbox()
