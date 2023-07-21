import allure
from facades.facade_base import FacadeBase
from facades.allure_secure_step import allure_secure_step


class LoginFacade(FacadeBase):
    def __init__(self):
        super().__init__()

    @allure_secure_step("Fill email and password fields")
    def fill_credentials(self, email, password):
        self._login_page.fill_credentials(email, password)

    @allure.step("Click Sign in button")
    def click_signin_button(self):
        self._login_page.get_sign_in_button().click()

    @allure.step("Get Log in button")
    def get_login_button(self):
        return self._login_page.get_login_button()

    @allure.step("Click Log in button")
    def click_login_button(self):
        self._login_page.get_login_button().click()

    @allure.step("Get Log in form close button")
    def get_login_close_button(self):
        return self._login_page.get_login_close_button()

    @allure.step("Get Log in form title")
    def get_login_form_title(self):
        return self._login_page.get_login_form_title()

    @allure.step("Wait for Log in form title to disappear")
    def wait_for_login_form_title_to_disappear(self):
        self._login_page.wait_for_login_form_title_to_disappear()

    @allure.step("Get Log in feedback")
    def get_login_feedback(self):
        return self._login_page.get_login_feedback()

    @allure.step("Get email validation feedback")
    def get_email_validation_feedback(self):
        return self._login_page.get_email_validation_feedback()

    @allure.step("Wait for email field css property value")
    def wait_email_field_css_property(self, css_property: str, value: str):
        return self._login_page.wait_email_field_css_property(css_property, value)

    @allure.step("Get password validation feedback")
    def get_password_validation_feedback(self):
        return self._login_page.get_password_validation_feedback()

    @allure.step("Get email field")
    def get_email_field(self):
        return self._login_page.get_email_field()

    @allure_secure_step("Do WEB UI Log in")
    def do_login(self, email, password):
        self.click_signin_button()
        self.fill_credentials(email, password)
        self.click_login_button()

    @allure.step("Check if profile displayed")
    def check_if_profile_displayed(self):
        return self._garage_page.get_my_profile_button().is_displayed()

    @allure.step("Wait for element CSS property")
    def wait_element_css_property(self, locator, css_property: str, value: str):
        return self._login_page.wait_element_css_property(locator, css_property, value)

    @allure.step("Wait for {locator_description} CSS property {css_property} to be {value}")
    def wait_element_css_property_color_hex(self, locator, locator_description: str, css_property: str, value: str):
        return self._login_page.wait_element_css_property_color_hex(locator, css_property, value)

    @allure.step("Get 'Remember Me' checkbox")
    def get_remember_me_checkbox(self):
        return self._login_page.get_remember_me_checkbox()

    def get_login_locators(self):
        return self._login_page.Locators
