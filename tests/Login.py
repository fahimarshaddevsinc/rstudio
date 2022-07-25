import time

import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from colorama import Fore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#chrome driver path
s = Service('/home/dev/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(2)
driver.maximize_window()
#give url of your website
url = 'https://rstudio.cloud/'
driver.get(url)
time.sleep(2)

#Click on Login from dashboard
Login = driver.find_element(By.LINK_TEXT, "Log In").click()
print(Fore.GREEN + 'Click on Login')

#Enter Email
Email = driver.find_element(By.NAME,"email").send_keys("emailusman.66@gmail.com")
print(Fore.GREEN + 'Enter Email Address for Login')


Continue = driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
print(Fore.GREEN + 'Click on Continue button')
time.sleep(2)

Password = driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Helloworld@11")
# Email = wait.until(EC.visiblity_of_element_located((By.NAME, "password"))).send_keys("Helloworld@11")
print(Fore.GREEN + 'Enter Password for Login')

Login = driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
print(Fore.GREEN + 'Click on Log In button')
time.sleep(10)

#Delete Existing space
Space = driver.find_element(By.CLASS_NAME, "spaceNameWithOwner").click()
print(Fore.GREEN + 'Click on Existing Space')
time.sleep(2)
Space = driver.find_element(By.XPATH, "//button[@class='action moreActions']").click()
print(Fore.GREEN + 'Click on Popup menu')
time.sleep(2)
Space = driver.find_element(By.XPATH, "//button[@class='action delete']").click()
print(Fore.GREEN + 'Click on Delete Space')
time.sleep(2)
Space = driver.find_element(By.XPATH, "//input[@aria-label='Name of space to delete']").send_keys("Delete Auto-Space")
print(Fore.GREEN + 'Enter "Delete Auto-Space')
time.sleep(2)
Space = driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(Fore.GREEN + 'Click on Delete button')
time.sleep(5)
#After login click on +New Space
Space = driver.find_element(By.XPATH, "//button[@class='menuItem newSpace']").click()
print(Fore.GREEN + 'Click on +New Space')
time.sleep(5)
Space = driver.find_element(By.ID, "name").send_keys("Auto-Space")
print(Fore.GREEN + 'Enter Space Name as Auto-Space')
time.sleep(2)
Space = driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(Fore.GREEN + 'Click on Create button')
time.sleep(5)

#Click on New Project
Project = driver.find_element(By.XPATH, "//button[@class='action menuDropDown withActionTitle imageRight alwaysShowTitle']").click()
print(Fore.GREEN + 'Click on New Project button')
time.sleep(2)
Project = driver.find_element(By.XPATH, "//button[@class='action newRStudioProject']").click()
print(Fore.GREEN + 'Click on New RStudio Project button')
time.sleep(20)
Project = driver.find_element(By.ID, "currentLocation").send_keys("Auto-Project")
print(Fore.GREEN + 'Re-Enter Project name as "Auto-Project"')
time.sleep(2)

driver.close
driver.quit()
