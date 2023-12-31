from selenium.webdriver.common.by import By
from .base_page_with_driver import BasePageWithDriver
from controls.button import Button
from controls.selectbox import SelectBox
from controls.textbox import TextBox


class GaragePage(BasePageWithDriver):
    def __init__(self):
        super().__init__()

    class Locators:

        add_carr_button = (By.XPATH, "//button[text()='Add car']")
        modify_car_button = (By.XPATH, "//button[contains(@class,'car_edit')]")
        form_add_car_button = (By.XPATH, "//button[text()='Add']")
        form_save_car_button = (By.XPATH, "//button[text()='Save']")
        form_remove_car_button = (By.XPATH, "//button[text()='Remove car']")
        form_remove_confirm_button = (By.XPATH, "//button[text()='Remove']")
        form_brand_field = (By.ID, "addCarBrand")
        form_model_field = (By.ID, "addCarModel")
        form_mileage_field = (By.ID, "addCarMileage")

    def get_my_profile_button(self):
        return Button(self._driver.find_element(By.ID, "userNavDropdown"))

    def get_add_car_button(self):
        return Button(self._driver.find_element(*self.Locators.add_carr_button))

    def get_modify_car_button(self):
        return Button(self._driver.find_element(*self.Locators.modify_car_button))

    def get_form_add_car_button(self):
        return Button(self._driver.find_element(*self.Locators.form_add_car_button))

    def get_form_save_car_button(self):
        return Button(self._driver.find_element(*self.Locators.form_save_car_button))

    def get_form_remove_car_button(self):
        return Button(self._driver.find_element(*self.Locators.form_remove_car_button))

    def get_form_remove_car_confirm_button(self):
        return Button(self._driver.find_element(*self.Locators.form_remove_confirm_button))

    def get_form_brand_field(self):
        return SelectBox(self._driver.find_element(*self.Locators.form_brand_field))

    def get_form_model_field(self):
        return SelectBox(self._driver.find_element(*self.Locators.form_model_field))

    def get_form_mileage_field(self):
        return TextBox(self._driver.find_element(*self.Locators.form_mileage_field))
