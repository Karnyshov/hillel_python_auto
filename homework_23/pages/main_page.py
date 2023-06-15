from homework_23.pages.base_page import BasePage
from homework_23.pages.prices_page import PricesPage
from homework_23.pages.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

# TODO: Improve calling?
        self._locators = MainPageLocators.MainPageLocators()

        self._page_url = "https://taxer.ua/uk/"
        self._page_title = "Taxer.ua — Електронний кабінет підприємця"

    def open_prices_page(self):
        self.find_visible(self._common_locators.header_price_button).click()
        return PricesPage(self._driver)
