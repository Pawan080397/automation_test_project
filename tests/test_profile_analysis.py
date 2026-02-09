import pytest
from pages.profile_analysis_page import ProfileAnalysisPage
import re

def normalize(text):
    text = text.lower()
    text = text.replace("_", " ")
    text = re.sub(r"\s+", " ", text)  # multiple spaces → single space
    return text.strip()

@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_profile_analysis_hover_menu(driver):
    page = ProfileAnalysisPage(driver)

    # 1 mouse hover
    page.hover_on_profile_analysis()

    # 2️ validate list
    assert page.is_option_visible(page.equipment_profile)
    assert page.is_option_visible(page.location_profile)
    assert page.is_option_visible(page.formation_profile)
    assert page.is_option_visible(page.civil_org)
    assert page.is_option_visible(page.person_profile)

@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_equipment_profile_data(driver):
    page = ProfileAnalysisPage(driver)
    page.hover_on_profile_analysis()
    page.click_equipment_profile()
    assert page.is_equipment_data_present(), " Equipment Profile table has NO data"


    page = ProfileAnalysisPage(driver)
    page.hover_on_profile_analysis()
    page.click_location_profile()
    assert page.is_location_data_present(), " Location Profile table has NO data"

    page.hover_on_profile_analysis()
    page.click_formation_profile()
    assert page.is_formation_data_present(), "formation Profile table has NO data"

    page.hover_on_profile_analysis()
    page.click_civilorg_profile()
    assert page.is_civilorg_data_present(), "Civil org Profile table has No data"

    page.hover_on_profile_analysis()
    page.click_person_profile()
    assert page.is_person_data_present(), "Person Profile table has No data"

@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_open_equipment_profile_data(driver):
    page = ProfileAnalysisPage(driver)
    page.hover_on_profile_analysis()                            # 1️ Click on Equipment Profile
    page.click_equipment_profile()


    list_profile_name = page.get_first_profile_name()           # 2️ Capture profile name from list

    main_window = driver.current_window_handle                  # 3️ Click on view icon
    page.click_view_icon()

    # 4️ Switch to new tab
    driver.switch_to.window(
        [w for w in driver.window_handles if w != main_window][0]
    )


    view_profile_heading = page.get_profile_heading()            # 5️ Get heading from view page

    list_name = normalize(list_profile_name)
    view_name = normalize(view_profile_heading)

    # 6️ VALIDATION
    print("FINAL COMPARISON:")
    print("From List :", list_name)
    print("From View :", view_name)

    assert list_name in view_name
