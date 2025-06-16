from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FormPage:
    def __init__(self, driver):
        # LOCATORS
        self.driver = driver
        self.firstName_input = (By.XPATH, "//input[@id='firstName']")
        self.lastName_input = (By.XPATH, "//input[@id='lastName']")
        self.email_input = (By.XPATH, "//input[@id='userEmail']")
        self.gender_rbtn = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
        self.number_input = (By.XPATH, "//input[@id='userNumber']")
        self.birthday_input = (By.XPATH, "//input[@id='dateOfBirthInput']")
        self.subjects_input = (By.XPATH, "//label[@class='subjects-auto-complete__input']")
        self.hobbies_checkbox = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
        self.file_upload = (By.XPATH, "//input[@id='uploadPicture']")
        self.currentAddress_input = (By.XPATH, "//textarea[@id='currentAddress']")
        self.state_dropdown = (By.CSS_SELECTOR, "#state")
        self.city_dropdown = (By.CSS_SELECTOR, "#city")
        self.submit_btn = (By.XPATH, "//button[@id='submit']")


    def open(self):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.maximize_window()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 400)")

    def enter_firstName(self, firstName):
        self.driver.find_element(*self.firstName_input).send_keys(firstName)

    def enter_lastName(self, lastName):
        self.driver.find_element(*self.lastName_input).send_keys(lastName)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    # different implementation - makes sure element is in view before being clicked
    def select_gender(self):
        gender_label = self.driver.find_element(*self.gender_rbtn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", gender_label)
        gender_label.click()

    def enter_number(self, number):
        self.driver.find_element(*self.number_input).send_keys(number)

    # different implementation but same functions
    def enter_birthday(self, birthday):
        birthday_input = self.driver.find_element(*self.birthday_input)
        birthday_input.clear()
        birthday_input.send_keys(birthday)
        birthday_input.send_keys(Keys.ESCAPE)

    def enter_subject(self, subject):
        subjects_input_field = self.driver.find_element(By.ID, "subjectsInput")
        subjects_input_field.send_keys(subject)
        subjects_input_field.send_keys('\n') # selects data from autocomplete

    def select_hobby(self):
        element = self.driver.find_element(*self.hobbies_checkbox)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def upload_picture(self, file_path):
        self.driver.find_element(*self.file_upload).send_keys(file_path)

    def enter_current_address(self, address):
        self.driver.find_element(*self.currentAddress_input).send_keys(address)

    def select_state_and_city(self, state, city):
        # clicks and selects state
        self.driver.find_element(*self.state_dropdown).click()
        self.driver.find_element(By.XPATH, f"//div[text()='{state}']").click()

        # clicks and selects city
        self.driver.find_element(*self.city_dropdown).click()
        self.driver.find_element(By.XPATH, f"//div[text()='{city}']").click()

    def click_submit(self):
        self.driver.find_element(*self.submit_btn).click()

