import allure

from pages.BasePage import BasePageHelper
from  selenium.webdriver.common.by import By

class VKEcosystemPageLocators:
    VK_LOGO = (By.XPATH, '//*[@class="Header_logo__tL_od"]')

class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки старницы'):
            self.attach_screenshot()
        self.find_element(VKEcosystemPageLocators.VK_LOGO)
