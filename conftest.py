import pytest
from selenium.webdriver.support import expected_conditions
import selenium


@pytest.fixture(scope='module')
def start():
    start = selenium.webdriver.Chrome(executable_path='D:\\learn\\projects\\test_selenium\\chromedriver.exe')
    start.fullscreen_window()
    start.get('https://market.yandex.ru/')
    start.implicitly_wait(20)
    return start
