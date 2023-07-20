from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


class Driver:
    driver = None

    @staticmethod
    def get_chrome_driver() -> WebDriver:
        if Driver.driver is None:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            Driver.driver = webdriver.Chrome(options=chrome_options)
            Driver.driver.implicitly_wait(5)
            return Driver.driver
        else:
            return Driver.driver
