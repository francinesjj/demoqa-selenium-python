from selenium import webdriver
from pages.elements.button import ButtonPage

def test_buttons(driver):
    button_page = ButtonPage(driver)
    button_page.open()

    button_page.double_click()
    assert "You have done a double click" in button_page.double_click()

    button_page.right_click()
    assert "You have done a right click" in button_page.right_click()

    button_page.click()
    assert "You have done a dynamic click" in button_page.click()
