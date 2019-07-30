from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        field_email_address = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        field_email_address.send_keys(email)
        field_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        field_password.send_keys(password)
        field_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        field_confirm_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "URL is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    