import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckboxPage:
    def __init__(self, driver):
        # LOCATORS
        self.driver = driver
        self.expand_all_button = (By.CSS_SELECTOR, ".rct-icon.rct-icon-expand-all")
        self.notes_checkbox = (By.XPATH, "//span[@class='rct-title' and text()='Notes']")
        self.result_text = (By.ID, "result")

    # ACTIONS
    def open(self):
        self.driver.get("https://demoqa.com/checkbox")
        self.driver.maximize_window()

        time.sleep(2)

        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => {
                iframe.remove();

                // hide iframes
                // iframe.style.display = 'none';
            });
        """)

    def click_expand_all(self):
        element = self.driver.find_element(*self.expand_all_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(1)

    def click_notes_checkbox(self):
        notes = self.driver.find_element(*self.notes_checkbox)
        ActionChains(self.driver).move_to_element(notes).click().perform()

    def get_result_text(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.result_text))
        return element.text
