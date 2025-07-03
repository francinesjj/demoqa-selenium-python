from selenium.webdriver.common.by import By
from pages.widgets.selectmenu import SelectMenuPage

def test_select_menu_options(driver):
    select_page = SelectMenuPage(driver)
    select_page.open()

    select_page.select_from_custom_dropdown()
    select_page.select_gender()
    select_page.select_from_html_select()

    selected_option = driver.find_element(By.XPATH, "//div[@id='withOptGroup']//div[contains(@class,'singleValue')]")
    assert selected_option.text == "Group 1, option 2"

    selected_gender = driver.find_element(By.XPATH, "//div[@id='selectOne']//div[contains(@class,'singleValue')]")
    assert selected_gender.text == "Ms."

    selected_value = driver.find_element(By.ID, "oldSelectMenu").get_attribute("value")
    assert selected_value == "4"  # Purple