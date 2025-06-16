from selenium import webdriver
from pages.elements.checkbox import CheckboxPage  # adjust import path as needed

def test_checkbox():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    checkbox_page = CheckboxPage(driver)

    checkbox_page.open()
    checkbox_page.click_expand_all()
    checkbox_page.click_notes_checkbox()

    result = checkbox_page.get_result_text()
    assert "notes" in result.lower()

    driver.quit()
