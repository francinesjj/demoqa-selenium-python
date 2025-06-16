from selenium import webdriver
from pages.elements.radiobutton import RadioButtonPage

def test_radio_buttons():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    radio_page = RadioButtonPage(driver)

    radio_page.open()
    radio_page.click_yes()
    assert "Yes" == radio_page.get_result_text()

    radio_page.open()
    radio_page.click_impressive()
    assert "Impressive" == radio_page.get_result_text()

    driver.quit()
