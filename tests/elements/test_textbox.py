from faker import Faker
from pages.elements.textbox import TextboxPage

fake = Faker()

def test_textbox(driver):
    textbox_page = TextboxPage(driver)

    textbox_page.open()
    textbox_page.enter_fullname(fake.name())
    textbox_page.enter_email(fake.email())
    textbox_page.enter_currentAddress(fake.address())
    textbox_page.enter_permanentAddress(fake.address())
    textbox_page.click_submit()

    driver.quit()