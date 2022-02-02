from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), "Message 'basket is empty' is " \
                                                                                     "not presented"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "Items in basket are presented but " \
                                                                                 "should not be"
