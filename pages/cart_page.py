from .base_page import BasePage
from .locators import CartPageLocators
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def cart_should_be_empty(self):
        assert self.is_element_present(*CartPageLocators.CART_IS_EMPTY), "Cart is not empty"
    
    def items_should_not_be(self):
        assert self.is_not_element_present(*CartPageLocators.ITEM_IN_THE_CART), "Cart has item"