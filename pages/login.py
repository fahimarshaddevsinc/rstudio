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
    PASSWORD = "//input[@name='password']"
    CONTINUE = "button[type=\"submit\"]"
    LOGIN = "button[type=\"submit\"]"
    RSTUDIO_CLOUD = "a[@class='appPicker cloud noLink']"
    LOGIN_MESSAGE_FIELD = "//span[contains(text(), 'You are logged in to RStudio. Please select your destination.')]"

    # get funtions
    def get_email_field(self):
        return self.driver.find_element(By.NAME, self.EMAIL)

    def get_continue_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.CONTINUE)

    def get_password_field(self):
        return self.driver.find_element(By.XPATH, self.PASSWORD)

    def get_login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.LOGIN)

    def get_rstudio_button(self):
        return self.driver.find_element(By.XPATH, self.RSTUDIO_CLOUD)

    def get_login_text(self):
        return self.driver.find_element(By.XPATH, self.LOGIN_MESSAGE_FIELD).text

    # set functions
    def enter_email_id(self, email):
        self.get_email_field().send_keys(email)

    def enter_password(self, password):
        self.get_password_field().send_keys(password)

    def click_continue_button(self):
        self.get_continue_button().click()

    def click_login_button(self):
        self.get_login_button().click()

    def click_rstudio_cloud(self):
        self.get_rstudio_button().click()

    # test functions
    def login_to_website(self, email, password):
        self.enter_email_id(email)
        self.click_continue_button()
        element = BaseDriver.wait_until_element_presence_of_element_located(self, By.XPATH, self.PASSWORD)
        self.enter_password(password)
        self.click_login_button()

    

