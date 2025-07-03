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
            iframes.forEach(iframe => {
                iframe.remove();
            });
        """)


    def click_accordion(self):
        # Accordion 1
        accordion1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.accordian1)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", accordion1)
        time.sleep(0.5)
        accordion1.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.accordian1_content)
        )

        # Accordion 2
        accordion2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.accordian2)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", accordion2)
        time.sleep(0.5)
        accordion2.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.accordian2_content)
        )

        # Accordion 3
        accordion3 = self.driver.find_element(*self.accordian3)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", accordion3)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.accordian3))

        # Remove blocking ads before clicking
        self.driver.execute_script("""
            const ads = document.querySelectorAll('[id^="google_ads_iframe"], .ad_iframe, #adplus-anchor');
            ads.forEach(ad => ad.remove());
        """)

        accordion3.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.accordian3_content)
        )

