from homework_23.pages.base_page import BasePage
from homework_23.pages.prices_page import PricesPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self._price_button_locator = "//div[1]/div[1]/div//a[@routerlink='/prices']"
        self._page_url = "https://taxer.ua/uk/"
        self._page_title = "Taxer.ua — Електронний кабінет підприємця"
        self._price_section = "//ui-section[3]/section/div/ui-heading"

    def open_prices_page(self):
        self.find_visible(self._price_button_locator).click()
        return PricesPage(self._driver)
