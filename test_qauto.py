import pytest
import requests
import time
import allure
import os

from driver import Driver

# from pages.login_page import LoginPage
from facades.login_facade import LoginFacade
# from pages.garage_page import GaragePage
from facades.garage_facade import GarageFacade

WEB_UI_URL = 'https://guest:welcome2qauto@qauto2.forstudy.space/'

WEB_USER = os.getenv('WEB_USER', 'test@example.com')
WEB_PASS = os.getenv('WEB_PASS', 'testpass')


class QautoColors:
    RED = '#dc3545'


class TestLoginPopUp:
    def setup_class(self):
        self.session = requests.session()

        self.driver = Driver.get_chrome_driver()
        self.login_facade = LoginFacade()
        self.garage_facade = GarageFacade()

    def setup_method(self):
        self.driver.get(WEB_UI_URL)

    # Verify that the login pop-up displays the text "Log-in" correctly.,
    @allure.description("check login form title")
    @allure.issue("https://qauto2.forstudy.space/", "Test issue: Login")
    def test_login_form_title(self):
        self.login_facade.click_signin_button()
        assert self.login_facade.get_login_form_title().get_text() == 'Log in'

    # Verify that the login pop-up closes on the cross button click
    @allure.description("check login form close button functionality")
    @allure.issue("https://qauto2.forstudy.space/", "Test issue: Login")
    def test_login_close_button(self):
        self.login_facade.click_signin_button()

        close_button = self.login_facade.get_login_close_button()
        assert close_button.is_displayed()
        close_button.click()

        self.login_facade.wait_for_login_form_title_to_disappear()
    #
    # Field Email
    #
    # 3.1
    @allure.description("check for error message on empty email")
    @allure.issue("https://qauto2.forstudy.space/", "Test issue: Login")
    def test_email_empty(self):
        self.login_facade.click_signin_button()
        self.login_facade.fill_credentials('', WEB_PASS)
        assert not self.login_facade.get_login_button().is_enabled()
        assert self.login_facade.get_email_validation_feedback().get_text() == 'Email required'

    # 3.2
    @allure.description("check for error message on incorrect email")
    @allure.issue("https://qauto2.forstudy.space/", "Test issue: Login")
    def test_email_incorrect(self):
        self.login_facade.click_signin_button()
        self.login_facade.fill_credentials('invalid', WEB_PASS)
        assert not self.login_facade.get_login_button().is_enabled()
        assert self.login_facade.get_email_validation_feedback().get_text() == 'Email is incorrect'

    #
    # Login functionality with valid credentials
    #
    @allure.description("check for successful login with valid credentials")
    @allure.issue("https://qauto2.forstudy.space/", "Test issue: Login")
    def test_login(self):
        self.login_facade.do_login(WEB_USER, WEB_PASS)
        # assert self.login_facade.get_login_feedback().get_text() == 'Email is incorrect'
        assert self.garage_facade.get_my_profile_button().is_displayed()

    @allure.description("check for error message on login with unregistered email")
    @allure.issue("https://qauto2.forstudy.space/", "Test issue: Login")
    def test_unregistered_email_login(self):
        self.login_facade.do_login("unregistered@example.com", "password123")
        assert self.login_facade.get_login_feedback().get_text() == "Wrong email or password"

    @allure.description("Verify the visual representation of the email field when an error occurs")
    @allure.issue("https://qauto2.forstudy.space/", "Test issue: Login")
    def test_email_field_visual_representation_on_error(self):
        self.login_facade.click_signin_button()
        self.login_facade.fill_credentials('', 'test')

        self.login_facade.wait_element_css_property_color_hex(
            self.login_facade.get_login_locators().email_field,
            'border-color', QautoColors.RED
        )

        # assert 'test' == self.login_facade.get_email_validation_feedback().element.value_of_css_property('color')
        # self.login_facade.wait_element_css_property(
        #     self.login_facade.get_login_locators().email_validation_feedback,
        #     'color', 'rgba(220, 53, 69, 1)'from_string
        # )
        assert self.login_facade.wait_element_css_property_color_hex(
            self.login_facade.get_login_locators().email_validation_feedback,
            'color', QautoColors.RED
        )

    @allure.description("Verify the visual representation of the email field when an error occurs")
    @allure.issue("https://qauto2.forstudy.space/", "Test issue: Login")
    def test_password_field_visual_representation_on_error(self):
        self.login_facade.click_signin_button()
        self.login_facade.fill_credentials('test@example.com', '')

        # remove focus from the password field to run related validator
        self.login_facade.get_login_form_title().click()

        self.login_facade.wait_element_css_property_color_hex(
            self.login_facade.get_login_locators().password_field,
            'border-color', QautoColors.RED
        )

        # assert 'test' == self.login_facade.get_email_validation_feedback().element.value_of_css_property('color')
        # self.login_facade.wait_element_css_property(
        #     self.login_facade.get_login_locators().email_validation_feedback,
        #     'color', 'rgba(220, 53, 69, 1)'from_string
        # )
        assert self.login_facade.wait_element_css_property_color_hex(
            self.login_facade.get_login_locators().password_validation_feedback,
            'color', QautoColors.RED
        )

    # N.5 Check assert remember_me_checkbox

    @allure.description(
        "Check the 'Remember me' checkbox retains its selection state when the login pop-up is closed and reopened.")
    @allure.issue("https://qauto2.forstudy.space/", "Test issue: Login")
    def test_remember_me_checkbox(self):
        self.login_facade.click_signin_button()
        remember_me_checkbox = self.login_facade.get_remember_me_checkbox()
        assert not remember_me_checkbox.is_selected()
        remember_me_checkbox.click()
        assert remember_me_checkbox.is_selected()
        # close login pop-up
        close_button = self.login_facade.get_login_close_button()
        close_button.click()
        self.login_facade.wait_for_login_form_title_to_disappear()
        # open login pop-up
        self.login_facade.click_signin_button()
        # recheck checkbox state
        assert not self.login_facade.get_remember_me_checkbox().is_selected()

    @allure.description("check for error message on login with unregistered email")
    @allure.issue("https://qauto2.forstudy.space/", "Test issue: Login")
    def test_wrong_password_login(self):
        self.login_facade.do_login(WEB_USER, "wrongpass123")
        assert self.login_facade.get_login_feedback().get_text() == "Wrong email or password"

    @allure.description("check for successful login with valid credentials")
    @allure.issue("https://qauto2.forstudy.space/", "Test issue: Login")
    def test_login_mixedcase_sensitivity(self):
        user_mixed_case = ''.join([c if i % 2 else c.swapcase() for i, c in enumerate(WEB_USER)])
        self.login_facade.do_login(user_mixed_case, WEB_PASS)
        # assert that the login is case-insensitive
        # and the user is able to log in successfully regardless of the case used.
        assert self.garage_facade.get_my_profile_button().is_displayed()

    def teardown_method(self):
        # force logout
        self.driver.delete_all_cookies()

        screen_name_using_current_time = time.strftime("%Y%m%d-%H%M%S")
        allure.attach(self.driver.get_screenshot_as_png(), name=screen_name_using_current_time)

    def teardown_class(self):
        self.driver.close()
