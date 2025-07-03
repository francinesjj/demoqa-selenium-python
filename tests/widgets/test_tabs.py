from pages.widgets.tabs import TabsPage

def test_tabs_switch_and_read_content(driver):
    tabs_page = TabsPage(driver)
    tabs_page.open()

    tabs_page.click_tab("Origin")
    origin_content = tabs_page.get_tab_content("Origin")
    assert "Lorem Ipsum" in origin_content

    tabs_page.click_tab("Use")
    use_content = tabs_page.get_tab_content("Use")
    assert "Lorem Ipsum" in use_content

    # tabs_page.click_tab("More")
    # more_content = tabs_page.get_tab_content("More")
    # assert "Lorem Ipsum" in more_content
