# запуск pytest -v --tb=line --language=en test_main_page.py
# або для класу за маркуванням pytest -m login_guest test_main_page.py
import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)  # ініціалізуєм Page Object, передаємо в конструктор драйвера екземпляр драйвера і url адресу
        page.open()  # відкриваємо сторінку
        page.go_to_login_page()  # виконуємо метод сторінки — переходимо на сторінку логіна
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.view_basket()
    page.basket_should_be_empty()
    page.basket_should_have_message_about_emptiness()

