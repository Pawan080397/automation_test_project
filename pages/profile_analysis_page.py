from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfileAnalysisPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.actions = ActionChains(driver)

    # 🔹 Profile Analysis tab
    profile_analysis_tab = (
        By.XPATH, "//a[normalize-space()='Profile Analysis']"
    )

    # 🔹 dropdown list items
    equipment_profile = (By.XPATH, "//a[normalize-space()='Equipment Profile']")
    location_profile = (By.XPATH, "//a[normalize-space()='Location Profile']")
    formation_profile = (By.XPATH, "//a[normalize-space()='Formation Profile']")
    civil_org = (By.XPATH, "//a[normalize-space()='Civil Organization']")
    person_profile = (By.XPATH, "//a[normalize-space()='Person Profile']")
    table_rows = (By.XPATH, "//table//tbody/tr")
    def hover_on_profile_analysis(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.profile_analysis_tab)
        )
        self.driver.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));",
            element
        )

    def is_option_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    def click_equipment_profile(self):
        self.wait.until(
            EC.element_to_be_clickable(self.equipment_profile)
        ).click()

    def is_equipment_data_present(self):
        rows = self.wait.until(
            EC.presence_of_all_elements_located(self.table_rows)
        )
        return len(rows) > 0

    def click_location_profile(self):
        self.wait.until(
            EC.element_to_be_clickable(self.location_profile)
        ).click()

    def is_location_data_present(self):
        rows = self.wait.until(
            EC.presence_of_all_elements_located(self.table_rows)
        )
        return len(rows) > 0

    def click_formation_profile(self):
        self.wait.until(
            EC.element_to_be_clickable(self.formation_profile)
        ).click()

    def is_formation_data_present(self):
        rows = self.wait.until(
            EC.presence_of_all_elements_located(self.table_rows)
        )
        return len(rows) > 0

    def click_civilorg_profile(self):
        self.wait.until(
            EC.element_to_be_clickable(self.civil_org)
        ).click()

    def is_civilorg_data_present(self):
        rows = self.wait.until(
            EC.presence_of_all_elements_located(self.table_rows)
        )
        return len(rows) > 0

    def click_person_profile(self):
        self.wait.until(
            EC.element_to_be_clickable(self.person_profile)
        ).click()

    def is_person_data_present(self):
        rows = self.wait.until(
            EC.presence_of_all_elements_located(self.table_rows)
        )
        return len(rows) > 0

    first_profile_name = (
            By.XPATH, "//td[normalize-space()='TTQA 16']"
        )
    first_view_icon = (
        By.XPATH, "//tbody/tr[1]/td[4]//*[name()='svg']"
    )

    # Heading in view page
    profile_heading = (
        By.XPATH, "//h4[normalize-space()='TTQA_16']"
    )

    def get_first_profile_name(self):
        name = self.wait.until(
            EC.visibility_of_element_located(self.first_profile_name)
        ).text.strip()

        print("LIST PROFILE NAME:", name)
        return name



    def click_view_icon(self):
        self.wait.until(
            EC.element_to_be_clickable(self.first_view_icon)
        ).click()

    def get_profile_heading(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(self.profile_heading)
        ).text.strip()

        print("VIEW PROFILE HEADING:", heading)
        return heading