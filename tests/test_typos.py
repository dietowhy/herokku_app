import pytest
from pages.typos_page import TyposPage


@pytest.mark.advanced
def test_typos_both_variants_found_with_refresh(browser):
    page = TyposPage(browser)
    page.open_page()

    variant_ok = "Sometimes you'll see a typo, other times you won't."
    variant_typo = "Sometimes you'll see a typo, other times you won,t."
    expected = {variant_ok, variant_typo}

    seen = set()
    max_attempts = 10

    for attempt in range(1, max_attempts + 1):
        text = page.get_second_paragraph()
        seen.add(text)

        if expected.issubset(seen):
            break

        if attempt < max_attempts:
            page.refresh()

    assert variant_ok in seen, (
        f"За {max_attempts} попыток не увидели вариант с апострофом. "
        f"Встретились: {seen}"
    )
    assert variant_typo in seen, (
        f"За {max_attempts} попыток не увидели вариант с опечаткой. "
        f"Встретились: {seen}"
    )