from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class UserManagementPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Navigation
    def click_settings(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='jss2']//li[4]//*[name()='svg']")
        )).click()

    def click_user_management(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='User Management']")
        )).click()

    def click_user_list(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='User List']")
        )).click()

    def click_add_user(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Add']")
        )).click()

    def click_user_role(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@id=':r4:']")
        )).click()


    # Form actions
    def select_role(self, role_name):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[normalize-space()='{role_name}']")
        )).click()

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, "//input[@id=':r9:']").send_keys(username)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, "//input[@id=':ra:']").send_keys(email)

    def enter_batch_no(self, batch):
        self.driver.find_element(By.XPATH, "//input[@id=':rc:']").send_keys(batch)

    def enter_phone(self, phone):
        self.driver.find_element(By.XPATH, "//input[@id=':rb:']").send_keys(phone)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, "//input[@id=':rd:']").send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(By.XPATH, "//input[@id=':re:']").send_keys(password)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Continue']")
        )).click()


    def is_user_created_successfully(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'User Added successfully')]")
            )
        ).is_displayed()
