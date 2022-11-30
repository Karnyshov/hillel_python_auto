"""
Создать тест в котором происходит инициализация драйвера.
Перейдите на любой выбранный вами ресурс.
Нажмите на копку либо введите текст в поле ввода.
В этом же тесте попробуйте реализовать скролинг в окне где есть скрол бар."""

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome()

driver.get("https://taxer.ua/")
price_button_locator = "//div[1]/div[1]/div//a[@routerlink='/prices']"

sleep(2)
price_button = driver.find_element(By.XPATH, price_button_locator)
sleep(2)
price_button.click()
sleep(2)
driver.maximize_window()
sleep(2)

driver.execute_script("window.scrollBy(0, 500)", "")
sleep(2)
