import pytest

from pages.dynamic_dashboards_page import DynamicDashboardsPage
from pages.fusion_analysis_page import FusionAnalysisPage
from utils.logger import get_logger
logger = get_logger("FusionDashboardTest")

@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_dynamic_dashboards(driver):

    Dynamic_Dashboards = DynamicDashboardsPage(driver)

    Dynamic_Dashboards.click_on_Dynamic_dashboards()


@pytest.mark.analyst
@pytest.mark.user("analyst")
def test_rank_button(driver):
    Dynamic_Dashboards = DynamicDashboardsPage(driver)
    Dynamic_Dashboards.click_on_Dynamic_dashboards()
    Rank_Button = DynamicDashboardsPage(driver)
    Rank_Button.click_on_Rank()