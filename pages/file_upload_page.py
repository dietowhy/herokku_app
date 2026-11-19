from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FileUploadPage(BasePage):
    FILE_INPUT = (By.ID, "file-upload")
    SUBMIT_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILES = (By.ID, "uploaded-files")

    def open_page(self):
        self.open("/upload")

    def upload_file(self, file_path: str):
        self.find(self.FILE_INPUT).send_keys(file_path)

    def click_upload(self):
        self.find(self.SUBMIT_BUTTON).click()

    def uploaded_filename(self) -> str:
        return self.find(self.UPLOADED_FILES).text.strip()