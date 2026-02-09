import pytest

from pages.user_management_page import UserManagementPage
@pytest.mark.admin
@pytest.mark.user("admin")
def test_create_user(driver):
    user_page = UserManagementPage(driver)

    # Navigation
    user_page.click_settings()
    user_page.click_user_management()
    user_page.click_user_list()
    user_page.click_add_user()
    user_page.click_user_role()

    # Test data
    user_page.select_role("Admin")
    user_page.enter_username("test_user_03")
    user_page.enter_email("test_user_0011@gmail.com")
    user_page.enter_batch_no("BATCH_101")
    user_page.enter_phone("9876543210")
    user_page.enter_password("Test@1234")
    user_page.enter_confirm_password("Test@1234")

    user_page.click_continue()

    assert user_page.is_user_created_successfully(), "User creation failed"
