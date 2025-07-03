import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DatepickerPage:
    def __init__(self, driver):
        self.driver = driver
        self.date_input = (By.CSS_SELECTOR, "#datePickerMonthYearInput")
        self.datetime_input = (By.CSS_SELECTOR, "#dateAndTimePickerInput")

    def open(self):
        self.driver.get("https://demoqa.com/date-picker")
        self.driver.maximize_window()

        time.sleep(2)

        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => iframe.remove());
        """)

    def enter_date(self, date_str):
        date_field = self.driver.find_element(*self.date_input)
        date_field.clear()
        date_field.send_keys(date_str)
        date_field.send_keys(Keys.ESCAPE)

    def enter_date_time(self, datetime_str):
        datetime_field = self.driver.find_element(*self.datetime_input)
        datetime_field.clear()
        datetime_field.send_keys(datetime_str)
        datetime_field.send_keys(Keys.ESCAPE)

