# https://stackoverflow.com/questions/47649746/wait-for-css-property-to-change-before-asserting-the-change
# https://stackoverflow.com/questions/15102323/how-to-get-a-color-of-a-web-element-using-selenium-webdriver-with-python

from selenium.webdriver.support.color import Color


class ElementHasCssProperty(object):
    """An expectation for checking that an element has a particular css property value

    locator - used to find the element
    returns the WebElement once it has the particular css property with specified value
    """
    def __init__(self, locator, css_property: str, value: str):
        self.locator = locator
        self.css_property = css_property
        self.value = value

    def __call__(self, driver):
        element = driver.find_element(*self.locator)  # Finding the referenced element
        if element.value_of_css_property(self.css_property) == self.value:
            return element
        else:
            return False


class ElementHasCssPropertyColorHex(object):
    """An expectation for checking that an element has a particular css property value converted to the hex color

    locator - used to find the element
    returns the WebElement once it has the particular css property with specified value
    """
    def __init__(self, locator, css_property: str, value: str):
        self.locator = locator
        self.css_property = css_property
        self.value = value

    def __call__(self, driver):
        # Finding the referenced element
        element = driver.find_element(*self.locator)
        # convert color string to hex
        color_value = element.value_of_css_property(self.css_property)
        hex_color = Color.from_string(color_value).hex
        # compare against value
        if hex_color == self.value:
            return element
        else:
            return False
