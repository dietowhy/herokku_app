import pytest
from pages.file_upload_page import FileUploadPage


@pytest.mark.basic
def test_file_upload(browser, tmp_path):
    test_file = tmp_path / "test_upload.txt"
    test_file.write_text("Hello, Selenium!", encoding="utf-8")

    page = FileUploadPage(browser)
    page.open_page()

    page.upload_file(str(test_file))
    page.click_upload()

    assert page.uploaded_filename() == test_file.name