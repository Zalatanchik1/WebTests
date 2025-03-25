import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageLocators, HelpPageHelper
from pages.AdvertisementCabinetHelp import AdvertismentCabinetHelpHelper

BASE_URL = 'https://ok.ru/help'


@allure.suite('Проверка формы "Помощь"')
@allure.title('Проверка скролла и переход в "Рекламный кабинет" страницы "Помощь"')
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertismentCabinetHelpHelper(browser)
