from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ModalsPage:
    def __init__(self, driver):
        self.driver = driver
        self.small_modal_btn = (By.ID, "showSmallModal")
        self.small_modal_text = (By.CLASS_NAME, "modal-body")
        self.close_small_modal_btn = (By.ID, "closeSmallModal")
        self.large_modal_btn = (By.ID, "showLargeModal")
        self.large_modal_text = (By.CLASS_NAME, "modal-body")
        self.close_large_modal_btn = (By.ID, "closeLargeModal")

    def open(self):
        self.driver.get("https://demoqa.com/modal-dialogs")
        self.driver.maximize_window()

        time.sleep(2)

        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => iframe.remove());
        """)

    def open_small_modal(self):
        button = self.driver.find_element(*self.small_modal_btn) # finds element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button) # scrolls to the element
        button.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.small_modal_text) # waits until modal text is visible
        )

        modal_body = self.driver.find_element(*self.small_modal_text) # retrieves modal text
        expected_text = "This is a small modal. It has very less content"
        assert modal_body.text.strip() == expected_text, f"Modal text mismatch: {modal_body.text}" # compares extracted text to expected_text

        self.driver.find_element(*self.close_small_modal_btn).click() # closes modal

    def open_large_modal(self):
        button = self.driver.find_element(*self.large_modal_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.small_modal_text)
        )

        modal_body = self.driver.find_element(*self.small_modal_text)
        expected_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        assert modal_body.text.strip() == expected_text, f"Modal text mismatch: {modal_body.text}"

        self.driver.find_element(*self.close_large_modal_btn).click()
