import pytest
from pages.report_page import ReportPage

@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_report_tab_data_loaded(driver):
    report_page = ReportPage(driver)

    # Click on Report tab
    report_page.click_report_tab()

    assert report_page.is_report_data_present(), " Report table has no data"


    data = report_page.get_all_report_data()

    print("\n===== REPORT TABLE DATA =====")
    for index, row in enumerate(data, start=1):
        print(f"Row {index} => {row}")

    # Validation
    assert len(data) > 0, " Report table empty"

