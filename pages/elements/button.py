import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.double_btn = (By.XPATH, "//button[@id='doubleClickBtn']")
        self.double_msg = (By.ID, "doubleClickMessage")
        self.right_btn = (By.XPATH, "//button[@id='rightClickBtn']")
        self.right_msg = (By.ID, "rightClickMessage")
        self.click_btn = (By.XPATH, "//div[@class='mt-4']/button[text()='Click Me']")
        self.click_msg = (By.ID, "dynamicClickMessage")

    def open(self):
        self.driver.get("https://demoqa.com/buttons")
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

    def double_click(self):
        double = self.driver.find_element(*self.double_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", double)
        actions = ActionChains(self.driver)
        actions.double_click(double).perform()
        double_elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.double_msg)
        )
        return double_elem.text

    def right_click(self):
        right = self.driver.find_element(*self.right_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", right)
        actions = ActionChains(self.driver)
        actions.context_click(right).perform()
        right_elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.right_msg)  # ✅ correct message
        )
        return right_elem.text

    def click(self):
        click = self.driver.find_element(*self.click_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", click)
        actions = ActionChains(self.driver)
        actions.click(click).perform()
        click_elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.click_msg)
        )
        return click_elem.text