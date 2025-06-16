import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RadioButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.yes_radio = (By.CSS_SELECTOR, "label[for='yesRadio']")
        self.impressive_radio = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
        self.result_text = (By.CSS_SELECTOR, "p.mt-3 span.text-success")

    def open(self):
        self.driver.get("https://demoqa.com/radio-button")
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

    def click_yes(self):
        wait = WebDriverWait(self.driver, 10)
        yes_label = wait.until(EC.presence_of_element_located(self.yes_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", yes_label)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", yes_label)

    def click_impressive(self):
        wait = WebDriverWait(self.driver, 10)
        impressive_label = wait.until(EC.presence_of_element_located(self.impressive_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", impressive_label)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", impressive_label)

    def get_result_text(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.result_text))
        return element.text
