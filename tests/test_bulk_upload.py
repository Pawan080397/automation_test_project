import os
from pages.upload_page import UploadPage
import pytest

@pytest.mark.admin
@pytest.mark.user("admin")
def test_bulk_upload(driver):
    upload_page = UploadPage(driver)

    # test data
    file_path = os.path.abspath("C:/Users/tectum23/automation_test_project/test_data/WIS_25-31Nov2025.pdf")
    upload_page.click_ingestor_name()
    upload_page.select_file(file_path)
    upload_page.click_upload()
    assert upload_page.is_file_uploaded_successfully(), "File upload failed"
