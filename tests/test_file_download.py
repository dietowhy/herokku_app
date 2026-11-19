import time
from pathlib import Path

import pytest
from pages.file_download_page import FileDownloadPage


def wait_for_download(directory: Path, filename: str, timeout: int = 20) -> Path:
    target = directory / filename
    crdownload = directory / f"{filename}.crdownload"
    deadline = time.time() + timeout
    while time.time() < deadline:
        if target.exists() and not crdownload.exists():
            return target
        time.sleep(0.3)
    raise AssertionError(
        f"Файл {filename!r} не появился в {directory} за {timeout} сек."
    )


@pytest.mark.advanced
def test_file_download(browser, tmp_path):
    browser.execute_cdp_cmd(
        "Page.setDownloadBehavior",
        {"behavior": "allow", "downloadPath": str(tmp_path)},
    )

    page = FileDownloadPage(browser)
    page.open_page()
    page.click_file_by_name("some-file.txt")

    downloaded = wait_for_download(tmp_path, "some-file.txt")
    assert downloaded.exists()
    assert downloaded.stat().st_size > 0