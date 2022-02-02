from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def product_name_is_correct(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME)
        message_about_adding = self.browser.find_element(
            *ProductPageLocators.ADDED_PRODUCT)
        print(product_name.text)
        print(message_about_adding.text)
        assert product_name.text == message_about_adding.text, "No product name in the message"

    def should_be_correct_adding_product_price(self):
        message_basket_total = self.browser.find_element(
            *ProductPageLocators.CART_PRICE)
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE)
        print(product_price.text)
        print(message_basket_total.text)
        assert product_price.text == message_basket_total.text, "Price is not correct"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT), "seccess messege is not present, but should be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ADDED_PRODUCT), "seccess messege is present, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT), \
            "Success_message is not disappeared"
