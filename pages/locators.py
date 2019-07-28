from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators(object):
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    DESCRIPTION_OF_GOOD = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE_OF_GOOD = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    DESCRIPTION_OF_GOOD_IN_THE_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_OF_GOOD_IN_THE_CART = (By.CSS_SELECTOR, "div.alert-info > div strong")