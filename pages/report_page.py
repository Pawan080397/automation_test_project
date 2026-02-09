from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReportPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Report tab
    REPORT_TAB = (By.XPATH, "//a[normalize-space()='Reports']")

    # Table rows (data rows)
    REPORT_TABLE_ROWS = (By.XPATH, "//table//tbody")

    def click_report_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.REPORT_TAB)).click()

    def is_report_data_present(self):
        rows = self.wait.until(
            EC.presence_of_all_elements_located(self.REPORT_TABLE_ROWS)
        )
        return len(rows) > 0

    def get_all_report_data(self):
        rows = self.wait.until(
            EC.presence_of_all_elements_located(self.REPORT_TABLE_ROWS)
        )

        all_data = []

        for row in rows:
            cells = row.find_elements(By.XPATH, ".//td")
            row_data = [cell.text.strip() for cell in cells]
            all_data.append(row_data)

        return all_data
