from homework_23.pages.base_page import BasePage
from selenium.webdriver import Chrome


class MainPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)

        # self._price_button_locator = self._wait_until_visible("//div[1]/div[1]/div//a[@routerlink='/prices']")
        self._price_button_locator = self.wait_until_visible("//div[1]/div[1]/div//a[@routerlink='/prices']")

    def open_prices_page(self):
        self._price_button_locator.click()
