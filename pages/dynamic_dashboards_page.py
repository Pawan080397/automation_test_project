import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class DynamicDashboardsPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

        self.wait = WebDriverWait(driver, 20)

    # Dynamic Dashboard tab locator
    Dynamic_Dashboard = (By.XPATH, "//a[normalize-space()='Dynamic Dashboards']")
    # Loader / overlay (jo click block kar raha hai)
    loader_overlay = (
        By.XPATH,
        "//div[contains(@style,'z-index: 1000')]"
    )
    Rank_button = (By.XPATH, "//button[@class='primary-btn rankButton']")

    def click_on_Dynamic_dashboards(self):

        # wait till loader disappears
        self.wait.until(
            EC.invisibility_of_element_located(self.loader_overlay)
        )

        # wait till tab clickable
        element = self.wait.until(
            EC.element_to_be_clickable(self.Dynamic_Dashboard)
        )
        assert element.is_displayed(), "Dynamic dashboards tab is NOT visible"
        element.click()
    def click_on_Rank(self):

        # wait till loader disappears
        self.wait.until(
            EC.invisibility_of_element_located(self.loader_overlay)
        )

        # wait till tab clickable
        element = self.wait.until(
            EC.element_to_be_clickable(self.Rank_button)
        )
        assert element.is_displayed(), "Dynamic dashboards tab is NOT visible"
        element.click()

