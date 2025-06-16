import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class WebTablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_btn = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
        self.firstName_input = (By.CSS_SELECTOR, "input[id='firstName']")
        self.lastName_input = (By.CSS_SELECTOR, "input[id='lastName']")
        self.email_input = (By.CSS_SELECTOR, "input[id='userEmail']")
        self.age_input = (By.CSS_SELECTOR, "input[id='age']")
        self.salary_input = (By.CSS_SELECTOR, "input[id='department']")
        self.submit_btn = (By.CSS_SELECTOR, "button[id='submit']")
        self.searchbox_input = (By.CSS_SELECTOR, "input[id='searchBox']")

    def open(self):
        self.driver.get("https://demoqa.com/webtables")
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

    def click_add(self):
        add_button = self.driver.find_element(*self.add_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
        self.driver.find_element(*self.add_btn).click()

    def enter_firstName(self, firstName):
        self.driver.find_element(*self.firstName_input).send_keys(firstName)

    def enter_lastName(self, lastName):
        self.driver.find_element(*self.lastName_input).send_keys(lastName)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_age(self, age):
        self.driver.find_element(*self.age_input).send_keys(age)

    def enter_salary(self, salary):
        self.driver.find_element(*self.salary_input).send_keys(salary)

    def click_submit(self):
        submit_button = self.driver.find_element(*self.submit_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def search_by_firstName(self, firstName):
        search_box = self.driver.find_element(*self.searchbox_input)
        search_box.clear()
        search_box.send_keys(firstName)
        time.sleep(1)

    def edit_user_by_firstName(self, firstName, new_age=None, new_salary=None):
        self.search_by_firstName(firstName)

        edit_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='row']//div[text()='{firstName}']/ancestor::div[@role='row']//span[@title='Edit']"))
        )

        self.driver.execute_script("arguments[0].click();", edit_btn)

        if new_age:
            age_input = self.driver.find_element(*self.age_input)
            age_input.clear()
            age_input.send_keys(str(new_age))

        if new_salary:
            salary_input = self.driver.find_element(*self.salary_input)
            salary_input.clear()
            salary_input.send_keys(str(new_salary))

        self.click_submit()

    def delete_user_by_firstName(self, firstName):
        self.search_by_firstName(firstName)

        delete_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='row']//div[text()='{firstName}']/ancestor::div[@role='row']//span[@title='Delete']"))
        )
        delete_btn.click()

        time.sleep(1)