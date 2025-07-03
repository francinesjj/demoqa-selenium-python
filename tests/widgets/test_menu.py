from pages.widgets.menu import MenuPage

def test_nested_menu_hover(driver):
    menu_page = MenuPage(driver)
    menu_page.open()

    is_visible = menu_page.hover_nested_menu()
    assert is_visible == True
