import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutocompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.multiple_input = (By.CSS_SELECTOR, "#autoCompleteMultipleInput")
        self.suggestions = (By.CSS_SELECTOR, ".auto-complete__option")
        self.selected_tags = (By.CSS_SELECTOR, ".auto-complete__multi-value__label")

        self.single_input = (By.CSS_SELECTOR, "#autoCompleteSingleInput")
        self.single_selected = (By.CSS_SELECTOR, ".auto-complete__single-value")

    def open(self):
        self.driver.get("https://demoqa.com/auto-complete")
        self.driver.maximize_window()

        time.sleep(2)

        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => iframe.remove());
        """)

    def enter_color(self, color_partial, full_color_name):
        input_box = self.driver.find_element(*self.multiple_input)
        input_box.send_keys(color_partial)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.suggestions)
        )

        suggestions = self.driver.find_elements(*self.suggestions)

        for suggestion in suggestions:
            if suggestion.text.strip().lower() == full_color_name.lower():
                self.driver.execute_script("arguments[0].scrollIntoView(true);", suggestion)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(suggestion))
                suggestion.click()
                return

        raise Exception(f"Color '{full_color_name}' not found in suggestions.")

    def get_selected_tags(self):
        return [tag.text for tag in self.driver.find_elements(*self.selected_tags)]

    def enter_single_color(self, color_partial, full_color_name):
        input_box = self.driver.find_element(*self.single_input)
        input_box.clear()
        input_box.send_keys(color_partial)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.suggestions)
        )

        suggestions = self.driver.find_elements(*self.suggestions)

        for suggestion in suggestions:
            if suggestion.text.strip().lower() == full_color_name.lower():
                self.driver.execute_script("arguments[0].scrollIntoView(true);", suggestion)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(suggestion))
                suggestion.click()
                return

        raise Exception(f"Color '{full_color_name}' not found in single input suggestions.")

    def get_single_selected_color(self):
        return self.driver.find_element(*self.single_selected).text.strip()


