from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_add_to_cart.click()
        
    def should_be_product_page(self):
        self.should_be_message_add_to_cart()
        self.should_be_message_price_of_cart()
        
    def should_be_message_add_to_cart(self):
        description_of_good = self.browser.find_element(*ProductPageLocators.DESCRIPTION_OF_GOOD).text        
        description_of_good_in_the_cart = self.browser.find_element(*ProductPageLocators.DESCRIPTION_OF_GOOD_IN_THE_CART).text        
        assert description_of_good == description_of_good_in_the_cart, "Description of good does not match"
        
    def should_be_message_price_of_cart(self):
        price_of_good = self.browser.find_element(*ProductPageLocators.PRICE_OF_GOOD).text        
        price_of_good_in_the_cart = self.browser.find_element(*ProductPageLocators.PRICE_OF_GOOD_IN_THE_CART).text        
        assert price_of_good == price_of_good_in_the_cart, "Price of good does not match"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
       
    def should_be_disapeared(self):
        assert self.is_disappeared(*ProductPageLocators.DISAPPEARED_ELEMENT), \
        "Element is not disappeared"
    