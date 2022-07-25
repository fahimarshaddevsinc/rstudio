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
    NEW_PROJECT_NAME_FIELD = "//button[@class='projectTitle clearButtonStyles']"
    HEADER_TITLE = "headerTitle"

    # Get Functions
    def get_header_title(self):
      return self.driver.find_element(By.ID, self.HEADER_TITLE).text

    def get_project_name(self):
      return self.driver.find_element(By.XPATH, self.NEW_PROJECT_NAME_FIELD).text

    # Set Functions
    def click_new_space(self):
      self.driver.find_element(By.XPATH, self.NEW_SPACE).click()

    def enter_new_space_name(self, name):
      self.driver.find_element(By.ID, self.NEW_SPACE_NAME_FIELD).send_keys(name)

    def click_create_space_button(self):
      self.driver.find_element(By.XPATH, self.CREATE_NEW_SPACE_BUTTON).click()

    def click_new_project_button(self):
      self.driver.find_element(By.XPATH, self.NEW_PROJECT_BUTTON).click()

    def click_new_rstudio_button(self):
      self.driver.find_element(By.XPATH, self.NEW_RSTUDIO_PROJECT_BUTTON).click()

    def enter_new_project_name(self, name):
      self.driver.find_element(By.XPATH, self.NEW_PROJECT_NAME_FIELD).send_keys(name)

    # Test Functions
    def create_new_space(self, name):
      self.driver.get("https://rstudio.cloud/projects/")
      element = BaseDriver.wait_until_element_presence_of_element_located(self, By.XPATH, self.NEW_SPACE)
      self.click_new_space()
      element = BaseDriver.wait_until_element_presence_of_element_located(self, By.ID, self.NEW_SPACE_NAME_FIELD)
      self.enter_new_space_name(name)
      element = BaseDriver.wait_until_element_presence_of_element_located(self, By.XPATH, self.CREATE_NEW_SPACE_BUTTON)
      self.click_create_space_button()
      time.sleep(2)
      element = BaseDriver.wait_until_element_presence_of_element_located(self, By.ID, self.HEADER_TITLE)
      return self.get_header_title()

    def create_new_project(self):
      self.driver.get("https://rstudio.cloud/projects/")
      element = BaseDriver.wait_until_element_presence_of_element_located(self, By.XPATH, self.NEW_PROJECT_BUTTON)
      self.click_new_project_button()
      self.click_new_rstudio_button()
      time.sleep(30)
      return self.get_project_name()
