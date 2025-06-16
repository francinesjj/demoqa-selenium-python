from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccordianPage:
    def __init__(self, driver):
        self.driver = driver
        self.accordian1 = (By.CSS_SELECTOR, "div#section1Heading")
        self.accordian1_content = (By.CSS_SELECTOR, "#section1Content")
        self.accordian2 = (By.CSS_SELECTOR, "div#section2Heading")
        self.accordian2_content = (By.CSS_SELECTOR, "#section2Content")
        self.accordian3 = (By.CSS_SELECTOR, "div#section3Heading")
        self.accordian3_content = (By.CSS_SELECTOR, "#section3Content")

    def open(self):
        self.driver.get("https://demoqa.com/accordian")
        self.driver.maximize_window()

        time.sleep(2)

        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => iframe.remove());
        """)

    def click_accordion(self):
        # accordion 1
        accordion1 = self.driver.find_element(*self.accordian1)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", accordion1)
        accordion1.click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.accordian1_content)
        )

        # accordion 2
        accordion2 = self.driver.find_element(*self.accordian2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", accordion2)
        accordion2.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.accordian2_content)
        )

        # accordion 3
        accordion3 = self.driver.find_element(*self.accordian3)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", accordion3)
        accordion3.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.accordian3_content)
        )

