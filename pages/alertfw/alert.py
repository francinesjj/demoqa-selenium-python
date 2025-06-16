import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertPage:
    def __init__(self, driver):
        self.driver = driver
        self.alert_btn = (By.XPATH, "//button[@id='alertButton']")
        self.time_alert_btn = (By.XPATH, "//button[@id='timerAlertButton']")
        self.confirm_btn = (By.XPATH, "//button[@id='confirmButton']")
        self.prompt_btn = (By.XPATH, "//button[@id='promtButton']")

    def open(self):
        self.driver.get("https://demoqa.com/alerts")
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

    def click_alert_btn(self):
        alert_btn =  self.driver.find_element(*self.alert_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", alert_btn)
        alert_btn.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == "You clicked a button", "Alert text did not match"

        alert.accept()

    def click_time_alert(self):
        time_alert_btn = self.driver.find_element(*self.time_alert_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", time_alert_btn)
        time_alert_btn.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        time_alert = self.driver.switch_to.alert

        assert time_alert.text == "This alert appeared after 5 seconds", "Alert text did not match"

        time_alert.accept()

    def click_confirm_alert(self):
        confirm_alert_btn = self.driver.find_element(*self.confirm_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", confirm_alert_btn)
        confirm_alert_btn.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        confirm_alert = self.driver.switch_to.alert

        assert confirm_alert.text == "Do you confirm action?", "Confirm alert text did not match"

        confirm_alert.accept()
        result_text = self.driver.find_element(By.ID, "confirmResult").text
        assert result_text == "You selected Ok", "Result text not updated correctly"

    def click_cancel_alert(self):
        cancel_alert_btn = self.driver.find_element(*self.confirm_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cancel_alert_btn)
        cancel_alert_btn.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        cancel_alert = self.driver.switch_to.alert

        assert cancel_alert.text == "Do you confirm action?", "Cancel alert text did not match"

        cancel_alert.dismiss()
        result_text = self.driver.find_element(By.ID, "confirmResult").text
        assert result_text == "You selected Cancel", "Result text not updated correctly"

    def click_prompt_alert_with_input(self, name="Franz"):
        prompt_alert_btn = self.driver.find_element(*self.prompt_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", prompt_alert_btn)
        prompt_alert_btn.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        prompt_alert = self.driver.switch_to.alert

        assert prompt_alert.text == "Please enter your name", "Prompt alert text did not match"

        prompt_alert.send_keys(name)
        prompt_alert.accept()

        result_text = self.driver.find_element(By.ID, "promptResult").text
        assert result_text == f"You entered {name}", "Prompt result text did not match input"

    def click_cancel_prompt_alert(self):
        prompt_alert_btn = self.driver.find_element(*self.prompt_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", prompt_alert_btn)
        prompt_alert_btn.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        prompt_alert = self.driver.switch_to.alert

        assert prompt_alert.text == "Please enter your name", "Prompt alert text did not match"

        prompt_alert.dismiss()

        result_text = self.driver.find_element(By.ID, "promptResult").text
        assert result_text == "", "Prompt result should be empty after cancel"




