from faker import Faker
from pages.forms.form import FormPage
import os
import time

fake = Faker()

def test_form(driver):
    form_page = FormPage(driver)
    form_page.open()

    form_page.enter_firstname(fake.first_name())
    form_page.enter_lastname(fake.last_name())
    form_page.enter_email(fake.email())
    form_page.select_gender()
    form_page.enter_number(fake.msisdn()[:10])
    form_page.enter_birthday("10 Oct 1990")
    form_page.enter_subject("Math")
    form_page.select_hobby()

    # uploads a sample file
    file_path = os.path.abspath("resources/sample.jpg")
    form_page.upload_picture(file_path)

    form_page.enter_current_address(fake.address())
    form_page.select_state_and_city("NCR", "Delhi")

    form_page.click_submit()

    driver.quit()
