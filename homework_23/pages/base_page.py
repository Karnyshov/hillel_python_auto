"""
Организовать пэйдж обджекты
Описать базовые методы по клику, сенд кейсу, скролу и прочие в базовой странице
"""

from homework_23.core.Singleton import Singleton
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep


class BasePage(Singleton):
    def __init__(self, driver):
        super().__init__(driver)

        self._wait = WebDriverWait(driver, 5)

        self._body = "/html/body"
        self._header = "//layout-header"
        self._footer = "//layout-footer"
        self._logo_button = "//div[1]/layout-header/header/div/a[1]"

    def find_visible(self, locator):
        return self._wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def scroll_to_footer(self):
        body = self._driver.find_element(By.XPATH, self._body)
        body.send_keys(Keys.END)

    def scroll_to_header(self):
        body = self._driver.find_element(By.XPATH, self._body)
        body.send_keys(Keys.HOME)

    def scroll_to_element(self, locator):
        element = self._driver.find_element(By.XPATH, locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
        sleep(3)

    def get_title(self):
        return self._driver.title

    def get_current_url(self):
        return self._driver.current_url

    def open_main_page(self):
        self._wait.until(ec.visibility_of_element_located((By.XPATH, self._logo_button))).click()
