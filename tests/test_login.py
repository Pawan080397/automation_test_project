from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.mark.admin
@pytest.mark.user("admin")
def test_login_success_admin(driver):
    # wait until page title is "IFS"
    wait = WebDriverWait(driver, 20)
    wait.until(lambda d: d.title == "IFS")
    # assert the title
    assert driver.title == "IFS"

@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_login_success_analyst(driver):
    # wait until page title is "IFS"
    wait = WebDriverWait(driver, 20)
    wait.until(lambda d: d.title == "IFS")
    # assert the title
    assert driver.title == "IFS"