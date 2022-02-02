from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_NEW_USER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_NEW_USER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_NEW_USER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_NEW_USER_BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")

class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    ITEM_NAME = (By.CSS_SELECTOR, "div[class = \"col-sm-6 product_main\"] > h1")
    ITEM_ADDED_TEXT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_COST = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
    ITEM_COST = (By.CSS_SELECTOR, "p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "form.basket_summary")