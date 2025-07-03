import pytest
from selenium import webdriver
from pages.widgets.autocomplete import AutocompletePage

def test_autocomplete_select_color(driver):
    auto_page = AutocompletePage(driver)
    auto_page.open()

    auto_page.enter_color("Re", "Red")
    selected_tags = auto_page.get_selected_tags()
    assert "Red" in selected_tags, f"'Red' not found in selected tags: {selected_tags}"


    auto_page.enter_color("Bla", "Black")
    selected_tags = auto_page.get_selected_tags()
    assert "Black" in selected_tags, f"'Red' not found in selected tags: {selected_tags}"

def test_autocomplete_single_input(driver):
    single_page = AutocompletePage(driver)
    single_page.open()

    single_page.enter_single_color("Gr", "Green")
    selected = single_page.get_single_selected_color()
    assert selected == "Green", f"Expected 'Green', but got '{selected}'"
