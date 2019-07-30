from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "div.basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    
    
class ProductPageLocators(object):
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    DESCRIPTION_OF_GOOD = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE_OF_GOOD = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    DESCRIPTION_OF_GOOD_IN_THE_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_OF_GOOD_IN_THE_CART = (By.CSS_SELECTOR, "div.alert-info > div strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    DISAPPEARED_ELEMENT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    
class CartPageLocators(object):
    CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    ITEM_IN_THE_CART = (By.CSS_SELECTOR, ".basket-items")