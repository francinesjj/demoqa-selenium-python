from selenium.webdriver.common.by import By

class TextboxPage:
    def __init__(self, driver):
        # LOCATORS
        self.driver = driver
        self.fullName_input = (By.XPATH, "//input[@id='userName']")
        self.email_input = (By.XPATH, "//input[@id='userEmail']")
        self.currentAdd_input = (By.XPATH, "//textarea[@id='currentAddress']")
        self.permanentAdd_input = (By.XPATH, "//textarea[@id='permanentAddress']")
        self.submit_btn = (By.XPATH, "//button[@id='submit']")

    # ACTIONS
    def open(self):
        self.driver.get("https://demoqa.com/text-box")
        self.driver.maximize_window()

    def enter_fullname(self, fullName):
        self.driver.find_element(*self.fullName_input).send_keys(fullName)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_currentAddress(self, currentAddress):
        self.driver.find_element(*self.currentAdd_input).send_keys(currentAddress)

    def enter_permanentAddress(self, permanentAddress):
        self.driver.find_element(*self.permanentAdd_input).send_keys(permanentAddress)

    def click_submit(self):
        button = self.driver.find_element(*self.submit_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

