import allure

from pages.BasePage import BasePageHelper
from  selenium.webdriver.common.by import By

class RecoveryStartPageLocators:
    PHONE_BUTTON = (By.XPATH, '//*[@data-l="t,phone"]')
    EMAIL_BUTTON = (By.XPATH, '//*[@data-l="t,email"]')
    QR_CODE = (By.XPATH, '//*[@class="qr_code_image"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="support-link_item-text"]')

class RecoveryStartPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки старницы'):
            self.attach_screenshot()
        self.find_element(RecoveryStartPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryStartPageLocators.EMAIL_BUTTON)
        self.find_element(RecoveryStartPageLocators.QR_CODE)
        self.find_element(RecoveryStartPageLocators.SUPPORT_BUTTON)

