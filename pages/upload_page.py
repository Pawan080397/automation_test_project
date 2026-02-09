from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UploadPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    INGESTOR_NAME = (By.XPATH, "//span[normalize-space()='WIS Injester']")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")
    UPLOAD_BUTTON = (By.XPATH, "//span[normalize-space()='Upload']")


    def click_ingestor_name(self):
        self.wait.until(EC.element_to_be_clickable(self.INGESTOR_NAME)).click()


    def select_file(self, file_path):
        file_input = self.wait.until(EC.presence_of_element_located(self.FILE_INPUT))
        file_input.send_keys(file_path)

    def click_upload(self):
        self.wait.until(EC.element_to_be_clickable(self.UPLOAD_BUTTON)).click()

    def is_file_uploaded_successfully(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'Activity form created successfully')]")
            )
        ).is_displayed()
