from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)  # max 20 seconds wait

    username = (By.XPATH, "//input[@type='text']")
    password = (By.XPATH, "//input[@type='password']")
    login_btn = (By.XPATH, "//span[@class='MuiButton-label']")

    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(pwd)
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()

