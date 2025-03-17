from pages.BasePage import BasePage
from  selenium.webdriver.common.by import By

class LoginPageLocators:
    QR_TAB = (By.ID, 'login-9255135378')
    INPUT_TAB = (By.ID, 'qrCode-9255135426')

    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    QR_BUTTON = (By.ID, 'qrCode-8899793566')
    HYPER_LINK_CANT_LOGIN = (By.ID, '//*[@data-l="t,restore"]')

    REGISTER_BUTTON = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]')
    VK_ICON = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    EMAIL_ICON = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    YANDEX_ICON = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')


class LoginPageHelper(BasePage):
    pass