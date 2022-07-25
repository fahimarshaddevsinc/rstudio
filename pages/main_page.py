import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class MainPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    NEW_SPACE = "//button[@class='menuItem newSpace']"
    NEW_SPACE_NAME_FIELD = "name"
    CREATE_NEW_SPACE_BUTTON = "//button[@type='submit']"
    NEW_PROJECT_BUTTON = "//button[@class='action menuDropDown withActionTitle imageRight alwaysShowTitle']"
    NEW_RSTUDIO_PROJECT_BUTTON = "//button[@class='action newRStudioProject']"
    NEW_PROJECT_NAME_FIELD = "currentLocation"

    # Set Functions
    def click_new_space(self):
      self.driver.find_element(By.XPATH, self.NEW_SPACE).click()

    def enter_new_space_name(self, space_name):
      self.driver.find_element(By.ID, self.NEW_SPACE_NAME_FIELD).send_keys(space_name)

    def click_create_space_button(self):
      self.driver.find_element(By.XPATH, self.CREATE_NEW_SPACE_BUTTON).click()

    def click_new_project_button(self):
      self.driver.find_element(By.XPATH, self.NEW_PROJECT_BUTTON).click()

    def click_new_rstudio_button(self):
      self.driver.find_element(By.XPATH, self.NEW_RSTUDIO_PROJECT_BUTTON).click()

    def enter_new_project_name(self, project_name):
      self.driver.find_element(By.ID, self.NEW_PROJECT_NAME_FIELD).send_keys(project_name)

    # Test Functions
    def create_new_space(self, space_name):
      self.click_new_space()
      time.sleep(5)
      self.enter_new_space_name(self, space_name)
      time.sleep(2)
      self.click_create_space_button()
      time.sleep(5)

    def create_new_project(self, project_name):
      self.click_new_project_button()
      self.click_new_rstudio_button()
      self.enter_new_project_name(project_name)
