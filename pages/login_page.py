from selenium.webdriver.common.by import By
from pages.base_page_with_driver import BasePageWithDriver

from controls.button import Button
from controls.textbox import TextBox
from controls.label import Label
from controls.checkbox import Checkbox
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePageWithDriver):

    class Locators:
        sign_in_button = (By.XPATH, "//button[text()='Sign In']")
        remember_me_button = (By.ID, "remember")

        email_field = (By.ID, "signinEmail")
        email_validation_feedback = (
            By.XPATH, "//input[@id='signinEmail']/following::div[contains(@class, 'invalid-feedback')]/p")

        password_field = (By.ID, "signinPassword")
        password_validation_feedback = (
            By.XPATH, "//input[@id='signinPassword']/following::div[contains(@class, 'invalid-feedback')]/p")

        login_button = (By.XPATH, "//button[text()='Login']")
        login_close_button = (By.XPATH, "//button[contains(@class,'close')]")
        login_form_title = (By.CLASS_NAME, 'modal-title')
        login_feedback = (By.XPATH, "//form/p[contains(@class, 'alert')]")
        remember_me_checkbox = (By.XPATH, "//input[@id='remember']")

    def __init__(self):
        super().__init__()

    def get_sign_in_button(self):
        return Button(self._driver.find_element(*self.Locators.sign_in_button))

    def get_email_field(self):
        return TextBox(self._driver.find_element(*self.Locators.email_field))

    def get_password_field(self):
        return TextBox(self._driver.find_element(*self.Locators.password_field))

    def get_login_button(self):
        return Button(self._driver.find_element(*self.Locators.login_button))

    def get_login_close_button(self):
        return Button(self.wait.until(EC.presence_of_element_located(self.Locators.login_close_button)))

    def get_login_form_title(self):
        return Label(self.wait.until(EC.presence_of_element_located(self.Locators.login_form_title)))

    def wait_for_login_form_title_to_disappear(self):
        return self.wait.until(EC.invisibility_of_element_located(self.Locators.login_form_title))

    def get_login_feedback(self):
        return Label(self._driver.find_element(*self.Locators.login_feedback))

    def get_email_validation_feedback(self):
        return Label(self._driver.find_element(*self.Locators.email_validation_feedback))

    def get_password_validation_feedback(self):
        return Label(self._driver.find_element(*self.Locators.password_validation_feedback))

    def get_remember_me_button(self):
        return Button(self._driver.find_element(*self.Locators.remember_me_button))

    def fill_credentials(self, email, password):
        self.get_email_field().fill_field(email)
        self.get_password_field().fill_field(password)

    def do_login(self, email, password):
        self.get_sign_in_button().click()
        self.fill_credentials(email, password)
        self.get_login_button().click()

    def get_remember_me_checkbox(self):
        return Checkbox(self._driver.find_element(*self.Locators.remember_me_checkbox))
