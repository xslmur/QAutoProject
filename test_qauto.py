import requests
import time
import allure
import os

from driver import Driver
from facades.login_facade import LoginFacade
from facades.garage_facade import GarageFacade

WEB_UI_URL = 'https://guest:welcome2qauto@qauto2.forstudy.space/'

WEB_USER = os.getenv('WEB_USER', 'test@example.com')
WEB_PASS = os.getenv('WEB_PASS', 'testpass')

GITHUB_REPO_LINK = "https://github.com/xslmur/login_auto_testing"


def issue_link(issue_id):
    return GITHUB_REPO_LINK + '#' + issue_id


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

    @allure.description("Verifying, that comparing the retrieving text value with the expected text 'Log in',"
                        " to ensures it matches exactly.")
    @allure.issue(issue_link("n1_1"), "Test issue: Check for text value comparison Log in pop up")
    def test_login_form_title_n1_1(self):
        self.login_facade.click_signin_button()
        assert self.login_facade.get_login_form_title().get_text() == 'Log in'

    @allure.description("Verifying, that clicking on the cross button ensures that the login pop up is closed.")
    @allure.issue(issue_link("n2_1"), "Test issue: Check Log in form close button functionality")
    def test_login_close_button_n2_1(self):
        self.login_facade.click_signin_button()

        close_button = self.login_facade.get_login_close_button()
        assert close_button
        # assert close_button.is_displayed()
        close_button.click()

        self.login_facade.wait_for_login_form_title_to_disappear()

    @allure.description("Verifying, that when the email field is left empty and the form is submitted, "
                        "an error message stating 'Email required' should appear")
    @allure.issue(issue_link("n3_1"), "Test issue: Check for error message on empty email")
    def test_email_empty_n3_1(self):
        self.login_facade.click_signin_button()
        self.login_facade.fill_credentials('', WEB_PASS)
        assert not self.login_facade.get_login_button().is_enabled()
        assert self.login_facade.get_email_validation_feedback().get_text() == 'Email required'

    @allure.description("Verifying, that when an invalid email format (without '@' symbol) is entered"
                        " and the form is submitted, an error message appears stating 'Email is incorrect'")
    @allure.issue(issue_link("n3_2"), "Test issue: Check for error message on incorrect email")
    def test_email_incorrect_n3_2(self):
        self.login_facade.click_signin_button()
        self.login_facade.fill_credentials('invalid', WEB_PASS)
        assert not self.login_facade.get_login_button().is_enabled()
        assert self.login_facade.get_email_validation_feedback().get_text() == 'Email is incorrect'

    @allure.description("Verifying that when an email that isn`t registered with the site is entered and "
                        "the form is submitted, an error message appears stating 'Wrong email or password'")
    @allure.issue(issue_link("n3_3"), "Test issue: Check for error message on Log in"
                                      " with unregistered email")
    def test_unregistered_email_login_n3_3(self):
        self.login_facade.do_login("unregistered@example.com", "password123")
        assert self.login_facade.get_login_feedback().get_text() == "Wrong email or password"

    @allure.description("Verifying that when an error occurs, the email field's border color turns red, "
                        "and the associated labels also turn red.")
    @allure.issue(issue_link("n3_4"), "Test issue: Check that the email field's border color "
                                      "and associated labels turn red")
    def test_email_field_visual_representation_n3_4(self):
        self.login_facade.click_signin_button()
        self.login_facade.fill_credentials('', 'test')

        self.login_facade.wait_element_css_property_color_hex(
            self.login_facade.get_login_locators().email_field, 'Email field',
            'border-color', QautoColors.RED
        )

        assert self.login_facade.wait_element_css_property_color_hex(
            self.login_facade.get_login_locators().email_validation_feedback, 'Email validation text',
            'color', QautoColors.RED
        )

    @allure.description("Verifying that when the password field is left empty and the form is submitted, "
                        "an error message appears stating 'Password required'")
    @allure.issue(issue_link("n4_1"), "Test issue: Check for error message on empty password")
    def test_password_empty_n4_1(self):
        self.login_facade.click_signin_button()
        self.login_facade.fill_credentials(WEB_USER, '')

        # remove focus from the password field to run related validator
        self.login_facade.get_login_form_title().click()

        assert not self.login_facade.get_login_button().is_enabled()
        assert self.login_facade.get_password_validation_feedback().get_text() == 'Password required'

    @allure.description("Verifying that when an incorrect password is entered for a valid email and "
                        "the form is submitted, an error message appears stating 'Wrong email or password.'")
    @allure.issue(issue_link("n4_2"), "Test issue: Check for error message "
                                      "on login with wrong password")
    def test_wrong_password_login_n4_2(self):
        self.login_facade.do_login(WEB_USER, "wrongpass123")
        assert self.login_facade.get_login_feedback().get_text() == "Wrong email or password"

    @allure.description("Verifying that when an error occurs, the password field's border color turns red, "
                        "and the associated labels also turn red.")
    @allure.issue(issue_link("n4_3"), "Test issue: Check that the password field's border color "
                                      "and associated labels turn red")
    def test_password_field_visual_representation_n4_3(self):
        self.login_facade.click_signin_button()
        self.login_facade.fill_credentials('test@example.com', '')

        # remove focus from the password field to run related validator
        self.login_facade.get_login_form_title().click()

        self.login_facade.wait_element_css_property_color_hex(
            self.login_facade.get_login_locators().password_field, 'Password field',
            'border-color', QautoColors.RED
        )

        assert self.login_facade.wait_element_css_property_color_hex(
            self.login_facade.get_login_locators().password_validation_feedback, 'Password validation text',
            'color', QautoColors.RED
        )

    @allure.description("Verifying that the 'Remember me' check box retains its selection state " 
                        "when the login pop up is closed and reopened.")
    @allure.issue(issue_link("n5_1"), "Test issue: Check that the 'Remember me' check box retaining")
    def test_remember_me_checkbox_n5_1(self):
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

    @allure.description("check for successful login with valid credentials")
    @allure.issue(issue_link("p1_1"), "Test issue: Login")
    def test_login_p1_1(self):
        self.login_facade.do_login(WEB_USER, WEB_PASS)
        # assert self.login_facade.get_login_feedback().get_text() == 'Email is incorrect'
        assert self.garage_facade.get_my_profile_button().is_displayed()

    @allure.description("Verifying, that when entering a valid email and password combination and submitting, "
                        "the login is successful, and the user is redirected to the appropriate page or dashboard.")
    @allure.issue(issue_link("p1_2"), "Test issue: Check for successful login with valid credentials")
    def test_login_mixedcase_sensitivity_p1_2(self):
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
