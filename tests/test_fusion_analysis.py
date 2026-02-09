import pytest
from pages.fusion_analysis_page import FusionAnalysisPage
from utils.logger import get_logger

logger = get_logger("FusionDashboardTest")

@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_fusion_analysis_tab(driver):
    logger.info("Test started: fusion tab click")

    fusion_page = FusionAnalysisPage(driver)

    fusion_page.click_fusion_tab()
    logger.info("Test completed: fusion tab click")

@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_activity_type_list(driver):
    fusion_page = FusionAnalysisPage(driver)

    fusion_page.click_fusion_tab()

    # 2️ Open Activity Type filter
    fusion_page.click_activity_type_filter()

    # 3️ Read raw activity text
    raw_activities = fusion_page.get_activity_types_raw()

    print("\nRAW ACTIVITIES FROM UI:")
    for r in raw_activities:
        print("----")
        print(r)

    # 4️ CLEAN & SPLIT
    cleaned_activities = []
    for block in raw_activities:
        for line in block.split("\n"):
            if line.strip():
                cleaned_activities.append(line.strip())

    print("\nCLEANED ACTIVITIES:")
    for c in cleaned_activities:
        print("-", c)

    # 5️ Normalize text
    actual_set = {
        a.lower().replace("_", " ").strip()
        for a in cleaned_activities
    }

    expected_activities = [
        "Overall Data",
        "Force Disposition",
        "Training",
        "IMINT Analysis",
        "PLA Sitrep",
        "Infra Development",
        "SAM Deployment",
        "AIR Aspects",
        "mobile interception",
        "Overall Force Disposition"
    ]

    expected_set = {
        e.lower().replace("_", " ").strip()
        for e in expected_activities
    }

    print("\nACTUAL SET:", actual_set)
    print("EXPECTED SET:", expected_set)

    assert actual_set == expected_set, (
        f" Activity mismatch\n"
        f"Missing: {expected_set - actual_set}\n"
        f"Extra: {actual_set - expected_set}"
    )

@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_time_period_filter(driver):
    fusion_page = FusionAnalysisPage(driver)

    # 1️ Click on Fusion Analysis
    fusion_page.click_fusion_tab()

    # 2️ Click on Time Period filter
    fusion_page.click_time_period_filter()

    # 3️ Get raw options from UI
    raw_options = fusion_page.get_time_period_options()

    print("\nRAW OPTIONS FROM UI:")
    for o in raw_options:
        print(repr(o))

    # 4️ SPLIT multiline text properly
    cleaned_options = []
    for block in raw_options:
        lines = block.split("\n")
        for line in lines:
            line = line.strip()
            if line:
                cleaned_options.append(line)

    print("\nCLEANED OPTIONS:")
    for o in cleaned_options:
        print("-", o)

    # 5 Normalize actual values
    actual_set = {
        o.lower()
         .replace(" ", "")
         .replace("days", "day")
         .replace("months", "month")
         .strip()
        for o in cleaned_options
    }

    # 11 Expected options
    expected_options = [
        "1 Day",
        "7 Days",
        "14 Days",
        "30 Days",
        "45 Days",
        "60 Days",
        "90 Days",
        "6 Month",
        "1 Year",
        "2 Year",
        "Custom"
    ]

    expected_set = {
        e.lower()
         .replace(" ", "")
         .replace("days", "day")
         .replace("months", "month")
         .strip()
        for e in expected_options
    }

    print("\nACTUAL SET:", actual_set)
    print("EXPECTED SET:", expected_set)

    # 7️ STRICT VALIDATION
    missing = expected_set - actual_set
    extra = actual_set - expected_set

    assert not missing, f" Missing options: {missing}"
    assert not extra, f" Extra options: {extra}"

    print("Time Period filter validation PASSED")
    # 2️ Click Custom option
    fusion_page.click_custom_option()

    # 3️ Validate Start & End date fields
    assert fusion_page.is_start_date_visible(), "Start Date field not visible"
    assert fusion_page.is_end_date_visible(), "End Date field not visible"

    print("Custom Time Period shows Start & End Date filters")

import re
@pytest.mark.analyst
@pytest.mark.user("analyst")
def normalize_location(text: str) -> str:
    """
    Delhi (WTC) -> delhi
    Delhi, NCR  -> delhi
    """
    text = text.lower()
    text = re.sub(r"\(.*?\)", "", text)   # brackets hatao
    text = re.sub(r"[,|-].*", "", text)   # , ya - ke baad hatao
    return text.strip()
def test_location_filter(driver):
    fusion = FusionAnalysisPage(driver)

    fusion.click_fusion_tab()
    fusion.click_time_period_filter()
    fusion.get_time_period_options()
    fusion.SELECT_TWO_YEARS()


    selected = fusion.select_location_from_suggestions("del")

    print("\nFINAL SELECTED LOCATIONS:")
    for s in selected:
        print("-", s)

    fusion.click_on_search()
    fusion.click_on_table_view()
    # time.sleep(10)

    assert fusion.is_table_data_present(), "No data after applying filter"

    #  SINGLE SOURCE OF TRUTH
    selected = fusion.get_selected_locations()
    table_locations = fusion.get_table_locations()

    print("SELECTED RAW:", selected)
    print("TABLE RAW:", table_locations)

    selected_norm = {normalize_location(s) for s in selected}

    invalid = []
    for loc in table_locations:
        if normalize_location(loc) not in selected_norm:
            invalid.append(loc)

    assert not invalid, f" Table data and filter data is not same : {invalid}"



@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_equipment_type_filter(driver):

    fusion = FusionAnalysisPage(driver)
    fusion.click_time_period_filter()
    fusion.SELECT_TWO_YEARS()
    fusion.click_on_search()


    # 1️⃣ More filter
    fusion.click_more_filter()

    # 2️⃣ Equipment type filter
    fusion.click_equipment_type_filter()

    # 3️⃣ Dropdown
    fusion.open_equipment_dropdown()

    # 4️⃣ Select all
    selected_equipment = fusion.select_all_equipment_types()

    print("\nSELECTED EQUIPMENT TYPES:")
    for s in selected_equipment:
        print("-", s)

    fusion.click_search()

    # 5️⃣ Table view
    fusion.click_on_table_view()

    # 6️⃣ Validation
    assert fusion.is_table_data_present(), "Table me data nahi aaya"

    table_equipment = fusion.get_table_equipment_types()

    print("\nTABLE EQUIPMENT TYPES:")
    for t in table_equipment:
        print("-", t)

    selected_norm = {s.lower() for s in selected_equipment}

    invalid = []

    for eq in table_equipment:
        if eq.lower() not in selected_norm:
            invalid.append(eq)

    # assert not invalid, f" Filter ke bahar ka equipment aa gaya: {invalid}"