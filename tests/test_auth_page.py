from pages.labirint_locators import MainPage

# Для запуска тестов этойго файла ввести в терминал:
# python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_auth_page.py

"""Тестируем возможность входа  в личный кабинет с корректным и некорректным логином (код скидки). 4 теста."""

"""Вход с корретными данными"""


def test_valid_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("9547-4779-8CFD")
    page.enter.click()
    page.automatic_closing.click()

    assert page.get_current_url() == 'https://www.labirint.ru/'


"""Вход с некорретными данными"""


def test_invalid_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("947C-43B6-8BC9")
    page.enter.click()

    assert page.auth_error


"""Вход с пробелом"""


def test_blanc_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("             ")

    assert page.auth_error_2


"""Вход по электронной почте"""


def test_email_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("test@gmail.com")
    page.enter.click()

    assert page.login_field
