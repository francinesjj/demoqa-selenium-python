import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LinkPage:
    def __init__(self, driver):
        self.driver = driver
        self.home_link = (By.XPATH, "//div[@id='linkWrapper']/p/a[@id='simpleLink']")
        self.dynamic_link = (By.XPATH, "//div[@id='linkWrapper']/p/a[@id='dynamicLink']")
        self.created_link = (By.XPATH, "//div[@id='linkWrapper']/p/a[@id='created']")
        self.no_content_link = (By.XPATH, "//div[@id='linkWrapper']/p/a[@id='no-content']")
        self.moved_link = (By.XPATH, "//div[@id='linkWrapper']/p/a[@id='moved']")
        self.bad_request_link = (By.XPATH, "//div[@id='linkWrapper']/p/a[@id='bad-request']")
        self.unauthorized_link = (By.XPATH, "//div[@id='linkWrapper']/p/a[@id='unauthorized']")
        self.forbidden_link = (By.XPATH, "//div[@id='linkWrapper']/p/a[@id='forbidden']")
        self.not_found_link = (By.XPATH, "//div[@id='linkWrapper']/p/a[@id='invalid-url']")
        self.link_response = (By.XPATH, "//div[@id='linkWrapper']/p[@id='linkResponse']")

    def open(self):
        self.driver.get("https://demoqa.com/links")
        self.driver.maximize_window()

        time.sleep(2)

        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => {
                iframe.remove();
            });
        """)

    def click_simple_link(self):
        original_window = self.driver.current_window_handle  # store current window
        existing_windows = self.driver.window_handles  # store existing windows

        home = self.driver.find_element(*self.home_link)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", home)
        home.click()

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > len(existing_windows)
        )
        # lambda = a quick way to define a function that takes driver and returns something

        new_window = [w for w in self.driver.window_handles if w != original_window][0]
        # finds the new browser window or tab that was just opened, and stores it in the variable new_window
        self.driver.switch_to.window(new_window)

        self.driver.close()  # closes new window
        self.driver.switch_to.window(original_window)  # goes back to the original window

    def click_dynamic_link(self):
        original_window = self.driver.current_window_handle
        existing_windows = self.driver.window_handles

        dynamic = self.driver.find_element(*self.dynamic_link)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dynamic)
        dynamic.click()

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > len(existing_windows)
        )

        new_window = [w for w in self.driver.window_handles if w != original_window][0]
        self.driver.switch_to.window(new_window)


        self.driver.close()
        self.driver.switch_to.window(original_window)

    def click_created(self):
        wait = WebDriverWait(self.driver, 10)
        created = wait.until(EC.presence_of_element_located(self.created_link))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", created)
        created.click()

    def click_no_content(self):
        wait = WebDriverWait(self.driver, 10)
        no_content = wait.until(EC.presence_of_element_located(self.no_content_link))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", no_content)
        no_content.click()

    def click_moved(self):
        wait = WebDriverWait(self.driver, 10)
        moved = wait.until(EC.presence_of_element_located(self.moved_link))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", moved)
        moved.click()

    def click_bad_request(self):
        wait = WebDriverWait(self.driver, 10)
        bad_request = wait.until(EC.presence_of_element_located(self.bad_request_link))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bad_request)
        bad_request.click()

    def click_unauthorized(self):
        wait = WebDriverWait(self.driver, 10)
        unauthorized = wait.until(EC.presence_of_element_located(self.unauthorized_link))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", unauthorized)
        unauthorized.click()

    def click_forbidden(self):
        wait = WebDriverWait(self.driver, 10)
        forbidden = wait.until(EC.presence_of_element_located(self.forbidden_link))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", forbidden)
        forbidden.click()

    def click_not_found(self):
        wait = WebDriverWait(self.driver, 10)
        not_found = wait.until(EC.presence_of_element_located(self.not_found_link))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", not_found)
        not_found.click()

    def get_link_response(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda d: d.find_element(*self.link_response).text.strip() != "")

        raw = self.driver.find_element(*self.link_response).text.strip() # grabs the sentence from the page
        parts = raw.split() # splits the sentence into words

        code = next((p for p in parts if p.isdigit() and len(p) == 3), None) # looks through each word for a 3 digit number (status code)

        text = ' '.join(parts[parts.index(code) + 3:]) if code in parts else None # goes to 3 positions after the status code and grabs the text after it
        return code, text




