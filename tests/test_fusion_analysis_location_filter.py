import pytest
from pages.fusion_analysis_page import FusionAnalysisPage
import re
import time


@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_force_disposition_equipment_filter(driver):
    fusion = FusionAnalysisPage(driver)

    fusion.click_fusion_tab()
    fusion.click_time_period_filter()
    fusion.get_time_period_options()
    fusion.SELECT_TWO_YEARS()
    fusion.click_more_filter()
    fusion.click_equipment_type_filter()
    # fusion.open_equipment_filter()

    fusion.select_equipment_by_search("art")
    time.sleep(3)
#     # print("\n FINAL SELECTED EQUIPMENT:")
#     # for eq in selected_equipment:
#     #     print(" -", eq)
#     #
#     # assert len(selected_equipment) > 0, " Equipment select nahi hua"
#
    fusion.click_on_search()
    fusion.click_on_table_view()
    time.sleep(10)
