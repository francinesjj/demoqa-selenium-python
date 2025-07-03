import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SelectMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/select-menu"

        self.select_value_input = (By.XPATH, "//div[contains(@class, 'css-1wa3eu0-placeholder') and contains(text(), 'Select Option')]")
        self.select_value_option = (By.XPATH, "//div[@id='withOptGroup']//div[text()='Group 1, option 2']")

        self.select_gender_input = (By.XPATH, "//div[contains(@class, 'css-1wa3eu0-placeholder') and contains(text(), 'Select Title')]")
        self.select_gender_option = (By.XPATH, "//div[@id='selectOne']//div[text()='Ms.']")

        self.old_style_select = (By.ID, "oldSelectMenu")
        self.old_style_option = (By.XPATH, "//select[@id='oldSelectMenu']/option[text()='Purple']")

        self.multi_select_input = (
        By.XPATH, "//div[contains(@class, 'css-1wa3eu0-placeholder') and contains(text(),'Select...')]")
        self.multi_select_options = {
            "Green": (By.XPATH, "//div[@id='selectMenuContainer']//div[text()='Green']"),
            "Blue": (By.XPATH, "//div[@id='selectMenuContainer']//div[text()='Blue']"),
        }

    def open(self):
        self.driver.get(self.url)
        time.sleep(2)

        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => {
                iframe.remove();
            });
        """)

    def select_from_custom_dropdown(self):
        wait = WebDriverWait(self.driver, 10)

        dropdown_input = wait.until(EC.element_to_be_clickable(self.select_value_input))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_input)
        dropdown_input.click()

        option = wait.until(EC.visibility_of_element_located(self.select_value_option))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
        option.click()

    def select_gender(self):
        wait = WebDriverWait(self.driver, 10)

        gender_container = wait.until(EC.element_to_be_clickable(self.select_gender_input))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", gender_container)
        gender_container.click()

        option = wait.until(EC.visibility_of_element_located(self.select_gender_option))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
        option.click()

    def select_from_html_select(self):
        wait = WebDriverWait(self.driver, 10)
        select_element = wait.until(EC.element_to_be_clickable(self.old_style_select))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", select_element)

        # select class to change the selection
        select = Select(select_element)
        select.select_by_visible_text("Purple")