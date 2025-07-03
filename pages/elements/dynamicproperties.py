import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicPropertiesPage:
    def __init__(self, driver):
        self.driver = driver
        self.enable_button = (By.ID, "enableAfter")
        self.color_change_button = (By.ID, "colorChange")
        self.visible_after_button = (By.ID, "visibleAfter")

    def open(self):
        self.driver.get("https://demoqa.com/dynamic-properties")
        self.driver.maximize_window()

        time.sleep(2)

        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => {
                iframe.remove();
            });
        """)

    def scroll_to_enable_button(self):
        element = self.driver.find_element(*self.enable_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_visible_after_button(self):
        element = self.driver.find_element(*self.visible_after_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_enable_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.enable_button)
        )
        return self.driver.find_element(*self.enable_button)

    def wait_for_visible_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.visible_after_button)
        )
