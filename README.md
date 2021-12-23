Итоговый проект по курсу SF группы QAP-39 по автоматизированному тестирвоанию с использованием PyTest и Selenium
интернет-магазина Labirint.ru.

Для запуска тестов необходимо предварительно установить следующие библиотеки (pip install):
1. pytest
2. pytest-selenium
3. selenium
4. termcolor
5. allure-python-commons

Актуальный нв 23.12.2021 драйвер для браузера Crome лежит в папке tests.

Для запуска всех тестов в данном репрезитории необходимо ввести команду:
python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe

Тестируемые сценарии:
1. tests_test_auth_page.py - Тестируем возможность входа в личный кабинет. 4 теста. 
   Для запуска теста вводим команду:
   python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_cart_page.py

2. test_book_page.py - Тестируем книги с главной страницы. 4 теста. 
   Для запуска теста вводим команду:
   python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_book_page.py

3. test_home_page.py - Тестируем ссылки в шапке главной страницы. 32 теста. 
   Для запуска теста вводим команду:
   python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_home_page.py

4. test_search_page.py - Тестируем поиск по тексту с главной страницы. 7 тестов. 
   Для запуска теста вводим команду:
   python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_search_page.py

5. test_cart_page.py - Тестируем корзину с книгами. 3 теста. 
   Для запуска теста вводим команду:
   python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_cart_page.py

