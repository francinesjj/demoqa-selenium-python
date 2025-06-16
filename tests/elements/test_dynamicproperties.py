from pages.elements.dynamicproperties import DynamicPropertiesPage

def test_dynamic_properties(driver):
    dynamic_page = DynamicPropertiesPage(driver)
    dynamic_page.open()

    dynamic_page.scroll_to_enable_button()
    enable_btn = dynamic_page.wait_for_enable_button()
    assert enable_btn.is_enabled(), "Enable button is not clickable after wait"

    dynamic_page.scroll_to_visible_after_button()
    visible_btn = dynamic_page.wait_for_visible_button()
    assert visible_btn.is_displayed(), "Visible After button did not appear after 5 seconds"
