import time
import allure
from page_object import click_edit
import logging


log = logging.getLogger('log')


def test_yandex(start):
    """
    Тест проверяющий работу фильтра по цене на странице яндекс маркет
    :param start: фикстура запускающая экземпляр браузера
    :return:
    """
    with allure.step('Ввод значения для поиска'):
        log.info('Ввод значения для поиска')
        search_text = start.find_element_by_id('header-search')
        click_edit(loc=search_text).send_keys('Телевизоры Toshiba Москва')

    with allure.step('Нажатие кнопки "Найти"'):
        log.info('Нажатие кнопки "Найти"')
        search_click = start.find_element_by_xpath('//span[@class="search2__button"]')
        search_click.click()

    with allure.step('Ввод ограничения по цене'):
        log.info('Ввод ограничения по цене')
        search_price = start.find_element_by_id('glpriceto')
        click_edit(search_price).send_keys('20000')

    with allure.step('Ожидание загрузки'):
        log.info('Ожидание загрузки')
        time.sleep(10)

    # выборка найденного
    with allure.step('Формирование контрольного списка'):
        log.info('Формирование контрольного списка')
        result = start.find_elements_by_class_name('price')
        price_list = [price.text for price in result if int(str(price.text).replace(' ₽', '').replace(' ', '')) > 20000]

    with allure.step('Проверка контрольного списка'):
        log.info('Проверка контрольного списка')
        assert len(price_list) == 0, f"Контрольный список не пуст!\n Контрольный список:\n {price_list}"
