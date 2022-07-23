import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class Login(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    EMAIL = "email"
    PASSWORD = "password"
    CONTINUE = "button[type=\"submit\"]"
    LOGIN = "button[type=\"submit\"]"

    # get funtions
    def get_email_field(self):
        return self.driver.find_element(By.NAME, self.EMAIL)

    def get_continue_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.CONTINUE)

    def get_password_field(self):
        return self.driver.find_element(By.NAME, self.PASSWORD)

    def get_login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.LOGIN)

    # set functions
    def enter_email_id(self, email):
        self.get_email_field().send_keys(email)

    def enter_password(self, password):
        self.get_password_field().send_keys(password)

    def click_continue_button(self):
        self.get_continue_button().click()

    def click_login_button(self):
        self.get_login_button().click()

    def login_to_website(self, email, password):
        self.enter_email_id(email)
        self.click_continue_button()
        self.enter_password(password)
        self.click_login_button()
