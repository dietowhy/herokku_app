import pytest
from pages.tables_page import TablesPage


@pytest.mark.advanced
def test_table_cells_content(browser):
    page = TablesPage(browser)
    page.open_page()

    assert page.cell_text(1, 1, 1) == "Smith"
    assert page.cell_text(1, 1, 2) == "John"
    assert page.cell_text(1, 1, 3) == "jsmith@gmail.com"

    assert page.cell_text(2, 1, 1) == "Smith"
    assert page.cell_text(2, 1, 2) == "John"