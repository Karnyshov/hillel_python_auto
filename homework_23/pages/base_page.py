"""
Организовать пэйдж обджекты
Описать базовые методы по клику, сенд кейсу, скролу и прочие в базовой странице
"""

from homework_23.core.Singleton import Singleton
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage(Singleton):
    def __init__(self, driver):
        super().__init__(driver)

        self._wait = WebDriverWait(driver, 5)

    def wait_until_visible(self, locator):
        return self._wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
