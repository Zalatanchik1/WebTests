import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelper

BASE_URL = 'https://ok.ru/'


@allure.suite('Проверка формы регистрации')
@allure.title('Проверка соответствия маски поля "Номер телефона" со страной в поле "Страна/регион"')
def test_registration_random_country(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelper(browser)
    RegistrationPage.select_random_country()
    Selected_country_code = RegistrationPage.select_random_country()
    Actual_actual_code = RegistrationPage.get_phone_field_value()
    assert Selected_country_code == Actual_actual_code
