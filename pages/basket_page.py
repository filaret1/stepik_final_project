from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.SOME_ITEM), \
            "Some item in basket now!"

    def basket_null_text(self):
        assert "Your basket is empty. " in self.element_text(*BasketPageLocators.EMPTY_TEXT)