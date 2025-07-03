from pages.widgets.tooltip import ToolTipPage

def test_tool_tips(driver):
    tooltip_page = ToolTipPage(driver)
    tooltip_page.open()

    tooltip_text = tooltip_page.hover_and_get_tooltip(tooltip_page.button)
    assert tooltip_text == "You hovered over the Button"
