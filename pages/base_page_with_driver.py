import pytest

from driver import Driver
from conditions.element_has_css_property import ElementHasCssProperty, ElementHasCssPropertyColorHex

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import TimeoutException


class BasePageWithDriver:

    WEB_DRIVER_WAIT_TIMEOUT = 2

    def __init__(self):
        self._driver = Driver.get_chrome_driver()
        self.wait = WebDriverWait(self._driver, self.WEB_DRIVER_WAIT_TIMEOUT)

    def wait_element_css_property(self, locator, css_property: str, value: str):
        try:
            return self.wait.until(ElementHasCssProperty(
                locator,
                css_property, value
            ))
        except TimeoutException:
            element = self._driver.find_element(*locator)
            result = element.value_of_css_property(css_property)
            pytest.fail(f'locator:{locator}, property:{css_property}, expected:{value}, got:{result}')

    def wait_element_css_property_color_hex(self, locator, css_property: str, value: str):
        try:
            return self.wait.until(ElementHasCssPropertyColorHex(
                locator,
                css_property, value
            ))
        except TimeoutException:
            element = self._driver.find_element(*locator)
            color_value = element.value_of_css_property(css_property)
            result = Color.from_string(color_value).hex
            pytest.fail(f'locator:{locator}, property:{css_property}, expected:{value}, got:{result}')
