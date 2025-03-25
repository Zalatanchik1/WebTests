import allure
import random

from pages.BasePage import BasePageHelper
from  selenium.webdriver.common.by import By

class RegistrationPageLocators:
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//div[@class="country-select_code"]')
    PHONE_FIELD = (By.XPATH, '//div[@data-l="t,phone"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="svg-ic svg-ico_help_circle_16 tico_img"]')

class RegistrationPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки старницы'):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.COUNTRY_LIST)
        self.find_element(RegistrationPageLocators.PHONE_FIELD)
        self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
        self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)

    def select_random_country(self):
        random_number = random.randint(0, 212)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        country_code = country_items[random_number].get_attribute('text')
        with allure.step('Проверяем корректность загрузки старницы'):
            self.attach_screenshot()
        country_items[random_number].click()
        return country_code

    def get_phone_field_value(self):
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('value')