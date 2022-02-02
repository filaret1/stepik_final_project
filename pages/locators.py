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
    ADD_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    ADDED_PRODUCT = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    CART_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_TEXT = (By.XPATH, "//*[@id='content_inner']/p")
    SOME_ITEM = (By.XPATH, "//div[@class='basket-items']")