import allure

from pages.BasePage import BasePage
from  selenium.webdriver.common.by import By

class LoginPageLocators:
    QR_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')

    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    HYPER_LINK_CANT_LOGIN = (By.XPATH, '//*[@data-l="t,restore"]')

    REGISTRATION_BUTTON = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]')
    VK_ICON = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    EMAIL_ICON = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    YANDEX_ICON = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')

    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')

    RECOVERY_BUTTON = (By.XPATH, '//*[@class="button-pro __wide mb-3x"]')
    RETURN_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="external-oauth-login_title-tx"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки старницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.QR_BUTTON)
        self.find_element(LoginPageLocators.HYPER_LINK_CANT_LOGIN)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_ICON)
        self.find_element(LoginPageLocators.EMAIL_ICON)
        self.find_element(LoginPageLocators.YANDEX_ICON)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Вводим значение в поле "Логин"')
    def input_value_login_field(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Вводим значение в поле "Пароль"')
    def input_value_password_field(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RECOVERY_BUTTON).click()

    @allure.step('Нажимаем на кнопку "Регистрация"')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()
