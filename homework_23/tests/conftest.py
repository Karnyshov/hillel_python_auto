import pytest
from homework_23.pages.main_page import MainPage


@pytest.fixture(scope="session")
def main_page(driver):
    main_page = MainPage(driver)
    yield main_page
