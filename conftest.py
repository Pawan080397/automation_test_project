# import pytest
# from utils.driver_factory import get_driver
# from pages.login_page import LoginPage
# from config.config import BASE_URL, USERNAME, PASSWORD
# import pytest
# import os
# from datetime import datetime
#
# @pytest.fixture(scope="session")
# def driver():
#     driver = get_driver()
#     driver.get(BASE_URL)
#
#     login_page = LoginPage(driver)
#     login_page.login(USERNAME, PASSWORD)
#
#     yield driver
#     driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import ReadConfig
from pages.login_page import LoginPage

@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get(ReadConfig.BASE_URL)

    # 🔑 default role
    role = "admin"

    marker = request.node.get_closest_marker("user")
    if marker:
        role = marker.args[0]

    user = ReadConfig.get_user(role)
    assert user, f"Invalid user role: {role}"

    # 🔐 login
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])

    yield driver
    driver.quit()







#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#
#     # sirf test execution phase
#     if report.when == "call":
#         driver = item.funcargs.get("driver", None)
#         if not driver:
#             return
#
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#
#         if report.passed:
#             screenshots_dir = "reports/screenshots/pass"
#             status = "PASS"
#         else:
#             screenshots_dir = "reports/screenshots/fail"
#             status = "FAIL"
#
#         os.makedirs(screenshots_dir, exist_ok=True)
#
#         screenshot_name = f"{item.name}_{status}_{timestamp}.png"
#         screenshot_path = os.path.join(screenshots_dir, screenshot_name)
#
#         driver.save_screenshot(screenshot_path)
#