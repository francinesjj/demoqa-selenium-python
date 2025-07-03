import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProgressBarPage:
    def __init__(self, driver):
        self.driver = driver
        self.start_button = (By.ID, "startStopButton")
        self.progress_bar = (By.CSS_SELECTOR, "div.progress-bar")

    def open(self):
        self.driver.get("https://demoqa.com/progress-bar")
        self.driver.maximize_window()

        time.sleep(1)
        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => iframe.remove());
        """)

    def start_progress(self):
        start_btn = self.driver.find_element(*self.start_button)
        progress_bar = self.driver.find_element(*self.progress_bar)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", start_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", progress_bar)
        start_btn.click()

    def wait_until_complete(self, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_progress_value() == "100%"
        )

    def get_progress_value(self):
        return self.driver.find_element(*self.progress_bar).text.strip()
