from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.demoblaze.com/")

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "signin2"))
).click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "sign-username"))
).send_keys("haris")

driver.find_element(By.ID, "sign-password").send_keys("haris")

driver.find_element(By.XPATH, "//button[contains(text(), 'Sign up')]").click()

time.sleep(10)
