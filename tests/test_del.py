from pages.labirint_locators import MainPage
import time

# Для запуска тестов этойго файла ввести в терминал:
# python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_del.py
def test_make_more_books_in_cart(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    page.btn_ok_close.click()
    page.plus_one_more.click()
    time.sleep(30)

    assert page.two_books_in_cart
