from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.basket_null_text()

#  pytest -v --tb=line --language=en test_main_page.py::test_guest_cant_see_product_in_basket_opened_from_main_page