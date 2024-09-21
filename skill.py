from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

username_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "username"))
)
username_input.send_keys("Admin")

password_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "password"))
)
password_input.send_keys("admin123")

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "oxd-button--main"))
)
login_button.click()

admin_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/web/index.php/admin/viewAdminModule')]"))
)
admin_link.click()

qualifications_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Qualifications')]"))
)
qualifications_menu.click()
skills_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li/a[contains(@class,'oxd-topbar-body-nav-tab-link') and contains(text(),'Skills')]"))
)
skills_link.click()
add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "oxd-button--secondary"))
)
add_button.click()
input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@data-v-957b4417]//input[@data-v-1f99f73c]"))
)
input_field.send_keys("Problem Solving")




textarea = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "oxd-textarea--active"))
)
textarea.send_keys("Employee")


save_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "oxd-button--secondary"))
)
save_button.click()
